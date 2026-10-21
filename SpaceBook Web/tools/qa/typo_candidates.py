"""Typo candidates in the English text of the Class 9/10 page books (check 1, automatic part).
    python -X utf8 tools/qa/typo_candidates.py <books.json> <out.tsv>
A word is a candidate when it occurs once in the whole Class 9/10 corpus AND is not in the Word/OCR text of the same subject
(D:/SpaceBook/Books/<class>/<subject>/word/*.docx) AND is not in the lexicon of curated English words. The list is for a human reading the scan.
"""
import json, re, sys, zipfile, glob, collections
from pathlib import Path
books = json.load(open(sys.argv[1], encoding='utf8'))
DOCS = {'c9/bio': '9th Biology', 'c9/chem': '9th Chemistry', 'c9/sci': '9th General Science', 'c9/comp': '9th Computer Science', 'c9/eng': '9th English',
        'c9/hpe': '9th  HPE', 'c9/drawing': '9th Drawing', 'c9/math': '9th MTHA', 'c10/phys': '10th physics', 'c10/chem': '10th Chemistry',
        'c10/sci': '10th General Science', 'c10/comp': '10th CS', 'c10/math': '10th Maths', 'c10/drawing': '10th  Drawing', 'c10/hpe': '10th HPE'}
def docwords(folder):
    out = set()
    for f in glob.glob(f'D:/SpaceBook/Books/{folder.split()[0]}/{folder}/word/*.docx'):
        try:
            x = zipfile.ZipFile(f).read('word/document.xml').decode('utf8', 'ignore')
        except Exception:
            continue
        out.update(w.lower() for w in re.findall(r"[A-Za-z]{4,}", re.sub(r'<[^>]+>', ' ', x)))
    return out
def strs(o, f, ctx):
    if isinstance(o, str): return
    if isinstance(o, list):
        for x in o: strs(x, f, ctx)
    elif isinstance(o, dict):
        if o.get('t') == 'page': ctx['pdf'] = o.get('pdf')
        for k in ('en', 'text'):
            if isinstance(o.get(k), str) and o.get('t') not in ('m', 'eq', 'svg'): f(o[k], ctx['pdf'])
        for v in o.values():
            if isinstance(v, (list, dict)): strs(v, f, ctx)
freq = collections.Counter(); where = {}
for cls in ('c9', 'c10'):
    for sub, bk in books[cls].items():
        key = f'{cls}/{sub}'
        ctx = {'pdf': 0}
        def add(t, pdf):
            t = re.sub(r'\$[^$]*\$', ' ', t)
            for w in re.findall(r"[A-Za-z]{5,}", t):
                lw = w.lower(); freq[lw] += 1
                where.setdefault(lw, (key, pdf, w))
        strs(bk['units'], add, ctx)
lex = set()
for f in glob.glob(str(Path(__file__).resolve().parents[2] / 'docs' / 'lexicon' / 'curated' / '*.txt')):
    for l in open(f, encoding='utf8'): lex.add(l.split('|')[0].strip().lower())
out = []
cache = {}
for w, c in freq.items():
    if c != 1 or w in lex: continue
    key, pdf, orig = where[w]
    if key not in DOCS: continue
    if key not in cache: cache[key] = docwords(DOCS[key])
    if not cache[key] or w in cache[key]: continue
    if orig.isupper() or re.search(r'(.)\1\1', w): pass
    out.append((key, pdf, orig))
out.sort()
open(sys.argv[2], 'w', encoding='utf8').write('\n'.join(f'{k}\t{p}\t{w}' for k, p, w in out))
print(len(out), collections.Counter(k for k, _, _ in out).most_common())
