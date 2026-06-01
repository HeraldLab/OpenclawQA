#!/usr/bin/env python3
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.github.com/repos/openclaw/openclaw"
HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "herald-openclawqa"}


def fetch(path):
    req = urllib.request.Request(API + path, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fetch-openclaw-release-context.py <tag>", file=sys.stderr)
        return 2
    tag = sys.argv[1]
    run = ROOT / "runs" / tag
    run.mkdir(parents=True, exist_ok=True)
    (run / "receipts").mkdir(exist_ok=True)
    releases = fetch("/releases?per_page=20")
    tags = fetch("/tags?per_page=30")
    issues = fetch("/issues?state=open&per_page=20&sort=updated&direction=desc")
    prs = fetch("/pulls?state=open&per_page=20&sort=updated&direction=desc")
    receipt = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "target_tag": tag,
        "releases": releases,
        "tags": tags,
        "issues": issues,
        "prs": prs,
    }
    (run / "receipts" / "github-fetch.json").write_text(json.dumps(receipt, indent=2) + "\n")
    latest_beta = next((t["name"] for t in tags if "-beta." in t.get("name", "")), None)
    latest_alpha = next((t["name"] for t in tags if "-alpha." in t.get("name", "")), None)
    stable = next((r["tag_name"] for r in releases if not r.get("prerelease")), None)
    prereleases = [r["tag_name"] for r in releases if r.get("prerelease")]
    prior_pre = next((x for x in prereleases if x != tag), None)
    md = [
        "# Freshness Report\n\n",
        f"Target tag: `{tag}`\n\n",
        f"Fetched at: `{receipt['fetched_at']}`\n\n",
        f"Latest beta tag: `{latest_beta or 'NOT_ENOUGH_INFO'}`\n\n",
        f"Latest alpha tag: `{latest_alpha or 'NOT_ENOUGH_INFO'}`\n\n",
        f"Stable baseline: `{stable or 'NOT_ENOUGH_INFO'}`\n\n",
        f"Prior prerelease baseline: `{prior_pre or 'NOT_ENOUGH_INFO'}`\n\n",
        "## Recent issue signals\n\n",
    ]
    for i in issues:
        if "pull_request" in i:
            continue
        md.append(f"- #{i['number']} {i['title']} — {i['html_url']}\n")
    md.append("\n## Recent PR signals\n\n")
    for p in prs:
        md.append(f"- PR #{p['number']} {p['title']} draft={p.get('draft')} — {p['html_url']}\n")
    (run / "freshness-report.md").write_text("".join(md))
    print(run / "freshness-report.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
