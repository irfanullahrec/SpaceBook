# SpaceBook — Agent Start Prompt (single file)

> **Give this whole file to the coding agent as its first message.** It is self-contained: everything the agent needs
> (facts, rules, findings, phases, acceptance criteria, cleanup procedure) is inside. The longer background documents in
> `D:\SpaceBook\SpaceBook Web\docs\` (`SPACEBOOK_DEEP_AUDIT.md`, `SPACEBOOK_IMPLEMENTATION_ROADMAP.md`,
> `SPACEBOOK_CLEANUP_REPORT.md`) are optional extra detail. Finding IDs such as `ARCH-01` are explained in **Appendix A**.
> Written 2026-10-19 from a full investigation of the project.

---

## 0. Start here — your first session

1. **Do not write code yet.** Read this whole file, then open and skim: `index.html`, `js/data.js`, `js/app.js` (functions `openSubject` ~line 1894, `getSubjectChapterList` ~19207, `getCurriculumQuestionsForCategory` ~12014), `js/sb_structure.js`, `js/sb_medium.js`, `js/universal_translate.js`, `js/sb_rewards.js`, `js/sb_study_plan.js`, `js/test_prep.js`, `api/*.php`, `.github/workflows/deploy.yml`, `tools/build_upload_zip.py`.
2. **Ask the owner one question before anything else:** "Have the Phase 0 server steps been done — the zip `spacebook_upload.zip` deleted from `public_html/spacebook/`, directory listing turned off, and the database password rotated?" Do not perform server actions yourself unless the owner explicitly tells you to.
3. Then start **Phase 0** (the parts that are local code/git work), then **Phase 1** (safety net). Do not start Phase 3 or later until the Phase 1 exit gate is green.
4. Keep `docs/PROGRESS_LOG.md` updated using the reporting format in section 8. Keep working through steps without asking "continue?"; stop only for the owner decisions listed in section 9 or for a failing gate you cannot resolve.

---

## 1. Your role and the mission

You are the lead engineer for **SpaceBook (TuitionHub – KPK Portal)**, an educational web app for Khyber Pakhtunkhwa Textbook Board (KPTBB) books, Classes 1–12, in four languages (English, Urdu, Pashto, Arabic). You will turn the existing project into a **stable, secure, offline-first, multilingual, fast and maintainable** platform **without destroying or degrading the verified educational content and the features that already work.**

The learning flow is: **Class → Subject → Book → Chapter/Unit → Lesson → Topics / Activities / Examples → Exercises**, and every chapter also offers **Summary**, **Board SLO Based MCQs / SQs / LQs**, and **Word Stats** when content for them exists.

Only user-related records (statistics, activity, progress, test-prep history, study plans, coins) need the server; **everything educational must work offline.**

---

## 2. Facts about the project you must not re-discover from scratch

**Location and stack**
- Web app root: `D:\SpaceBook\SpaceBook Web` (git root is `D:\SpaceBook`, branch `main`, remote `github.com/irfanullahrec/SpaceBook`, currently **public**).
- Front end: vanilla JS, no bundler, no framework. `index.html` loads **250 synchronous scripts (358 MB)**: `js/data.js` (registry of classes/subjects), ~170 book data files, `js/app.js` (23,456 lines, 395 functions, global `state`), then ~60 add-on modules.
- Back end: PHP 8 + PDO MySQL in `api/` (`auth.php`, `progress.php`, `study_plans.php`, `test_prep.php`, `health.php`, `db.php`, `session.php`, `schema.sql`, `.htaccess`). Session cookie `spacebook_sid`. Tables: `users`, `login_attempts`, `activity_progress`, `study_plans`, `test_prep_records`, `test_prep_sessions`.
- Local run: `.claude/launch.json` → `spacebook-php` (`C:/xampp/php/php.exe -S 127.0.0.1:8790 -t .`) and `spacebook-static` (python, 8765). MySQL from XAMPP (`C:\xampp`) must be started for the API.
- Deploy: `.github/workflows/deploy.yml` (FTP to wantuch.pk, writes `api/config.php` from secrets) and a manual `tools/build_upload_zip.py`. **The last five CI deploys failed; the live URL currently serves a directory listing.**
- Vendored: KaTeX in `assets/vendor/katex/`. No npm dependencies in the app.

**Content contracts that exist today (all must keep working until migrated)**
- A. `Object.assign(DATA, …)` in `js/data_chem.js`, `data_phys.js`, `data_eng.js`, `data_bio.js`, `data_comp.js` (legacy Class 9/10).
- B. Named globals (`BIO_DATA`, `ENGLISH_DATA`, `MATH_DATA`, `URDU_7_DATA`, `PHYS_12_DATA`, …) chosen by if-chains in `getSubjectChapterList` (`js/app.js:19207`).
- C. `window.CLS1_BOOKS … CLS10_BOOKS[subjectKey] = {units, book, words}` (rebuilt books, Classes 1–10) + shared `window.CLS6_SOLUTIONS` (19,910 keys, prefixed per class/subject, no collisions).
- D. `window.CLASS11_BOOKS` + per-book render functions (Class 11) routed by `js/class11_study_views.js`.
- E. Class 12 per-subject data + `js/*12_exercise_banks.js` + `js/*_study.js` routed by `js/class12_study_views.js`, plus `math12_*` translation/recovery overlays.
- Load-time overlays mutate other files' data: `chemistry_10_source_data.js`, `physics_10_source_data.js`, `english_10_source_review.js`, `biology_10_*_source.js`, `math12_*_recovery.js`.
- **Slot quirk:** in several Urdu/Arabic-medium books the original text sits in the `en` slot and English in `ur` (documented in `js/sb_solve.js`). Do not "fix" data blindly — add an explicit `lang` field via adapters.

**Generated files (never hand-edit; regenerate after data changes)**
- `js/test_prep_bank.js` ← `node --max-old-space-size=8192 tools/test_prep/build_mcq_bank.js`
- `js/study_plan_index.js` ← `tools/study_plan/build_study_index.js` (**currently stale** vs 15 data files)
- `js/word_stats_words.js`, `js/word_stats_summary.js` ← `tools/word_stats/build_word_stats.js`
- Book data files under `js/` are generated by per-class pipelines in `docs/source-verification/class-*/` (e.g. `build_book1.py`). Edit the transcriptions, not the generated JS.

**Owner decisions you must respect (from project history)**
- No language drop-downs or language tabs in readers; **clicking a sentence opens a drawer under it with the other languages, each on its own line**; word meanings on hover/long-press.
- Topic cards start collapsed and each has its own full-screen button.
- Chapter structure follows **book order**: Lessons → Summary → Exercise → practice; nothing shown twice.
- **Class 9/10 layout is the reference**; Classes 11/12 must match its tabs, cards and clicks.
- Tab labels follow the subject's **medium** (English/Urdu/Pashto/Arabic); only tabs with content appear.
- **Qur'anic text is never translated or altered.**
- Do not stop to ask "continue?" between routine steps; keep going until the phase gate or a genuine owner decision.

**Measured baseline (desktop, local)**: DOMContentLoaded 17.4 s; JS heap 698 MB; subject open up to 5.2 s (Class 12 Physics); 14+ document-wide `MutationObserver`s; `switchSubjectTab` wrapped ≥14 times; `tools/validate.js` crashes after 10 failures; `tools/smoke.js` 32 failures.

---

## 3. Non-negotiable safety and quality rules

1. **Never destroy completed work.** No deletion of data files, pipelines, transcriptions or covers. Unused files are *moved* to `D:\SpaceBook\SpaceBook_Archive\` with a log, only after verification.
2. **Never overwrite verified educational content without review.** Data changes go through the pipelines and a diff reviewed by the owner.
3. **Never modify unrelated subjects.** A task names its scope; touching anything outside it requires the full regression suite.
4. **No broad search-and-replace** across `js/` or `css/` without a dependency analysis and a snapshot run.
5. **Never invent textbook content, translations presented as book text, or official board questions.** Missing content shows "Not available yet".
6. **Never claim a feature is complete without running its tests and showing the evidence** (command + output, screenshot, or measurement).
7. **Never depend on internet services for essential offline functionality.**
8. **Never put secrets in front-end code, in the repository, or in any web-reachable file or archive.**
9. **Never clear, overwrite or drop unsynchronised student records.** The sync outbox is never evicted.
10. **Never trade educational accuracy for speed.**
11. **Never declare a module complete without testing it offline and online.**
12. **Use version control:** a branch per task, a tag `checkpoint/<phase>-<step>` before risky steps, small commits, and a backup of `.git` + `SpaceBook Web` before P10 cleanup or any DB migration.
13. **Shared changes are tested across all affected subjects** (see 5.3).
14. **Stay realistic:** client-side code that runs offline can always be read by a determined person. Say so; do not promise otherwise.
15. **Honest reporting:** every progress report lists what was done, how it was verified (with numbers), what was *not* verified, and known risks. Never report a guess as a result.
16. **Outward-facing actions** (deploying, deleting server files, rotating passwords, changing repo visibility, emailing/messaging anyone) require the owner's explicit approval in the conversation.

---

## 4. Working method

### 4.1 Before each phase
1. Read the phase section below and the referenced audit findings.
2. `git status` must be clean; create branch `phase/<id>-<slug>`; tag `checkpoint/<id>-start`.
3. Run the current test suite and save the results as the phase baseline.

### 4.2 During a phase
- One finding or one subject migration per commit/PR.
- After every change to a shared file (`js/app.js`, `css/style.css`, `index.html`, any `sb_*.js`, any reader, `structure_harmonizer.js`, `universal_translate.js`, `class11_study_views.js`, `class12_*`): run the **full** snapshot suite.
- After a subject-local change: run that subject's suite + the neighbours listed in its trace file.
- Keep a running `docs/PROGRESS_LOG.md`: date, task, files, tests run, results, open issues.

### 4.3 Rollback
- Code: `git revert <commit>` (never force-push `main`; never rewrite shared history).
- DB: every migration has a down-migration and runs only after a fresh `mysqldump`.
- Content packages: the manifest keeps the previous version; clients can pin back.
- Deploy: atomic release folders (`releases/<sha>`) with a pointer switch; rollback = switch pointer.

### 4.4 Definition of done (every task)
Code + tests + docs updated; full or scoped regression suite green; offline check where relevant; measured numbers recorded; owner-visible summary written.

---

## 5. Reusable components and data contracts to build

### 5.1 Book Content Contract v1 (`content/<classId>/<subjectId>/book.v1.json`)
```json
{
  "schema": "spacebook.book/1",
  "classId": "cls9", "subjectId": "cls9-bio", "title": {"en": "Biology", "ur": "حیاتیات"},
  "medium": "en", "dir": "ltr", "langs": ["en", "ur", "ps", "ar"],
  "version": "2026.10.19-1", "source": {"publisher": "KPTBB", "edition": "…", "pages": 0},
  "verification": {"status": "verified|partial|unverified", "lastPage": 0, "notes": ""},
  "units": [{
    "id": "u1", "number": "1", "title": {"orig": "…", "lang": "en", "tr": {"ur": {"t": "…", "src": "book"}}},
    "lessons": [{
      "id": "u1-l1", "title": {...},
      "blocks": [
        {"id": "u1-l1-b1", "type": "para|heading|figure|table|math|example|activity|exercise|summary|glossary|quran",
         "orig": "…", "lang": "en", "page": 12,
         "tr": {"ur": {"t": "…", "src": "book|reviewed|machine"}, "ps": {...}, "ar": {...}}}
      ],
      "topics": [{"id": "…", "title": {...}, "blockIds": ["…"]}]
    }],
    "exercise": [{"id": "…", "kind": "mcq|sq|lq|fill|match|tf|numerical|activity", "stem": {...},
                  "options": [{...}], "answerIndex": 2, "answer": {...}, "solutionId": "…", "page": 33,
                  "source": "textbook|board-paper:<year>|teacher", "verified": true, "slo": ["BIO-9-1.2"]}],
    "summary": [{...}], "slos": [{"code": "…", "text": {...}}]
  }]
}
```
Rules: `quran` blocks are never translated; every question has `source` and `verified`; `answerIndex` is `null` when no key exists.

### 5.2 Other contracts
- **Manifest** `content/manifest.json`: `{schema, version, generated, books:[{classId, subjectId, path, version, bytes, sha256, langs, medium}], lexicon:{path, sha256}, search:{…}, signature}`.
- **Lexicon v1**: `{id, lemma, lang, forms[], pos, meanings:{en,ur,ps,ar}, source, reviewed}` + per-language normalised index (Arabic-script normalisation: ي→ی, ك→ک, ۀ/ة/ه handling, diacritics stripped for lookup only).
- **MCQ (normalised)**: `{id, classId, subjectId, unitId, stem, options[], answerIndex|null, explanation, source, verified, page}` — used by chapter tabs, Test Prep and Papers alike.
- **Sync event**: `{eventId (uuid v4), deviceId, userId?, type, payload, clientTs, schema}`; server returns `{accepted:[eventId], seq}`.
- **Hook API** (`js/core/hooks.js`): `SB.hooks.on(name, fn, {subjects?, classes?, order})`, `SB.hooks.run(name, ctx)`; names: `book:loaded`, `chapter:beforeRender`, `chapter:afterRender`, `tabs:plan`, `tab:afterRender`, `word:lookup`, `sentence:translate`.
- **Content loader** (`js/core/content.js`): `SB.content.getBook(classId, subjectId)` (arguments only — never `state`), `SB.content.getManifest()`, `SB.content.isOffline(classId, subjectId)`.
- **Storage** (`js/core/store.js`): IndexedDB wrapper with stores `packages`, `lexicon`, `progress`, `testprep`, `plans`, `settings`, `outbox`.

### 5.3 Protecting completed subjects
- `tests/baseline/` holds per-chapter DOM-text hashes, tab lists and screenshots for every class/subject (created in Phase 1).
- `tests/trace/<subject>.json` lists the data globals and functions each subject touches (from the tracer); use it to compute "neighbours".
- A change is accepted only if every affected subject's snapshot is identical **or** each difference is listed and approved as intended.

---

## 6. Phases

Each phase: **Objective → Existing problems → Affected files → Required changes → Dependencies → Safety precautions → Testing → Acceptance criteria.**

---

### Phase 0 — Security incident and deploy recovery

**Objective.** Remove the live credential exposure, restore a working deployment, secure all local work.

**Existing problems.** SEC-01: `https://wantuch.pk/spacebook/` lists `spacebook_upload.zip` (117,161,854 B), which contains `api/config.php` with the live DB password; directory listing is on. DEP-01: app not served (index 404); five failing Actions runs; local `main` ahead by 2 with 5 uncommitted files and 83 untracked cover images. SEC-03: repo is public.

