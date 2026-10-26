# Suggestions and problem reports (Web and App)

Students can send five kinds of report from anywhere in the website and from the Android app: **a suggestion**, **something broken**, **a mistake in a textbook page**, **a wrong meaning or translation**, **a wrong answer**, with an optional picture. Added 2026-10-26 (migration 009).

## What the student sees

* A 💬 button in the header, a link in the menu ("Suggest / Report a problem"), a link in the footer, and **"Wrong answer? Tell us"** under every answer (the question is copied into the box).
* One dialog: what is it about, the words (5 to 2,000 characters), an optional picture (JPEG, PNG or WebP; the browser decodes it and draws it again as a JPEG of at most 1,600 pixels and 1.5 MB, so location data does not leave the device), and "Include where I am" (class, subject, book, edition, chapter, tab, page, screen, version; it can be switched off).
* **A review page** lists exactly what will be sent, every technical value included, and what is not sent (name, phone number, e-mail, password, other pages). Nothing leaves the device before the Send button.
* The report is saved on the device first. Offline the button says "Save to send later". **My reports** shows each one as *Waiting to be sent*, *Sending*, *Received*, *Seen by the team*, *Fixed*, *Looked at, not changed*, *Already reported* or *Could not be sent* (with the reason, Send now and Delete). The state words come back from the server for the report's own id; the server never returns anyone's text.
* Signed-in students are **not** linked by default. Ticking "Link this report to my account" sends the session cookie as well (the account then also gets the report in its data export).

## What the server keeps (`api/feedback.php`, `api/lib/feedback.php`)

* `feedback_reports`: a client UUID (a retry never makes a second report), the account id (only when linked, `NULL` otherwise, and `NULL` again if the account is deleted), platform (web or app), kind, the words, a context of short whitelisted strings, state, an administrator's note.
* `feedback_images`: the picture, in the database, never as a file. With GD the server decodes and re-encodes it (JPEG, at most 1,600 px); without GD the bytes are kept after the header, size and a scan for `<?php`, `<script` and `<html`. Only administrators can fetch it, and it is served as an image with `Content-Security-Policy: sandbox` and `nosniff`.
* Not kept: address, device name, user agent, name, number, e-mail.
* Limits: 8 an hour and 20 a day per address when not signed in, 20 an hour per student, 2,000 a day for the whole service; a retry of a stored report is always answered.
* Retention (`php api/migrate.php prune`, run it from a monthly cron): pictures go 90 days after a report was closed, closed reports after a year.

## Receiving the reports

`api/admin.php?v=feedback` (administrators only, the role is given on the command line): list with filters by state and kind, one report with its words, place and picture, a state and a note, every change written to the audit log, a count of new reports on the overview. Opening a new report marks it *seen*. There is no way to reply to a student (reports may be anonymous): the state and the note are what the sender can see, as a word. If replies are wanted later, a contact field would have to be added and justified.

## Tests

| Test | What it proves |
|---|---|
| `php tests/php/run.php` (`feedback_tests.php`, 69 checks; also `SB_TEST_NO_GD=1` for a host without GD) | validation, whitelisting, duplicates, the rules for who is the sender (a cross-site cookie request is not linked), picture checks (GIF, a PHP file called .png, hidden script, oversize, SVG refused; a photo with short markers accepted), limits, the administrator pages (404 for others, CSRF, escaping), export, account deletion, retention, migration down |
| `node tests/feedback/browser.js` (40 checks, real Chrome, real API) | the whole path: dialog, keyboard, focus, axe, a 1.2 MB noisy PNG made small, review page, sending, the report on the administrator's page with its picture, offline queue and automatic send, a lost answer retried without a second report, a refused report, a server error, the answer link, a 390 px phone |

## Not done / for the owner

* Urdu labels were written for this dialog; **Pashto is not written** (no native review yet).
* The Android entry points and the WebView picture chooser are listed in `docs/parity.json` (`feedback.report`).
* If the host has no GD, pictures are stored as the browser made them (already metadata-free); install GD when possible.
* Cron: `php api/migrate.php prune` (see `docs/BACKUP_RESTORE.md` for the other housekeeping).
