# Human QA/QC Testing Playbook

OpenClaw release QA is primarily a **human usability and behavior validation exercise**. Agents can prepare packets, collect receipts, and review evidence, but the core test is a human using OpenClaw like a real user and judging whether the feature actually works.

## Principle

Do not reduce QA to command execution or automated pass/fail checks.

A good human QA packet answers:

- Can a real user understand what to do?
- Does the feature behave correctly in the actual app/runtime/channel?
- Does the output land where the human expects?
- Are errors understandable enough for a non-maintainer to recover?
- Does the workflow feel broken, confusing, slow, duplicated, or unsafe?
- Would this survive normal messy usage outside CI?

## Agent vs human responsibilities

| Actor | Responsibility |
|---|---|
| Agent / QA coordinator | Read release/commits, create scenario cards, define expected behavior, collect reports, dedupe issues. |
| Human tester | Manually perform scenarios, screen-record the experience, narrate confusion/errors, judge whether the flow works in real conditions. |
| Evidence reviewer | Watch the full video, confirm the human actually exercised the scenario, record errors/warnings/confusion. |

Agents may assist a tester with setup, but they must not replace the human interaction being tested.

## What humans should test

Each release packet should contain **human scenario cards**, not only technical checklist rows. Use `docs/human-scenario-library.md` as the scenario source for common OpenClaw surfaces such as messaging channels, plugin install/use, provider routes, restart/state, and error recovery.

A scenario card must include:

- **User goal:** what the tester is trying to accomplish.
- **Context:** platform, channel, provider/model route, starting state.
- **Manual steps:** what the human should click/type/run/read.
- **What “working” looks like:** observable behavior and success criteria.
- **What to watch for:** confusing UX, wrong route, missing output, duplicate messages, stale state, misleading errors.
- **Evidence required:** screen recording segment, screenshot, logs, issue link.
- **Human judgment question:** “Would you trust this as a user? If not, why?”

## Required human observations

For every scenario, testers should record:

- What they expected to happen.
- What actually happened.
- Whether they had to guess or ask for help.
- Whether any error message was clear and actionable.
- Whether the app felt stuck, slow, duplicated, or inconsistent.
- Whether output appeared in the correct place.
- Whether the feature worked after restart/retry when relevant.

These observations matter even when commands technically return success.

## Human scenario categories

Release QA should include the relevant categories below.

### 1. First-run / onboarding experience

Human goal: install/update OpenClaw and get to a useful first response without maintainer hand-holding.

Test:
- follow public instructions from a clean or realistic existing setup
- note every point of confusion
- confirm version/tag
- send first prompt
- verify response quality and route

Failure examples:
- instructions unclear
- command succeeds but app not usable
- wrong model/provider route
- hidden credential/budget issue
- error says schema/tool payload when budget is exhausted

### 2. Messaging/channel behavior

Human goal: make OpenClaw communicate in the configured channel.

Test:
- send a unique marker from the real channel/thread
- verify response appears in the same expected surface
- check duplicates, missing replies, delayed replies, wrong thread, wrong identity
- test reply vs receive path when relevant

Failure examples:
- response appears in wrong channel
- bot sees message but does not reply
- duplicate replies
- confusing no-output behavior
- permissions look fine but delivery fails

### 3. Feature workflow from the release commits

Human goal: use the actual feature changed by this release.

Test:
- run the release-specific scenario derived from commits/PRs
- use realistic input, not a toy “hello” only
- verify the visible result matches the release claim
- try one normal edge case

Failure examples:
- feature exists but is unusable
- output is technically present but wrong/incomplete
- UI/CLI wording sends user down wrong path
- state changes do not persist

### 4. Error recovery

Human goal: hit a safe failure and understand how to recover.

Test:
- trigger one harmless failure: invalid provider alias, missing optional config, capped budget, disconnected channel, etc.
- read the error as a user would
- state what action the error tells the user to take

Failure examples:
- misleading error
- stack trace with no user action
- wrong subsystem blamed
- no clear recovery instruction

### 5. Persistence / restart / upgrade state

Human goal: confirm the feature survives real usage, restart, or upgrade.

Test when relevant:
- restart gateway/app
- reopen TUI/session
- rerun command after update
- confirm prior config/state still works

Failure examples:
- works once then breaks after restart
- stale config silently overrides new behavior
- migration partially succeeds

## Human report format

Each tester report should include:

```md
## Human QA summary
- Tester:
- Release tag:
- OS/device:
- Provider/model route:
- Channel(s):
- Overall verdict: PASS / PASS_WITH_CAVEAT / BLOCKED / FAIL / NOT_ENOUGH_INFO

## Scenario results

### Scenario: <name>
Human goal: <goal>
What I did:
1. ...
2. ...

Expected:
Actual:
Human judgment: <worked / confusing / broken / not trustworthy>
Evidence: <video timestamp/link, screenshot, logs>
Warnings/errors observed:

## Confusion / UX notes
- <anything unclear, surprising, or hard to recover from>

## Bugs/blockers
- <one bullet per issue-worthy finding>

## Secrets check
- [ ] No raw API keys/tokens
- [ ] No private SSH keys
- [ ] No .env/passwords/cookies/private DMs
```

## Checklist quality gate

Reject a QA packet if it only asks the tester to:

- install/update
- send “hello”
- confirm one message appears
- paste logs

That is smoke testing, not human QA/QC.

A valid packet must include release-specific human scenarios that require observation and judgment.

## Evidence review requirement

The evidence reviewer must watch the full recording and confirm:

- the human performed the assigned scenarios
- visible behavior matched the expected result
- any warnings/errors were captured and classified
- tester confusion was captured when present
- no secrets were exposed

A report with a passing command but a visibly confused/broken human workflow is not a clean pass.
