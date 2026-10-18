"""Render top/bottom halves of a PDF page at proof-reading resolution: python half.py 5 [6 ...]"""
import sys, os, fitz
d = fitz.open(r'D:\SpaceBook\Books\9th\9th urdu\PDF\9th Urdu.pdf')
V = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\urdu_view'
for a in sys.argv[1:]:
    n = int(a); pg = d[n - 1]; r = pg.rect
    for k, (y0, y1) in enumerate(((0.0, 0.53), (0.47, 1.0))):
        clip = fitz.Rect(r.x0 + r.width * 0.04, r.y0 + r.height * y0, r.x1 - r.width * 0.04, r.y0 + r.height * y1)
        pg.get_pixmap(dpi=125, clip=clip).save(os.path.join(V, f'h{n:03d}{"ab"[k]}.png'))
print('ok')
