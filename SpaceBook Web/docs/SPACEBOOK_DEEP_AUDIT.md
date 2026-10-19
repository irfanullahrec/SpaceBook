# SpaceBook — Deep Technical Audit

**Date:** 2026-10-19  ·  **Scope:** `D:\SpaceBook\SpaceBook Web` (plus the live deployment at `https://wantuch.pk/spacebook/`, the GitHub repository, and the sibling folders under `D:\SpaceBook` where they affect the web app)
**Method:** static reading of the source, Node-based checks of the data files, the project's own test scripts, and a live run of the app in the in-app browser (PHP built-in server on port 8790). Read-only HTTP requests to the live site and the public GitHub API.
**Nothing in the application was modified.** Only the four `docs/SPACEBOOK_*.md` files were created.

Companion documents:
- `docs/SPACEBOOK_CLEANUP_REPORT.md` — unnecessary files, sizes, archive plan
- `docs/SPACEBOOK_IMPLEMENTATION_ROADMAP.md` — ordered tasks, dependencies, verification
- `docs/SPACEBOOK_ULTIMATE_MASTER_PROMPT.md` — the implementation directive for a coding agent

---

## 0. Act first: live credential exposure (CRITICAL)

| | |
|---|---|
| **Problem** | `https://wantuch.pk/spacebook/` shows a public **directory listing** whose only entry is `spacebook_upload.zip` (117,161,854 bytes, uploaded 2026-10-19 06:44). Anyone can download it. The local copy of that zip, `D:\SpaceBook\deploy\spacebook_upload.zip` (same byte size), contains `api/config.php` with the **live database password** (13 characters, not a placeholder). |
| **Evidence** | `curl https://wantuch.pk/spacebook/` → "Index of /spacebook/" listing `spacebook_upload.zip`. `curl -I …/spacebook_upload.zip` → `200 OK`, `Content-Length: 117161854`. `unzip -l` of the local zip lists `api/config.php`; parsing it with PHP shows a non-placeholder `db_pass`. The live zip itself was **not** downloaded during this audit. |
| **Root cause** | `tools/build_upload_zip.py` writes the live credentials into the zip on purpose ("api/config.php inside it points at the live database"), the zip was uploaded to the public web root and not extracted/deleted, and LiteSpeed autoindex is on for `/spacebook/`. The script comment also says the local XAMPP password is the same as the live one. |
| **Severity** | Critical |
| **Immediate actions (owner: you, on the server — an agent must not do these without your explicit go-ahead)** | 1) Delete `public_html/spacebook/spacebook_upload.zip` from the server. 2) Change the password of MySQL user `tafseelk_spacebook` in cPanel, update the `DB_PASSWORD` GitHub secret, and use a **different** password locally. 3) Turn off directory listing for `public_html/spacebook` (`Options -Indexes` in an `.htaccess` there). 4) Check the cPanel raw access log for downloads of the zip and for logins to phpMyAdmin/MySQL since 2026-10-19 06:44. 5) Stop putting secrets inside upload packages (see roadmap task P0-2). |
| **Verification** | `curl -I https://wantuch.pk/spacebook/spacebook_upload.zip` → 404; `curl https://wantuch.pk/spacebook/` no longer lists files; `api/health.php` still reports `"db":true` with the new password. |

Related deployment state (also confirmed): the app is **not live** — `https://wantuch.pk/spacebook/index.html` returns 404, and the last five GitHub Actions "Deploy SpaceBook" runs (2026-10-19 04:44–05:07 UTC) all ended in `failure`. Local `main` is 2 commits ahead of `origin/main` and has uncommitted edits in 5 files (`css/style.css`, `index.html`, `js/app.js`, `js/sb_topic_practice.js`, `js/test_prep.js`).

---

## 1. Executive summary

SpaceBook is a large, content-rich, **dependency-free vanilla-JS single page** (`index.html` + `js/app.js` + ~250 script files) with a **small PHP/MySQL API** for accounts and student records. The educational content (Classes 1–12, KPTBB textbooks) is extensive and much of it has been source-verified page by page. The architecture around that content is the problem:

1. **Everything loads at once.** `index.html` has 250 synchronous `<script>` tags totalling **358 MB**. Measured locally: DOMContentLoaded at **17.4 s**, JS heap **698 MB** after load. This alone rules out offline use and low-end phones.
2. **Behaviour is built by layering patches.** Core functions are re-wrapped by many later files (`switchSubjectTab` ≥14 wrappers, `openSubject` 7, `getSubjectChapterList` 6), and **at least 14 `MutationObserver`s** watch the whole document and rewrite the rendered HTML (direction, labels, tabs, translations, collapsing, MCQ widgets…). Order of `<script>` tags decides the final behaviour. This is the main, confirmed root cause of "finishing one subject breaks another".
3. **There is no offline layer** — no service worker, no manifest, no IndexedDB. Translation, TTS, fonts and videos call third-party services.
4. **Student data sync is fragile.** Several confirmed paths lose or resurrect data (rewards earned offline while signed in are dropped; offline study-plan edits never upload; offline deletes come back; guest test-prep history is never merged into the account).
5. **Some "board" content is generated, not sourced.** Class 9 Mathematics "Board SLO" MCQs are mostly five generic templates repeated across 64 topics with every answer keyed to option A, and they feed the Papers generator.
6. **Security basics are missing** beyond the live credential exposure: client-decided reward coins can be farmed, selections are sent to unofficial Google/MyMemory endpoints, the public GitHub repository carries the full textbook transcriptions, and the front end needs `eval` and 400+ inline handlers (so no Content-Security-Policy is possible today).
7. **The existing test gates are broken** (`tools/validate.js` crashes after 10 failures; `tools/smoke.js` has 32 failures) and are not run in CI.

What is **good** and must be protected: the verified book data files (`*_data.js`, `*_book.js`, Class 12 exercise banks), the per-class book pipelines under `docs/source-verification/`, the server-side password hashing and prepared statements, the test-prep merge logic, the Qur'anic-text protection in the translator, vendored KaTeX, and the generator tools (`tools/test_prep`, `tools/study_plan`, `tools/word_stats`).

