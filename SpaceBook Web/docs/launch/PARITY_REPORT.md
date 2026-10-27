# Web and App parity (Phase 9)

Date 2026-10-27. Web `6e75cdf9`, App `74a1a40` (branch `launch/readiness` in both). The first state of this branch (Web `a749fb4e`, App `dfe6a0b`) was pushed on the owner's order; the commits after it are not pushed.

## Same data, same functions

| Check | Command | Result |
|---|---|---|
| The App bundles exactly what the website is | `node tools/app/sync_app.js --check` | pass: 264 generated files, 0 missing, 0 changed, 0 leftover, service worker 4d83afeb5d66 (re-run after the text and accessibility changes; 26 files rewritten) |
| The App's books are the website's books | `node tools/app/pack_books.js --check` | pass: 404 files (422 MB), 0 missing, 0 changed |
| Data parity (catalog, question bank, covers, tests) | `node --max-old-space-size=6144 tools/parity/data_parity.js` | pass: 15 of 15 (7,389 questions in 98 subjects equal; 149 covers) |
| Feature matrix, endpoints, sync events, item kinds, migrations | `node tools/parity/check.js` | pass: 17 of 17 |
| Answers: the App shows the answers written for Classes 11 and 12 | the bundle is regenerated from the committed books (`sync_app.js`, 55 stale files rewritten) | the same `sol` lines reach the App; exercise coverage is one number for both platforms (`EXERCISE_COVERAGE.md`) |

## Native build and tests

| Check | Command | Result |
|---|---|---|
| Unit tests | `.\gradlew.bat :app:testDebugUnitTest` | pass: 219 tests, 0 failures, 0 errors, re-run on the final bundle (24 classes: titles, feed, reward keys, network layer, screen renderings) |
| Debug build | `.\gradlew.bat :app:assembleDebug` | pass (the debug APK with the 422 MB of packed books is 164 MB; copy for the owner: `D:\SpaceBook\Phone\SpaceBook-launch-readiness-debug.apk`, not installed) |

Two defects were found by this pass and fixed in the App repository (commit `15cdc34`):

1. The new "Suggestions and problems" row in Me did nothing: `MeScreen` received `onFeedback` but did not hand it to `MeContent`.
2. `SbWebView.kt` did not compile: a comment quoted `accept="image/*"` and Kotlin reads `/*` inside a comment as a nested comment, so the whole file was swallowed (14 errors in three files).

## What is NOT verified

* **On a phone.** No phone was connected (`adb devices` was empty) and no emulator is installed (E-03). Not tried: install, start, reader, back button, offline start with the books inside the APK, notifications, the Me row and the reader menu item for reports, the WebView picture chooser. `parity.json` therefore keeps `feedback.report` as `partial` with that stated.
* Instrumented (on-device) tests: the App has none; the picture chooser cannot be exercised in a JVM test.
* Gradle dependencies of the App were read, not scanned for vulnerabilities (no advisory database offline): `SECURITY_REPORT.md`, last section.

## Secrets

Scan of the App repository changes of this pass (Kotlin, scripts, bundle): no password, key, token, private key or connection string; no database host, user or password is in the App.

## Open parity rows

See `docs/PARITY_MATRIX.md`; the only row changed in this pass is `feedback.report` (still partial, reason above).

## Commits

* App: `15cdc34` (entry points, chooser), `21c13d2`, `dfe6a0b` (earlier bundles), `74a1a40` (bundle regenerated from Web `6e75cdf9`).
* Web: see `git log launch/readiness` (answers, build tools, offline layer, documents).
