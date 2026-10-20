# BISE Swat (bisess.edu.pk) alignment — findings and work plan (2026-10-20)

## 1. What was collected and how much was actually read
Source pages: https://www.bisess.edu.pk/site/home/syllabus-model-papers, /emarking-model-papers/, /teacher-profile-form, the E-Answer Sheet PDF on the home page, the Scheme of Studies 2019.

| Collected | Count | Read how |
|---|---|---|
| Syllabus & Model Papers PDFs (Class 9: 39, 10: 43, 11: 21, 12: 21 text files) | 124 text extractions | text extracted with pdftotext; structure checked on every file (marks/time lines), full text read for: Physics 9 paper + marking scheme + ToS, Chemistry 9 ToS, Biology 9 ToS, Physics 12 ToS, English 10 ToS + marking scheme, Maths 10 and Chemistry 11 marking schemes, Physics 10 curriculum (SLO format, weights, assessment pattern), Biology 10 curriculum (SLO format) |
| National Curriculum PDFs with SLOs, Class 9–10 | Physics, Chemistry, Biology, Maths (also General Maths), English, Computer Science, Pak Studies | structure and SLO format only; about 4,000 SLO bullets in total |
| E-Answer Sheet PDF (26 pages, scanned) | 1 | pages 1–3 viewed |
| E-Marking (Model Papers) page | 12 JPEGs from Google Drive | 2 viewed |
| Scheme of Studies 2019 (10-page scan) | 1 | pages 2 and 4 viewed |

Not read in full: most marking schemes, the other curricula in depth, Urdu/Islamiat/Mutala-e-Quran files (pdftotext garbles Urdu), and Maths files (symbols are lost). Those need page images or OCR before they can be used as data. Three Class 11 Islamiat PDFs downloaded as 239-byte error pages and must be re-fetched.

## 2. Findings
### 2.1 The three item types (Board vocabulary)
MCQ (Section A, bubble sheet), RRQ = restricted-response question (Section B, short), ERQ = extended-response question (Section C, long). Every ToS lists, per chapter, how many MCQ/RRQ/ERQ items and marks it gets, plus the cognitive level (knowledge/understanding/application) and difficulty (easy/moderate/difficult).

| Class and subject | A: MCQ | B: RRQ | C: ERQ | Total |
|---|---|---|---|---|
| 9/10 Physics, Chemistry, Biology | 12 (20 min) | any 8 of 11 × 4 = 32 | any 3 of 4 × 7 = 21 | 65 |
| 9/10 English, Maths, Gen. Maths | 15 | 36 | 24 | 75 |
| 9/10 Computer Science | 11 | 28 | 16 | 55 |
| 9 Pak Studies | 10 | 24 (1h45 total) | 16 | 50 |
| 11/12 Physics, Chemistry | 18 | any 10 of 13 × 4 = 40 | any 3 of 4 × 9 = 27 | 85 |
| 11/12 English | 20 | 50 (any 10, Q1–2 compulsory, 5 marks each) | 30 (Q14 essay compulsory + 2 of 3) | 100 |
| 11 Maths, CS | 20 / 15 | 36 | 24 | 80 / 75 |
Total time for B + C: 2h 40m (Class 9/10 Pak Studies 1h 45m, Computer Science 2h 15m).

### 2.2 SLOs (Student Learning Outcomes)
- Class 10 (and 9) National Curriculum PDFs list SLOs per chapter under "Major Concepts and Learning Outcomes", grouped by level (Knowledge / Understanding / Application / Skills) and by skill (Analysing, Performing and Recording...).
- They also carry: chapter weighting in %, theory and practical periods per chapter (Physics: 18 chapters, 240 theory + 120 practical periods), list of standard practicals, assessment objectives, recommended paper pattern and sections (Physics: Mechanics ch.1–7 40%, Heat 10%, Waves 15%, Electricity 30%, Atomic 5%).
- Each ToS row ties a chapter, topic and sub-topic to one chosen SLO, an item type, marks, cognitive level and difficulty.
- The marking schemes show the "possible answers" in 1-mark points with the textbook page (KPTBB).
- The app already uses "SLO" in some tab names, but there it means a question bank, not the Board's SLOs. Naming needs care.

