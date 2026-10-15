# Freshness Report

Target tag: `v2026.10.5-beta.4`

Target exists upstream: **yes**

Fetched at: `2026-10-15T06:30:22Z`

Latest beta tag: `v2026.10.5-beta.4`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.10.3`

Prior prerelease baseline: `v2026.10.5-beta.3`

## Recent issue signals

- #70266 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:other] [Feature]: Use assistant avatar in macOS Talk Mode overlay — https://github.com/openclaw/openclaw/issues/70266
- #53345 [enhancement, P3, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Feature]: Add Korean (ko) language support to Control UI and AI agent — https://github.com/openclaw/openclaw/issues/53345
- #137299 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, impact:security, issue-rating: 🦞 diamond lobster, clawsweeper:bulk-filed] [Feature]: exec children carry no calling-agent identity, so a scoped wrapper must encode the agent in its own path — https://github.com/openclaw/openclaw/issues/137299
- #108599 [clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit] sessions_send announce delivery causes 2-3x turn amplification on claude-cli agents (session-limit exhaustion observed) — https://github.com/openclaw/openclaw/issues/108599
- #111143 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Feature]: Allow pinning plugin tabs in the Control UI sidebar — https://github.com/openclaw/openclaw/issues/111143
- #159276 [clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster] Native Ollama: plugin runtime.llm.complete() does not serialize reasoning: off as think: false — https://github.com/openclaw/openclaw/issues/159276
- #170367 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, impact:auth-provider, issue-rating: 🦪 silver shellfish] [Feature]: OAuth usage-limit errors (ChatGPT/Codex 5h & weekly) should trigger auth profile rotation to the next configured OAuth account — https://github.com/openclaw/openclaw/issues/170367

## Recent PR signals

- PR #172771 draft=False fix(whatsapp): queued messages show an error reaction after successful handling — https://github.com/openclaw/openclaw/pull/172771
- PR #172841 draft=False test(plugins): remove low-value tests (batch d089) — https://github.com/openclaw/openclaw/pull/172841
- PR #172847 draft=False perf(gateway): remove redundant work from repeated RPC reads — https://github.com/openclaw/openclaw/pull/172847
- PR #172814 draft=False fix(agents): preserve whitespace in node-host exec workdir paths — https://github.com/openclaw/openclaw/pull/172814
- PR #172569 draft=True feat(macos): launch the compiled OpenClaw runtime — https://github.com/openclaw/openclaw/pull/172569
- PR #172810 draft=False fix: queued follow-up answers appear twice in WebChat — https://github.com/openclaw/openclaw/pull/172810
- PR #172848 draft=True perf(agents): bound requester lookup and transcript replay work — https://github.com/openclaw/openclaw/pull/172848
- PR #171846 draft=False refactor(ui): remove Lit dependency from subscriptions — https://github.com/openclaw/openclaw/pull/171846
- PR #87434 draft=True [codex] Expire Telegram message-cache plugin state — https://github.com/openclaw/openclaw/pull/87434
- PR #172833 draft=False fix(ci): continue stale PR scans at the label limit — https://github.com/openclaw/openclaw/pull/172833
- PR #172044 draft=False fix(ui): lint Solid TypeScript helpers — https://github.com/openclaw/openclaw/pull/172044
- PR #86793 draft=False fix(gateway): lighten session event row snapshots — https://github.com/openclaw/openclaw/pull/86793
- PR #172845 draft=False fix(ci): verify stale checkpoints in their actual cache backend — https://github.com/openclaw/openclaw/pull/172845
- PR #171664 draft=False refactor(ui): separate presentation contract from Lit adapters — https://github.com/openclaw/openclaw/pull/171664
- PR #172846 draft=False fix(crabbox): wait for availability when Crabbox cannot attest capture — https://github.com/openclaw/openclaw/pull/172846
- PR #172363 draft=False refactor(ui): render plugin routes directly with Solid — https://github.com/openclaw/openclaw/pull/172363
- PR #171549 draft=False fix(database): account, approval, and usage writes hold the SQLite writer during host admission — https://github.com/openclaw/openclaw/pull/171549
- PR #172844 draft=True feat: compress oversized videos without blocking chat — https://github.com/openclaw/openclaw/pull/172844
- PR #157806 draft=False fix(sessions): preserve requester identity at execution admission — https://github.com/openclaw/openclaw/pull/157806
- PR #172840 draft=False fix(subagents): keep completions from same-key children of different agents — https://github.com/openclaw/openclaw/pull/172840
- PR #172843 draft=False fix: remove redundant chat delivery and restart subtext — https://github.com/openclaw/openclaw/pull/172843
- PR #165481 draft=False fix(gateway): report stt-tts readiness and transports in talk.catalog — https://github.com/openclaw/openclaw/pull/165481
- PR #155634 draft=False feat(provider): add Databricks Unity Gateway — https://github.com/openclaw/openclaw/pull/155634
- PR #172834 draft=False fix(ci): retire unused internal channel and helper exports — https://github.com/openclaw/openclaw/pull/172834
- PR #172802 draft=False feat: shrink standalone sidecars and bundle SQLite — https://github.com/openclaw/openclaw/pull/172802
- PR #172695 draft=False test(ui): cover reasoning handoff disclosures — https://github.com/openclaw/openclaw/pull/172695
- PR #172653 draft=False fix(ai): detach OpenAI stream partial snapshots from live output — https://github.com/openclaw/openclaw/pull/172653
- PR #172283 draft=False fix(buzz): preserve literal credential-file paths — https://github.com/openclaw/openclaw/pull/172283
- PR #172676 draft=False improve: avoid repeated SQLite admission after handle closure — https://github.com/openclaw/openclaw/pull/172676
- PR #154607 draft=False improve(browser): default managed Chromium to efficient headless launches — https://github.com/openclaw/openclaw/pull/154607
