# QA Checklist — OpenClaw `v2026.6.2-beta.1`

Generated: `2026-06-04T01:08:00Z`
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.2-beta.1
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.2-beta.1
Baseline: prior prerelease `v2026.6.1-beta.3`; stable `v2026.6.1`.

## Gate status

- Status: `REVIEW_READY_WITH_CAVEATS`.
- Public dispatch: **not approved yet**.
- Upstream issue filing: disabled unless separately approved.
- Active cohort caveat: Samuel and Gabriel still have unresolved beta2 close/blocker state; do not overload them with beta62 unless Henry/admin explicitly waives or assigns.
- Recommended first wave: Ayomide, Miriam, Anny. Hold Samuel/Gabriel until beta2 close/unblock decision.

## Evidence contract for every tester report

Every accepted report must include:

1. OS/platform/version and device notes.
2. Install or upgrade method and exact command used.
3. OpenClaw version/tag observed after install/upgrade.
4. Provider/model route if any model call is exercised.
5. Human-visible evidence: screenshots or screen recording for the path tested.
6. Expected vs actual behavior, plus a human trust/confusion note.
7. Logs for failures, redacted for secrets.
8. Secret exposure check: no raw API keys, SSH keys, tokens, private customer data, or unsanitized env dumps.

Verdicts: `PASS_COMPLETE`, `PASS_WITH_CAVEAT`, `INCOMPLETE_NEEDS_EVIDENCE`, `BLOCKED_NEEDS_HELP`, `FAIL_FILE_ISSUE`.

## Always-run Baseline P0

| ID | Scenario | Manual steps | Expected human-visible behavior | Evidence required | Fail / block criteria |
|---|---|---|---|---|---|
| P0-1 | Install/upgrade to beta62 | Upgrade from current install using the tester's normal path (`npm install -g openclaw@beta`, official installer, or documented update flow). | Install completes without unclear false success; version points at `2026.6.2-beta.1` or an explicit mismatch is reported. | Command, version output, screenshot/log. | Install fails, version remains older without explanation, or success is claimed without version proof. |
| P0-2 | First useful response | Start OpenClaw and send a simple `hello` / short user request. | User sees one coherent useful response in the intended surface. | Screenshot or short log snippet of prompt + response. | No response, duplicate finals, internal trace leak, or confusing provider/model failure. |
| P0-3 | One configured messaging channel | Use the tester's assigned channel: Discord thread, Telegram, or other configured channel. | Reply lands in the correct human-visible target; parent/thread isolation is preserved; no duplicate preview/final spam. | Screenshot with channel/thread context and timestamp. | Message lands in wrong channel/thread, duplicates, silent drop, or confusing partial progress. |
| P0-4 | Plugin/tool visibility sanity | Run tool/plugin list or use one safe configured plugin/tool. | Expected tools/plugins are visible and usable, or unavailable state is clearly explained. | Screenshot/log of list/use result. | Tool silently omitted, unreadable tool breaks the whole list, or unsafe install prompt is unclear. |
| P0-5 | Harmless failure clarity | Trigger a safe bad config/provider/model/plugin command that cannot leak secrets. | Error is understandable and actionable; no raw secret is printed. | Screenshot/log of error and tester's judgment. | Silent false success, stack trace only, secret exposure, or no recovery hint. |
| P0-6 | Report/evidence flow | Submit report in Discord thread or OpenclawQA issue with evidence. | Report has enough detail to triage without private DMs. | Link/message ID/issue URL. | Evidence inaccessible, missing OS/version/steps, or asks tester to file upstream directly without approval. |

## Core Baseline P1

These are mandatory unless marked `NOT_RUN` with reason, owner, and next action.

| ID | Scenario | Manual steps | Expected behavior | Evidence required | Priority |
|---|---|---|---|---|---|
| P1-1 | Restart/gateway persistence | Restart gateway/session after upgrade, then repeat one simple request. | State survives restart; gateway status is clear. | `openclaw gateway status` plus before/after evidence. | P1 |
| P1-2 | Safe plugin lifecycle | Install or update one safe package/marketplace/source plugin using the new operator policy surface. | Operator decision is understandable; doctor/CLI/ClawHub surfaces agree. | Screenshots/logs of prompt, decision, result. | P1 |
| P1-3 | Provider/model route visibility | Use a configured provider/model and capture the shown route. | Route is visible enough for support/debug; no false provider claim. | Screenshot/log. | P1 |
| P1-4 | Config/session continuity | Confirm a setting/channel/provider remains after session restart/update. | Continuity is preserved or failure is clearly explained. | Before/after screenshot/log. | P1 |
| P1-5 | Useful logs/status | When something fails, run the documented status/log command. | Logs help triage without leaking secrets. | Redacted status/log excerpt. | P1 |

## Release-delta coverage matrix

