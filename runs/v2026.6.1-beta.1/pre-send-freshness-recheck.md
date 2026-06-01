# Pre-send Freshness Recheck — OpenClaw `v2026.6.1-beta.1`

Checked at: `2026-06-01T16:48:47Z`

## Target decision

- Current selected target: `v2026.6.1-beta.1`
- Latest beta tag: `v2026.6.1-beta.1`
- Latest alpha tag: `v2026.6.1-alpha.2`
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.6.1-beta.1
- Superseded before tester send: **NO**

## Decision

PASS: target remains current. Tester instructions may proceed after checklist/review/human sign-off.

## Recent open issue watchlist

- #87938 [Bug]: Feishu DM sessions rebuilt after gateway restart — duplicate keys + maintenance pruning — https://github.com/openclaw/openclaw/issues/87938
- #75767 openclaw gateway restart hangs on macOS with SMB-mounted volumes (lsof stat() timeout) — https://github.com/openclaw/openclaw/issues/75767
- #77717 Feishu channel: bot identity recovery race condition causes permanent disconnection — https://github.com/openclaw/openclaw/issues/77717
- #85692 Feishu agent intermittently returns replies=0 (silent failure, no error logged) — https://github.com/openclaw/openclaw/issues/85692
- #89139 webchat creates new agent run per message, destroying prompt cache (93% → 29% hit rate) — https://github.com/openclaw/openclaw/issues/89139
- #88039 [Bug]: Session-selected model incorrectly included in fallback list in v2026.5.26 — https://github.com/openclaw/openclaw/issues/88039
- #88128 [Bug]: Internal messages surface in Telegram chat — https://github.com/openclaw/openclaw/issues/88128
- #89147 Native hook relay starves mid-turn after long model-thinking gap (renewal loop tool-call-driven) — https://github.com/openclaw/openclaw/issues/89147


## Recent open PR watchlist

PRs are risk signals only; they are not proof of shipped content in `v2026.6.1-beta.1`.

- PR #89143 draft=False fix(agents): stabilize message send loop detection — https://github.com/openclaw/openclaw/pull/89143
- PR #89138 draft=False fix #88009: [Feature]: batched memory embedding should batch over files — https://github.com/openclaw/openclaw/pull/89138
- PR #88875 draft=False docs: document markdown and shared helpers — https://github.com/openclaw/openclaw/pull/88875
- PR #89128 draft=False fix: skip Responses item id replay without store — https://github.com/openclaw/openclaw/pull/89128
- PR #85982 draft=False fix(models): dedupe implicit CLI runtime aliases — https://github.com/openclaw/openclaw/pull/85982
- PR #88690 draft=False Emit sessions.changed for in-chat command metadata — https://github.com/openclaw/openclaw/pull/88690
- PR #82353 draft=False feat(auto-reply): expose safe requester identity metadata — https://github.com/openclaw/openclaw/pull/82353
- PR #88059 draft=False feat(browser): extend --labels overlay to full-page and element captures — https://github.com/openclaw/openclaw/pull/88059
- PR #59365 draft=False feat(doctor): detect volatile filesystem (tmpfs/ramfs/overlay) for state directory — https://github.com/openclaw/openclaw/pull/59365
- PR #88685 draft=False Render dashboard chat history incrementally — https://github.com/openclaw/openclaw/pull/88685
- PR #88023 draft=False feat(hooks): emit session:aborted + opt-in auto-continue hook — https://github.com/openclaw/openclaw/pull/88023
- PR #87907 draft=True fix(memory): validate memory index identity — https://github.com/openclaw/openclaw/pull/87907
- PR #84306 draft=False Fix chat.abort during attachment send preprocessing — https://github.com/openclaw/openclaw/pull/84306
- PR #67783 draft=False fix(feishu): target typing reaction on inbound — https://github.com/openclaw/openclaw/pull/67783
- PR #89148 draft=False fix(auto-reply): guard optional getFailedCounts on dispatcher variants — https://github.com/openclaw/openclaw/pull/89148

