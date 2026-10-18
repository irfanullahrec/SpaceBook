"""Two optional Physics labels; protect fresh shared-file read with exclusive lock."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
lock = ROOT / 'tmp/class-content-shared.lock'
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
os.write(fd, b'class12: optional Physics source-language labels')
os.close(fd)
try:
    target = ROOT / 'js/app.js'
    text = target.read_bytes().decode('utf-8')
    for old, new in [
        ('English Original (Hover for Word Meaning • Click Sentence for Translation):',
         "${subjKey === 'phys' && sec.sourceOriginalLabel ? sanitize(sec.sourceOriginalLabel) : 'English Original (Hover for Word Meaning • Click Sentence for Translation):'}"),
        ('letter-spacing:0.5px;">Urdu Translation (اردو ترجمہ):',
         "letter-spacing:0.5px;\">${subjKey === 'phys' && sec.sourceUrduLabel ? sanitize(sec.sourceUrduLabel) : 'Urdu Translation (اردو ترجمہ):'}"),
    ]:
        assert text.count(old) == 1
        text = text.replace(old, new)
    target.write_bytes(text.encode('utf-8'))
finally:
    lock.unlink()
