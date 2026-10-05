# Release Context — OpenClaw `v2026.10.1-beta.1`

Fetched at: `2026-10-05T20:00:16Z`

## Target

- Target tag: `v2026.10.1-beta.1`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.1-beta.1
- Target tag SHA: 6830fe76b3db05ad59e8ff7f0f872d4e2639a1fe

## Freshness baselines

- Latest beta tag: `v2026.10.1-beta.1`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.9.8`
- Prior prerelease baseline: `linux-stable`

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

- npm package: https://www.npmjs.com/package/openclaw/v/2026.10.1-beta.1
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.10.1-beta.1.tgz
- integrity: `sha512-W0sRPDFaNYDprNBEbdRNz55CwaETVGla3yuD0A2bp+ccpTLnmBo7lcY042YeWedf6ofkT0JBidpMc6iC7/dhug==`
- release SHA: `6830fe76b3db05ad59e8ff7f0f872d4e2639a1fe`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.10.1-beta.1/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/37357820450
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/37287442679
- full release validation: https://github.com/openclaw/openclaw/actions/runs/37286762318
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/37358739420
- plugin ClawHub publish: no normal OIDC candidates
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/37347905631/attempts/1
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- #165763 [no-labels] [Bug]: Control UI paste > 1000 chars reaches the model as EXTERNAL_UNTRUSTED_CONTENT (paste origin dropped before render) — https://github.com/openclaw/openclaw/issues/165763
- #165745 [no-stale, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Bug]: deferred tool_call serializes MCP image blocks into text instead of preserving model-visible images — https://github.com/openclaw/openclaw/issues/165745
- #164074 [clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, P0, issue-rating: 🦐 gold shrimp, impact:ux-release-blocker] Native update recovery stuck at publication-complete when retained previous package fingerprint changes — https://github.com/openclaw/openclaw/issues/164074
- #165748 [clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:needs-info, impact:security, P0, issue-rating: 🦪 silver shellfish] exec mode "ask" fails open: commands run with no approval card; flaps to approval-request-failed after restart — https://github.com/openclaw/openclaw/issues/165748
- #137264 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, issue-rating: 🦞 diamond lobster] A tombstoned agent:<id>:main has no replacement path; `sessions delete --dry-run` says would_delete but the real run refuses — https://github.com/openclaw/openclaw/issues/137264
- #97616 [bug, P1, impact:message-loss, impact:crash-loop, issue-rating: 🦪 silver shellfish, clawsweeper-recovery-stuck] [Bug]: OpenClaw leaks unreaped hook/tool child processes, causing zombie accumulation and runtime degradation — https://github.com/openclaw/openclaw/issues/97616
- #164459 [clawsweeper:needs-info, P0, issue-rating: 🦪 silver shellfish, maturity:stable, impact:ux-release-blocker] Update failure: update-executor-settlement (2026.9.7) — https://github.com/openclaw/openclaw/issues/164459

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #165377 draft=False perf(sessions): reuse revision-bound transcript projection status — https://github.com/openclaw/openclaw/pull/165377
- PR #165749 draft=False fix: open MCP server details in a dialog — https://github.com/openclaw/openclaw/pull/165749
- PR #165764 draft=False refactor(channels): persist feedback through transcript workers — https://github.com/openclaw/openclaw/pull/165764
- PR #165583 draft=False fix(auth): configured primary account blocks CLI fallback — https://github.com/openclaw/openclaw/pull/165583
- PR #116175 draft=False feat(sandbox): allow named host roots for sandbox bind sources — https://github.com/openclaw/openclaw/pull/116175
- PR #164749 draft=False fix(talk): voice consults loop on confirmations, start duplicate runs and block read-only commands — https://github.com/openclaw/openclaw/pull/164749
- PR #165334 draft=False fix(ui): revert Slack and Discord session return buttons — https://github.com/openclaw/openclaw/pull/165334
- PR #164951 draft=False fix(voice-call): keep continue poll deadline on the monotonic clock — https://github.com/openclaw/openclaw/pull/164951
- PR #161838 draft=False fix(bedrock): prompt cache misses when tool registration order changes — https://github.com/openclaw/openclaw/pull/161838
- PR #164005 draft=False fix: restore acknowledgements for bound ACP reset commands — https://github.com/openclaw/openclaw/pull/164005
- PR #165762 draft=True fix: preserve images returned by deferred tool calls — https://github.com/openclaw/openclaw/pull/165762
- PR #165758 draft=False fix(diagnostics-otel): restore CI after worker metrics addition — https://github.com/openclaw/openclaw/pull/165758
- PR #165724 draft=False fix(agents): Talk forced consults reject their recorded input when checking speech finalizes — https://github.com/openclaw/openclaw/pull/165724
- PR #165755 draft=False fix(ci): improve fixture cleanup and acceptance diagnostics — https://github.com/openclaw/openclaw/pull/165755
- PR #165756 draft=False feat(memory-lancedb): report health and serve search through the memory provider runtime — https://github.com/openclaw/openclaw/pull/165756
- PR #164705 draft=False fix(ui): number keys leave optional question answers unselected — https://github.com/openclaw/openclaw/pull/164705
- PR #165628 draft=False refactor(sessions): wire incognito creation and entry patches to the shared actor binding (P7h2, inactive) — https://github.com/openclaw/openclaw/pull/165628
- PR #165733 draft=False refactor(sessions): persist run outcomes only; liveness comes from the run registry — https://github.com/openclaw/openclaw/pull/165733
- PR #165205 draft=False perf(sessions): serve session observer authority reads from workers — https://github.com/openclaw/openclaw/pull/165205
- PR #165658 draft=False perf(auth): settle OAuth refresh through workers — https://github.com/openclaw/openclaw/pull/165658
- PR #163358 draft=False fix(llama-cpp): managed setup crashes and loops on macOS below 13.3 — https://github.com/openclaw/openclaw/pull/163358
- PR #165728 draft=False fix(codex): prevent raw visualization directives in chat — https://github.com/openclaw/openclaw/pull/165728
- PR #165760 draft=False refactor(core): deslop error and normalization paths — https://github.com/openclaw/openclaw/pull/165760
- PR #165718 draft=False refactor(channels): deslop channels — https://github.com/openclaw/openclaw/pull/165718
- PR #147238 draft=False feat(ios): own Cloudflare Access browser and profile admission — https://github.com/openclaw/openclaw/pull/147238
- PR #165761 draft=True perf(sqlite): keep scheduled checkpoints out of commits — https://github.com/openclaw/openclaw/pull/165761
- PR #165754 draft=False fix(media): preserve apostrophes in download filenames — https://github.com/openclaw/openclaw/pull/165754
- PR #165753 draft=False fix(text): keep prose between `<|` and `|>` operators in replies — https://github.com/openclaw/openclaw/pull/165753
- PR #165759 draft=False perf(gateway): retain artifact summaries across authorized requests — https://github.com/openclaw/openclaw/pull/165759
- PR #164756 draft=True fix(heartbeat): let a conversation's chained command completions skip the interval wait — https://github.com/openclaw/openclaw/pull/164756
