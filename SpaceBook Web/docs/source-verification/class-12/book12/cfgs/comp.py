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


def route(k, group):
    """The inside back cover (verse) and the outer back cover are one page each, photographed in two halves / as a picture: the text goes on the first JPG."""
    if k in (165, 166):
        return {pdf_jpgs(k)[0]: None}
    return None


BLANK = {pdf_jpgs(165)[1]: 'The other half of the framed verse on the inside back cover (the page was photographed in two halves).',
         pdf_jpgs(166)[1]: 'The outer back cover: a picture of a fort, no text.',
         pdf_jpgs(164)[1]: 'The right half of the About Authors page 316 (the page was photographed in two halves).'}


def printed_of(jpg):
    """Every photograph of the book is in order: printed page = scan index - 9 from the first unit's opening page (the footers read 108, 109 ... 316 on scans 117, 118 ... 325). The reviewed data's own page labels are off by one in 13 scans."""
    return jpg - 9 if 10 <= jpg <= 325 else None
