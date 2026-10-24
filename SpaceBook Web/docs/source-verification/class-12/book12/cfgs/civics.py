# -*- coding: utf-8 -*-
"""Class 12 Civics (KPTBB, Urdu medium).  JPG 000 = front cover, 001 = imprint, 002-005 = contents (4 pages), JPG j = printed page j-5
from JPG 006 (page 1, the chapter opening) to JPG 186 (page 181).  PDF scan k of the reviewed data = JPG 2k-5 and 2k-4."""
import re
from pathlib import Path

KEY = 'civics'
DATA_FILE, GLOBAL = 'civics_12_data.js', 'CIVICS_12_DATA'
BANK_FILES, BANK_KEY = 'civics12_exercise_banks.js', 'civics'
JPG = Path('D:/SpaceBook/Books/12th/12th Civics/JPG')
TOTAL_JPG = 187
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Civics', 'civics_12_book.js', 'CIVICS_12_BOOK', 'Shehriyat 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th Civics/JPG']
TABS = ['lesson', 'exercise']
OCR_DOCX = []
FM_TITLE = ('ابتدائیہ', 'Front matter', 'سریزه')
BACK_TITLE = ('آخری صفحات', 'Last pages', 'وروستي مخونه')
EX_TITLE = ('مشق', 'Exercise', 'تمرین')
DUPLICATE = {}
NOTES = {}
BLANK = {}


def printed_of(jpg):
    return jpg - 5 if 6 <= jpg <= 186 else None


def pdf_jpgs(k):
    if k == 1:
        return (0,)
    if 3 <= k <= 95:
        return (2 * k - 5, 2 * k - 4)
    return None


def route(k, group):
    if k == 1:
        return {0: None}
    if k == 3:
        return {1: lambda s: s['id'].endswith('imprint'), 2: lambda s: 'contents' in s['id']}
    if k == 4:
        return {3: None}
    if k == 5:
        return {5: lambda s: 'contents' in s['id']}
    return None


def sec_kind(sec):
    return 'ex' if 'exercise' in sec['id'] else 'text'


def is_front(ch):
    return ch['number'] == 'FM'
LINE_PARTS = True   # numbered list lines of an exercise are the parts of the numbered instruction above them
