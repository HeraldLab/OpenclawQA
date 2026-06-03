# Evidence Review Workflow

Every submitted report for **Baseline P0** or **Delta P0** needs a second-pass evidence review before we call it accepted.

The tester's GitHub issue is the canonical receipt, but the issue is not accepted until a reviewer has watched/analyzed the attached evidence and checked it against the assigned baseline/delta scenario.

Tool-assisted video review is allowed. **Tool-only acceptance is not.** A human reviewer owns the acceptance verdict for release-blocking scenarios.

## Policy

A report can be marked accepted only when:

1. The GitHub QA issue has the required environment fields.
2. All evidence links open for the QA team.
3. Any screen recording/video has been reviewed end-to-end, not skimmed.
4. The video shows the claimed P0 result without unacknowledged errors.
5. Any visible warnings/errors are either:
   - already listed as caveats in the report,
   - converted to a blocker/finding, or
   - confirmed unrelated/non-blocking with a note.
6. The evidence does not expose raw API keys, private SSH keys, `.env`, tokens, cookies, passwords, or private DMs.

## Reviewer steps

### 1. Intake the QA issue

Capture:

- issue URL and number
- tester
- release tag
- OS/device
- OpenClaw version/commit
- reported verdict
- evidence URLs
- video/screen recording URLs

If any required field is missing, comment with `NOT_ENOUGH_INFO` and request the exact missing field.

### 2. Open/download the video evidence

Preferred video evidence:

- Loom
- Tella
- OBS/QuickTime recording uploaded to Drive
- any equivalent recording link that the QA team can open

The reviewer should preserve:

- source URL
- local filename if downloaded
- duration
- checksum when local file is available
- whether audio is present

### 3. Watch/analyze the whole video

Use the strongest available path:

1. Native video model review, e.g. Gemini video analysis.
2. If native video review fails, extract frames/contact sheet plus transcript/audio and inspect those artifacts.
3. If no automated tool can access the video, a human reviewer must watch it and record timestamps manually.

The review must cover the full duration. Do not mark accepted from the first screenshot or a partial skim.

### 4. Timestamp visible events

Record timestamps for:

- install/upgrade proof
- OpenClaw version proof
- first normal response
- channel delivery proof
- plugin/tool visibility proof
- harmless failure proof
- release-specific scenario proof
- any visible error, warning, stack trace, failed command, red text, crash, timeout, or confusing output
- any possible secret exposure

### 5. Compare video to report

For each P0 row:

- `CONFIRMED` — video/evidence shows the claim.
- `MISSING` — claim is not visible in evidence.
- `CONTRADICTED` — evidence shows failure or a different result.
- `NOT_APPLICABLE` — row was not assigned/configured.

### 6. Produce review verdict

Allowed review verdicts:

- `EVIDENCE_CONFIRMED` — report claims match the full video/evidence; no unhandled errors.
- `EVIDENCE_CONFIRMED_WITH_CAVEAT` — claims pass but there are non-blocking warnings documented.
- `NEEDS_MORE_EVIDENCE` — missing timestamp, missing video segment, inaccessible link, or unclear result.
- `BLOCKED_BY_EVIDENCE_ERROR` — evidence shows setup/provider/permission/budget blocker.
- `FAIL_FILE_UPSTREAM` — reproducible product bug appears and should be deduped/filed upstream.
- `SECRET_EXPOSURE_REDACT` — evidence exposes secrets and must be replaced/redacted before acceptance.

### 7. Comment back on the QA issue

Use this format:

```md
## Evidence review
Verdict: <EVIDENCE_CONFIRMED | EVIDENCE_CONFIRMED_WITH_CAVEAT | NEEDS_MORE_EVIDENCE | BLOCKED_BY_EVIDENCE_ERROR | FAIL_FILE_UPSTREAM | SECRET_EXPOSURE_REDACT>

Reviewed evidence:
- Video: <url or filename>
- Duration reviewed: <full duration>
- Reviewer: <agent/person>

Checklist confirmation:
- Install/upgrade: <CONFIRMED/MISSING/CONTRADICTED/NA> — <timestamp>
- First response: <CONFIRMED/MISSING/CONTRADICTED/NA> — <timestamp>
- Channel delivery: <CONFIRMED/MISSING/CONTRADICTED/NA> — <timestamp>
- Plugins/tools: <CONFIRMED/MISSING/CONTRADICTED/NA> — <timestamp>
- Harmless failure: <CONFIRMED/MISSING/CONTRADICTED/NA> — <timestamp>
- Release-specific scenario: <CONFIRMED/MISSING/CONTRADICTED/NA> — <timestamp or NA>

Observed warnings/errors:
- <timestamp> — <warning/error or "None observed">

Secrets check:
- <PASS/FAIL> — <notes>

Next action:
- <accept / ask tester for missing clip / dedupe and file upstream / request redacted replacement>
```

## Acceptance rule

Do not mark the tester/report done until the QA issue contains an evidence review comment with `EVIDENCE_CONFIRMED` or `EVIDENCE_CONFIRMED_WITH_CAVEAT` for every assigned Baseline P0 and Delta P0 scenario.

If the tester only submitted screenshots, accept them only when they cover every required row and the scenario is non-sequential/static. If a row depends on a workflow sequence, ask for video or record an explicit waiver.
