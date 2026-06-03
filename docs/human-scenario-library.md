# OpenClaw Human QA Scenario Library

This library gives QA coordinators concrete human scenarios to include in release packets. Pick the scenarios that match the release commits and tester environment. Do not send this whole file blindly; build a focused plan from it.

Each scenario is designed for a human tester. Agents may assist with setup and logging, but the tester must manually observe whether OpenClaw behaves correctly and whether the experience is understandable.

## Scenario card format

Each tester-facing scenario should include:

- **User goal** — what a normal user is trying to accomplish.
- **Starting state** — OS, channel, provider, existing config, account state.
- **Manual steps** — what the human does.
- **Expected visible behavior** — what success looks like.
- **Failure/confusion signs** — what to watch for.
- **Evidence required** — screen recording timestamps, screenshots, logs.
- **Human judgment** — would the tester trust/use this flow?

---

# A. Messaging Channels

## A1. Discord thread reply routing

**User goal:** Ask OpenClaw for help inside a Discord thread and receive exactly one useful reply in that same thread.

**Starting state:**
- OpenClaw installed and configured.
- Discord integration enabled.
- Tester has an assigned public Discord thread.

**Manual steps:**
1. Start screen recording.
2. Open the assigned Discord thread.
3. Send: `OpenClaw beta test <timestamp>: reply in this thread with one short checklist of what you can do.`
4. Wait up to 2 minutes.
5. Observe where the reply lands.
6. Send a follow-up in the same thread: `Now summarize your previous reply in one sentence.`
7. Observe whether OpenClaw keeps context.

**Expected visible behavior:**
- Reply appears in the same thread, not the parent channel or a DM.
- Exactly one reply per user message.
- Reply identity is expected bot/account.
- Follow-up uses thread context.
- No duplicate, stale, or cross-thread response.

**Failure/confusion signs:**
- No reply and no clear error.
- Reply in wrong channel/thread.
- Duplicate replies.
- Bot replies to itself or loops.
- Context lost between first and second message.
- Permissions look fine but delivery fails silently.

**Evidence required:**
- Video from before first send through second reply/failure.
- Screenshot of Discord thread after test.
- OpenClaw status/log snippet only if delivery fails.

**Human judgment:**
Would you trust this bot to operate in a customer/community Discord thread? If not, why?

## A2. Discord parent channel vs thread isolation

**User goal:** Confirm OpenClaw does not leak a thread conversation into the parent channel or another thread.

**Manual steps:**
1. Open assigned thread and parent channel side by side if possible.
2. Send a unique marker in the thread: `thread-isolation-<timestamp>`.
3. Confirm reply location.
4. Check parent channel and nearby threads for stray replies.

**Expected visible behavior:**
- Only the assigned thread receives the reply.
- Parent channel stays clean.
- No unrelated thread receives output.

**Failure/confusion signs:**
- Reply lands outside the thread.
- Duplicate in parent + thread.
- Tester cannot tell which conversation OpenClaw is answering.

**Evidence required:**
- Video showing thread and parent channel check.
- Screenshot of reply location.

## A3. Discord error recovery when bot cannot reply

**User goal:** Understand what happens when Discord delivery is blocked or permissions are wrong.

**Manual steps:**
1. If safe and assigned, remove/restrict a permission or use a known restricted test thread/channel.
2. Ask OpenClaw to reply in that surface.
3. Observe user-facing error/log output.
4. Restore permission if changed.

**Expected visible behavior:**
- OpenClaw reports a clear delivery/permission issue.
- Error identifies the channel/thread and likely fix.
- No misleading schema/model/tool error.

**Failure/confusion signs:**
- Silent failure.
- Misleading provider/model error.
- Retry loop or duplicate attempts.
- Error includes token/secret.

**Evidence required:**
- Video of blocked attempt and recovery.
- Redacted logs if available.

## A4. Telegram DM or group delivery

**User goal:** Confirm Telegram messages reach the expected chat and preserve context.

**Manual steps:**
1. Open the assigned Telegram DM/group.
2. Send marker: `telegram-route-<timestamp>`.
3. Ask OpenClaw for a short response.
4. Send a follow-up question.
5. Observe reply location, identity, delay, and context retention.

**Expected visible behavior:**
- Reply arrives in same Telegram chat.
- Follow-up retains context.
- No duplicate or delayed stale response.

**Failure/confusion signs:**
- Reply in wrong chat.
- Bot cannot distinguish group vs DM.
- No reply despite message being visible.
- Context reset unexpectedly.

**Evidence required:**
- Screen recording.
- Screenshot of final Telegram chat.
- Logs only if blocked.

## A5. Media/file attachment delivery

**User goal:** Send or receive an attachment through the configured channel without corruption or wrong format.

