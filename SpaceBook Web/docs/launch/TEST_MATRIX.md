# Test matrix

Status: **pass** / **fail** / **blocked** (cannot run here, reason given) / **untested**. "Baseline" = a clean checkout of `origin/main` a0773486 on 2026-10-26. "Release" = the branch `launch/readiness` on 2026-10-27, run on the development PC (Windows 11, Node 24, PHP 8.2, MySQL from XAMPP, Chrome installed; 8 GB with 1 to 2 GB free, so the heavy suites were run one at a time and a few needed a second try, noted in the cell). Nothing was run on a production server.

## Web: automated (Node)

| Check | Command | Baseline | Release |
|---|---|---|---|
| Syntax, data, wiring, contracts | `node tools/validate.js` | pass: 1,284 passed, 0 failed | pass: 1,288 passed, 0 failed (22 s) |
| Whole app loads, every rebuilt book and tab opens | `node --max-old-space-size=6144 tools/smoke.js` | pass: 0 failed | pass: 0 failed (20 s) |
| Generated files are fresh | `node --max-old-space-size=6144 tools/build/all.js --check` | pass: every step fresh (293 s) | pass: every step fresh (13.5 min on this PC, 11 of them the offline step); re-run after the last build-tool change, see `LAUNCH_DECISION.md` |
| Web/App matrix, endpoints, sync events, migrations | `node tools/parity/check.js` | pass: 12 passed | pass: 17 passed |
| Data parity with the App | `node --max-old-space-size=6144 tools/parity/data_parity.js` | pass: 15 passed | pass: 15 passed (7,389 questions, 98 subjects, 149 covers) |
| App bundle equals the website | `node tools/app/sync_app.js --check` | pass: 239 files | pass: 264 files, service worker 03851b114c10 |
| App carries the website's books | `node tools/app/pack_books.js --check` | untested | pass: 404 files, 422 MB |
| API tests (migrations, auth, sync, plans, feed, feedback, backup drill) | `php tests/php/run.php` (XAMPP PHP 8.2, local MySQL) | pass: 422 passed | pass: 491 passed, 0 failed |
| PHP 7.4 syntax | `node tools/php74_lint.js` | untested | pass |
| Answers audit (CLSn_BOOKS) | `node --max-old-space-size=6144 tools/audit/answers_audit.js --check` | pass | pass: no book has more unanswered questions than its baseline |
| Exercise completeness and answer coverage per chapter | `node --max-old-space-size=6144 tools/launch/exercise_coverage.js --check` | baseline written: 4,652 questions without an answer | pass: 45,445 questions in 1,532 chapters, **177 without an answer** (Maths 5 to 8: 171; Class 10 Urdu: 6), 84 open MCQs, 9 clashes; no chapter lost a question |
| Coverage manifest / books inventory | `coverage_manifest.js --check`, `books_inventory.js --check` | new | pass (manifest regenerated for the new question counts) |
| Secrets | `node tools/launch/secrets_scan.js [--history]` | manual scan | pass: Web 38,277 files and 531,336 history lines, App 377 files and 97,038 history lines, 0 found (the scanner finds a planted key, a planted password and a planted key block) |
| Game content (every level recomputed) | `node tests/games/content.js` | untested | pass: 77,348 ok |
| Question bank, Create Test data | `node tests/createtest/data.js` | untested | pass: 26 |
| Grammar data | `node tests/grammar/data.js` | untested | pass: 37 |
| Mastery data / engine | `node tests/mastery/data.js`, `engine.js` | untested | pass: 10 / 37 |
| Feed cards, locator parity, entitlements, study sheet data | `tests/feed/cards.js`, `tests/parity/locator.js`, `tests/sync/entitlements.js`, `tests/plan/study_sheet_data.js` | untested | pass: 19 / 8 / 8 / 7 |
| Offline module, service worker, read aloud, mutation test | `tests/offline/offline.js`, `sw.js`, `tts.js`, `mutate.js` | untested | pass: 41 / 33 / 23 / pass (the first run of `offline.js` after my change found a message regression, fixed) |
| Sync (client, API, two devices, website vs app request shapes) | `tests/sync/unit.js`, `e2e.js`, `items.js`, `parity_e2e.js` | untested | pass: 51 / 17 / 23 / 20 (`items.js` died of memory on three runs, passed on the fourth) |
| Contrast tool | `node tests/a11y/contrast.js` | untested | pass: 14 |

