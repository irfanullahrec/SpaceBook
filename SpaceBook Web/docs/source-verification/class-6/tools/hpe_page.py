"""Crop one HPE scan page from the KPTBB PDF spreads: hpe_page.py IDX [IDX...] -> _crops/hpeNNN_a.png (top) / _b.png (bottom).
Spread 3 holds scans 1 (right half) and 2 (left half); scan k>=1 is in spread 3+(k-1)//2."""
import sys
from PIL import Image
for a in sys.argv[1:]:
    k = int(a); s = 3 + (k - 1) // 2
    im = Image.open(f'D:/SpaceBook/_cls6_jpg/_hpepdf/h{s:02}.png').convert('L')
    w, h = im.size
    pg = im.crop((w // 2, 0, w, h)) if k % 2 else im.crop((0, 0, w // 2, h))
    pw, ph = pg.size
    pg.crop((0, 0, pw, ph * 52 // 100)).save(f'D:/SpaceBook/_cls6_jpg/_crops/hpe{k:03}_a.png')
    pg.crop((0, ph * 48 // 100, pw, ph)).save(f'D:/SpaceBook/_cls6_jpg/_crops/hpe{k:03}_b.png')
    print(k, s, pg.size)
