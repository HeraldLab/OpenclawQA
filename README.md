# OpenClaw QA

Public release QA runs and tester reports for OpenClaw alpha/beta validation.

This repo is the public system of record for Herald Labs OpenClaw testing:

1. A new OpenClaw alpha/beta tag appears.
2. A run folder is created under `runs/<tag>/`.
3. Agents generate a freshness report, QA checklist, and tester instructions.
4. Testers submit reports through GitHub Issues.
5. Validated bugs are deduped and filed upstream into `openclaw/openclaw`.
6. Each run closes with a public closeout report.

## Current Runs

| Tag | Status | Folder | Instructions | Closeout |
|---|---|---|---|---|
| `v2026.6.1-beta.1` | manual_qa_dispatched_to_correct_mariam_thread_pending_report | [folder](runs/v2026.6.1-beta.1/) | [instructions](runs/v2026.6.1-beta.1/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.1/closeout-report.md) |
| `v2026.6.1-beta.2` | beta2_dispatched_to_mariam_anny_ayomide_pending_reports | [folder](runs/v2026.6.1-beta.2/) | [instructions](runs/v2026.6.1-beta.2/tester-instructions.md) | [closeout](runs/v2026.6.1-beta.2/closeout-report.md) |

## Tester Flow

- Open the run folder for the target tag.
- Read `tester-instructions.md`.
- Screen-record the manual QA session.
- Submit a tester report issue using the appropriate issue template.
- Include logs, screenshots, and recording links where possible.

## Maintainer Flow

- Use `scripts/create-run.py <tag>` to create or refresh a run folder.
- Use `scripts/fetch-openclaw-release-context.py <tag>` for freshness context.
- Use `scripts/collect-reports.py <tag>` to summarize tester reports.
- Use `scripts/dedupe-upstream-issues.py <tag>` before filing upstream.
- Use `scripts/file-upstream-issues.py <tag> --dry-run` before first live filing.

## Privacy

Do not commit secrets, private tokens, private Entity URLs, or unsanitized logs. If evidence contains private data, summarize it publicly and keep the raw artifact internal.