**Affected files.** Server `public_html/spacebook/`; `tools/build_upload_zip.py`; `.github/workflows/deploy.yml`; `api/config.sample.php` (contains an old cPanel user name `ameencon_Irfan`); `D:\SpaceBook\deploy\spacebook_upload.zip`.

**Required changes.**
1. Prepare (do not execute without owner approval) the exact server steps: delete the zip, add `Options -Indexes`, rotate the DB password, update the GitHub secret, set a different local password.
2. Change `tools/build_upload_zip.py` to exclude `api/config.php` entirely; document one-time server config creation.
3. Read the failing workflow logs; fix the cause (e.g. split upload, timeouts, `security: strict` with a valid certificate, exclude unused files); add a post-deploy check for `index.html` 200 + `health.php`.
4. Commit outstanding work to `wip/2026-10-19` and commit `covers/Books/*/kptb_*.webp`.
5. Replace the real-looking names in `api/config.sample.php` with placeholders.
6. Present the owner with the repo-visibility decision (private repo vs. code-only public repo + private content).

**Dependencies.** None. Everything else waits for this.

**Safety precautions.** No server action without approval. Do not open, print or log the password. Keep the local zip off cloud-synced folders until deleted.

**Testing.** `curl -I https://wantuch.pk/spacebook/spacebook_upload.zip` → 404; `curl https://wantuch.pk/spacebook/` returns the app; `api/health.php` → `"db":true`; `unzip -l` of a freshly built package shows no `config.php`.

