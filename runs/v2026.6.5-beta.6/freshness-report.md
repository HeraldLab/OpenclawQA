# Freshness Report

Target tag: `v2026.6.5-beta.6`

Target exists upstream: **yes**

Fetched at: `2026-06-09T09:00:36Z`

Latest beta tag: `v2026.6.5-beta.6`

Latest alpha tag: `v2026.6.9-alpha.1`

Stable baseline: `v2026.6.1`

Prior prerelease baseline: `v2026.6.5-beta.5`

## Recent issue signals

- #90911 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster, impact:other] [Feature]: Record token usage on task_runs / subagent_runs (parity with cron_run_logs.total_tokens) — https://github.com/openclaw/openclaw/issues/90911
- #91664 [bug, bug:behavior, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:session-state, impact:data-loss, issue-rating: 🐚 platinum hermit] [Bug]:  Dashboard session labels lost after gateway restart or Control UI reconnect — https://github.com/openclaw/openclaw/issues/91664
- #48003 [P1, clawsweeper:no-new-fix-pr, clawsweeper:source-repro, clawsweeper:linked-pr-open, impact:session-state, impact:message-loss, issue-rating: 🦞 diamond lobster] Steer mode does not inject messages mid-turn for main sessions — https://github.com/openclaw/openclaw/issues/48003
- #91016 [P1, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, impact:auth-provider, issue-rating: 🐚 platinum hermit] ⚠️ 升级 2026.6.1 后 DeepSeek Prompt Cache 完全失效，一小时烧掉约 $6 — https://github.com/openclaw/openclaw/issues/91016

## Recent PR signals

- PR #78441 draft=False feat(subagents): forward toolsAllow from sessions_spawn — https://github.com/openclaw/openclaw/pull/78441
- PR #91028 draft=True feat(lobster): in-process LLM adapters for embedded runner (#90909) — https://github.com/openclaw/openclaw/pull/91028
- PR #91657 draft=False fix(ollama): use provider thinking default in SDK session factory — https://github.com/openclaw/openclaw/pull/91657
- PR #91668 draft=False fix(agents): skip stale orphaned subagent sessions during restart recovery — https://github.com/openclaw/openclaw/pull/91668
- PR #85104 draft=False feat: fast talks auto mode — https://github.com/openclaw/openclaw/pull/85104
- PR #91438 draft=False feat(voice-call): Microsoft Teams provider — CVI voice/video calls — https://github.com/openclaw/openclaw/pull/91438
- PR #88709 draft=False fix(auth): cooldown inline api key billing failures — https://github.com/openclaw/openclaw/pull/88709
- PR #91667 draft=False fix(android): queue notification events until node connect — https://github.com/openclaw/openclaw/pull/91667
- PR #91478 draft=False block unauthorized Telegram DM text from prompt context — https://github.com/openclaw/openclaw/pull/91478
- PR #90500 draft=False Fix stale session routes for removed providers — https://github.com/openclaw/openclaw/pull/90500
- PR #91666 draft=False chore(deps): bump useblacksmith/setup-docker-builder from 1.8.0 to 1.9.0 in the actions group — https://github.com/openclaw/openclaw/pull/91666
- PR #91665 draft=False docs: fix release CI Android dispatch guidance — https://github.com/openclaw/openclaw/pull/91665
- PR #91663 draft=False fix(backup): clean up stale .tmp archives from interrupted runs before creating new backup — https://github.com/openclaw/openclaw/pull/91663
- PR #78715 draft=False Fix minor grammar issue in plugin documentation (capabilities plural) — https://github.com/openclaw/openclaw/pull/78715
- PR #90310 draft=False fix(openai-responses): sanitize null content before SDK serialization (#90094) — https://github.com/openclaw/openclaw/pull/90310
- PR #91658 draft=False feat(gateway): forward generic clientContext onto diagnostic events — https://github.com/openclaw/openclaw/pull/91658
- PR #90121 draft=False fix(memory): write dream fallback without subagent runtime — https://github.com/openclaw/openclaw/pull/90121
- PR #91644 draft=False feat(gateway): add OpenAI-compatible /v1/audio/speech endpoint — https://github.com/openclaw/openclaw/pull/91644
- PR #91653 draft=False fix(control-ui): wire ui.seamColor from bootstrap config to CSS variables — https://github.com/openclaw/openclaw/pull/91653
- PR #91648 draft=False [codex] Fix CLI plugin install hook bootstrap — https://github.com/openclaw/openclaw/pull/91648
- PR #91093 draft=False Feat/acp hub delegated sessions — https://github.com/openclaw/openclaw/pull/91093
- PR #91660 draft=False [AI] fix(memory): backfill provider.model with resolved model name in… — https://github.com/openclaw/openclaw/pull/91660
- PR #91661 draft=False chore(plugin-sdk): refresh API baseline hash — https://github.com/openclaw/openclaw/pull/91661
- PR #90782 draft=False perf(tui): prewarm runtime plugins before first send — https://github.com/openclaw/openclaw/pull/90782
- PR #72677 draft=False fix(cron): warn on main heartbeat handoff ghost runs — https://github.com/openclaw/openclaw/pull/72677
- PR #90960 draft=False fix(google): enable vertex image and video generation — https://github.com/openclaw/openclaw/pull/90960
- PR #87255 draft=False fix(config): skip .openclaw append when OPENCLAW_HOME already names a state dir (#45765) — https://github.com/openclaw/openclaw/pull/87255
- PR #91646 draft=False fix(browser): remove dead void requireRef in navigation registration — https://github.com/openclaw/openclaw/pull/91646
- PR #91656 draft=False test(cron): expand parseAbsoluteTimeMs test coverage to 39 cases — https://github.com/openclaw/openclaw/pull/91656
- PR #91345 draft=False fix: suggest close CLI commands — https://github.com/openclaw/openclaw/pull/91345
