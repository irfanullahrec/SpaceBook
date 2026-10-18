"""Side-by-side sheet of two English PDF pages: python pair.py 15 16"""
import sys, os
from PIL import Image
V = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\urdu_view'
ims = [Image.open(os.path.join(V, f'p{int(n):03d}.png')) for n in sys.argv[1:]]
ims = [im.crop((int(im.width*.1), int(im.height*.08), int(im.width*.9), int(im.height*.92))) for im in ims]
h = max(i.height for i in ims); w = sum(i.width for i in ims)
s = Image.new('RGB', (w, h), 'white'); x = 0
for im in ims: s.paste(im, (x, 0)); x += im.width
s.thumbnail((1900, 1300))
f = os.path.join(V, 'pair_' + '_'.join(sys.argv[1:]) + '.png'); s.save(f); print(f)
