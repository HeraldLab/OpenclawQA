# Release Context — OpenClaw `v2026.6.10-beta.2`

Fetched at: `2026-06-22T10:00:36Z`

## Target

- Target tag: `v2026.6.10-beta.2`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.10-beta.2
- Target tag SHA: 87b40c7160da1e9d470f86520f64ff1642a55b66

## Freshness baselines

- Latest beta tag: `v2026.6.10-beta.2`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.6.9`
- Prior prerelease baseline: `v2026.6.10-beta.1`

## Release notes excerpt

## 2026.6.10

### Highlights

- **Automatic fast mode for talks:** OpenClaw can enable fast mode for short conversational turns, then return to normal mode for longer runs with bounded fallback and delivery behavior. (#85104) Thanks @alexph-dev and @vincentkoc.
- **More reliable model routing:** Zai model synthesis, GLM overload failover, and native reasoning-level selection now follow the active model catalog more consistently. (#94461, #93241, #94067, #94136) Thanks @Pandah97, @chrysb, @0xghost42, @zhengli0922, @openperf, @civiltox, and @BorClaw.
- **Safer session and channel state:** channel switches reset stale origin fields, and cron delivery awareness stays attached to the target session. (#95328, #93580) Thanks @ZengWen-DT, @jalehman, @gorkem2020, and @scotthuang.
- **Trusted policies survive hook composition:** composed hook registries keep the trusted tool policies required by approval-sensitive flows. (#94545) Thanks @jesse-merhi.

### Changes

- **Agent and channel runtime:** fast-mode state now survives retries, fallback transitions, progress events, and embedded/CLI/ACP normalization; session and channel routing retain the current target and delivery context. (#85104, #93580, #95328) Thanks @alexph-dev, @vincentkoc, @scotthuang, @ZengWen-DT, @jalehman, and @gorkem2020.
- **Provider behavior:** model catalogs now supply the correct Zai base URL, overload classification, and native reasoning controls for live-discovered models. (#94461, #93241, #94067, #94136) Thanks @Pandah97, @chrysb, @0xghost42, @zhengli0922, @openperf, @civiltox, and @BorClaw.

### Fixes

- **Fast-mode and policy correctness:** fallback cutoffs and reset notices are bounded, repeated progress events remain visible, Codex service-tier state is normalized, and trusted policies are not lost when hook registries are composed. (#85104, #94545) Thanks @alexph-dev, @vincentkoc, and @jesse-merhi.
- **Model and delivery edge cases:** Zai and GLM failover paths use the right runtime metadata, while stale channel-origin state no longer leaks across session changes. (#94461, #93241, #95328) Thanks @Pandah97, @chrysb, @0xghost42, @zhengli0922, @ZengWen-DT, @jalehman, and @gorkem2020.

### Complete contribution record

This audited record covers the complete v2026.6.9..HEAD history: 11 merged PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

#### Pull requests

- **PR #86627** Keep core doctor health in contribution order. Thanks @giodl73-repo.
- **PR #93580** fix: preserve cron delivery awareness for target sessions. Thanks @scotthuang and @jalehman.
- **PR #95030** refactor: add SDK transcript identity target API. Thanks @jalehman.
- **PR #94838** refactor(copilot): complete harness lifecycle parity. Thanks @vincentkoc.
- **PR #95328** fix(sessions): reset stale per-channel origin fields on channel switch. Related #95325. Thanks @ZengWen-DT and @jalehman and @gorkem2020.
- **PR #94461** fix(zai): fall back to manifest baseUrl for synthesized GLM-5 models. Related #94269. Thanks @Pandah97 and @chrysb.
- **PR #93241** fix(agents): classify Zhipu GLM overload as overloaded for failover. Related #93211. Thanks @0xghost42 and @zhengli0922.
- **PR #94067** fix(channels): resolve native /think menu levels via runtime catalog for live-discovered models. Related #93835. Thanks @openperf and @civiltox.
- **PR #94136** fix(zai): expose GLM-5.2 reasoning levels [AI-assisted]. Thanks @BorClaw.
- **PR #85104** feat: fast talks auto mode. Related #85087. Thanks @alexph-dev.
- **PR #94545** fix: keep trusted policies with hook registry. Thanks @jesse-merhi.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.6.10-beta.2
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.6.10-beta.2.tgz
- integrity: `sha512-fOz52YzVw3MhQjQ5qqfPsfSbaMWOM62DNCxDsO/wZXvgvgrqPdZuNEPQokjFX9J7QXDeidl2uMBCnXRxynMzRg==`
- release SHA: `87b40c7160da1e9d470f86520f64ff1642a55b66`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.6.10-beta.2/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/27942155128
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/27938779493
- full release validation: https://github.com/openclaw/openclaw/actions/runs/27938779833
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/27942563340
- plugin ClawHub publish: https://github.com/openclaw/openclaw/actions/runs/27942565547
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/27943117132
- npm Telegram beta E2E: https://github.com/openclaw/openclaw/actions/runs/27941744910


## Recent issue risk signals

- No recent open issue signals returned.

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #84896 draft=False fix(memory): export LanceDB artifacts for wiki bridge — https://github.com/openclaw/openclaw/pull/84896
- PR #95301 draft=False fix: make post-turn compaction non-fatal — https://github.com/openclaw/openclaw/pull/95301
- PR #95728 draft=False docs: add Clawcks install option — https://github.com/openclaw/openclaw/pull/95728
- PR #95715 draft=False fix: preserve user model override during compaction — https://github.com/openclaw/openclaw/pull/95715
- PR #95153 draft=False [AI] fix(gateway): reuse active dashboard session key on reconnect — https://github.com/openclaw/openclaw/pull/95153
- PR #94915 draft=False fix(gateway): report draining state in readiness — https://github.com/openclaw/openclaw/pull/94915
- PR #94412 draft=False fix(agent-core): stop loop after aborted tool run — https://github.com/openclaw/openclaw/pull/94412
- PR #52664 draft=False feat: expose rawBody on user messages in plugin hook events — https://github.com/openclaw/openclaw/pull/52664
- PR #95602 draft=False test: save ~79 CI hours/mo in gateway session utils — https://github.com/openclaw/openclaw/pull/95602
- PR #79541 draft=False fix(acp): warm-restore active sessions on gateway start with PID-liveness guard — https://github.com/openclaw/openclaw/pull/79541
- PR #95485 draft=False fix(ui): roll values near 1M over from k to M in compact token format — https://github.com/openclaw/openclaw/pull/95485
- PR #79548 draft=False fix(acp): bind-aware persistent dispatcher for spawn-child outbound after parent ends — https://github.com/openclaw/openclaw/pull/79548
- PR #79540 draft=False fix(acp): capture and persist usage_update tokens for ACP sessions — https://github.com/openclaw/openclaw/pull/79540
- PR #88479 draft=False feat(ui): inline rename in the in-chat session picker — https://github.com/openclaw/openclaw/pull/88479
- PR #79536 draft=False fix(acp): honor tagVisibility.agent_thought_chunk for thought-stream events — https://github.com/openclaw/openclaw/pull/79536
- PR #79501 draft=False Add ambient initiative mode to heartbeat — https://github.com/openclaw/openclaw/pull/79501
- PR #79438 draft=False Reduce remote node bin probe churn — https://github.com/openclaw/openclaw/pull/79438
- PR #79405 draft=False fix: harden subagent completion fallback delivery — https://github.com/openclaw/openclaw/pull/79405
- PR #95691 draft=False fix(ui): bump dompurify to patched release — https://github.com/openclaw/openclaw/pull/95691
- PR #79401 draft=False feat(reply): emit structured runtime incidents — https://github.com/openclaw/openclaw/pull/79401
- PR #79342 draft=False Add anti-sycophancy stress fixture suite — https://github.com/openclaw/openclaw/pull/79342
- PR #79200 draft=False feat(cli): add --message-file flag to openclaw message send — https://github.com/openclaw/openclaw/pull/79200
- PR #79041 draft=False fix(webhooks): scope child task sessions — https://github.com/openclaw/openclaw/pull/79041
- PR #78958 draft=False fix(gateway): yield during embedded agent prep — https://github.com/openclaw/openclaw/pull/78958
- PR #78852 draft=False perf(agents): reuse media tool availability during tool prep — https://github.com/openclaw/openclaw/pull/78852
- PR #78747 draft=False fix(cache): emit `tools` before `input` in OpenAI Responses request body for prefix-cache stability — https://github.com/openclaw/openclaw/pull/78747
- PR #95700 draft=False feat(session): add named new and close chat commands — https://github.com/openclaw/openclaw/pull/95700
- PR #78715 draft=False Fix minor grammar issue in plugin documentation (capabilities plural) — https://github.com/openclaw/openclaw/pull/78715
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #78440 draft=False fix(memory-core): make dream narrative timeout configurable — https://github.com/openclaw/openclaw/pull/78440
