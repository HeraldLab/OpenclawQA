# OpenClaw QA

Public release QA runs and tester reports for OpenClaw alpha/beta validation.

This repo is the public system of record for Herald Labs **manual human QA** of OpenClaw.

Core rule: **human QA is the release gate; automation is support/preflight.**

1. A new OpenClaw alpha/beta tag appears.
2. A run folder is created under `runs/<tag>/`.
3. Automation gathers release context: release notes, commits, PRs, issue signals.
4. QA coordinator creates a manual human QA packet with named tester/reviewer assignments.
5. Human testers manually run baseline and release-delta scenarios.
6. Testers submit GitHub reports with evidence and human judgment notes.
7. Human reviewers review submitted evidence end-to-end, including full screen recordings for workflow scenarios.
8. Validated bugs are deduped and filed upstream into `openclaw/openclaw`.
9. Each run closes with a human-centered closeout report: confidence, confusion/trust findings, missing coverage, waivers, and blockers.

## Current Runs

| Tag | Status | Folder | Instructions | Closeout |
|---|---|---|---|---|
| `v2026.6.1-beta.1` | manual_qa_dispatched_to_correct_mariam_thread_pending_report | [folder](runs/v2026.6.1-beta.1/) | [instructions](runs/v2026.6.1-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.1/closeout-report.md) |
| `v2026.6.1-beta.2` | beta2_dispatched_to_mariam_anny_ayomide_pending_reports | [folder](runs/v2026.6.1-beta.2/) | [instructions](runs/v2026.6.1-beta.2/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.2/closeout-report.md) |
| `v2026.6.1-beta.3` | instructions_ready | [folder](runs/v2026.6.1-beta.3/) | [instructions](runs/v2026.6.1-beta.3/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.3/closeout-report.md) |
| `v2026.6.2-beta.1` | review_ready_with_caveats_not_dispatched | [folder](runs/v2026.6.2-beta.1/) | [instructions](runs/v2026.6.2-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.2-beta.1/closeout-report.md) |
| `v2026.6.5-beta.1` | review_ready_pending_approval | [folder](runs/v2026.6.5-beta.1/) | [instructions](runs/v2026.6.5-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.5-beta.1/closeout-report.md) |
| `v2026.6.5-beta.2` | closed_initial_dry_run | [folder](runs/v2026.6.5-beta.2/) | [instructions](runs/v2026.6.5-beta.2/tester-instructions.md) | [closeout](runs/v2026.6.5-beta.2/closeout-report.md) |
| `v2026.6.5-beta.3` | closed_initial_dry_run | [folder](runs/v2026.6.5-beta.3/) | [instructions](runs/v2026.6.5-beta.3/tester-instructions.md) | [closeout](runs/v2026.6.5-beta.3/closeout-report.md) |
| `v2026.6.5-beta.5` | closed_initial_dry_run | [folder](runs/v2026.6.5-beta.5/) | [instructions](runs/v2026.6.5-beta.5/tester-instructions.md) | [closeout](runs/v2026.6.5-beta.5/closeout-report.md) |
| `v2026.6.5-beta.6` | review_ready_with_caveats | [folder](runs/v2026.6.5-beta.6/) | [instructions](runs/v2026.6.5-beta.6/tester-instructions.md) | [closeout](runs/v2026.6.5-beta.6/closeout-report.md) |
| `v2026.6.6-beta.1` | closed_initial_dry_run | [folder](runs/v2026.6.6-beta.1/) | [instructions](runs/v2026.6.6-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.6-beta.1/closeout-report.md) |
| `v2026.6.6-beta.2` | closed_initial_dry_run | [folder](runs/v2026.6.6-beta.2/) | [instructions](runs/v2026.6.6-beta.2/tester-instructions.md) | [closeout](runs/v2026.6.6-beta.2/closeout-report.md) |
| `v2026.6.7-beta.1` | closed_initial_dry_run | [folder](runs/v2026.6.7-beta.1/) | [instructions](runs/v2026.6.7-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.7-beta.1/closeout-report.md) |
| `v2026.6.8-beta.1` | closed_initial_dry_run | [folder](runs/v2026.6.8-beta.1/) | [instructions](runs/v2026.6.8-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.8-beta.1/closeout-report.md) |
| `v2026.6.8-beta.2` | closed_initial_dry_run | [folder](runs/v2026.6.8-beta.2/) | [instructions](runs/v2026.6.8-beta.2/tester-instructions.md) | [closeout](runs/v2026.6.8-beta.2/closeout-report.md) |

## Tester Flow

- Start with the [OpenClaw setup guide](docs/openclaw-setup-guide.md) if this is your first install, upgrade, or channel setup.
- Open the run folder for the target tag.
- Read `tester-instructions.md`.
- Screen-record the manual QA session end-to-end where possible.
- Submit a tester report issue using the appropriate issue template.
- Include logs, screenshots, and recording links where possible.
- Reply in the assigned Discord thread with the GitHub issue link.

## Maintainer Flow

- Use `scripts/create-run.py <tag>` to create or refresh a run folder.
- Use `scripts/fetch-openclaw-release-context.py <tag>` for freshness context.
- Use `docs/openclaw-setup-guide.md` for first-install, upgrade, Discord/Telegram setup, common blocker, and FAQ guidance derived from the Herald Labs tester threads.
- Use `docs/human-qa-layer-v1-research-and-feedback.md` with testers so they understand the problem, V1, official issue research, and where their feedback can improve the process.
- Use `docs/manual-human-qa-operating-model.md` as the release operating model: named humans, manual execution, evidence review, waiver policy, human-centered closeout.
- Use `docs/baseline-human-qa-checklist.md` for always-run Baseline P0/P1 manual QA.
- Use `docs/release-delta-qa-policy.md` to generate release-specific Delta P0/P1/P2 manual QA from the actual release changes.
- Use `templates/release-qa-generation-prompt.md` to generate a commit-aware human QA checklist from the release notes, compare diff, commits, PRs, and issue signals.
- Use `docs/human-qaqc-testing-playbook.md` so tester packets are hands-on manual QA scenarios, not automated command checks.
- Pull concrete channel/plugin/provider/state/error cards from `docs/human-scenario-library.md`; do not invent shallow “test it works” rows.
- Reject generic/copy-pasted packets with `docs/release-checklist-quality-rubric.md`; P0 smoke is required but not sufficient.
- Use `scripts/collect-reports.py <tag>` to summarize tester reports.
- Use `scripts/review-evidence-video.py --video <local-video> --tag <tag> --tester <handle> --issue <issue-url>` or `docs/evidence-review-workflow.md` to review evidence end-to-end before accepting a report.
- Use `scripts/dedupe-upstream-issues.py <tag>` before filing upstream.
- Use `scripts/file-upstream-issues.py <tag> --dry-run` before first live filing.

## Privacy

Do not commit secrets, private tokens, private Entity URLs, or unsanitized logs. If evidence contains private data, summarize it publicly and keep the raw artifact internal.
