"""Insert `sol` lines into page sources from an answers batch file.

    python -X utf8 tools/qa/apply_answers.py <class-dir> <subject> <batch.txt> [--dry]

Batch format (UTF-8):
    @@ p053:6                      <- anchor printed by tools/qa/list_unanswered.py (page:line of the q/qp line)
    B ## Echo is a reflected sound ...      <- the text that follows `sol ` on the inserted line (ANSWER ## step || step || step)
Lines starting with '#' outside an answer are comments. An answer may span one line only. The anchor line must be a q/qp
line; when its next line is already a `sol` the entry is skipped (listed). Line endings of the page file are kept.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'docs' / 'source-verification'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
DRY = '--dry' in sys.argv
cls, subj, batch = args[0], args[1], Path(args[2])
pdir = ROOT / cls / subj / 'pages'
entries = {}
cur = None
for ln in batch.read_text(encoding='utf-8').split('\n'):
    ln = ln.rstrip('\r')
    m = re.match(r'@@\s*(p\d{3}):(\d+)\s*$', ln)
    if m:
        cur = (m.group(1), int(m.group(2)))
        continue
    if cur and ln.strip() and not ln.startswith('#'):
        entries.setdefault(cur[0], {})[cur[1]] = ln.strip()
        cur = None
done = skipped = 0
for page, anchors in sorted(entries.items()):
    f = pdir / (page + '.txt')
    raw = f.read_bytes()
    crlf = b'\r\n' in raw
    L = raw.decode('utf-8').replace('\r\n', '\n').split('\n')
    for line in sorted(anchors, reverse=True):
        a = L[line - 1].strip() if 0 < line <= len(L) else ''
        if not re.match(r'(qp|q)\s', a):
            print(f'  SKIP {page}:{line} is not a q/qp line: {a[:60]}'); skipped += 1; continue
        nxt = L[line].strip() if line < len(L) else ''
        if nxt.startswith(('sol ', 'solution', 'qsol')):
            print(f'  SKIP {page}:{line} already has an answer'); skipped += 1; continue
        L.insert(line, 'sol ' + anchors[line])
        done += 1
    if not DRY:
        data = ('\r\n' if crlf else '\n').join(L).encode('utf-8')
        for attempt in range(8):   # Windows sometimes refuses a write for a moment (EINVAL)
            try:
                with open(f, 'wb') as fh:
                    fh.write(data)
                break
            except OSError:
                import time; time.sleep(0.6)
        else:
            raise
print(f'{cls}/{subj}: inserted {done}, skipped {skipped}{" (dry run)" if DRY else ""}')