## Web: real browser (Playwright with the installed Chrome)

The suites that load `index.html` (the whole app in one page) time out on this PC; they accept `SB_PAGE=lazy.html`, the page the website serves, and were run on it (`library` was changed to accept it too). Both pages are proved equal by `tools/build/lazy_parity.js`.

| Area | Command | Baseline | Release |
|---|---|---|---|
| Games (play, pause stops timers, levels) | `tests/games/browser.js`, `tests/launch/games_pause.js`, `tests/launch/arcade_speed.js` | untested | pass: 24 / 20 / 12 |
| Fonts (no tofu with device fonts removed, shaping) | `tests/launch/fonts_browser.js` | untested | pass: 15 |
| Every tab of every subject | `tests/launch/tab_sweep.js` | untested | pass: 132 subjects, 823 tabs opened, 0 empty, 0 script errors (the first run was stopped by a stalled machine after 129 subjects; the last three were swept separately, `TAB_SWEEP_LOG.txt`) |
| Library (bookmarks, notes) | `tests/library/browser.js` | untested | pass: 21 |
| Reader workspace / cards / fills | `tests/reader/workspace.js`, `cards.js`, `tests/fills/browser.js` | untested | pass: 23 / 16 / 9 |
| Create Test, Grammar Stats, Ask SpaceBook | `tests/createtest/browser.js`, `tests/grammar/browser.js`, `tests/tutor/browser.js` | untested | pass: 22 / 19 / 15 |
| Study Plan (reminders, day cards, lesson sheet) | `tests/plan/reminders.js`, `day_cards.js`, `study_sheet_browser.js` | untested | pass: 9 / 13 / 31 |
| Mastery check | `tests/mastery/browser.js` | untested | pass: 37 |
| News Feed | `tests/feed/browser.js` | untested | pass: 36 |
| Search | `tests/search/search.js` | untested | pass: 41 |
| Accessibility (axe, tabs) | `tests/a11y/axe.js`, `tabs.js` | untested | pass: 15 views, 0 rule hits; 50 |
| Offline in a real browser | `tests/launch/offline_browser.js` | untested | pass: 21 of 21 after three defects were fixed (O-01 to O-03) |
| Feedback (form, picture, queue, My reports) | `tests/feedback/browser.js` | new | pass: 40 |
| Loading speed | `tools/launch/perf_browser.js` desktop and phone profile | measured | measured, see `PERFORMANCE_REPORT.md` |

## App

| Check | Baseline | Release |
|---|---|---|
| Gradle unit tests (`:app:testDebugUnitTest`) | untested | pass: 219 tests, 0 failures (the first run did not compile: two defects found and fixed, `PARITY_REPORT.md`) |
| Debug build (`:app:assembleDebug`) | untested | pass: 53 MB without the books, 162 MB with the 422 MB of packed books (copy in `D:\SpaceBook\Phone\SpaceBook-launch-readiness-debug.apk`, not installed) |
| On the owner's phone (adb): launch, reader, back button, offline, notifications, report dialog and picture chooser | untested | **blocked: no phone was connected (`adb devices` empty)**. Owner action: connect the phone and run the list in `LAUNCH_DECISION.md` |
| Emulator | blocked: no emulator or system image installed (E-03) | blocked (same) |

## Honest limits

* The tests run the app's logic in Node and flows in Chrome on Windows. They do not read the scans; a spot check of 4 pages against the scans is in `VERIFICATION_REPORT.md`.
* A passing answers audit means "every question the app holds has an answer or is named"; it does not mean the answer was checked by a teacher.
* Browsers other than Chrome, real phones, slow real networks, a production server and the live site were not tested.
