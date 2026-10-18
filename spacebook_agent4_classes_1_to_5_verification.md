# SpaceBook — Agent 4: Classes 1 → 5 Textbook Verification & Content Repair

Progress tracker. A page/section is **Verified** only after the original PDF and the
SpaceBook source content were compared and every discrepancy repaired.

## Rules of engagement
- Source of truth: `D:\SpaceBook\Books\<class>\<subject>\**\*.pdf` (PDF only).
- Target: `D:\SpaceBook\SpaceBook Web` (static site; no database, no rebuild).
- Word/DOC/JPG files are **not** used as verification sources.
- Order: Class 1 → 2 → 3 → 4 → 5; books inside a class in folder order.

## Tooling
- `pdf_survey.py` — page counts / text-layer survey (all Class 1–5 PDFs are scans; text layers are watermark only).
- `ocr.py` / `ocr_batch.py` — RapidOCR extraction of scanned pages (English/Latin script).
- `ocr_pos.py` / `render.py` — targeted page rendering + crop for visual confirmation of wording.

---

## CLASS STATUS

| Class | Subjects with PDF | Subject data files present | Status |
|---|---|---|---|
| 1 | Drawing, English, Islamyat, Maths, Nazera, Pashto (6) | drawing_1, english_1, islamyat_1, math_1, nazira_1, pashto_1 | In Progress |
| 2 | Drawing, English, GK, Islamyat, Maths, Nazira, Pashto, Urdu (8) | drawing_2, english_2, gk_2, islamyat_2, math_2, nazira_2, pashto_2, urdu_2 | Pending |
| 3 | GK, Drawing, English, Islamyat, Maths, Nazira, Pashto (7) | drawing_3, english_3, gk_3, islamyat_3, math_3, nazira_3, pashto_3 | Pending |
| 4 | English, General Science, Islamiat, Math, Pashto, Social Studies (EM), Social Studies (UM→Urdu), Urdu (8) | **NONE — Class 4 has no data file and no `<script>` wiring** | Pending (BLOCKER: entire class missing) |
| 5 | English, General Science, Islamiat, Maths, Pashto, Social Studies (EM), Social Studies (UM), Urdu (8) | english_5, general_science_5, islamiat_5, math_5, pashto_5, social_studies_5, social_studies_um_5, urdu_5 | Pending |

---

## BOOK LEDGER

### Class 1
| # | Subject | PDF (pages) | PDF parts | Data file | Status |
|---|---|---|---|---|---|
| 1 | Drawing | `1st/1st Drawing/PDF/Drawing Book 1 KPTBB.pdf` (34 = cover + ad + printed 1–32) | — | `drawing_1_data.js` | **Verified — Corrected** (32/32 activities match; 4 teacher notes + 3 titles made verbatim) |
| 2 | English | `1st/1st English/PDF/English book 1  KPTBB.pdf` (127) | KPTBB1/2/3 = 46+46+35 | `english_1_data.js` | In Progress |
| 3 | Islamyat | `1st/1st Islamyat/PDF/Islamiat book  KPTBB.pdf` (58) | KPTBB1/2 = 29+31 | `islamyat_1_data.js` | Pending |
| 4 | Maths | `1st/1st Maths/PDF/Math book 1 KPTBB.pdf` (146) | KPTBB1/2 = 75+72 | `math_1_data.js` | Pending |
| 5 | Nazera | `1st/1st Nazera/PDF/Nazera book 1 KPTBB.pdf` (62) | — | `nazira_1_data.js` | Pending |
| 6 | Pashto | `1st/1st Pashto/PDF/Pashto book 1 KPTBB.pdf` (88) | KPTBB1/2pdf = 45+44 | `pashto_1_data.js` | Pending |