### Severity counts (confirmed findings only)

| Severity | Count |
|---|---|
| Critical | 4 (SEC-01, DEP-01, PERF-01, ARCH-01) |
| High | 13 (ARCH-02, ARCH-03, CONT-01, CONT-02, CONT-03, SYNC-01, SYNC-02, SEC-03, SEC-04, OFF-01, ML-01, TAB-01, QA-01) |
| Medium / Medium-High | 13 (SYNC-03, SEC-02, SEC-05, SEC-06, DATA-01, DATA-02, PERF-02, MCQ-01, PDF-01, UX-01, ADMIN-01, PRIV-01, BAK-01) |
| Low-Medium | 1 (MAINT-01) |
| Suspected (unconfirmed) | 8 (S-01 … S-08) |

---

## 2. What was inspected (and what was not)

**Inspected**
- Folder tree and sizes of `SpaceBook Web` (8.0 GB on disk) and the sibling folders in `D:\SpaceBook`.
- `index.html` script wiring (250 scripts, every one resolved to a file — no 404s).
- `js/app.js` (23,456 lines, 1.4 MB, 395 top-level functions) — routing, renderers, search, papers, word hover, TTS.
- All non-data modules: `sb_*.js`, `structure_harmonizer.js`, `universal_translate.js`, `test_prep.js`, `sb_study_plan.js`, `sb_rewards.js`, `auth.js`, `word_stats.js`, `continue_learning.js`, `reader_tools.js`, the `cls*_book_reader.js` / `math*_reader.js` readers, `class11_study_views.js`, `class12_*`.
- Data files: global names, contracts, overlays, solution stores (`CLS6_SOLUTIONS`: 19,910 keys, 0 collisions), dictionary/lexicon coverage, MCQ bank (6,120 MCQs).
- `api/*.php`, `api/schema.sql`, `api/.htaccess`, `.github/workflows/deploy.yml`, `tools/build_upload_zip.py`.
- CSS: 11 files, 9,503 lines; `!important` counts; injected `<style>` blocks.
- Tests: `tools/validate.js`, `tools/smoke.js`, `tools/ui_audit/audit_tabs.js`, `test_cls2_all_subjects.js`.
- Runtime: load metrics, subject-open timings for all 115 subjects, tab survey, stale-state reproduction, papers answer-key check, offline translation coverage sample, search timing, storage estimate.
- Live site (read-only `curl`) and GitHub repository metadata/Actions runs (public API).

**Not inspected / limitations**
- **MySQL was not running locally** (`api/auth.php?action=me` → 500), so the PHP endpoints were reviewed by reading code only; abuse scenarios (coin farming, record overwrite) are confirmed by code paths, not exercised against a database.
- The 2,507 one-off Python scripts in `tools/` and the per-class pipeline scripts in `docs/source-verification/` were inventoried, not read one by one. Their outputs (the data files) were inspected instead.
- Textbook accuracy was **not** re-verified against the scans (that is the job of the existing per-book pipelines). Content findings below are limited to provable structural problems (templated questions, wrong keys, placeholders).
- Mobile devices were not tested on hardware; low-end performance is extrapolated from desktop measurements.
- Tab survey opened the first chapter of every subject plus a middle chapter of 20 subjects; it records main tabs only, not every sub-tab.

---

## 3. Architecture as found

### 3.1 Runtime
- **Shell:** `index.html` → global CSS (11 files) → 250 `<script>` tags in a fixed order: `js/data.js` (registry: classes, subjects, books), ~170 book data files, `js/app.js` (controller), then ~60 add-on modules that wrap/patch `app.js` and post-process the DOM.
- **State:** one global `state` object in `app.js` (`selectedClass`, `activeSubject`, `selectedSubjChapter`, tab ids…). Navigation is function calls (`openSubject`, `openSubjectWorkspace`, `switchSubjectTab`, `select*Chapter`), no URL routing, no history API (Back is `handleGlobalNavBack`).
- **Rendering:** template-string HTML assigned to `innerHTML` (243 sites in `app.js`) with inline `onclick` handlers (416 in `app.js`).
- **Lazy loads:** only 7 files are injected on demand (`test_prep_bank.js`, `word_stats_words.js`, `math_5/6/7/8/11_solutions.js`).
- **Backend:** PHP 8 / PDO MySQL, 5 endpoints (`auth`, `progress`, `study_plans`, `test_prep`, `health`), session cookie `spacebook_sid`, schema auto-applied on first request.
- **Deploy:** two paths — GitHub Actions FTP upload of `SpaceBook Web/` (writes `api/config.php` from secrets), and a manual zip built by `tools/build_upload_zip.py`.

### 3.2 Content data contracts (five co-existing)
| Contract | Where | Consumers |
|---|---|---|
| A. `Object.assign(DATA, {...})` legacy chapter arrays | `data_chem.js`, `data_phys.js`, `data_eng.js`, `data_bio.js`, `data_comp.js` (Class 9/10) | old per-subject renderers in `app.js` |
| B. Named globals (`BIO_DATA`, `ENGLISH_DATA`, `MATH_DATA`, `URDU_7_DATA`, …) | most `*_data.js` | `getSubjectChapterList` if-chains |
| C. `window.CLSn_BOOKS[subj] = {units, book, words}` + shared `CLS6_SOLUTIONS` | Classes 1–10 rebuilt books | `cls*_book_reader.js`, `math*_reader.js`, `sb_book_skin.js` |
| D. `CLASS11_BOOKS` with per-book render functions | Class 11 | `class11_study_views.js` |
| E. Class 12 per-subject data + `*12_exercise_banks.js` overlays + `*_study.js` | Class 12 | `class12_study_views.js`, `math12_*` |

Plus **load-time overlays** that mutate other files' data (`chemistry_10_source_data.js` sets `sourceReview:{status:'in-progress', lastFullyVerifiedPdfPage:4}` on Class 10 Chemistry; `english_10_source_review.js`; `biology_10_unit*_source.js`; `math12_*_recovery.js`).

