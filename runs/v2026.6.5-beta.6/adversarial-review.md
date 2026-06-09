# Adversarial Review — OpenClaw `v2026.6.5-beta.6`

Generated/repaired: `2026-06-09T10:18:00Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.5-beta.6

## Verdict

`REVIEW_READY_WITH_CAVEATS` — the initial workflow produced stub `qa-checklist.md` and `adversarial-review.md` files. This review repaired the release gate by adding baseline P0/P1 coverage, release-delta human scenario cards, fixed per-person thread routing, evidence requirements, and first-wave recommendations for `v2026.6.5-beta.6`. Public dispatch still requires Henry/admin approval.

## Hard blockers before dispatch

| Blocker | Status | Required action |
|---|---|---|
| Public dispatch approval | Not approved | Send approval packet to thread `1511147437329485977`; wait for `APPROVE DISPATCH`, `CHANGE: ...`, or `BLOCK: ...`. |
| Correct tester threads | Defined | Use Ayomide `1511072287250714626`, Mariam `1510234021052026880`, Anny `1511072288412405980`. Do not use Anny old thread `1511018659131297933`. |
| Active Gabriel blocker | Open | Hold Gabriel until security-audit evidence arrives, or Henry/admin explicitly waives/closes. Latest follow-up before this review: `1513834231233642506`. |
| Evidence review | No reports yet | Do not mark beta665.6 ready until reports are evidence-reviewed, not merely self-declared PASS. |
| Upstream issue filing | Disabled | File/comment upstream only after dedupe and separate approval or explicit policy. |
| CI/proof caveat | Partial | Release verification links exist, but npm Telegram beta E2E was not supplied and ClawHub publish was dispatched separately/not awaited; human channel/plugin proof remains required. |

## Rubric review

| Rubric item | Result | Notes |
|---|---|---|
| Baseline P0 included | PASS | Install/upgrade, version proof, first response, fixed messaging/thread delivery, plugin/tool visibility, harmless failure, report flow, package integrity, secrets check. |
| Core P1 included | PASS | Restart/gateway persistence, provider/model route, config/session continuity, plugin lifecycle, useful logs/status, evidence review path. |
| Release-specific delta included | PASS | Reasoning leak prevention, MCP rich-result coercion, Anthropic/Codex restart recovery, Parallel/Google provider state, Matrix/native channels, auth/plugin/ClawHub durability, macOS/mobile gateway UX, cron/service env migrations, TUI message stability, security/config/transcript guards, package proof caveats. |
| Commit/release coverage matrix | PASS_WITH_CAVEAT | Uses coherent release-note/PR groups from `release-context.md`. This is acceptable for human QA if dispatch cards cover the grouped behavior risks; not a substitute for automated per-commit CI proof. |
| Human scenario quality | PASS | Requires human observation of visible output, thread routing, duplicate/missing finals, reasoning leaks, recovery text, and trust/confusion. Not satisfiable by invisible agent automation alone. |
| Evidence requirements | PASS | Requires screenshots/recordings/logs, expected vs actual, secret check, message IDs/issue links, and accessible evidence. |
| Tester assignment realism | PASS_WITH_CAVEAT | First wave avoids Gabriel because blocker remains open; Samuel optional only by admin assignment. |
| Duplicate public-send risk | PASS | Approval packet goes to approval thread only; dispatch held; per-person thread map is explicit. |

## Highest-risk release deltas

1. **Reasoning/thinking content boundary**
   - Risk: internal model reasoning leaks into user-visible channel replies.
   - Required human proof: visible channel screenshots showing final answers without `<thinking>`/trace/progress dump.

2. **MCP/tool rich-result materialization**
   - Risk: tool results with resources/audio/malformed image blocks cause provider 400s or corrupt session history.
   - Required human proof: safe tool/plugin output plus follow-up response after tool result.

3. **Restart/provider/agent recovery**
   - Risk: gateway restart, prompt-cache expiry, stale thinking signatures, or compaction handoffs create hangs, invisible finals, or misleading retries.
   - Required human proof: before/after restart prompt and status evidence.

4. **Provider/plugin/auth durability**
   - Risk: auth profiles, trusted plugin pins, ClawHub installs, prerelease fallback integrity, or provider catalog/cooldown state become misleading after upgrade.
   - Required human proof: package/version/status/plugin/provider screenshots.

5. **Thread/channel routing**
   - Risk: beta comms and OpenClaw replies land in wrong parent/thread; duplicate finals or hidden errors return.
   - Required human proof: fixed tester thread screenshots/message IDs.

6. **Cron/service env/channel migration**
   - Risk: upgrade silently breaks cron stores, masks state-dir env secrets with placeholders, or strands WhatsApp/native channel startup/reload.
   - Required human proof: doctor/status or configured channel proof where available.

## Negative tests to require

- One harmless bad provider/model/config/plugin path.
- One fixed-thread channel request with exact target/thread verification.
- One restart after upgrade before a second request.
- One plugin/tool visibility or rich-output sanity check.
- One visible-output inspection for reasoning/progress/trace leakage.
- One evidence privacy check before upload.

## Dispatch recommendation

Recommended approval ask:

> Approve Ada/SuperAda to dispatch `v2026.6.5-beta.6` first-wave packets to Ayomide, Mariam, and Anny in their fixed per-person threads. Hold Gabriel until the security-audit blocker resolves or Henry/admin explicitly waives/closes. Samuel remains optional by admin assignment.

Reason: latest beta is real and the packet is now release-depth/human-QA ready, but Gabriel's unresolved blocker makes a 3-person first wave cleaner than all-active dispatch.

## What would make this fail review

- Sending tester packets before approval.
- Sending to cohort-wide `#openclaw` instead of fixed per-person tester threads.
- Sending Anny's packet to old thread `1511018659131297933`.
- Dispatching a generic install-only smoke without release-delta cards.
- Counting a PDF/issue as PASS without evidence review.
- Accepting reports that omit version/tag, OS, install method, channel/thread evidence, harmless failure result, or secrets check.
- Filing upstream bugs directly from tester claims without dedupe/approval.

## Final review status

`REVIEW_READY_WITH_CAVEATS`; not public-dispatched.
