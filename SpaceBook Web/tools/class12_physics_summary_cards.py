from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: source formulas alongside existing overview'); os.close(fd)
try:
    path=ROOT/'js/app.js'; text=path.read_bytes().decode('utf-8')
    newline='\r\n' if '\r\n' in text else '\n'
    start=text.index('function renderScienceOrHumanitiesSummaryTab(')
    end=text.index(newline+'}',start)+len(newline+'}')
    segment=text[start:end]
    old='    return `'+newline+'      <div>'
    new=old+newline+"        ${subjKey === 'phys' && typeof PHYS_12_DATA !== 'undefined' && PHYS_12_DATA.includes(ch) ? renderClass12PhysicsSourceFormulas(ch) : ''}"
    assert segment.count(old)>=1
    segment=segment.replace(old,new,1)
    helper='''function renderClass12PhysicsSourceFormulas(ch) {
  const formulas = (ch.formulas || []).filter(item => item.id?.startsWith('phys12-'));
  if (!formulas.length) return '';
  return `<section class="physics-source-formulas" style="margin-bottom:1.5rem;">
    <h4>Textbook equations from reviewed source pages</h4>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:.75rem;">
      ${formulas.map(item => `<article style="padding:.8rem;border:1px solid #cbd5e1;border-radius:8px;">
        <h5>${sanitize(item.name)}${item.number ? ' ('+sanitize(item.number)+')' : ''}</h5>
        <div style="overflow-x:auto;">${typeof SpaceBookLessonMath !== 'undefined' ? SpaceBookLessonMath.renderMath({latex:item.latex,display:false}) : sanitize(item.formula)}</div>
        <small>PDF page ${sanitize(String(item.sourceReferences?.[0]?.pdfPage || ''))}; printed ${sanitize(String(item.sourceReferences?.[0]?.printedPage || ''))}</small>
      </article>`).join('')}
    </div>
  </section>`;
}

'''.replace('\n',newline)
    path.write_bytes((text[:start]+helper+segment+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
