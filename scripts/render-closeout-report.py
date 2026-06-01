#!/usr/bin/env python3
from __future__ import annotations

import argparse
from common import PUBLIC_REPO, UPSTREAM_REPO, load_json, now_iso, run_dir, write_json


def main() -> int:
    ap = argparse.ArgumentParser(description="Render OpenClawQA run closeout report")
    ap.add_argument("tag")
    args = ap.parse_args()
    tag = args.tag
    rd = run_dir(tag)
    status = load_json(rd / "tester-status.json", {}) or {}
    dedupe = load_json(rd / "receipts" / "issue-dedupe.json", {}) or {}
    filing = load_json(rd / "receipts" / "issue-file-results.json", {}) or {}
    run = load_json(rd / "run.json", {}) or {}
    reports = status.get("reports", [])
    filed = filing.get("filed_items", [])
    dry = filing.get("dry_run_items", [])
    lines = [
        f"# Closeout Report — OpenClaw `{tag}`\n\n",
        f"Generated: `{now_iso()}`\n\n",
        f"Public run folder: https://github.com/{PUBLIC_REPO}/tree/main/runs/{tag}\n\n",
        f"Upstream release: https://github.com/{UPSTREAM_REPO}/releases/tag/{tag}\n\n",
        "## Summary\n\n",
        f"- Tester reports collected: **{len(reports)}**\n",
        f"- Dedupe checks run: **{len(dedupe.get('results', []))}**\n",
        f"- Upstream issues filed live: **{len(filed)}**\n",
        f"- Upstream dry-run candidates: **{len(dry)}**\n",
        "- Upstream live filing mode: **disabled unless explicitly run with `--live`**\n",
        "\n## Reports\n\n",
    ]
    if not reports:
        lines.append("No tester reports found yet.\n")
    for r in reports:
        lines.append(f"- [#{r['number']}]({r['url']}) — `{r['status']}` — evidence={'yes' if r.get('has_evidence') else 'no'} — {r['title']}\n")
    lines.append("\n## Upstream filing\n\n")
    if filed:
        for item in filed:
            lines.append(f"- Filed: [{item['title']}]({item.get('created_url')})\n")
    else:
        lines.append("No live upstream OpenClaw issues were created by this run.\n")
    lines.append("\n## Receipts\n\n")
    for receipt in run.get("receipts", []):
        lines.append(f"- `{receipt}`\n")
    (rd / "closeout-report.md").write_text("".join(lines), encoding="utf-8")
    run["status"] = "closed_initial_dry_run"
    run["closeout_generated_at"] = now_iso()
    write_json(rd / "run.json", run)
    print(rd / "closeout-report.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
