# Release Context — OpenClaw `v2026.6.5-beta.5`

Fetched at: `2026-06-08T23:00:09Z`

## Target

- Target tag: `v2026.6.5-beta.5`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.5
- Target tag SHA: ff0b21e950809f0b492c7c5ecfb273cb1cad8cac

## Freshness baselines

- Latest beta tag: `v2026.6.5-beta.5`
- Latest alpha tag: `v2026.6.8-alpha.1`
- Stable baseline: `v2026.6.1`
- Prior prerelease baseline: `v2026.6.5-beta.3`

## Release notes excerpt


### Highlights

- QQBot now strips model reasoning/thinking scaffolding before native delivery, preventing raw `<thinking>` content from leaking into channel replies. (#89913, #90132) Thanks @openperf.
- MCP tool results now coerce `resource_link`, `resource`, `audio`, malformed image, and future non-text/image blocks at the materialize boundary, preventing Anthropic 400s and poisoned session history after a tool returns richer MCP content. (#90710, #90728) Thanks @RanSHammer and @849261680.
- Anthropic extended-thinking sessions recover after prompt-cache expiry or Gateway restart because stream start events wait for `message_start`, letting pre-generation signature errors trigger the existing recovery retry. (#90667, #90697) Thanks @openperf.
- Parallel is now a bundled `web_search` provider with `PARALLEL_API_KEY` discovery, guarded endpoint handling, cache-safe session ids, onboarding picker support, and docs. (#85158) Thanks @NormallyGaussian.
- Google Vertex ADC users get static catalog rows and runtime model resolution again, while single-provider cooldown recovery and memory adapter status checks are more reliable. (#90506, #90609, #90717, #90816) Thanks @849261680.
- Matrix can preflight voice notes before mention gating, preserve thread reads/replies through Matrix relations pagination, and carry QA coverage for voice and thread flows. (#78016, #90415)
- Auth and plugin install state is more durable: auth profiles now live in SQLite, official npm plugin install records keep their trusted pins, and prerelease fallback integrity checks avoid carrying stale integrity forward. (#89102, #88585)
- Agent, tool, and provider loops are stricter around MCP lease timestamps, prompt-cache tool names, local tool catalogs, unreadable dynamic tools, owner-only HTTP tools, and provider catalog metadata, reducing hidden retries and unsafe exposure. (#91124, #91233, #90022, #90261)
- macOS node mode no longer silently self-reconnects away from a healthy direct Gateway session, reducing unexpected companion app session churn. (#90668, #90815) Thanks @vrurg.
- Upgrade and service paths are safer: cron legacy JSON stores migrate during doctor preflight, service env placeholders no longer mask state-dir secrets, WhatsApp startup waits are bounded, and disabled WhatsApp accounts tear down on config reload. (#90072, #90208, #90277, #90488, #90486, #87951, #87965) Thanks @MonkeyLeeT, @sallyom, @mcaxtr, and @MukundaKatta.

### Changes

- Search/providers: add the Parallel bundled web-search plugin, live provider tests, registration contracts, onboarding/docs wiring, and guarded `api.parallel.ai/v1/search` support. (#85158) Thanks @NormallyGaussian.
- Matrix/channels: add voice-message preflight and thread-aware read/reply behavior, including Matrix QA scenario wiring and docs for voice-message behavior. (#78016, #90415)
- Skills/ClawHub: install ClawHub skills backed by GitHub repositories through the resolved install API, download the pinned GitHub commit, keep install-policy checks, and report install telemetry after success. (#90478) Thanks @Patrick-Erichsen.
- Google Chat/channels: add native approval card actions and click handling so Google Chat approvals use platform-native cards instead of generic message flow.
- Mobile: Android provider/model screens now surface expiring, unavailable, unresolved, and attention states more clearly, Android adds theme mode selection, and iOS settings and Talk tabs keep diagnostics, gateway rows, attachment labels, fallback copy, and unavailable Talk controls reachable. (#90752, #91201)
- Memory: QMD search can use the new rerank toggle, and memory adapter status uses the resolved default model identity when checking plain status. (#61834)
- Docs/tooling: add Parallel search docs, refresh weather-skill guidance toward `web_fetch`, clarify legacy `openai-codex` auth, document release/test helper scripts, and tighten changed-test routing docs for CI/debugging work. (#90028, #90250) Thanks @fuller-stack-dev.
- Release/process: switch release trains to `YYYY.M.PATCH` monthly patch numbering, keep pre-transition tags compatible, and pin the June 2026 floor at `2026.6.5` after the published beta.
- Release metadata: align OpenClaw, publishable plugin manifests, generated shrinkwraps, app version metadata, iOS release notes, Matrix plugin changelog, and generated release baselines with the `2026.6.5` beta train.
- Platform maintenance: refresh Android, Swift/macOS, Docker, CodeQL, Buildx, Docker build/push, and Codex Action dependencies for this release train. (#74980, #81757, #86481, #86483, #90601)

### Fixes

- Channel content boundaries: QQBot now strips reasoning/thinking tags before sending, preserving final answers while hiding internal model narration from users. (#89913, #90132) Thanks @openperf.
- Agents/MCP/providers: coerce non-text/image MCP tool-result blocks before they reach provider converters, preserving valid images and turning richer MCP content into text instead of malformed image blocks. (#90710, #90728) Thanks @RanSHammer and @849261680.
- Anthropic/Codex/ACP/agent recovery: defer Anthropic stream start events until `message_start`, strip stale compaction thinking signatures before Anthropic replay, detect unsigned thinking-only stalls, refresh prompt fences after compaction writes, reject empty completion handoffs, preserve parent streaming-off overrides/shared progress commentary, forward heartbeat metadata to context-engine hooks, and cover Codex session/thread migration edge cases. (#90667, #90697, #90163, #90108, #89874, #89505, #90632, #89302, #90729, #90317, #90319) Thanks @openperf, @100yenadmin, and @ooiuuii.
- Agents/Codex/tools: MCP lease release no longer refreshes `lastUsedAt`, prompt-cache tool names are guarded, lean local tool catalogs stay compact, unreadable dynamic tools are quarantined, orphan tool errors still surface, native subagent completion results survive app-server monitoring, and background-session name derivation avoids regex backtracking risk. (#91124, #90612, #90022, #91235, #91233)
- Provider/model resolution: preserve Google Vertex ADC auth markers in generated catalogs, re-probe a single-provider primary after cooldown, share Codex model visibility, fail closed for unknown model auth, preserve Codex alias availability, keep unresolved profile refs unknown, and avoid resolving auth while listing models. (#90506, #90609, #90717, #90702) Thanks @849261680.
- Provider/model resolution: live provider model catalogs keep helper coverage, Ollama catalog metadata is preserved, Google provider prefixes are stripped from Gemini paths, Foundry Responses reasoning replay ids survive, MiniMax M3 thinking stays enabled, Vertex multi-region calls use the right regional host, and OpenRouter streamed generation cost is reconciled. (#91125)
- Gateway/macOS/mobile: avoid duplicate Gateway probe warnings by identity, rate-limit node pairing requests while preserving paired-node reconnects, keep macOS node mode on a healthy direct Gateway session, keep iOS diagnostics and gateway rows reachable, and avoid Linux ARM Gradle resource tasks during Android builds. (#85791, #90147, #90668, #90815) Thanks @giodl73-repo and @vrurg.
- Gateway/security/config: owner-only HTTP tools are gated, sandbox skills remain readable in writable sandboxes, legacy agent registry and Codex model metadata migrate safely, and stalled MCP response bodies time out instead of tying up Gateway workers. (#90261)
- Plugins/Gateway: legacy flat Control UI descriptors from shipped JavaScript plugins now normalize `name` and missing surface fields into session descriptors, restoring Kitchen Sink RPC descriptor proof for package-backed plugin validation.
- TUI/chat/Workboard/auto-reply: optimistic user messages stay stable across stale history reloads, runId reassignment, and abort windows instead of disappearing, jumping, or lingering as ghost rows; Workboard stale lifecycle bulk updates no longer overwrite newer status/provenance; message-tool sends now count as delivery. (#86205, #89600, #88592, #90123) Thanks @RomneyDa.
- Cron/update/service env: doctor config preflight now migrates legacy cron JSON stores into SQLite before runtime reads, isolated agent turn payload messages preserve timeout context, service env planning skips unresolved placeholders that would mask state-dir `.env` values, and session transcript rewrites keep registry markers/discriminants consistent. (#90072, #90208, #91230, #90277, #90488) Thanks @MonkeyLeeT and @sallyom.
- State/storage: Matrix sync and crypto sidecars, memory-wiki import/source-sync state, sandbox registry state, ACPX process state, device-pair notify state, Zalo hosted media, and plugin SDK dedupe state now use SQLite-owned storage instead of ad hoc runtime files. (#91100, #91108, #91056)
- Security/config/tooling: guard MCP HTTP redirects, protect global agent config defaults, and keep release/test/tooling proof failures bounded and explicit. (#89732, #90145)
- Channels: WhatsApp restarts when per-account config changes, bounds background startup waits, closes failed sockets, and preserves reconnect behavior; Mattermost slash commands keep their state on `globalThis`; Feishu streaming cards preserve full merged content; iMessage private-API failures and send timeouts explain themselves while split-send coalescing honors balloon metadata; voice-call tracks Twilio streams after connect; ClickClack reply tools respect `toolsAllow`; Discord runtime adapters stay resolvable; and outbound delivery retries survive budget deferrals. (#87951, #87965, #90486, #68113, #90534, #90181, #90607, #89500, #91041, #90858, #91119, #91241) Thanks @MukundaKatta, @mcaxtr, @infoanton, @mushuiyu886, and @sahibzada-allahyar.
- Release/CI/E2E: main CI guard drift, PR merge diff scoping, live Docker credential staging, base-image qualification, installer Docker classification, Playwright dependency install recovery, API-key auth for Codex live Docker lanes, Parallels option terminators, and JSON-mode progress handling are tighter so release proof fails cleaner. (#90532, #90287, #90058) Thanks @RomneyDa, @hxy91819, and @mrunalp.
- Release/CI/E2E: installed-package root dist verification now allows the current package's JavaScript file count while keeping dependency, per-file-size, and scan-bound checks active.
- Release/CI/E2E: Chutes OAuth model-discovery proof now accepts standard `Headers` requests, and QR package install smoke caps Docker CPU requests to the hosted runner capacity so beta validation fails on real package regressions.
- Release/CI/E2E: Matrix and Slack release validation fixtures now seed SQLite-backed session metadata, keeping channel proof aligned with the current session store.
- Release/CI/E2E: Matrix exec approval and WhatsApp group activation release fixtures now seed SQLite-backed session metadata, and QA Lab capability-flip proof tolerates restart-aborted waits only after restored image media proof lands.
- Release/CI/E2E: Discord native `/think` autocomplete release fixtures now seed SQLite-backed session overrides, keeping provider-specific reasoning choices aligned with the current session store.
- Release/CI/E2E: Telegram native approval release fixtures now seed SQLite-backed session origin metadata, keeping plugin approval routing aligned with the current session store.
- Release/CI/E2E: Memory Core dreaming release fixtures now seed SQLite-backed session metadata, keeping stale dreaming cleanup and session ingestion proof aligned with the current session store.
- Release/CI/E2E: Docker E2E and live Docker harness runs now apply default memory, CPU, and process ceilings while preserving explicit per-lane overrides.
- Release/CI/E2E: Docker E2E CPU limits now cap to the runner capacity, keeping package Telegram acceptance on hosted 8-vCPU runners focused on package regressions instead of impossible Docker resource requests.
- Release/CI/E2E: task maintenance release checks now reset pinned config and one-time session migration state around isolated temp state dirs, keeping normal CI focused on the active session-store fixture instead of stale process snapshots.
- Release/CI/E2E: plugin lifecycle matrix resource sampling now fails phases that exceed RSS, wall-clock, or CPU ceilings instead of only logging the measurements.
- Release/CI/E2E: Codex npm plugin live assertions now cap transcript discovery and diagnostic log reads so failure proof stays bounded.
- Release/CI/E2E: browser snapshot, release-scenario, release-user-journey, Telegram desktop/RTT/package, web-search, Parallels update, plugin update, doctor switch, and upgrade-survivor diagnostics now stream or bound log/artifact reads so failed proof stays inspectable without unbounded output.
- Tests/state isolation: QA Lab valid-tool-call metrics now require runtime tool-call evidence when runtime parity data is available instead of counting tool-backed scenario pass status alone.
- Tests/state isolation: QA Lab runtime parity now fails planned-only tool-call rows without matching tool results instead of treating matching mock plans as real tool evidence.
- Tests/state isolation: QA Lab runtime parity now treats matching controlled tool errors as equivalent and falls back to transcript tool results when mock debug rows miss async image-generation starts.
- Tests/state isolation: QA suites now fail closed on skipped summaries, missing runtime tool proof, planned-only rows, loose release limits, missing live/provider artifacts, failed agent reply markers, and package Telegram summary failures.
- Tests/state isolation: provider, media, auth, cron, task, session, sandbox, Gateway, and Codex timeout fixtures now scope more home/state/env data per test, reducing cross-test leakage and making release validation failures less noisy. (#90027, #89974)

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.5-beta.5
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.5-beta.5.tgz
- integrity: `sha512-xyh5/CLaxdm9Zh2VBnmS2wxYR6kcqIrMFXNTWklJbVHSmmkLy7HRH6Rnw0cm4pRUXOvh3WQUDJgOqQOjjxG6PQ==`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.6.5-beta.5/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/27171268701
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27169704715
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27169706642
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27171395546
- plugin ClawHub publish: https://github.com/openclaw/openclaw/actions/runs/27171399026
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27171782461
- npm Telegram beta E2E: not supplied


## Recent issue risk signals

- #91522 [no-labels] member-info fails with "fetch failed" on WSL2 in 2026.6.1 (SSRF fetch guard / undici dispatcher regression) — https://github.com/openclaw/openclaw/issues/91522
- #91035 [bug, regression, P2, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit, impact:other] [Bug]: Build fails on v2026.6.1 — https://github.com/openclaw/openclaw/issues/91035
- #91521 [bug] [Bug]: Tailscale + Control UI Token mode cause images can't load — https://github.com/openclaw/openclaw/issues/91521
- #79223 [stale] Feature request: configurable Dream Diary language / prompt — https://github.com/openclaw/openclaw/issues/79223
- #91518 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:message-loss, issue-rating: 🐚 platinum hermit] Durable inbound receive journal for Slack channel (parity with Telegram ingress spool) — https://github.com/openclaw/openclaw/issues/91518
- #91517 [P1, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:crash-loop, issue-rating: 🦞 diamond lobster] getSubagentRunsSnapshotForRead does an uncached full SQLite re-read on every call; many consumers drive it to ~22 Hz and pin a CPU core — https://github.com/openclaw/openclaw/issues/91517
- #90083 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:auth-provider, issue-rating: 🐚 platinum hermit] [Bug]: 2026.6.1 OpenAI ChatGPT Responses transport fails with invalid_provider_content_type for gpt-5.4/gpt-5.5 — https://github.com/openclaw/openclaw/issues/90083
- #91514 [no-labels] ACP: effort config option sent to Claude Haiku causes "Unknown config option: effort" — https://github.com/openclaw/openclaw/issues/91514
- #91513 [P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:auth-provider, issue-rating: 🦞 diamond lobster] ACP: model prefix not stripped when dispatching to Claude ACP adapter — Cannot replay saved model "anthropic/claude-sonnet-4-6" — https://github.com/openclaw/openclaw/issues/91513

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #83169 draft=False Discord: add reaction notification wake policy — https://github.com/openclaw/openclaw/pull/83169
- PR #90500 draft=False Fix stale session routes for removed providers — https://github.com/openclaw/openclaw/pull/90500
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #91520 draft=False fix(control-ui): show agents as a visible list instead of a dropdown — https://github.com/openclaw/openclaw/pull/91520
- PR #91519 draft=False feat(qa-lab): add Codex Slack approval scenarios — https://github.com/openclaw/openclaw/pull/91519
- PR #91478 draft=False block unauthorized Telegram DM text from prompt context — https://github.com/openclaw/openclaw/pull/91478
- PR #90666 draft=False fix(cron): cancel active cron task runs — https://github.com/openclaw/openclaw/pull/90666
- PR #88815 draft=False feat: channel echo / session pinning — https://github.com/openclaw/openclaw/pull/88815
- PR #90759 draft=False fix #76888: [Bug]: Queued/orphaned user-message merge can produce stale reply — https://github.com/openclaw/openclaw/pull/90759
- PR #89040 draft=False perf: avoid event-loop stall during embedded_run bootstrap-context — https://github.com/openclaw/openclaw/pull/89040
- PR #91499 draft=False fix(cron): preserve scheduled turn tool policy [AI] — https://github.com/openclaw/openclaw/pull/91499
- PR #85249 draft=False fix(cron): guard against undefined sourceDelivery in isolated executor — https://github.com/openclaw/openclaw/pull/85249
- PR #91515 draft=False fix(cron): classify spaced 'timed out' failures as retryable timeout — https://github.com/openclaw/openclaw/pull/91515
- PR #88796 draft=False fix(discord): resolve guildId from session channel for search actions — https://github.com/openclaw/openclaw/pull/88796
- PR #83988 draft=False fix(tts): defer text settlement for final-mode TTS to eliminate churn (#83511) — https://github.com/openclaw/openclaw/pull/83988
- PR #91010 draft=False fix(memory): honor local model path in index identity — https://github.com/openclaw/openclaw/pull/91010
- PR #90035 draft=False fix(sqlite): support Node 23.0–23.10 runtimes lacking StatementSync.columns() — https://github.com/openclaw/openclaw/pull/90035
- PR #82955 draft=False fix(install): validate downloaded scripts before execution — https://github.com/openclaw/openclaw/pull/82955
- PR #91507 draft=False Canonicalize Codex protocol JSON asset ordering — https://github.com/openclaw/openclaw/pull/91507
- PR #86649 draft=False fix: relay Claude CLI assistant partial messages as streaming deltas — https://github.com/openclaw/openclaw/pull/86649
- PR #91080 draft=False feat(gateway): startup watchdog dumps in-flight phases on hang — https://github.com/openclaw/openclaw/pull/91080
- PR #91509 draft=False Update Google Meet chrome-node invoke policy [AI] — https://github.com/openclaw/openclaw/pull/91509
- PR #90060 draft=False fix(edit): preserve unrelated lines during fuzzy text matching — https://github.com/openclaw/openclaw/pull/90060
- PR #91511 draft=False fix(ui): keep mobile composer above keyboard — https://github.com/openclaw/openclaw/pull/91511
- PR #91510 draft=False Add claw score taxonomy — https://github.com/openclaw/openclaw/pull/91510
- PR #89517 draft=True [codex] fix gateway hot-mode restart reloads — https://github.com/openclaw/openclaw/pull/89517
- PR #91408 draft=False feat(channels/acp): support ACP bindings for direct-message peers — https://github.com/openclaw/openclaw/pull/91408
- PR #89526 draft=True [codex] fix gateway restart-required reload drift — https://github.com/openclaw/openclaw/pull/89526
- PR #91452 draft=False Add claw-score agent skill — https://github.com/openclaw/openclaw/pull/91452
- PR #56674 draft=False feat(openresponses): return reasoning/thinking content in /v1/responses output — https://github.com/openclaw/openclaw/pull/56674
