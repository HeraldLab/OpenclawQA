# Release Context — OpenClaw `v2026.6.1-beta.1`

Fetched at: `2026-06-01T16:29:58Z`

## Target

- Target tag: `v2026.6.1-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.1-beta.1
- Target tag SHA: 8ad3e55e588cec1f2c7b4a2c33e482797eb1af82

## Freshness baselines

- Latest beta tag: `v2026.6.1-beta.1`
- Latest alpha tag: `v2026.6.1-alpha.2`
- Stable baseline: `v2026.5.28`
- Prior prerelease baseline: `v2026.5.31-beta.4`

## Release notes excerpt

## 2026.6.1

### Highlights

- Agents and CLI-backed runtimes recover more cleanly from interrupted tool calls, stale session bindings, compaction handoffs, and media delivery retries. (#88129, #88136, #88141, #88162, #88182)
- Channels and mobile delivery are steadier across Telegram, WhatsApp, iMessage, Slack, Discord, Microsoft Teams, Google Chat, Google Meet, and iOS realtime Talk. (#88096, #88105, #88183, #88231)
- Provider and plugin requests now bound more timers, retries, OAuth/device-code lifetimes, media downloads, local service probes, and generated-content polling paths before they can hang a run.
- Skills, session metadata, gateway runtime state, plugin metadata, and store writes do less repeated work on hot paths while keeping config and dispatch behavior stable.
- Skills and plugin loading now handle stale disabled snapshots and loader failures more clearly, so channel turns avoid disabled SecretRefs and operators get better recovery guidance. (#79072, #79173) Thanks @zeus1959.
- Workboard, SecretRef plugin manifests, hosted iOS push relay, and external Copilot/Tokenjuice packaging add broader orchestration, integration, and plugin delivery surfaces. (#82326, #87469, #87796, #88107, #88117)
- Skill Workshop now has a fuller Control UI flow with proposal lists, today actions, revision handoff, searchable file previews, review states, locale coverage, and reusable session routing.
- Chat and Control UI startup paths keep sends alive through history loading, stream deltas incrementally, skip markdown work while streaming, keep drafts local while typing, trace first-output latency, and expose calmer composer controls. (#88772, #88825, #88998) Thanks @vincentkoc.
- Provider coverage and model metadata now include MiniMax M3, account OAuth endpoints, Google/Vertex catalog fixes, OpenRouter SQLite model caching, Copilot Claude 1M capabilities, Foundry reasoning alignment, and OpenAI response replay guards. (#88480, #88512, #88851, #88860)
- iMessage monitor state, inbound queues, and plugin install ledgers moved toward SQLite-backed state so restarts and local monitors recover with less duplicate filesystem scanning. (#88794, #88797)
- Release, CI, Docker, E2E, plugin install, and diagnostics lanes now cap more logs, response bodies, readiness probes, artifact checks, status polling, and rollback snapshots so failures report bounded proof instead of stalling.

### Changes

- Docs: add a dedicated Skill Workshop guide covering governed skill creation, reviewable proposals, CLI, Gateway, agent tool behavior, approval policy, support files, and recovery. Thanks @shakkernerd.
- Skills: let the `skill_workshop` agent tool apply, reject, and quarantine explicit proposals through the guarded review flow. Thanks @shakkernerd.
- Skills: let proposals carry approved support files under standard skill folders, with scanner, hash, and rollback safeguards. Thanks @shakkernerd.
- Skills: let pending proposals be revised in place with versioned, dated proposal frontmatter before approval. Thanks @shakkernerd.
- Skills: add Skill Workshop with pending proposals, CLI/Gateway review actions, rollback metadata, and the `skill_workshop` agent tool. Thanks @shakkernerd.
- Skill Workshop: add the Control UI navigation, styled dashboard, proposal today view, revision dialog, file preview modal, searchable preview files, reusable session handoff, and localized strings.
- Plugins: externalize Tokenjuice as the official `@openclaw/tokenjuice` plugin with npm and ClawHub publish metadata.
- Plugins: externalize the GitHub Copilot agent runtime as the official `@openclaw/copilot` plugin with npm and ClawHub publish metadata.
- iOS: add hosted push relay defaults, realtime Talk playback, and a guarded WebSocket ping path for more reliable mobile sessions. (#88096, #88105, #88231)
- iOS: support native iPad display layouts.
- Workboard: add orchestration primitives and agent coordination tools for multi-agent planning and run tracking. (#87469)
- Workboard: wire task-backed board runs and show task comments in the edit modal.
- Code mode: add internal namespaces for scoped agent/global sessions and exact namespace tool dispatch. (#88043)
- Code mode: add MCP API files and docs for code-mode integrations.
- Control UI: add a Dreaming-tab agent selector and propagate the selected agent through Dreaming status, diary, and diary actions. (#78748) Thanks @stevenepalmer.
- Control UI: add calmer chat composer controls, local draft typing state, and first-output latency instrumentation for active chat entry. (#88772, #88998) Thanks @vincentkoc.
- Plugins: add a SecretRef provider integration manifest contract and extract shared LLM core packages for provider/plugin reuse. (#82326, #88117)
- Plugins: persist the plugin install index in SQLite so installed package lookup survives reloads with less filesystem scanning. (#88794)
- Providers: add MiniMax M3 model support. (#88860)
- Doctor: add disk space health checks and stabilize post-upgrade JSON probes.
- Channels: store inbound queues in SQLite and migrate iMessage monitor state to SQLite-backed tracking. (#88797)
- Skills: add the core skills index and centralize skills runtime loading, status, filtering, and prompt formatting.

### Fixes

- Agents/TUI: keep local custom provider runs from loading plugin runtime and auth alias metadata when plugins are disabled.
- Agents/TUI: restore in-flight TUI run switch-back behavior, keep no-policy native hook fallback available, guard vanished workspaces, and keep lightweight isolated subagents lightweight.
- Agents/media: keep async image, music, and video generation starts from ending the Codex turn, so mixed requests can continue with summaries or other work while media renders in the background.
- Agents/Codex: keep public OpenAI API-key profiles from being treated as native Codex app-server auth while preserving persisted Codex OAuth sessions.
- Agents/Codex: stream Codex app-server final-answer partials to live reply previews, preserve ACP metadata in SQLite, prefer real tool results over synthetic repair output, prevent aborted app-server turn handles from lingering, migrate legacy OpenAI Codex `lastGood` auth state, and preserve workspace/session metadata through ACP runtime refactors. (#88405, #88724, #88730) Thanks @vincentkoc.
- Control UI: keep collapsed tool cards labeled with the tool name and action instead of generic output text. Thanks @shakkernerd.
- Agents/Codex: surface Skill Workshop guidance in Codex app-server prompts when `skill_workshop` is available. Thanks @shakkernerd.
- Agents/auth: write auth profiles atomically, add force re-login recovery, preserve workspaces during state-only uninstall, and compact before oversized turns so recovery paths avoid partial state.
- Skills: skip disabled skill env overrides from stale persisted snapshots so disabled skill `apiKey` SecretRefs cannot abort embedded or channel turns. (#79072, #79173) Thanks @zeus1959.
- CLI: avoid live catalog validation during `openclaw agents add`, so adding a secondary agent no longer depends on provider catalog availability. (#76284, #88314) Thanks @zhangguiping-xydt.
- CLI: keep `plugins list --json` on the snapshot-only path so plugin sweeps avoid loading the full runtime status graph.
- CLI/desktop: bridge WSL clipboard operations through the shell and recognize manual-update launchd jobs. (#88764)
- Plugins: make PixVerse external-plugin ClawHub metadata explicit and keep it out of bundled dist builds.
- Plugins: clarify plugin loader failure guidance so missing or incompatible plugin packages point operators at the right repair path.
- Plugins: preserve npm plugin roots after blocked installs, skip plugin-local `openclaw` peer symlinks during rollback snapshots, relink those peers after restore, isolate cached tool runtime siblings, and isolate web-provider factory failures so one bad plugin does not poison sibling runtime paths. (#77237, #88807)
- Cron: keep SQLite cron migrations compatible with legacy run-log tables, archived job stores, diagnostic cron names, and legacy one-shot delete-after-run behavior. (#88285)
- Cron: keep update delivery validation scoped, harden restart state, and retire MCP runtimes on isolated cron cleanup.
- Memory: serialize QMD update/embed writes per store, preserve phase signals on read errors, harden envelope metadata sanitization, and rewrite generated transcript paths on rollover so memory/search state survives concurrent gateway and CLI activity. (#66339, #85931) Thanks @openperf and @amittell.
- Providers: bound generated media downloads from OpenAI, Runway, xAI, MiniMax, BytePlus, DashScope-compatible, FAL, OpenRouter, Google, Vydra, and Comfy providers.
- Providers: resolve Google defaults to `google-generative-ai`, register Vertex static catalog rows, align Foundry reasoning metadata, skip DeepSeek V4 thinking params on Foundry fallback, use MiniMax account OAuth endpoints, preserve Copilot Claude 1M capabilities, suppress disabled Ollama reasoning output, keep OpenAI stop-finished tool calls, and avoid replay ids when the Responses store is disabled. (#88480, #88512)
- Providers: cap GitHub Copilot OAuth request timeouts before creating abort signals.
- Cron: retry recurring jobs after transient model rate limits before waiting for the next scheduled slot.
- Agents/Codex: keep live session locks during cleanup, recover interrupted CLI tool transcripts, preserve Codex auth and compaction session identity, clear orphan tool state, cap app-server idle timers, and keep media completion delivery retryable. (#88129, #88136, #88141, #88162, #88182)
- Chat/UI: show Gateway chat failures as visible assistant messages in the Control UI instead of only setting an invisible error state.
- Channels: cap Telegram, Discord, WhatsApp, Signal, Feishu, Google Chat, Microsoft Teams, QQBot, Nostr, Zalo, Zalouser, and Nextcloud-style request/retry timers; preserve SMS approval reply routes; and retry WhatsApp QR login 408 timeouts. (#88183)
- Security/config parsing: reject unsafe OAuth/token lifetimes, retry-after delays, inbound timestamps, response body sizes, command timeout config, sandbox observer token TTLs, and gateway WebSocket calls after close.
- Providers/media: cap local service, model, usage, queue, generated media, TTS, music, workflow polling, and provider OAuth request timers across hosted and local providers.
- Release/CI/E2E: bound release candidate reads, beta smoke REST calls, plugin npm verification commands, changelog restore, cross-OS process groups, kitchen-sink and bundled plugin readiness probes, secret-provider probes, Telegram credential timeouts, Control UI i18n and CLI startup metadata generation, Vitest routing, and mainline test flakes. (#88127, #88137, #88155, #88160)
- Release/CI/E2E: keep Kitchen Sink live plugin MCP probes resolving source-checkout workspace packages and align the live gauntlet with current Kitchen Sink diagnostics.
- Release/CI/E2E: run the secret-provider integration proof through the repo pnpm runner so native macOS and Windows validation use the hydrated package-manager shim.
- Release/CI/E2E: run the Telegram desktop proof gateway through the repo pnpm runner so native macOS proof uses the hydrated package-manager shim.
- Docs/CI: run Mintlify anchor checks through the repo pnpm runner so docs link validation works when pnpm is only available through the hydrated package-manager shim.
- Agents: keep configured fallback model metadata typed so provider params, context-token caps, and media input limits do not break changed-gate typechecks.
- Agents: accept hidden `sessions_send` body aliases before validation while keeping the model-facing `message` schema canonical. (#88229) Thanks @zhangguiping-xydt.
- Chat/UI: preserve startup chat sends during history loading, unblock the initial Control UI chat send, stream chat deltas incrementally, skip markdown parsing while streaming, keep drafts local while typing, guard composer rerenders, honor Chromium executable overrides, and detect system Chromium for E2E. (#88998) Thanks @vincentkoc.
- Channels: preserve long Feishu streaming replies, send visible fallbacks when accepted Feishu turns produce no final reply, tolerate iMessage self-chat timestamp skew, preserve colon-prefixed slash commands in mention parsing, decode Nostr `npub` allowlists correctly, and suppress raw provider errors during channel delivery. (#87896)
- Config/status/doctor: skip unresolved shell references in state-dir dotenv files, resolve gateway auth secrets during deep status audits, respect explicit PI runtime policy, report runtime tool-schema errors, and keep post-upgrade JSON stable. (#88288)
- Gateway/session state: list commands from the Gateway plugin registry, harden MCP loopback tool schemas, hide phantom agent-store rows from `sessions.list`, make task persistence failures explicit, and carry session UUIDs on interactive dispatch events.
- OpenAI/TTS: handle speed directives for OpenAI TTS voices. (#74089)
- CI/Crabbox: keep default runner capacity on the Azure credit-backed on-demand D4 lane with the Azure SSH port and a Git-independent full check job, so broad validation avoids low-priority spot quota stalls, hydrate port mismatches, non-Git hydrated workspaces, and stale AWS region hints.
- CI/Crabbox: route Crabbox wrapper and Testbox workflow edits to their regression tests so changed-test gates do not silently run zero specs.
- CI/workflows: route workflow sanity helper edits to their guard tests and cover composite-action input interpolation checks.
- CI/tooling: route CI scope, dependency, changelog, and docs helper edits to their owner tests instead of silently skipping changed-test coverage.
- CI/tooling: route package, release, and install helper edits to their owner tests so changed-test gates cover publish and installer script changes.
- CI/tooling: route shared script library edits through their owner tests so lock, process, safety, and scan helpers do not skip changed-test coverage.
- CI/tooling: skip expensive import-graph scans once a changed diff already requires broad fallback, keeping local changed-test planning fast while still collecting explicit owner tests.
- CI/tooling: route script edits through conventional owner tests when matching `test/scripts` or `src/scripts` coverage already exists.
- CI/tooling: honor option terminators in the memory FD repro script so follow-on arguments are not reparsed.
- Release/CI/E2E: assert plugin lifecycle runtime inspect output instead of only capturing it.
- Release/CI/E2E: make gateway-network prove the advertised health RPC and retry early WebSocket closes without burning full open timeouts.
- Release/CI/E2E: honor option terminators across release, Parallels smoke, plugin gauntlet, and extension-memory scripts.
- Release/CI/E2E: fail plugin gateway gauntlet QA chunks when the requested suite summary is missing or invalid.
- Performance: prebuild QA runtime probes with generated plugin assets but without CLI startup metadata.
- Performance: skip declaration bundling for runtime-only CLI startup and gateway watch build profiles.
- Performance: reuse prepared provider handles, strict tool schemas, gateway runtime metadata, session maintenance config, plugin metadata, bundled skill allowlists, package-local plugin artifacts, single-entry store writes, and validated/serialized session prompt blobs.



## Recent issue risk signals

- #89145 [P3, impact:session-state] feat: auto-trigger self-improving on user corrections/feedback — https://github.com/openclaw/openclaw/issues/89145
- #89147 [no-labels] Native hook relay starves mid-turn after long model-thinking gap (renewal loop tool-call-driven) — https://github.com/openclaw/openclaw/issues/89147
- #89139 [no-labels] webchat creates new agent run per message, destroying prompt cache (93% → 29% hit rate) — https://github.com/openclaw/openclaw/issues/89139

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #89149 draft=True fix(agents): validate extension tool names — https://github.com/openclaw/openclaw/pull/89149
- PR #72557 draft=False feat: PluginStatusProvider plugin API for TUI footer status (resolves #64086) — https://github.com/openclaw/openclaw/pull/72557
- PR #87771 draft=False feat(config): add $includeText raw-text include directive — https://github.com/openclaw/openclaw/pull/87771
- PR #88821 draft=False trace: Correlate channel message diagnostics into one trace — https://github.com/openclaw/openclaw/pull/88821
- PR #88875 draft=False docs: document markdown and shared helpers — https://github.com/openclaw/openclaw/pull/88875
- PR #89144 draft=False feat(channels): add Zulip external channel catalog entry — https://github.com/openclaw/openclaw/pull/89144
- PR #89148 draft=False fix(auto-reply): guard optional getFailedCounts on dispatcher variants — https://github.com/openclaw/openclaw/pull/89148
- PR #67783 draft=False fix(feishu): target typing reaction on inbound — https://github.com/openclaw/openclaw/pull/67783
- PR #87072 draft=False feat(telegram): opt-in interleaved progress lane — https://github.com/openclaw/openclaw/pull/87072
- PR #64127 draft=False feat: Provider circuit breaker for quota exhaustion — https://github.com/openclaw/openclaw/pull/64127
- PR #86233 draft=False fix(codex): cap managed app-server trace logs — https://github.com/openclaw/openclaw/pull/86233
- PR #82353 draft=False feat(auto-reply): expose safe requester identity metadata — https://github.com/openclaw/openclaw/pull/82353
- PR #89128 draft=False fix: skip Responses item id replay without store — https://github.com/openclaw/openclaw/pull/89128
- PR #80823 draft=False fix(cli): differentiate gateway-restart hint for hot-loadable agent config sets (#80722) — https://github.com/openclaw/openclaw/pull/80823
- PR #88748 draft=True fix(gemini): bridge OAuth profiles into CLI runtime — https://github.com/openclaw/openclaw/pull/88748
- PR #89133 draft=False Restore GPT-5.3 Codex Spark OAuth routing — https://github.com/openclaw/openclaw/pull/89133
- PR #89143 draft=False fix(agents): stabilize message send loop detection — https://github.com/openclaw/openclaw/pull/89143
- PR #69707 draft=False fix(memory-lancedb): stop forwarding embedding dimensions upstream — https://github.com/openclaw/openclaw/pull/69707
- PR #87898 draft=False fix(secrets): skip PLAINTEXT_FOUND for apiKey values that look like env var references — https://github.com/openclaw/openclaw/pull/87898
- PR #89091 draft=False fix(memory-core): retry narrative message reads — https://github.com/openclaw/openclaw/pull/89091
- PR #88504 draft=False feat(memory): add multi-slot memory role architecture — https://github.com/openclaw/openclaw/pull/88504
- PR #89142 draft=False fix(secrets): generate secretref reference docs from the credential matrix — https://github.com/openclaw/openclaw/pull/89142
- PR #85982 draft=False fix(models): dedupe implicit CLI runtime aliases — https://github.com/openclaw/openclaw/pull/85982
- PR #89141 draft=True fix(agents): guard provider tool diagnostic names — https://github.com/openclaw/openclaw/pull/89141
- PR #89073 draft=False fix(exec): reuse duplicate background sessions — https://github.com/openclaw/openclaw/pull/89073
- PR #89138 draft=False fix #88009: [Feature]: batched memory embedding should batch over files — https://github.com/openclaw/openclaw/pull/89138
- PR #89109 draft=False fix(agents): block message-tool spam loops defeated by volatile message ids — https://github.com/openclaw/openclaw/pull/89109
- PR #89104 draft=False fix(exec): expose termination metadata in tool details — https://github.com/openclaw/openclaw/pull/89104
- PR #89135 draft=False fix(ui): render skill workshop tab — https://github.com/openclaw/openclaw/pull/89135
- PR #88964 draft=False fix(agents): repair context-engine tool-result pairing — https://github.com/openclaw/openclaw/pull/88964
