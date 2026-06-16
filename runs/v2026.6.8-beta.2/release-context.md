# Release Context — OpenClaw `v2026.6.8-beta.2`

Fetched at: `2026-06-16T02:01:01Z`

## Target

- Target tag: `v2026.6.8-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.8-beta.2
- Target tag SHA: b1736723d716b1abe1f8d324772371661146f3b8

## Freshness baselines

- Latest beta tag: `v2026.6.8-beta.2`
- Latest alpha tag: `v2026.6.15-alpha.1`
- Stable baseline: `v2026.6.6`
- Prior prerelease baseline: `v2026.6.8-beta.1`

## Release notes excerpt


### Highlights

- Telegram and WhatsApp channel delivery are richer and less brittle: Telegram can send structured rich text with tables, lists, expandable blockquotes, preserved intentional line breaks, prompt-preserving CLI backend delivery, retired native draft migration, and safer rich-media boundaries, while WhatsApp now honors configured ACP bindings. (#92679, #93164, #84082, #89421, #92513) Thanks @obviyus, @jzakirov, @spacegeologist, and @TurboTheTurtle.
- Agent and Gateway recovery is sharper across account-scoped DM sends, generated media completions, auto-reply message-tool final replies, reset archive fallback reads, restart shutdown aborts, yielded subagent pauses, trusted subagent thinking override fallback, yielded cron media, heartbeat dedupe, session identity prompts, and unknown OpenAI agent selector rejection. (#92788, #91246, #92879, #91357, #92631, #92412, #92146, #91287, #92468, #92510) Thanks @yetval, @TurboTheTurtle, @masatohoshino, @CadanHu, @ooiuuii, @openperf, @IWhatsskill, @ZengWen-DT, and @zhangguiping-xydt.
- Provider/model handling expands and tightens with GLM-5.2, Claude Haiku 4.5 catalog rows, OpenRouter and Google Vertex provider-prefix normalization, managed SecretRef auth, OAuth image-default routing through Codex, bounded model browse discovery, LM Studio binary thinking-off delivery, storeless OpenAI Responses replay gating, invalid OpenAI reasoning-signature and genericized Anthropic thinking-signature recovery, Claude 4.5 Copilot tool-streaming safety, and OpenAI/Anthropic-family payload quarantine for unreadable or post-hook tool schemas. (#92796, #90116, #92627, #91218, #90686, #92824, #92247, #92002, #90706, #92941, #92201, #92916, #75393, #92908, #92921, #92928) Thanks @arkyu2077, @liuhao1024, @bymle, @rohitjavvadi, @nxmxbbd, @bek91, @samson910022, @mmyzwl, @CarlCapital, @snowzlm, @Kailigithub, and @vincentkoc.
- `/usage` and reply payload hooks now have a native full footer renderer, default template, fixed-decimal formatting, credential-aware limits, better partial-count handling, and warnings for broken templates instead of silent bad output. (#92657, #89835, #89629) Thanks @Marvinthebored.
- UI and mobile flows are steadier: workspace files can collapse and start collapsed, WebChat backscroll survives streaming, the sidebar session picker remains interactive above the desktop workbench, reset soft args survive UI dispatch, stale dashboard session parent lineage is preserved, and iOS reconnects stale foreground gateways. (#92779, #92622, #92705, #91353, #90658, #92552) Thanks @shakkernerd, @TurboTheTurtle, @NianJiuZst, @zhouhe-xydt, @luoyanglang, and @Solvely-Colin.
- Memory, state, and diagnostics recover cleaner: oversized OpenAI embedding batches split before 431s, QMD memory search stays available in transient mode, SQLite avoids WAL on NFS state volumes, stuck-session recovery scheduling no longer resets warning backoff, full memory reindexes preserve rollback/cache recovery, raw Memory Wiki source pages stop looking malformed, and Infinity chunk limits stay genuinely unbounded. (#92650, #92618, #92639, #91247, #92752, #92881, #59137, #92876, #69700, #92735) Thanks @mushuiyu886, @TurboTheTurtle, @849261680, @gnanam1990, @TSHOGX, @arlen8411, and @yhterrance.

### Changes

- Providers/models: add GLM-5.2 support and Claude Haiku 4.5 catalog entries while keeping provider-qualified model IDs normalized across OpenRouter and Google Vertex paths. (#92796, #90116, #92627, #91218) Thanks @arkyu2077, @liuhao1024, and @bymle.
- Channel plugins: ship Telegram rich-message delivery and WhatsApp ACP binding support, including preserved intentional line breaks, rich prompt handoff to CLI backends, and transport fixtures for richer drafts. (#92679, #93164, #92513) Thanks @obviyus and @TurboTheTurtle.
- Agent commands: support `/btw` in CLI-backed sessions and keep CLI usage-error exits classified as usage failures instead of successful runs. (#92669, #92162) Thanks @joshavant and @Pandah97.
- Usage hooks: add built-in full footer rendering, default footer templates, per-turn usage state, credential-aware limits, and fixed-decimal formatting for usage-bar templates. (#92657, #89835, #89629) Thanks @Marvinthebored.
- Docs and operator guidance: document node config examples, clarify before-install hook scope, correct agent default concurrency comments, refresh ZAI provider docs, and update channel/group docs for current Telegram and WhatsApp behavior. (#92677, #92766, #92695) Thanks @liuhao1024, @sallyom, and @ArielSmoliar.

### Fixes

- Channels and delivery: preserve account-scoped DM channel send policy, intentional rich-message line breaks in Telegram and status output, rich Telegram final replies, rich Telegram tables and lists, Telegram thread-create CLI remapping, Feishu dynamic-agent routes after persisted binding reuse, Slack outbound `message_sent` hooks, contributed message-tool schema optionality, same-channel generated media completions, and channel chunking around surrogate pairs and Infinity limits. (#92788, #93164, #92679, #89421, #89943, #42837, #92814, #91137, #91246, #92735) Thanks @yetval, @obviyus, @spacegeologist, @rishitamrakar, @liuhao1024, @lundog, @TurboTheTurtle, and @yhterrance.
- Discord: give generated auto-thread titles a 60-second timeout and 4,096-token reasoning-model output budget, clamped to the selected model output cap. (#64734) Thanks @hanamizuki.
- Agent, cron, and Gateway runtime: mark active main sessions before restart shutdown aborts, pause yielded subagent runs whose terminal also signals abort, clamp trusted subagent thinking overrides through provider/model fallback, preserve yielded media completions, deliver channel message-tool final replies through auto-reply while hiding internal delivery hints, restore reset archive fallback reads when active async transcripts are missing, de-duplicate main-session heartbeat events, expose session identity in runtime prompts, reject unknown OpenAI agent selectors, keep generated media completions, slash-command block replies, and trajectory export commands in WebChat, and require admin privileges for HTTP session/model override surfaces. (#91357, #92631, #92412, #92146, #92879, #91287, #92468, #92510, #91246, #92651, #92646) Thanks @ooiuuii, @openperf, @IWhatsskill, @masatohoshino, @CadanHu, @ZengWen-DT, @zhangguiping-xydt, and @TurboTheTurtle.
- Providers and model replay: preserve storeless OpenAI Responses replay compatibility, recover invalid OpenAI reasoning signatures and genericized Anthropic thinking-signature replay errors, route OAuth image defaults through Codex for eligible OpenAI profiles, avoid eager tool streaming for Claude 4.5 in Copilot, quarantine unreadable and post-hook OpenAI/Anthropic-family tool schemas without broadening allowed tool choices, deliver explicit thinking-off requests to LM Studio binary-thinking models, honor profile auth for SecretRef model entries, bound model browsing, strip provider prefixes where runtimes need bare IDs, and surface nested embedding fetch failures. (#90706, #92941, #92201, #92916, #92824, #75393, #92908, #92921, #92928, #92002, #90686, #92247, #92627, #91218, #92628) Thanks @snowzlm, @mmyzwl, @CarlCapital, @bek91, @Kailigithub, @vincentkoc, @rohitjavvadi, @samson910022, @nxmxbbd, @liuhao1024, @bymle, and @mushuiyu886.
- Memory, state, diagnostics, and config: split header-too-large embedding batches, keep QMD memory search enabled in transient mode, avoid SQLite WAL on NFS volumes, preserve recovery scheduling outside stuck-session warning backoff, preserve full-reindex rollback/cache recovery, treat raw Memory Wiki source pages as source evidence, and keep shell environment fallbacks contained in config write tests. (#92650, #92618, #92639, #91247, #92752, #92881, #59137, #92876, #69700) Thanks @mushuiyu886, @TurboTheTurtle, @849261680, @gnanam1990, @TSHOGX, and @arlen8411.
- UI/mobile/TUI: preserve dashboard session parent lineage, WebChat backscroll, reset soft command args, sidebar session picker interactivity, collapsed workspace files, resolved `/model` confirmation refs, stale foreground iOS Gateway reconnects, and paused setup-parent stdin after inherited-stdio child exit. (#90658, #92622, #91353, #92705, #92779, #92773, #92552, #93159) Thanks @luoyanglang, @TurboTheTurtle, @zhouhe-xydt, @NianJiuZst, @shakkernerd, @NarahariRaghava, @Solvely-Colin, and @fuller-stack-dev.
- Release and test reliability: extend slow Gateway/full-suite watchdogs, split local full-suite shards when throttled, stabilize plugin auth marker fixtures, avoid brittle provider-ref error text, fold Telegram RTT sampling into live QA evidence, simplify QA scorecard mappings around canonical coverage IDs, keep QA Lab bootstrap selection assertions aligned with flow-only scenarios, skip QA coverage artifact consumers when runtime parity producer status is not green, keep Feishu lifecycle release checks pointed at the active fixture config, isolate trajectory-export live seed turns from Codex-native shell approvals, preserve release-check child refs while pinning expected SHAs, widen live OpenAI TTS budgets for slower provider responses, and avoid false downgrade prompts for unresolved latest-tag updates. (#92652, #92550, #92558, #92911) Thanks @RomneyDa and @Andy312432.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.8-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.8-beta.2.tgz
- integrity: `sha512-44ab7b24zUY14dpEVt9TZpd6o6PfbYfnNjSbALHULsCkE7e1ju+ZOia46EawvRLqbYqOwjM9oucnbk7P9/eWsQ==`
- release SHA: `b1736723d716b1abe1f8d324772371661146f3b8`
- release publish: https://github.com/openclaw/openclaw/actions/runs/27587320308
- postpublish recovery: exact npm install, 35 npm plugins, and 35 ClawHub packages verified after registry propagation
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27582865457
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27584541070
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27587508776
- plugin ClawHub publish: https://github.com/openclaw/openclaw/actions/runs/27587512198
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27587814328
- npm Telegram beta E2E: https://github.com/openclaw/openclaw/actions/runs/27588410701


## Recent issue risk signals

- #29387 [bug, P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, issue-rating: 🦞 diamond lobster] [Bug]: Bootstrap files in agentDir are silently ignored — only workspace directory files are injected into system prompt — https://github.com/openclaw/openclaw/issues/29387
- #25574 [P1, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, impact:crash-loop, issue-rating: 🦞 diamond lobster] [Bug]: Config warnings logged repeatedly on every reload, spamming error log with thousands of duplicates — https://github.com/openclaw/openclaw/issues/25574
- #23353 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, impact:auth-provider, issue-rating: 🦞 diamond lobster] [Feature]: Support Anthropic native server-side tools (web_search, web_fetch, code_execution) — https://github.com/openclaw/openclaw/issues/23353
- #22358 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:session-state, impact:security, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature Request] Post-subagent completion extension hook — https://github.com/openclaw/openclaw/issues/22358
- #20756 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:message-loss, issue-rating: 🦞 diamond lobster] message tool should auto-select the only enabled account — https://github.com/openclaw/openclaw/issues/20756
- #17840 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: opt-in reaction-triggered agent turns — https://github.com/openclaw/openclaw/issues/17840
- #15032 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] Feature: Per-spawn tool restrictions for sub-agents — https://github.com/openclaw/openclaw/issues/15032
- #14747 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:other] Feature request: configurable lane wait diagnostic threshold — https://github.com/openclaw/openclaw/issues/14747
- #14629 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Output sanitizer: improve duplicate detection for same-line and partial duplicates — https://github.com/openclaw/openclaw/issues/14629
- #83954 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:auth-provider, issue-rating: 🐚 platinum hermit] Document/support a Pro-plan path for gpt-5.5-pro and retired Spark via Codex CLI/app-server — https://github.com/openclaw/openclaw/issues/83954

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #93072 draft=False fix(sessions): preserve titles on release upsert — https://github.com/openclaw/openclaw/pull/93072
- PR #24661 draft=True feat: Provider/Cohere onboarding + auth-choice support — https://github.com/openclaw/openclaw/pull/24661
- PR #92700 draft=False #92664: [Bug]: read tool fails to read GBK-encoded text files on Chinese Windows (displays garbled text) — https://github.com/openclaw/openclaw/pull/92700
- PR #93461 draft=False fix: add compact mode to cron list tool — https://github.com/openclaw/openclaw/pull/93461
- PR #39386 draft=True fix(gateway): forward child session node events to spawnedBy subscribers — https://github.com/openclaw/openclaw/pull/39386
- PR #39245 draft=False fix(agents): normalize mangled tool names and IDs from OpenAI-compati… — https://github.com/openclaw/openclaw/pull/39245
- PR #93282 draft=False fix: trust all ClawHub channel types when package matches official catalog — https://github.com/openclaw/openclaw/pull/93282
- PR #36630 draft=False fix(signal): complete bidirectional quote-reply support — https://github.com/openclaw/openclaw/pull/36630
- PR #18778 draft=True Discord: Discord canvas! — https://github.com/openclaw/openclaw/pull/18778
- PR #12581 draft=False feat(hooks): emit session prune lifecycle event — https://github.com/openclaw/openclaw/pull/12581
- PR #93267 draft=False fix(session-memory): skip delivery-mirror entries and dedup consecutive identical assistant messages (#92563) — https://github.com/openclaw/openclaw/pull/93267
- PR #92945 draft=False #92944: Telegram commands can remain empty after interrupted sync due to stale local command hash — https://github.com/openclaw/openclaw/pull/92945
- PR #93371 draft=False fix(memory): keep recalled memory out of user prompts — https://github.com/openclaw/openclaw/pull/93371
- PR #93460 draft=False fix(cli): honor --log-level in route-first commands — https://github.com/openclaw/openclaw/pull/93460
- PR #92813 draft=False fix(state): refuse chmod-less agent database volumes that cannot prove credential privacy — https://github.com/openclaw/openclaw/pull/92813
- PR #93459 draft=False fix(discord): resolve guildId from channel info for search actions (fixes #88790) — https://github.com/openclaw/openclaw/pull/93459
- PR #90167 draft=False fix(plugins): resolve config env vars for runtime loads — https://github.com/openclaw/openclaw/pull/90167
- PR #88968 draft=False fix: prevent memory flush failure from aborting user reply (#85645) — https://github.com/openclaw/openclaw/pull/88968
- PR #28081 draft=False doctor(config): auto-prune removed google-antigravity-auth entries — https://github.com/openclaw/openclaw/pull/28081
- PR #93458 draft=True feat(telegram): accept structured spec in rich message — https://github.com/openclaw/openclaw/pull/93458
- PR #89038 draft=False fix: skip setup-only channel plugins in outbound resolution and drain pending deliveries on qqbot reconnect — https://github.com/openclaw/openclaw/pull/89038
- PR #92877 draft=False fix(usage): make built-in footer easier to wrap on Telegram — https://github.com/openclaw/openclaw/pull/92877
- PR #85643 draft=False fix(sessions): honor explicit default model pins — https://github.com/openclaw/openclaw/pull/85643
- PR #89762 draft=False feat(messages): config-level default for responseUsage (persistent /usage footer) — https://github.com/openclaw/openclaw/pull/89762
- PR #89123 draft=False refactor: route transcript writers through session seam — https://github.com/openclaw/openclaw/pull/89123
- PR #93007 draft=False feat(gateway): forward web_search_options through OpenAI-compatible chat completions — https://github.com/openclaw/openclaw/pull/93007
- PR #92686 draft=True feat(agents): add stable A2A session metadata — https://github.com/openclaw/openclaw/pull/92686
- PR #92682 draft=False fix(read): use system encoding fallback for non-UTF-8 text files on Windows — https://github.com/openclaw/openclaw/pull/92682
- PR #90579 draft=False fix: allow trusted host-read html after outbound staging — https://github.com/openclaw/openclaw/pull/90579
- PR #92676 draft=False feat: Rate-limit fallback user-visible error notification (message-lifecycle Phase 2 extension) — https://github.com/openclaw/openclaw/pull/92676
