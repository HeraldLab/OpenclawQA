# Release Checklist Quality Rubric

This rubric prevents OpenClaw QA packets from becoming copy-pasted “does it turn on?” smoke tests.

## Rule

Every release QA packet must contain two layers:

1. **P0 baseline smoke** — proves the build installs, starts, responds, routes messages, exposes tools/plugins, and handles one harmless failure.
2. **Commit-depth QA** — proves the actual behavior changed by the release works in real user conditions.

A packet with only P0 baseline smoke is incomplete unless the release has no behavior-changing commits and the checklist explicitly says so with evidence.

## Required checklist sections

### 1. Release delta summary

Include:
- target tag
- compare range
- commit count
- changed subsystems
- user-facing changes
- operational/routing/migration risks

### 2. Commit coverage matrix

Every commit must appear in the matrix, either individually or in a justified group.

Required columns:
- commit SHA/title
- changed files/subsystem
- behavior or risk introduced
- manual test case
- expected result
- evidence required
- priority: P0/P1/P2
- disposition: `TESTED`, `GROUPED`, or `NO_MANUAL_TEST_NEEDED`

`NO_MANUAL_TEST_NEEDED` requires a reason, e.g. docs-only, comments-only, internal refactor with existing coverage plus no user-facing path.

### 3. P0 baseline

Use the standard P0 smoke checks:
- install/upgrade to assigned tag
- version/commit proof
- first normal response
- visible channel delivery
- plugin/tool visibility
- harmless failure/error clarity

### 4. Release-specific depth checks

For each behavior-changing commit group, add a test that exercises the actual shipped behavior.

Good test shape:
- setup/preconditions
- exact steps
- expected result
- failure signs to watch for
- evidence required
- pass/fail/block criteria

Bad test shape:
- “Test the feature”
- “Confirm it works”
- “Run app”
- “Check no errors” without a specific user path

### 5. Regression and edge cases

Include tests for:
- upgrade/migration state
- stale config/backward compatibility
- provider/model routing
- channel delivery and replies
- permissions/auth/budget limits
- plugin/tool injection
- persistence/session state
- errors that should be human-understandable

## Acceptance gate for checklist quality

Before dispatching testers, the QA coordinator must answer:

- Does every behavior-changing commit have a manual test or a justified no-test disposition?
- Are tests specific enough for a human tester to execute without asking what “works” means?
- Does each test say what evidence proves pass/fail?
- Are release-specific changes tested beyond generic P0 smoke?
- Would this checklist catch a real-world failure even if automated CI is green?

If any answer is no, do not dispatch. Revise the checklist.

## Anti-copy-paste checks

Flag the packet if:
- it is materially identical to the previous release checklist
- it only tests install/start/hello
- it does not mention commit SHAs or changed subsystems
- it lacks release-specific scenarios
- it has no expected results beyond “works”
- it has no edge/failure checks

## Evidence review tie-in

Even a good checklist is not accepted until submitted evidence is reviewed end-to-end:
- all evidence links opened
- full video/screen recording watched or analyzed
- timestamps recorded for each P0 and release-specific row
- visible warnings/errors classified
- secrets checked