**Acceptance criteria.** No secret reachable over HTTP or in any package; green deploy; app loads online; `git status` clean.

---

### Phase 1 — Safety net: baselines, repaired tests, tracing, CI gate

**Objective.** Make regressions visible before any refactor.

**Existing problems.** QA-01 (validate crashes, smoke 32 failures, no CI tests, outdated CONTRIBUTING.md); ARCH-01 (behaviour depends on script order and DOM observers); DATA-01 (unknown which data files are live).

**Affected files.** `tools/validate.js`, `tools/smoke.js`, `tools/ui_audit/audit_tabs.js`, `test_cls2_all_subjects.js`, `.github/workflows/deploy.yml`, new `tests/` folder, `package.json` (dev-only, for Playwright), `CONTRIBUTING.md`.

**Required changes.**
1. Baseline runner (Playwright, Chromium) that, for every class × subject × chapter × visible main tab, records: tab labels in order, DOM text hash of the content area, console errors, render time; screenshots at 1280×800 and 375×812 for the first, middle and last chapter of each subject. Output `tests/baseline/2026-10-xx/`.
2. Repair `tools/validate.js` and `tools/smoke.js`. For each failing assertion decide: real defect (fix the code/data via the correct pipeline) or stale expectation (update with a recorded reason). Known failures include `DATA.eng2Chapters = 12 -> got 16`, `load english_10_data.js`, Class 1/2 Maths, Class 2/3 Drawing, Class 12 English units, the crash at `validate.js:146`.
3. Global-access tracer (dev only): wraps each book global in a `Proxy`, opens every chapter/tab, writes `tests/trace/<subject>.json` (globals read, functions called).
4. CI: `test` job (validate + smoke + baseline subset of 1 chapter per subject) required by `deploy`.
5. Rewrite `CONTRIBUTING.md` to describe the real structure, generators, and the regression rule.

**Dependencies.** Phase 0.

**Safety precautions.** Test code only; no app behaviour change in this phase except genuine bug fixes approved by the owner. Playwright is a dev dependency, never shipped.

**Testing.** The suite itself runs green twice in a row (flake check); baseline reproducible (hash stability across two runs ≥ 99.5 %; list unstable chapters).

**Acceptance criteria.** validate 0 failures and no crash; smoke 0 failures; baseline stored and documented; CI blocks deploy on failure; trace files exist for all 115 subjects.

---

### Phase 2 — Server and synchronisation correctness

**Objective.** Durable, secure, idempotent synchronisation of user records; hardened auth; backups.

**Existing problems.** SYNC-01 (`js/sb_rewards.js` drops offline steps; demotes user to guest on errors); SYNC-02 (`js/sb_study_plan.js` never re-pushes offline edits; offline deletes resurrect; client clock vs server clock); SYNC-03 (`js/test_prep.js` guest data not merged; whole-record LWW; no `online` retry; unbounded sessions); SEC-02 (coin farming in `api/progress.php`); SEC-05 (no CSRF token, enumeration, per-number throttling only, no reset, no pruning, DDL on request path, verbose health); PRIV-01; BAK-01; S-01 (session lifetime).

**Affected files.** `api/*.php`, `api/schema.sql` → `api/migrations/*.sql`, new `api/v2/sync.php`, `api/lib/*.php`; `js/sb_rewards.js`, `js/sb_study_plan.js`, `js/test_prep.js`, `js/auth.js`; new `js/core/store.js`, `js/core/sync.js`.

