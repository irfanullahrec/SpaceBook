# Test matrix

Status: **pass** / **fail** / **blocked** (cannot run here, reason given) / **untested**. "Baseline" = a clean checkout of `origin/main` a0773486 on 2026-10-26, run one at a time on the development PC (Windows 11, Node 24, PHP 8.2, MySQL from XAMPP, Chrome installed). Release results are added in the "Release" column when Phase 10 runs everything again.

## Web: automated

| Check | Command | Baseline | Release |
|---|---|---|---|
| Syntax, data, wiring, contracts | `node tools/validate.js` | pass: 1,284 passed, 0 failed (29 s) | |
| Whole app loads, every rebuilt book and tab opens | `node --max-old-space-size=6144 tools/smoke.js` | pass: 0 failed (22 s) | |
| Generated files are fresh | `node --max-old-space-size=6144 tools/build/all.js --check` | pass: every step fresh (293 s) | |
| Web/App matrix | `node tools/parity/check.js` | pass: 12 passed | |
| Data parity with the App | `node --max-old-space-size=6144 tools/parity/data_parity.js` | pass: 15 passed, 0 failed (with the App checked out beside the site) | |
| App bundle equals the website | `node tools/app/sync_app.js --check` | pass after the App worktree was checked out with LF endings (see E-05): 239 generated files | |
| API tests (migrations, auth, sync, plans, feed, backup drill) | `php tests/php/run.php` | pass: 422 passed, 0 failed (local MySQL) | |
| Answers audit (CLSn_BOOKS) | `node --max-old-space-size=6144 tools/audit/answers_audit.js --check` | pass against its 2026-10-24 baseline of 91 books; **it does not know the 22 Class 11 / Class 12 books added since**, which hold 5,256 unanswered questions (C-01) | |
| Exercise completeness and answer coverage per chapter | `node --max-old-space-size=6144 tools/launch/exercise_coverage.js --check` | new; baseline written: 118 books, 1,532 chapters, 45,581 questions, 5,427 unanswered, 124 open MCQs, 9 clashes | |
| Books inventory equals the Books folder | `node tools/launch/books_inventory.js --check` | new; 133 folders, 23,475 scans | |

## Web: real browser (Playwright with the installed Chrome)

Not run in the baseline. Run in later phases and recorded here: games, library, reader workspace, tools, a11y/axe, offline, performance, feedback.

| Area | Command | Baseline | Release |
|---|---|---|---|
| Games | `node tests/games/browser.js` | untested | |
| Library (bookmarks, notes) | `node --max-old-space-size=8192 tests/library/browser.js` | untested | |
| Reader workspace / cards / fills | `npm run test:reader` | untested | |
| Create Test, Grammar, Ask | `npm run test:tools` | untested | |
| Accessibility (axe, contrast, tabs) | `node tests/a11y/*.js` | untested | |
| Offline / service worker | `node tests/offline/*.js` | untested | |
| Sync end to end | `npm run test:sync` | untested | |

## App

| Check | Baseline | Release |
|---|---|---|
| Gradle unit tests | untested | |
| Debug build | untested | |
| On the owner's phone (adb): launch, reader, back button, offline, notifications | untested | |
| Emulator | blocked: no emulator or system image installed (E-03) | |

## Honest limits of the baseline

* The existing tests run the app's logic in Node and a few flows in Chrome. They do not read the scans.
* A passing audit means "every question the app holds has an answer record or is named"; it does not mean the question list equals the printed one.
