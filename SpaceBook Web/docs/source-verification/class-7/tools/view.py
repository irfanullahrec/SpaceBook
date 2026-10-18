"""Render scan pages for inspection: view.py SUBJECTDIR OUTDIR idx [idx...] [--w 1100] [--crop top,bottom]"""
import sys
from pathlib import Path
from PIL import Image, ImageOps
args = sys.argv[1:]; src = Path(args.pop(0)); out = Path(args.pop(0)); out.mkdir(parents=True, exist_ok=True)
w = 1100; crop = None; idxs = []
while args:
    a = args.pop(0)
    if a == '--w': w = int(args.pop(0))
    elif a == '--crop': crop = [float(x) for x in args.pop(0).split(',')]
    else: idxs.append(a)
for i in idxs:
    im = Image.open(src / f'{int(i):03}.jpg'); im = ImageOps.exif_transpose(im).convert('RGB')
    if crop: im = im.crop((0, int(crop[0]*im.height), im.width, int(crop[1]*im.height)))
    r = w / im.width; im = im.resize((w, int(im.height*r)))
    name = f'v{int(i):03}' + (f'_{crop[0]}' if crop else '') + '.png'
    im.save(out / name); print(out / name)
