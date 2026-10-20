# Data contracts (as in use on 2026-10-20)

Three groups: the **book data** a person or a class pipeline writes (section 1), the **generated files** a build writes (section 2), and the **wire formats** between the page and the server (section 3). Nothing here is aspirational: each shape was read from the code or the files. The single unified "Book Content Contract v1" with a validator and adapters, planned in Phase 3, is **not built**; section 4 says what exists instead and what would have to change.

## 1. Book data (five shapes, all in use)

`js/data.js` is the registry. `DATA.classes` lists the classes; `DATA.subjects[classId]` lists each class's subjects (`{id, name, nameUrdu, emoji, chapters, has<Kind>...}`); `DATA.books` the textbooks. Adding a subject means one entry there and one `<script>` line in `index.html` before `js/app.js`.

| Shape | Where | What the file defines |
|---|---|---|
| **A. `Object.assign(DATA, {...})`** | legacy Classes 9-10: `data_chem.js`, `data_phys.js`, `data_eng.js`, `data_bio.js`, `data_comp.js` | arrays on the registry: `DATA.chemChapters`, `physChapters`, `engChapters`, `bioChapters`, `compChapters`, `chem10Chapters`, ... Each chapter: `{num, name, pageRange, status, slos[], topics[], textbookExercise{mcqs[], ...}, definitions, differences, diagrams, ...}` |
| **B. named globals** | legacy: `BIO_DATA`, `ENGLISH_DATA`, `ENGLISH_10_DATA`, `MATH_DATA`, `MATH_7_DATA`, `MATH_8_DATA`, `MATH_10_DATA`, `URDU_DATA`, `ISLAMYAT_DATA`, `PAKSTUDY_DATA`, ... | an array of units; a Maths unit is `{number, id, title, titleUrdu, status, pageRange, sections[], workedExamples[], exercises[], slos, formulaSheet}` |
| **C. `window.CLSn_BOOKS[subject]`** | rebuilt books of Classes 1-8 and 10 (e.g. `math_2_data.js`) | `{units[], book, words}`; a unit is `{number, id, title, titleUrdu, titlePashto, type, pageStart, sections[], workedExamples[], exercises[], slos, sourcePdfPages, reviewStatus}`; a section is `{id, title, titleUrdu, titlePashto, blocks[], sourcePdfPages, sourcePrintedPages}`; a block is `{t, ...}` with `t` = `page` (`{pdf, printed}`), `h` (`{l, en, ur, ps}`), `p` (`{en, ur, ps}`), `q` (a question, with `solId`), and the like. Solutions are looked up by `solId` in a shared `CLSn_SOLUTIONS` object |
| **D. `CLASS11_BOOKS[key]`** | Class 11 | `{key, subjectId, data[], render, searchText, tabs, pdf, badge}`; routed by `js/class11_study_views.js` |
| **E. per-subject data + exercise banks** | Class 12 | one data file per subject plus `*12_exercise_banks.js`; routed by `js/class12_study_views.js` |

Conventions that hold across the shapes:

- **Three or four languages per text:** `en`, `ur`, `ps` (and `ar` where the book is Arabic). A translation is stored next to its sentence; a sentence that has no translation is left empty, not machine-filled.
- **Provenance:** `sourcePdfPages` / `sourcePrintedPages` (scan and printed page numbers) and `reviewStatus` / `status` on a unit. A page that is missing from the scans is recorded in the class pipeline's notes (`docs/source-verification/class-N/`), never invented.
- **MCQs** carry their key in one of `correctIndex`, `answerIndex`, `correct`, `ans`, `answer`, `key` (a number, a numeric string, a letter or the option text). **One reader decides**: `sbMcqKey(m)` in `js/app.js` (returns 0-3 or `null`). Nothing may default a missing key to option A.
- **Generated practice** (items made from templates, not from the book) must carry `generated: true`; the owner flag `hideGeneratedSlo` hides them (`CONTENT_REVIEW.md`).
- **Videos and PDFs:** only a real YouTube embed URL (`sbRealVideo`) and a path listed in `SB_PACKAGED_PDFS` (`sbPdf`) are ever shown.

Chapter lookup always goes through `getSubjectChapterList(subjKey, classId)` with the **arguments**, never `state.selectedClass`.

## 2. Generated files

None of these is edited by hand; `node --max-old-space-size=8192 tools/build/all.js` writes them (`--check` in CI).

