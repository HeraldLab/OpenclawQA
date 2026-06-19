# Freshness Report

Target tag: `v2026.6.9-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-06-19T06:00:29Z`

Latest beta tag: `v2026.6.9-beta.1`

Latest alpha tag: `v2026.6.19-alpha.1`

Stable baseline: `v2026.6.8`

Prior prerelease baseline: `v2026.6.8-beta.2`

## Recent issue signals

- #88955 [bug, regression, P1, clawsweeper:no-new-fix-pr, clawsweeper:linked-pr-open, clawsweeper:needs-live-repro, impact:message-loss, issue-rating: 🐚 platinum hermit] [Bug]: qqbot WebSocket reconnection causes "Outbound not configured for channel: qqbot" error — https://github.com/openclaw/openclaw/issues/88955
- #88954 [bug, stale, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:linked-pr-open, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit, impact:other] [Bug]: openclaw update --channel beta cmd couldn't get v2026.3.30 beta 4 — https://github.com/openclaw/openclaw/issues/88954
- #88951 [bug, bug:behavior, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-info, impact:session-state, impact:message-loss, issue-rating: 🦪 silver shellfish] [Bug]: Duplicate message content — https://github.com/openclaw/openclaw/issues/88951
- #88920 [stale, P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:linked-pr-open, issue-rating: 🌊 off-meta tidepool] docs: add Third-party UIs section to documentation (deepclaw-ui) — https://github.com/openclaw/openclaw/issues/88920
- #88909 [P3, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:other] NSUserDefaults warning: app passes own bundle identifier as suite name — https://github.com/openclaw/openclaw/issues/88909
- #88907 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:message-loss, impact:auth-provider, issue-rating: 🐚 platinum hermit] Chronic agent failures on Telegram — LLM timeouts before configured timeout + silent incomplete turns + dead fallbacks (OpenRouter/DeepSeek+V4-Flash, v2026.5.28) — https://github.com/openclaw/openclaw/issues/88907

## Recent PR signals

- PR #94760 draft=False [Bug] Fix Feishu p2p DM replies fail with SUBSCRIPTION_NOT_FOUND (fixes #83730) — https://github.com/openclaw/openclaw/pull/94760
- PR #88992 draft=False fix: recover stranded replies in message_tool_only mode (#85714) — https://github.com/openclaw/openclaw/pull/88992
- PR #94561 draft=False Add stdout diagnostics OTEL log exporter — https://github.com/openclaw/openclaw/pull/94561
- PR #74235 draft=False fix(googlechat): preserve thread reply target through delivery — https://github.com/openclaw/openclaw/pull/74235
- PR #89291 draft=False test(plugins): cover filtered bundle MCP servers — https://github.com/openclaw/openclaw/pull/89291
- PR #94812 draft=False test(perf): compare saved CLI startup benchmarks — https://github.com/openclaw/openclaw/pull/94812
- PR #88988 draft=False feat(status): show session duration in footer — https://github.com/openclaw/openclaw/pull/88988
- PR #94817 draft=False fix(ollama): treat undefined reasoning as potentially reasoning-capable — https://github.com/openclaw/openclaw/pull/94817
- PR #88980 draft=False fix(telegram): gate bot-authored group messages — https://github.com/openclaw/openclaw/pull/88980
- PR #88962 draft=False fix: complete preserveKeys implementation for session maintenance — https://github.com/openclaw/openclaw/pull/88962
- PR #88959 draft=True fix(plugins): ignore throwing provider runtime hooks — https://github.com/openclaw/openclaw/pull/88959
- PR #91656 draft=False test(cron): expand parseAbsoluteTimeMs test coverage to 39 cases — https://github.com/openclaw/openclaw/pull/91656
- PR #92230 draft=False feat: add model switch choices to /model — https://github.com/openclaw/openclaw/pull/92230
- PR #94798 draft=False Respect explicit compaction reserve tokens — https://github.com/openclaw/openclaw/pull/94798
- PR #94784 draft=False fix(doctor): stop promising --fix for working isolated shell-prompt cron jobs (#94655) — https://github.com/openclaw/openclaw/pull/94784
- PR #88953 draft=False fix(exec): auto-approve recognized read-only boolean flags on default safe bins — https://github.com/openclaw/openclaw/pull/88953
- PR #88936 draft=True fix(plugins): skip broken web provider factories — https://github.com/openclaw/openclaw/pull/88936
- PR #79818 draft=False feat(slack): expand message action parity — https://github.com/openclaw/openclaw/pull/79818
- PR #84794 draft=False Clean up isolated cron sessions after runs — https://github.com/openclaw/openclaw/pull/84794
- PR #88935 draft=False fix(agent): load shared tools bootstrap instructions — https://github.com/openclaw/openclaw/pull/88935
- PR #88925 draft=False Fix stuck-session recovery aborts for active reply runs — https://github.com/openclaw/openclaw/pull/88925
- PR #94813 draft=False fix(control-ui): improve session key display for direct chats with long identifiers — https://github.com/openclaw/openclaw/pull/94813
- PR #88919 draft=False fix: allow preflight compaction to reenter session locks — https://github.com/openclaw/openclaw/pull/88919
- PR #88916 draft=True [codex] Fix Telegram active-run ingress and legacy file SecretRefs — https://github.com/openclaw/openclaw/pull/88916
- PR #88908 draft=False fix(gateway): force exit on zombie shutdown + 503 healthz during shutdown — https://github.com/openclaw/openclaw/pull/88908
- PR #94680 draft=False fix(line): prevent silent message loss via retry, batch push, loading keepalive (#86012) — https://github.com/openclaw/openclaw/pull/94680
- PR #88905 draft=False feat(dreaming): expose shadow-trial scoring in reports — https://github.com/openclaw/openclaw/pull/88905
- PR #88899 draft=False fix(android): widen chat bubbles and render markdown consistently — https://github.com/openclaw/openclaw/pull/88899
- PR #88898 draft=False fix(reply): also drop tool-error progress payloads under messages.suppressToolErrors — https://github.com/openclaw/openclaw/pull/88898
- PR #94733 draft=False fix(telegram): honor ingest config before skipping unaddressed group media — https://github.com/openclaw/openclaw/pull/94733
