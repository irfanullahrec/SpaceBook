# QA — Classes 1 to 5 (2026-10-21)

Scope: every book in `CLS1_BOOKS` … `CLS5_BOOKS` (Class 1: 6 books, Class 2: 8, Class 3: 7, Class 4: 8, Class 5: 8; about 4,500 scanned pages).
The seven checks are far larger than one session can do by hand for that many pages, so this report says exactly what was done, what was only measured, and what is open. Nothing is claimed that was not run.

## Tools added (all re-runnable)
| Tool | What it does |
|---|---|
| `tools/qa_cls15_scan.cjs` | Structural scan of all Class 1-5 books: empty text, unbalanced `**`/`$`, control characters, wide tables, SVGs without `viewBox` or with a fixed width, questions without a stored answer. |
| `docs/source-verification/class-4/tools/unanswered.py CLASS SUBJ [--show N]` | Lists question lines (leaf `q` / `qp`) of any book that still have no answer in the page transcriptions. |
| `.../class-4/tools/arith4.py` (`CLS=n`) | Adds computed answers + worked steps for plain arithmetic (whole numbers and decimals). |
| `.../class-4/tools/keyans4.py` | Copies the printed answer key of Class 4 Maths onto its questions; derives rounding / decimal place value / divisibility parts the key leaves out; reports where the key disagrees with arithmetic. |
| `.../class-4/tools/upgrade_arith.py` (`CLS=n`) | Gives existing one-line arithmetic answers a worked-equation chain the animated solution can step through (never changes an answer that disagrees with the computed value). |
| `.../class-5/tools/fill5_try.py` | Computed answers for 42 unkeyed Class 5 "Try yourself" parts (conversions, differences, sequences, comparisons, percentages). |
| `tools/offline_meanings/missing_cls15.js` | Class 1-5 English words that still lack an Urdu / Pashto / Arabic meaning, most frequent first. |

## 2. Answers
Open questions per book (leaf questions with no answer; `unanswered.py`):

| Book | Open | Of | What they are |
|---|---:|---:|---|
| Class 1 Math | 1 | 454 | "join the dots and colour" |
| Class 2 Math | 14 | 477 | worked examples shown "done in the textbook" (the answer is printed in the question), one story stem |
| Class 3 Math | 7 | 514 | "done for you" examples and two "(given)" items - answer already in the question text |
| **Class 4 Math** | **48** | 969 | drawing, measuring, constructing, colouring, labelling (no answer exists) |
| **Class 5 Math** | **32** | 951 | drawing squares/angles, "estimate" items whose rounding rule the book does not state, days-to-months (month length not stated) |
| Class 2 Eng / Urdu | 3 / 2 | | read-aloud items |
| Class 3 Eng / Pashto | 56 / 6 | | "read and notice", discussion, "learn to speak" prompts |
| Class 4 Eng / Urdu / Sci | 203 / 60 / 7 | | instruction stems ("read", "notice", "discuss", "write a paragraph"), spelling gap-fills with no key (45), projects |
| Class 5 Eng / Urdu / Sci / Pashto | 132 / 21 / 4 / 2 | | same kinds |
| Class 1 Eng/Isl/Nazira/Pashto, Class 2 GK/Isl/Pashto, Class 3 GK/Isl, Class 4 Isl/Pashto, Class 5 Isl/SST/SSTUM | 0 | | complete |

Done in this pass:
- **Class 4 Maths had no answers at all.** Now **921**: 757 copied from the book's printed answer key (answers pages 173-181), 67 more key-derived (letter-list "mark the numbers" parts, labelled groups), ~10 derived from the question where the key skips a part (rounding, decimal place value, one MCQ), 79 computed arithmetic items with worked steps, 9 decimal products/quotients. All 70 early computed answers agree with the printed key.
- **Printed-key error found:** Class 4 Maths Unit 2 Exercise 1 Q2 - the key lists "b, c, e" as divisible by 3 but 6,720 and 52,110 are also divisible by 3 (digit sums 15 and 9). The SpaceBook answer uses the computed value; the page already carried an `@issue` note.
- Class 5 Maths: 957 -> **999** answers (42 added); Class 3 compound-unit sums were checked and found already answered (a first attempt that would have overwritten richer answers was reverted).
- MCQs without keys: `docs/test_prep_review/no_key.csv` stays the authoritative list (not regenerated here because the `mcq-bank` build step failed on a file write; the file in the tree is not from this pass).

