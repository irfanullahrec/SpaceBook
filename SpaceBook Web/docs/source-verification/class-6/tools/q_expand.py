"""Expand compact Quran verse lines into the page DSL.

Usage: python tools/q_expand.py SUBJ NNN [NNN ...]   (reads SUBJ/src/pNNN.src, writes SUBJ/pages/pNNN.txt)

In a .src file a line
    v ARABIC || URDU || ENGLISH || PASHTO
becomes the two page lines
    p **ARABIC** || **ARABIC** || **ARABIC**
    p ترجمہ: URDU || ENGLISH || PASHTO
so the Arabic is typed once and placed unchanged in all three slots. Every other line is copied as is.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
subj = sys.argv[1]
for n in sys.argv[2:]:
    src = HERE / subj / 'src' / f'p{int(n):03}.src'
    out = []
    for line in src.read_text(encoding='utf-8').splitlines():
        if line.startswith('v '):
            parts = [p.strip() for p in line[2:].split('||')]
            if len(parts) != 4:
                raise SystemExit(f'{src.name}: verse line needs AR || UR || EN || PS: {line[:80]}')
            ar, ur, en, ps = parts
            out.append(f'p **{ar}** || **{ar}** || **{ar}**')
            out.append(f'p ترجمہ: {ur} || {en} || {ps}')
        else:
            out.append(line)
    (HERE / subj / 'pages' / f'p{int(n):03}.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('wrote', f'p{int(n):03}.txt')
