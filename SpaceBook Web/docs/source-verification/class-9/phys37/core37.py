# -*- coding: utf-8 -*-
"""Full-text rebuild of Class 9 Physics Units 3-7 (PDF 65-201).
A page module pNNN.py defines TITLE and SECTIONS in the phys89 item format
(('h'|'p'|'q', en, ur, ps), ('ul', [...]), ('eq', id|None, expr[, num]), ('fig', en, ur, ps),
('tab', id, title, headers, rows, (ur_h, ur_rows), (ps_h, ps_rows))). Only the page's
sections/title/status/comparison/pageMetrics are replaced; every other key of the existing
record (exercise data, extras) is kept. Usage: python core37.py 65 66 ..."""
import json, sys, importlib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'phys89'))
sys.path.insert(0, str(HERE))
import core as C

OUT = HERE.parent


def build(n):
    m = importlib.import_module(f'p{n:03d}')
    rec = json.loads((OUT / f'physics-page-{n:03d}.json').read_text(encoding='utf-8'))
    sections = []
    eqn = 0
    for spec in m.SECTIONS:
        code, (he, hu, hp), items = spec[:3]
        cont = len(spec) > 3 and spec[3]
        paras, layout, blocks = [], [], []
        def add(en, ur, ps):
            paras.append(dict(text=C.uni(en), urdu=C.uni(ur), pashto=C.uni(ps)))
            return len(paras) - 1
        for it in items:
            k = it[0]
            if k in ('h', 'p', 'q'):
                i = add(*it[1:4])
                layout.append(dict(type={'h': 'heading', 'p': 'paragraph', 'q': 'quotation'}[k], indices=[i]))
            elif k == 'fig':
                i = add(*it[1:4])
                layout.append(dict(type='paragraph', indices=[i], role='figureCaption'))
            elif k == 'ul':
                layout.append(dict(type='numberedList', indices=[add(*row) for row in it[1]]))
            elif k == 'eq':
                eqn += 1
                bid = it[1] or f'phys9-p{n:03d}-eq{eqn}'
                expr = it[2]
                num = it[3] if len(it) > 3 else None
                svg, w = C.eq_svg(expr, num, f'Equation {num}: {C.plain(expr)}' if num else f'Equation: {C.plain(expr)}')
                blocks.append(dict(type='formula', id=bid, svg=svg, svgUrdu=svg, svgPashto=svg,
                                   sourceWidthRatio=round(min(0.98, max(0.2, w / 850)), 2),
                                   plain=C.uni(expr).replace('[[', '(').replace('|', ')/(').replace(']]', ')')))
                layout.append(dict(type='visual', blockId=bid))
            elif k == 'tab':
                _, tid, title, headers, rows, urt, pst = it
                tid = tid or f'phys9-p{n:03d}-tab{len(blocks)+1}'
                blocks.append(dict(type='sourceTable', id=tid, title=title, headers=headers, rows=rows,
                                   translations=[dict(language='اردو', headers=urt[0], rows=urt[1]),
                                                 dict(language='پښتو', headers=pst[0], rows=pst[1])]))
                layout.append(dict(type='sourceDataTable', tableId=tid))
            else:
                raise ValueError(k)
        sec = dict(code=code, heading=he, headingUrdu=hu, headingPashto=hp, paras=paras, blocks=blocks, sourceLayout=layout)
        if cont:
            sec['continuesPreviousParagraph'] = True
        sections.append(sec)
    for sec in sections:
        for p in sec['paras']:
            assert p['text'] and p['urdu'] and p['pashto'], (n, sec['code'], p)
    rec['sections'] = sections
    rec['title'] = m.TITLE
    rec['status'] = 'corrected-fresh-review'
    rec['comparison'] = getattr(m, 'NOTE', 'Full-text rebuild from the rendered PDF page (2026-10-13): every printed paragraph, heading, definition, equation, table and caption transcribed in order with paired Urdu and Pashto translations; figure drawings are represented by their printed captions.')
    rec['pageMetrics'] = dict(visualInspection='rendered PDF page at 110 dpi', textLayer='none', rebuild='class9-physics-u3u7-fulltext-2026-10-13')
    (OUT / f'physics-page-{n:03d}.json').write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return rec


if __name__ == '__main__':
    for a in sys.argv[1:]:
        p = build(int(a))
        print(a, [s['code'] for s in p['sections']], sum(len(s['paras']) for s in p['sections']))