### 3.3 Folder map (sizes)
| Path | Size | Role |
|---|---|---|
| `tmp/` | 6.4 GB | scratch renders and agent scripts (gitignored) |
| `docs/` | 862 MB | `source-verification/` pipelines (scripts + transcriptions tracked; images ignored) and docs |
| `js/` | 360 MB | app, add-ons, all book data |
| `tools/` | 347 MB | 2,631 entries; `source-review/` 282 MB (ignored); 2,507 `.py` one-offs |
| `cover-replacement-staging/` | 58 MB | ignored staging |
| `covers/` | 46 MB | book covers, 3 MP4 videos |
| `assets/` | 8 MB | KaTeX + Class 12 figures |
| root `*.png` | 23 MB | page renders (ignored) |
| `backup/` | 2.8 MB | ad-hoc backups (ignored) |
| `.git` (repo root `D:\SpaceBook`) | 1.3 GB | 30,029 tracked files, 64 MB of `tmp_obj` garbage |

---

## 4. Findings

Format per finding: **Problem · Affected · Evidence · Root cause · Severity · Cross-impact · Recommendation · Risks/deps · Verification.**
IDs are referenced by the roadmap and the master prompt.

### 4A. Confirmed defects

#### SEC-01 — Live database credentials publicly downloadable
See section 0. **Critical.**

#### DEP-01 — Live site not serving the app; deploy pipeline failing
- **Affected:** `.github/workflows/deploy.yml`, `tools/build_upload_zip.py`, server `public_html/spacebook/`.
- **Evidence:** `GET /spacebook/index.html` → 404; directory listing instead of the app; GitHub Actions runs for `a12f8d0c` and `27273b6d` all `failure`; local `main` ahead 2 with uncommitted work.
- **Root cause (hypothesis):** FTP sync state was reset ("new FTP state file name to force a full re-upload") and the 358 MB upload over FTPS with `security: loose` fails/times out; meanwhile a manual zip was placed in the web root but not extracted. The failing step was not read (Actions logs need auth).
- **Severity:** Critical (students cannot use the site; the zip in its place leaks secrets).
- **Recommendation:** fix SEC-01 first; then one deploy path only (CI), with a build step that produces a hashed, compressed `dist/`, uploads atomically (upload to `releases/<sha>/` then switch), and a post-deploy check that `index.html` returns 200 and `health.php` reports `db:true`.
- **Verification:** green Actions run; `curl -I /spacebook/` 200 with the app HTML.

#### PERF-01 — 358 MB of JavaScript loaded synchronously at startup
- **Affected:** `index.html` (250 `<script>` tags), every `*_data.js`.
- **Evidence (browser run):** 250 resources, 358.0 MB transferred (local server, no compression), DOMContentLoaded 17,404 ms, `usedJSHeapSize` 698 MB after load (397 MB after GC later). Largest: `chem_12_data.js` 20 MB, `phys_12_data.js` 18 MB, `economics_12_data.js` 18 MB, `quran_12_data.js` 12.9 MB, `biology_12_data.js` 10.6 MB, `data_chem.js` 9.7 MB.
- **Root cause:** every book is a global script that must exist before `app.js` runs; `app.js` reads globals with `typeof X !== 'undefined'`.
- **Severity:** Critical. On a 2–3 GB RAM Android phone the tab will be killed or take minutes; on mobile data 358 MB per visit is unaffordable (live server compression unknown because the app is not deployed).
- **Cross-impact:** all subjects; makes offline caching of "the app shell" equal to caching all content.
- **Recommendation:** per-book content packages loaded on demand (by class → subject), registry-only startup (`data.js` + a generated manifest), compression (gzip/brotli) and long-cache hashed filenames. Target: initial JS ≤ 2 MB, first render ≤ 3 s on a mid-range phone.
- **Risks/deps:** needs the loader in ARCH-03 and a manifest generator; every consumer that reads book globals (search, test prep builder, study plan, word stats, papers, translator lexicon) must switch to an async API.
- **Verification:** Performance API measurement before/after; Lighthouse mobile; per-subject smoke test after lazy loading.

#### ARCH-01 — Cross-subject regressions: patch chains and global DOM rewriters (root cause)
- **Affected:** `js/app.js` and the add-on layer: `cls1..6_book_reader.js`, `cls2_page_reader.js`, `math5/6/7/8/11_reader.js`, `math12_*`, `class11_study_views.js`, `class12_study_views.js`, `sb_structure.js`, `structure_harmonizer.js`, `sb_medium.js`, `sb_rtl.js`, `sb_trilingual.js`, `sb_four_lang.js`, `sb_topic_practice.js`, `sb_global_ui.js`, `sb_mcq.js`, `sb_trace.js`, `sb_vertical.js`, `sb_solve.js`, `sb_book_skin.js`, `word_stats.js`, `test_prep.js`, `continue_learning.js`, `reader_tools.js`, `universal_translate.js`.
- **Evidence:**
  - Wrappers of the same global: `switchSubjectTab` wrapped in `cls1/2/3/4/5/6_book_reader.js`, `cls2_page_reader.js`, `math5/6/7/8/11_reader.js`, `class11_study_views.js:260`, `sb_structure.js:114/251` (≥14); `openSubject` in `cls1/2/3/4_book_reader.js`, `cls2_page_reader.js`, `continue_learning.js:95`, `word_stats.js:606` (7); `getSubjectChapterList` in 5 readers + `class11_study_views.js:225`; `typesetChapterMath` in 5 math readers; `goToSubjects`, `renderTestsPreps`, `switchMathTab`, `selectSubjectChapter`, `openSubjectWorkspace`, `renderSubjectChapterView` also wrapped.
  - Document-wide observers (`childList+subtree` on `document.body`/`documentElement`): `app.js:15308`, `reader_tools.js:128`, `sb_four_lang.js:44`, `sb_global_ui.js:105`, `sb_mcq.js:504`, `sb_medium.js:315`, `sb_rtl.js:58`, `sb_structure.js:295` and `:395`, `sb_topic_practice.js:351`, `sb_trace.js:322`, `sb_trilingual.js:379`, `sb_vertical.js:123`, `structure_harmonizer.js:424`, `word_stats.js:690`. Each rewrites DOM, which re-triggers the others (debounced by 40–80 ms timers).
  - 22 modules inject their own `<style>`; `css/style.css` (8,506 lines) has 180 `!important`, `css/sb_theme.css` 46.
  - Language/direction are guessed from text (`sb_rtl.js` counts Arabic vs Latin letters in the first 400 text nodes; `sb_medium.js` "medium of the open subject is read from its own text"; `sb_solve.js` "Urdu-medium data keeps the Urdu original in the 'en' slot").
