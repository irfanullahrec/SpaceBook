"""The Munawar series ("Kanz", Classes 1-4): the list of books, the single source for everything generated about them.

    python docs/source-verification/private/munawar/tools/registry.py          writes books.json and js/munawar_registry.js
    python docs/source-verification/private/munawar/tools/registry.py --check  fails when either file is stale

Each book is one PDF in D:/SpaceBook/Books/Private/Munawar (not in git). They are *sample copies* of the publisher's books:
about 437 x 547 pixels a page, with a diagonal "Munawar Publisher" / "SAMPLE" watermark, so small print (all running Urdu
text, most captions) cannot be read from them. See README.md in this folder for what that means for the transcription.

A book is registered on the website as a subject of its class with `series: 'munawar'`:
    subject id   cls<N>-mun-<code>              e.g. cls1-mun-math
    book key     mun-<code>                     the key in window.CLS<N>_BOOKS (the class readers use subject id minus "cls<N>-")
    data file    js/munawar_c<N>_<code>_book.js built by build_munawar.py from <id>/pages/pNNN.txt and <id>/units.tsv
    cover        covers/Munawar/cls<N>-mun-<code>.webp  (made by make_covers.py, referenced from coverPageMap in js/app.js)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]          # docs/source-verification/private/munawar
APP = HERE.parents[3]                                # SpaceBook Web
PDF_DIR = 'D:/SpaceBook/Books/Private/Munawar'

# code -> (English name, Urdu name, emoji, medium, cover theme)
#   medium: en = English; ur = Urdu (slot order UR || EN || PS); bl = bilingual (English with an Urdu line under it)
SUBJECTS = {
    'math':   ('Kanz Mathematics',           'ریاضی',                 '📐', 'en', 'math'),
    'eng':    ('Kanz English',               'انگریزی',               '📖', 'en', 'english'),
    'gram':   ('Kanz English Grammar',       'انگریزی گرامر',         '✏️', 'bl', 'grammar'),
    'urdu':   ('Kanz Urdu',                  'اردو',                  '📜', 'ur', 'urdu'),
    'ugram':  ('Kanz Urdu Grammar',          'اردو قواعد',            '🖋️', 'ur', 'urdugrammar'),
    'isl':    ('Kanz Islamiyat',             'اسلامیات',              '🕌', 'ur', 'islamiyat'),
    'gk':     ('Kanz General Knowledge',     'جنرل نالج',             '🌍', 'en', 'gk'),
    'prel':   ('Kanz Preliminary Knowledge', 'ابتدائی معلومات',       '🧭', 'bl', 'prelim'),
    'waqf':   ('Kanz Waqfiyat-e-Aama',       'واقفیتِ عامہ',          '🧠', 'ur', 'waqf'),
    'comp':   ('Kanz Computer',              'کمپیوٹر',               '💻', 'en', 'computer'),
    'compbl': ('Kanz Computer (Bilingual)',  'کمپیوٹر (دو لسانی)',    '🖥️', 'bl', 'computer'),
    'sci':    ('Kanz Science',               'سائنس',                 '🔬', 'en', 'science'),
    'sst':    ('Kanz Social Studies',        'معاشرتی علوم',          '🗺️', 'en', 'sst'),
}

# (class, code, pdf file name, pages in the pdf)
BOOKS = [
    (1, 'comp',   'New Kanz Computer- 01 (Ch-6 AI Add) 03-01-26 Final-compressed.pdf', 48),
    (1, 'compbl', 'New Kanz Computer (BL)  1-compressed.pdf', 32),
    (1, 'eng',    'New Kanz English Book Class - 1-compressed.pdf', 72),
    (1, 'gram',   'New Kanz English Grammar -1-compressed.pdf', 32),
    (1, 'gk',     'New Kanz General Knowledge -1-compressed.pdf', 80),
    (1, 'isl',    'New Kanz Islamiyat Book 1-compressed.pdf', 40),
    (1, 'math',   'New Kanz Mathematics Book Class- 1-compressed.pdf', 88),
    (1, 'prel',   'New Kanz Preliminary  Knowledge 1-compressed.pdf', 64),
    (1, 'urdu',   'New Kanz Urdu Book Class -1-compressed.pdf', 80),
    (1, 'ugram',  'New Kanz Urdu Grammar - 1-compressed.pdf', 24),
    (1, 'waqf',   'New Kanz Waqfiyat-e-Aama - 1-compressed.pdf', 56),

    (2, 'comp',   'NK Computer 2 - EM (Revised) Added AI 0 08-01-26-compressed.pdf', 56),
    (2, 'compbl', 'New Kanz Computer (BL)  2-compressed.pdf', 40),
    (2, 'eng',    'New Kanz English Book Class - 2-compressed.pdf', 80),
    (2, 'gram',   'New Kanz English Grammar -2-compressed.pdf', 40),
    (2, 'gk',     'New Kanz General Knowledge -2-compressed.pdf', 80),
    (2, 'isl',    'New Kanz Islamiyat Book 2-compressed.pdf', 48),
    (2, 'math',   'New Kanz Mathematics Book Class- 2-compressed.pdf', 75),
    (2, 'prel',   'New Kanz Preliminary  Knowledge 2-compressed.pdf', 72),
    (2, 'ugram',  'New Kanz Urdu Grammar - 2-compressed.pdf', 24),
    (2, 'waqf',   'New Kanz Waqfiyat-e-Aama - 2-compressed.pdf', 56),

    (3, 'comp',   'New Kanz Computer- 03 (Added AI) 10-01-26-compressed.pdf', 64),
    (3, 'compbl', 'New Kanz Computer (BL)  3-compressed.pdf', 48),
    (3, 'eng',    'New Kanz English Book Class - 3-compressed.pdf', 96),
    (3, 'gram',   'New Kanz English Grammar -3-compressed.pdf', 48),
    (3, 'gk',     'New Kanz General Knowledge -3-compressed.pdf', 80),
    (3, 'isl',    'New Kanz Islamiyat Book 3-compressed.pdf', 56),
    (3, 'math',   'New Kanz Mathematics Book Class- 3-compressed.pdf', 80),
    (3, 'prel',   'New Kanz Preliminary  Knowledge 3-compressed.pdf', 80),
    (3, 'urdu',   'New Kanz Urdu Book Class -3-compressed.pdf', 88),
    (3, 'ugram',  'New Kanz Urdu Grammar - 3-compressed.pdf', 32),
    (3, 'waqf',   'New Kanz Waqfiyat-e-Aama - 3-compressed.pdf', 64),

    (4, 'comp',   'New Kanz Computer- 04 (Added AI) 16-01-26F-compressed.pdf', 64),
    (4, 'compbl', 'New Kanz Computer (BL)  4-compressed.pdf', 48),
    (4, 'eng',    'New Kanz English Book Class - 4-compressed.pdf', 104),
    (4, 'gram',   'New Kanz English Grammar -4-compressed.pdf', 56),
    (4, 'isl',    'New Kanz Islamiyat Book 4-compressed.pdf', 80),
    (4, 'math',   'New Kanz Mathematics Book Class- 4-compressed.pdf', 75),
    (4, 'sci',    'New Kanz Science  - 4-compressed.pdf', 112),
    (4, 'sst',    'New Kanz Social Studies- 4-compressed.pdf', 96),
    (4, 'urdu',   'New Kanz Urdu - 4-compressed.pdf', 82),
    (4, 'ugram',  'New Kanz Urdu Grammar - 4-compressed.pdf', 30),
]

# Which tools (figure generators, answer helpers) a class's books are built with: the class's own pipeline copy.
SERIES = {
    'id': 'munawar',
    'name': 'Munawar',
    'nameUrdu': 'منور',
    'line': 'Kanz Series',
    'publisher': 'Munawar Publisher',
    'classes': [1, 2, 3, 4],
}


def book_id(cls, code):
    return f'c{cls}-{code}'


def entries():
    out = []
    for cls, code, pdf, pages in BOOKS:
        name, ur, emoji, medium, theme = SUBJECTS[code]
        out.append({
            'id': book_id(cls, code), 'cls': cls, 'classId': f'cls{cls}', 'code': code,
            'subjectId': f'cls{cls}-mun-{code}', 'key': f'mun-{code}',
            'name': name, 'nameUrdu': ur, 'emoji': emoji, 'medium': medium, 'theme': theme,
            'pdf': pdf, 'pdfPages': pages,
            'cover': f'Munawar/cls{cls}-mun-{code}.webp',
            'dataFile': f'munawar_c{cls}_{code}_book.js',
        })
    return out


def unit_count(bid):
    """Units listed on the book's contents page (units.tsv); a book without one has a single placeholder unit."""
    f = HERE / bid / 'units.tsv'
    if not f.exists():
        return 1
    return sum(1 for l in f.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#')) or 1


def registry_js(es):
    """js/munawar_registry.js: adds the books to DATA.subjects (flagged series:'munawar') and describes the series."""
    subs = {}
    for e in es:
        subs.setdefault(e['classId'], []).append({
            'id': e['subjectId'], 'name': e['name'], 'nameUrdu': e['nameUrdu'], 'emoji': e['emoji'],
            'chapters': unit_count(e['id']), 'series': SERIES['id'], 'seriesBook': e['key'], 'medium': e['medium'],
            'cover': 'covers/' + e['cover'], 'pdfPages': e['pdfPages'],
        })
    lines = ['// Munawar series (Kanz, Classes 1-4): generated by docs/source-verification/private/munawar/tools/registry.py. Do not edit.',
             '// Adds the books to DATA.subjects with series:"munawar"; the Government list of a class never shows them (js/sb_private_books.js).',
             '(function () {', "  'use strict';",
             '  if (typeof DATA === "undefined") return;',
             '  DATA.series = DATA.series || {};',
             '  DATA.series.munawar = ' + json.dumps(SERIES, ensure_ascii=False) + ';',
             '  const add = ' + json.dumps(subs, ensure_ascii=False, separators=(',', ':')) + ';',
             '  Object.keys(add).forEach(function (cls) {',
             '    DATA.subjects[cls] = DATA.subjects[cls] || [];',
             '    add[cls].forEach(function (s) { if (!DATA.subjects[cls].some(function (x) { return x.id === s.id; })) DATA.subjects[cls].push(s); });',
             '  });',
             '})();', '']
    return '\n'.join(lines)


def main():
    es = entries()
    books_json = json.dumps({'series': SERIES, 'books': es}, ensure_ascii=False, indent=1) + '\n'
    js = registry_js(es)
    targets = [(HERE / 'books.json', books_json), (APP / 'js' / 'munawar_registry.js', js)]
    if '--check' in sys.argv:
        stale = [str(p) for p, t in targets if not p.exists() or p.read_text(encoding='utf-8') != t]
        if stale:
            sys.exit('stale: ' + ', '.join(stale))
        print('registry up to date:', len(es), 'books')
        return
    for p, t in targets:
        p.write_text(t, encoding='utf-8', newline='\n')
    print('wrote', len(es), 'books ->', targets[0][0].name, targets[1][0].name)


if __name__ == '__main__':
    main()
