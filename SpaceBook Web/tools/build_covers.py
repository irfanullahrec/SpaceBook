# Copies the cover art and videos that js/app.js references from D:\SpaceBook\Books\Cover Pages into
# SpaceBook Web/covers/, resizing large pictures for the web (same file names and formats, so no code changes).
# Re-run after adding a cover to app.js:   python tools/build_covers.py
import os, re, shutil, sys, urllib.parse
from PIL import Image

WEB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(os.path.dirname(WEB), 'Books', 'Cover Pages')
DST = os.path.join(WEB, 'covers')
MAX_W = 1000          # cards and book covers never display wider than this
JPEG_Q = 82

text = open(os.path.join(WEB, 'js', 'app.js'), encoding='utf-8').read()
names = {urllib.parse.unquote(m) for m in re.findall(r"[\"'`]([^\"'`\n]{1,120}?\.(?:png|jpe?g|jfif|webp|mp4))[\"'`]", text)}
found, missing, before, after = 0, [], 0, 0
for n in sorted(names):
    rel = re.sub(r'^.*?covers/', '', n)
    for base in ['', 'Classes Cards/Another-Look', 'Videos']:
        src = os.path.join(SRC, base, rel)
        if os.path.isfile(src):
            break
    else:
        if not n.startswith(('assets/', 'logo')) and not os.path.isfile(os.path.join(WEB, n)):
            missing.append(n)
        continue
    dst = os.path.join(DST, base, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    found += 1
    before += os.path.getsize(src)
    ext = os.path.splitext(src)[1].lower()
    if ext == '.mp4':
        shutil.copy2(src, dst)
    else:
        im = Image.open(src)
        fmt = 'PNG' if ext == '.png' else 'JPEG' if ext in ('.jpg', '.jpeg', '.jfif') else im.format
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        if fmt == 'JPEG':
            im.convert('RGB').save(dst, 'JPEG', quality=JPEG_Q, optimize=True, progressive=True)
        else:
            im.save(dst, fmt, optimize=True)
        if os.path.getsize(dst) > os.path.getsize(src):   # never make a file bigger
            shutil.copy2(src, dst)
    after += os.path.getsize(dst)
print(f'{found} files: {before/1e6:.0f} MB -> {after/1e6:.0f} MB in covers/')
if missing:
    print('referenced but not in Books/Cover Pages:', missing)
