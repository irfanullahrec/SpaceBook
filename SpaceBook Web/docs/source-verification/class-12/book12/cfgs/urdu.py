# -*- coding: utf-8 -*-
"""Class 12 Urdu (Lazmi, KPTBB): one JPG per book page (001.jpg ... 274.jpg).

JPG 0 = imprint, 1 = title page, 2 = learning outcomes, 3-4 = contents, JPG n (n >= 5) = printed page n - 4 (the footers read 11 on JPG 15 ...).
The reviewed records (PDF scans of two pages) do not line up with the pages (a record starts in the middle of a page), so the book is cut as
ONE stream by the words every page begins with (GLOBAL_MODE, 'K B words' lines in splits_*.txt where K = the JPG index)."""
import re
from pathlib import Path
from cfgs._base import *

KEY = 'urdu'
DATA_FILE, GLOBAL = 'urdu_12_data.js', 'URDU_12_DATA'
BANK_FILES, BANK_KEY = 'urdu12_exercise_banks.js', 'urdu'
JPG = Path('D:/SpaceBook/Books/12th/12th Urdu/JPG')
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Urdu', 'urdu_12_book.js', 'URDU_12_BOOK', 'Urdu (Lazmi) 12 (KPTBB)')
BOOK_SOURCE = ['12th Urdu/JPG']
TOTAL_JPG = len(sorted(JPG.glob('*.jpg')))
GLOBAL_MODE = True
GLOBAL_DIRECT = ('urdu12-glossary',)      # the glossary records are one per two pages: scan by scan, split lines '10000 + PDF number T table rows'
FM_TITLE = ('ابتدائیہ', 'Front matter', 'سریزه')
BACK_TITLE = ('آخری صفحات', 'Last pages', 'وروستي مخونه')
EX_TITLE = ('مشق', 'Exercise', 'تمرین')


def printed_of(jpg):
    return jpg - 4 if 5 <= jpg <= 271 else 268 if jpg == 273 else None


def pdf_jpgs(k):
    return (2 * k - 6, 2 * k - 5) if 3 <= k <= 139 else None


BLANK = {272: 'The inside back cover (a framed verse): the photograph is a mirror image and cannot be read.'}
