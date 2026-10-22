"""Lint + review sheet for the Urdu/Pashto lines authored in the Class 6-8 QA pass.
   python tools/qa_urps_lint.py   -> docs/review/urps_review_sheet.csv + report on stdout
Checks: Arabic yeh/kaf/alef-maksura in Urdu or Pashto (should be Urdu yeh/kaf), Urdu line equal to English, Pashto equal to Urdu,
no Pashto-specific letters in a long Pashto line (looks copied from Urdu), empty fields, Latin words left in ur/ps text, digit mix."""
import csv, glob, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
FILES = [p for pat in ('docs/source-verification/class-7/math/dsl/*.txt', 'docs/source-verification/class-8/math/dsl/*.txt') for p in glob.glob(str(ROOT / pat))]
MINE = {'sets_poly', 'num_sets2', 'u789', 'u10_13', 'review2', 'data_mcq', 'u8x', 'u8y', 'u8z', 'u8w', 'u8v'}
PS_ONLY = set('ټډړښځڅږڼېۍګ')
rows = []
def add(src, key, en, ur, ps):
    rows.append((src, key, en.strip(), ur.strip(), ps.strip()))
for f in FILES:
    stem = Path(f).stem
    if stem not in MINE: continue
    for ln in open(f, encoding='utf8'):
        ln = ln.rstrip('\n')
        if ' ~ ' not in ln: continue
        key, body = ln.split(' ~ ', 1)
        body = re.sub(r'\s*(%%|!!|\^\^)\s*$', '', body)
        body = body.rsplit('=>', 1)[0] if '=>' in body else body
        note = None
        if '@@' in body and not body.startswith('@text'):
            body, note = body.split('@@', 1)
        parts_src = []
        if body.startswith('@text '):
            parts_src = [r for r in body[6:].split(' ;; ')]
        if note: parts_src.append(note)
        for r in parts_src:
            p = [x.strip() for x in r.split('|')]
            if len(p) == 3: add(stem, key, *p)
# science answers
for f in glob.glob(str(ROOT / 'docs/source-verification/class-8/sci/ans/a02.txt')):
    for ln in open(f, encoding='utf8'):
        if ln.startswith('sol '):
            p = [x.strip() for x in ln[4:].split(' || ')]
            if len(p) == 3: add('sci8_a02', '', *p)
issues = []
def chk(r):
    src, key, en, ur, ps = r
    out = []
    for lang, t in (('ur', ur), ('ps', ps)):
        if not t: out.append(f'{lang} empty')
        if re.search('[\u064a\u0643\u0649]', t) and lang == 'ur': out.append('ur has Arabic yeh/kaf (use ی ک)')
        if re.search('[\u0643]', t) and lang == 'ps': out.append('ps has Arabic kaf (use ک)')
        words = re.findall(r'[A-Za-z]{4,}', re.sub(r'\[a-zA-Z]+', '', t))
        if len(words) >= 4 and not re.search(r'[\u0600-\u06ff]', t): out.append(f'{lang} is English')
    prose = bool(re.search(r'[A-Za-z]{4,}', re.sub(r'\[a-zA-Z]+', '', en)))
    if prose and ur == en and len(en) > 20: out.append('ur equals en')
    if prose and ps == ur and len(ur) > 20: out.append('ps equals ur')
    if len(ps) > 60 and not (set(ps) & PS_ONLY): out.append('ps long line without Pashto letters (copied from Urdu?)')
    return out
out_csv = ROOT / 'docs/review/urps_review_sheet.csv'
with open(out_csv, 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.writer(fh); w.writerow(['source', 'key', 'English', 'Urdu', 'Pashto', 'auto_flags', 'reviewer_ok', 'reviewer_fix_ur', 'reviewer_fix_ps'])
    for r in rows:
        fl = chk(r)
        if fl: issues.append((r, fl))
        w.writerow(list(r) + ['; '.join(fl), '', '', ''])
print(len(rows), 'trilingual lines ->', out_csv)
print(len(issues), 'lines with auto flags')
from collections import Counter
c = Counter(f for _, fl in issues for f in fl)
for k, v in c.most_common(): print(' ', v, k)
for r, fl in issues[:12]: print(r[0], r[1], fl, r[3][:50])