**Manual steps:**
1. Ask OpenClaw to send a small text file or image if supported by the assigned channel.
2. Open/download the attachment as a normal user.
3. Confirm filename/type/content is usable.
4. If inbound attachments are supported, upload a harmless small file and ask OpenClaw to summarize it.

**Expected visible behavior:**
- Attachment appears in correct channel.
- File opens normally.
- No broken media preview or missing attachment.
- Inbound attachment is acknowledged correctly if supported.

**Failure/confusion signs:**
- Attachment sent as wrong type.
- Broken preview/download.
- Bot claims file sent but nothing appears.
- Inbound file ignored without explanation.

**Evidence required:**
- Video of send/open flow.
- Screenshot of attachment in channel.

---

# B. Plugin Install and Use

## B1. Discover and install a plugin

**User goal:** A normal user can find, install, and understand a plugin without maintainer help.

**Starting state:**
- OpenClaw installed.
- Plugin system available.
- Pick a safe plugin assigned by QA coordinator, preferably one with no destructive side effects.

**Manual steps:**
1. Start recording before opening docs/CLI.
2. Find the plugin using the documented path or command.
3. Install it using the public instructions.
4. Note any prompts, warnings, permissions, or auth steps.
5. Run the command that lists installed/enabled plugins.

**Expected visible behavior:**
- Plugin can be discovered from public docs/CLI.
- Install command succeeds or gives clear next action.
- Plugin appears in installed/enabled plugin list.
- Any permissions/auth warnings are understandable.

**Failure/confusion signs:**
- Tester cannot find plugin instructions.
- Install command differs from docs.
- Success message appears but plugin is not listed.
- Error assumes maintainer knowledge.
- Plugin asks for secrets in unsafe way.

**Evidence required:**
- Video from discovery through installed list.
- Screenshot/log of install output and plugin list.

**Human judgment:**
Could a normal technical user install this plugin without asking the team for help?

## B2. Configure plugin auth safely

**User goal:** Configure a plugin credential or setting without leaking secrets and with clear validation.

**Manual steps:**
1. Follow plugin config/auth instructions.
2. Enter a test credential or configured safe key if assigned.
3. Run plugin validation/status command.
4. Confirm output redacts secrets.

**Expected visible behavior:**
- Config path is clear.
- Validation distinguishes missing auth vs invalid auth vs network failure.
- Secrets are redacted in output/logs.

**Failure/confusion signs:**
- Raw key printed back.
- Error says generic failure without fix.
- User cannot tell whether auth is saved.
- Auth works before restart but fails after restart.

**Evidence required:**
- Video with secrets hidden/redacted.
- Redacted config/status output.

## B3. Use installed plugin in a real task

**User goal:** Use the plugin to complete a realistic user task, not just confirm it installed.

**Manual steps:**
1. Ask OpenClaw to use the plugin for its intended purpose.
2. Verify the plugin tool/action appears in reasoning/output if visible.
3. Inspect the final result as a user.
4. Try one normal edge case: empty input, invalid target, missing optional setting, or small malformed input.

**Expected visible behavior:**
- Plugin is callable from OpenClaw.
- Result is correct/useful for the task.
- Edge case returns understandable error.
- No unrelated tool/provider error.

**Failure/confusion signs:**
- Plugin installed but not available to runtime.
- OpenClaw hallucinates plugin result.
- Edge case crashes or gives stack trace.
- Plugin action happens but user cannot see outcome.

**Evidence required:**
- Video of task execution.
- Screenshot/log of plugin result.
- Edge-case error evidence.

## B4. Plugin persistence after restart/update

**User goal:** Plugin remains installed/configured after restart or update when expected.

**Manual steps:**
1. Install/configure plugin.
2. Restart OpenClaw gateway/app/TUI according to normal instructions.
3. Re-check plugin list/status.
4. Run the same plugin task again.

**Expected visible behavior:**
- Plugin remains installed/enabled.
- Auth/config persists safely.
- Tool still works after restart.

**Failure/confusion signs:**
- Plugin disappears.
- Config lost.
- Needs undocumented restart step.
- Status says enabled but runtime cannot use it.

**Evidence required:**
- Video spanning install → restart → reuse, or clearly timestamped clips.
- Status before/after restart.

## B5. Disable/uninstall plugin cleanly

**User goal:** Remove or disable a plugin without breaking OpenClaw.

**Manual steps:**
1. Disable or uninstall the assigned plugin.
2. Confirm plugin no longer appears as enabled.
3. Ask OpenClaw to perform the plugin task again.
4. Observe the error/recovery instruction.

**Expected visible behavior:**
- Disable/uninstall succeeds.
- Plugin no longer available.
- OpenClaw says plugin is missing/disabled and how to re-enable.
- No crash.

