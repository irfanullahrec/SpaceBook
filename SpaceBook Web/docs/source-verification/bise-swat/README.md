# BISE Swat sources, tools and data

What the Board of Intermediate & Secondary Education, Saidu Sharif Swat publishes (https://www.bisess.edu.pk/site/, read 2026-10-20) and how it became `js/bise_swat_data.js`. The full description, findings and open points are in `docs/07_BISE_SWAT_ALIGNMENT.md`.

| Folder | What |
|---|---|
| `tools/` | `fetch_sources.py` (download), `check_links.py` (does each Board link work), `extract_slos.py` (curriculum PDFs to learning outcomes), `extract_book_slos.js` + `build_book_slos.py` (outcomes and section headings printed in the app's own textbooks, for subjects with no Board SLO list; raw dump not committed), `dump_app_chapters.js` (the app's own chapters), `build_bise.py` (builds `js/bise_swat_data.js`) |
| `data/` | `slos_*.json` (extracted from the Board's curriculum), `slos_book.json` (from the app's textbooks), `tos_tables.json` and `patterns.json` (hand-transcribed from the Board's page images; every total is checked by `tests/bise/data.js`), `link_status.json`, `app_chapters.json`, `page_syllabus_2026-10-20.html` (the Board's page, so the build is reproducible) |
| `sources/` | git-ignored: downloaded PDFs and their text |

Reading rules for the next person: `pdftotext -layout -enc UTF-8` gives no usable text for the Urdu papers and loses Maths symbols: read those from page images. The Board's server blocks browser-like User-Agents and Range requests (403): use `curl/8.4.0` as the tools do. Quote spaces in file names (`%20`).
