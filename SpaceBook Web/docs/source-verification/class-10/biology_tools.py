"""Class 10 Biology helpers: shared-file lock patching, page rendering, progress records.

Usage:
  python -X utf8 biology_tools.py wire        # add Biology script tags to index.html (under the shared lock)
  python -X utf8 biology_tools.py render A B  # render PDF pages A..B to tmp/class-10-biology/bio-NNN.png
  python -X utf8 biology_tools.py crop N x0 y0 x1 y1 [dpi]  # crop region of PDF page N (fractions 0-1)
"""
import json, os, sys, time
from pathlib import Path

ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
LOCK = ROOT / 'tmp' / 'class-content-shared.lock'
PDF = Path(r'D:\SpaceBook\Books\10th\10th Bio\PDF\Biology Class 10 kpk book.pdf')
import os as _os
OUT = Path(_os.environ.get('BIO_RENDER_DIR', str(ROOT / 'tmp' / 'class-10-biology')))
PROGRESS = ROOT / 'docs' / 'source-verification' / 'class-10'


class SharedLock:
    def __enter__(self):
        deadline = time.time() + 120
        while True:
            try:
                self.fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(self.fd, f'class-10 biology agent pid={os.getpid()} {time.ctime()}'.encode())
                return self
            except FileExistsError:
                if time.time() > deadline:
                    raise RuntimeError('shared lock held by another agent for >120s; retry later')
                time.sleep(0.5)

    def __exit__(self, *a):
        try:
            os.close(self.fd)
        finally:
            try:
                LOCK.unlink()
            except FileNotFoundError:
                pass


SCRIPTS = [
    ('js/biology_10_front_source.js', 'js/data_bio.js'),
    ('js/biology_10_unit10_source.js', 'js/biology_10_front_source.js'),
    ('js/biology_10_unit11_source.js', 'js/biology_10_unit10_source.js'),
    ('js/biology_10_unit12_source.js', 'js/biology_10_unit11_source.js'),
    ('js/biology_10_unit13_source.js', 'js/biology_10_unit12_source.js'),
    ('js/biology_10_unit14_source.js', 'js/biology_10_unit13_source.js'),
    ('js/biology_10_unit15_source.js', 'js/biology_10_unit14_source.js'),
    ('js/biology_10_unit16_source.js', 'js/biology_10_unit15_source.js'),
    ('js/biology_10_unit17_source.js', 'js/biology_10_unit16_source.js'),
    ('js/biology_10_unit18_source.js', 'js/biology_10_unit17_source.js'),
    ('js/biology_10_back_source.js', 'js/biology_10_unit18_source.js'),
]
READER = ('js/biology_10_reader.js', 'js/app.js')


def wire(version):
    with SharedLock():
        html_path = ROOT / 'index.html'
        html = html_path.read_text(encoding='utf-8')
        lines = html.split('\n')
        changed = False

        def ensure(src, after):
            nonlocal lines, changed
            if any(f'src="{src}' in ln for ln in lines):
                return
            if not (ROOT / src).exists():
                return
            idx = next(i for i, ln in enumerate(lines) if f'src="{after}' in ln)
            indent = lines[idx][:len(lines[idx]) - len(lines[idx].lstrip())]
            lines.insert(idx + 1, f'{indent}<script src="{src}?v={version}"></script>')
            changed = True

        for src, after in SCRIPTS:
            ensure(src, after)
        ensure(*READER)
        if changed:
            html_path.write_text('\n'.join(lines), encoding='utf-8')
        return changed


def bump(version, srcs):
    """Bump cache-busting version of already wired Biology scripts (under the lock)."""
    import re
    with SharedLock():
        html_path = ROOT / 'index.html'
        html = html_path.read_text(encoding='utf-8')
        for src in srcs:
            html = re.sub(rf'(src="{re.escape(src)})\?v=[^"]*"', rf'\1?v={version}"', html)
        html_path.write_text(html, encoding='utf-8')


def render(a, b, dpi=110):
    import pymupdf
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(PDF)
    for n in range(a, b + 1):
        doc[n - 1].get_pixmap(dpi=dpi).save(OUT / f'bio-{n:03d}.png')
    return [str(OUT / f'bio-{n:03d}.png') for n in range(a, b + 1)]


def crop(n, x0, y0, x1, y1, dpi=220):
    import pymupdf
    doc = pymupdf.open(PDF)
    page = doc[n - 1]
    r = page.rect
    clip = pymupdf.Rect(r.x0 + r.width * x0, r.y0 + r.height * y0, r.x0 + r.width * x1, r.y0 + r.height * y1)
    path = OUT / f'bio-{n:03d}-crop-{int(x0*100)}-{int(y0*100)}-{int(x1*100)}-{int(y1*100)}.png'
    page.get_pixmap(dpi=dpi, clip=clip).save(path)
    return str(path)


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'wire':
        print('index.html changed' if wire(sys.argv[2] if len(sys.argv) > 2 else time.strftime('%Y%m%d_1')) else 'index.html already wired')
    elif cmd == 'bump':
        bump(sys.argv[2], sys.argv[3:])
        print('bumped')
    elif cmd == 'render':
        print('\n'.join(render(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 110)))
    elif cmd == 'crop':
        print(crop(int(sys.argv[2]), *map(float, sys.argv[3:7]), *( [int(sys.argv[7])] if len(sys.argv) > 7 else [])))
