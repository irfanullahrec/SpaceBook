# SpaceBook progress log

## 2026-10-19 — Phase 0 (local part): security incident + deploy recovery
Done:
- Committed the outstanding work on branch `wip/2026-10-19`: 5 modified files, 137 `covers/Books/*/kptb_*.webp` covers (6.9 MB) and the audit/roadmap docs. Tag `checkpoint/p0-start`.
- Branch `phase/p0-security`: `tools/build_upload_zip.py` no longer writes `api/config.php` into the package. It asserts that no secret file is inside, and it takes an optional output path.
- `api/config.sample.php`: the real cPanel account names are replaced with placeholders.
- `.github/workflows/deploy.yml`: connects to `s26.hosterpk.com` (the name on the FTPS certificate, same IP 64.31.31.90) with `security: strict`. The live check now fails separately for "index.html not served", "upload zip reachable" and "database unreachable".
- `docs/PHASE0_SERVER_STEPS.md`: the exact steps the owner does on the server.

Files: tools/build_upload_zip.py, api/config.sample.php, .github/workflows/deploy.yml, docs/PHASE0_SERVER_STEPS.md, docs/PROGRESS_LOG.md

Verified by:
- `python tools/build_upload_zip.py <scratch>/test_upload.zip` → 747 files, 124 MB. The only config entry is `api/config.sample.php`. The test zip was deleted afterwards.
- `openssl s_client -starttls ftp -connect wantuch.pk:21` → certificate CN=s26.hosterpk.com, verify code 0. `s26.hosterpk.com` and `wantuch.pk` both resolve to 64.31.31.90.
- GitHub API, last 6 runs: all failed at "Check the live site". "Upload to wantuch.pk" succeeded each time, in 3 s, or 3 min 16 s on the full re-upload.
- Live probes now: `/spacebook/` 200 (directory listing), `/spacebook/index.html` 404, `/spacebook/api/health.php` 404, `/spacebook/spacebook_upload.zip` **200 (still exposed)**.
- `deploy.yml` parses as YAML.

Root cause of DEP-01: the FTP account `spacebook@wantuch.pk` uploads into a folder that is not `public_html/spacebook`. A workflow change cannot fix this; the owner fixes it in cPanel (server steps, step 5).

Not verified:
- Strict-TLS FTP upload from CI. Nothing has been pushed yet, because a push to `main` deploys.
- Any server step: SEC-01 is still open.

Risks / owner decisions needed:
- Server steps 1–6 in docs/PHASE0_SERVER_STEPS.md.
- Repository visibility. The repo is public and now also holds the audit docs, which describe the leak. Do not push them while the zip is still online.
- The live server runs PHP 7.4.33 (earlier health output), not PHP 8 as the start prompt says. api/ must stay 7.4-compatible until the host is upgraded.

Next: Phase 1 (baseline runner, repair validate.js/smoke.js, tracer, CI test gate).

## 2026-10-19 — Phase 1 (in progress): safety net
Done:
- Branch `phase/p1-safety-net` (tag `checkpoint/p1-start`).
- `tools/validate.js`: no longer crashes (every check runs inside `safe()`); sandbox defines `window`; 35 stale pre-rebuild checks replaced by Contract C checks over all 92 `CLSn_BOOKS` files plus a unit-count lock `tests/contract/cls_books.json` (`--update-books` to accept a rebuild).
- `tools/smoke.js`: now loads all 248 index.html scripts in order (`tools/lib/app_sandbox.js`); 41 stale tests replaced by one test that opens 88 rebuilt books through the real reader and renders every tab of the first and last unit, plus 10 Class 12 books.
- `package.json` (dev-only, Playwright 1.63.0) and `tests/baseline/{lib,run}.js` (browser baseline runner).

Verified by:
- `node tools/validate.js` → 946 passed, 0 failed (two runs; was 10 failures then a crash). Changing a locked count makes it fail.
- `node tools/smoke.js` → 251 passed, 0 failed, ~21 s (two runs; was 32 failures). A wrong expected count makes it fail.

Not verified:
- The Playwright baseline runner has NOT completed a run. Two trial runs crashed the page ("Target crashed") while free RAM was 0.5–1.2 GB of 7.9 GB; the app needs ~0.7 GB per page. An earlier probe with `explore.js` did load the app in Chrome with 0 console errors.
- No tracer, no CI test job, no CONTRIBUTING.md rewrite yet.
- Baseline stability (≥ 99.5 % hash match over two runs) not measured.

