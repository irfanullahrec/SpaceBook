# SpaceBook — Implementation Roadmap

**Date:** 2026-10-19 · Based on `docs/SPACEBOOK_DEEP_AUDIT.md` (finding IDs in brackets).
Ordering principle: **stop the bleeding → build a safety net → change architecture behind that net → add features.** No phase starts until the previous phase's exit gate is green.

---

## Phase map

| Phase | Goal | Key findings | Depends on | Size |
|---|---|---|---|---|
| **P0** | Security incident + deploy recovery | SEC-01, DEP-01 | — | 1–2 days |
| **P1** | Safety net: baseline, tests, tracing, CI | QA-01, ARCH-01 (freeze), DATA-01 (trace) | P0 | 1–2 weeks |
| **P2** | Server & sync correctness | SYNC-01/02/03, SEC-02, SEC-05, PRIV-01, BAK-01 | P1 | 1–2 weeks |
| **P3** | Content contract + manifest + lazy loading | PERF-01, ARCH-03, ARCH-02, DATA-02 | P1 | 3–5 weeks |
| **P4** | Offline-first (PWA, IndexedDB, packages, fonts) | OFF-01, PERF-01 | P3 (and P2 for the outbox) | 2–3 weeks |
| **P5** | Rendering core: hooks, scoped CSS, remove DOM rewriters | ARCH-01, PERF-02, SEC-06, UX-01 | P1, P3 | 4–6 weeks (subject by subject) |
| **P6** | Tab model + content integrity | TAB-01, CONT-01/02/03, MCQ-01, PDF-01 | P5 | 2–3 weeks |
| **P7** | Multilingual engine (lexicon + sentence store) | ML-01, SEC-04 | P3, P4 | 3–4 weeks (+ content review time) |
| **P8** | Licensing, integrity, secure updates, CSP | SEC-03, SEC-06, additional req. 1–3, 14 | P3, P4, P5 | 2 weeks |
| **P9** | Modules: Papers, Test Prep, Study Plan, Stats, Profiles, Admin | CONT-02, ADMIN-01, PRIV-01, DATA-02 | P2, P6 | 3–4 weeks |
| **P10** | Cleanup & archive | Cleanup report | P1 (tracing), P3 | 2–3 days, then per release |
| **P11** | Performance tuning & low-end devices | PERF-02, S-08 | P4, P5 | 1–2 weeks |
| **P12** | Accessibility, search, docs, handover | UX-01, S-08, MAINT-01 | P5 | 1–2 weeks |

Estimates assume one focused developer/agent with owner review; content-review work (lexicon, Board SLO mapping) is extra and runs in parallel from P7.

---

## P0 — Security incident and deploy recovery (do first)

| # | Task | Owner | Verification |
|---|---|---|---|
| P0-1 | Delete `public_html/spacebook/spacebook_upload.zip`; add `Options -Indexes` for `public_html/spacebook`; rotate DB password; update `DB_PASSWORD` secret; separate local password | **Site owner** (agent only with explicit approval) | `curl -I …/spacebook_upload.zip` → 404; listing gone; `health.php` `db:true` |
| P0-2 | Change `tools/build_upload_zip.py` so it **never** embeds `api/config.php`; config is created on the server once (outside web root if possible) or by CI from secrets | agent | zip listing has no `config.php` |
| P0-3 | Read the failing Actions logs; fix deploy (likely size/timeout); deploy a known-good commit | agent + owner | green run; `/spacebook/` serves the app |
| P0-4 | Commit current uncommitted work on a branch (`wip/2026-10-19`) and the 83 untracked cover webp files, so nothing is lost | agent | `git status` clean |
| P0-5 | Make the GitHub repo private or split content out (decision: owner) | owner | API `private:true` |

**Exit gate:** no secret reachable over HTTP; live site loads; all local work committed.

---

## P1 — Safety net before any refactor

