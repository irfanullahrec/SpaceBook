"""Wire a staged Class 10 book build into the live site (under the shared content lock).

Usage: python -X utf8 tools/wire_book10.py urdu <version>
  - copies class-10/<subj>/build/<file> to js/<file>
  - adds cls10 (window.CLS10_BOOKS) to js/cls6_book_reader.js if missing (minimal patch)
  - bumps ?v= of js/<file> and js/cls6_book_reader.js in index.html
"""
import re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
from biology_tools import SharedLock, ROOT  # noqa: E402

FILES = {'urdu': 'urdu_10_data.js', 'pakstudy': 'pakstudy_10_data.js', 'comp': 'computer_10_data.js', 'sci': 'general_science_10_data.js', 'drawing': 'drawing_10_data.js', 'hpe': 'hpe_10_data.js', 'islopt': 'islamiat_ikhtiari_10_data.js', 'quran': 'mutalia_quran_10_data.js', 'phys': 'physics_10_book_data.js', 'chem': 'chemistry_10_book_data.js'}
OLD = "classId === 'cls8' ? (window.CLS8_BOOKS || {}) : {})[subjKey]"
NEW = "classId === 'cls8' ? (window.CLS8_BOOKS || {}) : classId === 'cls10' ? (window.CLS10_BOOKS || {}) : {})[subjKey]"


def bump(html, path, ver):
    pat = re.compile(r'(<script src="' + re.escape(path) + r')(\?v=[^"]*)?(")')
    new, n = pat.subn(lambda m: m.group(1) + '?v=' + ver + m.group(3), html)
    if n != 1:
        raise SystemExit(f'expected exactly one script tag for {path}, found {n}')
    return new


def main():
    subj, ver = sys.argv[1], sys.argv[2]
    name = FILES[subj]
    src = HERE / subj / 'build' / name
    with SharedLock():
        shutil.copyfile(src, ROOT / 'js' / name)
        reader = ROOT / 'js' / 'cls6_book_reader.js'
        rt = open(reader, encoding='utf-8', newline='').read()
        if NEW not in rt and 'window.CLS10_BOOKS' not in rt:
            if rt.count(OLD) != 1:
                raise SystemExit('cls6_book_reader.js: anchor not found exactly once; not patched')
            open(reader, 'w', encoding='utf-8', newline='').write(rt.replace(OLD, NEW))
        idx = ROOT / 'index.html'
        html = open(idx, encoding='utf-8', newline='').read()
        html = bump(html, 'js/' + name, ver)
        html = bump(html, 'js/cls6_book_reader.js', ver + '_c10')
        open(idx, 'w', encoding='utf-8', newline='').write(html)
    print('wired', name, ver)


if __name__ == '__main__':
    main()
