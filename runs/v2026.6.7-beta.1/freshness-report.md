# Freshness Report

Target tag: `v2026.6.7-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-06-13T10:00:32Z`

Latest beta tag: `v2026.6.7-beta.1`

Latest alpha tag: `v2026.6.10-alpha.2`

Stable baseline: `v2026.6.6`

Prior prerelease baseline: `v2026.6.6-beta.2`

## Recent issue signals

- #91016 [P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, impact:auth-provider, issue-rating: 🦐 gold shrimp] ⚠️ 升级 2026.6.1 后 DeepSeek Prompt Cache 完全失效，一小时烧掉约 $6 — https://github.com/openclaw/openclaw/issues/91016
- #39847 [stale, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:security, issue-rating: 🦞 diamond lobster] Echo contamination: stripInboundMetadata not called in outbound delivery pipeline — https://github.com/openclaw/openclaw/issues/39847
- #39688 [bug, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, issue-rating: 🦞 diamond lobster] [Bug]: Internal hooks (message:received, message:sent) 返回内容没有发送给用户 — https://github.com/openclaw/openclaw/issues/39688
- #54253 [bug, stale, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, impact:auth-provider, issue-rating: 🦪 silver shellfish] [Bug]: OpenClaw returns "run Error : LLM Request Failed" on RISC-V64 System. — https://github.com/openclaw/openclaw/issues/54253
- #39685 [enhancement, P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:security, issue-rating: 🌊 off-meta tidepool] [Feature]: Network Access Control (allowedDomains / denyDomains) — Egress Firewall — https://github.com/openclaw/openclaw/issues/39685
- #39680 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:security, issue-rating: 🦞 diamond lobster] [Bug] Sandbox validateEnvVarValue base64 heuristic false-positives on legitimate long alphanumeric values — https://github.com/openclaw/openclaw/issues/39680
- #39588 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:data-loss, issue-rating: 🐚 platinum hermit] [Bug]: macOS app 'Launch at login' stops sticking / appears to turn itself off after app updates — https://github.com/openclaw/openclaw/issues/39588
- #39406 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Feature request: config option to suppress transient tool error warnings — https://github.com/openclaw/openclaw/issues/39406

## Recent PR signals

- PR #92356 draft=False fix(heartbeat): skip reasoning payloads when selecting heartbeat reply — https://github.com/openclaw/openclaw/pull/92356
- PR #90057 draft=False Polish Workboard operations view — https://github.com/openclaw/openclaw/pull/90057
- PR #92650 draft=False fix #92465: split OpenAI 431 embedding batches — https://github.com/openclaw/openclaw/pull/92650
- PR #92639 draft=True fix(memory): keep memory_search in transient qmd mode — https://github.com/openclaw/openclaw/pull/92639
- PR #87504 draft=False fix(skill-workshop): align agent_end hook timeout with max reviewer timeout — https://github.com/openclaw/openclaw/pull/87504
- PR #40311 draft=False feat(web-search): expose Brave Goggles for custom search filtering and ranking — https://github.com/openclaw/openclaw/pull/40311
- PR #92642 draft=False fix #86872: Subagent run reports success but fails to write output file — https://github.com/openclaw/openclaw/pull/92642
- PR #92649 draft=False feat(kimi): show code quota in usage status — https://github.com/openclaw/openclaw/pull/92649
- PR #88815 draft=False feat: channel echo / session pinning — https://github.com/openclaw/openclaw/pull/88815
- PR #41375 draft=False fix(hooks): deliver internal hook replies on replyable surfaces — https://github.com/openclaw/openclaw/pull/41375
- PR #39496 draft=False feat(feishu): comprehensive plugin enhancements — streaming, dedup, skills, calendar, and stability — https://github.com/openclaw/openclaw/pull/39496
- PR #92643 draft=False #92076: Subagent completion delivery can fail when requester run is inactive and session transcript is locked — https://github.com/openclaw/openclaw/pull/92643
- PR #92641 draft=False fix(memory): run memory+supplement searches in parallel for corpus=all (fixes #92633) — https://github.com/openclaw/openclaw/pull/92641
- PR #85696 draft=True fix(agent): use static catalog for embedded model fast path — https://github.com/openclaw/openclaw/pull/85696
- PR #41275 draft=False fix(cron): allow timeoutSeconds: 0 for no-timeout mode — https://github.com/openclaw/openclaw/pull/41275
- PR #41892 draft=False feat(control-ui): add cron calendar timeline view — https://github.com/openclaw/openclaw/pull/41892
- PR #90861 draft=False fix #77426: [Bug]:sessions_yield: always returns "No session context" on MCP/claude-cli agent runtime path (gateway tool resolver missing sessionId + onYield) — https://github.com/openclaw/openclaw/pull/90861
- PR #90090 draft=True fix(plugins): guard runtime boundary manifest rows — https://github.com/openclaw/openclaw/pull/90090
- PR #92648 draft=False #92523: Bug: Orphaned TaskFlows in `waiting` status permanently block agent heartbeats (requests-in-flight deadlock) — https://github.com/openclaw/openclaw/pull/92648
- PR #42617 draft=False feat(pairing): add configurable pairingMessage text per channel (#41058) — https://github.com/openclaw/openclaw/pull/42617
- PR #39386 draft=True fix(gateway): forward child session node events to spawnedBy subscribers — https://github.com/openclaw/openclaw/pull/39386
- PR #92647 draft=False fix(memory): attribute corpus=all timeouts to the slow branch instead of the provider — https://github.com/openclaw/openclaw/pull/92647
- PR #92617 draft=False [Bug]: `openclaw plugins update whatsapp` silently wipes Baileys session — full QR re-pair required after every minor plugin update — https://github.com/openclaw/openclaw/pull/92617
- PR #92623 draft=False fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494) — https://github.com/openclaw/openclaw/pull/92623
- PR #92555 draft=False ci: gate stable releases on Windows companion assets — https://github.com/openclaw/openclaw/pull/92555
- PR #90745 draft=False fix: carry reply metadata into runtime context — https://github.com/openclaw/openclaw/pull/90745
- PR #92590 draft=False Docker image ships an extraneous stale openclaw in /app/node_modules (extensions pin the published release) — https://github.com/openclaw/openclaw/pull/92590
- PR #92644 draft=False fix(openrouter): strip openrouter/ prefix from model IDs before API calls — https://github.com/openclaw/openclaw/pull/92644
- PR #81721 draft=False Add diarized JSON transcript segments to media-understanding audio providers — https://github.com/openclaw/openclaw/pull/81721
- PR #91632 draft=False feat: add tool search directory mode — https://github.com/openclaw/openclaw/pull/91632
