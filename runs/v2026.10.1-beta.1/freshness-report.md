# Freshness Report

Target tag: `v2026.10.1-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-10-05T20:00:16Z`

Latest beta tag: `v2026.10.1-beta.1`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.9.8`

Prior prerelease baseline: `linux-stable`

## Recent issue signals

- #165763 [no-labels] [Bug]: Control UI paste > 1000 chars reaches the model as EXTERNAL_UNTRUSTED_CONTENT (paste origin dropped before render) — https://github.com/openclaw/openclaw/issues/165763
- #165745 [no-stale, P2, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Bug]: deferred tool_call serializes MCP image blocks into text instead of preserving model-visible images — https://github.com/openclaw/openclaw/issues/165745
- #164074 [clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-info, P0, issue-rating: 🦐 gold shrimp, impact:ux-release-blocker] Native update recovery stuck at publication-complete when retained previous package fingerprint changes — https://github.com/openclaw/openclaw/issues/164074
- #165748 [clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:needs-info, impact:security, P0, issue-rating: 🦪 silver shellfish] exec mode "ask" fails open: commands run with no approval card; flaps to approval-request-failed after restart — https://github.com/openclaw/openclaw/issues/165748
- #137264 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, issue-rating: 🦞 diamond lobster] A tombstoned agent:<id>:main has no replacement path; `sessions delete --dry-run` says would_delete but the real run refuses — https://github.com/openclaw/openclaw/issues/137264
- #97616 [bug, P1, impact:message-loss, impact:crash-loop, issue-rating: 🦪 silver shellfish, clawsweeper-recovery-stuck] [Bug]: OpenClaw leaks unreaped hook/tool child processes, causing zombie accumulation and runtime degradation — https://github.com/openclaw/openclaw/issues/97616
- #164459 [clawsweeper:needs-info, P0, issue-rating: 🦪 silver shellfish, maturity:stable, impact:ux-release-blocker] Update failure: update-executor-settlement (2026.9.7) — https://github.com/openclaw/openclaw/issues/164459

## Recent PR signals

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
