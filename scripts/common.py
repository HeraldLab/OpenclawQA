#!/usr/bin/env python3
"""Shared helpers for OpenClawQA automation."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_REPO = os.environ.get("OPENCLAWQA_REPO", "HeraldLab/OpenclawQA")
UPSTREAM_REPO = os.environ.get("OPENCLAW_UPSTREAM_REPO", "openclaw/openclaw")
BETA_RE = re.compile(r"-beta\.\d+$", re.I)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_dir(tag: str) -> Path:
    return ROOT / "runs" / tag


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def gh_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        return token
    try:
        return subprocess.check_output(["gh", "auth", "token"], text=True, timeout=15).strip()
    except Exception:
        return ""


def gh_api(path: str, *, method: str = "GET", data: Any = None, token_required: bool = False) -> Any:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "HeraldLab-OpenclawQA"}
    token = gh_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    elif token_required:
        raise RuntimeError("GITHUB_TOKEN or gh auth token required")
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request("https://api.github.com" + path, headers=headers, method=method, data=body)
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read().decode()
    return json.loads(raw) if raw else None


def gh_search_issues(query: str) -> list[dict[str, Any]]:
    data = gh_api(f"/search/issues?q={urllib.parse.quote(query)}&per_page=20")
    return data.get("items", []) if isinstance(data, dict) else []


def latest_beta_release() -> dict[str, Any] | None:
    releases = gh_api(f"/repos/{UPSTREAM_REPO}/releases?per_page=100")
    for rel in releases:
        if BETA_RE.search(rel.get("tag_name") or ""):
            return rel
    tags = gh_api(f"/repos/{UPSTREAM_REPO}/tags?per_page=100")
    for tag in tags:
        name = tag.get("name") or ""
        if BETA_RE.search(name):
            return {"tag_name": name, "name": name, "html_url": f"https://github.com/{UPSTREAM_REPO}/releases/tag/{name}", "published_at": None, "body": "", "source": "tag"}
    return None


def ensure_run(tag: str) -> Path:
    dest = run_dir(tag)
    if not dest.exists():
        subprocess.check_call([sys.executable, str(ROOT / "scripts" / "create-run.py"), tag], cwd=ROOT)
    return dest


def append_receipt(tag: str, name: str, data: Any) -> Path:
    p = run_dir(tag) / "receipts" / name
    write_json(p, data)
    run_path = run_dir(tag) / "run.json"
    run = load_json(run_path, {}) or {}
    receipts = run.setdefault("receipts", [])
    rel = str(p.relative_to(run_dir(tag)))
    if rel not in receipts:
        receipts.append(rel)
    write_json(run_path, run)
    return p
