# -*- coding: utf-8 -*-
"""Class 12 Islamiat Ikhtiari (KPTBB, Urdu medium): one reviewed section per printed page (virtual mode, see engine.py)."""
from pathlib import Path
from cfgs._base import *

KEY = 'islopt'
DATA_FILE, GLOBAL = 'islamiat_ikhtiari_12_data.js', 'ISLAMIAT_OPT_12_DATA'
BANK_FILES, BANK_KEY = 'islopt12_exercise_banks.js', 'islopt'
JPG = Path('D:/SpaceBook/Books/12th/12th Islamiat Ikhtiari/JPG')
VIRTUAL = True
TOTAL_JPG = 0
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Islamiat Ikhtiari', 'islamiat_ikhtiari_12_book.js', 'ISLAMIAT_IKHTIARI_12_BOOK', 'Islamiat Ikhtiari 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th Islamiat Ikhtiari/JPG']


def sec_kind(sec):
    i = sec['id']
    if '-exercise-' in i or '-activities-' in i:
        return 'ex'
    if '-bm-' in i:
        return 'back'
    return 'text'
