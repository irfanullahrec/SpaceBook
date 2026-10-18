"""Contact sheet of scan pages: sheet.py SUBJ OUT.png idx [idx...] [--w 760]  (2 pages per row)"""
import sys
from pathlib import Path
from PIL import Image, ImageOps
args = sys.argv[1:]; subj = args.pop(0); out = args.pop(0); w = 760; idx = []
while args:
    a = args.pop(0)
    if a == '--w': w = int(args.pop(0))
    else: idx.append(int(a))
ims = []
for i in idx:
    im = ImageOps.exif_transpose(Image.open(f'D:/SpaceBook/_cls6_jpg/{subj}/{i:03}.jpg')).convert('RGB')
    ims.append(im.resize((w, int(im.height * w / im.width))))
h = max(i.height for i in ims)
rows = (len(ims) + 1) // 2
sheet = Image.new('RGB', (w * 2 + 10, rows * (h + 10)), 'white')
for k, im in enumerate(ims):
    sheet.paste(im, ((k % 2) * (w + 10), (k // 2) * (h + 10)))
sheet.save(out); print(out)
