#!/usr/bin/env python3
from __future__ import annotations

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


def iso_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fetch-openclaw-release-context.py <tag>", file=sys.stderr)
        return 2
    tag = sys.argv[1]
    run = ROOT / "runs" / tag
    run.mkdir(parents=True, exist_ok=True)
    (run / "receipts").mkdir(exist_ok=True)

    releases = fetch("/releases?per_page=100")
    tags = fetch("/tags?per_page=100")
    issues = fetch("/issues?state=open&per_page=30&sort=updated&direction=desc")
    prs = fetch("/pulls?state=open&per_page=30&sort=updated&direction=desc")
    fetched_at = iso_now()
    target_release = next((r for r in releases if r.get("tag_name") == tag), None)
    target_tag = next((t for t in tags if t.get("name") == tag), None)
    target_exists = bool(target_release or target_tag)
    latest_beta = next((t["name"] for t in tags if "-beta." in t.get("name", "")), None)
    latest_alpha = next((t["name"] for t in tags if "-alpha." in t.get("name", "")), None)
    stable = next((r["tag_name"] for r in releases if not r.get("prerelease")), None)
    prereleases = [r["tag_name"] for r in releases if r.get("prerelease")]
    prior_pre = next((x for x in prereleases if x != tag), None)

    receipt = {
        "fetched_at": fetched_at,
        "target_tag": tag,
        "target_exists": target_exists,
        "target_release_url": (target_release or {}).get("html_url"),
        "target_tag_sha": (target_tag or {}).get("commit", {}).get("sha"),
        "latest_beta": latest_beta,
        "latest_alpha": latest_alpha,
        "stable_baseline": stable,
        "prior_prerelease_baseline": prior_pre,
        "release_count_checked": len(releases),
        "tag_count_checked": len(tags),
        "issue_count_checked": len([i for i in issues if "pull_request" not in i]),
        "pr_count_checked": len(prs),
        "recent_releases": [{"tag_name": r.get("tag_name"), "name": r.get("name"), "prerelease": r.get("prerelease"), "published_at": r.get("published_at"), "url": r.get("html_url")} for r in releases[:20]],
        "recent_tags": [{"name": t.get("name"), "sha": (t.get("commit") or {}).get("sha")} for t in tags[:30]],
        "recent_issues": [{"number": i.get("number"), "title": i.get("title"), "url": i.get("html_url"), "labels": [l.get("name") for l in i.get("labels", [])]} for i in issues if "pull_request" not in i][:30],
        "recent_prs": [{"number": p.get("number"), "title": p.get("title"), "url": p.get("html_url"), "draft": p.get("draft")} for p in prs[:30]],
    }
    (run / "receipts" / "github-fetch.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    issue_lines = []
    for i in issues:
        if "pull_request" in i:
            continue
        labels = ", ".join(l.get("name", "") for l in i.get("labels", [])) or "no-labels"
        issue_lines.append(f"- #{i['number']} [{labels}] {i['title']} — {i['html_url']}\n")
    pr_lines = [f"- PR #{p['number']} draft={p.get('draft')} {p['title']} — {p['html_url']}\n" for p in prs]

    freshness = [
        "# Freshness Report\n\n",
        f"Target tag: `{tag}`\n\n",
        f"Target exists upstream: **{'yes' if target_exists else 'no'}**\n\n",
        f"Fetched at: `{fetched_at}`\n\n",
        f"Latest beta tag: `{latest_beta or 'NOT_ENOUGH_INFO'}`\n\n",
        f"Latest alpha tag: `{latest_alpha or 'NOT_ENOUGH_INFO'}`\n\n",
        f"Stable baseline: `{stable or 'NOT_ENOUGH_INFO'}`\n\n",
        f"Prior prerelease baseline: `{prior_pre or 'NOT_ENOUGH_INFO'}`\n\n",
        "## Recent issue signals\n\n",
        *(issue_lines or ["- No recent open issue signals returned.\n"]),
        "\n## Recent PR signals\n\n",
        *(pr_lines or ["- No recent open PR signals returned.\n"]),
    ]
    (run / "freshness-report.md").write_text("".join(freshness), encoding="utf-8")

    context = [
        f"# Release Context — OpenClaw `{tag}`\n\n",
        f"Fetched at: `{fetched_at}`\n\n",
        "## Target\n\n",
        f"- Target tag: `{tag}`\n",
        f"- Target exists upstream: **{'yes' if target_exists else 'no'}**\n",
        f"- Target release URL: {(target_release or {}).get('html_url') or 'NOT_ENOUGH_INFO'}\n",
        f"- Target tag SHA: {(target_tag or {}).get('commit', {}).get('sha') or 'NOT_ENOUGH_INFO'}\n",
        "\n## Freshness baselines\n\n",
        f"- Latest beta tag: `{latest_beta or 'NOT_ENOUGH_INFO'}`\n",
        f"- Latest alpha tag: `{latest_alpha or 'NOT_ENOUGH_INFO'}`\n",
        f"- Stable baseline: `{stable or 'NOT_ENOUGH_INFO'}`\n",
        f"- Prior prerelease baseline: `{prior_pre or 'NOT_ENOUGH_INFO'}`\n",
        "\n## Release notes excerpt\n\n",
        (target_release or {}).get("body") or "NOT_ENOUGH_INFO",
        "\n\n## Recent issue risk signals\n\n",
        *(issue_lines or ["- No recent open issue signals returned.\n"]),
        "\n## Recent PR risk signals\n\n",
        "PRs are risk signals, not proof of shipped code in this tag.\n\n",
        *(pr_lines or ["- No recent open PR signals returned.\n"]),
    ]
    (run / "release-context.md").write_text("".join(context), encoding="utf-8")

    run_path = run / "run.json"
    if run_path.exists():
        data = json.loads(run_path.read_text(encoding="utf-8"))
        data.setdefault("freshness", {})["trigger_checked_at"] = fetched_at
        data["freshness"].update({"primary_target": tag, "stable_baseline": stable, "prior_prerelease_baseline": prior_pre, "latest_alpha": latest_alpha, "latest_beta": latest_beta, "target_exists": target_exists})
        receipts = data.setdefault("receipts", [])
        if "receipts/github-fetch.json" not in receipts:
            receipts.append("receipts/github-fetch.json")
        run_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    if not target_exists:
        print(f"warning: target tag {tag} was not found upstream", file=sys.stderr)
    print(run / "freshness-report.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