Known tests dropped (reasons in commit messages): old Drawing 2/3, Maths 1/2/3 tab tests and legacy counts for rebuilt books.

Risks / owner decisions: baseline needs ~1.5 GB free RAM; close other programs or run it on a bigger machine.
Next: re-run the baseline with free RAM, then tracer, CI gate, CONTRIBUTING.md.

## 2026-10-19 — Phase 1 (continued): tracer, CI gate, CONTRIBUTING
Done:
- `tools/trace_globals.js` + `tools/lib/app_sandbox.js` trace mode: opens every class x subject, selects first/middle/last chapter, renders every tab, and records the data globals read. Output `tests/trace/<class>/<subject>.json`, `tests/trace/index.json` (globalsToSubjects), `tests/trace/never_read.json`.
- `.github/workflows/deploy.yml`: new `test` job (validate + smoke on Node 22); `deploy` now `needs: test` and is skipped on pull requests, which also run `test`.
- `CONTRIBUTING.md` rewritten to the real structure (five contracts, generators, regression rule, secrets, deploy).

Verified by:
- `node tools/trace_globals.js` → 147 subjects traced, 0 step errors, 56 s, 147 trace files. (The brief said 115 subjects; the registry has 147.) Class 2 Maths reads `CLS2_BOOKS`, not `MATH_2_DATA`.
- `deploy.yml` parses as YAML; jobs `test`, `deploy`; `deploy.needs == test`.

Not verified:
- The `test` job has not run on GitHub (nothing pushed); Linux case-sensitivity of file names is therefore untested there.
- Functions called are not traced (cannot be wrapped from outside). `never_read.json` (69 globals) is a hint only: reads during script load are not captured, and e.g. Class 11 source globals feed `CLASS11_BOOKS` at load.
- Browser baseline (screenshots, DOM hashes, 99.5 % stability) still pending: needs ~1.5 GB free RAM. The baseline subset is NOT in CI yet, because it has never completed a run.
- Phase 1 exit gate is not met (baseline missing).

Next: run the baseline when memory allows; push Phase 0 and Phase 1 branches only after the owner confirms the server steps.

## 2026-10-19 — Phase 1 (continued): HTML snapshot baseline
Done:
- `tools/snapshot_html.js`: renders every class x subject x chapter x tab in the app sandbox and stores tab labels + HTML hash; `--compare` lists differences. Baseline stored in `tests/baseline/html-2026-10-19/` (147 subjects, 1.2 MB).

Verified by:
- Two full runs → 147 subjects, 1,831 chapters, 9,715 tab renders each; `--compare` → 0 differences (100.00 % identical). The first comparison showed 18 differences, all from random `sbq<n>_xxxx` ids generated by `js/sb_mcq.js`; these are normalised before hashing.
- Browser baseline retried: Chrome page crashed again with 0.6 GB free RAM (single subject, `--subset`), so Playwright baseline is still unverified.

Defect found (not fixed; shared file `js/app.js`, needs owner OK): Class 9 Physics, chapter index 2: numericals 4, 6, 7, 9, 11, 13 have an object in `question`, so `js/app.js:22177` throws `.slice is not a function` and the "Concepts & Examples" render for that chapter fails. Probably a `{en, ur, ps}` object; fix by picking the string before `.slice`.

Not verified: layout, fonts, screenshots, console errors, timings (browser-only). The snapshot is not yet a CI gate (Windows-vs-Linux output identity untested).
Phase 1 exit gate: validate 0 failures ✔, smoke 0 failures ✔, trace for all subjects ✔ (147), CI blocks deploy ✔ (unrun on GitHub), baseline stored — HTML snapshot ✔, browser baseline ✘.

## 2026-10-19 — Class 9 Physics numericals fix + Phase 2 design
Done:
- Fixed `js/app.js` (renderer around line 22150): numericals whose `question`/`solution` are `{text, urdu, pashto}` objects made the Class 9 Physics chapter-3 "Concepts & Examples" tab throw (blank tab). `numText()` now takes `.text`.
- `docs/PHASE2_SYNC_DESIGN.md`: confirmed defects (SYNC-01/02/03, SEC-02, SEC-05, S-01 suspected) with code locations, event model, v2 API, tables, client outbox, merge rules, migration/rollout, tests, work breakdown, owner decisions. Design only; no code written for Phase 2.

