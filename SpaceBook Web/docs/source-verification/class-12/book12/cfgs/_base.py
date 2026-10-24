# -*- coding: utf-8 -*-
"""Defaults shared by the page-book configs of Class 12 (cfgs/KEY.py: from cfgs._base import *).

A config names the book (KEY, DATA_FILE, GLOBAL, BANK_*, JPG, TOTAL_JPG, LANGS, ORIG, BOOK_NAME, BOOK_SOURCE, TABS) and says where the printed
pages are: OFFSETS = [(first_jpg, last_jpg, offset)] with printed = jpg - offset (read from the scans' footers: engine.py KEY footers /
segments), DUPLICATE = {jpg: jpg it repeats}, NO_PAGE = jpgs without a printed page (ads, covers), EXTRA_PDF = {pdf scan: (jpgs)} for the
scans that carry no printed number (cover, imprint, contents), route() to send front-matter sections to their own JPG."""
import re

FM_TITLE = ('ابتدائیہ', 'Front matter', 'سریزه')
BACK_TITLE = ('آخری صفحات', 'Last pages', 'وروستي مخونه')
EX_TITLE = ('مشق', 'Exercise', 'تمرین')
DUPLICATE = {}
NOTES = {}
BLANK = {}
NO_PAGE = ()
TABS = ['lesson', 'exercise']


def sec_kind(sec):
    i = sec['id']
    if re.search(r'exercise|-ex-|-ex\d|questions?$|review', i):
        return 'ex'
    if re.search(r'-bm-|back-cover|glossary|appendix|about-author', i):
        return 'back'
    return 'text'


def is_front(ch):
    return str(ch['number']) == 'FM'
