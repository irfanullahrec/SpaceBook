# -*- coding: utf-8 -*-
"""Compact authoring for Class 9 Physics Units 8-9 page records.

A page module pNNN.py defines:
  TITLE   str
  SECTIONS list of (code, (heading_en, heading_ur, heading_ps), items[, continues])
  EXTRA   optional dict merged into the page (objectives, definitions, numericals,
          activities, textbookExercise, chapterEnd ...)
  NOTE    review note (comparison text)

items:
  ('h', en, ur, ps)            sub-heading
  ('p', en, ur, ps)            paragraph
  ('q', en, ur, ps)            boxed definition / quotation
  ('ul', [(en,ur,ps), ...])     list
  ('eq', id, expr[, num[, ratio]])   equation; expr uses [[num|den]] for fractions
  ('fig', en, ur, ps)          figure caption (printed caption text; drawing not reproduced)
  ('tab', id, title, headers, rows, (ur_headers, ur_rows), (ps_headers, ps_rows))
"""
import json, re, importlib, sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
SOURCE = r'D:\SpaceBook\Books\9th\9th physics\pdf\9thphysics.pdf'
CHAPTERS = {8: 'Unit 8: Thermal Properties of Matter', 9: 'Unit 9: Transfer of Heat'}
CW = 13.6  # approx glyph width at font-size 25


SUBRE = re.compile(r'_(\{[^}]*\}|[A-Za-z0-9]+)')
SUPRE = re.compile(r'\^(\{[^}]*\}|[\-0-9]+)')


def _w(t):
    t = re.sub(r'&[a-z]+;', 'x', t)
    main = SUBRE.sub('', SUPRE.sub('', t))
    small = ''.join(m.strip('{}') for m in SUBRE.findall(t) + SUPRE.findall(t))
    return max(1, len(main) * CW + len(small) * CW * 0.68)


def _rich(t):
    t = escape(t, quote=False)
    t = SUBRE.sub(lambda m: f'<tspan baseline-shift="sub" font-size="17">{m.group(1).strip("{}")}</tspan>', t)
    return SUPRE.sub(lambda m: f'<tspan baseline-shift="super" font-size="17">{m.group(1).strip("{}")}</tspan>', t)


def _txt(t, x, y, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x:.1f}" y="{y}"{a}>{_rich(t)}</text>'


SUBMAP = dict(zip('0123456789+-=()aeoxhklmnpstiruvAEOXHKLMNPSTIRUVCFcfgdb', '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₕₖₗₘₙₚₛₜᵢᵣᵤᵥₐₑₒₓₕₖₗₘₙₚₛₜᵢᵣᵤᵥcfcfgdb'))
SUPMAP = dict(zip('0123456789+-=()n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ'))


def uni(t):
    """Prose: turn _x / _{xy} / ^{-1} into Unicode sub/superscripts where possible."""
    def sub(m):
        v = m.group(1).strip('{}')
        return ''.join(SUBMAP.get(c, c) for c in v) if all(c in SUBMAP for c in v) else '_' + m.group(1)
    def sup(m):
        v = m.group(1).strip('{}')
        return ''.join(SUPMAP.get(c, c) for c in v) if all(c in SUPMAP for c in v) else '^' + m.group(1)
    return SUPRE.sub(sup, SUBRE.sub(sub, t))


def plain(expr):
    e = re.sub(r'\[\[(.*?)\|(.*?)\]\]', r'()/()', expr)
    e = SUBRE.sub(lambda m: m.group(1).strip('{}'), e)
    return SUPRE.sub(lambda m: '^' + m.group(1).strip('{}'), e)


def eq_svg(expr, num=None, label='Textbook equation'):
    """Single-line equation; [[a|b]] renders as a stacked fraction."""
    parts = re.split(r'(\[\[.*?\]\])', expr)
    x, body, frac = 5.0, '', False
    for part in parts:
        if not part:
            continue
        m = re.fullmatch(r'\[\[(.*?)\|(.*?)\]\]', part)
        if m:
            frac = True
            n, d = m.group(1), m.group(2)
            w = max(_w(n), _w(d)) + 10
            body += _txt(n, x + w / 2, 34, 'middle') + _txt(d, x + w / 2, 92, 'middle')
            body += f'<path d="M{x:.1f} 54h{w:.1f}" stroke="currentColor" stroke-width="2"/>'
            x += w + 6
        else:
            body += _txt(part, x, 64 if frac or '[[' in expr else 45)
            x += _w(part)
    h = 110 if '[[' in expr else 70
    if '[[' not in expr:
        body = body.replace(' y="64"', ' y="45"')
    if num:
        x += 30
        body += f'<rect x="{x:.1f}" y="{h/2-20:.1f}" width="72" height="40" rx="4" fill="#3e899d"/>'
        body += f'<text x="{x+36:.1f}" y="{h/2+9:.1f}" text-anchor="middle" fill="#fff">{escape(num)}</text>'
        x += 72
    w = int(x + 10)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, quote=True)}">'
            f'<g font-family="sans-serif" font-size="25" fill="currentColor">{body}</g></svg>'), w


