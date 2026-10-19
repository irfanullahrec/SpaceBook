# Contributing to SpaceBook

SpaceBook is a vanilla-JS portal (no bundler, no framework) for KPTBB textbooks, Classes 1–12, with a small PHP/MySQL API for user records. `index.html` loads 248 scripts in order; `js/app.js` is the controller; each book is a data file plus a reader.

The rule that matters most: **a change must not alter any subject you did not mean to touch.** The checks below exist to prove that.

## 1. Every change

```bash
git switch -c fix/short-name            # one branch per task or per subject
# ... edit ...
node tools/validate.js                  # syntax, datasets, wiring, rebuilt-book contract (~950 checks)
node --max-old-space-size=8192 tools/smoke.js   # loads the whole app, opens every rebuilt book and tab (~20 s)
git commit                              # small commits, one finding or one subject each
```

Both scripts must print 0 failures; CI (`.github/workflows/deploy.yml`, job `test`) runs them and **blocks the deploy** if either fails. Never force-push `main`; undo with `git revert`.

Changed `api/`? Also run (needs local MySQL, e.g. XAMPP; uses a throwaway database `spacebook_test`, never your real one):

```bash
node tools/php74_lint.js        # PHP 8-only syntax is rejected: the live host ran PHP 7.4
php tests/php/run.php           # migrations, auth hardening, rate limits, device tokens, v2 sync, account, backup drill (196 checks)
node tests/sync/unit.js         # client core js/core: outbox, back-off, pull merge (39 checks, no PHP needed)
node tests/sync/e2e.js          # real client against the real API on the scratch DB (17 checks)
node tests/sync/rewards.js      # the real sb_rewards.js in the app sandbox against the real API (15 checks)
node tests/sync/planner.js      # the real sb_study_plan.js likewise (13 checks)
node tests/sync/testprep.js     # the real test_prep.js with the real MCQ bank likewise (17 checks)
node tests/sync/account.js      # the "My account" screen of auth.js in a real DOM (jsdom) against the API (17 checks)
```

Setup for the browser tools only: `npm install` (Playwright, dev-only; nothing from `package.json`, `node_modules/` or `tests/` is deployed).

## 2. Where content lives (five contracts, all still in use)

| Contract | Classes | Shape |
|---|---|---|
| A. `Object.assign(DATA, …)` | legacy 9/10 | `js/data_chem.js`, `data_phys.js`, `data_eng.js`, `data_bio.js`, `data_comp.js` |
| B. Named globals | legacy | `BIO_DATA`, `ENGLISH_DATA`, `MATH_DATA`, … picked by if-chains in `getSubjectChapterList` (`js/app.js`) |
| C. `window.CLSn_BOOKS[subject] = {units, book, words}` | **1–10 rebuilt books** | one file per book, e.g. `js/math_2_data.js`; `CLS6_SOLUTIONS` is shared |
| D. `CLASS11_BOOKS` + render functions | 11 | routed by `js/class11_study_views.js` |
| E. per-subject data + exercise banks | 12 | routed by `js/class12_study_views.js` |

`js/data.js` is the registry (classes, subjects, books). Add a subject there and one `<script>` line in `index.html` **before** `js/app.js`.

Chapter lookup must come from the arguments (`classId`, `subjKey`), never from `state.selectedClass` (defect ARCH-02, fixed: `getSubjectChapterList('eng', 'cls9')` returned the Class 7 book while `state.selectedClass` was `cls7`; `node tools/arch02_matrix.js` and CI keep it fixed).

## 3. Never hand-edit generated files

| File | Regenerate with |
|---|---|
| Rebuilt book data, `js/<subject>_<class>_data.js` | the class pipeline in `docs/source-verification/class-N/tools/` (e.g. `build_book2.py`); edit the page transcriptions, not the JS |
| `js/test_prep_bank.js`, `js/study_plan_index.js`, `js/word_stats_words.js`, `js/word_stats_summary.js`, `lazy.html`, `content/lazy_manifest.json` | **`node --max-old-space-size=8192 tools/build/all.js`** (one command; `--list` says what each step reads, `--only word-stats,lazy` runs a subset). The individual generators are `tools/test_prep/build_mcq_bank.js`, `tools/study_plan/build_study_index.js` (no browser needed any more), `tools/word_stats/build_word_stats.js`, `tools/build/make_lazy.js`. |
| `tests/contract/cls_books.json` (unit counts) | `node tools/validate.js --update-books` — only after an intended rebuild; commit the diff |
| `tests/trace/**` | `node --max-old-space-size=8192 tools/trace_globals.js` |

Rerun `tools/build/all.js` after data changes (CI runs it with `--check` and fails when a committed output is stale; the generation date is ignored). Run it from a clean checkout before a release: the outputs describe the committed data, not whatever else is lying in the working tree. Data changes are reviewed as diffs; do not invent textbook text, translations presented as book text, or board questions. Qur'anic text is never translated or altered.

## 4. Regression rule

