# QA Checklist — OpenClaw `v2026.6.5-beta.6`

Generated/repaired: `2026-06-09T10:18:00Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.5-beta.6  
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.6  
Baseline: prior prerelease `v2026.6.5-beta.5`; stable `v2026.6.1`.  
Release verification: package `openclaw@2026.6.5-beta.6`, integrity `sha512-jwz9IP/LbR6qgS5SUTpgeBArNf2eIM+8jc7LCEMAMQznsznjml/7IrsxBn2S89XieEX6BEhGVtjspOOJt0jVXg==`.

## Gate status

- Status: `REVIEW_READY_WITH_CAVEATS`.
- Public tester dispatch: **not approved yet** for `v2026.6.5-beta.6`.
- Upstream issue filing: disabled unless separately approved after dedupe/evidence review.
- Dispatch model: one packet per tester in the fixed per-person thread; do not send beta packets to cohort-wide `#openclaw`.
- Recommended first wave if Henry/admin approves: **Ayomide, Mariam, Anny**.
- Hold **Gabriel** until the security-audit blocker resolves or Henry/admin waives/closes it. Samuel can be assigned only if Henry/admin wants an additional install smoke lane.

## Fixed tester dispatch threads

| Tester | Fixed thread | Use for beta6 packets? | Notes |
|---|---:|---|---|
| Ayomide | `1511072287250714626` | Yes, if approved | Windows/package/provider evidence lane. |
| Mariam | `1510234021052026880` | Yes, if approved | Gateway/restart/auth/plugin continuity lane. |
| Anny | `1511072288412405980` | Yes, if approved | Fixed-thread/channel delivery and reasoning-leak lane. |
| Samuel | `1511072249715888359` | Optional hold | Prior beta62 accepted; assign only if admin wants broader install coverage. |
| Gabriel | `1511072287690981468` | Hold | Current blocker: gateway security-audit evidence pending; no raw secrets. |

## Evidence contract for every tester report

Every accepted report must include:

1. Tester handle and assigned thread.
2. OS/platform/version and device notes.
3. Install or upgrade method and exact command used.
4. OpenClaw version/tag observed after install/upgrade.
5. Provider/model route if a model call is exercised.
6. Human-visible evidence: screenshots or screen recording for the path tested.
7. Expected vs actual behavior, plus a human trust/confusion note.
8. Logs for failures, redacted for secrets.
9. Secret exposure check: no raw API keys, SSH keys, tokens, private customer data, cookies, passwords, `.env`, or unsanitized dumps.

Verdicts: `PASS_COMPLETE`, `PASS_WITH_CAVEAT`, `INCOMPLETE_NEEDS_EVIDENCE`, `BLOCKED_NEEDS_HELP`, `FAIL_FILE_ISSUE`.

## Always-run Baseline P0

