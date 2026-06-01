#!/usr/bin/env python3
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def run(*args):
    return subprocess.run([sys.executable, *args], cwd=ROOT, text=True, capture_output=True, check=True)

class WorkflowScriptTests(unittest.TestCase):
    tag = "v2099.1.1-beta.1"

    @classmethod
    def setUpClass(cls):
        run("scripts/create-run.py", cls.tag)

    def test_create_run_force(self):
        p = ROOT / "runs" / self.tag / "run.json"
        self.assertTrue(p.exists())
        data = json.loads(p.read_text())
        self.assertEqual(data["tag"], self.tag)
        self.assertIn("HeraldLab/OpenclawQA", data["links"]["github_run_folder"])

    def test_render_instructions_for_existing_run(self):
        run("scripts/render-tester-instructions.py", self.tag)
        text = (ROOT / "runs" / self.tag / "tester-instructions.md").read_text()
        self.assertIn(f"OpenClaw `{self.tag}`", text)
        self.assertIn("Report results", text)

    def test_collect_dedupe_file_no_reports(self):
        run("scripts/collect-reports.py", self.tag)
        data = json.loads((ROOT / "runs" / self.tag / "tester-status.json").read_text())
        self.assertEqual(data["tag"], self.tag)
        run("scripts/dedupe-upstream-issues.py", self.tag)
        self.assertTrue((ROOT / "runs" / self.tag / "receipts" / "issue-dedupe.json").exists())
        run("scripts/file-upstream-issues.py", self.tag, "--dry-run")
        self.assertTrue((ROOT / "runs" / self.tag / "receipts" / "issue-file-results.json").exists())

    def test_validate_run(self):
        result = run("scripts/validate-run.py", self.tag)
        self.assertIn("ok", result.stdout)

if __name__ == "__main__":
    unittest.main()
