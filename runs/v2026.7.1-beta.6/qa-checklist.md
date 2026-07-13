# QA Checklist — `v2026.7.1-beta.6`

## Dispatch gate

- [x] Exact-tag `#clawtributors` search completed: no dedicated beta.6 ping found as of `2026-07-13T19:53:11Z`.
- [x] Latest release-family `@Beta Pings` message captured: Vincent K, message `1700153`, `2026-07-11T11:08:55.303Z`.
- [x] Family-level asks converted into tester scenarios.
- [ ] Re-check `#clawtributors` immediately before each later beta packet dispatch for newer corrections or instructions.

## Universal baseline

- [ ] Install/upgrade and version proof.
- [ ] One normal response.
- [ ] One human-visible channel response where configured.
- [ ] Plugin/tool visibility.
- [ ] One harmless failure with clear recovery.
- [ ] Restart/config/session continuity.
- [ ] No secrets in evidence; visible outcome matches verdict.

## New-surface coverage

Each tester runs at least two available lanes and marks unavailable lanes `NOT_AVAILABLE`.

- [ ] Control UI layout/search/context/model-token/reasoning/preview/approval flow.
- [ ] Session title/group/unread/rename/fork/archive/delete flow.
- [ ] Crestodian conversational onboarding on a fresh/safe profile.
- [ ] `openclaw attach`, Claude Code, or Codex app-server continuity.
- [ ] Mobile/native offline cache, reconnect, switching, voice/TTS, or macOS chat.
- [ ] Messaging retry/restart with no duplicate, stale, leaked, or misrouted reply.

## Evidence

- [ ] Exact steps and commands.
- [ ] Expected versus actual behavior.
- [ ] Screenshots/recording.
- [ ] Redacted logs for failures.
- [ ] Usability/confusion notes.
- [ ] One GitHub issue per bug.
