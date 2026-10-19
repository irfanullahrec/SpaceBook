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

## 2026-10-19 — Phase 2, step 6c: Tests Preps on the sync core (SYNC-03)
Done:
- `js/test_prep.js`: with the flag on and a signed-in student, every answer (`tp.answer`), finished session (`tp.session`), change of the unfinished test (`tp.run`, kept to one waiting copy by `emitLatest`) and its clearing (`tp.run.clear`) is written to the outbox first. The statistics the page reads are rebuilt from the last pulled snapshot plus unconfirmed events (`derive()`), so two devices answering the same MCQ both count. Records made as a guest, or by the old version on this device, are sent once at sign-in as `tp.import` (+ their sessions); the guest copy is removed so it joins one account only (SYNC-03a). The v1 whole-record push/pull is not used in v2. Flag off: unchanged.
- Server: `tp.import` event (more attempts wins per MCQ, larger numbers per day).
- `js/core/sync.js`: `emitLatest()` (serialised); a 401 only counts as "auth lost" when the credentials are still the ones the request was sent with (a stale 401 while the device token was arriving used to latch auth-lost and block all syncing: found by the integration test).
- `tests/sync/testprep.js`.

Verified by:
- `node tests/sync/testprep.js` (real module, real 6,120-MCQ bank, real API) -> 15 passed, 0 failed, run after the final code: offline practice (3 answers + session + run changes queued, numbers visible at once, student stays signed in); delivered, nothing waits; a second device sees attempts, session and daily numbers; the other device's answer to the same MCQ adds (1 -> 2); guest practice kept locally, then joins the account at sign-in with the guest copy removed and not given to another student on the same browser; pre-update local record imported (5 attempts, old session, day); the unfinished test follows the student to another device and disappears when finished; 5 answers leave 5 answer events and a single run event; flag off: no outbox, no v2 requests. Mutation (answers not emitted) caught.
- `node tests/sync/unit.js` -> 42 passed (new: emitLatest keeps one copy under concurrent calls; stale 401 ignored and retried; mutation caught).
- Whole battery on the final code: validate 971/0, smoke 0 failed, unit 42/0, e2e 17/0, rewards 15/0, planner 13/0, testprep 15/0, PHP 155/0, php74_lint 0 problems; HTML snapshot: only the 20 known cls1-eng differences.

Not verified: in a real browser (Chrome cannot run here); IndexedDB itself (tests use fake-indexeddb or the localStorage fallback); statistics screens beyond what the stored record shows; the Tests Preps "My Stats" counters on the home page (separate, local, unchanged); PHP 7.4/MySQL 5.7; the CI jobs on GitHub.

Phase 2 status: server steps 1-4 and client steps 5-6 are done behind the `sb_sync_v2` flag (default off). Remaining: step 7 (guest-merge prompt before adding guest data to an account, profile edit/export/delete, change password) and step 8 (backups + restore drill, v1 deprecation) — these need owner decisions on the reset channel and backup destination.

## 2026-10-19 — Phase 2, steps 7-8: account management, consent before moving guest data, backups
Done (all behind the same flag where it touches sync; the account actions are always available):
- Server (`api/auth.php`, `api/lib/account.php`, migration 005): `update_profile`, `change_password` (current password required; every other device is signed out, the requesting device stays; throttled), `export` (all data of the student as a JSON download; no password hash, no tokens), `delete_account` (password required; soft delete, devices revoked, login answers like a wrong password; `php api/migrate.php purge` removes accounts deleted more than 30 days ago from every table, including those without a foreign key).
- Client: `js/auth.js` "My account" screen (details, change password, download my data, delete my account) reachable from the user menu; logout and delete forget the device token and keep waiting events.
- `js/core/consent.js`: the student is asked once before progress, study plans or practice saved on this device while signed out are added to the account (shared lab computers); "No" keeps the data on the device and is remembered for 7 days; one question however many modules ask. Wired into `sb_rewards.js`, `sb_study_plan.js`, `test_prep.js` (their own earlier record needs no question). These modules' sign-in sync is now single-flight (the page announces a sign-in more than once).
- Step 8: `tools/backup/dump.php` (pure PHP, consistent snapshot, gzip, rotation, refuses `public_html`) and `restore.php` (refuses a non-empty target without `--force`, reports a cut-off file); `docs/BACKUP_RESTORE.md` (cron line, off-site options, restore drill, real recovery).
- Bugs found and fixed by the new tests: incremental pulls always carried `run: null` and wiped the unfinished test from the client snapshot (now only sent when it changed); `getopt` ignored `--keep 2` written with a space (backup rotation kept 1).

