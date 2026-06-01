#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "run.json", "release-context.md", "freshness-report.md", "qa-checklist.md",
    "adversarial-review.md", "tester-instructions.md", "tester-status.json",
    "tester-status.md", "evidence-manifest.md", "triage-notes.md",
    "upstream-issues-filed.md", "closeout-report.md",
]

def validate(run: Path):
    missing = [name for name in REQUIRED if not (run / name).exists()]
    if missing:
        raise SystemExit(f"{run}: missing {missing}")
    json.loads((run / "run.json").read_text())
    json.loads((run / "tester-status.json").read_text())

if len(sys.argv) > 1:
    validate(ROOT / "runs" / sys.argv[1])
else:
    for run in (ROOT / "runs").iterdir():
        if run.is_dir():
            validate(run)
print("ok")
