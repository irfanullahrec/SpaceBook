# Architecture (as built on 2026-10-20)

This replaces `01_PROJECT_STRUCTURE_AND_ARCHITECTURE.md`, written before the agent plan of 2026-10-19 (lazy loading, offline, hooks, sync, search). Where this file and an older one disagree, this one is right; where it and the code disagree, the code is right and this file has a bug: say so in `PROGRESS_LOG.md`.

SpaceBook (TuitionHub, KPK portal) is a **vanilla-JavaScript app** for the textbooks of the Khyber Pakhtunkhwa board, Classes 1-12, in English, Urdu, Pashto and Arabic, with a small **PHP + MySQL API** for accounts and for syncing a student's progress. There is no framework and no bundler. Everything the browser runs is a plain file in this folder.

## 1. The folder (`SpaceBook Web/`)

| Path | What it is | Edited by hand? |
|---|---|---|
| `index.html` | the source page: every `<script>` and stylesheet, the header, the sidebar, the dialogs | yes |
| `lazy.html` | **generated** copy of `index.html` that does not load the book data at start (section 4) | no |
| `offline.html`, `manifest.webmanifest`, `sw.js`, `icons/` | installable app and the page shown with no network (section 5) | yes |
| `js/app.js` | the core: routing, the subject workspace, the chapter/tab renderers, Papers, Tests Preps shell, global search of titles (about 23,000 lines) | yes (carefully) |
| `js/core/` | small modules with their own contract: `hooks` (extend a function), `lazy` (load data on first use), `offline` (download for offline), `tts` (read aloud), `a11y` (keyboard and screen reader), `search` (words inside the books), `lazycards` (owner flag, off: closed Maths cards cost nothing until opened), `store`/`sync`/`consent` (client side of sync), `items` (the student's own marks: bookmarks, notes, positions ...), `entitlements` (the plan answer shared with the app) | yes |
| `js/<subject>_<class>_data.js`, `js/*_book.js`, `js/data_*.js`, `js/*12_exercise_banks.js` | **book data**: verified transcriptions of the textbooks (about 150 files, 360 MB) | only through the class pipelines (section 6) |
| `js/*_reader.js`, `js/class11_study_views.js`, `js/class12_study_views.js` | renderers of the rebuilt books (Classes 1-12) | yes |
| `js/sb_*.js`, `js/structure_harmonizer.js`, `js/reader_tools.js`, `js/universal_translate.js`, `js/word_stats.js`, `js/test_prep.js`, `js/sb_study_plan.js`, `js/sb_rewards.js`, `js/continue_learning.js`, `js/sb_library.js`, `js/auth.js` | add-on modules loaded after `app.js`; they extend the core through `SBHooks` and, still, 19 `MutationObserver`s (section 3) | yes |
| `js/word_stats_*.js`, `js/test_prep_bank.js`, `js/study_plan_index.js`, `js/lexicon_data.js` | **generated** from the book data (section 6) | no |
| `css/` | stylesheets; `a11y.css` and `search.css` are the newest | yes |
| `content/` | **generated**: `lazy_manifest.json`, `offline_map.json`, `sw_version.js`, `search/` | no |
| `api/` | PHP 7.4-compatible API: `auth.php`, `v2/sync.php`, `v2/entitlements.php`, `billing.php`, `progress.php`, `study_plans.php`, `test_prep.php`, `health.php`, `admin.php`, `migrations/`, `lib/` | yes |
| `manage/` | the administrator's page (payments, users, subscriptions, extensions, dashboard, audit): `index.php` + `manage.css`, no JavaScript (`BILLING.md`) | yes |
| `deploy/spacebook.htaccess` | the server rules the owner installs (headers, report-only CSP) | yes |
| `docs/` | documentation and the per-class source-verification pipelines (`docs/source-verification/class-N/`) | yes |
| `tools/`, `tests/` | build, audit and test tooling; never deployed | yes |
| `covers/`, `assets/` | cover images, KaTeX, figures | yes |

Outside it, at the repository root: `.github/workflows/deploy.yml` (tests, then upload), `SpaceBook App/` (the separate Android app), `SpaceBook_Archive/` (moved scratch files, git-ignored; see `CLEANUP_LOG.md`).

## 2. How a page starts

1. The browser loads `lazy.html` (the entry the service worker caches; `index.html` still works and loads everything). Its `<script>` list is `index.html`'s, minus the book data.
2. `js/data.js` creates the registry `DATA` (classes, subjects, books). Per-subject files only add to it (`Object.assign(DATA, ...)` or a named global); see `DATA_CONTRACT.md`.
3. `js/core/lazy.js` and the inline manifest put a stand-in in place of every book global: touching `MATH_2_DATA` loads `js/math_2_data.js` (one synchronous request, then the real object). The shell therefore starts in about 0.2 s and about 20 MB of heap, against 7.5 s and 1 GB for the eager page (Node measurements; `PHASE3_LAZY_LOADING.md`).
4. `js/app.js`, the readers and the add-on modules load; `SBHooks` registrations happen in script order, and that order is locked in `tests/contract/hooks.json`.
5. `openSubject(classId, subjectId)` renders the subject workspace; `selectSubjectChapter(...)` / `selectMathChapter(...)` renders a chapter; `switchSubjectTab(...)` renders one tab (only the active tab is in the DOM).

State is a single object `state` in `app.js` (a top-level `const`, **not** `window.state`). Chapter lookups use the arguments, never the previously selected class (defect ARCH-02, fixed and guarded by `tools/arch02_matrix.js`).

## 3. Extending the core: SBHooks, and what is still not clean

`SBHooks.use(name, next => function (...) { ... })` extends a global function; `SBHooks.replace` replaces it. 109 hand-made wrappers of 53 functions were converted; `tools/wrappers_audit.js --check` fails if any script wraps a global function itself again, and `tests/contract/hooks.json` locks who extends what, in which order. Order is script order: a new module goes at the end of `index.html` unless it must run earlier.

Not clean yet (`PHASE5_HOOKS.md`): 19 `MutationObserver`s that re-process the page after a render (`sb_rtl`, `sb_medium`, `sb_trilingual`, `sb_structure`, ...), 22 injected `<style>` blocks, about 230 `!important`, 418 inline `onclick` handlers in `app.js` and `eval` in the lazy loader and four content lookups. These are why the content-security policy is report-only and why a render is not a single pass.

## 4. Lazy loading (Phase 3)

`tools/build/make_lazy.js` reads `index.html` and writes `lazy.html` and `content/lazy_manifest.json` (per file: path, size, sha256, which globals/keys/functions it provides, files that must load with it and overlays that patch it after). URLs carry a content hash (`?v=<12 hex>`), so a file is immutable. `tools/build/lazy_parity.js` renders every chapter and tab of every subject on both pages and requires identical HTML (9,710 renders, both orders). Any change to a script or to the script list makes `lazy.html` stale: regenerate (section 6).

## 5. Offline (Phase 4) and search (Phase 12)

- `sw.js` keeps three caches: the shell (the page and what it needs first; a new version is a new cache), `sb-content-v1` (hash-named book files and search shards; never wiped), `sb-assets-v1` (images and other files; answered from cache, refreshed in the background). Nothing from another origin and nothing under `api/` is cached.
- `js/core/offline.js` is the "Offline books" dialog: per subject it downloads the book files, the images and the subject's search shard listed in `content/offline_map.json` (generated by `tools/build/make_offline.js`), verifying each file's sha256.
- `js/core/search.js` adds "In the books" to the header search box from `content/search/` (`SEARCH.md`).
- Reading aloud uses the device's own voices only (`js/core/tts.js`); nothing is sent to a third party.
- The lexicon (`js/lexicon_data.js`) gives word meanings in the four languages with no network (`PHASE7_LEXICON.md`).

## 6. The build (what is generated, from what, with which command)

`node --max-old-space-size=8192 tools/build/all.js` runs, in this order: `word-stats`, `mcq-bank` (also writes `docs/test_prep_review/no_key.csv`), `study-index`, `lexicon`, `lazy`, `search`, `app-catalog` (what the Android app lists, section 11), `offline`. `--check` changes nothing and fails when a committed output is stale (CI). `--list` says what each step reads. **Generate from a clean checkout of the commit being released**: the outputs describe the committed data, not whatever else is lying in a working folder; see `RELEASE_AND_ROLLBACK.md`.

Book data is not built from `js/`: each class has a pipeline in `docs/source-verification/class-N/tools/` (Python/Node scripts that read the scanned pages' transcriptions and write the `js/*_data.js`). Edit the transcriptions and rerun the pipeline; never edit the generated `.js` by hand.

## 7. Accounts and sync (Phase 2)

- `api/auth.php`: register / login / logout / me, profile, password change, export, delete (30-day grace, then `php api/migrate.php purge`). Cookie session (SameSite=Lax) plus per-device bearer tokens (only the SHA-256 is stored). Throttled logins, same-site check on cookie POSTs, an audit log.
- `api/v2/sync.php`: the client queues events (`step`, `again`, `plan.save`, `plan.delete`, `tp.answer`, `tp.session`, `tp.run`, `tp.run.clear`, `tp.import`, `item.put`, `item.del`) in an outbox in IndexedDB (`js/core/store.js`, `sync.js`); the server applies each event id at most once, decides coins from facts (never from amounts the browser sends), and returns a cursor; `GET ?since=` pulls what changed. Caps: 600 coins and 300 new activities per 24 hours. Rejected events are recorded by code in `sync_errors`.
- The client side is **off by default**. The owner's one switch is published by the server (`flags.syncV2` in `api/auth.php?action=me` and `api/v2/entitlements.php`, from `api/lib/flags.php`: create `api/flags.local.php` on the server with `<?php return ['syncV2' => true];`, which a deploy does not undo); the website copies it to `localStorage sb_sync_server`, the Android app hands it to its page, and a browser can still force it with `sb_sync_v2 = 'on' | 'off'` or `window.SB_FLAGS.syncV2`. The owner switches it on after the first live checks.
- **User items** (bookmarks, notes and highlights, where the student stopped, marked words, best game runs, the chosen class, ticked SLOs, drills): one table `user_items` (migration 007) with a rule set per kind in `api/lib/items.php`, events `item.put` / `item.del`, returned by the pull as `items` / `itemsDeleted`; the later time wins, a delete is a tombstone, caps per kind. Website client: `js/core/items.js` (local first, queued like everything else, obeys the owner's switch) and `js/sb_library.js` (the buttons, the Saved page, positions, "my class"). The Android app keeps the same items in its own database.
- Schema: `api/migrations/001`-`007` with down scripts for 002-007; applied automatically by the first request that finds the database behind, under a lock; `php api/migrate.php status|up|down|prune|purge|make-admin|remove-admin`.
- `api/admin.php`: administration (`ADMIN.md`).
- **Plans, free limits, Easypaisa payments, subscriptions** (migration 010): `api/lib/billing.php` holds every rule, `api/billing.php` and `api/v2/entitlements.php` are what the website and the app call, `manage/` is the administrator's page; the free allowance is counted by the server per account or per visitor id; a payment is approved by hand and then opens the same access on both platforms. Everything about it, including the decisions taken where the request left a scope open, is in `BILLING.md`.

## 8. The modules built on the books

| Module | File | Notes |
|---|---|---|
| Papers (exam paper builder) | `js/app.js` (about lines 10200-13300) | the pool of a subject is the book data of its own class only (`sbPaperPoolBelongsTo`); keys come from `sbMcqKey`, never defaulted to A; Set A / B / C reorder questions and options with the key moved along; generated "Board SLO" items are hidden behind an owner flag |
| Tests Preps | `js/test_prep.js`, `js/test_prep_bank.js` | MCQ bank built from the books (only questions with a key from their source); progress synced as events |
| Study Plan | `js/sb_study_plan.js`, `js/study_plan_index.js` | chapter counts built from the books; plans synced |
| Word Stats | `js/word_stats.js` | counts per project, class and subject |
| Rewards | `js/sb_rewards.js` | coins decided on the server when sync is on |
| Interactive MCQs | `js/sb_mcq.js` | every MCQ is a radio group with right / wrong feedback |
| Saved: bookmarks, notes, highlights, "continue", "my class" | `js/sb_library.js`, `js/core/items.js`, `css/sb_library.css` | a 🔖 and a 📝 on every page of a book, Highlight / Note on selected words, a Saved page in the menu, the reading position and the class follow the account (item kinds `bm`, `note`, `pos`, `pref`); inside the Android app (`html.sbapp`) it draws nothing: the app has its own controls and writes the same items |
| BISE Swat Board centre | `js/sb_bise.js`, `css/sb_bise.css`, `js/bise_swat_data.js` (generated) | pattern, chapter weightage, SLOs, Board papers, Section A drill, e-answer sheet for Classes 9-12; a strip on chapters, a preset in Papers, a card on the class subject list (`07_BISE_SWAT_ALIGNMENT.md`) |
| Create Test | `js/sb_create_test.js`, `content/testbank/` (made by `tools/tests/build_test_bank.js`) | a test from a class, subjects, chapters or one topic: MCQs, true or false, fill in, calculations, grammar and vocabulary, short, long, activities; the books' own questions with their answers (a topic is the lesson section a question shares most words with); take it, print it (answer key), save it (localStorage `sbct:v1`); 81 MCQs whose options repeat are left out and listed in `docs/test_bank_review/repeated_options.csv` |
| Grammar Stats | `js/sb_grammar.js`, `content/grammar/` (`tools/grammar/build_grammar.js`, topics in `tools/grammar/topics.js`) | topics of English, Urdu, Pashto and Arabic grammar from easy to hard with the books' own lessons and practice questions; a card on Home > Project Stats and a page; the Arabic books are reading lessons, so Arabic is small |
| Ask SpaceBook (offline tutor) | `js/sb_tutor.js`, `content/assistant/` (`tools/assistant/build_assistant.js`), the test bank, `content/search/`, the lexicon | BM25 over the books' passages, the books' own answers, definitions and word meanings, chapter links; no model, nothing sent anywhere; Class 11 and subjects without passages are found by chapter through the search index |
| Fill the table / Show the work | `js/sb_fill.js`, `js/fills_data.js` (`tools/fills/build_fills.js`, sources `tools/fills/src/*.json`) | a button next to a table with empty cells or a project / activity box when an answer was written for it (key = hash of the book and the text; a source that does not line up with the book fails the build) |

## 9. Tests (what guards what)

| Command | Guards |
|---|---|
| `node tools/validate.js` | syntax of every script, datasets, `index.html` wiring, the rebuilt-book contract, no third-party requests |
| `node --max-old-space-size=8192 tools/smoke.js` (`SB_PAGE=lazy.html` for the lazy page) | the whole app loads, every rebuilt book and tab opens |
| `tools/arch02_matrix.js`, `tools/wrappers_audit.js --check`, `tests/hooks/hooks.js` | chapter lookup, no wrapper of a global function, the hook registry |
| `tools/build/lazy_parity.js [--reverse]`, `tools/build/all.js --check` | the lazy page renders the same HTML; no stale generated file |
| `tests/offline/*.js`, `tests/search/search.js`, `tests/lexicon/*.js` | service worker, downloads, read aloud, search, lexicon |
| `tests/content/integrity.js`, `tools/content_lint.js --check` | answer keys, placeholder media, dead PDF links, class pools, paper sets, Test Prep bank |
| `tests/a11y/tabs.js`, `contrast.js`, `axe.js`, `tools/a11y_contrast.js --check` | keyboard, dialogs, language, text contrast, axe-core on 15 views |
| `php tests/php/run.php`, `tests/sync/*.js` | migrations, auth, sync rules, plans, test prep, account, administration, user items, owner flags; the real client against the real API (`items.js`, `parity_e2e.js`) |
| `node tools/parity/check.js`, `tools/parity/data_parity.js`, `tests/parity/*.js`, `tests/plan/reminders.js`, `tests/sync/entitlements.js` | the Web / App matrix against both platforms' code; every class, subject, chapter, file and the app's bundled shell against the website; where a page is; the numbers of Home; reminders; the plan answer (section 11) |
| `node tests/library/browser.js` | bookmarks, notes, highlights, Saved, "my class" in a real Chrome (local only: CI has no browser) |
| `node tools/snapshot_html.js --out <dir>` then `--compare tests/baseline/html-2026-10-20 <dir>` | the HTML of every chapter and tab, 9,710 renders |

None of these runs a real browser; `tests/baseline/run.js` (Playwright) exists and has never been run. The first real-browser check is still to be done by a person (`PROGRESS_LOG.md`, "Not verified" lines).

## 10. Deploy

A push to `main` runs the `test` job and, if it passes, uploads `SpaceBook Web/` to the host over FTPS (excluding `docs/`, `tools/`, `tests/`, `kotlin/`, dev files), writing `api/config.php` from repository secrets. The first request after a deploy applies pending migrations to the live database. Details, rollback and the owner's server steps: `RELEASE_AND_ROLLBACK.md`, `SERVER_CONFIG.md`, `PHASE0_SERVER_STEPS.md`, `BACKUP_RESTORE.md`.

## 11. One product on two platforms (the Android app)

`SpaceBook App/` is its own repository (the outer repository ignores it). The two are **the same in functions, data and database**; only the user interface differs. The rules for whoever works here next are in `D:\SpaceBook\CLAUDE.md`: a request about functions, data, the API, content or tests is a request for both platforms; look-and-layout only changes the platform named; data flows from this folder to the app, never the other way.

- **One database.** The app never talks to MySQL and holds no credential; both platforms use `tafseelk_spacebook` through the same PHP endpoints. `docs/parity.json` lists the endpoints the app calls, the sync event types each platform sends and the item kinds each writes; `tools/parity/check.js` fails when the lists and the code disagree, when a migration has no down script or no PHP test, or when `docs/PARITY_MATRIX.md` is not the table made from the JSON.
- **The matrix.** `docs/PARITY_MATRIX.md` (generated; do not edit) says for every function what each platform does and where its data lives. `web-only`, `app-only`, `partial`, `blocked` and `retired` rows carry a written reason and, where it is the owner's call, the decision.
- **Data parity.** `node tools/app/sync_app.js` regenerates everything the app bundles (the shell in `assets/site`, `app_catalog.json`, `mcq_bank.json`, `prep_tests.json`, covers, the golden test files) and `--check` lists what is stale; it must run from a clean checkout of the commit being released. `node --max-old-space-size=8192 tools/parity/data_parity.js` fails when a class, subject, chapter or book of the registry is missing from the catalog or the offline map (exemptions are named in `parity.json` with the reason), when a file of the offline map has the wrong size or SHA-256, when `lazy.html` names a script the app can neither bundle nor download, or when the app's bundled files are not what the website produces now.
- **Same behaviour.** `tests/sync/parity_e2e.js` plays the app (a raw client sending exactly `tests/parity/events_contract.json`) and the website (the real client code) on one account against the real API, both directions; the app's `EventContractTest` checks its own events against the same contract; `tests/parity/locator.js` checks that the website's page locator and the app's bridge find the same pages; `tests/parity/app_pages.js` runs the website's pages with the app's stylesheet and bridge in a touch Chrome at phone width; `tests/parity/stats_numbers.js` compares the numbers of Home.
- **Plans and payments** are the same on both: the plans window, the Easypaisa payment window and "My plans" are `js/sb_billing.js`, which the app shows inside its web page (`SBApp.openPlans`, `openMyPlans`); the chapter lock, the question and paper limits are `js/sb_access.js` (the app also locks its native chapter list, `access/AccessRules.kt`); `tests/parity/access_contract.json` is run by PHP, Node and Kotlin.
- **What only one platform can do** is listed with its counterpart: the app's expiry lock and offline folder, the browser's service worker and install banner; study reminders are a browser Notification on the website and phone notifications in the app, made from the same function (`SBStudyPlan.reminders()`).