- **Root cause:** no extension points — every new feature was added by wrapping globals or rewriting finished HTML, and the final behaviour depends on script order and timing, not on declared configuration.
- **Severity:** Critical (this is the regression mechanism the owner reported).
- **Cross-impact:** any change to `app.js` renderers, CSS class names, tab button markup or text content can silently change behaviour in every class.
- **Recommendation:** (1) freeze the current behaviour with snapshot tests per subject (QA-02) before touching anything; (2) introduce explicit hooks in one place (a `SB.hooks` registry: `beforeChapterRender`, `afterChapterRender(ctx)`, `tabsFor(ctx)`), and migrate wrappers one at a time; (3) replace text-sniffing with declared book metadata (`medium`, `dir`, `langs`) in the manifest; (4) scope post-processors to the rendered container they own, run once per render via the hook, and delete their `MutationObserver`s; (5) move injected CSS into scoped stylesheets with a per-subject root class.
- **Risks/deps:** highest-risk refactor; needs QA-02 first; must be done module by module with screenshots/DOM snapshots compared.
- **Verification:** per-subject DOM-snapshot + screenshot diffs for every class/subject before and after each migrated module; observer count = 0 outside the translator UI.

#### ARCH-02 — Chapter lookup prefers stale global state over the requested class
- **Affected:** `js/app.js:19207` `getSubjectChapterList` and the same `classId === X || state.selectedClass === X` pattern across `app.js` (e.g. `getCurriculumQuestionsForCategory`, `getComprehensiveChapterSLOBank`, `showWordHoverTooltip`).
- **Evidence (reproduced in the running app):** `state.selectedClass='cls7'; getSubjectChapterList('eng','cls9') === ENGLISH_7_DATA` → **true** (`=== ENGLISH_9_BOOK` false). `state.selectedClass='cls12'; getSubjectChapterList('urdu','cls10') === URDU_12_DATA` → **true**.
- **Root cause:** each branch tests the argument OR the global, and branches are ordered by class, so the first class matching the stale global wins.
- **Severity:** High. Callers that pass an explicit class while another class is open (e.g. `sb_topic_practice.js:150`, paper generator selectors, search) get another class's book.
- **Recommendation:** resolve chapters through a single `getBook(classId, subjectId)` that uses only its arguments (registry lookup), make `state` an input only at the UI edge.
- **Verification:** unit test matrix: for every (class, subject) and every possible `state.selectedClass`, `getBook` returns the same object.

#### ARCH-03 — Five incompatible content contracts and per-subject copy-paste renderers
- **Affected:** see 3.2; `app.js` has parallel renderer families (`renderBio*`, `renderChem*`, `renderPhys*`, `renderEng*`, `renderUrdu*`, `renderIsl*`, `renderPakStudy*`, `renderMath*`) plus generic `renderSubject*`; `openSubject` (`app.js:1894`) is a 270-line if-chain over class ids and `has*` flags (`hasEng`, `hasIsl`… 32 different flags).
- **Evidence:** function list of `app.js`; `openSubject` branches for `cls5`, `cls6`, `cls7`, `cls8`, `cls11`, …; `class11_study_views.js:31,33` and `class12_exercise_banks.js:7` use `eval(name)` because `const` globals are not on `window`.
- **Severity:** High (maintainability; every fix must be repeated per family).
- **Recommendation:** define one **Book Content Contract v1** (JSON) with adapters from each legacy contract, one reader shell, per-block renderers. Migrate subject by subject behind a feature flag; keep legacy renderers until the new one matches snapshots.
- **Verification:** contract validator passes on every book; per-subject snapshot parity.

#### CONT-01 — Generated "Board SLO" MCQs presented as board questions
- **Affected:** `js/app.js:14189` `getTopicSpecificSLOs`, `js/app.js:18013` `getComprehensiveChapterSLOBank` (Class 9/10 Mathematics paths); consumed by the SLO tabs and by Papers (`getCurriculumQuestionsForCategory`, `app.js:12014`).
- **Evidence (running app):** for `MATH_DATA` (Class 9) the SLO bank holds 324 MCQs; **320** of them are 5 generic stems repeated over 64 topics ("Under KPK Board SLOs for X, which statement correctly expresses…", "What is the primary operational competency evaluated under X…", …) and **all 320 are keyed to option index 0**. The remaining hand-written ones include a claim that "Arthur Cayley introduced the concept of matrices in 1860" (his matrix memoir is usually dated 1858 — needs checking against the textbook).
- **Root cause:** placeholder generator code from an early agent pass was never removed; the MCQ bank builder filters "template filler" (`tools/test_prep/build_mcq_bank.js`), but Papers and the in-chapter SLO tabs do not.
- **Severity:** High (educational integrity; violates "never invent board questions").
- **Recommendation:** remove templated items from all student-facing paths; show only textbook/board-sourced questions with provenance (`source: textbook|board-paper|teacher`, page reference). Where a chapter has no sourced SLO questions, show "Not available yet" rather than generated text.
- **Verification:** a content lint that flags any question stem repeated across ≥3 chapters or any bank where ≥80 % of keys are the same index.

