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
**Result (first pass, first/middle/last chapter): 29 subjects, about 490 checks, 0 overflows. Full pass (`overflow.js --all`, every chapter, every visible tab, 1280 / 768 / 375 px): 29 subjects, 428 chapters, 2,589 checks, 0 overflows** (`docs/qa/overflow_classes_11_12.json`).
Not covered: table cells that scroll inside their own container (allowed by the checker), pixel-level clipping of text inside fixed-height boxes, Arabic diacritic rendering (needs eyes). The built-in browser pane refuses local addresses, so no screenshots were taken.

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

## Class 11 Maths numeric spot-check (`python tools/qa/check_m11.py`)
Method: every step of the 879 solutions in `js/math_11_solutions.js` that carries a TeX chain `A = B = C` (1,542 chains in 2,360 steps) is translated to sympy and each side is evaluated at four random points; the sides of one chain must agree. Lone-symbol sides (definitions like `a_n = …`), equations being solved (`… = 0`) and chains with unreadable notation (sets, matrices, sums, limits, text) are skipped, and the last side of a solution's last chain is compared with the printed answer when both are plain numbers.

Result: **144 chains checked, 104 agree, 40 flagged; 29 printed answers compared, 1 flagged.** I read every flagged item. None is an arithmetic error in the solutions:
* parser limits or conditional relations, not identities: `rank(A)=…`, `P(E^c)=1-P(E)`, `f(x)=…` with an unknown function, `… = 5m` divisibility proofs, `\sin(\theta+2k\pi)` with integer k, substitutions such as `1+\cos\alpha=1+\frac{b^2+c^2-a^2}{2bc}` (a, b, c, α are not independent), `\sin3\theta=3x-4x^3` (θ is defined by `\sin\theta=x`), and a few trig identities with `\sin^22\theta` that I re-checked by hand (`\cos4\theta=1-2\sin^22\theta=1-8\sin^2\theta\cos^2\theta` is correct).
* the one answer flag is s408 (six people round a table, two of them always together): the solution answers 240 and explains that the printed key's 120 leaves out the two orders of the pair. 240 is correct.

So: no wrong number was found in the part that could be checked, but that part is small (about 9% of the chains). The other ~91% (matrices, sets, sums, limits, probability tables, text) were **not** verified automatically; the next step would be a sympy translator for those forms or a human spot-check. Class 11 answers outside this file (the exercise banks of other Class 11 books) were not touched.

## Class 12 Maths: the last 82 unanimated items (third batch)
`js/sol_m12_calc.js` now holds **44 checked packs** (21 more): order/degree of ODEs, Euler's theorem (Ex 11.2 Q2), three partial-derivative MCQs, three vector-derivative MCQs (Ex 5 review: the printed options of Q-ix have no correct choice, and Q-viii/-ix notes say so), triangle areas (Ex 7.4 Q5), interior angles (WE 7.24, Ex 7.3 Q7), inscribed angle (Ex 8.3 Q4), incenter JO, four bisection iterates (Ex 12.1 Q2, every residual checked against the stored values), vector operations (Ex 5.1 Q2), the integration-by-parts rule (review vi, q6), the equal-limits integral, the ln derivative MCQ and the Taylor-polynomial MCQ (noted: no option is exactly right as printed). Each pack re-checks its numbers on load and is not registered if they disagree; all 44 render with KaTeX and none warned. Items without animation: 82 -> **61**.

What the remaining 61 are, and why they were not done:
* **Worked examples keyed by title** (`we-1-3`, `we-5-source-5..11`, `we-7-7`, `we-7-9`, …): they have no `question` field, so `SBVR.autoHtml` cannot match a pack. Fixing that is a one-line change in `autoHtml` (`item.question || item.problem || item.title`) plus a check of the worked-example renderer in `app.js`; not done because app.js is shared and needs a browser look.
* **OCR-garbled source items** (`we-2-14` … `we-2-30`: "Sketch the graph of", "Evaluate lim", formulas lost): the question itself is unreadable, so no solution can be written honestly; they need the page re-read from the scan.
* **Maple command lists and plot instructions** (`ex-2-3-q5`, `ex-3-5-q7`, `we-2-18`, `we-4-source-17`, …), **one-word concept questions** (`ex-2-review-q1`, `ex-6-review-q1`, `ex-10-review-q3`, `ex-11-review-q1/q5/q6`, `ex-12-review-q3/q5/q8/q10`, …) and **proof-style vector items** (`ex-5-2-q5`): nothing numeric to animate.

## Proofreading, word and sentence meanings: what was done in the third pass (2026-10-21)
**Proofreading (`node tools/qa/proof_scan.js`).** An automatic scan of the 32 Class 11/12 data files (about 110,000 English strings) lists strings with the marks of a bad transcription: repeated words, OCR confusions (`tbe`, `arid`, `inthe`), unbalanced brackets, replacement characters, doubled punctuation. It found no replacement characters and almost no OCR confusions; the repeated words and unbalanced brackets are mostly dot-leader lines, "1)" list markers, headings repeated by a paragraph break, and printed errors that the earlier page-by-page passes **kept on purpose** and annotated ("preserved as printed"). I checked one of them against the scan to be sure: Biology 12 PDF page 85 prints "to hamper the the nerve impulse", exactly as the data has it. `tools/qa/sample_pages.js` draws random paragraphs with their page for a visual sample. A full comparison of every page with its scan was **not** done in this pass (about 5,000 pages; the scan files are named per source PDF, not per page number, so each book needs its own page map). Urdu-source books (Economics, Pakistan Studies, HPE UM, Islamiat, Islamic History, Mutalia) hold an English rendering, which cannot be proofread without the Urdu page; they were not touched.

**Word meanings.** 633 more hand-written entries (`docs/lexicon/curated/c019.txt`, EN / UR / PS / AR, the most frequent real vocabulary of Class 11/12 that had no meaning). Words that another session had already written (files c020, c021, c901, c902) were left out so that the better entry wins. Entries where I was not sure of the Pashto were left blank rather than guessed. `js/lexicon_data.js` was **not** rebuilt (shared generated file): it picks the new entries up at the final regeneration. About 25,000 distinct Class 11/12 tokens still lack a meaning in at least one language; most are names, code, scan artefacts and rare terms (queue: `node tools/qa/missing_words_1112.js`).

**Sentence meanings (`node tools/qa/sent_lint.js`).** Of 10,163 stored sentence translations (`js/sent_data_*.js`, all classes): hand-written 1,128 fields, computer-made 22,498 fields, **none 6,863 (almost all Arabic: 6,829 sentences have no Arabic line; Urdu 23 and Pashto 11 are missing)**. Latin letters left in a translation: 138 Urdu, 110 Pashto, 21 Arabic, mostly proper names and Arabic-script transliteration targets (a few are real defects, listed with `--show`). Filling the Arabic gap is the machine-translation job another session is running (`D:/lexsrc/mt`, youngest classes first); Class 11/12 sentences come last in that queue. I did not start a second translation job or touch the generated sentence files.
