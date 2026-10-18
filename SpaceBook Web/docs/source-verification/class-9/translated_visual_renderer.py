import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 paired visual labels\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    start=text.index('function renderScienceSourceLayout(')
    end=text.index('\nfunction renderClass9PhysicsFrontMatterBlocks(',start)
    chunk=text[start:end]
    anchor="    if (block.type === 'visual')"
    pos=chunk.index(anchor)
    addition='''    if (block.type === 'visual' && block.blockId && sec.sourceBlocks) {
      const visual = sec.sourceBlocks.find(item => item.id === block.blockId);
      return lang === 'en' ? (visual?.svg || '') : (lang === 'ur' ? visual?.svgUrdu || '' : visual?.svgPashto || '');
    }
'''
    chunk=chunk[:pos]+addition+chunk[pos:]
    file.write_text(text[:start]+chunk+text[end:],encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
