# Launch readiness checklist (started 2026-10-26, closed 2026-10-27)

Persistent checklist for the launch-readiness work (branch `launch/readiness`, worktree `D:\SpaceBook_launch_wt`, based on `origin/main` a0773486). Every `[x]` names the evidence (a command and its result, or a file). `[ ]` means not done or not verified, with the reason. Findings are in `FINDINGS_REGISTER.md`, targets and results in `ACCEPTANCE_CRITERIA.md`, test results in `TEST_MATRIX.md`, the decision in `LAUNCH_DECISION.md`.

Status words: **done** (checked, evidence named) · **partial** (what is covered and what is not is written) · **blocked** (the smallest action that unblocks it is written) · **not started**.

## Phase 1 - Baseline and acceptance criteria: done
- [x] Inventory of the books folder: `tools/launch/books_inventory.js` -> `books_inventory.json` (133 folders, 23,475 scans); `--check` passes.
- [x] Inventory of the content: `content/app_catalog.json` (12 classes, 132 subjects, 1,836 chapters), 129 pipeline ledgers.
- [x] Baseline of the existing tests in a clean checkout of `origin/main` (`TEST_MATRIX.md`, Baseline column).
- [x] Acceptance criteria written (`ACCEPTANCE_CRITERIA.md`) and answered on the release commit (its last section).
- [x] Findings register opened and kept up to date (`FINDINGS_REGISTER.md`).
- [x] Baseline loading performance in a real browser (`docs/launch/perf/before_*.json`).

## Phase 2 - Textbook completeness and accuracy: partial
- [x] Coverage manifest Class -> Subject -> Book -> Chapter -> printed page -> content location -> status (`COVERAGE_MANIFEST.md`, `--check` passes).
- [x] **EX-1 Exercise completeness per chapter**: `tools/launch/exercise_coverage.js`: 118 books, 1,532 chapters, 45,445 questions, 0 chapters with an exercise and no questions. Partial: 14 subjects keep their exercises in an older data shape and are not counted (C-02); order and numbering as printed depend on the page pipelines and were spot-checked on 4 pages only (`VERIFICATION_REPORT.md`).
- [x] **EX-2 Answer coverage per chapter**: 45,268 of 45,445 questions have an answer; **177 do not** and are named: Maths 5 to 8 (171, drawings, graphs, figure-dependent parts) and Class 10 Urdu (6, source pages missing). Before the pass: 4,652 (`ANSWERS_WRITTEN.md`).
- [x] **EX-3 Answers kept apart from the printed text**: every written answer is a `sol` line in the page file, shown as "SpaceBook answer, not printed in the textbook"; open-ended ones start "Model answer" and say other answers are possible; 31 answers carry a "check with the teacher" note (listed in `ANSWERS_WRITTEN.md`).
- [ ] **EX-4 Independent check of answers**: partial. Calculations of Statistics, Chemistry and Economics figures were recomputed in code; 56 numeric MCQ keys that the reader misread were repaired (C-12); 84 MCQs whose answer matches no option and 9 clashes are listed (C-04). No second person (teacher) has checked the 5,170 written answers: human review list in `VERIFICATION_REPORT.md`.
- [x] Regression checks that detect a future omission: `exercise_coverage.js --check`, `coverage_manifest.js --check`, `answers_audit.js --check`.
- [ ] Text quality scan of all book data (OCR debris, mojibake, empty pages, duplicated pages): **not done** beyond the per-page notes of the pipelines (6,748 pages carry notes).
- [ ] Review of meanings, translations and explanations: **not done** (machine-assisted, no native reviewer): disclosed in `VERIFICATION_REPORT.md`.
- [x] Human expert review list: `VERIFICATION_REPORT.md` section 5.

## Phase 3 - Web usability, languages, games: done with limits
- [x] Navigation sweep of every tab of every subject in a real browser: `tests/launch/tab_sweep.js`: 132 subjects, 823 tabs, 0 empty, 0 script errors (`TAB_SWEEP_LOG.txt`).
- [x] Urdu / Pashto / Arabic fonts bundled (open licence) and used with correct shaping: `FONT_COVERAGE.md` (183 characters, 0 missing), `tests/launch/fonts_browser.js` 15 checks.
- [ ] Mixed-language text, numerals, copy and search: search 41 checks, shaping in the font test; **copy and paste was not tested**.
- [x] Keyboard, focus, labels, contrast, touch targets, zoom, reduced motion: jsdom axe on 15 views (0 rule hits), 50 keyboard/ARIA checks, contrast tool (0 failing pairs); real Chrome: `tests/launch/touch_zoom.js` 19 checks (targets 44 px on touch screens, no sideways scroll at 360 to 412 px and 200 % zoom, reduced motion, header fits). **Not done: a screen reader, Lighthouse/axe in a real browser.** Found and fixed on the way: U-01, U-02.
- [x] Games beginner friendly: how to play, gentle start, adjustable speed, pause stops every timer, restart, no loss for slow reading: `tests/games/browser.js` 24, `games_pause.js` 20, `arcade_speed.js` 12, `content.js` 77,348 recomputed answers.

