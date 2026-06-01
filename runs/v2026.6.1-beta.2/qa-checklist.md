# QA Checklist — OpenClaw `v2026.6.1-beta.2`

Generated: `2026-06-01T22:00:16Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.1-beta.2  
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.1-beta.2

## Pre-dispatch gate

- [x] Target tag exists upstream: `v2026.6.1-beta.2`.
- [x] Freshness run completed.
- [x] Tester instructions generated.
- [x] Adversarial review completed.
- [x] Live upstream issue filing remains disabled by default.
- [ ] Henry approved public tester dispatch.
- [ ] Pre-send freshness rerun after approval.
- [ ] Ada-owned public dispatch sent once.
- [ ] Discord release thread/message IDs recorded.

## Required tester evidence

Each tester report should include:

- [ ] OS/platform and version.
- [ ] Install/upgrade method and exact command used.
- [ ] Observed OpenClaw version/tag after install.
- [ ] Provider/model route used, if a model call is part of the test.
- [ ] Screenshot, screen recording, or Discord/message receipt where relevant.
- [ ] Redacted logs for failures.
- [ ] Clear final state: `PASS`, `BLOCKED`, or `NOT_ENOUGH_INFO`.

## P0 scenarios

- [ ] Install or upgrade to `v2026.6.1-beta.2`.
- [ ] Start OpenClaw and get one normal response.
- [ ] If configured, verify a human-visible message delivery path such as Discord/Telegram.
- [ ] Confirm configured tools/plugins are visible and usable.
- [ ] Trigger one harmless provider/config failure if safe, and confirm the error is understandable.

## Triage rules

- [ ] Do not file upstream until Herald Labs validates and dedupes the report.
- [ ] One issue per bug; do not combine unrelated failures.
- [ ] Keep secrets/API keys/private data out of public evidence.
- [ ] Mark reports missing OS, version/tag, steps, expected/actual, or evidence as `NOT_ENOUGH_INFO`.
- [ ] For severe install/auth/message-loss regressions, escalate to Henry/admin before public upstream filing.
