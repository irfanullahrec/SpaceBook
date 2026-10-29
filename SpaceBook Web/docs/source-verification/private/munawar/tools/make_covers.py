"""Makes covers/Munawar/<subject id>.webp for every Munawar book: runs make_covers.js (Playwright draws each cover), then compresses.

    python docs/source-verification/private/munawar/tools/make_covers.py

The covers are our own artwork (see make_covers.js). Needs Node + Playwright + Pillow. Dev-only, never deployed.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
APP = HERE.parents[4]
OUT = APP / 'covers' / 'Munawar'
OUT.mkdir(parents=True, exist_ok=True)

tmp = tempfile.mkdtemp(prefix='munawar_covers_')
env = dict(os.environ, COVER_TMP=tmp)
r = subprocess.run(['node', str(HERE / 'make_covers.js')], env=env, cwd=str(APP))
if r.returncode:
    sys.exit('make_covers.js failed')

total = 0
for png in sorted(Path(tmp).glob('*.png')):
    im = Image.open(png).convert('RGB')
    if im.width > 380:
        im = im.resize((380, round(im.height * 380 / im.width)), Image.LANCZOS)
    dest = OUT / (png.stem + '.webp')
    im.save(dest, 'WEBP', quality=82, method=6)
    total += dest.stat().st_size
    png.unlink()
print(f'{len(list(OUT.glob("*.webp")))} covers, {total / 1024:.0f} KB in {OUT}')
