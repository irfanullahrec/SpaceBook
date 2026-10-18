# -*- coding: utf-8 -*-
"""Split a batch file ('=== pNNN' markers) into src/pNNN.src, expand them into pages/, then build.
    python -X utf8 comp/sp.py BATCHFILE"""
import re, sys, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
cur, buf, done = None, [], []


def flush():
    if cur:
        (HERE / 'src' / f'{cur}.src').write_text('\n'.join(buf).strip('\n') + '\n', encoding='utf-8')
        done.append(int(cur[1:]))


for line in Path(sys.argv[1]).read_text(encoding='utf-8').splitlines():
    m = re.match(r'^=== (p\d{3})\s*$', line)
    if m:
        flush(); cur, buf = m.group(1), []
    else:
        buf.append(line)
flush()
subprocess.run([sys.executable, '-X', 'utf8', str(HERE / 'expand.py')] + [str(n) for n in done], check=True)
subprocess.run([sys.executable, '-X', 'utf8', str(HERE.parent / 'tools' / 'build_book9.py'), 'comp'], check=True)
