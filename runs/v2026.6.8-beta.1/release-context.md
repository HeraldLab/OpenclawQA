# Release Context — OpenClaw `v2026.6.8-beta.1`

Fetched at: `2026-06-13T22:01:09Z`

## Target

- Target tag: `v2026.6.8-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.8-beta.1
- Target tag SHA: a13710a225c334a115dfd32918e823ec0af99eb0

## Freshness baselines

- Latest beta tag: `v2026.6.8-beta.1`
- Latest alpha tag: `v2026.6.10-alpha.2`
- Stable baseline: `v2026.6.6`
- Prior prerelease baseline: `v2026.6.7-beta.1`

## Release notes excerpt

## 2026.6.8

### Highlights

- Telegram and WhatsApp channel delivery are richer and less brittle: Telegram can send structured rich text with tables, lists, expandable blockquotes, prompt-preserving CLI backend delivery, retired native draft migration, and safer rich-media boundaries, while WhatsApp now honors configured ACP bindings. (#92679, #84082, #89421, #92513) Thanks @obviyus, @jzakirov, @spacegeologist, and @TurboTheTurtle.
- Agent and Gateway recovery is sharper across account-scoped DM sends, generated media completions, restart shutdown aborts, yielded subagent pauses, yielded cron media, heartbeat dedupe, session identity prompts, and unknown OpenAI agent selector rejection. (#92788, #91246, #91357, #92631, #92146, #91287, #92468, #92510) Thanks @yetval, @TurboTheTurtle, @ooiuuii, @openperf, @IWhatsskill, @ZengWen-DT, and @zhangguiping-xydt.
- Provider/model handling expands and tightens with GLM-5.2, Claude Haiku 4.5 catalog rows, OpenRouter and Google Vertex provider-prefix normalization, managed SecretRef auth, bounded model browse discovery, storeless OpenAI Responses replay gating, and Claude 4.5 Copilot tool-streaming safety. (#92796, #90116, #92627, #91218, #90686, #92247, #90706, #75393) Thanks @arkyu2077, @liuhao1024, @bymle, @rohitjavvadi, @samson910022, @snowzlm, and @Kailigithub.
- `/usage` and reply payload hooks now have a native full footer renderer, default template, fixed-decimal formatting, credential-aware limits, better partial-count handling, and warnings for broken templates instead of silent bad output. (#92657, #89835, #89629) Thanks @Marvinthebored.
- UI and mobile flows are steadier: workspace files can collapse and start collapsed, WebChat backscroll survives streaming, the sidebar session picker remains interactive above the desktop workbench, reset soft args survive UI dispatch, stale dashboard session parent lineage is preserved, and iOS reconnects stale foreground gateways. (#92779, #92622, #92705, #91353, #90658, #92552) Thanks @shakkernerd, @TurboTheTurtle, @NianJiuZst, @zhouhe-xydt, @luoyanglang, and @Solvely-Colin.
- Memory, state, and diagnostics recover cleaner: oversized OpenAI embedding batches split before 431s, QMD memory search stays available in transient mode, SQLite avoids WAL on NFS state volumes, stuck-session recovery scheduling no longer resets warning backoff, and Infinity chunk limits stay genuinely unbounded. (#92650, #92618, #92639, #91247, #92752, #92735) Thanks @mushuiyu886, @TurboTheTurtle, @849261680, @gnanam1990, and @yhterrance.

### Changes

- Providers/models: add GLM-5.2 support and Claude Haiku 4.5 catalog entries while keeping provider-qualified model IDs normalized across OpenRouter and Google Vertex paths. (#92796, #90116, #92627, #91218) Thanks @arkyu2077, @liuhao1024, and @bymle.
- Channel plugins: ship Telegram rich-message delivery and WhatsApp ACP binding support, including rich prompt handoff to CLI backends and transport fixtures for richer drafts. (#92679, #92513) Thanks @obviyus and @TurboTheTurtle.
- Agent commands: support `/btw` in CLI-backed sessions and keep CLI usage-error exits classified as usage failures instead of successful runs. (#92669, #92162) Thanks @joshavant and @Pandah97.
- Usage hooks: add built-in full footer rendering, default footer templates, per-turn usage state, credential-aware limits, and fixed-decimal formatting for usage-bar templates. (#92657, #89835, #89629) Thanks @Marvinthebored.
- Docs and operator guidance: document node config examples, clarify before-install hook scope, correct agent default concurrency comments, refresh ZAI provider docs, and update channel/group docs for current Telegram and WhatsApp behavior. (#92677, #92766, #92695) Thanks @liuhao1024, @sallyom, and @ArielSmoliar.

### Fixes

- Channels and delivery: preserve account-scoped DM channel send policy, rich Telegram final replies, rich Telegram tables and lists, Telegram thread-create CLI remapping, Slack outbound `message_sent` hooks, contributed message-tool schema optionality, same-channel generated media completions, and channel chunking around surrogate pairs and Infinity limits. (#92788, #92679, #89421, #89943, #91137, #91246, #92735) Thanks @yetval, @obviyus, @spacegeologist, @rishitamrakar, @lundog, @TurboTheTurtle, and @yhterrance.
- Agent, cron, and Gateway runtime: mark active main sessions before restart shutdown aborts, pause yielded subagent runs whose terminal also signals abort, preserve yielded media completions, de-duplicate main-session heartbeat events, expose session identity in runtime prompts, reject unknown OpenAI agent selectors, keep generated media completions in WebChat, and require admin privileges for HTTP session/model override surfaces. (#91357, #92631, #92146, #91287, #92468, #92510, #91246, #92651, #92646) Thanks @ooiuuii, @openperf, @IWhatsskill, @ZengWen-DT, @zhangguiping-xydt, and @TurboTheTurtle.
- Providers and model replay: preserve storeless OpenAI Responses replay compatibility, avoid eager tool streaming for Claude 4.5 in Copilot, honor profile auth for SecretRef model entries, bound model browsing, strip provider prefixes where runtimes need bare IDs, and surface nested embedding fetch failures. (#90706, #75393, #90686, #92247, #92627, #91218, #92628) Thanks @snowzlm, @Kailigithub, @rohitjavvadi, @samson910022, @liuhao1024, @bymle, and @mushuiyu886.
- Memory, state, diagnostics, and config: split header-too-large embedding batches, keep QMD memory search enabled in transient mode, avoid SQLite WAL on NFS volumes, preserve recovery scheduling outside stuck-session warning backoff, and keep shell environment fallbacks contained in config write tests. (#92650, #92618, #92639, #91247, #92752) Thanks @mushuiyu886, @TurboTheTurtle, @849261680, and @gnanam1990.
- UI/mobile/TUI: preserve dashboard session parent lineage, WebChat backscroll, reset soft command args, sidebar session picker interactivity, collapsed workspace files, resolved `/model` confirmation refs, and stale foreground iOS Gateway reconnects. (#90658, #92622, #91353, #92705, #92779, #92773, #92552) Thanks @luoyanglang, @TurboTheTurtle, @zhouhe-xydt, @NianJiuZst, @shakkernerd, @NarahariRaghava, and @Solvely-Colin.
- Release and test reliability: extend slow Gateway/full-suite watchdogs, split local full-suite shards when throttled, stabilize plugin auth marker fixtures, avoid brittle provider-ref error text, and keep QA Lab bootstrap selection assertions aligned with flow-only scenarios. (#92652)



## Recent issue risk signals

- #46109 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:auth-provider, issue-rating: 🦞 diamond lobster] Feature request: first-class .env / environment-backed secret config UX — https://github.com/openclaw/openclaw/issues/46109
- #46031 [P2, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:auth-provider, issue-rating: 🦞 diamond lobster] auth.order ignored for GitHub Copilot provider — first profile in auth.profiles always wins — https://github.com/openclaw/openclaw/issues/46031
- #45854 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:session-state, impact:security, issue-rating: 🌊 off-meta tidepool] [Feature]: Android Node Tools & Session Enhancement — https://github.com/openclaw/openclaw/issues/45854
- #45841 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] [Feature]: Sandboxing + ACP — https://github.com/openclaw/openclaw/issues/45841
- #45839 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:security, impact:auth-provider, issue-rating: 🌊 off-meta tidepool] [Feature Request] Telegram inline buttons for pairing approve/deny — https://github.com/openclaw/openclaw/issues/45839
- #45771 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, impact:auth-provider, issue-rating: 🌊 off-meta tidepool] Feature: Built-in pace-aware rate limiting for autonomous agents — https://github.com/openclaw/openclaw/issues/45771
- #45469 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:crash-loop, issue-rating: 🦞 diamond lobster] [Bug P2] scheduleReconnect() has no max retry limit — infinite reconnect loop — https://github.com/openclaw/openclaw/issues/45469
- #45382 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] [Feature]: add VALUE.md as a first-class workspace context file — https://github.com/openclaw/openclaw/issues/45382
- #45323 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:other] Feature Request: Slack-Style @Mention Autocomplete in Control UI Chat — https://github.com/openclaw/openclaw/issues/45323
- #44603 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] [Feature]: pty setting — https://github.com/openclaw/openclaw/issues/44603
- #44551 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Feature]: [Feature Request] Gateway UI 支持中文显示 — https://github.com/openclaw/openclaw/issues/44551
- #44431 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, issue-rating: 🐚 platinum hermit] Browser tool: 7 improvements from real-world automation field test — https://github.com/openclaw/openclaw/issues/44431
- #44395 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, issue-rating: 🦞 diamond lobster] feat: heading-aware chunking + entity extraction for memory search — https://github.com/openclaw/openclaw/issues/44395
- #44347 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:needs-live-repro, impact:security, impact:message-loss, impact:auth-provider, issue-rating: 🐚 platinum hermit] Google Chat: Add threaded reply support + receive all messages in spaces — https://github.com/openclaw/openclaw/issues/44347
- #44302 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: Optional webchat-to-external-channel mirroring — https://github.com/openclaw/openclaw/issues/44302
- #44253 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster] Per-agent tools.selfDeny — allow tool inheritance to subagents while denying direct use — https://github.com/openclaw/openclaw/issues/44253
- #92451 [bug, regression, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit, impact:other] v2026.6.x system prompt bloat causes instruction following degradation on smaller models — https://github.com/openclaw/openclaw/issues/92451

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #46502 draft=False Rescue: add watchdog core service and cron engine — https://github.com/openclaw/openclaw/pull/46502
- PR #46303 draft=False fix: drain inbound debounce buffer and followup queues before SIGUSR1 reload — https://github.com/openclaw/openclaw/pull/46303
- PR #45901 draft=False security: create session dirs with private permissions — https://github.com/openclaw/openclaw/pull/45901
- PR #45465 draft=False cron: add lifecycle hooks for job execution — https://github.com/openclaw/openclaw/pull/45465
- PR #44884 draft=False security: gateway public network hardening — https://github.com/openclaw/openclaw/pull/44884
- PR #44288 draft=False feat(backup): add exclude patterns, --smart-exclude, and protected path guards [ai] — https://github.com/openclaw/openclaw/pull/44288
- PR #92725 draft=False External reranker — https://github.com/openclaw/openclaw/pull/92725
- PR #92738 draft=False Forward suppressed-source progress for message-tool channel replies — https://github.com/openclaw/openclaw/pull/92738
- PR #88748 draft=False fix(gemini): bridge OAuth profiles into CLI runtime — https://github.com/openclaw/openclaw/pull/88748
- PR #92790 draft=False fix(session): clear stale auto fallback origins — https://github.com/openclaw/openclaw/pull/92790
- PR #75662 draft=False fix(agents): pause yielded main-session runs — https://github.com/openclaw/openclaw/pull/75662
- PR #44111 draft=False Backup: add encrypted snapshot backup flow — https://github.com/openclaw/openclaw/pull/44111
- PR #43469 draft=False security: scan markdown skill definitions for injection threats — https://github.com/openclaw/openclaw/pull/43469
- PR #39102 draft=False feat(agents): per-agent outbound A2A allowlist override — https://github.com/openclaw/openclaw/pull/39102
- PR #39059 draft=False Security: harden gateway timeouts and auth store sealing — https://github.com/openclaw/openclaw/pull/39059
- PR #92789 draft=False fix(telegram): skip IPv4 fallback when user configures explicit network settings (fixes #75574) — https://github.com/openclaw/openclaw/pull/92789
- PR #41067 draft=False Fix dashboard chat run recovery across reconnects — https://github.com/openclaw/openclaw/pull/41067
- PR #92793 draft=False fix(feishu): re-resolve route when dynamic agent binding already exists in runtime config — https://github.com/openclaw/openclaw/pull/92793
- PR #92787 draft=False fix(security): bound ancestor context file walk at home directory (fixes #92561) — https://github.com/openclaw/openclaw/pull/92787
- PR #92795 draft=False fix(gateway): use resolveNonNegativeNumber for totalTokens to display 0 instead of ? (fixes #43009) — https://github.com/openclaw/openclaw/pull/92795
- PR #43493 draft=False feat: configure metadata (contextWindow, maxTokens, etc.) for custom provider setup — https://github.com/openclaw/openclaw/pull/43493
- PR #18860 draft=False feat(agents): expose tools and their schemas via new after_tools_resolved hook [AI-assisted] — https://github.com/openclaw/openclaw/pull/18860
- PR #92775 draft=False fix(status): warm context window cache at startup for correct /status on first call — https://github.com/openclaw/openclaw/pull/92775
- PR #88815 draft=False feat: channel echo / session pinning — https://github.com/openclaw/openclaw/pull/88815
- PR #92791 draft=False fix(agents): recover genuine terminal child result on lost-context sweep (#90299) — https://github.com/openclaw/openclaw/pull/92791
- PR #92782 draft=False fix #92688: [Bug]: Qwen vision models fail with 400 "Unexpected item type in content" on DashScope — https://github.com/openclaw/openclaw/pull/92782
- PR #44143 draft=True fix: serialize outbound deliveries per channel+recipient — https://github.com/openclaw/openclaw/pull/44143
- PR #92792 draft=False fix(agents): catch malformed image blocks in sanitizeContentBlocksImages — https://github.com/openclaw/openclaw/pull/92792
- PR #39617 draft=False fix: reload config in slash command routing so dmScope is respected — https://github.com/openclaw/openclaw/pull/39617
- PR #38295 draft=False fix(config): dedupe warning spam and slow restart storms — https://github.com/openclaw/openclaw/pull/38295
