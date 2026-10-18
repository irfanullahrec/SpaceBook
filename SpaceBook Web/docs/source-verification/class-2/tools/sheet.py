"""Contact sheet of scans: sheet.py SUBJ OUT.png FIRST LAST [W=260 COLS=6]"""
import sys
from PIL import Image, ImageDraw
subj, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
W = int(sys.argv[5]) if len(sys.argv) > 5 else 260; COLS = int(sys.argv[6]) if len(sys.argv) > 6 else 6
cells = []
for i in range(a, b + 1):
    im = Image.open(f'D:/SpaceBook/_cls2_jpg/{subj}/{i:03}.jpg').convert('RGB')
    im = im.resize((W, int(im.height * W / im.width)))
    c = Image.new('RGB', (W, im.height + 18), 'white'); c.paste(im, (0, 18))
    ImageDraw.Draw(c).text((4, 3), f'idx {i:03}', fill='red'); cells.append(c)
h = max(x.height for x in cells); rows = (len(cells) + COLS - 1) // COLS
s = Image.new('RGB', (COLS * (W + 4), rows * (h + 4)), 'black')
for k, c in enumerate(cells): s.paste(c, ((k % COLS) * (W + 4), (k // COLS) * (h + 4)))
s.save(out); print(out, s.size)
