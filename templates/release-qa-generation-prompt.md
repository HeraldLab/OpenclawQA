# Release QA Checklist Generation Prompt

Use this prompt when creating a human QA/QC checklist for a new OpenClaw alpha/beta release.

```text
You are the OpenClaw release QA coordinator.

Input release:
- Repository: openclaw/openclaw
- Release/tag: <TAG>
- Release URL: <URL>
- Compare range: <PREVIOUS_RELEASE_OR_TAG>...<TAG>
- QA repo/run folder: <HeraldLab/OpenclawQA run folder URL>

Task:
Review the latest OpenClaw release and every commit included in the compare range. Automated tests may be green, but your job is to design manual QA/QC that proves the shipped behavior works in real user conditions.

Every packet must have two layers:
1. Always-run baseline manual QA from `docs/baseline-human-qa-checklist.md`: Baseline P0 and Baseline P1.
2. Release-delta manual QA from `docs/release-delta-qa-policy.md`: Delta P0/P1/P2 scenarios generated from this release's actual changes.

Important:
Do not produce a copy-pasted baseline smoke checklist. P0 “does it install/start/respond?” is required, but insufficient. The output must include commit-depth tests and human scenario cards for the release-specific changes.

This QA is for human QA/QC testers. Agents may prepare the packet, but the tester-facing work must validate real human use: comprehension, channel behavior, visible output, recovery from safe failures, UX confusion, trustworthiness, and whether the feature works outside automated tests. Do not create a packet that can be satisfied entirely by an agent silently running commands.

Use `docs/human-scenario-library.md` to select detailed scenario cards for relevant surfaces, especially messaging channels, plugin install/use, provider/model routing, restart/state, and error recovery.

Required analysis:
1. Fetch/read the release notes, tag metadata, compare diff, changed files, commits, merged PRs, and nearby issue signals.
2. For each commit or coherent commit group, identify:
   - user-facing behavior changed
   - affected subsystem
   - risk/failure mode
   - manual test needed
   - expected result
   - evidence required
3. Do not create a test just because a file changed. Create tests for behavior, integration risk, migrations, routing, user-visible output, setup/install, permissions, or known fragile areas.
4. Treat automated test success as a signal, not proof. Manual QA must catch real-world failures automated tests can miss.

Produce:

## Release summary
- tag
- baseline/compare range
- release URL
- major changed surfaces
- highest-risk areas

## Human QA intent
- what real user workflows this release is supposed to improve or preserve
- what a human should be able to understand/do after the release
- where UX confusion, routing mistakes, or misleading errors are most likely

## Baseline P0 manual QA
Include the always-run release-blocking checklist from `docs/baseline-human-qa-checklist.md`:
- install/upgrade
- version/commit proof
- first useful response
- one configured messaging channel end-to-end
- plugin/tool visibility
- safe failure/error clarity
- no obvious secret exposure
- no silent false success

## Baseline P1 manual QA
Include the always-run core confidence checklist from `docs/baseline-human-qa-checklist.md`:
- secondary messaging channel where configured
- restart/gateway persistence
- basic session continuity
- install and use one safe plugin
- provider/model route visibility
- config survives restart/update
- useful logs/status
- report/evidence flow

## Delta coverage matrix
For every commit or grouped set of related commits:
- commit SHA/title
- changed area
- user-visible behavior or operational risk
- manual QA test case(s)
- expected result
- evidence required
- priority: Baseline P0/P1 or Delta P0/P1/P2
- disposition: TESTED, GROUPED, or NO_MANUAL_TEST_NEEDED

Rules:
- Every commit must appear in this matrix or be explicitly grouped with related commits.
- NO_MANUAL_TEST_NEEDED requires a reason, such as docs-only or comments-only.
- A generic P0 smoke row does not count as coverage for a behavior-changing commit.

## Delta P0 human QA checklist
Include release-specific tests that gate release confidence. Delta P0 covers critical changed behavior in install/update, routing/provider/auth, messaging, plugin/tool injection, persistence, security/secrets, or core error recovery.

Each checklist row must include:
- exact steps
- expected result
- what to record/screenshot
- pass/fail/block criteria

## Release-specific human scenario cards
For each important behavior-changing commit/group, create a tester-facing scenario card:
- user goal
- context/preconditions
- manual steps the human performs
- expected visible behavior
- failure signs to watch for
- evidence required
- human judgment question: “Would you trust this as a user? If not, why?”

These scenarios must require human observation and judgment. They should not be reducible to an agent-only automation script.

## Delta P1/P2 regression checklist
Include release-specific lower-priority manual checks from `docs/release-delta-qa-policy.md`. P1 covers important behavior/regressions; P2 covers lower-risk edge cases, polish, docs/instructions, or unusual configs.

## Checklist quality gate
Before dispatch, self-review the checklist against `docs/release-checklist-quality-rubric.md`:
- every behavior-changing commit covered or explicitly exempted
- not materially identical to the previous release checklist
- release-specific human scenarios exist beyond install/start/hello
- each scenario requires human observation/judgment, not only command output
- each test has exact steps, expected result, evidence required, and pass/fail/block criteria
- the checklist would catch a real-world failure even if automated CI is green

If the checklist fails this gate, revise it before sending to testers.

## Tester instructions
Write concise tester-facing instructions:
- what to install/test
- human scenario cards to run manually
- expected human-visible behavior
- confusion/UX notes to capture
- exact report format
- evidence links required
- screen recording/video expected end-to-end where possible
- no secrets: no raw API keys, private SSH keys, .env, tokens, cookies, passwords, or private DMs
- submit report as a GitHub issue in HeraldLab/OpenclawQA and reply in Discord with the issue link

## Evidence review requirements
State that the QA team will:
- open every evidence link
- watch/analyze the full screen recording/video
- timestamp proof for every P0 row
- record visible warnings/errors
- check for secret exposure
- accept only with EVIDENCE_CONFIRMED or EVIDENCE_CONFIRMED_WITH_CAVEAT

## Issue routing
- Tester reports go to HeraldLab/OpenclawQA first.
- Confirmed bugs are deduped before upstream filing.
- Only validated product bugs get filed/commented upstream in openclaw/openclaw.

Output style:
- Be concrete and tester-executable.
- Avoid vague “test this feature” wording.
- Prefer tables/checklists.
- Include NOT_ENOUGH_INFO where release/commit data is missing.
- Do not invent behavior not supported by release notes, commits, or diff evidence.
```

## Why this prompt exists

The QA goal is commit-aware manual validation. A release can have green automated checks and still fail in install/update flows, provider routing, real Discord/Telegram delivery, plugin/tool injection, persistence, permissions, or user-visible error handling.
