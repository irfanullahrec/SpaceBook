# Phase 8: licensing, integrity and the web surface: what exists, what does not, and why

This is the honest version. The Phase 8 plan has five parts; two of them could be done without your decisions and are done (headers, no third parties), the others need a decision or a refactor first.

## Done

| Part | State |
|---|---|
| Security headers | `deploy/spacebook.htaccess` (template for you to install, `docs/SERVER_CONFIG.md`): `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `X-Frame-Options: DENY`, a restrictive `Permissions-Policy`, HSTS prepared but commented out (it is a one-way door: enable it once https is certain). |
| Content-Security-Policy | Shipped as **report-only** in the same template: the browser lists what an enforced policy would block and blocks nothing. `connect-src 'self'` makes any request to another website show up; `frame-src` allows only YouTube lessons; `object-src 'none'`, `frame-ancestors 'none'`. |
| No third parties | No script, stylesheet or font from another website at start-up (`tools/validate.js`), no text sent to Google/MyMemory (`tests/lexicon/privacy.js`), no Google audio (`tests/offline/tts.js`). The service worker never caches another origin or `/api/`. |
| Deploy | Phase 0: strict TLS to the named host, live check separated, no secrets in the upload zip (tests), `api/config.php` never packaged. |
| Accounts and sync | Phase 2: throttling, same-site check on cookie POSTs, device tokens stored hashed, audit log, caps on coins and events, backups. |

## Not done, and why

1. **Enforcing the CSP.** `app.js` alone contains 418 inline `onclick` handlers (the readers and `sb_*` modules add more), inline `<script>` blocks in `lazy.html` (the manifest, `attachData`), and the lazy loader uses `eval` (so do four content lookups). `script-src 'self'` would stop all of them. The way out is Phase 5's second half (delegated `data-action` handlers, no `eval`: the loader would fetch asynchronously and inject `<script>` tags). Until then the report-only policy is the tool: install it, use the site, read the console, and the violation list is the work list.
2. **Signed manifest and per-package verification.** Technically straightforward (Ed25519 signature of a release file listing the hashes of `lazy.html`, `content/*.json`, `sw.js`; the private key only in a CI secret; the downloader refuses a map whose signature does not verify). It needs one thing from you: a key pair and where the private half lives (a GitHub Actions secret). What it would and would not do is in the next section; without a key nothing can be signed, so I did not build a half-working version.
3. **Licences, device activation, encrypted packages, revocation.** These need your licensing model (free or paid, how many devices per account, how long offline, who can revoke). I will not guess a model that students would live under.
4. **Watermark with the account id** in pages and prints: depends on the licensing decision (which id, shown how loudly); trivial afterwards.
5. **Atomic releases** (`releases/<sha>` with a pointer switch): the host is reached by FTPS only; a pointer switch needs a symlink or a rename the deploy action cannot do. Rollback today = redeploy the previous commit (the workflow deploys what is checked out); a safer scheme needs shell or cPanel API access.

## What each measure does and does not do (the threat model you asked me to state)

| Threat | Measure | Does not stop |
|---|---|---|
| Someone downloads the book text from the live site | none can: the browser must receive the text to show it. Encrypting packages with a per-device key only makes bulk copying a little slower. | A student (or a bot) who is logged in can still read and copy what they can see. |
| Someone copies the repository | **make the repository private** (your step; the books' transcriptions are in it) | Anyone who already cloned it. |
| Tampered files on the server or in transit | https, signed release (when you give a key), hash check of every downloaded book file (done in `offline.js`) | An attacker who controls the server can replace the code that checks the signature. The signature protects against a partly compromised content store, not a fully compromised host. |
| Injected script (XSS) | a CSP (report-only now, enforced after the refactor), no `eval` (after the refactor), escaping | Today nothing enforces it. |
| Personal data leaking to third parties | removed (see above), `Referrer-Policy: strict-origin-when-cross-origin` | Embedded YouTube lessons contact YouTube when opened (`youtube-nocookie.com`, only on the video tab). |
| Password guessing, farming coins | Phase 2 | A password reset does not exist yet (your channel decision). |

## Decisions I need from you

1. A signing key pair (I can give you a script that makes it; the private half goes into the repository's Actions secrets as `SB_SIGNING_KEY`, the public half is committed), or "not now".
2. The licensing model, or "free for everyone, no licensing" (then parts 3-4 are dropped and the signed release is the whole of the integrity story).
3. Whether to make the repository private now.

## 2026-10-24: what the Android app now does for the copy on the phone (and what is still true)

The owner asked that nobody can simply take the books from the app, and that the website and the app are protected as far as possible. What exists now:

| Measure | Where | What it stops | What it does not stop |
|---|---|---|---|
| Downloaded books, pictures and the page are stored **encrypted** (AES-256-GCM, 64 KiB chunks, a key of their own per file; the data key is wrapped by a non-exportable Android Keystore key) | `SpaceBook App/.../data/offline/Vault.kt`, tests `VaultTest.kt` | copying the app's folder off the phone (backup tool, file manager on a rooted phone, a stolen storage chip), reading it on another phone, changing a file (any change fails to decrypt) | someone who controls the running app on an unlocked, rooted phone and asks it for the text the way the reader does |
| The device token is kept sealed with the same key | `Vault.kt` (`Seal`), `Prefs.kt` | reading the sign-in token from the app's data | the same |
| A release build checks its signing certificate (when the owner pins it with `-Pspacebook.certSha256=...`) and refuses to run with a debugger attached | `security/Integrity.kt` | a copy that was unpacked, changed and re-signed with another key | a determined reverse engineer who patches the check out |
| No screenshots, screen recordings or app-switcher thumbnails in release builds | `FLAG_SECURE` in `MainActivity` | casual capture of the books | filming the screen with another camera |
| No backup of the app's data, no debugging of the WebView in release, R8 shrinking and renaming on | manifest, `SbWebView`, `proguard-rules.pro` | `adb backup`, remote debugging, easy reading of the decompiled code | a patient decompiler |
| No database host, user or password anywhere in the app or in a commit; accounts, coins and plans are decided by the server | design | an unpacked app giving access to the database | nothing |

**What cannot be protected, said plainly.** The books are also public files of the website: the browser must receive the text to show it, so anyone can fetch them there with a browser or a script. Making the files unreadable in the browser is impossible; making them hard to take in bulk needs a server-side decision (login before the book files, a request limit per account) that changes how the site works for guests and offline use. That is the owner's decision (see "Decisions I need from you" above). The app's encrypted store protects the copy on the phone, not the public copy on the server. Both repositories are public: nothing secret may ever be committed.

**Offline writes** (website): `js/core/offline_queue.js` keeps coins and steps, study plans and test records made with no connection on the device and sends them when it is back, in order, never under another student's session (`tests/sync/offline_queue.js`). The v2 sync outbox (`js/core/sync.js`) was already offline-safe but is behind the owner's switch; the queue covers the older endpoints that are live today.
