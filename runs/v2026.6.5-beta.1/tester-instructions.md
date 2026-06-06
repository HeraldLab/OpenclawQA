# Tester Instructions — OpenClaw `v2026.6.5-beta.1`

Generated: `2026-06-06T11:00:00Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.5-beta.1  
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.1  
Report results: https://github.com/HeraldLab/OpenclawQA/issues/new/choose  
Deadline: **6 hours after packet receipt**, unless Henry/admin sets a different SLA.

## Target

Test OpenClaw beta release `v2026.6.5-beta.1` with human-observed QA. This is not just command output. We need to know whether a real user would trust the install, messaging, tool/plugin, provider, restart, and recovery surfaces.

## Required report header

Include these in every report:

- Tester handle.
- Assigned Discord/thread/channel.
- OS/platform/version.
- Install/upgrade method and exact command used.
- OpenClaw version/tag observed after install.
- Provider/model route used if a model call is part of the test.
- Assigned surface: TUI, Discord thread, Telegram, WebChat, Matrix, Workboard, etc.
- Evidence links/screenshots/recording.
- Secrets check: confirm no raw keys/tokens/private customer data/cookies/passwords are exposed.

If a fact is unavailable, write `NOT_ENOUGH_INFO` and explain why.

## Baseline checks every dispatched tester must cover

1. Install/upgrade to `v2026.6.5-beta.1`.
2. Prove version/tag/commit.
3. Get one normal first response.
4. Verify one assigned human-visible messaging/channel path.
5. Check plugin/tool visibility or use one safe plugin/tool.
6. Trigger one harmless failure and judge whether recovery is clear.
7. Run one Core P1 check: restart/gateway persistence, provider route, or config/session continuity.
8. Include expected vs actual behavior and a human trust/confusion note.

## Release-specific focus for beta665

The release notes call out these high-risk behavior changes:

- Native channel replies should strip reasoning/thinking scaffolding before users see them.
- MCP/tool results with resource/audio/image-like blocks should not break provider calls or poison session history.
- Anthropic/Codex/agent sessions should recover more cleanly after prompt-cache expiry or Gateway restart.
- Parallel is now bundled as a `web_search` provider; missing/available provider state should be clear.
- Google Vertex/provider catalog/cooldown and memory adapter status paths changed.
- Matrix voice/thread behavior changed.
- Auth profiles, official npm plugin install records, and prerelease fallback integrity should be more durable.
- macOS node mode should avoid unexpected reconnect churn.
- Doctor/cron/service-env/WhatsApp config reload paths changed.
- TUI/chat/Workboard message stability improved around stale history/reloads/abort windows.
- Security/config/tooling guards should fail clearly without leaking secrets.

## Short tester cards

### Card A — Windows install/package + provider/tool visibility

Best for: Ayomide.

1. Run:
   ```powershell
   npm view openclaw@beta version
   npm install -g openclaw@beta
   openclaw --version
   openclaw gateway status
   ```
2. Start OpenClaw and send `hello`.
3. Capture provider/model route if visible.
4. Use one safe tool/plugin or list available tools/plugins.
5. Trigger one harmless bad provider/model/config error if safe.

Expected: beta channel points to `2026.6.5-beta.1`; gateway status is understandable; one useful response appears; tool/plugin state is visible; bad config fails clearly without secrets.

Evidence: command screenshots, first response screenshot, tool/plugin screenshot, redacted failure screenshot.

### Card B — Gateway restart + auth/plugin continuity

Best for: Mariam.

1. Upgrade/install to beta665 and capture version.
2. Send one normal prompt.
3. Restart gateway/session using the documented command/path.
4. Send a second prompt in the same surface.
5. Confirm auth/profile/plugin state survives or fails clearly.
6. If provider/key/server errors appear, classify whether it is OpenClaw install failure or external provider outage.

Expected: after restart, OpenClaw responds again; no hang; no stale provider route; no secret exposure in logs.

Evidence: before/after screenshots, gateway/status screenshot, provider/error classification if blocked.

### Card C — Fixed-thread delivery + no reasoning leak

Best for: Anny or any tester with a configured channel.

1. Upgrade/install to beta665 and capture version.
2. Use the assigned per-person thread/channel and send: `OpenClaw beta665 test <timestamp>: reply with a short checklist.`
3. Send a follow-up in the same thread.
4. Confirm the reply lands in the correct target, appears once, and preserves context.
5. Check the visible reply for `<thinking>`, raw provider trace, internal progress dump, duplicate finals, or parent-channel leakage.
6. Trigger one harmless failure and record whether the channel error is readable.

Expected: exactly one final answer in the correct thread/channel; no reasoning leak; no duplicate; no wrong parent/thread delivery.

Evidence: channel screenshots or recording with timestamps/message IDs, plus version proof.

### Card D — Tool/MCP/plugin rich-result sanity

Best for: tester with safe tools/plugins configured.

1. Use a safe tool/plugin that returns a link, file-like result, media-like result, or structured/rich output if available.
2. Ask one follow-up after the tool result.
3. If no such tool is available, list tools/plugins and mark `NOT_RUN` with reason.

Expected: tool result is readable; follow-up still works; no Anthropic/provider 400, malformed image error, or broken session history.

Evidence: screenshot/log of tool output and follow-up result.

### Card E — Optional provider-specific checks

Only run if your environment has the relevant provider/channel:

- Parallel `web_search`: confirm provider/tool availability or clear missing-key state.
- Google/Vertex: confirm catalog/status and one simple call if configured.
- Matrix: confirm voice/thread preflight if configured.
- WhatsApp: confirm config reload/startup does not hang if configured.
- macOS node mode: confirm direct Gateway session does not churn if configured.

If not configured, write `NOT_RUN — not configured`.

## Recommended first wave

- Ayomide: Card A + harmless failure.
- Mariam: Card B + provider/blocker classification.
- Anny: Card C + tool/plugin visibility.

Hold Samuel and Gabriel unless Henry/admin explicitly assigns beta665 despite unresolved prior state.

## Report format

Use GitHub Issues in this repo or the existing per-person Discord thread:

- Use **Install smoke result** for install-only passes/failures.
- Use **Tester report** for general scenario reports.
- Use **Beta blocker** only for issues that block release validation.

One issue per bug. Do not combine unrelated failures. Do **not** file upstream `openclaw/openclaw` issues directly unless asked.

## Evidence quality bar

A report is triage-ready when it has target tag, OS/platform, install method, exact steps, expected behavior, actual behavior, screenshots/recording/logs, and whether the issue reproduces.

Do not upload secrets, API keys, SSH private keys, cookies, private customer data, or unsanitized environment dumps. If raw evidence contains private data, summarize publicly and say the raw artifact is private.
