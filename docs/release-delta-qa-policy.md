# Release Delta QA Policy

Every OpenClaw release gets two kinds of manual QA:

1. **Baseline human QA** — always run for every release.
2. **Release-delta human QA** — generated from the actual release notes, compare diff, commits, PRs, and issue signals.

Baseline QA prevents copy-paste “does it turn on?” regressions. Delta QA proves the new or changed behavior works for real humans.

## Priority model

| Layer | Priority | Meaning |
|---|---|---|
| Baseline | P0 | Always-run release blocker |
| Baseline | P1 | Always-run core confidence |
| Delta | P0 | Release-specific blocker tied to critical changed behavior |
| Delta | P1 | Important release-specific behavior/regression |
| Delta | P2 | Lower-risk edge case, polish, docs/instructions, unusual config |

## Always-run baseline

The baseline source of truth is `docs/baseline-human-qa-checklist.md`.

Every release packet must include:

- Baseline P0 section
- Baseline P1 section
- which tester(s) are assigned to each baseline row
- evidence required for each row

## Release-delta QA

Delta QA is generated per release.

Input sources:
- release notes
- compare range from previous release/tag to target tag
- commit list
- changed files
- merged PRs
- recent issues/regression signals
- known product risk areas

For each behavior-changing commit or coherent commit group, decide whether it creates a delta P0/P1/P2 scenario.

## Delta P0 — release-specific blockers

Classify a changed behavior as **Delta P0** when it touches or risks:

- install/update/migration
- first-run/onboarding
- provider/model/auth/budget route
- messaging delivery to human-visible channels
- plugin/tool injection or execution
- user/session/state persistence
- security/secrets/permissions
- destructive or irreversible actions
- user-visible error recovery for core flows
- anything likely to make OpenClaw unusable for normal testers

Delta P0 scenarios must pass or receive explicit waiver before release confidence is claimed.

## Delta P1 — important release-specific behavior

Classify as **Delta P1** when it touches:

- important but non-blocking workflow changes
- secondary channel behavior
- plugin lifecycle that is not the main release claim
- restart/retry behavior
- config/docs mismatch that could confuse users
- performance/latency visible to humans
- regressions in adjacent but non-critical flows

Delta P1 failures need caveat, owner, and next action.

## Delta P2 — lower-risk edge cases

Classify as **Delta P2** when it touches:

- uncommon configs
- polish/wording/UX copy
- docs-only behavior validation
- rare platform edge cases
- nice-to-have regression coverage

Delta P2 can be deferred, but should be tracked.

## Required delta output

Every release packet must include a **Delta coverage matrix**:

| Commit/group | Changed area | Human risk | Scenario | Priority | Evidence | Disposition |
|---|---|---|---|---|---|---|

Allowed dispositions:

- `DELTA_P0_TEST`
- `DELTA_P1_TEST`
- `DELTA_P2_TEST`
- `GROUPED_WITH_<id>`
- `NO_MANUAL_TEST_NEEDED`

`NO_MANUAL_TEST_NEEDED` requires a concrete reason, such as docs-only, comments-only, or internal-only refactor with no user path and existing coverage.

## Human scenario requirement

Each delta P0/P1 scenario must be written as a human scenario card:

- user goal
- starting state/context
- manual steps
- expected visible behavior
- failure/confusion signs
- evidence required
- pass/fail/block criteria
- human judgment prompt

A command-only checklist row is not enough.

## How to combine baseline and delta QA

A release tester packet should be ordered like this:

1. Release summary
2. Baseline P0 checklist
3. Baseline P1 checklist
4. Delta coverage matrix
5. Delta P0 human scenarios
6. Delta P1/P2 human scenarios
7. Evidence and reporting instructions
8. Evidence review acceptance gate

## Assignment model

Not every tester must run every scenario.

Recommended assignment:

- Every active tester runs Baseline P0, unless explicitly scoped.
- At least one tester runs Baseline P1 plugin and restart checks.
- Delta P0 scenarios are assigned to named testers/platforms.
- Delta P1/P2 scenarios are split by platform/channel expertise.

Example:

| Tester | Baseline | Delta scenario |
|---|---|---|
| Miriam / Windows | Baseline P0 + plugin P1 | Windows install/update + Discord delivery |
| Ayomide / Telegram | Baseline P0 messaging | Telegram delivery + backup scenario |
| Anny / Discord | Baseline P0 channel | Discord permissions/reply routing |
| Gabriel / macOS | Baseline P0/P1 restart | Gateway restart/session persistence |

## Acceptance rule

A release is not “QA complete” until:

- Baseline P0 is passed or explicitly waived.
- Delta P0 is passed or explicitly waived.
- P1 failures are documented with owner/next action.
- Evidence review confirms submitted evidence and videos.
- Confirmed bugs are deduped and filed/commented upstream when appropriate.

## Anti-patterns

Reject packets that:

- only include Baseline P0
- treat “green automated tests” as sufficient
- omit delta commit coverage
- have no human scenario cards
- can be completed entirely by an agent out of sight
- lack expected visible behavior
- lack failure/confusion signs
- lack evidence requirements
