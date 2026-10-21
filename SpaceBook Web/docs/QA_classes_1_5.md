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
Class 1 31% -> 32%; Class 2 48% -> 50%; Class 3 44% -> 46%; **Class 4 0% -> 19%** (172 of 921; 93 fraction/decimal items were upgraded to worked chains by `upgrade_ctx4.py`, which reads the question's instruction and refuses any item whose computed value differs from the printed key; the rest of the key answers are single-line); **Class 5 52% -> 66%** (661 of 999).
Not animated: number lines, word problems, geometry, mixed-denominator fraction sums and the remaining key-only answers of Class 4 (conversions, rounding, factors, time). They keep the normal presentation.

## 3. Page view (browser, 375 px)
Every unit of every book of Classes 1-5 (**562 units, 40 books**) was opened in the in-app browser at **375 px** by an automated check: page scroll width equal to the viewport, and no element wider than the viewport outside the header tab strip. Result: **0 units overflow**. Class 4 Maths Unit 2 (exercise cards, "Show answer", KaTeX) was also checked at 768 px and desktop width: no horizontal scroll, answers display, 0 KaTeX errors.
Limits: the check opens each unit's default view (lessons / first cards); it does not expand every exercise card or every "Show answer" panel, and tablet width was checked on that one page only. The scan still flags fixed-width SVGs (Class 1 Math 88, Eng 33, Nazira 44; Class 2 Math 33, Eng 66, Drawing 32, Nazira 39; Class 3 Math 29; Class 4 Math 11) and tables over 5 columns (Class 2 Urdu 11, Class 3 Math 9, Class 4 Eng 9 / Math 7); in the views opened they scale to fit.

## 4. Word meanings
Coverage (share of English word *occurrences* with a meaning, `docs/LEXICON_COVERAGE.md`): Classes 1-5 are 98.0-99.0% in Urdu, Pashto and Arabic. By distinct word, 1,459 Class 1-5 English words lacked a meaning in at least one language (1,036 had no Urdu). This pass added **~230 hand-written child-level entries** (`docs/lexicon/curated/c019.txt`, `c020.txt`, `c021.txt`: comparatives and superlatives, possessives, everyday nouns and verbs, common school words), leaving about **1,250** (the last 100 entries, `c021.txt`, are not yet built into `js/lexicon_data.js`) (975 without Urdu; `missing_cls15.js` lists them). The remainder are mostly science/maths terms and abbreviations used as examples in the upper units; they were not translated because they need a subject teacher's check. The two lists were written by the assistant, not a native-speaking teacher (same tier as the existing curated files).

## 5. Sentence meanings and translation consistency
`tests/lexicon/sentences.js`: 27 passed, 0 failed. Class 1-5 books carry their own English / Urdu / Pashto text; Arabic lines come from the stored tier-4/5 data. A sentence-by-sentence audit of the machine-made (tier 4, `≈`) translations needs the local NLLB model (hours) and a native speaker: not done.
New check `tools/qa_cls15_translations.cjs` compares the three languages of every text block (about 13,000 blocks in 27 books with English text): **no block lacks an Urdu or Pashto line**. Numbers of two or more digits differ between English and Urdu/Pashto in 59 blocks; the ones read by hand were correct ("ساڑھے ۲۹" = 29.5, "15 کروڑ" = 150 million, "50 ہزار" = 50,000 are written in words/lakh-crore style, not errors). Left as leads, not errors: Class 4-5 Social Studies Urdu-medium books are stored Urdu-in-the-English-field (the check reports them as "not translated"), and English-practice fill-in sentences are deliberately left in English.

## 1. Proofreading
Evidence available in this pass:
- Every page of Classes 2-5 was OCR-compared with its scan when it was built (`ocrWordRecall` in each `ledger.json`). All pages are at or above 0.93 except Class 5 Maths pp. 1, 140 (0.82, mostly figures), 144 and 153 (0.0, drawing pages with no printed text). Class 1 has no OCR (its scans were read by eye).
- Each ledger also lists the transcriber's open source notes (`issues`): e.g. Class 4 SST 129 of 131 pages, Class 5 Science 134 of 161: these are recorded misprints, faded or missing scan text, and decisions, not unfixed errors.
- Structural scan (`qa_cls15_scan.cjs`): empty text, unbalanced markup, control characters: none found beyond the items listed under "Page view".
- Spelling: no OCR-junk words found among the rare Class 1-5 English words (the 19 rarest unmatched words are names and science terms).
Not done: re-reading every page against its scan by eye.

## Missing sources (not invented)
Class 1 Urdu and General Knowledge have no source scans.

## Not finished
Proofreading against scans for all books; browser check of expanded exercise cards and tablet width for all units; Class 4 Maths animation of non-arithmetic items; Arabic grid / Nazira diacritics review; translation of the remaining ~1,350 words; native-speaker review of all hand-written meanings; the `mcq-bank` and `search` build steps (they fail on a file write / on `cls8-eng`, outside this scope).

## Left for the final regeneration (nothing shared was regenerated after commit `cad60ae0`)
Data changed since the last regeneration, so the owner's final run of `node tools/build/all.js` (lazy page, manifest, search index, offline map, service-worker version, lexicon) must happen after these:
- `js/math_4_data.js` (Class 4 Maths: 93 more worked chains; rebuilt from `docs/source-verification/class-4/math/pages`).
- `docs/lexicon/curated/c021.txt` (100 word meanings): needs `node tools/build/make_lexicon.js` / the lexicon step before the lazy page is rebuilt.
- Nothing else: `js/lexicon_data.js` and the Class 1/2/3/5 Maths files were rebuilt before the last regeneration commit.
`index.html` versions were not touched. No lock files were removed.

Search data: all 40 Class 1-5 subjects (including all eight Class 1 subjects) (including `cls1-pashto`) build cleanly in isolation (`make_search.js --only cls1-... --out <temp dir>`) and the generated `cls1-pashto.json` is byte-identical to the committed file, so no fault in Class 1 data could be reproduced. The failure another session saw is therefore not in the Class 1 book data; `js/cls1_book_reader.js` and `figs1.py` carry uncommitted edits from another session and are the likely cause if it recurs.
