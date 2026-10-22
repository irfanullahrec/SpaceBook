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
**Result (first pass, first/middle/last chapter): 29 subjects, about 490 checks, 0 overflows. Full pass (`overflow.js --all`, every chapter, every visible tab, 1280 / 768 / 375 px): 29 subjects, 462 chapters, 2,589 checks, 0 overflows** (`docs/qa/overflow_classes_11_12.json`).
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

## Page-by-page proofreading (started 2026-10-22)
Tools: `tools/qa/page_text.js` (groups a data file's strings by scan page; `--urdu` collects the Urdu-script strings), `tools/qa/qa_page.js <book> <pdf pages>` (prints the data of a page next to its scan path; the scan of PDF page N is the N-th JPG in sorted file-name order in `Books/12th/<book>/JPG`), `tools/qa/ocr_book.py` + `tools/qa/compare_pages.py` (RapidOCR of the English science books and a per-page list of lines that differ), `tools/qa/crop.py` (enlarge a region of a scan), `tools/qa/fix_text.js` (apply a correction and log it in `docs/qa/proofreading_fixes.tsv`).

**HPE 12 (Urdu medium), PDF pages 1-157, every page read against its scan: 5 corrections** (full list in `docs/qa/proofreading_fixes.tsv`):
* p. 13: "اگر کوئی بلڈ پریشر" -> "اگر ہائی بلڈ پریشر" (the scan prints "ہائی"), all 4 copies in the data.
* p. 19: the paragraph on the heart's functions says the pulmonary vessels that leave the right ventricle are "شریانوں" in the data; the printed page has "وریدوں" (veins) — the textbook's own slip, so the data now **follows the print** and the source note says the print means the pulmonary arteries.
* p. 36: "چولہا خرید جائے" -> "چولہا خریدا جائے" (the scan prints "خریدا"; the old note "retained as printed" was wrong).
* p. 72: "ہائیکنگ (Hitch Kick)" -> "سائیکلنگ، (Hitch Kick)" (the scan prints "سائیکلنگ،").
Everything else on the 157 pages (Urdu text, the numbers in the MCQs and rules, the table of results, the handwritten key marks which are not part of the data) agrees with the scans. Pashto lines of HPE were not proofread (no scan exists for them).

### Automatic scan comparison and Qur'an check (2026-10-22)
Limits first: the scans of the Urdu-source books are 616 x 830 px (their PDFs hold nothing better), no Urdu OCR is installed, and the "pdf page" recorded in several data files drifts by one against the scan file order (Pakistan Studies: the data page 5 covers the scans 003 and 004; Physics: strings inherit the page of their unit). So a page-by-page reading was only done where the data and the scan could be paired reliably (HPE 12, above; Pakistan Studies printed pp. 1-9 also read, no error) and the rest was compared by machine:
* **English books, whole-book comparison against RapidOCR of the scans** (`tools/qa/ocr_book.py`, `compare_pages.py`, `word_pairs.py`, `typo_candidates.py`): Biology 12, Physics 12 and Chemistry 12 (every scan page OCR'd, 3 s/page). Data words that are rare in the whole project and occur nowhere in the OCR of the book, and OCR lines that the data does not carry anywhere, were listed and opened. What remained were genuine printed oddities, all already annotated as printed: "Helmhold's Coils" (Physics, the book's own spelling), "(ocytocia=childbirth)" (Biology p. 124 of the scan, checked in the OCR), "triiodothyronin", "Ebner's glands", "propylnonane" (correct nomenclature). **No transcription error was found in these three books by this method.** It does not see formulas, figures or tables, and the numbers cannot be compared page by page because of the page drift above (`digits_check.py` is for pages whose attribution is exact).
* **Qur'an text** (`tools/qa/ayat_check.py`): every Arabic-script string of a data file that carries vowel marks is matched against the complete Uthmani text of the project cache (`_qcache`, 114 surahs). Mutalia-e-Quran 12: **5,623 strings identified with the canonical text, 2 differences, both outside the Qur'an** (a Pashto gloss and an English sentence quoting verse 5:2). Class 11 Mutalia: 3,480 identified, 72 flagged segments (all are runs that cross a pause sign or an ayah end, where the printed spelling differs from Uthmani in one or two letters: the book uses the modern spelling); Islamiat Ikhtiari 11 and Lazmi 11: 0 spelling differences; Ikhtiari 12: 18 flagged segments, all of them non-Qur'anic phrases (the isti'adha, "الجهاد في سبيل الله") or partial ayat. The flagged segments are listed in `docs/qa/ayat_flags_*.json` for a check against the scan. Vowel-mark differences (hundreds) are the known differences of script between the Uthmani cache and the Indo-Pak typesetting of the textbooks (shadda without fatha, dagger alif) and were not treated as errors; this check proves the ayat agree with the canonical text, **not** that they agree with the scan.
* Maths 12 was OCR'd too (357 scan pages): the pagebook text carries almost only formulas and TeX, so the word comparison finds nothing, and the number comparison (`digits_check.py`) lists about 4,500 differences per book that are page numbers, figure labels and the drift of the page attribution, which cannot be triaged by hand; Maths formulas and answers were checked by the numeric tools instead (`tools/vr`, `tools/qa/check_m11.py`).
* **Not done:** OCR and comparison of the other English books (Maths 11, Statistics, English, Computer Science, Civics, Biology / Chemistry / Physics 11), and a page-by-page reading of the Urdu-source books other than HPE. Dependency: the **Arabic sentence lines** of every book depend on the machine-translation job that another session runs (`D:/lexsrc/mt`, youngest classes first); nothing was changed in the generated sentence files, so the Arabic lines of Class 11/12 sentences stay as they are until that job reaches them.

## Class 12 Maths animations, fourth batch (2026-10-22)
`js/sol_m12_calc.js` now has **61 checked packs**; `js/vr_auto.js` lets a pack be matched by a pattern of the question (`re`), which is how the worked examples (`we-*`, whose printed question carries combining arrows and primes) are reached. New packs: the vector worked examples (continuity domain, derivative, product rule for the cross product, two derivatives, velocity, acceleration), the unit-vector derivative proof, two vector review MCQs (one has no correct printed option, and the pack says so), Maple plots of x² + 3x + 8 and x² + 2 (table, vertex, intercepts), centroid, distance, concurrency of the right bisectors, the intermediate-value rule, and the Newton-Raphson formula. Class 12 Maths items without animation: 61 -> **44**; what is left is Maple command lists, number-line and sketch instructions, one-word concept questions and the OCR-garbled worked examples (`we-2-11` ... `we-2-30`) whose question is unreadable.

## Round 3 additions (2026-10-22)
* **Animations**: Class 12 Maths unanimated items 82 -> 42 (61 checked packs); Class 11 Maths animatable solutions 791 -> **831 of 879** (the engine now treats a bmatrix/pmatrix/vmatrix as one atom, so matrix equalities such as `AB = [...]` animate; `tools/qa/m11_vr.js` checks every row with KaTeX: 0 errors; `tools/vr/validate_specs.js`: no new error, the 52 existing ones are Class 8 strings such as `\2times`, not from this work). The 48 Class 11 items left are Gaussian-elimination row-operation chains (their rows are joined by "⇒", not "=").
* **Word meanings**: `docs/lexicon/curated/c022.txt`, 182 names and terms (scholars, rulers, surahs, places) in EN/UR/PS/AR; with c018 and c019 about 1,000 hand-written entries for Class 11/12. The most frequent words still without a meaning are now code identifiers, Pashto/Urdu transliteration tokens and rare terms.
* **Sentence meanings (Arabic and the rest)**: the other session's translation job had stopped, so a local job for Class 11/12 was started: `tools/qa/queue_1112.js` builds the queue (22,083 sentences that occur at least twice in Class 11/12 and have no translation from the book, 104,300 occurrences), `mt_sentences.py` writes `D:/lexsrc/mt/sentences_1112.jsonl` (Urdu, Pashto and Arabic, local NLLB model, nothing leaves the machine; about 1 sentence/s, so roughly 6 hours; it can be stopped and resumed with the same command). **To use the result at the final regeneration:** rename the file to `sentences_mt_1112.jsonl` (the builder only reads `sentences_mt*.jsonl`), run `node tools/offline_meanings/build_sentences.js`, then the usual `node tools/build/all.js`. Machine lines are shown with a leading ≈ by design.
* **Proofreading**: unchanged from the previous entry (HPE 12 complete; automatic OCR and Qur'an comparisons for the rest). A page-by-page reading of the 616 x 830 scans of Pakistan Studies, Economics, Islamiat Ikhtiari and Islamic History cannot be done reliably by reading (the data pages and the scan pages do not line up one to one: one data "page" covers 1.2 scan pages), so those four books remain **open**.

## Urdu-source proofreading log (continued)

- **Pakistan Studies 12, scans 017–031 (printed pp. 15–29, Chapters 1–2):** Urdu text read against the scans. No transcription errors found (movement, Cripps, Shimla, 1945-46 elections, Cabinet Mission, 3 June plan, Exercise 1 and the start of Chapter 2 all match). "تمرین" lines are the Pashto heading, not a mismatch.
- **Open finding (not from the book): generated filler questions.** The legacy chapter layer holds template-generated "exercise" blocks that appear on no printed page, for example "باب نمبر N کا مرکزی موضوع کیا ہے؟" with the distractor "علمِ فلکیات", plus generic short/long questions. Counts of the template line: pakstudy_12 22 (11 chapters × 2 copies), economics_12 24, english_12 6, ikhtiari_11 5, islamiat_ikhtiari_12 8. They conflict with the book-only rule for topic practice. Recommended owner decision: delete the blocks (the printed exercises stay) or label them "practice – not from the book". Left untouched here because the reader paths that display them were not changed in this pass.

### Pakistan Studies 12 — complete (scans 001–228, all 11 chapters + exercises + back matter)

- Urdu text read against every scan in document order. **0 transcription errors found; 0 data changes.** Duplicate scans (PDF 33 = 32, PDF 110/109 right page, 212/213) are already excluded in the data and noted there.
- The data file's own "retained as printed" notes were checked against the scans and are correct (e.g. p.120 prints the Pashtun-culture closing clause twice; p.201 prints "1347ء" for 1947; p.179 skips item 10; p.180 numbers an item "1"). One edit I made on the strength of a stream reading (the duplicated p.120 clause) was reverted after zooming into the scan showed the duplication is in the print. Lesson recorded: confirm against the zoomed scan before touching text the data already flags as printed.
- Tables checked in the data: Senate seats (sum 104), National Assembly (342), provincial assemblies.
- The legacy raw layer inside the same file (`"text"` blocks of garbled OCR such as ".V", "iv.") is not what readers show; the page-book layer is what was proofread.

### Economics 12 — COMPLETE (phase 7, part 1)

- Compared with the scans so far: front matter, contents, Chapter 1 (scans 016–039), Chapter 2 (035–060) and Chapter 3 up to printed p.66 (scans 061–081). **0 transcription errors found, 0 data changes.** The data file already records every printed misprint ("retained as printed" notes), and the ones spot-checked against zoomed scans were correct.
- Method caveat (honest): the scans are 616×830 px, and I read the Urdu by eye with no Urdu OCR available. This reliably catches missing/duplicated paragraphs, wrong numbers, wrong tables and changed words, but a one-dot or one-diacritic slip can be missed. Early in this chapter I read scans faster than the matching stream text, so printed pp. 27–58 were compared at paragraph level rather than line by line; those pages are worth a second pass if line-level certainty is needed.
- Update: Chapters 3 (rest), 4, 5, 6 and Chapter 7 up to printed p.121 compared (scans 082–136), still 0 errors, 0 data changes. Pace restored to line level.
- Update 2: Chapter 7 (rest), 8, 9 up to printed p.181 compared (scans 137–196), 0 errors, 0 data changes. Two stream artefacts (headings without body, MCQ options) were checked against the data and are present there; they come from my dedupe, not from the data.
- Update 3: through scan 266 (printed p.251, stream ¶4780) compared, 0 errors, 0 data changes. Covers chapter 11 end (zakat/ushr, model paper, MCQs, pp.239-248) and chapter 12 start (foreign trade, exports, composition table).
- Update 4: through scan 289 (printed p.274, stream ¶5142) compared, 0 errors, 0 data changes. Chapter 12 (foreign trade, balance of payments, ECO/SAARC/WTO, exchange rates, model paper) complete; chapter 13 (Islamic economic system) begun.
- Update 5: through scan 301 (printed p.286, stream ¶5324) compared. 1 error fixed in data: p.283 "آمدنی کا خسارہ اور مزد دیکھتا ہے" had a stray word "مزد" (printed: "اور دیکھتا ہے"), 5 occurrences corrected (logged in docs/qa/proofreading_fixes.tsv). Everything else matched; p.275 last sentence (dangling "افراد میں خود … دنیا کا کوئی اور نظام ایسی عمدہ") is printed that way and kept.
- Update 6 (final): scans 302–322 compared (chapter 13 end, model paper, 2018-19 budget appendix, 2018 and 2019 board papers), 0 further errors. Result for Economics 12: all 322 scans compared; 1 genuine misprint fixed (stray "مزد" on p.283, 5 mirrored occurrences). The budget table numbers and the English table labels were checked against the data. Caveat as above: eye-reading may miss a single dot or diacritic.

### Islamiat Ikhtiari 12 — COMPLETE (phase 7, part 2)
- Compared ALL scans 001–256 (printed pp.1–251, front matter, chapters 1–6, back matter and author notes) against the Urdu stream; 0 text errors found, 0 data changes. Checked in detail: all cropped right-edge lines (bracketed in data), the p.82 and p.96 matching tables, the p.148 MCQ options, the p.155 factor list (printed "نفسیاتی"). Data notes about printed slips (e.g. "مزد" is Economics only; here "اس سے لیے", "ظرفہ تماشہ", "فاشی", "احادث", "9 ستمبر 2001ء") match the scans.
- Remaining in Economics: printed p.181–end (scans ~197–322).

### Islamic History 12 — COMPLETE (phase 7, part 3)
- Compared ALL scans 000–230 (printed pp.1–223, front matter, lessons 1–42, bibliography, covers) against the Urdu stream. 2 genuine errors fixed in the proofread layer (both logged in docs/qa/proofreading_fixes.tsv): (1) p.12 heading and text "یزید بن ہبیرہ" corrected to the printed "یزید بن ہیرہ" (11 occurrences); (2) p.15 "منصور نے بربر کے خلاف" corrected to the printed "منظور نے بربر کے خلاف" (4 occurrences; the data's own note said it was kept as printed but 4 of 7 copies had been silently "corrected"). Pp.36–37 are missing from the scan (documented in the data).
- Result: 231 scans compared, 2 printed spellings restored (15 occurrences, all in the proofread layer; the legacy OCR layer was left alone). Everything else — including the many printed slips the data notes already record (e.g. "وزیر افضل", "مکتفی", "طغرل ۱۰۲۳ء", "۱۶۹۰ء", "مستعصم نے ... بڑے عہدے دیئے") — matched the scan. Pp.36–37 are missing from the scan set; pp.180–181 appear twice (scans 183/184 vs 185/186); no other gaps.

### Mutalia-e-Quran 12 — partly verified against the scans (phase 7, part 4)
- Actually viewed and matching the data, 0 errors: scans 0–7, 72–107 (Surah al-Ma'idah 5:60–120 end, Surah al-Nur lesson 9 and 10 through the exercises) and 188–231. Nothing changed in `js/quran_12_data.js`.
- **Not viewed** (image reads returned "media removed: request limit" repeatedly): scans 8–71 and 108–187. For these only the extracted text was read (consistent; Arabic ayat match the Uthmani cache). They remain **to be proofread against the scans**.
- Printed slips the data already annotates were kept as printed.

### Urdu 11 — COMPLETE (phase 8, part 1)
- Compared all 203 scans (`Document 2_1` … `_203`: front matter, 14 prose lessons, 13 poems, 8 ghazal sections, exercises, the whole farhang glossary, author notes, national anthem, back cover) against the Urdu stream and the glossary tables. Some scans were read at crop level to settle blurred words; where an image read failed it was retried until the page was actually viewed.
- 34 log rows (some cover several occurrences) logged in `docs/qa/proofreading_fixes.tsv` (`urdu11` rows). Kinds: restored printed wording (قُوائے عمل, تحفۂ خلوص, بٹے بیانوے, تچی for چابک, درنگ, تیس چالیس فٹ, «پایا دُرِّ مراد بڑی خاک چھان کے»); dialect spellings restored as printed in the Daroga/Khoji dialogue; a duplicated phrase removed; two glossary entries corrected (کھداوند, کٹا ہوا تنا).
- Two omissions filled: the paragraph «میرا کلام میرے پاس کبھی کچھ نہ رہا…» in Ghalib's first letter (scan 112, with new EN/PS lines) and exercise 1 items (ب)–(ہ) on scan 184 (with EN/PS lines). The new EN/PS lines are machine-drafted and need native review like the rest.
- Left as printed: the book's own slips and the print run/price line on the back cover (not in the data).

### Islamiat Lazmi 11 — read through, 0 changes (phase 8, part 2)
- Viewed scans 004–073 (both halves of each photo spread: printed pp.1–137, the Q&A pages, the closing boxed quotations) beside the Urdu stream. This was a reading comparison of the Urdu body text, not a word-by-word diff of every Arabic ayah: no mismatch showed up, so `js/isl_11_data.js` was not changed. Arabic verses and hadith still need checking against a Mushaf/source (as the data's own notes say).
- Not viewed: scans 001–003 (front cover, contents, imprint). The data's own source notes already flag a clipped word in Q3 (printed «حجۃ الوداع») and the photographed pages' clipped edges; those were kept as noted.
### Islamiat Ikhtiari 11 — every scan viewed, 3 changes (phase 8, part 3)

Scans 1 and 3–301 (file 2 does not exist in the source) were each opened and compared against the book's paragraph stream. Scans 1–7 and 229–301 were re-viewed after an image-limit gap, so this entry covers the whole book. Changes (all logged in `docs/qa/proofreading_fixes.tsv`):

- printed p.267: «بدو چونکہ کہ» → «بدو چونکا کہ» (as printed).
- printed p.283: «ابو مالک غیاث» → «ابو ملک غیاث» (Akhtal).
- contents table (scan 6): the chapter/letter column had English and Urdu cells swapped; 12 cells corrected.

Kept as printed: the exercise labels of printed p.289 (see the section note), the repeated numeral 3 on p.274, "شمس الحق ظہیر" on the title verso against "شمس الحسین ظہیر" in the author notes.

### Mutalia-e-Quran 11 — every scan viewed, 3 changes (phase 8, part 4)

Scans 4–193 (the whole book; 1–3 are the cover and ad page) were each opened and compared against the paragraph stream and the vocabulary and MCQ tables. Changes (logged in `docs/qa/proofreading_fixes.tsv`):

- printed p.128 (al-Anfal intro): «مال کا بلا جان» → «مال کا مل جانا» (English gap filled: "into one's hands").
- printed p.183 (al-Ahqaf 46:32): «کو بس کر سکے گا» → «کو نہ بے بس کر سکے گا اور نہ اُس کے سوا».
- printed p.6 (merit of al-Baqara): Sahih Muslim reference «۷۸۰» → «۸۰» as printed, in the Urdu and English lines.

Kept as printed: the "منافقین" wording in items 5–6 of printed p.21 and the numbering quirks already noted in the data.

### HPE 11 — every scan viewed, 1 change (phase 8, part 5)

Scans 1 and 3–148 (file 2 does not exist; printed pp.37–38 are absent from the source) were each opened and compared against the paragraph stream and the tables (calorie tables pp.12–13, field-event score sheet, hockey measurements). Scans 1–73 were viewed in a second pass after an image-limit gap; scans 74–148 were viewed first. Change (logged in `docs/qa/proofreading_fixes.tsv`):

- printed p.85: the print gives the Berlin Olympics as «1836ء»; data now reads as printed and the source note says so (the English line keeps 1936).

Kept as printed and already annotated: the relay-team "چھ کھلاڑی" line, "63 سالوں", «دھڑ سوا اختتامی لکیر» on p.52, "Charle Bucher"/"Nikson Koszen" spellings, the Latin-letter abbreviations on the credits page.


### English 12 — phase 9, started (partial)

Scans viewed against the data: front matter, contents, Unit 1 in full (printed pp.1–15), Unit 2 text, glossary and exercises (pp.16–24), Unit 4 pp.32–34, Unit 5 pp.43–45. Beyond those, the book was cross-checked only by comparing the repeated copies of each sentence inside `english_12_data.js` (`tools/qa/variants.js`, 149 groups left, nearly all dash/quote/spacing differences) — not against the other scans. Changes (in `proofreading_fixes.tsv`): "The Last Leaf" p.44 had a garbled line ("your chances for a little now/And then… Try to can buy") restored to "…chances for getting well… Try to eat a little now. And then… and then I can buy"; p.43 and p.45 sentence ends (", After" → ". After"; "night?" → "night."); "/" used as a full stop in three Truck Art sentences; Unit 1 "Mu 'tah", "Al-khattab" and the Surah al-Hashr citation made consistent; a missing blank ("it's ________"); the Hubble dash/quote/comma differences. Clipped words at the scan edge (Truck Art, Hubble) were left as printed. Not done: the other ~150 pages of English 12 and English 11 against their scans.

Update: scans of Unit 3 (printed pp.25–31), Unit 5 pp.46–52 and Unit 6 pp.53–58 were also viewed against the data; no further mismatches (printed slips such as "Doughter", "apparant", "lesson,decrease" are kept as printed and annotated). English 12 viewed so far: pp.1–58 except Truck Art p.35 onward and The Last Leaf text p.43; the rest (Units 7–19, pp.61–190) and English 11 are not yet compared against their scans.