- Changing a **shared file** (`js/app.js`, `css/style.css`, `index.html`, any `sb_*.js`, readers, `structure_harmonizer.js`, `universal_translate.js`, `class11_study_views.js`, `class12_*`): run validate + smoke, and check the subjects that use it. `tests/trace/index.json` (`globalsToSubjects`) lists which subjects read which data global, so you can find a subject's neighbours.
- Changing **one subject's data**: validate + smoke, then open that book in the browser.
- No broad search-and-replace across `js/` or `css/` without a dependency check.
- Unused files are moved to `D:\SpaceBook\SpaceBook_Archive\` with a log, never deleted.

`tests/trace` records only data globals read while a subject is opened and its tabs rendered (first/middle/last chapter). A global that appears "never read" may still be used at load time or by features the tracer does not open; do not remove a file on that evidence alone.

## 4a. Lazy book data

`lazy.html` is generated from `index.html` (`node tools/build/make_lazy.js`, or `tools/build/all.js` which also runs it last; every script and stylesheet in it carries the content hash of the file as `?v=`, so changing ANY script makes `lazy.html` stale; details and numbers in `docs/PHASE3_LAZY_LOADING.md`). Adding or renaming a script in `index.html`, or changing which globals a data file defines, makes it stale: regenerate and commit it (CI runs `make_lazy.js --check` and `tools/build/lazy_parity.js`, which renders every subject on both pages and requires identical HTML). A script that only patches lazy data at load goes into `tools/build/lazy_overlays.json` (it then runs right after its parent file loads, so do not read the book at script load: touching a lazy book from an eager script loads it at start-up; `node tools/build/measure_lazy.js --startup-only` must say `0 of N`); a data-like file that must be in the page at load goes into `lazy_eager.json`. Do not reassign (wrap) a function that a lazy file declares: the build keeps such a file eager and says why (`node tools/build/make_lazy.js --check --explain` lists every file that stays eager).

## 4c. Offline layer

`sw.js`, `manifest.webmanifest`, `offline.html`, `icons/`, `js/core/offline.js`, `js/core/tts.js` (details: `docs/PHASE4_OFFLINE.md`). Rules: never cache `/api/` or another origin in the service worker; a book file is cached only under its `?v=<content hash>` URL; an update never deletes `sb-content-v1`, `sb-assets-v1` or anything in IndexedDB (the sync outbox lives there); read-aloud uses device voices only (no `translate_tts`, no third-party audio); no script, stylesheet or font from another website at start-up (`tools/validate.js` checks). After changing the page's scripts run `tools/build/all.js` (it regenerates the worker version and the offline map). Tests: `node tests/offline/sw.js`, `offline.js`, `tts.js`, and `node tests/offline/mutate.js` after touching `sw.js` or `offline.js`.

## 4d. Extending a function of another file: SBHooks

Never write `window.someFunction = function () { ... original ... }` for a function another file defined. Use `SBHooks.use('someFunction', next => function (...) { ... next.apply(this, arguments) ... })` to extend it or `SBHooks.replace('someFunction', fn)` to override it (`js/core/hooks.js`, loaded before `app.js`; details `docs/PHASE5_HOOKS.md`). Order = script order in `index.html`. `node tools/wrappers_audit.js --check` fails when a script still replaces a global function itself, and `node tests/hooks/hooks.js` compares who extends what with `tests/contract/hooks.json` (`--update` after an intended change).

## 4e. Meanings, translation and privacy

Word meanings come from `js/lexicon_data.js` (generated by `tools/build/make_lexicon.js` from the books' word lists, `ENG_URDU_DICT` and `SB_OFFLINE_LEXICON`; edit the sources, not the file) and are looked up on the device. **No script may send a word, a sentence or a selection to a website** (no Google/MyMemory/translate_tts): `tests/lexicon/privacy.js` and `tools/validate.js` fail otherwise. A translation service is allowed only behind the owner's own server (`window.SB_TRANSLATE_PROXY`, off by default) and its text is labelled as machine text. Do not write machine text into a dictionary or a book. Coverage: `node tools/build/lexicon_report.js --write`.

## 4b. Database changes

Never edit an applied migration and never create tables from endpoint code. Add `api/migrations/NNN_name.sql` (additive; idempotent `IF NOT EXISTS`) and, where safe, `NNN_name.down.sql`. The first request that finds the database behind applies pending migrations once under a database lock; `php api/migrate.php status|up|down [N]|prune` does the same by hand. Migration 001 has no down (it would drop student data). Take a `mysqldump` before migrating the live database. **A push to `main` deploys, and the first live request then runs any new migration.**

## 5. Secrets

`api/config.php` is gitignored and **never** goes into an upload package (`tools/build_upload_zip.py` refuses to include it). Create it once on the server from `api/config.sample.php`. CI writes it from repository secrets. Never put passwords, tokens or keys in the repository, in front-end code, or in any web-reachable file. Server steps for the owner: `docs/PHASE0_SERVER_STEPS.md`.

## 6. Deploy

Push to `main` → `test` job → FTPS upload to wantuch.pk (`security: strict`) → live check (`index.html` 200, no `spacebook_upload.zip`, `api/health.php` reports `"db":true`). Manual fallback: `python tools/build_upload_zip.py`, upload and extract, then delete the zip from the server. `api/` must stay compatible with the server's PHP (7.4 at last check).

## 7. Reader UI decisions to keep

No language tabs or drop-downs in readers; clicking a sentence opens a drawer with the other languages. Topic cards start collapsed, each with its own full-screen button. Chapter order follows the book: Lessons → Summary → Exercise → practice, nothing repeated. Class 9/10 layout is the reference for 11/12. Tab labels follow the subject's medium; only tabs with content appear.

## 8. Progress notes

Record each task in `docs/PROGRESS_LOG.md`: what was done, how it was verified (command and numbers), what was not verified, risks, next step. Do not write "complete" without a verification line.
