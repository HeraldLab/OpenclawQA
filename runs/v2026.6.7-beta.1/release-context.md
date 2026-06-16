# Release Context — OpenClaw `v2026.6.7-beta.1`

Fetched at: `2026-06-15T06:19:27Z`

## Target

- Target tag: `v2026.6.7-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.7-beta.1
- Target tag SHA: 45a103a903872bcf6b26d5eba4cc2db0ff68bc69

## Freshness baselines

- Latest beta tag: `v2026.6.8-beta.1`
- Latest alpha tag: `v2026.6.10-alpha.2`
- Stable baseline: `v2026.6.6`
- Prior prerelease baseline: `v2026.6.8-beta.1`

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

- #71211 [security, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:security, issue-rating: 🦞 diamond lobster] Security: exec tool returns raw stdout/stderr to agent without secret redaction — https://github.com/openclaw/openclaw/issues/71211
- #90588 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:message-loss, impact:auth-provider, impact:crash-loop, issue-rating: 🐚 platinum hermit] [Bug] v2026.5.28 ~ v2026.6.1: All QQ Bot agents unresponsive — Cannot read properties of undefined (reading 'run') — https://github.com/openclaw/openclaw/issues/90588
- #54578 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] Add tree view command to visualize active agents — https://github.com/openclaw/openclaw/issues/54578
- #54373 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:linked-pr-open, impact:session-state, issue-rating: 🌊 off-meta tidepool] [RFC] Context Provenance: Add source/volatility metadata to injected context segments — https://github.com/openclaw/openclaw/issues/54373

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #92428 draft=False fix(qqbot): keep markdown table chunks valid — https://github.com/openclaw/openclaw/pull/92428
- PR #93187 draft=False fix(memory-core): exclude archive transcripts from dreaming corpus and propagate cron parentage to subagents — https://github.com/openclaw/openclaw/pull/93187
- PR #78664 draft=False perf(agents): cache provider tool schema normalization — https://github.com/openclaw/openclaw/pull/78664
- PR #93188 draft=False test(macos): cover root CLI command parsing — https://github.com/openclaw/openclaw/pull/93188
- PR #93184 draft=False fix(ui): preserve live tool stream order — https://github.com/openclaw/openclaw/pull/93184
- PR #93149 draft=False feat(cron): add add dry-run preview — https://github.com/openclaw/openclaw/pull/93149
- PR #69199 draft=False fix(memory): improve error message when node:sqlite is unavailable — https://github.com/openclaw/openclaw/pull/69199
- PR #70046 draft=False fix(cron): support HH:MM time-only strings in --at; apply --tz to time-only input — https://github.com/openclaw/openclaw/pull/70046
- PR #92680 draft=False feat(read): add encoding parameter for GBK and non-UTF-8 text files (#92664) — https://github.com/openclaw/openclaw/pull/92680
- PR #93186 draft=False fix(cache): stable tool result aggregate truncation — https://github.com/openclaw/openclaw/pull/93186
- PR #45901 draft=False security: create session dirs with private permissions — https://github.com/openclaw/openclaw/pull/45901
- PR #93151 draft=False #92664: fix(read): decode GBK-encoded files on Chinese Windows via existing decoder — https://github.com/openclaw/openclaw/pull/93151
- PR #93185 draft=False [codex] fix(telegram): drop unused rich markdown parameter — https://github.com/openclaw/openclaw/pull/93185
- PR #84896 draft=False fix(memory): export LanceDB artifacts for wiki bridge — https://github.com/openclaw/openclaw/pull/84896
- PR #93174 draft=False test: fold channel message flows into qa e2e — https://github.com/openclaw/openclaw/pull/93174
- PR #88750 draft=False feat(context-engine): pass runtime settings into lifecycle — https://github.com/openclaw/openclaw/pull/88750
- PR #87739 draft=False Telegram: keep long DM turns alive through progress previews — https://github.com/openclaw/openclaw/pull/87739
- PR #75066 draft=False fix(sessions): preserve activity for compaction metadata — https://github.com/openclaw/openclaw/pull/75066
- PR #74954 draft=False fix(agents): prevent provider defaultModel from overriding agents.defaults.model (fixes #24170) — https://github.com/openclaw/openclaw/pull/74954
- PR #47604 draft=False feat(android): add Wear OS app MVP — https://github.com/openclaw/openclaw/pull/47604
- PR #93179 draft=False excludeTestExecution option for more compact QA profile evidence — https://github.com/openclaw/openclaw/pull/93179
- PR #93183 draft=True [codex] Fix /btw Codex runtime side-question routing — https://github.com/openclaw/openclaw/pull/93183
- PR #93175 draft=False Add smoke-ci primary scorecard evidence — https://github.com/openclaw/openclaw/pull/93175
- PR #91193 draft=False fix(cli): document Commander rawArgs internal API dependency in action-reparse.ts — https://github.com/openclaw/openclaw/pull/91193
- PR #91192 draft=False fix(tts): allow trusted local media in message_tool_only mode — https://github.com/openclaw/openclaw/pull/91192
- PR #91180 draft=False feat(whatsapp): support opt-in group-name config — https://github.com/openclaw/openclaw/pull/91180
- PR #91177 draft=False fix(tui): persist canonical provider in session modelProvider — https://github.com/openclaw/openclaw/pull/91177
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #91162 draft=False fix(cron): honor configured delivery.channel instead of misrouting (#46899) — https://github.com/openclaw/openclaw/pull/91162
- PR #91161 draft=False fix: prevent A2A target from reverse-calling sessions_send to requester (#39476) — https://github.com/openclaw/openclaw/pull/91161
