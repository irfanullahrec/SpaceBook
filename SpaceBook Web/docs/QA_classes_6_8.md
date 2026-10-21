# QA report: Classes 6, 7 and 8 (2026-10-21)

Scope: every book in `CLS6_BOOKS`, `CLS7_BOOKS`, `CLS8_BOOKS` plus Mathematics 6/7/8 (35 books). This is a **partial pass**. What was done, what was not, and why, is stated per check. Nothing here claims 100 %.

Tools added (re-runnable):
- `node tools/qa_cls678_scan.cjs [--json out.json]`: loads every data file and reports empty units/sections, questions without an answer, text defects (`**`, `$`, `||`, U+FFFD), wide tables, fixed-width SVGs.
- `tools/qa_layout_harness.js`: in-browser (load on `lazy.html`) overflow test per unit and tab: `await QA.run('cls7','hpe',{tabs:['lesson','exercise']})`.
- `docs/source-verification/class-7/tools/`: `fix_secs.py` (moves stacked `@sec` lines to their headings), `add_sols.py` + `list_unanswered.py` + `qa_show.py` (author answers into page files, then rebuild).

## 1. Proofreading against scans
- **Found and fixed (real defect): Class 7 HPE units 2-12 rendered empty.** Two `exercise` blocks (p014, p106) were never closed, so everything after them was swallowed. Fixed in the page files; rebuilt (`hpe_7_data.js`). 73 pages also had several `@sec` lines stacked at the top (157 of 275 sections were empty cards); moved to their headings (now 12 empty, 4 %). The same stacking was fixed in Class 7 Geography (11 pages) and History (4 pages).
- Cross-check of page-file line counts against built data for all 35 books: no other swallowed content.
- Builder OCR-recall check (English-medium books only; Urdu/Arabic/Pashto OCR is empty): pages with recall below 0.6 are listed in each `ledger.json` (c6 comp 27/28/32, drawing 67/82; c7 comp 21/35/36/43/64, drawing 50/71, geo 88/89, hist 4, sci 80/95/99). One spot-checked (c7 comp scan 34) matched the scan; the low score is screenshots.
- Spot-checked Class 7 HPE scans 35/36 (an exercise question cut off in the scan stays out, with an `@issue`).
- **Not done:** a page-by-page eye comparison of every page (about 12,000 pages). The re-verification of Class 8 Drawing (121), HPE (122) and Pashto (232) against scans was **not done**; only the structural scan above ran on them (no empty units, no swallowed content).
- Class 7 Pashto: no scans and no data (`pashto_7_data.js` does not exist). Cannot be checked or built.
- Builder warnings kept as open work: untranslated table/figure captions in Class 7 Geography, History and Computer (listed in the build output of `build_book7.py geo|hist|comp`).

## 2. Answers
- **Class 7 HPE: 158 of 160 questions now answered** (was 0). Left open: Ch.11 fill Q10 (post height) and Ch.12 fill Q8 (lane distance): the book text gives neither and the book has no key. Ch.4 short Q3 is cut off in the scan.
- **Class 7 Computer: 20 of 20 now answered** (was 0 for the two exercises; MCQs already had keys).
- Answers were written from the lesson text. The Pashto and Urdu wording is mine and has **not been reviewed by a native teacher**.
- Still without a stored answer (439 items, scan on built data): c6 eng 20, c7 eng 51, c7 sci 16, c7 urdu 4, c8 eng 97, c8 sci 60, c8 isl 20, c8 pashto 140, c8 urdu 29, c7 hpe 2. Almost all are open tasks (write a paragraph, explain verses, dictionary look-ups, draw/label diagrams, projects, listening) with no single correct answer. A minority are closed (matching, fill from a passage) and still need authoring.
- MCQs without a key: the scan reports 0 MCQ blocks lacking a solution id in these books; the Math MCQ gaps are tracked in `docs/test_prep_review/no_key.csv`.
- **Mathematics:** Class 6 has a worked solution for 1304 of 1344 question parts. Class 8 has an entry for every part, but they are **template stubs** ("Step 1 understand, Step 2 given, Step 3 result = the textbook key"), not worked steps. **Class 7 has none** (`MATH_7_SOLUTIONS` is empty): 1531 parts, 996 of which have a textbook key. Not fixed in this pass.

## 3. Page view (desktop / tablet / 375 px)
- Browser harness run at 375 px on a partial set before the preview pane closed: c7 HPE 0 issues; c6 Science 2, c6 English 12, c6 Urdu 8 (a table or box wider than the tab area; the tab area clips horizontally). One CSS hardening was added to `js/math6_reader.js` (long words wrap, SVG/images scale). It was **not re-measured**. Tablet and desktop were not run.
- The site header overflows at 375 px in the harness (search, coin chip): app chrome, outside this scope.
- Static scan: tables with more than 5 columns (Class 8 Urdu 25, Class 7 Science 9, Class 8 Pashto 6, others fewer), fixed-width SVGs above 420 px (c8 sci 67, c7 sci 8, c8 eng 5). Tables scroll inside their box; fixed-width SVGs are now scaled by the CSS above.

## 4-5. Word and sentence meanings
- Not extended in this pass. Current device coverage for these classes (from `docs/LEXICON_COVERAGE.md`): Class 6/7/8 English words 60 / 58 / 62 % of types and 97.9 / 97.8 / 97.8 % of occurrences have an Urdu meaning. The missing-word queues are `docs/lexicon_review/*.csv`. No new entries were added and no sentence translations were audited.

## 6. Animated solutions
- Only the status is reported above. No new animations were generated. Class 6: 829 of 1414 solutions animate (vr_auto). Class 8 stubs have one result row and do not animate. Class 7 has no solutions at all.

## Regeneration
`node tools/build/all.js` was run for the lazy page, manifest, search index and service-worker version (see the commit). Not pushed.

## Next steps (in order of value)
1. Class 7 Mathematics: build worked solutions (arithmetic, fractions, algebra, equations, roots can be generated and checked against the printed key; word problems need hand-written steps).
2. Replace the Class 8 stub solutions the same way.
3. Re-run the layout harness at 375/768/1280 once the browser pane is open; fix wide tables.
4. Closed English/Science/Urdu/Pashto/Islamiat questions (matching, fill-in) and native-speaker review of the new answers.
5. Meanings queue for these classes; scan-vs-page review of Class 8 Drawing, HPE, Pashto.
