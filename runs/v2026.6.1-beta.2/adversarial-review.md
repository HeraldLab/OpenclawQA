# Adversarial Review — OpenClaw `v2026.6.1-beta.2`

Reviewed: `2026-06-01T22:00:16Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.1-beta.2  
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.1-beta.2

## Dispatch posture

**Recommendation:** hold for Henry approval before public tester dispatch.

The run artifact is ready enough for review, but not automatically safe to blast to testers because:

- No public dispatch approval is recorded in this run.
- Tester reports collected for this tag: **0**.
- Live upstream issue filing is disabled unless explicitly run with `--live`.
- Current onboarding state still has one active setup blocker (`annywrld`) and three testers still collecting final install-smoke evidence.

## Freshness / target checks

- Target tag exists upstream: **yes** — `v2026.6.1-beta.2`.
- Latest beta tag: `v2026.6.1-beta.2`.
- Stable baseline: `v2026.5.28`.
- Prior prerelease baseline: `v2026.6.1-beta.1`.
- Recent upstream signals include active P1/P2 issue/PR churn around message delivery, auth/provider config, Windows security/SecretRef behavior, and agent tool/plugin visibility.

## Risk focus for testers

Ask testers to avoid generic “it installed” replies. The useful evidence is concentrated around:

1. **Install/upgrade path** — exact command, OS/version, and observed OpenClaw tag/version.
2. **First response path** — at least one normal model response after startup.
3. **Visible delivery path** — Discord/Telegram delivery if configured; screenshot/message receipt if possible.
4. **Plugin/tool visibility** — configured tools/plugins present and not silently omitted.
5. **Failure clarity** — one harmless provider/config failure if safe, with readable error text and redacted logs.

## Dispatch caveats

- Testers do **not** need write access to the upstream `openclaw/openclaw` repo.
- Preferred reporting path remains the HeraldLab QA issue form or the existing tester thread; Herald Labs should validate/dedupe before filing upstream.
- Do not ask testers to paste secrets, API keys, private customer data, or unsanitized env dumps.
- For `annywrld`, do not convert the current model-auth blocker into release QA until API key/model config is resolved.

## Review gate

Before public dispatch, Henry should approve one of:

- `APPROVE DISPATCH v2026.6.1-beta.2`
- `CHANGE: <specific packet edits>`
- `BLOCK: <reason>`

If approved, rerun freshness immediately before dispatch, then send one Ada-owned public release packet and record the Discord message/thread IDs.
