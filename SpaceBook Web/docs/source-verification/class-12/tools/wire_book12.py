"""Wire a staged Class 12 book build into the live site (under the shared content lock).

Usage: python -X utf8 tools/wire_book12.py SUBJ <version>      (SUBJ: math, stat, pakstudy, hpe, civics, ...)
  - copies class-12/<subj>/build/<file> to js/
  - bumps (or, for the page books made by book12/engine.py, inserts after the book's data script) the ?v= tag in index.html
  - adds the book's unit count to tests/contract/cls_books.json (page books)
"""
import json, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE.parent / 'class-10'))
sys.path.insert(0, str(HERE / 'book12'))
from biology_tools import SharedLock, ROOT  # noqa: E402

FILES = {'math': 'math_12_pagebook_data.js', 'stat': 'statistics_12_book_data.js'}


def bump(html, path, ver, after=None):
    pat = re.compile(r'(<script src="' + re.escape(path) + r')(\?v=[^"]*)?(")')
    new, n = pat.subn(lambda m: m.group(1) + '?v=' + ver + m.group(3), html)
    if n == 1:
        return new
    if n == 0 and after:
        m = re.search(r'<script src="' + re.escape(after) + r'[^"]*"></script>(\r?\n)', html)
        if not m:
            raise SystemExit(f'cannot insert {path}: {after} not found')
        return html[:m.end()] + f'  <script src="{path}?v={ver}"></script>' + m.group(1) + html[m.end():]
    raise SystemExit(f'expected exactly one script tag for {path}, found {n}')


def main():
    subj, ver = sys.argv[1], sys.argv[2]
    after = None
    if subj in FILES:
        name = FILES[subj]
    else:
        import importlib
        cfg = importlib.import_module('cfgs.' + subj)
        name = cfg.BOOK_NAME[1]
        after = 'js/' + cfg.DATA_FILE
    src = HERE / subj / 'build' / name
    with SharedLock():
        shutil.copyfile(src, ROOT / 'js' / name)
        idx = ROOT / 'index.html'
        html = open(idx, encoding='utf-8', newline='').read()
        html = bump(html, 'js/' + name, ver, after)
        open(idx, 'w', encoding='utf-8', newline='').write(html)
        if after:
            lock = ROOT / 'tests' / 'contract' / 'cls_books.json'
            txt = open(lock, encoding='utf-8', newline='').read()
            units = len(json.loads(re.search(r'const \w+ = (\[.*\]);\nif \(typeof window', src.read_text(encoding='utf-8'), re.S).group(1)))
            key = f'cls12.{subj}'
            if f'"{key}"' not in txt:
                d = json.loads(txt)
                d[key] = units
                nl = '\r\n' if '\r\n' in txt else '\n'
                open(lock, 'w', encoding='utf-8', newline='').write(json.dumps(d, indent=1, ensure_ascii=False).replace('\n', nl) + nl)
    print('wired', name, ver)


if __name__ == '__main__':
    main()