**Required changes.**
1. Migrations folder + runner (CLI/CI only). New tables: `devices(id, user_id, token_hash, created_at, last_seen, revoked)`, `sync_events(user_id, event_id UNIQUE, device_id, type, payload JSON, client_ts, server_seq AUTO, received_at)`, `activity_catalog(activity_key PK, title, steps_total, coins_step, coins_complete)`, `audit_log`.
2. `POST /api/v2/sync` (batch ≤ 500 events, ≤ 1 MB): validates schema, user/device, idempotency; applies events to materialised tables (progress, plans, test prep) with server sequence; returns accepted ids + current server cursor. `GET /api/v2/sync?since=<seq>` for pulls.
3. Coins computed only from `activity_catalog`; unknown keys rejected; per-user rate limit.
4. Client outbox (`js/core/sync.js`): every user action → event in IndexedDB first → UI updates from local state → background sync on start/`online`/`visibilitychange`/interval with back-off. Never drop events; never switch user to guest because of a transient error.
5. Guest → account: on first sign-in, show "Add this device's progress to your account?"; on yes, re-tag local events with the user id and sync.
6. Auth: device tokens for sync (Authorization header), CSRF token for cookie endpoints, throttle by IP and account, generic messages, password change, reset (owner chooses the channel), prune attempts, consistent session lifetime, logout revokes device.
7. `health.php` → public `{"ok":true}`; detailed health behind a secret token.
8. Profile: view/edit, export JSON, delete account (soft delete + purge job).
9. Backups: cPanel cron `mysqldump` nightly to off-site storage; restore runbook tested once.
10. Keep v1 endpoints working until all clients use v2; then deprecate.

**Dependencies.** Phase 1 (tests). Coordinate the IndexedDB store with Phase 4.

**Safety precautions.** Migrate existing rows into the new model with a reversible migration; dump DB first. Never delete `activity_progress`, `study_plans`, `test_prep_*` rows during migration. Test on a copy of the live DB.

**Testing.** PHP CLI tests: idempotent re-send (same events twice → one effect); 1,000-event batch; unknown activity → 422; rate limit → 429; token revoked → 401; two devices offline then online → merged result deterministic. Browser tests: complete steps offline, reload, reconnect → exactly-once on server.

**Acceptance criteria.** Zero data loss and zero duplication in the scripted scenarios; coins cannot be raised by crafted requests; backups produced and one restore verified.

---

### Phase 3 — Content contract, manifest and lazy loading

**Objective.** Load only what the student opens; one way to get a book; regenerate derived files reliably.

**Existing problems.** PERF-01 (358 MB eager); ARCH-02 (`getSubjectChapterList` prefers stale `state.selectedClass` — reproduced: with `state.selectedClass='cls7'`, `getSubjectChapterList('eng','cls9')` returns `ENGLISH_7_DATA`); ARCH-03 (five contracts, `eval` lookups, 32 `has*` flags, 270-line `openSubject`); DATA-02 (stale `study_plan_index.js`); DATA-01 (superseded files).

**Affected files.** `index.html`, `js/data.js`, `js/app.js` (`openSubject` 1894, `getSubjectChapterList` 19207, all `typeof X !== 'undefined'` lookups), all readers, `js/test_prep.js`, `js/sb_study_plan.js`, `js/word_stats.js`, `js/universal_translate.js` (lexicon from book globals), search (`handleGlobalSearch`), papers (`getCurriculumQuestionsForCategory` 12014); new `tools/build/*.js`, `content/`.

**Required changes.**
1. JSON Schema for Contract v1 + validator.
2. Build-time adapters (Node, `vm` sandbox like `tools/word_stats/build_word_stats.js`) from each legacy contract to v1; keep a per-book adapter report (counts of units/lessons/blocks/questions before vs after — must match).
3. Manifest + search index + MCQ bank + study index + word stats generated by one command `node tools/build/all.js`; CI fails when outputs are stale.
4. `SB.content.getBook()` loader; registry-driven `openSubject` (data, not if-chains); remove reliance on `state` inside data lookups.
5. Migrate consumers one at a time; after each, compare with the Phase 1 baseline.
6. Remove eager `<script>` tags for a book only after that book's parity passes; keep the legacy file in the repo until P10.
7. Server: enable gzip/brotli and long-cache headers for hashed packages (`.htaccess` / LiteSpeed).

**Dependencies.** Phase 1.

**Safety precautions.** Adapters never modify legacy files. Parity = identical rendered text per chapter/tab (whitespace-normalised) unless an intended fix is listed. Migrate in this order: Classes 1–8 rebuilt books (`CLSn_BOOKS`, most uniform) → Class 9/10 → Class 11 → Class 12; one subject per commit.

**Testing.** Adapter counts; schema validation for every book; baseline parity per subject; ARCH-02 matrix test (every class × subject × every `state.selectedClass` → same book); load metrics.

**Acceptance criteria.** Initial JS transfer ≤ 3 MB compressed; DOMContentLoaded ≤ 2 s on desktop local; heap after home ≤ 80 MB; all subjects parity-green; no `eval` in content lookup; derived files always current.

---

### Phase 4 — Offline-first

**Objective.** Every educational feature works with no network; installable app; durable local data.

**Existing problems.** OFF-01 (no SW/manifest/IndexedDB; Google Fonts link; Urdu/Pashto fonts not bundled; online TTS and translation); PERF-01.

**Affected files.** New `sw.js`, `manifest.webmanifest`, `icons/`, `fonts/`, `js/core/store.js`, `js/core/offline.js`; `index.html` (remove `fonts.googleapis.com`), `css/*.css` (font stacks), `js/app.js` TTS (`translate.google.com/translate_tts` at ~4184), `js/universal_translate.js`, `js/sb_four_lang.js`, `js/word_stats.js`.

**Required changes.**
1. Service worker: versioned precache of shell (HTML, CSS, core JS, KaTeX, fonts, icons); runtime cache-first for hashed content packages; network-first for API with outbox fallback; offline page.
2. "Download for offline" per class/subject with size and progress; verify sha256; store; show offline badge; `navigator.storage.persist()`; storage-quota UI with safe eviction (never the outbox).
3. Bundle WOFF2 fonts with open licences (Noto Nastaliq Urdu, Noto Naskh Arabic, Noto Sans); subset if needed.
4. TTS: Web Speech API voices only; hide the button when no voice for that language exists.
5. All translation/meaning features read local stores (Phase 7 completes coverage).
6. Update flow: manifest version change → prompt → delta download.

**Dependencies.** Phase 3 (packages), Phase 2 (outbox).

