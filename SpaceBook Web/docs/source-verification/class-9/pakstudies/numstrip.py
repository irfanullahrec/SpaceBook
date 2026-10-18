import sys, fitz
from PIL import Image, ImageDraw
from view import page, V
a, b = int(sys.argv[1]), int(sys.argv[2])
ims = []
for g in range(a, b + 1):
    pg = page(g); r = pg.rect
    pg.get_pixmap(dpi=70, clip=fitz.Rect(r.x0 + r.width * 0.3, r.y0 + r.height * 0.74, r.x1 - r.width * 0.3, r.y0 + r.height * 0.9)).save(V + '/n.png')
    im = Image.open(V + '/n.png').convert('RGB'); c = Image.new('RGB', (im.width + 60, im.height), 'white'); c.paste(im, (60, 0))
    ImageDraw.Draw(c).text((5, im.height // 2), str(g), fill='red'); ims.append(c)
w = max(i.width for i in ims); h = max(i.height for i in ims); cols = 5
s = Image.new('RGB', (w * cols, h * ((len(ims) + cols - 1) // cols)), 'white')
for k, i in enumerate(ims): s.paste(i, ((k % cols) * w, (k // cols) * h))
s.save(V + f'/nums_{a}_{b}.png'); print('ok')
