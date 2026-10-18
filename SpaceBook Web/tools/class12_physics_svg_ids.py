"""Give parallel Physics12 diagram panels independent SVG definition IDs."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1]
lock = ROOT / 'tmp/class-content-shared.lock'
fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
os.write(fd, b'class12: Physics parallel-panel SVG IDs')
os.close(fd)
try:
    path = ROOT / 'js/app.js'
    text = path.read_bytes().decode('utf-8')
    old = "if (block.type === 'visual') return lang === 'en' ? (block.blockId && sec.sourceBlocks ? (sec.sourceBlocks.find(item => item.id === block.blockId)?.svg || '') : (sec.diagramSvg || '')) : (sec.id?.startsWith('phys12-front-') ? (lang === 'ur' ? sec.diagramSvgUrdu || '' : sec.diagramSvgPashto || '') : '');"
    newline = '\r\n' if '\r\n' in text else '\n'
    new = '''if (block.type === 'visual') {
      let visual = lang === 'en' ? (block.blockId && sec.sourceBlocks ? (sec.sourceBlocks.find(item => item.id === block.blockId)?.svg || '') : (sec.diagramSvg || '')) : (sec.id?.startsWith('phys12-front-') ? (lang === 'ur' ? sec.diagramSvgUrdu || '' : sec.diagramSvgPashto || '') : '');
      if (sec.id?.startsWith('phys12-front-')) {
        const ids = [...visual.matchAll(/\\bid="([^"]+)"/g)].map(match => match[1]);
        for (const id of ids) {
          const unique = `${id}-${sectionIndex}-${lang}-${blockIndex}`;
          visual = visual.replaceAll(`id="${id}"`, `id="${unique}"`).replaceAll(`#${id})`, `#${unique})`).replaceAll(`aria-labelledby="${id}"`, `aria-labelledby="${unique}"`);
        }
      }
      return visual;
    }'''.replace('\n', newline)
    assert text.count(old) == 1
    path.write_bytes(text.replace(old, new).encode('utf-8'))
finally:
    lock.unlink()
