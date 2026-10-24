# -*- coding: utf-8 -*-
"""Class 12 Islamic History (KPTBB, Urdu medium): the reviewed data keeps one section per printed page, labelled with its printed number,
so the pages are built in virtual mode (one page per printed number; the scan files are not needed to place the text)."""
from pathlib import Path
from cfgs._base import *

KEY = 'islhist'
DATA_FILE, GLOBAL = 'islamic_history_12_data.js', 'ISLAMIC_HISTORY_12_DATA'
BANK_FILES, BANK_KEY = 'islhist12_exercise_banks.js', 'islhist'
JPG = Path('D:/SpaceBook/Books/12th/12th Islamic History/JPG')
VIRTUAL = True
TOTAL_JPG = 0
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Islamic History', 'islamic_history_12_book.js', 'ISLAMIC_HISTORY_12_BOOK', 'Islamic History 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th Islamic History/JPG']


def sec_kind(sec):
    i = sec['id']
    if 'exercise' in i:
        return 'ex'
    if 'backcover' in i or 'cover-None' in i:
        return 'back'
    return 'text'
