"""Grid of page-number crops to map printed page numbers: footers.py SUBJ OUT.png FIRST LAST [y0 y1]
Each cell = scan index label + the bottom band (default 88%-97% of height, middle 60% of width)."""
import sys
from PIL import Image, ImageDraw
subj, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
y0, y1 = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else (0.88, 0.97)
CW, COLS = 300, 4
cells = []
for i in range(a, b + 1):
    im = Image.open(f'D:/SpaceBook/_cls3_jpg/{subj}/{i:03}.jpg').convert('RGB')
    c = im.crop((int(im.width * 0.2), int(im.height * y0), int(im.width * 0.8), int(im.height * y1)))
    c = c.resize((CW, int(c.height * CW / c.width)))
    cell = Image.new('RGB', (CW, c.height + 22), 'white')
    cell.paste(c, (0, 22))
    ImageDraw.Draw(cell).text((4, 4), f'idx {i:03}', fill='red')
    cells.append(cell)
h = max(x.height for x in cells)
rows = (len(cells) + COLS - 1) // COLS
sheet = Image.new('RGB', (COLS * (CW + 6), rows * (h + 6)), 'black')
for k, cell in enumerate(cells):
    sheet.paste(cell, ((k % COLS) * (CW + 6), (k // COLS) * (h + 6)))
sheet.save(out); print(out, sheet.size)
