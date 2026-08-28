# Freshness Report

Target tag: `v2026.9.1-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-08-28T21:00:43Z`

Latest beta tag: `v2026.9.1-beta.1`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.7.1-2`

Prior prerelease baseline: `v2026.8.1-beta.3`

## Recent issue signals

- #75001 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Feishu @all mentions silently dropped after PR #72658 — should be handled via prompt, not API-level block — https://github.com/openclaw/openclaw/issues/75001
- #77819 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:source-repro, impact:session-state, issue-rating: 🦞 diamond lobster, impact:ux-friction] WebChat history after session reset hides archived sessions and loses image attachment display — https://github.com/openclaw/openclaw/issues/77819
- #82121 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, issue-rating: 🦞 diamond lobster] Leaked truncation sentinels (`...(truncated)...` / `[..., N more characters truncated]`) can appear in final assistant replies — https://github.com/openclaw/openclaw/issues/82121
- #71330 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool] Feature: Configurable memory promotion target file — https://github.com/openclaw/openclaw/issues/71330
- #90911 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:other] [Feature]: Record token usage on task_runs / subagent_runs (parity with cron_run_logs.total_tokens) — https://github.com/openclaw/openclaw/issues/90911
- #110896 [enhancement, maintainer, P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool, impact:other] [Feature]: System agent overhaul: shared chat UI, config change journal, durable history, agentic identity — https://github.com/openclaw/openclaw/issues/110896
- #106149 [bug, P2, impact:auth-provider, issue-rating: 🦪 silver shellfish] [Bug]: [Bug]: Embedded agent gets "401 User not found" from OpenRouter despite valid API key — https://github.com/openclaw/openclaw/issues/106149
- #132078 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:security, issue-rating: 🌊 off-meta tidepool] feat(sandbox): allow an approved Docker runtime per sandbox profile — https://github.com/openclaw/openclaw/issues/132078
- #71930 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Mattermost plugin drops post_edited events — @mentions added via edit do not trigger agent wake — https://github.com/openclaw/openclaw/issues/71930
- #85366 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:crash-loop, issue-rating: 🦞 diamond lobster] ACP startup sidecars saturate event loop on installs with many sessions — identity-reconcile + session-locks 450-460 s wall, eventLoopDelayP99 6 min — https://github.com/openclaw/openclaw/issues/85366
- #41860 [bug, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:linked-pr-open, clawsweeper:needs-live-repro, impact:message-loss, issue-rating: 🐚 platinum hermit] [Bug]: When openclaw sends a link with an underscore to Feishu, the full hyperlink cannot be displayed — https://github.com/openclaw/openclaw/issues/41860
- #84486 [P1, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, issue-rating: 🦞 diamond lobster] Bug: Text before tool calls is lost in Feishu streaming card reply mode — https://github.com/openclaw/openclaw/issues/84486
- #90573 [P2, clawsweeper:no-new-fix-pr, clawsweeper:linked-pr-open, impact:auth-provider, clawsweeper:not-repro-on-main, issue-rating: 🦪 silver shellfish] Bug: Remaining hardcoded DEFAULT_AGENT_ID="main" assumptions after PR #30654 — https://github.com/openclaw/openclaw/issues/90573
- #84110 [bug, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, impact:session-state, impact:auth-provider, issue-rating: 🦪 silver shellfish] [Bug]: Codex app-server rewrites prompt on tool-call continuation turns, busting OpenAI prompt cache mid-turn (cache ratio 93% → 47%) — https://github.com/openclaw/openclaw/issues/84110
- #111370 [bug, bug:behavior, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:crash-loop, issue-rating: 🐚 platinum hermit] [Bug]: openclaw-hooks helper processes orphaned when a run terminates abnormally — https://github.com/openclaw/openclaw/issues/111370

## Recent PR signals

- PR #132103 draft=True feat(sandbox): run workspace MCP servers in capable sandboxes — https://github.com/openclaw/openclaw/pull/132103
- PR #132097 draft=False fix(brave): bind preflight to request cancellation — https://github.com/openclaw/openclaw/pull/132097
- PR #131503 draft=False fix(cli): avoid repeated plugin preparation at startup — https://github.com/openclaw/openclaw/pull/131503
- PR #113611 draft=False fix(feishu): accept uppercase HTTPS custom domains — https://github.com/openclaw/openclaw/pull/113611
- PR #130463 draft=False fix(gateway): images sent to Claude CLI sessions show as raw cache-path links in chat history — https://github.com/openclaw/openclaw/pull/130463
- PR #132100 draft=False fix(exec): inherit configured host for per-call auto — https://github.com/openclaw/openclaw/pull/132100
- PR #128254 draft=False fix(matrix): deliver explicit reasoning notices — https://github.com/openclaw/openclaw/pull/128254
- PR #132096 draft=False fix(macos): MCP Apps stay inside the dashboard — https://github.com/openclaw/openclaw/pull/132096
- PR #131510 draft=False feat(plugins): support package-local icon assets — https://github.com/openclaw/openclaw/pull/131510
- PR #124467 draft=False refactor(qa): keep Crabline thread identity structured — https://github.com/openclaw/openclaw/pull/124467
- PR #131829 draft=False fix(ui): show Codex node approvals in the controlling chat — https://github.com/openclaw/openclaw/pull/131829
- PR #112174 draft=False fix: localized Chinese rate-limit messages skip same-model retry — https://github.com/openclaw/openclaw/pull/112174
- PR #81190 draft=False fix(agents): truncate tool results before overflow compaction — https://github.com/openclaw/openclaw/pull/81190
- PR #131465 draft=False fix(openshell): unblock hosted E2E gateway authentication — https://github.com/openclaw/openclaw/pull/131465
- PR #131569 draft=False fix(auto-reply): defer rollover for legacy pending-reset tombstones with active runs — https://github.com/openclaw/openclaw/pull/131569
- PR #131600 draft=False fix(ui): skill workshop shows success notice for unconfirmed proposal actions — https://github.com/openclaw/openclaw/pull/131600
- PR #132099 draft=False fix(doctor): preserve large media migration timestamps — https://github.com/openclaw/openclaw/pull/132099
- PR #131691 draft=False fix(cron): stop retiring one-shots whose stale guard discarded their deliverable — https://github.com/openclaw/openclaw/pull/131691
- PR #131891 draft=False feat(sessions): add graph-aware retention benchmark — https://github.com/openclaw/openclaw/pull/131891
- PR #131812 draft=False fix(webchat): hide attachment pipeline stages — https://github.com/openclaw/openclaw/pull/131812
- PR #132102 draft=False fix(webchat): announce attachment failures before long replies — https://github.com/openclaw/openclaw/pull/132102
- PR #132040 draft=False fix: keep ACP thinking aligned after model switches — https://github.com/openclaw/openclaw/pull/132040
- PR #132087 draft=False feat(codex): add scoped plugin readiness status — https://github.com/openclaw/openclaw/pull/132087
- PR #124543 draft=False fix(gateway): render Claude CLI history turns once — https://github.com/openclaw/openclaw/pull/124543
- PR #132101 draft=False chore(i18n): refresh native locales — https://github.com/openclaw/openclaw/pull/132101
- PR #127280 draft=False fix(qa): reserve Matrix no-reply cleanup budget — https://github.com/openclaw/openclaw/pull/127280
- PR #131715 draft=False feat(qa): add Convex-leased Telegram userbot proof — https://github.com/openclaw/openclaw/pull/131715
- PR #130902 draft=False improve(update): use local pnpm packages before the registry — https://github.com/openclaw/openclaw/pull/130902
- PR #131914 draft=False perf(release): pipeline full release validation — https://github.com/openclaw/openclaw/pull/131914
- PR #132091 draft=False test: overlap independent CLI build admission outcomes — https://github.com/openclaw/openclaw/pull/132091
