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

## 6. Animated worked solutions (updated 2026-10-21, second pass)
* **Engine (`js/vr_auto.js`)**: the auto-animator now reads physics numericals it used to reject: units after numbers (`12.8 V`, `5 Hz`, `2 kg`, shown upright), Ω and Φ, subscripts (`I_g`, `V_s`, `X_L`, `I_rms`), products between two equals signs (`V = IR = …`, `F = ma = …`), and a sentence end (`… 360 Ω. 60 W bulb`) now closes a chain. Text is shown as written; nothing is recomputed.
* **Measured** (`tools/qa/bank_vr.js`, answers with two or more equations): Class 12 Physics 118 -> **138** of 157, Statistics 21/39, Chemistry 12/26, Computer Science 17/34 (unchanged: chemistry is descriptive reaction text, statistics uses nCr / factorial notation the parser does not read).
* **Regression checks**: `tools/qa/vr_regress.js` compares old and new engine on every bank item: 214 unchanged, 32 newly animated, 54 with more rows, 1 lost (a line ending "(632.8 nm, red)" that earlier lost its unit instead); `tools/qa/vr_katex.js`: 246 animated items, 1,415 rows, 0 KaTeX errors; project-wide scan (`tools/vr/scan_all.js`) 6,054 -> 6,068 animatable, none lost; `tools/vr/validate_arith.js`: no issues. The earlier backup of the engine is `tools/qa/bak/vr_auto.orig.js`.
* **Hand-written calculus packs** (`js/sol_m12_calc.js`, 23 packs, each re-checked by finite differences / Simpson's rule when the file loads; wired into `index.html`): Ex 6.2 Q3 integration by parts (a)-(f); Ex 6 review Q3, Q4, Q5, Q8, Q9 integrals; coth x; separable ODEs (Ex 10.2 Q1b, Q1c); implicit derivative of the ellipse (Ex 3.3 Q7); sign chart of f(x) = x³ − 3x² − 9x + 1; partial derivatives (WE 11.2, Ex 11.1 Q4, Q5, Ex 11 review Q3, Q4, Q8, Q9). Confirmed in real Chrome (`tools/qa/vr_browser.js`): the new packs produce animation hosts on the live data, 0 page errors.
* **Trigonometry**: nothing new was needed. Class 11 Maths already animates in full, Class 10 has the unit-circle specs, and the Class 12 trig items already animate through the auto-animator; the Class 12 items still without animation (`node tools/qa/unanimated.js`, 82 left) are Maple command lists, vector-function items, coordinate geometry one-liners and Newton/bisection tables.
* **Not done**: statistics notation (ⁿCᵣ, n!), hand specs for the remaining ~90 Class 12 Maths items, Chemistry numericals beyond the 12 that already animate (their answers are mostly equation prose).

## 7. Derived files
After the data change: Tests Preps bank (`build_mcq_bank.js`), study index (`build_study_index.js`), lexicon, lazy page + manifest, search index, offline map / service-worker version were regenerated with `node tools/build/all.js --only mcq-bank,study-index,lexicon,lazy,search,offline`. (Writes to large files failed intermittently with `EUNKNOWN` on this machine and were retried.)

## Tools added (all dev-only, `tools/qa/`)
`audit_q.js`, `banks.js`, `bank_vr.js`, `bank_peek.js`, `dump_nokey.js`, `noans.js`, `peek.js`, `shape.js`, `missing_words_1112.js`, `overflow.js`, `key_phys12.js`, `key_phys12b.js` (+ `vr_regress.js`, `vr_katex.js`, `vr_browser.js`, `unanimated.js`, `showitem.js`, `fix_bs.js`).

## Open list, in order of value
1. Page-by-page proofreading against scans (check 1) and sentence translations (check 5).
2. Unit-aware animation for Physics/Chemistry/Statistics numericals, then hand specs for calculus/trig/sequences/complex/probability.
3. Translator pass over the lexicon queues; native review of c018.
4. The 3 unresolved Physics MCQs; Class 11 Maths spot-check.
5. Full `--all` layout run, and a human look at Urdu/Arabic pages with diacritics.

## Left for the final regeneration (owner, from a clean checkout)
Not done by this QA work, on purpose (shared files):
1. `index.html`: add `<script src="js/sol_m12_calc.js?v=20261025_1"></script>` after the `sol_m12_hand.js` line and bump `vr_auto.js` to `?v=20261025_5`. Without this the 18 calculus packs do not load.
2. Regenerate: `node tools/build/all.js` (lazy page + manifest, search index, offline map, service-worker version, Tests Preps bank, study index, lexicon). The Tests Preps bank and `no_key.csv` already reflect the Physics 12 keys in the working tree; the lexicon already includes `docs/lexicon/curated/c018.txt`.
3. Commit the regenerated outputs together with the sources above.

Added after the first calculus batch (same file, 5 more packs): Ex 7.1 Q1 and Ex 7.2 Q1, Q9 (distance, area), Maclaurin series of e^x, partial derivatives from the definition (Ex 11.1 Q6). Statistics notation (nCr, n!) was looked at and left alone: the remaining Statistics bank answers are definitions and procedures, not equation chains.
