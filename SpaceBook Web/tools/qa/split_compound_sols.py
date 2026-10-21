"""Split group-level answer lines ("sol 1: (a) X; 2: (b) Y ... ## 3: why ...") into one `sol` per question part.

    python -X utf8 tools/qa/split_compound_sols.py <class-dir> <subject> [--write]
    e.g. python -X utf8 tools/qa/split_compound_sols.py class-9 sci --write

The page builder (class-6/tools/build_book6.py -> build_math6.py) attaches a `sol` line to the LAST question part only,
so a compound line leaves every other MCQ / short question of the group without a key. This tool finds each compound
line, matches the numbers to the `qp N` lines of the latest group (the group may start on an earlier page) and puts
`sol ANSWER ## step || step || step` straight after every matched `qp` (slot order of the book's languages, read from
the builder's LANGS). Keys can be 1, 2, 3 / i, ii, iii / Urdu letters. A `qp` that already has its own `sol` line is
left alone. Unclean lines are listed and left untouched.
Order of work for a book: apply_answers.py batches first (their anchors are line numbers), this tool afterwards.
"""
import re, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'docs' / 'source-verification'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
WRITE = '--write' in sys.argv
cls, subj = args[0], args[1]
bsrc = (ROOT / cls / 'tools' / ('build_book9.py' if cls == 'class-9' else 'build_book10.py')).read_text(encoding='utf-8')
mm = re.search(r"'%s':\s*\[('ur'|'en'|'ps'),\s*('ur'|'en'|'ps'),\s*('ur'|'en'|'ps')\]" % subj, bsrc.split('def main')[0].split('LANGS =')[-1] if 'LANGS =' in bsrc else '')
ORDER = [x.strip("'") for x in mm.groups()] if mm else ['en', 'ur', 'ps']
pdir = ROOT / cls / subj / 'pages'
files = sorted(pdir.glob('p[0-9][0-9][0-9].txt'))
raw = {f: f.read_bytes() for f in files}
crlf = {f: b'\r\n' in raw[f] for f in files}
lines = {f: raw[f].decode('utf-8').replace('\r\n', '\n').split('\n') for f in files}

DIG = str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', '01234567890123456789')
ROMAN = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, 'x': 10, 'xi': 11, 'xii': 12, 'xiii': 13, 'xiv': 14, 'xv': 15, 'xvi': 16, 'xvii': 17, 'xviii': 18, 'xix': 19, 'xx': 20}
UR = ['الف', 'ب', 'ج', 'د', 'ہ', 'و', 'ز', 'ح', 'ط', 'ی']
KEY = r'(?:\d{1,2}|xx|xix|xviii|xvii|xvi|xv|xiv|xiii|xii|xi|x|ix|viii|vii|vi|v|iv|iii|ii|i|الف|ب|ج|د|ہ|و|ز|ح|ط|ی)'
COMPOUND = re.compile(r'^sol\s+((?:Model answers\b.*?)|(?:(?:\d+|[۰-۹]+|i|ii|iii|iv|v|vi|vii|viii|ix|x|الف|ب|ج|د|ہ|و|ز|ح|ط|ی)\s*:\s*\S.*)|(?:\d+\.(?=\s)\s*\S.*))$')
MARK = re.compile('(' + KEY + r')\s*:\s+(?=\S)')
PS = re.compile('[ټځڅډړږښګڼېۍ]')
AR = re.compile('[؀-ۿ]')


def keyval(k):
    k = k.strip().translate(DIG).lower()
    if k.isdigit():
        return int(k)
    if k in UR:
        return UR.index(k) + 1
    return ROMAN.get(k)


def lang_of(t):
    if PS.search(t):
        return 'ps'
    if len(AR.findall(t)) > len(t) * 0.25:
        return 'ur'
    return 'en'


def lab(t):
    return re.sub(r'^Model answers\s*(?:\|\|)?\s*', '', t).strip()


def parse_numbered(s):
    """'1: a. 2: b' -> {1:'a.', 2:'b'}; keys must rise; label text before the first key is ignored."""
    s = s.strip().translate(DIG)
    pos, prev = [], 0
    for m in MARK.finditer(s):
        n = keyval(m.group(1))
        if n is not None and (m.start() == 0 or s[m.start() - 1] in ' \t') and n > prev and (prev == 0 or n <= prev + 12):
            pos.append((n, m.start(), m.end())); prev = n
    if not pos or pos[0][1] > 40:
        return None
    return {n: s[b:(pos[i + 1][1] if i + 1 < len(pos) else len(s))].strip().rstrip(';').strip() for i, (n, a, b) in enumerate(pos)}


