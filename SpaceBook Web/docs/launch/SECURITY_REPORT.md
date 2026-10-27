# Security and privacy review (Phase 5)

Date 2026-10-27. Method: reading the code of the website, the API and the app; secret scans of the files and the git history; read-only requests to the live site (5 HEAD requests and one `health.php` GET, no probing, no load); tests on a local PHP and Apache. No destructive test was run against the live site. **Limits:** nobody has penetration-tested this; the live host's PHP settings, database user rights and server logs were not visible to me.

## Findings and what was done

| ID | Finding | Status |
|---|---|---|
| S-01 | The live site sent none of the security headers (no `nosniff`, framing, referrer or permissions policy, no HSTS). `deploy/spacebook.htaccess` was never installed, and the file the deploy does upload only set the directory index. | **Fixed in the repository:** `.htaccess` now sends `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`, `Permissions-Policy` (camera, microphone, geolocation, payment, USB off) and `Cross-Origin-Opener-Policy`, refuses `.sql` / `.bak` / `.log` / `~` files, and sets cache rules. Tested on Apache 2.4: `tests/launch/htaccess_check.js` (16 checks). Reaches the host with the next deploy. HSTS and the Content-Security-Policy stay out (see S-02). |
| S-07 | The cache rule in `deploy/spacebook.htaccess` for content-hashed files ("keep for a year") never took effect: the `FilesMatch` section that sets `no-cache` is applied after the directive outside it. Found by the test above. | Fixed in both files. Effect: repeat visits stop re-asking for hundreds of unchanged files. |
| S-02 | The Content-Security-Policy can only be report-only: 416 inline `onclick` handlers and `eval` in the lazy loader. | Accepted for launch; documented (`PHASE8_SECURITY.md`). Removing the handlers is a large refactor, not a launch fix. The admin pages already send an enforced strict policy. |
| S-03 | Secrets: none in tracked files, in the history (`api/config.php` was never committed), or in the App repository; the deploy writes `config.php` from repository secrets; the live `config.php` and `.htaccess` answer 403; `health.php` shows only `{ok, db}` without its token. | Checked. |
| S-04 | No way to report a mistake, a bug or a wrong answer. | **Built** (Phase 7): `api/feedback.php`; see `docs/FEEDBACK.md`. Uploads are validated (type, size, hidden script text), re-encoded when GD is available, stored in the database and never served as files; rate limits per address, per student and overall; a retry never duplicates; only administrators can read a report or its picture. |
| S-05 | Owner actions of `PHASE0_SERVER_STEPS.md` (delete the leaked zip from the host, rotate the database password, point the FTP account at the site folder, make the repository private) cannot be seen from here. | **Owner action.** Rotating the password would be needed if the zip was ever downloadable. |
| S-06 | Licence of the textbooks for redistribution. The scans in `Books` carry the watermark of a third-party site and "NOT FOR SALE"; the books are Khyber Pakhtunkhwa Textbook Board publications; nothing in the repository records permission to ship their text and pages inside a public website and an app. The repository is public. | **Owner action: written permission or confirmation; until then the risk is the owner's.** |
| S-08 | Fonts: Noto Nastaliq Urdu, Noto Naskh Arabic and Amiri, SIL Open Font Licence 1.1, copies of the licences in `assets/fonts`. KaTeX (MIT) carries its licence. | Checked. |
| S-09 | Dependencies: `npm audit` finds 0 vulnerabilities (dev-only tools, nothing ships); the Android app's Gradle dependencies were not audited (no tool offline). | Partly checked. |

## What the code already does well (read, and covered by the existing PHP tests)

* Every query uses prepared statements; the few dynamic lists are integer-cast (`lib/feed.php`).
* Passwords: `password_hash` with rehash on login, a dummy hash on unknown users (no timing leak), throttled logins, an audit log.
* Sessions: `HttpOnly`, `SameSite=Lax`, `Secure` over https; device tokens are stored only as SHA-256; cookie-authenticated writes must be same-site.
* The administration pages: role read from the database on every request, a CSRF token, escaped output, `noindex`, no inline script, a strict policy; the role can be granted only from the command line.
* Per-student rate limits and daily caps on coins and activities (decided on the server).

## Privacy of children

* Reports (new): no name, number, e-mail, address, device name or browser string; the context is a whitelist of short strings (class, subject, chapter, page, screen, version); a review page shows exactly what leaves the device; reports are anonymous unless the student ticks "Link it to my account"; pictures are deleted 90 days after a report is closed and closed reports after a year (`php api/migrate.php prune`, to be run monthly).
* Account data: export and deletion exist (30-day grace, then purge); the News Feed shows only "Ali K." style names.
* The audit log keeps an address and a short browser hash for 365 days (`prune`).
* Backups: `BACKUP_RESTORE.md`, restore drill in the PHP tests. An off-site destination and a schedule are owner decisions.
* Screenshots: the release app blocks screenshots of the books (`FLAG_SECURE`), so a student cannot capture a page to attach; they can attach any picture from the phone.

## Honest limits

Anything the site sends to a device so that it works offline can be copied by a person who tries. Hashing, headers and the app's integrity check make casual copying harder; they do not make it impossible. The offline downloads trade protection for availability, as the owner chose.

## Owner actions for launch

1. Install the new `.htaccess` by pushing (it is uploaded by the deploy). Check `https://www.wantuch.pk/spacebook/` with `curl -I` afterwards (the test lists the headers expected).
2. After a few days over https with no problem, add `Header always set Strict-Transport-Security "max-age=31536000"` by hand.
3. Run `php api/migrate.php prune` monthly (cron) and keep a database dump before each deploy that carries a migration (009 adds two tables).
4. Confirm the textbook licence (S-06) and finish the steps of `PHASE0_SERVER_STEPS.md` (S-05).
5. Install PHP's GD extension on the host if missing (pictures are then re-encoded on the server too).

## Re-check on the release commit (2026-10-27)

* Secret scan of the branch's code and configuration changes against `origin/main` a0773486 (834 files, data files excluded): no password, key, token, private key or connection string; no `.env`, `.pem` or key file is tracked.
* The changes since the first review are books (answers), build tools, the offline layer (`js/core/offline.js`, `tools/build/make_offline.js`) and tests. None adds a network endpoint, a stored credential or a third-party request; `tools/validate.js` still passes its check that no script sends text to a third-party translation service (1,288 checks).
* The offline layer stores only the public book files and the list of subjects the student downloaded, in the browser's own storage on the device; it sends nothing.
* The Android app: see `PARITY_REPORT.md` for the secret scan of the App repository.