**Failure/confusion signs:**
- Plugin still runs after uninstall.
- Runtime crashes because tool disappeared.
- Error blames unrelated provider/model.

**Evidence required:**
- Video of disable/uninstall and follow-up task.
- Status output.

---

# C. Provider / Model Route

## C1. Correct provider/model route visible to user

**User goal:** Know which provider/model OpenClaw is using and verify it matches the assigned beta route.

**Manual steps:**
1. Open OpenClaw config/status/model display.
2. Send a normal prompt.
3. Check whether output/status/logs identify the expected route.
4. Switch to an invalid model/provider only if assigned and safe.

**Expected visible behavior:**
- Expected route is visible or inferable.
- Invalid route gives clear recovery.
- No silent fallback to an unexpected model.

**Failure/confusion signs:**
- Uses wrong provider silently.
- Route hidden from user.
- Budget/auth errors mislabeled as schema/tool errors.

**Evidence required:**
- Screen recording/status output.
- Error evidence if route invalid.

## C2. Budget/auth failure clarity

**User goal:** Understand when a test key hits budget/auth limits.

**Manual steps:**
1. Use assigned capped/invalid test route only if QA coordinator provides one.
2. Trigger a safe request.
3. Read the error as a user.
4. State what action the error tells you to take.

**Expected visible behavior:**
- Error says budget/auth problem clearly.
- No misleading schema/tool-payload message.
- No token exposure.

**Failure/confusion signs:**
- User cannot tell whether issue is budget, model, provider, or OpenClaw bug.
- Raw token/key appears in logs.

**Evidence required:**
- Video of failed request and error.
- Redacted logs.

---

# D. Sessions, State, and Restart

## D1. Session continuity after restart

**User goal:** Continue a conversation/task after restarting OpenClaw.

**Manual steps:**
1. Start a short task with a unique marker.
2. Restart OpenClaw using normal instructions.
3. Reopen the same session or channel.
4. Ask a follow-up referencing the marker.

**Expected visible behavior:**
- User can find/reopen the session if supported.
- Context is retained or clearly documented as not retained.
- No confusing stale state.

**Failure/confusion signs:**
- Session disappears without explanation.
- Old context leaks into wrong channel.
- Follow-up answers a different conversation.

**Evidence required:**
- Video before/after restart.
- Screenshot of session/channel state.

## D2. Upgrade preserves usable config

**User goal:** Update to the release without losing working configuration.

**Manual steps:**
1. Start from previous release or realistic existing setup.
2. Verify current working channel/provider/plugin state.
3. Upgrade to target tag.
4. Re-run one normal task and one assigned release-specific scenario.

**Expected visible behavior:**
- Upgrade completes.
- Existing config still works or migration gives clear action.
- No duplicate services/watchers.

**Failure/confusion signs:**
- Works before upgrade, fails after.
- Migration warning is unclear.
- Service/gateway state inconsistent.

**Evidence required:**
- Video of before/after checks.
- Version proof and status output.

---

# E. Error Recovery and UX

## E1. Human-readable failure

**User goal:** Recover from a normal mistake without maintainer help.

**Manual steps:**
1. Make one safe mistake assigned by QA: bad config key, invalid plugin name, wrong channel target, invalid model alias, etc.
2. Read the resulting error.
3. Try the recovery action if the error gives one.

**Expected visible behavior:**
- Error identifies cause.
- Recovery action is clear.
- Fix works without searching private maintainer notes.

**Failure/confusion signs:**
- Stack trace only.
- Wrong subsystem blamed.
- No recovery path.
- Error disappears but behavior still broken.

**Evidence required:**
- Video of mistake → error → recovery attempt.
- Human note: “I would/would not know what to do next.”

## E2. No silent success

**User goal:** Confirm OpenClaw does not claim success when nothing happened.

**Manual steps:**
1. Perform a task with an observable external result: channel reply, plugin action, file/report creation.
2. If OpenClaw says success, verify the external result exists.
3. If result is missing, record mismatch.

**Expected visible behavior:**
- Success claim matches observable result.
- If action fails, OpenClaw says so.

**Failure/confusion signs:**
- “Done” but no message/file/plugin output exists.
- Success in logs but user-visible state missing.

**Evidence required:**
- Video showing claim and external verification.

---

# F. Reporting Expectations

For each assigned scenario, tester report must include:

- scenario name
- expected behavior
- actual behavior
- human judgment: worked/confusing/broken/not trustworthy
- evidence link + timestamp
- warnings/errors observed
- whether a bug should be filed

Reports that only say “pass” without human observations and evidence timestamps should be returned as `NEEDS_MORE_EVIDENCE`.
