# Release Context — OpenClaw `v2026.6.7-beta.1`

Fetched at: `2026-06-13T10:00:32Z`

## Target

- Target tag: `v2026.6.7-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.7-beta.1
- Target tag SHA: 45a103a903872bcf6b26d5eba4cc2db0ff68bc69

## Freshness baselines

- Latest beta tag: `v2026.6.7-beta.1`
- Latest alpha tag: `v2026.6.10-alpha.2`
- Stable baseline: `v2026.6.6`
- Prior prerelease baseline: `v2026.6.6-beta.2`

## Release notes excerpt

## 2026.6.7

### Highlights

- Channel delivery is tighter across Slack, Telegram, outbound media, silent replies, progress drafts, and paged action results: same-channel Slack finals persist in transcripts, top-level `image` message-tool sends attach media, expandable Telegram blockquotes and spooled replay survive delivery, explicit silent assistant replies stay silent, progress draft startup failures are reported, and channel action result pages can be fetched incrementally. (#92498, #92407, #92416, #92281, #92073, #92083, #88993) Thanks @TurboTheTurtle, @ichirokyoto, @xydigit-sj, @joshavant, @sallyom, @hansraj316, and @fuller-stack-dev.
- Provider and model handling is more resilient: Kimi K2.7 Code is available, Kimi native tool-call ids and replayed `reasoning_content` are repaired, Mistral skips unreadable tool schemas, Fireworks catalog parameters come from manifests, DeepSeek keeps configured static transport, provider fallbacks resolve correctly, Anthropic thinking replay is repaired, and Anthropic Vertex stops re-marking transport-budgeted cache control. (#92554, #92396, #90242, #90326, #92265, #92293, #92286, #92387) Thanks @xialonglee, @vincentkoc, @obuchowski, @joshavant, and @openperf.
- User-visible context and auth boundaries are safer: Feishu no longer leaks prompt-preface runtime context into replies, WebSocket payload handling is hardened, CLI-backed `/btw` fallback fails closed, local setup trust is hardened, and Skill Workshop symlink writes are gated and validated before rollback metadata is written. (#92589, #92593, #92226, #92175) Thanks @jovi2014-cyber, @zhangqueping, and @joshavant.
- Agent, memory, Codex, cron, and update recovery paths preserve the useful failure now: invalid plugin model catalogs are isolated, QMD startup failures survive fallback errors, Codex memory prompts remain registered, source message tool replies no longer stop agent progress, structured unsupported-model errors are classified, heartbeat/cron terminal state is preserved, Linux service updates hand off cleanly, and cron status reports the SQLite store path. (#92564, #92218, #92618, #92350, #92343, #92280, #92231, #92225, #92144) Thanks @tangtaizong666, @zhbcher, @mushuiyu886, @rubencu, @joshavant, and @liuhao1024.
- UI, docs, QA, Docker, and release proof are easier to trust: accessibility contrast/focus/font fixes landed, empty Workboard columns can hide, the design-system docs are documented, uptime monitors are pointed at `/health`, Windows Hub docs pin the verified stable installer links, QA evidence and scorecard taxonomy artifacts are produced, QA Lab is bundled into Docker images, and lifecycle timeout cleanup survives leader exit. (#89822, #89615, #89827, #55768, #92608, #92605, #91484, #91500, #92087, #92566) Thanks @BunsDev, @faahim, @liuhao1024, @lzyyzznl, @RomneyDa, and @jesse-merhi.

### Changes

- QA and release validation now emit scorecard taxonomy and evidence artifacts, split plugin ClawHub publishing paths, use trusted plugin npm publishing, keep plugin publish checks authoritative, and align the root package, publishable plugin manifests, generated baselines, and native app versions for the 2026.6.7 beta train. (#91484, #91500) Thanks @RomneyDa.
- Docs and operator guidance now cover Gateway uptime monitoring, design-system guidance, Windows Hub stable download pins, removed stale ClawHub navigation, WhatsApp inbound compatibility, and doctor/update progress behavior. (#55768, #92608, #89827, #92605) Thanks @faahim, @liuhao1024, @BunsDev, and @lzyyzznl.
- Matrix plugin release metadata is aligned with the core beta train and records the version-alignment changelog entry for package publication.

### Fixes

- Channels and outbound flows preserve user intent across Slack transcript mirrors, Telegram polling conflicts and transient draft-preview failures, outbound image sends, explicit silent assistant replies, progress-draft startup errors, paged action results, WhatsApp inbound aliases, local setup trust, and heartbeat commitment delivery. (#92498, #92281, #92407, #92416, #92073, #92083, #88993, #92175, #92231) Thanks @TurboTheTurtle, @joshavant, @ichirokyoto, @xydigit-sj, @sallyom, @hansraj316, and @fuller-stack-dev.
- Provider, model, and tool replay fixes cover unreadable Mistral schemas, Fireworks manifest model parameters, Kimi K2.7 Code/tool-call/reasoning replay, DeepSeek transport inheritance, managed SecretRef auth, static model fallbacks, rejected Anthropic thinking replay, Anthropic Vertex cache control, and OTLP trace correlation. (#90242, #90326, #92554, #92396, #92265, #92235, #92293, #92286, #92387, #92276) Thanks @vincentkoc, @obuchowski, @xialonglee, @joshavant, and @openperf.
- Agent/runtime recovery now isolates invalid plugin model catalogs, preserves Codex memory prompt registration, continues after source message tool replies, classifies structured unsupported-model errors, reports QMD startup failures beside fallback errors, preserves cron timeout/cancel state, keeps disabled heartbeat one-shot retries working, and keeps Linux service auto-updates readable and handed off. (#92564, #92350, #92343, #92280, #92218, #92618, #92225, #92282, #92144) Thanks @tangtaizong666, @rubencu, @joshavant, @zhbcher, @mushuiyu886, and @liuhao1024.
- Install, sandbox, doctor, and security surfaces render CLI skill prompts from materialized paths, fail closed for CLI-backed `/btw`, resolve doctor SecretRef previews, diagnose blocked external channel plugins, validate and gate Skill Workshop symlink writes, stop after failed Node package installs, and keep unsupported daemon service status readable. (#92508, #92226, #92229, #86629) Thanks @brokemac79, @joshavant, and @brokemac79.
- Release, CI, E2E, Docker, and dependency gates keep lifecycle timeout cleanup alive, bundle QA Lab runtime in Docker images, update the esbuild audit pin, harden Docker process cleanup, keep plugin publish checks authoritative, and remove noisy redundant proof scripts so release failures stay bounded. (#92566, #92087, #92540) Thanks @RomneyDa and @jesse-merhi.



## Recent issue risk signals

- #91016 [P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, impact:auth-provider, issue-rating: 🦐 gold shrimp] ⚠️ 升级 2026.6.1 后 DeepSeek Prompt Cache 完全失效，一小时烧掉约 $6 — https://github.com/openclaw/openclaw/issues/91016
- #39847 [stale, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:security, issue-rating: 🦞 diamond lobster] Echo contamination: stripInboundMetadata not called in outbound delivery pipeline — https://github.com/openclaw/openclaw/issues/39847
- #39688 [bug, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, issue-rating: 🦞 diamond lobster] [Bug]: Internal hooks (message:received, message:sent) 返回内容没有发送给用户 — https://github.com/openclaw/openclaw/issues/39688
- #54253 [bug, stale, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, impact:auth-provider, issue-rating: 🦪 silver shellfish] [Bug]: OpenClaw returns "run Error : LLM Request Failed" on RISC-V64 System. — https://github.com/openclaw/openclaw/issues/54253
- #39685 [enhancement, P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:security, issue-rating: 🌊 off-meta tidepool] [Feature]: Network Access Control (allowedDomains / denyDomains) — Egress Firewall — https://github.com/openclaw/openclaw/issues/39685
- #39680 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:security, issue-rating: 🦞 diamond lobster] [Bug] Sandbox validateEnvVarValue base64 heuristic false-positives on legitimate long alphanumeric values — https://github.com/openclaw/openclaw/issues/39680
- #39588 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:data-loss, issue-rating: 🐚 platinum hermit] [Bug]: macOS app 'Launch at login' stops sticking / appears to turn itself off after app updates — https://github.com/openclaw/openclaw/issues/39588
- #39406 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Feature request: config option to suppress transient tool error warnings — https://github.com/openclaw/openclaw/issues/39406

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

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
