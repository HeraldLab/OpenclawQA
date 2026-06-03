# QA Checklist — OpenClaw `v2026.6.1-beta.3`

Updated: `2026-06-03T09:48:49Z`

## Gate status

- Target tag exists upstream: `v2026.6.1-beta.3`.
- Latest beta observed by freshness check: `v2026.6.1-beta.3`.
- Public tester dispatch: **pending Henry approval** in the release QA approval thread.
- GitHub issue filing: **disabled** unless Henry explicitly approves live filing.
- Dispatch route if approved: one packet per active tester's existing person-thread, not cohort-wide `#openclaw`.

## P0 manual smoke

1. **Install/upgrade path**
   - Upgrade from each tester's current path to `v2026.6.1-beta.3`.
   - Record exact command, package manager, OS/platform, Node/runtime version, and observed OpenClaw tag.
   - If the beta feed still resolves an older tag, report `BLOCKED — beta3 not available via update path` with screenshot.
2. **First response path**
   - Start OpenClaw and obtain one normal response from `openclaw tui` or the tester's configured primary interface.
   - Include screenshot or short log snippet showing the successful response.
3. **Messaging delivery path**
   - Verify Discord and/or Telegram delivery if configured.
   - Classify failures as receive-side, reply-side, credential/permission, webhook/routing, or unknown.
   - Redact tokens/API keys before sharing logs.
4. **Plugin/tool visibility**
   - Confirm expected configured tools/plugins are visible and not silently omitted.
   - Capture `openclaw status` or equivalent redacted output if plugin/tool inventory is wrong.
5. **Failure clarity**
   - Trigger one harmless provider/config failure only if safe.
   - Confirm the error is understandable and does not expose secrets.

## Targeted regression probes from current cohort state

- **Windows clean reinstall/config migration:** Gabriel is currently reinstalling after a broken Windows setup; beta3 should not regress `openclaw --version`, `openclaw doctor --fix`, `openclaw gateway status`, or `openclaw tui` recovery.
- **Delivery blocker:** Anny has a beta2 local TUI PASS but Discord/Telegram delivery blocked; beta3 validation should capture whether delivery still fails and where.
- **Stale-report discipline:** Samuel and Ayomide still need concrete PASS/BLOCKED/ETA evidence; beta3 dispatch should not blur current unresolved beta2 asks.

## Evidence quality bar

A triage-ready report includes target tag, OS/platform, install/upgrade command, observed version, expected behavior, actual behavior, screenshots/recording or redacted logs, and reproducibility notes.
