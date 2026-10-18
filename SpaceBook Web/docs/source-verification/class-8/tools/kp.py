"""kp.py P [P...] : render printed page P of the Class 8 Math book from the uncropped KPTBB two-page spreads
to _render/kp<P>.png (spread i holds printed pages 2i-7 on the left and 2i-6 on the right)."""
import sys
from pathlib import Path
import pymupdf

PDF = r'D:/SpaceBook/Books/8th/8th MAths/PDF/Math Book for 8 class KPTBB.pdf'
OUT = Path(__file__).resolve().parents[1] / '_render'
doc = pymupdf.open(PDF)
for a in sys.argv[1:]:
    p = int(a)
    i, left = ((p + 7) // 2, True) if p % 2 else ((p + 6) // 2, False)
    if p >= 101:  # spread 54 repeats printed pages 99-100
        i += 1
    if p >= 137:  # spread 70 repeats printed pages 135-136
        i += 1
    page = doc[i]
    r = page.rect
    clip = pymupdf.Rect(0, 0, r.width * 0.53, r.height) if left else pymupdf.Rect(r.width * 0.47, 0, r.width, r.height)
    page.get_pixmap(dpi=190, clip=clip).save(OUT / f'kp{p}.png')
    print(p, 'spread', i, 'left' if left else 'right')
