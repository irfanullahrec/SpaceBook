# -*- coding: utf-8 -*-
"""Compare the automatic cut candidates with the confirmed cuts: python -X utf8 cutcmp.py KEY"""
import json, sys
sys.path.insert(0, '.')
import engine
b = engine.Book(sys.argv[1])
spec = b.read_splits()
cands = json.loads((b.dir / 'candidates.json').read_text(encoding='utf-8'))
by_id = {s['id']: s for s in b.sections()}
stat = {}
for k, jp, pp, units in b.two_page_scans():
    sp = spec.get(k)
    c = cands.get(str(k))
    if not sp or not c or sp.get('mode') in (None, 'ok', 'para', 'ink') or False:
        continue
    try:
        cu, cw = b.find_cut(units, by_id, sp, c)
    except SystemExit:
        continue
    def off(ui, wi):
        pos = 0
        for i, u in enumerate(units):
            ws = b.text_of(by_id, u).split()
            if i == ui:
                return pos + sum(len(engine.norm(w)) for w in ws[:wi])
            pos += sum(len(engine.norm(w)) for w in ws)
        return pos
    man = off(cu, cw)
    for lab in ('ca', 'cb'):
        o = (c.get('opts') or {}).get(lab)
        if not o:
            continue
        d = abs(man - off(o['unit'], o['word']))
        stat.setdefault(lab, []).append(d)

for k, v in stat.items():
    print(k, 'n', len(v), 'exact(<=12 chars)', sum(1 for x in v if x <= 12))