| ID | Scenario | Manual steps | Expected human-visible behavior | Evidence required | Fail / block criteria |
|---|---|---|---|---|---|
| P0-1 | Install/upgrade to beta665.6 | Upgrade from current install using tester's normal path (`npm install -g openclaw@beta`, official installer, or documented update flow). Capture package/version before and after. | Install completes without unclear false success; version points at `2026.6.5-beta.6` or mismatch is reported. | Command screenshot/log, `openclaw --version`, package/version proof. | Install fails, version remains older without explanation, or success is claimed without version proof. |
| P0-2 | First useful response | Start OpenClaw and send a simple `hello` / short user request. | User sees one coherent useful response in the intended surface. | Screenshot or recording of prompt + response. | No response, duplicate finals, internal reasoning leak, or confusing provider/model failure. |
| P0-3 | Fixed per-person messaging surface | Use the tester's assigned Discord/Telegram/thread/channel. For Discord testers, use the fixed tester thread from this packet. | Reply lands in the correct human-visible target; parent/thread isolation is preserved; no duplicate preview/final spam. | Screenshot/recording with channel/thread context and timestamp/message ID. | Message lands in wrong channel/thread, duplicates, silent drop, or confusing partial progress. |
| P0-4 | Plugin/tool visibility sanity | Run tool/plugin list or use one safe configured plugin/tool. If no plugin is available, mark `NOT_RUN` with reason. | Expected tools/plugins are visible and usable, or unavailable state is clearly explained. | Screenshot/log of list/use result. | Tool silently omitted, unreadable tool breaks the whole list, or unsafe install prompt is unclear. |
| P0-5 | Harmless failure clarity | Trigger a safe bad config/provider/model/plugin command that cannot leak secrets. | Error is understandable and actionable; no raw secret is printed. | Screenshot/log of error and tester's judgment. | Silent false success, stack trace only, secret exposure, or no recovery hint. |
| P0-6 | Report/evidence flow | Submit report in the fixed tester thread and/or OpenclawQA issue with evidence link. | Report has enough detail to triage without private DMs. | Discord message link or GitHub issue URL. | Evidence inaccessible, missing OS/version/steps, or asks tester to file upstream directly without approval. |
| P0-7 | Package integrity sanity | Confirm `npm view openclaw@beta version` or install source matches `2026.6.5-beta.6`; note if beta channel has moved. | Tester knows exactly which beta they tested. | Screenshot/log of package/version source. | Tester accidentally validates an older/newer tag without caveat. |

## Core Baseline P1

Mandatory unless marked `NOT_RUN` with reason, owner, and next action.

| ID | Scenario | Manual steps | Expected behavior | Evidence required | Priority |
|---|---|---|---|---|---|
| P1-1 | Restart/gateway persistence | Restart gateway/session after upgrade, then repeat one simple request. | State survives restart; gateway status is clear; no restart loop. | `openclaw gateway status` plus before/after prompt evidence. | P1 |
| P1-2 | Provider/model route visibility | Use configured provider/model and capture any shown route/status. | Route is visible enough for support/debug; no false provider claim. | Screenshot/log, provider/model route if visible. | P1 |
| P1-3 | Config/session continuity | Confirm a setting/channel/provider remains after restart/update. | Continuity is preserved or failure is clearly explained. | Before/after screenshot/log. | P1 |
| P1-4 | Safe plugin lifecycle | Install/update/use one safe plugin/tool, or verify installed official plugin state. | Trusted pin/install state is durable; errors are understandable. | Screenshots/logs of prompt, decision, result. | P1 |
| P1-5 | Useful logs/status | When something fails, run the documented status/log command. | Logs help triage without leaking secrets. | Redacted status/log excerpt. | P1 |
| P1-6 | Evidence review path | Link the Discord thread message and any GitHub issue/evidence artifact. | QA operator can open, review, and timestamp proof. | Issue URL / message ID / attachment link. | P1 |

## Release-delta coverage matrix

