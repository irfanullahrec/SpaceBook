# Urdu, Pashto and Arabic fonts (bundled)

| File | Font | Used for | Licence |
|---|---|---|---|
| `NotoNastaliqUrdu-400.woff2`, `-700.woff2` | Noto Nastaliq Urdu | Urdu text (the traditional Nastaliq hand) | SIL OFL 1.1, `OFL-NotoNastaliqUrdu.txt` (Noto Project Authors, github.com/notofonts/nastaliq) |
| `NotoNaskhArabic-400.woff2`, `-700.woff2` | Noto Naskh Arabic | Pashto, Arabic reading text, Urdu interface words | SIL OFL 1.1, `OFL-NotoNaskhArabic.txt` (Noto Project Authors, github.com/notofonts/arabic) |
| `Amiri-400.woff2` | Amiri | Quranic and textbook Arabic with full diacritics | SIL OFL 1.1, `OFL-Amiri.txt` (Amiri Project Authors, github.com/aliftype/amiri) |

Where they come from: the npm packages `@fontsource/noto-nastaliq-urdu@5.3.0`, `@fontsource/noto-naskh-arabic@5.3.0` and `@fontsource/amiri@5.3.0` (the "arabic" subset files `*-arabic-400-normal.woff2`, `*-arabic-700-normal.woff2`), installed on 2026-10-27 into an empty folder with `npm install --ignore-scripts`. The files are used unchanged. The OFL allows bundling, embedding and redistributing them with software; it does not allow selling the fonts by themselves, and a changed version may not use a Reserved Font Name (none is declared in these three).

How they are used: `css/sb_fonts.css` declares each family under every name the stylesheets already use (Jameel Noori Nastaleeq, Urdu Typesetting, Pashto Koodak, Scheherazade New, Traditional Arabic, Lateef ...), so all existing font stacks resolve to these files without edits; a phone with none of those fonts installed draws the same letters as the PC. `unicode-range` limits each file to Arabic-script characters, so a page without them downloads none. The files are in the service worker's shell (`tools/build/make_offline.js` reads the `url()` lines), so they work offline.

Checks: `node tools/launch/font_coverage.js` (every Arabic-script character used in the books, the lexicon and the interface has a glyph in the font that is meant to draw it) and `node tests/launch/fonts_browser.js` (the files load, only when needed, and are used).

To add or update a font: install the package in an empty folder (`npm install --ignore-scripts`), copy the woff2 files and the LICENSE here, add `@font-face` lines to `css/sb_fonts.css`, regenerate the offline files (`node tools/build/all.js --only offline`).
