# -*- coding: utf-8 -*-
"""Class 12 Computer Science (KPTBB, English medium): every PDF page was photographed as two halves, NNN_page_1.jpg (left, lower printed page) and
NNN_page_2.jpg (right); the scan number NNN is the PDF page of the reviewed data."""
import re
from pathlib import Path
from cfgs._base import *

KEY = 'comp'
DATA_FILE, GLOBAL = 'computer_12_data.js', 'COMP_12_DATA'
BANK_FILES, BANK_KEY = 'comp12_exercise_banks.js', 'comp'
JPG = Path('D:/SpaceBook/Books/12th/12th Computer Science/JPG')
LANGS = ['en', 'ur', 'ps']
ORIG = 'text'
BOOK_NAME = ('Computer Science', 'computer_12_book.js', 'COMP_12_BOOK', 'Computer Science 12 (KPTBB, English medium)')
BOOK_SOURCE = ['12th Computer Science/JPG']
_files = sorted(JPG.glob('*.jpg'))
TOTAL_JPG = len(_files)
_by_pdf = {}
for _j, _f in enumerate(_files):
    _m = re.match(r'(\d+)_page_(\d+)', _f.name)
    if _m:
        _by_pdf.setdefault(int(_m.group(1)), []).append((int(_m.group(2)), _j))


def pdf_jpgs(k):
    return tuple(j for _, j in sorted(_by_pdf.get(k, []))) or None
