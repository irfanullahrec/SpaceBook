# QA, all classes (2026-10-22): measured audit, first pass

**Status: Part A partly measured, Part B barely started. This is NOT a completion report.** Resume point is at the end of this file.
Other chats were still committing page proofreading while this ran (`git log` showed commits seconds apart), so the final regeneration was **not** run.

## What was measured in this pass
`tools/qa/audit_all.js` (new, generalises `audit_c9_c10.js` to every `CLSn_BOOKS` plus all `CLSn_SOLUTIONS` stores) was run with `node --max-old-space-size=6144 tools/qa/audit_all.js --json out.json`; the full per-book result is `tools/qa/audit_all_latest.json`. It covers Classes 1-10 and Class 12 Maths/Statistics (the only Class 12 page books). **Class 11 and the other Class 12 books use older data shapes and were not covered by it.**

| Class | Books | Pages | Question leaves | With stored answer | MCQs | MCQs w/o key | KaTeX errors | MCQ key/option mismatches | Empty pages | Not verified | Derived |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 8 | 510 | 1320 | 1319 | 17 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 8 | 951 | 2031 | 2001 | 44 | 0 | 0 | 3 | 0 | 0 | 0 |
| 3 | 8 | 904 | 1791 | 1703 | 56 | 0 | 1 | 0 | 1 | 0 | 0 |
| 4 | 8 | 1297 | 3460 | 3108 | 116 | 0 | 15 | 1 | 4 | 0 | 0 |
| 5 | 7 | 1221 | 2878 | 2701 | 72 | 0 | 6 | 0 | 0 | 0 | 0 |
| 6 | 12 | 1889 | 3763 | 3741 | 253 | 0 | 0 | 0 | 4 | 0 | 3 |
| 7 | 11 | 1699 | 3469 | 3430 | 325 | 0 | 0 | 2 | 13 | 1 | 0 |
| 8 | 12 | 1878 | 3100 | 1743 | 286 | 17 | 0 | 0 | 7 | 58 | 12 |
| 9 | 11 | 2311 | 4408 | 2966 | 720 | 0 | 287 | 16 | 14 | 0 | 9 |
| 10 | 12 | 2741 | 3099 | 2167 | 357 | 0 | 295 | 12 | 8 | 0 | 0 |
| 12 | 2 | 584 | 975 | 282 | 135 | 135 | 6 | 0 | 17 | 0 | 0 |

Book-level notes from the same run (see the JSON for every book):
* Class 12 Statistics: 0 of 590 leaves carry a stored answer and 90 of 90 MCQs have no key; Class 12 Maths: 45 of 45 MCQs have no key, 282 of 385 leaves answered. These are the biggest answer gaps measured.
* Class 8: 1,743 of 3,100 leaves have a solId. Lowest: HPE 0/127, Drawing 3/45, Computer 33/72, History 52/102, Geography 53/102, Islamiat 118/300, Quran 125/400, Science 126/247, Pashto 140/394. Many of these are not questions (tables, activities), so the count is an upper bound on the gap; it was not hand-sorted.
* Class 9/10/12 Maths and Class 12 Stat show 0 stored answers in the page-book store because their answers live in separate `sol_m*` / `math_*_solutions` stores; those books are covered by the animation tools below, not by this table.
* The Class 5 "solution missing" figure that the first run printed (2,701 ids) was a loader bug (Class 5 uses `CLS5_SOLUTIONS`); fixed, now 0 missing across all classes.
* KaTeX errors: all 287 (Class 9) and 295 (Class 10) are Computer Science code listings containing `$`, as the Class 9/10 report said; the real formula errors are Class 4 (15, 7+8), Class 5 (6), Class 3 (1), Class 12 Maths (6). Not yet fixed.
* Not-verified labels: Class 8 has 58, Class 7 has 1. Derived labels: Class 8 12, Class 9 9, Class 6 3.

Animations (re-run `tools/qa/vr_coverage_c9_c10.js`): Class 9 Maths 655 items, 109 hand packs, 546 auto-animatable, 0 without animation; Class 10 Maths 635 items, 260 packs, 375 auto, 0 without. Class 12 Maths `unanimated.js` still lists items (e.g. the continuity and triangular-pool problems in `math_12_data.js`); the 82-item figure from the earlier report was not re-counted. Class 12 Statistics was not measured.

Words: `docs/LEXICON_COVERAGE.md` (existing generated file, not regenerated here) gives English-to-Urdu 35.2 % of types / 96.0 % of occurrences, English-to-Pashto 32.1 % / 95.6 %, English-to-Arabic 30.3 % / 95.4 %; the owner targets (95 % tokens, Arabic 85 %) are met for English by token share, not for Pashto/Urdu source words (91-94 %).

## Part B done in this pass
* Template-generated filler exercises removed at generator level: `tools/build_pakstudy_12_from_docx.py` and `tools/build_economics_12_from_docx.py` now emit no template MCQ/short/long questions, and `tools/qa/strip_template_exercises.py` applied the same to `js/pakstudy_12_data.js` (22 blocks) and `js/economics_12_data.js` (24 blocks). The filler string `علمِ فلکیات` is now 0 occurrences in both files (commit `98119ab9`). Printed exercises were not touched (only the blocks whose first MCQ is the template one were cleared).
* Checked the other two files named in the brief: `ikhtiari_11_data.js` (5) and `islamiat_ikhtiari_12_data.js` (8) contain `علمِ فلکیات` only in real book text about astronomy, not as a template distractor, so nothing was removed. The remaining hits (`islamiat_ikhtiari_10_data.js`, `urdu_8_data.js`) were not checked.
* Machine-translation job NOT restarted: free RAM was about 0.9 GB at the check (needs more than 1.5 GB). Resume with the exact command in `docs/QA_classes_11_12.md`, then rename the output to `sentences_mt_1112.jsonl`.

