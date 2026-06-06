# Tester Instructions — OpenClaw `v2026.6.5-beta.1`

Generated: `2026-06-06T04:00:11Z`
Run folder: https://github.com/HeraldLab/OpenclawQA/tree/main/runs/v2026.6.5-beta.1
Upstream release: https://github.com/openclaw/openclaw/releases/tag/v2026.6.5-beta.1
Report results: https://github.com/HeraldLab/OpenclawQA/issues/new/choose
Deadline: **6 hours after packet receipt**

## Target

Test OpenClaw beta release `v2026.6.5-beta.1`. This is a manual QA pass for release confidence, not a general support thread.

- Latest beta tag: `v2026.6.5-beta.1`

## Required setup evidence

Please include these in every report:

- OS/platform and version.
- Install/upgrade method and exact command used.
- OpenClaw version/tag observed after install.
- Provider/model route used if a model call is part of the test.
- Screen recording or screenshots.
- Logs for failures.

If a fact is unavailable, write `NOT_ENOUGH_INFO`.

## How your assigned card is generated

You should receive a short human QA card, not this whole operating model. The coordinator generates the card from:

1. **Universal baseline:** install/update, version proof, first response, one visible channel, plugin/tool sanity, safe failure, secrets check.
2. **Your real setup:** OS, channel, provider/model route, available plugin, restart path.
3. **Release risk:** one or two delta scenarios from the release notes, commits, PRs, and current upstream issues.

Default card shape is 6–8 checks:

1. Install/upgrade to `v2026.6.5-beta.1`.
2. Prove version/tag/commit.
3. Get one normal response.
4. Verify your assigned human-visible channel.
5. Check plugin/tool visibility or install/use one safe plugin.
6. Trigger one harmless failure and judge whether recovery is clear.
7. Run one Core P1 check: restart/persistence, provider route, or config/session continuity.
8. Run one release-specific delta check if assigned.

If you already proved a row in a previous issue, do not rerun it unless asked. Submit only the addendum.

## Baseline P0 smoke scenarios

1. **Install or upgrade** to `v2026.6.5-beta.1` from your normal path.
2. **Version proof:** show OpenClaw version/tag/commit after install.
3. **First response path:** start OpenClaw and get one normal response.
4. **Messaging delivery path:** if you have Discord/Telegram configured, verify a response reaches the human-visible channel.
5. **Plugin/tool visibility:** confirm configured tools/plugins are present and not silently omitted.
6. **Failure clarity:** intentionally trigger one harmless config/provider failure if safe, and verify the error is understandable.
7. **Secrets/false-success check:** confirm evidence has no secrets and success claims match visible results.

## Core P1 add-ons

Run assigned add-ons only:

- Restart/gateway persistence.
- Install and use one safe plugin.
- Provider/model route visibility.
- Config/session continuity after restart/update.
- Secondary messaging channel if configured.

## Release-delta add-ons

The coordinator may assign one release-specific scenario derived from changed code or current upstream issue signals. Treat it as manual human QA: record the real flow, expected vs actual, confusion/trust notes, and evidence.

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
