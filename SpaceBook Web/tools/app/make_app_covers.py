"""Makes the book-cover and class-card thumbnails the Android app bundles.

The website shows each book as its cover picture (js/app.js `coverPageMap`: subject id -> file under covers/) and each class as a
card picture (covers/Classes Cards/Another-Look/N.png). The app shows the same pictures, so it carries small copies:

    <out>/covers/<subjectId>.webp       width 360, one per subject that has a cover in coverPageMap
    <out>/covers/class-<classId>.webp   width 540, classes 1-12

Usage:   python tools/app/make_app_covers.py "<repo>/SpaceBook App/app/src/main/assets"
Needs Pillow. Dev-only (never deployed).
"""
import os
import re
import sys

from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
if not OUT:
    sys.exit(__doc__)

src = open(os.path.join(ROOT, 'js', 'app.js'), encoding='utf8').read()
m = re.search(r'const coverPageMap = \{(.*?)\n  \};', src, re.S)
if not m:
    sys.exit('coverPageMap not found in js/app.js')
pairs = re.findall(r'"([^"]+)"\s*:\s*"([^"]+)"', m.group(1))

os.makedirs(os.path.join(OUT, 'covers'), exist_ok=True)


def thumb(path, width, dest):
    im = Image.open(path)
    im = im.convert('RGB')
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(dest, 'WEBP', quality=78, method=6)
    return os.path.getsize(dest)


made, missing, total = 0, [], 0
for subject, rel in pairs:
    p = os.path.join(ROOT, 'covers', rel)
    if not os.path.isfile(p):
        missing.append((subject, rel))
        continue
    total += thumb(p, 360, os.path.join(OUT, 'covers', subject + '.webp'))
    made += 1

for n in range(1, 13):
    p = os.path.join(ROOT, 'covers', 'Classes Cards', 'Another-Look', f'{n}.png')
    if os.path.isfile(p):
        total += thumb(p, 540, os.path.join(OUT, 'covers', f'class-cls{n}.webp'))
        made += 1
    else:
        missing.append((f'cls{n}', p))

print(f'{made} thumbnails, {total / 1024:.0f} KB in {os.path.join(OUT, "covers")}')
for s, r in missing:
    print('missing cover file:', s, r)