#### CONT-02 — Papers answer key reads the wrong field for Math SLO MCQs
- **Affected:** `js/app.js:12014` (`ans: m.correctIndex ?? m.ans ?? 0`) vs bank items that use `correct`.
- **Evidence:** all 324 Class 9 Math SLO MCQs carry `correct`; the paper builder therefore sets `ans = 0` for every one. 4 hand-written items (correct = 1 or 2) are printed with the wrong key.
- **Severity:** High (wrong answer keys on printed papers).
- **Recommendation:** normalise MCQs once (`{stem, options[], answerIndex|null, explanation, source}`) at load; papers refuse to print an answer key for items with `answerIndex == null`.
- **Verification:** unit test that every MCQ reaching the paper has a validated key or is flagged "no key".

#### CONT-03 — Placeholder and misleading media
- **Affected:** `app.js:4611` `renderEngVideo` (same three files `covers/Videos/English.mp4`, `URdu.mp4`, `1st Paraghraph.mp4` for every chapter); `app.js:19945` `renderClass9EnglishVideoTabs`; `app.js:8978` `renderIslVideo` fallback `https://www.youtube.com/embed/dQw4w9WgXcQ` with invented title/duration/instructor; `app.js:~14738` a fake "Click to Play Topic Lecture · Quality 1080p HD" card in Math.
- **Evidence:** code; tab survey shows "🎥 Videos" / "🎥 ویڈیو لیکچر" tabs in Class 11 Physics, Chemistry, Biology, English, Urdu and Class 12 Computer, English.
- **Severity:** High (misleading students; external dependency).
- **Recommendation:** hide video tabs unless a chapter has a real, offline-available video with metadata; delete the fake player and the placeholder YouTube ID.
- **Verification:** grep finds no `dQw4w9WgXcQ`; video tab appears only where `chapter.videos.length > 0`.

#### SYNC-01 — Reward progress lost when a signed-in student is offline
- **Affected:** `js/sb_rewards.js` `step()`/`again()`.
- **Evidence:** on a network error `call()` returns `{ok:false}` (no `error`), so `step()` goes to `else r = {ok:false, earned:0}` — the finished step is neither queued nor stored. On any server error message (e.g. 500 "Could not save progress") it sets `user = null` and silently continues as guest.
- **Severity:** High (data loss for the exact offline case the owner wants).
- **Recommendation:** write every activity event to a durable local outbox (IndexedDB) first, then sync; never demote the user on a transient error.
- **Verification:** offline test — complete steps offline, reload, go online → server shows the steps exactly once.

#### SYNC-02 — Study plans: offline edits never uploaded, offline deletes resurrect
- **Affected:** `js/sb_study_plan.js:72` `persist`, `:77` `syncWithAccount`, `:591` delete; `api/study_plans.php`.
- **Evidence:** `persist()` fires `api('save')` once and ignores failure. `syncWithAccount()` only pushes plans **missing** on the server, not plans that are newer locally, so an offline edit stays local until the next edit. Delete calls `api('delete')` once; if it fails, the next `syncWithAccount` re-adds the plan from the server. Save uses the device clock (`updatedAt = Date.now()`), delete uses the server clock — clock skew decides conflicts.
- **Severity:** High.
- **Recommendation:** outbox with retry; tombstones created locally and synced; server-assigned versions (`version` integer or server timestamp) instead of client clocks.
- **Verification:** scripted offline edit/delete → online → second device sees the correct result.

#### SYNC-03 — Test prep: guest history orphaned; whole-record last-writer-wins
- **Affected:** `js/test_prep.js:134` `storeKey`, `:174` `push`, `:186` `pull`; `api/test_prep.php` `save`.
- **Evidence:** guest data lives under `sbTP:v1:guest` and signed-in data under `sbTP:v1:<id>` — nothing merges guest into the account at login. The server keeps whichever whole record has the larger client `updatedAt`. No `online` event listener anywhere in the project, so pending pushes wait for the next answer. `test_prep_sessions` has no per-user cap (only per-request size).
- **Severity:** Medium-High.
- **Recommendation:** event-level sync (append answers/sessions with idempotency keys) instead of whole-record overwrite; merge guest data on first sign-in with consent; retry on `online`/`visibilitychange`.
- **Verification:** two-device offline test; guest → sign-in test.

#### SEC-02 — Reward coins can be farmed
- **Affected:** `api/progress.php` `add_steps`, `sync`.
- **Evidence:** the activity key and its `total` are chosen by the browser (`valid_key` only checks characters; `total` capped at 200, fixed by the first report). A crafted `sync` request with 500 random keys × 200 steps earns ≈ 500 × 205 coins per request.
- **Severity:** Medium (no money involved, but coins are a motivation/ranking feature).
- **Recommendation:** server-side activity catalogue (generated from the content manifest) with fixed totals; rate limits per user per hour; reject unknown keys.
- **Verification:** API test — unknown key → 422; over-limit → 429.

