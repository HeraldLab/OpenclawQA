#!/usr/bin/env python3
from __future__ import annotations

import argparse
from common import PUBLIC_REPO, append_receipt, gh_api, now_iso, run_dir, write_json

STATUS_LABELS = {"status:needs-triage", "status:needs-info", "status:validated", "status:upstream-filed", "status:duplicate", "status:not-reproducible"}


def main() -> int:
    ap = argparse.ArgumentParser(description="Collect OpenClawQA tester reports from GitHub issues")
    ap.add_argument("tag")
    ap.add_argument("--state", default="all", choices=["open", "closed", "all"])
    args = ap.parse_args()
    tag = args.tag
    rd = run_dir(tag)
    issues = gh_api(f"/repos/{PUBLIC_REPO}/issues?state={args.state}&per_page=100")
    reports = []
    for issue in issues:
        if "pull_request" in issue:
            continue
        body = issue.get("body") or ""
        title = issue.get("title") or ""
        if tag not in title and tag.lower() not in body.lower():
            continue
        labels = [l.get("name") for l in issue.get("labels", [])]
        status = next((l for l in labels if l in STATUS_LABELS), "status:needs-triage")
        has_evidence = any(t in body.lower() for t in ["http://", "https://", "screenshot", "screen recording", "log", "```"])
        reports.append({"number": issue["number"], "title": title, "url": issue["html_url"], "state": issue["state"], "labels": labels, "status": status, "author": issue.get("user", {}).get("login"), "created_at": issue.get("created_at"), "updated_at": issue.get("updated_at"), "has_evidence": has_evidence, "body_chars": len(body)})
    summary = {"tag": tag, "collected_at": now_iso(), "repo": PUBLIC_REPO, "reports": reports}
    write_json(rd / "tester-status.json", summary)
    lines = [f"# Tester Status — `{tag}`\n\n", f"Collected: `{summary['collected_at']}`\n\n", f"Reports found: **{len(reports)}**\n\n", "| Issue | Status | Evidence | Title |\n|---|---|---:|---|\n"]
    for r in reports:
        lines.append(f"| [#{r['number']}]({r['url']}) | `{r['status']}` | {'yes' if r['has_evidence'] else 'no'} | {r['title']} |\n")
    (rd / "tester-status.md").write_text("".join(lines), encoding="utf-8")
    ev = [f"# Evidence Manifest — `{tag}`\n\n"]
    for r in reports:
        ev.append(f"- [#{r['number']}]({r['url']}) — evidence={'yes' if r['has_evidence'] else 'no'} — `{r['status']}`\n")
    (rd / "evidence-manifest.md").write_text("".join(ev), encoding="utf-8")
    append_receipt(tag, "collect-reports.json", summary)
    print(f"reports={len(reports)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