**Safety precautions.** Version every cache; on SW update never delete the outbox store; test update from the previous version with pending events.

**Testing.** Playwright with `context.setOffline(true)` after install: open every subject/chapter/tab (sample) incl. images, diagrams, meanings, sentence translations, test prep, study plan, paper generation, question banks, progress; then go online and check the outbox drains. Lighthouse PWA audit. Storage-full simulation.

**Acceptance criteria.** All listed modules usable offline; zero third-party requests during normal use; outbox survives reload, SW update and quota pressure; installable on Android Chrome.

---

### Phase 5 — Rendering core: hooks instead of patches (regression root fix)

**Objective.** Make behaviour explicit and scoped so one subject's change cannot break another.

**Existing problems.** ARCH-01: wrappers of `switchSubjectTab` (≥14), `openSubject` (7), `getSubjectChapterList` (6), `typesetChapterMath` (5), plus `goToSubjects`, `renderTestsPreps`, `switchMathTab`, `selectSubjectChapter`, `openSubjectWorkspace`, `renderSubjectChapterView`; document-wide `MutationObserver`s in `app.js:15308`, `reader_tools.js:128`, `sb_four_lang.js:44`, `sb_global_ui.js:105`, `sb_mcq.js:504`, `sb_medium.js:315`, `sb_rtl.js:58`, `sb_structure.js:295,395`, `sb_topic_practice.js:351`, `sb_trace.js:322`, `sb_trilingual.js:379`, `sb_vertical.js:123`, `structure_harmonizer.js:424`, `word_stats.js:690`; 22 injected `<style>` blocks; ≈ 230 `!important` (180 in `style.css`, 46 in `sb_theme.css`); language/direction guessed from text. PERF-02 (whole chapter rendered; `sb_structure.js` renders every tab to compare). SEC-06 (`eval`, 416 inline `onclick`). UX-01.

**Affected files.** `js/app.js`, all readers (`cls1..6_book_reader.js`, `cls2_page_reader.js`, `math5/6/7/8/11_reader.js`, `math12_*`, `lesson_math_reader.js`, `biology_10_reader.js`, `english_10_reader.js`), `class11_study_views.js`, `class12_study_views.js`, `class12_exercise_banks.js`, all `sb_*.js`, `structure_harmonizer.js`, `reader_tools.js`, `continue_learning.js`, `word_stats.js`, `test_prep.js`, `css/*.css`.

**Required changes.**
1. Add `js/core/hooks.js` and a render pipeline `SB.render(ctx)`; `ctx` carries `classId, subjectId, book, unitIdx, tab, medium, dir`.
2. Convert each wrapper into a hook registration, one module per commit, in this order: readers → `sb_structure` (move its tab-dedup logic to build time) → `sb_medium`/`sb_rtl`/`sb_solve` (read `medium/dir/langs` from the manifest) → `sb_trilingual`/`sb_four_lang`/`structure_harmonizer` (one sentence-drawer component) → `sb_topic_practice` → `sb_mcq` → `sb_book_skin`/`sb_trace`/`sb_vertical` → `word_stats` → `continue_learning`/`reader_tools` → `test_prep`.
3. Delete each module's `MutationObserver` once its hook works. Post-processing runs once per render on the container it owns.
4. CSS: per-component files with a root class; move injected CSS into files; scope subject themes under `[data-subject=…]`; reduce `!important` below 20.
5. Replace `eval` and inline handlers with registry lookups and delegated `data-action` handlers.
6. Render only the active tab; lazy-render long lists.
7. Set `<html lang dir>` (or the reader root) from the open book.

**Dependencies.** Phases 1 and 3.

**Safety precautions.** This is the riskiest phase. Feature flag `SB.flags.coreRender` per subject; legacy path remains until parity. Full snapshot suite after every commit. Never change data here.

**Testing.** Full baseline parity; observer count via `PerformanceObserver`/instrumentation = 0 document-wide; CSP report-only run shows zero violations from inline scripts/eval; chapter-open timing.

**Acceptance criteria.** All subjects parity-green on the new core; no global function is wrapped by another file; zero document-wide observers; zero `eval`; chapter open p95 ≤ 300 ms desktop.

---

### Phase 6 — Intelligent tab structure and content integrity

**Objective.** Every chapter shows the right tabs in the right order with only real, sourced content.

**Existing problems.** TAB-01 (Board SLO tab absent in Class 11/12 and most Urdu/Arabic-medium books; Summary missing in many; Word Stats position varies; duplicate "Lessons"/"Lesson text"; three Math numbering styles); CONT-01 (Class 9 Math: 320 of 324 "Board SLO" MCQs are 5 templates × 64 topics, all keyed to option A; hard-coded MCQs in `app.js:14189` and `app.js:18013`; "Cayley … 1860" needs checking); CONT-02 (`app.js:12014` reads `correctIndex/ans`, bank uses `correct` → paper key 0); CONT-03 (same 3 MP4s for every chapter, placeholder YouTube ID `dQw4w9WgXcQ` in `renderIslVideo`, fake "1080p lecture" card); MCQ-01; PDF-01.

**Affected files.** `js/app.js` (`getTopicSpecificSLOs`, `getComprehensiveChapterSLOBank`, `getCurriculumQuestionsForCategory`, `renderEngVideo`, `renderClass9EnglishVideoTabs`, `renderIslVideo`, math video card, PDF map), tab plan module (new `js/core/tabs.js`), `js/word_stats.js`, `js/sb_topic_practice.js`, `js/sb_mcq.js`, `tools/test_prep/build_mcq_bank.js`, content adapters.

**Required changes.**
1. `tabs:plan` hook builds tabs from the v1 book: `Lessons` (horizontal nested sub-tabs: Topics / Activities / Examples, in book order) → `Exercises` → `Summary` → `Board SLO` (sub-tabs MCQs / SQs / LQs) → `Word Stats`. Hide empty tabs. Labels from the medium dictionary (`en/ur/ps/ar`). Horizontal, scrollable, responsive at 375 px.
2. Board SLO content only from verified sources (textbook exercises tagged with SLO codes, past board papers with year, teacher-entered with review). Load the official KPK SLO list when the owner provides it; until then label as "Textbook practice", not "Board".
3. Remove templated/generated questions from student-facing paths; keep them nowhere in shipped data.
4. One MCQ normaliser used by chapters, Test Prep and Papers; Papers print keys only for `verified` items with `answerIndex != null`.
5. Remove placeholder media; video tab only for real per-chapter videos available offline.
6. PDF buttons only for licensed, packaged PDFs.
7. Content lints in CI (repeated stems across chapters, ≥ 80 % same key index in a bank, missing keys, duplicate stems).

