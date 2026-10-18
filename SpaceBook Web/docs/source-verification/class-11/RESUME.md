# Class 11 resume note (written 2026-10-12)

## Status
- **Chemistry (chemistryfull.pdf, 419 PDF pages, printed = PDF − 5): all 419 pages installed** in `js/chem_11_data.js` (coverage check: 419 present, 0 missing, 0 duplicate). Every page is saved with status **unresolved**: Urdu/Pashto are my own translations awaiting native review; scans are skewed/clipped, so many lines carry `[scan obscured]`; some printed typos retained and labelled in each page's `sourceNote`.
- Back cover (PDF 419): the national anthem lyrics were not transcribed (heading only).
- Skipped by user instruction: Mathematics, Physics, Biology.
- **Not started:** Statistics (`D:\SpaceBook\Books\11th\11th stastic`, has a `jpg` subfolder), English, Urdu, Pakistan Studies (none in the 11th folder list), Computer Science, Civics, Economics (not in folder list), General Science (not in list), Drawing (not in list), HPE, Islamiat compulsory, Islamiat Ikhtiari, Islamic History, Mutalia-e-Quran.
  Source folders present: `11TH islamyAT LAZIMI`, `11english`, `11th Hpe`, `11th Maths`(skip), `11th Urdu`, `11th bio`(skip), `11th chemisty`, `11th civic`, `11th computer`, `11th mutalia quran`, `11th physics`(skip), `11th stastic`, `11thslamyat ekhtyri`, `islamic history`.