### Class 2
| # | Subject | PDF (pages) | Data file | Status |
|---|---|---|---|---|
| 1 | Drawing | `2nd/2nd Drawing/PDF/Drawing  Book for 2 class KPTBB.pdf` (34) | `drawing_2_data.js` | Pending |
| 2 | English | `2nd/2nd English/PDF/English Book for 2 class KPTBB.pdf` (138) | `english_2_data.js` | Pending |
| 3 | GK | `2nd/2nd GK/PDF/GK Book for 2 class KPTBB.pdf` (102) | `gk_2_data.js` | Pending |
| 4 | Islamyat | `2nd/2nd Islamyat/PDF/Islamiat Book for 2 class KPTBB.pdf` (58) | `islamyat_2_data.js` | Pending |
| 5 | Maths | `2nd/2nd Maths/PDF/Math Book for 2 class KPTBB.pdf` (167) | `math_2_data.js` | Pending |
| 6 | Nazira | `2nd/2nd Nazira/PDF/2nd Nazira.pdf` (91) | `nazira_2_data.js` | Pending |
| 7 | Pashto | `2nd/2nd Pashto/PDF/pashto 2nd.pdf` (34) | `pashto_2_data.js` | Pending |
| 8 | Urdu | `2nd/2nd Urdu/PDF/Urdu Book for 2 class KPTBB 1..4.pdf` (30×4=120) | `urdu_2_data.js` | Pending |

### Class 3
| # | Subject | PDF (pages) | Data file | Status |
|---|---|---|---|---|
| 1 | GK | `3rd/3rd  GK/PDF/GK Book for 3 class KPTBB 11/12/21/22.pdf` (33+33+33+34=133) | `gk_3_data.js` | Pending |
| 2 | Drawing | `3rd/3rd Drawing/PDF/Drawing Book for 3 class KPTBB.pdf` (33) | `drawing_3_data.js` | Pending |
| 3 | English | `3rd/3rd English/PDF/...11/12/21/22.pdf` (34+34+34+35=137) | `english_3_data.js` | Pending |
| 4 | Islamyat | `3rd/3rd ISlamyat/PDF/Islamiat Book for 3 class KPTBB.pdf` (88) | `islamyat_3_data.js` | Pending |
| 5 | Maths | `3rd/3rd Maths/PDF/Math book 3 class KPK_page_part_01..05.pdf` (37+41+43+39+33=193) | `math_3_data.js` + `math_3_book_text.js` | Pending |
| 6 | Nazira | `3rd/3rd Nazira/PDF/Nazira Book for 3 class KPTBB.pdf` (99) | `nazira_3_data.js` | Pending |
| 7 | Pashto | `3rd/3rd Pashto/PDF/Pashto Book for 3 class KPTBB.pdf` (150) | `pashto_3_data.js` | Pending |

### Class 4 — **NO IMPLEMENTATION EXISTS**
| # | Subject | PDF (pages) | Data file | Status |
|---|---|---|---|---|
| 1 | English | `4th/4th/English Book for 4 class KPTBB.pdf` (152) | — | Pending |
| 2 | General Science | `4th/4th/General Science Book for 4 class KPTBB.pdf` (149) | — | Pending |
| 3 | Islamiat | `4th/4th/Islamiat Book for 4 class KPTBB.pdf` (62) | — | Pending |
| 4 | Mathematics | `4th/4th/Math books 4 KPK.pdf` (188) | — | Pending |
| 5 | Pashto | `4th/4th/Pashto Book for 4 class KPTBB.pdf` (78) | — | Pending |
| 6 | Social Studies (EM) | `4th/4th/Social Study Book 4th EM KPK.pdf` (131) | — | Pending |
| 7 | Social Studies (UM) | `4th/4th/Social Study book 4th KPK.pdf` (136) | — | Pending |
| 8 | Urdu | `4th/4th/Urdu book 4th KPK.pdf` (166) | — | Pending |

### Class 5
| # | Subject | PDF (pages) | Data file | Status |
|---|---|---|---|---|
| 1 | English | `5th/5th English/PDF/English Book for 5 class KPTBB.pdf` (169) | `english_5_data.js` | Pending |
| 2 | General Science | `5th/5th General Science/PDF/General Sceince Book for 5 class KPTBB.pdf` (161) | `general_science_5_data.js` | Pending |
| 3 | Islamiat | `5th/5th Islamiat/PDF/Islamiat Book for 5 class KPTBB.pdf` (128) | `islamiat_5_data.js` | Pending |
| 4 | Mathematics | `5th/5th Maths/PDF/Math Book for 5 class KPTBB.pdf` (201) | `math_5_data.js` | Pending |
| 5 | Pashto | `5th/5th Pashto/PDF/Pashto Book for 5 class KPTBB.pdf` (188) | `pashto_5_data.js` | Pending |
| 6 | Social Studies (EM) | `5th/5th Social Study/PDF/Social Study Book 5th EM KPK.pdf` (125) | `social_studies_5_data.js` | Pending |
| 7 | Social Studies (UM) | `5th/5th Social Study UM/PDF/Social Study Book UM for 5 class KPTBB.pdf` (133) | `social_studies_um_5_data.js` | Pending |
| 8 | Urdu | `5th/5th Urdu/PDF/Urdu Book for 5 class KPTBB.pdf` (173) | `urdu_5_data.js` | Pending |

