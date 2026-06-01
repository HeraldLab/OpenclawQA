# Human Review Packet — OpenClaw `v2026.6.1-beta.1` Manual QA Dispatch

**Review this.**

## Decision requested

Approve or change the tester dispatch package for OpenClaw `v2026.6.1-beta.1`.

Reply with one of:

- `APPROVE DISPATCH`
- `CHANGE: <specific edits>`
- `BLOCK: <reason>`

If approved, Book should dispatch the tester instructions publicly and begin collecting real manual QA evidence.

## What you need to review

You do **not** need to review the automation scripts or repo internals for this gate.

Review these three things:

1. **Target freshness** — are we testing the right release?
   - File: `pre-send-freshness-recheck.md`
   - Current decision: target remains current; latest beta is `v2026.6.1-beta.1`.

2. **Manual QA checklist** — are these the right things to ask testers to run?
   - File: `manual-qa-checklist.md`
   - Includes install, stable upgrade, prior prerelease upgrade, first-run smoke, provider/model routing, messaging delivery, `message.send` leak/routing regression, plugin/tool visibility, memory/session persistence, UI send reset, sleep/reconnect, and diagnostics/secrets checks.

3. **Tester instructions / dispatch content** — is this acceptable to send publicly to testers?
   - File: `tester-instructions.md`
   - Requires screen recording, environment header, logs/screenshots, redaction, and one issue-worthy bug per finding.

## Links

- Pre-send freshness recheck: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.1-beta.1/pre-send-freshness-recheck.md
- Manual QA checklist: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.1-beta.1/manual-qa-checklist.md
- Tester instructions: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.1-beta.1/tester-instructions.md
- Review gate report: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.1-beta.1/review-gate-report.md
- Status vs v4 workflow: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.1-beta.1/workflow-status-vs-v4.md

## Current status

- Automation spine: built and verified.
- Latest beta: `v2026.6.1-beta.1`.
- Pre-send freshness recheck: passed at `2026-06-01T16:48:47Z`.
- Checklist/review gates: draft passed.
- Human sign-off: **pending**.
- Tester dispatch: **not sent**.
- Real manual QA evidence: **not collected yet**.

## Proposed dispatch summary

If approved, Book should send a public tester message that says:

```markdown
QA run open for `v2026.6.1-beta.1`.

Review target/freshness:
- Latest beta confirmed: `v2026.6.1-beta.1`
- Release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.1-beta.1
- Full run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.1-beta.1
- Checklist: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.1-beta.1/manual-qa-checklist.md

Please run the checklist with screen recording on.
No repo write access is needed. Reply in Discord with the report; Herald Labs will dedupe and file validated upstream OpenClaw issues using our account.
For every row, report: `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN`.

Required environment header:
- OpenClaw version:
- Operating system:
- Install method:
- Model:
- Provider / routing chain:
- Additional provider/model setup details:

For each bug finding:
- Bug type:
- Beta release blocker:
- Summary:
- Steps to reproduce:
- Expected behavior:
- Actual behavior:
- Logs, screenshots, and evidence:
- Impact and severity:
- Additional information:

Rules:
- One issue-worthy bug per finding.
- Do not speculate.
- Redact tokens/API keys/private URLs/customer data.
- If a field cannot be answered from evidence, write `NOT_ENOUGH_INFO`.
```

## Known caveat

The release-context packet is usable, but not perfect against the v4 ideal: changed-files / compare-range / confirmed-in-range classification is still partial. The checklist compensates with broad beta regression coverage and watchlist probes, but if you want strict v4 purity, ask for `CHANGE: complete compare-range classification first`.