| Delta group | Release signal / commit group | Behavior / risk | Manual human test | Expected result | Evidence | Priority | Disposition |
|---|---|---|---|---|---|---|---|
| D0 Channel reasoning boundary | QQBot strips reasoning/thinking scaffolding; agent/channel stripping (#89913, #90132, #90051). | Internal `<thinking>` or provider trace can leak into native channel replies. | In fixed tester channel/thread, ask one normal and one longer/tool-like question; inspect final visible answer. | User-facing answer only; no `<thinking>`, hidden chain, raw trace, or progress dump. | Screenshot/recording of final channel replies. | Delta P0 | `GROUPED` with P0-2/P0-3 for every dispatched tester. |
| D1 MCP/tool-result materialization | MCP `resource_link`, `resource`, `audio`, malformed image, and future blocks coerced before provider conversion (#90710, #90728). | Rich tool results can poison session history or trigger provider 400s. | Use one safe tool/plugin. If output includes link/file/media-like content, ask a follow-up after the tool result. | Tool result remains readable and follow-up still works. | Tool/plugin output and follow-up proof. | Delta P0/P1 | `TESTED` where tool/plugin available; otherwise `NOT_RUN`. |
| D2 Anthropic/Codex/agent recovery | Extended-thinking recovery after cache expiry/restart; stream waits for `message_start`; stale signatures/empty completions handled (#90667, #90697, #90163, #90108, #89874, #89505, #90632, #89302, #90729, #90317, #90319). | Session may hang, silently retry forever, lose final, or replay stale thinking after restart/compaction. | Run response, restart gateway/session if safe, send second prompt in same surface; note recovery text if failure occurs. | Second prompt returns or fails clearly; no invisible final or unsigned-thinking stall. | Before/after screenshots/status. | Delta P1 | `GROUPED` with P1-1/P1-2. |
| D3 Provider onboarding and route truth | Parallel bundled `web_search`; Google Vertex ADC/static catalog/cooldown/model status; Codex aliases/model visibility; Ollama metadata (#85158, #90506, #90609, #90717, #90816, #90702, #91125). | Provider picker/status can advertise unavailable routes or hide missing keys/cooldowns. | Inspect provider/model route; if Parallel/Google/Vertex available, run one harmless search/model call; otherwise capture explicit unavailable/missing-key state. | Availability is truthful; missing/cooldown state is clear. | Provider/status screenshot/log and prompt result. | Delta P1 | `TESTED` on relevant provider environments. |
| D4 Matrix/native channel flows | Matrix voice preflight and thread relations; Google Chat native approval cards; WhatsApp bounded waits/reload; Feishu retry/streaming cards; Discord adapter resolution (#78016, #90415, #87951, #87965, #90486, #89659, #90858). | Replies/cards/voice/thread behavior can land wrong, hang, or fail silently. | If configured, test one native channel action: thread reply, voice preflight, approval card, or restart/reload. | Visible channel behavior is correct and understandable. | Channel screenshot/recording/message IDs. | Delta P1/P2 | Optional unless tester has channel. |
| D5 Auth/plugin/ClawHub durability | Auth profiles to SQLite; official npm plugin pins; prerelease fallback integrity; ClawHub GitHub-backed skill install; watcher count reduction (#89102, #88585, #90478). | Upgrade can lose auth/plugin state, trust pins, or install stale/corrupt fallback. | After upgrade, verify auth/profile/plugin state; use/install one safe official plugin or ClawHub skill if already approved. | State survives or migration failure is clear; no unsafe prompt. | Plugin/auth/status screenshots. | Delta P0/P1 | `TESTED` by plugin/auth lane. |
| D6 macOS/mobile/gateway UX | macOS node direct Gateway session stability; duplicate probe warning identity; Android/iOS diagnostics/settings rows; node pairing rate limit (#90668, #90815, #85791, #90147, #90752, #91201). | Companion app/gateway can churn, reconnect unexpectedly, or hide diagnostics. | On macOS/mobile if available, observe gateway status before/after prompt/restart. | Healthy direct session persists; diagnostics remain reachable. | Status screenshot/recording. | Delta P2 | Optional platform-specific. |
| D7 Cron/update/service env migrations | Cron legacy stores migrate during doctor preflight; service env placeholders no longer mask state-dir secrets; transcript markers preserved; WhatsApp disabled account teardown (#90072, #90208, #91230, #90277, #90488). | Upgrade may strand cron/config/service env or mask secrets with placeholders. | Run `openclaw doctor` or safe status command; if WhatsApp configured, observe startup/reload. | Status is actionable; no secret leakage; no endless wait. | Redacted doctor/status screenshot/log. | Delta P1 | `TESTED` where available. |
| D8 TUI/chat/Workboard/session stability | Optimistic messages, stale history reloads, runId reassignment, abort windows, Workboard lifecycle, message-tool delivery (#86205, #89600, #88592, #90123). | User message/final can vanish, duplicate, jump sessions/cards, or not count as delivery. | Send prompt in TUI/chat; refresh/reopen if safe; inspect message and final stability. | User message and final remain visible once in the right session/card. | Screenshot/recording before/after refresh. | Delta P1/P2 | `TESTED` by UI lane. |
| D9 Security/config/transcript guards | Owner-only HTTP tools gated; MCP redirect guard; global agent config defaults; inline image payload redaction; release/test proof failures bounded (#90261, #89732, #90145, #91529). | Unsafe tools/redirects/defaults or raw image/data URLs can leak or fail unclearly. | Trigger one safe unsupported config/tool/provider path; inspect rejection and redaction. | Clear rejection/recovery; no secrets or raw image bytes exposed. | Redacted error screenshot/log. | Delta P0/P1 | `GROUPED` with P0-5 secrets/failure test. |
| D10 Release/CI/package proof | Release CI/package proof links supplied; npm Telegram beta E2E not supplied; ClawHub publish dispatched separately, not awaited. | Package proof can look complete while a channel/plugin lane lacks runtime validation. | Tester must still perform human install/channel/plugin proof; do not accept CI links alone. | Human evidence confirms package works in real setup. | Version, install, channel, plugin evidence. | Delta P0 | `TESTED` through P0/P1; CI is supporting evidence only. |

## Recommended first-wave tester cards

### Ayomide — Windows install/package + provider/tool visibility

Assigned thread: `1511072287250714626`

- Run `npm view openclaw@beta version`, install/upgrade, then capture `openclaw --version` and gateway/status output.
- Run one TUI/chat `hello`, then refresh/reopen if safe and verify the final answer remains visible once.
- Capture provider/model route; if Parallel/Google/Vertex/other provider is configured, capture truthfulness of availability or missing-key/cooldown state.
- Use one safe tool/plugin or mark `NOT_RUN` with reason.
- Trigger one harmless bad provider/model/config error and judge clarity/secrets.

### Mariam — Windows/gateway restart + auth/plugin continuity

Assigned thread: `1510234021052026880`

- Verify beta package/version and install/upgrade to `v2026.6.5-beta.6`.
- Run first useful response, restart gateway/session, then run a second response in the same surface.
- Verify auth/profile/plugin status where available after restart/update.
- Run `openclaw doctor` or safe status command and redact secrets.
- If a provider/key blocker appears, separate provider outage from OpenClaw install failure.

### Anny — fixed-thread channel delivery + no reasoning leak

Assigned thread: `1511072288412405980`

- Upgrade/install and capture version proof.
- In the fixed Anny thread/channel, send one normal request and one follow-up.
- Confirm reply stays in the correct thread, appears once, and contains no `<thinking>`, raw provider trace, or internal progress dump.
- Check one safe plugin/tool visibility path if available.
- Trigger one harmless failure and capture whether the user would know what to do next.

### Samuel — optional install smoke only if admin assigns

If Henry/admin assigns Samuel, keep it narrow: install/version/TUI/channel smoke plus one harmless failure and evidence link.

### Gabriel — hold unless admin resolves/waives blocker

Current blocker: gateway security-audit evidence still pending. Do not assign beta6 until Gabriel replies with PASS + redacted gateway audit outputs/diagnostics, `BLOCKED_SECURITY`, `BLOCKED` + exact command/error/screenshot, ETA, or Henry/admin waives/closes.

## Readiness rule

This beta is **not cohort-ready** until:

- Every dispatched tester has `PASS_COMPLETE` or `PASS_WITH_CAVEAT`, or Henry/admin explicitly waives/closes them.
- Any P0 blocker is resolved or filed/deduped as an upstream issue through the approved process.
- Evidence is accessible and reviewed; screenshots/video are actually inspected, not accepted from title alone.
- Confirmed bugs are deduped before upstream filing; upstream filing needs separate approval.
- Gabriel's blocker is resolved/waived before counting the overall cohort ready.
