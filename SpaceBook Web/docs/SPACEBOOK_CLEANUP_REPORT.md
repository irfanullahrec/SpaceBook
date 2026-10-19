# SpaceBook — Project Cleanup Report

**Date:** 2026-10-19 · **Scope:** `D:\SpaceBook\SpaceBook Web` (primary) and, for disk planning only, the sibling folders in `D:\SpaceBook`.
**Rule:** nothing was deleted or moved. Every item below is a *recommendation*. Verified-safe items may be **moved** (not deleted) to `D:\SpaceBook\SpaceBook_Archive\<same relative path>` after a backup; items marked **Verify** must stay untouched until the stated check passes.

---

## 1. Three different "sizes" (do not confuse them)

| Measure | Today | What it means |
|---|---|---|
| **Active project folder** `SpaceBook Web` on disk | **8.0 GB** | Everything in the folder, including scratch output |
| **Production payload** (what the site serves) | **≈ 425 MB uncompressed / 117 MB zipped** (611 files: `index.html`, logo, `css/`, `js/`, `assets/`, `api/`, `covers/`) | From `tools/build_upload_zip.py`'s `SITE` list; `js/` alone is 360 MB |
| **Loaded at startup** | **358 MB** (250 scripts) | Measured in the browser; see PERF-01 in the audit |
| **Git repository** (`D:\SpaceBook\.git`) | **1.3 GB** (30,029 tracked files; 64 MB garbage) | History of all commits; GitHub reports 215 MB packed |

Disk savings from archiving ≠ production savings: almost all disk weight is scratch (`tmp/`, renders) that is never deployed. Production savings come from removing unused **deployed** files (section 4) and, much more, from the lazy-loading/compression work in the roadmap (P3).

---

## 2. Summary of recommended moves

| Group | Size | Tracked in git? | Deployed? | Verdict |
|---|---|---|---|---|
| `tmp/` image renders and scan crops | ≈ 6.3 GB | No (ignored) | No | **Safe** to archive |
| `tmp/` scripts (`*.py` 53, `*.cjs` 113, `*.js` 19, logs/txt 138, json 44) | < 10 MB | No | No | **Verify** (some are pipeline helpers named in project notes, e.g. `ch_go.py`, `ch_run.py`, `bk_*.py`) → archive as a block, keep a list |
| `tools/source-review/` | 282 MB | No (ignored) | No | **Safe** to archive |
| `tools/*.png|*.jpg` at tools root (33 files, `_m7_*`) | 21 MB | No (ignored) | No | **Safe** |
| `tools/10th_Maths_*_aux.txt` (9 files) | 0.7 MB | No (`*_aux.txt` ignored) | No | **Safe** |
| `tools/__pycache__/` | 5 MB | No | No | **Safe** (regenerated automatically) |
| `cover-replacement-staging/` | 58 MB | No (ignored) | No | **Safe** after confirming final covers are in `covers/Books/` (they are: 83 new `kptb_cls*.webp` files, currently **untracked** — commit them first) |
| `backup/class-2`, `backup/class4_pre_review` | 2.8 MB | No (ignored) | No | **Safe** (superseded by git history + pipelines) |
| Root page renders: `doc1_p3.png`, `doc2_p1.png`, `urdu_p3.png` … `urdu_p7.png` | 22.7 MB | No (ignored) | No | **Safe**; `doc1_p3.png` is byte-identical to `urdu_p3.png` (same MD5) |
| Unreferenced cover images (section 4.1) | ≈ 28 MB | partly | **Yes** | **Verify** then archive — saves production bytes |
| `assets/biology12/` (96 files), `assets/physics12/` (9 files) | 5.5 MB | Yes | **Yes** | **Verify** (no filename referenced in JS/CSS) |
| `assets/math9-agent1/` (1 file), `assets/physics9-agent1/` (empty) | 0.2 MB | Yes | Yes | **Verify** (no reference found) |
| `kotlin/PhysChapters.kt` | 1.5 KB | Yes | No (excluded) | **Safe** (no Kotlin build anywhere in the web app) |
| Agent progress files: `exercise-pages.json`, `biology-progress.json`, `docs/math-agent1-progress.json`, `docs/physics-agent1-progress.json` | 40 KB | Yes | No (excluded) | **Safe** to move into `docs/history/` or archive |
| `test_cls2_all_subjects.js` (absolute paths `D:/SpaceBook/...`) | 6 KB | Yes | No | **Verify** — fold into the new test suite, then archive |
| `js/math_12_book_data.js` | 8.5 KB | Yes | **Yes** | **Safe** to remove from deploy (not referenced by `index.html` or any script) — archive after one release |
| `js/unkeyed.json` | 2.5 KB | Yes | **Yes** | Move to `tools/test_prep/` (tool output; not used by the app) |
| Superseded data files (section 4.2) | ≈ 5.4 MB | Yes | **Yes** (eager) | **Verify** with runtime tracing first |
| Git object garbage (`tmp_obj_*`, 30 files) | 64 MB | n/a | No | Run `git gc --prune=now` **after** a full backup of `.git` — not a file move |