## Blocker that stopped the run
**Drive C: has 0 GB free and D: has about 3 GB.** Symptoms: memory file write failed (ENOSPC), PowerShell output formatting failed, `head`/`cut` pipes fail. Free several GB on C: (the Claude session `.jsonl` transcripts under `C:\Users\Shehroz Khan\.claude\projects\D--SpaceBook\` are about 1.5 GB each) before resuming, otherwise the session itself can fail to save.

## Workaround for every shell command
```
export TMPDIR="D:/SpaceBook/SpaceBook Web/tmp" TEMP="D:/SpaceBook/SpaceBook Web/tmp" TMP="D:/SpaceBook/SpaceBook Web/tmp"
... > "D:/SpaceBook/SpaceBook Web/tmp/fin.log" 2>&1   # then read the log with the Read tool
```
Delete old renders in `tmp/class-11/*.png` as you go.

## Pipeline per batch of 4 pages (Chemistry; reuse the same pattern for other books)
1. `python render_chemistry_page.py N` (renders to `tmp/class-11/chemistry-pNNN.png`) and view the PNGs.
2. Write `prepare_chemistry_AAA_BBB.py` using `chemlib.py` helpers (`page, add, head, cell, table, eq, save, lab, fig, svg, T, mcq`) and a local `Flow` class (paragraph ids must appear exactly once in the flow; tables via `s['tables']` + flow `{type:'table',index}`; glossary/index pages need a heading paragraph plus a lowercase vocabulary term).
3. `python prepare_...py`, then `python finalize_chemistry_page.py N unresolved "<title>" --issue "<text>"` (installs into `js/chem_11_data.js`, runs `verify_chemistry_pages.cjs`, saves the checkpoint).
Verifier rules: Urdu/Pashto must contain script whenever English has ≥4 Latin letters; vocabulary keys lowercase; coded SVG only; equations carry latex + accessible text.

## Next action
Free disk space on C:, then inventory the Statistics book (PDF pages, `jpg` folder vs PDF, printed-page offset), then continue in the assignment order.

---
## Update — Statistics (started after the user said "start statistics of class 11")
- Source: `D:\Books\11th\11th stastic` — 244 jpg scans numbered 1–247 (scans 2, 3, 238 absent); 8 derivative PDFs (253 pages) used for cross-checks only; 8 docx are scan exports.
- Printed page = scan − 8 from scan 9 (page 1) up to scan 14 (page 7); **printed page 6 is absent** (scan 13=p5, scan 14=p7). Scan 15 and 16 are the same printed page 8 (scan 16 is a duplicate crop, recorded and not installed). After that scan − 8 holds (scan 17 = p9 … scan 61 = p53, scan 62 = p54 = Unit 2).
- Installed so far: scans 1,4–15,17–62 in `js/stat_11_data.js` (reader `renderStatistics11Tab`, wired by `wire_statistics.py`). Chapter ids `stat11-*`. Unit 1 complete (scans 9–61).
- Tools: `statlib.py` (page/add/head/table/Flow), `statcharts.py` (bar, line, histogram, step, xy), `prepare_stat_AAA_BBB.py` per batch, `finalize_stat_page.py N unresolved "note" --issue "..."` (installs via `install_stat_page.py`, verifies with `verify_stat_pages.cjs`, writes `statistics-progress.json`).
- Handwritten ticks on printed MCQ options are NOT recorded as answers. Statistics chapters 8, 9, answers, glossary, index may be absent from the scan set (scan set ends at printed page 237).
- Next: scan 63 (printed page 55, Unit 2 content).
- Progress 2026-10-12: Statistics installed through scan 98 (printed page 90, start of Unit 3). Unit 2 (Measures of Central Tendency) complete (scans 62–97). Next: scan 99 (printed page 91, Unit 3 outcomes continue). Scan 16 is a duplicate of scan 15 and is not installed; printed page 6 is absent from the local scans.

- Statistics installed through scan 110 (printed p102, start of 3.5.1 Standard deviation). Next scan 111. Prep scripts prepare_stat_103_106.py, prepare_stat_107_110.py use build() helper (seq of paragraph keys, E:key, T:i).
- Statistics installed through scan 126 (printed p118, Example 3.19 start). Next scan 127. Use stathelp.py build() helper in prepare_stat_111_114.py onward.
- Statistics installed through scan 138 (printed p130, Bowley method working). Next scan 139. stathelp.build() supports F:i for figures; skew() figure helper lives in prepare_stat_135_138.py.
- Statistics installed through scan 146 (printed p138, Unit 3 key points). Next scan 147. Gotcha: equation keys must differ from paragraph keys on the same page (id collision -> lesson visibility assertion).
- Statistics installed through scan 154 (printed p146; Unit 3 incl. Exercise-3 done, Unit 4 Index Numbers started at scan 153 with chapter key index-numbers). Next scan 155.
- Statistics installed through scan 166 (printed p158, Example 4.8 Fisher working). Next scan 167.
- Statistics installed through scan 169 (printed p161); scan 170 is a duplicate of scan 168 (printed 160), recorded excluded-duplicate in statistics-progress.json. Next scan 171.
- Statistics installed through scan 174 (printed p164); scan 171 is a duplicate of scan 169 (excluded-duplicate). Next scan 175.
- Statistics installed through scan 182 (printed p172): Unit 4 Index Numbers + Exercise-4 complete. Next scan 183 (Unit 5 expected: regression-correlation).
- Statistics installed through scan 190 (printed p180, 5.2 Correlation types). Next scan 191. Unit 5 chapter key regression-correlation.
- Statistics installed through scan 198 (printed p188, Example 5.8 rank correlation). Next scan 199.
- Statistics installed through scan 202 (printed p192, Exercise-5 Q5.3 (ix)). Next scan 203. Verifier gotcha: option text with only Latin names needs Pashto/Urdu script (transliterate).
- Statistics installed through scan 206 (printed p196): Unit 5 + Exercise-5 complete; Unit 6 Time Series started at scan 205 (chapter key time-series). Next scan 207.
- Statistics installed through scan 214 (printed p204, Example 6.5 start). Next scan 215.
- Statistics installed through scan 222 (printed p212, Exercise-6 Q6.2 (vi)). Next scan 223.
- Statistics installed through scan 226 (printed p216): Unit 6 + Exercise-6 complete; Unit 7 Vital Statistics started at scan 225 (chapter key vital-statistics). Next scan 227.
- Statistics installed through scan 234 (printed p224, Example 7.4 start). Next scan 235. Scan 238 absent from source set.
- Statistics installed through scan 239 (printed p229); scan 238 recorded absent-from-source. Next scan 240.
- STATISTICS COMPLETE (2026-10-12): scans 1,4-15,17-37,... all 241 installed through scan 247 (printed p237); scans 2,3,238 absent from source; scans 16,170,171 duplicates excluded. Units 8-9, answers, glossary, index are not in the local scans (chapters carry sourceGap). All pages status unresolved (translations need native review). Next subject: English (inventory D:\SpaceBook\Books	th first).

## English 11 (started after Statistics, 2026-10-12)
- Source: D:\SpaceBook\Books\11th\11english\jpg — 240 half-page photos NNN_page_H.jpg. Scan n = 2*(NNN-1)+H (n odd = _page_1, even = _page_2). Printed page = scan − 9 (scan 10 = printed p1, Unit 1 opener). Right/left edges are clipped on many halves → [scan obscured].
- Also english.docx (OCR text, extracted to english-docx-text.txt with PAGEBREAK markers) and english1-7.pdf (image-only) for cross-checks.
- Tooling: gen_eng11.py (done), wire_english.py + wire_english_data.py (applied), englib.py/enghelp.py/install_eng_page.py/finalize_eng_page.py/verify_eng_pages.cjs, js/eng_11_data.js (ENG_11_DATA, chapters eng11-front-matter, eng11-u01…u22, eng11-back-matter). Prep scripts prepare_eng_AAA_BBB.py; run `python finalize_eng_page.py N unresolved "note" --issue "..."` per scan; progress in english-progress.json.
- Layout tags for tabs: sec.layout in outcomes|glossary|vocabulary|language|grammar|writing|exercise (see renderEnglish11Tab). Poems/lyrics: summarise if copyright uncertain, else transcribe.
- ENGLISH COMPLETE: all 240 scans (1–240, front matter through back matter incl. feedback form and Qur'an verse card) installed and verified together on 2026-10-12. Reader tooling: gen_eng11.py, englib.py, enghelp.py, install/finalize_eng_page.py, verify_eng_pages.cjs. Rules learned: call F.tb(i) for every table before F.done(); modern essays summarised, pre-1975 works kept in full; unique paragraph keys per page. Next book: Urdu (inventory D:\SpaceBook\Books	th	th Urdu first).

## Islamiat (Compulsory) 11 (2026-10-13)
- Source: D:\SpaceBook\Books\11th\11TH islamyAT LAZIMI\jpg — 73 photos x 2 halves = 146 scans; scan = 2*(NNN-1)+H. Reader js/isl_11_data.js (ISL_11_DATA, key isl, subject cls11-isl); tooling mkbook.py output: isllib.py/islhelp.py/install_isl_page.py/finalize_isl_page.py/verify_isl_pages.cjs/wire_book_isl.py; prep scripts prepare_isl_AAA_BBB.py; run ./runisl.sh prepare_isl_AAA_BBB.py n1 n2 ...
- Chapter keys: u00 (intro) u01 (beliefs) u02 (Islamic identity, printed 39-95; chapter heading scan 45) u03 (printed 96-107: Example of the Messenger, mercy, rights, etc. — NOTE earlier scans 73-98 were re-keyed u02 because the social-duties/rights material is still Chapter 2 in the book; u03 = Chapter 3 "اسوۂ رسول" from scan 103) u04 (Qur'an & Hadith, printed 108-137) back-matter (scans 145-146, unnumbered boxed quotes).
- ISLAMIAT COMPLETE: all 146 scans installed, all status unresolved, verify_isl_pages.cjs passed for scans 1-146 (2026-10-13). Source gaps flagged per page (clipped lines, scan 143 Q3 wording, misprinted verse references). Arabic from scan needs Mushaf check; translations are ours and need native review.
- Next: HPE (11th Hpe, 147 scans), then Mutalia-e-Quran 193, Urdu 207, Civics 226, Islamiat Ikhtiari 299, Computer Science 330, Islamic History 344.

## HPE 11 (started 2026-10-13)
- Source: D:\SpaceBook\Books\11th\11th Hpe\jpg\HPE book UM 11th class KPK_N.jpg (147 files; N=2 missing). Scan = file number if N=1, else N-1. Printed page = scan-5 up to scan 40 (printed 36); then printed pages 37–38 are ABSENT from the source (scan 41 = printed 39), so printed = scan-2 from scan 41. Urdu medium; Word text in hpe-hpeN-text.txt.
- Tooling: books/hpe.json via mkbook.py (applied); hpelib.py/hpehelp.py/install_hpe_page.py/finalize_hpe_page.py/verify_hpe_pages.cjs/js/hpe_11_data.js; prep scripts prepare_hpe_AAA_BBB.py; run `K=hpe ./runisl.sh prepare_hpe_AAA_BBB.py n1 n2 …`. Chapter keys u00 intro, u01 non-communicable diseases, u02 respiratory, u03 narcotics, u04 emergency, u05 biomechanics (printed 38+), u06 fitness plan, u07 sports rules, front-matter/back-matter.
- HPE COMPLETE: all 147 scans installed (through printed 145), all status unresolved; verify_hpe_pages.cjs passed for scans 1-147 (2026-10-13). Printed pages 37-38 absent from the source (noted in sourceGap). Photographs replaced by simplified coded SVG schematics; translations ours, need native review.
- Next: Mutalia-e-Quran 193 (11th mutalia quran), then Urdu 207, Civics 226, Islamiat Ikhtiari 299, Computer Science 330, Islamic History 344.

## Mutalia-e-Quran 11 (started 2026-10-13)
- Source: D:\SpaceBook\Books\11th\11th mutalia quran\jpg\Mutlia_e_Quran_Book_KPK_11_N.jpg, N=1..193 contiguous; scan = N; printed page = scan-3 (scan 9 = printed 6). Urdu-source; 21 lessons (TOC scan 7): lesson starts printed 6,15,23,32,41,52,63,71,80,89,97,105,113,121,128,138,145,153,162,171,179 (scan = printed+3). Scan 192/193: back matter (national anthem on 193; check 192).
- Tooling: books/mq.json via mkbook.py (applied, wire_book_mq.py applied); mqlib.py/mqhelp.py/install_mq_page.py/finalize_mq_page.py/verify_mq_pages.cjs/js/mq_11_data.js; prep scripts prepare_mq_AAA_BBB.py; run `K=mq ./runisl.sh prepare_mq_AAA_BBB.py n1 n2 …`. Chapter keys front-matter, l01..l21, back-matter. Qur'anic line model: one `kind='quran'` para per printed Arabic line = Arabic + newline + translation in each language (helper A(s,ar,ur,en,ps)).
- **COMPLETE 2026-10-13: scans 1–193 installed and verified (verify_mq_pages.cjs 1–193: 0 failures).** All pages status unresolved; Arabic read from scan (needs Mushaf check), English/Pashto our translations (need native review). Back matter scans 191–193 (TIF/attestation, KPTBB feedback form in English, national anthem + publisher block). Next book: Urdu 207 (11th Urdu/JPG, Document 2_N.jpg), then Civics 226, Islamiat Ikhtiari 299, Computer Science 330, Islamic History 344.

## Urdu Compulsory — COMPLETE (2026-10-13)
- 202 pages installed/verified (scan 6 missing in source, printed page 71 absent). Status all `unresolved`; translations ours.

## Civics — COMPLETE (2026-10-13)
- 226/226 scans installed in `js/civics_11_data.js` and verified together with `node verify_civics_pages.cjs $(seq 1 226)`. Scan = printed + 9. Scans skewed/cut with pen marks (ignored); missing words restored from Word text where noted. Glossary (scans 216–224), author page 225, back matter 226. Status all `unresolved`.
- Next: Islamiat Ikhtiari (299), Computer Science (330), Islamic History (344).

## Islamiat Ikhtiari — COMPLETE (2026-10-13)
- Source D:\SpaceBook\Books\11th\11thslamyat ekhtyri\jpg\Islamiat Ikhtiari book 11 class KPK_<file>.jpg; 299 scans (files 2 and 31 missing). scan 1=file 1; scans 2–29 = file+1; scans ≥30 = file = scan+2; printed = scan−6 (scans ≤29) or scan−5 (scans ≥30); printed page 24 absent.
- Toolchain: ikhtiarilib.py / ikhtiarihelp.py / books/ikhtiari.json / wire_book_ikhtiari.py (done, wired). Scans 1–289 installed (chapter 5 complete; chapter 6 in progress) (chapter 4 complete; chapter 5 started) (chapters 1–3 complete; chapter 4 in progress) and verified through `node verify_ikhtiari_pages.cjs`. Run: `K=ikhtiari ./runisl.sh prepare_ikhtiari_A_B.py n1 n2 …`.
- Ikhtiari COMPLETE; next book: Computer Science (330 scans, folder 11th computer)..

## Computer Science (Class 11, English source) — COMPLETE 330/330 (2026-10-13)
- Toolchain: `books/cs.json` -> mkbook.py -> cslib/cshelp/install_cs_page/finalize_cs_page/verify_cs_pages.cjs/wire_book_cs.py (wired). Memory: class11-cs-pipeline.md. scan n = file `{(n+1)//2:03d}_page_{1|2}.jpg`; printed = scan − 9.
- Run: `K=cs timeout 115 ./runisl.sh prepare_cs_AAA_BBB.py n1 n2 n3 n4`, then `node verify_cs_pages.cjs n1 …`.
- COMPLETE: scans 1–330 (front matter, Units 1–8, MCQ answers, glossary, index, about the author, closing page) installed; verify_cs_pages.cjs 1–330 passed in three batches. All pages status unresolved; Urdu/Pashto are our translations (need native review). Next book: Islamic History (344 scans, folder `islamic history`).

## Islamic History — COMPLETE (344/344, 2026-10-13)
- Toolchain: ishist* (ishistlib.py/ishisthelp.py/install_ishist_page.py/finalize_ishist_page.py/verify_ishist_pages.cjs/wire_book_ishist.py, js/ishist_11_data.js). Memory: class11-ishist-pipeline.md. Source is Urdu; scan n = printed n-1 from scan 129 on (scans 127-128 duplicate printed 126-127).
- Run: `K=ishist timeout 115 ./runisl.sh prepare_ishist_AAA_BBB.py n1 n2 n3 n4`, then `node verify_ishist_pages.cjs n1 …`.
- Scans 1–344 installed (ch1–ch20, exercises, back-matter "Important questions" and two closing framed-text pages); verify_ishist_pages.cjs 1–344 passed in three batches (115/115/114 pages).
- Honest caveats: all pages status unresolved; English/Pashto/Urdu-rendered translations are ours and need native review; printed 36 cropped; printed 1 title page not scanned; scans 127-128 are duplicates; many pages cropped at an edge; scans 319–322 are close-up crops without page numbers; scans 341–342 are cropped at the top (final questions 9, 21 and the start of 22 not visible); handwriting/circled marks excluded; quotations and numerals read from print and need checking against complete scans.
- ALL Class 11 books except the skipped Mathematics, Physics and Biology are now done.
