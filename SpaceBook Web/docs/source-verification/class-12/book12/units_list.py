# -*- coding: utf-8 -*-
"""Global mode: list the units of the stream:  python -X utf8 units_list.py KEY FROM TO"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.stdout.reconfigure(encoding='utf-8')
import engine


def main():
    b = engine.Book(sys.argv[1])
    a, z = int(sys.argv[2]), int(sys.argv[3])
    secs = b.sections()
    G = {sid for e in b.read_splits().values() for sid in e.get('G', [])}
    by = {s['id']: s for s in secs}
    direct = tuple(getattr(b.cfg, 'GLOBAL_DIRECT', ()))
    units = [u for s in secs if s['pdf'] is not None and s['id'] not in G and not (direct and s['id'].startswith(direct)) for u in b.units_of(s)]
    for i in range(a, min(z, len(units))):
        u = units[i]
        t = b.text_of(by, u) if 'pi' in u else '<' + u['k'] + ' ' + u.get('id', '') + '>'
        print(i, u['sec'].split('-', 1)[-1], u['k'], len(t.split()), t[:int(sys.argv[4]) if len(sys.argv) > 4 else 70])


main()
