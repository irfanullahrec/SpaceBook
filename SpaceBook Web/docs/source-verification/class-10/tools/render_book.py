"""Render full source pages of a build_book10 book: python -X utf8 tools/render_book.py SUBJ a b [dpi]
Writes _render/fNNN.png where NNN is the page-file index (pNNN.txt) and prints idx -> pdf file:page."""
import sys
from pathlib import Path
import pymupdf
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_book10 as bb

subj, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 150
pages = bb.source_pages(subj)
out = Path(__file__).resolve().parents[1] / '_render'
out.mkdir(exist_ok=True)
for i in range(a, min(b, len(pages) - 1) + 1):
    path, k = pages[i]
    pymupdf.open(path)[k - 1].get_pixmap(dpi=dpi).save(str(out / f'f{i:03}.png'))
    print(f'p{i:03} = {Path(path).name} page {k}')
