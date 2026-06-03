# Baseline Human QA Checklist

This checklist runs for every OpenClaw alpha/beta release, regardless of what changed.

It is **manual QA/QC**, not automated QA. A human tester should perform the flow, screen-record where possible, and judge whether OpenClaw is understandable, reliable, and trustworthy in real use.

## Priority model

- **P0 baseline** — release-blocking. Must pass, or the release needs an explicit Henry/admin waiver.
- **P1 baseline** — core confidence. Should run every release; failures may ship only with documented caveat/owner/next action.

Evidence is required for every claimed pass.

---

# P0 Baseline — Always Run / Release Blocking

## P0-1. Install or upgrade to the assigned release

**User goal:** A normal tester can install or update OpenClaw to the target release.

**Steps:**
1. Start screen recording.
2. Follow the public install/update instructions for the target tag.
3. Run the command or UI path that shows OpenClaw version/tag/commit.
4. Note any warnings, confusing prompts, or undocumented steps.

**Expected:**
- Install/update completes.
- OpenClaw reports the assigned version/tag.
- Tester can explain what happened without maintainer help.

**Evidence:**
- Screen recording or screenshots of install/update and version proof.
- Exact command/path used.

**Blockers:**
- Cannot install/update.
- Version/tag cannot be verified.
- Instructions require private maintainer knowledge.

## P0-2. First useful response

**User goal:** OpenClaw can answer one normal user request after install/update.

**Steps:**
1. Open the normal OpenClaw surface assigned for testing: TUI, CLI, Discord, Telegram, web, etc.
2. Send: `OpenClaw P0 <timestamp>: reply with one short sentence and mention the current test surface.`
3. Observe response quality, route, delay, and errors.

**Expected:**
- One useful response appears in the expected surface.
- No duplicate response.
- No crash or hidden provider/tool failure.

**Evidence:**
- Video from prompt through response.
- Screenshot/log of final response.

**Blockers:**
- No response.
- Wrong surface/provider/identity.
- Duplicate or looping response.

## P0-3. One configured messaging channel works end-to-end

**User goal:** OpenClaw responds in a real configured channel/thread/chat.

**Steps:**
1. Use the assigned channel: Discord thread, Discord parent channel, Telegram DM/group, etc.
2. Send a unique marker: `channel-p0-<timestamp>`.
3. Ask OpenClaw to reply in that same place.
4. Send one follow-up to verify basic context continuity.

**Expected:**
- Reply arrives in the same expected channel/thread/chat.
- Exactly one reply per message.
- Follow-up keeps basic context.
- No wrong-channel delivery.

**Evidence:**
- Screen recording.
- Screenshot of final channel/thread/chat.

**Blockers:**
- Silent delivery failure.
- Wrong channel/thread/chat.
- Duplicate replies.
- Bot identity/account mismatch.

## P0-4. Plugin/tool visibility sanity check

**User goal:** OpenClaw exposes its expected tools/plugins after install/update.

**Steps:**
1. Run the documented status/doctor/tools/plugins command, or use the assigned UI route.
2. Confirm tools/plugins are visible.
3. If the release affects tools/plugins, verify the changed item appears.

**Expected:**
- Tool/plugin list or status is accessible.
- No silent omission of expected tools/plugins.
- Errors are understandable.

**Evidence:**
- Screenshot/log of status/tool/plugin list.

**Blockers:**
- Tool/plugin system missing or inaccessible.
- Expected tools silently omitted.
- Status claims success while runtime cannot use tools.

## P0-5. One safe failure gives understandable recovery

**User goal:** A normal user can understand and recover from a harmless mistake.

**Steps:**
1. Trigger one assigned safe failure: invalid provider/model alias, missing optional config, restricted channel, nonexistent plugin name, etc.
2. Read the error as a user.
3. State what action the error tells you to take.
4. If safe, try the recovery action.

**Expected:**
- Error identifies the real problem.
- Recovery action is clear.
- No misleading schema/tool/provider error.
- No secret exposure.

**Evidence:**
- Video of failure and recovery attempt.
- Redacted logs if relevant.

**Blockers:**
- Silent failure.
- Misleading error.
- Stack trace only.
- Raw secrets shown.

## P0-6. No obvious secret exposure

**User goal:** Normal testing does not expose private keys, API keys, tokens, `.env`, cookies, passwords, private DMs, or private SSH keys.

**Steps:**
1. During all P0 tests, watch for secrets in UI, logs, screenshots, and uploaded evidence.
2. Before submitting report, inspect evidence for accidental exposure.

