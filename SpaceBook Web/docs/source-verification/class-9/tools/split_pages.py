"""Split a batch file into pages: lines '=== pNNN' start a new page file.
Usage: python -X utf8 tools/split_pages.py SUBJ BATCHFILE"""
import sys, re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
subj, batch = sys.argv[1], Path(sys.argv[2])
out = HERE / subj / 'pages'
out.mkdir(parents=True, exist_ok=True)
cur, buf, written = None, [], []
def flush():
    if cur:
        (out / f'{cur}.txt').write_text('\n'.join(buf).strip('\n') + '\n', encoding='utf-8')
        written.append(cur)
for line in batch.read_text(encoding='utf-8').splitlines():
    m = re.match(r'^=== (p\d{3})\s*$', line)
    if m:
        flush(); cur, buf = m.group(1), []
    else:
        buf.append(line)
flush()
print('wrote', ' '.join(written))