---

## FINDINGS LOG

### 2026-10-09
1. **All Class 1–5 PDFs are image scans.** `get_text()` returns only
   `awazeinqilab.com` advertising overlays; no textbook body text layer exists.
   Verification therefore requires OCR or visual page inspection.
2. **Class 4 is entirely absent from SpaceBook.** `DATA.subjects.cls4` lists
   six subjects, but no `*_4_data.js` file exists, no `<script>` tag wires Class 4
   content, and no Class 4 book entries route to real data. 8 textbook PDFs exist.
3. **Class 1 Drawing — CORRECTED.** All 32 activities verified against printed
   pages 1–32 (PDF pages 3–34). Titles/sequence correct. Four `teacherNote`
   strings and three titles had been paraphrased; replaced with the verbatim
   textbook wording after OCR + cropped visual confirmation of PDF page 31.

## REMAINING / NEXT
- Next page: Class 1 English, PDF page 1 (`English book 1  KPTBB.pdf`, 127 pages).

### 2026-10-09 (page-by-page vector infrastructure)
Per the standing directive (scan page-by-page; redraw every illustration as
inline SVG vector code — NOT pdf/jpg/png; build learning logic per page), the
reusable pipeline is now in place and the canonical example page is fully
implemented.

**New files (all load before `js/app.js`; registered in `tools/validate.js`):**
- `js/primary_page_art.js` — `PRIMARY_PAGE_ART` SVG registry (inline vector
  art, 320×320 viewBox, kid-friendly flat fills + heavy rounded strokes,
  house style matches `renderDrawingArtwork`). Helpers `primaryArtSvg(kind)` /
  `renderPrimaryArtwork(kind, label)`. Class 1 English Getting Started
  objects: `cat, hen, flowerpot, hat, net, sun, top, bed`.
- `js/english_1_pages.js` — `ENGLISH_1_PAGES` page model (one entry per
  printed page). Fully implements printed page 2 (PDF p7): verbatim
  "Getting Started / Look and say the names." + "Let's Talk" bullets, the 8
  figures (word + initial letter), and derived activities.
- `js/primary_page_learning.js` — `renderPrimaryPageView(classId, subjKey)`
  turns a page into (1) tap-to-name cards (reveal word + initial sound,
  SpeechSynthesis audio), (2) initial-sound quiz (which picture starts with
  this letter), (3) "name five objects" collection. Activities are generated
  from page data, not hard-coded.

**Wiring:** `index.html` loads the three scripts (before `app.js`); Class 1
English Lesson sub-tab bar gains a "🖼️ Page by Page (Vector)" button
(`switchLangLessonSubTab('eng','pages')` → `renderPrimaryPageView`).
`tools/validate.js` adds the three files to `DATA_FILES` + a load-order check.

**Verified:** all three files `node --check` clean, evaluate in a `vm` context
(8 art keys, 1 page, 8 figures, 15045-char view HTML with quiz + name-five),
and the wiring check (`srcs.indexOf(f) < srcs.indexOf('js/app.js')`) PASSES.

**Not ours (pre-existing, other agents' contended files):**
`tools/validate.js` crashes at line 152 (`sb.MATH_1_DATA.every(...)`) because
`math_1_data.js` chapters 2/4/5 lack `slos.mcqs/shortQuestions/longQuestions`.
Also `biology_12_data.js` and `phys_12_data.js` fail to load. None of these are
our files; do not revert.

**Next:** continue Class 1 English page by page (printed pages 3, 4, … following
the page map) — render each PDF page, transcribe text + objects, extend
`ENGLISH_1_PAGES` / `PRIMARY_PAGE_ART`. Then Islamyat → Maths → Nazera → Pashto,
then Classes 2, 3, build Class 4 from scratch, then Class 5.
