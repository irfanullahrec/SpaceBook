# usage: css_append.py <rules-file>  -- appends rules to css/style.css under the shared lock
import os, sys, time, pathlib
root = pathlib.Path(r'D:\SpaceBook\SpaceBook Web'); lock = root / 'tmp/class-content-shared.lock'
for _ in range(60):
    try: fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); break
    except FileExistsError: time.sleep(2)
else: raise SystemExit('lock busy')
try:
    os.write(fd, b'class-11 biology css')
    css = root / 'css/style.css'; t = css.read_text(encoding='utf-8')
    add = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').strip('\n')
    if add not in t: css.write_text(t.rstrip('\n') + '\n' + add + '\n', encoding='utf-8', newline='\n'); print('css appended')
finally:
    os.close(fd); lock.unlink()
