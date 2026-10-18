"""Lock-protected cache-key bump in the shared index.html for one Class 7 data file.

Usage: bump_cache.py js/general_science_7_data.js
Sets (or replaces) the ?v= key on that single <script src> line and touches nothing else.
Lock: tmp/class-content-shared.lock (atomic create; never removes another agent's lock).
"""
import os, re, sys, time, datetime
from pathlib import Path

APP = Path(__file__).resolve().parents[4]
LOCK = APP / 'tmp' / 'class-content-shared.lock'
INDEX = APP / 'index.html'


def acquire(timeout=120):
    LOCK.parent.mkdir(exist_ok=True)
    t0 = time.time()
    while True:
        try:
            fd = os.open(str(LOCK), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f'class-7 books agent pid {os.getpid()} {datetime.datetime.now().isoformat()}'.encode())
            os.close(fd)
            return
        except FileExistsError:
            if time.time() - t0 > timeout:
                raise SystemExit('lock busy: ' + LOCK.read_text(errors='replace'))
            time.sleep(1)


def main():
    target = sys.argv[1]
    if not re.fullmatch(r'js/[a-z0-9_]+_7_data\.js', target):
        raise SystemExit('only Class 7 data files may be bumped: ' + target)
    ver = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    acquire()
    try:
        s = open(INDEX, encoding='utf-8', newline='').read()
        pat = re.compile(r'(<script src="' + re.escape(target) + r')(\?v=[\w.]+)?(")')
        n = len(pat.findall(s))
        if n != 1:
            raise SystemExit(f'expected exactly one script line for {target}, found {n}')
        s2 = pat.sub(lambda m: f'{m.group(1)}?v={ver}{m.group(3)}', s)
        tmp = INDEX.with_suffix('.html.c7tmp')
        open(tmp, 'w', encoding='utf-8', newline='').write(s2)
        os.replace(tmp, INDEX)
        print(f'{target}?v={ver}')
    finally:
        LOCK.unlink()


if __name__ == '__main__':
    main()
