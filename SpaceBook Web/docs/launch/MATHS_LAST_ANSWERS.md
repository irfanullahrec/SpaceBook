# The last 171 Mathematics answers (Classes 5 to 8)

Date 2026-10-27. Before: 177 exercise questions had no answer (`FINDINGS_REGISTER.md` C-11): 171 in Mathematics 5 to 8 and 6 in Class 10 Urdu. After: **7** (the 6 Urdu questions, whose source pages are missing, and one Class 8 question with two right options). The list was produced by `node --max-old-space-size=6144 tools/launch/exercise_coverage.js --list-unanswered <file>` and every question was answered from the printed page and the data typed with it (scans under `D:\SpaceBook\Books`, page files under `docs/source-verification/class-N/math/pages`).

## What was answered

| Class | Questions | What they were |
|---|---|---|
| 5 | 26 | Unit 7 Geometry: labelling six quadrilaterals (Ex. 3 Q1), squares and rectangles to draw with protractor and ruler (Ex. 3 Q2, Q3, Review 7 Q8, Q9), angles to draw (Review 7 Q2) |
| 6 | 31 | "Hamza’s number" clues (Unit 1), the odd one out (Unit 2), "is it a set" and "write the set" examples, finite, infinite, singleton and universal sets (Unit 5) |
| 7 | 102 | numbers between 70,000 and 80,000; four operations and properties of rational numbers; squares of fractions; the carpet problem; plotting points (8.5, Review 8); Zara’s walk and the crayon-and-eraser graph; unit conversion; quadrilaterals, polygons, interior angles, circles (11.1 to 11.4, Review 11); line symmetry, rotations, translations (12.1, 12.3, Review 12); line, pie and bar graphs, frequency tables, histograms, mean of grouped data (13.2 to 13.5, Review 13) |
| 8 | 12 | significant figures MCQ (Review 1 Q1 b), Venn diagram of Exercise 5.3 Q14, "evaluate x" of Unit 7 Think Higher, frequency table and highest marks of Exercise 11.3 Q2 |

## How they are stored (so a rebuild keeps them)

* **Classes 5, 6, 7:** as `sol` (Classes 5, 6) and `solution` / `ss` / `sm` / `endsolution` lines (Classes 6, 7) in the page files, rebuilt with `build_math5.py`, `build_math6.py`, `build_math7.py`. These builders reproduce the committed `js/math_N_data.js` and `js/math_N_solutions.js` exactly plus the new answers (checked: no existing solution changed or lost).
* **Class 8:** `js/math_8_data.js` and `js/math_8_solutions.js` are **not** reproducible from the Class 8 page files with `build_math8.py` (a rebuild drops all 3,238 solution ids). So `docs/source-verification/class-8/tools/add_last_answers8.py` finds each question by its printed text, gives it a solution id and adds the entry (12 added, 0 existing entries changed); the entries are also in `class-8/math/gen_solutions.json`. Do not run `build_math8.py` without restoring the two js files.
* The answers are the same on the website and in the App (`sync_app.js`, `pack_books.js`).

## How they were made

* Every number is computed from the typed data (fractions with exact arithmetic, frequency tables and mean by counting, pie angles = value / total x 360, rotations and translations on the typed vertices), so a table or an angle cannot disagree with the data on the page.
* Drawings are answered with the construction steps and the values to plot (a drawing cannot be shown in text); open-ended questions are marked as model answers ("Model answer", "for example", "other answers are possible").
* Each step is written in English, Urdu and Pashto.

## What to check (human review list)

* 16 answers were read from small printed drawings or grids (Class 7: naming the figures of 11.1 Q2, the lines of symmetry of 11.1 Q7, 12.1 Q1, Review 12 Q2 and Q4, regular / convex polygons of Review 11 Q6, the rotations and translations on printed grids of 12.1 Q4, 12.3 Q1 and Q2, Review 12 Q6, Q10, Q11). The grid vertices were typed from low-resolution scans and are approximate (for example a translated corner can fall outside the printed grid), so each of these answers ends with a step asking the student to check it with the teacher.
* Where the book is inconsistent, the answer says so: Class 6 Unit 5 (the LCM of 12, 18, 30 is 180, the book prints 130), Class 7 Think Higher p. 196 (the lengths cannot be split into two equal groups as printed: one length, 24.1 km, is more than half of the total), Exercise 13.3 Q4 (1,080 students are stated, the table adds up to 845), Exercise 13.4 Q2 (23 blood groups are printed for 25 people), Exercise 11.3 Q2 of Class 8 (21 marks are printed for 25 students), Review 6 Q5 a) of Class 7 (no set A is defined; read as N).
* Exercise 5.3 Q14 of Class 8: "both pizza and burger" is read as the whole overlap of the two circles (4 + 6 = 10); a teacher who wants only the region outside the third circle would say 4. The step shows both numbers.
* **On screen:** checked in a real browser by pressing Ans in Classes 5, 6, 7 and 8 (`tests/launch/maths_answers_browser.js`). That check found that on a computer the Ans buttons of Classes 5, 7, 8 and 11 had been reading Class 6's answers (finding M-01, fixed the same day in `js/sb_book_spread.js` and `js/math6_reader.js`), so the older answers of those classes are also shown correctly now.
* No teacher has read these answers (as for the 5,170 answers of Classes 11 and 12).

## The 7 that are left

| Book | Question | Why |
|---|---|---|
| Class 10 Urdu | 6 questions | the printed pages that hold the passage are missing from the scans |
| Class 8 Maths | Review Exercise 1 Q1 b) "Which of these have 3 significant figures?" | the printed key gives two right options (iii and iv); the coverage tool cannot score a question with two right options. The key and the solution state both |