## Phase 4 - Fast loading: done, budgets partly missed
- [x] Real-browser profile: cold load, repeat load, open book, open chapter, open exercise (`perf_browser.js`, before and after in `PERFORMANCE_REPORT.md`).
- [x] Measured bottlenecks fixed: desktop cold start 3.36 s -> 646 ms, repeat 1.34 s -> ~0.35 s, heap 47 -> 12 MB (`PERFORMANCE_REPORT.md`).
- [x] Budgets and test conditions written and each marked met or not met. **Not met** on the throttled phone profile: cold start 8.6 s against 4 s; the slowest book opens in 16.4 s against 12 s (Class 12 Statistics); the slowest chapter 7.1 s against 6 s. Reason and next step are in the report.

## Phase 5 - Security and child privacy: done, owner actions open
- [x] Secrets: `tools/launch/secrets_scan.js`: Web 38,277 files + 531,336 history lines, App 377 files + 97,038 history lines, 0 found.
- [x] Live site read-only header check (5 HEAD requests): no security headers (S-01); `config.php` and `.htaccess` answer 403.
- [x] PHP review (SQL, XSS, CSRF, IDOR, uploads, sessions, rate limits): `SECURITY_REPORT.md`; 491 PHP checks pass.
- [ ] Dependency audit: `npm audit` 0 vulnerabilities (dev tools only); **the App's Gradle dependencies were not audited** (no tool offline).
- [x] Privacy, retention, deletion, backups, logging review: `SECURITY_REPORT.md`, `docs/FEEDBACK.md`; reports carry no personal data; backup drill in the PHP tests.
- [x] Hardened `.htaccess` prepared and tested on Apache (`tests/launch/htaccess_check.js`); owner steps listed (S-05).
- [ ] Licence / permission of the bundled textbooks: **owner action** (S-06). Fonts: OFL, copies in `assets/fonts`.

## Phase 6 - Offline and sync: done
- [x] Real-browser offline test: install, download, go offline, reopen, interrupted download, remove: `tests/launch/offline_browser.js` 21 of 21 (three defects found and fixed: O-01 to O-03, `OFFLINE_REPORT.md`).
- [x] Download management and storage figures shown to the user: the Offline books dialog (sizes, what is on the device); checked by the test.
- [x] Queue states, retries, duplicates, conflicts: `tests/sync/*` 51 + 17 + 23 + 20 checks; feedback queue in `tests/feedback/browser.js` 40.
- [x] Interrupted download, content update (no mixed books, hash-checked): offline test steps 5 and 3, `tests/offline/offline.js` 41, `sw.js` 33. **Not tested: cache eviction by the browser, Safari/Firefox, a real phone.**

## Phase 7 - Suggestions and issue reporting: done on the web, partial on the app
- [x] API + migration + down script + PHP tests (`api/feedback.php`, migration 009): 69 checks inside the 491.
- [x] Web: button, form (kind, message, context, optional picture, review before send), offline queue, status: `tests/feedback/browser.js` 40.
- [ ] App: the same form through the shared page; the native entry points (Me row, reader menu) and the picture chooser are written, compile and pass 219 unit tests, **but were not tried on a phone** (none connected).
- [x] Receiving workflow (administration view) tested end to end in the PHP tests.

## Phase 8 - Validate the web: done
- [x] Full automated suite on the release commit (`TEST_MATRIX.md`): validate 1,288, smoke 0 failed, `all.js --check` fresh, PHP 491, parity 17, data parity 15, plus 30 browser and data suites.
- [x] Journeys, errors, refresh, back, interrupted operations, small screens: tab sweep, offline test, touch/zoom test, feedback queue; **slow network and low memory were measured with the throttled profile and on a PC with 1 to 2 GB free, not on a real low-end phone**.
- [x] Regression tests for every fixed defect: offline (O-01 to O-03), touch/zoom (U-01, U-02), numeric MCQ keys (`fix_numeric_keys.py` report mode), search/offline builds (E-07, the builds now fail loudly).

## Phase 9 - App parity: partial
- [x] `sync_app.js --check`, `pack_books.js --check` clean (264 and 404 files); the App carries the same exercises and answers (same books).
- [x] `data_parity.js` 15, `tools/parity/check.js` 17, App unit tests 219, debug builds (53 MB, 162 MB with books) (`PARITY_REPORT.md`).
- [x] Same exercises and answers in the app: the bundle is the website's (EX-5 by construction, `--check`).
- [ ] Native checks on the phone (adb): **blocked, no phone connected**. Smallest unblock: connect the phone, install `D:\SpaceBook\Phone\SpaceBook-launch-readiness-debug.apk`, run the list in `LAUNCH_DECISION.md`.

## Phase 10 - Launch decision
- [x] Production-like builds and checks for both products (above); nothing pushed or deployed.
- [x] Web / App content versions reconciled (`sync_app.js --check`, `pack_books.js --check`: same commit).
- [x] Measured loading results (`PERFORMANCE_REPORT.md`).
- [x] Offline and sync evidence (`OFFLINE_REPORT.md`).
- [x] Feedback reaches its destination (PHP end-to-end tests, administration page).
- [x] Deployment, backup, rollback, migration and recovery review (`DEPLOY_AND_MAINTAIN.md`, `docs/RELEASE_AND_ROLLBACK.md`, backup drill in the PHP tests).
- [x] Remaining limitations and human review list (`LAUNCH_DECISION.md`, `VERIFICATION_REPORT.md`).
- [x] Launch decision: see `LAUNCH_DECISION.md`.
