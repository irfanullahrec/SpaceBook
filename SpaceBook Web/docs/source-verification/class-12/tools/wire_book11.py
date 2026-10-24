"""Wire staged Class 11 page books into the live site (under the shared content lock).

Usage: python -X utf8 tools/wire_book11.py <version> KEY [KEY ...]
  - copies class-11/KEY/build/<name>_11_book.js to js/
  - inserts (or bumps) its <script> tag in index.html right after the book's data script
  - adds cls11.<reader subject key> (unit count) to tests/contract/cls_books.json
"""
import json, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE.parent / 'class-10'))
sys.path.insert(0, str(HERE / 'book12'))
from biology_tools import SharedLock, ROOT  # noqa: E402
import engine11 as E  # noqa: E402
from wire_book12 import bump  # noqa: E402


def main():
    ver, keys = sys.argv[1], sys.argv[2:]
    with SharedLock():
        idx = ROOT / 'index.html'
        html = open(idx, encoding='utf-8', newline='').read()
        lock = ROOT / 'tests' / 'contract' / 'cls_books.json'
        books = json.loads(open(lock, encoding='utf-8').read())
        for key in keys:
            data_file, glob, view, (name, out_file, g, title) = E.BOOKS[key]
            src = HERE.parent / 'class-11' / key / 'build' / out_file
            shutil.copyfile(src, ROOT / 'js' / out_file)
            html = bump(html, 'js/' + out_file, ver, 'js/' + data_file)
            units = json.loads(re.search(r'const \w+ = (\[.*\]);\nif \(typeof window', src.read_text(encoding='utf-8'), re.S).group(1))
            books[f'cls11.{view}'] = len(units)
            print('wired', out_file, len(units), 'units')
        open(idx, 'w', encoding='utf-8', newline='').write(html)
        txt = open(lock, encoding='utf-8', newline='').read()
        nl = '\r\n' if '\r\n' in txt else '\n'
        # existing entries keep their order; new Class 11 books go in before the first Class 12 entry
        old = json.loads(txt)
        out, put = {}, False
        for k, v in old.items():
            if k.startswith('cls12.') and not put:
                out.update({n: books[n] for n in sorted(books) if n not in old})
                put = True
            out[k] = books.get(k, v)
        if not put:
            out.update({n: books[n] for n in books if n not in out})
        open(lock, 'w', encoding='utf-8', newline='').write(json.dumps(out, indent=1, ensure_ascii=False).replace('\n', nl) + nl)


if __name__ == '__main__':
    main()
