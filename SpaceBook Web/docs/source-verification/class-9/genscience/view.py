"""General Science 9 page viewer. python view.py sheet a b | page g... | half g..."""
import sys, os, glob
from PIL import Image
V = r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\2623a4cf-2559-4fc5-8354-1efdc66bc9d4\scratchpad\gs_view'
os.makedirs(V, exist_ok=True)
FS = sorted(glob.glob('D:/SpaceBook/Books/9th/9th General Science/JPG/*.jpg'))
def img(g): return Image.open(FS[g - 1]).convert('RGB')
if sys.argv[1] == 'sheet':
    a, b = int(sys.argv[2]), int(sys.argv[3]); cols = 6
    ims = [img(g).resize((240, 330)) for g in range(a, b + 1)]
    s = Image.new('RGB', (240 * cols, 330 * ((len(ims) + cols - 1) // cols)), 'white')
    for k, i in enumerate(ims): s.paste(i, ((k % cols) * 240, (k // cols) * 330))
    s.save(V + f'/sheet_{a}_{b}.png')
elif sys.argv[1] == 'half':
    for a in sys.argv[2:]:
        g = int(a); im = img(g); w, h = im.size
        im.crop((0, 0, w, int(h * .53))).save(V + f'/h{g:03d}a.png'); im.crop((0, int(h * .47), w, h)).save(V + f'/h{g:03d}b.png')
print('ok')
if sys.argv[1] == 'pair':
    for a in sys.argv[2:]:
        g = int(a); ims = [img(g), img(g + 1)]
        h = 1100; ims = [i.resize((int(i.width * h / i.height), h)) for i in ims]
        s = Image.new('RGB', (sum(i.width for i in ims), h), 'white'); x = 0
        for i in ims: s.paste(i, (x, 0)); x += i.width
        s.save(V + f'/pair{g:03d}.jpg', quality=80)
