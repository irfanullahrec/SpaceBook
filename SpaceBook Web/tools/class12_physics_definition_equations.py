from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: inline notation in Physics definitions'); os.close(fd)
try:
    path=ROOT/'js/app.js'; text=path.read_bytes().decode('utf-8')
    newline='\r\n' if '\r\n' in text else '\n'
    start=text.index('function renderScienceConceptsTab(')
    end=text.index(newline+'function ',start+1)
    segment=text[start:end]
    old="${d.def || d.definition || d.desc || d.content || ''}"
    new="${subjKey === 'phys' && typeof PHYS_12_DATA !== 'undefined' && PHYS_12_DATA.includes(ch) && typeof SpaceBookLessonMath !== 'undefined' ? SpaceBookLessonMath.mathParts(d.def || d.definition || d.desc || d.content || '').map(part => part.latex === undefined ? sanitize(part.text) : SpaceBookLessonMath.renderMath(part)).join('') : (d.def || d.definition || d.desc || d.content || '')}"
    assert segment.count(old)==1
    path.write_bytes((text[:start]+segment.replace(old,new)+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
