"""Add the Class 6 Mathematics reader script to index.html under the shared content lock."""
import os, time
from pathlib import Path
ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
lock = ROOT / 'tmp' / 'class-content-shared.lock'
lock.parent.mkdir(exist_ok=True)
for _ in range(60):
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); break
    except FileExistsError:
        time.sleep(2)
else:
    raise SystemExit('lock busy; not forcing')
try:
    os.write(fd, f'class-6 pid={os.getpid()}\n'.encode())
    index = ROOT / 'index.html'
    text = index.read_text(encoding='utf-8')
    anchor = '<script src="js/math12_translation_reader.js'
    line = '  <script src="js/math6_reader.js?v=20261010_1"></script>\n'
    if 'js/math6_reader.js' not in text:
        assert text.count(anchor) == 1
        pos = text.index('\n', text.index(anchor)) + 1
        index.write_text(text[:pos] + line + text[pos:], encoding='utf-8', newline='\n')
        print('inserted')
    else:
        print('already present')
finally:
    os.close(fd); os.remove(lock)
