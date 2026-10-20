# Administration (Phase 9): what exists, how to switch it on, what it does not do

Written 2026-10-20. Code: `api/admin.php` (the pages), `api/lib/admin.php` (the logic), `api/admin.css`, migration `api/migrations/006_admin.sql`. Tests: `tests/php/admin_tests.php` (run by `php tests/php/run.php`, 50 checks).

## Switch it on (owner, on the server, once)

1. Deploy as usual. The first request after the deploy applies migration 006 (adds `users.role` and the table `sync_errors`). Take a dump first (`docs/BACKUP_RESTORE.md`).
2. Make yourself an administrator from the command line on the server (nothing over HTTP can do this):

   ```
   php api/migrate.php make-admin 03001234567
   ```

   The number is the one you registered with. `remove-admin <number>` takes the role away; both are written to the audit log (`admin_grant`, `admin_revoke`).
3. Sign in to the app as usual, then open `https://<your site>/api/admin.php`.

Anyone else (signed out, a student, a blocked or deleted administrator) gets the same plain "Not found" a missing file gives; the role and the status are read from the database on every request, so removing the role or blocking the account ends access at once.

## The pages

| Page | What it shows |
|---|---|
| Overview | accounts (blocked, deleted, administrators), joined in 7 days, signed in in 24 hours, by type; devices seen in 7 days; events applied in 24 hours; rejected events; **what is deployed**: service worker version, when the content was built, book files, offline packages, search index, database schema version and anything pending |
| People | search by part of a name or the start of a number (`0300…`, `92300…`, `+92 300…`); filter by status; numbers are masked (`92300*****67`) |
| One person | the whole number (opening the page is written to the audit log as `admin_view` with the administrator's id), type, status, joined, last sign-in, coins, devices, latest sync problems, latest audit rows, and the **block / unblock** form |
| Sync | events the server rejected, by code (24 hours, 7 days) and the latest 100, with the person and the device; devices signed in and how many are idle for 30 days |
| Audit log | the latest 200 rows, filter by action and by person |

## What an administrator can change

Only one thing: **block or unblock** an account (with a reason of up to 100 characters, kept in the audit log). Blocking signs out every device at once (sync stops), and the session cookie stops at the next request because the status is checked each time. Unblocking restores access. An administrator cannot block themselves or another administrator (that is done on the command line by the owner), cannot touch deleted accounts, and cannot grant or remove the role.

Protections: a token in every form (a form from another site is refused even with the right token), the same-site check the account API uses, at most 600 requests per hour per administrator, no JavaScript and no inline styles, and headers that forbid framing, caching, indexing and any outside resource.

## Sync errors

`api/v2/sync.php` now records each rejected event (code and event id only; never the payload) in `sync_errors`, at most 20 per request and 200 per person per hour so that a broken client cannot fill the table. `php api/migrate.php prune` removes rows older than 90 days.

## Not done, and why

- **No password re-entry, no second factor.** The administrator signs in with the same password as any account. If that matters to you, add a second step (a separate admin password or a one-time code); it needs your decision on the channel (see the password-reset item in the owner decisions).
- **No content editing, no user editing, no deletion** from the pages: they would need review rules (who may change what, and a way to undo) that are yours to decide.
- **Not tried in a real browser** (the layout is plain HTML and CSS; the tests read the HTML). **Not tried on PHP 7.4 / MySQL 5.7**: the code avoids PHP 8 syntax (`tools/php74_lint.js`) and uses plain SQL, but the CI job for that has not run on GitHub yet.
- **Statistics per subject and class** (the Phase 9 "Statistics" item) are not here: they need the events kept long enough to count, which the server deliberately does not do (it keeps ids, not payloads).
