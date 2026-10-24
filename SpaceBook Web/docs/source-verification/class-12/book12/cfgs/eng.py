# -*- coding: utf-8 -*-
"""Class 12 English (KPTBB, English medium): every PDF page of the book was photographed as two halves, NNN_page_1.jpg (left, lower
printed page) and NNN_page_2.jpg (right), so a scan's JPG files are known from their names (see engine.py)."""
import re
from pathlib import Path
from cfgs._base import *

KEY = 'eng'
DATA_FILE, GLOBAL = 'english_12_data.js', 'ENGLISH_12_DATA'
BANK_FILES, BANK_KEY = 'eng12_exercise_banks.js', 'eng'
JPG = Path('D:/SpaceBook/Books/12th/12th English/JPG')
LANGS = ['en', 'ur', 'ps']
ORIG = 'text'
BOOK_NAME = ('English', 'english_12_book.js', 'ENGLISH_12_BOOK', 'English 12 (KPTBB, English medium)')
BOOK_SOURCE = ['12th English/JPG']
_files = sorted(JPG.glob('*.jpg'))
TOTAL_JPG = len(_files)
_by_pdf = {}
for _j, _f in enumerate(_files):
    _m = re.match(r'(\d+)_page_(\d+)', _f.name)
    if _m:
        _by_pdf.setdefault(int(_m.group(1)), []).append((int(_m.group(2)), _j))


def pdf_jpgs(k):
    return tuple(j for _, j in sorted(_by_pdf.get(k, []))) or None


def sec_kind(sec):
    i = sec['id']
    if re.search(r'exercises|comprehension|writing|activities|vocab', i):
        return 'ex'
    if re.search(r'cover|imprint|foreword|acknowledg|toc', i):
        return 'back' if 'cover' in i and 'back' in i else 'text'
    return 'text'
