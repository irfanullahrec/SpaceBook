# Offline and sync: results (Phase 6)

Run on 2026-10-27 in the installed Chrome (Playwright), real service worker, real Cache Storage, local server, network switched off with the browser's offline mode.
Command: `node --max-old-space-size=3072 tests/launch/offline_browser.js` (21 checks). Sync: `tests/sync/unit.js`, `e2e.js`, `parity_e2e.js`, `items.js`.

## What the first run found (three real defects, all fixed)

| ID | Finding | Evidence | Fix |
|---|---|---|---|
| O-01 | Offline, the Home page (the 15 class cards) showed empty boxes with the alt text: the covers were not part of the service worker's start-up shell | screenshot `offline_home.png` of the first run; 15 `covers/Classes Cards/Another-Look/*.webp` requests failed | `tools/build/make_offline.js` adds the images the Home page names to the shell (shell 180 to 196 files, +0.7 MB) |
| O-02 | Offline, the Library (bookmarks, notes) could not name the class, subject and chapter of a saved page: `content/app_catalog.json` was not cached | 4 failed requests | the catalog is in the shell (197 KB) |
| O-03 | **A subject the student had downloaded did not open offline.** `js/core/lazy.js` loads a book with a synchronous request, and a service worker cannot answer a synchronous request, so the stored copy was never used (the page said "This subject is not on the device" although it was) | `fetch()` of the stored file returned 200, the synchronous request failed with the same URL offline | `js/core/offline.js` reads the downloaded books ahead of use with `SBLazy.preload` (a fetch, which the worker answers from its cache) when the page starts without a network and when the network goes away; the message now says "Opening this subject from the device" while that runs. The download record keeps the file list so the map is not needed offline |

## Results of the 21 checks

| Step | Result |
|---|---|
| A first visit with no connection at all cannot load anything | pass (the one unavoidable download; stated here and in the app's own wording) |
| First visit online: no self-reload when the worker takes over; the worker stores the whole 196-file shell | pass |
| Offline reload: Home drawn (15 covers load), a subject that was not downloaded says so | pass |
| "Download for offline": size announced first, progress, every file checked against its sha256, marked downloaded | pass |
| Offline: the downloaded subject opens, a chapter is drawn, its Exercise tab opens, an Ans button answers, no request of the site fails | pass |
| A download cut by the network is reported as a failure (code `network`) and the subject is not offered as downloaded; the retry completes it | pass |
| The Offline books dialog shows sizes and what happens to progress; removing a subject frees its files | pass |
| No script error in the whole run | pass |

## Sync

| Suite | Result |
|---|---|
| `tests/sync/unit.js` | 51 passed, 0 failed |
| `tests/sync/e2e.js` (client, API, MySQL) | 17 passed, 0 failed |
| `tests/sync/parity_e2e.js` (website client and app request shapes against one server) | 20 passed, 0 failed |
| `tests/sync/items.js` (two devices, one account: bookmarks, notes, offline outbox, late edits, guest, sign-in) | the first 16 to 19 checks pass; **the process then dies** (V8 out of memory with a 1.5 GB heap, or killed by the OS with a larger one): each scenario builds a fresh copy of the whole app and this PC has 1 to 2 GB free. Not a product failure, but the suite is not complete here. Re-run on a PC with 4 GB free before the release |

## Honest limits

* Chrome on Windows only. Not tried: Safari/iOS, Firefox, Chrome on the owner's phone as a web page (the Android app does not use the service worker: its books are inside the APK).
* The read-ahead keeps at most 150 MB of book text in memory (the smallest subjects first); a student with more than that on the device gets the rest on the next start.
* In the first seconds after the page starts without a network a downloaded subject can still say "Opening this subject from the device": tap it again.
* Storage quota exhaustion is handled in code (`quota` error) but was not provoked.
