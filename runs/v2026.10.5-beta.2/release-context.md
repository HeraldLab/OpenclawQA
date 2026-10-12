# Release Context — OpenClaw `v2026.10.5-beta.2`

Fetched at: `2026-10-12T12:30:42Z`

## Target

- Target tag: `v2026.10.5-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.5-beta.2
- Target tag SHA: 467e83dea27c0d9ade8e999d688de2ed656b2225

## Freshness baselines

- Latest beta tag: `v2026.10.5-beta.2`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.10.2`
- Prior prerelease baseline: `v2026.10.5-beta.1`

## Release notes excerpt

## 2026.10.5-beta.2

### Highlights

- **Updates finish and recover:** `openclaw update` settles stale handoff leases, completed receipts, and legacy 2026.9.8 recovery records instead of stopping on `update-recovery-pending`, keeps the service heap limit and webhook listeners, handles Windows short-name paths, and no longer reports accepted handoffs or successful updates as failures. (#169038, #169027, #168388, #168889, #169035, #169292, #168927, #168993, #169037, #169454, #168905) Thanks @mkdelta221, @waynegault, @chedong, @k94118, @bluet, @sirius1024, @RomneyDa, @sayitfast, and @hannesrudolph.
- **Doctor keeps your plugins and data:** Doctor preserves installed plugins' configuration when path safety checks block them, leaves malformed UTF-8 root memory files untouched, and recovery copies capture Canvas and Memory Core files before migrations move them, including on installs with no configured agents. (#168111, #169029, #169436, #169516) Thanks @obviyus, @wangmiao0668000666, and @RomneyDa.
- **Approved tool calls stay as approved:** hooks can no longer change tool arguments after a trusted inline approval; plugins that transform arguments must request approval for their final arguments. (#142700) Thanks @giodl73-repo and @giodl73.
- **Subagent message provenance:** inter-session messages keep their `[Inter-session message]` safety envelope from the first request and through replay, so parent-sent instructions are never presented to a child as direct user instructions. (#169130, #169238) Thanks @RomneyDa.
- **Control UI turns keep running:** chat turns from paired devices survive ordinary pairing activity such as node heartbeats, other devices' updates, and tab reconnects; real revocations still stop them. (#169457, #169134) Thanks @Oldrich333.

### Changes

- **Tool approval hooks:** ordinary hooks can no longer rewrite trusted-inline-approved tool arguments without another approval, and transforming plugins must request separate approval for their final arguments or the call is blocked; see `docs/plugins/hooks/tool-policy.md` for migration. (#142700) Thanks @giodl73-repo and @giodl73.
- **Codex runtime compatibility:** plugin admission rejects official Codex runtimes below 2026.9.7 with update and repair guidance, and incompatible plugins stay inspectable without being imported. (#168930, #168748, #168749, #168977) Thanks @ezimerman.
- **Session notices:** creating many sessions gives the main session one summary of new sessions instead of separate notices that crowd out reminders and wakes. (#168239)
- **Update performance:** updates stop rehashing unchanged runtime files while retaining the running updater and publishing the candidate, reducing update I/O. (#168958)

### Fixes

- **Tool Search provenance:** network results reached through Tool Search and Code Mode now taint the turn the same way direct network tool calls do. (#169560, #169332) Thanks @RomneyDa and @farisoftfry.
- **Subagent provenance:** child sessions keep the inter-session safety envelope on every replayed turn, and inter-session turns keep a stable provider prompt prefix across later turns and Gateway restarts. (#169130, #169238) Thanks @RomneyDa.
- **Node commands and approvals:** approved node commands replay when their prepared plan omitted session identity, Windows node shell commands keep quoted arguments, safe-bin commands accept trailing whitespace, and the Linux node service keeps its PATH when the login shell resets it. (#161980, #151622, #158160, #142847, #168120, #136677, #134354) Thanks @Program-123, @gaojian125, @Dimitri-lcht, @igs-rogenlo, @yetval, @harjothkhara, and @abacha.
- **Private reasoning:** unfinished model reasoning stays private when a reply hits a token limit or content filter after a tool call. (#168294)
- **Doctor data safety:** Doctor keeps blocked plugins' authored entries, enablement, policy, and slots; refuses to merge malformed UTF-8 root memory; captures Canvas and Memory Core files in new recovery copies (and works on installs with no configured agents); skips redundant cron backups for unchanged one-shot jobs; and honors Windows permissions for SQLite recovery snapshots. (#168111, #168066, #169029, #168567, #169436, #169516, #168938, #168838, #169397) Thanks @obviyus, @wangmiao0668000666, @RomneyDa, @harshitgupta31415, and @WG-Mojo.
- **Memory:** daily-note flushes reject copied saved content instead of repeating blocks, and correcting an embedding provider's endpoint or credential refreshes cached index managers without a Gateway restart. (#168123, #151263, #151055) Thanks @ruel225 and @Mirksen.
- **Restart recovery:** main sessions that were mid-turn during a Gateway restart resume on the next boot, interrupted completion replies are delivered instead of lost, and new replies wait for their agent to finish starting instead of failing with `prepared reply dispatch runtime owner was not published`. (#168651, #167814, #167766, #168826, #157814) Thanks @goutamadwant, @marknilsn, and @xiaozishan.
- **Reply routing:** WebChat task completions stay in WebChat, mirrored external sends no longer change a transcript's reply destination, and Reef carries GitHub commit links without flagging their revision IDs as credentials. (#168248)
- **Prompt caching:** conversations whose first message ends in whitespace keep a byte-stable prompt prefix, and OpenAI-compatible and local endpoints keep runtime context in a user-role message. (#168725, #168546, #164791) Thanks @flanker-stack.
- **Compaction:** sessions skip a redundant host compaction after native-only compaction, safeguard compaction keeps configured AGENTS.md sections, and memory-flush runs keep provider-native compaction off. (#168051, #168015, #168446, #168131, #168164) Thanks @ruel225, @xydigitLybnnnn, @robertoronderosjr, @jakeaadams, and @obviyus.
- **Control UI:** chat turns survive unrelated pairing activity, typed `/stop` also cancels queued turns for the session, and open chats recover after a Gateway update or recovery reload instead of sticking on **Server updated → Retry now**, keeping their place. (#169457, #169134, #167860, #167859, #168941, #169194) Thanks @Oldrich333 and @masatohoshino.
- **Telegram:** polling connects again when the ingress worker runs from a source checkout or packaged plugin build, and tables next to quotes or lists keep their boundaries and values. (#154286, #154180, #168383, #168366) Thanks @xydt-juyaohui, @markfietje, @dhruv1220, and @barry-ssb.
- **Channels and voice:** channels start again after a stopped-Tailscale failure, the Matrix probe stops its client after checking identity, and `openclaw voicecall steer` keeps stdout machine-readable JSON. (#162266, #168587) Thanks @RomneyDa.
- **Agent turns:** scheduled and ordinary turns reach the configured fallback after a provider timeout, queued follow-ups that switch model clear the auto-fallback probe, cancelled queued CLI work never runs, empty stream heartbeats no longer count as model progress, malformed tool calls whose argument length is 401 or 403 are not reported as auth failures, valid tool argument union values keep their type, and plugin completions keep working after another plugin reloads. (#168605, #160440, #160428, #169303, #145850, #168500, #168450, #158974, #168916, #156026) Thanks @hxy91819, @changeroa, @RileyJJY, @TYY-2005, @r3n3x, @Shenrui-Ma, and @jalehman.
- **Claude CLI:** Claude CLI models stay listed after another plugin's config changes, exec-completion turns keep their native and MCP tools, and saved session MCP server selections apply on the next turn. (#168315, #168670, #168342, #168393, #168207) Thanks @obviyus, @Oldrich333, and @dprev.
- **OpenRouter prompt caching:** cache-TTL context pruning now arms for Grok and Gemini 2.5+ models on OpenRouter. (#169548, #169133) Thanks @RomneyDa and @gregb100.
- **Models and providers:** API-key sign-in discovers the provider's models immediately, shared OAuth credentials refresh with historical agent stores, switching back to an OpenAI model works without the Codex plugin, timed-out Codex discovery clients are reaped, LM Studio waits for slow model loads instead of overflowing a fresh session, and credential removal during a model reload no longer leaves a restart warning. (#168617, #168957, #169412, #168365, #168044) Thanks @obviyus.
- **Model catalog memory:** a long-running Gateway's model-catalog worker evaluates an unchanged installed native ESM plugin once per workspace instead of retaining another copy of its module graph on every config change, and a failed native refresh re-registers the requested config on the next request. (#169272, #169321, #159662) Thanks @obviyus, @mcooks-cmd, @RomneyDa, and @svdinu-jpg.
- **MCP computer control:** computer control is released with its run, so later calls no longer fail with `COMPUTER_HOST_BUSY`. (#151127, #147420) Thanks @ylcn91 and @vovarbv.
- **Automations:** cron target and payload validation errors are reported as invalid requests, and Workboard fallback runs stay active until the overall outcome settles. (#169102, #168215, #167574) Thanks @obviyus, @skyzhao1223, and @asikorskiy.
- **Agents API sessions:** saved remote sessions continue with the same session ID across binding upgrades. (#168150)
- **Large Gateways:** large fleets reserve session stores without stack overflows, and process-owning Gateway stops no longer wait on native skills watcher cleanup. (#168354, #168160, #168273) Thanks @609NFT and @obviyus.
- **Updates and recovery:** managed updates settle eligible stale package recovery after a lost or replaced handoff lease database and archive completed receipts before the next preparation; `--dry-run` only reports the planned settlement. (#169038, #167506, #167771) Thanks @mkdelta221 and @waynegault.
- **Legacy update records:** 2026.9.8 package recovery records settle by identity and version after metadata drift, completed-receipt identity drift no longer blocks updates, and public repair exits nonzero with guidance when a journal stays pending. (#169027, #168856, #168388, #168092) Thanks @chedong, @k94118, and @RomneyDa.
- **Update outcomes:** accepted Gateway update handoffs are not reported as failures, recorded successes stay successful with a warning about stopped channels, original failures survive unavailable cleanup reporting, repaired migrations stop producing stale warnings, package verification tolerates clock jumps, and migrated-state failures point to `openclaw update repair`. (#168993, #168870, #169037, #169454, #169004, #168835, #168905) Thanks @sayitfast, @hannesrudolph, and @WG-Mojo.
- **Update memory and webhooks:** update children inherit the managed service's heap limits so Doctor finishes on large agent databases, and official webhook plugins deferred during candidate Doctor keep their listeners, including Teams' historical port 3978. (#168889, #168729, #169035, #168872) Thanks @bluet and @sirius1024.
- **Update runtimes:** updater workers stay on the retained runtime and `openclaw doctor --fix` reclaims retained runtimes when the install path uses a Windows short (8.3) name or different casing, and updates no longer copy unrelated dependencies into the retained runtime. (#169292, #168927) Thanks @RomneyDa.
- **Update diagnostics:** an unsealed original-state capture warning names the affected database, and a candidate config read failure warning includes its reason. (#169282, #169259, #169284, #169261) Thanks @DonnieFi.
- **Codex Ultrafast:** ChatGPT sign-in sessions keep Ultrafast on resumed turns instead of dropping to Fast after the first turn. (#169265, #169264) Thanks @SanderHelgesen.
- **npm-global updates:** the updater runtime keeps only OpenClaw's own dependencies instead of every unrelated package in the global `node_modules`. (#169551, #169373) Thanks @RomneyDa and @holgergruenhagen.
- **Update exit handling:** a completed update whose result reporting fails exits with its warning instead of opening interactive failure triage. (#168587)
- **Doctor maintenance:** Doctor and update repair enter maintenance on a running systemd Gateway even when checking a large state database is slow. (#168161, #168031) Thanks @obviyus and @Tosko4.

### Complete contribution record

This audited record covers the complete v2026.10.5-beta.1..8ed6123845921594f4643c1914e8ceb8cfb42c07 history: 91 in-range PRs + 0 retained seed-only PRs = 91 unique PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

Shipped baseline exclusions: v2026.10.5-beta.1 (3 PRs: #134837, #144420, #167460).

#### Pull requests

- **PR #169281** Thanks @RomneyDa.
- **PR #169292** Thanks @RomneyDa.
- **PR #169268** Thanks @RomneyDa.
- **PR #168103**
- **PR #168161** Related #168031. Thanks @obviyus and @Tosko4.
- **PR #168388** Related #168092. Thanks @k94118.
- **PR #168605**
- **PR #168826** Related #157814. Thanks @xiaozishan.
- **PR #168889** Related #168729. Thanks @bluet.
- **PR #168958**
- **PR #169035** Related #168872. Thanks @sirius1024.
- **PR #154286** Related #154180. Thanks @xydt-juyaohui and @markfietje.
- **PR #169027** Related #168856. Thanks @chedong.
- **PR #169038** Related #167506, #167771. Thanks @mkdelta221 and @waynegault.
- **PR #169084** Thanks @RomneyDa.
- **PR #168941**
- **PR #169272** Thanks @obviyus and @mcooks-cmd.
- **PR #169257** Thanks @RomneyDa.
- **PR #169321** Thanks @RomneyDa.
- **PR #169436** Thanks @RomneyDa.
- **PR #169457** Related #169134. Thanks @Oldrich333.
- **PR #168150**
- **PR #168097** Thanks @RomneyDa.
- **PR #168111** Related #168066. Thanks @obviyus.
- **PR #168128**
- **PR #168123**
- **PR #168264** Thanks @obviyus.
- **PR #168248**
- **PR #168239**
- **PR #168215** Related #167574. Thanks @obviyus and @skyzhao1223 and @asikorskiy.
- **PR #167814** Related #167766. Thanks @goutamadwant and @marknilsn.
- **PR #168273** Thanks @obviyus.
- **PR #151263** Related #151055. Thanks @ruel225 and @Mirksen.
- **PR #168294**
- **PR #168354** Related #168160. Thanks @609NFT.
- **PR #168315** Thanks @obviyus.
- **PR #168365**
- **PR #167860** Related #167859. Thanks @masatohoshino.
- **PR #168051** Related #168015. Thanks @ruel225 and @xydigitLybnnnn and @robertoronderosjr.
- **PR #168330** Thanks @RomneyDa.
- **PR #168546** Related #164791. Thanks @flanker-stack.
- **PR #168500** Related #168450. Thanks @TYY-2005 and @r3n3x.
- **PR #158974** Thanks @Shenrui-Ma.
- **PR #168617** Thanks @obviyus.
- **PR #168383** Related #168366. Thanks @dhruv1220 and @barry-ssb.
- **PR #168120** Thanks @yetval.
- **PR #168670** Related #168342. Thanks @Oldrich333.
- **PR #168725**
- **PR #151127** Related #147420. Thanks @ylcn91 and @vovarbv.
- **PR #142700** Thanks @giodl73-repo and @giodl73.
- **PR #158160** Related #142847. Thanks @Dimitri-lcht and @igs-rogenlo.
- **PR #168927**
- **PR #161980** Related #151622. Thanks @Program-123 and @gaojian125.
- **PR #168930** Related #168748, #168749. Thanks @ezimerman.
- **PR #168938** Related #168838. Thanks @harshitgupta31415 and @WG-Mojo.
- **PR #168957** Thanks @obviyus.
- **PR #168993** Related #168870. Thanks @sayitfast.
- **PR #169004** Related #168835. Thanks @WG-Mojo.
- **PR #169029** Related #168567. Thanks @wangmiao0668000666.
- **PR #169037**
- **PR #136677** Related #134354. Thanks @harjothkhara and @abacha.
- **PR #168916** Related #156026. Thanks @jalehman.
- **PR #168977**
- **PR #169130** Thanks @RomneyDa.
- **PR #169194**
- **PR #169225** Thanks @RomneyDa.
- **PR #169238** Thanks @RomneyDa.
- **PR #145850** Thanks @RileyJJY.
- **PR #169303** Thanks @changeroa.
- **PR #169397**
- **PR #169412** Thanks @obviyus.
- **PR #169454** Thanks @hannesrudolph.
- **PR #169516** Thanks @RomneyDa.
- **PR #169479** Thanks @RomneyDa.
- **PR #168651**
- **PR #168044**
- **PR #168446** Related #168131. Thanks @jakeaadams.
- **PR #168164** Thanks @obviyus.
- **PR #168393** Related #168207. Thanks @dprev.
- **PR #160440** Related #160428. Thanks @hxy91819.
- **PR #169102**
- **PR #169430**
- **PR #162266** Thanks @RomneyDa.
- **PR #168905**
- **PR #168587**
- **PR #169265** Related #169264. Thanks @SanderHelgesen.
- **PR #169282** Related #169259. Thanks @DonnieFi.
- **PR #169284** Related #169261. Thanks @DonnieFi.
- **PR #169548** Related #169133. Thanks @RomneyDa and @gregb100.
- **PR #169551** Related #169373. Thanks @RomneyDa and @holgergruenhagen.
- **PR #169560** Related #169332. Thanks @RomneyDa and @farisoftfry.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.10.5-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.10.5-beta.2.tgz
- integrity: `sha512-9OgCXW1ZUmMdBdtojEIp7P9qRh9hTHhTARNQfTLPTtKQViuNenvcjgJh6JaJsZx9b20J0FL4qXA4q1dkw795eg==`
- release SHA: `467e83dea27c0d9ade8e999d688de2ed656b2225`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.10.5-beta.2/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/38244441645
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/38227708658
- full release validation: https://github.com/openclaw/openclaw/actions/runs/38226906077
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/38245185150
- plugin ClawHub publish: no normal OIDC candidates
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/38241099968/attempts/1
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- #169882 [no-stale, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:ux-friction] [Bug]: macOS app node system.run uses launchd's bare PATH when OpenClaw.app is opened from Finder/Dock — https://github.com/openclaw/openclaw/issues/169882
- #169883 [bug, regression] [Bug]: Control UI: invalid chat.send params: unexpected property '__controlUiReconnectResume' after WebSocket reconnect — https://github.com/openclaw/openclaw/issues/169883

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #156484 draft=False feat(qa): compare recorded Decision answers offline — https://github.com/openclaw/openclaw/pull/156484
- PR #169714 draft=False refactor(runtime): prepare config, auth, and session facts asynchronously — https://github.com/openclaw/openclaw/pull/169714
- PR #89826 draft=False feat(chat): UX-012 — token usage progress meter — https://github.com/openclaw/openclaw/pull/89826
- PR #169757 draft=False perf(sessions): move target lookups and callers to workers — https://github.com/openclaw/openclaw/pull/169757
- PR #125286 draft=False fix(install): keep Windows Git installs on the validated Node runtime — https://github.com/openclaw/openclaw/pull/125286
- PR #167585 draft=False fix: tools.effective drops tool-only plugin tools when the inventory lease scopes its runtime generation — https://github.com/openclaw/openclaw/pull/167585
- PR #168852 draft=False refactor: migrate sidebar rendering to Solid 2 — https://github.com/openclaw/openclaw/pull/168852
- PR #169696 draft=False refactor(ui): own shared control theme tokens — https://github.com/openclaw/openclaw/pull/169696
- PR #169884 draft=False fix(macos): prevent discovery startup from crashing on transient bundles — https://github.com/openclaw/openclaw/pull/169884
- PR #169485 draft=False fix(windows): rely on fs-safe 0.26.2 for long private paths — https://github.com/openclaw/openclaw/pull/169485
- PR #169622 draft=False refactor: move bundled session reads and authority into workers — https://github.com/openclaw/openclaw/pull/169622
- PR #163435 draft=True feat(snowflake): add Cortex local application OAuth — https://github.com/openclaw/openclaw/pull/163435
- PR #169867 draft=False fix(gateway): Control UI rejects /workspace file links written by sandboxed agents — https://github.com/openclaw/openclaw/pull/169867
- PR #169363 draft=False refactor(sessions): activate memory-only incognito actors — https://github.com/openclaw/openclaw/pull/169363
- PR #163423 draft=False fix: final reply survives equivalent channel registry reload — https://github.com/openclaw/openclaw/pull/163423
- PR #169063 draft=False perf(agents): remove automatic tool payload secret masking — https://github.com/openclaw/openclaw/pull/169063
- PR #169858 draft=False fix(sessions): preserve facts across unrelated writes — https://github.com/openclaw/openclaw/pull/169858
- PR #101441 draft=False fix(zalouser): sanitize outbound tool traces — https://github.com/openclaw/openclaw/pull/101441
- PR #169857 draft=False fix(agents): replies waiting on operator approval are reclaimed as stalled — https://github.com/openclaw/openclaw/pull/169857
- PR #158067 draft=False fix: deliver background results to WebChat-only sessions — https://github.com/openclaw/openclaw/pull/158067
- PR #169874 draft=False refactor(ui): consolidate shared presentation — https://github.com/openclaw/openclaw/pull/169874
- PR #168612 draft=False refactor(ui): render the app shell and retained routes with Solid — https://github.com/openclaw/openclaw/pull/168612
- PR #124867 draft=False fix(ui): remove archived sessions from sidebar immediately — https://github.com/openclaw/openclaw/pull/124867
- PR #169843 draft=False fix: chat turns fail when session receipts exceed transport limits — https://github.com/openclaw/openclaw/pull/169843
- PR #169128 draft=False feat(ui): use native Solid overlays and tabs — https://github.com/openclaw/openclaw/pull/169128
- PR #169782 draft=False fix: Codex byte-triggered compaction ignores the configured summary model — https://github.com/openclaw/openclaw/pull/169782
- PR #124642 draft=False feat(feishu): add organization event bridge — https://github.com/openclaw/openclaw/pull/124642
- PR #169864 draft=False feat(feishu): show queued and confirmed processing feedback — https://github.com/openclaw/openclaw/pull/169864
- PR #169854 draft=False fix: avoid repeated database validation during memory indexing — https://github.com/openclaw/openclaw/pull/169854
- PR #169763 draft=False fix(state): complete async SDK auth and plugin discovery cutovers — https://github.com/openclaw/openclaw/pull/169763
