# Content rights audit

Made by `node tools/rights/audit_markings.js --write` (it changes nothing). Scope: the typed book text and data the website and the app serve (`js/*.js` data files), Classes 1 to 12. **Not scanned:** pictures (covers, figures, `assets/`): their text cannot be searched here and they must be looked at by a person (the covers carry the Textbook Board's mark).

## Decision

**Nothing was removed.** No written permission of a rights holder is on file (`FINDINGS_REGISTER.md` S-06, `docs/permissions/` is empty), so the rule of `CONTENT_RIGHTS.md` leaves every marking in place. Credits and rights notices are attribution and stay even with a permission. The "Not for sale" and free-distribution marks are listed for a decision by the owner with a lawyer.

| Category | Matches | Decision |
|---|---:|---|
| not-for-sale | 5807 | FLAG - not removed: removal needs the rights holder's written permission (none on file, S-06) and legal advice |
| free-distribution | 209 | FLAG - not removed: same as above; a free-distribution mark on a book we show under a subscription is the most sensitive case |
| rights-notice | 776 | KEEP - a copyright / rights notice is attribution and stays in any case |
| credit | 7320 | KEEP - names of authors, reviewers, editors, illustrators are attribution; removal also needs each person's consent and legal advice |
| board | 2494 | KEEP - the publisher's name; shows who made the book and must not suggest that SpaceBook is the publisher |

### What the matches are

Most "Not for sale" matches are **the scan's watermark text that ended up inside the typed pages** (for example in the Class 12 Physics and Chemistry data: a page footer in the middle of a paragraph), not a deliberate notice. Some are our own transcription notes ("Not For Sale is printed at the lower right"). The title-page lines ("Free From Government - NOT FOR SALE - Khyber Pakhtunkhwa Textbook Board Peshawar") are the book's own legend. Removing the stray watermark text would also remove the legend, so it waits for the same permission.

| Kind | Category | Matches |
|---|---|---:|
| data file | board | 1845 |
| data file | credit | 5514 |
| data file | free-distribution | 149 |
| data file | not-for-sale | 5733 |
| data file | rights-notice | 669 |
| other | board | 155 |
| other | credit | 432 |
| other | free-distribution | 11 |
| other | not-for-sale | 13 |
| other | rights-notice | 8 |
| page book | board | 494 |
| page book | credit | 1374 |
| page book | free-distribution | 49 |
| page book | not-for-sale | 61 |
| page book | rights-notice | 99 |

322 files scanned, 16606 matches in total; the full list (file, class, subject, page when the data gives it, a short snippet) is `content_rights_findings.csv`.

## Files with a "Not for sale" or free-distribution mark (for review)

| Class | Subject | File | Not for sale | Free distribution | Credit lines |
|---|---|---|---:|---:|---:|
| Class 1 | Mathematics | `js/math_1_book.js` | 1 | 0 | 33 |
| Class 1 | nazira | `js/nazira_1_book.js` | 2 | 0 | 5 |
| Class 10 | English | `js/english_10_data.js` | 2 | 1 | 26 |
| Class 10 | Mathematics | `js/math_10_book_data.js` | 1 | 1 | 2 |
| Class 10 | biology | `js/biology_10_book_data.js` | 2 | 1 | 12 |
| Class 10 | biology | `js/biology_10_front_source.js` | 2 | 1 | 0 |
| Class 10 | biology | `js/biology_10_unit10_source.js` | 1 | 0 | 0 |
| Class 10 | biology | `js/biology_10_unit11_source.js` | 1 | 0 | 0 |
| Class 10 | biology | `js/biology_10_unit12_source.js` | 1 | 0 | 0 |
| Class 10 | biology | `js/biology_10_unit13_source.js` | 1 | 0 | 0 |
| Class 10 | biology | `js/biology_10_unit14_source.js` | 1 | 0 | 0 |
| Class 10 | biology | `js/biology_10_unit15_source.js` | 1 | 0 | 0 |
| Class 10 | biology | `js/biology_10_unit16_source.js` | 1 | 0 | 3 |
| Class 10 | biology | `js/biology_10_unit17_source.js` | 1 | 0 | 1 |
| Class 10 | biology | `js/biology_10_unit18_source.js` | 1 | 0 | 0 |
| Class 10 | chemistry | `js/chemistry_10_source_data.js` | 2 | 1 | 5 |
| Class 10 | physics | `js/physics_10_book_data.js` | 1 | 1 | 22 |
| Class 10 | physics | `js/physics_10_source_data.js` | 9 | 1 | 16 |
| Class 11 | Chemistry | `js/chem_11_data.js` | 6 | 0 | 37 |
| Class 11 | Civics | `js/civics_11_data.js` | 1 | 0 | 27 |
| Class 11 | Computer Science | `js/cs_11_book.js` | 0 | 1 | 28 |
| Class 11 | English | `js/eng_11_book.js` | 2 | 2 | 90 |
| Class 11 | English | `js/eng_11_data.js` | 31 | 1 | 86 |
| Class 11 | HPE | `js/hpe_11_book.js` | 5 | 0 | 34 |
| Class 11 | HPE | `js/hpe_11_data.js` | 10 | 1 | 18 |
| Class 11 | Islamiat | `js/isl_11_data.js` | 105 | 0 | 24 |
| Class 11 | Statistics | `js/stat_11_book.js` | 6 | 0 | 12 |
| Class 11 | Statistics | `js/stat_11_data.js` | 3 | 0 | 10 |
| Class 11 | ikhtiari | `js/ikhtiari_11_data.js` | 3 | 0 | 88 |
| Class 11 | ishist | `js/ishist_11_book.js` | 0 | 1 | 49 |
| Class 11 | ishist | `js/ishist_11_data.js` | 0 | 1 | 42 |
| Class 11 | mq | `js/mq_11_book.js` | 5 | 5 | 53 |
| Class 11 | mq | `js/mq_11_data.js` | 11 | 3 | 26 |
| Class 12 | Chemistry | `js/chem_12_data.js` | 2315 | 4 | 245 |
| Class 12 | Civics | `js/civics_12_book.js` | 5 | 5 | 22 |
| Class 12 | Civics | `js/civics_12_data.js` | 19 | 10 | 81 |
| Class 12 | English | `js/english_12_book.js` | 9 | 3 | 48 |
| Class 12 | English | `js/english_12_data.js` | 12 | 3 | 124 |
| Class 12 | HPE | `js/hpe_12_book.js` | 5 | 0 | 24 |
| Class 12 | HPE | `js/hpe_12_data.js` | 82 | 0 | 60 |
| Class 12 | Islamiat | `js/islamiat_ikhtiari_12_book.js` | 0 | 1 | 90 |
| Class 12 | Islamiat | `js/islamiat_ikhtiari_12_data.js` | 279 | 4 | 224 |
| Class 12 | Mathematics | `js/math_12_data.js` | 2 | 1 | 12 |
| Class 12 | Mathematics | `js/math_12_pagebook_data.js` | 1 | 1 | 0 |
| Class 12 | Pakistan Studies | `js/pakstudy_12_book.js` | 5 | 6 | 44 |
| Class 12 | Pakistan Studies | `js/pakstudy_12_data.js` | 17 | 13 | 145 |
| Class 12 | Physics | `js/phys_12_data.js` | 2297 | 5 | 32 |
| Class 12 | Quran | `js/quran_12_book.js` | 4 | 4 | 53 |
| Class 12 | Quran | `js/quran_12_data.js` | 18 | 7 | 140 |
| Class 12 | Statistics | `js/stat_12_data.js` | 186 | 0 | 41 |
| Class 12 | Urdu | `js/urdu_12_book.js` | 5 | 5 | 194 |
| Class 12 | Urdu | `js/urdu_12_data.js` | 244 | 10 | 582 |
| Class 12 | computer | `js/computer_12_book.js` | 3 | 3 | 7 |
| Class 12 | computer | `js/computer_12_data.js` | 7 | 3 | 22 |
| Class 12 | islamic | `js/islamic_history_12_book.js` | 4 | 4 | 27 |
| Class 12 | islamic | `js/islamic_history_12_data.js` | 30 | 7 | 58 |
| Class 12 | statistics | `js/statistics_12_book_data.js` | 2 | 0 | 3 |
| Class 2 | English | `js/english_2_data.js` | 1 | 1 | 5 |
| Class 2 | General Knowledge | `js/gk_2_data.js` | 1 | 1 | 0 |
| Class 2 | Mathematics | `js/math_2_data.js` | 1 | 1 | 73 |
| Class 2 | Urdu | `js/urdu_2_data.js` | 1 | 1 | 13 |
| Class 2 | islamyat | `js/islamyat_2_data.js` | 1 | 1 | 7 |
| Class 2 | nazira | `js/nazira_2_data.js` | 3 | 0 | 6 |
| Class 3 | English | `js/english_3_data.js` | 1 | 0 | 6 |
| Class 3 | Mathematics | `js/math_3_book_text.js` | 2 | 0 | 2 |
| Class 3 | Mathematics | `js/math_3_data.js` | 1 | 1 | 18 |
| Class 3 | islamyat | `js/islamyat_3_data.js` | 1 | 1 | 34 |
| Class 4 | English | `js/english_4_data.js` | 1 | 1 | 13 |
| Class 4 | Mathematics | `js/math_4_data.js` | 1 | 1 | 11 |
| Class 4 | Urdu | `js/urdu_4_data.js` | 1 | 1 | 29 |
| Class 5 | English | `js/english_5_data.js` | 1 | 2 | 15 |
| Class 5 | Islamiat | `js/islamiat_5_data.js` | 2 | 2 | 27 |
| Class 5 | Mathematics | `js/math_5_data.js` | 2 | 1 | 8 |
| Class 5 | Pashto | `js/pashto_5_data.js` | 2 | 2 | 71 |
| Class 5 | Urdu | `js/urdu_5_data.js` | 2 | 2 | 12 |
| Class 5 | general | `js/general_science_5_data.js` | 1 | 1 | 16 |
| Class 5 | social | `js/social_studies_5_data.js` | 0 | 5 | 1 |
| Class 5 | social | `js/social_studies_um_5_data.js` | 2 | 5 | 24 |
| Class 6 | English | `js/english_6_data.js` | 1 | 1 | 17 |
| Class 6 | Mathematics | `js/math_6_data.js` | 1 | 1 | 17 |
| Class 6 | Urdu | `js/urdu_6_data.js` | 1 | 2 | 10 |
| Class 6 | computer | `js/computer_6_data.js` | 0 | 3 | 17 |
| Class 6 | general | `js/general_science_6_data.js` | 1 | 1 | 10 |
| Class 7 | English | `js/english_7_data.js` | 1 | 1 | 33 |
| Class 7 | Mathematics | `js/math_7_data.js` | 1 | 1 | 99 |
| Class 7 | computer | `js/computer_7_data.js` | 0 | 3 | 7 |
| Class 7 | general | `js/general_science_7_data.js` | 1 | 1 | 20 |
| Class 7 | history | `js/history_7_data.js` | 0 | 7 | 17 |
| Class 8 | Mathematics | `js/math_8_data.js` | 1 | 1 | 58 |
| Class 8 | Pashto | `js/pashto_8_data.js` | 0 | 1 | 15 |
| Class 9 | Drawing | `js/drawing_9_data.js` | 0 | 3 | 19 |
| Class 9 | English | `js/english_9_book.js` | 0 | 9 | 22 |
| Class 9 | computer | `js/computer_9_data.js` | 1 | 1 | 15 |
| class not in the file name | English | `js/data_eng.js` | 0 | 5 | 4 |
| class not in the file name | English | `js/english_data.js` | 0 | 6 | 12 |
| class not in the file name | lexicon | `js/lexicon_data.js` | 0 | 1 | 64 |
| class not in the file name | test | `js/test_prep_bank.js` | 0 | 10 | 44 |
