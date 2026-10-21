"""Write curated rows that supply ONLY the language columns a word still lacks (so a word that already has a row in
another file is completed, not duplicated).

    python fill_partial.py MISSING.json OUT.txt TRANSLATIONS.txt

MISSING.json   from `node tools/offline_meanings/missing_cls15.js --json` : [[word, freq, "ur,ps,ar"], ...]
TRANSLATIONS   lines  word|urdu|pashto|arabic  (all three written by hand)
OUT.txt        docs/lexicon/curated/cNNN.txt : word|urdu-if-missing|pashto-if-missing|arabic-if-missing
"""
import json, sys
miss = {w: need.split(',') for w, f, need in json.load(open(sys.argv[1], encoding='utf8'))}
rows, used = [], 0
for line in open(sys.argv[3], encoding='utf8').read().split('\n'):
    p = line.split('|')
    if len(p) != 4 or p[0] not in miss:
        continue
    need = miss[p[0]]
    cols = [p[1] if 'ur' in need else '', p[2] if 'ps' in need else '', p[3] if 'ar' in need else '']
    rows.append('|'.join([p[0]] + cols))
    used += 1
open(sys.argv[2], 'w', encoding='utf8', newline='\n').write('\n'.join(rows) + '\n')
print('rows written', used)
