# Release Context — OpenClaw `v2026.6.5-beta.2`

Fetched at: `2026-06-07T00:30:35Z`

## Target

- Target tag: `v2026.6.5-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.2
- Target tag SHA: 131c9bf4c814d02636072df2235c9b5856f59566

## Freshness baselines

- Latest beta tag: `v2026.6.5-beta.2`
- Latest alpha tag: `v2026.6.6-alpha.1`
- Stable baseline: `v2026.6.1`
- Prior prerelease baseline: `v2026.6.5-beta.1`

## Release notes excerpt


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
- Release/process: switch release trains to `YYYY.M.PATCH` monthly patch numbering, keep pre-transition tags compatible, and pin the June 2026 floor at `2026.6.5` after the published beta.
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

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.5-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.5-beta.2.tgz
- integrity: `sha512-6Bmx2rlReO1MOEi9ehuhsVO59keQ1xQQ8/PvwbNq0CatJkNwyCX/MBlhWrscByYAmBl6JCOSr+cLejoDk1sDBA==`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.6.5-beta.2/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/27077488131
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27076839788
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27076840299
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27077565695
- plugin ClawHub publish: dispatched separately, not awaited by this proof: https://github.com/openclaw/openclaw/actions/runs/27077567167
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27077747897
- npm Telegram beta E2E: not supplied


## Recent issue risk signals

- #91043 [no-labels] Reply target: ReplyToQuoteText short-circuits ReplyToBody and loses the rest of the replied-to message — https://github.com/openclaw/openclaw/issues/91043
- #91042 [no-labels] Reply-context body truncation: cover ReplyChain and fallback ReplyToBody JSON paths — https://github.com/openclaw/openclaw/issues/91042
- #91035 [bug, regression, P2, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit, impact:other] [Bug]: Build fails on v2026.6.1 — https://github.com/openclaw/openclaw/issues/91035
- #91036 [enhancement, P3, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, issue-rating: 🌊 off-meta tidepool, impact:other] [Feature]: web界面的右侧workspace里的文件显示栏 强烈建议增加按钮可以自动隐去 看着太烦了。 — https://github.com/openclaw/openclaw/issues/91036
- #90981 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] [Feature] sessions_history: add pagination/offset and export support — https://github.com/openclaw/openclaw/issues/90981

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #85155 draft=False fix(agents): avoid inviting provider swaps in model alias guidance — https://github.com/openclaw/openclaw/pull/85155
- PR #83988 draft=False fix(tts): defer text settlement for final-mode TTS to eliminate churn (#83511) — https://github.com/openclaw/openclaw/pull/83988
- PR #91026 draft=True feat(talk): add macOS realtime relay mode — https://github.com/openclaw/openclaw/pull/91026
- PR #79397 draft=False fix(nextcloud-talk): parse structured mention payloads — https://github.com/openclaw/openclaw/pull/79397
- PR #87909 draft=False fix(inbound-meta): head+tail truncation for reply context body preserves actionable tail content — https://github.com/openclaw/openclaw/pull/87909
- PR #90328 draft=False Expose model picker agent runtimes — https://github.com/openclaw/openclaw/pull/90328
- PR #90794 draft=False fix(outbound): materialize buffer-only message.send attachments — https://github.com/openclaw/openclaw/pull/90794
- PR #84017 draft=False fix(gateway): bind MCP loopback scope to tokens — https://github.com/openclaw/openclaw/pull/84017
- PR #85993 draft=False feat(browser): expand Chrome MCP web capabilities — https://github.com/openclaw/openclaw/pull/85993
- PR #90872 draft=False fix: surface safe terminal tool fallbacks — https://github.com/openclaw/openclaw/pull/90872
- PR #89045 draft=False fix: recover terminal session status on visible inbound turns — https://github.com/openclaw/openclaw/pull/89045
- PR #86627 draft=False Keep core doctor health in contribution order — https://github.com/openclaw/openclaw/pull/86627
- PR #91041 draft=False fix(imessage): self-explaining private-API failures and dedicated send timeout — https://github.com/openclaw/openclaw/pull/91041
- PR #88796 draft=False fix(discord): resolve guildId from session channel for search actions — https://github.com/openclaw/openclaw/pull/88796
- PR #90994 draft=True fix(codex): restore native PreToolUse relay delivery — https://github.com/openclaw/openclaw/pull/90994
- PR #85254 draft=False perf(plugins): thread prepared manifestPlugins through runtime model-id normalize chain — https://github.com/openclaw/openclaw/pull/85254
- PR #90101 draft=False feat: add runtime self context config and tool — https://github.com/openclaw/openclaw/pull/90101
- PR #89659 draft=False fix(feishu): retry on send rate-limit errors (230020/230006) — https://github.com/openclaw/openclaw/pull/89659
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #85249 draft=False fix(cron): guard against undefined sourceDelivery in isolated executor — https://github.com/openclaw/openclaw/pull/85249
- PR #77158 draft=False perf(qmd): persistent export-state cache + stat fast path in exportSessions — https://github.com/openclaw/openclaw/pull/77158
- PR #91031 draft=True [codex] Add OpenRouter OAuth login — https://github.com/openclaw/openclaw/pull/91031
- PR #91037 draft=False fix(config): allow thinkingLevelMap in persisted model schema — https://github.com/openclaw/openclaw/pull/91037
- PR #91010 draft=False fix(memory): honor local model path in index identity — https://github.com/openclaw/openclaw/pull/91010
- PR #71856 draft=False Fix TUI startup summary scoping — https://github.com/openclaw/openclaw/pull/71856
- PR #91032 draft=False docs(imessage): require DisableLibraryValidation on modern macOS; document macOS 26 injection gates — https://github.com/openclaw/openclaw/pull/91032
- PR #91028 draft=True feat(lobster): in-process LLM adapters for embedded runner (#90909) — https://github.com/openclaw/openclaw/pull/91028
- PR #90752 draft=False feat(android): add theme mode selection — https://github.com/openclaw/openclaw/pull/90752
- PR #91027 draft=False cron: add unit tests for manual-run gating + stale runningAtMs — https://github.com/openclaw/openclaw/pull/91027
- PR #90998 draft=False fix(sms): authorize text slash commands — https://github.com/openclaw/openclaw/pull/90998