Verified by:
- `tools/snapshot_html.js` vs the stored baseline: 9,715 tab renders, 1 difference (cls9-phy ch2 concepts, the fixed tab), step errors 1 → 0. Probe: no `[object Object]`, title and solution text present.
- `node tools/validate.js` → 946 passed, 0 failed; `node tools/smoke.js` → 0 failed.
- Delete-not-retried (SYNC-02c) confirmed in `sb_study_plan.js:591` (single fire-and-forget `api('delete')`).

Not verified: the fix in a real browser (Chrome could not run, low RAM). Coin cap numbers and trace `total <= 60` in the design are proposals; the largest shipped figure's step count has not been measured. S-01 (session lifetime) needs a check on the live host. Reward activity keys come from the SVG at runtime (`keyOf` in `sb_trace.js`), so a build-time activity catalog is not possible yet — the design uses patterns + caps instead.

Next: owner review of the design (section 10 decisions); server steps in `docs/PHASE0_SERVER_STEPS.md` still pending.

## 2026-10-19 — Phase 2, steps 1-2: migrations + auth hardening (branch `phase/p2-server`, tag `checkpoint/p2-start`)
Design approved by the owner with the proposed caps (600 coins/day, 300 new activities/day, trace total <= 60). Reset channel still open.

Done:
- Migrations: `api/migrations/001_baseline.sql` (the old schema.sql, idempotent), `002_security_sync_v2.sql` (+ `.down.sql`): `devices`, `rate_limits`, `audit_log`, `sync_events`, `activity_catalog`. `api/lib/migrate.php`, CLI `php api/migrate.php status|up|down|prune`. `db()` no longer runs DDL from a marker file in `api/`: it applies pending migrations once under `GET_LOCK`. Tests point `SB_CONFIG` at another config.
- Auth hardening (`api/auth.php`, `api/lib/security.php`): per-address failure ceiling (20/15 min) besides the per-number lock; Retry-After on 429; dummy bcrypt verify for unknown numbers (equal timing/identical message); 10 registrations/hour/address; opportunistic prune of `login_attempts` (+ `migrate.php prune`); audit log; device tokens (random 32 bytes, SHA-256 stored) issued on request (`want_device`), revoked by logout with the bearer token; same-site check (Sec-Fetch-Site / Origin) on all cookie POST endpoints. Public `api/health.php` now returns only `{"ok":true,"db":true}`; details need `?token=` (`health_token` in config). `api/session.php`: private session folder + `gc_maxlifetime` = 30 days (S-01 fix, effect on the live host unconfirmed).
- `tools/php74_lint.js`, `tests/php/run.php`, CI job `php-test` (PHP 7.4 + MySQL 5.7 service), CONTRIBUTING.

Verified by:
- `php tests/php/run.php` → 63 passed, 0 failed (three runs). Covers: 0→2→1→2 migration cycle; legacy populated DB migrates with no lost rows/coins; down never drops student data; rate limiter; token hashing/revoke/blocked user; same-site matrix; health public/token; 5-failure lock + Retry-After; 20-failure address ceiling; 11th registration 429; foreign Origin 403 on login/progress/test_prep/study_plans; same-origin v1 flows unchanged; logout revokes device.
- Mutation: raising the address ceiling to 200 and disabling the progress check made 3 tests fail; restored.
- `node tools/php74_lint.js` → 12 files, 0 problems; it flags match/str_contains/union types in a test file.

