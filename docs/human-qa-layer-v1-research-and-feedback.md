# Human QA Layer — Problem, V1, Research, and Tester Feedback

This document is for Herald Labs / OpenClaw human testers.

The goal is not to give testers a giant process document. The goal is to explain **why** we are changing the QA process, what we tried first, what we learned from official OpenClaw issues, and where testers can help us improve the process.

## 1. The problem we are trying to solve

OpenClaw already has a strong engineering culture around automated tests, CI, scripts, and agent-assisted checks.

That is useful, but it does not solve the whole release-quality problem.

The gap is **human QA**:

- Does install/update feel clear to a normal user?
- Does the bot actually reply in the expected Discord/Telegram/WhatsApp/Feishu channel?
- Does the reply arrive promptly, once, and in the right place?
- Does a plugin install and work in a real user setup?
- Does an error message explain what to do next?
- Does the UI feel trustworthy, or does it look stuck/broken/confusing?
- Does OpenClaw say “success” when nothing visible happened?

Automated tests can say “the code path passed.”

Human QA answers a different question:

> Would a real user trust this release after using it?

That is the layer Herald Labs is trying to provide.

## 2. What V1 of the process said

The first version of our process was simple:

1. Every release should get baseline manual QA.
2. Testers should check install/update, version proof, first response, channel delivery, plugin/tool visibility, harmless failure handling, and secrets safety.
3. Release-specific tests should be added from the release changes.
4. Testers should submit evidence through GitHub issues.
5. Evidence should be reviewed before a report counts as accepted.

In short, V1 said:

> “Please manually test the release and submit evidence.”

That was directionally right.

## 3. What V1 got right

V1 caught the right principle:

> Human QA is not more automation. Human QA is humans testing real flows and judging the experience.

It also gave us a useful baseline:

- install/update
- version/tag/commit proof
- first useful response
- one real channel working end-to-end
- plugin/tool visibility
- safe failure and recovery clarity
- no obvious secret exposure
- no silent false success

Those checks should stay.

## 4. What V1 did not solve well enough

V1 was still too generic.

A tester could reasonably ask:

- “Why these checks?”
- “Which 6–8 things should I personally test?”
- “How do I know what matters for this release?”
- “Should I just redo the same smoke test every time?”
- “Where can my human judgment actually add value?”

That is the mistake we are correcting.

The new process should not ask every tester to run a giant checklist.

Instead, every tester should receive a **small QA card** generated from:

1. the universal baseline,
2. the tester’s actual setup,
3. official OpenClaw issue patterns,
4. what changed in the release.

## 5. Research from official OpenClaw issues

We reviewed official `openclaw/openclaw` issues around the `2026.6.1` beta/release window.

The important finding: many reported problems are not “unit test failed” problems. They are human-visible experience problems.

### Messaging and channel reliability

Official issue examples:

