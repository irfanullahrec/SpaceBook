# Findings register

One row per finding. Severity: **Blocker** (do not launch with it), **High**, **Medium**, **Low**. Status: open / in progress / fixed (with where) / owner action / accepted (with the reason). Evidence is a command, a file or a measurement; nothing here is claimed without it.

Baseline commit: `origin/main` a0773486 (2026-10-26). Baseline results: `TEST_MATRIX.md`. Branch of the fixes: `launch/readiness`.

## Content: exercises and answers (the owner's requirement of 2026-10-26)

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| C-01 | Blocker | **5,427 of 45,581 exercise questions had no answer.** Class 11 (Biology 374, Chemistry 626, Civics 279, Computer Science 231, English 1,048, HPE 137, Statistics 394, Urdu 212, Islamiat Lazmi 33, Islamic History 489, Islamiat Ikhtiari 272, Mutalia-e-Quran 418), Class 12 (English 554, Economics 123, Civics 25, Islamiat Ikhtiari 19, Computer Science 6, HPE 4, Urdu 3, Islamic History 3), Class 10 Urdu 6, Class 5/6/7/8 Maths 26/31/102/12 | `tools/launch/exercise_coverage.js`, `EXERCISE_COVERAGE.md` | in progress: see `ANSWERS_WRITTEN.md` for what is done and what is left |
| C-02 | High | 9 subjects keep their exercises in an older data shape the chapter report cannot count: Class 9 Physics, Urdu, Islamiat Ikhtiari; Class 10 English, Islamiat; Class 11 Physics (being retyped by another session); Class 12 Physics, Chemistry, Biology | `EXERCISE_COVERAGE.md` | open: their answer coverage is unmeasured |
| C-03 | Medium | Method for the missing answers: a `sol` line in the book's page file (survives every rebuild, reviewed in a diff, reaches the App with the sync), marked "not printed in the textbook"; open questions say "Model answer"; doubtful ones say "needs a teacher's check" and the panel warns | `tools/launch/answers_worklist.js`, `js/sb_solve.js` | in place |
| C-04 | Medium | 124 MCQs have an answer that names no option; 9 questions where a solution and the printed key disagree | `EXERCISE_COVERAGE.md` columns | open |
| C-05 | Medium | 6 Class 10 Urdu questions have no answer because pages are missing from the scans | audit baseline | accepted until the pages are supplied |
| C-06 | Medium | No source supplied: Class 7 Pashto (empty folder), Class 1 Urdu, Class 1 General Knowledge, Class 3 Urdu; Play Group, Nursery and KG have no books | `COVERAGE_MANIFEST.md` | owner action |
| C-07 | Medium | Pages absent from the supplied scans (printed page numbers with no ledger row): Class 9 Chemistry 129, Class 9 Pak Studies 52, Class 10 Chemistry (11 pages), Class 10 Pak Studies, Class 10 Urdu (11 pages), Class 11 Physics 20, 21, 360, Class 11 Urdu 71, Class 12 Economics 298, Class 12 Islamic History 36, 37; Class 6 Maths 157, 158 are missing in every source | `COVERAGE_MANIFEST.md` | owner action: supply the pages |
| C-08 | Medium | 81 Test Prep MCQs lack an answer key; Physics 12 Unit 11 Q7, Q11, Q12 unkeyed | `docs/test_prep_review/no_key.csv` | open |
| C-09 | Info | The games' picture words (Pashto column) are unreviewed by a native reader | `docs/GAMES.md` | owner action |
| C-10 | Medium | In the committed state Class 12 Mathematics is a half-rebuilt page book (179 of 357 pages); the rest is the older topic data | `tools/validate.js` "KNOWN cls12.math not complete" | another session's work in progress |
| C-11 | Low | Representation differs from print: Class 1 English p. 63 numbers bullet sentences 18 to 22 (O-1); Urdu-medium MCQ options are labelled a b c d instead of ا ب ج د (O-2) | `VERIFICATION_REPORT.md` | accepted: the question text, order and options are the print's; labels are the app's |