| # | Task | Notes |
|---|---|---|
| P1-1 | **Baseline snapshot** of every class × subject × chapter × main tab: DOM text hash, tab list, screenshot (desktop 1280 + phone 375), console errors. Store under `tests/baseline/<date>/`. | Playwright (dev-only dependency) against `php -S`; reuse logic from `tools/ui_audit/audit_tabs.js` |
| P1-2 | Repair `tools/validate.js` (crash at line 146, 10 stale expectations) and `tools/smoke.js` (32 failures): each failure is either a real regression (fix data/code) or a stale expectation (update with evidence). Document each decision. | Do not "fix" by deleting assertions without recording why |
| P1-3 | **Global-access tracer**: a dev-only script that proxies each data global and records which properties each subject reads. Output `tests/trace/<subject>.json`. | Proof needed for DATA-01 and lazy loading |
| P1-4 | CI: add a `test` job (validate + smoke + headless snapshot subset) to `.github/workflows/deploy.yml`; `deploy` needs `test`. | Keep tests dependency-light; Playwright only in CI/dev |
| P1-5 | Regression rule: any PR touching a shared file (`app.js`, `style.css`, `index.html`, `sb_*.js`, readers) must run the **full** snapshot suite. | Written into CONTRIBUTING.md |

**Exit gate:** validate & smoke green; baseline stored; CI blocks deploy on failure.

---

## P2 — Server and synchronisation correctness

| # | Task | Findings |
|---|---|---|
| P2-1 | API v2 envelope: `/api/v2/sync` accepting **events** `{id(uuid), type, payload, clientTs, deviceId}`; idempotent insert (`UNIQUE(user_id, event_id)`); server assigns `seq`. Keep v1 endpoints working until clients migrate. | SYNC-01/02/03 |
| P2-2 | Server-side activity catalogue (generated from the content manifest) → coins computed only for known activities; per-user rate limit. | SEC-02 |
| P2-3 | Study plans and test-prep records become event streams + server-side materialised views; deletions are tombstone events; conflicts resolved by server `seq`, not client clocks. | SYNC-02/03 |
| P2-4 | Auth hardening: device tokens (random 256-bit, hashed in DB, revocable) for offline sync; CSRF token for cookie flows; throttling by IP **and** account; generic "invalid credentials"/"if this number is registered…" messages; password change; reset flow via verified channel (owner decision: WhatsApp OTP provider or admin-assisted); prune `login_attempts` > 30 days; set `session.gc_maxlifetime` consistent with cookie. | SEC-05, S-01 |
| P2-5 | Migrations run by deploy (`api/migrate.php` CLI-only or CI step), not on requests; `health.php` minimal public output (`ok`), details behind a token. | SEC-05 |
| P2-6 | Profile endpoints: view/edit, export (JSON), delete account (with grace period), privacy notice. | PRIV-01 |
| P2-7 | Backups: nightly `mysqldump` via cPanel cron to off-site storage; 30-day retention; documented restore drill. | BAK-01 |

**Exit gate:** API tests (PHPUnit or plain PHP CLI tests) cover idempotency, auth, limits; two-device offline scenarios pass.

---

## P3 — Content contract, manifest and lazy loading

| # | Task |
|---|---|
| P3-1 | Write **Book Content Contract v1** (JSON Schema): book meta (`classId`, `subjectId`, `medium`, `dir`, `langs`, `version`, `sourceStatus`), units → lessons → blocks (`para`, `heading`, `figure`, `table`, `math`, `example`, `activity`, `exercise`, `mcq`, `sq`, `lq`, `summary`, `glossary`), each block `id`, `orig` text + `lang`, `tr:{en,ur,ps,ar}` with provenance, `page` reference. |
| P3-2 | **Adapters** (build-time, Node) from the 5 legacy contracts to v1. Output `content/<classId>/<subjectId>/book.v1.json` + `meta.json` (sha256). Legacy files stay untouched. |
| P3-3 | **Manifest generator** `content/manifest.json` (books, versions, sizes, hashes) + registry used by `data.js`. |
| P3-4 | **Loader** `SB.content.getBook(classId, subjectId) → Promise<Book>` (uses only its arguments — fixes ARCH-02); in-memory LRU; later backed by IndexedDB (P4). |
| P3-5 | Migrate consumers to the async loader one by one: subject workspace, search (prebuilt index), test prep builder, study plan index, word stats, papers. Each migration verified against the P1 baseline. |
| P3-6 | Remove eager `<script>` tags subject by subject only after its snapshot parity passes. |
| P3-7 | One `npm run build` (or `node tools/build/all.js`): adapters → manifest → search index → MCQ bank → study index → word stats; CI fails if committed outputs differ. |

