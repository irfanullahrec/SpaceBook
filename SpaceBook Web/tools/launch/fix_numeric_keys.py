"""Numeric answers of multiple-choice questions in the page files ("sol 4 ## reason" under "(a) 2 (b) 4 (c) 6 (d) 8").

js/sb_mcq.js reads a bare number as the INDEX of the option (0 = first), so "sol 4" is not found among four options and "sol 2" marks option (c) when the
text means "2" = option (b). The page syntax that cannot be misread is the letter in front: "sol (b) 4 ## reason". This tool finds the question lines with
the options (a) (b) (c) (d) in the line, whose next line is  sol <number> [## reason]  and where exactly one option reads that number, and rewrites the sol line.

  python -X utf8 tools/launch/fix_numeric_keys.py            report only
  python -X utf8 tools/launch/fix_numeric_keys.py --write    rewrite the page files (then rebuild the books)

Dev-only, never shipped."""
import glob, os, re, sys, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
WRITE = '--write' in sys.argv
OPT = re.compile(r'\(([a-d])\)\s*(.*?)(?=\s*\([a-d]\)\s|$)')
SOL = re.compile(r'^(sol\s+)(\d+(?:\.\d+)?)(\s*##.*)?$')


def options(q):
    first = q.split(' || ')[0]
    if first.startswith(('q ', 'qp ')):
        first = first.split('|', 1)[1] if '|' in first else first
    ms = OPT.findall(first)
    if len(ms) < 3:
        return None
    letters = [m[0] for m in ms]
    if letters != list('abcd')[:len(letters)]:
        return None
    return [(m[0], m[1].strip()) for m in ms]


def reads_as(text, ans):
    t = text.strip().rstrip('.،۔')
    if t == ans:
        return True
    m = re.match(r'^' + re.escape(ans) + r'(?:\s+|(?=[^\d.]))(\D.*)$', t)
    return bool(m) and not re.match(r'^\d', m.group(1))


stats = collections.Counter()
by_dir = collections.Counter()
for path in sorted(glob.glob(os.path.join(ROOT, 'docs', 'source-verification', 'class-*', '*', 'pages', 'p*.txt'))):
    raw = open(path, encoding='utf8', newline='').read()
    eol = '\r\n' if '\r\n' in raw else '\n'
    lines = raw.split(eol)
    changed = False
    for i in range(len(lines) - 1):
        if not lines[i].startswith(('q ', 'qp ')):
            continue
        m = SOL.match(lines[i + 1])
        if not m:
            continue
        opts = options(lines[i])
        if not opts:
            continue
        ans = m.group(2)
        hits = [l for l, t in opts if reads_as(t, ans)]
        idx = int(ans) if ans.isdigit() else -1
        silent = 0 <= idx < len(opts) and 'abcd'[idx] not in hits
        if len(hits) != 1:
            stats['ambiguous or none (%s)' % ('silent wrong' if silent else 'open')] += 1
            if os.environ.get('SB_VERBOSE'):
                print('?', os.path.relpath(path, ROOT), i + 1, ans, [t for _, t in opts])
            continue
        stats['fixed' + (' (was marked wrong)' if silent else '')] += 1
        by_dir[os.path.relpath(os.path.dirname(os.path.dirname(path)), os.path.join(ROOT, 'docs', 'source-verification'))] += 1
        lines[i + 1] = m.group(1) + '(' + hits[0] + ') ' + ans + (m.group(3) or '')
        changed = True
    if changed and WRITE:
        open(path, 'w', encoding='utf8', newline='').write(eol.join(lines))

for k, v in sorted(stats.items()):
    print('%5d  %s' % (v, k))
for k, v in sorted(by_dir.items()):
    print('%5d  %s' % (v, k))
print('written' if WRITE else 'report only (--write to rewrite)')
