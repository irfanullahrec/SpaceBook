"""Render Class 9 source pages to JPEG in the scratchpad: python render9.py SUBJ IDX [IDX ...] [--dpi 110] [--half]
IDX is the 0-based page index (pNNN). --half also writes top/bottom halves at higher zoom for small Urdu print."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_book9 import SOURCES
OUT = 'D:/SpaceBook/_c9render'
args = sys.argv[1:]
subj = args.pop(0)
dpi = 110
half = '--half' in args
if '--dpi' in args:
    i = args.index('--dpi'); dpi = int(args[i + 1]); del args[i:i + 2]
args = [a for a in args if a != '--half']
os.makedirs(OUT, exist_ok=True)
src = SOURCES[subj]
from PIL import Image
for a in args:
    idx = int(a)
    if 'pdf' in src:
        import pymupdf
        n = idx
        for p in src['pdf']:
            d = pymupdf.open(p)
            if n < d.page_count:
                pix = d[n].get_pixmap(dpi=dpi)
                im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
                break
            n -= d.page_count
    else:
        import re
        files = sorted([f for f in os.listdir(src['jpg']) if re.fullmatch(r'\d+\.jpg', f)], key=lambda f: int(f[:-4]))
        im = Image.open(os.path.join(src['jpg'], files[idx])).convert('RGB')
        scale = 1100 / max(im.size)
        if scale < 1:
            im = im.resize((int(im.width * scale), int(im.height * scale)))
    im.save(f'{OUT}/{subj}{idx:03d}.jpg', quality=80)
    if half:
        w, h = im.size
        for k, box in (('a', (0, 0, w, h // 2 + 40)), ('b', (0, h // 2 - 40, w, h))):
            c = im.crop(box)
            c = c.resize((int(c.width * 1.4), int(c.height * 1.4)))
            c.save(f'{OUT}/{subj}{idx:03d}{k}.jpg', quality=80)
print('ok', OUT)
