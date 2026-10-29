# Munawar (Kanz) series, Classes 1-4

A private publisher's set of books, shown next to the Government books: clicking Class 1-8 asks **Government Books** or **Private Books**; Private asks for the **series**; "Munawar" opens the class's grid of Munawar books. Inside a book everything is the Government reader (tabs, open-book page view, sentence and word meanings in English / Urdu / Pashto, an Ans on every question, figures, games).

## How a book is wired

| What | Where |
|---|---|
| the list of 42 books (single source) | `tools/registry.py` -> `books.json`, `js/munawar_registry.js` (adds the books to `DATA.subjects` with `series: 'munawar'`), the `coverPageMap` lines in `js/app.js` |
| the two modals, the bar above the covers | `js/sb_private_books.js`, `css/sb_private.css`; `goToSubjects(classId, series)` in `js/app.js` |
| a book's data | `js/munawar_c<N>_<code>_book.js` -> `window.CLS<N>_BOOKS['mun-<code>']`, read by the class's own reader (`js/cls<N>_book_reader.js`: the key is the subject id minus `cls<N>-`) |
| covers | `tools/make_covers.py` (+ `make_covers.js`): our own artwork, `covers/Munawar/cls<N>-mun-<code>.webp` |
| the App | `ui/library/BoardChoice.kt`, `LibraryScreens.kt`; the catalog carries `series` (`tools/build/make_app_catalog.js`); covers via `tools/app/make_app_covers.py` |

Subject ids are `cls<N>-mun-<code>`; codes: `math eng gram urdu ugram isl gk prel waqf comp compbl sci sst`. Class 2 has no Urdu book and Class 4 no GK / Preliminary Knowledge / Waqfiyat-e-Aama in the supplied files.

## Transcribing a book (same as the Government books)

1. `python -P tools/render_pages.py c1-math 3 12` renders pages (outside the repository, `D:/SpaceBook_Helpers/munawar_jpg/<id>/`).
2. Write `<id>/pages/pNNN.txt` (NNN = PDF page index, 0-based, no gaps from p000) in the page syntax of `class-4/tools/build_book4.py` / `build_math6.py`, using the class's own figure ops (`class-1/tools/figs1.py`: `cnt`, `cards`, `train`, `stairs` ...). `@printed N` = printed page; every sentence `English || Urdu || Pashto` (Urdu-medium books: `Urdu || English || Pashto`, see `SLOT_ORDER` in `build_munawar.py`); `q` / `sol` for every question; `@issue` for anything that cannot be read.
3. `<id>/units.tsv` (from the contents page) and `<id>/vocab.tsv` (word, Urdu, Pashto).
4. `python -P tools/build_munawar.py <id>` (or `--all`), then regenerate the derived files (`node --max-old-space-size=8192 tools/build/all.js`, from a clean checkout) and `node tools/app/sync_app.js`.

## The source files (read this before promising a book)

The 42 PDFs in `D:\SpaceBook\Books\Private\Munawar` are **sample copies**: each page is one **437 x 547 pixel** image (about 48 dpi) with a diagonal "Munawar Publisher" / "SAMPLE" watermark. Consequences, found on 2026-10-29:

- Headings, big captions, numbers and large-print text read well; **small print does not** (learning-outcome lists, "Guidelines for Teachers" boxes, most captions, preface paragraphs), and **running Urdu text is unreadable** (Urdu, Urdu Grammar, Islamiyat, Waqfiyat-e-Aama and the Urdu lines of the bilingual books). Nothing unreadable is guessed: such text is left out and recorded as `@issue`.
- Some PDFs are shorter than their own contents pages (Mathematics 2 has 75 pages but its contents list Geometry on page 88; Mathematics 4 has 75 but lists Data Handling on page 92), so they look like partial extracts.
- A higher dpi only enlarges the page; it never shows more than the file holds. Full interactive books need the publisher's clean PDFs (or at least 150 dpi, no watermark).
- The contents pages were read for 20 books (`<id>/units.tsv`). The other 22 (English, Urdu, Urdu Grammar, Islamiyat, Waqfiyat-e-Aama, both bilingual Computer editions) have one placeholder unit, "Contents in preparation", because their contents tables are too small to read.
- Written permission from the publisher for showing the books should be filed with `docs/launch/CONTENT_RIGHTS.md` before release (open register item, same as the Government books).

## State (2026-10-29)

Built and wired: registry, builder, covers, modals, App dialogs, 42 data files. Transcribed: **c1-math pages 0-15 of 88** (front matter, Unit 1 printed pages 4-16: numbers 1-9, zero, number words, writing numbers, backward counting, ascending / descending order, activities on ordering and counting, before / between / after, the concept of ten, place value (tens and ones), the tables for numbers 0-10, 11-20 and 21-30; 62 answers). Everything else: units listed, pages awaiting review.
