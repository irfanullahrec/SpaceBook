# -*- coding: utf-8 -*-
"""List the unit sequence of a two-page scan (headings / paragraphs / tables with their rows) to place a cut:
    python -X utf8 tbl.py KEY PDF [PDF ...]"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import engine


def main():
    b = engine.Book(sys.argv[1])
    secs = [s for s in b.sections()]
    by_id = {s['id']: s for s in secs}
    by_pdf = b.by_pdf()
    for k in (int(x) for x in sys.argv[2:]):
        print(f'=== PDF {k}')
        group = by_pdf.get(k, [])
        jp, pp = b.scan_pages(k)
        stream = b.scan_streams(group, pp)[1] if pp else group
        for s in stream:
            for u in b.units_of(s):
                if 'pi' in u:
                    p = s['paras'][u['pi']]
                    print(f"  [{u['k']}{u['o']:>3}] {(p.get(b.cfg.ORIG) or '')[:90]}")
                elif u['k'] == 't':
                    tb = next(x for x in s['blocks'] if x['id'] == u['id'])
                    print(f"  [t{u['o']:>3}] TABLE {u['id']}: {len(tb['rows'])} rows; " + ' | '.join(' / '.join(str(c)[:14] for c in r[:3]) for r in tb['rows'][:12]))
                else:
                    print(f"  [{u['k']}{u['o']:>3}] {u['id']}")


main()
