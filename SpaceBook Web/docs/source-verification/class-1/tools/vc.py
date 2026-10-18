"""Crop the printed page out of a Class 1 scan and save a readable PNG: vc.py SUBJ OUT idx... [--box x0,y0,x1,y1] [--w 1150] [--half top|bottom]"""
import sys
from pathlib import Path
from PIL import Image, ImageOps
a = sys.argv[1:]; subj = a.pop(0); out = Path(a.pop(0)); out.mkdir(parents=True, exist_ok=True)
box = (0.09, 0.08, 0.91, 0.85); w = 1150; half = None; idx = []
while a:
    t = a.pop(0)
    if t == '--box': box = tuple(float(x) for x in a.pop(0).split(','))
    elif t == '--w': w = int(a.pop(0))
    elif t == '--half': half = a.pop(0)
    else: idx.append(int(t))
for i in idx:
    im = ImageOps.exif_transpose(Image.open(f'D:/SpaceBook/_cls1_jpg/{subj}/{i:03}.jpg')).convert('RGB')
    W, H = im.size
    x0, y0, x1, y1 = box
    if half == 'top': y1 = y0 + (y1 - y0) * 0.55
    if half == 'bottom': y0 = y0 + (y1 - y0) * 0.45
    c = im.crop((int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H)))
    c = c.resize((w, int(c.height * w / c.width)), Image.LANCZOS)
    p = out / f'{subj}{i:03}{("_" + half) if half else ""}.png'; c.save(p); print(p)
