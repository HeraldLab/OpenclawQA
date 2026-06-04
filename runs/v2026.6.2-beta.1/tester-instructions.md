# Tester Instructions — OpenClaw `v2026.6.2-beta.1`

Generated: `2026-06-04T01:10:00Z`
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.2-beta.1
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.2-beta.1
Report results: https://github.com/HeraldLab/OpenclawQA/issues/new/choose
Deadline: **6 hours after packet receipt**, unless Henry/admin sets a different SLA.

## Target

Test OpenClaw beta release `v2026.6.2-beta.1` with human-observed QA. This is not just command output. We need to know whether a real user would trust the install, messaging, plugin, failure, and recovery surfaces.

## Required report header

Include these in every report:

- Tester handle.
- OS/platform/version.
- Install/upgrade method and exact command used.
- OpenClaw version/tag observed after install.
- Provider/model route used if a model call is part of the test.
- Assigned channel/surface: TUI, Discord, Telegram, WebChat, Workboard, etc.
- Evidence links/screenshots/recording.
- Secrets check: confirm no raw keys/tokens/private customer data are exposed.

If a fact is unavailable, write `NOT_ENOUGH_INFO` and explain why.

## Baseline checks every dispatched tester must cover

1. Install/upgrade to `v2026.6.2-beta.1`.
2. Prove version/tag/commit.
3. Get one normal first response.
4. Verify one assigned human-visible messaging/channel path.
5. Check plugin/tool visibility or install/use one safe plugin.
6. Trigger one harmless failure and judge whether recovery is clear.
7. Run one Core P1 check: restart/gateway persistence, provider route, or config/session continuity.
8. Include expected vs actual behavior and a human trust/confusion note.

## Release-specific focus for beta62

The release notes call out these high-risk behavior changes:

- Plugin and skill installs now use an operator install policy instead of the old dangerous-code scanner path.
- Discord/Telegram/Feishu/WhatsApp/outbound delivery changed around duplicate transcript mirrors, Telegram admin writeback, streamed-final previews, approval allowlists, poll modifiers, Discord voice errors, and internal progress traces.
- Chat/UI/Workboard/WebChat flows changed around streaming text, completed-send reconciliation, ACK timing, keyboard movement, and current chat toggles.
- Security/policy/config recovery now rejects corrupt shell snapshots, unsupported policy keys, unsafe exec precheck envs, malformed numeric limits, and suspicious gateway startup configs.
- Gateway/agent/provider/model paths changed around session locks, abandoned Codex app-server startups, custom-provider fanout, bundled provider aliases, prompt-cache boundaries, Gemini/Kimi handling.
- Windows installer and package publication paths changed; verify the beta channel is not stale.

## Short tester cards

### Card A — Windows install/package + provider route

Best for: Ayomide or Miriam.

1. Run:
   ```powershell
   npm view openclaw@beta version
   npm install -g openclaw@beta
   openclaw --version
   openclaw gateway status
   ```
2. Start OpenClaw and send `hello`.
3. Capture provider/model route if visible.
4. Restart gateway, then send one more short prompt.
5. Trigger one harmless bad provider/model/config error if safe.

Expected: beta channel points to `2026.6.2-beta.1`; gateway status is understandable; one useful response appears; bad config fails clearly without secrets.

Evidence: command screenshots, first response screenshot, restart/status screenshot, redacted failure screenshot.

### Card B — Telegram/Discord delivery + duplicate/final-output check

Best for: Anny or any tester with a configured public channel.

1. Upgrade/install to beta62 and capture version.
2. Use the assigned channel/thread/bot and send `hello` or one normal request.
3. Watch whether progress preview and final output duplicate or leak internal traces.
4. Confirm reply lands in the correct human-visible target: not wrong parent channel, wrong thread, or silent drop.
5. Trigger one harmless failure and record whether the channel error is readable.

Expected: exactly one final answer in the correct target; no duplicate finals; no raw internal trace; failure message is useful.

Evidence: channel screenshots with timestamps/message IDs, plus version proof.

### Card C — Plugin operator install policy

Best for: tester comfortable with plugins/tools.

1. After upgrade, list configured tools/plugins or open the plugin install surface.
2. Install/update one safe plugin/tool or use an already-installed safe plugin.
3. Observe the operator install policy prompt/decision surface.
4. If safe, attempt one unsupported/unreadable plugin metadata path and observe recovery.

Expected: allow/deny decision is understandable; doctor/CLI/ClawHub surfaces agree; unreadable plugin does not break the entire tool list.

Evidence: screenshots/logs of prompt, decision, result, and trust note.

### Card D — Security/config harmless rejection

Best for: any tester after baseline smoke passes.

1. Use a safe malformed config/provider/model name or documented harmless bad setting.
2. Run the smallest command needed to trigger the error.
3. Redact logs before upload.

Expected: OpenClaw rejects unsafe/unsupported state clearly and does not print secrets.

Evidence: screenshot/log and one sentence: "Would a user know what to do next?"

## Recommended first wave

- Ayomide: Card A + one harmless failure.
- Miriam: Card A with Windows packaging/backup/SSH-safety note.
- Anny: Card B plus report quality check.

Hold Samuel and Gabriel unless Henry/admin explicitly assigns beta62 despite unresolved beta2 state.

## Report format

Use GitHub Issues in this repo or the existing per-person Discord thread:

- Use **Install smoke result** for install-only passes/failures.
- Use **Tester report** for general scenario reports.
- Use **Beta blocker** only for issues that block release validation.

One issue per bug. Do not combine unrelated failures.

## Evidence quality bar

A report is triage-ready when it has target tag, OS/platform, install method, exact steps, expected behavior, actual behavior, screenshots/recording/logs, and whether the issue reproduces.

Do not upload secrets, API keys, SSH private keys, private customer data, or unsanitized environment dumps. If raw evidence contains private data, summarize publicly and say the raw artifact is private.
