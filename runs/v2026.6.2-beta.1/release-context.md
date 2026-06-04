# Release Context — OpenClaw `v2026.6.2-beta.1`

Fetched at: `2026-06-04T00:00:47Z`

## Target

- Target tag: `v2026.6.2-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.2-beta.1
- Target tag SHA: f03f57aa2a0a381bed0fdefd98ac583cb13f4472

## Freshness baselines

- Latest beta tag: `v2026.6.2-beta.1`
- Latest alpha tag: `v2026.6.3-alpha.1`
- Stable baseline: `v2026.6.1`
- Prior prerelease baseline: `v2026.6.1-beta.3`

## Release notes excerpt

## 2026.6.2

### Highlights

- Plugin and skill installs now use an operator install policy instead of the old dangerous-code scanner path, with clearer doctor, CLI, ClawHub, and troubleshooting surfaces for package, archive, source, upload, and marketplace installs. (#89516) Thanks @joshavant.
- Telegram, Feishu, Discord, WhatsApp, and outbound delivery paths got safer around duplicate transcript mirrors, Telegram admin writeback, streamed-final previews, approval allowlists, setup runtime state, poll modifiers, Discord voice errors, and internal progress traces. (#88973, #89626, #89812, #89035, #89814, #89813, #89601) Thanks @pgondhi987, @Petru2224, @zhangguiping-xydt, @codezz, and @takhoffman.
- Chat, Control UI, Skill Workshop, Workboard, Android companion shell, and WebChat flows now preserve visible streaming text, reconcile completed sends, expose ACK timing, add Workboard keyboard movement, harden dialog accessibility, lazy-load usage views, keep current chat toggles working, and improve Android companion-first shell navigation. (#89801, #89777, #89802) Thanks @vincentkoc.
- Security, policy, and config recovery now reject corrupt shell snapshots, unsupported policy keys, unsafe exec approval precheck environments, malformed script limits, and suspicious gateway startup configs while adding data-handling conformance checks. (#89701, #87074, #81488, #87056, #89480) Thanks @RomneyDa, @giodl73-repo, and @mmaps.
- Gateway, agent, Codex, provider, model, and memory paths now recover session write-lock release failures, abandoned Codex app-server startups, stream-to-parent ACP spawns, custom-provider runtime fanout, bundled provider aliases, prompt-cache boundaries, Gemini stop sequences, Kimi cache markers, and watcher pressure warnings. (#89811, #89244) Thanks @RomneyDa and @takhoffman.
- Release, CI, Docker, Crabbox/Testbox, package, and E2E validation lanes now bound more network calls, malformed numeric limits, process groups, cleanup leaks, package hydration paths, Windows installer publishing, release asset verification, and log drains so failures produce bounded proof instead of hanging.

### Changes

- Plugins/security: replace dangerous-code scanner enforcement with operator install policy, install-policy context, doctor checks, install/update CLI wiring, ClawHub metadata paths, and package/archive/source/upload lifecycle coverage. (#89516) Thanks @joshavant.
- Policy: add data-handling conformance checks and reject unsupported policy keys. (#87056, #87074) Thanks @giodl73-repo.
- Telegram/channels: show commentary and reasoning in progress drafts, share progress draft compositors across channel plugins, and keep Telegram polling stop/reset boundaries cheaper and more reliable.
- UI/mobile: add Workboard keyboard movement controls, tighten Workboard card operations, improve Android companion-first shell UX, and document chat ACK timing metadata. (#89802) Thanks @vincentkoc.
- Release metadata: align the root package, publishable plugin manifests, generated shrinkwraps, appcast, iOS, Android, macOS, Matrix plugin changelog, and docs/generated baselines with the 2026.6.2 beta train.
- Release/packaging: promote Windows node installer publishing, require verified Windows release asset links, and document GitHub release-note edits.
- Docs: refresh Windows Hub setup guidance and document Gateway, CLI, and plugin SDK helper contracts.

### Fixes

- Channels/outbound: keep channel sends durable when transcript mirroring fails, stop schema-padded poll modifiers from blocking normal sends, preserve WebChat `sessions_send` handoffs, preserve Discord channel-label suppression while hiding internal agent failure traces, match Discord libopus error shapes, and sanitize Discord tool progress scaffolding. (#89626, #89812, #89601) Thanks @Petru2224, @codezz, and @takhoffman.
- Telegram/Feishu: require admin rights for Telegram target writeback, keep Telegram DM exec approval allowlists working with `ask:off`, prevent Telegram preview duplication across streaming modes, isolate verbose status after streamed finals, cancel clean restart stop timers, slow polling restart storms, and wire Feishu setup runtime setters. (#88973, #89035, #89813, #89814) Thanks @pgondhi987, @zhangguiping-xydt, and @takhoffman.
- Chat/UI/Gateway: preserve visible chat stream text, clear stale stream buffers before terminal commits, reconcile completed sends, scroll pending sends into view, harden Workboard dialog accessibility, stabilize WebChat prompt-cache affinity, overlap chat catalog startup, render chat history incrementally, lazy-load usage dashboard, and report gateway health auth diagnostics. (#89337) Thanks @RomneyDa.
- Agents/Codex/providers/models: release session write locks when prompt-release fence reads fail, retire abandoned Codex app-server startups, keep stream-to-parent ACP spawns registered, close Codex startup clients on timeout, recover bundled provider aliases, avoid custom-provider runtime fanout, preserve provider prompt-cache boundaries, forward Gemini stop sequences, and strip Kimi-incompatible Anthropic cache markers. (#89811) Thanks @takhoffman.
- Memory/build/update: warn after startup watcher pressure checks, externalize optional Baileys image backends, restore and pin Canvas A2UI compatibility assets, keep plugin repair fetch failures nonblocking, restore Skill Workshop view switching, and keep the current chat toggle active after awaited session switches. (#89244) Thanks @RomneyDa.
- Security/config/tooling: reject corrupt shell snapshots, suspicious gateway startup configs, malformed release/test/tooling/Docker/perf numeric limits, oversized audit responses, unsafe exec precheck env, and invalid pending-agent SQLite scaffold denials. (#89701, #89705, #89480, #81488) Thanks @RomneyDa and @mmaps.
- Release/CI/E2E: restore package changelog extraction after the post-2026.6.1 version bump, keep hydrated pnpm modules under `node_modules` for ARM/Linux package lifecycle scripts, keep OpenAI live-cache prerequisites advisory while Anthropic prerequisites stay blocking, retry Windows Parallels background log appends on transient file-lock errors, bound candidate GitHub and cross-OS Discord fetches, harden ARM smoke/browser checks, show Docker build heartbeats, reset Crabbox pnpm hydrate state, and isolate Testbox/Docker/release journey artifacts.


### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.2-beta.1
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.2-beta.1.tgz
- integrity: sha512-0lugviNlRNrTTK3Az+aJ/1f9bu7lo1WHwqHO2lkW4GJIV5LT58XhpoXXL3TKzosqJjAjvW4JXJstrK6nhZwpHg==
- full release validation: https://github.com/openclaw/openclaw/actions/runs/26918960809
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/26918964585
- release publish: https://github.com/openclaw/openclaw/actions/runs/26920144100
- release checks: https://github.com/openclaw/openclaw/actions/runs/26919202085
- CI: https://github.com/openclaw/openclaw/actions/runs/26919201946
- plugin prerelease validation: https://github.com/openclaw/openclaw/actions/runs/26919202959
- performance: https://github.com/openclaw/openclaw/actions/runs/26918932463


## Recent issue risk signals

- No recent open issue signals returned.

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #90033 draft=False fix(llm): apply model.compat.sendSessionAffinityHeaders at openai-tra… — https://github.com/openclaw/openclaw/pull/90033
- PR #90064 draft=True fix(plugins): isolate unreadable tool registrations — https://github.com/openclaw/openclaw/pull/90064
- PR #90019 draft=False fix(memory-search): default periodic sync fallback — https://github.com/openclaw/openclaw/pull/90019
- PR #90065 draft=False fix(agents): bound abort-path session lock release; force-release on unsettled retained writes — https://github.com/openclaw/openclaw/pull/90065
- PR #89918 draft=False fix(vertex): route eu/us multi-region to .rep.googleapis.com host — https://github.com/openclaw/openclaw/pull/89918
- PR #90063 draft=False fix(channels): clarify message receipt delivery evidence — https://github.com/openclaw/openclaw/pull/90063
- PR #90003 draft=True feat(policy): cover exec approvals artifact — https://github.com/openclaw/openclaw/pull/90003
- PR #85254 draft=False perf(plugins): thread prepared manifestPlugins through runtime model-id normalize chain — https://github.com/openclaw/openclaw/pull/85254
- PR #77158 draft=False perf(qmd): persistent export-state cache + stat fast path in exportSessions — https://github.com/openclaw/openclaw/pull/77158
- PR #88504 draft=False feat(memory): add multi-slot memory role architecture — https://github.com/openclaw/openclaw/pull/88504
- PR #90062 draft=True fix(agent): infer agent from fresh session keys — https://github.com/openclaw/openclaw/pull/90062
- PR #80013 draft=False perf(usage-cost-cache): throttle full-cache rewrites during refresh — https://github.com/openclaw/openclaw/pull/80013
- PR #73261 draft=False perf(models-config): targetProvider short-circuit with disk-vs-config validation — https://github.com/openclaw/openclaw/pull/73261
- PR #88585 draft=False Pin official npm plugin install records — https://github.com/openclaw/openclaw/pull/88585
- PR #88969 draft=False fix(imessage): persist echo markers before send — https://github.com/openclaw/openclaw/pull/88969
- PR #90061 draft=True fix(agent-runtime): guard prompt cache tool names — https://github.com/openclaw/openclaw/pull/90061
- PR #88245 draft=False refactor(whatsapp): introduce inbound message contexts — https://github.com/openclaw/openclaw/pull/88245
- PR #73260 draft=False perf(models-config): content-hash auth-profiles + models.json drift detection — https://github.com/openclaw/openclaw/pull/73260
- PR #90060 draft=False fix(edit): preserve unrelated lines during fuzzy text matching — https://github.com/openclaw/openclaw/pull/90060
- PR #90055 draft=False chore(deps): bump the actions group across 1 directory with 5 updates — https://github.com/openclaw/openclaw/pull/90055
- PR #86655 draft=False feat(claude): add claude-bridge app-server harness extension — https://github.com/openclaw/openclaw/pull/86655
- PR #90058 draft=False fix(docker): qualify base image refs for podman short-name mode — https://github.com/openclaw/openclaw/pull/90058
- PR #90059 draft=True fix(plugins): isolate tool metadata rows — https://github.com/openclaw/openclaw/pull/90059
- PR #90053 draft=False fix: hide Skill Workshop revision handoff from chat — https://github.com/openclaw/openclaw/pull/90053
- PR #89978 draft=False perf(config): dedupe plugin auto-enable fanout work — https://github.com/openclaw/openclaw/pull/89978
- PR #90056 draft=False fix(doctor): merge disjoint openai-codex model entries into canonical openai provider — https://github.com/openclaw/openclaw/pull/90056
- PR #90057 draft=False Polish Workboard operations view — https://github.com/openclaw/openclaw/pull/90057
- PR #90035 draft=False fix(sqlite): support Node 23.0–23.10 runtimes lacking StatementSync.columns() — https://github.com/openclaw/openclaw/pull/90035
- PR #63919 draft=False feat(gateway): wire coding tools into /tools/invoke HTTP surface — https://github.com/openclaw/openclaw/pull/63919
- PR #86483 draft=False chore(deps): bump the swift-deps group across 1 directory with 3 updates — https://github.com/openclaw/openclaw/pull/86483
