# -*- coding: utf-8 -*-
"""python -X utf8 chem/show.py N [M]   prints the generated body lines (English part) of pages N..M with line numbers"""
import sys, re
from pathlib import Path
import pagemap
HERE = Path(__file__).resolve().parent
a = int(sys.argv[1]); b = int(sys.argv[2]) if len(sys.argv) > 2 else a
for n in range(a, b + 1):
    t = (HERE / 'pages' / f'p{n:03}.txt').read_text(encoding='utf8').splitlines()
    print(f'===== p{n:03}  printed {pagemap.PAGES[n][2]}  {pagemap.PAGES[n][0]} pdf p{pagemap.PAGES[n][1]}')
    k = 0
    for l in t:
        if l.startswith('@'):
            print('      ' + l[:100]); continue
        k += 1
        print(f'{k:3} ' + l.split(' || ')[0][:130])
