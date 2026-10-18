from pathlib import Path
import os
ROOT = Path(__file__).resolve().parents[1]
lock = ROOT / 'tmp/class-content-shared.lock'
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
os.write(fd, b'class12: individual Physics figure translations')
os.close(fd)
try:
    path = ROOT / 'js/app.js'
    text = path.read_bytes().decode('utf-8')
    old = "let visual = lang === 'en' ? (block.blockId && sec.sourceBlocks ? (sec.sourceBlocks.find(item => item.id === block.blockId)?.svg || '') : (sec.diagramSvg || '')) : (sec.id?.startsWith('phys12-front-') ? (lang === 'ur' ? sec.diagramSvgUrdu || '' : sec.diagramSvgPashto || '') : '');"
    new = old + "\n      if (sec.id?.startsWith('phys12-front-') && block.blockId && sec.sourceBlocks && lang !== 'en') { const item = sec.sourceBlocks.find(item => item.id === block.blockId); visual = lang === 'ur' ? item?.svgUrdu || '' : item?.svgPashto || ''; }"
    newline = '\r\n' if '\r\n' in text else '\n'
    assert text.count(old) == 1
    path.write_bytes(text.replace(old, new.replace('\n',newline)).encode('utf-8'))
finally:
    lock.unlink()
