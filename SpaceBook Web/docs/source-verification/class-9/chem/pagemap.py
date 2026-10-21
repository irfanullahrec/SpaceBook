# -*- coding: utf-8 -*-
"""Canonical scan list of the Class 9 Chemistry book: one entry per printed page, in book order.

pNNN.txt (NNN = index into PAGES) is the transcription of PAGES[NNN]. The source PDFs overlap (each starts on the last
page of the previous one) and chemistry4.pdf holds two copies of printed 153-205, so one scan is chosen per page.
Printed page 129 is not in any source (recorded in class-9/chemistry*-page-*.json).

    python -X utf8 chem/pagemap.py render     renders every page to D:/SpaceBook/_c9render/chem/pNNN.jpg (100 dpi)
"""
import re, sys
from pathlib import Path

PDF = 'D:/SpaceBook/Books/9th/9th Chemistry/pdf/'
OUT = Path('D:/SpaceBook/_c9render/chem')
# (printed page range inclusive, pdf file, pdf page of the first printed page)
RUNS = [
    (1, 47, 'chemistry pdf1.pdf', 6),     # pdf page = printed + 5 for 1; printed 2 has a second scan (pdf page 8) -> see DUP_SKIP
    (48, 99, 'chemistry2.pdf', 1),
    (100, 151, 'chemistry3.pdf', 1),
    (152, 204, 'chemistry4(1).pdf', 1),
    (205, 256, 'chemistry5.pdf', 1),
]
FRONT = [('chemistry pdf1.pdf', n, None) for n in (2, 3, 4, 5)]
BACK = [('chemistry6.pdf', 1, 257), ('chemistry6.pdf', 2, 258), ('chemistry6.pdf', 3, 259), ('chemistry6.pdf', 4, 260),
        ('chemistry6.pdf', 5, 261), ('chemistry6.pdf', 6, 262), ('chemistry6.pdf', 7, None), ('chemistry6.pdf', 8, None)]


def build():
    """Pick one scan per printed page from the per-page audit records (class-9/chemistry*-page-*.json)."""
    import json, glob, os
    base = Path(__file__).resolve().parent.parent
    sets = ['chemistry', 'chemistry2', 'chemistry3', 'chemistry4a', 'chemistry5', 'chemistry6']
    best = {}
    for f in glob.glob(str(base / 'chemistry*-page-*.json')):
        m = re.match(r'(chemistry\w*?)-page-(\d+)', os.path.basename(f))
        if not m or m.group(1) not in sets:
            continue
        d = json.load(open(f, encoding='utf8'))
        pr = d.get('printedPage')
        if pr is None:
            continue
        pdf = os.path.basename(d['sourcePdf'])
        key = (sets.index(m.group(1)), d['pdfPage'])
        dup = 'duplicate' in (d.get('status') or '')
        cur = best.get(pr)
        cand = (dup, key, pdf, d['pdfPage'])
        if cur is None or cand < cur:
            best[pr] = cand
    pages = list(FRONT)
    for pr in range(1, 263):
        if pr in best:
            pages.append((best[pr][2], best[pr][3], pr))
    pages += BACK[6:]
    return pages


PAGES = build()


def render():
    import pymupdf
    OUT.mkdir(parents=True, exist_ok=True)
    docs = {}
    for n, (pdf, pg, printed) in enumerate(PAGES):
        d = docs.setdefault(pdf, pymupdf.open(PDF + pdf))
        pix = d[pg - 1].get_pixmap(dpi=100)
        pix.save(str(OUT / f'p{n:03}.jpg'), jpg_quality=70)
    print(len(PAGES), 'pages rendered to', OUT)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'render':
        render()
    else:
        for n, p in enumerate(PAGES):
            print(n, p)
