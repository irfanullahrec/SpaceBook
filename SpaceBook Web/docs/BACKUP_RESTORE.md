# Backups and restore (SpaceBook database)

What is backed up: the MySQL database `tafseelk_spacebook` (accounts, coins, study plans, Tests Preps records, sync ledger). The website files are in git and need no backup; `api/config.php` holds the only secret and is recreated by hand (`api/config.sample.php`).

## What exists

| Tool | What it does |
|---|---|
| `tools/backup/dump.php` | Writes `spacebook-YYYYmmdd-HHMMSS.sql.gz` (all tables, one consistent snapshot, pure PHP so it works where `mysqldump` is hidden) and keeps the newest N. Refuses to write inside `public_html`. |
| `tools/backup/restore.php` | Loads a dump into a database named in a config file. Refuses a database that already has tables unless `--force`. Reports a truncated dump. |

`tools/` is not uploaded by the deploy (`deploy.yml` excludes it). Put these two files **once**, by hand, in a folder outside `public_html` on the server (for example `/home/tafseelk/tools/backup/`).

## Set up the nightly backup (owner, cPanel)

1. File Manager: create `/home/tafseelk/spacebook_backups/` (outside `public_html`), and upload `dump.php` and `restore.php` to `/home/tafseelk/tools/backup/`.
2. Create `/home/tafseelk/tools/backup/config.php` with the same four database values as `public_html/spacebook/api/config.php` (copy that file; same format). Mode 600.
3. cPanel, Cron Jobs, daily at 02:30:
   `/usr/local/bin/php /home/tafseelk/tools/backup/dump.php --out /home/tafseelk/spacebook_backups --keep 14 --config /home/tafseelk/tools/backup/config.php`
   (use the PHP path that cPanel shows for your account; any PHP 7.4 or newer works).
4. Run it once by hand from cPanel Terminal or the cron screen and check that a `.sql.gz` appears and its size is more than a few KB.
5. **Off-site copy (decision for the owner):** a dump on the same server does not survive losing the server. Choose one: download the newest file weekly to your own computer; or a second hosting account / cloud drive and a cron `scp`/`rclone`; or cPanel "Backup" downloads. Until one is chosen, backups protect against mistakes (a bad migration, an accidental delete) but not against losing the hosting account.

## Before any risky step

Before merging to `main` while it contains a new migration, or before running `php api/migrate.php down`, take a dump by hand (step 4) and keep the file. Migrations 002–005 only add tables and columns, but a fresh dump costs seconds.

## Restore drill (do it once now, then every few months)

A backup you have never restored is a guess. The drill restores into a **new, empty** database and compares it with the live one; it never touches the live data.

1. cPanel, MySQL Databases: create a database `tafseelk_spacebook_restore` and give the same MySQL user all privileges on it.
2. Make `restore-config.php` (same keys as `config.php`, with `db_name` = `tafseelk_spacebook_restore`).
3. `php /home/tafseelk/tools/backup/restore.php --file /home/tafseelk/spacebook_backups/spacebook-YYYYmmdd-HHMMSS.sql.gz --config /home/tafseelk/tools/backup/restore-config.php`
   It prints `restored N statements into tafseelk_spacebook_restore`.
4. phpMyAdmin: compare row counts of `users`, `activity_progress`, `study_plans`, `tp_answers`, `sync_events` between the two databases (they match if no one used the app since the dump). Run `CHECKSUM TABLE users;` in both for an exact check.
5. Delete the restore database.

The same drill is run automatically against a scratch database by `php tests/php/run.php` (section "backup / restore drill": every table's row count and checksum match, quotes/newlines/emoji/Urdu survive, a non-empty target is refused, a cut-off file is reported, rotation keeps the newest N). That proves the tools; the drill above proves your server, PHP version and file permissions.

## Real recovery (the live data is damaged or lost)

1. Put the site in a safe state: rename `public_html/spacebook/api/config.php` temporarily so the app cannot write while you work (it then answers "Database connection failed").
2. Take a dump of whatever remains (step 4 above) and keep it; it may still hold rows the older backup lacks.
3. Restore the chosen backup into a **new** database (`restore.php`, no `--force`), run the checks from the drill.
4. Point `api/config.php` at the new database (or, if you must reuse the old one, drop its tables and restore with `--force`; only after step 2).
5. Open the app, sign in with a test account, check `https://wantuch.pk/spacebook/api/health.php` shows `"db":true`.
6. Work recorded on the server **after** the backup's time is lost. Devices only keep events the server has not confirmed, so they will not re-send what had already been confirmed; events still waiting in a device's outbox (made offline) are sent on its next visit, and the server applies each once. Tell students that coins and practice from the last day or so may be missing.

## What this does not cover

Nothing here backs up uploaded course files (there are none) or the git repository (GitHub holds it). Restoring an older dump also restores older `schema_version`; the app then applies any newer migrations by itself on the next request.
