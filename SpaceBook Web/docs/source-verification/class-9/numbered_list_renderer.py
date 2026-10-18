import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 source numbered steps\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    start=text.index('function renderScienceSourceLayout(')
    end=text.index('\nfunction renderClass9PhysicsFrontMatterBlocks(',start)
    chunk=text[start:end]
    anchor="    if (block.type === 'list')"
    new='''    if (block.type === 'numberedList') return `<ol style="list-style:none;margin:.6rem 0 1rem;padding-inline-start:.5rem;">${indices.map(index => `<li style="margin:.3rem 0;">${reading([index], `${blockIndex}-${index}`)}</li>`).join('')}</ol>`;
'''
    assert anchor in chunk
    chunk=chunk.replace(anchor,new+anchor,1)
    file.write_text(text[:start]+chunk+text[end:],encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