**Dependencies.** Phase 5 (hooks), Phase 3 (contract).

**Safety precautions.** Removing questions changes what students see — produce a list of removed items per subject for owner approval before merging. Never "repair" a key by guessing; mark `answerIndex:null` and queue for review.

**Testing.** Tab audit over every chapter (extend `tools/ui_audit/audit_tabs.js`) asserting order/labels/visibility rules; content lints; Papers answer-key test.

**Acceptance criteria.** 100 % of chapters follow the tab model; zero templated or placeholder items reachable; every printed key traceable to a source; owner sign-off on removal lists.

---

### Phase 7 — Multilingual engine (four languages, offline)

**Objective.** Hover/long-press on a word in any of the four languages shows its meaning in the other three; clicking a sentence shows its translation in the other three; all offline, with provenance.

**Existing problems.** ML-01 (offline lexicon 1,260 rows; `ENG_URDU_DICT` 6,497 entries with 0 Arabic and 378 placeholders; paragraph translation offline falls back to word-by-word; Arabic sentence lines fetched online; legacy English-only hover tooltip; slot quirk); SEC-04 (Google gtx, MyMemory, Google TTS endpoints).

**Affected files.** `js/universal_translate.js`, `js/offline_lexicon.js`, `js/dictionary_data.js`, `js/sb_trilingual.js`, `js/sb_four_lang.js`, `js/structure_harmonizer.js`, `js/app.js` (`showWordHoverTooltip` 18873, `fetchOnlineWordTranslation` 13618, `showWordLookupPopover`), `js/word_stats.js` (Google batch), new `tools/build/lexicon.js`, `content/lexicon/*`.

**Required changes.**
1. Build Lexicon v1 from: book glossaries/vocabulary tables, `ENG_URDU_DICT` (drop placeholders), `SB_OFFLINE_LEXICON`, per-book word lists, reviewed additions. Index per language with normalisation; lemma/form lookup (English inflections, Urdu/Pashto common suffixes).
2. Coverage report per book and per language pair; export review queues (CSV) for missing Arabic/Pashto meanings. Machine suggestions may pre-fill the queue **only** with `src:"machine", reviewed:false` and must be labelled in the UI.
3. Sentence store from book translations (`tr` in Contract v1); fill gaps through the review queue; never display machine text as book text.
4. One interaction component (replace legacy tooltip/popover paths): desktop hover with 250 ms delay, touch long-press, keyboard focus; card shows the other three languages, each line with its language name, RTL/LTR correct; Qur'anic text excluded.
5. Remove direct calls to third-party MT/TTS. Optional online fallback only through an owner-approved server proxy, disabled by default.

**Dependencies.** Phases 3 and 4; content review capacity (owner).

**Safety precautions.** Lexicon edits are data changes → reviewed diffs. Keep Qur'anic detection (`SBTranslate.isQuranic`) behaviour.

**Testing.** Offline lookup tests for samples in each language; coverage thresholds per book; RTL rendering screenshots; network log shows no third-party calls.

**Acceptance criteria.** Every word in every downloaded book returns either reviewed meanings in all three other languages or an explicit "meaning not yet available" state; targets (owner to confirm): ≥ 95 % token coverage EN↔UR↔PS, ≥ 85 % for Arabic in Phase 7, rising with review; lookup ≤ 30 ms offline.

---

### Phase 8 — Licensing, integrity, secure updates and CSP

**Objective.** Make unauthorised copying and tampering harder, detect tampering, and harden the web surface — honestly.

**Existing problems.** SEC-03 (public repo with all transcriptions; content served as plain JS); SEC-06; no integrity checks; deploy over FTPS with `security: loose`.

**Affected files.** `tools/build/*` (sign, encrypt), `js/core/content.js`, `js/core/license.js`, `api/v2/license.php`, `.htaccess`, `.github/workflows/deploy.yml`.

**Required changes.**
1. Sign `manifest.json` (Ed25519; private key only in CI secret); client verifies signature and each package sha256 before use.
2. Device activation and per-device package keys (AES-GCM); packages encrypted at rest; licence check offline with expiry and periodic online renewal; revocation list.
3. Watermark (account id) in rendered pages and prints.
4. Security headers: CSP `default-src 'self'; script-src 'self'; object-src 'none'; frame-ancestors 'none'`, HSTS, `X-Content-Type-Options: nosniff`, `Referrer-Policy: same-origin`.
5. Deploy only from CI with strict TLS, atomic releases and checksum verification.
6. Document clearly for the owner what this does and does not prevent.

**Dependencies.** Phases 3, 4, 5.

**Safety precautions.** Keys never in the repo or front end; test key rotation; never lock a student out of already-downloaded content without a grace period.

**Testing.** Tampered package rejected; expired licence handled; header scan; CSP enforcement with zero violations.

**Acceptance criteria.** Signature verification on every package load; CSP enforced; documented threat model accepted by the owner.

---

### Phase 9 — Modules: Papers, Test Prep, Study Plan, Statistics, Profiles, Administration

**Objective.** Complete, consistent, offline-capable modules built on the shared components.

**Existing problems.** CONT-02; MCQ-01 (answer-index skew, 51 duplicate stems, Class 11 has 0 bank MCQs); DATA-02; ADMIN-01 (`user_type` unused, no admin); PRIV-01; reminders only while the page is open.

**Affected files.** `js/app.js` papers section (≈10122–13330), `js/test_prep.js`, `js/sb_study_plan.js`, `js/word_stats.js`, `js/sb_rewards.js`, `js/auth.js`, `api/v2/*`, new `admin/` (server-rendered, role-checked).

**Required changes.**
- **Papers:** normalised questions with provenance; blueprint validation (marks, counts vs available); version A/B shuffles preserving keys; print/PDF offline; answer keys only for verified items.
- **Test Prep:** event sync; guest merge; review queue for skewed/duplicate items; Class 11 MCQs only from verified keys.
- **Study Plan:** built from the manifest; offline; event sync; honest reminder behaviour.
- **Statistics:** computed locally from events; synced summaries; dashboard per subject/class.
- **Profiles:** edit, export, delete.
- **Admin:** role checks server-side; user block/unblock; sync error view; content version status; audit log.

**Dependencies.** Phases 2, 6.

**Safety precautions.** No change to question content here; only presentation and plumbing.

**Testing.** Module-level Playwright flows online and offline; API tests for roles.

**Acceptance criteria.** Each module passes its offline and online flows; no unverified key printed; admin actions logged.

---

### Phase 10 — Cleanup and archive

