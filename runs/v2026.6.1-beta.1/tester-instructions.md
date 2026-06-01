# Tester Instructions — OpenClaw `v2026.6.1-beta.1`

Generated: `2026-06-01T16:29:58Z`  
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.1-beta.1  
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.1-beta.1  
Report results: https://github.com/HeraldLab/OpenclawQA/issues/new/choose  
Deadline: **48 hours after dispatch**


## Access and Reporting Route

You do **not** need write access to the `HeraldLab/OpenclawQA` repo to participate.

Preferred reporting path:

1. Reply in the Discord thread/channel where you were tagged with your checklist statuses and evidence links.
2. Book/Herald Labs will collect the report, validate it, dedupe it against existing OpenClaw issues, and file any confirmed upstream issue into `openclaw/openclaw` using the Herald Labs account.

Optional path if you have a GitHub account:

- You may also file a tester report in the public QA repo: https://github.com/HeraldLab/OpenclawQA/issues/new/choose
- Repo access beyond normal public GitHub access is not required.

Do **not** file directly into `openclaw/openclaw` unless asked. We want one deduped upstream issue per validated bug, not duplicate tester reports.

## Target

Test OpenClaw beta release `v2026.6.1-beta.1`. This is a manual QA pass for release confidence, not a general support thread.

- Latest beta tag: `v2026.6.1-beta.1`

## Required setup evidence

Please include these in every report:

- OS/platform and version.
- Install/upgrade method and exact command used.
- OpenClaw version/tag observed after install.
- Provider/model route used if a model call is part of the test.
- Screen recording or screenshots.
- Logs for failures.

If a fact is unavailable, write `NOT_ENOUGH_INFO`.

## P0 smoke scenarios

1. **Install or upgrade** to `v2026.6.1-beta.1` from your normal path.
2. **First response path:** start OpenClaw and get one normal response.
3. **Messaging delivery path:** if you have Discord/Telegram configured, verify a response reaches the human-visible channel.
4. **Plugin/tool visibility:** confirm configured tools/plugins are present and not silently omitted.
5. **Failure clarity:** intentionally trigger one harmless config/provider failure if safe, and verify the error is understandable.

## Report format

Use GitHub Issues in this repo:

- Use **Install smoke result** for install-only passes/failures.
- Use **Tester report** for general scenario reports.
- Use **Beta blocker** only for issues that block release validation.

One issue per bug. Do not combine unrelated failures.

## Evidence quality bar

A report is triage-ready when it has target tag, OS/platform, install method, exact steps, expected behavior, actual behavior, logs or screenshots/recording, and whether it reproduces again.

## Privacy

Do not upload secrets, API keys, private customer data, or unsanitized environment dumps. If raw evidence contains private data, summarize publicly and say the raw artifact is private.
