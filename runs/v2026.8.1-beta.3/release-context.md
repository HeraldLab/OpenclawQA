# Release Context — OpenClaw `v2026.8.1-beta.3`

Fetched at: `2026-08-24T05:00:58Z`

## Target

- Target tag: `v2026.8.1-beta.3`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.8.1-beta.3
- Target tag SHA: 5831b80721f802072b0ec1893b30a16cf42d538c

## Freshness baselines

- Latest beta tag: `v2026.8.1-beta.3`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.7.1-2`
- Prior prerelease baseline: `v2026.8.1-beta.2`

## Release notes excerpt

## Highlights

- GPT-5.6 Sol, Terra, Luna, and Ultra reasoning support across OpenClaw and the Codex runtime.
- Control UI first-run setup now continues verified model setup into Custodian and optional channel setup.
- Puppeteer-compatible CDP relay support for paired Chrome sessions.
- Explicit external Gateway lifecycle supervision with verified restart handoff.
- Compact, verified SQLite backup and fresh-target restore commands.
- Shared durable ingress monitors for channel plugins.

## Publication evidence

- npm: https://www.npmjs.com/package/openclaw/v/2026.8.1-beta.3
- Registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.8.1-beta.3.tgz
- Integrity: `sha512-8v+2Knr+0i1qzWXgJmtcBg78VaoMENahLxcuThOqyCmVaCGPj++mI9yv0R440wMv9Siv4fysd5e0YmBVftDvuQ==`
- Core npm preflight: https://github.com/openclaw/openclaw/actions/runs/32687267214
- Core npm publication: https://github.com/openclaw/openclaw/actions/runs/32689503061
- Official plugin publication and reconciliation: https://github.com/openclaw/openclaw/actions/runs/32680190375
- All 89 official npm plugins were read back at `2026.8.1-beta.3` with the `beta` selector and complete tarball integrity metadata.
- `@openclaw/codex@2026.8.1-beta.3` ships the exact managed `@openai/codex@0.149.1` runtime.

See [`CHANGELOG.md`](https://github.com/openclaw/openclaw/blob/v2026.8.1-beta.3/CHANGELOG.md) for the complete release notes.


## Recent issue risk signals

- #127562 [bug, maintainer, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] Bedrock tool discovery order destabilizes cache-eligible request identity — https://github.com/openclaw/openclaw/issues/127562
- #127954 [P3, clawsweeper:no-new-fix-pr, clawsweeper:linked-pr-open, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Feature]: expose a per-account channel reconnect (the watchdog already does it internally), and document `selfChatMode` — https://github.com/openclaw/openclaw/issues/127954
- #127634 [bug, maintainer, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] Plugin sessions.changed async fanout has no admission, backpressure, or service drain owner — https://github.com/openclaw/openclaw/issues/127634
- #127630 [bug, maintainer, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] sessions.preview and Talk materialize full transcripts before applying small output limits — https://github.com/openclaw/openclaw/issues/127630
- #127624 [bug, maintainer, P2, clawsweeper:no-new-fix-pr, clawsweeper:fix-shape-clear, clawsweeper:needs-maintainer-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:auth-provider, issue-rating: 🦞 diamond lobster] Managed OpenAI Chat Completions drops the provider-returned effective model — https://github.com/openclaw/openclaw/issues/127624
- #111405 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] Cron: agent runs that self-report ===DONE_ERR=== are recorded as ok — failureAlert never fires — https://github.com/openclaw/openclaw/issues/111405

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #128185 draft=False fix(crabbox): preserve Machine0 provisioning budget — https://github.com/openclaw/openclaw/pull/128185
- PR #128111 draft=False chore(ui): refresh control ui locales — https://github.com/openclaw/openclaw/pull/128111
- PR #126376 draft=False fix(ui): bound expanded tool activity panel — https://github.com/openclaw/openclaw/pull/126376
- PR #128503 draft=False fix(gateway): removed channel plugins remain falsely healthy after reload — https://github.com/openclaw/openclaw/pull/128503
- PR #101866 draft=False fix(sessions): ground assistant transcript media refs before replay — https://github.com/openclaw/openclaw/pull/101866
- PR #115933 draft=False fix: agent turn dies silently while waiting for an exec approval only someone else can grant — https://github.com/openclaw/openclaw/pull/115933
- PR #128414 draft=False chore: refresh dependencies after seven-day cooldown — https://github.com/openclaw/openclaw/pull/128414
- PR #122444 draft=False fix(cron): suggest canonical conversation targets — https://github.com/openclaw/openclaw/pull/122444
- PR #124301 draft=False improve(control-ui): restructure the composer as a multiline surface — https://github.com/openclaw/openclaw/pull/124301
- PR #128494 draft=False refactor(plugins)!: remove OpenProse — https://github.com/openclaw/openclaw/pull/128494
- PR #127226 draft=False feat(signal): link first account from setup QR — https://github.com/openclaw/openclaw/pull/127226
- PR #128502 draft=False fix(install): preserve Git command when npm verification fails — https://github.com/openclaw/openclaw/pull/128502
- PR #127224 draft=False feat(system-agent): present generic QR setup steps — https://github.com/openclaw/openclaw/pull/127224
- PR #120569 draft=False fix(ai): mark missing OpenAI Completions usage unavailable — https://github.com/openclaw/openclaw/pull/120569
- PR #123356 draft=False improve(control-ui): stage slash command arguments in the composer — https://github.com/openclaw/openclaw/pull/123356
- PR #128497 draft=False docs(nodes): clarify Mac node system commands — https://github.com/openclaw/openclaw/pull/128497
- PR #128459 draft=True perf(ci): split Telegram prerelease tests — https://github.com/openclaw/openclaw/pull/128459
- PR #120282 draft=False fix(diffs-language-pack): serve byte-accurate Content-Length on asset HEAD requests — https://github.com/openclaw/openclaw/pull/120282
- PR #111317 draft=False fix(msteams): token refresh hangs past deadline when DNS preflight stalls — https://github.com/openclaw/openclaw/pull/111317
- PR #125027 draft=True fix(ui): recover stale Control UI after gateway updates — https://github.com/openclaw/openclaw/pull/125027
- PR #128463 draft=True fix(ci): gate source package producers — https://github.com/openclaw/openclaw/pull/128463
- PR #128197 draft=False refactor(mantis): give Codex open-ended Telegram proof control — https://github.com/openclaw/openclaw/pull/128197
- PR #120230 draft=False fix(windows): preserve gateway restart CLI during Scheduled Task handoff — https://github.com/openclaw/openclaw/pull/120230
- PR #128397 draft=False fix(ui): terminal messages no longer reload the session roster — https://github.com/openclaw/openclaw/pull/128397
- PR #128244 draft=False fix(memory): do not block memory_search on dirty index sync — https://github.com/openclaw/openclaw/pull/128244
- PR #128501 draft=False fix(media): convert multi-frame HEIC and HEIF photos for image providers — https://github.com/openclaw/openclaw/pull/128501
- PR #128487 draft=False improve(irc): reuse transient connection for chunked sends — https://github.com/openclaw/openclaw/pull/128487
- PR #111125 draft=False fix(gateway): reject non-object MCP app tool arguments — https://github.com/openclaw/openclaw/pull/111125
- PR #128482 draft=False fix(ui): stop media prompts after leaving Appearance — https://github.com/openclaw/openclaw/pull/128482
- PR #121576 draft=False fix(text): only insert separator between word chars when stripping model tokens — https://github.com/openclaw/openclaw/pull/121576
