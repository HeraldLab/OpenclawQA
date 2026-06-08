# Freshness Report

Target tag: `v2026.6.5-beta.5`

Target exists upstream: **yes**

Fetched at: `2026-06-08T23:00:09Z`

Latest beta tag: `v2026.6.5-beta.5`

Latest alpha tag: `v2026.6.8-alpha.1`

Stable baseline: `v2026.6.1`

Prior prerelease baseline: `v2026.6.5-beta.3`

## Recent issue signals

- #91522 [no-labels] member-info fails with "fetch failed" on WSL2 in 2026.6.1 (SSRF fetch guard / undici dispatcher regression) — https://github.com/openclaw/openclaw/issues/91522
- #91035 [bug, regression, P2, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit, impact:other] [Bug]: Build fails on v2026.6.1 — https://github.com/openclaw/openclaw/issues/91035
- #91521 [bug] [Bug]: Tailscale + Control UI Token mode cause images can't load — https://github.com/openclaw/openclaw/issues/91521
- #79223 [stale] Feature request: configurable Dream Diary language / prompt — https://github.com/openclaw/openclaw/issues/79223
- #91518 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:message-loss, issue-rating: 🐚 platinum hermit] Durable inbound receive journal for Slack channel (parity with Telegram ingress spool) — https://github.com/openclaw/openclaw/issues/91518
- #91517 [P1, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:crash-loop, issue-rating: 🦞 diamond lobster] getSubagentRunsSnapshotForRead does an uncached full SQLite re-read on every call; many consumers drive it to ~22 Hz and pin a CPU core — https://github.com/openclaw/openclaw/issues/91517
- #90083 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:auth-provider, issue-rating: 🐚 platinum hermit] [Bug]: 2026.6.1 OpenAI ChatGPT Responses transport fails with invalid_provider_content_type for gpt-5.4/gpt-5.5 — https://github.com/openclaw/openclaw/issues/90083
- #91514 [no-labels] ACP: effort config option sent to Claude Haiku causes "Unknown config option: effort" — https://github.com/openclaw/openclaw/issues/91514
- #91513 [P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:auth-provider, issue-rating: 🦞 diamond lobster] ACP: model prefix not stripped when dispatching to Claude ACP adapter — Cannot replay saved model "anthropic/claude-sonnet-4-6" — https://github.com/openclaw/openclaw/issues/91513

## Recent PR signals

- PR #83169 draft=False Discord: add reaction notification wake policy — https://github.com/openclaw/openclaw/pull/83169
- PR #90500 draft=False Fix stale session routes for removed providers — https://github.com/openclaw/openclaw/pull/90500
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #91520 draft=False fix(control-ui): show agents as a visible list instead of a dropdown — https://github.com/openclaw/openclaw/pull/91520
- PR #91519 draft=False feat(qa-lab): add Codex Slack approval scenarios — https://github.com/openclaw/openclaw/pull/91519
- PR #91478 draft=False block unauthorized Telegram DM text from prompt context — https://github.com/openclaw/openclaw/pull/91478
- PR #90666 draft=False fix(cron): cancel active cron task runs — https://github.com/openclaw/openclaw/pull/90666
- PR #88815 draft=False feat: channel echo / session pinning — https://github.com/openclaw/openclaw/pull/88815
- PR #90759 draft=False fix #76888: [Bug]: Queued/orphaned user-message merge can produce stale reply — https://github.com/openclaw/openclaw/pull/90759
- PR #89040 draft=False perf: avoid event-loop stall during embedded_run bootstrap-context — https://github.com/openclaw/openclaw/pull/89040
- PR #91499 draft=False fix(cron): preserve scheduled turn tool policy [AI] — https://github.com/openclaw/openclaw/pull/91499
- PR #85249 draft=False fix(cron): guard against undefined sourceDelivery in isolated executor — https://github.com/openclaw/openclaw/pull/85249
- PR #91515 draft=False fix(cron): classify spaced 'timed out' failures as retryable timeout — https://github.com/openclaw/openclaw/pull/91515
- PR #88796 draft=False fix(discord): resolve guildId from session channel for search actions — https://github.com/openclaw/openclaw/pull/88796
- PR #83988 draft=False fix(tts): defer text settlement for final-mode TTS to eliminate churn (#83511) — https://github.com/openclaw/openclaw/pull/83988
- PR #91010 draft=False fix(memory): honor local model path in index identity — https://github.com/openclaw/openclaw/pull/91010
- PR #90035 draft=False fix(sqlite): support Node 23.0–23.10 runtimes lacking StatementSync.columns() — https://github.com/openclaw/openclaw/pull/90035
- PR #82955 draft=False fix(install): validate downloaded scripts before execution — https://github.com/openclaw/openclaw/pull/82955
- PR #91507 draft=False Canonicalize Codex protocol JSON asset ordering — https://github.com/openclaw/openclaw/pull/91507
- PR #86649 draft=False fix: relay Claude CLI assistant partial messages as streaming deltas — https://github.com/openclaw/openclaw/pull/86649
- PR #91080 draft=False feat(gateway): startup watchdog dumps in-flight phases on hang — https://github.com/openclaw/openclaw/pull/91080
- PR #91509 draft=False Update Google Meet chrome-node invoke policy [AI] — https://github.com/openclaw/openclaw/pull/91509
- PR #90060 draft=False fix(edit): preserve unrelated lines during fuzzy text matching — https://github.com/openclaw/openclaw/pull/90060
- PR #91511 draft=False fix(ui): keep mobile composer above keyboard — https://github.com/openclaw/openclaw/pull/91511
- PR #91510 draft=False Add claw score taxonomy — https://github.com/openclaw/openclaw/pull/91510
- PR #89517 draft=True [codex] fix gateway hot-mode restart reloads — https://github.com/openclaw/openclaw/pull/89517
- PR #91408 draft=False feat(channels/acp): support ACP bindings for direct-message peers — https://github.com/openclaw/openclaw/pull/91408
- PR #89526 draft=True [codex] fix gateway restart-required reload drift — https://github.com/openclaw/openclaw/pull/89526
- PR #91452 draft=False Add claw-score agent skill — https://github.com/openclaw/openclaw/pull/91452
- PR #56674 draft=False feat(openresponses): return reasoning/thinking content in /v1/responses output — https://github.com/openclaw/openclaw/pull/56674
