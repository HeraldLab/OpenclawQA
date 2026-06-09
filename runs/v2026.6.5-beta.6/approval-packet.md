# Approval Packet — OpenClaw `v2026.6.5-beta.6`

Status: `REVIEW_READY_WITH_CAVEATS`

Artifacts:
- Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.5-beta.6
- Tester instructions: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.5-beta.6/tester-instructions.md
- QA checklist: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.5-beta.6/qa-checklist.md
- Adversarial review: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.5-beta.6/adversarial-review.md
- Freshness report: https://github.com/HeraldLab/OpenclawQA/blob/main/runs/v2026.6.5-beta.6/freshness-report.md

Recommended dispatch:
- FIRST_WAVE: Ayomide, Mariam, Anny.
- Threads:
  - Ayomide: `1511072287250714626`
  - Mariam: `1510234021052026880`
  - Anny: `1511072288412405980`
- Hold Gabriel until gateway security-audit blocker resolves or Henry/admin explicitly waives/closes it.
- Samuel is optional only if Henry/admin wants one additional install-smoke lane.

Known caveats:
- No reports yet for beta6.
- npm Telegram beta E2E was not supplied in the release verification block.
- Plugin ClawHub publish was dispatched separately and not awaited by upstream proof.
- Confirmed bugs still require evidence review/dedupe and separate upstream filing approval.

Please reply with exactly one:
- `APPROVE DISPATCH v2026.6.5-beta.6 FIRST_WAVE`
- `APPROVE DISPATCH v2026.6.5-beta.6 ALL_ACTIVE`
- `CHANGE: <specific edits>`
- `BLOCK: <reason>`