Key entries with no matching question: Class 4 Maths Exercise 1 (p5) and Exercise 2 (p8) - those textbook pages are missing from every source; Exercise 3 (p173) has no exercise header in the transcribed pages.

## 6. Animated solutions
Share of each Maths solution bank whose steps the animated-solution engine can step through (`vr_auto.autoSpec`), before -> after:
Class 1 31% -> 32%; Class 2 48% -> 50%; Class 3 44% -> 46%; **Class 4 0% -> 9%** (79 of 921; the 757 key answers are single-line); **Class 5 52% -> 66%** (661 of 999).
Not animated: fractions, number lines, word problems, geometry and the key-only answers of Class 4. They keep the normal presentation.

## 3. Page view (browser, 375 px)
Every unit of every book of Classes 1-5 (**562 units, 40 books**) was opened in the in-app browser at **375 px** by an automated check: page scroll width equal to the viewport, and no element wider than the viewport outside the header tab strip. Result: **0 units overflow**. Class 4 Maths Unit 2 (exercise cards, "Show answer", KaTeX) was also checked at 768 px and desktop width: no horizontal scroll, answers display, 0 KaTeX errors.
Limits: the check opens each unit's default view (lessons / first cards); it does not expand every exercise card or every "Show answer" panel, and tablet width was checked on that one page only. The scan still flags fixed-width SVGs (Class 1 Math 88, Eng 33, Nazira 44; Class 2 Math 33, Eng 66, Drawing 32, Nazira 39; Class 3 Math 29; Class 4 Math 11) and tables over 5 columns (Class 2 Urdu 11, Class 3 Math 9, Class 4 Eng 9 / Math 7); in the views opened they scale to fit.

## 4. Word meanings
Coverage (share of English word *occurrences* with a meaning, `docs/LEXICON_COVERAGE.md`): Classes 1-5 are 98.0-99.0% in Urdu, Pashto and Arabic. By distinct word, 1,459 Class 1-5 English words lacked a meaning in at least one language (1,036 had no Urdu). This pass added **~120 hand-written child-level entries** (`docs/lexicon/curated/c019.txt`, `c020.txt`: comparatives and superlatives, possessives, everyday nouns, common school words), leaving **1,350** (975 without Urdu; `missing_cls15.js` lists them). The remainder are mostly science/maths terms and abbreviations used as examples in the upper units; they were not translated because they need a subject teacher's check. The two lists were written by the assistant, not a native-speaking teacher (same tier as the existing curated files).

## 5. Sentence meanings
`tests/lexicon/sentences.js`: 27 passed, 0 failed. Class 1-5 books carry their own English / Urdu / Pashto sentence text; Arabic lines come from the stored tier-4/5 data. A sentence-by-sentence audit of the machine-made (tier 4, `≈`) translations was not possible here: it needs the local NLLB model run (hours) and a native-speaker review.

## 1. Proofreading
Not done against the scans in this pass. The books were transcribed page by page from the scans earlier (see the per-class pipeline notes); the checks run here were structural only (scan above). Findings still to look at: repeated spaces inside Nazira text (Class 2: 84, Class 3: 252 - probably deliberate letter spacing), 3 stray `||` in Class 5 Social Studies (EM and UM), 16 runs of 3+ spaces in Class 4 Maths text.

## Missing sources (not invented)
Class 1 Urdu and General Knowledge have no source scans.

## Not finished
Proofreading against scans for all books; browser check of expanded exercise cards and tablet width for all units; Class 4 Maths animation of non-arithmetic items; Arabic grid / Nazira diacritics review; translation of the remaining ~1,350 words; native-speaker review of all hand-written meanings; the `mcq-bank` and `search` build steps (they fail on a file write / on `cls8-eng`, outside this scope).
