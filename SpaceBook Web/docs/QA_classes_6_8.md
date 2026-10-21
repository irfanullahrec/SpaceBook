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
- **Mathematics (updated 2026-10-21, second pass).** A worked-solution engine was built (`docs/source-verification/class-7/tools/msol*.py`, run with `python msol_run.py 7|8`). Every solution is **computed** (exact fractions / sympy) and checked against the printed key; one that disagrees is not emitted. Hand-authored rows (`class-N/math/dsl/*.txt`) are chain-checked (each `=` step must agree numerically).
  - **Class 7: 714 of 1531 question parts now have a worked, animatable solution** (was 0). Families: fractions and BODMAS, reciprocals/inverses, squares and square roots by factorisation, factorise/expand/identities, linear equations, sets (finite), ratio/proportion/profit/tax/Zakat, circle and cylinder formulas, speed/time/unit conversions, mean/median/mode, many word problems.
  - **Class 8: 466 of 1619 parts** had their template stub replaced by a real worked solution (simultaneous equations, cube/square roots, polynomial division, exponent laws, terminating decimals, absolute value, subsets, factorise). The other 1153 still show the old template (it is key-verified but not a worked solution). `apply_gen8.py` rewrites `js/math_8_solutions.js` (the stub file has no source in the repo, so rebuilding `build_math8.py` would drop it; use `apply_gen8.py` after any rebuild).
  - **Class 6: unchanged** (1304 of 1344 parts already solved).
  - **Printed-key errors found by the engine** (computed answer correct, key differs; the solution shows a note "the printed key shows X"): Class 7 about 40 items, for example 4.1 Q4a/c (58.85 and 89.375 min), 4.3 Q3/Q6/Q7, 4.4 Q9, 5.1 Q6/Q7, 5.2 Q1b, 7.4 Q10b/e, 9.2 Q1c/2f/3d, 9.5 Q1e, 10.2 Q2-3 (a.m./p.m. swapped), and Class 8 Chapter 7 exponent answers print `?` in place of every exponent (unreadable in the scan; the engine supplies them). The full mismatch list is in `tmp/disc7.json` / `disc8.json` when the engine is run.
  - **Left open (not computable by the engine):** drawing, graph plotting, constructions, number-line and Venn diagrams, text identification (polynomial or number classification), set-builder form, currency conversion (needs rates), word problems not yet authored, and every item whose printed key is missing and whose wording is ambiguous. Class 7: 817 parts; Class 8: 1153 parts.

## 3. Page view (desktop / tablet / 375 px)
- Browser harness run at 375 px on a partial set before the preview pane closed: c7 HPE 0 issues; c6 Science 2, c6 English 12, c6 Urdu 8 (a table or box wider than the tab area; the tab area clips horizontally). One CSS hardening was added to `js/math6_reader.js` (long words wrap, SVG/images scale). It was **not re-measured**. Tablet and desktop were not run.
- The site header overflows at 375 px in the harness (search, coin chip): app chrome, outside this scope.
- Static scan: tables with more than 5 columns (Class 8 Urdu 25, Class 7 Science 9, Class 8 Pashto 6, others fewer), fixed-width SVGs above 420 px (c8 sci 67, c7 sci 8, c8 eng 5). Tables scroll inside their box; fixed-width SVGs are now scaled by the CSS above.

## 4-5. Word and sentence meanings
- Not extended in this pass. Current device coverage for these classes (from `docs/LEXICON_COVERAGE.md`): Class 6/7/8 English words 60 / 58 / 62 % of types and 97.9 / 97.8 / 97.8 % of occurrences have an Urdu meaning. The missing-word queues are `docs/lexicon_review/*.csv`. No new entries were added and no sentence translations were audited.

## 6. Animated solutions
- The generated solutions carry one TeX row per step (`m`), so `vr_auto` offers the "Animate" button on them (checked in the browser for Class 7 5.3 Zakat). Class 7: 714 new animatable solutions; Class 8: 466 replaced stubs; Class 6: 829 of 1414 as before. Not converted: the open items listed under Mathematics, and Science numericals (no step data exists to animate).

