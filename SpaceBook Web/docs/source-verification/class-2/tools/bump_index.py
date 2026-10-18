"""Cache-bump Class 2 script tags in index.html under the shared content lock.

    python bump_index.py VERSION file1.js [file2.js ...]

Also makes sure js/cls2_page_reader.js is loaded right after js/cls3_book_reader.js (after MATH6_READER).
Only the Class 2 tags are touched; the lock is tmp/class-content-shared.lock (atomic create, released in finally).
"""
import os, re, sys, time
from pathlib import Path

APP = Path(__file__).resolve().parents[4]
LOCK = APP / 'tmp' / 'class-content-shared.lock'
INDEX = APP / 'index.html'


def acquire(timeout=300):
    t0 = time.time()
    while True:
        try:
            fd = os.open(str(LOCK), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f'class-2 agent pid {os.getpid()} {time.strftime("%Y-%m-%dT%H:%M:%S")}\n'.encode())
            os.close(fd)
            return
        except FileExistsError:
            if time.time() - t0 > timeout:
                raise SystemExit('lock busy: ' + LOCK.read_text(errors='replace'))
            time.sleep(2)


def main():
    ver, files = sys.argv[1], sys.argv[2:]
    acquire()
    try:
        s = INDEX.read_text(encoding='utf-8')
        orig = s
        for f in files:
            if not re.fullmatch(r'[a-z0-9_]+_2_[a-z0-9_]*\.js|[a-z0-9_]+_2_data\.js|cls2_page_reader\.js', f):
                raise SystemExit('not a Class 2 file: ' + f)
            s, n = re.subn(r'(<script src="js/' + re.escape(f) + r')(\?v=[^"]*)?(")', r'\g<1>?v=' + ver + r'\g<3>', s)
            if not n and f != 'cls2_page_reader.js':
                raise SystemExit('tag not found: ' + f)
        if 'js/cls2_page_reader.js' not in s:
            m = re.search(r'[ \t]*<script src="js/cls3_book_reader\.js[^"]*"></script>\n', s)
            if not m:
                raise SystemExit('cls3_book_reader tag not found')
            s = s[:m.end()] + f'  <script src="js/cls2_page_reader.js?v={ver}"></script>\n' + s[m.end():]
        if s != orig:
            tmp = INDEX.with_suffix('.html.c2tmp')
            tmp.write_text(s, encoding='utf-8')
            tmp.replace(INDEX)
        print('index.html updated' if s != orig else 'index.html unchanged')
    finally:
        LOCK.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
