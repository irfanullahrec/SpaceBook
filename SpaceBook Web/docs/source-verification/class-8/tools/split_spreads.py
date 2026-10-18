"""Split a Class 8 book whose scans are two-page spreads into one image per printed page.
python tools/split_spreads.py SUBJ PDF [--rtl]
Renders each PDF page at 160 dpi; landscape pages are cut in half (right page first with --rtl).
The original spread links are kept in D:/SpaceBook/_cls8_jpg/<subj>_spreads; the split pages go to
D:/SpaceBook/_cls8_jpg/<subj>/NNN.jpg and a map is written to class-8/<subj>/spreads.tsv (page idx -> pdf page, half)."""
import sys, shutil, pymupdf
from pathlib import Path
from PIL import Image
subj, pdf = sys.argv[1], sys.argv[2]
rtl = '--rtl' in sys.argv
root = Path('D:/SpaceBook/_cls8_jpg')
src, keep = root / subj, root / f'{subj}_spreads'
if not keep.exists():
    src.rename(keep)
src.mkdir(exist_ok=True)
for f in src.glob('*.jpg'):
    f.unlink()
doc = pymupdf.open(pdf)
rows, k = [], 0
for n in range(doc.page_count):
    pix = doc[n].get_pixmap(dpi=160)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    w, h = im.size
    if w > h:
        o = w // 30
        halves = [('R', im.crop((w // 2 - o, 0, w, h))), ('L', im.crop((0, 0, w // 2 + o, h)))]
        if not rtl:
            halves.reverse()
    else:
        halves = [('P', im)]
    for tag, c in halves:
        c.save(src / f'{k:03}.jpg', quality=85)
        rows.append(f'{k}\t{n + 1}\t{tag}')
        k += 1
out = Path(__file__).resolve().parents[1] / subj
out.mkdir(exist_ok=True)
(out / 'spreads.tsv').write_text('# page idx\tpdf page\thalf\n' + '\n'.join(rows) + '\n', encoding='utf-8')
print(subj, k, 'pages')
