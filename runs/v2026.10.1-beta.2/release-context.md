# Release Context — OpenClaw `v2026.10.1-beta.2`

Fetched at: `2026-10-08T01:00:31Z`

## Target

- Target tag: `v2026.10.1-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.1-beta.2
- Target tag SHA: c58cf3afa0793257a8127ae868d5e159da6d9d0a

## Freshness baselines

- Latest beta tag: `v2026.10.1-beta.2`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.9.8`
- Prior prerelease baseline: `v2026.10.1-beta.1`

## Release notes excerpt

## 2026.10.1

### Highlights

- **Sessions and memory:** preserved usage across registry changes, delivered worker attachments from remote workspaces, prevented queued cancellations and transcript aliases from stalling active turns, kept continuation signatures aligned, and migrated embedding caches in bounded batches with oversized-row reporting. (#164217, #164219, #163708, #164230, #164251, #164289, #164287, #164303) Thanks @vincentkoc.
- **Replies and media:** restored inline playback for local videos, replaced rejected media links with useful errors, kept Telegram progress updates free of preview cards, and fixed speech-only replies when reasoning is enabled. (#164137, #163727, #164285, #164256) Thanks @ivan-magda, @obviyus, and @Twilight-Networks.
- **Updates and Doctor:** improved serving-verdict recovery guidance, kept repairs working with read-only managed config, removed repeated config, backup, metadata, and pnpm-root probes, reported successful cleanup as progress without corrupting JSON output, and treated a still-starting Gateway as a warning. (#164193, #161924, #164235, #162259, #164182, #164186, #164183, #164184, #163477, #164261, #162236, #164312) Thanks @DonnieFi, @JD8855122, @Patrick-Erichsen, and @waynegault.
- **Windows workspaces and browser startup:** fixed empty and nested Windows worktree creation, improved Linux Chromium discovery, and automatically started Playwright Chromium on ARM64. (#164202, #164249, #163510, #163281) Thanks @ly85206559, @jesse-merhi, and @obviyus.
- **Cloud workers and Crabbox:** surfaced the real cloud-worker failure, enforced Linux leases, overlapped worker-bundle downloads with bootstrap, removed unrelated warm-image cleanup waits, and prevented slow reads or unsupported backends from stranding workers. (#164129, #164187, #164128, #164231)
- **Plugins, Codex, and MCP:** preserved Bun package-import capture, reduced prerelease metadata requests, kept expired remote-exec approvals from poisoning auth profiles, restored node policy hooks, synchronized MCP forms/files/context, and routed background skill reviews through Workshop proposals. (#164223, #164185, #164237, #164270, #164277, #164292)

### Changes

- Added inactive-foundation support for incognito actor memory and Codex history routing. (#164224)
- Migrated existing agents to local Claws. (#162329) Thanks @Patrick-Erichsen.
- Reduced Sessions-board and state-path overhead by serving prepared facts, reusing card payloads per store revision, moving lifecycle mutations off the main thread, and retaining canonical state handles. (#164218, #164301, #163815, #164110)

### Fixes

- Preserved plugin lifecycle fences for cancelled queued turns and retained investigated failures in ready PR reviews. (#164247, #164253) Thanks @vincentkoc.
- Honored agent-local model aliases in status summaries. (#164126, #164115) Thanks @ooiuuii and @obviyus.
- Kept Gateway tests on the selected Bun runtime and ran native Codex subagent checks in Docker. (#164276, #164163)
- Left webhook config migrations to Doctor and avoided Nextcloud Talk webhook migration for unconfigured channels.

### Upcoming deprecations

- `channel-webhook-listener-config-inputs` began warning on 2026-09-26; migrate to `legacyWebhook` for canonical listener config. See `/gateway/doctor/config-migrations#channel-webhook-listeners`.
- `session-manager-sync-persistence` began warning on 2026-10-01; await the matching Async-suffixed SessionManager method and its rewrite commit. See `/plugins/sdk-migration/how-to-migrate#await-session-transcript-persistence`.
- `extension-session-sync-persistence` began warning on 2026-10-01; await the Async-suffixed ExtensionAPI and AgentSession persistence methods. See `/plugins/sdk-migration/how-to-migrate#await-extension-session-changes`.
- `provider-replay-sync-persistence` began warning on 2026-10-01; use the async replay sanitizer and session-state APIs. See `/plugins/sdk-migration/how-to-migrate#await-provider-replay-metadata`.
- `memory-session-sync-inventory` began warning on 2026-10-01; await `loadArchivedSessionsAsync` and `resolveMemorySessionTargetsAsync`. See `/plugins/sdk-migration/compatibility-policy#memory-session-inventory-readers`.
- `workspace-mutation-guard-callback` began warning on 2026-10-02; await database preparation and use SQL-free `guard.assertHost` for live authority. See `/plugins/sdk-migration/how-to-migrate#workspace-mutation-guards`.
- `gateway-placement-sync-results` began warning on 2026-10-02; await the Async-suffixed Gateway placement and publication readers. See `/plugins/sdk-migration/compatibility-policy#gateway-placement-and-publication-readers`.
- `watched-sessions-sync-harness-context` began warning on 2026-10-03; await `prepareWatchedSessionsHarnessContext` with a current-host capability assertion. See `/plugins/sdk-migration/compatibility-policy#watched-session-harness-context`.
- `plugin-sdk-media-understanding-public-demotion` reached its 2026-09-30 removal target; migrate to `api.registerMediaUnderstandingProvider(...)` and provider-owned request helpers. It remains removal-pending until the focused public-artifact read seam is complete. See `/plugins/architecture`.
- `plugin-sdk-memory-host-core-public-demotion` reached its 2026-09-30 removal target; use host-prepared memory prompts and injected memory capability registration. It remains removal-pending until the focused public-artifact read seam is complete. See `/plugins/architecture-internals#context-engine-plugins`.
- `plugin-sdk-channel-setup-input-fields` reached its 2026-10-01 removal target; use plugin-local setup input intersections. It remains removal-pending until a published-plugin artifact sweep finds no readers. See `/plugins/sdk-migration#published-channel-setup-compatibility`.
- `plugin-sdk-broad-runtime-barrels` reached its 2026-10-01 removal target; use focused plugin SDK subpaths. It remains removal-pending until bundled and published plugins stop importing the broad barrels. See `/plugins/sdk-migration#compatibility-policy`.
- `plugin-sdk-provider-owned-helper-shims` reached its 2026-10-01 removal target; use provider-local auth, model, replay, OAuth, and stream helpers. It remains removal-pending until official and published-plugin readers are gone. See `/plugins/sdk-migration#compatibility-policy`.
- `message-presentation-legacy-bridges` reached its 2026-10-01 removal target; use `MessagePresentation` values and channel renderers. It remains removal-pending until official producers and channels no longer use legacy interactive replies. See `/plugins/sdk-migration#compatibility-policy`.
- `plugin-sdk-focused-compat-aliases` reached its 2026-10-01 removal target; use each alias's focused replacement. It remains removal-pending until all enumerated aliases have no bundled or published readers. See `/plugins/sdk-migration#compatibility-policy`.
- `agent-harness-terminal-result-aliases` reached its 2026-10-01 removal target; use `AgentHarnessAttemptResult.terminal` and `AgentHarnessDeliveryDefaults.visibleReplies`. It remains removal-pending until legacy readers are gone. See `/plugins/sdk-agent-harness`.
- `official-plugin-export-aliases` reached its 2026-10-01 removal target; use `MessagePresentation` renderers and host-owned runtime behavior. It remains removal-pending until supported official plugins stop importing the aliases. See `/plugins/compatibility#current-compatibility-areas`.
- `memory-host-compatibility-aliases` reached its 2026-10-01 removal target; use canonical memory cache and FTS tables. It remains removal-pending until supported integrations and legacy data are verified. See `/plugins/sdk-migration#compatibility-policy`.
- `plugin-runtime-api-compat-aliases` reached its 2026-10-01 removal target; use the namespaced plugin API and focused runtime methods. It remains removal-pending until all flat API/runtime readers are gone. See `/plugins/sdk-migration#compatibility-policy`.
- `plugin-provider-manifest-compat-aliases` reached its 2026-10-01 removal target; use manifest-owned plugin metadata and model-catalog registration. It remains removal-pending until provider readers are gone. See `/plugins/sdk-migration#compatibility-policy`.
- `media-legacy-projection` reached its 2026-10-01 removal target; use ordered media facts, typed hook media, attachment templates, and `media-local-roots`. It remains removal-pending until a clean published-plugin sweep finds no readers. See `/plugins/sdk-migration#media-legacy-projection`.

### Complete contribution record

This audited record covers the complete 9da28ad4bd0ee3a9ba9757b9d6f444a6306ac3a0..8ea8bb11a5bd5c0fa66665861c10b49aaf8ed989 history: 283 in-range PRs + 0 retained seed-only PRs = 283 unique PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

Shipped baseline exclusions: v2026.9.8 (4 PRs: #108683, #137149, #145632, #146361).

#### Pull requests

- **PR #164194**
- **PR #164137**
- **PR #164198**
- **PR #164218**
- **PR #164110**
- **PR #164205** Thanks @vincentkoc.
- **PR #164129**
- **PR #163510** Thanks @ly85206559 and @obviyus.
- **PR #163281** Thanks @jesse-merhi and @obviyus.
- **PR #164225**
- **PR #164217**
- **PR #164202**
- **PR #163815**
- **PR #164193** Related #161924. Thanks @DonnieFi.
- **PR #164239**
- **PR #164230** Thanks @vincentkoc.
- **PR #164187**
- **PR #164235** Related #162259. Thanks @JD8855122.
- **PR #164204**
- **PR #164134**
- **PR #164238**
- **PR #164244**
- **PR #164182**
- **PR #164126** Related #164115. Thanks @ooiuuii and @obviyus.
- **PR #164186**
- **PR #164219** Related #163708.
- **PR #164237**
- **PR #164247** Thanks @vincentkoc.
- **PR #164245** Thanks @vincentkoc.
- **PR #164128**
- **PR #164242**
- **PR #164185**
- **PR #164183**
- **PR #164253**
- **PR #164184**
- **PR #164248**
- **PR #164159**
- **PR #163477** Thanks @Patrick-Erichsen.
- **PR #164240**
- **PR #164260**
- **PR #164153**
- **PR #164163**
- **PR #163727** Thanks @ivan-magda and @obviyus.
- **PR #163137**
- **PR #163112**
- **PR #162329** Thanks @Patrick-Erichsen.
- **PR #164223**
- **PR #164261** Related #162236. Thanks @waynegault.
- **PR #164251**
- **PR #164165**
- **PR #164270**
- **PR #163930**
- **PR #163812** Related #163810. Thanks @vincentkoc.
- **PR #164252**
- **PR #164268**
- **PR #164276**
- **PR #164231**
- **PR #164262**
- **PR #164277**
- **PR #164281**
- **PR #164289** Thanks @vincentkoc.
- **PR #164287**
- **PR #164221**
- **PR #164299**
- **PR #164271**
- **PR #164301**
- **PR #164302**
- **PR #164249**
- **PR #164243**
- **PR #164295**
- **PR #164280** Thanks @vincentkoc.
- **PR #164224**
- **PR #164303**
- **PR #163535**
- **PR #164292**
- **PR #164285** Related #164256. Thanks @obviyus and @Twilight-Networks.
- **PR #164284**
- **PR #164222**
- **PR #164288**
- **PR #164312**
- **PR #163842** Thanks @jalehman.
- **PR #163857** Thanks @jalehman.
- **PR #164116** Thanks @joshavant.
- **PR #164135** Thanks @joshavant.
- **PR #164213** Thanks @joshavant.
- **PR #162177** Thanks @jalehman.
- **PR #162033** Related #161953. Thanks @cestercian and @RomneyDa and @zhyx1996.
- **PR #164317**
- **PR #164322**
- **PR #164331**
- **PR #164332**
- **PR #164333**
- **PR #164307**
- **PR #164313**
- **PR #164321**
- **PR #164197** Thanks @galiniliev and @KirDE.
- **PR #164335**
- **PR #164336** Related #164283. Thanks @jayzhou2309 and @obviyus and @nkarkare.
- **PR #164326**
- **PR #162954** Thanks @vincentkoc.
- **PR #160108** Thanks @galiniliev.
- **PR #164203**
- **PR #164348**
- **PR #164340**
- **PR #164161** Thanks @GoldArowana and @obviyus.
- **PR #164358**
- **PR #163350**
- **PR #164361**
- **PR #164353**
- **PR #162036** Thanks @LinzeShi and @obviyus.
- **PR #164337**
- **PR #164345** Thanks @vincentkoc.
- **PR #164349**
- **PR #164370**
- **PR #164352**
- **PR #164374**
- **PR #164151** Related #164149. Thanks @ooiuuii and @obviyus.
- **PR #164380**
- **PR #164367**
- **PR #164359**
- **PR #164350**
- **PR #164360**
- **PR #164364** Related #164362. Thanks @ooiuuii and @obviyus.
- **PR #164376**
- **PR #164386**
- **PR #164398**
- **PR #164291**
- **PR #164400**
- **PR #162938** Thanks @vincentkoc.
- **PR #164373**
- **PR #164378**
- **PR #164389**
- **PR #163701** Related #163700. Thanks @sxh313 and @obviyus.
- **PR #164173**
- **PR #164387**
- **PR #165** Thanks @Nachx639.
- **PR #164236** Related #163961. Thanks @JakeMalis.
- **PR #164410**
- **PR #164306**
- **PR #163799**
- **PR #164377**
- **PR #164296**
- **PR #164391**
- **PR #164402** Thanks @vincentkoc.
- **PR #164381**
- **PR #164418**
- **PR #164103**
- **PR #164413**
- **PR #164325** Related #164323. Thanks @ooiuuii and @obviyus.
- **PR #163203**
- **PR #164264**
- **PR #164428**
- **PR #164342** Thanks @RomneyDa.
- **PR #164434**
- **PR #164421**
- **PR #164419**
- **PR #164432** Thanks @RomneyDa.
- **PR #164437**
- **PR #164430**
- **PR #164259** Related #164257. Thanks @ooiuuii and @obviyus.
- **PR #160582** Related #122476. Thanks @jayzhou2309 and @obviyus and @imabotone-ui.
- **PR #164403**
- **PR #164423** Thanks @vincentkoc.
- **PR #164438**
- **PR #164446** Thanks @RomneyDa.
- **PR #164436**
- **PR #164411**
- **PR #164440** Thanks @RomneyDa.
- **PR #164435** Related #150152. Thanks @fuller-stack-dev and @joryirving.
- **PR #160619** Thanks @LinzeShi and @obviyus.
- **PR #164451** Thanks @RomneyDa.
- **PR #164457** Thanks @vincentkoc.
- **PR #163487** Thanks @ericcurtin and @obviyus.
- **PR #162258** Thanks @RomneyDa.
- **PR #162612**
- **PR #163766**
- **PR #163623**
- **PR #164483** Thanks @RomneyDa.
- **PR #164450** Thanks @RomneyDa.
- **PR #164481**
- **PR #164469**
- **PR #164460** Thanks @vincentkoc.
- **PR #164206** Related #164148. Thanks @jayzhou2309 and @obviyus and @TrevorDGreen33.
- **PR #164414**
- **PR #164487** Thanks @RomneyDa.
- **PR #164482**
- **PR #164495**
- **PR #164463**
- **PR #164467**
- **PR #164278**
- **PR #164489** Thanks @RomneyDa.
- **PR #164488**
- **PR #164486**
- **PR #164493**
- **PR #163471** Related #110190, #162001. Thanks @RomneyDa and @consoleaf and @JacquesLFR8.
- **PR #164448**
- **PR #164479**
- **PR #162844** Related #162031. Thanks @RvsL and @zsh20000414.
- **PR #164519**
- **PR #164524**
- **PR #164502**
- **PR #164454**
- **PR #164527**
- **PR #164513**
- **PR #164517**
- **PR #164530** Related #164499. Thanks @shakkernerd.
- **PR #164196** Thanks @RomneyDa.
- **PR #164491** Thanks @RomneyDa.
- **PR #164399**
- **PR #164543**
- **PR #163671** Thanks @vincentkoc.
- **PR #164546** Related #155644. Thanks @Alex-vonAllmen.
- **PR #164458**
- **PR #164555**
- **PR #164311** Related #164309. Thanks @ooiuuii and @obviyus.
- **PR #164466**
- **PR #164549**
- **PR #163926**
- **PR #164542**
- **PR #164565**
- **PR #164496**
- **PR #164544**
- **PR #164401**
- **PR #164552**
- **PR #164539** Thanks @vincentkoc.
- **PR #164560**
- **PR #164582**
- **PR #164492** Thanks @RomneyDa.
- **PR #164578**
- **PR #164581** Thanks @joshavant.
- **PR #164534**
- **PR #156493** Thanks @serg0x.
- **PR #162300** Related #162205. Thanks @serg0x.
- **PR #155640** Thanks @Ram-G and @RomneyDa.
- **PR #164535**
- **PR #164553** Thanks @RomneyDa.
- **PR #164464** Thanks @RomneyDa.
- **PR #163545** Related #163543. Thanks @RomneyDa.
- **PR #164286**
- **PR #163201** Related #163199. Thanks @ooiuuii and @obviyus.
- **PR #164595**
- **PR #164547**
- **PR #164586**
- **PR #164532**
- **PR #164086**
- **PR #164556**
- **PR #164576**
- **PR #164591**
- **PR #164522**
- **PR #164509** Related #164316. Thanks @rosmiroslav-create.
- **PR #164594**
- **PR #164049**
- **PR #164368** Related #164365. Thanks @ooiuuii and @obviyus.
- **PR #162204** Thanks @serg0x and @RomneyDa.
- **PR #163863**
- **PR #164614**
- **PR #164619**
- **PR #164521**
- **PR #164320**
- **PR #164561**
- **PR #164537** Related #164536.
- **PR #164573**
- **PR #149048** Thanks @nancymx-dev and @vyctorbrzezowski.
- **PR #163366**
- **PR #164623**
- **PR #164602**
- **PR #164618** Thanks @joshavant.
- **PR #164616**
- **PR #164600** Thanks @joshavant.
- **PR #164514**
- **PR #164441**
- **PR #164424**
- **PR #164628**
- **PR #164613**
- **PR #164587**
- **PR #162678** Thanks @vincentkoc.
- **PR #164606**
- **PR #164604**
- **PR #164632** Thanks @hannesrudolph.
- **PR #164330**
- **PR #164631** Thanks @joshavant.
- **PR #164634**
- **PR #164503** Thanks @RomneyDa.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.10.1-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.10.1-beta.2.tgz
- integrity: `sha512-PUWDnnOWy8pJoaBsmU4GkAQ6ZFqG3Iit7beL60io3kPoLimd66Gah6HKHKgFcgd1Clq/hm+YpzEjEGiXKuVBOQ==`
- release SHA: `c58cf3afa0793257a8127ae868d5e159da6d9d0a`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.10.1-beta.2/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/37699355693
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/37538974221
- full release validation: https://github.com/openclaw/openclaw/actions/runs/37538249385
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/37699886567
- plugin ClawHub submission: https://github.com/openclaw/openclaw/actions/runs/37699890960; public artifact verification follows successful release-parent completion
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/37700836790
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- #166856 [P0, maturity:stable, impact:ux-release-blocker] Update failure: gateway-recovery-verification (2026.9.8) — https://github.com/openclaw/openclaw/issues/166856

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #163641 draft=False fix(gateway): fence transport admission for a closing generation — https://github.com/openclaw/openclaw/pull/163641
- PR #166666 draft=False fix(browser): evict the least recently used tabs at the managed tab cap — https://github.com/openclaw/openclaw/pull/166666
- PR #166790 draft=False fix(qa): resolve stranded-reply scenario source references — https://github.com/openclaw/openclaw/pull/166790
- PR #165741 draft=False fix(plugins): use plain language for diagnostic checks — https://github.com/openclaw/openclaw/pull/165741
- PR #162126 draft=False fix: orphan-recovery restart test flakes when the retry timer has not been scheduled yet — https://github.com/openclaw/openclaw/pull/162126
- PR #166852 draft=False fix: retain Doctor failure evidence in release validation — https://github.com/openclaw/openclaw/pull/166852
- PR #161344 draft=False feat(lobster): run native LLM stages in embedded workflows — https://github.com/openclaw/openclaw/pull/161344
- PR #166587 draft=False perf(gateway): reduce SQLite work for restart-safe chat — https://github.com/openclaw/openclaw/pull/166587
- PR #166855 draft=True fix: backport Doctor validation diagnostics to 2026.10.2 — https://github.com/openclaw/openclaw/pull/166855
- PR #166850 draft=False test(models): backport catalog publication readiness to 2026.10.2 — https://github.com/openclaw/openclaw/pull/166850
- PR #166787 draft=False fix: preserve native prompt provenance through database aliases — https://github.com/openclaw/openclaw/pull/166787
- PR #144745 draft=False fix: config set gives no reason when a new agent model ref cannot resolve — https://github.com/openclaw/openclaw/pull/144745
- PR #151441 draft=False fix: messages stop sending after a reconnect until the app is relaunched — https://github.com/openclaw/openclaw/pull/151441
- PR #166846 draft=False fix(agents): reconcile interrupted subagents at startup — https://github.com/openclaw/openclaw/pull/166846
- PR #152205 draft=False fix(agents): steer background-exec completions into busy sessions — https://github.com/openclaw/openclaw/pull/152205
- PR #150246 draft=False test(agents): run the retry-after e2e against the built runtime — https://github.com/openclaw/openclaw/pull/150246
- PR #163964 draft=False fix(ui): retain image drafts after temporary files disappear — https://github.com/openclaw/openclaw/pull/163964
- PR #166858 draft=True refactor(process): align broker tests with supported transports — https://github.com/openclaw/openclaw/pull/166858
- PR #166857 draft=True fix(doctor): keep lint and JSON Doctor read-only on existing state — https://github.com/openclaw/openclaw/pull/166857
- PR #166820 draft=False test(gateway): prove inbound writer ordering without speed race — https://github.com/openclaw/openclaw/pull/166820
- PR #157739 draft=False fix(build): serialize unified tsdown runtime bundles to cap peak memory — https://github.com/openclaw/openclaw/pull/157739
- PR #166849 draft=False fix(test): keep MCP validation connected after automatic pairing approval — https://github.com/openclaw/openclaw/pull/166849
- PR #162132 draft=False fix: gateway cron test times out waiting for a forced run ack on a loaded shard — https://github.com/openclaw/openclaw/pull/162132
- PR #148581 draft=False fix(openai): gpt-5.4-nano rejects every API key as incompatible with the route when the codex plugin is enabled — https://github.com/openclaw/openclaw/pull/148581
- PR #166829 draft=False fix(ui): stop image controls from obscuring previews — https://github.com/openclaw/openclaw/pull/166829
- PR #162144 draft=False test(gateway): name the startup phase that overruns the catalog deadline — https://github.com/openclaw/openclaw/pull/162144
- PR #166828 draft=True test(gateway): backport FRV ordering and lifecycle fixtures — https://github.com/openclaw/openclaw/pull/166828
- PR #137778 draft=False fix(daemon): avoid argument-quoting scalar paths in WorkingDirectory and EnvironmentFile (#137747) — https://github.com/openclaw/openclaw/pull/137778
- PR #166817 draft=True test(release): backport Fleet and survivor harness corrections — https://github.com/openclaw/openclaw/pull/166817
- PR #166853 draft=False fix(ai): long ChatGPT Responses SSE turns fail after 16 MiB of streamed events — https://github.com/openclaw/openclaw/pull/166853
