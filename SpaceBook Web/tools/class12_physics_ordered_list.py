from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: numbered source dependency list'); os.close(fd)
try:
    path=ROOT/'js/app.js'; text=path.read_bytes().decode('utf-8')
    old="    if (block.type === 'list') return `<ul"
    addition="    if (block.type === 'orderedList' && sec.id?.startsWith('phys12-front-')) return `<ol style=\"list-style:none;padding-inline-start:1.5rem;\">${indices.map(index => `<li>${reading([index],`${blockIndex}-${index}`)}</li>`).join('')}</ol>`;"
    newline='\r\n' if '\r\n' in text else '\n'
    start=text.index('function renderScienceSourceLayout(')
    end=text.index(newline+'function ',start+1)
    segment=text[start:end]
    assert segment.count(old)==1
    path.write_bytes((text[:start]+segment.replace(old,addition+newline+old)+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