#### SEC-03 — Copyright/redistribution exposure
- **Affected:** public GitHub repo `irfanullahrec/SpaceBook` (`"visibility": "public"`, 215 MB) containing all book transcriptions (`js/*_data.js`, `docs/source-verification/**`), and the site serving all content as plain JS; app links to KPTBB PDFs (`Books/6th/Math/pdf/...`).
- **Severity:** High (legal/licensing; also "illegal redistribution" is one of the owner's concerns).
- **Recommendation:** make the repository private (or move content to a private repo/package store); keep only code public if desired; obtain written permission from KPTBB for distribution; serve content packages only to licensed/authenticated devices with signed manifests (see 6.F).
- **Verification:** GitHub API shows `private:true`; content packages require a valid licence token.

#### SEC-04 — Student selections sent to unofficial third-party endpoints
- **Affected:** `js/universal_translate.js:92` (`translate.googleapis.com/translate_a/single?client=gtx`), `:105` (`api.mymemory.translated.net`), `js/word_stats.js:222` (Google batch), `js/app.js:13620` (MyMemory), `js/app.js:4184` (`translate.google.com/translate_tts`).
- **Severity:** High (privacy of minors, ToS of an undocumented API, breaks offline, unpredictable quality).
- **Recommendation:** offline-first lexicon + stored book translations; if online MT is kept, route through your own server endpoint with an approved provider, rate limits, caching and no personal data; show a clear "machine translation" label.
- **Verification:** network log during normal reading shows no third-party requests.

#### SEC-05 — Authentication/session hardening gaps
- **Affected:** `api/auth.php`, `api/session.php`, `api/db.php`, `api/health.php`.
- **Evidence:** no CSRF token (relies on `SameSite=Lax`); registration returns "An account with this WhatsApp number already exists" (enumeration); failed-login limit is per WhatsApp number only (IP column stored but not used); `login_attempts` never pruned; no password change/reset; session cookie lifetime 30 days but PHP `session.gc_maxlifetime` not raised (default 1,440 s — suspected early logouts, unverified on host); `db.php` runs DDL on the request path when the marker file is missing; `health.php` publicly returns PHP version and table names; no security headers.
- **Severity:** Medium.
- **Recommendation:** see roadmap P2-4 (token-based device auth for offline sync, CSRF for cookie flows, IP+account throttling, generic messages, password reset via verified channel, migrations run by deploy not by requests, health endpoint behind a token).
- **Verification:** API tests + header scan.

#### SEC-06 — Front end cannot run under a Content-Security-Policy
- **Affected:** `eval` in `class11_study_views.js:31,33`, `class12_exercise_banks.js:7`, `universal_translate.js:134`; 416 inline `onclick` in `app.js` (92 on `<div>`); inline styles everywhere.
- **Severity:** Medium (blocks XSS defence-in-depth).
- **Recommendation:** registry lookups instead of `eval`; delegated event handlers with `data-action`; then CSP `script-src 'self'`.

#### OFF-01 — No offline capability at all
- **Affected:** whole app.
- **Evidence:** no service worker (`navigator.serviceWorker.controller` null), no `<link rel=manifest>`, no IndexedDB use; `navigator.storage.persisted()` false; Google Fonts stylesheet requested on every load (for "Segoe UI", which Google Fonts does not serve); Urdu/Pashto fonts (`Jameel Noori Nastaleeq`, `Pashto Koodak`) assumed installed, not bundled.
- **Severity:** High (core requirement).
- **Recommendation:** PWA shell + service worker (versioned precache of shell; runtime cache of content packages; download-for-offline per class/subject), IndexedDB for content index, lexicon and the sync outbox; bundle open-licence fonts (e.g. Noto Nastaliq Urdu, Noto Naskh Arabic) as WOFF2.
- **Verification:** airplane-mode test of every module listed in the requirements.

#### ML-01 — Four-language word meanings: partial, inconsistent, partly online
- **Affected:** `js/universal_translate.js` (hover/long-press card, the active path), `js/offline_lexicon.js`, `js/dictionary_data.js`, `js/app.js:18873` (legacy hover tooltip, now suppressed), `js/sb_trilingual.js`, `js/sb_four_lang.js`, `js/structure_harmonizer.js`.
- **Evidence:** offline lexicon = **1,260** rows with all four languages; `ENG_URDU_DICT` = **6,497** English entries, 4,083 with Pashto, **0 with Arabic**, **378** with the placeholder Urdu "اردو معنی…"; sample offline lookup (network blocked): English→3 languages 52/60, Urdu→3 languages 25/30, Pashto 15/15, all from the dictionary. Sentence/paragraph translation offline falls back to "≈ word by word" glosses; Arabic sentence lines come from the internet (`sb_four_lang.js` header). The legacy `showWordHoverTooltip` handles Latin letters only and shows Urdu+Pashto only. Data slot convention differs by book (Urdu original stored in `en` slot in Urdu-medium books — `sb_solve.js` header; `c7arabic-s1` has Arabic in `en` and English in `ur`).
- **Severity:** High.
- **Recommendation:** one **Lexicon v1** (lemma, language, POS, meanings in the other three, source, reviewed flag) built offline from book glossaries + reviewed dictionary; one **Sentence translation store** keyed by content id with `{en,ur,ps,ar}` and provenance (`book|reviewed|machine`); fix slot semantics (`orig` + `lang` field instead of overloaded `en`); single hover/tap component.
- **Verification:** coverage report per book (% of distinct words with all 3 target meanings; % of sentences with all 3 target translations); airplane-mode spot checks.

#### TAB-01 — Chapter tabs inconsistent across classes and subjects
- **Affected:** renderers in `app.js`, readers, `sb_structure.js`, `class11_study_views.js`, `class12_study_views.js`, `word_stats.js`.
- **Evidence (survey of all 115 subjects, plus middle-chapter re-check of 20):**
  - "🎯 Board SLO Based & MCQs, SQs, LQs" appears in many Classes 1–10 science/humanities books, but **not in any sampled Class 11 or Class 12 book**, nor in most Urdu/Arabic-medium books (which show "حاصلاتِ تعلّم" or nothing); English shows "🎯 SLOs"; Class 5/6/8 Math "Learning Outcomes".
  - "Summary" is missing in many books (e.g. Class 1/2/3 English, Urdu in most classes, Pashto, Class 11 Islamiat/Civics/Mutalia, Class 12 Mutalia).
  - "📊 Word Stats" is injected by `word_stats.js` at different positions (first in Class 11 Urdu, Class 11 Mutalia, Class 12 English; last elsewhere).
  - Duplicate content tabs: "📖 Lessons" and "📖 Lesson text" together (Class 11 Physics/Chemistry/Biology, Class 12 Computer).
  - Three numbering styles for Math ("1. Lessons (21)" in Class 7/9/10/11/12 vs plain in 5/6/8).
- **Severity:** High (owner requirement C).
- **Recommendation:** one declarative tab model per chapter: core tabs `Lessons → (Topics/Activities/Examples nested) → Exercises → Summary → Board SLO (MCQ/SQ/LQ) → Word Stats`, shown only when they have sourced content, labels from the medium dictionary, positions fixed.
- **Verification:** `tools/ui_audit/audit_tabs.js` extended into an automated assertion over every chapter.

#### DATA-01 — Superseded data still loaded (needs runtime proof before removal)
- **Affected (candidates):** `english_data.js` (vs `english_9_book.js`; still the Class 10 fallback per comment), `general_science_9_data.js` (vs `_book`), `pakstudy_data.js` (vs `pakstudy_9_book.js`), `english_1_data.js`, `islamyat_1_data.js`, `nazira_1_data.js`, `pashto_1_data.js`, `drawing_1_data.js` (vs `*_1_book.js`), `math_1_data.js` (`MATH_1_URDU` not referenced outside its file), `math_3_book_text.js` (`MATH_3_BOOK_TEXT` referenced only by a tool), `data_bio.js`/`bio_data.js` (both map to Class 9 Biology in the MCQ builder), `chemistry_10_source_data.js`/`physics_10_source_data.js` overlays, `math_12_book_data.js` (not loaded anywhere), `unkeyed.json` (tool output).
- **Severity:** Medium (size + confusion over which file is the truth).
- **Recommendation:** instrument which globals are read per subject (coverage run), then retire with the archive procedure.

#### DATA-02 — Generated indexes go stale
- **Affected:** `js/study_plan_index.js` (built 2026-10-18 12:50) is older than 15 data files changed afterwards (e.g. `english_8_data.js`, `computer_8/9/10_data.js`, `math_11_data.js`, `mutalia_quran_8/10_data.js`). `test_prep_bank.js` and `word_stats_*.js` happen to be current (2026-10-19 00:13/00:31).
- **Severity:** Medium.
- **Recommendation:** a single `build` command regenerates all derived files and fails CI if they differ from the committed copies.

#### QA-01 — Existing test gates are broken and not enforced
- **Affected:** `tools/validate.js`, `tools/smoke.js`, `test_cls2_all_subjects.js`, `.github/workflows/deploy.yml`, `CONTRIBUTING.md`.
- **Evidence:** `node tools/validate.js` → 648 PASS, 10 FAIL (e.g. `DATA.eng2Chapters = 12 -> got 16`, `load english_10_data.js -> Cannot read properties of undefined`), then **crashes** with `TypeError` at line 146. `node tools/smoke.js` → 247 PASS, **32 FAIL** (Class 1/2 Maths, Class 2/3 Drawing, Class 12 English …). The deploy workflow runs no tests. `CONTRIBUTING.md` promises "104 static + dataset checks" and "51 UI smoke tests" and describes an ownership table that no longer matches the code.
- **Severity:** High (no safety net = regressions).
- **Recommendation:** repair or rewrite as (a) data contract validation, (b) headless-browser smoke per subject (Playwright), (c) DOM/screenshot snapshots; run on every push; block deploy on failure.

#### PERF-02 — Slow subject/chapter rendering
- **Evidence (desktop, sync main-thread time of `openSubject`):** Class 12 Physics 5,186 ms; Class 9 Urdu 3,152 ms; Class 12 Statistics 3,103 ms; Class 7 HPE 3,112 ms; Class 12 Urdu 2,105 ms; Class 12 Chemistry 1,794 ms with 21,869 DOM nodes; Class 10 Physics 1,614 ms.
- **Root cause (hypothesis):** whole chapter (all tabs) rendered to strings at once; `sb_structure.js` renders every tab "once synchronously" to compare them; observers then re-walk the DOM.
- **Severity:** Medium-High (low-end phones ×5–10).
- **Recommendation:** render only the active tab; virtualise long lists; precompute the tab plan at build time instead of at render time.
- **Verification:** p95 chapter open < 300 ms desktop, < 1.5 s on a reference low-end Android.

#### MCQ-01 — MCQ bank quality signals
- **Affected:** `js/test_prep_bank.js` (6,120 MCQs from 13,173 candidates), `js/unkeyed.json`, Class 11 data.
- **Evidence:** answer index distribution 0: 1,626 · 1: **2,352** · 2: 1,419 · 3: 723 (skew toward "b"); 51 duplicate stems; **Class 11 contributes 0 MCQs** (no answer keys in source); per the builder report, 2,820 template-filler items and 4,048 duplicates were dropped upstream.
- **Severity:** Medium.
- **Recommendation:** content review queue for skewed/duplicate items; Class 11 keys only from verified sources; provenance per MCQ.

#### PDF-01 — "Official … Book PDF" buttons point outside the deployed site
- **Affected:** `app.js` cover/PDF map (e.g. `Books/6th/Math/pdf/Math Book for 6 class KPTBB.pdf`).
- **Evidence:** the deploy set (`tools/build_upload_zip.py` `SITE` list; CI uploads `SpaceBook Web/` only) contains no `Books/` folder; on the live host `GET /spacebook/Books/6th/Math/pdf/...` → 404 (the app is not deployed, so re-check after deployment). Locally the preview server happened to serve the PDF.
- **Severity:** Medium (broken button online; PDFs are also a redistribution question — SEC-03).

#### UX-01 — Accessibility and language semantics
- **Evidence:** `<html lang="en">` fixed and `dir` never set at the root; Urdu/Pashto/Arabic regions rely on `sb_rtl.js` guessing; 92 clickable `<div onclick>` in `app.js`; only 4 `role="tab"` in `app.js`; emoji-only icons without labels in many buttons; no focus management in modals (except the auth dialog).
- **Severity:** Medium.

#### MAINT-01 — Repository hygiene
- **Evidence:** `.git` 1.3 GB with 64 MB of `tmp_obj_*` garbage (30 files); 26,577 tracked files under `docs/`; 2,507 one-off `.py` files in `tools/`; CRLF/LF warnings on `app.js`; a stray `kotlin/PhysChapters.kt`; agent progress files at the web root (`exercise-pages.json`, `biology-progress.json`, `docs/*-progress.json`).
- **Severity:** Low-Medium.

#### ADMIN-01 — No administration, roles or content management
- **Evidence:** `users.user_type` (`school|teacher|student`) is stored but never checked by any endpoint; no admin endpoints, no audit log, no way to block/unblock users except SQL.
- **Severity:** Medium (needed before schools/teachers use it).

#### PRIV-01 — No profile management or data-subject controls
- **Evidence:** no endpoints to edit profile, change password, export or delete an account; minors' names, father names and WhatsApp numbers stored without a stated retention policy.
- **Severity:** Medium.

#### BAK-01 — No automated backups or restore procedure
- **Evidence:** only ad-hoc folders (`backup/`, `D:\SpaceBook\backup`, `Recovered-POS-Backup-*`); no DB dump job; no documented restore.
- **Severity:** Medium.

### 4B. Suspected problems (need confirmation)

| ID | Suspicion | Why | How to confirm |
|---|---|---|---|
| S-01 | Sessions expire after ~24 min idle on the host | cookie lifetime 30 d but `session.gc_maxlifetime` not set | check host `php -i`, log in, wait 30 min |
| S-02 | Deploy fails on FTP timeout/size | 358 MB upload over FTPS `security: loose`; state reset | read the Actions log (needs repo access) |
| S-03 | `sb_structure.js` hiding tabs whose text "already appears in an earlier tab" may hide legitimate content (e.g. a Summary that repeats lesson sentences) | heuristic in header comment | per-chapter snapshot comparison with the module disabled |
| S-04 | Answer-position skew (38 % "b") reflects generated rather than textbook MCQs in some books | distribution | sample 50 "b" items per class against scans |
| S-05 | `assets/biology12/` (96 files, 2 MB) and `assets/physics12/` (9 files, 3.5 MB) unused | no filename referenced by any JS/CSS | runtime network log over all Class 12 Biology/Physics chapters |
| S-06 | Superseded data files (DATA-01) are never read at runtime | static analysis only | property-access tracing per subject |
| S-07 | `chemistry_10_source_data.js` overlay marks Class 10 Chemistry `sourceReview.status:'in-progress', lastFullyVerifiedPdfPage:4` while memory notes say the book is complete | stale overlay may override newer data | compare rendered Class 10 Chemistry with/without the overlay |
| S-08 | Search (`handleGlobalSearch`, 168–196 ms per keystroke on desktop, no debounce) will lag on phones and after lazy loading will not find unloaded books | measurement | build a prebuilt search index |

---

## 5. Requirement-by-requirement status

| Requirement | Status today | Main findings |
|---|---|---|
| A. Stop cross-subject regression | Root cause confirmed | ARCH-01, ARCH-02, ARCH-03, QA-01 |
| B. Four-language word meanings + paragraph translation | Partial; online-dependent | ML-01, SEC-04, OFF-01 |
| C. Intelligent tab structure | Inconsistent | TAB-01, CONT-03, S-03 |
| D. Complete offline operation | Not implemented | OFF-01, PERF-01 |
| E. Secure activity sync | Partial; data-loss paths | SYNC-01/02/03, SEC-02 |
| F. Application security | Critical gaps | SEC-01…06, DEP-01 |
| G. Module completeness | Mixed | CONT-01/02, MCQ-01, ADMIN-01, PRIV-01, DATA-02 |
| H. Speed and accuracy | Poor speed; some accuracy defects | PERF-01/02, CONT-01/02 |
| I. Unnecessary files | Large savings available | see Cleanup Report |

---

## 6. Additional requirements identified (justified by the architecture)

1. **Content package versioning** — each book becomes `content/<class>/<subject>/<version>/book.json` + `meta.json` (sha256, schema version, page count, verification status). Needed for offline download, updates and integrity.
2. **Signed manifest** — `manifest.json` listing every package with hash; signed on the server (Ed25519); the app verifies before using a package. Detects tampering in transit or on disk. (It cannot stop someone who modifies the client itself.)
3. **Device licensing (realistic)** — per-device activation token bound to an account; packages encrypted per licence with a key delivered after activation; watermark the account id in rendered pages. This raises the cost of copying; it cannot make offline content unextractable.
4. **Storage quota handling** — `navigator.storage.persist()`, per-class download sizes shown before download, eviction policy that never removes the sync outbox.
5. **Search index** — build-time inverted index per book (Urdu/Pashto/Arabic normalisation), loaded lazily; works offline.
6. **Provenance on every educational item** — `source` (textbook page, board paper year, teacher), `verified` flag, reviewer. Lets the UI hide unverified items.
7. **Board SLO mapping** — load the official KPK SLO list per subject/grade and map questions to SLO codes; then "Board SLO" tabs are real, not inferred.
8. **Error reporting** — local error log with a "send report" button (no third-party tracker), plus server-side PHP error logging to a file outside the web root.
9. **Automated backups** — nightly `mysqldump` (cPanel cron) to off-site storage, 30-day retention, quarterly restore drill.
10. **Low-end device budget** — targets: initial download ≤ 3 MB, memory ≤ 150 MB while reading, chapter open ≤ 1.5 s on a 2 GB Android Go device.
11. **Multi-device sync** — event log with idempotency keys and server-assigned sequence numbers.
12. **Teacher/school accounts** — roles, class groups, assignment of study plans/tests; only after the core is stable.
13. **Privacy notice and consent** — minors' data, parental consent, retention, deletion on request.
14. **Update mechanism** — app shows "update available" when the manifest version changes; downloads only changed packages.

---

## 7. Protect-list (do not break)

- All verified book data: `js/*_data.js`, `js/*_book.js`, `js/*12_exercise_banks.js`, `js/math_*_solutions.js`, `js/math12_*translations*.js`, and the pipelines in `docs/source-verification/class-*/` that generate them.
- Generators: `tools/test_prep/build_mcq_bank.js`, `tools/study_plan/build_study_index.js`, `tools/word_stats/build_word_stats.js`.
- Owner decisions recorded in project memory: no language-tab drop-downs (sentence click → EN/UR/PS drawer), topic cards collapsed with their own full screen, book-order chapter structure (Lessons → Summary → Exercise → practice, no repeats), Class 9/10 is the reference layout for Classes 11/12, labels follow the subject's medium, Qur'anic text is never translated.
