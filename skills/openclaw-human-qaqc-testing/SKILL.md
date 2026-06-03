---
name: openclaw-human-qaqc-testing
description: Use when designing OpenClaw QA for human testers; turns release commits into realistic hands-on scenarios that validate user experience and behavior, not automatable smoke checks.
version: 1.0.0
author: Herald Labs / OpenClaw QA
license: MIT
metadata:
  hermes:
    tags: [openclaw, qa, human-testing, exploratory-testing, release-qa]
    related_skills: [openclaw-release-depth-qa, openclaw-p0-release-qa, openclaw-evidence-review]
---

# OpenClaw Human QA/QC Testing

## Overview

This skill is for designing QA that humans can use to test OpenClaw well.

Agents can generate checklists, but human QA is not meant to be a set of automatable commands. It should exercise real workflows, real channels, real setup confusion, and real user judgment.

## When to Use

Use this when:
- creating tester-facing instructions for an OpenClaw release
- converting commit changes into human scenario cards
- reviewing whether a QA packet is too shallow or too agent/automation-oriented
- asking testers to validate behavior outside automated tests

Do not use this to replace release-depth or P0 checks. It adds the human scenario layer on top.

## Core Rule

A valid human QA packet must answer:

> Can a real person use this OpenClaw feature successfully, understand what happened, recover from safe failures, and trust the result?

If the packet only asks “install, run hello, screenshot output,” it is not enough.

## Build Human Scenario Cards

For each important release change, write a scenario card.

Required fields:

- **User goal:** what the human is trying to accomplish.
- **Context:** OS, channel, provider/model, starting state.
- **Manual steps:** what the human should click/type/run/read.
- **Expected behavior:** what success looks like in the actual UI/CLI/channel.
- **Failure signs:** wrong channel, missing reply, duplicate output, confusing error, stale state, slow/hung flow.
- **Evidence required:** video timestamp, screenshot, logs, GitHub issue link.
- **Human judgment question:** would you trust this as a user? If not, why?

## Scenario Categories

Use whichever categories match the release commits. Pull concrete cards from `docs/human-scenario-library.md`, especially:

- Messaging channels: Discord thread routing, parent/thread isolation, permission failure, Telegram delivery, media attachments.
- Plugin lifecycle: discover/install, auth/config, use in a real task, restart persistence, disable/uninstall.
- Provider/model route: expected route visibility, budget/auth failure clarity.
- Sessions/state: restart continuity, upgrade preserving config.
- Error/UX: human-readable recovery and no silent success.

### First-run/onboarding

Goal: a human can install/update and get useful output without maintainer hand-holding.

Test:
- follow public instructions
- note confusion
- confirm version/tag
- send first prompt
- verify route and output

### Messaging/channel delivery

Goal: a human sees OpenClaw respond in the expected place.

Test:
- send a unique marker in the real channel/thread
- verify response arrives in that same expected surface
- check duplicates, delays, wrong identity, wrong thread, no-output behavior

### Release feature workflow

Goal: the human uses the actual feature changed by the release.

Test:
- use realistic input, not just “hello”
- follow the expected user path
- verify output/state against the release claim
- try one normal edge case

### Error recovery

Goal: a human can understand and recover from a safe failure.

Test:
- trigger a harmless failure
- read the error as a user
- state the recovery action the error suggests

### Persistence/restart/upgrade

Goal: behavior survives real usage.

Test when relevant:
- restart app/gateway
- reopen TUI/session
- rerun after update
- confirm config/state still works

## Tester Report Requirements

Every human QA report should include:

- tester name/handle
- release tag
- OS/device
- provider/model route
- channel(s)
- overall verdict
- scenario-by-scenario results
- evidence links
- warnings/errors observed
- confusion/UX notes
- secrets check

Required human observation fields per scenario:

- Expected
- Actual
- What felt confusing or broken
- Would you trust this as a user?
- Evidence link/timestamp

## Good vs Bad QA

Bad:
- “Run OpenClaw and check it works.”
- “Send hello.”
- “Confirm Discord works.”
- “Paste screenshot.”

Good:
- “In the assigned Discord thread, send marker `beta4-routing-<timestamp>`. Confirm OpenClaw replies in the same thread, only once, under the correct identity, within a reasonable delay. Record what happened and whether a normal user would know what to do if no reply appears.”

## Acceptance Gate

Before dispatching a tester packet, verify:

- [ ] It includes human scenario cards, not only commands.
- [ ] It tests release-specific behavior from commits.
- [ ] Each scenario has expected behavior and failure signs.
- [ ] Each scenario asks for human judgment/UX notes.
- [ ] Evidence requires screen recording/video where possible.
- [ ] It cannot be fully satisfied by an agent running commands invisibly.

## Evidence Review Tie-In

The reviewer must watch the full recording and check that:

- the human performed the scenario
- visible behavior matched expectations
- confusion/warnings/errors were recorded
- no secrets were exposed

If a command succeeds but the human workflow is confusing, broken, or not trustworthy, do not mark it as a clean pass.
