"""Wire a staged Class 9 book build into the live site (under the shared content lock).

Usage: python -X utf8 tools/wire_book9.py SUBJ <version>
  - copies class-9/<subj>/build/<file> to js/<file>
  - adds cls9 (window.CLS9_BOOKS) to js/cls6_book_reader.js if missing
  - for isl: adds an ISLAMIAT_9_DATA branch to the 'isl' chapter list in js/app.js if missing
  - bumps (or inserts) the ?v= script tag of js/<file> and bumps js/cls6_book_reader.js in index.html
"""
import os, re, shutil, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
LOCK = ROOT / 'tmp' / 'class-content-shared.lock'
FILES = {'isl': 'islamiat_9_data.js', 'quran': 'mutalia_quran_9_data.js', 'hpe': 'hpe_9_data.js', 'drawing': 'drawing_9_data.js', 'comp': 'computer_9_data.js', 'sci': 'general_science_9_book.js', 'pakstudy': 'pakstudy_9_book.js', 'eng': 'english_9_book.js'}
OLD = "classId === 'cls10' ? (window.CLS10_BOOKS || {}) : {})[subjKey]"
NEW = "classId === 'cls10' ? (window.CLS10_BOOKS || {}) : classId === 'cls9' ? (window.CLS9_BOOKS || {}) : {})[subjKey]"
ISL_ANCHOR = "  if (subjKey === 'isl') {\n"
COMP_ANCHOR = "    const isCls10 = (classId === 'cls10' || state.selectedClass === 'cls10');\n    if (isCls10 && typeof COMPUTER_10_DATA"
COMP_PATCH = "    if ((classId === 'cls9' || state.selectedClass === 'cls9') && typeof COMPUTER_9_DATA !== 'undefined' && Array.isArray(COMPUTER_9_DATA)) return COMPUTER_9_DATA;\n"
ISL_PATCH = "    if ((classId === 'cls9' || state.selectedClass === 'cls9') && typeof ISLAMIAT_9_DATA !== 'undefined' && Array.isArray(ISLAMIAT_9_DATA)) return ISLAMIAT_9_DATA;\n"


class SharedLock:
    def __enter__(self):
        deadline = time.time() + 120
        while True:
            try:
                self.fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self.fd, f'class-9 book agent pid={os.getpid()} {time.ctime()}'.encode())
                return self
            except FileExistsError:
                if time.time() > deadline:
                    raise RuntimeError('shared lock held by another agent for >120s')
                time.sleep(0.5)

    def __exit__(self, *a):
        os.close(self.fd)
        LOCK.unlink(missing_ok=True)


def rw(path, fn):
    t = open(path, encoding='utf-8', newline='').read()
    n = fn(t)
    if n != t:
        open(path, 'w', encoding='utf-8', newline='').write(n)


def bump(html, path, ver, insert_after=None):
    pat = re.compile(r'(<script src="' + re.escape(path) + r')(\?v=[^"]*)?(")')
    new, n = pat.subn(lambda m: m.group(1) + '?v=' + ver + m.group(3), html)
    if n == 1:
        return new
    if n == 0 and insert_after:
        m = re.search(r'<script src="' + re.escape(insert_after) + r'[^"]*"></script>\s*\n', html)
        if not m:
            raise SystemExit(f'cannot insert {path}: anchor {insert_after} not found')
        return html[:m.end()] + f'<script src="{path}?v={ver}"></script>\n' + html[m.end():]
    raise SystemExit(f'expected exactly one script tag for {path}, found {n}')


def main():
    subj, ver = sys.argv[1], sys.argv[2]
    name = FILES[subj]
    with SharedLock():
        shutil.copyfile(HERE / subj / 'build' / name, ROOT / 'js' / name)

        def reader(t):
            if NEW in t or "classId === 'cls9' ? (window.CLS9_BOOKS || {})" in t:
                return t
            if t.count(OLD) != 1:
                raise SystemExit('cls6_book_reader.js anchor not found exactly once')
            return t.replace(OLD, NEW)
        rw(ROOT / 'js' / 'cls6_book_reader.js', reader)
        if subj == 'isl':
            def app(t):
                if ISL_PATCH in t:
                    return t
                if t.count(ISL_ANCHOR) != 1:
                    raise SystemExit('app.js isl anchor not found exactly once')
                return t.replace(ISL_ANCHOR, ISL_ANCHOR + ISL_PATCH)
            rw(ROOT / 'js' / 'app.js', app)
        if subj == 'comp':
            def app_c(t):
                if COMP_PATCH.strip() in t:
                    return t
                pat = re.compile(r"(    const isCls10 = \(classId === 'cls10' \|\| state\.selectedClass === 'cls10'\);(\r?\n)    if \(isCls10 && typeof COMPUTER_10_DATA)")
                if len(pat.findall(t)) != 1:
                    raise SystemExit('app.js comp anchor not found exactly once')
                return pat.sub(lambda m: COMP_PATCH.rstrip('\n') + m.group(2) + m.group(1), t)
            rw(ROOT / 'js' / 'app.js', app_c)
        rw(ROOT / 'index.html', lambda h: bump(bump(h, 'js/' + name, ver, insert_after='js/hpe_9_data.js'), 'js/cls6_book_reader.js', ver + '_c9'))
    print('wired', name, ver)


if __name__ == '__main__':
    main()
