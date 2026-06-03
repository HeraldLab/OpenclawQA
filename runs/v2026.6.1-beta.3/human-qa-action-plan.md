# Human QA Action Plan — `v2026.6.1-beta.3`

Generated from current OpenclawQA issues and upstream OpenClaw issue signals.

## Current public QA receipts

| Issue | Tester | What it proves | Status | Human QA value | Next action |
|---|---|---|---|---|---|
| [#3](https://github.com/HeraldLab/OpenclawQA/issues/3) | Miriam / Windows 11 / Discord | Install/update, version proof, first response, Discord messaging, plugin visibility, safe failure, secrets check | submitted, needs review | Good Baseline P0 human evidence | Review evidence links; comment `EVIDENCE_CONFIRMED` or caveat/blocker |
| [#2](https://github.com/HeraldLab/OpenclawQA/issues/2) | Ayomide / Windows 11 / Telegram+Discord | Install, version, TUI response, Telegram response; Discord blocked; backup not done | submitted, blocked | Found a real human-visible channel problem | Ask for Discord evidence/logs; classify blocker; assign backup/restart follow-up |

## What beta 1/2/3 tell us

- **beta.1:** only public issue is [#1](https://github.com/HeraldLab/OpenclawQA/issues/1), a collector/dedupe workflow smoke. Useful for QA tooling, **not** human product QA.
- **beta.2:** no canonical OpenclawQA GitHub issue found. Miriam's beta.2 PDF/report existed outside GitHub and was blocked by LiteLLM budget. Value gap: external evidence must be converted into canonical issues.
- **beta.3:** two real human reports exist. This is where the process starts creating value: Miriam proves Windows+Discord P0; Ayomide exposes Discord delivery silence despite install/TUI/Telegram passing.

## Upstream release-risk issues to turn into delta scenarios

These are not all necessarily caused by beta.3, but they are current `2026.6.1` human-visible risks from upstream issues:

| Upstream issue | Risk area | Suggested delta priority | Human scenario |
|---|---|---|---|
| [openclaw#90007](https://github.com/openclaw/openclaw/issues/90007) | upgrade/plugin-state migration failure after upgrade from 2026.5.7 | Delta P0/P1 | Upgrade from older global install, run doctor, verify plugin state + one plugin action |
| [openclaw#89388](https://github.com/openclaw/openclaw/issues/89388) | inbound channel message silently delayed until watchdog | Delta P0/P1 | Send message to idle configured channel, wait for timely response, record delay/duplicate behavior |
| [openclaw#89278](https://github.com/openclaw/openclaw/issues/89278) | auth refresh timeout in cron/heartbeat | Delta P1 | Verify provider route/probe and one background/heartbeat run with OAuth-backed provider |
| [openclaw#89466](https://github.com/openclaw/openclaw/issues/89466) | Control UI input not cleared after sending | Delta P2 | Send Control UI message; verify input clears and duplicate resend risk is absent |
| [openclaw#89995](https://github.com/openclaw/openclaw/issues/89995) | duplicate completion messages after retry | Delta P1/P2 | Trigger long/background task completion; verify exactly one final message appears |

## Exact short cards to send now

### Miriam — evidence review + Core P1 addendum

Miriam already submitted Baseline P0. Do **not** ask her to rerun the full packet.

Ask for only:

1. Confirm the Drive evidence links are accessible.
2. If not already shown in video, add one screenshot/video for `openclaw models/status` or equivalent provider route proof.
3. Install/use one safe plugin, not just show plugin visibility.
4. Restart OpenClaw/gateway and confirm Discord still works.
5. Add a short human note: what was confusing, slow, or untrustworthy?

### Ayomide — Discord blocker + missing backup/restart

Ayomide already proved install/TUI/Telegram. Do **not** ask him to redo those.

Ask for only:

1. Record/send evidence of the Discord bot DM/thread where it stayed silent.
2. Include any pairing/setup screen or command output, redacting secrets.
3. Retry one Discord hello with unique marker after confirming bot/channel config.
4. Run backup or assigned backup/checkpoint flow if safe.
5. Restart OpenClaw and verify Telegram still works.
6. Say whether the Discord failure gave any visible recovery instruction.

### Remaining tester slot — migration/plugin-state delta

Assign one tester with an older OpenClaw install or safe disposable profile:

1. Start from older installed version if available.
2. Run backup.
3. Upgrade to current beta/release.
4. Run doctor.
5. Verify plugin list/state loads.
6. Install/use one safe plugin.
7. Restart and verify plugin state persists.
8. Report any `statement.columns is not a function` or migration warning.

### Remaining tester slot — channel latency/duplicate-response delta

Assign one tester with a real messaging channel:

1. Leave OpenClaw idle.
2. Send a unique marker in the channel.
3. Record from message send until reply.
4. Confirm reply arrives in the right place.
5. Confirm exactly one reply.
6. Send a follow-up.
7. Note latency and any silent period.
8. Report duplicates/delays as blocker/caveat.

## Status recommendation

`v2026.6.1-beta.3` is **not QA-complete yet** under the new human QA model.

It has useful human evidence, but still needs:

- evidence review verdict for Miriam [#3]
- blocker classification for Ayomide Discord [#2]
- Core P1 coverage: plugin install/use, restart/persistence, provider route proof
- at least one delta scenario from current upstream issue signals

Henry should not do this manually. The coordinator should send the short cards above, then bring back only blockers/waivers/final status.