**Exit gate:** startup ≤ 3 MB JS; every subject renders identically (snapshot parity) from v1 packages.

---

## P4 — Offline-first

| # | Task |
|---|---|
| P4-1 | `manifest.webmanifest`, icons, `sw.js` with versioned precache of the app shell (HTML/CSS/core JS/KaTeX/fonts). |
| P4-2 | Content packages: "Download for offline" per class/subject with size shown; stored via Cache Storage + IndexedDB index; `navigator.storage.persist()` requested. |
| P4-3 | Local stores in IndexedDB: progress, test prep, study plans, word-stats marks, reader settings, **sync outbox** (never evicted). |
| P4-4 | Sync worker: on `online`, `visibilitychange`, app start and every N minutes; exponential back-off; batch; idempotent. |
| P4-5 | Bundle fonts (Noto Nastaliq Urdu, Noto Naskh Arabic, Noto Sans) as WOFF2; remove the Google Fonts link. |
| P4-6 | Replace online TTS with Web Speech API voices when present; otherwise hide the button offline (no fake audio). |
| P4-7 | Update flow: SW detects new manifest → "Update available" → downloads changed packages only. |

**Exit gate:** airplane-mode acceptance test of every module (books, lessons, exercises, images, meanings, paragraph translations, test prep, study plans, paper generation, question banks, progress); sync of queued activity after reconnect with zero loss/duplication.

---

## P5 — Rendering core (the regression fix)

| # | Task |
|---|---|
| P5-1 | Introduce `SB.hooks` (ordered, named, per-subject-scopable) and `SB.render(ctx)` pipeline; `ctx = {classId, subjectId, book, chapterIdx, tab}`. |
| P5-2 | Migrate wrappers module by module (readers → structure → medium/rtl → trilingual/four-lang → topic practice → mcq → trace/skin → word stats → continue learning) from "wrap global" to "register hook". After each: snapshot parity. |
| P5-3 | Replace text-sniffing (`sb_rtl`, `sb_medium`, `sb_solve` slot guessing) with manifest metadata (`medium`, `dir`, `langs`). |
| P5-4 | Delete each `MutationObserver` once its hook replaces it. Target: 0 document-wide observers (translator UI may observe its own root only). |
| P5-5 | Scoped CSS: one stylesheet per component with a root class; move injected `<style>` strings to files; reduce `!important` (target < 20). |
| P5-6 | Event delegation (`data-action`) instead of inline `onclick`; remove `eval`. |
| P5-7 | Render only the active tab; precompute tab plans at build time. |

**Exit gate:** snapshot parity for all subjects; observer count = 0; `eval` count = 0; chapter-open p95 targets (P11) met on desktop.

---

## P6 — Tab model and content integrity

| # | Task |
|---|---|
| P6-1 | Declarative chapter tab plan from content: `Lessons (Topics / Activities / Examples nested, horizontal sub-tabs) → Exercises → Summary → Board SLO (MCQs / SQs / LQs) → Word Stats`, hidden when empty, labels from the medium dictionary, fixed positions. Respect the owner's recorded "book-order, no repeats" rule. |
| P6-2 | Remove templated MCQs (CONT-01) from all student paths; show "Not available yet" where no sourced items exist. |
| P6-3 | One MCQ normaliser (`answerIndex|null`, `source`, `page`) used by chapter tabs, Test Prep and Papers; no key → no key printed (CONT-02). |
| P6-4 | Remove placeholder videos / fake players / placeholder YouTube ID (CONT-03); video tab only with real, offline-capable media. |
| P6-5 | Content lints in CI: repeated stems across chapters, key-index skew, missing keys, duplicate stems, unreferenced page numbers. |
| P6-6 | PDF links: only if licensed and packaged; otherwise remove button (PDF-01). |

---

## P7 — Multilingual engine

