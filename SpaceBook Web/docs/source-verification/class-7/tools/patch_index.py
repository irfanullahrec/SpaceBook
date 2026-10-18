"""Minimal, lock-protected edits to the shared index.html for Class 7 Mathematics.

- bumps the ?v= cache key of js/math_7_data.js and js/math7_reader.js
- inserts the js/math7_reader.js <script> line right after js/math6_reader.js (once)
Lock: tmp/class-content-shared.lock (atomic create; never removes another agent's lock).
"""
import os, re, sys, time, datetime
from pathlib import Path

APP = Path(__file__).resolve().parents[4]
LOCK = APP / 'tmp' / 'class-content-shared.lock'
INDEX = APP / 'index.html'


def acquire(timeout=120):
    t0 = time.time()
    while True:
        try:
            fd = os.open(str(LOCK), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f'class-7 math agent pid {os.getpid()} {datetime.datetime.now().isoformat()}'.encode())
            os.close(fd)
            return
        except FileExistsError:
            if time.time() - t0 > timeout:
                raise SystemExit('lock busy: ' + LOCK.read_text(errors='replace'))
            time.sleep(1)


def main():
    ver = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    acquire()
    try:
        s = open(INDEX, encoding='utf-8', newline='').read()
        s2 = re.sub(r'js/math_7_data\.js\?v=[\w.]+', f'js/math_7_data.js?v={ver}', s)
        if 'js/math7_reader.js' not in s2:
            m = re.search(r'^([ \t]*)<script src="js/math6_reader\.js[^"]*"></script>\r?\n', s2, re.M)
            if not m:
                raise SystemExit('math6_reader.js script line not found')
            nl = '\r\n' if m.group(0).endswith('\r\n') else '\n'
            s2 = s2[:m.end()] + f'{m.group(1)}<script src="js/math7_reader.js?v={ver}"></script>{nl}' + s2[m.end():]
        else:
            s2 = re.sub(r'js/math7_reader\.js\?v=[\w.]+', f'js/math7_reader.js?v={ver}', s2)
        if s2 != s:
            INDEX.write_text(s2, encoding='utf-8', newline='')
        print('index.html updated' if s2 != s else 'index.html unchanged', ver)
    finally:
        LOCK.unlink()


if __name__ == '__main__':
    main()
