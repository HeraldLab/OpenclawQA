# OpenClaw QA

Public release QA runs and tester reports for OpenClaw alpha/beta validation.

This repo is the public system of record for Herald Labs OpenClaw testing:

1. A new OpenClaw alpha/beta tag appears.
2. A run folder is created under `runs/<tag>/`.
3. Agents generate a freshness report, QA checklist, and tester instructions.
4. Testers submit reports through GitHub Issues.
5. Maintainers review submitted evidence end-to-end, including full screen recordings.
6. Validated bugs are deduped and filed upstream into `openclaw/openclaw`.
7. Each run closes with a public closeout report.

## Current Runs

| Tag | Status | Folder | Instructions | Closeout |
|---|---|---|---|---|
| `v2026.6.1-beta.1` | manual_qa_dispatched_to_correct_mariam_thread_pending_report | [folder](runs/v2026.6.1-beta.1/) | [instructions](runs/v2026.6.1-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.1/closeout-report.md) |
| `v2026.6.1-beta.2` | beta2_dispatched_to_mariam_anny_ayomide_pending_reports | [folder](runs/v2026.6.1-beta.2/) | [instructions](runs/v2026.6.1-beta.2/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.2/closeout-report.md) |
| `v2026.6.1-beta.3` | targeted_dispatch_two_threads_evidence_collection | [folder](runs/v2026.6.1-beta.3/) | [instructions](runs/v2026.6.1-beta.3/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.3/closeout-report.md) |

## Tester Flow

- Open the run folder for the target tag.
- Read `tester-instructions.md`.
- Screen-record the manual QA session end-to-end where possible.
- Submit a tester report issue using the appropriate issue template.
- Include logs, screenshots, and recording links where possible.
- Reply in the assigned Discord thread with the GitHub issue link.

## Maintainer Flow

- Use `scripts/create-run.py <tag>` to create or refresh a run folder.
- Use `scripts/fetch-openclaw-release-context.py <tag>` for freshness context.
- Use `templates/release-qa-generation-prompt.md` to generate a commit-aware human QA checklist from the release notes, compare diff, commits, PRs, and issue signals.
- Reject generic/copy-pasted packets with `docs/release-checklist-quality-rubric.md`; P0 smoke is required but not sufficient.
- Use `scripts/collect-reports.py <tag>` to summarize tester reports.
- Use `scripts/review-evidence-video.py --video <local-video> --tag <tag> --tester <handle> --issue <issue-url>` or `docs/evidence-review-workflow.md` to review evidence end-to-end before accepting a report.
- Use `scripts/dedupe-upstream-issues.py <tag>` before filing upstream.
- Use `scripts/file-upstream-issues.py <tag> --dry-run` before first live filing.

## Privacy

Do not commit secrets, private tokens, private Entity URLs, or unsanitized logs. If evidence contains private data, summarize it publicly and keep the raw artifact internal.
