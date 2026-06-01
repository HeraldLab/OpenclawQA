# OpenClaw Release QA Operating Model

Public coordination lives in this GitHub repo. Entity/Mission Control remains internal.

Core workflow:

```text
qualifying alpha/beta tag or prerelease
  → mandatory freshness gate
  → release-context packet
  → agent-generated release checklist
  → coverage/adversarial/clarity review
  → human sign-off
  → pre-send freshness recheck
  → tester instructions
  → screen-recorded manual QA
  → report/log bundle collection
  → validation + aggressive dedupe
  → GitHub issue filing
  → blocker escalation
  → optional PR handoff
  → run closeout
```

## Rules

- Tag-driven, not commit-driven.
- Issue-first, not PR-first.
- Evidence-first.
- Alpha/beta only unless explicitly forced.
- One public owner agent per run/thread.
- One issue per confirmed bug.
- Use `NOT_ENOUGH_INFO` when facts are absent.
- PR recency is a risk signal, not proof a change shipped in a tag.
- Do not expose private Entity URLs publicly.
