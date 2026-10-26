# Findings register

One row per finding. Severity: **Blocker** (do not launch with it), **High**, **Medium**, **Low**. Status: open / in progress / fixed (with the commit or file) / owner action / accepted (with the reason). Evidence is a command, a file or a measurement; nothing here is claimed without it.

Baseline commit: `origin/main` a0773486 (2026-10-26). Baseline results: `TEST_MATRIX.md`.

## Content: exercises and answers (the owner's requirement of 2026-10-26)

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| C-01 | Blocker | **5,427 of 45,581 exercise questions have no answer.** By book: Class 11 (Biology 374, Chemistry 626, Civics 279, Computer Science 231, English 1,048, HPE 137, Statistics 394, Urdu 212, Islamiat Lazmi 33, Islamic History 489, Islamiat Ikhtiari 272, Mutalia-e-Quran 418), Class 12 (English 554, Economics 123, Civics 25, Islamiat Ikhtiari 19, Computer Science 6, HPE 4, Urdu 3, Islamic History 3), Class 10 Urdu 6, Class 8 Maths 12, Class 5 Maths 26, Class 6 Maths 31, Class 7 Maths 102 | `tools/launch/exercise_coverage.js` -> `EXERCISE_COVERAGE.md` | open: answers are written book by book (see C-03) |
| C-02 | High | 9 subjects keep their exercises in an older data shape that the chapter report cannot count: Class 9 Physics, Urdu, Islamiat Ikhtiari (9); Class 10 English, Islamiat; Class 11 Physics (being retyped by another session); Class 12 Physics, Chemistry, Biology. Their answer coverage is unmeasured by the new report | `EXERCISE_COVERAGE.md`, "Subjects without questions held as data" | open: legacy analyser (Phase 2) |
| C-03 | High | Answers for the unanswered questions must be written, checked and kept separate from the printed text. Method: a keyed answers file per book, built into `js/answers_extra.js` style records, each marked `written` (not printed in the book), with a reason; uncertain ones flagged, never shown as verified | this register | in progress |
| C-04 | Medium | 124 MCQs have an answer that does not name any of their options, 9 questions where the solution and the printed key disagree | `EXERCISE_COVERAGE.md` columns "Open MCQs", "Clashes" | open |
| C-05 | Medium | 6 Class 10 Urdu questions (u12 Q5, u13 Q4 a/b and Q8, u14 Q4, u7 Q1) have no answer: the pages are missing from the scans | memory note `every-question-has-an-ans-2026-10-24`, audit baseline | accepted until the pages are supplied |
| C-06 | Medium | Sources missing: Class 7 Pashto (folder empty), Class 1 Urdu, Class 1 General Knowledge, Class 3 Urdu (no book supplied); Play Group, Nursery and KG have no books | `books_inventory.json`, `content/app_catalog.json` | owner action: supply the books or confirm the subjects are not in scope |
| C-07 | Medium | Pages absent from the supplied scans (numbering gaps, not yet reconciled one by one): Class 9 Maths scans 157-171, Class 9 Computer 243-254, Class 9 Physics 263-268, Class 12 Chemistry 3-10, others listed in the manifest | `books_inventory.json` `scanNumbers.gaps` | open: reconciled in `COVERAGE_MANIFEST.md` |
| C-08 | Medium | 81 Test Prep MCQs lack an answer key; Physics 12 Unit 11 Q7, Q11, Q12 unkeyed | `docs/test_prep_review/no_key.csv`, `docs/qa/` | open |
| C-09 | Info | Games' picture words (Pashto column) have not been reviewed by a native reader | `docs/GAMES.md` | owner action: human review |

## Languages, usability, games

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| U-01 | High | No Urdu, Pashto or Arabic font is bundled: reading depends on the device's fonts (no `@font-face`, no `assets/fonts`) | `grep @font-face css index.html` is empty | open: Phase 3 |
| U-02 | High | "How to play", pause by tapping the question and the in-app pause exist only on the unmerged branch `feature/game-howto` (marked "not for pushing yet") | `git log origin/main..feature/game-howto` | open: Phase 3 reviews and merges |
| U-03 | Medium | No real-browser sweep of every tab and screen has been recorded in the project documents (the handover says nothing was run in a real browser; later sessions added browser tests for parts) | `docs/HANDOVER.md` | open: Phase 3 |

## Performance

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| P-01 | High | Performance budgets were only measured in Node, never in a browser on a throttled phone profile. Known outliers: 41 of 9,698 tabs over 150 ms, a Class 11 Maths lesson tab of 10.8 MB / 269,106 elements | `docs/PERFORMANCE.md` | open: Phase 4 |
| P-02 | Medium | `lazyCards` (defers closed card bodies) is built but off by default | `docs/PERFORMANCE.md` | open: Phase 4 decides after a browser check |

## Security and operations

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| S-01 | High | The live site sends none of the planned security headers (no HSTS, nosniff, X-Frame-Options, Referrer-Policy, Permissions-Policy, CSP): `deploy/spacebook.htaccess` was never installed; the in-repo `.htaccess` only sets the directory index | 5 read-only HEAD requests on 2026-10-26 | in progress: safe headers prepared in the in-repo `.htaccess` (Phase 5); HSTS and CSP are owner decisions |
| S-02 | Medium | Content-Security-Policy can only be report-only: 416 inline `onclick` handlers and `eval` in the lazy loader | `docs/PHASE8_SECURITY.md` | accepted for launch, documented |
| S-03 | Info | No secret in the tracked files, in the git history (`api/config.php` never committed) or in the App repository; the live `config.php` and `.htaccess` answer 403 | `git log --all -- api/config.php` empty, `git grep` patterns, HEAD requests | checked |
| S-04 | High | There is no way for a student to report a mistake, a bug or a suggestion (web or app) | no `feedback` endpoint in `api/` | open: Phase 7 |
| S-05 | Info | The leaked-zip clean-up, database password rotation and FTP directory steps of `PHASE0_SERVER_STEPS.md` are owner actions whose state this review cannot see | HANDOVER | owner action |
| S-06 | Medium | Licence status of the supplied textbooks (Khyber Pakhtunkhwa Textbook Board) for redistribution inside an app is not documented anywhere | repository | owner action: written permission or confirmation |

## Process and environment

| ID | Sev | Finding | Evidence | Status |
|---|---|---|---|---|
| E-01 | Medium | Other sessions leave unfinished work in `D:\SpaceBook` (Class 9 Maths, Class 11 Physics pages and a branch `feature/game-howto`); a release must be built from a clean checkout of committed work | `git status` of the main tree | open: this work uses its own worktree `D:\SpaceBook_launch_wt` |
| E-02 | Low | The local branch `phase/p2-server` is 6 commits behind `origin/main` | `git rev-list --count` | note |
| E-03 | Medium | No Android emulator or system image is installed; native checks use the owner's phone over `adb` (owner uses it too; screenshots first, no PIN) | `Sdk/` has platform-tools only | accepted: phone tests listed as such |
| E-04 | Low | Free RAM is about 1 GB of 7.9 GB: large checks run one at a time | `Win32_OperatingSystem` | note |
| E-05 | Low | The App repository has no `.gitattributes`: a fresh worktree on Windows checks files out with CRLF, which makes `sync_app.js --check` report 20 files as changed | `git ls-files --eol` | worked around in the launch worktree; tracked for the owner |
