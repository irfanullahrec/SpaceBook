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