| # | Task |
|---|---|
| P7-1 | Lexicon v1 builder: merge book glossaries, `ENG_URDU_DICT`, `SB_OFFLINE_LEXICON`, per-book word lists → `{lemma, lang, forms[], meanings:{en,ur,ps,ar}, pos, source, reviewed}`; normalisation for Arabic-script variants (ی/ي, ک/ك, ہ/ه, diacritics). Placeholder meanings ("اردو معنی") removed. |
| P7-2 | Coverage report per book: % words with all 3 target meanings; review queue (CSV) for missing/unreviewed items, especially Arabic and Pashto. |
| P7-3 | Sentence translation store keyed by block id with provenance (`book`, `reviewed`, `machine`); machine items labelled. Arabic lines added via review queue, not live MT. |
| P7-4 | Single interaction component: hover (desktop) / tap-and-hold (touch) on any word in any of the 4 languages → the other three meanings; sentence click → drawer with the other three translations (EN/UR/PS/AR, per owner rule). Qur'anic text never translated. |
| P7-5 | Optional online fallback through **your own** server proxy (approved provider, no personal data, cached, rate-limited); off by default for minors. |

---

## P8 — Licensing, integrity, secure updates

| # | Task |
|---|---|
| P8-1 | Signed manifest (Ed25519, private key only on the build machine/CI secret); client verifies signature + package hashes before use. |
| P8-2 | Device activation: account → device token → encrypted package keys (AES-GCM) delivered per device; packages stored encrypted at rest in IndexedDB; decrypted in memory. Honest limit: a determined user can extract decrypted content from a running client; this raises cost and enables revocation. |
| P8-3 | Visible + invisible watermark (account id) in rendered pages/prints. |
| P8-4 | CSP `default-src 'self'` (after P5-6), `frame-ancestors 'none'`, HSTS, `X-Content-Type-Options`, `Referrer-Policy`. |
| P8-5 | Deploy via CI only; atomic release folders; checksum verification post-upload. |

---

## P9 — Modules

| Module | Work |
|---|---|
| Papers | uses normalised MCQ/SQ/LQ with provenance; blueprint validation (marks, counts vs available); print key only when verified; offline. |
| Test Prep | event-based sync; guest→account merge with consent; Class 11 keys only from verified sources; review queue for MCQ-01 items. |
| Study Plan | index regenerated by the build; offline; event sync; reminders explained honestly (in-app when closed browsers can't notify). |
| Statistics / Word Stats | computed from local events; synced summaries; consistent tab position. |
| Profiles | P2-6 endpoints + UI. |
| Administration | role checks (`user_type`), admin page for blocking users, viewing sync errors, content version status; audit log table. |

---

## P10 — Cleanup and archive
Follow `docs/SPACEBOOK_CLEANUP_REPORT.md` section 6. Safe groups right after P1 (backup first); deployed/uncertain groups only after P1-3 tracing and P3 parity.

## P11 — Performance budget (measured on a reference low-end Android + desktop)
- Initial transfer ≤ 3 MB (compressed), JS heap ≤ 150 MB while reading, Time-to-Interactive ≤ 4 s (low-end, warm cache ≤ 1.5 s).
- Chapter open p95 ≤ 300 ms desktop / ≤ 1.5 s low-end; tab switch ≤ 150 ms / ≤ 600 ms.
- Word meaning lookup ≤ 30 ms offline; search ≤ 100 ms offline.
- Images: WebP/AVIF, width-appropriate `srcset`, lazy.

## P12 — Accessibility, search, documentation
- Root `lang`/`dir` set per open book; `role="tablist"`/`tab`/`tabpanel` with arrow keys; buttons not divs; focus management; contrast AA.
- Prebuilt offline search across all downloaded books with Urdu/Pashto/Arabic normalisation.
- Replace outdated `CONTRIBUTING.md` and `docs/01..06` with an accurate architecture doc, data-contract doc, release/rollback runbook, and the protect-list.

---

## Cross-cutting rules (all phases)
- Work on branches; one finding (or one subject migration) per PR; tag a checkpoint before each phase (`checkpoint/P<n>-start`).
- Shared-file changes require the full snapshot suite; subject-local changes require that subject's suite plus the "neighbour" subjects listed in the trace.
- Rollback = revert the PR (no data migrations without a down-migration and DB backup).
- Progress reports state **measured** results and list anything not verified.
