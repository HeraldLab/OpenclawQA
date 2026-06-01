#!/usr/bin/env python3
from __future__ import annotations

import argparse
from common import PUBLIC_REPO, UPSTREAM_REPO, ensure_run, load_json, now_iso, run_dir, write_json


def main() -> int:
    ap = argparse.ArgumentParser(description="Render public tester instructions for an OpenClawQA run")
    ap.add_argument("tag")
    ap.add_argument("--deadline", default="48 hours after dispatch")
    args = ap.parse_args()
    tag = args.tag
    ensure_run(tag)
    rd = run_dir(tag)
    run = load_json(rd / "run.json", {}) or {}
    release_context = (rd / "release-context.md").read_text(encoding="utf-8") if (rd / "release-context.md").exists() else ""
    latest_line = next((line for line in release_context.splitlines() if line.startswith("- Latest beta tag:")), "- Latest beta tag: `NOT_ENOUGH_INFO`")
    report_url = f"https://github.com/{PUBLIC_REPO}/issues/new/choose"
    run_url = f"https://github.com/{PUBLIC_REPO}/tree/main/runs/{tag}"
    upstream_url = f"https://github.com/{UPSTREAM_REPO}/releases/tag/{tag}"
    text = f"""# Tester Instructions — OpenClaw `{tag}`

Generated: `{now_iso()}`  
Run folder: {run_url}  
Upstream release: {upstream_url}  
Report results: {report_url}  
Deadline: **{args.deadline}**

## Target

Test OpenClaw beta release `{tag}`. This is a manual QA pass for release confidence, not a general support thread.

{latest_line}

## Required setup evidence

Please include these in every report:

- OS/platform and version.
- Install/upgrade method and exact command used.
- OpenClaw version/tag observed after install.
- Provider/model route used if a model call is part of the test.
- Screen recording or screenshots.
- Logs for failures.

If a fact is unavailable, write `NOT_ENOUGH_INFO`.

## P0 smoke scenarios

1. **Install or upgrade** to `{tag}` from your normal path.
2. **First response path:** start OpenClaw and get one normal response.
3. **Messaging delivery path:** if you have Discord/Telegram configured, verify a response reaches the human-visible channel.
4. **Plugin/tool visibility:** confirm configured tools/plugins are present and not silently omitted.
5. **Failure clarity:** intentionally trigger one harmless config/provider failure if safe, and verify the error is understandable.

## Report format

Use GitHub Issues in this repo:

- Use **Install smoke result** for install-only passes/failures.
- Use **Tester report** for general scenario reports.
- Use **Beta blocker** only for issues that block release validation.

One issue per bug. Do not combine unrelated failures.

## Evidence quality bar

A report is triage-ready when it has target tag, OS/platform, install method, exact steps, expected behavior, actual behavior, logs or screenshots/recording, and whether it reproduces again.

## Privacy

Do not upload secrets, API keys, private customer data, or unsanitized environment dumps. If raw evidence contains private data, summarize publicly and say the raw artifact is private.
"""
    (rd / "tester-instructions.md").write_text(text, encoding="utf-8")
    run.setdefault("links", {})["github_run_folder"] = run_url
    run["status"] = "instructions_ready"
    run["tester_instructions_generated_at"] = now_iso()
    write_json(rd / "run.json", run)
    print(rd / "tester-instructions.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
