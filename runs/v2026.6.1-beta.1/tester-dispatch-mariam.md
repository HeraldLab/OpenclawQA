# Tester Dispatch Receipt — Mariam — OpenClaw `v2026.6.1-beta.1`

Status: **sent to correct Mariam thread, awaiting report**

## Approval

- Approved by: Henry / HiM
- Approval source: Discord thread `1510982876508979210`

## Freshness before send

- Checked at: `2026-06-01T18:09:06Z`
- Latest beta: `v2026.6.1-beta.1`
- Superseded: `false`
- Decision: `PASS_SEND_ALLOWED`

## Recipient

- Mariam: `<@1151723886971473971>` / `miriampeter_26511`
- Correct thread supplied by Henry: `1510234021052026880`

## Correction / deletion

Henry identified `1510234021052026880` as Mariam's actual thread and instructed Book to delete the wrong message and resend there.

Deleted wrong messages:

- Wrong parent `#openclaw` dispatch: channel `1506198862526939247`, message `1511069188960292895` — deleted `204`
- Wrong accidental thread clarification: channel/thread `1511069188960292895`, message `1511069820060307486` — deleted `204`

Readback after deletion showed the parent `#openclaw` feed no longer contained Book's wrong dispatch; accidental thread no longer contained Book's clarification.

## Correct resend

- Platform: Discord
- Thread ID: `1510234021052026880`
- Message ID: `1511072106908090378`
- Sent at: `2026-06-01T18:21:04.649000+00:00`
- Readback verified: `true`

The correct message includes:

- beta target and freshness
- checklist/run links
- no repo write access required
- report in this Discord thread
- Herald Labs/Book will validate, dedupe, and file confirmed upstream issues into `openclaw/openclaw` using the Herald Labs account
- optional public QA issue form
- do not file directly into `openclaw/openclaw` unless asked

## Next required action

Wait for Mariam to reply with report or blocker. If no response within the SLA window from the corrected resend, send one concise follow-up or escalate according to the HeraldLabs tester SLA.