## Not done (so nothing here may be called complete)
1. Proofreading: no new page-by-page comparison in this pass. Per the four reports, only partial: Class 1-2 full, Class 3 Maths and GK, Class 8 HPE and Pashto, Class 9 Maths pp5-22, Class 11/12 partial. Still open everywhere else.
2. Layout harness at 375/768/1280 with cache bypass: not run (needs the browser harness and several hours); the Class 6-8 report says 375/768 done, 1280 partial.
3. Sentence-meaning gaps per book, word gaps per book: not re-measured.
4. Answer spot-checks (5 per book): not done.
5. Class 12 Stat/Maths MCQ keys (135 MCQs) and the Class 12 Maths unanimated items.
6. Final regeneration, `tools/validate.js`, hooks tests, the browser re-verification: not run, because other chats were still committing and a clean regeneration needs them idle.

## Final table (class x check): honest status
Legend: P = partly done (numbers above or in the class report), B = blocked, ? = not measured in this pass.

| Class | 1 Proofread | 2 Answers | 3 Layout | 4 Words | 5 Sentences | 6 Animations |
|---|---|---|---|---|---|---|
| 1 | P (Eng/Math/Isl full OCR; rest sampled) | P: 1319/1320 leaves; Urdu+GK sources missing (B) | ? | P | P | P arithmetic |
| 2 | P: fully done per report | P: 2001/2031 | ? | P | P | P |
| 3 | P: Maths, GK, part Nazira | P: 1703/1791 | ? | P | P | P |
| 4 | P | P: 3108/3460 | ? | P | P | P (fractions) |
| 5 | P | P: 2701/2878 | ? | P | P | P |
| 6 | P | P: 3741/3763; pp157-158 missing (B) | P (375, 768) | P | P | P |
| 7 | P; Pashto no scans (B) | P: 3430/3469, 1 Not verified | P | P | P | P (9 printed-key-only) |
| 8 | P: Math, HPE, Pashto, Eng done | P: 1743/3100 raw; 58 Not verified, 17 MCQs w/o key | P | P | P | P (7 stubs, figures unreadable: B) |
| 9 | P: Maths pp5-22 only | P: MCQ keys 0 missing; p137 Eng, p52 Pak Studies missing (B) | ? | P | P | done for Maths: 0 unanimated of 655 |
| 10 | P | P | ? | P | P | done for Maths: 0 unanimated of 635 |
| 11 | P | ? (no printed keys in several books; not in this audit's data shape) | ? | P | P (MT job stopped at 8,256/22,083) | P |
| 12 | P; HPE pp107,148 missing (B) | P: Maths 282/385, Stat 0/590, 135 MCQs w/o key | ? | P | P (same MT job) | P (Maths 82 left per report, Stat ?) |


## Update (second pass, same day)
* **Correction of the first pass.** Class 12 Statistics is NOT "0 of 590 answered": its answers are the printed key lines (`ans` entries), not per-question `solId`s, exactly like Class 9/10 Maths. `audit_all.js` now reports `keyEntries`: Stat 176, Class 9 Maths 487, Class 10 Maths 362. Of Stat's 252 exercise questions, 173 had a printed key; the 80 without are mostly definitions/explanations (no numeric answer). Three computational ones were answered and labelled `[Derived]` (1.6, 3.29, 6.11, in `stat/pages/p334.txt`). Left without any answer: 4.29 and 4.30 (data tables), 5.15 (random-number table), plus the theory questions. The 90 "MCQs without key" for Stat are covered by the printed key lines (e.g. `ans 1 | 1.3 | (i) c; ...`); the audit just cannot see them.
* **Class 12 Maths MCQ keys (45) and answers: blocked.** The Maths page book is reviewed only to scan 179 of 357 (printed answers start at 326), so the printed key is not in the data yet; another chat owns that book (the `class-12/math` and `class-12/stat` directories and their `js/` outputs are untracked in git, so I did not commit them).
* **KaTeX errors, Classes 3-5.** The reported strings were plain text lines (blanks `____`, URLs, `&`) typed as math blocks (`m`). Changed to paragraph lines in Class 3 English p050, Class 4 Maths pp028-030 and p184, Class 5 Science p004 and Class 5 English p002, then rebuilt (commit `bfde1223`). Not fixed: the 8 Class 4 English strings (blank-filling letters such as `depres__`), whose source is not in a `pages` directory.
* **Class 12 Maths KaTeX (6):** fixed the control character that had replaced `\cd` (`\cdot`) on p058 and the `\$` amounts on p079 (now `\mathdollar`) in `class-12/math/pages` (untracked, other chat's book). The prose `\$` on p064 is a checker false positive. The Maths build was rerun to `build/` only; `js/math_12_pagebook_data.js` was not overwritten.
* `js/statistics_12_book_data.js` was refreshed from its build (untracked file).

## Resume point
1. `node --max-old-space-size=6144 tools/qa/audit_all.js --json tools/qa/audit_all_latest.json` to refresh numbers.
2. Class 12 Stat/Maths MCQ keys and Stat answers, then the KaTeX errors in Classes 3-5, then the MT job when RAM allows, then layout harness runs, then the final regeneration when `git log -5 --format=%ar` shows no other chat committing.
