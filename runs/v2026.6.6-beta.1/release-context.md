# Release Context — OpenClaw `v2026.6.6-beta.1`

Fetched at: `2026-06-10T18:00:26Z`

## Target

- Target tag: `v2026.6.6-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.6-beta.1
- Target tag SHA: e3087b9325ed238832d36208b3613c7f1568dad2

## Freshness baselines

- Latest beta tag: `v2026.6.6-beta.1`
- Latest alpha tag: `v2026.6.10-alpha.1`
- Stable baseline: `v2026.6.5`
- Prior prerelease baseline: `v2026.6.5-beta.6`

## Release notes excerpt

## 2026.6.6

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
- Performance: prewarm TUI runtime plugins, deduplicate plugin auto-enable fanout, trim dense text-delta snapshots, and reuse prepared startup model metadata. (#90782, #89978, #91580, #91531) Thanks @RomneyDa and @ai-hpc.

### Fixes

- Agent/session recovery: drop stale approval follow-ups after session rebind, remove drained reply-queue items by identity, recover stale main and visible replies, preserve Codex context-engine compaction ownership, lower the default compaction timeout to 180 seconds while respecting explicit configuration, and keep provider-failure terminal lifecycle state correct. (#85679, #91450, #91566, #91840, #91590, #91361, #91895) Thanks @openperf, @yetval, @joshavant, @wangmiao0668000666, and @TurboTheTurtle.
- User-visible content boundaries: suppress Codex/Harmony protocol artifacts, neutralize browser and LanceDB memory media directives, redact transcript images, and preserve native `/compact` replies through source suppression. (#89151, #91422, #91425, #91529, #90212) Thanks @joelnishanth, @pgondhi987, @joshavant, and @snowzlm.
- Channel delivery: keep WhatsApp captured replies attached to the successor controller after restart, retry Feishu rate limits, preserve Mattermost thread replies, canonicalize LINE webhook paths, restore Discord reply hydration and runtime timeout exports, and show OpenAI Realtime WebRTC assistant transcripts. (#85823, #89659, #91684, #91649, #90263, #91686, #90426) Thanks @itsuzef, @ladygege, @jacobtomlinson, @fuller-stack-dev, and @shushushv.
- Cron: cancel active task runs cleanly, preserve terminal timeout/cancel state, and recover no-deliver tool warnings instead of silently losing the outcome. (#90666, #90678) Thanks @ai-hpc.
- Gateway/config/auth: share the approval runtime socket token, replace arrays explicitly in `config.patch`, skip the deleted-agent guard only for valid ACP harness sessions, surface headless LaunchAgent state, verify SQLite auth migration before cleanup, and arm QMD startup maintenance. (#87105, #91551, #91219, #91614, #91740, #91978) Thanks @fuller-stack-dev and @scotthuang.
- Providers/Codex: clarify quota errors, restore the Codex synthetic usage line, canonicalize Codex protocol assets, require API-key auth for realtime voice, normalize ACP model refs, preserve Gemma 4 `reasoning_content`, and avoid guardian review for local models. (#91390, #91709, #91507, #91567, #88630, #91696) Thanks @hxy91819, @brokemac79, @RomneyDa, @joshavant, and @Coder-Wangyankun.
- Updates/builds: recover package Gateway restarts after refresh failure, expose plugin convergence repair, fall back to Corepack in PATH-less pnpm environments, seed the correct Docker store packages, and keep ClawHub dry-run and publish paths reusable. (#91581, #91599, #91547, #91591) Thanks @fuller-stack-dev, @sallyom, and @Patrick-Erichsen.
- UI: require explicit user intent before opening chat sessions and drain restored chat queues after session switches. (#91480) Thanks @TurboTheTurtle.
- Android: avoid the `dataSync` foreground-service type for persistent nodes. (#80082) Thanks @davelutztx.
- Native hooks: bound relay lifetimes so abandoned native hook connections cannot linger indefinitely. (#91550) Thanks @joshavant.



## Recent issue risk signals

- #91804 [bug, P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster, impact:other] [Bug]: Internal Reasoning Leakage in 2026.6.5 — https://github.com/openclaw/openclaw/issues/91804
- #91330 [P2, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] Current-session message-tool replies can be replaced by private bookkeeping finals — https://github.com/openclaw/openclaw/issues/91330
- #91949 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, impact:auth-provider, issue-rating: 🐚 platinum hermit] invalid_request_error from Anthropic kills session instead of triggering fallback — https://github.com/openclaw/openclaw/issues/91949
- #22021 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:auth-provider, issue-rating: 🦞 diamond lobster] [Feature]: Add X-Actual-Model header to expose runtime model in HTTP responses — https://github.com/openclaw/openclaw/issues/22021
- #20935 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, impact:security, issue-rating: 🌊 off-meta tidepool] [Feature]: Audit log for agent memory changes — https://github.com/openclaw/openclaw/issues/20935
- #20837 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-product-decision, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: make agent aware of communication channel — https://github.com/openclaw/openclaw/issues/20837
- #91975 [P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:auth-provider, issue-rating: 🦞 diamond lobster] Native Anthropic adapter silently drops `thinking` to `off` for custom provider ids (resolveThinkingProfile only matches exact `anthropic`/`claude-cli`) — https://github.com/openclaw/openclaw/issues/91975
- #20756 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, issue-rating: 🦞 diamond lobster] message tool should auto-select the only enabled account — https://github.com/openclaw/openclaw/issues/20756
- #20237 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] [Feature]: WebUI notification system, cron job management popups, and context monitor integration — https://github.com/openclaw/openclaw/issues/20237
- #82719 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review] Allow user plugins to opt into trusted dispatch hooks — https://github.com/openclaw/openclaw/issues/82719
- #20173 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: Discord: Re-process edited user messages (MESSAGE_UPDATE event) — https://github.com/openclaw/openclaw/issues/20173
- #19289 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] Browser backend plugin interface (support third-party drivers via MCP/custom adapter) — https://github.com/openclaw/openclaw/issues/19289
- #18985 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Feature]: Supports Windows 11 MSYS environment and Fishshell. — https://github.com/openclaw/openclaw/issues/18985
- #18967 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, issue-rating: 🦞 diamond lobster] [Feature]: Parent-scoped sessions_send for sub-agents — https://github.com/openclaw/openclaw/issues/18967
- #18571 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:security, issue-rating: 🦞 diamond lobster] [Feature]: Expose sessionKey/runId to outbound message hook for deterministic verification — https://github.com/openclaw/openclaw/issues/18571
- #18548 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, issue-rating: 🦞 diamond lobster] [Feature]: 3 architecture improvements — bootstrap relevance, incremental compaction, observation extraction — https://github.com/openclaw/openclaw/issues/18548
- #18160 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: Direct Exec Mode for Cron Jobs — https://github.com/openclaw/openclaw/issues/18160
- #17925 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:auth-provider, issue-rating: 🦞 diamond lobster] [Feature]: Support native web_search passthrough for ZAI (GLM) and Google (Gemini) providers — https://github.com/openclaw/openclaw/issues/17925
- #17840 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: opt-in reaction-triggered agent turns — https://github.com/openclaw/openclaw/issues/17840
- #17213 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, issue-rating: 🐚 platinum hermit] [Reliability]: Enforce atomic intent→execution flow to prevent orphan pre-action notices — https://github.com/openclaw/openclaw/issues/17213
- #16711 [enhancement, P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool] [Feature]: Chat composer “Expand” button/modal (for long prompts) — https://github.com/openclaw/openclaw/issues/16711

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #91997 draft=False fix(telegram): survive getUpdates conflicts in isolated polling ingress — https://github.com/openclaw/openclaw/pull/91997
- PR #91800 draft=False fix(tools): propagate external content provenance to policy hooks — https://github.com/openclaw/openclaw/pull/91800
- PR #91996 draft=False refactor: prune unused iOS code — https://github.com/openclaw/openclaw/pull/91996
- PR #85104 draft=False feat: fast talks auto mode — https://github.com/openclaw/openclaw/pull/85104
- PR #82950 draft=False fix(security): add ReDoS guard to exec approval argPattern matching — https://github.com/openclaw/openclaw/pull/82950
- PR #88792 draft=False fix(state): harden sqlite path caching — https://github.com/openclaw/openclaw/pull/88792
- PR #88789 draft=True feat(agents): auto-trim lean local tools — https://github.com/openclaw/openclaw/pull/88789
- PR #88780 draft=True fix(check): clean ingress queue lint blockers — https://github.com/openclaw/openclaw/pull/88780
- PR #88776 draft=True fix: normalise wiki lint targets — https://github.com/openclaw/openclaw/pull/88776
- PR #88754 draft=False fix(text): normalize CJK/fullwidth quotes in reasoning tag delimiters — https://github.com/openclaw/openclaw/pull/88754
- PR #88750 draft=False feat(context-engine): pass runtime settings into lifecycle — https://github.com/openclaw/openclaw/pull/88750
- PR #88748 draft=True fix(gemini): bridge OAuth profiles into CLI runtime — https://github.com/openclaw/openclaw/pull/88748
- PR #88743 draft=False docs(sms): add Twilio A2P delivery guidance — https://github.com/openclaw/openclaw/pull/88743
- PR #88738 draft=False docs: document wacli message verification — https://github.com/openclaw/openclaw/pull/88738
- PR #88732 draft=True feat(feeds): add native feed search defaults — https://github.com/openclaw/openclaw/pull/88732
- PR #88726 draft=False [codex] Read exact X posts via FxTwitter — https://github.com/openclaw/openclaw/pull/88726
- PR #88718 draft=False fix(cli): make native hook relay resilient to stale bridges — https://github.com/openclaw/openclaw/pull/88718
- PR #88713 draft=False docs: document agent helper comments — https://github.com/openclaw/openclaw/pull/88713
- PR #88709 draft=False fix(auth): cooldown inline api key billing failures — https://github.com/openclaw/openclaw/pull/88709
- PR #22439 draft=False feat(workspace): add tiered bootstrap loading with configurable bootstrapTier — https://github.com/openclaw/openclaw/pull/22439
- PR #88687 draft=False Tag embedded subagent gap-fill rows as delivery mirrors — https://github.com/openclaw/openclaw/pull/88687
- PR #88686 draft=False Replay sessions_yield wait text in WebChat history — https://github.com/openclaw/openclaw/pull/88686
- PR #88684 draft=False Keep agent web_search on runtime provider resolution — https://github.com/openclaw/openclaw/pull/88684
- PR #88683 draft=False Reject unpublished npm targets consistently in update dry-run — https://github.com/openclaw/openclaw/pull/88683
- PR #91993 draft=False fix(logging): prune stale non-idle diagnostic session entries after TTL (fixes #91697) — https://github.com/openclaw/openclaw/pull/91993
- PR #88681 draft=False Make runtime plugin startup stalls name in-flight plugins — https://github.com/openclaw/openclaw/pull/88681
- PR #88680 draft=False docs(providers): register Ace Data Cloud third-party provider plugin — https://github.com/openclaw/openclaw/pull/88680
- PR #88673 draft=False test(outbound): align implicit source reply sink — https://github.com/openclaw/openclaw/pull/88673
- PR #88668 draft=True [codex] Add per-DM active directive prompt — https://github.com/openclaw/openclaw/pull/88668
- PR #88656 draft=False Drop reasoning-only length turns from replay — https://github.com/openclaw/openclaw/pull/88656
