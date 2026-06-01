#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from common import ROOT, PUBLIC_REPO, latest_beta_release, now_iso, write_json

STATE = ROOT / ".openclawqa-state" / "seen-beta.json"


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {}


def save_state(state: dict) -> None:
    write_json(STATE, state)


def run_workflow(tag: str, *, no_push: bool = False) -> None:
    cmds = [
        [sys.executable, "scripts/create-run.py", tag],
        [sys.executable, "scripts/fetch-openclaw-release-context.py", tag],
        [sys.executable, "scripts/render-tester-instructions.py", tag],
        [sys.executable, "scripts/collect-reports.py", tag],
        [sys.executable, "scripts/dedupe-upstream-issues.py", tag],
        [sys.executable, "scripts/file-upstream-issues.py", tag, "--dry-run"],
        [sys.executable, "scripts/render-closeout-report.py", tag],
        [sys.executable, "scripts/render-index.py"],
        [sys.executable, "scripts/validate-run.py", tag],
    ]
    for cmd in cmds:
        subprocess.check_call(cmd, cwd=ROOT)
    subprocess.check_call(["git", "add", "README.md", "runs", "scripts", "templates", "docs", ".github"], cwd=ROOT)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode != 0:
        subprocess.check_call(["git", "commit", "-m", f"chore: run QA workflow for {tag}"], cwd=ROOT)
        if not no_push:
            subprocess.check_call(["git", "push"], cwd=ROOT)


def main() -> int:
    ap = argparse.ArgumentParser(description="Poll upstream OpenClaw beta releases and trigger OpenclawQA workflow")
    ap.add_argument("--force", action="store_true", help="Run even if beta was already seen")
    ap.add_argument("--init", action="store_true", help="Initialize state to latest beta without running")
    ap.add_argument("--no-push", action="store_true", help="Commit locally but do not push")
    args = ap.parse_args()
    latest = latest_beta_release()
    if not latest:
        print("No beta release found")
        return 0
    tag = latest["tag_name"]
    state = load_state()
    if args.init and not state.get("last_beta"):
        save_state({"last_beta": tag, "initialized_at": now_iso(), "url": latest.get("html_url")})
        print(f"initialized latest beta {tag}")
        return 0
    if not args.force and state.get("last_beta") == tag:
        return 0
    run_workflow(tag, no_push=args.no_push)
    save_state({"last_beta": tag, "last_run_at": now_iso(), "url": latest.get("html_url"), "public_run": f"https://github.com/{PUBLIC_REPO}/tree/main/runs/{tag}"})
    print(f"OpenclawQA workflow triggered for new beta {tag}: https://github.com/{PUBLIC_REPO}/tree/main/runs/{tag}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
