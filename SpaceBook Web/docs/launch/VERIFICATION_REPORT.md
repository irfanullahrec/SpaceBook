# Verification report: what was checked, how, and by whom

Date: 2026-10-27. Scope: textbook coverage and accuracy (Phase 2). This page separates **automated checks**, **my own review** (an AI assistant reading scans and data, not a teacher), and **what only qualified people can sign off**. Nothing here is an expert approval.

## 1. Automated, exhaustive (every book, every chapter)

| Check | Result | Where |
|---|---|---|
| Every folder of `Books` is accounted for: 133 folders, 23,475 scan images, 36,005 PDF pages | 132 subjects mapped; 2 books of the app have no source (Class 7 Pashto folder is empty; Class 10 Islamiat is the Class 9 book); the 3 placeholder books (Class 1 Urdu and GK, Class 3 Urdu) have no scans | `COVERAGE_MANIFEST.md`, `books_inventory.json` |
| Every scan of a mapped book has a page-ledger row (PDF page, scan file, printed page, status, notes, chapter) | 87 books exact, 21 within a few pages (rows split or merged), 8 PDF-only, 1 spread book, 12 older books with no ledger, 2 differ (Class 1 English: the folder holds extracted figure images as well as pages; Class 10 Urdu: 181 files, 164 rows, pages 7, 64, 73, 75, 102 ... absent from the supplied scans) | same |
| Every question the app holds: has an answer, MCQ key names an option, no solution contradicts the printed key | **5,427 of 45,581 questions have no answer** (finding C-01); 124 MCQs whose answer matches no option; 9 clashes | `EXERCISE_COVERAGE.md`, `exercise_coverage.csv` |
| No chapter loses questions in future | `exercise_coverage.js --check` against the committed baseline | `exercise_coverage_baseline.json` |
| Arabic-script characters in the books all have a glyph in a bundled font | 183 characters, 0 missing | `FONT_COVERAGE.md` |
| The existing project checks | validate 1,288 · smoke 0 failed · lazy parity 0 differences · build fresh · PHP 491 | `TEST_MATRIX.md` |

## 2. My own review: a spot check against the scans (disclosed sampling)

I opened the scan and the typed page side by side for these printed pages. This is a sample of 4 pages out of about 20,000, not an audit.

| Book, printed page | Compared | Result |
|---|---|---|
| Class 5 Mathematics, p. 40 (Review Exercise 2, Q1 a to e) | question wording, the four options of each part, the learning-outcomes box and vocabulary box | identical; the five answers are right (HCF of 20, 48, 56 = 4; LCM of 33, 66, 81 = 1,782 recomputed) |
| Class 1 English, p. 63 (Grammar: proper nouns, question words) | every sentence, both "Read Me" boxes | identical text. **Observation O-1**: the five bullet sentences of exercise ii are printed without numbers; the app numbers them 18 to 22 (a running question number used by the answer system). The numbering is not "as printed". |
| Class 8 Mathematics, p. 134 (Q7 to Q13 and parts a to l) | all questions, all formulas, the heading 6.10 and the paragraph; the page note says the printed Example 1(a) ends "+ 5" (it should be "+ 6") and that this is kept as printed | identical; the printed misprint is preserved and flagged, not silently fixed |
| Class 12 Civics (Urdu medium), p. 113 (Q1 to Q3) | fill-in-the-blank sentences, MCQ stems and options, answers shown | identical wording. **Observation O-2**: printed option labels are Urdu letters (ا ب ج د); the app shows a b c d. |

## 3. What this review cannot establish

* That every word of every page equals the scan. The class pipelines recorded each page (ledger, `issues` notes: 6,748 of 20,095 ledger pages carry notes) but a second person has not compared them. Disagreements that the earlier sessions found are kept as notes in the ledger.
* The accuracy of the textbook's own content (the board's text is the source; where a printed answer or sentence looks wrong the pipeline keeps it and notes it).
* Translations (Urdu, Pashto, Arabic) and the Pashto and Urdu wording of the games and the feedback dialog: written or machine-assisted, not reviewed by a native specialist.
* Worked solutions and answers **written for the project** (not printed in the book): see section 4.
* Age suitability and psychological safety: my review of the reward and game rules (no streak pressure, no countdown without pause, no loss of lives by slow reading in the default mode, no manipulative notifications) is in `docs/launch/FINDINGS_REGISTER.md`; a child-development specialist has not reviewed it.

## 4. Answers written for the project

Each answer written in this work is stored as a `sol` line in the book's page file and is shown in the app as "SpaceBook answer · not printed in the textbook". Open-ended answers start with "Model answer" and the footer says other correct answers are possible. Answers I was not sure of say "needs a teacher's check" and the footer shows a warning. See `ANSWERS_WRITTEN.md` for the books done, the method of verification (numerical answers recomputed by script) and what is left.

## 5. Needs a person (human review list)

1. A teacher of each subject to read the answers written for the project (Class 11 and 12 books), starting with Islamic History, Islamiat, Mutalia-e-Quran, Civics and Economics where a wrong sentence matters most.
2. A native Pashto reader: the games' picture words, the arcade labels, the feedback dialog (Pashto is not written there yet).
3. A native Urdu reader for the Urdu labels of the new dialogs (written by me).
4. Someone with the printed books to settle the pages missing from the scans (Class 10 Urdu pp. 7, 64, 73, 75, 102 ...; Class 6 Maths pp. 157 to 158 are missing in every source).
5. The owner: permission to redistribute the textbook text and scans (the scans carry the watermark of a third-party site and "NOT FOR SALE").
