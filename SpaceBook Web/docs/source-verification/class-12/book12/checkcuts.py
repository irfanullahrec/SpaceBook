# -*- coding: utf-8 -*-
"""Which confirmed splits cannot be placed?  python -X utf8 checkcuts.py KEY"""
import json, sys
sys.path.insert(0, '.')
import engine
b = engine.Book(sys.argv[1])
spec = b.read_splits()
cands = json.loads((b.dir / 'candidates.json').read_text(encoding='utf-8'))
by_id = {s['id']: s for s in b.sections()}
bad = []
for k, jp, pp, units in b.two_page_scans():
    sp = spec.get(k)
    if not sp or sp.get('mode') is None:
        continue
    try:
        b.find_cut(units, by_id, sp, cands.get(str(k), {}))
    except SystemExit as e:
        bad.append((k, str(e)[:110]))
for x in bad:
    print(*x)
print(len(bad), 'unplaceable')
