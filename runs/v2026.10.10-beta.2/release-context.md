# Release Context — OpenClaw `v2026.10.10-beta.2`

Fetched at: `2026-10-19T12:30:26Z`

## Target

- Target tag: `v2026.10.10-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.10-beta.2
- Target tag SHA: 2b85c4c25ea98d72ca1d3e93fb0fd9cac8f0ddab

## Freshness baselines

- Latest beta tag: `v2026.10.10-beta.2`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.10.5`
- Prior prerelease baseline: `v2026.10.10-beta.1`

## Release notes excerpt

## 2026.10.10-beta.2

### Highlights

### Changes

### Fixes

- Workspace safety: reject a multi-file `apply_patch` before changing files when a later update target is missing or its context does not match, preserving the original workspace for the next attempt. Commit-time I/O failures can still leave partial effects. (#160409; related #117742 and #127496) Thanks @masatohoshino, @obviyus, and @yetval.
- Tool policy: run plugin `before_tool_call` hooks in standalone `openclaw agent exec` sessions so plugin tool guards take effect. (#159333; fixes #158824) Thanks @joseairosa and @obviyus.
- Buzz: reconnect when a relay closes during NIP-42 authentication without terminating the Gateway or interrupting other channels and sessions. (#170591; fixes #147269) Thanks @masatohoshino, @obviyus, @jarvis-modern-mail, and @RomneyDa.
- macOS downloads: save dashboard and conversation attachments through the native Save dialog while keeping the current page open. (#173654) Thanks @Patrick-Erichsen.
- OpenRouter onboarding: accept valid API keys with the default `openrouter/auto` model instead of rejecting setup with a route mismatch. (#173292; related #162798) Thanks @chandraveshchaudhari and @obviyus.
- macOS setup: let fresh native profiles start the Gateway and complete automatic setup, including when supervised startup needs a retry. (#173246)
- Gateway startup: follow a replacement model-runtime refresh instead of exiting when initial preparation is superseded. (#173366; related #173357) Thanks @Jackten and @RomneyDa.
- Gateway logging: keep serving and shut down normally when a deleted temporary-directory backing path makes daily log rollover fail. (#160433; fixes #130807) Thanks @masatohoshino, @obviyus, @WadeOwenWatts, and @Patrick-Erichsen.
- Gateway stability: stop session diff capture from opening live SQLite and hard-linked files, preventing SIGBUS crash loops when the shared-memory file is truncated. (#174017)
- Native app updates: let Doctor finish agent database upgrades on native-first profiles instead of reporting success while the Gateway refuses to start on an older schema. (#174297)
- Cron: plan history maintenance from run identities and load full payloads only for rows it updates, so large cron histories no longer exhaust the SQLite worker's memory and take channels down. (#174530; fixes #174078) Thanks @wangmiao0668000666, @RomneyDa, and @asikorskiy.
- Windows Claude CLI: stop every turn with a stored Anthropic credential from stalling until the no-output watchdog when Claude Code never reads the credential pipe. (#174571; fixes #174204) Thanks @RomneyDa and @scalesmart.
- Plugins: restore the SDK facade exports that published external plugins still import, so those plugins load again. (#173777; fixes #173386) Thanks @RomneyDa and @FtlC-ian.
- Chat tools: keep the chat usable after removing a tool server that failed to start, cleaning up its failed startup before reporting the launch error. (#171397) Thanks @joelagnel.
- Updates: bound the post-activation Doctor step by the update's allowance instead of waiting indefinitely with the Gateway down. (#173862)
- Updates: keep Gateway-managed source updates from failing with missing backup modules after the runtime is replaced. (#173587) Thanks @vishnusenthil-16.
- Updates: make `openclaw update --no-restart` honest for npm, pnpm, and bun installs, which restart themselves after the package is replaced, record the update as successful, and keep a still-serving older build unverified. (#173409, #174649; fixes #171311) Thanks @RomneyDa and @mwbroxson.

### Complete contribution record

This audited record covers the complete v2026.10.10-beta.1..f90bd063751f2448330ee6abbb4c894508600d63 history: 24 in-range PRs + 0 retained seed-only PRs = 24 unique PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

Shipped baseline exclusions: v2026.10.10-beta.1 (1 PRs: #171016).

#### Pull requests

- **PR #173654** Thanks @Patrick-Erichsen.
- **PR #159333** Related #158824. Thanks @joseairosa and @obviyus.
- **PR #160433** Related #130807. Thanks @masatohoshino and @obviyus and @WadeOwenWatts.
- **PR #170591** Related #147269. Thanks @masatohoshino and @obviyus and @jarvis-modern-mail.
- **PR #173246**
- **PR #173292** Thanks @chandraveshchaudhari and @obviyus.
- **PR #173366**
- **PR #173259** Thanks @RomneyDa.
- **PR #173511** Thanks @RomneyDa.
- **PR #173319** Thanks @RomneyDa.
- **PR #160409** Thanks @masatohoshino.
- **PR #171397** Thanks @joelagnel.
- **PR #174017**
- **PR #173777** Related #173386. Thanks @RomneyDa and @FtlC-ian.
- **PR #173587** Thanks @vishnusenthil-16.
- **PR #173862**
- **PR #174297**
- **PR #174556** Thanks @RomneyDa.
- **PR #173205** Thanks @RomneyDa.
- **PR #174530** Related #174078. Thanks @wangmiao0668000666 and @RomneyDa and @asikorskiy.
- **PR #174571** Related #174204. Thanks @RomneyDa and @scalesmart.
- **PR #174614** Thanks @RomneyDa.
- **PR #173409** Related #171311. Thanks @RomneyDa and @mwbroxson.
- **PR #174649** Thanks @RomneyDa.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.10.10-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.10.10-beta.2.tgz
- integrity: `sha512-Kbs8X970M+kouV52kMSaF0zpxf62vink1OqpEMCcc60O7uQx6VELzcpHT5bO6KuPFeKNNSzZ40mvWwebiTKuIQ==`
- release SHA: `2b85c4c25ea98d72ca1d3e93fb0fd9cac8f0ddab`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.10.10-beta.2/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/39189217327
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/38980450683
- full release validation: https://github.com/openclaw/openclaw/actions/runs/38979780344
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/39190082116
- plugin ClawHub submission: https://github.com/openclaw/openclaw/actions/runs/39190084831; public finalization and exact artifact verification follow terminal release-parent completion
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/39190750431
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- #177311 [no-stale, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:ux-friction] sessions list shows the raw model alias under the default provider (openai/opus) for sessions with no persisted model: resolveSessionDisplayDefaults skips alias resolution — https://github.com/openclaw/openclaw/issues/177311
- #146187 [P2, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:ux-friction] [Bug]: A PATH directory named like a required binary makes `skills check` report the skill as ready — https://github.com/openclaw/openclaw/issues/146187
- #145308 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] Feature: lazy skill-catalog discovery to reduce startup context and remove prompt-count ceiling — https://github.com/openclaw/openclaw/issues/145308
- #147728 [clawsweeper:source-repro, impact:auth-provider, P0, issue-rating: 🦞 diamond lobster, impact:ux-release-blocker] [Bug]: xAI OAuth inference 426s: x-grok-client-version carries OpenClaw's version, and isolated/utility completions omit the Grok headers entirely — https://github.com/openclaw/openclaw/issues/147728
- #148308 [P1, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other, maturity:stable] [Bug]: Gateway silently loses its foreground Tailscale Serve claim when tailscaled restarts and never re-claims it (mode=serve) — https://github.com/openclaw/openclaw/issues/148308
- #144679 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:linked-pr-open, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Design]: Make Connect a recognizable primary button in iOS Gateway setup — https://github.com/openclaw/openclaw/issues/144679
- #177239 [P2, impact:ux-friction] Update failure: global-install-foreign-destination (2026.10.4) — https://github.com/openclaw/openclaw/issues/177239

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #177310 draft=False test: remove low-value tests (batch d291) — https://github.com/openclaw/openclaw/pull/177310
- PR #177318 draft=False chore(i18n): refresh native locales — https://github.com/openclaw/openclaw/pull/177318
- PR #177297 draft=False fix(feishu): reject synthetic reply anchors — https://github.com/openclaw/openclaw/pull/177297
- PR #177306 draft=False test: remove low-value tests (batch d290) — https://github.com/openclaw/openclaw/pull/177306
- PR #177291 draft=False test(ui,core,plugins): remove low-value tests (batch d289) — https://github.com/openclaw/openclaw/pull/177291
- PR #177301 draft=False refactor: remove unused bootstrap and process arguments — https://github.com/openclaw/openclaw/pull/177301
- PR #177317 draft=False fix(codex): record rejected dynamic-tool cleanup on ordinary runs — https://github.com/openclaw/openclaw/pull/177317
- PR #177309 draft=False refactor(gateway): share skills RPC validation — https://github.com/openclaw/openclaw/pull/177309
- PR #177315 draft=False refactor(media): trim redundant media and voice summaries — https://github.com/openclaw/openclaw/pull/177315
- PR #171663 draft=True fix(diagnostics-otel): model call spans drop Anthropic cache-write TTL split — https://github.com/openclaw/openclaw/pull/171663
- PR #177279 draft=False test(core,plugins,ui): remove low-value tests (batch d287) — https://github.com/openclaw/openclaw/pull/177279
- PR #177316 draft=True fix(status): keep unreadable logs visible in diagnostic reports — https://github.com/openclaw/openclaw/pull/177316
- PR #177304 draft=False fix(gateway): stop worker reconciliation tails during shutdown — https://github.com/openclaw/openclaw/pull/177304
- PR #166568 draft=False fix: preserve assistant answers when media delivery reuses response indexes — https://github.com/openclaw/openclaw/pull/166568
- PR #174599 draft=False feat(state): local client credential cutover (R0 PR1b) — https://github.com/openclaw/openclaw/pull/174599
- PR #177313 draft=False fix(models): honor explicit catalog refresh budgets — https://github.com/openclaw/openclaw/pull/177313
- PR #177092 draft=False refactor(plugins): trim redundant install and runtime summaries — https://github.com/openclaw/openclaw/pull/177092
- PR #177153 draft=False perf(control-ui): admit warm full-UUID routes from snapshots — https://github.com/openclaw/openclaw/pull/177153
- PR #177314 draft=False feat(agents): expose system overview as a read action for the system agent — https://github.com/openclaw/openclaw/pull/177314
- PR #177307 draft=False fix(plugins): preserve resultContentSource declared on defineToolPlugin tools — https://github.com/openclaw/openclaw/pull/177307
- PR #166516 draft=False fix(discord): keep typing active while owned child work runs — https://github.com/openclaw/openclaw/pull/166516
- PR #173202 draft=False feat(workboard): target one card during dispatch — https://github.com/openclaw/openclaw/pull/173202
- PR #176955 draft=False fix(minimax): use MiniMax-M3.1-Flash model id — https://github.com/openclaw/openclaw/pull/176955
- PR #166464 draft=False fix(gateway): keep service credentials referenced only by auth profiles — https://github.com/openclaw/openclaw/pull/166464
- PR #166380 draft=False fix: agents in a group acknowledge each other forever when bot-sender silence is allowed — https://github.com/openclaw/openclaw/pull/166380
- PR #167529 draft=False feat(diagnostics): add bundle fingerprints to skill.used spans — https://github.com/openclaw/openclaw/pull/167529
- PR #175652 draft=False improve: speed up splitting long channel replies — https://github.com/openclaw/openclaw/pull/175652
- PR #175509 draft=False feat(providers): add Bifrost provider and allow anonymous self-hosted gateways — https://github.com/openclaw/openclaw/pull/175509
- PR #165798 draft=False feat(subagents): show how long a continuable yielded leaf has been paused — https://github.com/openclaw/openclaw/pull/165798
- PR #176154 draft=False fix(anthropic): stop reporting success after OpenClaw MCP startup fails — https://github.com/openclaw/openclaw/pull/176154