Verified by (final code, one run each):
- `php tests/php/run.php` 196/0 (new: profile/password/export/delete/purge incl. other accounts untouched; backup drill: dump of the test database restored into a fresh one, 17 tables with equal row counts and CHECKSUM TABLE, quotes/newlines/semicolons/emoji/Urdu byte for byte, refusal without --force, truncated dump reported, public_html refused, rotation).
- `node tests/sync/account.js` 17/0 in jsdom against the real API (menu -> My account -> each form; avatar initial updates; wrong/correct current password; export has no hash; logout keeps events and the server revokes the device; delete message, sign-out and no further login). Mutation (profile save not updating the user) caught by 3 checks.
- sync unit 51/0 (consent module), e2e 17/0, rewards 16/0 (asked once; Cancel keeps the guest copy and does not ask again), planner 15/0 (Cancel keeps the plan local), testprep 17/0 (Cancel leaves the guest record; the student's own record needs no question), validate 973/0, smoke 0 failed, php74_lint 0 problems; HTML snapshot: only the 20 known cls1-eng differences. Mutations caught: delete without password, purge missing a table, other devices not signed out on password change, the run:null pull bug.
- New dev dependency: `jsdom` 30.1.1 (exact, dev only, not deployed).

Not verified: any of the UI in a real browser (jsdom is not a browser: no layout, no real styling of the new "My account" screen, no real `confirm()` dialog); the backup tools on the cPanel host (PHP version, cron path, permissions, gzip availability: run the drill in docs/BACKUP_RESTORE.md once); MySQL 5.7 and PHP 7.4 (CI job php-test not yet run); the consent question uses a plain `confirm()`.

Owner decisions still open (none blocks the code): password-reset channel (WhatsApp OTP provider or admin-assisted) — no reset exists yet; where off-site copies of the backups go; the final wording/design of the consent dialog.

Phase 2 summary: migrations 001-005, auth hardening, device tokens, v2 sync (push + pull), plans/test-prep/rewards on the outbox, account management, consent, backups. Everything client-side is OFF by default (`localStorage sb_sync_v2` = `on` or `window.SB_FLAGS.syncV2`); v1 endpoints are unchanged except for the shared reward limits and change logging. Turning the flag on for everyone is the owner's release decision: do it after the browser checks above and after the first live deploy (which runs migrations 002-005 on the live database; take a dump first).

## 2026-10-20 — Phase 3, part 1: lazy book data, and the corrected HTML baseline (branch phase/p2-server)
Done:
- Lazy loading of large book data (PERF-01), nothing in `index.html` changed: `js/core/lazy.js` (forwarding stand-ins that load a data file on first use), `tools/build/make_lazy.js` (generates `lazy.html` + `content/lazy_manifest.json`, `--check` for CI), eager list and 15 overlay scripts in `tools/build/*.json`, measurement and parity tools. 129 of 261 scripts (289 MB) are lazy. Measured in the Node sandbox: ready 7.2-7.5 s -> 1.8 s, heap 1,063 MB -> 241 MB, 0 lazy files loaded at start. Design, rules and limits: `docs/PHASE3_LAZY_LOADING.md`.
- The HTML snapshot tool had a fidelity hole (found while checking order dependence): it hashed stale content for the five Maths subjects (their own view, `selectMathChapter`) and skipped the 12 chapterless pre-school pages. `tools/snapshot_html.js` now follows the three real views, blanks the content element before every tab, starts each render from the `state` values at load (sticky sub-selections, listed by the new `tools/stateleak.js`: finding ARCH-02b), and renames per-render random ids (sb_mcq, ids inside Maths diagrams, class prefix of shared-book answer ids) by first appearance. Baseline regenerated: `tests/baseline/html-2026-10-20` (old `html-2026-10-19` removed).

Verified by (clean checkout of the committed state, `git worktree` sparse):
- Snapshot of the eager page: 147 subjects, 1,843 chapters, 9,710 tab renders, 0 step errors. Forward vs reverse subject order on the eager page: 0 differences (before the fixes: 190; with the first tool version 1,522).
- `node tools/build/lazy_parity.js` and `--reverse`: eager page vs `lazy.html`, 9,710 renders each, 0 differences in both orders; 115 of 129 lazy files had been loaded by the end of the run, 282 of 288 MB.
- Working tree vs the new baseline: only the 20 `cls1-eng` renders differ (uncommitted edits by another session, not mine).
- Earlier in this phase: smoke 251/0 on `lazy.html`; validate 973/0 (Contract C locks the `CLSn_BOOKS` keys); `make_lazy.js --check` clean.

Not verified: any of it in a real browser (Chrome cannot run here: the Proxy stand-ins and synchronous requests follow the spec but were only exercised in the Node sandbox); load times on a phone; compression and cache headers (not done); the generated `lazy.html` on the live host (it is deployed beside `index.html` but nothing links to it).

Regressions: none known. `index.html` is untouched by this phase (the committed one still loads everything).

Risks: the lazy page blocks the page for one synchronous transfer + parse the first time a book is touched (about 1 s for the 20 MB Class 12 Physics file here); features that scan every book (global search, word statistics, Papers) still load them all. The 79 data-like files that stay eager (about 40 MB: legacy `DATA` extenders, Class 11, `urdu_data.js`, `math_*_data.js`) are not lazy yet. ARCH-02b stays open: the sticky `state` keys are only neutralised in the test tool, not in the app.

Next: make the remaining eager data lazy one subject group at a time with the same parity proof; JSON Schema + validator for Book Content Contract v1; one-command generation of manifest/search index/MCQ bank/study index; registry-driven `openSubject`; then the cut-over decision (owner) described in `docs/PHASE3_LAZY_LOADING.md`.

## 2026-10-20 — Phase 3: ARCH-02 fixed (book lookup no longer depends on the previously selected class)
Done:
- `js/app.js` `getSubjectChapterList`: 82 tests of the form `classId === 'clsN' || state.selectedClass === 'clsN'` became `cur === 'clsN'` with `const cur = classId || state.selectedClass` (the class asked for wins; the selected class only answers when the caller names none). `js/class11_study_views.js` wrapper likewise. Reproduced first: `getSubjectChapterList('eng', 'cls9')` with `state.selectedClass = 'cls7'` returned the Class 7 book.
- New test `tools/arch02_matrix.js` (`--page lazy.html` too) and a CI step: records the (subject, class) pairs the app asks for while opening all 147 subjects, then fetches each list with `state.selectedClass` set to every class id, `''` and `null`.

Verified by:
- Before the fix: 143 pairs x 17 values = 2,431 lookups, 186 differences. After: 0 differences on `index.html` and on `lazy.html`.
- Rendering unchanged: snapshot of the working tree vs `tests/baseline/html-2026-10-20`: 9,710 renders, only the 20 known `cls1-eng` differences (another session's uncommitted edits). validate 975/0, smoke 0 failed, trace_globals 147 subjects 0 step errors.

Not verified: in a real browser; callers that pass a class id different from the selected class on purpose and relied on the old OR (the snapshot, smoke and trace runs found none, but they only cover what those tools open).

Risks: 67 other `state.selectedClass ===` tests remain in `app.js` (outside this function); they move with their consumers. The matrix proves the list lookup only, not every consumer that reads `state` (papers, search, word statistics).

Next: registry-driven `openSubject` / one lookup table replacing the if-chains (ARCH-03), JSON Schema + validator for Book Content Contract v1.

## 2026-10-20 — Phase 3: lazy loading now covers Class 11, Class 12 Maths and the legacy Class 9/10 DATA files
Done:
- `tools/build/make_lazy.js` / `js/core/lazy.js`: public functions of a lazy file get forwarding stubs (705), keys a file adds to `DATA` are accessors until it loads (`SBLazy.attachData(DATA)` injected after `data.js`), the Class 11 registry `CLASS11_BOOKS` is a book container, and overlay scripts that declare functions get stubs bound to their parent. 152 files / 344 MB are lazy (was 129 / 289 MB); 47 patch scripts run after their parent (was 15). The build refuses a lazy file whose function another script reassigns (none today) and has `--explain` to list every file that stays eager and why.
- Source fixes the move needed: `class11BookBySubject()` looks up by key instead of scanning (and loading) every Class 11 book (`tools/validate.js` checks the invariant); `math12_study_views.js` no longer builds every Maths 12 study bank at script load (`warmMath12StudyBanks`, called by the new `js/math12_study_bank_warm.js`, which is a script tag on `index.html` and an overlay on the lazy page); the manifest no longer carries the generation date and hashes the LF form of each file (`--check` would have failed on any other day or on a CRLF Windows checkout).
- `lazy.html` and `content/lazy_manifest.json` regenerated from a clean checkout of the source commit.

Verified by (clean checkout of the committed source, sparse worktree):
- `lazy_parity.js` and `--reverse`: eager vs lazy, 147 subjects, 1,843 chapters, 9,710 tab renders, 0 differences both ways; the eager page equals `tests/baseline/html-2026-10-20` (0 differences). The parity run caught three real defects on the way (an overlay that declares functions, the sandbox not running `attachData`, Chemistry/Physics Class 9/10 losing their chapters), all fixed before the commit.
- Working tree: validate 978/0, smoke 0 failed on `index.html` and on `lazy.html`, `arch02_matrix.js --page lazy.html` 0 differences.
- Measured in the Node sandbox: lazy page ready in 0.23-0.29 s (eager 7.5 s), 64 scripts (262), heap after load 21 MB (1,063 MB), 0 of 152 lazy files loaded at start; opening Class 9 Biology 113 ms / 28 MB; Class 12 Physics 1.4 s / 60 MB.

Not verified: a real browser (Proxy stand-ins, accessors and synchronous requests follow the spec but ran only in the Node sandbox); compressed transfer size (needs server compression, still to configure); `lazy.html` on the live host.

Regressions: none known; `index.html` changed only by the Maths 12 study-bank script tag and a version bump on `math12_study_views.js`.

Risks: scripts that read a lazy book at load load it at start-up (none today, measured); a future wrapper around a function of a lazy file makes the build keep that file eager.

Next: Class 10 English chain (3.1 MB) as one parent with overlays; JSON Schema + validator for Book Content Contract v1 and per-book adapter reports; registry-driven `openSubject`; one command `tools/build/all.js` with stale checks; compression and cache headers.

## 2026-10-20 — Phase 3: one build command, content-hash URLs, server template, study index without a browser
Done:
- `tools/build/all.js` (+ `--check`, `--list`, `--only`): word stats, MCQ bank, study index, lazy page, in that order; `--check` runs each generator, compares with the committed file ignoring the generation date, restores the committed file, exits 1 when stale. CI runs it (replaces the `make_lazy --check` step).
- `tools/study_plan/node_backend.js`: the study index is built in the app sandbox (jsdom reads the rendered sidebar), 25 s, no Chrome; `--browser` keeps the old path. The committed index was stale (DATA-02) and is regenerated: Class 11 Maths 7 -> 12 chapters, Class 12 Physics/Chemistry/Statistics/English/Urdu exercise-bank counts, 5 phantom sidebar rows gone. `index.html` tag bumped to `study_plan_index.js?v=20261020_i2`.
- `lazy.html` / `lazy.js`: content-hash `?v=` on every script, stylesheet and lazy book file (the page is stale the moment any of them changes). `deploy/spacebook.htaccess` + `docs/SERVER_CONFIG.md`: gzip/brotli, `no-cache` by default, one-year `immutable` for hashed URLs, `Options -Indexes`; a template the owner reviews and installs (not uploaded by CI: a wrong `.htaccess` is a site-wide 500).

Verified by:
- Clean sparse checkout of the committed source (`git worktree`): `all.js` regenerate then `all.js --check` -> word-stats, mcq-bank, study-index and lazy all fresh (word stats ran with a 2 GB heap, so CI's 6 GB is ample).
- Working tree: lazy page equals the eager page on all 9,710 renders (after the hash-URL change), `measure_lazy.js --startup-only` 0 of 152 files at start, tests/sync/planner.js 15/0, validate 978/0, smoke 0 failed.

Not verified: the `.htaccess` template on the host (cannot be tested here), compressed sizes, the CI step (never run on GitHub), the study index counts against a browser run beyond the differences listed above.

Regressions: none known. Risk: every JS change now makes `lazy.html` stale, so a commit that touches any script must include the output of `tools/build/all.js` or CI fails; this is by design (derived files always current) but changes the contributors' routine (documented in CONTRIBUTING section 3).

Next: Book Content Contract v1 (schema, validator, adapters with per-book count reports), registry-driven `openSubject`/chapter lookup, the Class 10 English chain.

## 2026-10-20 — Phase 3: status summary and what is carried forward
Done in Phase 3: lazy loading of 153 book files (347 MB) with parity proof (9,710 renders, both orders), ARCH-02 fixed with a matrix test, the HTML baseline rebuilt and made order-independent, one build command with a CI staleness check (word stats, MCQ bank, study index without a browser, lazy page), content-hash URLs, a server template for compression/caching, the stale study index (DATA-02) regenerated.

Measured against the phase's acceptance criteria (Node sandbox; no real browser): initial transfer 1.6 MB gzip (<= 3 MB) met; DOMContentLoaded-equivalent 0.18-0.29 s (<= 2 s) met; heap after home 21 MB (<= 80 MB) met; all subjects parity-green met; derived files always current (CI) met; **no eval in content lookup: not met** (4 lookups in `class11_study_views.js`, `class12_exercise_banks.js`, `universal_translate.js`, plus the loader's own indirect eval).

Carried forward, with the reason: Book Content Contract v1 (schema, validator, adapters, per-book count reports), `SB.content.getBook`, registry-driven `openSubject`/chapter lookup, the remaining 67 `state.selectedClass` tests in `app.js`, the eval lookups. They are a consumer migration across 147 subjects whose payoff is the render core (Phase 5) and the multilingual engine (Phase 7); doing them now would move every consumer twice. Phase 4 (offline) starts from the lazy manifest instead, which already gives hashed, cacheable book packages.

## 2026-10-20 — Phase 4: offline-first (service worker, downloads, device voices)
Done (details and the honest "not verified" list: `docs/PHASE4_OFFLINE.md`):
- `sw.js` + generated `content/sw_version.js`: versioned shell cache (103 files), hash-addressed book cache that survives updates, asset cache; never caches the API, other origins or non-GET; updates wait for the student. `manifest.webmanifest`, `icons/` (192, 512, maskable, apple-touch; drawn, replaceable), `offline.html`. `index.html` links the manifest and no longer links Google Fonts.
- `js/core/offline.js` + `css/offline.css`: service worker registration and the "Update now" banner; the "Offline books" dialog (⬇ in the header): per-subject sizes, free space, download with progress and sha256 verification (CRLF-tolerant), quota check before and during, abort, remove that keeps files other subjects share, persistent-storage request; offline badge; message when a book cannot be fetched.
- `tools/build/make_offline.js` (part of `tools/build/all.js`): `content/offline_map.json` (what each of the 147 subjects loads, found by rendering all of it in a fresh app) and the worker version/shell list.
- Read-aloud: `js/core/tts.js` + `css/tts.css`; the English and Urdu sentence readers and the universal translator speak with device voices only (Google translate_tts removed), buttons are hidden for a language with no voice, a cancelled utterance no longer advances the reading.
- `js/core/lazy.js`: fetches a subject's files before running any of them, resets the "loaded" mark when a fetch fails (so it can be retried after a download), signals `sb:lazy-error`, treats status 0 with no text as a failure.
- Fewer accidental downloads: Class 9/10/11 physics no longer loads the 18 MB Class 12 book, Class 6-10 subjects no longer load the Class 11 book of the same key, Class 11/12 English no longer loads Class 10 English (rendered output unchanged).
- Tests: `tests/offline/{sw,offline,tts}.js` (33 + 41 + 23), `tests/offline/mutate.js` (9 mutations, all caught), validate.js offline section (11 checks), CI steps.

Verified by: the three suites above (all pass), mutation run (all caught), validate 993/0, smoke 0 failed on both pages, HTML snapshot eager = lazy = previous eager (0 differences in 9,710 renders), ARCH-02 matrix 0 differences.

Not verified: any of it in a real browser (service worker lifecycle, install prompt, a synchronous XHR answered by the worker, real storage quota, Safari eviction, Lighthouse PWA audit, the look of the dialog, speech on real voices); the `.htaccess` template; fonts are not bundled (waiting for your OK to download the Noto fonts).

Risks: Urdu read-aloud is now only as good as the Urdu voice on the device (many phones have none: the button is then hidden instead of calling Google); subjects of Classes 7-10 still pull their Class 6 sibling book for its word list (Phase 7); `start_url` stays `lazy.html` until the cut-over.

Next: Phase 5 (hooks instead of patches in the rendering core), starting from the wrappers and observers list in the audit.

## 2026-10-20 — Phase 6 (first part): content integrity — answer keys, placeholder media, dead PDF links
Done (owner decisions and numbers: `docs/CONTENT_REVIEW.md`):
- CONT-02: `sbMcqKey()` is the one reader of "which option is right"; the Papers pool used it in 9 places where it had read `correctIndex`/`ans` and defaulted to option A. In the pool, all Islamiat and Urdu keys and the Class 1-6/9/11/12 Maths keys were "A"; Islamiat is now 23 % A, Urdu 22 %. A question without a key prints "Key not available" and fills no OMR bubble. (84 %+ of the Maths keys are still A: those are the generated questions below, not a reading error.)
- CONT-03: no more fake video lectures (a test URL with invented titles/durations/instructor in 15 Islamiat chapters; a fake "1080p" Maths player and its tab button).
- PDF-01: no "Download PDF"/"Read Online" button or "PDF Available" claim unless a licensed copy is packaged (`SB_PACKAGED_PDFS`, empty): all former links were dead (`assets/books/` missing, `file:///D:/...`, a network share).
- CONT-01 (generated "Board SLO" practice, 1,860 items in Class 9/10 Maths): marked `generated: true`; switch `hideGeneratedSlo` (off) removes them from the tab and from Papers; waiting for your approval. `tools/content_lint.js` reports and gates (`tests/contract/content_lint.json`).

Verified by: `node tests/content/integrity.js` 32/0 (key reader, pool keys keep their source keys, no key defaulting to A, placeholder video not embedded, real embed still renders, no fake Maths player, generated items marked and hidden by the flag with authored section 1.1 untouched, no dead PDF button), mutation check (the PDF tests fail on the code before the fix), `tools/content_lint.js --check` (baseline), validate 993/0, smoke 0 failed, HTML snapshot: the only changed renders are the 30 Class 9/10 Maths "lesson" tab bars (the Video tab button is gone), everything else identical (9,710 renders).

Not verified: in a browser (the look of the empty states and of the library cards without PDF buttons); Papers printing end to end (only the pool and the key code are tested); the factual claim about Cayley (not changed).

Risks: students lose the dead buttons only; the generated questions stay until you approve (flag); Papers for Classes 1-6, 11 and 12 Maths still draw on Class 9 questions (Phase 9).

Next: Phase 5 (hooks instead of patches in the rendering core), then the Phase 6 tab model on top of it.

## 2026-10-20 — Phase 5 (first part): function wrappers replaced by SBHooks (ARCH-01, half of it)
Done (design, rules and the honest list of what is NOT done: `docs/PHASE5_HOOKS.md`):
- `js/core/hooks.js` (`SBHooks.use` / `replace` / `list`): one registry for "this function is extended by other modules", composition order = script order = the old wrapper order. The 109 hand-made wrappers of 53 global functions (35 files; `switchSubjectTab` 14, `openSubject` 7, `getSubjectChapterList` 6, the Maths renderers, `continue_learning.js` 20...) now register with it; each wrapper body is unchanged.
- `tools/wrappers_audit.js --check` (CI): no script may replace a global function itself any more (before: 53 functions / 109 replacements; now 0). `tests/contract/hooks.json` + `tests/hooks/hooks.js` (CI): who extends what, in which order.
- Found on the way: the codemod removed a `const orig = window.f` that a nearby `typeof orig` guard still used (`continue_learning.js`, `test_prep.js`): both fixed; an orphan scan (`typeof` guards and later uses of the removed variable) found no other.

Verified by: HTML snapshot of all 9,710 chapter/tab renders identical before and after, on the lazy and the normal page (0 differences, both pages equal); `tests/hooks/hooks.js` 17/0 (registry unit tests, lock file, continue-learning still records a chapter, Class 5 reader renders through the hook, an unowned subject reaches the original renderer); `tools/wrappers_audit.js --check` ok; smoke 0 failed on both pages; validate 995/0.

Not verified: in a real browser; the render-time behaviour of the 19 `MutationObserver`s (not changed here: the snapshot cannot see them, see PHASE5_HOOKS.md); `continue_learning` beyond the recorded chapter, `word_stats` and `universal_translate` overrides (their hook registration is checked by the lock, their behaviour by the parity of what they wrap, not exercised).

Risks: a new file that still wraps a function itself is caught by CI only after the fact; a function not defined when a module registers (hooking a name that does not exist yet) now throws instead of silently skipping where the old code returned early.

Next: a DOM-level comparison tool (jsdom with working observers) so the observers can be converted module by module; then the rest of the Phase 5 list.

## 2026-10-20 — Phase 7 (first part): offline meanings from one generated lexicon, no text sent to third parties
Done (`docs/PHASE7_LEXICON.md`, `docs/LEXICON_COVERAGE.md`):
- The first word lookup on the lazy page loaded 106 book files (150 MB, ~10 s) to build the offline lexicon. `tools/build/make_lexicon.js` now builds it at build time into `js/lexicon_data.js` (12,738 rows, 0.64 MB; part of `tools/build/all.js`); `universal_translate.js` adds the rows instead of scanning the books: 1 file / 1 MB / 0.4 s.
- SEC-04: the calls to Google (selection translation, word statistics) and MyMemory (selection translation, the word popover, which also wrote machine text into the dictionary) are removed. Nothing is sent to any website; an owner-approved server proxy (`window.SB_TRANSLATE_PROXY`) is the only possible way online, off by default.
- Coverage report (per direction and class, types and occurrences) and six review queues of the most frequent words without a meaning: `tools/build/lexicon_report.js`.

Verified by: `tests/lexicon/equivalence.js` 5/0 (the generated rows answer exactly like the old book scan on ~4,800 lookups in 12 directions; a lookup loads the lexicon and the dictionary, no book); `tests/lexicon/privacy.js` 8/0 (no request to any website while translating a sentence, a word, or using the old word lookup; with a proxy only the proxy is called; no script names a third-party translation/speech host); validate and smoke see below.

Not verified: the hover/selection UI in a browser; the proxy path against a real server (none exists); lexicon rows have no per-row provenance yet.

Result for the owner: offline coverage by occurrences: English->Urdu 84.3 %, ->Pashto 78.7 %, ->Arabic 63.2 % (targets 95 / 95 / 85 not met: translation work, queues in `docs/lexicon_review/`).

Risks: students who relied on Google for sentences no book translates now get a word-by-word gloss or "meaning not yet available"; the previously cached online translations in their browsers stay (labelled as machine text).

Next: Phase 7 interaction component and per-row provenance when reviewed meanings arrive; Phase 8 and the modules.

## 2026-10-20 — Phase 6 (addendum), Phase 8 (what could be done), Phase 10 (first part)
- Papers pool: the 288 "Review Exercise" MCQs parsed from book text no longer get the key A (they are key-less, "Key not available"); the per-unit English thematic MCQs are marked `generated` and hidden by the same owner switch (`docs/CONTENT_REVIEW.md`). `tools/content_lint.js` baseline updated (paperMcqsWithoutKey 5 -> 293: the 288 were hidden as "A" before). `tests/content/integrity.js` 35/0.
- Phase 8 (`docs/PHASE8_SECURITY.md`): security headers and a **report-only** CSP in `deploy/spacebook.htaccess`; no third parties (validate); everything that needs a decision of yours (signing key, licensing model, repository visibility) or the Phase 5 refactor (enforcing the CSP: 418 inline handlers in `app.js`, `eval`) is listed with the reason, plus the threat model in plain words. Nothing was faked: no signing, licensing, encryption or watermark exists.
- Phase 10 (`docs/CLEANUP_LOG.md`): `tools/cleanup/archive.js` moved 10,264 untracked files (7.2 GB: `tmp/`, `tools/source-review/`, staging folders, page images, backups) to `D:\SpaceBook\SpaceBook_Archive` with a path/size/SHA-256 log; nothing deleted. Working folder 8.0 GB -> 1.4 GB, production payload unchanged, disk freed 0 (same drive). validate 999/0 and smoke 0 failed after the move. The tracked leftovers, the 404/network-log checks and `git gc` are listed with their reasons.

## 2026-10-20 — Phase 12 (first part): keyboard and screen-reader basics (`js/core/a11y.js`)
Done (rules for contributors: `CONTRIBUTING.md` section 4f):
- Tab bars (every group of buttons whose class contains `tab-btn` or `top-tab`: chapter tabs, Maths tabs, sub-tab bars): `role=tablist` / `tab`, `aria-selected` follows the active tab, roving `tabindex` (one tab stop per bar), arrow keys (mirrored in right-to-left pages), Home and End open the tab reached and keep the focus on it, also when opening the tab reorders or redraws the bar. The Word Stats button is in the bar as an action, outside the arrow-key cycle. Applied after the 15 render functions that draw bars (through SBHooks, `switchSubjectTab` now has 15 extensions) and after every click; no MutationObserver.
- `SBA11y.trap(dialog, { onClose })`: Tab stays inside, Escape closes, the focus returns to the opener; controls inside hidden / `aria-hidden` / inert branches and inside a closed `<details>` do not count as first or last. Used by the sign-in dialog, the account dialog and the Offline books dialog.

Verified by: `tests/a11y/tabs.js` 26/0 in a real DOM (jsdom, the lazy page): roles, one selected tab, one tab stop, ArrowRight / Home / End open the tab and the focus follows (this found that moving a tab button, not only replacing it, makes the browser drop the focus: fixed), a click moves the selection, trap wrap both ways, Escape, focus return, hidden-control handling, the sign-in and offline dialogs; a mutation (`reachable()` always true) makes 3 of the checks fail. `tests/hooks/hooks.js` 17/0 with the lock updated (a11y.js appended to 15 functions), `tools/wrappers_audit.js --check` ok, validate 1001/0, smoke 0 failed on `index.html` and `lazy.html`, offline 33/41/23 and sync 51 pass, HTML snapshot of Classes 9 and 10 (1,535 tab renders) identical to the baseline.

Not verified: with a real screen reader (NVDA / TalkBack / VoiceOver) and in a real browser (the visible focus ring, the tab order of the whole page, the sign-in dialog on a phone); contrast and the remaining pages (reader pages, MCQ radios, the Papers views) are not audited; the other dialogs (menus, Word Stats, translate popover) do not use the trap yet; `lazy.html` / `sw_version.js` are regenerated separately.

Risks: a page that sets `role` or `tabindex` on a tab itself is overwritten on the next sync; a bar with fewer than two visible tabs is left alone.

Next: regenerate the derived files from a clean checkout; then the Phase 12 remainder (axe-style checks across the reader views, offline full-text search, docs) and the second half of Phase 5.