| File | Shape |
|---|---|
| `content/lazy_manifest.json` | `{schema, containers[], files[]}`; a file entry: `{src, bytes, sha256, stubs[{name, kind}], keys{}, fns[], dataKeys[], also[], after[]}` (what the file provides, what must load with it, what patches it afterwards) |
| `lazy.html` | `index.html` without the lazy `<script>` tags, plus `js/core/lazy.js` and the manifest inline; every script URL carries `?v=<12 hex of its content hash>` |
| `content/offline_map.json` | `{schema: 'spacebook.offline/1', files{src: {v, bytes, sha256}}, assets{path: {bytes}}, subjects{id: {classId, name, files[], assets[], bytes}}}`: what "Download for offline" fetches for a subject, found by rendering it |
| `content/sw_version.js` | `self.SB_SW = {version, entry, offlinePage, shell[]}`: the service worker's version (a new one installs a new worker) and shell |
| `content/search/index.json`, `content/search/<subject>.json` | index: `{schema: 'spacebook.search/1', source, subjects{id: {classId, name, h, bytes, n, c[{t, o}]}}}` (`h` = 12-hex hash of the shard, `c` = chapters with title and the call of their own button); shard: `{v: 1, n, x{word: [chapter, count, ...]}}` (`SEARCH.md`) |
| `js/lexicon_data.js` | `window.SB_LEXICON_V1 = {v: 1, rows: [[English, Urdu, Pashto, Arabic], ...]}` |
| `js/test_prep_bank.js` | `window.SB_MCQ_BANK = {generated, subjects{id: {name, cls, cat, n}}, counts, mcqs[{i, s, q, o[], a, e?, tf?, qu?, qp?}]}`; only questions whose key was resolved from their source |
| `js/bise_swat_data.js` | `window.SB_BISE = {v, board{pages, fetched}, subjects{id: {id, cls, exam, name, nameUr, inApp, key?, files[{k, label, url, bad?}], past[], pattern{A, B, C, total, time, conf}, chapters[{no, t, app?, w?, m?, r?, e?, ep?, pp?, sk?, periods?, topics[], slos[{g, t, l}]}], sections?, tosTotals?, mismatch?}}}`; built by `docs/source-verification/bise-swat/tools/build_bise.py` from hand-transcribed tables and extracted learning outcomes (not by `tools/build/all.js`); loaded on first use by `js/sb_bise.js` |
| `docs/test_prep_review/no_key.csv` | the questions the bank leaves out for want of a key (subject, class, source file, question, options) |
| `js/study_plan_index.js` | `window.SB_STUDY_INDEX = {generated, classes[{id, name, subjects[{id, name, ur, emoji, chapters[{t, c{counts}}]}]}]}` |
| `js/word_stats_summary.js`, `js/word_stats_words.js` | word counts per project, class and subject |
| `tests/baseline/html-2026-10-20/<class>/<subject>.json` | per chapter and tab: the labels in order and a hash of the rendered HTML |
| `tests/contract/hooks.json`, `cls_books.json`, `content_lint.json`, `contrast.json`, `axe.json` | locks: who extends which function; unit counts of the rebuilt books; content-lint counts; low-contrast pairs; axe findings |

## 3. Wire formats

Sync (`api/v2/sync.php`, `JSON`):

- push: `POST {events: [{eventId (uuid), type, payload, clientTs, schema: 1}]}` (at most 500 events, 1 MB) -> `{ok, accepted[eventId], rejected[{eventId, code}], cursor, coins}`; `rejected` events are permanently invalid (codes: `bad_event_id`, `bad_payload`, `bad_schema`, `too_large`, `unsupported_type`, `plan_limit`, ...); anything transient is an HTTP error and the whole batch stays in the client's outbox.
- event types and payloads: `step {key, title, total, step}`, `again {key}`, `plan.save {plan, baseRev}`, `plan.delete {id}`, `tp.answer {mcqId, track, day, correct, ms, ts}`, `tp.session {session}`, `tp.run {run}`, `tp.run.clear {clearedAt}`, `tp.import {record}`.
- pull: `GET ?since=<cursor>` -> `{ok, cursor, more, coins, progress, plans, plansDeleted, tp}`.
- auth: `Authorization: Bearer <64 hex device token>` or the session cookie (then the request must be same-site).

Accounts (`api/auth.php?action=register|login|logout|me|update_profile|change_password|export|delete_account`): `{ok: true, user}` or `{ok: false, error}`; the user object never carries the role.

The audit log (`audit_log`: user, action, ip, user-agent hash, detail) and the sync error record (`sync_errors`: user, device, event id, code) hold ids and codes, never payloads.

## 4. The unified contract that is not built

Phase 3 asked for one validated "Book Content Contract v1" (a schema, a validator, adapters from the five shapes, `SB.content.getBook(...)`, and `openSubject` driven by a registry). What exists instead is the lazy manifest (it knows every book file and what it provides), the offline map (it knows what each subject needs), the search index (it knows every chapter's title and call), and `tests/contract/cls_books.json` (unit counts). To build the contract: write adapters that turn shapes A-E into `{classId, subjectId, medium, dir, chapters[{id, title{en,ur,ps}, tabs[...]}]}`, test them with the HTML baseline (9,710 renders must stay identical), then let `getSubjectChapterList`, the Papers pool, the search builder and the study index read the adapter instead of five shapes. That is the work that also lets the 19 observers and the inline handlers go (`ARCHITECTURE.md`, section 3).
