# Tester Instructions Template

Target tag: `<tag>`

## Mandatory community-ping gate

Before dispatch, check `#clawtributors` for the exact tag, release family, and newer `@Beta Pings` corrections since the prior beta. Record message ID, author, timestamp, and extracted test asks in the run's `release-context.md`.

If no exact-tag ping exists, record that explicitly and use the newest verified family-level ask unless a newer message overrides it. Do not dispatch while community-ping status is `NOT_CHECKED`.

## Required evidence

- Run the assigned human scenario cards manually; do not only run commands invisibly through an agent
- End-to-end screen recording of the P0/scenario run where possible
- Logs or terminal output for each command
- OS and install method
- OpenClaw version/tag/commit
- Provider/model route
- Exact steps tested
- Expected vs actual behavior for each scenario
- Human judgment notes: what was confusing, broken, slow, duplicated, or not trustworthy
- Evidence link for every P0/scenario row
- One issue-worthy finding per bug
- Secrets check: no raw API keys, private SSH keys, `.env`, tokens, cookies, passwords, or private DMs

Submit reports using this repo's GitHub issue templates. After submission, reply in your assigned Discord thread with the issue link.

QA reviewers will open all evidence links and review the full screen recording before accepting the report.