**Expected:**
- No raw secrets visible.
- Sensitive values are redacted.

**Evidence:**
- Secrets check checkbox in report.

**Blockers:**
- Any raw secret appears in public evidence.
- Report must be replaced with redacted evidence before acceptance.

## P0-7. No silent false success

**User goal:** OpenClaw does not say “done” when the visible result is missing.

**Steps:**
1. Pick one externally visible action from the run: channel reply, plugin output, file/report creation, etc.
2. If OpenClaw claims success, verify the external result exists.

**Expected:**
- Success claim matches visible reality.
- If action failed, OpenClaw says so clearly.

**Evidence:**
- Video showing success claim and external verification.

**Blockers:**
- “Done” but no visible result exists.
- User cannot verify what happened.

---

# P1 Baseline — Always Run / Core Confidence

P1 baseline checks are core confidence checks. The minimum Core P1 set must run every release, or be explicitly marked `NOT_RUN` with reason, owner, and next action.

**Mandatory Core P1 every release:**
- restart/gateway persistence
- install and use one safe plugin
- provider/model route visibility
- config/session continuity after restart/update

Additional P1 rows should run when the relevant surface is configured.

## P1-1. Secondary messaging channel

If the tester has a second channel configured, repeat the channel end-to-end test there.

Examples:
- Discord + Telegram
- Discord parent + Discord thread
- Telegram group + DM

## P1-2. Restart/gateway persistence

**Goal:** Basic working state survives restart.

**Steps:**
1. Complete P0 first response or channel response.
2. Restart OpenClaw/gateway/app using normal instructions.
3. Run the same response/channel check again.

**Expected:**
- OpenClaw comes back cleanly.
- Config/channel/provider still works.
- No duplicate services/watchers.

## P1-3. Basic session continuity

**Goal:** Tester can continue or intentionally start fresh without confusion.

**Steps:**
1. Start a short conversation with a unique marker.
2. Close/reopen the interface or switch away/back.
3. Ask a follow-up referencing the marker.

**Expected:**
- Session continuity is retained where expected, or reset behavior is clear.
- No unrelated old context leaks in.

## P1-4. Install and use one safe plugin

**Goal:** A normal technical user can install and use a plugin.

**Steps:**
1. Discover plugin via documented route.
2. Install it.
3. Confirm it appears in plugin/tool status.
4. Use it for one realistic task.
5. Record confusion or missing docs.

**Expected:**
- Plugin can be discovered, installed, listed, and used.
- Errors/auth prompts are understandable.
- No secrets exposed.

## P1-5. Provider/model route visibility

**Goal:** Tester can tell which provider/model route OpenClaw is using.

**Steps:**
1. Open status/config/log output showing route if available.
2. Send one normal request.
3. Confirm route matches assigned tester config.

**Expected:**
- Route is visible or otherwise verifiable.
- No silent fallback to unexpected provider/model.

## P1-6. Config survives restart/update

**Goal:** Working config remains usable after restart/update.

**Steps:**
1. Record working config/status before restart/update.
2. Restart/update.
3. Re-run channel/provider/plugin checks.

**Expected:**
- Existing safe config still works.
- Migration warnings are clear and actionable.

## P1-7. Logs/status are useful to a tester

**Goal:** A tester can gather enough diagnostic info without maintainer-only knowledge.

**Steps:**
1. Run documented status/log command.
2. Confirm output is understandable and redacted.
3. Capture what would be useful in a bug report.

**Expected:**
- Status/log command exists.
- Output helps classify issue.
- Secrets are redacted.

## P1-8. Report/evidence flow works

**Goal:** Tester can submit a QA issue with evidence.

**Steps:**
1. Open `HeraldLab/OpenclawQA` issue form/template.
2. Submit report with evidence links.
3. Reply in assigned Discord thread with issue URL.

**Expected:**
- Issue form is usable.
- Evidence links open for QA team.
- Assigned thread receives the issue link.

---

# Required report fields

Every baseline report must include:

- release tag
- tester name/handle
- OS/device
- install/update method
- OpenClaw version/tag/commit proof
- provider/model route
- channel(s) tested
- P0 verdicts
- P1 verdicts if run
- evidence links/timestamps
- human judgment notes
- secrets check
- GitHub QA issue link

# Acceptance

- P0 baseline requires `PASS` or explicit waiver.
- P1 baseline requires `PASS`, `PASS_WITH_CAVEAT`, `BLOCKED`, or `NOT_RUN` with reason.
- The report is accepted only after evidence review confirms the visible behavior and checks for errors/secrets.
