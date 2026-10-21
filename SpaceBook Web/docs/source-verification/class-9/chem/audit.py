# -*- coding: utf-8 -*-
"""python -X utf8 chem/audit.py [limit]   pages whose generated English text and the page's OCR / Word text disagree.

Both texts are reduced to letters and digits; 10-character samples of one are looked up in the other.
prec = share of the generated page's samples found in the OCR text (low = content that belongs on another page)
rec  = share of the OCR text's samples found in the generated page   (low = content missing from the page)"""
import re, sys
from pathlib import Path
import gen, pagemap

HERE = Path(__file__).resolve().parent
K = 10


def samples(s):
    return [s[i:i + K] for i in range(0, max(0, len(s) - K), 5)]


def gen_text(i):
    t = (HERE / 'pages' / f'p{i:03}.txt').read_text(encoding='utf8').splitlines()
    en = []
    for l in t:
        if l.startswith(('@', '<svg', 'ss ', 'qsolution', 'solution', 'endsolution', 'svg', 'endsvg', 'endtable', 'endbox')):
            continue
        l = re.sub(r'^(p|th|tr|q|qp|slo|table|box \w+|#+|-|m)\s*\|?', ' ', l)
        en.append(l.split(' || ')[0])
    return gen.norm(' '.join(en))


def run(limit=0.5):
    out = []
    for i in range(len(pagemap.PAGES)):
        O = gen.TEXT.get(i)
        if not O:
            continue
        G = gen_text(i)
        if len(G) < 40:
            out.append((i, pagemap.PAGES[i][2], None, 0.0, len(G))); continue
        sg, so = samples(G), samples(O)
        prec = sum(1 for x in sg if x in O) / max(1, len(sg))
        rec = sum(1 for x in so if x in G) / max(1, len(so))
        out.append((i, pagemap.PAGES[i][2], round(prec, 2), round(rec, 2), len(G)))
    return out


if __name__ == '__main__':
    lim = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    rows = run(lim)
    print('LOW RECALL (content missing):', [(r[0], r[1], r[3]) for r in rows if r[3] < lim])
    print('LOW PRECISION (extra / misplaced):', [(r[0], r[1], r[2]) for r in rows if r[2] is not None and r[2] < lim])
