# BISE Swat (bisess.edu.pk) alignment — what was built, what it rests on, what is still open (2026-10-20)

The Board of Intermediate & Secondary Education, Saidu Sharif Swat publishes, for its SSC and HSSC students, a paper pattern, a table of specification and a model paper with a marking scheme for each subject, the National Curriculum with Student Learning Outcomes (SLOs), the Scheme of Studies, a sample e-answer sheet (answers are marked on a screen) and printed papers on its "E-Marking" page. SpaceBook now shows all of that where a Class 9-12 student studies. Nothing existing was restructured: the new module only adds to pages that already exist.

## 1. What the student sees

| Where | What | Code |
|---|---|---|
| Subject list of Class 9, 10, 11 or 12 | a green card "BISE Swat Board centre" | `classBanner` in `js/sb_bise.js` (hook on `goToSubjects`) |
| Top of every chapter the Board examines (Physics, Chemistry, Biology, Maths, Computer Science, Pakistan Studies; Class 9-12) | a strip: weightage %, MCQ / short / long items, "🎯 n/N SLOs" (tick-list), "Board centre ▸" | `insertStrip` (hooks on `renderSubjectChapterView`, `renderMathChapter`) |
| **Board centre** page (`SBBise.open(subjectId, tab)`) | six tabs, below | `js/sb_bise.js`, `css/sb_bise.css` |
| Papers | a bar "BISE Swat pattern for <subject>" and a button that sets the paper builder to the Board's sections, marks, time, header and bubble (OMR) response sheet, then fills it from the book | `applyPaperPreset`, `paperBanner` (hooks on `renderPapersView`, `onPaper*Select`, `renderLiveExamPaperHtml`) |

Board centre tabs: **Pattern & marks** (Section A / B / C boxes, time, total, chapter weightage table with bars and a link to each chapter), **Chapters & SLOs** (accordion, tick-list kept in this browser, search, "only not done", "Study next" = highest weightage x least done), **Board papers** (the Board's own model paper, marking scheme, table of specification, curriculum, past printed paper; dead links are shown as dead), **Practice** (Section A timed drill: 12 / 15 / 18 / 20 MCQs in 15-20 minutes from the books' MCQ bank, score and review; links to Tests Preps and Papers), **Answer sheet** (title page with roll-number bubbles, subject and class bubbles, the Board's ten rules in English and Urdu, a printable practice booklet with 1 page per Section B question and 3 per Section C question), **Scheme of Studies** (the 2019 tables for the student's group).

Rules kept: no language tabs; nothing that is not from a book is labelled a Board question (the Board's papers are only linked, the drill and the preset use the app's own books); progress stays on the device (`localStorage sbBise:v1:<user>`); no request leaves for anything but the Board's own links.

## 2. What it rests on (`docs/source-verification/bise-swat/`)

