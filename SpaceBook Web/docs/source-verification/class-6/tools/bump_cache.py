"""Bump ?v= cache keys for Class 6 scripts (all *_6_data.js and the Class 6 readers) in index.html under the shared content lock.
Usage: bump_cache.py VERSION"""
import os, re, sys, time
from pathlib import Path
ROOT = Path(r'D:\SpaceBook\SpaceBook Web')
lock = ROOT / 'tmp' / 'class-content-shared.lock'
version = sys.argv[1]
for _ in range(60):
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        break
    except FileExistsError:
        time.sleep(2)
else:
    raise SystemExit('lock busy; not forcing')
try:
    os.write(fd, b'class-6 cache bump\n')
    f = ROOT / 'index.html'
    t = f.read_text(encoding='utf-8')
    t2 = re.sub(r'js/(math_6_data|math6_reader|cls6_book_reader|[a-z_]+_6_data)\.js\?v=\w+', lambda m: f'js/{m.group(1)}.js?v=' + version, t)
    if 'js/cls6_book_reader.js' not in t2:
        t2 = re.sub(r'(<script src="js/math6_reader\.js\?v=\w+"></script>)', lambda m: m.group(1) + chr(10) + '  <script src="js/cls6_book_reader.js?v=' + version + '"></script>', t2)
    if t2 != t:
        for attempt in range(10):
            try:
                f.write_text(t2, encoding='utf-8', newline='\n')
                break
            except OSError:
                time.sleep(1.5)  # index.html briefly locked by another reader on Windows
        else:
            raise SystemExit('index.html stayed locked; cache key not bumped')
    print('index.html cache keys ->', version)
finally:
    os.close(fd)
    os.remove(lock)
