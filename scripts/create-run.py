#!/usr/bin/env python3
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG_RE = re.compile(r"^v.+-(alpha|beta)\.\d+$")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: create-run.py <tag> [--force]", file=sys.stderr)
        return 2
    tag = sys.argv[1]
    force = "--force" in sys.argv[2:]
    if not TAG_RE.match(tag) and not force:
        print(f"refusing non alpha/beta tag without --force: {tag}", file=sys.stderr)
        return 1
    src = ROOT / "templates" / "run-folder"
    dest = ROOT / "runs" / tag
    dest.mkdir(parents=True, exist_ok=True)
    for p in src.iterdir():
        target = dest / p.name
        if not target.exists():
            shutil.copy2(p, target)
    run_path = dest / "run.json"
    data = json.loads(run_path.read_text())
    data["tag"] = tag
    data["created_at"] = data.get("created_at") or datetime.now(timezone.utc).isoformat()
    data["links"]["github_run_folder"] = f"https://github.com/HeraldLabs/openclawQA/tree/main/runs/{tag}"
    run_path.write_text(json.dumps(data, indent=2) + "\n")
    print(dest)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
