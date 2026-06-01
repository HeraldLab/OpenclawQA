# Manual QA Checklist — OpenClaw `v2026.6.1-beta.1`

Status: **DRAFT — pending human sign-off before dispatch**  
Freshness recheck: `2026-06-01T16:48:47Z`  
Target: `v2026.6.1-beta.1`  
Stable upgrade baseline: `v2026.5.28`  
Prior prerelease baseline: `v2026.5.31-beta.4`

Each row must return `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN`, with evidence references.

| ID | Area | Preconditions | Action | Expected result | Evidence required | Priority |
|---|---|---|---|---|---|---|
| P0-01 | Fresh install | Clean machine/user env or isolated profile | Install OpenClaw `v2026.6.1-beta.1` using normal documented path | Install completes; version/tag can be verified as `v2026.6.1-beta.1` | screen recording, command transcript, version output, OS/version | P0 |
| P0-02 | Stable upgrade | Existing OpenClaw `v2026.5.28` install | Upgrade to `v2026.6.1-beta.1` | Upgrade completes without corrupting config/session state | screen recording, before/after version, logs | P0 |
| P0-03 | Prior prerelease upgrade | Existing `v2026.5.31-beta.4` install | Upgrade to `v2026.6.1-beta.1` | Upgrade completes; no duplicate services/sessions caused by prerelease churn | screen recording, before/after version, process/service list | P0 |
| P0-04 | First-run response | `v2026.6.1-beta.1` installed, provider configured | Start OpenClaw and send one normal prompt | One coherent response returns; no tool/runtime scaffolding leaks | recording, prompt/response, logs | P0 |
| P0-05 | Provider/model routing | Known provider/model route configured | Confirm selected provider/model route and run one request | Request uses intended provider/model; wrong-route errors are understandable | route config redacted, model/provider output, logs | P0 |
| P0-06 | Messaging delivery | Discord or Telegram configured | Send/receive one OpenClaw response in human-visible channel | Message reaches correct channel; no `chat_id` routing bleed | channel screenshot, logs, redacted config | P0 |
| P0-07 | `message.send` sanitization regression | Messaging/tool execution enabled; weaker model route if available | Prompt flow likely to invoke/send message; inspect tool args/logs | No runtime scaffolding leak; no private routing values exposed | redacted logs, screenshots, finding block if leak occurs | P0 |
| P1-01 | Telegram progress ordering | Telegram configured | Run a tool-heavy prompt that emits interleaved progress | Progress remains ordered/readable; final answer not overwritten | recording/screenshots, bot logs | P1 |
| P1-02 | Plugin/runtime visibility | MCP/plugins/tools configured | List/use configured tools/plugins | Configured tools are visible; no silent omission/confabulation | tool list, config excerpt redacted, logs | P1 |
| P1-03 | Exec/tool metadata | Safe command/tool available | Run harmless exec/tool action | Tool details include understandable status/termination metadata | transcript/logs | P1 |
| P1-04 | Memory/session persistence | Long-ish conversation available | Continue after restart/compaction if available | Critical instruction survives; no unrelated session bleed | transcript excerpt, session IDs redacted | P1 |
| P1-05 | UI/chat send reset | Control UI/chat available | Send message from UI | Composer clears after send; response stream remains stable | recording/screenshots | P1 |
| P1-06 | Sleep/reconnect resilience | Desktop/laptop test machine | Start run, sleep/wake or disconnect/reconnect | Gateway/session recovers or fails clearly | recording, logs, timestamps | P1 |
| P2-01 | Diagnostics quality | Any failed/blocked scenario | Capture diagnostic output | Error is actionable; no secrets leaked | logs/screenshots | P2 |

## Submission requirements

Each tester submission must include:

- exact OpenClaw version/tag
- OS and OS version
- install method
- model
- provider / routing chain
- additional provider/model setup details where relevant
- checklist item statuses
- screen recording link
- logs
- screenshots where useful
- redacted config/setup details
- one separated finding block per potential bug
