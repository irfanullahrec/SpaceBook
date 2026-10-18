"""preview.py N [N...] -> _render/preview.html with every SVG figure from those JPG-index pages (for visual checks)."""
import sys, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]
APP = HERE.parents[2]
src = (APP / 'js' / 'math_8_data.js').read_text(encoding='utf-8')
units = json.loads(re.search(r'const MATH_8_DATA = (.*?);\nconst MATH_8_BOOK', src, re.S).group(1))
book = json.loads(re.search(r'const MATH_8_BOOK = (.*?);\nconst MATH_8_WORDS', src, re.S).group(1))
want = {int(x) + 1 for x in sys.argv[1:]}
figs = []
def walk(blocks, pdf):
    for b in blocks:
        if b.get('t') == 'page':
            pdf[0] = b['pdf']
        if b.get('t') == 'svg' and pdf[0] in want:
            figs.append((pdf[0], b.get('cap'), b['svg']))
        if b.get('blocks'):
            walk(b['blocks'], pdf)
for u in units:
    for s in u.get('sections', []):
        if isinstance(s.get('blocks'), list):
            walk(s['blocks'], [None])
walk(book.get('frontMatter', []), [None])
html = '<!doctype html><meta charset="utf-8"><body style="font-family:sans-serif;background:#fff">' + ''.join(
    f'<figure style="border:1px solid #ccc;margin:8px;padding:8px"><figcaption>PDF {p} {(c or {}).get("en", "")}</figcaption>{s}</figure>' for p, c, s in figs)
(HERE / '_render' / 'preview.html').write_text(html, encoding='utf-8')
print(len(figs), 'figures')
