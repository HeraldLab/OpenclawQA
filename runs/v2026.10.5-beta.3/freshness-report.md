# Freshness Report

Target tag: `v2026.10.5-beta.3`

Target exists upstream: **yes**

Fetched at: `2026-10-13T10:01:07Z`

Latest beta tag: `v2026.10.5-beta.3`

Latest alpha tag: `v2026.6.21-alpha.1`

Stable baseline: `v2026.10.2`

Prior prerelease baseline: `v2026.10.5-beta.2`

## Recent issue signals

- #155859 [clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, impact:message-loss, impact:crash-loop, P0, issue-rating: 🦪 silver shellfish, impact:ux-release-blocker] [Bug]: Gateway startup wall-time scales with enabled plugin count on 2026.9.5; discord, codex and openclaw-weixin dominate the 120s publication budget — https://github.com/openclaw/openclaw/issues/155859
- #170866 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, impact:session-state, impact:message-loss, issue-rating: 🦪 silver shellfish] [Bug]: Telegram requester continuation has no final reply after model-runtime replacement refusal — https://github.com/openclaw/openclaw/issues/170866

## Recent PR signals

- PR #170929 draft=False feat(gateway): ready workers for empty-workspace cloud sessions — https://github.com/openclaw/openclaw/pull/170929
- PR #170712 draft=False refactor(sessions): activate memory-only incognito ownership — https://github.com/openclaw/openclaw/pull/170712
- PR #167796 draft=False refactor(automations): migrate periodic heartbeats and retire the executor — https://github.com/openclaw/openclaw/pull/167796
- PR #170853 draft=False fix(migrations): avoid string-limit failures on large transcript archives — https://github.com/openclaw/openclaw/pull/170853
- PR #170927 draft=True test(ui): stabilize sidebar roster refresh timing — https://github.com/openclaw/openclaw/pull/170927
- PR #170922 draft=False fix(core): remove unused runtime and test cache exports — https://github.com/openclaw/openclaw/pull/170922
- PR #170903 draft=False perf(sessions): reduce cold input reads and warm worktree lease contention — https://github.com/openclaw/openclaw/pull/170903
- PR #170842 draft=False perf(gateway): retain process-owned auth boot filesystem facts — https://github.com/openclaw/openclaw/pull/170842
- PR #170926 draft=False test(gateway): align recovery fixtures with run-owned notices — https://github.com/openclaw/openclaw/pull/170926
- PR #170898 draft=False fix(gateway): prevent worker failures from escaping cancelled history reads — https://github.com/openclaw/openclaw/pull/170898
- PR #170830 draft=False perf(agents): attribute turn preparation and repair final history once — https://github.com/openclaw/openclaw/pull/170830
- PR #170665 draft=False fix(gateway): keep terminal open deadline on the monotonic clock — https://github.com/openclaw/openclaw/pull/170665
- PR #160542 draft=False fix(tools): keep tools with JSON Schema examples available — https://github.com/openclaw/openclaw/pull/160542
- PR #170897 draft=False fix(update): prevent recursive workspace copies on Windows — https://github.com/openclaw/openclaw/pull/170897
- PR #170874 draft=False perf(cron): batch scheduled-run activation and reuse job state — https://github.com/openclaw/openclaw/pull/170874
- PR #129388 draft=False feat(continuation): context-pressure-aware continuation (continue_work / continue_delegate / request_compaction) — https://github.com/openclaw/openclaw/pull/129388
- PR #170924 draft=False fix(crabbox): new cloud workers keep failing when a warm image's checkpoint is gone — https://github.com/openclaw/openclaw/pull/170924
- PR #170925 draft=False fix(agents): stop retrying rejected empty replies — https://github.com/openclaw/openclaw/pull/170925
- PR #147027 draft=False feat(clickclack): answer ask_user from native ClickClack question cards — https://github.com/openclaw/openclaw/pull/147027
- PR #96291 draft=False [codex] Bound memory flush append payloads — https://github.com/openclaw/openclaw/pull/96291
- PR #170860 draft=False perf(runtime): reuse prepared facts in hot helpers — https://github.com/openclaw/openclaw/pull/170860
- PR #170923 draft=True docs: clarify product direction in VISION.md — https://github.com/openclaw/openclaw/pull/170923
- PR #169757 draft=False perf(sessions): move target lookups and callers to workers — https://github.com/openclaw/openclaw/pull/169757
- PR #160567 draft=False fix(llm): apply stream payload patches to replacement payloads — https://github.com/openclaw/openclaw/pull/160567
- PR #98662 draft=False fix(models): add provider request rate limits — https://github.com/openclaw/openclaw/pull/98662
- PR #142552 draft=False fix(telegram): include duration in voice and audio uploads — https://github.com/openclaw/openclaw/pull/142552
- PR #170911 draft=False feat(mcp): let trusted hosts attach protected request metadata — https://github.com/openclaw/openclaw/pull/170911
- PR #170917 draft=False refactor(ui): replace cron Web Awesome menus — https://github.com/openclaw/openclaw/pull/170917
- PR #170757 draft=False fix(agents): keep committed CLI replies successful — https://github.com/openclaw/openclaw/pull/170757
- PR #164415 draft=False fix(workboard): resume after checkout loss — https://github.com/openclaw/openclaw/pull/164415
