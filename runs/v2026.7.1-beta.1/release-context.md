# Release Context — OpenClaw `v2026.7.1-beta.1`

Fetched at: `2026-07-02T08:01:28Z`

## Target

- Target tag: `v2026.7.1-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-beta.1
- Target tag SHA: 4eb1d333cfeca440b796b6a3f70d3c2bef996243

## Freshness baselines

- Latest beta tag: `v2026.7.1-beta.1`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.6.11`
- Prior prerelease baseline: `v2026.6.11-beta.2`

## Release notes excerpt


### Highlights

- **OpenAI GPT-5.6 support:** OpenClaw now recognizes the GPT-5.6 model family across catalog, capability, and runtime selection paths. (#98333) Thanks @steipete-oai.
- **External harness attachment:** `openclaw attach` launches an external harness against an existing Gateway session, making interactive Codex-style workflows easier to resume and inspect. (#96454) Thanks @anagnorisis2peripeteia and @obviyus.
- **Telegram Codex workflows:** Telegram can now start Codex pairing with `/login`, steer active Codex runs, and recover final replies across transient API failures. (#98006, #98126, #98786) Thanks @100yenadmin, @Kyzcreig, and @obviyus.
- **Event-driven cron runs:** the new `on-exit` schedule kind wakes an agent when a watched command exits, while session-targeted runs can detach cleanly. (#92037, #98755) Thanks @anagnorisis2peripeteia, @obviyus, and @EthanSK.
- **Native app refresh:** iOS adopts the iOS 26 visual system with clearer navigation, settings, Chat, Talk, and onboarding flows, while native app localization expands across Apple and Android surfaces. (#98452, #98736, #98811, #97110, #97111, #97112, #97113) Thanks @vincentkoc.
- **Richer messaging:** iMessage gains native poll creation, reading, and voting, and built-in usage footers provide clearer per-turn accounting in chat. (#98421, #92657, #92877) Thanks @omarshahine, @lobster, and @Marvinthebored.
- **Safer scoped conversations:** capability profiles prepare per-conversation tool and access boundaries without weakening the existing default profile. (#98536)

### Changes

- **Model and provider coverage:** add GPT-5.6 support, use Nemotron Super's 1M context window, and preserve explicit OpenRouter authentication headers. (#98333, #98726, #98187) Thanks @steipete-oai, @eleqtrizit, @sunlit-deng, and @laurencebrown.
- **CLI and node workflows:** add `openclaw attach`, node context-path support, actionable device-approval recovery guidance, and clearer plugin install exit diagnostics. (#96454, #97679, #98115, #98146, #98497) Thanks @anagnorisis2peripeteia, @obviyus, @wm0018, @welfo-beo, @RomneyDa, @Sanjays2402, and @vincentkoc.
- **Cron and usage:** add exit-triggered schedules, detached session-targeted runs, an in-flight job doctor warning, and a built-in full usage footer. (#92037, #98755, #98620, #92657, #92877) Thanks @anagnorisis2peripeteia, @obviyus, @EthanSK, @masatohoshino, and @Marvinthebored.
- **Native apps and localization:** modernize iOS navigation, settings, presentation, and Talk controls, add Gateway speech providers, improve QR onboarding and protocol recovery, localize core Apple and Android surfaces, and add Swedish mobile localization. (#98452, #98736, #98811, #98376, #98302, #98385, #97110, #97111, #97112, #97113, #98043) Thanks @Tony-ooo, @joelnishanth, @cursoragent, @joshavant, @vincentkoc, and @yeager.
- **Messaging capabilities:** add native iMessage polls and Telegram Codex pairing and steering flows. (#98421, #98006, #98126) Thanks @omarshahine, @lobster, @100yenadmin, and @Kyzcreig.
- **Doctor and diagnostics:** expose auth-profile, workspace, device-pairing, channel-plugin, memory-provider, systemd exhaustion, and Windows LAN firewall findings. (#97125, #97358, #97366, #97496, #97968, #98291, #98666) Thanks @giodl73-repo, @masatohoshino, and @joshavant.
- **Conversation and review controls:** prepare scoped conversation capability profiles and add Cursor Agent as an autoreview engine. (#98536, #97348) Thanks @hxy91819.

### Fixes

- **Telegram durability:** recover stalled ingress claims, retry restart-dropped media, survive transient polling errors, dead-letter poison updates, preserve forwarded rich text, route plugin callbacks correctly, and fall back safely when rich final replies are rejected. (#97118, #98102, #98735, #98775, #98776, #97174, #98786) Thanks @vincentkoc, @luoyanglang, @DaveArcher18, @obviyus, and @goldmar.
- **Agent and context reliability:** preserve runtime overrides and steered subagent tasks, keep isolated cron `sessions_send` replies from feeding back into the requester, improve harness-aware context estimation and compaction prechecks, time out silent local streams, recover mid-stream failures, and cap Gateway run-cache growth. (#92237, #92283, #77539, #97928, #97861, #98525, #95430, #77973) Thanks @sercada, @amittell, @liuhao1024, @yetval, @harjothkhara, @nailujac, @osolmaz, @lzyyzznl, @vincentkoc, @alexelgier, and @fede-kamel.
- **Provider and network safety:** bound oversized or malformed responses across Moonshot, MiniMax, Anthropic OAuth, Discord, Matrix, SMS, browser, update, embeddings, Tlön, and Inworld paths. (#96502, #96322, #96644, #97693, #97889, #97662, #97999, #98455, #98508, #98554, #98496, #98660) Thanks @hugenshen, @cursoragent, @lsr911, @solodmd, @Alix-007, @wings1029, @lzyyzznl, @sunlit-deng, @vincentkoc, and @Pandah97.
- **Channel delivery and routing:** keep Slack replies in the active thread, preserve account-bound delivery routes, apply response prefixes, suppress internal traces and unwanted fallback replies, clear Nostr relay publish timers, and retain WeChat session routing for opaque account ids. (#97168, #98240, #89949, #93639, #97989, #80928, #98720, #93686) Thanks @LiuwqGit, @gorkem2020, @yetval, @wangwllu, @ZengWen-DT, @alexuser, @UnClouded77, @wangmiao0668000666, @zhangLei99586, @zhangguiping-xydt, and @htkillermax-gif.
- **Cron correctness:** preserve provider and model selections on timeouts, retain startup catch-up deferrals, keep action-required output, clear blank thinking overrides, and preserve provider-owned daily-reset sessions. (#95943, #94022, #93810, #96393, #96293, #98356) Thanks @ZengWen-DT, @cursoragent, @luke-renjoy, @RichChen01, @vincentkoc, @yetval, @snowzlmbot, @nz365guy, and @takamasa-aiso.
- **Memory and session recovery:** detect unindexed transcripts, preserve notes and hand-edited frontmatter through transient wiki reads during note updates and ChatGPT imports without weakening directory and hardlink collision guards, avoid cross-directory resumes, disambiguate reserved wiki index pages, and skip empty QMD sync work. (#97857, #98360, #98787, #97785, #94326, #90030) Thanks @zw-xysk, @CHE10X, @qingminglong, @yetval, @vincentkoc, @sahibzada-allahyar, and @ruben2000de.
- **Windows and execution:** bind allowlisted execution to the validated Windows path, propagate `PATHEXT`, normalize inbound paths case-insensitively, and prevent cleanup crashes on Windows. (#98260, #98093, #97630, #97901) Thanks @eleqtrizit, @wendy-chsy, @VectorPeak, and @paulcam206.
- **Mobile and UI stability:** preserve iOS chat line breaks and final replies, improve Android pairing and TLS recovery, hide expired pairing cards, and keep workspace file rails scrollable. (#98304, #98117, #98366, #98439, #98483, #98049, #98646, #98611) Thanks @joshavant, @Jabato01, @ooiuuii, @wuqxuan, @645648406-max, and @zw-xysk.
- **Codex and approval flows:** report ChatGPT authentication correctly, preserve plugin app approvals in side conversations, rename destructive approval mode to `ask`, classify dynamic goal and session tool results accurately, and derive terminal-idle timeouts from the explicit run deadline. (#91240, #98812, #98501, #98659, #96856, #85296) Thanks @849261680, @ukstem, @kevinslin, @yetval, @nxmxbbd, @alkor2000, and @vincentkoc.
- **Configuration and plugin health:** surface unloadable channel plugins, preserve defaulted provider base URLs during patches, validate bundled plugin updates by manifest contract, and retain legacy ClawHub families where required. (#96397, #98396, #98010, #98249) Thanks @849261680, @momothemage, @weltmaister, @LiLan0125, @herove, and @Patrick-Erichsen.
- **Gateway, browser, and setup diagnostics:** distinguish a reachable Gateway from a failed status probe, reject loosely parsed Gateway ports during setup, and avoid creating stray Chrome profile configuration keys from empty paths. (#98183, #98689, #98138) Thanks @masatohoshino, @qingminglong, and @zhangLei99586.

### Complete contribution record

This audited record covers the complete 66e676d29b92d040716376a75aca32bad655cfac..HEAD history: 222 merged PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

#### Pull requests

- **PR #96502** fix(moonshot): bound video description JSON response reads. Thanks @hugenshen and @cursoragent.
- **PR #98249** Preserve legacy ClawHub family for selected plugins. Thanks @Patrick-Erichsen.
- **PR #93767** fix(reasoning-tags): strip MiniMax `mm:` namespaced reasoning tags. Thanks @DrHack1.
- **PR #93820** fix(imessage): recognize MiniMax mm: reasoning tags in reflection guard (completes #93767). Thanks @Alix-007.
- **PR #94096** fix(usage): reject inverted startDate-endDate range in usage.cost and sessions.usage. Thanks @Alix-007.
- **PR #97125** Doctor: expose auth profile findings. Thanks @giodl73-repo.
- **PR #98256** fix(mcp): require owner for Claude permission replies. Thanks @eleqtrizit.
- **PR #98142** fix(cli): stop `pairing list` crashing with empty channel enum. Thanks @RomneyDa.
- **PR #98260** fix(exec): bind Windows allowlist execution path. Thanks @eleqtrizit.
- **PR #97118** fix(telegram): recover stalled ingress spool claims. Thanks @vincentkoc.
- **PR #97168** fix(slack): prefer current thread session for inherited outbound replies. Related #96535. Thanks @LiuwqGit and @gorkem2020.
- **PR #97769** fix(plugins): apply output text transforms to toolcall_delta and toolcall_end events. Related #97761. Thanks @ZOOWH and @get-viti.
- **PR #96544** fix(doctor): merge colliding model-ref map keys instead of dropping. Thanks @yetval and @vincentkoc.
- **PR #97177** fix(memory-wiki): gracefully handle unparsable YAML frontmatter in vault scans (#96125). Thanks @SunnyShu0925 and @cow11023.
- **PR #97167** fix #96840: [Bug]: Targetless message.send fails with 'Action send requires a target' in WebChat despite docs stating source-reply sink should handle it. Thanks @zhangguiping-xydt and @MantisCartography.
- **PR #98302** fix(ios): advance onboarding step after QR scan. Related #98297. Thanks @joelnishanth and @cursoragent.
- **PR #96644** fix(anthropic-oauth): bound OAuth token endpoint response reads. Thanks @solodmd.
- **PR #96397** fix: warn when configured channel plugins cannot load. Thanks @849261680.
- **PR #96359** test: migrate src/commands tests to shared temp dir helpers. Thanks @xialonglee.
- **PR #96293** fix(cron): clear agentTurn thinking override by blanking the field. Related #96287. Thanks @ZengWen-DT and @takamasa-aiso.
- **PR #96058** test: prefer shared temp dir helpers in auto-reply and install-fallback tests. Thanks @xialonglee.
- **PR #87298** test: add temp directory helper guidance. Thanks @hxy91819.
- **PR #97785** fix(sessions): avoid cross-cwd recent resumes. Related #96542. Thanks @qingminglong and @yetval.
- **PR #97698** fix(pdf): reject empty parsed page ranges before native analysis. Thanks @zhangguiping-xydt.
- **PR #97693** fix(discord): bound requestDiscord happy-path response reads to prevent OOM. Thanks @Alix-007.
- **PR #97683** fix(irc): guard surrogate-range codepoints in \u literal-escape decoder. Thanks @llagy009.
- **PR #96938** fix(utils): keep reply directive ids unicode-safe. Thanks @ly-wang19.
- **PR #97857** fix(memory): detect unindexed session transcripts in status mode (fixes #97814). Thanks @zw-xysk and @CHE10X.
- **PR #98094** fix(android): clarify gateway auth recovery states. Thanks @qingminglong.
- **PR #98205** test(gateway): add unit tests for node wake state tracking and testing seam. Thanks @zenglingbiao.
- **PR #98115** fix: surface node approval guidance from devices CLI. Thanks @welfo-beo.
- **PR #97898** docs: clarify source checkout Node floor. Related #97792. Thanks @lin-hongkuan and @aniruddhaadak80.
- **PR #94526** test(telegram): add regression test for forum topic message_thread_id with streamed reasoning. Related #89352. Thanks @xialonglee and @pmika.
- **PR #98145** fix(device-pairing): don't churn requestId on subset re-requests. Thanks @RomneyDa.
- **PR #98267** fix(system-prompt): move exec-approval + Authorized Senders below cache boundary. Related #98261. Thanks @headbouyJB.
- **PR #98304** fix: preserve iOS chat line breaks. Related #98028. Thanks @joshavant and @Jabato01.
- **PR #98187** fix(openrouter): send explicit auth headers. Related #97934. Thanks @sunlit-deng and @laurencebrown.
- **PR #95708** fix: show WebChat preamble progress during tool activity. Thanks @ragesaq.
- **PR #98210** fix(gateway): iOS Talk treats SecretRef-backed API keys as missing. Related #98209. Thanks @ooiuuii.
- **PR #98009** test(infra): add unit tests for SQLite number normalization. Thanks @dwc1997.
- **PR #98087** test(config): add unit tests for resolveExecCommandHighlighting. Thanks @solodmd.
- **PR #98219** test(utils): add unit tests for chunkItems. Thanks @zenglingbiao.
- **PR #98093** fix(core): propagate caller env PATHEXT through isExecutableFile on Windows. Thanks @wendy-chsy.
- **PR #97973** fix(matrix): guard JSON.parse against malformed homeserver response bodies. Thanks @lsr911.
- **PR #97999** fix(sms): guard Twilio JSON.parse against malformed API response bodies. Thanks @lsr911.
- **PR #98043** Add Swedish mobile app localization. Thanks @yeager.
- **PR #98144** fix(tui): correct disconnect copy for device scope upgrades. Thanks @RomneyDa.
- **PR #98240** fix(agents): keep merged delivery routes account-bound. Thanks @yetval.
- **PR #89949** fix(media): pin requester delivery route when task starts. Thanks @wangwllu.
- **PR #98226** Redact bare Fireworks API keys. Related #98225. Thanks @ooiuuii.
- **PR #98319** docs: publish release notes for v2026.6.11. Thanks @hannesrudolph.
- **PR #98257** fix: show in-progress status for channel runs. Thanks @scotthuang.
- **PR #97931** fix(gateway): keep provider-owned CLI sessions across the daily default reset. Thanks @yetval.
- **PR #98325** docs: refresh docs map for v2026.6.11. Thanks @hannesrudolph.
- **PR #97929** fix(auto-reply): stop level directives from eating the next message word. Thanks @yetval.
- **PR #97928** fix(agents): estimate harness role sizes in context guard char estimator (fixes #97927). Thanks @liuhao1024 and @yetval.
- **PR #97861** fix(compaction): count bashExecution and summary turns in pre-prompt overflow precheck. Thanks @yetval.
- **PR #97137** doctor: add memory search lint findings. Thanks @giodl73-repo.
- **PR #97358** Doctor: expose workspace status findings. Thanks @giodl73-repo.
- **PR #95622** test(qa-lab): harden whatsapp qa scenarios. Thanks @mcaxtr.
- **PR #98346** fix: prevent skill-creator from bypassing workshop proposals. Related #96054. Thanks @momothemage and @xianshishan.
- **PR #98169** fix(heartbeat): scope commitment fan-out prompts. Thanks @bdjben.
- **PR #97366** Doctor: expose device pairing findings. Thanks @giodl73-repo.
- **PR #98366** fix: Android TLS fingerprint verification times out on slow handshakes. Related #98365. Thanks @joshavant.
- **PR #98353** fix(ios): open app on Chat by default. Thanks @BsnizND.
- **PR #98352** fix(security): warn on agent skill MCP boundary drift. Thanks @momothemage.
- **PR #98347** fix: retry image describe fallback models. Thanks @momothemage.
- **PR #98117** fix(ios): avoid transient duplicate final replies. Related #98116. Thanks @ooiuuii and @joshavant.
- **PR #98293** fix(gateway): emit stale exec approval followup diagnostics. Thanks @BsnizND.
- **PR #98376** fix(ios): use Gateway speech providers in Talk. Related #98153. Thanks @Tony-ooo.
- **PR #66685** Suppress expired exec approval followup warnings. Thanks @pfrederiksen.
- **PR #98385** fix: show actionable mobile protocol mismatch recovery. Related #98384. Thanks @joshavant.
- **PR #98146** fix(cli): explain how to recover from device approve deadlock. Thanks @RomneyDa.
- **PR #98423** improve(ios): clarify Control and Talk visual hierarchy. Related #98397.
- **PR #98217** fix(doctor): recover legacy cron archive across devices. Thanks @masatohoshino.
- **PR #98333** feat(openai): add GPT-5.6 series support. Related #98296. Thanks @steipete-oai.
- **PR #96393** fix(cron): preserve action-required command output. Related #96346. Thanks @snowzlmbot and @nz365guy.
- **PR #98429** fix(ios): classify TLS fingerprint timeouts. Thanks @joshavant.
- **PR #98439** fix: Android setup codes accept local mDNS gateway hosts. Thanks @joshavant.
- **PR #98443** fix(ios): improve light and dark appearance contrast. Related #98440.
- **PR #97742** fix(llm): preserve structured tool result text across providers. Thanks @snowzlmbot.
- **PR #97968** fix(status): surface unregistered memory embedding providers. Thanks @masatohoshino.
- **PR #92237** fix(agents): preserve runtime settings overrides [AI-assisted]. Thanks @sercada.
- **PR #95888** fix(active-memory): caveat mutable ops facts; mark truncated recall as incomplete. Thanks @spencer2211.
- **PR #98291** fix(gateway): surface systemd start-limit exhaustion. Thanks @masatohoshino.
- **PR #90517** fix(gateway): hint missing external plugin for web login. Related #83277. Thanks @TUARAN and @carol-iung.
- **PR #98369** test(infra): add unit tests for SQLite user_version pragma helper. Thanks @dwc1997.
- **PR #98340** fix: extension api.exec leaves child processes after timeout. Related #98335. Thanks @ooiuuii.
- **PR #92063** fix(ui): collapse duplicate assistant groups during segmented streaming. Related #63956. Thanks @harjothkhara and @contentfree.
- **PR #98354** fix(infra): guard delivery queue inflate against corrupted entry_json. Thanks @Pick-cat.
- **PR #90566** fix(agents): warn on cron announce skip. Related #68561. Thanks @sahibzada-allahyar and @Mibslee.
- **PR #98371** fix(ports): validate lsof PID parsing before assignment. Thanks @lzyyzznl.
- **PR #98356** fix(cron): keep provider-owned CLI sessions across the daily default reset. Thanks @yetval.
- **PR #98395** test(shared): add unit tests for account enabled guard. Thanks @dwc1997.
- **PR #98411** fix(agents): recover thinking errors from provider body. Related #98308. Thanks @sunlit-deng and @clearhorizoninvestments.
- **PR #98494** docs(skills): support variable landable sweep batches. Thanks @vincentkoc.
- **PR #91240** fix: report Codex ChatGPT status auth. Related #91099. Thanks @849261680 and @ukstem.
- **PR #98370** test(agents): add unit tests for thinking block detection. Thanks @dwc1997.
- **PR #96711** test: prefer shared temp dir helpers in config, gateway, cron, crestodian, and state tests. Thanks @xialonglee.
- **PR #98483** fix: Android QR scan starts gateway pairing. Thanks @joshavant.
- **PR #95230** fix docs-list-mdx-pages. Thanks @hugenshen.
- **PR #96322** fix(minimax): bound JSON response reads to prevent OOM. Thanks @lsr911.
- **PR #95348** fix config-chmod-warning. Thanks @hugenshen and @cursoragent.
- **PR #95229** fix(copilot): guard against undefined runtime.state during cli-metadata registration. Related #94516. Thanks @sunlit-deng and @cuihaijun.
- **PR #94636** fix(memory): skip raw snippets during promotion. Thanks @tayoun.
- **PR #94013** [AI] fix(feishu): guard partial channelRuntime in monitor startup. Thanks @xydt-tanshanshan.
- **PR #93466** [AI] fix(feishu): guard against missing inbound in channelRuntime fallback. Thanks @xydt-tanshanshan.
- **PR #98049** fix: hide expired pairing QR cards in Control UI. Related #98039. Thanks @ooiuuii.
- **PR #96094** fix(memory): prove live manager recovery after CLI reindex. Related #91167. Thanks @849261680 and @kiagentkronos-cell.
- **PR #98482** fix: advertise route-aware LAN Control UI links. Thanks @joshavant.
- **PR #71537** Recover archived (.reset) session transcripts in memory hook + session-logs skill. Thanks @injinj.
- **PR #96375** docs(config-agents): correct built-in alias table for opus and gpt. Thanks @niks999.
- **PR #98453** docs(gateway): fix Telegram streaming default in config-channels.md. Thanks @solodmd.
- **PR #98533** fix: repair hosted CI baseline assertions.
- **PR #98421** feat(imessage): native poll support — create, read, vote. Thanks @omarshahine and @lobster.
- **PR #98318** docs(matrix): document missing streaming.progress mode, progress sub-fields, and mentionPatterns config. Thanks @wm0018 and @vincentkoc.
- **PR #97753** docs(onboard): document 11 missing non-interactive CLI flags. Thanks @wm0018 and @vincentkoc.
- **PR #97851** fix(mattermost): bound null-body error response reads. Thanks @Pick-cat.
- **PR #98360** fix(memory-wiki): preserve notes after transient page reads. Related #98345. Thanks @qingminglong and @yetval.
- **PR #98551** test: fix stale core test type failures. Thanks @RomneyDa.
- **PR #98455** fix(browser): bound error body read in fetchHttpJson to prevent OOM. Thanks @wings1029.
- **PR #95906** fix(code-mode): surface QuickJS error name and message to the model. Thanks @ZengWen-DT and @vincentkoc.
- **PR #97901** fix(agents): stop copilot autoreview cleanup crash on Windows. Thanks @paulcam206.
- **PR #97923** fix(slack): truncate served arg-menu option labels on a surrogate boundary. Thanks @LEXES7.
- **PR #98010** fix(update): validate bundle plugin payloads by manifest contract. Related #97985. Thanks @LiLan0125 and @herove.
- **PR #85296** fix(codex): derive terminal-idle watchdog from explicit run timeout. Thanks @alkor2000 and @vincentkoc.
- **PR #97110** feat(i18n): add native app locale inventory. Thanks @vincentkoc.
- **PR #98396** fix: allow config.patch with defaulted provider baseUrl. Related #98270. Thanks @momothemage and @weltmaister.
- **PR #98503** fix(usage-bar): use Object.hasOwn instead of in operator to avoid prototype chain pollution. Related #98466. Thanks @chenyangjun-xy and @zhangLei99586.
- **PR #97111** feat(android): localize core gateway surfaces. Thanks @vincentkoc.
- **PR #97630** fix(media): normalize Windows inbound paths case-insensitively. Thanks @VectorPeak.
- **PR #82638** fix(agents): skip implicit provider discovery when models.mode is 'replace' [AI-assisted]. Related #66957. Thanks @eldar702 and @wangzhengshu.
- **PR #87917** fix sessions json lineage metadata. Related #80286. Thanks @zhangguiping-xydt and @islandpreneur007.
- **PR #93639** fix(message-tool): apply messages.responsePrefix to outbound sends. Thanks @ZengWen-DT.
- **PR #94440** fix: #94432 classify Cloudflare challenge 403 as upstream_html instead of auth_html. Thanks @lzyyzznl and @pbm9z95m6z-hue.
- **PR #98119** fix: reduce Docker build memory pressure. Related #98118. Thanks @zyzo.
- **PR #97679** feat(node): add --context-path flag to node run/install for reverse-p…. Related #97678. Thanks @wm0018.
- **PR #98339** fix(irc): classify host-less nick!user allowlist entries as mutable. Thanks @yetval.
- **PR #97662** fix(matrix): bound raw transport response reads to prevent OOM. Thanks @Alix-007.
- **PR #98137** fix: hoist timer declaration to avoid TDZ ReferenceError in abortable delay. Thanks @zhangLei99586.
- **PR #98134** fix: clear timeout timer in Tailscale binary probe Promise.race. Thanks @zhangLei99586.
- **PR #97989** fix(sms): stop internal tool-trace banners from reaching SMS replies. Thanks @ZengWen-DT.
- **PR #97972** fix(browser): CDP auth fails with percent-encoded credentials. Thanks @VectorPeak.
- **PR #98063** fix(reply): suppress tool-error progress delivery when messages.suppressToolErrors is set. Thanks @moeedahmed and @amittell.
- **PR #94964** fix(reload): cancel deferred channel reload on in-process restart. Related #79487. Thanks @lzyyzznl and @tseller.
- **PR #98598** fix: restore main lint after timer repairs. Related #98462, #98464. Thanks @zhangLei99586.
- **PR #98587** fix(slack): guard relay WebSocket frame JSON.parse against malformed input. Thanks @lsr911 and @vincentkoc.
- **PR #90030** fix(memory-core): skip qmd zero-hit search sync. Related #90023. Thanks @sahibzada-allahyar and @ruben2000de.
- **PR #98493** fix(transcripts): close readline interface and destroy read stream on error exit. Related #98467. Thanks @wangmiao0668000666 and @zhangLei99586.
- **PR #98497** fix(cli): show exit code when plugin npm install returns empty output. Thanks @Sanjays2402 and @vincentkoc.
- **PR #97112** feat(apple): localize core native app surfaces. Thanks @vincentkoc.
- **PR #98610** fix: restore tooling CI after transcript test addition.
- **PR #77539** fix(subagent): preserve steered task text on restart redispatch. Thanks @amittell.
- **PR #97113** feat(i18n): refresh all native locale artifacts. Thanks @vincentkoc.
- **PR #98620** feat(doctor): warn about in-flight cron jobs. Thanks @masatohoshino.
- **PR #98605** test(shared): add unit tests for human-readable list formatting. Thanks @dwc1997.
- **PR #97348** feat(autoreview): support cursor-agent engine. Thanks @hxy91819.
- **PR #95943** fix(cron): preserve provider/model on isolated-run timeout row. Related #95873. Thanks @ZengWen-DT and @cursoragent and @luke-renjoy.
- **PR #94149** fix(status): bound systemd service probes so status cannot hang on a wedged systemctl (#84698). Thanks @ZengWen-DT and @cursoragent and @zus-assistant.
- **PR #88159** fix(cli): retry logs.tail after journal fallback in logs follow. Thanks @anyech and @vincentkoc.
- **PR #98508** fix(update-check): bound npm registry JSON response read to prevent OOM. Thanks @lzyyzznl.
- **PR #98496** fix(tlon): bound error response body reads to prevent OOM. Thanks @Pandah97.
- **PR #98554** fix(openai): bound embedding batch file downloads. Thanks @sunlit-deng and @vincentkoc.
- **PR #98652** fix: stop invalid message timeouts from stalling.
- **PR #77973** fix(gateway): cap agentRunCache to prevent unbounded growth under run fan-out. Related #77976. Thanks @fede-kamel and @vincentkoc.
- **PR #98525** fix(agents): time out local streams without first event. Thanks @osolmaz.
- **PR #94022** fix(cron): persist startup catch-up deferral ids in service state to prevent read-RPC clobber. Related #93935. Thanks @RichChen01 and @vincentkoc and @yetval.
- **PR #93810** fix(cron): preserve startup overflow catch-up deferrals in start() maintenance pass. Thanks @yetval and @vincentkoc.
- **PR #98623** fix: media tools skip env-key provider plugins when auto-selecting models. Thanks @medns.
- **PR #98665** fix(claude-cli): return updatedInput in can_use_tool allow response for Claude Code 2.1. Related #95171. Thanks @yetval and @carterdawson.
- **PR #94250** fix(feishu): send blocks as independent messages when blockStreaming is enabled. Related #55027. Thanks @xialonglee and @vincentkoc and @ZichaoLong.
- **PR #93379** fix(whatsapp): thread authDir through command authorization and owner bypass for LID JID resolution. Related #77755. Thanks @xialonglee and @jiveshkalra.
- **PR #98646** fix: keep workspace rail file sections scrollable. Related #98566. Thanks @wuqxuan and @645648406-max.
- **PR #98602** fix: iOS Talk fallback settings opens Voice & Talk. Related #98593. Thanks @PollyBot13.
- **PR #98611** fix(ui): add overflow-y:auto to workspace rail sections to prevent file list overflow (fixes #98566). Thanks @zw-xysk and @645648406-max.
- **PR #98619** fix(qa-lab): credential lease requests fail on oversized Convex broker responses. Thanks @ZengWen-DT.
- **PR #94326** fix(memory-wiki): disambiguate the reserved index page stem for synthesis and ingest. Thanks @yetval and @vincentkoc.
- **PR #98659** fix(codex): classify get_goal read statuses as successful dynamic tool calls. Thanks @yetval.
- **PR #96856** fix(codex): successful sessions_spawn and goal tool results recorded as failures. Thanks @nxmxbbd.
- **PR #98660** fix(inworld): guard voices JSON.parse against malformed API response bodies. Thanks @solodmd.
- **PR #95430** fix(embedded-agent-runner): pump async streamFn through pumpStreamWithRecovery for mid-stream error recovery. Related #95429. Thanks @lzyyzznl and @vincentkoc and @alexelgier.
- **PR #98644** fix: tool summaries preserve emoji truncation boundaries. Thanks @ZengWen-DT.
- **PR #80928** fix(telegram): suppress fallback reply when plugin command returns suppressReply: true. Related #80756. Thanks @alexuser and @UnClouded77.
- **PR #98701** fix: prevent agents-tools message test timeouts.
- **PR #92657** feat(usage): ship built-in /usage full footer. Thanks @Marvinthebored.
- **PR #92877** fix(usage): make built-in footer easier to wrap on Telegram. Thanks @Marvinthebored.
- **PR #98126** Restore Telegram /steer for active Codex runs. Related #81594. Thanks @100yenadmin and @Kyzcreig.
- **PR #92037** feat(cron): on-exit schedule — wake on a watched command's exit. Thanks @anagnorisis2peripeteia.
- **PR #98452** feat(ios): modernize the app with iOS 26 Liquid Glass.
- **PR #98006** Add Telegram /login Codex pairing flow. Thanks @100yenadmin.
- **PR #98735** fix(telegram): preserve rich forwarded message text. Thanks @obviyus.
- **PR #97962** refactor(qa): use transport-native actions in flow scenarios. Thanks @RomneyDa.
- **PR #98726** fix(nvidia): use Nemotron Super 1M context. Thanks @eleqtrizit.
- **PR #98691** fix(imessage): shed emoji anywhere in poll-vote echo match. Thanks @omarshahine.
- **PR #97174** Fix Telegram plugin callback routing. Thanks @goldmar.
- **PR #89597** fix: migrate QQBot credential backups to SQLite KV.
- **PR #98536** feat: prepare scoped conversation capability profiles.
- **PR #92274** fix(agents): classify embedded prompt lock error as permanent announce failure. Related #91527. Thanks @fsdwen and @zackchiutw.
- **PR #98102** fix(telegram): durably retry inbound media dropped during restart (#98076). Thanks @luoyanglang and @DaveArcher18.
- **PR #98755** fix(cron): detach session-targeted runs. Related #98121. Thanks @obviyus and @EthanSK.
- **PR #96065** fix(install): manage config-secretref env refs via OPENCLAW_SERVICE_MANAGED_ENV_KEYS. Thanks @Darren2030 and @obviyus.
- **PR #98666** fix: diagnose Windows LAN Gateway firewall blocks. Thanks @joshavant.
- **PR #98501** fix(codex): rename destructive approval mode to ask. Related #98499. Thanks @kevinslin.
- **PR #98775** fix(telegram): survive transient getUpdates errors and stop per-send cache rewrites. Related #98772, #98773. Thanks @obviyus.
- **PR #98776** fix(telegram): back off, dead-letter, and tombstone spooled updates so poison messages cannot block or duplicate. Related #98774. Thanks @obviyus.
- **PR #96454** feat(cli): openclaw attach — launch an external harness bound to a gateway session. Thanks @anagnorisis2peripeteia and @obviyus.
- **PR #98786** fix(telegram): final replies no longer drop on rejected rich entities, captions, quotes, or long flood waits. Related #98778. Thanks @obviyus.
- **PR #97496** Doctor: expose channel plugin blocker findings. Thanks @giodl73-repo.
- **PR #98792** fix(ci): restore docs and test type checks.
- **PR #98736** improve(ios): simplify Talk controls and composer alignment.
- **PR #97889** fix(discord): guard JSON.parse against malformed API response bodies. Thanks @lsr911.
- **PR #98812** fix(codex): preserve plugin app approvals in side conversations.
- **PR #92283** fix(agents): don't inject A2A turns into isolated-cron sessions_send (#92257). Thanks @harjothkhara and @nailujac.
- **PR #98138** fix: guard setDeep against empty keys array in Chrome profile decoration. Thanks @zhangLei99586.
- **PR #98183** fix(gateway): distinguish reachable gateway from failed status probe. Thanks @masatohoshino.
- **PR #98689** fix(wizard): reject loose gateway port input. Related #98681. Thanks @qingminglong.
- **PR #98720** fix(nostr): clear per-relay publish timeout timer to prevent dangling handles. Related #98463. Thanks @wangmiao0668000666 and @zhangLei99586.
- **PR #98818** fix(ci): recover incomplete Swift build caches.
- **PR #98787** fix(memory-wiki): retry transient existing-page reads in wiki_apply and chatgpt import. Thanks @yetval.
- **PR #98811** feat(ios): modernize navigation and settings. Related #98803.
- **PR #98843** docs: update mobile app release messaging. Thanks @joshavant.
- **PR #93686** fix(weixin): startAccount preserves session routing. Related #93556. Thanks @zhangguiping-xydt and @htkillermax-gif.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.7.1-beta.1
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.7.1-beta.1.tgz
- integrity: `sha512-Yu/ELLje9mxvFTlaxVGHnIkKvHcLnoEj3AQhzmhpP4k8Fi7/ln0NvYnBgaZ2BJ8tdAAsq3iZ8uroRUuXiMB0dg==`
- release SHA: `4eb1d333cfeca440b796b6a3f70d3c2bef996243`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.7.1-beta.1/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/28571485937
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/28569693832
- full release validation: https://github.com/openclaw/openclaw/actions/runs/28569693812
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/28571834366
- plugin ClawHub publish: success: https://github.com/openclaw/openclaw/actions/runs/28571835541
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/28572195585
- package Telegram E2E: passed in release checks: https://github.com/openclaw/openclaw/actions/runs/28569815816/job/84705725486
- advisory WhatsApp live QA: blocked before scenarios by exhausted Convex credential pool after two attempts: https://github.com/openclaw/openclaw/actions/runs/28569693831


## Recent issue risk signals

- #98986 [no-labels] [Migrate]: transcripts store (meeting capture) to SQLite — https://github.com/openclaw/openclaw/issues/98986

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #98892 draft=False fix: harden formatCurrencyAmount, formatCoords, and record code-mode bridge rejections — https://github.com/openclaw/openclaw/pull/98892
- PR #56806 draft=False feat(exec): expose knownLongFlags in safeBinProfiles config schema — https://github.com/openclaw/openclaw/pull/56806
- PR #98987 draft=False test: migrate docs-path and system-prompt-params tests to shared temp-dir helpers — https://github.com/openclaw/openclaw/pull/98987
- PR #58367 draft=True Gateway: preserve approved scope baseline during pairing — https://github.com/openclaw/openclaw/pull/58367
- PR #98860 draft=False fix(codex): guard parseRequest JSON.parse against malformed WebSocket data — https://github.com/openclaw/openclaw/pull/98860
- PR #59705 draft=True [codex] improve parallels windows smoke logging — https://github.com/openclaw/openclaw/pull/59705
- PR #58378 draft=True macOS: confirm discovered gateway trust — https://github.com/openclaw/openclaw/pull/58378
- PR #94566 draft=False fix(android): make offline chat actionable — https://github.com/openclaw/openclaw/pull/94566
- PR #61519 draft=False CI: report circular dependencies in PRs — https://github.com/openclaw/openclaw/pull/61519
- PR #61485 draft=False feat(plugins): upgrade llm_input/llm_output hooks from fire-and-forget to modifying — https://github.com/openclaw/openclaw/pull/61485
- PR #98952 draft=False fix(process): resolve gemini .cmd shim on Windows in supervisor child adapter — https://github.com/openclaw/openclaw/pull/98952
- PR #61396 draft=False fix(i18n): add device/node pairing terms to zh-CN glossary — https://github.com/openclaw/openclaw/pull/61396
- PR #61306 draft=False Claw: add mission control backbone — https://github.com/openclaw/openclaw/pull/61306
- PR #98823 draft=False fix(gateway): return structured capability error when node lacks exec approvals — https://github.com/openclaw/openclaw/pull/98823
- PR #98985 draft=False fix: clean up iOS About page copy — https://github.com/openclaw/openclaw/pull/98985
- PR #98988 draft=False fix(tools-manager): replace spawnSync extraction with safe extractArchive API — https://github.com/openclaw/openclaw/pull/98988
- PR #60860 draft=False feat(google): add Google Vertex AI provider with ADC auth and global endpoint routing — https://github.com/openclaw/openclaw/pull/60860
- PR #55901 draft=False feat(irc): support markdown messages via draft/multiline — https://github.com/openclaw/openclaw/pull/55901
- PR #60488 draft=False fix(security): close active April 4 transport and auth gaps — https://github.com/openclaw/openclaw/pull/60488
- PR #98941 draft=False fix(extensions): bound success-path JSON response reads — https://github.com/openclaw/openclaw/pull/98941
- PR #97134 draft=False fix(deepseek): recover V4 zero-cost spend — https://github.com/openclaw/openclaw/pull/97134
- PR #60212 draft=False [codex] Cron: repair empty sanitized final replies — https://github.com/openclaw/openclaw/pull/60212
- PR #54716 draft=False Fix sessions.list for literal per-agent store paths — https://github.com/openclaw/openclaw/pull/54716
- PR #59986 draft=True refactor(plugins): add lane-oriented channel interface — https://github.com/openclaw/openclaw/pull/59986
- PR #51067 draft=False feat(gateway): add configurable Control UI title — https://github.com/openclaw/openclaw/pull/51067
- PR #98997 draft=False fix(model-selection): warn on duplicate model aliases instead of silently overwriting [AI-assisted]model-selection: warn on duplicate model aliases instead of silently … — https://github.com/openclaw/openclaw/pull/98997
- PR #59214 draft=False Add user chat bubble color selector for macOS application — https://github.com/openclaw/openclaw/pull/59214
- PR #58823 draft=False fix(agents): restore global subagent model default priority over agent own model — https://github.com/openclaw/openclaw/pull/58823
- PR #58636 draft=False feat(tui): add /upload command for file context — https://github.com/openclaw/openclaw/pull/58636
- PR #58421 draft=False feat(plugins): add optional api.resetSession() — https://github.com/openclaw/openclaw/pull/58421