### 2.3 E-Marking (Model Papers) page
These are 12 images of real printed Annual-II 2025 papers (e.g. "PR IX (A-II-B4) 25 Chemistry"), for English, Chemistry, Physics in Class 9–12. Useful as real past-paper style: wording of "Answer any EIGHT parts", marks split as 2+2=4 or 1+1+1+1=4, and Section C parts (a) 4 + (b) 3.

### 2.4 E-Answer sheet (on-screen marking)
Barcode-numbered booklet. Roll number is 6 digit columns of bubbles, plus subject and class bubbles. One page per Section B question, three per Section C question; unattempted pages left blank; black ballpoint only; answer inside the allotted space; no space between lines. On-screen marking is done by e-markers who register on the Board's form (not something students use).

### 2.5 Scheme of Studies 2019
IX–X Humanities: Urdu 75, English 75, General Maths 75, General Science 75, Islamiat 50, Mutalae Quran-e-Hakeem, Pak Studies 50, two electives 75 + 75 (550 marks). Classes I–V: Urdu 100, English 100, Maths 100, Nazira 50, GK 100, regional language 100.

## 3. Work plan (in this order)
Each step ends with the full test run (`node tools/build/all.js --check` and the existing tests) and a browser check, and is committed separately.

**Phase A — Data (no UI yet)**
A1. Fix the downloads: re-fetch the three 239-byte Class 11 Islamiat files; keep all source files in `docs/source-verification/bise-swat/` (links + hashes only, not the PDFs themselves, until the copyright note below is settled).
A2. Build `content/bise/paper_pattern.json` from table 2.1 (per class and subject: sections, counts, marks, time, choice rule). Hand-checked.
A3. Build `content/bise/<class>_<subject>.json` for Physics, Chemistry, Biology (9, 10, 11, 12) first: chapters with weighting % and periods, SLOs per chapter with level, ToS rows (items, marks, cognitive level, difficulty).
A4. Map each ToS chapter to the app's chapter ids (`getSubjectChapterList`) in a reviewed table; flag any chapter that does not exist in the book data.
A5. Repeat for English, Maths, Computer Science, Pak Studies; use page images (not pdftotext) for Maths and Urdu.

**Phase B — Student features**
B1. Board-style paper mode inside Tests Prep: Section A timed bubble MCQs, Section B "attempt any N" with rubric self-marking in 1-mark points, Section C parts with the 4+3 split. Paper built from the ToS weights, drawing on the MCQ bank and the existing exercises.
B2. SLO map per chapter: each lesson shows its SLOs; a student ticks them off or the app infers it from MCQ/exercise results; a "weak SLOs" list feeds the Study Plan.
B3. Model Paper tab per subject (Board's own model papers + marking scheme as 1-mark rubric points, with the KPTBB page reference), starting with Physics/Chemistry/Biology 9 and 10.
B4. Answer-sheet practice: printable and on-screen booklet (roll number bubbles, one box per question, Board rules, "leave blank if not attempted").
B5. Show chapter weight (marks) at the top of each chapter, from the ToS.

**Phase C — Later / needs owner decisions**
C1. Past papers from the E-Marking page, transcribed as text, with answers written in the rubric style.
C2. Subject list and marks per class driven by the Scheme of Studies (Humanities vs Science group).
C3. Possible teacher-side tool for rubric marking (not for students; confirm scope with the owner).

## 4. Risks and decisions for the owner
- Copyright: the Board's papers are public but not licensed for re-hosting. Link to the Board's files, or ask the Board for permission, before shipping the full paper text.
- pdftotext loses Urdu text and Maths symbols; those subjects must be done from page images.
- The word "SLO" is already used in the app for question banks. Decide whether to rename those tabs.
- Exact chapter numbering can differ between the Board's ToS and the book data; A4 must be reviewed by a person.
