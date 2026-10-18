"""Render Pak Study pages. Global page g = 1..114 maps to pakstudy{1,2,3}.pdf. python view.py sheet 1 12 | half 5 6"""
import sys, os, fitz
from PIL import Image
V = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\pak_view'
os.makedirs(V, exist_ok=True)
DOCS = [fitz.open(r'D:/SpaceBook/Books/9th/9th Pak Study/PDF/pakstudy%d.pdf' % i) for i in (1, 2, 3)]


def page(g):
    return DOCS[(g - 1) // 38][(g - 1) % 38]


if sys.argv[1] == 'sheet':
    a, b = int(sys.argv[2]), int(sys.argv[3])
    ims = []
    for g in range(a, b + 1):
        page(g).get_pixmap(dpi=36).save(V + '/t.png'); ims.append(Image.open(V + '/t.png').copy())
    w = max(i.width for i in ims); h = max(i.height for i in ims); cols = 4
    s = Image.new('RGB', (w * cols, h * ((len(ims) + cols - 1) // cols)), 'white')
    for k, i in enumerate(ims):
        s.paste(i, ((k % cols) * w, (k // cols) * h))
    s.save(V + f'/sheet_{a}_{b}.png')
else:
    for a in sys.argv[2:]:
        g = int(a); pg = page(g); r = pg.rect
        for k, (y0, y1) in enumerate(((0.0, 0.53), (0.47, 1.0))):
            clip = fitz.Rect(r.x0 + r.width * 0.03, r.y0 + r.height * y0, r.x1 - r.width * 0.03, r.y0 + r.height * y1)
            pg.get_pixmap(dpi=125, clip=clip).save(os.path.join(V, f'p{g:03d}{"ab"[k]}.png'))
print('ok')