## Regeneration still needed (owner / final phase; not done by this pass)
I have stopped regenerating shared files. The last commits of this pass did include a regenerated `lazy.html`, `content/lazy_manifest.json`, `content/offline_map.json` and `content/sw_version.js`; they are stale again after any further data change below.
- Book data changed after that regeneration: `js/math_7_data.js`, `js/math_7_solutions.js`, `js/math_8_solutions.js`, `js/hpe_7_data.js`, `js/computer_7_data.js`, `js/geography_7_data.js`, `js/history_7_data.js`, `js/math6_reader.js`.
- To do once, from a clean checkout: bump the `?v=` keys of the changed data files in `index.html`, then `node --max-old-space-size=8192 tools/build/all.js` (lazy, search, offline map, service-worker version, word stats, MCQ bank).
- `all.js` failed at the `search` step in this working tree (the uncommitted Class 1/2 reader files, `js/cls1_book_reader.js` and `js/english_1_book.js`, look like the cause). The search index was not regenerated; Class 7 solutions load lazily and do not feed it, but the Class 7 Computer/HPE answers do.
- After any `build_math8.py` run, run `python docs/source-verification/class-8/tools/apply_gen8.py`.

## Class 8 Unit 3: answers that differ from the printed key (computed answer shown; solution carries a note)
3.1 Q8 (27000 cm³, key 22500), Q9 (4 workers, key 16), 3.2 Q2 (Rs 9,990,000, key 9,910,000), Q6 (Rs 43,890, key 39,501), 3.4 Q1 (16.67 days, key 16 1/3), Q4 (144 men, key 243), Q5 (son Rs 87,500 / daughter Rs 43,750, key daughter 4375). Not authored because the key and wording conflict: 3.2 Q9, 3.3 Q5-Q7, 3.4 (see `class-8/math/dsl/u3.txt` for what was written). Units 4 and 9: 4.2 Q6 (perimeter x rate = Rs 177,480, key Rs 44,370), 9.1 Q5 (17 m, key sqrt 161), Q6 (2.408 m, key 2408).

## Where to resume
- Run: `cd docs/source-verification/class-7/tools && python msol_run.py 7` (or `8`), then Class 7 `python build_math7.py`, Class 8 `python ../../class-8/tools/apply_gen8.py`. Leaf dumps come from `node tmp/mdump.cjs 7|8` (writes `tmp/mN_leaves.json`; recreate `tmp/mdump.cjs` from the description in `msol_run.py` if `tmp/` was cleaned).
- Author new rows in `class-7/math/dsl/*.txt` and `class-8/math/dsl/*.txt` (`ex|q|part ~ TeX rows ;; ... => answer`, append `!!` to emit with a key note, `%%` to skip the key check).
- Done: Class 7 Units 2-5, 7, 9, 10 and part of 8, 12, 13; Class 8 Units 1 (rounding), 2-4 (engine), 7-8 (engine), 9.1/9.5, 11.2.
- Resume with: Class 7 Units 6 (infinite sets), 11, 12, 13 (tables, graphs); Class 8 Units 6, 7 (exponent word items), 8, 10, 11.
- Last commit of this pass: 838a595f (Class 7: 714, Class 8: 466). Nothing pushed. Shared files (lazy, manifest, search, service worker, index.html) are untouched since the regeneration listed above.

## Next steps (in order of value)
1. More Mathematics solutions: author the remaining word problems in `class-N/math/dsl/*.txt` (one line per part: TeX rows + `=> answer`, checked by the engine), then `python msol_run.py N` and, for Class 8, `python apply_gen8.py`; Class 7 needs `python build_math7.py`.
2. Re-run the layout harness at 375/768/1280 once the browser pane is open; fix wide tables.
3. Closed English/Science/Urdu/Pashto/Islamiat questions (matching, fill-in) and native-speaker review of the new answers.
4. Meanings queue for these classes; scan-vs-page review of Class 8 Drawing, HPE, Pashto.
5. Class 8 Chapter 7 printed answers show `?` for exponents: re-read the key pages in the scans and fix the Class 8 Maths answer pages.
