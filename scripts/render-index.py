#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = []
for run_json in sorted((ROOT / "runs").glob("*/run.json")):
    data = json.loads(run_json.read_text())
    tag = data.get("tag", run_json.parent.name)
    status = data.get("status", "unknown")
    folder = f"runs/{tag}"
    rows.append(f"| `{tag}` | {status} | [folder]({folder}/) | [instructions]({folder}/tester-instructions.md) | [closeout]({folder}/closeout-report.md) |")
readme = ROOT / "README.md"
text = readme.read_text()
start = "| Tag | Status | Instructions | Closeout |"
if rows:
    table = "| Tag | Status | Folder | Instructions | Closeout |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n"
    before = text.split("## Current Runs", 1)[0]
    after = text.split("## Tester Flow", 1)[1]
    readme.write_text(before + "## Current Runs\n\n" + table + "\n## Tester Flow" + after)
print(readme)
