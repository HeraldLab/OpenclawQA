# QA Checklist — OpenClaw `v2026.6.5-beta.1`

Generated: `2026-06-06T11:00:00Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.5-beta.1  
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.1  
Baseline: prior prerelease `v2026.6.2-beta.1`; stable `v2026.6.1`.

## Gate status

- Status: `REVIEW_READY_WITH_CAVEATS`.
- Public tester dispatch: **not approved yet**.
- Upstream issue filing: disabled unless separately approved.
- Required dispatch model: **one packet per tester in their fixed per-person thread**. Do not send beta packets to cohort-wide `#openclaw`.
- Recommended first wave: **Ayomide, Mariam, Anny**.
- Hold Samuel/Gabriel unless Henry/admin explicitly waives the unresolved beta62/beta2 follow-up state.

## Fixed tester dispatch threads

| Tester | Fixed thread | Use for beta packets? | Notes |
|---|---:|---|---|
| Ayomide | `1511072287250714626` | Yes | Use this same thread for every beta packet unless Henry overrides. |
| Mariam | `1510234021052026880` | Yes | Use this same thread for every beta packet unless Henry overrides. |
| Anny | `1511072288412405980` | Yes | Henry corrected this as the right Anny thread; do not use old `1511018659131297933`. |
| Samuel | `1511072249715888359` | Hold by default | Resume only if explicitly assigned/waived. |
| Gabriel | `1511072287690981468` | Hold by default | Resume only if explicitly assigned/waived. |

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
9. Secret exposure check: no raw API keys, SSH keys, tokens, private customer data, cookies, passwords, or unsanitized env dumps.

Verdicts: `PASS_COMPLETE`, `PASS_WITH_CAVEAT`, `INCOMPLETE_NEEDS_EVIDENCE`, `BLOCKED_NEEDS_HELP`, `FAIL_FILE_ISSUE`.

## Always-run Baseline P0

| ID | Scenario | Manual steps | Expected human-visible behavior | Evidence required | Fail / block criteria |
|---|---|---|---|---|---|
| P0-1 | Install/upgrade to beta665 | Upgrade from current install using tester's normal path (`npm install -g openclaw@beta`, official installer, or documented update flow). Capture the package/version before and after. | Install completes without unclear false success; version points at `2026.6.5-beta.1` or mismatch is reported. | Command screenshot/log, `openclaw --version`, package/version proof. | Install fails, version remains older without explanation, or success is claimed without version proof. |
| P0-2 | First useful response | Start OpenClaw and send a simple `hello` / short user request. | User sees one coherent useful response in the intended surface. | Screenshot or recording of prompt + response. | No response, duplicate finals, internal reasoning leak, or confusing provider/model failure. |
| P0-3 | Fixed per-person messaging thread | Use the tester's assigned Discord/Telegram/thread/channel. For Discord testers, use the fixed tester thread from this packet. | Reply lands in the correct human-visible target; parent/thread isolation is preserved; no duplicate preview/final spam. | Screenshot/recording with channel/thread context and timestamp/message ID. | Message lands in wrong channel/thread, duplicates, silent drop, or confusing partial progress. |
| P0-4 | Plugin/tool visibility sanity | Run tool/plugin list or use one safe configured plugin/tool. If no plugin is available, mark `NOT_RUN` with reason. | Expected tools/plugins are visible and usable, or unavailable state is clearly explained. | Screenshot/log of list/use result. | Tool silently omitted, unreadable tool breaks the whole list, or unsafe install prompt is unclear. |
| P0-5 | Harmless failure clarity | Trigger a safe bad config/provider/model/plugin command that cannot leak secrets. | Error is understandable and actionable; no raw secret is printed. | Screenshot/log of error and tester's judgment. | Silent false success, stack trace only, secret exposure, or no recovery hint. |
| P0-6 | Report/evidence flow | Submit report in the fixed tester thread and/or OpenclawQA issue with evidence link. | Report has enough detail to triage without private DMs. | Discord message link or GitHub issue URL. | Evidence inaccessible, missing OS/version/steps, or asks tester to file upstream directly without approval. |

## Core Baseline P1

Mandatory unless marked `NOT_RUN` with reason, owner, and next action.

