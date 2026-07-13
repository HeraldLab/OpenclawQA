#!/usr/bin/env python3
from __future__ import annotations

import argparse
from common import PUBLIC_REPO, UPSTREAM_REPO, ensure_run, load_json, now_iso, run_dir, write_json


def main() -> int:
    ap = argparse.ArgumentParser(description="Render public tester instructions for an OpenClawQA run")
    ap.add_argument("tag")
    ap.add_argument("--deadline", default="6 hours after packet receipt")
    args = ap.parse_args()
    tag = args.tag
    ensure_run(tag)
    rd = run_dir(tag)
    run = load_json(rd / "run.json", {}) or {}
    release_context = (rd / "release-context.md").read_text(encoding="utf-8") if (rd / "release-context.md").exists() else ""
    latest_line = next((line for line in release_context.splitlines() if line.startswith("- Latest beta tag:")), "- Latest beta tag: `NOT_ENOUGH_INFO`")
    community_lines: list[str] = []
    in_community_section = False
    for line in release_context.splitlines():
        if line == "## Community beta-ping context":
            in_community_section = True
            continue
        if in_community_section and line.startswith("## "):
            break
        if in_community_section and line.strip():
            community_lines.append(line)
    community_context = "\n".join(community_lines) if community_lines else "- Status: `NOT_CHECKED` — inspect `#clawtributors` before dispatch."
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

## How your assigned card is generated

You should receive a short human QA card, not this whole operating model. The coordinator generates the card from:

1. **Universal baseline:** install/update, version proof, first response, one visible channel, plugin/tool sanity, safe failure, secrets check.
2. **Your real setup:** OS, channel, provider/model route, available plugin, restart path.
3. **Community beta instructions:** the latest `#clawtributors` `@Beta Pings` post for the exact tag or release family.
4. **Release risk:** one or two delta scenarios from the release notes, commits, PRs, and current upstream issues.

### Mandatory community-ping gate

Before dispatch, the coordinator must check `#clawtributors` for the exact tag, the release family, and newer `@Beta Pings` corrections posted since the prior beta. Record source message ID, author, timestamp, and extracted asks in `release-context.md`.

If no exact-tag ping exists, say so explicitly and use the newest verified family-level ask unless a newer message overrides it. **Do not dispatch while status is `NOT_CHECKED`.**

Current captured context:

{community_context}

Default card shape is 6–8 checks:

1. Install/upgrade to `{tag}`.
2. Prove version/tag/commit.
3. Get one normal response.
4. Verify your assigned human-visible channel.
5. Check plugin/tool visibility or install/use one safe plugin.
6. Trigger one harmless failure and judge whether recovery is clear.
7. Run one Core P1 check: restart/persistence, provider route, or config/session continuity.
8. Run one release-specific delta check if assigned.

If you already proved a row in a previous issue, do not rerun it unless asked. Submit only the addendum.

## Baseline P0 smoke scenarios

1. **Install or upgrade** to `{tag}` from your normal path.
2. **Version proof:** show OpenClaw version/tag/commit after install.
3. **First response path:** start OpenClaw and get one normal response.
4. **Messaging delivery path:** if you have Discord/Telegram configured, verify a response reaches the human-visible channel.
5. **Plugin/tool visibility:** confirm configured tools/plugins are present and not silently omitted.
6. **Failure clarity:** intentionally trigger one harmless config/provider failure if safe, and verify the error is understandable.
7. **Secrets/false-success check:** confirm evidence has no secrets and success claims match visible results.

## Core P1 add-ons

Run assigned add-ons only:

- Restart/gateway persistence.
- Install and use one safe plugin.
- Provider/model route visibility.
- Config/session continuity after restart/update.
- Secondary messaging channel if configured.

## Release-delta add-ons

The coordinator may assign one release-specific scenario derived from changed code or current upstream issue signals. Treat it as manual human QA: record the real flow, expected vs actual, confusion/trust notes, and evidence.

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
