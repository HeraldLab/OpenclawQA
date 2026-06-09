# Release Context — OpenClaw `v2026.6.5-beta.6`

Fetched at: `2026-06-09T09:00:36Z`

## Target

- Target tag: `v2026.6.5-beta.6`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.6
- Target tag SHA: 1514dc740a2e74c47e87cb7436a88a412044a3bd

## Freshness baselines

- Latest beta tag: `v2026.6.5-beta.6`
- Latest alpha tag: `v2026.6.9-alpha.1`
- Stable baseline: `v2026.6.1`
- Prior prerelease baseline: `v2026.6.5-beta.5`

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
- Skills/ClawHub: avoid one filesystem watcher per skill file during refresh, keeping large skill trees from exhausting watcher limits.
- Google Chat/channels: add native approval card actions and click handling so Google Chat approvals use platform-native cards instead of generic message flow.
- Mobile: Android provider/model screens now surface expiring, unavailable, unresolved, and attention states more clearly, Android adds theme mode selection, and iOS settings and Talk tabs keep diagnostics, gateway rows, attachment labels, fallback copy, and unavailable Talk controls reachable. (#90752, #91201)
- Memory: QMD search can use the new rerank toggle, and memory adapter status uses the resolved default model identity when checking plain status. (#61834)
- Docs/tooling: add Parallel search docs, refresh weather-skill guidance toward `web_fetch`, clarify legacy `openai-codex` auth, document release/test helper scripts, and tighten changed-test routing docs for CI/debugging work. (#90028, #90250) Thanks @fuller-stack-dev.
- Release/process: switch release trains to `YYYY.M.PATCH` monthly patch numbering, keep pre-transition tags compatible, and pin the June 2026 floor at `2026.6.5` after the published beta.
- Release/process: defer the session-metadata SQLite migration from the `2026.6.5` beta train so this release keeps the existing JSON-backed session metadata path while the migration risk is worked on `main`.
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
- Gateway/config: `config.patch` now preserves explicit array replacement semantics for arrays without merge keys, so replacement patches do not accidentally merge stale entries. (#91551)
- SDK: event pump failures now surface to clients instead of being swallowed behind a quiet iterator shutdown.
- Agents/transcripts: inline image payload redaction now catches data URLs and repaired transcript images before they can leak raw image bytes into stored or exported transcripts. (#91529)
- Plugins/Gateway: legacy flat Control UI descriptors from shipped JavaScript plugins now normalize `name` and missing surface fields into session descriptors, restoring Kitchen Sink RPC descriptor proof for package-backed plugin validation.
- TUI/chat/Workboard/auto-reply: optimistic user messages stay stable across stale history reloads, runId reassignment, and abort windows instead of disappearing, jumping, or lingering as ghost rows; Workboard stale lifecycle bulk updates no longer overwrite newer status/provenance; message-tool sends now count as delivery. (#86205, #89600, #88592, #90123) Thanks @RomneyDa.
- Cron/update/service env: doctor config preflight now migrates legacy cron JSON stores into SQLite before runtime reads, isolated agent turn payload messages preserve timeout context, service env planning skips unresolved placeholders that would mask state-dir `.env` values, and session transcript rewrites keep registry markers/discriminants consistent. (#90072, #90208, #91230, #90277, #90488) Thanks @MonkeyLeeT and @sallyom.
- State/storage: Matrix sync and crypto sidecars, memory-wiki import/source-sync state, sandbox registry state, ACPX process state, device-pair notify state, Zalo hosted media, and plugin SDK dedupe state now use SQLite-owned storage instead of ad hoc runtime files. (#91100, #91108, #91056)
- Security/config/tooling: guard MCP HTTP redirects, protect global agent config defaults, and keep release/test/tooling proof failures bounded and explicit. (#89732, #90145)
- Channels: WhatsApp restarts when per-account config changes, bounds background startup waits, closes failed sockets, and preserves reconnect behavior; Mattermost slash commands keep their state on `globalThis`; Feishu streaming cards preserve full merged content; iMessage private-API failures and send timeouts explain themselves while split-send coalescing honors balloon metadata; voice-call tracks Twilio streams after connect; ClickClack reply tools respect `toolsAllow`; Discord runtime adapters stay resolvable; and outbound delivery retries survive budget deferrals. (#87951, #87965, #90486, #68113, #90534, #90181, #90607, #89500, #91041, #90858, #91119, #91241) Thanks @MukundaKatta, @mcaxtr, @infoanton, @mushuiyu886, and @sahibzada-allahyar.
- Feishu: retry transient send rate-limit errors (HTTP 429, per-chat code 230020, tenant-level code 11232) with linear backoff, including SDK responses that fulfill with rate-limit bodies instead of throwing, and route streaming-card sends through the retry wrapper. (#89659) Thanks @ladygege.
- WhatsApp: captured replies after restart now route through the successor controller instead of the stale pre-restart controller. (#85823)
- Release/CI/E2E: main CI guard drift, PR merge diff scoping, live Docker credential staging, base-image qualification, installer Docker classification, Playwright dependency install recovery, API-key auth for Codex live Docker lanes, Parallels option terminators, and JSON-mode progress handling are tighter so release proof fails cleaner. (#90532, #90287, #90058) Thanks @RomneyDa, @hxy91819, and @mrunalp.
- Release/CI/E2E: installed-package root dist verification now allows the current package's JavaScript file count while keeping dependency, per-file-size, and scan-bound checks active.
- Release/CI/E2E: Chutes OAuth model-discovery proof now accepts standard `Headers` requests, and QR package install smoke caps Docker CPU requests to the hosted runner capacity so beta validation fails on real package regressions.
- Release/CI/E2E: Docker E2E and live Docker harness runs now apply default memory, CPU, and process ceilings while preserving explicit per-lane overrides.
- Release/CI/E2E: Docker E2E CPU limits now cap to the runner capacity, keeping package Telegram acceptance on hosted 8-vCPU runners focused on package regressions instead of impossible Docker resource requests.
- Release/CI/E2E: task maintenance release checks now reset pinned config around isolated temp state dirs, keeping normal CI focused on the active session-store fixture instead of stale process snapshots.
- Release/CI/E2E: plugin lifecycle matrix resource sampling now fails phases that exceed RSS, wall-clock, or CPU ceilings instead of only logging the measurements.
- Release/CI/E2E: Codex npm plugin live assertions now cap transcript discovery and diagnostic log reads so failure proof stays bounded.
- Release/CI/E2E: browser snapshot, release-scenario, release-user-journey, Telegram desktop/RTT/package, web-search, Parallels update, plugin update, doctor switch, and upgrade-survivor diagnostics now stream or bound log/artifact reads so failed proof stays inspectable without unbounded output.
- Release/CI/E2E: ClawHub publish jobs prepare dependencies after checking out the target ref, and Docker store seed package discovery now targets the intended production packages. (#91547)
- Release/CI/E2E: QA Lab capability-flip release validation now marks intentional `tools.deny` restores as array replacements, so beta validation fails only on real capability regressions.
- Tests/state isolation: QA Lab valid-tool-call metrics now require runtime tool-call evidence when runtime parity data is available instead of counting tool-backed scenario pass status alone.
- Tests/state isolation: QA Lab runtime parity now fails planned-only tool-call rows without matching tool results instead of treating matching mock plans as real tool evidence.
- Tests/state isolation: QA Lab runtime parity now treats matching controlled tool errors as equivalent and falls back to transcript tool results when mock debug rows miss async image-generation starts.
- Tests/state isolation: QA suites now fail closed on skipped summaries, missing runtime tool proof, planned-only rows, loose release limits, missing live/provider artifacts, failed agent reply markers, and package Telegram summary failures.
- Tests/state isolation: provider, media, auth, cron, task, session, sandbox, Gateway, and Codex timeout fixtures now scope more home/state/env data per test, reducing cross-test leakage and making release validation failures less noisy. (#90027, #89974)
- Sessions: the beta SQLite downgrade rescue now skips extra pre-reads for active non-empty JSON session stores, preserving cache race detection while still restoring missing or empty beta session files.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.5-beta.6
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.5-beta.6.tgz
- integrity: `sha512-jwz9IP/LbR6qgS5SUTpgeBArNf2eIM+8jc7LCEMAMQznsznjml/7IrsxBn2S89XieEX6BEhGVtjspOOJt0jVXg==`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.6.5-beta.6/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/27193326577
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27191457144
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27191453479
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27193511392
- plugin ClawHub publish: dispatched separately, not awaited by this proof: https://github.com/openclaw/openclaw/actions/runs/27193515101
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27193906215
- npm Telegram beta E2E: not supplied


## Recent issue risk signals

- #90911 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Feature]: Record token usage on task_runs / subagent_runs (parity with cron_run_logs.total_tokens) — https://github.com/openclaw/openclaw/issues/90911
- #91664 [bug, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, impact:data-loss, issue-rating: 🐚 platinum hermit] [Bug]:  Dashboard session labels lost after gateway restart or Control UI reconnect — https://github.com/openclaw/openclaw/issues/91664
- #48003 [P1, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] Steer mode does not inject messages mid-turn for main sessions — https://github.com/openclaw/openclaw/issues/48003
- #91016 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:auth-provider, issue-rating: 🐚 platinum hermit] ⚠️ 升级 2026.6.1 后 DeepSeek Prompt Cache 完全失效，一小时烧掉约 $6 — https://github.com/openclaw/openclaw/issues/91016

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #91028 draft=True feat(lobster): in-process LLM adapters for embedded runner (#90909) — https://github.com/openclaw/openclaw/pull/91028
- PR #91657 draft=False fix(ollama): use provider thinking default in SDK session factory — https://github.com/openclaw/openclaw/pull/91657
- PR #91668 draft=False fix(agents): skip stale orphaned subagent sessions during restart recovery — https://github.com/openclaw/openclaw/pull/91668
- PR #85104 draft=False feat: fast talks auto mode — https://github.com/openclaw/openclaw/pull/85104
- PR #91438 draft=False feat(voice-call): Microsoft Teams provider — CVI voice/video calls — https://github.com/openclaw/openclaw/pull/91438
- PR #88709 draft=False fix(auth): cooldown inline api key billing failures — https://github.com/openclaw/openclaw/pull/88709
- PR #91667 draft=False fix(android): queue notification events until node connect — https://github.com/openclaw/openclaw/pull/91667
- PR #91478 draft=False block unauthorized Telegram DM text from prompt context — https://github.com/openclaw/openclaw/pull/91478
- PR #90500 draft=False Fix stale session routes for removed providers — https://github.com/openclaw/openclaw/pull/90500
- PR #91666 draft=False chore(deps): bump useblacksmith/setup-docker-builder from 1.8.0 to 1.9.0 in the actions group — https://github.com/openclaw/openclaw/pull/91666
- PR #91665 draft=False docs: fix release CI Android dispatch guidance — https://github.com/openclaw/openclaw/pull/91665
- PR #91663 draft=False fix(backup): clean up stale .tmp archives from interrupted runs before creating new backup — https://github.com/openclaw/openclaw/pull/91663
- PR #78715 draft=False Fix minor grammar issue in plugin documentation (capabilities plural) — https://github.com/openclaw/openclaw/pull/78715
- PR #90310 draft=False fix(openai-responses): sanitize null content before SDK serialization (#90094) — https://github.com/openclaw/openclaw/pull/90310
- PR #91658 draft=False feat(gateway): forward generic clientContext onto diagnostic events — https://github.com/openclaw/openclaw/pull/91658
- PR #90121 draft=False fix(memory): write dream fallback without subagent runtime — https://github.com/openclaw/openclaw/pull/90121
- PR #91644 draft=False feat(gateway): add OpenAI-compatible /v1/audio/speech endpoint — https://github.com/openclaw/openclaw/pull/91644
- PR #91653 draft=False fix(control-ui): wire ui.seamColor from bootstrap config to CSS variables — https://github.com/openclaw/openclaw/pull/91653
- PR #91648 draft=False [codex] Fix CLI plugin install hook bootstrap — https://github.com/openclaw/openclaw/pull/91648
- PR #91093 draft=False Feat/acp hub delegated sessions — https://github.com/openclaw/openclaw/pull/91093
- PR #91660 draft=False [AI] fix(memory): backfill provider.model with resolved model name in… — https://github.com/openclaw/openclaw/pull/91660
- PR #91661 draft=False chore(plugin-sdk): refresh API baseline hash — https://github.com/openclaw/openclaw/pull/91661
- PR #90782 draft=False perf(tui): prewarm runtime plugins before first send — https://github.com/openclaw/openclaw/pull/90782
- PR #72677 draft=False fix(cron): warn on main heartbeat handoff ghost runs — https://github.com/openclaw/openclaw/pull/72677
- PR #90960 draft=False fix(google): enable vertex image and video generation — https://github.com/openclaw/openclaw/pull/90960
- PR #87255 draft=False fix(config): skip .openclaw append when OPENCLAW_HOME already names a state dir (#45765) — https://github.com/openclaw/openclaw/pull/87255
- PR #91646 draft=False fix(browser): remove dead void requireRef in navigation registration — https://github.com/openclaw/openclaw/pull/91646
- PR #91656 draft=False test(cron): expand parseAbsoluteTimeMs test coverage to 39 cases — https://github.com/openclaw/openclaw/pull/91656
- PR #91345 draft=False fix: suggest close CLI commands — https://github.com/openclaw/openclaw/pull/91345
