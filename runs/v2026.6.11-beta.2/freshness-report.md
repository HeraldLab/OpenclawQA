# Freshness Report

Target tag: `v2026.6.11-beta.2`

Target exists upstream: **yes**

Fetched at: `2026-06-28T23:30:15Z`

Latest beta tag: `v2026.6.11-beta.2`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.6.10`

Prior prerelease baseline: `v2026.6.11-beta.1`

## Recent issue signals

- #97588 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, impact:message-loss, impact:crash-loop, issue-rating: 🐚 platinum hermit, maturity:stable] Lane starvation: wedged model_call lane starves all sibling agent lanes (no preemption, no heartbeat alert) — https://github.com/openclaw/openclaw/issues/97588
- #97589 [no-labels] [Feature]: Per-message sender identity for multi-agent sessions — https://github.com/openclaw/openclaw/issues/97589

## Recent PR signals

- PR #97587 draft=False fix(google): bound OAuth project and token JSON response reads — https://github.com/openclaw/openclaw/pull/97587
- PR #97034 draft=False fix(session-memory): strip orphan plain-text role lines from session-memory transcripts — https://github.com/openclaw/openclaw/pull/97034
- PR #74185 draft=False fix(infra): wrap provider auth resolution in timeout for status --usage --json — https://github.com/openclaw/openclaw/pull/74185
- PR #73399 draft=False fix(feishu): carry forward DM fallback and topic labels — https://github.com/openclaw/openclaw/pull/73399
- PR #67433 draft=False feat(hooks): add waitForResult mode to POST /hooks/agent endpoint — https://github.com/openclaw/openclaw/pull/67433
- PR #97551 draft=False fix(proxy-capture): bound captured response bodies to prevent OOM — https://github.com/openclaw/openclaw/pull/97551
- PR #97548 draft=False improve(qa-lab): bound Discord API response reads in mantis smoke — https://github.com/openclaw/openclaw/pull/97548
- PR #89794 draft=True fix(gateway): guard plugin UI descriptors — https://github.com/openclaw/openclaw/pull/89794
- PR #90226 draft=False [AI-assisted] Preserve thread sessions across daily reset by default — https://github.com/openclaw/openclaw/pull/90226
- PR #97549 draft=False fix(cli): bound in-memory video download from provider URLs — https://github.com/openclaw/openclaw/pull/97549
- PR #95416 draft=False fix(inworld): bound TTS audio, voices, and error response reads to prevent OOM — https://github.com/openclaw/openclaw/pull/95416
- PR #97550 draft=False fix: bound APNs relay response body so an oversized relay reply can't exhaust gateway memory — https://github.com/openclaw/openclaw/pull/97550
- PR #97566 draft=False feat: add Pioneer.ai as an inference provider with live model discovery — https://github.com/openclaw/openclaw/pull/97566
- PR #89687 draft=False fix(feishu): scope queues by topic sessions — https://github.com/openclaw/openclaw/pull/89687
- PR #97547 draft=False fix(qa-matrix): bound Matrix homeserver response reads to prevent OOM — https://github.com/openclaw/openclaw/pull/97547
- PR #86655 draft=False feat(claude): add claude-bridge app-server harness extension — https://github.com/openclaw/openclaw/pull/86655
- PR #92003 draft=False fix(webchat): recover session after stop — https://github.com/openclaw/openclaw/pull/92003
- PR #89040 draft=False perf: avoid event-loop stall during embedded_run bootstrap-context — https://github.com/openclaw/openclaw/pull/89040
- PR #88968 draft=False fix: prevent memory flush failure from aborting user reply (#85645) — https://github.com/openclaw/openclaw/pull/88968
- PR #97540 draft=False fix(zai): bound Z.AI endpoint-probe error body reads to prevent OOM — https://github.com/openclaw/openclaw/pull/97540
- PR #82955 draft=False fix(install): validate downloaded scripts before execution — https://github.com/openclaw/openclaw/pull/82955
- PR #97585 draft=False fix(gateway): exec approvals CLI shows clear error when node lacks approvals capability — https://github.com/openclaw/openclaw/pull/97585
- PR #82951 draft=False fix(proxy): redact sensitive headers in standalone debug proxy captures — https://github.com/openclaw/openclaw/pull/82951
- PR #82950 draft=False fix(security): add ReDoS guard to exec approval argPattern matching — https://github.com/openclaw/openclaw/pull/82950
- PR #82934 draft=False fix(media): allow SSRF bypass for gateway-localhost URLs (Feishu media fetch) — https://github.com/openclaw/openclaw/pull/82934
- PR #82906 draft=False fix(codex): gate CLI session resume behind plugin approval — https://github.com/openclaw/openclaw/pull/82906
- PR #97539 draft=False fix(signal): bound container REST reads so a hostile signal-cli-rest-api host cannot exhaust memory — https://github.com/openclaw/openclaw/pull/97539
- PR #82895 draft=True fix(slack): preserve interaction thread status — https://github.com/openclaw/openclaw/pull/82895
- PR #97584 draft=False fix(docs): Fix formatting on permissions for Discord bot — https://github.com/openclaw/openclaw/pull/97584
- PR #82894 draft=False fix(gateway): prewarm agent runtime before ready — https://github.com/openclaw/openclaw/pull/82894
