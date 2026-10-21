# -*- coding: utf-8 -*-
"""Printed-page text of the Class 9 Chemistry Word OCR dumps (footer 'Chemistry Grade IX' + page number ends a page).

    python -X utf8 chem/docxpages.py    prints how many pages each file splits into
"""
import re, zipfile
from pathlib import Path

WORD = Path('D:/SpaceBook/Books/9th/9th Chemistry/word')
FILES = ['chemistry pdf1.docx', 'chemistry2.docx', 'chemistry3.docx', 'chemistry5.docx', 'chemistry6.docx']


def lines_of(f):
    x = zipfile.ZipFile(WORD / f).read('word/document.xml').decode('utf8')
    out = []
    for p in re.findall(r'<w:p[ >].*?</w:p>', x, flags=re.S):
        t = ''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, flags=re.S))
        out.append(t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').strip())
    return out


def split(f):
    """-> {printed: text}"""
    L = lines_of(f)
    pages, buf, last = {}, [], 0
    i = 0
    while i < len(L):
        line = L[i]
        m = re.match(r'^(?:Chemistry|Chemistr)\s+Grade\s+\S+\s*(\d{1,3})?$', line)
        if m:
            n = m.group(1)
            if n is None and i + 1 < len(L) and re.fullmatch(r'\d{1,3}', L[i + 1]):
                n = L[i + 1]
                i += 1
            if n is not None:
                n = int(n)
                if last < n <= last + 3 or last == 0:
                    pages[n] = ' '.join(buf)
                    buf, last = [], n
                    i += 1
                    continue
        buf.append(line)
        i += 1
    return pages


if __name__ == '__main__':
    for f in FILES:
        p = split(f)
        print(f, len(p), sorted(p)[:3], sorted(p)[-3:])
