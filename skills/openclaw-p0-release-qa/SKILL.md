---
name: openclaw-p0-release-qa
description: Use when a tester agent needs to run OpenClaw alpha/beta P0 release QA, collect evidence, and produce a GitHub-ready QA report without leaking secrets.
version: 1.0.0
author: Herald Labs / OpenClaw QA
license: MIT
metadata:
  hermes:
    tags: [openclaw, qa, p0, beta, tester, github-issues]
    related_skills: []
---

# OpenClaw P0 Release QA

## Overview

This skill gives a tester agent one job: run the OpenClaw P0 release smoke test for a specific alpha/beta tag, collect receipts, and produce a clean QA issue/report.

The goal is not "I tried it." The goal is a reproducible pass/block/fail record with environment, commands, evidence links, and no exposed secrets.

## When to Use

Use this when:
- You are assigned an OpenClaw release tag such as `v2026.6.1-beta.3`.
- You need to test install/upgrade, first response, channel delivery, plugin/tool visibility, and harmless failure handling.
- You need to file a QA receipt in `HeraldLab/OpenclawQA` or prepare a report for a Discord tester thread.

Do not use this to:
- File directly upstream in `openclaw/openclaw` unless the QA manager asks.
- Post raw API keys, private SSH keys, `.env` files, tokens, cookies, or full unredacted configs.
- Invent evidence. If a command failed or was not run, mark it `BLOCKED` or `NOT_ENOUGH_INFO`.

## Inputs Required

Before starting, capture:

- Release tag: `<tag>`
- Release URL: `<upstream release URL>`
- QA run folder: `<HeraldLab/OpenclawQA run URL>`
- Tester name/handle
- OS and device details
- Assigned channel(s): Discord, Telegram, etc.
- Provider/model route expected for the test
- Any release-specific extra scenario assigned by the QA manager

## P0 Test Checklist

Run these checks in order.

### 1. Install or upgrade to the assigned tag

Record:
- install/update command used
- final OpenClaw version
- commit/hash if shown
- screenshot or terminal output proving the version

Expected result:
- OpenClaw reports the assigned alpha/beta version.

### 2. First normal response

Start OpenClaw and send a simple prompt such as:

```text
hello — P0 smoke test for <tag>
```

Record:
- command/UI used
- model/provider route if visible
- screenshot/log snippet of a normal response

Expected result:
- OpenClaw responds normally without crashing or routing to an unexpected provider.

### 3. Visible channel delivery

If Discord/Telegram/another channel is configured, send or trigger one message through OpenClaw.

Record:
- channel tested
- message content or test marker
- screenshot showing the message reached the visible channel/thread
- whether reply and/or receive path worked

Expected result:
- Human-visible channel receives the expected response.

### 4. Plugin/tool visibility sanity check

Run the relevant doctor/tool/plugin command available in your build, for example:

```bash
openclaw doctor --fix
openclaw gateway status
openclaw tools list
openclaw plugins list
```

If a command does not exist in your build, record the exact error and continue with the closest available command.

Record:
- command used
- number/list of visible tools/plugins if available
- screenshot/log snippet

Expected result:
- Tools/plugins are visible and not silently omitted from the runtime.

### 5. Harmless failure handling

Trigger one safe, non-destructive failure. Examples:
- use an obviously invalid provider/model alias
- run a command with a missing optional config
- invoke a harmless nonexistent tool/route

Do not delete data or break a real credential.

Record:
- exact command/action
- error message
- screenshot/log snippet

Expected result:
- Error is understandable and points to the real problem. If it is misleading, report that as a finding.

### 6. Release-specific assigned scenario

If the QA manager assigned an extra scenario, run it here. Examples:
- backup creation
- SSH keys
- MCP tool route
- specific bug regression

Record:
- exact commands
- expected result
- actual result
- evidence

If not assigned, write `Not assigned`.

## Verdict Rules

Use exactly one verdict:

- `PASS` — all assigned P0 checks passed with accessible evidence.
- `PASS_WITH_CAVEAT` — checks passed, but there is a known non-blocking warning.
- `BLOCKED` — unable to complete because of setup, credentials, budget, permissions, or environment.
- `FAIL` — reproducible product failure in the assigned release.
- `NOT_ENOUGH_INFO` — evidence is missing or unclear.

