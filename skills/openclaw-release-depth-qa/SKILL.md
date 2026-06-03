---
name: openclaw-release-depth-qa
description: Use when generating or executing OpenClaw release QA that must cover every behavior-changing commit, not just baseline P0 smoke; produces commit-depth manual tests with evidence requirements.
version: 1.0.0
author: Herald Labs / OpenClaw QA
license: MIT
metadata:
  hermes:
    tags: [openclaw, qa, release, commit-coverage, manual-testing]
    related_skills: [openclaw-p0-release-qa, openclaw-evidence-review]
---

# OpenClaw Release Depth QA

## Overview

This skill prevents release QA from becoming a repeated “does it turn on?” checklist.

The standard P0 smoke test is necessary, but not sufficient. For every release, QA must also inspect the release delta and create manual tests for the actual behavior changed by commits.

## When to Use

Use this when:
- creating a QA checklist for a new OpenClaw alpha/beta release
- reviewing whether a tester packet is deep enough
- assigning tester scenarios beyond baseline smoke
- checking whether every commit in a release has meaningful manual coverage

Do not use this to replace P0 smoke. Use it alongside `openclaw-p0-release-qa`.

## Inputs Required

- target tag
- previous release/tag baseline
- compare URL or commit list
- release notes
- changed files
- merged PRs if available
- recent issues/risk signals
- target tester/platform/channel assignments

## Process

### 1. Build the release delta

Read:
- release notes
- compare diff
- commits between baseline and target tag
- changed files
- merged PRs
- nearby issues/regressions

Group commits only when they are part of the same behavior or subsystem. Do not hide unrelated commits under a generic group.

### 2. Create a commit coverage matrix

Every commit gets one row or a justified grouped row.

Required columns:
- commit SHA/title
- subsystem/files
- behavior or risk
- manual test
- expected result
- evidence required
- priority: P0/P1/P2
- disposition: `TESTED`, `GROUPED`, or `NO_MANUAL_TEST_NEEDED`

If `NO_MANUAL_TEST_NEEDED`, explain why.

### 3. Keep P0 baseline separate

P0 baseline proves the build is viable:
- install/upgrade
- version proof
- first response
- visible channel delivery
- plugin/tool visibility
- harmless failure/error clarity

Do not pretend this covers release-specific behavior.

### 4. Add release-specific depth tests

For each behavior-changing commit/group, write a human-executable test:

- preconditions
- exact steps
- expected result
- failure signs to watch for
- evidence required
- pass/fail/block criteria

Good examples:
- “Configure Discord, send marker `beta4-discord-reply-<timestamp>`, verify response lands in same thread and includes no duplicate delivery.”
- “Start from a pre-beta config using legacy provider alias, run upgrade, verify route migrates or error message identifies exact fix.”
- “Trigger budget exhaustion with a capped test key and verify error says budget exhausted, not schema/tool payload failure.”

Bad examples:
- “Test Discord.”
- “Check routing works.”
- “Make sure feature is okay.”

### 5. Assign depth scenarios

Not every tester needs every depth scenario. Assign focused scenarios by platform/channel:

- Windows installer/update
- macOS service/LaunchAgent
- Discord route
- Telegram route
- backup/restore
- SSH/MCP/tools
- provider/budget/error handling

Each tester still runs P0 baseline unless explicitly scoped otherwise.

### 6. Review checklist quality before dispatch

Before sending testers, reject the packet if:
- it has no commit coverage matrix
- it is materially the same as the prior release checklist
- it only asks install/start/hello
- it lacks release-specific expected results
- it lacks evidence requirements
- it cannot catch failures missed by green automated tests

## Output Structure

Produce:

1. Release summary
2. Commit coverage matrix
3. P0 baseline checklist
4. Release-specific depth checklist
5. Tester assignment matrix
6. Evidence requirements
7. Evidence review acceptance gate

## Verification Checklist

- [ ] Every behavior-changing commit is covered or explicitly exempted
- [ ] P0 baseline is present but not the only content
- [ ] Release-specific tests have exact steps and expected results
- [ ] Evidence required for each row
- [ ] Tester assignments are clear
- [ ] Full evidence review required before acceptance
