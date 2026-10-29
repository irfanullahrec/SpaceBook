# Launch decision

Date 2026-10-29. Branches `launch/readiness` in both repositories: Web `6fa13a4a` (code, tests and regenerated files; later Web commits are documents only), App `3d99f20`. **On the owner's order the branch was pushed on 2026-10-27** (Web `a749fb4e` to `SpaceBook`, App `dfe6a0b` to `SpaceBook-App`). The Web push starts the deploy workflow (tests, upload, migration 009 on the live database); I did not see its result (no `gh` here): read the Actions tab and run the after-deploy checks of `DEPLOY_AND_MAINTAIN.md`. Nothing was published to a store or charged. Work done after that push (the text-quality scan, Class 9 English typed back from the scans, real-browser accessibility, see `TEXT_QUALITY.md`, `AXE_BROWSER.json`, findings T-01 to T-03 and A-01) is committed on the branch and **not pushed**; so are the 1-month trial lock (L-01), the work that makes the phone and the app show the same printed book with the same Ans buttons as the website (X-01, X-02, X-04) and the phone check of 2026-10-29. Nothing was pushed or deployed during that work.

## Decision: READY WITH LIMITATIONS (for your approval; three conditions before it is announced)

* The **website** passes every automated check run on it (1,290 validator checks, 0 smoke failures, all generated files fresh, 491 API checks, 30 browser and data suites, 823 tabs opened with none empty, offline in a real Chrome 21 of 21, accessibility floor, secrets scan clean). It is **safe to put on the live host** once the owner steps below are done.
* The **app** compiles, passes its 255 unit tests, carries exactly the website's books and answers (422 MB inside the APK; `sync_app.js --check`: 266 generated files, 0 stale), and builds (`D:\SpaceBook\Phone\SpaceBook-launch-readiness-debug.apk`, 165 MB, debug-signed, built from App `3d99f20`, installed on the phone and checked again after the last regeneration). **It was checked on the owner's phone (Realme RMX5303) on 2026-10-29**, after the owner found that Class 11 English showed no answers on the phone and in the app. That check found a defect that no browser test could show (X-04: the website's service worker took the app over, so the phone kept showing the website's old reader); it was fixed and the same screens were checked again. *By hand on the phone:* Home, Library, Class 11 English, Unit 1 opening as printed pages, Ans under a question and inside the blanks of a sentence, the reader menu and the report dialog (opened, nothing sent), the Back button, a start with Wi-Fi and mobile data switched off. *Through the phone's debug connection (the page's own functions, not finger taps):* the five tabs, the Board SLO questions, and Ans in Class 5 Science and English, Class 8 Maths, Class 9 English, Class 10 Urdu and Chemistry, Class 11 Statistics and Class 12 English. **Not done on the phone:** sending a report with a picture, rotating, games, the text size setting, notifications, downloads, a fresh install on a phone that never had the app (the APK was installed over the owner's existing app, its data kept), any other phone or Android version.
* **Answers:** 45,473 of 45,480 exercise questions now have an answer (4,652 had none at the start). 7 do not (Class 10 Urdu, source pages missing: 6; one Class 8 MCQ with two right options: 1). 5,341 answers were written for the project (5,170 in Classes 11 and 12, 171 in Maths 5 to 8, `MATHS_LAST_ANSWERS.md`); **no teacher has read them**, and 16 of the Maths answers say that they were read from a small printed drawing and should be checked.

It is not "ready" without limits because of the three conditions and the limitations below; it is not "blocked" because no defect found in this pass is left open that stops the product working.

## Before launch (needs you, I cannot do these)

| # | Condition | Why | How |
|---|---|---|---|
| 1 | **Permission to redistribute the textbooks** (S-06) | the scans carry a third-party watermark and "NOT FOR SALE"; the repository is public | written permission from the Khyber Pakhtunkhwa Textbook Board or whoever holds the rights; otherwise make the repository private and serve only text |
| 2 | **Server steps** (S-05, `docs/PHASE0_SERVER_STEPS.md`, `SECURITY_REPORT.md`) | a zip containing the old database password was reachable on the host; the FTP account, the headers (S-01) and the cache rules (S-07) are not on the live host | delete the zip, rotate the database password, point the FTP account at the site folder, then deploy (the new `.htaccess` carries the headers) |
| 3 | **The rest of the phone check of the app** | on 2026-10-29 the main screens were checked on one phone (see below); sending a report with a picture, rotation, games, the text size, downloads and a second phone were not | run the items marked "not done" below on the phone and, if you can, on a second one |
| 4 | **A teacher reads the written answers** (not a code blocker, a trust one) | the answers are mine, checked by script and by reading, not by a subject expert | start with Islamic History, Islamiat, Mutalia-e-Quran, Civics, Economics (`VERIFICATION_REPORT.md` section 5); until then the app says "SpaceBook answer, not printed in the textbook" and 31 answers say "check with the teacher" |

Also decide: migration number 009 is used twice if `feature/social` merges after this branch (E-06; `tools/parity/check.js` fails on a duplicate). The second branch to merge renumbers.

## Phone check (about 30 minutes)

Connect the phone, `adb install -r "D:\SpaceBook\Phone\SpaceBook-launch-readiness-debug.apk"`, then look at the screen before every tap:

1. Start the app with the network on: Home, a class, a subject, a chapter, its Exercise tab, tap **Ans** on three questions (one MCQ, one written, one Class 11 or 12 answer from this pass: it must say "SpaceBook answer, not printed in the textbook"). **Done 2026-10-29** (Class 11 English Unit 1: the model answer opens under the question and says "SpaceBook model answer, not printed in the textbook"; a fill-in sentence gets its words in the blanks).
2. Switch on aeroplane mode, close and reopen the app: the same chapter opens with no internet (the books are inside the APK). **Done 2026-10-29** (Wi-Fi and mobile data switched off with `adb shell svc`, force-stop, start: Home says "You are offline", the Library, the chapter list and Unit 1 open, 13 pages, 63 Ans buttons).
3. **Me > Suggestions and problems**: the dialog opens; attach a picture (the picker must open and return); send; it shows "waiting" offline and "received" online. Then the reader's menu (three dots) > **Report a mistake or suggest**. **Partly done:** the reader's menu and its report dialog were opened and closed (nothing sent); Me > Suggestions and problems, the picture and sending are **not done**.
4. Back button from a chapter, from the dialog, from Me: it goes one step back and does not close the app. **Partly done:** from a chapter to its chapter list (it stayed in the app); the dialog and Me **not done**.
5. Rotate the phone in a chapter; open a game; the text size setting. **Not done.**
6. Report anything wrong with the screen it happened on; do not enter a PIN or a password anywhere for the test.

## What this pass changed (summary)

* **Answers:** 4,406 added in Class 11 books, 708 in Class 12 books, 56 numeric MCQ keys repaired (`ANSWERS_WRITTEN.md`).
* **Defects found by running the real thing and fixed:** downloaded subjects did not open offline in the website (O-03); the Home covers and the catalog were missing offline (O-01, O-02); on a phone the account button, coins and offline button were off the right edge of the header (U-01) and half the touch targets were under 44 px (U-02); numeric MCQ answers were read as option indexes (C-12); the search index and offline map builds died silently on a PC with little RAM (E-07); the App's report entry in Me did nothing and one App file did not compile (`PARITY_REPORT.md`).
* **Found by the owner on 2026-10-28 and fixed ("Class 11 English has no answers, the app does not look like the website"):** the phone and the app drew every reviewed book with an older reader than the website (X-01: now the same printed pages, one at a time, with the same Ans buttons and tabs); 3,242 saved Class 11 questions printed "The answer to this saved question still needs to be completed" (X-02: now 0); the owner had tested an old folder (X-03); and, on the real phone, the website's service worker bypassed the app's own copy of the site (X-04: found only by looking inside the phone's WebView) the last App commit had left two bundle files out (X-05), and running every step of the deploy gate on the final state found two more things that would have stopped the deploy (X-07).
* **New checks that stay:** `tests/launch/offline_browser.js`, `touch_zoom.js`, `tab_sweep.js`, `fonts_browser.js`, `games_pause.js`, `arcade_speed.js`, `tools/launch/exercise_coverage.js --check`, `secrets_scan.js`, `answers_written_report.js`.
* Feedback ("Suggestions and problems") on the web and in the app, fonts for Urdu/Pashto/Arabic, game pause and speed controls, faster loading, security headers in `.htaccess` were built earlier in the pass (`FINDINGS_REGISTER.md`).

## Known limitations (not blockers)

| ID | Limitation |
|---|---|
| L-01 | **1-month free-trial lock (added 2026-10-28 on the owner's request, `docs/TRIAL_LOCK.md`)**: 30 days after a person's first start (website and app) only a lock screen is left, asking them to contact the developer on WhatsApp 0343 0155606 or to type an unlock code: your **default code** (opens 30 days from typing, only its hash is in the repositories, it can be guessed offline from the public hash, so keep it long and private) or a signed code for one device made with `node tools/license/make_code.js <device ID>`. It runs on the person's own device, so clearing site data or reinstalling gives a new month and an edited page can remove it; a lock that cannot be bypassed needs the server. Once this version is live, **every current visitor's 30 days start at their next visit**; the private key (`~/SpaceBook-License/private_key.pem`, backup `D:\SpaceBook-License`) must be kept and backed up or no code can be made |
| C-11, C-05 | 7 questions without an answer: Class 10 Urdu 6 (the source pages are missing) and a Class 8 MCQ with two right options |
| M-01 | fixed 2026-10-28: on a computer the Ans buttons of Class 5, 7, 8 and 11 Maths read Class 6's answers (the open-book view used the Class 6 reader for every class); `tests/launch/maths_answers_browser.js` now presses an Ans in each Maths class |
| C-04 | 84 MCQs whose answer matches no option, 9 clashes between a solution and a printed key (listed) |
| X-06 | Class 9 Physics: the textbook's own exercise multiple-choice questions (8 of 9 chapters) show their options with no answer, in the app and on the website; the book prints no key. The keyed MCQs are in the Board SLO tab |
| C-02, C-10 | 14 subjects keep exercises in an older data shape the chapter report cannot count; Class 12 Maths is a half-rebuilt page book (179 of 357 pages) |
| C-06, C-07 | no source for Class 7 Pashto, Class 1 Urdu and General Knowledge, Class 3 Urdu, Play Group, Nursery, KG; pages missing from the supplied scans |
| P-07 | on the throttled phone profile (4x CPU, Fast 3G) cold start is 8.6 s (budget 4 s), the slowest book opens in 16.4 s (12 s), the slowest chapter in 7.1 s (6 s); on desktop all but the chapter budget are met (`PERFORMANCE_REPORT.md`) |
| S-02 | the Content-Security-Policy can only be report-only (416 inline handlers) |
| A11y | axe-core ran in a real Chrome (desktop and phone width, 7 views; `AXE_BROWSER.json`) and every finding was fixed (0 rule hits; Urdu copy and paste checked); no screen-reader test, no Lighthouse run; 8 of 302 touch targets are under 44 px |
| Offline | only Chrome on Windows was tried; the read-ahead keeps at most 150 MB of books in memory |
| Text | `TEXT_QUALITY.md`: 124 books, 20,107 pages, 0 broken-encoding pages, 0 unexplained empty pages (23 were found and fixed); 2,544 soft findings are a list for a reader. Class 9 English was compared with its OCR and typed back from the scans where lines were missing (T-02); the other books have no OCR to compare with, so a line dropped there would not be found by a script. No native review of the Urdu, Pashto and Arabic wording of the new dialogs and games, translations machine-assisted |
| Tests | `tests/sync/items.js`, `plan/reminders.js` and the `index.html` suites need 2 to 3 GB free; they passed on retry (`TEST_MATRIX.md`) |

## Deploy and rollback

`DEPLOY_AND_MAINTAIN.md` (steps, after-deploy checks, maintenance), `docs/RELEASE_AND_ROLLBACK.md` (pre-flight, rollback), the database dump before the deploy (this release adds migration 009: two tables, down script `api/migrations/009_feedback.down.sql`). "Push" means plain `git push` in **both** repositories (Web to `SpaceBook`, App to `SpaceBook-App`): the deploy workflow then tests, uploads and migrates the live database, so push only when you are ready for that.

## What was not tested

More than one real phone (one Realme RMX5303 was used) and any Android version other than that phone's; Safari, Firefox, Edge; the live host (LiteSpeed, brotli, the real network); a production database; a screen reader; load with many students at once.
