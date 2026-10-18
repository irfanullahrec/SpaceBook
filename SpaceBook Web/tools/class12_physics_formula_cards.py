"""Format audited Physics12 formula cards using the existing local engine."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
lock = ROOT / 'tmp/class-content-shared.lock'
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
os.write(fd, b'class12: audited Physics formula cards')
os.close(fd)
try:
    path = ROOT / 'js/app.js'
    text = path.read_bytes().decode('utf-8')
    old = "font-weight:700;color:#0f172a;margin-bottom:0.35rem;\">${f.formula}</div>"
    new = "font-weight:700;color:#0f172a;margin-bottom:0.35rem;\">${subjKey === 'phys' && f.id?.startsWith('phys12-') && f.latex && typeof SpaceBookLessonMath !== 'undefined' ? SpaceBookLessonMath.renderMath({latex:f.latex,display:false}) : f.formula}</div>"
    assert text.count(old) == 1
    path.write_bytes(text.replace(old, new).encode('utf-8'))
finally:
    lock.unlink()
