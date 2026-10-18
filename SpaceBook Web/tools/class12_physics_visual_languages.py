"""Optional paired Class 12 Physics visual captions, preserving other defaults."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
lock = ROOT / 'tmp/class-content-shared.lock'
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
os.write(fd, b'class12: translated Physics diagram captions')
os.close(fd)
try:
    path = ROOT / 'js/app.js'
    text = path.read_bytes().decode('utf-8')
    old = "if (block.type === 'visual') return lang === 'en' ? (sec.diagramSvg || '') : '';"
    new = "if (block.type === 'visual') return lang === 'en' ? (sec.diagramSvg || '') : (sec.id?.startsWith('phys12-front-') ? (lang === 'ur' ? sec.diagramSvgUrdu || '' : sec.diagramSvgPashto || '') : '');"
    assert text.count(old) == 1
    path.write_bytes(text.replace(old, new).encode('utf-8'))
finally:
    lock.unlink()