- [openclaw#89388](https://github.com/openclaw/openclaw/issues/89388): inbound WhatsApp message not delivered to idle warm process; response waits for watchdog and arrives late.
- [openclaw#89455](https://github.com/openclaw/openclaw/issues/89455): Feishu DM dispatch failure.
- [openclaw#66657](https://github.com/openclaw/openclaw/issues/66657): Feishu group messages with empty content crash dispatch.
- [openclaw#89995](https://github.com/openclaw/openclaw/issues/89995): subagent completion announce retries after message already delivered, causing duplicate messages.
- [openclaw#89189](https://github.com/openclaw/openclaw/issues/89189): Discord reconnect storm can exhaust host ports.

Human QA value:

- A tester can tell us whether a message actually arrives.
- A tester can catch silence, delay, duplicate replies, wrong-thread replies, and confusing recovery.

### Provider, auth, and model routing

Official issue examples:

- [openclaw#89278](https://github.com/openclaw/openclaw/issues/89278): Codex OAuth probe succeeds, but cron/heartbeat fails with a 10s auth refresh timeout.
- [openclaw#89551](https://github.com/openclaw/openclaw/issues/89551): session-memory hook model config ignored for LLM slug generation.
- [openclaw#89193](https://github.com/openclaw/openclaw/issues/89193): MiniMax OAuth configuration failure.

Human QA value:

- A tester can verify whether the configured route works in actual use, not only whether a status command says it is usable.
- A tester can notice if OpenClaw silently falls back to an unexpected route or gives an unclear auth error.

### Plugin, migration, and update risk

Official issue examples:

- [openclaw#90007](https://github.com/openclaw/openclaw/issues/90007): upgrade to `2026.6.1` breaks plugin install index and task/flow migrations with `statement.columns is not a function`.
- [openclaw#89609](https://github.com/openclaw/openclaw/issues/89609): `openclaw migrate codex` cannot discover globally installed plugin providers.
- [openclaw#90000](https://github.com/openclaw/openclaw/issues/90000): WhatsApp plugin incompatible with latest release.

Human QA value:

- A tester can run a real upgrade path, run doctor, install/use a plugin, restart, and judge whether recovery is understandable.

### Control UI and user trust

Official issue examples:

- [openclaw#89466](https://github.com/openclaw/openclaw/issues/89466): Control UI chat input not cleared after sending.
- [openclaw#89542](https://github.com/openclaw/openclaw/issues/89542): audio attachment shows “message too large” until manual refresh.
- [openclaw#89662](https://github.com/openclaw/openclaw/issues/89662): context indicator disappears or count mismatches.
- [openclaw#89249](https://github.com/openclaw/openclaw/issues/89249): session picker becomes un-navigable with many spawned sessions.
- [openclaw#89709](https://github.com/openclaw/openclaw/issues/89709): dashboard usage shows historical cumulative data instead of daily usage.

Human QA value:

- A tester can say whether the product looks stuck, misleading, or untrustworthy, even if the backend technically returned something.

## 6. Where testers are most valuable

Testers are most valuable where automation has weak judgment:

| Area | What testers should look for |
|---|---|
| Messaging | silence, delay, duplicate replies, wrong channel/thread, unclear pairing/setup |
| Install/update | unclear instructions, failed doctor, broken migration, confusing recovery |
| Plugins/tools | tool missing, plugin visible but unusable, install works but state breaks after restart |
| Provider/auth | status says OK but real turn fails, fallback route unclear, auth error not actionable |
| UI/session | stuck state, stale text, bad counts, confusing session picker, misleading success |
| Evidence/trust | “Would I trust this as a user?” and “Did I have to guess what to do?” |

## 7. How tester QA cards should be generated

A tester should not need to invent the whole checklist.

The coordinator should generate a small card using this formula:

```text
Tester QA card =
  3 fixed baseline checks
+ 2 checks based on the tester’s setup
+ 2 checks based on official issue patterns / release risk
+ 1 human judgment and evidence check
```

### The 3 fixed baseline checks

Every tester card should usually include:

1. Install/update to the target release.
2. Show version/tag/commit proof.
3. Get one normal useful OpenClaw response.

### The 2 setup-specific checks

Pick based on what the tester actually uses:

- Discord
- Telegram
- WhatsApp
- Feishu
- Control UI
- TUI/CLI
- plugin install/use
- provider/model route
- restart/persistence
- backup/restore

### The 2 issue-pattern checks

Pick from the official issue patterns above.

Examples:

- If official issues show delayed messages, run an idle-channel response test.
- If official issues show duplicate replies, run a long/background completion test.
- If official issues show plugin migration failures, run upgrade + doctor + plugin-use.
- If official issues show UI state confusion, run Control UI send/media/session-picker checks.
- If official issues show auth/provider timeouts, run provider proof + a real background/cron-style turn.

### The 1 human judgment/evidence check

Always include:

8. Submit evidence and answer:

- What was confusing?
- Did anything silently fail?
- Did anything duplicate or arrive late?
- Would you trust this flow as a normal user?
- Did the evidence expose any secrets?

## 8. Example cards

### Example: Windows + Discord tester

```text
1. Install/update to the target release.
2. Show OpenClaw version/tag/commit.
3. Get one normal response in TUI/CLI.
4. Send a unique marker in Discord and confirm the reply lands in the same channel/thread.
5. Show plugin/tool visibility.
6. Idle-channel test: leave OpenClaw idle, send a message, record whether reply arrives promptly and exactly once.
7. Plugin/update test: run doctor, install/use one safe plugin, restart, confirm plugin state still works.
8. Submit evidence plus confusion/trust notes.
```

### Example: Control UI tester

```text
1. Install/update to the target release.
2. Show OpenClaw version/tag/commit.
3. Get one normal response in Control UI.
4. Send a message and confirm the input clears after sending.
5. Open/switch sessions and confirm the session picker remains usable.
6. If media/audio is available, confirm attachment renders without manual refresh.
7. Confirm context/status indicators are not misleading after a message.
8. Submit evidence plus confusion/trust notes.
```

### Example: Plugin/migration tester

```text
1. Start from an older install or a safe disposable profile.
2. Create a backup if available.
3. Upgrade to the target release.
4. Run doctor/status.
5. Show plugin/tool visibility.
6. Install/use one safe plugin.
7. Restart and confirm plugin state persists.
8. Submit evidence plus any migration warnings/errors.
```

## 9. What we want testers to help improve

We want tester feedback on the QA process itself.

Please tell us:

1. Which checks were useful?
2. Which checks felt like busywork?
3. Which instructions were unclear?
4. Which real user flow should we add?
5. Which issue pattern should become a standard human QA card?
6. What evidence is realistic for you to collect?
7. Where did you need maintainer help?
8. What would make this easier for future testers?

## 10. Working proposal for V2

For the next release, the process should be:

1. Coordinator reviews official `openclaw/openclaw` issues and release changes.
2. Coordinator groups risks into clusters: messaging, auth/provider, plugin/migration, UI/session, security/secrets, performance/recovery.
3. Coordinator sends each tester a small QA card, not a giant checklist.
4. Tester manually runs the card and submits evidence.
5. Reviewer checks evidence before the report counts.
6. Confirmed findings are linked back to official OpenClaw issues or filed upstream.
7. Closeout says what humans actually proved, what remains untested, and what should improve next.

## 11. Bottom line

The purpose of Herald Labs human QA is not to duplicate OpenClaw automation.

The purpose is to answer:

> Does this release work for real people, in real channels, with real plugins, real auth, real UI, and understandable recovery when something goes wrong?

If the answer is unclear, confusing, or untrusted, that is valuable QA feedback — even when no automated test fails.
