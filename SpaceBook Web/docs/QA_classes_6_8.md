## RESUME HERE (top of report)
Done in this long pass: Class 7 Maths has an answer button on 1334 of 1531 parts (787 computed or hand-written worked solutions; 547 *Derived*: the printed key's answer is shown with the note "answer taken from the printed key, worked steps not computed"); Class 8 Maths: 554 of 1619 stubs replaced by worked solutions, the rest keep the key-verified template. Class 7 parts with no key and no solution (about 197) are drawings, graphs read from figures, text identification and a few unkeyed word problems.
Next: (1) non-Maths questions with no stored answer (list: `node tools/qa_cls678_scan.cjs --json tmp/qa_scan.json`, kinds `q-nosol`, `part-nosol`; author with `class-7/tools/add_sols.py`); (2) layout harness runs; (3) meanings queue; (4) page-by-page scan review of Class 8 Drawing/HPE/Pashto.

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
  - **Class 7: 772 of 1531 question parts now have a worked, animatable solution** (was 0). Families: fractions and BODMAS, reciprocals/inverses, squares and square roots by factorisation, factorise/expand/identities, linear equations, sets (finite), ratio/proportion/profit/tax/Zakat, circle and cylinder formulas, speed/time/unit conversions, mean/median/mode, many word problems.
  - **Class 8: 554 of 1619 parts** had their template stub replaced by a real worked solution (simultaneous equations, cube/square roots, polynomial division, exponent laws, terminating decimals, absolute value, subsets, factorise). The other 1101 still show the old template (it is key-verified but not a worked solution). `apply_gen8.py` rewrites `js/math_8_solutions.js` (the stub file has no source in the repo, so rebuilding `build_math8.py` would drop it; use `apply_gen8.py` after any rebuild).
  - **Class 6: unchanged** (1304 of 1344 parts already solved).
  - **Printed-key errors found by the engine** (computed answer correct, key differs; the solution shows a note "the printed key shows X"): Class 7 about 40 items, for example 4.1 Q4a/c (58.85 and 89.375 min), 4.3 Q3/Q6/Q7, 4.4 Q9, 5.1 Q6/Q7, 5.2 Q1b, 7.4 Q10b/e, 9.2 Q1c/2f/3d, 9.5 Q1e, 10.2 Q2-3 (a.m./p.m. swapped), and Class 8 Chapter 7 exponent answers print `?` in place of every exponent (unreadable in the scan; the engine supplies them). The full mismatch list is in `tmp/disc7.json` / `disc8.json` when the engine is run.
  - **Left open (not computable by the engine):** drawing, graph plotting, constructions, number-line and Venn diagrams, text identification (polynomial or number classification), set-builder form, currency conversion (needs rates), word problems not yet authored, and every item whose printed key is missing and whose wording is ambiguous. Class 7: 759 parts; Class 8: 1065 parts.

## 3. Page view (desktop / tablet / 375 px)
- Browser harness run at 375 px on a partial set before the preview pane closed: c7 HPE 0 issues; c6 Science 2, c6 English 12, c6 Urdu 8 (a table or box wider than the tab area; the tab area clips horizontally). One CSS hardening was added to `js/math6_reader.js` (long words wrap, SVG/images scale). It was **not re-measured**. Tablet and desktop were not run.
- The site header overflows at 375 px in the harness (search, coin chip): app chrome, outside this scope.
- Static scan: tables with more than 5 columns (Class 8 Urdu 25, Class 7 Science 9, Class 8 Pashto 6, others fewer), fixed-width SVGs above 420 px (c8 sci 67, c7 sci 8, c8 eng 5). Tables scroll inside their box; fixed-width SVGs are now scaled by the CSS above.

## 4-5. Word and sentence meanings
- Not extended in this pass. Current device coverage for these classes (from `docs/LEXICON_COVERAGE.md`): Class 6/7/8 English words 60 / 58 / 62 % of types and 97.9 / 97.8 / 97.8 % of occurrences have an Urdu meaning. The missing-word queues are `docs/lexicon_review/*.csv`. No new entries were added and no sentence translations were audited.

## 6. Animated solutions
- The generated solutions carry one TeX row per step (`m`), so `vr_auto` offers the "Animate" button on them (checked in the browser for Class 7 5.3 Zakat). Class 7: 772 new animatable solutions; Class 8: 518 replaced stubs; Class 6: 829 of 1414 as before. Not converted: the open items listed under Mathematics, and Science numericals (no step data exists to animate).

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
- Last commit of this pass: 838a595f (later commits: Class 7 772, Class 8 518). Nothing pushed. Shared files (lazy, manifest, search, service worker, index.html) are untouched since the regeneration listed above.

## Written by hand but not verified (figure- or drawing-dependent)
These solutions give the method (construction steps, graph table of values and features, proof reasoning). They depend on a figure or a drawing that was not checked against the book, so each ends with the line "Not verified". Constructions include a feasibility check (triangle inequality, hypotenuse longer than the side, and so on); where the data make the figure impossible the solution says so (for example Class 7 12.4 Q3: 3 + 2.5 < 6; Class 8 10.4 Q1 b and f).
- Class 7: 8.6 Q1 (a,b,c,d,e,f); 8.6 Q2 (a,b,c,d,e,f,g,h); 8.6 Q3 (a,b,c,d,e,f,g,h); 8.7 Q1 (a,b,c,d,e,f,g,h,i,j,k,l); R8 Q12 (a,b,c,d); R8 Q16 (a,b,c,d); R8 Q17 (a,b,c,d); R8 Q18 (a,b,c,d); 12.4 Q1; 12.4 Q2; 12.4 Q4; 12.4 Q5; 12.4 Q6; 12.4 Q7; 12.4 Q8.
- Class 8: 10.4 Q1 (a,b,c,d,e,f); 10.4 Q2 (a,b); 10.4 Q3 (a,b,c,d,e); 10.4 Q4 (a,b,c,d,e); 10.5 Q1 (i,ii,iii); 10.5 Q2; 10.5 Q3; 10.5 Q4 (i,ii); 10.5 Q5 (i,ii); 10.5 Q6 (i,ii); 8.9 Q2 (a,b,c,d,e,f,g); 8.9 Q3 (a,b,c,d,e,f); 8.9 Q4 (a,b,c,d,e,f); 10.10 Q3 (a,b); 10.10 Q6; 10.10 Q2.
Generators: `class-7/tools/gen_graphs.py 7|8` (graphs) and `gen_constr8.py` (Class 8 constructions); Class 7 constructions are in `class-7/math/dsl/u12_constr.txt`, Class 8 proofs in `class-8/math/dsl/u10_proofs.txt`.

## More printed-key mismatches
Class 8 6.9 Q4 (x² + 1/x² = 18 when x − 1/x = 4; key 6), Class 8 6.9 Q12 (p⁴ + 1/p⁴ = 898 when p² + 1/p² = 30; key 806402), Class 7 13.7 Q1 (key lists "zero (impossible)" under b and 13/20 under c; the correct order is b = 13/20, c = 0).

## Derived non-Maths answers (written from general knowledge or the lesson summary; to be checked by a teacher)
- Class 8 Islamiat: 16 open parts answered (Lessons 1.3 destiny, 3 fear of Allah, 7.3 purpose of worship, 12.1 purdah, 20.2 Imam Hussain, 25.1 enjoining good). Not answered: u23 MCQs d/e (options cut off), u19 Q2 and u24 Q4 tables.
- Class 8 General Science: 14 open parts answered (yoghurt activity 4.1, Bt corn, space short questions). Derived: Sun's motion speed (about 220 km/s). Not answered: figure/experiment-dependent parts (reaction-time table, periodic-table questions, ray diagrams, projects).
- Meanings: a sample of 141 words from the Class 6-8 slice of `docs/lexicon_review/en_to_ur.csv` was drafted as curated entries; `check_curated.js` showed 137 were already in the curated lists, so the review CSV is stale relative to `docs/lexicon/curated/`. No entries were added. The true missing-word list needs a fresh `make_lexicon.js` + `lexicon_report.js --write` (shared files; not run by this pass).
- Scan spot checks (this pass): Class 8 Drawing scans 10 and 11 and HPE scan 30 matched their page files (including the book's own oddities). Class 8 Pashto scan 60 shows the full story text where the page file carries a summary ("لنډیز"): this is the project's copyright rule for modern authors, not a transcription error. Not done: the full page-by-page comparison of the 475 pages.
- Scanner correction: a question whose sub-parts follow in a separate block is now counted as answered; the open count is about 390, almost all open-ended (writing, dictionary, listening, projects).
- Layout fix found by the harness at 375 px: the pill-shaped box titles of the book skin (`.c1-skin .m6-box-t`, `white-space:nowrap`, positioned absolute) stuck out of the page for long titles (Class 6 English units 4 and 8, similar in other books). Added a higher-specificity rule in `js/math6_reader.js` (`.m6-root.c1-skin .m6-box-t{white-space:normal;max-width:...}`); the same rule injected in the browser removed all overflow in Class 6 English unit 4. The cause is in `js/sb_book_skin.js` (shared, has uncommitted edits by another session; not touched). The page must be regenerated (lazy hashes) for the fix to ship.
- Second layout finding (375 px): the chapter-title row `.mch-titles` (inline `white-space:nowrap;overflow:hidden` in `js/app.js`) hides the end of long titles. Override added in `js/math6_reader.js` (wrap). `js/app.js` is shared and was not edited. Layout run (lesson tab only, 375 px, Class 6 books so far): only these two causes appeared; Classes 7 and 8 were still running when this note was written.

## Next steps (in order of value)
1. More Mathematics solutions: author the remaining word problems in `class-N/math/dsl/*.txt` (one line per part: TeX rows + `=> answer`, checked by the engine), then `python msol_run.py N` and, for Class 8, `python apply_gen8.py`; Class 7 needs `python build_math7.py`.
2. Re-run the layout harness at 375/768/1280 once the browser pane is open; fix wide tables.
3. Closed English/Science/Urdu/Pashto/Islamiat questions (matching, fill-in) and native-speaker review of the new answers.
4. Meanings queue for these classes; scan-vs-page review of Class 8 Drawing, HPE, Pashto.
5. Class 8 Chapter 7 printed answers show `?` for exponents: re-read the key pages in the scans and fix the Class 8 Maths answer pages.
