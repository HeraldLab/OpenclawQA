# Release Context — OpenClaw `v2026.6.5-beta.1`

Fetched at: `2026-06-06T04:00:11Z`

## Target

- Target tag: `v2026.6.5-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.1
- Target tag SHA: e386e60025d992ff21f73b4dae68a58a0e8ca79e

## Freshness baselines

- Latest beta tag: `v2026.6.5-beta.1`
- Latest alpha tag: `v2026.6.6-alpha.1`
- Stable baseline: `v2026.6.1`
- Prior prerelease baseline: `v2026.6.2-beta.1`

## Release notes excerpt

## 2026.6.5

### Highlights

- QQBot now strips model reasoning/thinking scaffolding before native delivery, preventing raw `<thinking>` content from leaking into channel replies. (#89913, #90132) Thanks @openperf.
- MCP tool results now coerce `resource_link`, `resource`, `audio`, malformed image, and future non-text/image blocks at the materialize boundary, preventing Anthropic 400s and poisoned session history after a tool returns richer MCP content. (#90710, #90728) Thanks @RanSHammer and @849261680.
- Anthropic extended-thinking sessions recover after prompt-cache expiry or Gateway restart because stream start events wait for `message_start`, letting pre-generation signature errors trigger the existing recovery retry. (#90667, #90697) Thanks @openperf.
- Parallel is now a bundled `web_search` provider with `PARALLEL_API_KEY` discovery, guarded endpoint handling, cache-safe session ids, onboarding picker support, and docs. (#85158) Thanks @NormallyGaussian.
- Google Vertex ADC users get static catalog rows and runtime model resolution again, while single-provider cooldown recovery and memory adapter status checks are more reliable. (#90506, #90609, #90717, #90816) Thanks @849261680.
- Matrix can preflight voice notes before mention gating, preserve thread reads/replies through Matrix relations pagination, and carry QA coverage for voice and thread flows. (#78016, #90415)
- Auth and plugin install state is more durable: auth profiles now live in SQLite, official npm plugin install records keep their trusted pins, and prerelease fallback integrity checks avoid carrying stale integrity forward. (#89102, #88585)
- macOS node mode no longer silently self-reconnects away from a healthy direct Gateway session, reducing unexpected companion app session churn. (#90668, #90815) Thanks @vrurg.
- Upgrade and service paths are safer: cron legacy JSON stores migrate during doctor preflight, service env placeholders no longer mask state-dir secrets, WhatsApp startup waits are bounded, and disabled WhatsApp accounts tear down on config reload. (#90072, #90208, #90277, #90488, #90486, #87951, #87965) Thanks @MonkeyLeeT, @sallyom, @mcaxtr, and @MukundaKatta.

### Changes

- Search/providers: add the Parallel bundled web-search plugin, live provider tests, registration contracts, onboarding/docs wiring, and guarded `api.parallel.ai/v1/search` support. (#85158) Thanks @NormallyGaussian.
- Matrix/channels: add voice-message preflight and thread-aware read/reply behavior, including Matrix QA scenario wiring and docs for voice-message behavior. (#78016, #90415)
- Skills/ClawHub: install ClawHub skills backed by GitHub repositories through the resolved install API, download the pinned GitHub commit, keep install-policy checks, and report install telemetry after success. (#90478) Thanks @Patrick-Erichsen.
- Google Chat/channels: add native approval card actions and click handling so Google Chat approvals use platform-native cards instead of generic message flow.
- Mobile: Android provider/model screens now surface expiring, unavailable, unresolved, and attention states more clearly, while iOS settings and Talk tabs keep diagnostics, gateway rows, attachment labels, and unavailable Talk controls reachable.
- Memory: QMD search can use the new rerank toggle, and memory adapter status uses the resolved default model identity when checking plain status. (#61834)
- Docs/tooling: add Parallel search docs, refresh weather-skill guidance toward `web_fetch`, clarify legacy `openai-codex` auth, document release/test helper scripts, and tighten changed-test routing docs for CI/debugging work. (#90028, #90250) Thanks @fuller-stack-dev.
- Platform maintenance: refresh Android, Swift/macOS, Docker, CodeQL, Buildx, Docker build/push, and Codex Action dependencies for this release train. (#74980, #81757, #86481, #86483, #90601)

### Fixes

- Channel content boundaries: QQBot now strips reasoning/thinking tags before sending, preserving final answers while hiding internal model narration from users. (#89913, #90132) Thanks @openperf.
- Agents/MCP/providers: coerce non-text/image MCP tool-result blocks before they reach provider converters, preserving valid images and turning richer MCP content into text instead of malformed image blocks. (#90710, #90728) Thanks @RanSHammer and @849261680.
- Anthropic/Codex/ACP/agent recovery: defer Anthropic stream start events until `message_start`, strip stale compaction thinking signatures before Anthropic replay, detect unsigned thinking-only stalls, refresh prompt fences after compaction writes, reject empty completion handoffs, preserve parent streaming-off overrides/shared progress commentary, forward heartbeat metadata to context-engine hooks, and cover Codex session/thread migration edge cases. (#90667, #90697, #90163, #90108, #89874, #89505, #90632, #89302, #90729, #90317, #90319) Thanks @openperf, @100yenadmin, and @ooiuuii.
- Provider/model resolution: preserve Google Vertex ADC auth markers in generated catalogs, re-probe a single-provider primary after cooldown, share Codex model visibility, fail closed for unknown model auth, preserve Codex alias availability, keep unresolved profile refs unknown, and avoid resolving auth while listing models. (#90506, #90609, #90717, #90702) Thanks @849261680.
- Gateway/macOS/mobile: avoid duplicate Gateway probe warnings by identity, rate-limit node pairing requests while preserving paired-node reconnects, keep macOS node mode on a healthy direct Gateway session, keep iOS diagnostics and gateway rows reachable, and avoid Linux ARM Gradle resource tasks during Android builds. (#85791, #90147, #90668, #90815) Thanks @giodl73-repo and @vrurg.
- TUI/chat/Workboard/auto-reply: optimistic user messages stay stable across stale history reloads, runId reassignment, and abort windows instead of disappearing, jumping, or lingering as ghost rows; Workboard stale lifecycle bulk updates no longer overwrite newer status/provenance; message-tool sends now count as delivery. (#86205, #89600, #88592, #90123) Thanks @RomneyDa.
- Cron/update/service env: doctor config preflight now migrates legacy cron JSON stores into SQLite before runtime reads, service env planning skips unresolved placeholders that would mask state-dir `.env` values, and session transcript rewrites keep registry markers/discriminants consistent. (#90072, #90208, #90277, #90488) Thanks @MonkeyLeeT and @sallyom.
- Security/config/tooling: guard MCP HTTP redirects, protect global agent config defaults, and keep release/test/tooling proof failures bounded and explicit. (#89732, #90145)
- Channels: WhatsApp restarts when per-account config changes, bounds background startup waits, closes failed sockets, and preserves reconnect behavior; Mattermost slash commands keep their state on `globalThis`; Feishu streaming cards preserve full merged content; voice-call tracks Twilio streams after connect; ClickClack reply tools respect `toolsAllow`. (#87951, #87965, #90486, #68113, #90534, #90181, #90607, #89500) Thanks @MukundaKatta, @mcaxtr, @infoanton, @mushuiyu886, and @sahibzada-allahyar.
- Release/CI/E2E: main CI guard drift, PR merge diff scoping, live Docker credential staging, base-image qualification, installer Docker classification, Playwright dependency install recovery, API-key auth for Codex live Docker lanes, Parallels option terminators, and JSON-mode progress handling are tighter so release proof fails cleaner. (#90532, #90287, #90058) Thanks @RomneyDa, @hxy91819, and @mrunalp.
- Tests/state isolation: provider, media, auth, cron, task, session, sandbox, Gateway, and Codex timeout fixtures now scope more home/state/env data per test, reducing cross-test leakage and making release validation failures less noisy. (#90027, #89974)


## Recent issue risk signals

- #90835 [P3, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, issue-rating: 🌊 off-meta tidepool] Docs feedback: /platforms/ios — https://github.com/openclaw/openclaw/issues/90835
- #89830 [P1, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] iMessage channel jams: valid JSON-RPC `imsg` response is split by Node readline on U+2028, every fragment fails JSON.parse — https://github.com/openclaw/openclaw/issues/89830
- #90810 [no-labels] [Bug]: Prompt cache invalidated on every user turn on full-resend transports — transient timestamp + content-form decoration on the current user message (regression from #3658) — https://github.com/openclaw/openclaw/issues/90810

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #85155 draft=False fix(agents): avoid inviting provider swaps in model alias guidance — https://github.com/openclaw/openclaw/pull/85155
- PR #82148 draft=False feat(agents): allow spawn fast mode overrides — https://github.com/openclaw/openclaw/pull/82148
- PR #90793 draft=False Fix OpenAI audio auth to use API keys — https://github.com/openclaw/openclaw/pull/90793
- PR #90837 draft=False fix(telegram): suppress internal tool warnings in groups — https://github.com/openclaw/openclaw/pull/90837
- PR #90836 draft=False fix(cron): block self-narrating auto-announce replies — https://github.com/openclaw/openclaw/pull/90836
- PR #90480 draft=False feat(whatsapp): expand live QA coverage — https://github.com/openclaw/openclaw/pull/90480
- PR #90811 draft=False fix(agents): stabilize user-turn serialization across turns to preserve prompt cache — https://github.com/openclaw/openclaw/pull/90811
- PR #90839 draft=False fix(memory-core): exclude soft-deleted .jsonl.deleted paths from dreaming corpus (#90466) — https://github.com/openclaw/openclaw/pull/90839
- PR #90328 draft=False Expose model picker agent runtimes — https://github.com/openclaw/openclaw/pull/90328
- PR #90791 draft=False fix(doctor): prevent repeat talk normalization from derived speakerVoice fallback (fixes #90446) — https://github.com/openclaw/openclaw/pull/90791
- PR #74235 draft=False fix(googlechat): preserve thread reply target through delivery — https://github.com/openclaw/openclaw/pull/74235
- PR #88796 draft=False fix(discord): resolve guildId from session channel for search actions — https://github.com/openclaw/openclaw/pull/88796
- PR #90838 draft=False fix(config): warn for retired skill-workshop plugin entry instead of failing validation (#90244) — https://github.com/openclaw/openclaw/pull/90838
- PR #90695 draft=False fix(agents): handle max_turns stop reason and improve retry-limit error context (fixes #78145) — https://github.com/openclaw/openclaw/pull/90695
- PR #90834 draft=False fix(matrix): guard against missing channel.inbound runtime (#90325) — https://github.com/openclaw/openclaw/pull/90834
- PR #88690 draft=False Emit sessions.changed for in-chat command metadata — https://github.com/openclaw/openclaw/pull/88690
- PR #90821 draft=False fix(compact): make /compact command cancelable via abortEmbeddedAgentRun — https://github.com/openclaw/openclaw/pull/90821
- PR #89514 draft=False fix(doctor): exclude platform-incompatible skills from missing requirements — https://github.com/openclaw/openclaw/pull/89514
- PR #90812 draft=False fix(voice-call): preserve live Twilio streams in stale reaper — https://github.com/openclaw/openclaw/pull/90812
- PR #90817 draft=False fix(agents): apply stale-run liveness check to aborted subagent orphan recovery — https://github.com/openclaw/openclaw/pull/90817
- PR #90579 draft=False fix: allow trusted host-read html after outbound staging — https://github.com/openclaw/openclaw/pull/90579
- PR #90051 draft=False fix(agents): strip reasoning tags from chat replies — https://github.com/openclaw/openclaw/pull/90051
- PR #90790 draft=False fix(codex): preserve completed replies after client close — https://github.com/openclaw/openclaw/pull/90790
- PR #88245 draft=False refactor(whatsapp): introduce inbound message contexts — https://github.com/openclaw/openclaw/pull/88245
- PR #89949 draft=False fix(announce-delivery): backfill effectiveDirectOrigin.to from requester session entry — https://github.com/openclaw/openclaw/pull/89949
- PR #90798 draft=False fix(agents): materialize sandbox skills for rw sandboxes — https://github.com/openclaw/openclaw/pull/90798
- PR #90805 draft=True fix(codex): fail closed on missing native hook relay delivery — https://github.com/openclaw/openclaw/pull/90805
- PR #90833 draft=False feat(control-ui): allow renaming sessions in sidebar (#90655) — https://github.com/openclaw/openclaw/pull/90833
- PR #90832 draft=False fix(gateway): surface in-progress assistant response on session reconnect — https://github.com/openclaw/openclaw/pull/90832
