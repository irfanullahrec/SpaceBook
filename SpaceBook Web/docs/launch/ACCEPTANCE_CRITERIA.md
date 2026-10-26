# Acceptance criteria (measurable)

A criterion is met only when the command or measurement in its last column was run on the release commit and passed. "Sample" means a stated number of items checked by eye against the scans; it is never described as exhaustive.

| ID | Area | Criterion | How it is checked |
|---|---|---|---|
| AC-C1 | Content coverage | Every supplied book folder maps to a subject of the app, or is listed as an open discrepancy with its reason | `tools/launch/coverage_manifest.js --check` |
| AC-C2 | Content coverage | Every scan of a mapped book is accounted for: a page file, or a ledger status (front matter, blank, duplicate, missing in the source) | manifest, ledger rows |
| AC-C3 | Exercises | No chapter that had questions in the baseline has fewer now (omission) | `tools/launch/exercise_coverage.js --check` |
| AC-C4 | Answers | Every question and sub-question has an answer or worked solution, except those listed (with the missing source page) in `EXERCISE_COVERAGE.md` | same tool, "No answer" column; `tools/audit/answers_audit.js --check` |
| AC-C5 | Answers | Every MCQ answer names one of its options; no solution contradicts the printed key | same tool, "Open MCQs" and "Clashes" columns |
| AC-C6 | Answers | Open-ended answers are labelled as model answers; uncertain answers are flagged, not shown as verified | `VERIFICATION_REPORT.md`, UI test |
| AC-C7 | Text | The printed text is kept apart from translations, answers and added material (own fields, own labels) | data contract, `tools/validate.js` |
| AC-P1 | Performance | Opening a chapter from a cold start: <= 4 s to first lesson on a 4x CPU-throttled mobile profile with Fast 3G; <= 1.5 s repeat | `tools/launch/perf_browser.js` |
| AC-P2 | Performance | Start page transfer <= 3 MB compressed, DOM <= 100,000 elements on any first screen | same |
| AC-P3 | Performance | No lesson/exercise tab builds more than 150,000 DOM nodes before the first card is shown | same |
| AC-A1 | Accessibility | axe-core: no serious or critical violations on the 15 audited views; text contrast >= 4.5:1 | `tests/a11y/*.js` |
| AC-A2 | Accessibility | Every interactive control reachable by keyboard with visible focus; touch targets >= 44 px on phones; works at 200 % zoom; honours reduced motion | real-browser tests |
| AC-L1 | Languages | Urdu, Pashto and Arabic text uses a bundled open-licence font, no tofu boxes with the device fonts removed; right-to-left layout correct; copy keeps shaping | font test in a browser with only the bundled fonts |
| AC-G1 | Games | Every game shows how to play before play; first level is gentle; pause stops every timer; a restart control exists | `tests/games/*.js` in a browser |
| AC-O1 | Offline | After "Download for offline" of a book, that book opens, navigates, shows exercises and answers with the network off | `tests/launch/offline_browser.js` |
| AC-O2 | Offline | A queued action (progress, feedback) shows pending, becomes synchronized when online, never duplicates; failures are visible | `tests/sync/*.js`, feedback tests |
| AC-O3 | Offline | A content update never leaves a mix of old and new files of one book (hash-checked) | `tests/offline/*.js` |
| AC-S1 | Security | No secret in tracked files, history, bundle, APK assets | secrets scan (`tools/launch/secrets_scan.js`) |
| AC-S2 | Security | Server rules for injection, XSS, CSRF, IDOR, uploads, rate limits covered by PHP tests; uploads accept only checked images, stored where they cannot execute | `php tests/php/run.php` |
| AC-S3 | Security | The live site sends nosniff, frame, referrer, permissions headers after the owner installs the rules; CSP stays report-only until inline handlers are removed (documented) | live header check after deploy |
| AC-F1 | Feedback | A report (suggestion, bug, content error, wrong answer) with an optional image reaches the administration view; offline it is queued and sent later | PHP tests + browser test |
| AC-X1 | Parity | Web and app list the same classes, subjects, chapters, files, questions and answers (same hashes) | `tools/app/sync_app.js --check`, `tools/parity/data_parity.js`, `exercise_coverage.js` on the bundle |
| AC-X2 | Parity | Native app behaviours tested on a device are listed; untested ones are listed as untested | `TEST_MATRIX.md` |
| AC-R1 | Release | `validate`, `smoke`, `build/all.js --check`, PHP tests, parity, App unit tests all pass on a clean checkout of the release commit | `TEST_MATRIX.md` |
