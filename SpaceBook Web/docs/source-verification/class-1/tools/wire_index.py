"""Add/refresh the Class 1 book scripts in index.html under tmp/class-content-shared.lock.

    python wire_index.py VERSION        e.g. 20261012_c1m40

Inserts js/<name>_1_book.js right after the matching legacy js/<name>_1_data.js tag (only for books that exist)
and js/cls1_book_reader.js right after js/cls4_book_reader.js; existing Class 1 book tags get ?v=VERSION.
Touches nothing else in index.html.
"""
import os, re, sys, time
from pathlib import Path

APP = Path(__file__).resolve().parents[4]
LOCK = APP / 'tmp' / 'class-content-shared.lock'
HTML = APP / 'index.html'
PAIRS = [('math_1_data.js', 'math_1_book.js'), ('english_1_data.js', 'english_1_book.js'),
         ('islamyat_1_data.js', 'islamyat_1_book.js'), ('nazira_1_data.js', 'nazira_1_book.js'),
         ('pashto_1_data.js', 'pashto_1_book.js'), ('drawing_1_data.js', 'drawing_1_book.js'),
         ('drawing_1_book.js', 'urdu_1_book.js'), ('urdu_1_book.js', 'gk_1_book.js')]


def acquire(timeout=120):
    t0 = time.time()
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, f'class1-agent {os.getpid()} {time.ctime()}'.encode())
            os.close(fd)
            return
        except FileExistsError:
            if time.time() - t0 > timeout:
                raise SystemExit('lock busy: ' + LOCK.read_text(errors='replace'))
            time.sleep(2)


def main():
    ver = sys.argv[1]
    acquire()
    try:
        s = HTML.read_text(encoding='utf-8')
        orig = s
        for legacy, new in PAIRS:
            if not (APP / 'js' / new).exists():
                continue
            if f'js/{new}' in s:
                s = re.sub(rf'js/{re.escape(new)}\?v=[^"]*', f'js/{new}?v={ver}', s)
            else:
                m = re.search(rf'(\n([ \t]*)<script src="js/{re.escape(legacy)}[^"]*"></script>)', s)
                if not m:
                    raise SystemExit('anchor not found for ' + legacy)
                s = s[:m.end()] + f'\n{m.group(2)}<script src="js/{new}?v={ver}"></script>' + s[m.end():]
        if 'js/cls1_book_reader.js' in s:
            s = re.sub(r'js/cls1_book_reader\.js\?v=[^"]*', f'js/cls1_book_reader.js?v={ver}', s)
        else:
            m = re.search(r'(\n([ \t]*)<script src="js/cls4_book_reader\.js[^"]*"></script>)', s)
            if not m:
                raise SystemExit('anchor not found for cls4_book_reader.js')
            s = s[:m.end()] + f'\n{m.group(2)}<script src="js/cls1_book_reader.js?v={ver}"></script>' + s[m.end():]
        if s != orig:
            tmp = HTML.with_suffix('.html.c1tmp')
            tmp.write_text(s, encoding='utf-8')
            tmp.replace(HTML)
        print('index.html updated' if s != orig else 'index.html unchanged')
    finally:
        LOCK.unlink(missing_ok=True)


if __name__ == '__main__':
    main()