- `tools/fetch_sources.py` downloads the ~100 PDFs and 12 images the Board links, `tools/check_links.py` asks its server whether each link works (note: the server answers 403 to a browser-like User-Agent; both tools use `curl/8.4.0`), `tools/extract_slos.py` reads the National Curriculum text into `data/slos_*.json`, `tools/dump_app_chapters.js` records the chapters the app shows, `tools/build_bise.py` joins everything into **`js/bise_swat_data.js`** (generated, ~400 KB, loaded on first use).
- Hand-transcribed from the Board's page images, and checked: `data/tos_tables.json` (chapter weightage and MCQ / short / long item counts; every table adds up to the Board's own totals, e.g. Physics 9 = 12 MCQ, 11 short, 4 long; Chemistry 11 = 18 / 13 / 8) and `data/patterns.json` (sections, choice, marks, time, from the model papers). `tests/bise/data.js` re-checks all sums.
- Learning outcomes (SLOs), by where they come from (`sloSrc` in the data; the Board centre says which on every subject):
  - **`curriculum`** (the Board's National Curriculum PDFs): Physics, Chemistry, Biology and Pakistan Studies for Classes 9-10; Mathematics 9-12; English skill groups; Computer Science 9-12 (about 2,400 entries).
  - **`textbook`** (the Board publishes none for these, so the outcomes **printed in the app's own KPTBB textbook** at the start of each unit are used; `tools/extract_book_slos.js` renders every chapter in the app and `tools/build_book_slos.py` keeps the outcome list): Physics, Chemistry and Biology 11-12 (Biology 12 prints none), Urdu 10 (per lesson, Urdu with English), Urdu 11-12 (whole-book outcomes plus a few lessons), Mutalia-e-Quran 9-10, Islamiat Elective 9-10.
  - **`headings`** (the book prints no outcomes): a topic checklist of the book's own section headings: Biology 12, Pakistan Studies 12, Islamiat 9-11, Urdu where a lesson has none, and Biology 11 "Acellular life".
  - Nothing in `textbook` or `headings` was written by me; each line is the book's own text, so it can carry the book's own typos. They are not the Board's SLO list and the page says so.
- Class 9-10 Mathematics: the curriculum numbers units 1-30 across both years; `MATH9` / `MATH10` in `build_bise.py` map them to the 17 and 13 chapters of the textbooks (the Board's tables use the same chapters).

## 3. Findings the owner should know

1. **Class 9 Computer Science is a different book.** The Board examines Class 9 on Fundamentals of Computer, Operating System, Office Automation, Data Communication, Networks and Security (plus a 20-mark practical); the app's Class 9 Computer Science is the Programming (C) book, which the Board examines in Class 10. The Board centre says so on that subject and shows the Board's six units and their SLOs as "not in the app". Which book is right is the owner's call.
2. **General Mathematics (Classes 9 and 10) is a Board subject the app does not have.** The Board centre lists it with its files and chapter table, marked "not yet a book in this app".
3. **Four of the Board's own links do not work** (checked 2026-10-20): the Class 11 Biology model paper (404) and the three Class 11 Islamiat files (403). The Board centre shows them as dead. Re-run `tools/check_links.py` and `tools/build_bise.py` to refresh.
4. **The Board's own numbers disagree in places**: Class 12 English Table of Specification totals 110 marks while its model paper sets 100; Class 12 Biology chapter percentages add up to 92.8 % while its section totals add up to 100 %. The app shows what the Board printed and says which source it used.
5. The sample e-answer sheet and the "E-Marking (Model Papers)" page are for marking: the answer-sheet tab teaches the student the layout and rules; on-screen marking itself (teachers register as e-markers) is only linked.

## 4. Not done / not verified

- **Not checked in a real phone or with a screen reader**; checked in the built-in browser pane (desktop width), in the Node sandbox and by `tests/bise/data.js`.
- No Board **unit tables** (chapter weightage) for Urdu, Islamiat, Mutalia-e-Quran: their tables are by skill or by Board unit, not by textbook chapter, and are Urdu-language scans; their paper patterns are read from page images. Class 11 Islamiat: the Board's files are dead, so no pattern.
- The SLO text is read from PDFs by script: lists such as Computer Science "following types of ..." are joined into one outcome, and some Maths formulas lose their symbols. The counts differ slightly from the Board's own "No. of SLOs" (e.g. Computer Science 9: 64 read, 76 printed).
- Per-question answers and the Board's rubrics are **linked, not copied**; copying them needs the Board's permission.
- Past papers: the "E-Marking" page's 12 images (English, Chemistry, Physics, Classes 9-12) are linked, not transcribed.
- Section A drill: needs at least 4 MCQs with an answer key for the subject; Class 11 books have no keys in the MCQ bank, so the drill says so there.
- Practical marks (Class 9-10: 10 per science subject, Computer Science 20; Class 11-12: 15) are shown in the Scheme of Studies but are not part of any pattern box.

## 5. How to refresh

```
cd "SpaceBook Web/docs/source-verification/bise-swat"
python -X utf8 tools/fetch_sources.py                       # sources/ (git-ignored) + txt8/
python -X utf8 tools/check_links.py                         # data/link_status.json
python -X utf8 tools/extract_slos.py sources/txt8 data      # data/slos_*.json (Board curriculum)
node --max-old-space-size=6144 tools/extract_book_slos.js raw.json                  # renders the app's books (outcomes printed in the textbooks)
python -X utf8 tools/build_book_slos.py raw.json data/slos_book.json               # data/slos_book.json
node --max-old-space-size=8192 tools/dump_app_chapters.js data/app_chapters.json   # only when the app's chapters changed
python -X utf8 tools/build_bise.py data/page_syllabus_2026-10-20.html              # js/bise_swat_data.js
node tests/bise/data.js
```
Then the usual generated files (`node --max-old-space-size=8192 tools/build/all.js`, from a clean checkout; `tests/hooks/hooks.js --update` if the hooks changed).
