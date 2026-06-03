# Manual Human QA Operating Model

OpenClaw release QA exists to provide the human validation that automated tests cannot provide.

Automation can prepare context, generate packets, collect reports, and help reviewers inspect evidence. It is **not** the release evidence. The release evidence is named humans manually exercising OpenClaw in real surfaces, recording what happened, and judging whether the behavior is understandable, trustworthy, and usable.

## Core principle

> Human QA is the release gate. Automation is support/preflight.

Do not replace missing human QA with more scripts. If human coverage is missing, mark it missing, assign an owner, waive explicitly, or do not claim QA complete.

## Required roles

| Role | Responsibility | Must not do |
|---|---|---|
| QA coordinator | Build baseline + delta packet, assign humans, track coverage, collect receipts | Treat packet generation as QA completion |
| Human tester | Manually run assigned scenarios, screen-record, report confusion/errors/trust | Be replaced by silent agent/automation runs |
| Evidence reviewer | Watch/review evidence, confirm or contradict claims, classify warnings/errors | Accept release blockers from tool-only review |
| Release approver | Approve waivers and final QA status | Claim QA complete without accepted human evidence or waiver |

## Required release flow

1. **Detect release/tag.**
2. **Create run folder.**
3. **Prepare context with automation.** Release notes, compare diff, commits, PRs, issue signals.
4. **Generate manual QA packet.** Must include:
   - Baseline P0
   - Core Baseline P1
   - Delta P0/P1/P2 scenarios
   - named tester assignments
   - evidence requirements
   - reviewer assignment
5. **Human testers execute scenarios manually.** They record the session and capture expected vs actual behavior.
6. **Tester submits GitHub QA issue.** One canonical issue/report with evidence links and human judgment notes.
7. **Evidence reviewer reviews evidence.** Full video/evidence review for all blocking scenarios.
8. **Coordinator dedupes/file issues.** Confirmed bugs are deduped before upstream filing.
9. **Closeout report.** Includes human confidence, confusion/trust findings, missing coverage, waivers, and open blockers.

## Mandatory baseline coverage

### Baseline P0 — release-blocking

Every release must cover:

- install/upgrade
- version/commit proof
- first useful response
- one configured messaging channel end-to-end
- plugin/tool visibility sanity check
- one safe failure with understandable recovery
- no obvious secret exposure
- no silent false success

### Core Baseline P1 — mandatory unless explicitly marked `NOT_RUN`

Every release should have named human coverage for:

- restart/gateway persistence
- install and use one safe plugin
- provider/model route visibility
- config/session continuity after restart/update

If the release has multiple messaging surfaces in scope, each configured surface needs either human coverage or explicit `NOT_RUN` reason.

## Release-delta coverage

Delta QA is generated from the actual release changes.

- **Delta P0:** release-specific blocker tied to critical changed behavior.
- **Delta P1:** important changed behavior/regression.
- **Delta P2:** lower-risk edge case, polish, docs/instructions, unusual config.

Every behavior-changing commit must be covered by a scenario or explicitly marked `NO_MANUAL_TEST_NEEDED` with reason.

## Assignment requirements

Every blocking scenario must name:

- tester
- platform/OS
- channel/surface
- provider/model route if relevant
- scenario(s)
- expected evidence
- evidence reviewer
- due time

No named human assignee means no human QA coverage.

## Evidence requirements

Baseline P0 and Delta P0 require:

- end-to-end screen recording where possible
- timestamps for scenario proof
- screenshots/logs as supporting evidence
- secrets check
- human judgment notes
- reviewer verdict

Screenshots alone are acceptable only for static/non-sequential checks. If the scenario is a workflow, require video or an explicit reason video is unavailable.

## Reviewer requirements

For Baseline P0 and Delta P0:

- tool-assisted review is allowed
- tool-only acceptance is not
- a human reviewer owns the verdict

Allowed reviewer verdicts:

- `EVIDENCE_CONFIRMED`
- `EVIDENCE_CONFIRMED_WITH_CAVEAT`
- `NEEDS_MORE_EVIDENCE`
- `BLOCKED_BY_EVIDENCE_ERROR`
- `FAIL_FILE_UPSTREAM`
- `SECRET_EXPOSURE_REDACT`

## Waiver policy

A missing/failed Baseline P0 or Delta P0 requires explicit waiver.

Waiver must include:

- scenario waived
- reason
- risk accepted
- approver
- expiry/next action

Waivers are not silent skips. They appear in closeout.

## Closeout requirements

Every closeout must include:

- Baseline P0 status
- Core Baseline P1 status
- Delta P0/P1/P2 status
- human confidence summary
- top confusion/trust findings
- missing coverage
- waivers and owners
- upstream issues filed/commented
- whether QA is complete, incomplete, blocked, or waived

## Anti-patterns

Reject these:

- “CI is green, so QA is done.”
- “Agent ran commands, so human QA is done.”
- “Tester said pass, but no evidence review exists.”
- “Only install/start/hello tested.”
- “No named human owner for release blockers.”
- “No video/evidence for a workflow scenario.”
- “Waiver implied by silence.”
