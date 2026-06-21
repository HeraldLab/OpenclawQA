# Release Context — OpenClaw `v2026.6.10-beta.1`

Fetched at: `2026-06-21T09:30:41Z`

## Target

- Target tag: `v2026.6.10-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.10-beta.1
- Target tag SHA: d91c1607c4d254b6dafa2ea052aef82e68b0c1b0

## Freshness baselines

- Latest beta tag: `v2026.6.10-beta.1`
- Latest alpha tag: `v2026.6.20-alpha.1`
- Stable baseline: `v2026.6.9`
- Prior prerelease baseline: `v2026.6.9-beta.1`

## Release notes excerpt


### Highlights

- **More reliable agent turns and session state:** OpenClaw now preserves pending subagent completion announcements, keeps chat history transcripts non-empty, maintains media index alignment, restarts dormant follow-up drains, and resolves compaction model aliases consistently. (#94349, #92383, #94257, #95039, #90885) Thanks @sallyom, @oiGaDio, @Hidetsugu55, @Nas01010101, @SFVVC, @Pick-cat, and @vincentkoc.
- **Stronger Codex and approval flows:** Codex app-server SecretRefs, thread context, bounded turn text, routed approval context, and typed SDK approval/session helpers now work together more predictably. (#94093, #94324, #94756, #90918, #95144, #95188, #95196, #95169) Thanks @VACInc, @kevinlin-openai, @kevinslin, @Nas01010101, @849261680, @choury, and @vincentkoc.
- **Richer channel delivery:** Telegram, Discord, and Slack now preserve richer progress/reasoning/thread output, handle structured send errors, support Slack shortcuts, and record canonical sent threads more reliably. (#94891, #94856, #94810, #95029, #94881, #78536, #95250) Thanks @obviyus, @zhangqueping, @jairrab, @ZOOWH, @parveshsaini, @vincentkoc, @Marvinthebored, @chrisbaker2000, @KennanHoa, @bek91, and @rockyloveswine.
- **Safer release and network boundaries:** SSH tunnel preflight is loopback-scoped, device-backed node pairings are removed, volatile SQLite state is surfaced by doctor, and legacy Codex routes are repaired instead of silently persisting stale state. (#94607, #90373, #94725, #94478) Thanks @wangwllu, @Alix-007, @manju-rn, @vincentkoc, @TurboTheTurtle, and @Sleepyarno.
- **Useful new CLI and status workflows:** Rename sessions from chat, compact sessions explicitly, show session duration, preserve command progress detail, and preview message sends/polls with dry-run output. (#88581, #91378, #88988, #94868, #94684) Thanks @BSG2000, @Alix-007, @sallyom, @redasadki, @marshall-gordfam, @vincentkoc, @lzyyzznl, and @YB0y.
- **More capable mobile and desktop clients:** Android settings are grouped by intent, iOS notification state is cleaner, the Watch app uses the Xcode 27-compatible target layout, and macOS file inputs open through the native panel. (#94539, #91923, #92477, #94612) Thanks @Tosko4, @zats, @joshavant, @bbblending, @DINGDANGMAOUP, and @vincentkoc.
- **Broader plugin and skill coverage:** Zalo is available as an external channel entry, Trello skills declare their curl dependency, stale managed skill links are retargeted, and tool discovery no longer clears active providers. (#89586, #94729, #86719, #93276) Thanks @ken-kuro, @liuhao1024, @berkgungor, @stevenepalmer, @shakkernerd, @medns, and @vincentkoc.

### Changes

- **Agent and provider behavior:** Codex turn limits, CLI-owned auth, provider-internal error wording, recurring cron backoff, explicit cron delivery targets, and isolated cron key requirements now fail or recover more clearly. (#94756, #88551, #94737, #93051, #94453, #92318, #91685) Thanks @Nas01010101, @yu-xin-c, @snowzlmbot, @Alix-007, @jincheng-xydt, @sallyom, @davectr, @hxy91819, @nxmxbbd, and @vincentkoc.
- **Channels and integrations:** WhatsApp retries the opening text chunk after media failure, Feishu avoids axios internals, Slack records inbound mentions and preserves buffered streams, and external Zalo/Slack shortcuts are wired through the current channel seams. (#93823, #89806, #94790, #78536, #89586, #94881) Thanks @yetval, @sweetcornna, @davinci282828, @ZengWen-DT, @BryceMurray, @vincentkoc, @KennanHoa, @ken-kuro, and @chrisbaker2000.
- **Skills and setup:** OnePassword auth no longer forces tmux when the desktop app is available, stale plugin skill symlinks are repaired, and Trello requirements match their examples. (#81825, #86719, #94729) Thanks @koshaji, @tylerbittner, @stevenepalmer, @shakkernerd, @liuhao1024, @berkgungor, and @vincentkoc.
- **Apps and platform support:** iOS notification cleanup, the single-target Watch migration, Android intent grouping, native macOS file panels, and explicit realtime SDP bounds keep the app surfaces aligned with the Gateway. (#91923, #92477, #94539, #94612, #95093) Thanks @zats, @joshavant, @Tosko4, @bbblending, @DINGDANGMAOUP, and @vincentkoc.
- **Operator diagnostics:** Gateway probes now distinguish reachable-but-errored from unreachable, plugin methods authorize through the attached registry, session status exposes duration, and provider pricing streams are bounded. (#93948, #94343, #88988, #95103) Thanks @xialonglee, @MAdArab872, @wangmiao0668000666, @RDavies8, @Alix-007, @marshall-gordfam, @vincentkoc, @ozthedivine, and @shakkernerd.

### Fixes

- **Reply and transcript correctness:** OpenClaw now keeps pending completions, non-empty histories, media fields, queued follow-ups, buffered Slack replies, and reasoning deliveries intact across retries and partial turns. (#94349, #92383, #94257, #95039, #78536, #95029, #84292) Thanks @sallyom, @oiGaDio, @Hidetsugu55, @Nas01010101, @SFVVC, @vincentkoc, @KennanHoa, @Marvinthebored, @zerone0x, and @pearl-dot.
- **Security and bounded input handling:** SSH tunnel checks stay on loopback, unsafe chat/tool/package/response lengths are rejected, device-backed pairings are removed, and stale abort markers no longer affect fresh chat events. (#94607, #95066, #95078, #95085, #95090, #90373, #91013) Thanks @wangwllu, @vincentkoc, @Alix-007, @manju-rn, and @nxmxbbd.
- **Telegram, WhatsApp, and Slack delivery:** Rich progress previews, structured Telegram errors, WhatsApp listener recovery, and canonical Slack thread/send behavior now survive the edge cases covered by the new release. (#94891, #94856, #94810, #93873, #95250) Thanks @obviyus, @zhangqueping, @jairrab, @ZOOWH, @parveshsaini, @xialonglee, @octaivermatt, @bek91, and @rockyloveswine.
- **Cron and queue safety:** Recurring error backoff honors configured floors, implicit isolated delivery requires an explicit target, and dormant follow-up drains restart instead of disappearing. (#93051, #91685, #92318, #95039) Thanks @Alix-007, @nxmxbbd, @hxy91819, and @SFVVC.
- **Provider, auth, and migration repair:** CLI-owned transports skip the wrong auth gate, compaction aliases resolve canonically, legacy Codex routes are repaired, and tool discovery no longer clears active providers. (#88551, #90885, #94478, #93276) Thanks @yu-xin-c, @Pick-cat, @TurboTheTurtle, @Sleepyarno, @medns, and @vincentkoc.
- **SDK and release tooling:** Approval/session RPC params are typed more strictly, stale packed tarballs are ignored, and DMG output directories are created reliably. (#95144, #95152, #95188, #95196, #95169, #95126, #95133) Thanks @vincentkoc.

### Complete contribution record

This audited record covers the complete v2026.6.9-beta.1..HEAD history: 109 merged PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

#### Pull requests

- **PR #93685** refactor(auto-reply): add lifecycle storage seams. Thanks @jalehman.
- **PR #94349** fix(agents): preserve pending subagent completion announces. Related #93323. Thanks @sallyom and @oiGaDio.
- **PR #93174** test: fold channel message flows into qa e2e. Thanks @RomneyDa.
- **PR #94093** Prevent Codex thread rotation from losing next-step context. Thanks @VACInc.
- **PR #53920** fix(scripts): avoid mutating tracked auth-monitor template during setup. Thanks @JackWuGlobal.
- **PR #94702** Standardize QA coverage IDs on dotted names. Thanks @RomneyDa.
- **PR #81825** fix(skills/1password): stop forcing tmux for desktop app auth (#52540). Thanks @koshaji and @tylerbittner.
- **PR #94725** fix(doctor): warn on volatile SQLite state. Thanks @vincentkoc.
- **PR #88551** fix(agents): skip auth gate for CLI-owned transport. Thanks @yu-xin-c.
- **PR #88581** feat(commands): add /name to rename the current session from chat. Thanks @BSG2000.
- **PR #94324** feat(codex): support app-server SecretRefs. Thanks @kevinlin-openai and @kevinslin.
- **PR #90882** fix: add self-knowledge docs rule to system prompt. Related #90713. Thanks @SutraHsing.
- **PR #94684** fix: #80507 show dry-run output for message send/poll. Thanks @lzyyzznl and @YB0y.
- **PR #93823** fix(whatsapp): keep opening text chunk when first media fails on multi-chunk reply. Thanks @yetval.
- **PR #89203** refactor: route SDK session compatibility through seam. Thanks @jalehman.
- **PR #94453** fix: default cron runMode to "due" instead of "force" (#94270). Thanks @jincheng-xydt and @sallyom and @davectr.
- **PR #94746** fix(note): prevent clack from re-breaking copy-sensitive tokens. Related #94730. Thanks @xzh-icenter and @berkgungor.
- **PR #89904** refactor: route sdk session compatibility through accessor. Thanks @jalehman.
- **PR #86719** fix(skills): retarget stale plugin skill symlinks. Related #85925. Thanks @stevenepalmer and @shakkernerd.
- **PR #94337** fix(tui): show 0 not ? for fresh-session context tokens in footer. Thanks @mushuiyu886.
- **PR #94539** fix(android): group settings by intent. Thanks @Tosko4.
- **PR #92383** fix(gateway): never return an empty chat.history transcript. Thanks @Hidetsugu55.
- **PR #92574** test(browser): cover action-input CLI request bodies. Related #83877. Thanks @yu-xin-c and @davinci282828.
- **PR #92873** test(diffs): add viewerState, toolbar toggle, shadow root, and hydrateProps tests (fixes #83915). Thanks @liuhao1024 and @davinci282828.
- **PR #94257** fix(sessions): preserve Media\* index alignment when reading user-turn fields. Thanks @Nas01010101.
- **PR #94756** fix(codex): bound turn/start text when context budget is non-positive. Related #94748. Thanks @Nas01010101.
- **PR #94729** fix(skills/trello): add curl to requires.bins to match body examples (fixes #94727). Thanks @liuhao1024 and @berkgungor.
- **PR #94790** feat(slack): log INFO receipt for inbound app_mention events. Related #94691. Thanks @ZengWen-DT and @BryceMurray.
- **PR #81696** fix: guard tool event callbacks (AI-assisted). Thanks @enjoylife1243.
- **PR #94809** chore: forward-port alpha release fixes.
- **PR #94612** fix(macos): open NSOpenPanel for embedded Control UI file inputs (#94468). Thanks @bbblending and @DINGDANGMAOUP.
- **PR #89806** fix(feishu): avoid axios interceptor internals. Related #83913. Thanks @sweetcornna and @davinci282828.
- **PR #91923** fix(ios): clean up notification settings state. Thanks @zats.
- **PR #91345** fix: suggest close CLI commands. Related #83999. Thanks @glenn-agent and @HannesOberreiter.
- **PR #94561** Add stdout diagnostics OTEL log exporter. Thanks @jesse-merhi.
- **PR #91013** fix(gateway): ignore stale abort markers for fresh chat events. Related #91012. Thanks @nxmxbbd.
- **PR #89279** fix(tasks): deliver ACP completions to bound Discord threads. Related #84022. Thanks @anyech and @h-mascot.
- **PR #91656** test(cron): expand parseAbsoluteTimeMs test coverage to 39 cases. Related #91654. Thanks @SpecialLeon.
- **PR #94810** fix(telegram): classify sendChatAction 401 by structured error_code, not bare substring match. Related #94787. Thanks @ZOOWH and @parveshsaini.
- **PR #94737** fix(reply): clarify provider internal error copy. Thanks @snowzlmbot.
- **PR #94868** fix(channels): preserve command progress detail. Thanks @vincentkoc.
- **PR #94891** fix(telegram): send progress previews as html text. Thanks @obviyus.
- **PR #94683** fix(outbound): keep direct-only targets out of group sessions. Related #92384. Thanks @scotthuang and @haiwei01.
- **PR #92477** fix: migrate watch app to single-target app (Xcode 27+ compat). Thanks @zats and @joshavant.
- **PR #94812** test(perf): compare saved CLI startup benchmarks. Thanks @FelixIsaac.
- **PR #94856** fix(telegram): normalize all HTML tables before entity-escaping in rich messages. Related #94317. Thanks @zhangqueping and @jairrab.
- **PR #91685** fix(cron): refuse keyless implicit isolated cron delivery inherited from shared agent-main bucket. Thanks @nxmxbbd.
- **PR #88988** feat(status): show session duration in footer. Related #68226. Thanks @Alix-007 and @marshall-gordfam.
- **PR #94020** docs(browser): resolve networkidle contradiction across browser docs. Related #80587. Thanks @ZengWen-DT and @esqandil.
- **PR #93948** fix(gateway): distinguish reachable-but-errored from unreachable in probe diagnostics. Related #79099. Thanks @xialonglee and @ozthedivine.
- **PR #93276** fix(plugins): stop tool-discovery loads from clearing active providers. Thanks @medns.
- **PR #94343** fix(gateway): authorize plugin methods from attached registry. Related #92044. Thanks @wangmiao0668000666 and @RDavies8.
- **PR #94589** fix(channels): stop duplicating inbound previews in system events. Related #94549. Thanks @hugenshen and @gorkem2020.
- **PR #93873** fix(whatsapp): restart listener on selfChatMode config change. Related #86888. Thanks @xialonglee and @octaivermatt.
- **PR #93969** fix(xai): reject unsupported multi-agent model refs before runtime fallback. Related #85106. Thanks @xialonglee and @tess020126-cmyk.
- **PR #89586** feat(channels): add Zalo ClawBot external channel entry and documenta…. Thanks @ken-kuro.
- **PR #78536** fix(slack): preserve buffered thread stream replies. Related #78061. Thanks @vincentkoc and @KennanHoa.
- **PR #89236** fix(slack): default member-info userId to inbound sender. Thanks @stroupaloop.
- **PR #94881** feat(slack): handle global and message shortcuts. Related #63920. Thanks @chrisbaker2000.
- **PR #90885** fix(agent): resolve compaction model alias to canonical model ref. Thanks @Pick-cat.
- **PR #90918** fix(agents): forward turn-source routing fields to plugin.approval.request. Related #74003. Thanks @849261680 and @choury.
- **PR #95029** fix(discord): deliver reasoning replies. Related #94936. Thanks @vincentkoc and @Marvinthebored.
- **PR #89581** refactor: use canonical transcript reader identity. Thanks @jalehman.
- **PR #94607** fix(ssh): scope tunnel port preflight to loopback (#94603). Thanks @wangwllu.
- **PR #95060** fix(test): harden script probe bounds. Thanks @vincentkoc.
- **PR #95066** fix(e2e): reject unsafe chat tools body lengths. Thanks @vincentkoc.
- **PR #93941** docs: fix two broken cross-reference anchors. Thanks @Alix-007.
- **PR #92996** fix(cli): reject present-but-invalid --timeout on status/health fast path. Thanks @Alix-007.
- **PR #94314** refactor(policy): split doctor modules. Thanks @giodl73-repo.
- **PR #93051** fix(cron): honor configured retry.backoffMs for recurring error backoff floor. Thanks @Alix-007.
- **PR #95078** fix(scripts): reject unsafe package download lengths. Thanks @vincentkoc.
- **PR #91378** feat(cli): add `openclaw sessions compact` and fail loudly on CLI `/compact` (fixes #90640). Thanks @Alix-007 and @sallyom and @redasadki.
- **PR #94676** improve: simplify PR context and evidence. Thanks @hannesrudolph.
- **PR #95085** fix(scripts): reject unsafe bounded response lengths. Thanks @vincentkoc.
- **PR #95090** fix(e2e): reject unsafe bounded response text lengths. Thanks @vincentkoc.
- **PR #95076** [codex] docs: clarify PR body evidence updates. Thanks @brokemac79.
- **PR #84292** fix(agents): preserve delivered message send results. Related #84271. Thanks @zerone0x and @pearl-dot.
- **PR #95039** fix(queue): restart dormant followup drains. Related #91909. Thanks @SFVVC.
- **PR #90373** fix(gateway): remove device-backed node pairings. Related #88488. Thanks @Alix-007 and @manju-rn.
- **PR #95093** fix(dev): bound realtime SDP answer reads. Thanks @vincentkoc.
- **PR #95103** fix(gateway): bound pricing catalog streams. Thanks @vincentkoc.
- **PR #95108** fix(agents): bound Anthropic error streams. Thanks @vincentkoc.
- **PR #95111** fix(memory): abort batch upload response reads. Thanks @vincentkoc.
- **PR #95105** fix(ci): cancel stale Testbox PR runs. Thanks @RomneyDa.
- **PR #95114** fix(test): stabilize tooling guard probes. Thanks @vincentkoc.
- **PR #94478** fix(doctor): repair legacy Codex route persistence. Related #94184. Thanks @TurboTheTurtle and @Sleepyarno.
- **PR #95119** fix(test): stream QA Lab stdout artifacts. Thanks @vincentkoc.
- **PR #95116** fix(ci): cancel stale CodeQL runs. Thanks @RomneyDa.
- **PR #95126** fix(package): ignore stale packed tarballs. Thanks @vincentkoc.
- **PR #95133** fix(macos): create DMG output directories. Thanks @vincentkoc.
- **PR #95137** test(docker): stabilize build signal probe. Thanks @vincentkoc.
- **PR #95144** fix(sdk): send exec approval resolve id. Thanks @vincentkoc.
- **PR #95152** fix(sdk): list helpers work without filters. Thanks @vincentkoc.
- **PR #95207** fix(scripts): preserve kitchen sink RPC request errors. Thanks @vincentkoc.
- **PR #95203** fix(scripts): guard reused testbox keys. Thanks @vincentkoc.
- **PR #95188** fix(sdk): type agent mutation RPC params. Thanks @vincentkoc.
- **PR #95196** fix(sdk): tighten approval response params. Thanks @vincentkoc.
- **PR #95169** fix(sdk): require session key for effective tools. Thanks @vincentkoc.
- **PR #95250** fix(slack): record canonical sent thread. Related #95235. Thanks @bek91 and @rockyloveswine.
- **PR #86627** Keep core doctor health in contribution order. Thanks @giodl73-repo.
- **PR #93580** fix: preserve cron delivery awareness for target sessions. Thanks @scotthuang and @jalehman.
- **PR #95030** refactor: add SDK transcript identity target API. Thanks @jalehman.
- **PR #94838** refactor(copilot): complete harness lifecycle parity. Thanks @vincentkoc.
- **PR #95328** fix(sessions): reset stale per-channel origin fields on channel switch. Related #95325. Thanks @ZengWen-DT and @jalehman and @gorkem2020.
- **PR #94461** fix(zai): fall back to manifest baseUrl for synthesized GLM-5 models. Related #94269. Thanks @Pandah97 and @chrysb.
- **PR #93241** fix(agents): classify Zhipu GLM overload as overloaded for failover. Related #93211. Thanks @0xghost42 and @zhengli0922.
- **PR #94067** fix(channels): resolve native /think menu levels via runtime catalog for live-discovered models. Related #93835. Thanks @openperf and @civiltox.
- **PR #94136** fix(zai): expose GLM-5.2 reasoning levels [AI-assisted]. Thanks @BorClaw.
- **PR #92318** fix(cron): require explicit message target proof. Thanks @hxy91819.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.10-beta.1
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.10-beta.1.tgz
- integrity: `sha512-OgdN7P0Scm8rNgcXUrCGFyrMPJGdC3TdMxdS95jPbEzws9tp3CgZnehcmBNyBqCc9QU4uK0QUk7bnNSW+3ohbw==`
- release SHA: `d91c1607c4d254b6dafa2ea052aef82e68b0c1b0`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.6.10-beta.1/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/27898612086
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27897098428
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27897098492
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27898772805
- plugin ClawHub publish: dispatched separately, not awaited by this proof: https://github.com/openclaw/openclaw/actions/runs/27898773498
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27899322972
- npm Telegram beta E2E: not supplied


## Recent issue risk signals

- #87023 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: First-class relay of MCP ImageContent (and other binary Content) to channel extensions (iMessage/BlueBubbles, Telegram, Signal, …) — https://github.com/openclaw/openclaw/issues/87023
- #88646 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:data-loss, issue-rating: 🦞 diamond lobster] Persist image understanding summaries for agent attachments — https://github.com/openclaw/openclaw/issues/88646
- #88568 [stale, P3, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] feat: support pinning / starring sessions for quick access — https://github.com/openclaw/openclaw/issues/88568
- #88373 [P3, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:auth-provider, issue-rating: 🦞 diamond lobster] Windows post-onboarding provider switch path is not discoverable — https://github.com/openclaw/openclaw/issues/88373
- #87876 [P1, clawsweeper:source-repro, impact:session-state, impact:data-loss, impact:auth-provider, issue-rating: 🦞 diamond lobster] Bug: Bedrock Converse Streaming silently aborts on long-context agent sessions (~6 min timeout, no retry, no fallback) — https://github.com/openclaw/openclaw/issues/87876
- #86632 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:needs-live-repro, impact:security, impact:auth-provider, issue-rating: 🐚 platinum hermit] OpenClaw local embedded Ollama/Qwen session fails live-data request that Pi coding agent handles via shell/curl — https://github.com/openclaw/openclaw/issues/86632

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #95308 draft=False fix(ci): filter ClawSweeper comment dispatches before token minting — https://github.com/openclaw/openclaw/pull/95308
- PR #95501 draft=False fix(agents): classify generic external runner failure text as fallback-worthy — https://github.com/openclaw/openclaw/pull/95501
- PR #95307 draft=False fix(gateway): surface cross-agent subagent sessions via allAgents flag (#95295) — https://github.com/openclaw/openclaw/pull/95307
- PR #95524 draft=False fix(agents): classify upstream_error errorType as server_error for model fallback (fixes #95519) (AI-assisted) — https://github.com/openclaw/openclaw/pull/95524
- PR #95522 draft=False feat(telegram): unify progress fallback with assistant preview lane — https://github.com/openclaw/openclaw/pull/95522
- PR #95183 draft=False fix(telegram): materialize streaming progress placeholders — https://github.com/openclaw/openclaw/pull/95183
- PR #93680 draft=False feat(browser): My Browser node-anchored turn routing (stacks on #93411) — https://github.com/openclaw/openclaw/pull/93680
- PR #93187 draft=False fix(memory-core): exclude archive transcripts from dreaming corpus and propagate cron parentage to subagents — https://github.com/openclaw/openclaw/pull/93187
- PR #94308 draft=False feat(status): show session costs — https://github.com/openclaw/openclaw/pull/94308
- PR #67820 draft=False fix(whatsapp): reuse active QR and preserve runtime warnings — https://github.com/openclaw/openclaw/pull/67820
- PR #95517 draft=False fix(macos): recognize launchd Node.js gateway in PortGuardian sweep (fixes #94476) (AI-assisted) — https://github.com/openclaw/openclaw/pull/95517
- PR #95508 draft=False fix #95489: [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response — https://github.com/openclaw/openclaw/pull/95508
- PR #62503 draft=False feat: add devcontainer for cross-platform development — https://github.com/openclaw/openclaw/pull/62503
- PR #93168 draft=False fix(active-memory): exclude dreaming-narrative session keys from interactive eligibility gate — https://github.com/openclaw/openclaw/pull/93168
- PR #95527 draft=False fix(scripts): type windows taskkill helper — https://github.com/openclaw/openclaw/pull/95527
- PR #88684 draft=False Keep agent web_search on runtime provider resolution — https://github.com/openclaw/openclaw/pull/88684
- PR #88522 draft=True Fix Telegram active-run ingress sequencing — https://github.com/openclaw/openclaw/pull/88522
- PR #95487 draft=False feat(tts): strip emoji characters before speech synthesis (fixes #95478) — https://github.com/openclaw/openclaw/pull/95487
- PR #87958 draft=False fix(agents): scale read output for small contexts — https://github.com/openclaw/openclaw/pull/87958
- PR #85671 draft=False fix(outbound): auto-select single enabled message account — https://github.com/openclaw/openclaw/pull/85671
- PR #85670 draft=False perf(doctor): parallel I/O for repair sequence and plugin dep cleanup (A1) — https://github.com/openclaw/openclaw/pull/85670
- PR #78606 draft=False fix: keep origin-only approval delivery out of DMs — https://github.com/openclaw/openclaw/pull/78606
- PR #59859 draft=False feat: cute GTK-native Linux App (#75) — https://github.com/openclaw/openclaw/pull/59859
- PR #75225 draft=False feat(agents): add description field for dynamic agent discovery — https://github.com/openclaw/openclaw/pull/75225
- PR #49063 draft=False Telegram: allow native channel commands in explicitly allowed chats — https://github.com/openclaw/openclaw/pull/49063
- PR #94772 draft=False fix(gateway): cancel deferred channel reload when restart becomes pending — https://github.com/openclaw/openclaw/pull/94772
- PR #90610 draft=False Surface Codex final answer candidates in activity — https://github.com/openclaw/openclaw/pull/90610
- PR #93841 draft=False fix(ui): render persisted history text blocks — https://github.com/openclaw/openclaw/pull/93841
- PR #93351 draft=False feat(cli): add --message-file to openclaw agent — https://github.com/openclaw/openclaw/pull/93351
- PR #43493 draft=False feat: configure metadata (contextWindow, maxTokens, etc.) for custom provider setup — https://github.com/openclaw/openclaw/pull/43493
