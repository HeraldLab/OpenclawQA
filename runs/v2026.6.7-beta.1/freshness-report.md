# Freshness Report

Target tag: `v2026.6.7-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-06-15T06:19:27Z`

Latest beta tag: `v2026.6.8-beta.1`

Latest alpha tag: `v2026.6.10-alpha.2`

Stable baseline: `v2026.6.6`

Prior prerelease baseline: `v2026.6.8-beta.1`

## Recent issue signals

- #71211 [security, P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-security-review, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:security, issue-rating: 🦞 diamond lobster] Security: exec tool returns raw stdout/stderr to agent without secret redaction — https://github.com/openclaw/openclaw/issues/71211
- #90588 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-live-repro, impact:message-loss, impact:auth-provider, impact:crash-loop, issue-rating: 🐚 platinum hermit] [Bug] v2026.5.28 ~ v2026.6.1: All QQ Bot agents unresponsive — Cannot read properties of undefined (reading 'run') — https://github.com/openclaw/openclaw/issues/90588
- #54578 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, impact:session-state, issue-rating: 🌊 off-meta tidepool] Add tree view command to visualize active agents — https://github.com/openclaw/openclaw/issues/54578
- #54373 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, clawsweeper:linked-pr-open, impact:session-state, issue-rating: 🌊 off-meta tidepool] [RFC] Context Provenance: Add source/volatility metadata to injected context segments — https://github.com/openclaw/openclaw/issues/54373

## Recent PR signals

- PR #92428 draft=False fix(qqbot): keep markdown table chunks valid — https://github.com/openclaw/openclaw/pull/92428
- PR #93187 draft=False fix(memory-core): exclude archive transcripts from dreaming corpus and propagate cron parentage to subagents — https://github.com/openclaw/openclaw/pull/93187
- PR #78664 draft=False perf(agents): cache provider tool schema normalization — https://github.com/openclaw/openclaw/pull/78664
- PR #93188 draft=False test(macos): cover root CLI command parsing — https://github.com/openclaw/openclaw/pull/93188
- PR #93184 draft=False fix(ui): preserve live tool stream order — https://github.com/openclaw/openclaw/pull/93184
- PR #93149 draft=False feat(cron): add add dry-run preview — https://github.com/openclaw/openclaw/pull/93149
- PR #69199 draft=False fix(memory): improve error message when node:sqlite is unavailable — https://github.com/openclaw/openclaw/pull/69199
- PR #70046 draft=False fix(cron): support HH:MM time-only strings in --at; apply --tz to time-only input — https://github.com/openclaw/openclaw/pull/70046
- PR #92680 draft=False feat(read): add encoding parameter for GBK and non-UTF-8 text files (#92664) — https://github.com/openclaw/openclaw/pull/92680
- PR #93186 draft=False fix(cache): stable tool result aggregate truncation — https://github.com/openclaw/openclaw/pull/93186
- PR #45901 draft=False security: create session dirs with private permissions — https://github.com/openclaw/openclaw/pull/45901
- PR #93151 draft=False #92664: fix(read): decode GBK-encoded files on Chinese Windows via existing decoder — https://github.com/openclaw/openclaw/pull/93151
- PR #93185 draft=False [codex] fix(telegram): drop unused rich markdown parameter — https://github.com/openclaw/openclaw/pull/93185
- PR #84896 draft=False fix(memory): export LanceDB artifacts for wiki bridge — https://github.com/openclaw/openclaw/pull/84896
- PR #93174 draft=False test: fold channel message flows into qa e2e — https://github.com/openclaw/openclaw/pull/93174
- PR #88750 draft=False feat(context-engine): pass runtime settings into lifecycle — https://github.com/openclaw/openclaw/pull/88750
- PR #87739 draft=False Telegram: keep long DM turns alive through progress previews — https://github.com/openclaw/openclaw/pull/87739
- PR #75066 draft=False fix(sessions): preserve activity for compaction metadata — https://github.com/openclaw/openclaw/pull/75066
- PR #74954 draft=False fix(agents): prevent provider defaultModel from overriding agents.defaults.model (fixes #24170) — https://github.com/openclaw/openclaw/pull/74954
- PR #47604 draft=False feat(android): add Wear OS app MVP — https://github.com/openclaw/openclaw/pull/47604
- PR #93179 draft=False excludeTestExecution option for more compact QA profile evidence — https://github.com/openclaw/openclaw/pull/93179
- PR #93183 draft=True [codex] Fix /btw Codex runtime side-question routing — https://github.com/openclaw/openclaw/pull/93183
- PR #93175 draft=False Add smoke-ci primary scorecard evidence — https://github.com/openclaw/openclaw/pull/93175
- PR #91193 draft=False fix(cli): document Commander rawArgs internal API dependency in action-reparse.ts — https://github.com/openclaw/openclaw/pull/91193
- PR #91192 draft=False fix(tts): allow trusted local media in message_tool_only mode — https://github.com/openclaw/openclaw/pull/91192
- PR #91180 draft=False feat(whatsapp): support opt-in group-name config — https://github.com/openclaw/openclaw/pull/91180
- PR #91177 draft=False fix(tui): persist canonical provider in session modelProvider — https://github.com/openclaw/openclaw/pull/91177
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #91162 draft=False fix(cron): honor configured delivery.channel instead of misrouting (#46899) — https://github.com/openclaw/openclaw/pull/91162
- PR #91161 draft=False fix: prevent A2A target from reverse-calling sessions_send to requester (#39476) — https://github.com/openclaw/openclaw/pull/91161
