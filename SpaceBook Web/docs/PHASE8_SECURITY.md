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
