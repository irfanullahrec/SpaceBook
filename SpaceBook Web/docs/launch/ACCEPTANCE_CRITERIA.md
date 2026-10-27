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

## Result on the release commit (2026-10-27)

| ID | Result | Evidence |
|---|---|---|
| AC-C1 | met | `coverage_manifest.js --check`: 132 subjects mapped; two folders without a source (Class 7 Pashto empty, Class 10 Islamiat = the Class 9 book) are listed |
| AC-C2 | met | every scan is accounted for: 87 books exact, 21 within a few pages, 8 PDF-only, 2 differ (named in `COVERAGE_MANIFEST.md`) |
| AC-C3 | met | `exercise_coverage.js --check`: no chapter lost a question |
| AC-C4 | **not met** | 177 of 45,445 questions have no answer (Maths 5 to 8: 171; Class 10 Urdu: 6, pages missing); all are named in `ANSWERS_WRITTEN.md`; before the pass 4,652 |
| AC-C5 | partly met | 84 MCQs whose answer matches no option (most are lists of parts written like options, the app shows them as plain questions) and 9 clashes are listed in `EXERCISE_COVERAGE.md`; 56 real numeric-key MCQs were repaired |
| AC-C6 | met by construction | written answers are `sol` lines shown as "SpaceBook answer, not printed in the textbook", open-ended ones start "Model answer"; 31 uncertain answers say "check with the teacher"; no teacher has reviewed them (human list in `VERIFICATION_REPORT.md`) |
| AC-C7 | met | `node tools/validate.js` 1,288 passed |
| AC-P1 | **not met** on the phone profile | cold start ready 8.6 s (budget 4 s); slowest chapter 7.1 s; repeat visit 861 ms (met). Desktop: cold start 646 ms. `PERFORMANCE_REPORT.md` |
| AC-P2 | met | start page transfer 1.4 to 1.8 MB; the first screens are small |
| AC-P3 | met (narrowly) | largest tab 149,103 nodes (Class 11 Maths exercises) |
| AC-A1 | met (in jsdom) | axe on 15 views: 0 rule hits; contrast: 0 failing pairs. Not run in a real browser or with a screen reader |
| AC-A2 | partly met | real Chrome (`tests/launch/touch_zoom.js`, 19 checks): 97 % of touch targets on five phone views are 44 px or more, no sideways scrolling at 360 to 412 px and at 200 % zoom, reduced motion honoured, header fits; 8 of 264 targets are smaller. Keyboard and focus: jsdom only (50 checks) |
| AC-L1 | met | `FONT_COVERAGE.md`: 183 characters, 0 without a glyph; `tests/launch/fonts_browser.js` 15 checks |
| AC-G1 | met | `tests/games/browser.js` 24, `tests/launch/games_pause.js` 20, `arcade_speed.js` 12 |
| AC-O1 | met | `tests/launch/offline_browser.js` 21 of 21 (after fixing O-01 to O-03) |
| AC-O2 | met | `tests/sync/*` 111 checks, `tests/feedback/browser.js` 40 |
| AC-O3 | met | `tests/offline/offline.js` 41, `sw.js` 33; stored files are hash-checked (offline test) |
| AC-S1 | met | `tools/launch/secrets_scan.js`: Web and App, tracked files and history, 0 found |
| AC-S2 | met | `php tests/php/run.php` 491 passed |
| AC-S3 | **owner action** | the rules are in the repository and tested on Apache; they apply only after the owner deploys; the live site was last seen without them |
| AC-F1 | met on the web, untested on a phone | PHP tests and `tests/feedback/browser.js` 40; the App entry points compile and pass unit tests but were not used on a phone |
| AC-X1 | met | `sync_app.js --check`, `pack_books.js --check`, `data_parity.js` 15, same books and answers |
| AC-X2 | met | untested items are listed (`TEST_MATRIX.md`, `PARITY_REPORT.md`): the phone |
| AC-R1 | met | validate, smoke, `all.js --check`, PHP, parity, App unit tests (219) pass on the committed branch, run in a clean worktree |

Two criteria are not met (AC-C4, AC-P1 on the throttled phone profile), two are met only in part (AC-C5, AC-A2), one waits for the owner (AC-S3). `LAUNCH_DECISION.md` says what that means for the launch.
