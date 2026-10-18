from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: synchronized Physics main lesson layout'); os.close(fd)
try:
    path=ROOT/'js/app.js'; text=path.read_bytes().decode('utf-8')
    newline='\r\n' if '\r\n' in text else '\n'
    start=text.index('function renderScienceOrHumanitiesLessons(')
    end=text.index(newline+'function ',start+1)
    segment=text[start:end]
    old="const contentStr = t.content || t.text || t.theory || t.urduTranslation || t.arabic || (Array.isArray(t.paras) ? t.paras.join('\\n\\n') : '') || 'Detailed textbook theory and explanation.';"
    new="const contentStr = subjKey === 'phys' && t.id?.startsWith('phys12-front-') && t.sourceLayout ? renderScienceSourceLayout(t, getScienceSectionParagraphsWithTranslations(t,ch,subjKey), 'en', idx) : (t.content || t.text || t.theory || t.urduTranslation || t.arabic || (Array.isArray(t.paras) ? t.paras.join('\\n\\n') : '') || 'Detailed textbook theory and explanation.');"
    assert segment.count(old)==1
    path.write_bytes((text[:start]+segment.replace(old,new)+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