# Textbook answer key, printed page 254 (PDF 259)
ANSWER_KEY = {'Assignment 8.1': '−23 °C', 'Assignment 8.2': '2.3 × 10⁻⁵ °C⁻¹', 'Assignment 8.3': '0.522 cm³', 'Assignment 8.4': '262 Liter',
              'Assignment 8.5': '235.2 J/kg K', 'Assignment 8.6': '7.1 × 10⁶ J', 'Assignment 9.1': '2.6 × 10⁶ J'}


def build(n):
    m = importlib.import_module(f'p{n:03d}')
    ch = 8 if n <= 237 else 9
    sections = []
    for spec in m.SECTIONS:
        code, (he, hu, hp), items = spec[:3]
        cont = len(spec) > 3 and spec[3]
        paras, layout, blocks = [], [], []
        def add(en, ur, ps):
            paras.append(dict(text=uni(en), urdu=uni(ur), pashto=uni(ps)))
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
                idx = [add(*row) for row in it[1]]
                layout.append(dict(type='numberedList', indices=idx))
            elif k == 'eq':
                bid, expr = it[1], it[2]
                num = it[3] if len(it) > 3 else None
                svg, w = eq_svg(expr, num, f'Equation {num}: {plain(expr)}' if num else f'Equation: {plain(expr)}')
                ratio = it[4] if len(it) > 4 else round(min(0.98, max(0.2, w / 850)), 2)
                blocks.append(dict(type='formula', id=bid, svg=svg, svgUrdu=svg, svgPashto=svg,
                                   sourceWidthRatio=ratio, plain=uni(expr).replace('[[', '(').replace('|', ')/(').replace(']]', ')')))
                layout.append(dict(type='visual', blockId=bid))
            elif k == 'tab':
                _, tid, title, headers, rows, urt, pst = it
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
    page = dict(id=f'cls9-physics-page-{n:03d}', pdfPage=n, printedPage=n - 5, status='corrected-fresh-review',
                chapterNumber=ch, chapter=CHAPTERS[ch], title=m.TITLE, sourcePdf=SOURCE, sections=sections,
                comparison=getattr(m, 'NOTE', 'Full-text rebuild from the rendered PDF page (2026-10-12): every printed paragraph, heading, definition, equation, table and caption transcribed in order with paired Urdu and Pashto translations; figure drawings are represented by their printed captions.'),
                pageMetrics=dict(visualInspection='rendered PDF page at 110 dpi', textLayer='none', rebuild='class9-physics-u8u9-fulltext-2026-10-12'))
    for k, v in getattr(m, 'EXTRA', {}).items():
        for item in (v if isinstance(v, list) else []):
            if isinstance(item, dict):
                item.setdefault('sourcePdfPage', n)
                item.setdefault('sourcePrintedPage', n - 5)
        if k == 'activities':
            for item in v:
                if item.get('num') in ANSWER_KEY:
                    item['answer'] = ANSWER_KEY[item['num']]
                    item['answerSource'] = 'Textbook answer key, printed page 254 (PDF page 259)'
        if k == 'textbookExercise':
            for lst in v.values():
                for item in lst:
                    item.setdefault('sourcePdfPage', n)
                    item.setdefault('sourcePrintedPage', n - 5)
        page[k] = v
    for sec in sections:
        for p in sec['paras']:
            assert p['text'] and p['urdu'] and p['pashto'], (n, sec['code'], p)
    (OUT / f'physics-page-{n:03d}.json').write_text(json.dumps(page, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return page


if __name__ == '__main__':
    sys.path.insert(0, str(HERE))
    for a in sys.argv[1:]:
        p = build(int(a))
        print(a, 'sections', [s['code'] for s in p['sections']], 'paras', sum(len(s['paras']) for s in p['sections']))
