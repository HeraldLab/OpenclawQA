# Freshness Report

Target tag: `v2026.7.1-beta.2`

Target exists upstream: **yes**

Fetched at: `2026-07-05T09:30:18Z`

Latest beta tag: `v2026.7.1-beta.2`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.6.11`

Prior prerelease baseline: `v2026.7.1-beta.1`

## Recent issue signals

- #52568 [enhancement, P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster, maturity:stable] [Feature]: Discord thread-reply mention gate — respond to thread starter freely, require mention for follow-up replies — https://github.com/openclaw/openclaw/issues/52568
- #100250 [bug, maintainer] [Bug]: Workspace skill approvals leave the initiating TUI — https://github.com/openclaw/openclaw/issues/100250
- #95042 [stale, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, impact:session-state, impact:data-loss, impact:crash-loop, issue-rating: 🦐 gold shrimp, maturity:stable] [Bug]: 2026.6.x regression cascade — memory search broken, then sessions lost on every reconnect (multi-agent deployment broken) — https://github.com/openclaw/openclaw/issues/95042
- #51534 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster, maturity:stable] [Feature]: Discord - auto-inject @mention for guild message replies — https://github.com/openclaw/openclaw/issues/51534
- #99957 [bug, no-stale, bug:behavior, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:ux-friction] [Bug]: Openclaw workboard ui is not optimised for multiple cards — https://github.com/openclaw/openclaw/issues/99957
- #100246 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, impact:security, issue-rating: 🌊 off-meta tidepool, maturity:stable] [Feature]: only accept signed messages to prevent prompt injection [improvement] [hardening] — https://github.com/openclaw/openclaw/issues/100246
- #10005 [enhancement, P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, issue-rating: 🦞 diamond lobster, maturity:stable, impact:ux-friction] Add option to hide session status card — https://github.com/openclaw/openclaw/issues/10005
- #7909 [enhancement, P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Feature]: Add plain text copy option — https://github.com/openclaw/openclaw/issues/7909
- #7717 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster, maturity:stable] Feature Request: Discord role-mention triggers — https://github.com/openclaw/openclaw/issues/7717

## Recent PR signals

- PR #89569 draft=False feat(channels): add pre-auth access requests and grouped DM allowlists — https://github.com/openclaw/openclaw/pull/89569
- PR #100019 draft=False improve: keep isolated tests under one second — https://github.com/openclaw/openclaw/pull/100019
- PR #100046 draft=False fix(imessage): false group drop-all startup warning when groupAllowFrom is set without groups — https://github.com/openclaw/openclaw/pull/100046
- PR #90689 draft=False fix(agents): align custom provider auth labels with runtime (#82020) — https://github.com/openclaw/openclaw/pull/90689
- PR #90259 draft=False Add reset family carryover summaries — https://github.com/openclaw/openclaw/pull/90259
- PR #99864 draft=False fix(compaction): avoid cached usage overcount — https://github.com/openclaw/openclaw/pull/99864
- PR #100253 draft=False docs(maint): raise PR close batch limit — https://github.com/openclaw/openclaw/pull/100253
- PR #97722 draft=False fix(macos): prevent hatch and web chat from timing out on slow first replies — https://github.com/openclaw/openclaw/pull/97722
- PR #99972 draft=False fix(watch): defer restart when dist/entry.js is missing mid-rebuild — https://github.com/openclaw/openclaw/pull/99972
- PR #100251 draft=True fix(tui): keep skill approvals in the terminal — https://github.com/openclaw/openclaw/pull/100251
- PR #99564 draft=False fix(agents): prevent malformed HTML entities from breaking tool calls — https://github.com/openclaw/openclaw/pull/99564
- PR #99871 draft=False fix(android): accept case-insensitive assistant roles in voice chat text — https://github.com/openclaw/openclaw/pull/99871
- PR #99887 draft=False fix: default TLS gateway deep links to port 443 when port is omitted — https://github.com/openclaw/openclaw/pull/99887
- PR #93265 draft=False feat(onboard): streamline setup with agent-assisted configuration — https://github.com/openclaw/openclaw/pull/93265
- PR #97135 draft=False fix(auto-reply): hide recovered failed tool progress — https://github.com/openclaw/openclaw/pull/97135
- PR #100206 draft=False chore(ci): fail CI when gateway events go unhandled by the mobile apps — https://github.com/openclaw/openclaw/pull/100206
- PR #91262 draft=False fix(build): fall back to tsx for build TypeScript scripts — https://github.com/openclaw/openclaw/pull/91262
- PR #100149 draft=False fix: prevent Anthropic thinking-signature replay causing permanent session bricks (#94228) — https://github.com/openclaw/openclaw/pull/100149
- PR #99614 draft=False fix(gateway): defer hot-reload restart when dist/entry.js is missing — https://github.com/openclaw/openclaw/pull/99614
- PR #90239 draft=False [AI-assisted] Add session history family lookup — https://github.com/openclaw/openclaw/pull/90239
- PR #100231 draft=False fix: report rejected plugin approval requests accurately — https://github.com/openclaw/openclaw/pull/100231
- PR #99873 draft=False fix(android): accept boolean flag aliases in node invoke params — https://github.com/openclaw/openclaw/pull/99873
- PR #99555 draft=False fix(gateway-protocol): trim connect error detail codes in readConnectErrorDetailCode — https://github.com/openclaw/openclaw/pull/99555
- PR #100244 draft=False fix(core): use UTF-16-safe truncation for chat display, ACP stream relay, and native hook relay — https://github.com/openclaw/openclaw/pull/100244
- PR #91603 draft=False fix(acp): preserve structured error kinds — https://github.com/openclaw/openclaw/pull/91603
- PR #100229 draft=False fix: embedded_run completes with empty final payload → reply silently dropped (lane goes dark — https://github.com/openclaw/openclaw/pull/100229
- PR #93505 draft=False fix: support baseURL alias in memory embedding provider config resolution — https://github.com/openclaw/openclaw/pull/93505
- PR #98402 draft=False fix(infra): guard channel ingress queue parseJson against corrupted JSON — https://github.com/openclaw/openclaw/pull/98402
- PR #93587 draft=False fix(ui): avoid fallback main session parent in Control UI — https://github.com/openclaw/openclaw/pull/93587
- PR #100221 draft=False fix(test): unit tests fail on built checkouts and live host configs while CI stays green — https://github.com/openclaw/openclaw/pull/100221
