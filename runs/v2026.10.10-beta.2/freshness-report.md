# Freshness Report

Target tag: `v2026.10.10-beta.2`

Target exists upstream: **yes**

Fetched at: `2026-10-19T12:30:26Z`

Latest beta tag: `v2026.10.10-beta.2`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.10.5`

Prior prerelease baseline: `v2026.10.10-beta.1`

## Recent issue signals

- #177311 [no-stale, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:ux-friction] sessions list shows the raw model alias under the default provider (openai/opus) for sessions with no persisted model: resolveSessionDisplayDefaults skips alias resolution — https://github.com/openclaw/openclaw/issues/177311
- #146187 [P2, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, issue-rating: 🦞 diamond lobster, impact:ux-friction] [Bug]: A PATH directory named like a required binary makes `skills check` report the skill as ready — https://github.com/openclaw/openclaw/issues/146187
- #145308 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] Feature: lazy skill-catalog discovery to reduce startup context and remove prompt-count ceiling — https://github.com/openclaw/openclaw/issues/145308
- #147728 [clawsweeper:source-repro, impact:auth-provider, P0, issue-rating: 🦞 diamond lobster, impact:ux-release-blocker] [Bug]: xAI OAuth inference 426s: x-grok-client-version carries OpenClaw's version, and isolated/utility completions omit the Grok headers entirely — https://github.com/openclaw/openclaw/issues/147728
- #148308 [P1, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other, maturity:stable] [Bug]: Gateway silently loses its foreground Tailscale Serve claim when tailscaled restarts and never re-claims it (mode=serve) — https://github.com/openclaw/openclaw/issues/148308
- #144679 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:linked-pr-open, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Design]: Make Connect a recognizable primary button in iOS Gateway setup — https://github.com/openclaw/openclaw/issues/144679
- #177239 [P2, impact:ux-friction] Update failure: global-install-foreign-destination (2026.10.4) — https://github.com/openclaw/openclaw/issues/177239

## Recent PR signals

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
