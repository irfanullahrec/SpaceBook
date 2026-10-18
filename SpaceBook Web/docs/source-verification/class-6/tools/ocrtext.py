"""Print cached OCR text of scan pages in reading order: ocrtext.py SUBJ idx [idx...]"""
import json, sys
from pathlib import Path
H = Path(__file__).resolve().parents[1]
subj = sys.argv[1]
for a in sys.argv[2:]:
    f = H / subj / 'ocr' / f'{int(a):03}.json'
    if not f.exists():
        print(f'== {a}: no OCR yet'); continue
    lines = json.loads(f.read_text(encoding='utf-8'))['lines']
    rows = []
    for l in lines:
        ys = [p[1] for p in l['box']]; xs = [p[0] for p in l['box']]
        rows.append((min(ys), max(ys), min(xs), l['text'], l['conf']))
    rows.sort(key=lambda r: (r[0], r[2]))
    out, cur, last = [], [], None
    for r in rows:
        if last is not None and r[0] > last + (r[1] - r[0]) * 0.6:
            out.append(cur); cur = []
        cur.append(r); last = r[0] if not cur[:-1] else last
        if len(cur) == 1: last = r[0]
    if cur: out.append(cur)
    print(f'== {a}')
    for c in out:
        print('  '.join(x[3] + ('?' if x[4] < 0.8 else '') for x in sorted(c, key=lambda r: r[2])))
