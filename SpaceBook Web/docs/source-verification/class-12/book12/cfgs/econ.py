# -*- coding: utf-8 -*-
"""Class 12 Economics (KPTBB, Urdu and English): one reviewed section per printed page (virtual mode, see engine.py)."""
from pathlib import Path
from cfgs._base import *

KEY = 'econ'
DATA_FILE, GLOBAL = 'economics_12_data.js', 'ECON_12_DATA'
BANK_FILES, BANK_KEY = 'econ12_exercise_banks.js', 'econ'
JPG = Path('D:/SpaceBook/Books/12th/12th Economics/JPG')
VIRTUAL = True
TOTAL_JPG = 0
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Economics', 'economics_12_book.js', 'ECON_12_BOOK', 'Economics 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th Economics/JPG']


def sec_kind(sec):
    i = sec['id']
    if '-model-' in i or '-papers-' in i:
        return 'ex'
    if '-appx-' in i:
        return 'back'
    return 'text'
