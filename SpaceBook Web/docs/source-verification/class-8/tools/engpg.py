"""engpg.py N [N...] : render Class 8 English page idx N (JPG index) from the KPTBB PDF at 190 dpi to _render/eN.png.
PDF spread = N//2 + 3, left half if N is even, right half if odd (the PDF is a two-page-spread scan; idx 0 = spread 3 left)."""
import sys
from pathlib import Path
import pymupdf
PDF = r'D:/SpaceBook/Books/8th/8th English/PDF/English Book for 8 class KPTBB.pdf'
OUT = Path(__file__).resolve().parents[1] / '_render'
doc = pymupdf.open(PDF)
for a in sys.argv[1:]:
    n = int(a)
    page = doc[n // 2 + 3]
    r = page.rect
    clip = pymupdf.Rect(0, 0, r.width * 0.5, r.height) if n % 2 == 0 else pymupdf.Rect(r.width * 0.5, 0, r.width, r.height)
    page.get_pixmap(dpi=190, clip=clip).save(OUT / f'e{n}.png')
    print(n, 'spread', n // 2 + 3, 'L' if n % 2 == 0 else 'R')
