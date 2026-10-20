# Release and rollback

Written 2026-10-20 for the owner. A release is a push to `main`: the workflow tests, then uploads. Nothing below has been run against the live site yet (no push has happened); the steps are what the code and the workflow do, checked by reading and by the local test suites.

## 0. What identifies a release

The git commit; the service worker version (`content/sw_version.js`, a hash of the shell); the database schema number (`api/health.php?token=...` and the Administration overview show `version N of 6`). All three are visible in the admin overview (`ADMIN.md`).

## 1. Before pushing to `main`

1. **Server steps are done** (`PHASE0_SERVER_STEPS.md`): the leaked `spacebook_upload.zip` deleted from the server, `Options -Indexes` in effect, the database password rotated and stored as the `DB_PASSWORD` secret, the FTP account's home folder is `public_html/spacebook`. Without them the deploy's own checks fail on purpose.
2. **Take a database dump** (`BACKUP_RESTORE.md`, step 4). The first request after the deploy applies migrations 002-006 to the live database (new tables and columns only; nothing is dropped), but a fresh dump costs seconds.
3. **Generated files match the code.** From a clean checkout of the exact commit (not the working folder, which may hold unfinished work):

   ```
   node --max-old-space-size=8192 tools/build/all.js          # rewrites the generated files
   node --max-old-space-size=8192 tools/build/lazy_parity.js  # and again with --reverse
   node --max-old-space-size=8192 tools/build/all.js --check  # must say fresh for every step
   ```

   Commit the result (`lazy.html`, `content/*`, `js/test_prep_bank.js`, `js/study_plan_index.js`, `js/word_stats_*.js`, `js/lexicon_data.js`, `docs/test_prep_review/no_key.csv`). Any change to a script, a stylesheet reference or the script list of `index.html` makes `lazy.html` and `content/sw_version.js` stale.
4. **The tests the workflow runs pass locally** (the list is in `ARCHITECTURE.md`, section 9; `php tests/php/run.php` needs a local MySQL).
5. **Decide the owner flags** (`CONTENT_REVIEW.md`, `PHASE8_SECURITY.md`): `hideGeneratedSlo` (default off), the client sync flag `sb_sync_v2` (default off). Both are safe to leave off at first.
6. **Install `deploy/spacebook.htaccess`** if you want the security headers (`SERVER_CONFIG.md`). It ships a report-only content-security policy: it blocks nothing.

## 2. What the push does

`.github/workflows/deploy.yml`:

1. `test` job: `validate`, `smoke`, ARCH-02 matrix, lazy parity, `all.js --check`, offline layer, content integrity and lint gate, SBHooks audit and registry lock, lexicon, accessibility (tab bars, contrast, axe-core), search, sync core, then (PHP 7.4 + MySQL 5.7) `php tests/php/run.php` and the client-with-server tests. Any failure stops the release; the first run on GitHub may show failures that local runs did not (different Node, PHP and MySQL versions): fix them, do not skip them. The `php-test` job is `continue-on-error` until it has been seen green once; then add it to `deploy.needs`.
2. `deploy` job: checks the secrets, writes `api/config.php` from them, uploads `SpaceBook Web/` over FTPS with a verified certificate (excluding `docs/`, `tools/`, `tests/`, dev files), then checks the live site: `index.html` answers 200, the old zip and `config.php.bak` are not downloadable, `api/health.php` reports `"db":true`.

## 3. After the deploy (a person, in a real browser: nothing in this repository has been checked in one)

- Open the site on a phone and a desktop; open a book of each kind (Class 1 English, Class 5 Maths, Class 9 Biology, Class 12 Urdu). Check the tabs, a sentence click, the search box ("In the books"), the sign-in dialog, the Offline books dialog (download a small subject, switch the network off, reopen it), a Papers screen (Class 9 Maths: Set B differs from Set A and the key still matches).
- `https://<site>/api/health.php?token=<health_token>` shows the schema at the latest version (6) and no pending migration.
- Make yourself an administrator and open `api/admin.php` (`ADMIN.md`).
- With the browser's developer tools: the console shows the report-only policy violations (the list is the Phase 5 work list); the network tab shows no request to another website while reading.
- Run `axe` (the browser extension or Lighthouse) on the pages in `ACCESSIBILITY.md`.

## 4. Rollback

**Code.** The workflow deploys exactly the commit it runs on. To go back: create a branch at the last good commit (`git switch -c rollback <sha>`), push it, and run the `Deploy SpaceBook` workflow on that branch from the Actions tab (it has a manual trigger), or revert on `main` (`git revert <sha>`) and push. The uploader keeps a state file, so files that exist only in the bad release are removed again.

**Database.** Migrations only add; the previous code ignores the new tables and columns, so a code rollback needs **no** database rollback. Undo a migration only if the migration itself is the problem, with a fresh dump in hand: `php api/migrate.php down` (one step; 005 turns deleted accounts into blocked ones, 006 drops the role column and the sync error record). The runner refuses to go below version 1. To restore data, `BACKUP_RESTORE.md`.

**Browsers that already installed the new service worker.** The worker's version is a hash of the shell; a rollback publishes the old shell, a different hash, and every browser installs it and offers "Update available". The book-file cache is addressed by content hash and is never wiped, so nothing stale can be served from it. If the **service worker itself** is the fault, replace `sw.js` on the server by this kill switch and leave it for a few days:

```js
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(
  caches.keys().then(k => Promise.all(k.map(c => caches.delete(c)))).then(() => self.registration.unregister())));
```

(The site then works as a plain website; students lose offline reading until it is restored.)

**Sync.** The client sends nothing unless a device has `sb_sync_v2` on. If the server side misbehaves, the quickest stop is to deploy a build in which `js/core/sync.js` does not start (or set the server to answer 503 on `api/v2/sync.php`); the devices keep their outbox and resend later (events are idempotent).

**Search and offline packages.** `content/search/` and `content/offline_map.json` are regenerated with the other generated files; they roll back with the commit.

## 5. Things that need a person each time

- Reading the report-only policy violations after a release.
- The owner decisions list in `PROGRESS_LOG.md` (signing key, licensing model, translators for the lexicon queues, password-reset channel, off-site backup).
- Reviewing `docs/test_prep_review/no_key.csv` and `docs/lexicon_review/`.
