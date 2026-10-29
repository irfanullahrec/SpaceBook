"""Renders the pages of a Munawar sample PDF to JPG so they can be read (and cropped) while transcribing.

    python -P docs/source-verification/private/munawar/tools/render_pages.py c1-math            every page
    python -P docs/source-verification/private/munawar/tools/render_pages.py c1-math 3 12       pages with index 3..12 (0-based; PDF page = index + 1)
    python -P docs/source-verification/private/munawar/tools/render_pages.py c1-math 7 --crop 0 0.5 1 1 --dpi 160   bottom half of page 7, larger

Output: D:/SpaceBook_Helpers/munawar_jpg/<id>/NNN.jpg (outside the repository; delete the folder when a book is finished).
The sample PDFs hold one 437 x 547 pixel image per page, so a higher dpi only enlarges it: it never shows more than the source has.
"""
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import registry  # noqa: E402

OUT = Path('D:/SpaceBook_Helpers/munawar_jpg')


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        sys.exit(__doc__)
    dpi, crop = 110, None
    if '--dpi' in args:
        i = args.index('--dpi'); dpi = int(args[i + 1]); del args[i:i + 2]
    if '--crop' in args:
        i = args.index('--crop'); crop = [float(x) for x in args[i + 1:i + 5]]; del args[i:i + 5]
    bid = args[0]
    e = next((x for x in registry.entries() if x['id'] == bid), None)
    if not e:
        sys.exit('unknown book ' + bid)
    doc = pymupdf.open(f"{registry.PDF_DIR}/{e['pdf']}")
    lo, hi = (int(args[1]), int(args[2])) if len(args) >= 3 else ((int(args[1]), int(args[1])) if len(args) == 2 else (0, doc.page_count - 1))
    d = OUT / bid
    d.mkdir(parents=True, exist_ok=True)
    for i in range(lo, min(hi, doc.page_count - 1) + 1):
        page = doc[i]
        clip = None
        if crop:
            r = page.rect
            clip = pymupdf.Rect(r.x0 + crop[0] * r.width, r.y0 + crop[1] * r.height, r.x0 + crop[2] * r.width, r.y0 + crop[3] * r.height)
        name = f'{i:03}' + ('c' if crop else '') + '.jpg'
        page.get_pixmap(dpi=dpi, clip=clip).save(str(d / name), jpg_quality=72)
    print(f'{bid}: pages {lo}-{min(hi, doc.page_count - 1)} -> {d}')


if __name__ == '__main__':
    main()
