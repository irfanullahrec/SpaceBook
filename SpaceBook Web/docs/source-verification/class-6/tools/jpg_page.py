"""Crop a scan into upscaled top/bottom halves for reading: jpg_page.py SUBJ IDX [IDX...] -> _crops/<subj>NNN_a.png / _b.png"""
import sys
from PIL import Image, ImageOps
subj = sys.argv[1]
for a in sys.argv[2:]:
    k = int(a)
    im = ImageOps.autocontrast(ImageOps.exif_transpose(Image.open(f'D:/SpaceBook/_cls6_jpg/{subj}/{k:03}.jpg')).convert('L'))
    w, h = im.size; s = 1300 / w
    im = im.resize((1300, int(h * s)), Image.LANCZOS); w, h = im.size
    im.crop((0, 0, w, h * 53 // 100)).save(f'D:/SpaceBook/_cls6_jpg/_crops/{subj}{k:03}_a.png')
    im.crop((0, h * 47 // 100, w, h)).save(f'D:/SpaceBook/_cls6_jpg/_crops/{subj}{k:03}_b.png')
print('ok')
