"""Expand compact glossary pages into the page DSL.

Usage: python tools/gloss_expand.py SUBJ NNN [NNN ...]   (reads SUBJ/src/pNNN.gls, writes SUBJ/pages/pNNN.txt)

A .gls file is ordinary page DSL, except that a line
    g ARABIC = URDU = ENGLISH = PASHTO
becomes a table row with the Arabic word (unchanged, bold) and its Urdu meaning as printed,
plus English and Pashto renderings. Consecutive g-lines are wrapped in one table.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
subj = sys.argv[1]
HEAD = 'th الفاظ || Word || لغت | معانی || Meaning || مانا'
for n in sys.argv[2:]:
    src = HERE / subj / 'src' / f'p{int(n):03}.gls'
    out, intable = [], False
    for line in src.read_text(encoding='utf-8').splitlines():
        if line.startswith('g '):
            parts = [p.strip() for p in line[2:].split(' = ')]
            if len(parts) != 4:
                raise SystemExit(f'{src.name}: glossary line needs AR = UR = EN = PS: {line[:80]}')
            ar, ur, en, ps = parts
            if not intable:
                out += ['table', HEAD]
                intable = True
            out.append(f'tr **{ar}** || **{ar}** || **{ar}** | {ur} || {en} || {ps}')
        else:
            if intable:
                out.append('endtable')
                intable = False
            out.append(line)
    if intable:
        out.append('endtable')
    (HERE / subj / 'pages' / f'p{int(n):03}.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('wrote', f'p{int(n):03}.txt')
