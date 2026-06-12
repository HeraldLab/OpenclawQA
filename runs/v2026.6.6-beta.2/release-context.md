# Release Context — OpenClaw `v2026.6.6-beta.2`

Fetched at: `2026-06-12T04:00:31Z`

## Target

- Target tag: `v2026.6.6-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.6-beta.2
- Target tag SHA: 3129eed4de92d0ddc0209fbf195c790c3d73ab03

## Freshness baselines

- Latest beta tag: `v2026.6.6-beta.2`
- Latest alpha tag: `v2026.6.10-alpha.2`
- Stable baseline: `v2026.6.5`
- Prior prerelease baseline: `v2026.6.6-beta.1`

## Release notes excerpt


### Highlights

- Security boundaries are substantially tighter across transcripts, sandbox binds, host environment inheritance, MCP stdio, Codex HTTP access, native search policy, elevated sender checks, deleted-agent ACP bypasses, loopback tools, Discord moderation, and Teams group actions; exec approvals now fail closed on timeout. (#91529, #91618, #91615, #91619, #91741, #91745, #91746, #91748, #91749, #91750, #91751, #91752, #91763, #89938) Thanks @joshavant, @pgondhi987, @mmaps, @eleqtrizit, @shakkernerd, and @drobison00.
- Telegram delivery is safer and more coherent: account-scoped topics route to the right agent, streamed text survives tool calls, `/compact` works on generic ingress, callback handling uses concrete APIs, draft chunking is shared, durable dispatch dedupe moved into the SDK, and unauthorized DM text stays out of cache and prompt context. (#91189, #88682, #89588, #90212, #91876, #91874, #91904, #91478, #91915) Thanks @codysai001, @alexzhu0, @joelnishanth, @snowzlm, @obviyus, and @sallyom.
- iMessage recovery and delivery now cover always-on inbound restart, durable echo markers, block streaming, idle approval discovery, hardened outbound transport, and actionable inbound startup diagnostics. (#91335, #91449, #88969, #88530, #91783, #91785) Thanks @omarshahine, @jmissig, and @colmbrogan.
- Browser and MCP connectivity gained existing-session CDP support, discovered WebSocket validation, default-profile `cdpUrl` handling, safer browser-output boundaries, Streamable HTTP loopback transport, corrected OAuth/SSE authorization handling, and broader schema compatibility. (#91422, #89851, #91736, #91747, #91451, #80143) Thanks @pgondhi987, @anagnorisis2peripeteia, @lifuyue, @eleqtrizit, @LiuwqGit, and @HemantSudarshan.
- Control UI startup and first-reply latency are lower through cached model metadata, removal of the startup catalog wait, lazy slash-command loading, and first-event tracing with slow-reply diagnostics. (#91531, #91538, #91568, #91583, #91598)
- Provider support expands with OpenRouter OAuth onboarding and Claude Fable 5 adaptive thinking, while Codex sessions keep correct compaction ownership, local models skip guardian review, dynamic tool progress normalizes cleanly, and Gemma 4 reasoning replay is preserved. (#91830, #91882, #91590, #88630, #88768, #91696) Thanks @Patrick-Erichsen, @joshavant, @bdjben, and @Coder-Wangyankun.

### Changes

- CLI progress: emit Claude CLI commentary progress events and bridge inter-tool commentary into channel progress without exposing internal protocol scaffolding. (#89834, #90883) Thanks @anagnorisis2peripeteia.
- Observability: allow trusted diagnostics channels to capture tool input/output content, add first-assistant-event traces, and warn on slow initial replies. (#91256, #91568, #91583) Thanks @amknight.
- Plugins/ClawHub: dogfood reusable package publishing, let dry runs skip publish approval, allow declared installed trusted hooks, report managed plugin version drift, and warn instead of failing on retired Skill Workshop configuration. (#91574, #91591, #90004, #90927, #90838) Thanks @Patrick-Erichsen, @brokemac79, and @lonexreb.
- Memory/providers: move the local llama.cpp runtime into its provider plugin, batch embeddings across files, persist the agent model catalog cache, and keep QMD JSON search one-shot while filtering stale REM recall previews. (#91324, #89138, #90457, #91837, #91851) Thanks @osolmaz, @mushuiyu886, @ai-hpc, and @TurboTheTurtle.
- Channels/mobile: add the QQBot group mention toggle, improve iPad and iPhone control surfaces, and expose the active connection host in the TUI footer. (#91423, #91557, #89909) Thanks @cxyhhhhh, @Solvely-Colin, and @baskduf.
- Performance: prewarm TUI runtime plugins, deduplicate plugin auto-enable fanout, stop `/models` derived-registry rescan storms, trim dense text-delta snapshots, and reuse prepared startup model metadata. (#90782, #89978, #92127, #91580, #91531) Thanks @RomneyDa, @obuchowski, and @ai-hpc.

### Fixes

- Agent/session recovery: drop stale approval follow-ups after session rebind, remove drained reply-queue items by identity, recover stale main and visible replies, preserve Codex context-engine compaction ownership, project thinking catalog compatibility through SDK sessions, retry same-model assistant calls across short rate-limit windows, lower the default compaction timeout to 180 seconds while respecting explicit configuration, and keep provider-failure terminal lifecycle state correct. (#85679, #91450, #91566, #91840, #91590, #91911, #91361, #91895) Thanks @openperf, @yetval, @joshavant, @lanzhi-lee, @wangmiao0668000666, and @TurboTheTurtle.
- User-visible content boundaries: suppress Codex/Harmony protocol artifacts, neutralize browser and LanceDB memory media directives, redact transcript images, and preserve native `/compact` replies through source suppression. (#89151, #91422, #91425, #91529, #90212) Thanks @joelnishanth, @pgondhi987, @joshavant, and @snowzlm.
- Channel delivery: keep WhatsApp captured replies attached to the successor controller after restart, retry Feishu rate limits, preserve Mattermost thread replies, canonicalize LINE webhook paths, restore Discord reply hydration and runtime timeout exports, and show OpenAI Realtime WebRTC assistant transcripts. (#85823, #89659, #91684, #91649, #90263, #91686, #90426) Thanks @itsuzef, @ladygege, @jacobtomlinson, @fuller-stack-dev, and @shushushv.
- Cron: cancel active task runs cleanly, preserve terminal timeout/cancel state, and recover no-deliver tool warnings instead of silently losing the outcome. (#90666, #90678) Thanks @ai-hpc.
- Gateway/config/auth: share the approval runtime socket token, replace arrays explicitly in `config.patch`, keep indexed `replacePaths` consent from widening to whole arrays, reject malformed Gateway RPC timeout inputs, skip the deleted-agent guard only for valid ACP harness sessions, surface headless LaunchAgent state, verify SQLite auth migration before cleanup, and arm QMD startup maintenance. (#87105, #91551, #91966, #54646, #40953, #91219, #91614, #91740, #91978) Thanks @fuller-stack-dev, @yetval, @ruanrrn, @comeran, and @scotthuang.
- Providers/Codex: clarify quota errors, restore the Codex synthetic usage line, canonicalize Codex protocol assets, require API-key auth for realtime voice, normalize ACP model refs, preserve Gemma 4 `reasoning_content`, honor Ollama's provider-declared thinking default in SDK sessions, and avoid guardian review for local models. (#91390, #91709, #91507, #91567, #88630, #91657, #91696) Thanks @hxy91819, @brokemac79, @RomneyDa, @joshavant, @openperf, and @Coder-Wangyankun.
- Updates/builds: recover package Gateway restarts after refresh failure, expose plugin convergence repair, fall back to Corepack in PATH-less pnpm environments, seed the correct Docker store packages, keep ClawHub dry-run and publish paths reusable, and keep beta GitHub release pages draft until OpenClaw npm, dependency evidence, postpublish verification, and required plugin publishes pass. (#91581, #91599, #91547, #91591) Thanks @fuller-stack-dev, @sallyom, and @Patrick-Erichsen.
- UI: require explicit user intent before opening chat sessions and drain restored chat queues after session switches. (#91480) Thanks @TurboTheTurtle.
- Android: avoid the `dataSync` foreground-service type for persistent nodes. (#80082) Thanks @davelutztx.
- Native hooks: bound relay lifetimes so abandoned native hook connections cannot linger indefinitely. (#91550) Thanks @joshavant.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.6-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.6-beta.2.tgz
- integrity: `sha512-617ITjTL0UxtQK4qGOc248nQBJjExX43/RR7CBr+0rEpqnA88i/VWABfTPrUnNT25181uZkOyzgguZjMW0u4Ug==`
- release SHA: `3129eed4de92d0ddc0209fbf195c790c3d73ab03`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.6.6-beta.2/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/27392222148
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27390602410
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27390601362
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27392305214
- plugin ClawHub publish: dispatched separately, not awaited by this proof: https://github.com/openclaw/openclaw/actions/runs/27392308021
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27392531757
- npm Telegram beta E2E: https://github.com/openclaw/openclaw/actions/runs/27392727108



## Recent issue risk signals

- #15073 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:auth-provider, issue-rating: 🦞 diamond lobster] Feature Request: Per-agent context/workspace on model fallback — https://github.com/openclaw/openclaw/issues/15073
- #14747 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:other] Feature request: configurable lane wait diagnostic threshold — https://github.com/openclaw/openclaw/issues/14747
- #13870 [enhancement, P3, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] Feature Request: Human-friendly device names in paired devices list — https://github.com/openclaw/openclaw/issues/13870
- #13593 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, impact:message-loss, issue-rating: 🐚 platinum hermit] Add logging and warnings for cron job execution failures — https://github.com/openclaw/openclaw/issues/13593
- #13583 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] [Feature] Pre-response enforcement hooks (hard gates) for mandatory tool-call / policy rules — https://github.com/openclaw/openclaw/issues/13583
- #13543 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:security, issue-rating: 🌊 off-meta tidepool] Feature: Tool-level sandbox mode for selective isolation — https://github.com/openclaw/openclaw/issues/13543
- #13487 [enhancement, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] Discord routing: mention > reply-target > default owner (suppress default owner when targeted) — https://github.com/openclaw/openclaw/issues/13487
- #13479 [enhancement, P3, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:other] Feature Request: Show cron job details (prompt/summary) in Web UI — https://github.com/openclaw/openclaw/issues/13479
- #13364 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] [Feature]: Expose before_tool_call/after_tool_call in internal hooks system — https://github.com/openclaw/openclaw/issues/13364
- #13337 [enhancement, channel: voice-call, P3, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:auth-provider, issue-rating: 🌊 off-meta tidepool] [Feature] Voice Call Plugin: Add Vapi provider — https://github.com/openclaw/openclaw/issues/13337
- #13304 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: Content-based agent routing in bindings — https://github.com/openclaw/openclaw/issues/13304
- #13239 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:auth-provider, issue-rating: 🌊 off-meta tidepool] Proposal: Publish a provider compatibility matrix with deprecation policy — https://github.com/openclaw/openclaw/issues/13239
- #13225 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:session-state, impact:security, impact:auth-provider, issue-rating: 🌊 off-meta tidepool] Feature Request: Pre-tool-call routing hook for model delegation — https://github.com/openclaw/openclaw/issues/13225
- #13219 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:auth-provider, issue-rating: 🦞 diamond lobster] Feature Request: Per-model usage logging for cost tracking — https://github.com/openclaw/openclaw/issues/13219
- #12855 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:security, issue-rating: 🌊 off-meta tidepool] [Feature]: Built-in auto-update with configurable schedule, confirmation, and post-update notification — https://github.com/openclaw/openclaw/issues/12855
- #12602 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Feature]: Slack Block Kit support for agent messages — https://github.com/openclaw/openclaw/issues/12602
- #12512 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, issue-rating: 🦞 diamond lobster] [Feature Request] SKILL.md Instruction Isolation from Agent Context — https://github.com/openclaw/openclaw/issues/12512
- #12507 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] [Feature Request] Code Verification and Signature for Skills — https://github.com/openclaw/openclaw/issues/12507
- #12441 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:auth-provider, issue-rating: 🦞 diamond lobster] [Feature] Control UI should accept gateway token from Authorization header — https://github.com/openclaw/openclaw/issues/12441

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #92213 draft=False feat(plugins): add iFlow Search external provider — https://github.com/openclaw/openclaw/pull/92213
- PR #91889 draft=False feat(plugin-sdk): surface accountId on agent hook context — https://github.com/openclaw/openclaw/pull/91889
- PR #88748 draft=False fix(gemini): bridge OAuth profiles into CLI runtime — https://github.com/openclaw/openclaw/pull/88748
- PR #14432 draft=False System prompt: add guidance for spawning background sub-agents — https://github.com/openclaw/openclaw/pull/14432
- PR #12581 draft=False feat(hooks): emit session prune lifecycle event — https://github.com/openclaw/openclaw/pull/12581
- PR #92081 draft=True feat(msteams): Teams voice (CVI) + chat + governance integration — https://github.com/openclaw/openclaw/pull/92081
- PR #92335 draft=False fix(exec-approvals): allow YOLO fast path when socket token exists (fixes #92330) — https://github.com/openclaw/openclaw/pull/92335
- PR #92294 draft=False fix(codex): keep OpenClaw exec when native surface has no environment (#92238) — https://github.com/openclaw/openclaw/pull/92294
- PR #92151 draft=False fix(telegram): rethrow dispatch errors so spooled updates are not silently deleted — https://github.com/openclaw/openclaw/pull/92151
- PR #92336 draft=False [AI] fix: initialize execSecurity from config on cold gateway startup — https://github.com/openclaw/openclaw/pull/92336
- PR #92154 draft=False Gate private QQBot group commands — https://github.com/openclaw/openclaw/pull/92154
- PR #92334 draft=False fix(exec-approvals): skip socket in YOLO mode regardless of token presence — https://github.com/openclaw/openclaw/pull/92334
- PR #91921 draft=False fix(agents): deliver background exec completion to agent via [OpenClaw exec completion] — https://github.com/openclaw/openclaw/pull/91921
- PR #92274 draft=False fix(agents): classify embedded prompt lock error as permanent announce failure — https://github.com/openclaw/openclaw/pull/92274
- PR #92328 draft=False Fix dashboard history projection and approval followups — https://github.com/openclaw/openclaw/pull/92328
- PR #84758 draft=False feat(subagents): add execution backend placement contract — https://github.com/openclaw/openclaw/pull/84758
- PR #41275 draft=False fix(cron): allow timeoutSeconds: 0 for no-timeout mode — https://github.com/openclaw/openclaw/pull/41275
- PR #92287 draft=False fix: start typing for queued followup turns and honor configured typingMode for Telegram room events — https://github.com/openclaw/openclaw/pull/92287
- PR #92292 draft=False fix(doctor): warn when resolved default model is not in the catalog (fixes #92009) — https://github.com/openclaw/openclaw/pull/92292
- PR #92331 draft=False fix(webchat): ensure senderLabel is properly normalized to prevent empty string display — https://github.com/openclaw/openclaw/pull/92331
- PR #86655 draft=False feat(claude): add claude-bridge app-server harness extension — https://github.com/openclaw/openclaw/pull/86655
- PR #62063 draft=False Add Swedish control UI locale — https://github.com/openclaw/openclaw/pull/62063
- PR #22439 draft=False feat(workspace): add tiered bootstrap loading with configurable bootstrapTier — https://github.com/openclaw/openclaw/pull/22439
- PR #92318 draft=False fix(cron): require explicit message target proof — https://github.com/openclaw/openclaw/pull/92318
- PR #91080 draft=False feat(gateway): startup watchdog dumps in-flight phases on hang — https://github.com/openclaw/openclaw/pull/91080
- PR #85664 draft=False feat(gateway): wire read coding tool into HTTP /tools/invoke (narrow) — https://github.com/openclaw/openclaw/pull/85664
- PR #92300 draft=False fix(openai-responses): collapse cumulative message snapshots — https://github.com/openclaw/openclaw/pull/92300
- PR #92172 draft=False fix(feishu): bilingual no-visible-reply fallback with reason code — https://github.com/openclaw/openclaw/pull/92172
- PR #92170 draft=False fix(imessage): respect actions.reply=false in outbound delivery — https://github.com/openclaw/openclaw/pull/92170
- PR #87504 draft=False fix(skill-workshop): align agent_end hook timeout with max reviewer timeout — https://github.com/openclaw/openclaw/pull/87504
