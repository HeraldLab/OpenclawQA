# Freshness Report

Target tag: `v2026.6.1-beta.3`

Target exists upstream: **yes**

Fetched at: `2026-06-03T09:30:35Z`

Latest beta tag: `v2026.6.1-beta.3`

Latest alpha tag: `v2026.6.3-alpha.1`

Stable baseline: `v2026.5.28`

Prior prerelease baseline: `v2026.6.1-beta.2`

## Recent issue signals

- #89774 [no-labels] Feature: toggle to show subagent / spawnedBy sessions in chat-view session switcher — https://github.com/openclaw/openclaw/issues/89774
- #89773 [no-labels] session_status with current sessionKey resolves to wrong session in webchat — https://github.com/openclaw/openclaw/issues/89773
- #89766 [P1, clawsweeper:needs-live-repro, impact:session-state, impact:crash-loop, issue-rating: 🐚 platinum hermit] Isolated cron lanes leak on claude-cli backend: queued_work_without_active_run → release_lane released=0, lanes accumulate until restart — https://github.com/openclaw/openclaw/issues/89766
- #84139 [P2, clawsweeper:needs-live-repro, impact:session-state, impact:message-loss, issue-rating: 🐚 platinum hermit] [2026.5.18] Compaction safeguard causes duplicate messages on sessions_send interactions — https://github.com/openclaw/openclaw/issues/84139

## Recent PR signals

- PR #89613 draft=False docs: document auth profile failure policy contract — https://github.com/openclaw/openclaw/pull/89613
- PR #66000 draft=False fix(cli): clear conflicting OPENCLAW_LAUNCHD_LABEL when --profile is provided — https://github.com/openclaw/openclaw/pull/66000
- PR #89768 draft=False fix(mattermost): merge progress preview lines by identity instead of full overwrite — https://github.com/openclaw/openclaw/pull/89768
- PR #89776 draft=False fix(status): render sub-1000 token counts as plain integers in formatKTokens — https://github.com/openclaw/openclaw/pull/89776
- PR #89548 draft=False fix(agents): classify read-only shell commands as non-mutating — https://github.com/openclaw/openclaw/pull/89548
- PR #89775 draft=True fix(plugins): guard codex app extension factories — https://github.com/openclaw/openclaw/pull/89775
- PR #89729 draft=False fix: skip Responses item id replay when store support is stripped — https://github.com/openclaw/openclaw/pull/89729
- PR #89719 draft=False fix(cron): prune isolated-target cron sessions in session reaper — https://github.com/openclaw/openclaw/pull/89719
- PR #86900 draft=False fix(compaction): add circuit breaker to stop token burn when summarizer unavailable — https://github.com/openclaw/openclaw/pull/86900
- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #87696 draft=False fix(cli): load plugins for openclaw sandbox so OpenShell backend reports live status (#59528) — https://github.com/openclaw/openclaw/pull/87696
- PR #89488 draft=False fix: stabilize Anthropic cache marker through tool loops — https://github.com/openclaw/openclaw/pull/89488
- PR #89769 draft=True fix(agents): guard tool inventory metadata — https://github.com/openclaw/openclaw/pull/89769
- PR #78395 draft=False fix(agents): resolve bare alias fallbacks via alias index — https://github.com/openclaw/openclaw/pull/78395
- PR #78172 draft=False feat(tts): add skipEmojiSymbols option to prevent TTS from reading emoji/symbols — https://github.com/openclaw/openclaw/pull/78172
- PR #89724 draft=False feat(voice-call): add Microsoft Teams voice provider (OpenClawTeamsBridge) — https://github.com/openclaw/openclaw/pull/89724
- PR #89772 draft=False fix(webchat): keep context indicator visible with stale token data — https://github.com/openclaw/openclaw/pull/89772
- PR #89629 draft=False feat(hooks): per-turn usageState (provider limits + rich atoms) on reply_payload_sending — https://github.com/openclaw/openclaw/pull/89629
- PR #89770 draft=False fix(agents): fall back to direct channel send when ACP subagent announce loses gateway scope — https://github.com/openclaw/openclaw/pull/89770
- PR #89767 draft=True fix(skills): route installs to requested agent workspace [AI-assisted] — https://github.com/openclaw/openclaw/pull/89767
- PR #89764 draft=False fix(feishu): notify user when media download fails due to size limit — https://github.com/openclaw/openclaw/pull/89764
- PR #78664 draft=False perf(agents): cache provider tool schema normalization — https://github.com/openclaw/openclaw/pull/78664
- PR #86526 draft=False fix(openai): allow RFC 2544 fake-IP range for Realtime session requests — https://github.com/openclaw/openclaw/pull/86526
- PR #88968 draft=False fix: prevent memory flush failure from aborting user reply (#85645) — https://github.com/openclaw/openclaw/pull/88968
- PR #89765 draft=True fix(plugins): guard tool result middleware metadata — https://github.com/openclaw/openclaw/pull/89765
- PR #89763 draft=True fix(gateway): guard plugin session action dispatch — https://github.com/openclaw/openclaw/pull/89763
- PR #81260 draft=False fix(progress-draft): only trigger onToolStart on phase=start to remove duplicate tool lines — https://github.com/openclaw/openclaw/pull/81260
- PR #89752 draft=False fix(sessions): make transcript migration rewrite atomic — https://github.com/openclaw/openclaw/pull/89752
- PR #88159 draft=False fix(cli): retry logs.tail after journal fallback in logs follow — https://github.com/openclaw/openclaw/pull/88159
- PR #89454 draft=False fix(feishu): resolve exec/keychain appSecret SecretRefs on the outbound path — https://github.com/openclaw/openclaw/pull/89454
