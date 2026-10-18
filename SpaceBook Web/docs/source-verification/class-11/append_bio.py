# usage: append_bio.py <partfile>
# Appends a part to the MASTER copy (kept on C: so a full D: disk can never truncate it), then deploys it to
# js/bio_11_data.js through a temp file and an atomic replace. Never writes the target in place.
import sys, pathlib, os, shutil
MASTER = pathlib.Path(r'C:\Users\SHEHRO~1\AppData\Local\Temp\claude\D--SpaceBook\1fc55121-65b0-446b-afe5-4d6046a4a9b5\scratchpad\bio_11_data.MASTER.js')
TARGET = pathlib.Path(r'D:\SpaceBook\SpaceBook Web\js\bio_11_data.js')
m = '// @@BIO11_APPEND_POINT@@'
def deploy():
    tmp = TARGET.with_suffix('.js.tmp')
    shutil.copyfile(MASTER, tmp)
    if tmp.stat().st_size != MASTER.stat().st_size: raise SystemExit('deploy size mismatch; target untouched')
    os.replace(tmp, TARGET)
if len(sys.argv) > 1:
    t = MASTER.read_text(encoding='utf-8'); assert t.count(m) == 1
    part = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').rstrip('\n') + '\n\n'
    bak = MASTER.with_suffix('.js.bak'); shutil.copyfile(MASTER, bak)
    MASTER.write_text(t.replace(m, part + m), encoding='utf-8', newline='\n')
    print('appended', len(part), 'chars to master')
deploy(); print('deployed', TARGET.stat().st_size, 'bytes')