Deviations from the design (decided while building):
- CSRF: Origin/Sec-Fetch-Site check now instead of a token, because the existing JS sends no token and must keep working; the token arrives with the v2 client. Bearer-token requests will skip the check.
- Migrations: the design said "CLI/CI only", but deploys are FTP-only (CI cannot reach the host's localhost MySQL), so pending migrations are applied by the first request under a lock; the CLI exists for local use and the owner.
- IP failure ceiling is 20 (not 5) because a school shares one address.

Not verified:
- PHP 7.4 itself: local PHP is 8.2.12; 7.4 is covered only by the syntax lint until the `php-test` job runs on GitHub.
- Behaviour on the live host (LiteSpeed): `Authorization` header pass-through (`.htaccess` rule added), private session folder, `Retry-After`.
- Running the suite against MySQL 5.7 (local is MariaDB 10.4).
- Registration still reveals "number already exists" (enumeration is only rate limited; closing it needs a verified channel, see reset-channel decision).
- Nothing pushed. **Pushing to main deploys, and the first live request then runs migration 002 on the live database (additive).** Take a mysqldump first.

Next: step 3 (`api/v2/sync.php` POST, progress events + coin rules) after the owner confirms the server steps.

## 2026-10-19 — Phase 2, step 3: api/v2/sync.php + reward rules (branch phase/p2-server)
Done:
- `api/lib/rewards.php`: the coin rules and abuse limits in one place, used by v1 `progress.php` (refactored, same responses) and by v2. Limits per user and 24 h: 600 coins, 300 new activities; 200 steps per activity. Progress is recorded past the coin limit; past the activity limit nothing is created.
- `api/v2/sync.php` (POST): batch <= 500 events and <= 1 MB; bearer device token or same-site cookie session; 60 batches/min/user; event ledger `sync_events` makes each eventId apply at most once; rejected events (bad_key, bad_total, bad_step, bad_event_id, bad_payload, bad_schema, too_large, unsupported_type, not_completed, activity_limit) leave no trace; response has accepted, rejected, cursor, coins. Types now: step, again. GET (pull) and plan/test-prep events are the next step.
- `tests/php/run.php` now 100 checks.

Verified by:
- `php tests/php/run.php` -> 100 passed, 0 failed (two runs). Includes: replay of the same event; same step under a new id pays nothing; 8 coins for a 3-step activity; again pays 2 only on a later day; every invalid-event reason; 501 events and >1 MB -> 413; 1,000 events in two batches all accepted, coins capped at 600 with progress still recorded, budget returns after 24 h; 301st new activity -> activity_limit; two devices in opposite order give identical coins (8) and steps; revoked token 401; cookie session needs same-site; 61st batch -> 429 + Retry-After; v1 sync capped at 600 and v1 total clamped to 200.
- Mutations caught: coin limit raised (5 failures), event ledger disabled (replayed repeat counted twice).
- `node tools/php74_lint.js` -> 14 files, 0 problems.

Deviations from the approved design:
- Per-activity step cap is 200, not 60: the largest shipped figure has 126 countable items (measured), so 60 would reject real figures. The daily budgets are the abuse limit.
- Real activity keys look like `cls2|math|u0|trace|<hash>|0`, not `trace|...` as the design assumed.
- Finishing an activity counts as that day practice: an immediate repeat pays 0 (same as v1).

Not verified: PHP 7.4 and MySQL 5.7 (CI job not yet run); no client uses v2 yet; behaviour on the live host. Another session changed `index.html` and added `js/cls1_eng_activities.js` in this working tree; they are not part of these commits.

Next: step 4 (GET since cursor, plan and test-prep events, merge rules) — still waiting for the owner to confirm the server steps before any push.

## 2026-10-19 — Phase 2, step 4: pull, plans, test prep (branch phase/p2-server)
Done:
- Migration `003_sync_state.sql` (+ down): `sync_changes`, `user_sync_state`, `tp_answers`, `tp_days`, `tp_runs`, `study_plans.rev`.
- `api/v2/sync.php` GET `?since=` (absolute state of changed objects, paged by 2,000 changes) and new events `plan.save`, `plan.delete`, `tp.answer`, `tp.session`, `tp.run`, `tp.run.clear`; libs `changes.php`, `plans.php`, `testprep.php`, `pull.php`.
- v1 `study_plans.php`, `test_prep.php` and the rewards library write the change log; v1 test-prep saves also merge into the v2 tables (more attempts wins); first v2 contact imports the old `test_prep_records` blob once.
- Design section 11 documents what differs from the approved design (answers are additive; change log as cursor).

Verified by:
- `php tests/php/run.php` -> 152 passed, 0 failed (two runs, ~40 s). New checks: pull empty/full/incremental/paged (1,100 answers over 3 pages, all delivered), absolute and repeatable; plan fast-forward, concurrent edit (later arrival wins fields, done = max, removed task stays removed), tombstones (delete, late offline edit, delete-before-create), 50-plan limit, 512 KB limit, bad ids; v1 plan save/delete visible to v2 and the reverse; two devices answering one MCQ add up; out-of-order answers keep the newest last_correct; time caps; daily numbers per track with derived `all`; session stored once; unfinished-run ordering around a clear; old record import once, old client cannot lower totals and an unchanged resend adds no change rows; cookie pull; wrong bearer 401.
- Mutations caught: plan merge off, tombstone check off (after strengthening the test), answers overwrite instead of add, last_correct ignoring time, paging off.
- `node tools/php74_lint.js` -> 18 files, 0 problems.

Not verified: PHP 7.4 / MySQL 5.7 (only PHP 8.2 + MariaDB 10.4 here; CI job php-test not yet run); the ALTER TABLE in migration 003 on the live database (no IF NOT EXISTS on MySQL 5.7, so it must run exactly once: take a mysqldump first); performance of pulls for a user with all 6,000 MCQs answered; no client uses any of this yet. The working tree also holds another session's Class 1 changes (index.html, js/english_1_book.js, js/cls1_*.js, figs1.py); they are not in my commits.

Next: steps 5-7 are client work (js/core/store.js + sync.js outbox, convert sb_rewards/sb_study_plan/test_prep, guest-merge prompt, profile/export/delete, password change). Server steps in docs/PHASE0_SERVER_STEPS.md still pending; nothing pushed.

## 2026-10-19 — Phase 2, step 5: client sync core (branch phase/p2-server)
Owner instruction: no more questions about pushing or the server steps; the owner pushes after all phases.

Done:
- `js/core/store.js`: IndexedDB key-value store (outbox, meta, state) with localStorage and memory fallbacks.
- `js/core/sync.js` (`window.SBSync`): `emit()` writes to the outbox first; `flush()` sends oldest-first in batches of 200 with exponential back-off + jitter, Retry-After, 401 -> auth-lost (events and sign-in kept, never demoted to guest), 413/422 -> batch halved to isolate a poison event; `pull()` follows the cursor and merges into a stored snapshot (applyPull is pure and repeatable); guest events wait for `adoptGuest()`; single-flight; survives reload.
- Feature flag: automatic triggers run only when localStorage `sb_sync_v2` = `on` (or `window.SB_FLAGS.syncV2`), so the live page behaves as before until step 6 converts the modules.
- `js/auth.js`: login/register ask for a device token and hand it to SBSync; logout sends the bearer token (server revokes the device) and forgets it locally; waiting events stay.
- `index.html`: loads js/core/store.js and sync.js before auth.js (only that hunk committed; the file also holds another session's uncommitted Class 1 script tags).
- `tools/validate.js` checks js/core syntax and the load order; CI: `test` job runs the client unit tests, `php-test` job runs the end-to-end test.

Verified by:
- `node tests/sync/unit.js` -> 39 passed, 0 failed (three runs). 5 mutations caught (network error drops events, 401 signs out, guest events sent without consent, retry not re-armed after an event during back-off, events removed without a server answer); the feature flag has its own test.
- `node tests/sync/e2e.js` (real client + real PHP + MySQL scratch DB) -> 17 passed, 0 failed: delivery and snapshot; a lost answer is resent with the same ids and applied once (also for a repeat, which sets cannot protect); offline + reload + online; two devices editing one plan converge; delete propagates; guest events offered then adopted; revoked token -> auth-lost, event kept, resumes with a new token; bad event rejected without blocking the good one. Mutation (server ledger off) is caught.
- `node tools/validate.js` -> 961 passed, 0 failed; `node tools/smoke.js` -> 0 failed (255 scripts load); PHP suite 152 passed.
- HTML snapshot vs baseline: 9,715 tab renders, 20 differences, all in cls1-eng, where the other session has uncommitted edits (js/english_1_book.js, js/cls1_*.js); nothing else changed.

Not verified: any of this in a real browser (Chrome cannot run here: RAM); IndexedDB behaviour beyond fake-indexeddb; PHP 7.4/MySQL 5.7; the CI jobs on GitHub. Nobody calls `SBSync.emit` yet.

Next: step 6: convert `sb_rewards.js`, `sb_study_plan.js`, `test_prep.js` to emit events and read the pulled snapshot (one commit each, snapshot + smoke after each), then step 7 (guest-merge prompt, profile/export/delete, password change) and step 8 (backups).

## 2026-10-19 — Phase 2, step 6a: sb_rewards.js on the sync core (SYNC-01)
Done:
- `js/sb_rewards.js`: the coin rules are now pure functions (`applyStep`, `applyAgain`) used by the guest path and by a new v2 path. With the flag on (`sb_sync_v2`), a signed-in student's numbers = the last pulled snapshot + the events the server has not confirmed yet, replayed with the same rules (`derive()`); `step()`/`again()` write the event to the outbox first, so a failed request neither loses the step nor demotes the student to guest (the old `user = null` path is not used in v2). Progress made as a guest becomes events at sign-in and the local guest copy is removed. Flag off: the old code path, unchanged.
- `js/core/sync.js`: `pendingEvents()` and `isEnabled()`. `index.html`: core scripts now load before `sb_rewards.js`. `tools/lib/app_sandbox.js`: the document stub has a working event bus.

Verified by:
- `node tests/sync/rewards.js` (real sb_rewards.js + core in the app sandbox, real PHP + MySQL scratch DB): 15 passed, 0 failed, twice. Offline steps earn immediately (8 coins shown) and stay signed in; they sit in the outbox, none in guest storage; back online the server agrees and a second fresh page sees the same coins/steps; a failed request keeps the student signed in with back-off recorded; guest steps join the account (7 coins, 2 steps seen from a fresh page); repeat refused when never finished, 0 coins the same day; with the flag off rewards still call progress.php and never v2. Mutation (no replay of pending events) is caught.
- Full battery after the change: validate 971/0, smoke 0 failed, sync unit 39/0, e2e 17/0, PHP 152/0; HTML snapshot: only the 20 known cls1-eng differences (the other session's uncommitted Class 1 work).

Not verified: in a real browser; a reload with a cookie-less session (the page still decides who is signed in from `auth.php?action=me`, i.e. the session cookie; a valid device token alone does not show the student as signed in); the coin total shown between a successful flush and the following pull is the pre-flush value (it self-corrects after the pull); the guest-to-account prompt (step 7) — today guest progress joins the account silently, as it did before.

Next: 6b `sb_study_plan.js` (plan.save/delete with baseRev, snapshot-based list), 6c `test_prep.js` (tp.* events, snapshot-based stats).

## 2026-10-19 — Phase 2, step 6b: study planner on the sync core (SYNC-02)
Done:
- Migration 004 (`study_plans.last_device`) + `sb_plan_save(..., $deviceId)`: a save from the device that wrote the plan last is a fast-forward whatever its baseRev (so un-ticking a task sticks), a stale save from another device is merged (done = max, incoming fields win). v1 saves clear `last_device`.
- `js/sb_study_plan.js`: with the flag on, `persist()` writes `plan.save {plan, baseRev}` and deleting writes `plan.delete` to the outbox first (`removePlan()`); a pull is folded into the local list by `mergeSnapshot()` without overwriting an edit that is waiting to be sent and without bringing back a plan whose deletion is waiting; plans made before the first sync are sent at sign-in; nothing is queued while signed out. Flag off: unchanged v1 code. Exports `persist`, `removePlan`, `add` for tests.
- `tests/sync/harness.js` shared scaffolding; `tests/sync/planner.js`.

Verified by:
- `node tests/php/run.php` -> 155 passed, 0 failed (new: same device with a stale baseRev is a fast-forward and un-ticking sticks; another device with a stale baseRev is merged; migration cycle 0->4->0->4). Mutation (rule removed) caught by 2 tests.
- `node tests/sync/planner.js` (real module + real API) -> 13 passed, 0 failed, twice: offline plan + tick queued then delivered and seen by a second device; un-tick before sync wins everywhere; two devices editing offline converge (B's name, A's ticked work kept); offline delete does not resurrect on a pull and reaches the other device; signed-out plans stay local and join the account at sign-in; reload with waiting events delivers them; flag off uses api/study_plans.php only. Mutation (pending-delete guard removed) caught.
- Battery: validate 971/0, smoke 0 failed, sync unit 39/0, e2e 17/0, rewards 15/0, PHP 155/0; HTML snapshot: only the 20 known cls1-eng differences.

Not verified: in a real browser; reminders (they read local plans and are unchanged); two tabs of one browser editing at once (they share one outbox and one device id, so the server treats them as one device: a stale save from the second tab fast-forwards instead of merging); the "ask before adding this device's plans to the account" prompt (step 7).

Next: 6c `test_prep.js` (tp.answer/session/run events, snapshot-based statistics).