## Evidence Rules

Evidence can be:
- screen recording/video, preferred for full P0 runs
- screenshots, acceptable only when they cover every required row
- terminal logs
- Discord/Telegram message links
- GitHub issue links
- cloud folder links accessible to the QA team

Video expectation:
- Record the whole P0 run when possible, not just the final screen.
- The QA reviewer will inspect the video end-to-end before accepting the report.
- If the video shows warnings/errors not mentioned in the report, the report may be returned for clarification.

Required hygiene:
- redact API keys/tokens
- redact private SSH keys
- do not post `.env` files
- do not expose passwords, cookies, or private DMs
- include enough surrounding context to prove what happened

## GitHub QA Issue Format

File QA receipts in `HeraldLab/OpenclawQA`, not upstream, unless instructed.

Title format:

```text
[<tag>][P0 Smoke] <tester name> — <OS/device> — <PASS|BLOCKED|FAIL>
```

Body template:

```md
## Verdict
<PASS | PASS_WITH_CAVEAT | BLOCKED | FAIL | NOT_ENOUGH_INFO> — <one sentence summary>

## Environment
- Tester: <name / handle>
- OpenClaw version: `<version>`
- Commit: `<commit if known>`
- OS/device: <OS and device>
- Install/update method: `<command or package path>`
- Provider/model route: `<route>`
- Assigned channel(s): <Discord / Telegram / etc.>

## Commands / setup used
<paste safe commands only, no secrets>

## P0 checklist
- [ ] Install/upgrade to assigned tag
- [ ] One normal OpenClaw response
- [ ] Visible channel delivery works
- [ ] Plugins/tools visible
- [ ] Harmless failure gives understandable error
- [ ] Release-specific scenario, if assigned: <name or Not assigned>

## Evidence links
- Screen recording / video:
- Install/upgrade:
- First response:
- Channel delivery:
- Plugins/tools:
- Harmless failure:
- Release-specific scenario:

## Actual results
<What happened. Include exact error strings for failures.>

## Expected results
<What should have happened.>

## Bugs/blockers
<None, or one bullet per issue-worthy finding.>

## Caveats / warnings
<Known non-blocking warnings, if any.>

## Secrets check
- [ ] No raw API keys/tokens included
- [ ] No private SSH keys included
- [ ] No passwords/cookies/private DMs included
```

## If You Hit a Bug

Do this before calling it a product bug:

1. Re-run once if safe.
2. Capture exact command/action and exact error text.
3. Note whether it is reproducible.
4. Search the QA run/issues for the same symptom if you can.
5. File the QA issue with verdict `FAIL` or `BLOCKED`.
6. Let the QA manager dedupe and decide whether to file upstream.

## Common Pitfalls

1. **Only saying “passed.”** A pass without evidence is not complete.
2. **Posting secrets.** Redact first. If unsure, ask before posting.
3. **Filing upstream directly.** Use the QA repo unless told otherwise.
4. **Skipping environment details.** Version, OS, and route are mandatory.
5. **Treating warnings as failures without proof.** Mark non-blocking caveats separately from blockers.
6. **Using stale instructions.** Always test the assigned tag and run folder.

## Verification Checklist

Before submitting:

- [ ] Verdict selected from the allowed set
- [ ] Version/tag included
- [ ] OS/device included
- [ ] Install/update method included
- [ ] Provider/model route included
- [ ] Every P0 row has pass/block/fail status
- [ ] Evidence links open for the QA team
- [ ] Screen recording/video provided for any sequence-dependent result, or screenshots fully cover every P0 row
- [ ] Secrets check completed
- [ ] GitHub QA issue or Discord report link shared back in the assigned thread

## Reviewer Follow-Up

After submission, the QA reviewer will run the evidence review workflow:

- open all evidence links
- watch/analyze the full video duration
- timestamp proof for every P0 row
- record visible warnings/errors
- confirm no secrets are exposed
- comment on the QA issue with `EVIDENCE_CONFIRMED`, `EVIDENCE_CONFIRMED_WITH_CAVEAT`, or a request for missing/redacted evidence

The report is not operationally accepted until that evidence review is complete.
