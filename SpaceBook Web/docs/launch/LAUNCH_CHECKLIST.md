# Launch readiness checklist (started 2026-10-26)

Persistent checklist for the launch-readiness work (branch `launch/readiness`, worktree `D:\SpaceBook_launch_wt`, based on `origin/main` a0773486). Update the status as work lands; every `[x]` names the evidence (a command and its result, or a file). `[ ]` means not done or not verified. Findings are in `FINDINGS_REGISTER.md`, targets in `ACCEPTANCE_CRITERIA.md`, test results in `TEST_MATRIX.md`.

Status words: **done** (checked, evidence named) · **partial** (what is covered and what is not is written) · **blocked** (the smallest action that unblocks it is written) · **not started**.

## Phase 1 - Baseline and acceptance criteria
- [x] Inventory of the books folder: `tools/launch/books_inventory.js` -> `books_inventory.json` (133 folders, 23,475 scans).
- [x] Inventory of the content: `content/app_catalog.json` (12 classes, 132 subjects, 1,876 chapters), 129 pipeline ledgers (20,097 page rows).
- [x] Baseline of the existing tests in a clean checkout of `origin/main` (see `TEST_MATRIX.md`).
- [x] Acceptance criteria written (`ACCEPTANCE_CRITERIA.md`).
- [x] Findings register opened (`FINDINGS_REGISTER.md`).
- [ ] Baseline loading performance in a real browser (Phase 4 does this).

## Phase 2 - Textbook completeness and accuracy
- [ ] Coverage manifest Class -> Subject -> Book -> Chapter -> printed page / PDF page -> content location -> status (`COVERAGE_MANIFEST.md`).
- [ ] **EX-1 Exercise completeness per chapter**: every chapter that has an exercise in its book has its questions in the app, in printed order, with numbering and sub-parts; `tools/launch/exercise_coverage.js` per-chapter report, plus a manual sample against the scans (disclosed in `VERIFICATION_REPORT.md`).
- [ ] **EX-2 Answer coverage per chapter**: every question and sub-question has an answer or worked solution (or is named as open with its reason).
- [ ] **EX-3 Answers kept apart from the printed text**, open-ended questions carry a model answer and say other valid answers exist; uncertain answers are flagged, never presented as verified.
- [ ] **EX-4 Independent check of answers** (calculations recomputed, MCQ keys match an option, printed key vs solution clashes).
- [ ] Regression checks that detect a future omission (`exercise_coverage.js --check`, manifest `--check`).
- [ ] Text quality scan of all book data (OCR debris, mojibake, empty pages, duplicated pages).
- [ ] Review of meanings, translations and explanations (sampled; disclosed).
- [ ] Human expert review list (what only a person can sign off).

## Phase 3 - Web usability, languages, games
- [ ] Navigation sweep of every tab and screen in a real browser.
- [ ] Urdu / Pashto / Arabic fonts bundled (open licence) and used with correct shaping and line height.
- [ ] Mixed-language text, numerals, copy and search checked.
- [ ] Keyboard, focus, labels, contrast, touch targets, zoom, reduced motion.
- [ ] Games beginner friendly: how to play, gentle start, adjustable speed, pause that stops timers, restart, no punishment for slow readers, no manipulative reward patterns.

## Phase 4 - Fast loading
- [ ] Real-browser profile: cold load, repeat load, open book, open chapter, open exercise, offline reopen (before numbers in `PERFORMANCE_REPORT.md`).
- [ ] Fix the measured bottlenecks; after numbers.
- [ ] Performance budgets and test conditions written.

## Phase 5 - Security
- [x] Secrets scan of the tracked files, the history and the App repo (nothing found; values never printed).
- [x] Live site read-only header check (5 HEAD requests): no security headers; `config.php` and `.htaccess` are 403.
- [ ] PHP review (SQL, XSS, CSRF, IDOR, uploads, sessions, rate limits).
- [ ] Dependency audit (`npm audit`, Gradle).
- [ ] Privacy, retention, deletion, backups, logging review.
- [ ] Hardened `.htaccess` prepared for deploy; owner steps listed.
- [ ] Licence / permission status of the bundled textbooks and fonts.

## Phase 6 - Offline and sync
- [ ] Real-browser offline test: install, download a book, go offline, reopen; fresh install without network.
- [ ] Download management and storage figures shown to the user.
- [ ] Queue states (pending / synced / failed) visible; retries, duplicates, conflicts.
- [ ] Interrupted download, cache eviction, content update (no mixed books).

## Phase 7 - Suggestions and issue reporting
- [ ] API + migration + down script + PHP tests (`api/feedback.php`).
- [ ] Web: button, form (kind, message, context, optional image, review before send), offline queue, status.
- [ ] App: same form through the shared page, native entry point.
- [ ] Receiving workflow (administration view) tested end to end.

## Phase 8 - Validate the web
- [ ] Full automated suite in a clean checkout (`TEST_MATRIX.md`).
- [ ] Journeys, errors, refresh, back, interrupted operations, small screens, slow network, low memory.
- [ ] Regression tests for every fixed defect.

## Phase 9 - App parity
- [ ] `sync_app.js` / `pack_books.js` from the verified web commit; `--check` clean.
- [ ] `data_parity.js`, `tools/parity/check.js`, App unit tests.
- [ ] Same exercises and answers in the app (EX-5: `exercise_coverage.js` numbers equal for the bundle).
- [ ] Native checks on the phone (adb), listed with what was not tested.

## Phase 10 - Launch decision
- [ ] Production builds and checks for both products.
- [ ] Web / App content versions reconciled.
- [ ] Measured loading results.
- [ ] Offline and sync evidence.
- [ ] Feedback reaches its destination (end-to-end test).
- [ ] Deployment, backup, rollback, migration and recovery review.
- [ ] Remaining limitations and human review list.
- [ ] Launch decision: ready / ready with limitations / blocked.