| ID | Scenario | Manual steps | Expected behavior | Evidence required | Priority |
|---|---|---|---|---|---|
| P1-1 | Restart/gateway persistence | Restart gateway/session after upgrade, then repeat one simple request. | State survives restart; gateway status is clear; no restart loop. | `openclaw gateway status` plus before/after prompt evidence. | P1 |
| P1-2 | Provider/model route visibility | Use configured provider/model and capture any shown route/status. | Route is visible enough for support/debug; no false provider claim. | Screenshot/log, provider/model route if visible. | P1 |
| P1-3 | Config/session continuity | Confirm a setting/channel/provider remains after restart/update. | Continuity is preserved or failure is clearly explained. | Before/after screenshot/log. | P1 |
| P1-4 | Safe plugin lifecycle | Install/update/use one safe plugin/tool, or verify installed official plugin state. | Trusted pin/install state is durable; errors are understandable. | Screenshots/logs of prompt, decision, result. | P1 |
| P1-5 | Useful logs/status | When something fails, run the documented status/log command. | Logs help triage without leaking secrets. | Redacted status/log excerpt. | P1 |

## Release-delta coverage matrix

| Delta group | Release signal | Behavior / risk | Manual test | Expected result | Evidence | Priority | Disposition |
|---|---|---|---|---|---|---|---|
| D0 Channel reasoning/content boundary | QQBot strips reasoning/thinking scaffolding before native delivery (#89913, #90132); agents strip reasoning tags (#90051). | Internal `<thinking>` or reasoning scaffolding may leak to users in native channel replies. | In the fixed tester thread/channel, ask for a normal answer and one longer/tool-like answer. Watch the final visible reply. | Final reply contains user-facing answer only; no `<thinking>`, hidden chain, raw provider trace, or progress dump. | Screenshot/recording of channel reply. | Delta P0 | `TESTED` by every dispatched tester through channel P0. |
| D1 MCP/tool-result materialization | MCP tool results coerce `resource_link`, `resource`, `audio`, malformed image, and future blocks before provider conversion (#90710, #90728). | A tool/plugin returning rich content can poison session history or cause provider 400s. | Use one safe tool/plugin. If tool output includes file/link/media-like content, ask one follow-up after the tool result. | Tool result is readable; follow-up still works; no provider 400/malformed image failure. | Tool/plugin screenshot/log plus follow-up proof. | Delta P0/P1 | `TESTED` where plugin/tool is available; otherwise `NOT_RUN`. |
| D2 Anthropic/Codex/agent recovery after restart/cache expiry | Anthropic extended-thinking sessions recover after prompt-cache expiry or Gateway restart; stream starts wait for `message_start` (#90667, #90697). | Long/extended sessions may fail after restart, replay stale signatures, or silently hang. | Run first response, restart gateway/session, then send a second prompt in same session/surface if safe. | Second prompt returns or fails clearly; no hang, unsigned-thinking-only stall, or invisible final. | Before/after screenshots/status. | Delta P1 | `TESTED` by restart/provider card. |
| D3 Parallel web_search provider onboarding | Parallel is now bundled `web_search` provider with `PARALLEL_API_KEY` discovery, endpoint handling, cache-safe session ids, onboarding picker/docs (#85158). | Provider appears but is misconfigured, unavailable, or confusing; missing key may look like model failure. | If tester has Parallel configured, run one harmless web search or inspect provider/tool availability. If no key, confirm unavailable state is explicit. | Configured provider works; missing key says missing/unavailable clearly. | Screenshot/log of availability or search result. | Delta P1/P2 | `TESTED` by provider/tool tester if available. |
| D4 Google Vertex/static catalog/cooldown/memory status | Google Vertex ADC catalog rows, runtime resolution, single-provider cooldown recovery, memory adapter status checks (#90506, #90609, #90717, #90816). | Provider catalog can advertise wrong availability, cooldown may strand primary provider, status checks may mislead support. | If tester uses Google/Vertex or has model picker/status available, inspect route/status and run a simple model call. | Available route is truthful; unavailable/cooldown state is clear. | Screenshot/log of model/status and prompt result. | Delta P1/P2 | `TESTED` only on relevant provider environments. |
| D5 Matrix/voice/thread flows | Matrix voice-note preflight, mention gating, thread read/reply via relations pagination (#78016, #90415). | Voice/thread replies may land wrong, fail silently, or bypass mention gating. | If Matrix is configured, test one thread read/reply or voice-note preflight. Otherwise mark `NOT_RUN`. | Thread/voice behavior is visible and understandable. | Matrix screenshot/recording. | Delta P2 | Optional unless tester has Matrix. |
| D6 Auth and plugin install durability | Auth profiles now live in SQLite; official npm plugin install records keep trusted pins; prerelease fallback integrity avoids stale integrity (#89102, #88585). | Upgrade can lose auth/plugin state or install stale/corrupt prerelease fallback. | After upgrade, verify auth/profile/plugin status where available; run `npm view openclaw@beta version`; use one safe plugin/tool. | Auth/plugin state survives or gives clear migration; beta package is current. | Screenshots/logs. | Delta P0/P1 | `TESTED` by install/plugin cards. |
| D7 macOS node/direct Gateway session | macOS node mode no longer silently self-reconnects away from healthy direct Gateway session (#90668, #90815). | Companion app/node sessions can churn or attach to wrong gateway. | If macOS node mode is available, observe gateway connection before/after simple prompt/restart. | Healthy direct session persists; reconnection behavior is understandable. | macOS screenshot/status. | Delta P2 | Optional unless macOS tester assigned. |
| D8 Doctor/cron/service env/WhatsApp config reload | Cron legacy JSON stores migrate during doctor preflight; service env placeholders do not mask state-dir secrets; WhatsApp waits/reload bounded (#90072, #90208, #90277, #90488, #90486, #87951, #87965). | Upgrade may leave cron/config/service env broken or WhatsApp in restart/wait loop. | Run `openclaw doctor` or status command if safe; if WhatsApp configured, confirm startup/reload does not hang. | Doctor/status is actionable; no secret leakage; disabled/changed WhatsApp account is handled cleanly. | Redacted doctor/status screenshot/log. | Delta P1 | `TESTED` where available. |
| D9 TUI/chat/Workboard final-message stability | Optimistic user messages, stale history reloads, runId reassignment, abort windows, and Workboard lifecycle updates are stabilized (#86205, #89600, #88592, #90123). | User may think message vanished, duplicated, or wrong card/session updated. | In visible TUI/chat surface, send one prompt, wait for final, refresh/reopen if safe, and observe whether message remains stable. | User message and final answer remain visible exactly once. | Screenshot/recording. | Delta P1/P2 | `TESTED` by available UI tester. |
| D10 Security/config/tooling guards | MCP HTTP redirects, global agent config defaults, and release/test proof failures are guarded (#89732, #90145). | Unsafe redirects/defaults/proof failures can be hidden or confusing. | Trigger one safe unsupported config/provider/tool path; inspect error clarity and secret redaction. | Clear rejection/recovery; no secrets; no misleading success. | Redacted error screenshot/log. | Delta P0/P1 | `TESTED` through harmless-failure card. |

## Recommended first-wave tester cards

### Ayomide — Windows install/package + provider/tool visibility

Assigned thread: `1511072287250714626`

- Run `npm view openclaw@beta version`, install/upgrade, then capture `openclaw --version` and gateway/status output.
- Run one TUI/chat `hello`, then refresh/reopen if safe and verify the final answer remains visible once.
- Capture provider/model route if visible.
- Use one safe tool/plugin or mark `NOT_RUN` with reason.
- Trigger one harmless bad provider/model/config error and judge clarity.

### Mariam — Windows/gateway restart + auth/plugin continuity

Assigned thread: `1510234021052026880`

- Verify beta package/version and install/upgrade to `v2026.6.5-beta.1`.
- Run first useful response, restart gateway/session, then run a second response.
- Verify auth/profile/plugin status where available after restart/update.
- If previous key/provider blocker appears, separate provider outage from OpenClaw install failure.
- Trigger one harmless failure and check no secrets are exposed.

### Anny — fixed-thread channel delivery + no reasoning leak

Assigned thread: `1511072288412405980`

- Upgrade/install and capture version proof.
- In the fixed Anny thread/channel, send one normal request and one follow-up.
- Confirm reply stays in the correct thread, appears once, and contains no `<thinking>`, raw provider trace, or internal progress dump.
- Check one safe plugin/tool visibility path if available.
- Trigger one harmless failure and capture whether the user would know what to do next.

### Samuel — hold unless admin assigns

Current follow-up state is unresolved. If Henry/admin assigns anyway: straight-path install/version/TUI/channel smoke only, then ask for PASS/BLOCKED/ETA.

### Gabriel — hold unless admin assigns

Current blocker history includes provider/key/install confusion. If Henry/admin assigns anyway: first verify npm beta install/version/gateway/TUI `hello`, then classify provider/key failures separately.

## Readiness rule

This beta is **not cohort-ready** until:

- Every dispatched tester has `PASS_COMPLETE` or `PASS_WITH_CAVEAT`, or Henry/admin explicitly waives/closes them.
- Any P0 blocker is resolved or filed/deduped as an upstream issue through the approved process.
- Evidence is accessible and reviewed; screenshots/video are actually inspected, not accepted from title alone.
- Confirmed bugs are deduped before upstream filing; upstream filing needs separate approval.
