# Release Context — OpenClaw `v2026.10.10-beta.3`

Fetched at: `2026-10-21T07:01:19Z`

## Target

- Target tag: `v2026.10.10-beta.3`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.10-beta.3
- Target tag SHA: 15dffe5258a93c3d9c5dfd0a2b2de9989ebe7e14

## Freshness baselines

- Latest beta tag: `v2026.10.10-beta.3`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.10.5`
- Prior prerelease baseline: `v2026.10.10-beta.2`

## Release notes excerpt

## 2026.10.10-beta.3

### Highlights

- Windows reliability: restore fresh state initialization and Gateway startup, hide SQLite helper windows during app updates, and make forced Gateway reinstalls tolerate launcher timestamp settling. (#176194, #174969, #176174, #176945; related #176111, #174906, #176163, and #176872) Thanks @skyzhao1223, @RomneyDa, @easyteacher, @throwingbones, @tjarrau-dev, and @cnnceart.
- Upgrade recovery: converge app-owned plugins to the upgraded core version, restore affected agent stores including held system agents after schema-changing updates, and scope migration rollback backups to the versioned tables being changed. (#174257, #175007, #176783, #172671; related #174120 and #176669) Thanks @RomneyDa, @kazuyuki-eguchi, and @PennyVibe.

### Changes

### Fixes

- Agent state: concurrent initialization can no longer let two agents claim ownership of the same agent database. (#174251)
- Codex and native apps: previews no longer block replies after a context refresh, session replies resume after native child recovery, bound Codex history survives app-server restarts, and native app messages send again after reconnecting. (#177716, #177564, #172705, #171528) Thanks @jjjhenriksen and @RomneyDa.
- Background tasks: completions are no longer dropped when the config changes mid-turn. (#169529; related #169054) Thanks @wangmiao0668000666, @RomneyDa, and @Oldrich333.
- Discord: restore native slash commands in channels and threads. Thanks @montrellcruse and @RomneyDa.
- Agents: keep the prompt cache when a rate-limited run retries, and preserve steering messages that arrive without an explicit target. Thanks @montrellcruse, @RomneyDa, and @obviyus.
- Cron/CLI continuity: preserve CLI chat sessions across cron announce wakes instead of resetting their provider session. (#176218; related #176208) Thanks @eliavb43 and @RomneyDa.
- CLI tools: invalidate reused CLI sessions when the available tool catalog changes, restoring tools such as `exec` after Gateway restarts and preventing stale catalogs from reaching spawned agents. (#176577; related #175670) Thanks @RomneyDa, @jackylecalvez2, and @vincentkoc.
- GMI: omit unsupported `reasoning_effort` values on GPT-5.6 tool turns so the provider no longer rejects them with HTTP 400. (#176709) Thanks @RomneyDa.
- Windows updates: recognize Scheduled Task permission denials in every Windows display language, keep Windows plugin dependency links across Doctor phases, and clean up backup scratch directories without EPERM failures. (#178624, #178219, #169672, #176836; related #176743) Thanks @RomneyDa, @n572770, @xutongxue233, and @WG-Mojo.
- Update and Doctor: update finalization honors `TMPDIR` for disposable copies, Doctor suggests a retry instead of a restore after snapshot contention, and repeated Docker container restarts no longer take a full Doctor pre-repair capture each time. (#178009, #176779, #173711; related #176750 and #173564) Thanks @RomneyDa, @WG-Mojo, and @8bitsforge.
- Memory: cold Gateway starts no longer open every memory index (restoring 2026.10.4 startup memory), memory files keep indexing after plugin reloads, and plugin reloads no longer time out during slow dreaming cleanup. (#174718, #167756, #169945) Thanks @RomneyDa and @Stronggenetics.
- Nodes: synchronous node exec output is no longer repeated as a separate `Exec finished` wake after the waiting caller already received it. (#164511) Thanks @holgergruenhagen and @obviyus.
- macOS: long exec commands through the macOS app node no longer fail after 20 seconds. (#172117; related #139706) Thanks @holgergruenhagen, @RomneyDa, @ylcn91, and @Colton-Harris.
- Control UI: offer desktop setup instead of Retry when Host Desktop is off, model pickers refresh when the catalog changes mid-read, and locale refresh works again after adding a source-only locale. (#177888, #174812, #172689; related #174368) Thanks @etzelm, @RomneyDa, and @hannesrudolph.

### Complete contribution record

This audited record covers the complete v2026.10.10-beta.2..bd1a53a3a5f59a8319112250b48d338d74dbaceb history: 53 in-range PRs + 0 retained seed-only PRs = 53 unique PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

#### Pull requests

- **PR #176194** Related #176111. Thanks @skyzhao1223 and @RomneyDa and @easyteacher.
- **PR #174969** Related #174906. Thanks @RomneyDa and @throwingbones.
- **PR #174257** Related #174120. Thanks @RomneyDa and @kazuyuki-eguchi.
- **PR #176174** Related #176163. Thanks @RomneyDa and @tjarrau-dev.
- **PR #175007** Thanks @RomneyDa.
- **PR #176783** Related #176669. Thanks @RomneyDa and @PennyVibe.
- **PR #176945** Related #176872. Thanks @RomneyDa and @cnnceart.
- **PR #176218** Related #176208. Thanks @eliavb43 and @RomneyDa.
- **PR #176577** Related #175670. Thanks @RomneyDa and @jackylecalvez2.
- **PR #176709** Thanks @RomneyDa.
- **PR #172671** Thanks @RomneyDa.
- **PR #177355** Thanks @RomneyDa.
- **PR #177159** Thanks @vincentkoc and @RomneyDa.
- **PR #177586** Thanks @RomneyDa.
- **PR #175872** Thanks @RomneyDa.
- **PR #177648** Thanks @RomneyDa.
- **PR #177725** Thanks @RomneyDa.
- **PR #177752** Thanks @RomneyDa.
- **PR #177813** Thanks @RomneyDa.
- **PR #177851** Thanks @RomneyDa.
- **PR #172117** Related #139706. Thanks @holgergruenhagen and @RomneyDa and @ylcn91 and @Colton-Harris.
- **PR #177564** Thanks @jjjhenriksen and @RomneyDa.
- **PR #177913** Thanks @RomneyDa.
- **PR #169945** Thanks @Stronggenetics and @RomneyDa.
- **PR #169529** Related #169054. Thanks @wangmiao0668000666 and @RomneyDa and @Oldrich333.
- **PR #173711** Related #173564. Thanks @RomneyDa and @8bitsforge.
- **PR #172661** Thanks @RomneyDa.
- **PR #170297** Related #170291. Thanks @RomneyDa.
- **PR #172689** Thanks @RomneyDa.
- **PR #172745** Thanks @RomneyDa.
- **PR #172668** Thanks @RomneyDa.
- **PR #172705** Thanks @RomneyDa.
- **PR #173615** Thanks @RomneyDa.
- **PR #173656** Thanks @RomneyDa.
- **PR #173465** Thanks @RomneyDa.
- **PR #173781** Thanks @RomneyDa.
- **PR #173813** Thanks @RomneyDa.
- **PR #174718** Thanks @RomneyDa.
- **PR #167756** Thanks @RomneyDa.
- **PR #174812** Thanks @RomneyDa.
- **PR #177716** Thanks @jjjhenriksen and @RomneyDa.
- **PR #177888** Related #174368. Thanks @etzelm and @RomneyDa and @hannesrudolph.
- **PR #171528** Thanks @jjjhenriksen and @RomneyDa.
- **PR #178009** Thanks @RomneyDa.
- **PR #176836** Related #176743. Thanks @xutongxue233 and @RomneyDa and @WG-Mojo.
- **PR #176779** Related #176750. Thanks @RomneyDa and @WG-Mojo.
- **PR #169672** Thanks @n572770 and @RomneyDa.
- **PR #178219** Thanks @RomneyDa.
- **PR #178624** Thanks @RomneyDa.
- **PR #174251**
- **PR #178231** Thanks @RomneyDa.
- **PR #164511** Thanks @holgergruenhagen and @obviyus.
- **PR #178862** Thanks @RomneyDa.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.10.10-beta.3
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.10.10-beta.3.tgz
- integrity: `sha512-OGKys4zxLjYeZny0aHZK3k1VBoZC/5MyqT+lCk6Pzw52QxkqtAyKtyu/cu4GfcelbRZHOCo3yJZvaYE7Ua9ISA==`
- release SHA: `15dffe5258a93c3d9c5dfd0a2b2de9989ebe7e14`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.10.10-beta.3/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/39555832807
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/39529505653
- full release validation: https://github.com/openclaw/openclaw/actions/runs/39528806396
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/39557095517
- plugin ClawHub publish: no normal OIDC candidates
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/39553212507/attempts/1
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- No recent open issue signals returned.

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #179108 draft=False chore: refresh dependencies with a seven-day cutoff — https://github.com/openclaw/openclaw/pull/179108
- PR #179133 draft=False refactor(ui): use Solid primitives for component state and rendering — https://github.com/openclaw/openclaw/pull/179133
- PR #179115 draft=False refactor(ui): adopt Solid lifetimes and actions in chat panels — https://github.com/openclaw/openclaw/pull/179115
- PR #168211 draft=False fix: show recovery guidance for interrupted conversation startup — https://github.com/openclaw/openclaw/pull/168211
- PR #179184 draft=False fix: honor startup refusals in provider review proof — https://github.com/openclaw/openclaw/pull/179184
- PR #179117 draft=False improve(ui): speed up theme contrast checks — https://github.com/openclaw/openclaw/pull/179117
- PR #179162 draft=False perf(sessions): avoid duplicate actor command graph copies — https://github.com/openclaw/openclaw/pull/179162
- PR #179091 draft=False perf(sessions): keep cold checkout polls responsive — https://github.com/openclaw/openclaw/pull/179091
- PR #169163 draft=False fix(media): files above 50 MB are not staged when mediaMaxMb is raised — https://github.com/openclaw/openclaw/pull/169163
- PR #178917 draft=False fix(workspace): exclude generated build caches without losing tracked inputs — https://github.com/openclaw/openclaw/pull/178917
- PR #179118 draft=False refactor(ui): use native Solid boundaries for shell and catalog reads — https://github.com/openclaw/openclaw/pull/179118
- PR #179167 draft=False perf(github): show cached hover previews without forced refresh — https://github.com/openclaw/openclaw/pull/179167
- PR #179022 draft=False fix(memory-core): refuse to rewrite DREAMS.md containing invalid UTF-8 — https://github.com/openclaw/openclaw/pull/179022
- PR #179131 draft=True perf: reduce PostgreSQL restart chat-admission delay — https://github.com/openclaw/openclaw/pull/179131
- PR #179048 draft=False refactor: localize private login, evidence, and transport phases — https://github.com/openclaw/openclaw/pull/179048
- PR #175589 draft=False fix(telegram): sends into another DM topic land in a separate session when the account has an explicit binding — https://github.com/openclaw/openclaw/pull/175589
- PR #179087 draft=False refactor(ui): adopt Solid page loading and settled lifetimes — https://github.com/openclaw/openclaw/pull/179087
- PR #179142 draft=False perf(agents): reuse wire JSON for provider prompt fingerprints — https://github.com/openclaw/openclaw/pull/179142
- PR #168913 draft=False fix(plugins): clear warnings after removing unreadable load paths — https://github.com/openclaw/openclaw/pull/168913
- PR #179160 draft=True perf(agents): stop re-parsing streamed tool-call arguments on every delta — https://github.com/openclaw/openclaw/pull/179160
- PR #117352 draft=False fix(agents): propagate client tool cancellation — https://github.com/openclaw/openclaw/pull/117352
- PR #179163 draft=False refactor(ui): replace shell loaders with Solid lazy boundaries — https://github.com/openclaw/openclaw/pull/179163
- PR #179150 draft=False fix(gateway): workspace icon returns 403 for sessions an operator can see — https://github.com/openclaw/openclaw/pull/179150
- PR #179168 draft=False test(ui): share the media transcript Gateway fixture — https://github.com/openclaw/openclaw/pull/179168
- PR #179148 draft=False fix(ios): recover partial Watch runtime deletion during screenshots — https://github.com/openclaw/openclaw/pull/179148
- PR #179157 draft=False perf(ui): reduce dashboard and chat reload RPC fan-out — https://github.com/openclaw/openclaw/pull/179157
- PR #175291 draft=False feat: open new agent chats instantly and simplify agent selection — https://github.com/openclaw/openclaw/pull/175291
- PR #179137 draft=True improve: reduce PostgreSQL store startup waits — https://github.com/openclaw/openclaw/pull/179137
- PR #179121 draft=False fix(ci): surface daily repo E2E failures separately — https://github.com/openclaw/openclaw/pull/179121
- PR #179141 draft=False perf(ui): share transcript structure across streamed replies — https://github.com/openclaw/openclaw/pull/179141