## Languages, usability, games

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| U-01 | High | No Urdu / Pashto / Arabic font was bundled | no `@font-face` | **Fixed**: three OFL fonts, `css/sb_fonts.css`, `FONT_COVERAGE.md` (0 of 183 characters missing), `tests/launch/fonts_browser.js` (15 checks) |
| U-02 | High | The timed games (Math Sprint, True or False) ran a clock with no pause and took a life when time ran out; the page arcade ran at one speed | `js/sb_games.js` before | **Fixed**: Relaxed clock by default (twice as long), no-clock option, a Pause (button and P key) that really stops the clock, a hidden page pauses, a Relaxed time-out costs no life; arcade speed Easy by default; `tests/launch/games_pause.js` (20), `arcade_speed.js` (12), existing games 74,636 + 24 and arcade 45 still pass |
| U-03 | Medium | "How to play" with a voice exists only on the unmerged `feature/game-howto` ("not for pushing yet"); the arcade shows its how-to screen the first time a game is chosen | `git log origin/main..feature/game-howto` | owner decision: merge that branch after its own review |
| U-04 | Medium | The progress sync state was invisible (no "waiting / sent / could not be sent" anywhere) | `js/core/offline.js` | **Fixed**: the Offline dialog shows it, with Send now |
| U-05 | Low | Pashto labels are not written for the feedback dialog and the arcade speed buttons (Urdu and Arabic are) | `js/sb_feedback.js` | owner action: a native Pashto reader |
| U-06 | Medium | The first visit reloaded the page by itself a second or two in (the worker taking control) | tests/reader failures after delaying registration | **Fixed** (`js/core/offline.js`); checked by `tests/launch/offline_browser.js` |

## Performance

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| P-01 | High | Performance was only measured in Node | `PERFORMANCE.md` | **Measured** in Chrome: `PERFORMANCE_REPORT.md` |
| P-03 | High | A 0.9 s task (3.7 s on a 4x slower phone) froze every page after load (the lexicon table) | `tools/launch/perf_profile.js` | **Fixed** (10 ms slices) |
| P-04 | High | On wide screens each chapter and tab was drawn twice with layout twice (6 s for a Class 5 Maths chapter) | profile | **Fixed**: off-screen layout skipped, no clones, formulas typeset once; chapter 6.0 s to 1.7 s |
| P-05 | Medium | 15 class cover PNGs cost 2.2 MB on the Classes page | network breakdown | **Fixed**: WebP 0.37 MB |
| P-06 | Medium | The service worker re-downloaded 3 MB of files the page had just loaded, one after the other | `sw.js` | **Fixed** (hashed files from the browser's copy, six at a time, after the first screen) |
| P-02 | Medium | `lazyCards` (closed Maths cards cost nothing) is built but off | `docs/PERFORMANCE.md` | owner decision after a phone check; the biggest chapters (Class 11 Maths, 100,000 nodes) are still heavy on a 2 GB phone |

## Security and operations

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| S-01 | High | The live site sent no security headers | read-only HEAD requests | **Fixed in the repository** (`.htaccess`, tested on Apache), reaches the host with the next deploy; see `SECURITY_REPORT.md` |
| S-02 | Medium | The Content-Security-Policy can only be report-only (416 inline handlers) | `PHASE8_SECURITY.md` | accepted for launch |
| S-03 | Info | No secret in the files, the history or the App repository | scans | checked |
| S-04 | High | No way to report a mistake, a bug or a wrong answer | no endpoint | **Fixed**: feedback in Web and App (`docs/FEEDBACK.md`) |
| S-05 | Info | The server steps of `PHASE0_SERVER_STEPS.md` cannot be seen from here | | owner action |
| S-06 | Medium | No record of permission to redistribute the textbooks (scans carry a third-party watermark and "NOT FOR SALE"; the repository is public) | | owner action |
| S-07 | Medium | The year-long cache rule for hashed files never applied | `tests/launch/htaccess_check.js` | **Fixed** (both `.htaccess` files) |

## Process and environment

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| E-01 | Medium | Other sessions' unfinished work sits in `D:\SpaceBook` | `git status` | this work uses its own worktree `D:\SpaceBook_launch_wt` |
| E-02 | Low | `phase/p2-server` is 6 commits behind `origin/main` | | note |
| E-03 | Medium | No Android emulator or system image is installed; native checks use the owner's phone over `adb` | `Sdk/` | accepted: phone tests are listed separately and say what was not tried |
| E-04 | Low | About 1 GB of free RAM: large checks run one at a time; performance numbers are taken with nothing else running | | note |
| E-05 | Low | The App repository has no `.gitattributes`: a Windows checkout has CRLF and `sync_app.js --check` reports 20 files changed | | worked around in the launch worktree |
| E-06 | Medium | `feature/social` also uses migration number 009 | branch list | the second to merge must renumber; `tools/parity/check.js` now fails on a duplicate number |
