# -*- coding: utf-8 -*-
"""Class 12 Pakistan Studies (KPTBB, Urdu medium): where each printed page is on the scans.

JPG folder: D:/SpaceBook/Books/12th/12th Pak Studies/JPG  (000 = front cover, 001 = imprint, 002 = contents, 003.. = book pages)
  JPG n = printed page n-2 up to JPG 58 (p.56); JPG 59/60 repeat 57/58 (p.55-56); JPG 61.. = printed n-4.
  The tail (JPG 211..) was photographed twice in places; the first clear copy is kept, the other scans are `duplicate`.
PDF k (the 117-page scan PDF the earlier review used) = JPG 2*(k-4)+1 and +2 up to PDF 108; PDF 109..117 are single pages.
"""
import re
from pathlib import Path

KEY = 'pakstudy'
DATA_FILE, GLOBAL = 'pakstudy_12_data.js', 'PAKSTUDY_12_DATA'
BANK_FILES, BANK_KEY = 'pakstudy12_exercise_banks.js', 'pakstudy'
JPG = Path('D:/SpaceBook/Books/12th/12th Pak Studies/JPG')
TOTAL_JPG = 229
LANGS = ['ur', 'en', 'ps']            # slot order of "original || translation || translation"
ORIG = 'urdu'                          # field of the original text (cut and compared)
BOOK_NAME = ('Pakistan Studies', 'pakstudy_12_book.js', 'PAKSTUDY_12_BOOK', 'Mutalia-e-Pakistan 12 (KPTBB, Urdu medium)')
BOOK_SOURCE = ['12th Pak Studies/JPG']
TABS = ['lesson', 'exercise']
OCR_DOCX = ['D:/SpaceBook/Books/12th/12th Pak Studies/Word/000_and_228_more_part_0%d_of_03.docx' % i for i in (1, 2, 3)]
OCR_START = 'باب اول'
FM_TITLE = ('ابتدائیہ', 'Front matter', 'پېژندنه')
BACK_TITLE = ('آخری صفحات', 'Last pages', 'وروستي مخونه')
EX_TITLE = ('مشق', 'Exercise', 'تمرین')


def printed_of(jpg):
    if 3 <= jpg <= 58:
        return jpg - 2
    if 61 <= jpg <= 211:
        return jpg - 4
    return {214: 208, 215: 209, 220: 210, 221: 211, 222: 212}.get(jpg)


# duplicate scan -> the JPG it repeats
DUPLICATE = {59: 57, 60: 58, 212: 210, 213: 211, 216: 214, 217: 215, 218: 220, 219: 221, 224: 222, 225: 223, 228: 227}
NOTES = {228: 'Scan 228 is the left half of the back cover on scan 227 (national anthem).'}


def pdf_jpgs(k):
    """The JPG pages scan k of the reviewed data holds (right-hand page first)."""
    if 4 <= k <= 108:
        j = 2 * (k - 4) + 1
        return None if j in (59, 60) else (j, j + 1)
    return {109: (211,), 110: (214,), 111: (215,), 112: (220,), 113: (221,), 114: (222,), 115: (223,), 116: (226,), 117: (227,)}.get(k)


def route(k, group):
    """Scans that are not ordinary text pages: {jpg: predicate(section) or None for all}.  None = ordinary."""
    if k in (1, 3):
        return {0: None}
    if k == 4:
        return {1: lambda s: s['id'].endswith('imprint'), 2: lambda s: s['id'].endswith('contents')}
    if k >= 115:
        return {pdf_jpgs(k)[0]: None}
    return None


def sec_kind(sec):
    i = sec['id']
    return 'ex' if 'exercise' in i else ('back' if '-bm-' in i or 'back-cover' in i else 'text')


def is_front(ch):
    return ch['number'] == 'FM'


def cover_jpgs():
    return {0, 1, 2}
