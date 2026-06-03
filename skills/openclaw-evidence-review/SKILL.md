---
name: openclaw-evidence-review
description: Use when reviewing OpenClaw tester evidence after a QA issue/report is submitted; validates full video recordings, timestamps checklist proof, detects errors, and decides whether a report can be accepted.
version: 1.0.0
author: Herald Labs / OpenClaw QA
license: MIT
metadata:
  hermes:
    tags: [openclaw, qa, evidence, video-review, tester, github-issues]
    related_skills: [openclaw-p0-release-qa]
---

# OpenClaw Evidence Review

## Overview

This skill is for the reviewer agent, not the tester. It runs after a tester submits a QA issue/report and evidence links.

The reviewer must inspect the submitted evidence, including full screen recordings, and decide whether the report is actually proven. A report is not accepted just because the tester says `PASS`.

## When to Use

Use this when:
- A tester files a QA issue in `HeraldLab/OpenclawQA`.
- A tester posts a PDF/report with video, screenshot, or Drive/Loom/Tella evidence.
- You need to confirm whether beta/alpha P0 testing is complete.
- You need to decide whether a warning is non-blocking, missing evidence, or an upstream bug.

Do not use this to:
- Skim the first screenshot and call it done.
- Ignore video warnings/errors because the written report says pass.
- Publish secrets from the evidence.
- File upstream bugs before dedupe.

## Required Inputs

Capture:

- QA issue/report URL
- tester name/handle
- release tag
- reported verdict
- evidence URLs
- video/screen recording URLs
- expected P0 checklist for that packet
- any release-specific assigned scenario

## Review Workflow

Follow `docs/evidence-review-workflow.md` as the canonical workflow.

### 1. Verify the issue/report fields

Required:
- OpenClaw version/tag
- commit/hash if available
- OS/device
- install/update method
- provider/model route
- assigned channel(s)
- P0 checklist status
- evidence links
- secrets check

If fields are missing, classify `NEEDS_MORE_EVIDENCE` and ask for the exact missing items.

### 2. Open every evidence link

For each link:
- confirm it opens for the QA team
- record whether it is screenshot, video, logs, issue, or folder
- note inaccessible/private links

Inaccessible evidence cannot prove a pass.

### 3. Watch/analyze the full video

Use the strongest available path:

1. Native video model review, e.g. Gemini video analysis, with a prompt that asks for timestamped P0 proof and visible errors.
2. If model review fails, extract frames/contact sheets and transcript/audio, then inspect those artifacts.
3. If automation cannot access the video, require a human reviewer to watch it and record timestamps.

The full duration must be covered. Do not call a video reviewed if only the first section was inspected.

### 4. Timestamp proof and errors

Record timestamps for:
- install/upgrade proof
- version proof
- first normal response
- channel delivery proof
- plugin/tool visibility proof
- harmless failure proof
- release-specific scenario proof
- warnings/errors/red text/stack traces/timeouts/crashes
- possible secret exposure

### 5. Compare evidence to the checklist

For each P0 row, classify:

- `CONFIRMED`
- `MISSING`
- `CONTRADICTED`
- `NOT_APPLICABLE`

### 6. Decide verdict

Allowed evidence-review verdicts:

- `EVIDENCE_CONFIRMED`
- `EVIDENCE_CONFIRMED_WITH_CAVEAT`
- `NEEDS_MORE_EVIDENCE`
- `BLOCKED_BY_EVIDENCE_ERROR`
- `FAIL_FILE_UPSTREAM`
- `SECRET_EXPOSURE_REDACT`

Acceptance rule: a tester/report is not done until the QA issue contains `EVIDENCE_CONFIRMED` or `EVIDENCE_CONFIRMED_WITH_CAVEAT` from this review workflow.

## Video Review Prompt

Use this prompt with Gemini or another native video model:

```text
You are reviewing an OpenClaw P0 release QA screen recording. Watch/analyze the whole video from start to finish.

Release tag: <tag>
Tester: <tester>
Reported verdict: <verdict>
Expected checklist:
1. install/upgrade to assigned tag
2. OpenClaw version/commit proof
3. one normal OpenClaw response
4. configured visible channel delivery
5. plugin/tool visibility sanity check
6. one harmless failure with understandable error
7. release-specific scenario if assigned

Return JSON with:
- duration_reviewed
- whether the whole video was analyzed
- checklist: each row as CONFIRMED/MISSING/CONTRADICTED/NOT_APPLICABLE with timestamp and evidence note
- visible_errors: timestamped warnings/errors/red text/tracebacks/timeouts/crashes/misleading output
- possible_secret_exposure: timestamped evidence or PASS
- mismatch_with_written_report
- recommended_verdict from: EVIDENCE_CONFIRMED, EVIDENCE_CONFIRMED_WITH_CAVEAT, NEEDS_MORE_EVIDENCE, BLOCKED_BY_EVIDENCE_ERROR, FAIL_FILE_UPSTREAM, SECRET_EXPOSURE_REDACT
- concise reviewer comment suitable for GitHub

Do not assume success. If a checklist row is not visible, mark MISSING. If an error appears but the report claims pass, call it out.
```

## GitHub Evidence Review Comment

```md
## Evidence review
Verdict: <verdict>

Reviewed evidence:
- Video: <url or filename>
- Duration reviewed: <full duration>
- Reviewer: <agent/person>

Checklist confirmation:
- Install/upgrade: <status> — <timestamp/evidence>
- Version proof: <status> — <timestamp/evidence>
- First response: <status> — <timestamp/evidence>
- Channel delivery: <status> — <timestamp/evidence>
- Plugins/tools: <status> — <timestamp/evidence>
- Harmless failure: <status> — <timestamp/evidence>
- Release-specific scenario: <status> — <timestamp/evidence or NA>

Observed warnings/errors:
- <timestamp> — <warning/error or None observed>

Secrets check:
- <PASS/FAIL> — <notes>

Next action:
- <accept / request missing evidence / dedupe and file upstream / request redacted replacement>
```

## Common Pitfalls

1. **Trusting a PASS PDF without watching the video.** The video is where hidden errors show up.
2. **Partial video review.** A two-minute screen recording means two minutes reviewed.
3. **Missing silent failures.** Watch for error banners, red text, tracebacks, timeouts, and commands returning non-zero.
4. **Ignoring contradictions.** If written report says Discord passed but video shows no delivery, classify `CONTRADICTED`.
5. **Leaking evidence.** If a video reveals a secret, stop and request a redacted replacement.

## Verification Checklist

- [ ] Every evidence link opened or was marked inaccessible
- [ ] Full video duration reviewed
- [ ] P0 rows classified with timestamps
- [ ] Visible warnings/errors recorded
- [ ] Secrets check completed
- [ ] Evidence-review verdict posted/comment-ready
- [ ] Tracker updated only after confirmed evidence
