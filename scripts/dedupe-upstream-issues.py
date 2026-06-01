#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from common import UPSTREAM_REPO, append_receipt, gh_search_issues, load_json, now_iso, run_dir


def terms_from_title(title: str) -> list[str]:
    words = re.findall(r"[A-Za-z0-9_-]{4,}", title)
    stop = {"tester", "report", "beta", "blocker", "openclaw", "install", "smoke"}
    return [w for w in words if w.lower() not in stop][:5]


def main() -> int:
    ap = argparse.ArgumentParser(description="Dedupe tester reports against upstream OpenClaw issues")
    ap.add_argument("tag")
    args = ap.parse_args()
    tag = args.tag
    rd = run_dir(tag)
    status = load_json(rd / "tester-status.json", {}) or {}
    results = []
    for report in status.get("reports", []):
        title = report.get("title") or ""
        terms = terms_from_title(title)
        query = f"repo:{UPSTREAM_REPO} is:issue {' '.join(terms) if terms else tag}"
        items = gh_search_issues(query)
        candidates = [{"number": i.get("number"), "title": i.get("title"), "state": i.get("state"), "url": i.get("html_url")} for i in items[:5]]
        results.append({"report": report, "query": query, "candidate_count": len(candidates), "candidates": candidates})
    receipt = {"tag": tag, "deduped_at": now_iso(), "upstream_repo": UPSTREAM_REPO, "results": results}
    append_receipt(tag, "issue-dedupe.json", receipt)
    lines = [f"# Triage Notes — `{tag}`\n\n", f"Deduped: `{receipt['deduped_at']}`\n\n"]
    if not results:
        lines.append("No tester reports found for dedupe.\n")
    for result in results:
        r = result["report"]
        lines.append(f"## Tester report #{r['number']}: {r['title']}\n\nSearch: `{result['query']}`\n\n")
        if result["candidates"]:
            for c in result["candidates"]:
                lines.append(f"- Candidate upstream #{c['number']} ({c['state']}): [{c['title']}]({c['url']})\n")
        else:
            lines.append("- No candidate duplicate found.\n")
        lines.append("\n")
    (rd / "triage-notes.md").write_text("".join(lines), encoding="utf-8")
    print(f"deduped_reports={len(results)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
