# Release Context — OpenClaw `v2026.10.5-beta.4`

Fetched at: `2026-10-15T06:30:22Z`

## Target

- Target tag: `v2026.10.5-beta.4`
- Target exists upstream: **yes**
- Target release URL: https://github.com/openclaw/openclaw/releases/tag/v2026.10.5-beta.4
- Target tag SHA: 6b4b2a945d5ff157920efa663d1c6192a9a1e717

## Freshness baselines

- Latest beta tag: `v2026.10.5-beta.4`
- Latest alpha tag: `v2026.6.21-alpha.1`
- Stable baseline: `v2026.10.3`
- Prior prerelease baseline: `v2026.10.5-beta.3`

## Release notes excerpt

## 2026.10.5-beta.4

### Highlights

- **Updates finish more reliably:** macOS updates no longer time out on aliased temporary directories, systemd user installs reclaim abandoned runtimes, pacman and FreeBSD package installs are left to their package manager, snapshot failures are identified before activation with accurate recovery advice, and the success summary no longer repeats settled plugin upgrades as pending. (#169860, #171488, #169055, #171457, #170351, #170413) Thanks @RomneyDa, @DonnieFi, and @Pegorim.
- **ChatGPT models work on the default Codex runtime:** ChatGPT-listed models no longer fail before sending any request. (#168033) Thanks @obviyus.
- **Headless browser sign-ins stay usable:** headless pages keep accepting clicks and key presses while a site waits for a passkey. (#170857) Thanks @trukhinyuri.

### Changes

- **Context limits:** status shows corrected context limits after model discovery, Copilot honors reported context capacity when native limits are missing, and llama.cpp keeps live router model limits and tools on refresh. (#165991, #156636, #168309) Thanks @snotty, @saju01, and @RomneyDa.

### Fixes

- **Gateway access:** local access keeps working when the tailnet denies Tailscale Serve, and lifecycle publications survive after the emitting producer drains. (#171509, #170231) Thanks @RomneyDa.
- **macOS repair and recovery:** update recovery finishes repairing the bundled Gateway, the app keeps a compatible newer Gateway during recovery instead of downgrading it, LaunchAgent repair accepts verified bootstrap recovery, and Doctor allows offline state repair for app-owned Gateways. (#171508, #170766, #170740, #170768) Thanks @RomneyDa.
- **Update resilience:** updates keep moving when optional cron inspection or snapshot cleanup fails. (#170754) Thanks @RomneyDa.
- **Security:** Tlon never treats group DM authors as the owner. (#165801) Thanks @eleqtrizit.
- **Turns and replies:** Claude CLI sessions remember announced sub-agent results on the next turn, agent plugin reloads no longer wait on their own turn, interrupted turns are preserved when new messages arrive, ACP follow-up replies no longer disappear after the previous turn is stopped, context-engine advancement survives steering, visible sub-agent spawns try the primary model first, and launched agent turns no longer fail with writer claim errors. (#164175, #171257, #170647, #170883, #168394, #169984, #170077) Thanks @robertoronderosjr, @RomneyDa, @etzelm, and @jacobtomlinson.
- **Gateway lifecycle:** the Gateway stays responsive during reply-tagged streams and long quoted tool XML no longer triggers per-token Markdown parsing, blocked context-engine turns stop repeating in the Gateway log on every run, the Control UI no longer reconnects on delayed heartbeats, state reads stay closed until restart after a failed state cleanup, the Gateway recovers state ownership after sleep and clock changes, stalled transcript workers no longer block shutdown, database admission no longer blocks worker startup, shutdown joins lifecycle publication, forced descendant cleanup releases worker capacity, enabled standalone plugin files start with the Gateway, Gateway restart works from verified external macOS terminals, and Android/Termux gateways no longer fail with "shared-state database generation changed". (#166782, #171573, #167595, #171253, #171709, #170790, #170493, #170348, #170555, #168746, #171330, #170354, #167719) Thanks @aniruddhaadak80, @holgergruenhagen, @obviyus, @RomneyDa, @yxshee, @grabowskidaniel359-design, @jjjhenriksen, @AnvinaLI, @sgh6688, @waynegault, @Oldrich333, @residentb2b, @boeingchoco, and @jalehman.
- **Workers:** worker heap limits are enforced under process-wide Node flags. (#166581) Thanks @valkyriweb, @xydigitLybnnnn, @goslingmanagment, and @waynegault.
- **Channels and tools:** MCP OAuth login completes with portless loopback registrations, and each Feishu monitor start gets its own binding adapter registration. (#170876, #169226) Thanks @9fw2pq8sgb-art, @ruel225, @obviyus, and @junniar.
- **Update and Doctor:** update repair no longer fails after Doctor completes on busy macOS hosts, slow update admission no longer holds the database writer and disrupts Gateway work, update repair prepares its config before inference, metadata inventory survives progress-output backpressure, Docker upgrades stop retry loops on older Linux hosts, Doctor explains plugin migration backup coverage, and Doctor no longer logs spurious WAL maintenance warnings while repairing shared state. (#170779, #171493, #170276, #168493, #162305, #169295, #170783) Thanks @vincentkoc, @yxshee, @Ludwigtheo0815, @RomneyDa, and @DonnieFi.
- **Plugin publishing:** plugin npm publication no longer fails when artifact pagination repeats an entry. (#171044) Thanks @RomneyDa.

### Complete contribution record

This audited record covers the complete v2026.10.5-beta.3..9e0a1c922e978fbcfb14c29d112573f6a99468d7 history: 61 in-range PRs + 0 retained seed-only PRs = 61 unique PRs. The generation manifest also supplies direct commits as editorial input; the grouped notes above prioritize user impact.

#### Pull requests

- **PR #166581** Related #157575, #157630. Thanks @valkyriweb and @xydigitLybnnnn and @goslingmanagment and @waynegault.
- **PR #171504** Thanks @RomneyDa.
- **PR #169295** Thanks @RomneyDa.
- **PR #169055** Related #157338. Thanks @Pegorim.
- **PR #168309**
- **PR #165991** Thanks @snotty and @saju01.
- **PR #156636** Thanks @saju01 and @snotty.
- **PR #168816**
- **PR #168033** Thanks @obviyus.
- **PR #168394** Related #168014. Thanks @robertoronderosjr.
- **PR #168746** Related #160643. Thanks @aniruddhaadak80.
- **PR #168926**
- **PR #169860**
- **PR #169984**
- **PR #170276**
- **PR #170348**
- **PR #170354** Thanks @RomneyDa.
- **PR #170555**
- **PR #169226** Related #169190. Thanks @ruel225 and @obviyus and @junniar.
- **PR #168493** Thanks @vincentkoc.
- **PR #170647**
- **PR #170883**
- **PR #170876** Related #170848. Thanks @9fw2pq8sgb-art.
- **PR #171044** Thanks @RomneyDa.
- **PR #165801** Thanks @eleqtrizit.
- **PR #167719** Related #167623. Thanks @yxshee and @grabowskidaniel359-design.
- **PR #162305** Related #161746. Thanks @yxshee and @Ludwigtheo0815.
- **PR #171330** Thanks @holgergruenhagen and @obviyus.
- **PR #170351** Thanks @DonnieFi and @RomneyDa.
- **PR #170857** Thanks @trukhinyuri.
- **PR #170077**
- **PR #170783**
- **PR #171457** Related #171408. Thanks @RomneyDa and @DonnieFi.
- **PR #171488** Related #171410. Thanks @RomneyDa and @DonnieFi.
- **PR #170413** Related #170334. Thanks @RomneyDa and @DonnieFi.
- **PR #171493** Related #169260. Thanks @RomneyDa and @DonnieFi.
- **PR #170790** Related #169829, #170525, #170597. Thanks @jjjhenriksen and @AnvinaLI and @sgh6688 and @waynegault.
- **PR #170493** Related #169777. Thanks @Oldrich333.
- **PR #167051**
- **PR #170231**
- **PR #168569** Related #168014. Thanks @robertoronderosjr.
- **PR #170768** Thanks @RomneyDa.
- **PR #170754** Thanks @RomneyDa.
- **PR #171509** Thanks @RomneyDa.
- **PR #170740** Thanks @RomneyDa.
- **PR #170766** Thanks @RomneyDa.
- **PR #171747** Thanks @RomneyDa.
- **PR #164236** Related #163961. Thanks @JakeMalis.
- **PR #171952** Thanks @RomneyDa.
- **PR #171709** Related #162085. Thanks @RomneyDa and @residentb2b.
- **PR #172321** Thanks @RomneyDa.
- **PR #171543** Thanks @RomneyDa.
- **PR #170779**
- **PR #170804**
- **PR #171508** Thanks @RomneyDa.
- **PR #171257** Related #170881. Thanks @jacobtomlinson.
- **PR #164175** Related #171195. Thanks @etzelm.
- **PR #171253**
- **PR #166782** Related #166781. Thanks @boeingchoco.
- **PR #167595** Thanks @jalehman.
- **PR #171573** Related #171363. Thanks @boeingchoco.

### Release verification

- npm package: https://www.npmjs.com/package/openclaw/v/2026.10.5-beta.4
- registry tarball: https://registry.npmjs.org/openclaw/-/openclaw-2026.10.5-beta.4.tgz
- integrity: `sha512-7p8Hc1xnJFOAk6gSlMvWW7S4ywYlliY9oTVWMfHeBxJ7GcTRnZuqszoFYXEVGhCf7F0Sp5fN0AXBK49R9BwW6w==`
- release SHA: `6b4b2a945d5ff157920efa663d1c6192a9a1e717`
- full release CI report: https://github.com/openclaw/releases/blob/main/evidence/2026.10.5-beta.4/release-evidence.md
- release publish: https://github.com/openclaw/openclaw/actions/runs/38688765823
- npm preflight: https://github.com/openclaw/openclaw/actions/runs/38675599773
- full release validation: https://github.com/openclaw/openclaw/actions/runs/38675026301
- plugin npm publish: https://github.com/openclaw/openclaw/actions/runs/38689391881
- plugin ClawHub publish: no normal OIDC candidates
- plugin ClawHub bootstrap: not needed
- OpenClaw npm publish: https://github.com/openclaw/openclaw/actions/runs/38685225005/attempts/1
- npm Telegram beta E2E: not supplied

## Recent issue risk signals

- #70266 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:other] [Feature]: Use assistant avatar in macOS Talk Mode overlay — https://github.com/openclaw/openclaw/issues/70266
- #53345 [enhancement, P3, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Feature]: Add Korean (ko) language support to Control UI and AI agent — https://github.com/openclaw/openclaw/issues/53345
- #137299 [P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-product-decision, impact:security, issue-rating: 🦞 diamond lobster, clawsweeper:bulk-filed] [Feature]: exec children carry no calling-agent identity, so a scoped wrapper must encode the agent in its own path — https://github.com/openclaw/openclaw/issues/137299
- #108599 [clawsweeper:needs-product-decision, clawsweeper:needs-live-repro, issue-rating: 🐚 platinum hermit] sessions_send announce delivery causes 2-3x turn amplification on claude-cli agents (session-limit exhaustion observed) — https://github.com/openclaw/openclaw/issues/108599
- #111143 [P3, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, clawsweeper:needs-product-decision, issue-rating: 🌊 off-meta tidepool, impact:ux-friction] [Feature]: Allow pinning plugin tabs in the Control UI sidebar — https://github.com/openclaw/openclaw/issues/111143
- #159276 [clawsweeper:needs-product-decision, clawsweeper:source-repro, issue-rating: 🦞 diamond lobster] Native Ollama: plugin runtime.llm.complete() does not serialize reasoning: off as think: false — https://github.com/openclaw/openclaw/issues/159276
- #170367 [enhancement, P2, clawsweeper:no-new-fix-pr, clawsweeper:needs-maintainer-review, impact:auth-provider, issue-rating: 🦪 silver shellfish] [Feature]: OAuth usage-limit errors (ChatGPT/Codex 5h & weekly) should trigger auth profile rotation to the next configured OAuth account — https://github.com/openclaw/openclaw/issues/170367

## Recent PR risk signals

PRs are risk signals, not proof of shipped code in this tag.

- PR #172771 draft=False fix(whatsapp): queued messages show an error reaction after successful handling — https://github.com/openclaw/openclaw/pull/172771
- PR #172841 draft=False test(plugins): remove low-value tests (batch d089) — https://github.com/openclaw/openclaw/pull/172841
- PR #172847 draft=False perf(gateway): remove redundant work from repeated RPC reads — https://github.com/openclaw/openclaw/pull/172847
- PR #172814 draft=False fix(agents): preserve whitespace in node-host exec workdir paths — https://github.com/openclaw/openclaw/pull/172814
- PR #172569 draft=True feat(macos): launch the compiled OpenClaw runtime — https://github.com/openclaw/openclaw/pull/172569
- PR #172810 draft=False fix: queued follow-up answers appear twice in WebChat — https://github.com/openclaw/openclaw/pull/172810
- PR #172848 draft=True perf(agents): bound requester lookup and transcript replay work — https://github.com/openclaw/openclaw/pull/172848
- PR #171846 draft=False refactor(ui): remove Lit dependency from subscriptions — https://github.com/openclaw/openclaw/pull/171846
- PR #87434 draft=True [codex] Expire Telegram message-cache plugin state — https://github.com/openclaw/openclaw/pull/87434
- PR #172833 draft=False fix(ci): continue stale PR scans at the label limit — https://github.com/openclaw/openclaw/pull/172833
- PR #172044 draft=False fix(ui): lint Solid TypeScript helpers — https://github.com/openclaw/openclaw/pull/172044
- PR #86793 draft=False fix(gateway): lighten session event row snapshots — https://github.com/openclaw/openclaw/pull/86793
- PR #172845 draft=False fix(ci): verify stale checkpoints in their actual cache backend — https://github.com/openclaw/openclaw/pull/172845
- PR #171664 draft=False refactor(ui): separate presentation contract from Lit adapters — https://github.com/openclaw/openclaw/pull/171664
- PR #172846 draft=False fix(crabbox): wait for availability when Crabbox cannot attest capture — https://github.com/openclaw/openclaw/pull/172846
- PR #172363 draft=False refactor(ui): render plugin routes directly with Solid — https://github.com/openclaw/openclaw/pull/172363
- PR #171549 draft=False fix(database): account, approval, and usage writes hold the SQLite writer during host admission — https://github.com/openclaw/openclaw/pull/171549
- PR #172844 draft=True feat: compress oversized videos without blocking chat — https://github.com/openclaw/openclaw/pull/172844
- PR #157806 draft=False fix(sessions): preserve requester identity at execution admission — https://github.com/openclaw/openclaw/pull/157806
- PR #172840 draft=False fix(subagents): keep completions from same-key children of different agents — https://github.com/openclaw/openclaw/pull/172840
- PR #172843 draft=False fix: remove redundant chat delivery and restart subtext — https://github.com/openclaw/openclaw/pull/172843
- PR #165481 draft=False fix(gateway): report stt-tts readiness and transports in talk.catalog — https://github.com/openclaw/openclaw/pull/165481
- PR #155634 draft=False feat(provider): add Databricks Unity Gateway — https://github.com/openclaw/openclaw/pull/155634
- PR #172834 draft=False fix(ci): retire unused internal channel and helper exports — https://github.com/openclaw/openclaw/pull/172834
- PR #172802 draft=False feat: shrink standalone sidecars and bundle SQLite — https://github.com/openclaw/openclaw/pull/172802
- PR #172695 draft=False test(ui): cover reasoning handoff disclosures — https://github.com/openclaw/openclaw/pull/172695
- PR #172653 draft=False fix(ai): detach OpenAI stream partial snapshots from live output — https://github.com/openclaw/openclaw/pull/172653
- PR #172283 draft=False fix(buzz): preserve literal credential-file paths — https://github.com/openclaw/openclaw/pull/172283
- PR #172676 draft=False improve: avoid repeated SQLite admission after handle closure — https://github.com/openclaw/openclaw/pull/172676
- PR #154607 draft=False improve(browser): default managed Chromium to efficient headless launches — https://github.com/openclaw/openclaw/pull/154607