**Objective.** Shrink the working folder and the deployed payload without losing anything.

**Existing problems.** See Appendix B: ≈ 6.7 GB safe-to-archive scratch in `SpaceBook Web`; ≈ 35–40 MB deployed-but-unused files; 64 MB git garbage; stray `kotlin/`, progress JSONs, `js/math_12_book_data.js`, `js/unkeyed.json`.

**Required changes.** Follow Appendix B exactly: backup → log with sizes and SHA-256 → move (never delete) to `D:\SpaceBook\SpaceBook_Archive\` → full tests → commit tracked moves separately. Superseded data files only after Phase 1 traces prove zero reads and Phase 3 parity passes. `git gc --prune=now` only after a `.git` backup.

**Acceptance criteria.** Archive log complete; tests green; reported active-folder size, production payload size, and actual disk freed (three separate numbers).

---

### Phase 11 — Performance and low-end devices

**Objective.** Fast on a 2 GB-RAM Android phone.

**Budgets.** Initial transfer ≤ 3 MB compressed; heap ≤ 150 MB while reading; TTI ≤ 4 s cold / ≤ 1.5 s warm on the reference device; chapter open p95 ≤ 1.5 s low-end, ≤ 300 ms desktop; tab switch ≤ 600 ms / ≤ 150 ms; word lookup ≤ 30 ms; search ≤ 100 ms offline.

**Required changes.** Active-tab rendering, list virtualisation, image `srcset`/WebP, KaTeX pre-rendering at build time where possible, search index sharding, avoid layout thrash.

**Testing.** Lighthouse mobile; Chrome CPU ×6 throttling profile; real-device run if available.

**Acceptance criteria.** All budgets met or documented with reasons and owner sign-off.

---

### Phase 12 — Accessibility, search, documentation, handover

**Required changes.** ARIA tablists with arrow keys; real buttons; focus traps in modals; AA contrast; root `lang/dir`; offline full-text search with Urdu/Pashto/Arabic normalisation; accurate architecture, data-contract, release and rollback docs; updated protect-list.

**Acceptance criteria.** axe-core: zero serious/critical issues on sampled pages; search works offline across downloaded books; docs reviewed by the owner.

---

## 7. Automated testing requirements (summary)

| Layer | Tool | When |
|---|---|---|
| Data contract validation (schema, counts, provenance, keys) | Node | every commit |
| Content lints (templates, skew, duplicates, placeholders) | Node | every commit |
| Unit tests (loader, lexicon, MCQ normaliser, tab planner, sync reducer) | Node test runner | every commit |
| API tests (auth, sync idempotency, limits, roles) | PHP CLI | every commit touching `api/` |
| Snapshot parity per subject (DOM text + tabs + screenshots) | Playwright | shared-file changes: full; otherwise scoped |
| Offline acceptance (airplane mode) | Playwright `setOffline` | each phase from P4 |
| Performance budgets | Lighthouse CI + custom timings | P3 onward, nightly |
| Accessibility | axe-core | P12 onward |

## 8. Progress reporting format (use every time)

```
## <date> — <phase/task>
Done: …
Files: …
Verified by: <command> → <result numbers> ; screenshots: <paths>
Not verified: …
Regressions found/fixed: …
Risks / owner decisions needed: …
Next: …
```
Never write "complete", "done" or "fixed" for anything that lacks a "Verified by" line.

## 9. Owner decisions to request (do not guess)
1. Server actions in Phase 0 (delete zip, rotate password, disable listing) — approval and who performs them.
2. Repository visibility / content split.
3. Password-reset channel (WhatsApp OTP provider vs admin-assisted).
4. Source of official KPK Board SLO lists and past papers.
5. Licensing model (free/paid, devices per account, offline grace period).
6. Translation targets and who reviews Arabic and Pashto meanings.
7. Approval of each "removed items" list in Phase 6.
8. Which archived folders may eventually be deleted (never by the agent).

---

## Appendix A — Finding reference (evidence summary)

| ID | Severity | Problem | Where | Evidence |
|---|---|---|---|---|
| SEC-01 | Critical | Live DB password publicly downloadable | server `public_html/spacebook/spacebook_upload.zip`; `tools/build_upload_zip.py` | directory listing shows the 117,161,854-byte zip; local copy contains `api/config.php` with a real 13-char password |
| DEP-01 | Critical | Live app not served; deploys failing | `.github/workflows/deploy.yml` | `/spacebook/index.html` → 404; last 5 Actions runs `failure`; local `main` ahead 2 + 5 uncommitted files + 83 untracked covers |
| PERF-01 | Critical | 250 scripts / 358 MB loaded at startup | `index.html` | DOMContentLoaded 17.4 s, heap 698 MB (desktop, local) |
| ARCH-01 | Critical | Regressions caused by global wrappers + page-wide DOM rewriters | `app.js`, readers, `sb_*.js`, `structure_harmonizer.js`, `word_stats.js`, `continue_learning.js`, `reader_tools.js` | `switchSubjectTab` wrapped ≥14×, `openSubject` 7×, `getSubjectChapterList` 6×; 14+ `MutationObserver`s on `document.body`; 22 injected `<style>`; ≈230 `!important`; language/direction guessed from text |
| ARCH-02 | High | Chapter lookup uses stale `state.selectedClass` | `app.js:19207` and similar `classId===X \|\| state.selectedClass===X` code | reproduced: `state.selectedClass='cls7'` → `getSubjectChapterList('eng','cls9') === ENGLISH_7_DATA` |
| ARCH-03 | High | Five content contracts; copy-paste renderers; `eval` lookups | `app.js` render families, `openSubject` if-chain (32 `has*` flags), `class11_study_views.js:31,33`, `class12_exercise_banks.js:7` | code reading |
| CONT-01 | High | Generated "Board SLO" MCQs | `app.js:14189` `getTopicSpecificSLOs`, `app.js:18013` | Class 9 Maths: 320 of 324 MCQs = 5 templates × 64 topics, all keyed to option A; also "Cayley … 1860" claim to check |
| CONT-02 | High | Papers answer key reads wrong field | `app.js:12014` | reads `correctIndex/ans`, bank uses `correct` → key defaults to 0 |
| CONT-03 | High | Placeholder media | `app.js:4611`, `:19945`, `:8978`, ~`:14738` | same 3 MP4s for every chapter; placeholder YouTube id `dQw4w9WgXcQ`; fake "1080p lecture" card |
| SYNC-01 | High | Rewards lost offline when signed in | `js/sb_rewards.js` `step()` | network error → `{ok:false, earned:0}` not queued; server error → user demoted to guest |
| SYNC-02 | High | Study-plan offline edits never pushed; deletes resurrect | `js/sb_study_plan.js` `persist`, `syncWithAccount`, delete | only plans missing on server are pushed; delete not retried; client vs server clocks |
| SYNC-03 | Med-High | Test-prep guest data orphaned; whole-record LWW; no retry | `js/test_prep.js:134,174,186`, `api/test_prep.php` | separate `sbTP:v1:guest` key; no `online` listener anywhere |
| SEC-02 | Medium | Coins can be farmed | `api/progress.php` | client chooses activity key and total (≤200); `sync` takes 500 items |
| SEC-03 | High | Copyright/redistribution | public GitHub repo; plain-JS content; KPTBB PDF links | repo `visibility: public` |
| SEC-04 | High | Selections sent to unofficial third parties | `universal_translate.js:92,105`, `word_stats.js:222`, `app.js:13620`, `app.js:4184` | Google gtx, MyMemory, Google TTS |
| SEC-05 | Medium | Auth gaps | `api/auth.php`, `session.php`, `db.php`, `health.php` | no CSRF token; enumeration; per-number throttle only; no reset; DDL on requests; health leaks PHP version/tables |
| SEC-06 | Medium | CSP impossible today | `eval` (3 files), 416 inline `onclick` in `app.js` | code |
| OFF-01 | High | No offline support | whole app | no service worker, manifest, IndexedDB; Google Fonts link; fonts not bundled |
| ML-01 | High | Four-language meanings partial and online-dependent | `universal_translate.js`, `offline_lexicon.js` (1,260 rows), `dictionary_data.js` (6,497 entries, 0 Arabic, 378 placeholders), `sb_four_lang.js`, `app.js:18873` | offline sample: EN 52/60, UR 25/30, PS 15/15; sentences offline = word-by-word; Arabic sentences online |
| TAB-01 | High | Tabs inconsistent | renderers, `sb_structure.js`, class 11/12 views, `word_stats.js` | no Board SLO tab in sampled Class 11/12 books and most Urdu/Arabic-medium books; Summary often missing; Word Stats position varies; duplicate "Lessons"/"Lesson text" |
| QA-01 | High | Test gates broken, not in CI | `tools/validate.js`, `tools/smoke.js` | validate: 10 failures then crash at line 146; smoke: 32 failures |
| DATA-01 | Medium | Possibly superseded data still loaded | `math_1_data.js`, `math_3_book_text.js`, `english_1/islamyat_1/nazira_1/pashto_1/drawing_1_data.js`, `general_science_9_data.js`, `pakstudy_data.js`, `english_data.js`, `data_bio.js`, `math_12_book_data.js` | static analysis only — prove with tracing before removing |
| DATA-02 | Medium | Generated index stale | `js/study_plan_index.js` | older than 15 data files |
| PERF-02 | Med-High | Slow subject open | renderers + `sb_structure.js` | Class 12 Physics 5.2 s, Class 9 Urdu 3.2 s, Class 12 Statistics 3.1 s, Class 12 Chemistry 21,869 DOM nodes |
| MCQ-01 | Medium | MCQ bank quality signals | `js/test_prep_bank.js` | key index 1 = 38 %; 51 duplicate stems; Class 11 = 0 MCQs |
| PDF-01 | Medium | PDF buttons point outside the deployed site | `app.js` PDF map (`Books/<n>th/...`) | not in deploy set |
| UX-01 | Medium | Accessibility/lang semantics | `index.html`, `app.js` | fixed `lang="en"`, no root `dir`, 92 clickable divs, 4 `role="tab"` |
| ADMIN-01 / PRIV-01 / BAK-01 | Medium | No admin/roles; no profile edit/export/delete; no automated backups | `api/` | `user_type` never checked |
| MAINT-01 | Low-Med | Repo hygiene | `.git` 1.3 GB (64 MB garbage), 2,507 one-off `.py` in `tools/`, stray `kotlin/` | — |

**Suspected (confirm before acting):** S-01 sessions may expire after ~24 min idle (PHP `gc_maxlifetime`); S-02 deploy fails on FTP size/timeout; S-03 `sb_structure.js` may hide legitimate tabs; S-04 answer-key skew may reveal generated MCQs; S-05 `assets/biology12/` and `assets/physics12/` may be unused; S-06 superseded data files never read; S-07 `chemistry_10_source_data.js` overlay marks a completed book "in-progress"; S-08 search will miss books once loading is lazy.

---

## Appendix B — Cleanup quick reference (Phase 10)

Never delete. **Move** to `D:\SpaceBook\SpaceBook_Archive\<same relative path>` with a log (path, size, SHA-256), after a full backup, then run all tests.

| Group | Size | Verdict |
|---|---|---|
| `SpaceBook Web/tmp/` image renders | ≈ 6.3 GB | safe |
| `tmp/` scripts (`*.py`, `*.cjs`, `*.js`) | < 10 MB | archive as a block with a list (some were pipeline helpers) |
| `tools/source-review/` | 282 MB | safe |
| `tools/*.png|*.jpg` (root), `tools/10th_Maths_*_aux.txt`, `tools/__pycache__/` | 27 MB | safe |
| `cover-replacement-staging/` | 58 MB | safe after committing `covers/Books/*/kptb_*.webp` |
| `backup/` | 2.8 MB | safe |
| root `doc1_p3.png` (duplicate of `urdu_p3.png`), `doc2_p1.png`, `urdu_p3..p7.png` | 23 MB | safe |
| `kotlin/`, `exercise-pages.json`, `biology-progress.json`, `docs/*-progress.json` | < 0.1 MB | safe |
| `js/math_12_book_data.js` (not loaded), `js/unkeyed.json` (tool output → `tools/test_prep/`) | 11 KB | safe |
| 114 unreferenced cover images (keep `covers/Books/12th/HPE.jpg`, `covers/History.jpg`) | 28.6 MB | verify with a 404 check first |
| `assets/biology12/`, `assets/physics12/`, `assets/math9-agent1/`, `assets/physics9-agent1/` | 5.7 MB | verify with a network log first |
| Superseded data files (DATA-01) | ≈ 5.4 MB | only after tracing shows zero reads and parity passes |
| Git garbage | 64 MB | `git gc --prune=now` only after backing up `.git` |
| `docs/source-verification/**` tracked files, any `js/*_data.js|*_book.js`, `api/config.php` | — | **never archive** |

Report three separate numbers at the end: active-folder size, production payload size, actual disk freed. (Today: folder 8.0 GB; production ≈ 425 MB uncompressed / 117 MB zipped; startup load 358 MB.)
