# SpaceBook progress log

## 2026-10-19 — Phase 0 (local part): security incident + deploy recovery
Done:
- Committed the outstanding work on branch `wip/2026-10-19`: 5 modified files, 137 `covers/Books/*/kptb_*.webp` covers (6.9 MB) and the audit/roadmap docs. Tag `checkpoint/p0-start`.
- Branch `phase/p0-security`: `tools/build_upload_zip.py` no longer writes `api/config.php` into the package. It asserts that no secret file is inside, and it takes an optional output path.
- `api/config.sample.php`: the real cPanel account names are replaced with placeholders.
- `.github/workflows/deploy.yml`: connects to `s26.hosterpk.com` (the name on the FTPS certificate, same IP 64.31.31.90) with `security: strict`. The live check now fails separately for "index.html not served", "upload zip reachable" and "database unreachable".
- `docs/PHASE0_SERVER_STEPS.md`: the exact steps the owner does on the server.

Files: tools/build_upload_zip.py, api/config.sample.php, .github/workflows/deploy.yml, docs/PHASE0_SERVER_STEPS.md, docs/PROGRESS_LOG.md

Verified by:
- `python tools/build_upload_zip.py <scratch>/test_upload.zip` → 747 files, 124 MB. The only config entry is `api/config.sample.php`. The test zip was deleted afterwards.
- `openssl s_client -starttls ftp -connect wantuch.pk:21` → certificate CN=s26.hosterpk.com, verify code 0. `s26.hosterpk.com` and `wantuch.pk` both resolve to 64.31.31.90.
- GitHub API, last 6 runs: all failed at "Check the live site". "Upload to wantuch.pk" succeeded each time, in 3 s, or 3 min 16 s on the full re-upload.
- Live probes now: `/spacebook/` 200 (directory listing), `/spacebook/index.html` 404, `/spacebook/api/health.php` 404, `/spacebook/spacebook_upload.zip` **200 (still exposed)**.
- `deploy.yml` parses as YAML.

Root cause of DEP-01: the FTP account `spacebook@wantuch.pk` uploads into a folder that is not `public_html/spacebook`. A workflow change cannot fix this; the owner fixes it in cPanel (server steps, step 5).

Not verified:
- Strict-TLS FTP upload from CI. Nothing has been pushed yet, because a push to `main` deploys.
- Any server step: SEC-01 is still open.

Risks / owner decisions needed:
- Server steps 1–6 in docs/PHASE0_SERVER_STEPS.md.
- Repository visibility. The repo is public and now also holds the audit docs, which describe the leak. Do not push them while the zip is still online.
- The live server runs PHP 7.4.33 (earlier health output), not PHP 8 as the start prompt says. api/ must stay 7.4-compatible until the host is upgraded.

Next: Phase 1 (baseline runner, repair validate.js/smoke.js, tracer, CI test gate).

## 2026-10-19 — Phase 1 (in progress): safety net
Done:
- Branch `phase/p1-safety-net` (tag `checkpoint/p1-start`).
- `tools/validate.js`: no longer crashes (every check runs inside `safe()`); sandbox defines `window`; 35 stale pre-rebuild checks replaced by Contract C checks over all 92 `CLSn_BOOKS` files plus a unit-count lock `tests/contract/cls_books.json` (`--update-books` to accept a rebuild).
- `tools/smoke.js`: now loads all 248 index.html scripts in order (`tools/lib/app_sandbox.js`); 41 stale tests replaced by one test that opens 88 rebuilt books through the real reader and renders every tab of the first and last unit, plus 10 Class 12 books.
- `package.json` (dev-only, Playwright 1.63.0) and `tests/baseline/{lib,run}.js` (browser baseline runner).

Verified by:
- `node tools/validate.js` → 946 passed, 0 failed (two runs; was 10 failures then a crash). Changing a locked count makes it fail.
- `node tools/smoke.js` → 251 passed, 0 failed, ~21 s (two runs; was 32 failures). A wrong expected count makes it fail.

Not verified:
- The Playwright baseline runner has NOT completed a run. Two trial runs crashed the page ("Target crashed") while free RAM was 0.5–1.2 GB of 7.9 GB; the app needs ~0.7 GB per page. An earlier probe with `explore.js` did load the app in Chrome with 0 console errors.
- No tracer, no CI test job, no CONTRIBUTING.md rewrite yet.
- Baseline stability (≥ 99.5 % hash match over two runs) not measured.

Known tests dropped (reasons in commit messages): old Drawing 2/3, Maths 1/2/3 tab tests and legacy counts for rebuilt books.

Risks / owner decisions: baseline needs ~1.5 GB free RAM; close other programs or run it on a bigger machine.
Next: re-run the baseline with free RAM, then tracer, CI gate, CONTRIBUTING.md.
