# Open-book view (full screen): coverage

`js/sb_book_spread.js` turns the **Lessons** and **Exercises** tabs into two facing pages when a workspace is in full screen (odd page left, even page right; right-to-left books mirror). It adds Previous / Next (and the arrow keys), shows answers and solutions in a large window, and collapses the chapter list to its numbers.

It works in two ways:

1. **True pages** – books stored in the shared page format (`CLS1_BOOKS` … `CLS10_BOOKS`, `MATH_5/6/7/8/11_DATA`). Every printed page is rebuilt from the book data in printed order, so a page that ends one topic and starts the next appears once, with its printed number.
2. **One card per scan** – older readers that already draw one card per source scan (Class 11 sciences, Class 12 books). The cards become the pages, in order, labelled with their scan number.

Books whose data holds whole topics, not pages, are left in their normal view (nothing is invented).

## State on 2026-10-21 (full-screen sweep, chapter 1 of each book)

| Group | Result |
|---|---|
| Classes 1–8, every sourced book | true pages |
| Class 9: Urdu, Islamiat, Computer, Pak Studies, General Science, HPE, Drawing, Islamiat Ikhtiari, Quran | true pages |
| Class 10: Chemistry, Urdu, Pak Studies, Computer, Science, HPE, Drawing, Islamiat, Ikhtiari, Quran | true pages |
| Class 11 Mathematics | true pages (`MATH_11_DATA`) |
| Class 11: Chemistry, Biology, Statistics, Physics, Computer Science, English, Islamic History, Ikhtiari, Civics, Urdu, Mutalia-e-Quran, HPE, Islamiat | one card per scan |
| Class 12: Chemistry, Biology, Physics, English, Urdu, Pak Studies, Civics, Economics, HPE, Islamiat Ikhtiari | one card per scan |
| Class 9 Chemistry | **rebuilt page by page 2026-10-21** (267 scans, `docs/source-verification/class-9/chem/`), true pages |
| Class 9 Biology | **rebuilt page by page 2026-10-21** (225 scans, `docs/source-verification/class-9/biology/gen.py` -> `bio/pages`), true pages |
| Class 10 Physics | **rebuilt page by page 2026-10-21** (7 scan PDFs, 279 pages; Units 10-12 typed from the scans in `class-10/phys10/fix/`, English only; Units 13-18 from the earlier page build) |
| Class 10 Biology | **rebuilt page by page 2026-10-21** (197 scans, `class-10/bio10/gen.py`), true pages, English + Urdu + Pashto text from the dataset |
| Class 8 Drawing, HPE, Pashto | **rebuilt page by page 2026-10-21** from the scans (Drawing 121, HPE 122, Pashto 232 pages); Pashto modern poems and long prose are summarised per page (copyright), glossary typed in full |
| Class 10 Mathematics | **typed page by page 2026-10-21** (314 scans, `class-10/math/pages`, English only, Venn/graph figures drawn by `venn_svg.py`); answer pages are appended after the printed page 269 spread |
| Class 9: Mathematics; Class 12: Mathematics, Statistics | topic-based data, **not converted** |

Not checked one by one: Class 9 English (some cards very tall), Class 12 Computer (one very tall card), Class 12 Islamic History and Quran, Class 9 Physics.

## What a "not converted" book needs

Its data would have to be rebuilt page by page from the scans in `D:\SpaceBook\Books\<class>\` in the shared page format (`@page` markers, as the Class 5–8 books were). Until then the normal card view stays.

## Release note

`lazy.html`, `content/sw_version.js`, the offline map and the script inventory are generated files. `index.html` now loads `js/sb_book_spread.js`, so they must be regenerated from a clean checkout (`RELEASE_AND_ROLLBACK.md`, section 1) before this ships. `tests/contract/hooks.json` and the hook test already include the two new hooks (`switchSubjectTab`, `switchMathTab`).

## Page tabs (2026-10-21)
Every lesson page in this view (and in the Lessons tab cards) carries the fixed bar **Board SLOs / Exercise** with the sub-tabs **MCQs, SQs, LQs** (`js/sb_page_tabs.js`; details in `PROGRESS_LOG.md`, entry 2026-10-21). Exercise pages and the pages after the last exercise carry none.
