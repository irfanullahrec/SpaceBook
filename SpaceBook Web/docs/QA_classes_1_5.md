# QA — Classes 1 to 5 (2026-10-21)

Scope: every book in `CLS1_BOOKS` … `CLS5_BOOKS` (Class 1: 6 books, Class 2: 8, Class 3: 7, Class 4: 8, Class 5: 8).
This is a **partial** pass. The seven checks are very large for ~29 books (about 4,500 scanned pages); this report says exactly what was done, what was measured only, and what is open. Nothing below is claimed unless it was run.

## Tools added
- `tools/qa_cls15_scan.cjs` — structural scan of all Class 1-5 books (empty units, empty text, unbalanced `**` / `$`, control characters, wide tables, SVG without `viewBox` or with a fixed width, questions with no stored answer). `node tools/qa_cls15_scan.cjs --json out.json`.
- `docs/source-verification/class-4/tools/arith4.py` — inserts computed answers and step-by-step working (`solution` / `ss` / `sm` lines) after plain arithmetic questions that have no answer yet. `CLS=<n> python arith4.py math [--write] [--list]` works for any of Classes 1-5. Every value is computed by the script; it never touches word problems, patterns or fractions.

## 2. Answers
| Book | Result |
|---|---|
| Class 1 Math | Every plain-arithmetic item already has an answer (0 found by the new tool). |
| Class 2 Math | Same: 0 missing (parts are answered through the parent `qsolve`). |
| Class 3 Math | Same: 0 missing. |
| **Class 4 Math** | **Had no answers at all (0 of 1,181 question lines).** Now 827 answers: 70 computed plain-arithmetic items with 3-5 step working (all 70 animatable; all 70 agree with the printed key) plus 757 copied from the book's printed answer key (`class-4/tools/keyans4.py`, answers pages 173-181). |
| Class 5 Math | 2 items added (`100 × 100`, `1,000 × 10`); 955 → 957 solutions. |

**Still open (Class 4 Math):** ~43 stems remain without an answer: drawing, measuring, colouring, marking and labelling items (geometry unit 6, patterns, prime-colouring) which the key does not cover, and the parent stems of graph questions whose parts do have answers. Key entries with no question: Exercise 1 (page 5) and Exercise 2 (page 8) (those textbook pages are missing from every source) and Exercise 3 (page 173) (no matching exercise header in the transcribed pages). The key gives only the final value, so non-arithmetic answers are one-step ("printed answer key") and are not animated.
Other books: the scan lists questions without an answer for Class 4 English (182), Urdu (82), Class 3 English (59), Class 5 English (136) and Urdu (35). Many of these are oral/discussion prompts ("Practise greetings…") that have no single answer; they were **not** individually triaged.
MCQs without keys: the scan counted 0 per book, but `docs/test_prep_review/no_key.csv` is the authoritative list for the Tests Preps bank.

## 6. Animated solutions
The new Class 4/5 answers carry `sm` rows (the question, the worked equation, a check for division), which is the form the animated worked-solution engine can step through. Not run in the browser (see 3).
Coverage numbers from `docs/09_VR_COVERAGE.md` (before this pass): Class 1 math 31%, Class 2 49%, Class 3 44%, Class 5 51%; Class 4 had none. Fractions, number lines and word problems for Classes 1-5 have **no** animation yet.

## 4 and 5. Word and sentence meanings
Not worked in this pass. Coverage as of `docs/LEXICON_COVERAGE.md` (share of English word *occurrences* that have a meaning): Class 1 99.0% Urdu / 98.8% Pashto / 98.7% Arabic; Class 2 99.0 / 98.8 / 98.7; Class 3 98.6 / 98.4 / 98.2; Class 4 98.6 / 98.4 / 98.2; Class 5 98.4 / 98.2 / 98.0. By distinct word the share is 63-76%, so rarer words still lack a meaning. Child-level wording for the missing words and a sentence-translation audit remain open.

## 1 and 3. Proofreading and page view
Not done against the scans, and not tested in the browser at desktop/tablet/375 px in this pass. What the scan found:
- Fixed-width SVGs (risk of overflow at 375 px; should be checked): Class 1 Math 88, Eng 33, Nazira 44; Class 2 Math 33, Eng 66, Drawing 32, Nazira 39; Class 3 Math 29; Class 4 Math 11, Eng 7; others few.
- SVG without `viewBox`: Class 3 English 1, Class 3 Math 2.
- Tables wider than 5 columns (check for horizontal scroll): Class 2 Urdu 11, Class 3 Math 9, Class 4 English 9, Class 4 Math 7, Class 5 English 4, others fewer.
- Repeated spaces inside Nazira text (Class 2: 84, Class 3: 252) — probably deliberate letter spacing for reading practice; confirm before changing.
- Stray `||` in Class 5 Social Studies (3 each, EM and UM).

## Missing sources (not invented)
Class 1 Urdu and General Knowledge have no source scans.
## Not finished
All seven checks for Classes 1, 2, 3, 5 beyond the arithmetic answers above; Class 4 Math answers for non-arithmetic items; browser verification; meanings audits. Generated files were rebuilt after the data change (see the commit).
