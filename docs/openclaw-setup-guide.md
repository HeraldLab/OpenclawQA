# OpenClaw Setup Guide for Herald Labs Testers

This guide turns the setup help we have been giving in Discord into one repeatable path.

Use it for the first OpenClaw install, beta upgrade smoke tests, and basic Discord/Telegram setup. The official OpenClaw docs remain the source of truth for product commands; this document adds the Herald Labs tester workflow, evidence expectations, and field-tested troubleshooting notes.

## Quick links

- Official getting started: <https://docs.openclaw.ai/start/getting-started>
- Official install docs: <https://docs.openclaw.ai/install>
- Official releases: <https://github.com/openclaw/openclaw/releases>
- Herald Labs QA reports: <https://github.com/HeraldLab/OpenclawQA/issues/new/choose>
- FAQ: [Frequently asked questions](#frequently-asked-questions)

## Before you start

You need:

- A laptop/desktop for the install. Windows is fine; several beta testers use Windows.
- Node 24 recommended, or Node 22.19+.
- A model/API key from the current Herald Labs packet or your own provider.
- A place to report evidence: your assigned Discord thread or a GitHub issue in this repo.
- Screenshots or screen recording where possible.

Do **not** post raw API keys, Discord bot tokens, SSH private keys, passwords, or full unsanitized environment dumps in Discord or GitHub.

## Recommended first install path

### macOS / Linux / WSL

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
openclaw gateway status
openclaw --version
```

### Windows PowerShell

Run PowerShell normally first. If Gateway/service install fails, rerun PowerShell as Administrator for the gateway install/start commands.

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
openclaw onboard --install-daemon
openclaw gateway status
openclaw --version
```

Expected result:

- `openclaw --version` prints the installed OpenClaw version/tag.
- `openclaw gateway status` says the Gateway is running/listening.
- You can start a chat surface and get one useful response.

The official getting-started doc says the Gateway should listen on port `18789`. If a support helper asks for a port check, capture the output from OpenClaw itself instead of guessing a port.

## Alternative npm install path

Use this if the tester packet specifically asks you to install via npm or beta channel.

```bash
npm view openclaw@latest version
npm install -g openclaw@latest
openclaw onboard --install-daemon
openclaw --version
openclaw doctor
openclaw gateway status
```

For beta packets, use the version/channel in the run instructions. Example from recent beta packets:

```bash
npm view openclaw@beta version
npm install -g openclaw@beta
openclaw --version
openclaw gateway status
```

If `npm view openclaw@beta version` does not show the target beta from your packet, report that as a packaging/channel blocker instead of pretending you installed the right version.

## First smoke test

After install/onboarding:

1. Capture version proof:

   ```bash
   openclaw --version
   openclaw gateway status
   openclaw doctor
   ```

2. Start a local chat surface, usually TUI:

   ```bash
   openclaw tui
   ```

3. In the TUI, send:

   ```text
   hello
   ```

4. Capture the result:
   - PASS if you got one useful response.
   - BLOCKED if there was no response, duplicate output, provider/auth error, or gateway failure.
   - NOT_ENOUGH_INFO if you cannot tell what happened.

For manual QA, `install succeeded` is not enough. We need visible proof that OpenClaw can produce a normal response and that the user-facing error path is understandable when something fails.

## Model/API key setup

During onboarding, OpenClaw should prompt for model/provider auth. Use the route specified in the current Herald Labs packet or key-handoff thread.

Recent Herald Labs beta setups have used an `openclaw-beta` route. Depending on package/config generation it may appear as `openai/openclaw-beta`, `litellm/openclaw-beta`, or another explicitly assigned route. Use the route in your current packet; do not guess.

Useful checks:

```bash
openclaw models status
openclaw status --deep
openclaw doctor
```

If support asks you to paste a key, stop and ask for the approved key-handoff path. Keys should be handled in public per-tester handoff threads, acknowledged, then the key-bearing message should be deleted. Never paste a key in a normal report.

## Discord setup

Discord is useful for human-visible QA, but it has more moving parts than Telegram. If you only need a first smoke result and Discord is blocking you, use Telegram first and report Discord as a separate setup blocker.

### Create or use a test Discord server

For beta testing, the cleanest path is a private test server:

1. Discord → left sidebar **+**.
2. Create a server for testing.
3. Add your OpenClaw bot to that server.
4. Keep your testing thread/screenshots in your assigned Herald Labs follow-up thread.

### Create the Discord bot

1. Go to <https://discord.com/developers/applications>.
2. Create a **New Application**.
3. Open **Bot** and create/copy the bot token.
4. Enable the needed intents when requested by OpenClaw/support:
   - Message Content Intent.
   - Server Members Intent.
5. Open **OAuth2 → URL Generator**.
6. Select scopes:
   - `bot`
   - `applications.commands`
7. Add bot permissions such as:
   - View Channels
   - Send Messages
   - Read Message History
   - Embed Links
   - Attach Files
   - Add Reactions
8. Use the generated invite URL to add the bot to your test server.

Do not paste the bot token in Discord/GitHub.

### Configure Discord in OpenClaw

Run in PowerShell/bash, **not inside the TUI**:

```bash
openclaw configure --section channels
openclaw gateway restart
openclaw channels status
```

Choose Discord and paste the bot token when the wizard asks for it.

For group/server testing, prefer a narrow allowlist and `requireMention` behavior where available. If a helper asks you to temporarily use `*` for a private test server, record that as a test-only setting and tighten it after the smoke.

### Pair and test Discord

1. Confirm the bot appears online.
2. DM the bot or mention it in the test server, depending on your packet:

   ```text
   hello
   ```

3. If OpenClaw gives a pairing code, approve it in PowerShell/bash:

   ```bash
   openclaw pairing list discord
   openclaw pairing approve discord <CODE>
   ```

4. Send `hello` again and capture whether the reply lands in the correct DM, server channel, or thread.

## Telegram setup

Telegram has been lower-friction for several testers. Use it when Discord setup is slowing down the install-smoke.

1. In Telegram, message `@BotFather`.
2. Run:

   ```text
   /newbot
   ```

3. Copy the bot token.
4. In PowerShell/bash:

   ```bash
   openclaw configure --section channels
   openclaw gateway restart
   openclaw channels status
   ```

5. Choose Telegram and paste the token.
6. DM your Telegram bot:

   ```text
   hello
   ```

7. Approve pairing if needed:

   ```bash
   openclaw pairing list telegram
   openclaw pairing approve telegram <CODE>
   ```

8. DM `hello` again and capture the result.

If Telegram works and Discord does not, report that clearly:

```text
TUI: PASS
Telegram: PASS
Discord: BLOCKED — <what happened>
```

## What to include in your report

Every report should include:

- Tester handle.
- OS/platform/version.
- Install or upgrade method and exact command used.
- OpenClaw version/tag observed after install.
- Provider/model route used, if a model call is part of the test.
- Surface tested: TUI, Discord, Telegram, WebChat, Workboard, etc.
- Expected behavior.
- Actual behavior.
- Evidence: screenshots, screen recording, logs, or Discord message IDs.
- Secret check: confirm no raw keys/tokens/private data are exposed.
- Human judgment: what was confusing, slow, silent, duplicated, or untrustworthy?

Minimum install-smoke report:

```text
STATUS: PASS / BLOCKED / NOT_ENOUGH_INFO
OS/platform:
Install command:
Observed OpenClaw version:
TUI hello result:
Discord/Telegram delivery result:
Provider/model route:
Evidence:
Human judgment:
Secrets check:
```

Use the GitHub issue form when the report is ready: <https://github.com/HeraldLab/OpenclawQA/issues/new/choose>

## Troubleshooting playbook

### `openclaw` command is not found

Run:

```bash
node -v
npm prefix -g
echo "$PATH"
```

On Windows PowerShell:

```powershell
node -v
npm prefix -g
$env:PATH
where openclaw
```

If installed via npm, make sure the global npm bin directory is on PATH. If support asks you to reinstall, capture `openclaw --version` and `where openclaw` first so we know what you are removing.

### Need to uninstall an old global npm install

First identify it:

```powershell
openclaw --version
where openclaw
npm list -g openclaw --depth=0
```

If it is a global npm install:

```powershell
npm uninstall -g openclaw
where openclaw
openclaw --version
```

Expected after uninstall: `where openclaw` finds nothing and `openclaw --version` fails.

Do not delete your config folder, usually `C:\Users\<you>\.openclaw`, unless the current packet or support helper explicitly asks for a clean config wipe.

### Gateway unreachable or not installed

Run:

```bash
openclaw status
openclaw gateway status
openclaw channels status
openclaw doctor
```

On Windows, if the Gateway service is not installed/running, try from Administrator PowerShell:

```powershell
openclaw gateway install --force
openclaw gateway start
openclaw gateway status
openclaw status
```

If service startup is still blocked, run foreground mode and screenshot the first red/error lines:

```powershell
openclaw gateway run --force --verbose
```

If OpenClaw says gateway mode is missing:

```bash
openclaw config set gateway.mode local
openclaw config validate
openclaw gateway restart
```

### `openclaw logs --tail` fails

Use `--limit`, not `--tail`:

```bash
openclaw logs --limit 120 --plain
```

Search the log for the component you are testing, for example `discord`, `telegram`, `gateway`, `token`, `401`, `provider`, or `model`.

### No API key found

This usually means Gateway is running but the model/provider auth path is not configured for the active agent/session.

Run:

```bash
openclaw models status
openclaw doctor
openclaw logs --limit 120 --plain
```

Then, if instructed by the packet/helper, add the provider key through OpenClaw instead of pasting secrets in chat:

```bash
openclaw models auth paste-api-key --provider openai --agent main
openclaw gateway restart
openclaw tui
```

If your beta packet uses a custom base URL or route, verify it from the packet and redact the actual key/base URL in screenshots.

### `key not allowed to access model` / wrong model route

This means OpenClaw is trying to call a model that your key is not allowed to use.

Common cause from the tester threads: a default model was changed, but a stale per-agent override or old session still pointed at a different model.

Run this in the same terminal/user context that starts OpenClaw:

```bash
openclaw models status
openclaw status --deep
openclaw doctor
```

On Windows, support may ask you to inspect the config model fields:

```powershell
node -e "const fs=require('fs'); const p=process.env.USERPROFILE+'/.openclaw/openclaw.json'; const c=JSON.parse(fs.readFileSync(p)); console.log('default:', c.agents?.defaults?.model?.primary); console.table((c.agents?.list||[]).map((a,i)=>({i,id:a.id,primary:a.model?.primary})))"
```

If a stale model appears under `agents.list[].model.primary`, ask support before editing. The field to fix is the effective model route, not the key itself.

After changing model config:

```bash
openclaw gateway restart
```

Start a fresh session. Old Discord/OpenClaw sessions can cache old model choices.

### Max tokens too large

One tester hit a beta endpoint error like:

```text
max_tokens is too large
```

A temporary workaround is to cap provider token settings:

```bash
openclaw config set models.providers.openai.contextTokens 96000 --strict-json
openclaw config set models.providers.openai.maxTokens 4096 --strict-json
openclaw config validate
openclaw gateway restart
```

If it still fails, try a smaller cap only if support asks:

```bash
openclaw config set models.providers.openai.contextTokens 64000 --strict-json
openclaw config set models.providers.openai.maxTokens 2048 --strict-json
openclaw gateway restart
```

Report this as a product/config bug if it blocks first chat.

### Discord bot is offline or never replies

Check in this order:

```bash
openclaw channels status
openclaw gateway restart
openclaw channels status
openclaw logs --limit 120 --plain
```

Then verify in Discord Developer Portal:

- Bot token is valid and was not reset after copying.
- Message Content Intent is enabled.
- Server Members Intent is enabled if required.
- Bot was invited to the correct server with `bot` scope.
- Bot has View Channel, Send Messages, and Read Message History permissions.
- You are DMing the bot or mentioning it in the expected server/thread.

If Discord remains blocked, switch to Telegram for the install-smoke and report Discord separately.

### Telegram works but does not respond after `/start`

Usually pairing approval is missing.

Run in PowerShell/bash, not Telegram and not TUI:

```bash
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

Then send the bot:

```text
hello
```

If still blocked:

```bash
openclaw channels status
openclaw logs --limit 120 --plain
```

### Config path is wrong or `.openclaw` folder is missing

On Windows, do not assume the username/path from a screenshot. Find it:

```powershell
$env:USERNAME
$env:USERPROFILE
Get-Command openclaw -ErrorAction SilentlyContinue | Format-List
npm list -g openclaw --depth=0
Get-ChildItem -Path "$env:USERPROFILE" -Filter ".openclaw" -Recurse -ErrorAction SilentlyContinue
```

If support gives you a path like `C:\Users\use\.openclaw\...`, replace `use` with your actual Windows username.

### TUI opens a repair/Crestodian agent instead of normal chat

Treat that as a config/gateway recovery state, not a normal pass.

Capture:

```powershell
openclaw doctor
openclaw gateway status
openclaw status --deep
openclaw logs --limit 120 --plain
```

Also validate the JSON config if support asks:

```powershell
Get-Content "$env:USERPROFILE\.openclaw\openclaw.json" | ConvertFrom-Json | ConvertTo-Json -Compress
```

If JSON validation fails, report the exact error. Do not manually edit large config blocks unless support gives a targeted patch.

### Remote help / SSH access

If support needs access to your machine, use a safe route.

Rules:

- Do not paste SSH private keys in Discord.
- If a private key was posted, treat it as burned and rotate/regenerate it.
- A `10.x`, `172.16-31.x`, or `192.168.x` IP is usually private LAN only and not reachable from Herald Labs machines.
- Tailscale is the preferred route. Install/sign in to Tailscale and send the `100.x.x.x` IP.
- First probe reachability; only then decide how to handle a fresh key.

Good remote-help handoff:

```text
Tailscale IP: 100.x.x.x
OS: Windows/macOS/Linux
SSH running: yes/no
What I need help with: <short blocker>
I have rotated any key that was exposed: yes/no
```

## Frequently asked questions

### Do we already have a setup guide?

Before this file, the repo had a short `docs/tester-guide.md`, run-specific tester instructions, and links to official OpenClaw docs. It did not have one Herald Labs setup guide that consolidated the Discord setup-help threads and common FAQ.

### Should I use the official docs or this guide?

Use both:

- Official docs for the latest product command reference.
- This guide for Herald Labs tester workflow, what evidence to capture, and common beta setup blockers we have already seen.

### Should I test with Discord or Telegram?

If you are new or blocked, use Telegram first. It has been easier for several testers. Still report Discord issues if Discord was assigned or if it failed during setup.

### Do I run commands in TUI, PowerShell, or bash?

Run `openclaw ...` commands in PowerShell/bash/terminal. Use the TUI for chat prompts like `hello`, not for shell commands.

### What counts as install-smoke PASS?

Minimum PASS:

- installed/upgraded to the target version,
- version proof captured,
- Gateway status is understandable,
- one normal `hello` or short prompt gets a useful response,
- at least one assigned channel/surface is tested,
- no secrets leaked in evidence.

If Discord is blocked but TUI/Telegram works, report `PASS_WITH_CAVEAT` or `BLOCKED` depending on the assigned packet.

### Should I file directly upstream in `openclaw/openclaw`?

No, not by default. File in Herald Labs OpenclawQA or your assigned Discord thread. Herald Labs will validate, dedupe, and file/comment upstream through the approved account.

### What if I only have screenshots, not a video?

Screenshots are acceptable for simple install/status checks if they show the actual result. For sequence-dependent flows, screen recording is better. If you cannot record, say why and provide enough screenshots/logs to reconstruct the sequence.

### Can I post logs publicly?

Yes, if redacted. Remove API keys, tokens, private keys, passwords, private customer data, and full environment dumps. If a log contains secrets, summarize the relevant error instead.

### What if I am stuck and do not know what to send?

Send this:

```text
STATUS: BLOCKED
OS/platform:
Exact command I ran:
Exact error text:
Screenshot/log:
What I expected:
What happened instead:
Can I reproduce it again:
Secrets redacted: yes/no
```

### Why does Herald Labs keep asking for OS, version, and exact command?

Because most setup failures differ by OS, install path, package channel, and active model/provider route. Without those, the support loop becomes guesswork.

### Why should I not DM reports or keys?

Public per-tester threads keep the support context visible for the team and reusable for the next tester. Keys are the exception: if a key must be shared, it should use the approved key-handoff path, be acknowledged, then the key-bearing message should be deleted with a receipt.

### What if npm beta is stale?

Report it as a packaging blocker. Include:

```bash
npm view openclaw@beta version
npm install -g openclaw@beta
openclaw --version
```

If the observed version is not the target in your packet, do not mark the target beta as installed.

### What if the bot replies twice or in the wrong channel/thread?

Report it. Include screenshots with timestamps/message IDs and say where you expected the reply to land. Duplicate/wrong-target delivery is exactly the kind of human-visible issue this QA layer is meant to catch.

### What if OpenClaw says success but nothing visible happened?

Report it as a silent/false-success issue. Include the command/output and what visible result was missing.

## Field notes used to build this guide

This guide was built from the Herald Labs setup-help threads and channel readback, including:

- onboarding and setup links in `#general`, `#introductions`, and `#openclaw`,
- Samuel/Gboye install-start thread,
- Miriam Windows/key/model-precedence thread,
- Ayomide Discord and Telegram setup sequence,
- Anny gateway/auth/delivery blocker thread,
- Gabriel Windows gateway/config/Crestodian blocker thread,
- the later remote-help/Tailscale safety discussion.

The repeated lessons were simple: keep commands out of TUI, capture exact outputs, use Telegram when Discord blocks the smoke, treat model-route mismatch separately from key validity, and never leak credentials. Boring rules. Useful ones usually are.
