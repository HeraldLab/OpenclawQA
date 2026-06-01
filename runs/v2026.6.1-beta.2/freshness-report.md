# Freshness Report

Target tag: `v2026.6.1-beta.2`

Target exists upstream: **yes**

Fetched at: `2026-06-01T22:00:14Z`

Latest beta tag: `v2026.6.1-beta.2`

Latest alpha tag: `v2026.6.1-alpha.3`

Stable baseline: `v2026.5.28`

Prior prerelease baseline: `v2026.6.1-beta.1`

## Recent issue signals

- #89237 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] iMessage bridge recovery can dispatch stale inbound backlog as fresh requests — https://github.com/openclaw/openclaw/issues/89237
- #89233 [security, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:auth-provider, issue-rating: 🦞 diamond lobster] [Bug]: Default models.providers.lmstudio.apiKey ships as plaintext placeholder 'lm-studio' — triggers false-positive security audit warning — https://github.com/openclaw/openclaw/issues/89233
- #89235 [P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] iMessage cron delivery: hex group chat ID stripped to bogus phone number — https://github.com/openclaw/openclaw/issues/89235
- #89173 [no-labels] External plugin tools (memory_store, memory_recall, etc.) not routed/exposed to the Agent in v2026.5.27+ — https://github.com/openclaw/openclaw/issues/89173
- #89232 [P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Bug]: openclaw doctor reports platform-incompatible skills (macOS-only / Linux-only) as 'missing requirements' on incompatible hosts — https://github.com/openclaw/openclaw/issues/89232
- #89231 [P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:crash-loop, issue-rating: 🦞 diamond lobster] [Bug]: Windows installer-created scheduled task launches gateway.cmd with visible console — should use windowless launcher — https://github.com/openclaw/openclaw/issues/89231
- #89228 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:session-state, issue-rating: 🐚 platinum hermit, impact:other] Regression: exec intermittently unavailable in isolated cron sessions (was fixed in 2026.4.1) — https://github.com/openclaw/openclaw/issues/89228
- #87714 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:needs-info, impact:security, issue-rating: 🦪 silver shellfish] [Feature]: Proposal: Source-Aware Instruction Tracking as architectural mitigation for indirect prompt injection — https://github.com/openclaw/openclaw/issues/87714
- #89225 [P2, clawsweeper:source-repro, impact:crash-loop, issue-rating: 🦞 diamond lobster] doctor: unhandled rejection "FsSafeError: root dir not found" when an agent workspace dir is missing — https://github.com/openclaw/openclaw/issues/89225
- #89223 [P1, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-security-review, clawsweeper:needs-live-repro, impact:security, impact:auth-provider, issue-rating: 🐚 platinum hermit] [Bug]: SecretRef file provider broken on Windows 11 26200 — icacls /sid unsupported, preflight validator ignores allowInsecurePath — https://github.com/openclaw/openclaw/issues/89223
- #89222 [P2, clawsweeper:needs-info, impact:message-loss, issue-rating: 🦪 silver shellfish] Slack Socket Mode events not reaching Gateway despite full config per documentation — https://github.com/openclaw/openclaw/issues/89222

## Recent PR signals

- PR #87072 draft=False feat(telegram): opt-in interleaved progress lane — https://github.com/openclaw/openclaw/pull/87072
- PR #89238 draft=True fix(reply): let active turns reach queue policy — https://github.com/openclaw/openclaw/pull/89238
- PR #89083 draft=False fix(feishu): prevent later final-shaped diagnostics from overwriting streaming card answer — https://github.com/openclaw/openclaw/pull/89083
- PR #89157 draft=False docs: document reusable helper contracts — https://github.com/openclaw/openclaw/pull/89157
- PR #89240 draft=True fix(codex): guard dynamic tool descriptors — https://github.com/openclaw/openclaw/pull/89240
- PR #89144 draft=False feat(channels): add Zulip external channel catalog entry — https://github.com/openclaw/openclaw/pull/89144
- PR #88748 draft=True fix(gemini): bridge OAuth profiles into CLI runtime — https://github.com/openclaw/openclaw/pull/88748
- PR #89239 draft=True fix(imessage): repair DM sender fallback before pairing — https://github.com/openclaw/openclaw/pull/89239
- PR #88504 draft=False feat(memory): add multi-slot memory role architecture — https://github.com/openclaw/openclaw/pull/88504
- PR #89236 draft=True fix(slack): default member-info userId to inbound sender — https://github.com/openclaw/openclaw/pull/89236
- PR #89234 draft=False feat(browser): type secrets from env vars via {{env:KEY}} placeholders — https://github.com/openclaw/openclaw/pull/89234
- PR #86719 draft=False test(skills): cover stale plugin skill symlink retarget — https://github.com/openclaw/openclaw/pull/86719
- PR #89229 draft=True fix(llm): guard Anthropic provider tool descriptors — https://github.com/openclaw/openclaw/pull/89229
- PR #89230 draft=False fix(agent-tools): resolve workspace-scoped tool fs root lazily — https://github.com/openclaw/openclaw/pull/89230
- PR #86233 draft=False fix(codex): cap managed app-server trace logs — https://github.com/openclaw/openclaw/pull/86233
- PR #88948 draft=False Keep iMessage typing active during tool work — https://github.com/openclaw/openclaw/pull/88948
- PR #89220 draft=False fix(agents): avoid duplicate generated media fallback — https://github.com/openclaw/openclaw/pull/89220
- PR #89221 draft=True fix(agents): guard Anthropic tool descriptors — https://github.com/openclaw/openclaw/pull/89221
- PR #87703 draft=False fix(agents): run before_agent_finalize for embedded agents — https://github.com/openclaw/openclaw/pull/87703
- PR #88815 draft=True feat: channel echo / session pinning — https://github.com/openclaw/openclaw/pull/88815
- PR #78303 draft=False feat(mcp): channel-mediated approval for MCP tool calls (consent envelope) — https://github.com/openclaw/openclaw/pull/78303
- PR #89191 draft=False fix(webchat): show sessions_send handoffs as forwarded — https://github.com/openclaw/openclaw/pull/89191
- PR #89214 draft=False whatsapp: expose connection watchdog tuning in account config — https://github.com/openclaw/openclaw/pull/89214
- PR #82497 draft=False fix(auth): prefer agent-local provider profiles — https://github.com/openclaw/openclaw/pull/82497
- PR #89213 draft=True fix(agents): guard CLI loopback prompt tools — https://github.com/openclaw/openclaw/pull/89213
- PR #88821 draft=False trace: Correlate channel message diagnostics into one trace — https://github.com/openclaw/openclaw/pull/88821
- PR #82490 draft=False fix(browser): reject credentialed navigation URLs — https://github.com/openclaw/openclaw/pull/82490
- PR #89183 draft=True fix(tui): keep local slash commands out of model prompts — https://github.com/openclaw/openclaw/pull/89183
- PR #82495 draft=False fix(doctor): scope state dir scan to current home — https://github.com/openclaw/openclaw/pull/82495
- PR #81907 draft=False fix(webchat): preserve code block whitespace — https://github.com/openclaw/openclaw/pull/81907
