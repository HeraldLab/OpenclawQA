# Freshness Report

Target tag: `v2026.6.8-beta.2`

Target exists upstream: **yes**

Fetched at: `2026-06-16T02:01:01Z`

Latest beta tag: `v2026.6.8-beta.2`

Latest alpha tag: `v2026.6.15-alpha.1`

Stable baseline: `v2026.6.6`

Prior prerelease baseline: `v2026.6.8-beta.1`

## Recent issue signals

- #29387 [bug, P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, issue-rating: 🦞 diamond lobster] [Bug]: Bootstrap files in agentDir are silently ignored — only workspace directory files are injected into system prompt — https://github.com/openclaw/openclaw/issues/29387
- #25574 [P1, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, impact:crash-loop, issue-rating: 🦞 diamond lobster] [Bug]: Config warnings logged repeatedly on every reload, spamming error log with thousands of duplicates — https://github.com/openclaw/openclaw/issues/25574
- #23353 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, impact:auth-provider, issue-rating: 🦞 diamond lobster] [Feature]: Support Anthropic native server-side tools (web_search, web_fetch, code_execution) — https://github.com/openclaw/openclaw/issues/23353
- #22358 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature Request] Post-subagent completion extension hook — https://github.com/openclaw/openclaw/issues/22358
- #20756 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, issue-rating: 🦞 diamond lobster] message tool should auto-select the only enabled account — https://github.com/openclaw/openclaw/issues/20756
- #17840 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: opt-in reaction-triggered agent turns — https://github.com/openclaw/openclaw/issues/17840
- #15032 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] Feature: Per-spawn tool restrictions for sub-agents — https://github.com/openclaw/openclaw/issues/15032
- #14747 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:other] Feature request: configurable lane wait diagnostic threshold — https://github.com/openclaw/openclaw/issues/14747
- #14629 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Output sanitizer: improve duplicate detection for same-line and partial duplicates — https://github.com/openclaw/openclaw/issues/14629
- #83954 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:auth-provider, issue-rating: 🐚 platinum hermit] Document/support a Pro-plan path for gpt-5.5-pro and retired Spark via Codex CLI/app-server — https://github.com/openclaw/openclaw/issues/83954

## Recent PR signals

- PR #93072 draft=False fix(sessions): preserve titles on release upsert — https://github.com/openclaw/openclaw/pull/93072
- PR #24661 draft=True feat: Provider/Cohere onboarding + auth-choice support — https://github.com/openclaw/openclaw/pull/24661
- PR #92700 draft=False #92664: [Bug]: read tool fails to read GBK-encoded text files on Chinese Windows (displays garbled text) — https://github.com/openclaw/openclaw/pull/92700
- PR #93461 draft=False fix: add compact mode to cron list tool — https://github.com/openclaw/openclaw/pull/93461
- PR #39386 draft=True fix(gateway): forward child session node events to spawnedBy subscribers — https://github.com/openclaw/openclaw/pull/39386
- PR #39245 draft=False fix(agents): normalize mangled tool names and IDs from OpenAI-compati… — https://github.com/openclaw/openclaw/pull/39245
- PR #93282 draft=False fix: trust all ClawHub channel types when package matches official catalog — https://github.com/openclaw/openclaw/pull/93282
- PR #36630 draft=False fix(signal): complete bidirectional quote-reply support — https://github.com/openclaw/openclaw/pull/36630
- PR #18778 draft=True Discord: Discord canvas! — https://github.com/openclaw/openclaw/pull/18778
- PR #12581 draft=False feat(hooks): emit session prune lifecycle event — https://github.com/openclaw/openclaw/pull/12581
- PR #93267 draft=False fix(session-memory): skip delivery-mirror entries and dedup consecutive identical assistant messages (#92563) — https://github.com/openclaw/openclaw/pull/93267
- PR #92945 draft=False #92944: Telegram commands can remain empty after interrupted sync due to stale local command hash — https://github.com/openclaw/openclaw/pull/92945
- PR #93371 draft=False fix(memory): keep recalled memory out of user prompts — https://github.com/openclaw/openclaw/pull/93371
- PR #93460 draft=False fix(cli): honor --log-level in route-first commands — https://github.com/openclaw/openclaw/pull/93460
- PR #92813 draft=False fix(state): refuse chmod-less agent database volumes that cannot prove credential privacy — https://github.com/openclaw/openclaw/pull/92813
- PR #93459 draft=False fix(discord): resolve guildId from channel info for search actions (fixes #88790) — https://github.com/openclaw/openclaw/pull/93459
- PR #90167 draft=False fix(plugins): resolve config env vars for runtime loads — https://github.com/openclaw/openclaw/pull/90167
- PR #88968 draft=False fix: prevent memory flush failure from aborting user reply (#85645) — https://github.com/openclaw/openclaw/pull/88968
- PR #28081 draft=False doctor(config): auto-prune removed google-antigravity-auth entries — https://github.com/openclaw/openclaw/pull/28081
- PR #93458 draft=True feat(telegram): accept structured spec in rich message — https://github.com/openclaw/openclaw/pull/93458
- PR #89038 draft=False fix: skip setup-only channel plugins in outbound resolution and drain pending deliveries on qqbot reconnect — https://github.com/openclaw/openclaw/pull/89038
- PR #92877 draft=False fix(usage): make built-in footer easier to wrap on Telegram — https://github.com/openclaw/openclaw/pull/92877
- PR #85643 draft=False fix(sessions): honor explicit default model pins — https://github.com/openclaw/openclaw/pull/85643
- PR #89762 draft=False feat(messages): config-level default for responseUsage (persistent /usage footer) — https://github.com/openclaw/openclaw/pull/89762
- PR #89123 draft=False refactor: route transcript writers through session seam — https://github.com/openclaw/openclaw/pull/89123
- PR #93007 draft=False feat(gateway): forward web_search_options through OpenAI-compatible chat completions — https://github.com/openclaw/openclaw/pull/93007
- PR #92686 draft=True feat(agents): add stable A2A session metadata — https://github.com/openclaw/openclaw/pull/92686
- PR #92682 draft=False fix(read): use system encoding fallback for non-UTF-8 text files on Windows — https://github.com/openclaw/openclaw/pull/92682
- PR #90579 draft=False fix: allow trusted host-read html after outbound staging — https://github.com/openclaw/openclaw/pull/90579
- PR #92676 draft=False feat: Rate-limit fallback user-visible error notification (message-lifecycle Phase 2 extension) — https://github.com/openclaw/openclaw/pull/92676
