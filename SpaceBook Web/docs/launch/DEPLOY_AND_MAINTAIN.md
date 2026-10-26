# Deploying and maintaining SpaceBook (launch edition)

For the owner. Nothing here has been done for you: **nothing was pushed or deployed** by the launch-readiness work. The work is on the branch `launch/readiness` (Web repository, worktree `D:\SpaceBook_launch_wt`) and the same branch name in the App repository.

## 1. Before you deploy

1. **Decide what goes**. `origin/main` is what is live. `launch/readiness` is `origin/main` plus the launch work. Other sessions' unfinished work (Class 9 Maths, Class 11 Physics pages, the `feature/game-howto` and `feature/social` branches) is **not** in it. `feature/social` has its own migration 009: the one that merges second must be renumbered (`tools/parity/check.js` fails when two migrations share a number).
2. **Take a database dump** (this release adds migration 009: two tables, nothing existing changes). `php api/migrate.php` is not needed: the first request after the deploy applies it. Down script: `api/migrations/009_feedback.down.sql`.
3. **From a clean checkout of the commit you push**, run the release checks (all are in `docs/launch/TEST_MATRIX.md`):

```bash
cd "SpaceBook Web"
node tools/validate.js
node --max-old-space-size=6144 tools/smoke.js
node --max-old-space-size=6144 tools/build/all.js --check
php tests/php/run.php
node tools/parity/check.js
node --max-old-space-size=6144 tools/parity/data_parity.js
node --max-old-space-size=6144 tools/launch/exercise_coverage.js --check
node tools/launch/coverage_manifest.js --check
```

   The browser tests (`tests/launch/*.js`, `tests/feedback/browser.js`, `tests/games/*`, `tests/arcade/*`) need Chrome and are not run by the deploy workflow; run them yourself.
4. **Server steps** (`docs/SECURITY_REPORT.md`, section "Owner actions"): the leaked zip, the database password, the FTP directory, the textbook licence.

## 2. Deploy

Push `launch/readiness` to `main` with plain `git push` in **both** repositories (Web to `SpaceBook`, App to `SpaceBook-App`). The workflow tests, then uploads over FTPS and writes `api/config.php` from the repository secrets. The new `.htaccess` goes up with the site. Rollback: `docs/RELEASE_AND_ROLLBACK.md`.

After the deploy, in a browser:

* `curl -I https://www.wantuch.pk/spacebook/` shows `x-content-type-options`, `referrer-policy`, `x-frame-options`, `permissions-policy`.
* Open the site, wait ten seconds, reload: the page must not reload by itself on the first visit.
* Send a test suggestion from the 💬 button; open `api/admin.php?v=feedback` as an administrator (`php api/migrate.php make-admin <number>`): it is there.
* Open the Urdu, Pashto and Quran books: the text is in Nastaliq / Naskh / Amiri.

## 3. The Android app

`SpaceBook App` carries the website's files. After the website is final: `node tools/app/sync_app.js` then `node tools/app/pack_books.js` from the clean Web checkout, `.\gradlew.bat :app:testDebugUnitTest`, build the APK, install it on the phone and do the checks in `docs/launch/TEST_MATRIX.md` (app section). Commit the App repository separately.

## 4. Ongoing maintenance

| Job | When | How |
|---|---|---|
| Read new reports | weekly | `api/admin.php?v=feedback`; set a state and a note; fix the book data, rebuild, deploy |
| Prune old reports, pictures, logs | monthly (cron) | `php api/migrate.php prune` |
| Fix a book | when a mistake is reported | edit the page file in `docs/source-verification/class-N/<book>/pages/`, rebuild the book (`tools/build_book<N>.py KEY` then `wire_book<N>.py`), `node tools/build/all.js`, then the checks of section 1; the exercise checks fail if a chapter loses a question |
| Add answers | until `docs/launch/EXERCISE_COVERAGE.md` says 0 unanswered | `node tools/launch/answers_worklist.js list <book>` writes the work list, `apply` puts the answers into the page files |
| New book | when supplied | put the scans in `Books`, run the class pipeline, `node tools/launch/books_inventory.js` and `coverage_manifest.js`, commit the regenerated `docs/launch/*` |
| Fonts | rarely | `assets/fonts/README.md` |
| After any change to `index.html`, a script or a stylesheet | every time | `node --max-old-space-size=6144 tools/build/all.js --only lazy,offline` from a clean checkout (about 5 minutes), commit the result |
| Performance | before each release | `node tools/launch/perf_browser.js --profile phone`, nothing else running |

## 5. Rules that keep the product honest

* The printed textbook text, its translations, and answers written for the project are kept apart in the data (`||` slots; `sol` lines are not printed text) and are labelled differently on screen.
* An answer that was not sure says "needs a teacher's check" and the answer panel warns the student.
* Nothing is shown as sent that was not sent: reports and progress show *waiting*, *sent* or *could not be sent*.
