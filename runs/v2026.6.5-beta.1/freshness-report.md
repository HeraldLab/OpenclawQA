# Freshness Report

Target tag: `v2026.6.5-beta.1`

Target exists upstream: **yes**

Fetched at: `2026-06-06T04:00:11Z`

Latest beta tag: `v2026.6.5-beta.1`

Latest alpha tag: `v2026.6.6-alpha.1`

Stable baseline: `v2026.6.1`

Prior prerelease baseline: `v2026.6.2-beta.1`

## Recent issue signals

- #90835 [P3, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, issue-rating: 🌊 off-meta tidepool] Docs feedback: /platforms/ios — https://github.com/openclaw/openclaw/issues/90835
- #89830 [P1, clawsweeper:fix-shape-clear, clawsweeper:queueable-fix, clawsweeper:source-repro, impact:message-loss, issue-rating: 🦞 diamond lobster] iMessage channel jams: valid JSON-RPC `imsg` response is split by Node readline on U+2028, every fragment fails JSON.parse — https://github.com/openclaw/openclaw/issues/89830
- #90810 [no-labels] [Bug]: Prompt cache invalidated on every user turn on full-resend transports — transient timestamp + content-form decoration on the current user message (regression from #3658) — https://github.com/openclaw/openclaw/issues/90810

## Recent PR signals

- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #85155 draft=False fix(agents): avoid inviting provider swaps in model alias guidance — https://github.com/openclaw/openclaw/pull/85155
- PR #82148 draft=False feat(agents): allow spawn fast mode overrides — https://github.com/openclaw/openclaw/pull/82148
- PR #90793 draft=False Fix OpenAI audio auth to use API keys — https://github.com/openclaw/openclaw/pull/90793
- PR #90837 draft=False fix(telegram): suppress internal tool warnings in groups — https://github.com/openclaw/openclaw/pull/90837
- PR #90836 draft=False fix(cron): block self-narrating auto-announce replies — https://github.com/openclaw/openclaw/pull/90836
- PR #90480 draft=False feat(whatsapp): expand live QA coverage — https://github.com/openclaw/openclaw/pull/90480
- PR #90811 draft=False fix(agents): stabilize user-turn serialization across turns to preserve prompt cache — https://github.com/openclaw/openclaw/pull/90811
- PR #90839 draft=False fix(memory-core): exclude soft-deleted .jsonl.deleted paths from dreaming corpus (#90466) — https://github.com/openclaw/openclaw/pull/90839
- PR #90328 draft=False Expose model picker agent runtimes — https://github.com/openclaw/openclaw/pull/90328
- PR #90791 draft=False fix(doctor): prevent repeat talk normalization from derived speakerVoice fallback (fixes #90446) — https://github.com/openclaw/openclaw/pull/90791
- PR #74235 draft=False fix(googlechat): preserve thread reply target through delivery — https://github.com/openclaw/openclaw/pull/74235
- PR #88796 draft=False fix(discord): resolve guildId from session channel for search actions — https://github.com/openclaw/openclaw/pull/88796
- PR #90838 draft=False fix(config): warn for retired skill-workshop plugin entry instead of failing validation (#90244) — https://github.com/openclaw/openclaw/pull/90838
- PR #90695 draft=False fix(agents): handle max_turns stop reason and improve retry-limit error context (fixes #78145) — https://github.com/openclaw/openclaw/pull/90695
- PR #90834 draft=False fix(matrix): guard against missing channel.inbound runtime (#90325) — https://github.com/openclaw/openclaw/pull/90834
- PR #88690 draft=False Emit sessions.changed for in-chat command metadata — https://github.com/openclaw/openclaw/pull/88690
- PR #90821 draft=False fix(compact): make /compact command cancelable via abortEmbeddedAgentRun — https://github.com/openclaw/openclaw/pull/90821
- PR #89514 draft=False fix(doctor): exclude platform-incompatible skills from missing requirements — https://github.com/openclaw/openclaw/pull/89514
- PR #90812 draft=False fix(voice-call): preserve live Twilio streams in stale reaper — https://github.com/openclaw/openclaw/pull/90812
- PR #90817 draft=False fix(agents): apply stale-run liveness check to aborted subagent orphan recovery — https://github.com/openclaw/openclaw/pull/90817
- PR #90579 draft=False fix: allow trusted host-read html after outbound staging — https://github.com/openclaw/openclaw/pull/90579
- PR #90051 draft=False fix(agents): strip reasoning tags from chat replies — https://github.com/openclaw/openclaw/pull/90051
- PR #90790 draft=False fix(codex): preserve completed replies after client close — https://github.com/openclaw/openclaw/pull/90790
- PR #88245 draft=False refactor(whatsapp): introduce inbound message contexts — https://github.com/openclaw/openclaw/pull/88245
- PR #89949 draft=False fix(announce-delivery): backfill effectiveDirectOrigin.to from requester session entry — https://github.com/openclaw/openclaw/pull/89949
- PR #90798 draft=False fix(agents): materialize sandbox skills for rw sandboxes — https://github.com/openclaw/openclaw/pull/90798
- PR #90805 draft=True fix(codex): fail closed on missing native hook relay delivery — https://github.com/openclaw/openclaw/pull/90805
- PR #90833 draft=False feat(control-ui): allow renaming sessions in sidebar (#90655) — https://github.com/openclaw/openclaw/pull/90833
- PR #90832 draft=False fix(gateway): surface in-progress assistant response on session reconnect — https://github.com/openclaw/openclaw/pull/90832
