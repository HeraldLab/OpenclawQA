# Freshness Report

Target tag: `v2026.7.1-beta.5`

Target exists upstream: **yes**

Fetched at: `2026-07-11T11:00:35Z`

Latest beta tag: `v2026.7.1-beta.5`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.6.11`

Prior prerelease baseline: `v2026.7.1-beta.2`

## Recent issue signals

- #104413 [no-labels] askFallback=deny not honored: exec allowlist miss with no approver hangs silently until ~600s abort (2026.7.1-beta.2) — https://github.com/openclaw/openclaw/issues/104413
- #104412 [no-labels] cron: recurring jobs whose fire time falls in a gateway stop are skipped silently — one-shot --at jobs catch up, recurring jobs don't, and no missed-run signal exists — https://github.com/openclaw/openclaw/issues/104412
- #104409 [app: web-ui, maintainer] Control UI: multi-select sessions in the sidebar for batch archive/delete/group actions — https://github.com/openclaw/openclaw/issues/104409

## Recent PR signals

- PR #104319 draft=False refactor(agents): converge CLI tool terminal reason onto run-termination — https://github.com/openclaw/openclaw/pull/104319
- PR #97189 draft=False Persist gateway restart audit events — https://github.com/openclaw/openclaw/pull/97189
- PR #104366 draft=False fix(agents): propagate Retry-After from Anthropic transport to session auto-retry — https://github.com/openclaw/openclaw/pull/104366
- PR #103118 draft=False fix(web-search): align credential presence with usable providers — https://github.com/openclaw/openclaw/pull/103118
- PR #102082 draft=False fix(slack): suppress progress chrome sends — https://github.com/openclaw/openclaw/pull/102082
- PR #96513 draft=False fix(feishu): pace outbound sends per target — https://github.com/openclaw/openclaw/pull/96513
- PR #104027 draft=False chore(deps): bump the actions group across 1 directory with 14 updates — https://github.com/openclaw/openclaw/pull/104027
- PR #104420 draft=False fix(scripts): bound conflict-marker scan reads to prevent OOM on large files — https://github.com/openclaw/openclaw/pull/104420
- PR #104364 draft=False fix(msteams): detect provider-prefixed target ids — https://github.com/openclaw/openclaw/pull/104364
- PR #104419 draft=False fix(agents): keep exec finalization suspension-safe — https://github.com/openclaw/openclaw/pull/104419
- PR #102429 draft=False fix: prevent operational notices from leaking to source chats — https://github.com/openclaw/openclaw/pull/102429
- PR #104418 draft=False fix(release): wait for Telegram proc marker — https://github.com/openclaw/openclaw/pull/104418
- PR #104410 draft=False fix(workboard): scope default positions by board — https://github.com/openclaw/openclaw/pull/104410
- PR #104414 draft=False fix(nodes): reject malformed media payloads when base64 is invalid — https://github.com/openclaw/openclaw/pull/104414
- PR #103761 draft=False fix(line): AI-assisted - requireMention can now optionally gate non-text messages with bounded pending-media retention — https://github.com/openclaw/openclaw/pull/103761
- PR #104373 draft=False chore(ui): refresh control ui locales — https://github.com/openclaw/openclaw/pull/104373
- PR #104417 draft=False perf(ci): use source performance build profile — https://github.com/openclaw/openclaw/pull/104417
- PR #104393 draft=False fix(ui): adapt background-tasks rail to narrow panes — https://github.com/openclaw/openclaw/pull/104393
- PR #103534 draft=False fix(gateway): enforce plugin-ownership check in sessions.patch — https://github.com/openclaw/openclaw/pull/103534
- PR #104416 draft=False feat(ui): multi-select sessions in the sidebar with batch menu actions — https://github.com/openclaw/openclaw/pull/104416
- PR #104401 draft=False feat(gateway): durable cloud worker environments, provider SDK contract, and lifecycle RPCs — https://github.com/openclaw/openclaw/pull/104401
- PR #103728 draft=False fix(memory): skip blank search provider bootstrap — https://github.com/openclaw/openclaw/pull/103728
- PR #104218 draft=False fix(imessage): apply authoritative projection in anchorless recovery — https://github.com/openclaw/openclaw/pull/104218
- PR #103562 draft=False fix(discord): retry reply session init conflicts to prevent silent message loss — https://github.com/openclaw/openclaw/pull/103562
- PR #104149 draft=False fix(agents): honor Anthropic Retry-After in auto-retry backoff (#103849) — https://github.com/openclaw/openclaw/pull/104149
- PR #89442 draft=False fix(codex): isolated cron reports Codex startup stalls — https://github.com/openclaw/openclaw/pull/89442
- PR #103731 draft=False fix(plugins): honor empty document extractor scope — https://github.com/openclaw/openclaw/pull/103731
- PR #104216 draft=False fix(searxng): stop web search requests when runs are aborted — https://github.com/openclaw/openclaw/pull/104216
- PR #104278 draft=False fix(tasks): reset omitted lifecycle start time — https://github.com/openclaw/openclaw/pull/104278
- PR #104234 draft=False fix(process): bound Windows exec timeout cleanup — https://github.com/openclaw/openclaw/pull/104234
