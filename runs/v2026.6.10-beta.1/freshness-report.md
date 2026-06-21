# Freshness Report

Target tag: `v2026.6.10-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-06-21T09:30:41Z`

Latest beta tag: `v2026.6.10-beta.1`

Latest alpha tag: `v2026.6.20-alpha.1`

Stable baseline: `v2026.6.9`

Prior prerelease baseline: `v2026.6.9-beta.1`

## Recent issue signals

- #87023 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:source-repro, impact:security, impact:message-loss, issue-rating: 🦞 diamond lobster] [Feature]: First-class relay of MCP ImageContent (and other binary Content) to channel extensions (iMessage/BlueBubbles, Telegram, Signal, …) — https://github.com/openclaw/openclaw/issues/87023
- #88646 [stale, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, impact:session-state, impact:data-loss, issue-rating: 🦞 diamond lobster] Persist image understanding summaries for agent attachments — https://github.com/openclaw/openclaw/issues/88646
- #88568 [stale, P3, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] feat: support pinning / starring sessions for quick access — https://github.com/openclaw/openclaw/issues/88568
- #88373 [P3, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:auth-provider, issue-rating: 🦞 diamond lobster] Windows post-onboarding provider switch path is not discoverable — https://github.com/openclaw/openclaw/issues/88373
- #87876 [P1, clawsweeper:source-repro, impact:session-state, impact:data-loss, impact:auth-provider, issue-rating: 🦞 diamond lobster] Bug: Bedrock Converse Streaming silently aborts on long-context agent sessions (~6 min timeout, no retry, no fallback) — https://github.com/openclaw/openclaw/issues/87876
- #86632 [P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-security-review, clawsweeper:needs-live-repro, impact:security, impact:auth-provider, issue-rating: 🐚 platinum hermit] OpenClaw local embedded Ollama/Qwen session fails live-data request that Pi coding agent handles via shell/curl — https://github.com/openclaw/openclaw/issues/86632

## Recent PR signals

- PR #95308 draft=False fix(ci): filter ClawSweeper comment dispatches before token minting — https://github.com/openclaw/openclaw/pull/95308
- PR #95501 draft=False fix(agents): classify generic external runner failure text as fallback-worthy — https://github.com/openclaw/openclaw/pull/95501
- PR #95307 draft=False fix(gateway): surface cross-agent subagent sessions via allAgents flag (#95295) — https://github.com/openclaw/openclaw/pull/95307
- PR #95524 draft=False fix(agents): classify upstream_error errorType as server_error for model fallback (fixes #95519) (AI-assisted) — https://github.com/openclaw/openclaw/pull/95524
- PR #95522 draft=False feat(telegram): unify progress fallback with assistant preview lane — https://github.com/openclaw/openclaw/pull/95522
- PR #95183 draft=False fix(telegram): materialize streaming progress placeholders — https://github.com/openclaw/openclaw/pull/95183
- PR #93680 draft=False feat(browser): My Browser node-anchored turn routing (stacks on #93411) — https://github.com/openclaw/openclaw/pull/93680
- PR #93187 draft=False fix(memory-core): exclude archive transcripts from dreaming corpus and propagate cron parentage to subagents — https://github.com/openclaw/openclaw/pull/93187
- PR #94308 draft=False feat(status): show session costs — https://github.com/openclaw/openclaw/pull/94308
- PR #67820 draft=False fix(whatsapp): reuse active QR and preserve runtime warnings — https://github.com/openclaw/openclaw/pull/67820
- PR #95517 draft=False fix(macos): recognize launchd Node.js gateway in PortGuardian sweep (fixes #94476) (AI-assisted) — https://github.com/openclaw/openclaw/pull/95517
- PR #95508 draft=False fix #95489: [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response — https://github.com/openclaw/openclaw/pull/95508
- PR #62503 draft=False feat: add devcontainer for cross-platform development — https://github.com/openclaw/openclaw/pull/62503
- PR #93168 draft=False fix(active-memory): exclude dreaming-narrative session keys from interactive eligibility gate — https://github.com/openclaw/openclaw/pull/93168
- PR #95527 draft=False fix(scripts): type windows taskkill helper — https://github.com/openclaw/openclaw/pull/95527
- PR #88684 draft=False Keep agent web_search on runtime provider resolution — https://github.com/openclaw/openclaw/pull/88684
- PR #88522 draft=True Fix Telegram active-run ingress sequencing — https://github.com/openclaw/openclaw/pull/88522
- PR #95487 draft=False feat(tts): strip emoji characters before speech synthesis (fixes #95478) — https://github.com/openclaw/openclaw/pull/95487
- PR #87958 draft=False fix(agents): scale read output for small contexts — https://github.com/openclaw/openclaw/pull/87958
- PR #85671 draft=False fix(outbound): auto-select single enabled message account — https://github.com/openclaw/openclaw/pull/85671
- PR #85670 draft=False perf(doctor): parallel I/O for repair sequence and plugin dep cleanup (A1) — https://github.com/openclaw/openclaw/pull/85670
- PR #78606 draft=False fix: keep origin-only approval delivery out of DMs — https://github.com/openclaw/openclaw/pull/78606
- PR #59859 draft=False feat: cute GTK-native Linux App (#75) — https://github.com/openclaw/openclaw/pull/59859
- PR #75225 draft=False feat(agents): add description field for dynamic agent discovery — https://github.com/openclaw/openclaw/pull/75225
- PR #49063 draft=False Telegram: allow native channel commands in explicitly allowed chats — https://github.com/openclaw/openclaw/pull/49063
- PR #94772 draft=False fix(gateway): cancel deferred channel reload when restart becomes pending — https://github.com/openclaw/openclaw/pull/94772
- PR #90610 draft=False Surface Codex final answer candidates in activity — https://github.com/openclaw/openclaw/pull/90610
- PR #93841 draft=False fix(ui): render persisted history text blocks — https://github.com/openclaw/openclaw/pull/93841
- PR #93351 draft=False feat(cli): add --message-file to openclaw agent — https://github.com/openclaw/openclaw/pull/93351
- PR #43493 draft=False feat: configure metadata (contextWindow, maxTokens, etc.) for custom provider setup — https://github.com/openclaw/openclaw/pull/43493