| Delta group | Release signal | Behavior / risk | Manual test | Expected result | Evidence | Priority | Disposition |
|---|---|---|---|---|---|---|---|
| D0 Plugin operator install policy | Release notes: plugin/security path replaces dangerous-code scanner with operator install policy; package/archive/source/upload/marketplace lifecycle (#89516). | Human may see new install prompts, doctor checks, or ClawHub metadata; unsafe/confusing plugin flows can block adoption. | Install or update one safe plugin; if possible also attempt one intentionally unsupported/unreadable plugin metadata path. Judge prompt clarity and recovery. | Clear allow/deny decision, no silent unsafe install, doctor/CLI surfaces agree. | Prompt screenshots, command output, trust note. | P0/P1 | `TESTED` by assigned plugin-lifecycle tester. |
| D1 Messaging/outbound durability | Release notes: Discord/Telegram/Feishu/WhatsApp duplicate mirrors, Telegram admin writeback, streamed finals, approval allowlists, poll modifiers, Discord voice errors, progress traces (#88973, #89626, #89812, #89035, #89814, #89813, #89601). | Messages may duplicate, land in wrong target, hide final output, or expose internal progress. | In an assigned human-visible channel, send one normal request and one harmless failure; observe preview/final behavior and target routing. | Exactly one final answer in correct target; previews do not duplicate final; errors are human-readable. | Channel screenshot or recording with message IDs/timestamps. | P0 | `TESTED` by Discord/Telegram assigned testers. |
| D2 Chat/UI/Workboard/WebChat surfaces | Release notes: preserve visible streaming text, reconcile completed sends, ACK timing metadata, Workboard keyboard movement/dialog a11y, current chat toggles (#89801, #89777, #89802). | User can think a send failed, duplicate, or navigate the wrong card/session. | Use one visible UI surface available to tester: send a prompt, watch streaming/final state, navigate Workboard card if available, note ACK timing or confusion. | Visible stream/final is coherent; completed send reconciles; navigation works or unavailable is documented. | Screenshot/recording plus trust note. | P1/P2 | `GROUPED` under UI tester card. |
| D3 Security/policy/config recovery | Release notes: reject corrupt shell snapshots, unsupported policy keys, unsafe exec precheck envs, malformed script limits, suspicious gateway startup configs (#89701, #87074, #81488, #87056, #89480). | Bad local config can produce unsafe behavior or inscrutable failures. | Trigger one safe malformed config/policy value or use a documented harmless bad provider/model config. | OpenClaw rejects it safely with actionable text and no secrets. | Redacted error screenshot/log. | P0/P1 | `TESTED` by harmless-failure card. |
| D4 Gateway/agent/provider/model recovery | Release notes: session write-lock release failures, abandoned Codex app-server startup, custom-provider runtime fanout, bundled aliases, prompt-cache boundaries, Gemini stop sequences, Kimi cache markers (#89811, #89244). | Requests can hang, use wrong provider/model, or fail after restart. | Use configured provider route; restart gateway; run simple request; capture model/provider route and errors. | No hang; route is clear; restart recovers. | Status/log screenshot and first-response proof. | P1 | `GROUPED` under restart/provider card. |
| D5 Release/packaging/Windows assets | Release notes: Windows installer publishing, verified release asset links, npm package and registry tarball. | Windows testers may install wrong package/version or hit stale beta channel. | On Windows, verify npm package `openclaw@beta` / installer points to `2026.6.2-beta.1`; install/upgrade; capture version. | Latest beta package available and installed; if not, report packaging blocker. | Command screenshots for `npm view`, install, version. | P0 | `TESTED` by Windows testers. |
| D6 Memory/build/update and optional deps | Release notes: watcher pressure warnings, optional Baileys image backends, plugin repair fetch failures nonblocking, Skill Workshop view switching. | Lower-risk regressions may appear as warnings or broken optional features. | If the tester naturally sees warnings/Skill Workshop/plugin repair, record expected vs actual; otherwise mark `NOT_RUN` with reason. | Warnings are understandable and nonblocking. | Screenshot/log if encountered. | P2 | `NO_MANUAL_TEST_NEEDED` unless surface is available. |

## Recommended tester cards

### Ayomide — Windows install/backup/provider route

- Install/upgrade to `v2026.6.2-beta.1` using npm/normal Windows route.
- Capture `npm view openclaw@beta version`, `openclaw --version`, `openclaw gateway status`.
- Send one TUI `hello` and note provider/model route if visible.
- Trigger one harmless provider/model failure and judge error clarity.
- Evidence: screenshots/log snippets; no raw keys.

### Miriam — Windows packaging + SSH/backup continuity

- Verify beta62 package availability on Windows.
- Upgrade/install and capture version/gateway status.
- Confirm prior backup/SSH-key guidance remains safe: no raw keys in evidence; backup path visible if relevant.
- Run one restart/gateway persistence check.
- Evidence: screenshots/log snippets and trust/confusion note.

### Anny — Telegram/outbound delivery + report quality

- Upgrade/install to beta62 if available.
- Verify TUI `hello` and Telegram bot reply in the existing thread/channel flow.
- Observe whether Telegram progress/final output duplicates or leaks internal traces.
- Trigger one harmless failure and record clarity.
- Evidence: Telegram screenshots, TUI/version screenshot, report PDF or issue.

### Samuel — hold unless admin assigns

- Current beta2 state is unresolved/no-response. If Henry/admin assigns anyway: run straight-path install/version/TUI/channel smoke only and ask for PASS/BLOCKED/ETA.

### Gabriel — hold until blocker is resolved or live help is scheduled

- Current state: installed/testing but blocked/stale after wrong GitHub clone path and npm beta reinstall guidance. If Henry/admin assigns beta62 anyway: first resolve npm install/version/gateway/TUI `hello`, then beta62 package check.

## Readiness rule

This beta is **not cohort-ready** until:

- Every dispatched tester has `PASS_COMPLETE` or `PASS_WITH_CAVEAT`, or Henry/admin explicitly waives/closes them.
- Any P0 blocker is resolved or filed/deduped as an upstream issue through the approved account.
- Evidence is accessible and reviewed; screenshots/video are actually inspected, not accepted from title alone.
