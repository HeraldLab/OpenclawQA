# Release Context — OpenClaw `v2026.7.2-beta.7`

Fetched at: `2026-08-02T08:30:16Z`

## Target

- Target tag: `v2026.7.2-beta.7`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.7.2-beta.7
- Target tag SHA: dabe1915362e20c25704af91612a32a8f4c96e83

## Freshness baselines

- Latest beta tag: `v2026.7.2-beta.7`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.7.1`
- Prior prerelease baseline: `v2026.7.2-beta.6`

## Release notes excerpt

## 2026.7.2

### Highlights

- **State safety and recovery:** protect persisted data with a quarantine store that survives primary-database damage, crash-recoverable SQLite snapshots, crash-durable filesystem publication, schema-upgrade data-loss rejection, and rollback-writer snapshot recovery. (#110453, #113367, #113453, #113473, #113580) Thanks @vincentkoc.
- **Durable channel delivery:** keep accepted messages recoverable across gateway restarts and local crashes through the shared ingress drain and dead-letter recovery, covering Telegram, Signal, Slack, QQBot, Twitch, Synology Chat, Tlon, IRC, and Zalo User. #108656, #107246, #109911 (#108924, #107288, #109907, #109910, #110844, #110852, #110899, #110910, #110914, #110916, #111029) Thanks @obviyus and @edenfunf.
- **Session rewind and branching:** rewind or fork conversations from individual messages, switch transcript branches across web and native apps, fork upstream Codex sessions, preserve branch-safe queued sends, reject stale-pane writes, and restore prompt images after a fork. (#110660, #110857, #110886, #111149, #112056, #112284, #113073, #113945) Thanks @vincentkoc.
- **Interactive MCP Apps and dashboards:** host ticketed MCP Apps with bound tools, resources, and bounded context updates; open them from channel replies, pin them to durable dashboards, harden their shared sandbox, and let native plugins declare them directly. #109851, #110451, #113218 (#109861, #109807, #110515, #111211, #111212, #111524, #111687, #111748, #113224) Thanks @fuller-stack-dev.
- **Questions and approvals everywhere:** let agents ask structured questions with option cards across web, channels, macOS, and native apps, while approvals gain push notifications, history, fair queuing, headless resolution, Claude tool-request relay, reviewer detail, and clearer formatted prompts. #85954 (#108505, #108709, #108776, #109922, #110242, #110372, #110584, #110681, #110989, #111060, #112918, #113027, #113193) Thanks @omarshahine.
- **Meetings and realtime Talk:** join Teams, Zoom, and Google Meet calls with default-enabled meeting plugins and durable transcript collection, while realtime Talk adds OpenAI and Gemini video and requires a supported OpenAI Platform API key instead of the rejected Codex OAuth fallback. #86425, #113353, #115021 (#109579, #109719, #109964, #111048, #113022, #113053, #113122, #113354, #115211) Thanks @shushushv, @Solvely-Colin, and @vincentkoc.
- **Wear OS companion:** add the phone-proxied Wear companion with home-screen agent/session/model selection, realtime Talk controls, audio-reactive playback, and an instant-talk tile. #108781 (#108835, #109341, #109433, #109483, #110661, #111516, #112721) Thanks @sibbl, @IWhatsskill, and @Solvely-Colin.
- **Guided setup and local inference:** guide setup across browser, Linux, and macOS with local-provider detection, strongest-model selection, downloadable models, lean mode, memory imports, and an in-process RAM-gated llama.cpp/Gemma path. #108604 (#108605, #108868, #108977, #109250, #109444, #109585, #110054, #110141, #110596, #113476)

### Changes

- **Models and providers:** add Claude Opus 5 across catalog and runtime, Kimi K3, and GPT Live realtime support with the supported Platform API authentication path. (#113391, #113392, #113633; related #113412; #113909, #113354; related #113353) Thanks @fuller-stack-dev, @vincentkoc, and @Solvely-Colin.
- **Local inference and setup:** detect local inference providers during onboarding, add in-process llama.cpp GGUF inference and Baseten Model API support, discover models from live provider catalogs, and offer model downloads from web and macOS setup. (#108605; related #108604; #109444, #108708; related #108665; #112412; related #112405; #113476) Thanks @fuller-stack-dev.
- **Sessions and dashboards:** add rewind/fork and branch switching across web and native chat, session boards and dashboards, archived/visibility/draft/incognito session states, and suggestion queues with typing indicators. (#110660, #110857, #110886, #111149, #110644, #110960, #112554, #112787, #113006, #113127, #113173)
- **Native apps:** bring Quick Chat to macOS and Linux with streaming, routing, context capture, dictation, and model controls; add Linux desktop integration and signed updates; add multi-gateway apps and mobile dashboards; and expand Wear OS companion/Talk support. (#109720, #109947, #110285, #110631, #110632, #110635, #110994, #109236, #108770, #111932; related #111931; #112163, #109341, #109433; related #108781; #109483, #112721) Thanks @sibbl, @IWhatsskill, @Solvely-Colin, and @vincentkoc.
- **Meetings:** add Teams and Zoom meeting guests, enable Teams, Zoom, and Google Meet plugins by default, and automatically collect durable meeting transcripts. (#109964, #111048, #113022, #113053, #113122)
- **Channels:** add the Buzz plugin, Slack user-identity and Agent View modes, Telegram Bot API rich blocks and native Markdown lists, and richer Matrix formatting. (#113419, #109837, #103895; related #103673; #107986, #113158, #113199) Thanks @Patrick-Erichsen and @obviyus.
- **Browser and MCP Apps:** add a secure per-tab browser copilot, batch browser CLI, bounded page-question extraction, a ticketed MCP App host and Control UI bridge, and manifest-declared MCP Apps for native plugins. (#109817, #111457, #113861, #109861; related #109851; #109807, #113224; related #113218) Thanks @anagnorisis2peripeteia, @FMLS, @cursoragent, @hxy91819, and @fuller-stack-dev.
- **Memory:** add fast active-memory recall, default cross-conversation recall for personal installs, guided imports from Claude Code/Codex/Hermes, and a dedicated Memory settings page. (#108043, #110597, #108977, #114037)
- **Scheduling:** add per-job dynamic cadence, gated script payloads, durable schedule-source streaming, cron-backed heartbeat monitors, heartbeat-task conversion, current-conversation defaults, and `/loop`. (#110978, #111112, #112387, #112585, #113165, #114328)
- **Fish Audio speech:** add hosted S2.1 synthesis with streaming, voice notes, voice discovery, and telephony, plus local Fish S2 Pro reference-voice streaming in native macOS Talk. (#115790) Thanks @Rheingold777, @ImLukeF, and @Conan-Scott.
- **Control UI setup:** continue verified model setup into Custodian, explain that the web app is ready without a channel, and offer an optional dismissible path to Channels. (#116078, #116079) Thanks @vincentkoc.
- **Buzz messaging:** preserve Markdown and structured room content, then add room- and thread-scoped typing indicators with reconnect-safe lifecycle handling. (#116096, #116194) Thanks @shakkernerd.
- **Automations naming:** rename the scheduler-facing `cron` agent tool and visible CLI/UI surfaces to Automations while retaining the compatible CLI alias. (#114841, #114854, #114853) Thanks @omarshahine.
- **DuckDuckGo search:** move DuckDuckGo search into the plugin boundary so provider ownership, installation, and runtime behavior stay outside core. (#116740) Thanks @vincentkoc.

### Fixes

- **Security and authorization:** prevent channel allowlists from granting owner access, keep session exports inside the workspace, close a forged-marker/web-search boundary bypass, prevent non-owner ACP session exposure, reject unsafe explicit approval IDs, harden secret redaction and exec/OAuth approvals, validate downloaded install scripts, and prevent insecure secrets-plan writes. (#107403; related #104984; #104708; related #102391; #110417, #110745; related #103055; #111055, #112947, #112952, #112953, #112956, #112946, #112957, #113307; related #90013; #113707) Thanks @obviyus, @yetval, @VACInc, @pgondhi987, and @SebTardif.
- **SQLite and data safety:** commit session indexes before transcript eviction, preserve state through maintenance races and live-WAL verification, reject invalid backups and schema data loss, make snapshot publication crash-recoverable, retain complete backups after interrupted commits, and evict only the exact corrupted cached database owner so repairs recover without a Gateway restart. (#108378, #113216; related #113209, #113210, #113211; #113287; related #113265; #113367, #113473, #113607, #114016, #114278) Thanks @yetval, @vincentkoc, @VACInc, and @rizquuula.
- **Channel delivery:** stop Telegram durable-ingress loss across restarts and persist offsets only after spool writes, preserve Discord/iMessage/WhatsApp traffic across crashes or restarts, restore assistant context and interrupted turns after restart, suppress outbound echoes, deliver ingress retries whose queued run was dropped, report finalized Telegram previews to plugins, explain invalid native queue arguments instead of false model-failure fallbacks, validate native settings, and preserve Telegram ingress outcomes. (#107288; related #107246; #113368; related #113315; #110274, #110409, #110418, #112548; related #112520; #112562, #114058, #114531, #111341, #115891; related #115888; #116214; related #116171; #116726; related #116688; #116773) Thanks @obviyus, @carlosjarenom, @JesusSerrano-Seimako, @vincentkoc, @edenfunf, @joshavant, and @hannesrudolph.
- **Sessions and transcripts:** preserve final replies, active turns, Codex-bound history, and transcript cursors; prevent repeated tool-call IDs from poisoning sessions; close lifecycle races and cross-agent deadlocks; keep migrated transcripts usable after restart; keep restart prompts on the active transcript tail; and preserve TUI session state across switches and reconnects. (#107799; related #106594; #110389, #110518; related #109443; #112016, #112988, #114477; related #103077, #103089, #113005, #114187; #114524, #114504, #116077, #116399, #117260) Thanks @joshavant, @lockhartheavyindustries, @flashosophy, @yetval, @realaudreyserber-afk, @hvhoon, and @vincentkoc.
- **Install and upgrade:** preserve working installs on unsupported Node and npm 12, isolate source postinstall state, repair missing native adapters, keep versioned plugins off source paths, avoid dirty source builds, repair plugin config during upgrades, stabilize package-to-dev switches, restore production installs after the TypeBox package removal, ship documented plugin SDK typings, and discover external web-search plugins on fresh installs. (#106994; related #106870; #108100; related #107290; #111514; related #111513; #111682, #112829; related #112827; #113094, #113324, #113856, #113821, #114090, #114215; related #113975; #114327, #115292, #116333, #116345) Thanks @woohahahaaa, @fuller-stack-dev, @vincentkoc, @sallyom, @alxfyvwebaccts-png, and @pash-openai.
- **Provider reliability:** prevent false Codex exhaustion and silent replies, honor Anthropic Retry-After, preserve selected Claude CLI profiles and adopted chats, remove the rejected Codex OAuth realtime fallback, recover stalled Claude CLI sessions without losing native cache continuity, reuse plugin metadata during model selection, bound stalled provider response bodies, and stabilize Ollama/LM Studio/local-model discovery. (#110381; related #96815; #110980, #111072; related #103849; #112458; related #95612, #107668; #113078, #113393, #114397, #114094; related #114086; #114288, #114405, #114582, #115211; related #115021; #113866, #114117, #109088) Thanks @xxw77, @yetval, @fuller-stack-dev, @cstreeter, @josh-cornelius, @lanyoung, @LeonidasLux, @BomBastikDE, @vincentkoc, @VACInc, and @SunnyShu0925.
- **Agent and Codex runtime:** bound malformed Code Mode repair to one correction turn, preserve valid native Codex controls, keep promoted approvals from blocking unattended runs, and retain the original requester when an approval is promoted. (#115729; related #115311; #107588, #116117, #116152) Thanks @vincentkoc and @VACInc.
- **Cron reliability:** restore one-shot and startup catch-up jobs, preserve script state and scheduled authority across restarts, accept benign same-generation updates, bind jobs to the durable store session, unblock completed jobs behind slower batches, and trim job IDs before exact lookup. (#107236, #110351; related #102236; #111292; related #111271, #111272, #111273, #111274; #112483, #113088; related #113085; #114421, #114441, #110849) Thanks @SL4N, @yetval, @joshavant, @metahacker, @efpiva, @nocodet888-arch, and @vincentkoc.
- **Compaction and response delivery:** account for CJK text in compaction estimates and treat `no_compactable_entries` as a benign skip. (#114386; related #103930; #114449; related #114385) Thanks @qingminglong, @revision-co-ltd, @loulanyue, and @alfredjbclaw.
- **Platform and transport reliability:** respect debug-proxy response backpressure, cancel early-woken meeting audio timers, preserve Windows PATH delimiters in node status, and prevent duplicate user/system systemd Gateway ownership with actionable recovery guidance. (#114076; related #105701; #114526, #114505, #116162; related #116129) Thanks @qingminglong, @aniruddhaadak80, @IWhatsskill, @vincentkoc, and @obviyus.
- **Channel edge cases:** settle Feishu outbound delivery, surface Signal recipient failures, and support reverse-proxy paths in Matrix homeserver URLs. (#113152, #111960; related #111959; #93516; related #102885) Thanks @joshavant, @ooiuuii, and @Papilionidae.

### Complete contribution record

The full contribution record is available in the tag-pinned [CHANGELOG.md](https://github.com/openclaw/openclaw/blob/v2026.7.2-beta.7/CHANGELOG.md#complete-contribution-record).

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.7.2-beta.7
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.7.2-beta.7.tgz
- integrity: `sha512-raD4Z96RcZ5XY0cdtqsRRQVhPv8JOHgA4vK/0D2/BsF9czI3d5w9O1xhYGKGsNKXp+3A0HipL6oeV0zKRK/lAA==`
- release SHA: `dabe1915362e20c25704af91612a32a8f4c96e83`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.7.2-beta.7/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/30738213764
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/30714148718
- full release validation: https://github.com/openclaw/openclaw/actions/runs/30714067986
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/30738340512
- plugin ClawHub publish: no normal OIDC candidates
- plugin ClawHub bootstrap: dispatched separately, not awaited by this proof: https://github.com/openclaw/openclaw/actions/runs/30738341581
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- #117061 [enhancement, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:needs-live-repro, impact:message-loss, impact:auth-provider, issue-rating: 🐚 platinum hermit] [Feature]: A broken non-core model provider can suppress all gateway channels at startup — https://github.com/openclaw/openclaw/issues/117061
- #72504 [no-stale, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] Feishu: bot strips its own <at> mention causing NO_REPLY in multi-bot groups — https://github.com/openclaw/openclaw/issues/72504

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #117912 draft=False chore(agents): consolidate agent test clusters — https://github.com/openclaw/openclaw/pull/117912
- PR #117911 draft=False fix(exec): explain Linux OOM-score-adjusted SIGKILLs — https://github.com/openclaw/openclaw/pull/117911
- PR #104240 draft=False fix(line): record every LINE push message id in send receipts — https://github.com/openclaw/openclaw/pull/104240
- PR #117676 draft=False fix(memory-core): pass allowTranscriptTurnSnippet at all isContaminatedDreamingSnippet call sites — https://github.com/openclaw/openclaw/pull/117676
- PR #111539 draft=False fix(ui): increasing webchat lags per keystroke on slash commands and input-history recall in long sessions — https://github.com/openclaw/openclaw/pull/111539
- PR #117788 draft=False fix(imessage): rewind the recovery cursor when chat.db is replaced at the same path — https://github.com/openclaw/openclaw/pull/117788
- PR #117915 draft=False feat(browser): relay CDP compat for Puppeteer clients (chrome-devtools-mcp) — https://github.com/openclaw/openclaw/pull/117915
- PR #117906 draft=False fix(feishu): preserve self mentions in agent-facing group messages — https://github.com/openclaw/openclaw/pull/117906
- PR #115277 draft=False fix(agents): materialize MCP for server-name toolsAllow globs — https://github.com/openclaw/openclaw/pull/115277
- PR #117914 draft=False feat(agents): add visible-reply loop detection library — https://github.com/openclaw/openclaw/pull/117914
- PR #117909 draft=False fix(ui): preserve advanced cron delivery settings when cloning — https://github.com/openclaw/openclaw/pull/117909
- PR #117908 draft=True feat(memory-core): add durable dreaming cycle controller — https://github.com/openclaw/openclaw/pull/117908
- PR #117913 draft=False fix(doctor): stop stale builds before repair guidance — https://github.com/openclaw/openclaw/pull/117913
- PR #117893 draft=False fix(cli): reject incomplete hosted video downloads — https://github.com/openclaw/openclaw/pull/117893
- PR #117727 draft=False fix: prevent fractional chunk limits from stalling text splitting — https://github.com/openclaw/openclaw/pull/117727
- PR #117454 draft=False fix(browser): gateway crashes after abandoned download wait — https://github.com/openclaw/openclaw/pull/117454
- PR #95885 draft=False Prevent repeated byte-triggered compactions — https://github.com/openclaw/openclaw/pull/95885
- PR #117846 draft=False fix(auth): preserve cooldown fallback state — https://github.com/openclaw/openclaw/pull/117846
- PR #95676 draft=False fix(agents): retry same profile before timeout auth rotation — https://github.com/openclaw/openclaw/pull/95676
- PR #117910 draft=False refactor(whatsapp): split inbox lifecycle coverage — https://github.com/openclaw/openclaw/pull/117910
- PR #117681 draft=False fix(ui): pass qualified skill ref to ClawHub install/read endpoints — https://github.com/openclaw/openclaw/pull/117681
- PR #89287 draft=False fix(agents): verify completion delivery target — https://github.com/openclaw/openclaw/pull/89287
- PR #117896 draft=False fix(voice): bound Google Live tool ownership — https://github.com/openclaw/openclaw/pull/117896
- PR #117184 draft=False feat(auto-reply): clean empty staged inbound media directories (#104358) — https://github.com/openclaw/openclaw/pull/117184
- PR #117443 draft=False fix(status): resolve effective channel model override — https://github.com/openclaw/openclaw/pull/117443
- PR #117744 draft=False fix(model-catalog): decode hosted model catalog bundles with fatal UTF-8 validation — https://github.com/openclaw/openclaw/pull/117744
- PR #117904 draft=False fix(macos): gate remote onboarding on gateway auth — https://github.com/openclaw/openclaw/pull/117904
- PR #117400 draft=False fix(compaction): use canonical session context projection for post-turn estimator — https://github.com/openclaw/openclaw/pull/117400
- PR #117509 draft=False fix(agents): surface sessions_yield waiting status — https://github.com/openclaw/openclaw/pull/117509
- PR #117721 draft=False fix(control-ui): render live thinking agent events in WebChat — https://github.com/openclaw/openclaw/pull/117721
