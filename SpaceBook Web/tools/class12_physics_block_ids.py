from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: block visual unique ids');os.close(fd)
try:
    path=ROOT/'js/app.js';text=path.read_bytes().decode('utf-8')
    start=text.index('function renderScienceSourceLayout(')
    end=text.index('\nfunction ',start+1)
    segment=text[start:end]
    old="if (block.type === 'visual' && block.blockId && sec.sourceBlocks) {"
    new="if (block.type === 'visual' && block.blockId && sec.sourceBlocks && !sec.id?.startsWith('phys12-front-')) {"
    assert segment.count(old)==1
    segment=segment.replace(old,new)
    path.write_bytes((text[:start]+segment+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
