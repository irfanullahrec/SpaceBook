"""sheet.py SUBJ START COUNT [COLS] -> _render/sheet_SUBJ_START.png thumbnail grid with scan numbers."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps
subj, start, count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); cols = int(sys.argv[4]) if len(sys.argv) > 4 else 4
src = Path('D:/SpaceBook/_cls7_jpg') / subj; tw = 420
ims = []
for i in range(start, start + count):
    p = src / f'{i:03}.jpg'
    if not p.exists(): break
    im = ImageOps.exif_transpose(Image.open(p)).convert('RGB'); im = im.resize((tw, int(im.height * tw / im.width)))
    ImageDraw.Draw(im).rectangle((0, 0, 60, 30), fill='yellow'); ImageDraw.Draw(im).text((5, 5), str(i), fill='black')
    ims.append(im)
th = max(i.height for i in ims); rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cols * tw, rows * th), 'white')
for k, im in enumerate(ims): sheet.paste(im, ((k % cols) * tw, (k // cols) * th))
out = Path(__file__).resolve().parents[1] / '_render' / f'sheet_{subj}_{start}.png'; sheet.save(out); print(out)
