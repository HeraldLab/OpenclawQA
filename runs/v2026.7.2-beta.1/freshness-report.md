# Freshness Report

Target tag: `v2026.7.2-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-07-15T19:00:22Z`

Latest beta tag: `v2026.7.2-beta.1`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.7.1`

Prior prerelease baseline: `v2026.7.1-beta.6`

## Recent issue signals

- #108427 [no-labels] cron: retention deletes same-ID history from unrelated stores — https://github.com/openclaw/openclaw/issues/108427
- #107658 [bug, docs, P2, impact:ux-friction] [Docs Bug]: relaesa — https://github.com/openclaw/openclaw/issues/107658
- #107517 [P3, clawsweeper:not-repro-on-main, issue-rating: 🦪 silver shellfish] [Bug] Memory leak in WeakMap usage for draft progress tracking in streaming views — https://github.com/openclaw/openclaw/issues/107517
- #107550 [P3] [Performance] Thread pool starvation due to synchronous crypto hashing in password validation — https://github.com/openclaw/openclaw/issues/107550
- #107520 [P2, impact:data-loss, issue-rating: 🦪 silver shellfish] [Bug] Race condition on event-ledger log rotation under high concurrent load — https://github.com/openclaw/openclaw/issues/107520
- #107531 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, impact:security, issue-rating: 🦪 silver shellfish] [Security] Privilege escalation via mock environment overrides in testing framework — https://github.com/openclaw/openclaw/issues/107531
- #107502 [P3] [Performance] Inefficient serialization in src/agents/transcript-writer.ts blocks Event Loop — https://github.com/openclaw/openclaw/issues/107502
- #107495 [P3] [Bug] Subagent configuration overrides are ignored in plugin-tools-handlers.ts — https://github.com/openclaw/openclaw/issues/107495
- #107496 [P3] [Performance] Re-evaluating regex matching in status-message.ts for every active socket message — https://github.com/openclaw/openclaw/issues/107496
- #107347 [P0, impact:ux-release-blocker] [Bug]: @qingchencloud/openclaw-zh@2026.7.1-zh.1 包含 workspace:* 协议依赖，导致 npm install EUNSUPPORTEDPROTOCOL — https://github.com/openclaw/openclaw/issues/107347
- #106722 [P3] [Refactor] Unify error boundary and fallback stack behavior for provider routing — https://github.com/openclaw/openclaw/issues/106722
- #106716 [P3] [Performance] Inefficient provider capability negotiation causes O(n*m) routing delay — https://github.com/openclaw/openclaw/issues/106716
- #106715 [P3, impact:security] [Security] SSRF vulnerability in remote manifest resolution for external plugins — https://github.com/openclaw/openclaw/issues/106715
- #106709 [P3] [Architecture] Split gateway protocol into distinct inbound/outbound schema validation boundaries — https://github.com/openclaw/openclaw/issues/106709
- #106687 [P2, impact:crash-loop] [Bug] Hook injection payload size limit bypass in host-hook-state.ts — https://github.com/openclaw/openclaw/issues/106687
- #106679 [P2, impact:auth-provider, impact:crash-loop] [Bug] Infinite fallback loop on generic provider errors — https://github.com/openclaw/openclaw/issues/106679
- #106674 [P2, impact:security] [Security] Exposure of sensitive environment variables in crash dumps — https://github.com/openclaw/openclaw/issues/106674
- #106675 [P2, impact:other] [Performance] Memory leak in continuous conversation streams via embedded agent — https://github.com/openclaw/openclaw/issues/106675
- #106669 [P2, impact:crash-loop] [Bug] Unbounded memory growth in context-engine caching — https://github.com/openclaw/openclaw/issues/106669
- #106646 [P3] [Bug] Module-level cache with no invalidation path in config-presence.ts — https://github.com/openclaw/openclaw/issues/106646
- #106626 [P2, impact:security] [Security] Prototype Pollution Risk in interactive-state.ts Payload Parsing — https://github.com/openclaw/openclaw/issues/106626

## Recent PR signals

- PR #108418 draft=False fix(release): propagate frozen-target guard and retry live timeouts — https://github.com/openclaw/openclaw/pull/108418
- PR #108420 draft=False ci: stabilize release validation tests — https://github.com/openclaw/openclaw/pull/108420
- PR #108416 draft=False refactor(plugins): split plugin type contracts — https://github.com/openclaw/openclaw/pull/108416
- PR #108283 draft=False fix: channel turns recover safely after gateway restart — https://github.com/openclaw/openclaw/pull/108283
- PR #108426 draft=False fix(gateway): cloud session resumes after gateway restart — https://github.com/openclaw/openclaw/pull/108426
- PR #107676 draft=False fix: check channel health after startup grace — https://github.com/openclaw/openclaw/pull/107676
- PR #107623 draft=False fix(codex): reject hex/exponent computer wait duration strings — https://github.com/openclaw/openclaw/pull/107623
- PR #85583 draft=False Control-plane hardening from Optimus ops findings — https://github.com/openclaw/openclaw/pull/85583
- PR #108386 draft=False improve(ci): speed warm Node shards with sticky bind mount — https://github.com/openclaw/openclaw/pull/108386
- PR #107811 draft=False test(nextcloud-talk): type replay response mock — https://github.com/openclaw/openclaw/pull/107811
- PR #104027 draft=False chore(deps): bump the actions group across 1 directory with 14 updates — https://github.com/openclaw/openclaw/pull/104027
- PR #107735 draft=False fix(heartbeat): stop reporting success after tool failures — https://github.com/openclaw/openclaw/pull/107735
- PR #108425 draft=False feat: add Browser Use CLI skill — https://github.com/openclaw/openclaw/pull/108425
- PR #108424 draft=False refactor(agents): split agent command orchestration — https://github.com/openclaw/openclaw/pull/108424
- PR #108220 draft=False test(state): regression test — operator-approval migration must not nest a raw BEGIN — https://github.com/openclaw/openclaw/pull/108220
- PR #108423 draft=True fix: gateway-owned work fails through same-host relay — https://github.com/openclaw/openclaw/pull/108423
- PR #86655 draft=False feat(claude): add claude-bridge app-server harness extension — https://github.com/openclaw/openclaw/pull/86655
- PR #108305 draft=False test(agents): register session lock helpers in vitest workers — https://github.com/openclaw/openclaw/pull/108305
- PR #108422 draft=False refactor(ui): split app sidebar responsibilities — https://github.com/openclaw/openclaw/pull/108422
- PR #102594 draft=False fix(slack): include canonical session transcript in prompt context (extends #95390) — https://github.com/openclaw/openclaw/pull/102594
- PR #108419 draft=False refactor(cli): split capability commands by domain — https://github.com/openclaw/openclaw/pull/108419
- PR #108392 draft=False fix(acp): skip unsupported automatic thinking config in manager gate — https://github.com/openclaw/openclaw/pull/108392
- PR #107879 draft=False feat(ios): unify chat and voice experience — https://github.com/openclaw/openclaw/pull/107879
- PR #103371 draft=False fix(qqbot): require own account credential entries — https://github.com/openclaw/openclaw/pull/103371
- PR #105887 draft=False fix(deepinfra): apply request policy to video generation requests — https://github.com/openclaw/openclaw/pull/105887
- PR #97280 draft=False fix(auth): allow OpenAI OAuth for audio transcription — https://github.com/openclaw/openclaw/pull/97280
- PR #107366 draft=False fix(acp): keep completed run-mode sessions resumable — https://github.com/openclaw/openclaw/pull/107366
- PR #77158 draft=False perf(qmd): persistent export-state cache + stat fast path in exportSessions — https://github.com/openclaw/openclaw/pull/77158
- PR #108404 draft=False fix(anthropic): honor server Retry-After on rate-limited turns (#103849) — https://github.com/openclaw/openclaw/pull/108404
- PR #104862 draft=False fix(sms): ack rate-limited Twilio callbacks instead of dropping them [AI] — https://github.com/openclaw/openclaw/pull/104862
