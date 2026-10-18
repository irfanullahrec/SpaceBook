"""Contact sheet of a unit's coded figures: python sheet.py <unit> <id-substring...>"""
import sys, os, fitz, bio9_tools as T
from PIL import Image
O = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\svgprev'
unit = int(sys.argv[1]); keys = sys.argv[2:]
u = next(x for x in T.load_bio() if x['number'] == unit)
ims = []
for s in u['sections']:
    for b in s.get('sourceBlocks', []):
        if 'svg' in b and (not keys or any(k in b['id'] for k in keys)):
            d = fitz.open(stream=b['svg'].encode(), filetype='svg'); p = d[0].get_pixmap(dpi=55)
            ims.append(Image.frombytes('RGB', (p.width, p.height), p.samples))
cols = 3; cw = max(i.width for i in ims); ch = max(i.height for i in ims); rows = (len(ims) + cols - 1) // cols
sheet = Image.new('RGB', (cw * cols, ch * rows), 'white')
for i, im in enumerate(ims): sheet.paste(im, ((i % cols) * cw, (i // cols) * ch))
f = os.path.join(O, f'sheet{unit}.png'); sheet.save(f); print(f, len(ims))
