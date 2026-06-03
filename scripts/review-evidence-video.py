#!/usr/bin/env python3
"""Review OpenClaw QA video evidence and produce a GitHub-ready evidence review.

This script is intentionally safe-by-default:
- It never posts to GitHub by itself.
- It records metadata/checksum for local videos.
- It uses Gemini video review only when google-genai + an API key are available.
- If model review is unavailable, it still writes a manual-review scaffold.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_VERDICTS = [
    "EVIDENCE_CONFIRMED",
    "EVIDENCE_CONFIRMED_WITH_CAVEAT",
    "NEEDS_MORE_EVIDENCE",
    "BLOCKED_BY_EVIDENCE_ERROR",
    "FAIL_FILE_UPSTREAM",
    "SECRET_EXPOSURE_REDACT",
]


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def ffprobe(path: Path) -> dict:
    if not shutil.which("ffprobe"):
        return {"available": False, "error": "ffprobe not found"}
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration,size,format_name:stream=index,codec_type,codec_name,width,height,avg_frame_rate",
        "-of",
        "json",
        str(path),
    ]
    try:
        out = subprocess.check_output(cmd, text=True, timeout=30)
        data = json.loads(out)
        data["available"] = True
        return data
    except Exception as exc:  # pragma: no cover - diagnostic path
        return {"available": True, "error": str(exc)}


def env_api_key() -> str | None:
    for key in ["GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENERATIVE_AI_API_KEY"]:
        if os.environ.get(key):
            return os.environ[key]
    secret = Path.home() / ".hermes" / "secrets" / "gemini-api-key"
    if secret.exists():
        val = secret.read_text().strip()
        if val:
            return val
    env = Path.home() / ".hermes" / ".env"
    if env.exists():
        for line in env.read_text(errors="ignore").splitlines():
            if not line.strip() or line.lstrip().startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            if k.strip() in {"GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENERATIVE_AI_API_KEY"}:
                return v.strip().strip('"').strip("'")
    return None


def review_prompt(args: argparse.Namespace, metadata: dict) -> str:
    return f"""You are reviewing an OpenClaw P0 release QA screen recording. Watch/analyze the whole video from start to finish.

Release tag: {args.tag}
Tester: {args.tester}
Reported verdict: {args.reported_verdict or 'unknown'}
QA issue/report: {args.issue or 'not provided'}
Video metadata: {json.dumps(metadata, indent=2)[:4000]}

Expected checklist:
1. install/upgrade to assigned tag
2. OpenClaw version/commit proof
3. one normal OpenClaw response
4. configured visible channel delivery
5. plugin/tool visibility sanity check
6. one harmless failure with understandable error
7. release-specific scenario if assigned: {args.release_specific or 'Not assigned'}

Return JSON with:
- duration_reviewed
- whole_video_analyzed: true/false
- checklist: each row as CONFIRMED/MISSING/CONTRADICTED/NOT_APPLICABLE with timestamp and evidence note
- visible_errors: timestamped warnings/errors/red text/tracebacks/timeouts/crashes/misleading output
- possible_secret_exposure: timestamped evidence or PASS
- mismatch_with_written_report
- recommended_verdict, one of {ALLOWED_VERDICTS}
- concise reviewer comment suitable for GitHub

Do not assume success. If a checklist row is not visible, mark MISSING. If an error appears but the report claims pass, call it out.
"""


def gemini_review(video: Path, prompt: str, model: str) -> tuple[str | None, str | None]:
    api_key = env_api_key()
    if not api_key:
        return None, "No Gemini API key found"
    try:
        from google import genai  # type: ignore
    except Exception as exc:
        return None, f"google-genai unavailable: {exc}"

    try:
        client = genai.Client(api_key=api_key)
        uploaded = client.files.upload(file=str(video))
        # File processing can be async for larger videos.
        for _ in range(60):
            refreshed = client.files.get(name=uploaded.name)
            state = getattr(refreshed, "state", None)
            state_name = getattr(state, "name", str(state))
            if state_name in {"ACTIVE", "FileState.ACTIVE"}:
                uploaded = refreshed
                break
            if state_name in {"FAILED", "FileState.FAILED"}:
                return None, f"Gemini file processing failed: {state_name}"
            time.sleep(2)
        resp = client.models.generate_content(model=model, contents=[uploaded, prompt])
        return getattr(resp, "text", None) or str(resp), None
    except Exception as exc:  # pragma: no cover - depends on external service
        return None, f"Gemini review failed: {exc}"


def manual_scaffold(args: argparse.Namespace, source: str, metadata: dict, model_error: str | None) -> str:
    return f"""## Evidence review
Verdict: NEEDS_MORE_EVIDENCE

Reviewed evidence:
- Video: {source}
- Duration reviewed: MANUAL_REVIEW_REQUIRED
- Reviewer: <agent/person>
- Generated at: {utc_now()}

Automation status:
- Metadata: `{json.dumps(metadata)[:1000]}`
- Model review: {model_error or 'not run'}

Checklist confirmation:
- Install/upgrade: MISSING — <timestamp/evidence>
- Version proof: MISSING — <timestamp/evidence>
- First response: MISSING — <timestamp/evidence>
- Channel delivery: MISSING — <timestamp/evidence>
- Plugins/tools: MISSING — <timestamp/evidence>
- Harmless failure: MISSING — <timestamp/evidence>
- Release-specific scenario: {'NOT_APPLICABLE' if not args.release_specific else 'MISSING'} — {args.release_specific or 'Not assigned'}

Observed warnings/errors:
- <timestamp> — <warning/error or None observed after full manual review>

Secrets check:
- <PASS/FAIL> — <notes>

Next action:
- Complete full-duration video review, replace MISSING rows with timestamped statuses, then update verdict.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Review OpenClaw QA video evidence")
    parser.add_argument("--video", required=True, help="Local video file path. URLs are recorded but require manual/native-model review outside this script unless downloaded.")
    parser.add_argument("--tag", required=True)
    parser.add_argument("--tester", required=True)
    parser.add_argument("--issue", default="")
    parser.add_argument("--reported-verdict", default="")
    parser.add_argument("--release-specific", default="")
    parser.add_argument("--model", default="gemini-2.0-flash")
    parser.add_argument("--out", default="", help="Markdown output path")
    parser.add_argument("--json-out", default="", help="JSON metadata output path")
    args = parser.parse_args()

    source = args.video
    path = Path(args.video).expanduser()
    metadata: dict = {"source": source, "generated_at": utc_now()}
    model_text = None
    model_error = None

    if path.exists() and path.is_file():
        metadata.update({
            "local_file": str(path.resolve()),
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
            "ffprobe": ffprobe(path),
        })
        model_text, model_error = gemini_review(path, review_prompt(args, metadata), args.model)
    else:
        metadata["note"] = "Video is not a local file. Download it first or run a native video URL review, then paste results into the review comment."
        model_error = "non-local video input"

    if model_text:
        body = f"""## Evidence review model output

Generated at: {utc_now()}
Source: {source}
Tester: {args.tester}
Tag: {args.tag}
Issue/report: {args.issue or 'not provided'}

```json
{model_text.strip()}
```

Reviewer must verify the model output, then post the final GitHub evidence-review comment using `docs/evidence-review-workflow.md`.
"""
    else:
        body = manual_scaffold(args, source, metadata, model_error)

    out = Path(args.out) if args.out else Path(f"evidence-review-{args.tag}-{args.tester}.md")
    out.write_text(body)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(metadata, indent=2) + "\n")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
