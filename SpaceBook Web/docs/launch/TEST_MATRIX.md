# Test matrix

Status: **pass** / **fail** / **blocked** (cannot run here, reason given) / **untested**. "Baseline" = a clean checkout of `origin/main` a0773486 on 2026-10-26. "Release" = the branch `launch/readiness` on 2026-10-27, run on the development PC (Windows 11, Node 24, PHP 8.2, MySQL from XAMPP, Chrome installed; 8 GB with 1 to 2 GB free, so the heavy suites were run one at a time and a few needed a second try, noted in the cell). Nothing was run on a production server.

## Web: automated (Node)

| Check | Command | Baseline | Release |
|---|---|---|---|
| Syntax, data, wiring, contracts | `node tools/validate.js` | pass: 1,284 passed, 0 failed | pass: 1,288 passed, 0 failed (22 s) |
| Whole app loads, every rebuilt book and tab opens | `node --max-old-space-size=6144 tools/smoke.js` | pass: 0 failed | pass: 0 failed (20 s) |
| Generated files are fresh | `node --max-old-space-size=6144 tools/build/all.js --check` | pass: every step fresh (293 s) | pass after the full regeneration of 2026-10-27 (every derived file rebuilt from the committed book data: search, test bank, grammar, assistant, offline map; the check takes about 14 min on this PC, 11 of them the offline step) |
| Web/App matrix, endpoints, sync events, migrations | `node tools/parity/check.js` | pass: 12 passed | pass: 17 passed |
| Data parity with the App | `node --max-old-space-size=6144 tools/parity/data_parity.js` | pass: 15 passed | pass: 15 passed (7,389 questions, 98 subjects, 149 covers) |
| App bundle equals the website | `node tools/app/sync_app.js --check` | pass: 239 files | pass: 266 files, 0 missing, 0 changed, 0 leftover, service worker ec33161c1ddf (2026-10-29) |
| App carries the website's books | `node tools/app/pack_books.js --check` | untested | pass: 404 files, 422 MB |
| API tests (migrations, auth, sync, plans, feed, feedback, backup drill) | `php tests/php/run.php` (XAMPP PHP 8.2, local MySQL) | pass: 422 passed | pass: 491 passed, 0 failed |
| PHP 7.4 syntax | `node tools/php74_lint.js` | untested | pass |
| Answers audit (CLSn_BOOKS) | `node --max-old-space-size=6144 tools/audit/answers_audit.js --check` | pass | pass: no book has more unanswered questions than its baseline |
| Exercise completeness and answer coverage per chapter | `node --max-old-space-size=6144 tools/launch/exercise_coverage.js --check` | baseline written: 4,652 questions without an answer | pass: 45,480 questions in 1,532 chapters, **7 without an answer** (Class 10 Urdu: 6; Class 8 two-answer MCQ: 1; the Maths 5 to 8 gap of 171 was closed on 2026-10-27), 84 open MCQs, 9 clashes; no chapter lost a question |
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
| Reader workspace / cards / fills | `tests/reader/workspace.js`, `cards.js`, `tests/fills/browser.js` | untested | pass: 23 / 16 / 9 (the Ans window check of `workspace.js` now tries Ans buttons until one opens a window: after the M-01 fix a short answer shows in the page) |
| Ans buttons of Maths 5, 6, 7, 8, 11 (real clicks, wide screen) | `tests/launch/maths_answers_browser.js` | new: failed on the old code for Classes 5, 7, 8, 11 (every Ans named Class 6, Class 8 showed "Answer not available") | pass: 24 (every Ans button and multiple-choice widget names its class; the named question of Classes 5, 6, 7, 8 shows its own answer; a Class 11 multiple-choice question marks the option of its own key; the phone layouts keep their own handlers; no script error) |
| The phone and the app show the same book as the website (Class 11 English and Statistics, Class 5 Science and English; the bridge refuses the website's service worker) | `tests/parity/app_same_book.js` (the app's own stylesheet and bridge on the website in a phone-size Chrome) | new: failed on the old code (Exercise was a list of 70 cards with no Ans) | pass: 16 (tabs equal the website's; Lesson 12+ printed pages; no blank page; Exercise opens at the first exercise page; as many Ans buttons as the wide website; Ans opens under the question and fills the blanks; SLOs none pending; narrow browser one page at a time; the bridge refuses `sw.js`) |
| Saved questions of Class 11 all have their answer | `node tools/launch/study_pending.js --check` | new: 3,242 "answer still needs to be completed" | pass: 0 |
| Free-trial lock: codes, 30-day clock, lock screen (website) | `tests/license/unit.js` (40 checks), `tests/license/browser.js` (36 checks, Chrome) | new | pass: codes made by `tools/license/make_code.js` verify in the page; device-bound, dated and `--any` codes; day 0/25/29/30/31; a first visit; the notice of the last 7 days; the lock covers the window, the page behind it is inert, Tab stays inside, buttons 44 px, WhatsApp link carries the device ID; wrong/right/other-device/ended codes; five wrong tries block; a clock moved back stays locked; the app's WebView is left to the app; 390 px wide fits |
| Free-trial lock (app) | `TrialGateTest`, `LicenseCodeTest` (28 tests) | new | pass: codes made in node are accepted in Kotlin; the trial clock; clock moved back; wrong-try blocking; the dated preview lock and the trial together; part of the 255 unit tests; the lock screen drawn on the PC (`lock-trial.png`). **On the phone (2026-10-29):** a fresh trial shows no lock screen and Home > account says "Access: 30 more days. After that, contact the developer on WhatsApp 0343 0155606."; **the lock screen itself (day 30) was not tried on the phone** |
| Create Test, Grammar Stats, Ask SpaceBook | `tests/createtest/browser.js`, `tests/grammar/browser.js`, `tests/tutor/browser.js` | untested | pass: 22 / 19 / 15 |
| Study Plan (reminders, day cards, lesson sheet) | `tests/plan/reminders.js`, `day_cards.js`, `study_sheet_browser.js` | untested | pass: 9 / 13 / 31 |
| Mastery check | `tests/mastery/browser.js` | untested | pass: 37 |
| News Feed | `tests/feed/browser.js` | untested | pass: 36 |
| Search | `tests/search/search.js` | untested | pass: 41 |
| Accessibility (axe, tabs) | `tests/a11y/axe.js`, `tabs.js` | untested | pass: 15 views, 0 rule hits; 50 |
| Accessibility in a real Chrome (axe-core, Urdu copy) | `tests/launch/axe_browser.js` | new | pass: 19 checks, 0 rule hits on 7 views at 1280 and 375 px (the first run found serious contrast and nested-control violations, fixed: A-01) |
| Text of every typed page | `node tools/launch/text_quality.js --check` | new | pass: 124 books, 20,107 pages, 0 hard faults, 0 unexplained empty pages (23 found and fixed: T-01) |
| Typed Class 9 English against its scan OCR | `python -X utf8 tools/launch/ocr_compare.py class-9/eng/pages class-9/english/ocr 1` | new | 127 of 2,242 OCR lines not found (5.7 %), from 378 (16.9 %) before T-02 was fixed; the 5 pages with 4 or more were looked at: OCR noise, underlined words, placeholder pages |
| Rebuilt subjects open (Class 9 English, Pak Studies, Class 11 Chemistry, Ikhtiari) | `tests/launch/tab_sweep.js --subjects cls9-eng,cls9-pakstudy,cls11-chem,cls11-ikhtiari --chapters 3` | untested | pass: 81 tabs opened, 0 empty, 0 script errors |
| Offline in a real browser | `tests/launch/offline_browser.js` | untested | pass: 21 of 21 after three defects were fixed (O-01 to O-03) |
| Feedback (form, picture, queue, My reports) | `tests/feedback/browser.js` | new | pass: 40 |
| Loading speed | `tools/launch/perf_browser.js` desktop and phone profile | measured | measured, see `PERFORMANCE_REPORT.md` |

## App

| Check | Baseline | Release |
|---|---|---|
| Gradle unit tests (`:app:testDebugUnitTest`) | untested | pass: 255 tests, 0 failures, 26 test classes (2026-10-29, after the service-worker fix; the first run of the pass did not compile: two defects found and fixed, `PARITY_REPORT.md`) |
| Debug build (`:app:assembleDebug`) | untested | pass: 165 MB with the 422 MB of packed books, built from the tree of App `86df3f9` (copy in `D:\SpaceBook\Phone\SpaceBook-launch-readiness-debug.apk`; installed on the owner's phone 2026-10-29) |
| On the owner's phone (adb): launch, reader, back button, offline, notifications, report dialog and picture chooser | untested | **partly done 2026-10-29** (Realme RMX5303, APK of App `86df3f9` installed over the owner's existing app with `adb install -r`, data kept). *First install of the pass:* the phone still showed the website's old reader (Class 11 English Exercise = 70 cards, no Ans): the website's service worker bypassed the app's copy (X-04); fixed in the bridge and `SbWebView`, installed again. *By hand, after the fix:* Home, Library, Class 11 English chapter list, Unit 1 opens as 13 printed pages at the first exercise page, 7 questions with an Ans button each, Ans opens the model answer under question 1, Ans on "A ___ of locusts attacked a ___ of cattle" fills "swarm" and "herd" into the blanks, Back goes reader > chapter list > Library without closing the app, the reader menu opens and its "Report a mistake or suggest" dialog opens (closed, nothing sent), Home > account shows "Access: 30 more days", and with Wi-Fi and mobile data off the app starts ("You are offline"), the Library, chapter list and Unit 1 open (13 pages, 63 Ans buttons). *Through the debug connection:* no service worker, no caches, every `?v=` file equals its address (one old Windows-line-ending copy of `sb_games_content.js` from 2026-10-24 on the owner's phone, same code), five tabs as the website, 70 SLO questions none pending, Ans opens an answer in Class 5 Science and English, Class 8 Maths (step solution after a few seconds), Class 9 English, Class 10 Urdu and Chemistry, Class 11 Statistics, Class 12 English. **Not tried:** sending a report with a picture and the picture chooser, Me > Suggestions and problems, rotation, games, the text size, notifications, downloads, a fresh install on a phone that never had the app, other phones and Android versions |
| Emulator | blocked: no emulator or system image installed (E-03) | blocked (same) |

## Honest limits

* The tests run the app's logic in Node and flows in Chrome on Windows. They do not read the scans; a spot check of 4 pages against the scans is in `VERIFICATION_REPORT.md`.
* A passing answers audit means "every question the app holds has an answer or is named"; it does not mean the answer was checked by a teacher.
* Browsers other than Chrome, real phones, slow real networks, a production server and the live site were not tested.
