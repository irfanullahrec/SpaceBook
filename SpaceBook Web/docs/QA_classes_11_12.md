# QA report: Class 11 and Class 12 (2026-10-21)

Scope asked: the seven checks on every page of every Class 11 / 12 book. **This pass did not complete all seven for every page.** It built repeatable checkers, ran them over all 29 Class 11/12 subjects, fixed what they proved wrong, and lists what is still open. Nothing was pushed.

## 1. Proofreading against the scans: NOT DONE
Comparing ~5,000 pages with their scans needs a person (or a vision pass per page). The earlier per-book pipelines (see the pipeline notes) already did a page-by-page comparison at build time; this pass did not repeat it. A crude automatic junk scan (`tools/qa/audit_q.js`) only flags replacement characters / long repeated runs; its hits are mostly dot leaders and code samples, not typos. Known source gaps stay as recorded: Class 12 HPE pp. 107 and 148 missing, Mutalia-e-Quran faded pages flagged, Islamic History scans 64/65 swapped, Civics scan = printed + 9.

## 2. Answers
Checked with `tools/qa/banks.js` (Class 12 exercise-bank layer), `tools/qa/dump_nokey.js`, and the Tests Preps review queue.

* Class 12 exercise banks: 2,879 items in 13 books. Every MCQ has a correct-option index and worked lines except **Physics 12 Unit 15 item 14 and Unit 20 item 9** (illegible source, already annotated in the bank) and **HPE 12 Ch 7 item 48** (no listed option equals the book's 1.80 m; annotated). Economics short questions and Statistics long answers cite the book's own answer paragraphs instead of a written solution (by design).
* **Fixed:** 36 Class 12 Physics textbook MCQs (Units 11, 12, 19) printed no key. Each was worked out by hand and given `"answer"` plus `"answerOrigin": "Derived (the textbook prints no key)..."` in `js/phys_12_data.js` (`tools/qa/key_phys12.js`, `key_phys12b.js`). Tests Preps queue for Class 12 Physics: **41 -> 3**.
* **Left open (3):** Unit 11 Q7 (E at 20 cm from 2 µC is 4.5x10^5 N/C; no option matches and the units are N), Q11 (needs the circuit figure), Q12 (stem truncated by the scan). They stay unkeyed rather than guessed. Q5 (V/m and N/C are both correct units) was keyed B with a note.
* Class 11 has no printed keys in several books; Class 11 Maths (879 leaves) was **not** re-spot-checked this pass. Class 11 MCQs without keys are in `docs/test_prep_review/no_key.csv` (none remain for Class 11 in the queue).
* Remaining no-key MCQs outside this scope (Class 9/10) are untouched.

## 3. Page view (desktop 1280, tablet 768, phone 375)
`tools/qa/overflow.js` drives real Chrome (Playwright) on `lazy.html`: for every Class 11/12 subject it opens the first, middle and last chapter, every visible tab, at three widths, and records page-level sideways scroll and any element that leaves the viewport outside a scroll container.
**Result: 29 subjects, 474+ chapter-tab-width checks (cls11-chem re-run separately, 18), 0 overflows.** Summary in `docs/qa/overflow_classes_11_12.json`.
Not covered: chapters other than first/middle/last (`--all` runs them; Class 11 Chemistry alone takes ~20 minutes), table cells that scroll inside their own container (allowed by the checker), pixel-level clipping of text inside fixed-height boxes, Arabic diacritic rendering (needs eyes). The built-in browser pane refuses local addresses, so no screenshots were taken.

## 4. Word meanings
Class 11/12 books hold ~40,700 distinct English tokens; ~25,000 have a gap in at least one of UR/PS/AR (most are names, code, scan artefacts like `scan`, `kptbb`, chemical symbols). `tools/qa/missing_words_1112.js` lists them by frequency. **Added** 190 hand-written real-word entries (EN/UR/PS/AR) in `docs/lexicon/curated/c018.txt` (science, medical, economics, general vocabulary) and rebuilt `js/lexicon_data.js`. This is a small fraction of the gap: the long tail needs a translator (queues in `docs/lexicon_review/`). The new Pashto/Arabic entries were written by the assistant, not a native reviewer.

## 5. Sentence meanings
Not audited this pass (`sb_trilingual.js` / `universal_translate.js` untouched). Coverage numbers remain in `docs/LEXICON_COVERAGE.md`; machine-translated sentences are marked with a leading approximation sign by design.

## 6. Animated worked solutions
Measured, not extended:
* Class 12 Maths: 493 of 586 worked items animate (84%); Class 11 Maths 791 of 879 (90%) (`docs/09_VR_COVERAGE.md`).
* Class 12 exercise banks (`tools/qa/bank_vr.js`): of the answers that contain at least two equations, Physics 118/157, Chemistry 12/26, Statistics 21/39, Computer Science 17/34 animate.
* Main reason numericals miss: unit symbols after numbers (`12.8 V / 3.2 A`, `16 A·Ω`) make the auto-parser reject the line. I prototyped a unit-aware parser in `js/vr_auto.js`; it lowered Physics coverage (118 -> 112), so it was **reverted** (file is byte-equivalent to before). A proper fix needs its own test pass. Hand-authored specs for calculus, trig, sequences, complex numbers, probability/distributions were **not** added.

## 7. Derived files
After the data change: Tests Preps bank (`build_mcq_bank.js`), study index (`build_study_index.js`), lexicon, lazy page + manifest, search index, offline map / service-worker version were regenerated with `node tools/build/all.js --only mcq-bank,study-index,lexicon,lazy,search,offline`. (Writes to large files failed intermittently with `EUNKNOWN` on this machine and were retried.)

## Tools added (all dev-only, `tools/qa/`)
`audit_q.js`, `banks.js`, `bank_vr.js`, `bank_peek.js`, `dump_nokey.js`, `noans.js`, `peek.js`, `shape.js`, `missing_words_1112.js`, `overflow.js`, `key_phys12.js`, `key_phys12b.js` (+ `patch_vr.js`/`unpatch_vr.js`, the reverted prototype).

## Open list, in order of value
1. Page-by-page proofreading against scans (check 1) and sentence translations (check 5).
2. Unit-aware animation for Physics/Chemistry/Statistics numericals, then hand specs for calculus/trig/sequences/complex/probability.
3. Translator pass over the lexicon queues; native review of c018.
4. The 3 unresolved Physics MCQs; Class 11 Maths spot-check.
5. Full `--all` layout run, and a human look at Urdu/Arabic pages with diacritics.
