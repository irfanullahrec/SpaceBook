# -*- coding: utf-8 -*-
"""Class 12 Health & Physical Education (KPTBB, Urdu medium): one reviewed scan per printed page.
JPG j = PDF page j+1 (JPG 000 = front cover, 001 = advertisement); printed pages come from the reviewed data's labels
(offset 5 up to p.107, then 4 and 3: printed pages 107 and 148 are missing from the scans)."""
from pathlib import Path
KEY = 'hpe'
DATA_FILE, GLOBAL = 'hpe_12_data.js', 'HPE_12_DATA'
BANK_FILES, BANK_KEY = 'hpe12_exercise_banks.js', 'hpe'
JPG = Path('D:/SpaceBook/Books/12th/12th HPE/JPG')
TOTAL_JPG = 157
LANGS = ['ur', 'en', 'ps']
ORIG = 'urdu'
BOOK_NAME = ('Health & Physical Education', 'hpe_12_book.js', 'HPE_12_BOOK', 'Health & Physical Education 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th HPE/JPG']
TABS = ['lesson', 'exercise']
FM_TITLE = ('ابتدائیہ', 'Front matter', 'سریزه')
BACK_TITLE = ('آخری صفحات', 'Last pages', 'وروستي مخونه')
EX_TITLE = ('مشق', 'Exercise', 'تمرین')
DUPLICATE = {}
NOTES = {}
BLANK = {1: 'Scan 1 is an advertisement page (not part of the book).'}


def pdf_jpgs(k):
    return (k - 1,) if 1 <= k <= 157 else None


def route(k, group):
    return None


def sec_kind(sec):
    return 'ex' if 'exercise' in sec['id'] else 'text'


def is_front(ch):
    return ch['number'] == 'FM'

# HPE numbers its questions "i In baseball..." (no dot) and prints the choices as a paragraph of their own
QNO = r'^\s*\(?(\d{1,2}|[ivxlc]{1,5})(?:\s*[.۔)]|\s+(?=[^\s\d]))'
