# Freshness Report

Target tag: `v2026.10.10-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-10-15T18:30:23Z`

Latest beta tag: `v2026.10.10-beta.1`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.9.33`

Prior prerelease baseline: `v2026.10.5-beta.4`

## Recent issue signals

- #173386 [no-labels] [Bug]: plugin-sdk/approval-reaction-runtime no longer exports readApprovalReactionDeliveryMetadata (2026.10.5 betas break external plugins) — https://github.com/openclaw/openclaw/issues/173386
- #148658 [bug, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:linked-pr-open, issue-rating: 🦪 silver shellfish, impact:other] [Bug]: macOS realtime Talk cancels multi-sentence replies with playback-overflow — https://github.com/openclaw/openclaw/issues/148658
- #173388 [no-labels] Control UI Talk: one talk.session.appendAudio slower than 8 s ends the session, even when the gateway recovers — https://github.com/openclaw/openclaw/issues/173388
- #48709 [stale, P2, impact:session-state, impact:message-loss, issue-rating: 🦪 silver shellfish] Gemini 2.5 Pro: textSignature bloat + think tags + mixed text/tool causes session failures — https://github.com/openclaw/openclaw/issues/48709
- #173381 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:auth-provider, issue-rating: 🦞 diamond lobster] Same-model rate_limit retry never records a failure on the auth profile, so every concurrent run re-hits the limited profile and sleeps the full Retry-After — https://github.com/openclaw/openclaw/issues/173381

## Recent PR signals

- PR #173378 draft=False test(ui): remove retired community dismissal from cron proof — https://github.com/openclaw/openclaw/pull/173378
- PR #173226 draft=False fix: publish model picker fixtures through Gateway — https://github.com/openclaw/openclaw/pull/173226
- PR #173374 draft=False refactor(tests): remove redundant Wear cases — https://github.com/openclaw/openclaw/pull/173374
- PR #171664 draft=False refactor(ui): separate presentation contract from Lit adapters — https://github.com/openclaw/openclaw/pull/171664
- PR #173376 draft=False test(logging): isolate prefix cases from cached inode — https://github.com/openclaw/openclaw/pull/173376
- PR #173387 draft=True fix(agents): contain failures publishing saved transcript updates — https://github.com/openclaw/openclaw/pull/173387
- PR #173277 draft=False perf(gateway): bound pairing snapshots during connect attachment — https://github.com/openclaw/openclaw/pull/173277
- PR #168596 draft=False fix: guide repair of archived native command sessions — https://github.com/openclaw/openclaw/pull/168596
- PR #159136 draft=False fix: CLI channel sessions cannot spawn worker threads — https://github.com/openclaw/openclaw/pull/159136
- PR #173382 draft=False fix(code-mode): distinguish worker retirement causes — https://github.com/openclaw/openclaw/pull/173382
- PR #173385 draft=False fix(ui): clear stuck model checks after catalog publication — https://github.com/openclaw/openclaw/pull/173385
- PR #173375 draft=False refactor(providers): share catalog facts and JSON response ownership — https://github.com/openclaw/openclaw/pull/173375
- PR #173239 draft=False fix: preserve session caches when database workers exit — https://github.com/openclaw/openclaw/pull/173239
- PR #155634 draft=False feat(provider): add Databricks Unity Gateway — https://github.com/openclaw/openclaw/pull/155634
- PR #171784 draft=False refactor(ui): render chat widgets and tool previews with Solid — https://github.com/openclaw/openclaw/pull/171784
- PR #173264 draft=False perf(control-ui): avoid reparsing completed code while replies stream — https://github.com/openclaw/openclaw/pull/173264
- PR #173384 draft=False perf(recovery): skip archived sessions before writer preparation — https://github.com/openclaw/openclaw/pull/173384
- PR #173346 draft=False feat(claws): prepare private drafts for reviewed publication — https://github.com/openclaw/openclaw/pull/173346
- PR #173371 draft=False fix: warn when session participant recording fails — https://github.com/openclaw/openclaw/pull/173371
- PR #173190 draft=False docs(config): warn about Windows environment snapshot serialization — https://github.com/openclaw/openclaw/pull/173190
- PR #173178 draft=False fix: plugin builds reject manifests with JSON5 syntax — https://github.com/openclaw/openclaw/pull/173178
- PR #173275 draft=True experiment(control-ui): menu first-open attribution [do not merge] — https://github.com/openclaw/openclaw/pull/173275
- PR #160873 draft=False feat(discord): AI auto-naming for threads via channels.discord.thread.autoName — https://github.com/openclaw/openclaw/pull/160873
- PR #173377 draft=False feat(ui): create and review Claws from agents and sessions — https://github.com/openclaw/openclaw/pull/173377
- PR #162078 draft=False fix(whatsapp): messages that first arrive undecryptable are never delivered — https://github.com/openclaw/openclaw/pull/162078
- PR #168375 draft=False fix(oc-path): recursive wildcard misses zero-segment matches and duplicates results — https://github.com/openclaw/openclaw/pull/168375
- PR #173004 draft=False refactor(ui): remove activity media bridge — https://github.com/openclaw/openclaw/pull/173004
- PR #173372 draft=False fix(test): prepare Gateway workers before fixture shutdown deadlines — https://github.com/openclaw/openclaw/pull/173372
- PR #173345 draft=False feat(claws): discover and add community Claws — https://github.com/openclaw/openclaw/pull/173345
- PR #173265 draft=False refactor(ui): port chat pane support to Solid — https://github.com/openclaw/openclaw/pull/173265
