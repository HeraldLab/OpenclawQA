# Action Gate Policy

Any Discord/public coordination for a release QA run must have one owner agent.

Dedupe key shape:

```text
openclaw-release-qa:<tag>:<phase>:<audience>
```

Examples:

```text
openclaw-release-qa:v2026.6.1-beta.1:tester-instructions:discord-thread
openclaw-release-qa:v2026.6.1-beta.1:check-in:tester-miriam
openclaw-release-qa:v2026.6.1-beta.1:closeout:discord-thread
```

Non-owner public sends should be blocked or silent-dropped by runtime Action Gate.
