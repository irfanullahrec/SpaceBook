# -*- coding: utf-8 -*-
"""Class 12 Mutalia-e-Quran (KPTBB, Urdu medium): one reviewed scan per printed page; JPG j = PDF page j+1
(JPG 001 = advertisement); printed pages come from the reviewed data's labels (some printed numbers skip: 4 pages are missing)."""
from pathlib import Path
KEY = 'quran'
DATA_FILE, GLOBAL = 'quran_12_data.js', 'QURAN_12_DATA'
BANK_FILES, BANK_KEY = 'quran12_exercise_banks.js', 'quran'
JPG = Path('D:/SpaceBook/Books/12th/12th Mutalia e Quran/JPG')
TOTAL_JPG = 231
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Mutalia-e-Quran', 'quran_12_book.js', 'QURAN_12_BOOK', 'Mutalia-e-Quran 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th Mutalia e Quran/JPG']
TABS = ['lesson', 'exercise']
FM_TITLE = ('ابتدائیہ', 'Front matter', 'سریزه')
BACK_TITLE = ('آخری صفحات', 'Last pages', 'وروستي مخونه')
EX_TITLE = ('مشق', 'Exercise', 'تمرین')
DUPLICATE = {}
NOTES = {}
BLANK = {1: 'Scan 1 is an advertisement page (not part of the book).'}


def pdf_jpgs(k):
    return (k - 1,) if 1 <= k <= 231 else None


def route(k, group):
    return None


def sec_kind(sec):
    i = sec['id']
    return 'ex' if 'exercise' in i else ('back' if '-bm-' in i else 'text')


def is_front(ch):
    return ch['number'] == 'FM'