groups = []     # {parts:{n:(file,idx)}, has:set}
report = {'split': 0, 'lines': 0, 'skipped_has': 0, 'unmatched': [], 'unparsed': []}
edits = {f: [] for f in files}
drop = {f: set() for f in files}

for f in files:
    L = lines[f]
    for i, ln in enumerate(L):
        s = ln.strip()
        if re.match(r'q\s', s):
            groups.append({'parts': {}, 'has': set()})
        elif s.startswith('qp '):
            if not groups:
                groups.append({'parts': {}, 'has': set()})
            m = re.match(r'qp\s+([^|\s]+)\s*\|', s)
            n = keyval(m.group(1)) if m else None
            if n is not None:
                groups[-1]['parts'][n] = (f, i)
                nxt = L[i + 1].strip() if i + 1 < len(L) else ''
                if nxt.startswith('sol ') and not COMPOUND.match(nxt):
                    groups[-1]['has'].add(n)
        elif s.startswith('sol '):
            m = COMPOUND.match(s)
            if not m:
                continue
            body = m.group(1)
            head, sep, tail = body.partition(' ## ')
            report['lines'] += 1
            where = f'{f.name}:{i + 1}'
            vals = {'en': {}, 'ur': {}, 'ps': {}}
            heads = {}
            if not head.startswith('Model answers'):
                heads = parse_numbered(head)
                if heads is None:
                    report['unparsed'].append(where); continue
            for t in [lab(x.strip()) for x in tail.split(' || ')] if sep else []:
                d = parse_numbered(t) if t else None
                if not d:
                    continue
                for n, tx in d.items():
                    vals[lang_of(tx)][n] = tx
            core = sorted(heads or {n for l in vals for n in vals[l]})
            if not core:
                report['unparsed'].append(where); continue
            tgt = next((g for g in reversed(groups) if g['parts']), None)   # the sol line belongs to the latest group, never an older one
            if tgt is None or sum(n in tgt['parts'] for n in core) < 0.6 * len(core):
                report['unmatched'].append(f'{where} keys {core[0]}..{core[-1]}'); continue
            absent = [n for n in core if n not in tgt['parts']]
            if absent:
                report.setdefault('absent', []).append(f'{where} no qp for {absent}')
            core = [n for n in core if n in tgt['parts']]
            for n in core:
                if n in tgt['has']:
                    report['skipped_has'] += 1
                    continue
                a = heads.get(n) or next((vals[l][n] for l in ('en', 'ur', 'ps') if n in vals[l]), '')
                if heads:
                    vals[lang_of(a)].setdefault(n, a)
                steps = [vals[l].get(n) or a for l in ORDER]
                if len(set(steps)) == 1:        # one language only: a single part, not the same text three times
                    steps = steps[:1]
                ff, ii = tgt['parts'][n]
                edits[ff].append((ii, 'sol ' + a + ' ## ' + ' || '.join(steps)))
                tgt['has'].add(n)
                report['split'] += 1
            drop[f].add(i)

changed = 0
for f in files:
    if not edits[f] and not drop[f]:
        continue
    ins = {}
    for ii, text in edits[f]:
        ins.setdefault(ii, []).append(text)
    out = []
    for i, ln in enumerate(lines[f]):
        if i in drop[f]:
            continue
        out.append(ln)
        out.extend(ins.get(i, []))
    changed += 1
    if WRITE:
        data = ('\r\n' if crlf[f] else '\n').join(out).encode('utf-8')
        for attempt in range(6):   # Windows sometimes refuses a write for a moment (EINVAL)
            try:
                with open(f, 'wb') as fh:
                    fh.write(data)
                break
            except OSError:
                time.sleep(0.5)
        else:
            raise
print(f'{cls}/{subj}: order {ORDER}, compound lines {report["lines"]}, parts answered {report["split"]}, already-answered {report["skipped_has"]}, files {"written" if WRITE else "would change"} {changed}')
for k in ('unparsed', 'unmatched', 'absent'):
    for x in report.get(k, []):
        print('  ', k, x)
