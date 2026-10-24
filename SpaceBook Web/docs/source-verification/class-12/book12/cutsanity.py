# -*- coding: utf-8 -*-
"""Compare every confirmed cut with the ink share of the two scans: python -X utf8 cutsanity.py KEY [limit]"""
import json, sys, bisect
sys.path.insert(0, '.')
import engine
b = engine.Book(sys.argv[1])
lim = float(sys.argv[2]) if len(sys.argv) > 2 else 0.18
spec = b.read_splits()
cands = json.loads((b.dir / 'candidates.json').read_text(encoding='utf-8'))
by_id = {s['id']: s for s in b.sections()}
for k, jp, pp, units in b.two_page_scans():
    sp = spec.get(k)
    if not sp or sp.get('mode') is None:
        continue
    cu, cw = b.find_cut(units, by_id, sp, cands.get(str(k), {}))
    total = sum(len(engine.norm(w)) for u in units for w in b.text_of(by_id, u).split())
    pos = 0
    for ui, u in enumerate(units):
        ws = b.text_of(by_id, u).split()
        if ui == cu:
            pos += sum(len(engine.norm(w)) for w in ws[:cw]); break
        pos += sum(len(engine.norm(w)) for w in ws)
    frac = pos / max(total, 1)
    ia, ib = b.ink(jp[0]), b.ink(jp[1])
    ink = ia / max(ia + ib, 1)
    flag = '  <-- CHECK' if abs(frac - ink) > lim else ''
    if flag:
        print(f'PDF {k} pages {pp}: cut at {frac:.2f} of the text, ink share {ink:.2f}{flag}')