**Estimated disk space freed in `SpaceBook Web`:** ≈ **6.7 GB** from the "Safe" rows alone (`tmp/` renders 6.3 GB + `tools/source-review` 282 MB + staging 58 MB + root PNGs 23 MB + tools images/aux/pycache 27 MB + backup 3 MB).
**Estimated production payload reduction from cleanup alone:** ≈ **35–40 MB** (unreferenced covers, unused assets and superseded data) out of 425 MB — about 9 %. The big production win is architectural (lazy packages + compression), not deletion.

---

## 3. Details: scratch and source-review material

### 3.1 `tmp/` (6.4 GB, 1,042 entries, gitignored)
Largest subfolders: `bk/` 3.2 GB (2,115 PNG page renders), `class12-review/` 754 MB, `biology12-source/` 483 MB, `class-10-english/` 288 MB, `stat-zz/` 281 MB, `class-10-physics/` 217 MB, `pdfs/` 194 MB, `math12-missing-source/` 191 MB, `eng-zz/` 175 MB, `class-11/` 127 MB, `class-10-chemistry/` 125 MB.
- Only one tracked script references `tmp/`: `tools/class12_render_fidelity_svgs.js` (writes there). No app code reads `tmp/`.
- The project notes record every book these renders were made for as **COMPLETE**, so the renders are no longer needed for active work. If a book is re-verified later, renders can be regenerated from `D:\SpaceBook\Books`.
- **Procedure:** move the whole folder to `SpaceBook_Archive\SpaceBook Web\tmp\`; write `tmp_INVENTORY.txt` (path, size, mtime) beside it; leave an empty `tmp/` (it is gitignored).

### 3.2 `docs/source-verification/` (≈ 866 MB on disk)
- Tracked: per-class pipeline scripts and page transcriptions — **these are the source of truth for the book data. KEEP.**
- Ignored: page images (`*.png|*.jpg|*.webp…`) used during verification. Archiving them saves most of the 866 MB, but a future re-verification would need them regenerated. **Verify** with the owner per class; recommended order: classes whose pipeline notes say COMPLETE (all of them today).

### 3.3 `tools/` (347 MB, 2,631 entries)
- 2,507 one-off Python scripts (e.g. `biology12_*.py`, `apply_*`, `analyze_*`) — tracked, small. They document how data was produced. **Keep**, but move into `tools/legacy/<topic>/` in a later, separate commit so `tools/` root holds only maintained tools.
- Maintained tools to keep in place: `test_prep/`, `study_plan/`, `word_stats/`, `ui_audit/`, `i18n/`, `class12_answers/`, `validate.js`, `smoke.js`, `build_upload_zip.py` (but see security note in the audit SEC-01: it must stop embedding the live password).

---

## 4. Details: files that are deployed but probably unused

### 4.1 Cover images not referenced by name
Method: every file under `covers/` compared with the cover map in `js/app.js` and the dynamic paths (`covers/Videos/${file}`, `covers/Classes Cards/Another-Look/${file}`), then each remaining basename searched in `js/data.js`, `js/app.js`, `js/sb_*.js`, readers, CSS and `index.html`.
- **114 files / 28.6 MB** not referenced: loose legacy covers at `covers/` root (`2nd *.jpg`, `3rd *.jpg`, `5th *.jpg`, `7th *.jpg`, `8th *.jpg`, `9th *.jpg`, `Arabic.jpg`, `Computer.jpg`, `Drawing.jpg`, `English.jpg`, `General science.jpg`, `Geography.jpg`, `Hpe.jpg`, `Islamiat.jpg`, `Math.jpg`, `Pashto.jpg`, `Urdu.jpg`) and alternates under `covers/Books/<class>/` (e.g. `Gemini_Generated_Image_*.jfif`, `12th/*.jpg`, `8th/8 *.png`, `1st/Futuristic English Class 1 Cover.png` 2.2 MB).
- **Exceptions found by the basename search (keep):** `covers/Books/12th/HPE.jpg`, `covers/History.jpg`.
- **Verify:** load every class page and subject card with the network panel open (or a headless run that records 404s after moving files to a staging copy). Only then archive.
- Note: 83 new `covers/Books/*/kptb_cls*.webp` files are **untracked** in git — commit them before any move so they are not lost.

### 4.2 Data files that may be superseded (eagerly loaded today)
| File | Size | Why it looks superseded | Required proof |
|---|---|---|---|
| `js/math_1_data.js` (`MATH_1_URDU`) | 148 KB | global never referenced outside its file; Class 1 Maths served by `math_1_book.js` | property-access trace over Class 1 Maths |
| `js/math_3_book_text.js` (`MATH_3_BOOK_TEXT`) | 113 KB | referenced only by `tools/generate_math3_text.py` and the word-stats report | trace over Class 3 Maths |
| `js/english_1_data.js`, `islamyat_1_data.js`, `nazira_1_data.js`, `pashto_1_data.js`, `drawing_1_data.js` | ≈ 1.06 MB | `*_1_book.js` versions registered in `CLS1_BOOKS`; legacy globals still referenced by `app.js` branches | trace + smoke tests of Class 1 |
| `js/general_science_9_data.js` | 910 KB | `general_science_9_book.js` is the page-by-page rebuild | trace over Class 9 Science |
| `js/pakstudy_data.js` | 1.27 MB | `pakstudy_9_book.js` is the rebuild | trace over Class 9 Pak Studies |
| `js/english_data.js` | 1.31 MB | `english_9_book.js` is the rebuild, **but** comment says it is still the Class 10 fallback | trace over Class 9 and 10 English |
| `js/data_bio.js` | 606 KB | `bio_data.js` and `biology_10_*` cover Classes 9/10 | trace over Class 9/10 Biology and search |
| `js/math_12_book_data.js` | 8.5 KB | not in `index.html`, not loaded dynamically | none further — safe after one release |

None of these may be archived until the tracing step (roadmap P1-3) shows zero reads and all subject smoke tests pass without them.

---

## 5. Sibling folders in `D:\SpaceBook` (disk planning; outside the web app)

| Folder | Size | Note |
|---|---|---|
| `_cls1_jpg` … `_cls8_jpg` | ≈ 7.0 GB | page renders for completed pipelines (ignored) — **archive candidate** |
| `.gradle_user_home` | 1.8 GB | Android/Gradle cache for `SpaceBook App` — regenerable |
| `SpaceBook App` | 1.3 GB | separate Android project (ignored) — **out of scope**, do not touch |
| `tmp` | 847 MB | scratch — archive candidate |
| `Other-Users-Work` | 534 MB | other people's work — **do not touch** without the owner |
| `Recovered-POS-Backup-20261013`, `POS-Local` | 513 MB | unrelated POS project — **out of scope** |
| `backup` | 178 MB | ad-hoc backups — verify |
| `deploy` | 112 MB | **contains `spacebook_upload.zip` with the live DB password** — keep it off any shared/synced location; delete after the password is rotated and the server copy removed |
| root `*.png|*.jpg` (86 files) | 60 MB | verification sheets — archive candidate |
| `AgentTemp`, `AgentTempmkdir`, `AgentTempn` | 0 B | empty — safe to remove |
| `circle_crops`, `circle_hires`, `dome_crops`, `verification_strips`, `_c9render`, `__pycache__` | ≈ 17 MB | scratch — archive candidate |

---

## 6. Archive procedure (for the implementing agent)

1. Confirm a full backup exists: `D:\SpaceBook` copied (or at least `SpaceBook Web`, `.git`, `deploy`) to an external drive, and `git status` clean or committed.
2. Create `D:\SpaceBook\SpaceBook_Archive\` and inside it `ARCHIVE_LOG.md`.
3. For each group: list files with size and SHA-256 into the log; **move** (never delete) preserving relative paths; record the exact command.
4. After each group: run the full test suite (validate, smoke, per-subject headless run). If anything fails, move the group back and record why.
5. Commit only the changes to tracked files (e.g. moving `kotlin/`, progress JSONs) in a separate "chore: archive unused files" commit with the log excerpt in the message.
6. Never archive: anything under `js/` without a passing trace, anything in `docs/source-verification/**` that is tracked, `api/config.php`, `covers/Books/*/kptb_*.webp`.
