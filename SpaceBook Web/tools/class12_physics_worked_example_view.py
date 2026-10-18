from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: source worked examples in concepts view'); os.close(fd)
try:
    path=ROOT/'js/app.js'; text=path.read_bytes().decode('utf-8')
    newline='\r\n' if '\r\n' in text else '\n'
    start=text.index('function renderScienceConceptsTab(')
    end=text.index(newline+'function ',start+1)
    segment=text[start:end]
    old="${subjKey === 'phys' ? renderClass10PhysicsWorkedExamples(ch) : ''}"
    new=old+newline+"      ${subjKey === 'phys' && typeof PHYS_12_DATA !== 'undefined' && PHYS_12_DATA.includes(ch) ? renderClass12PhysicsWorkedExamples(ch) : ''}"
    assert segment.count(old)==1
    segment=segment.replace(old,new)
    helper='''function renderClass12PhysicsWorkedExamples(ch) {
  const sourceLessons = {
    'textbook-example-1': ['phys12-front-example111','phys12-front-solution111'],
    'textbook-example-2': ['phys12-front-example112-start','phys12-front-example112-solution'],
    'textbook-example-3': ['phys12-front-example113']
  };
  return (ch.workedExamples || []).filter(example => sourceLessons[example.id]).map((example, index) =>
    `<details class="physics-source-worked-example" style="margin:1rem 0;padding:1rem;border:1px solid #cbd5e1;border-radius:8px;">
      <summary>${sanitize(example.title)} — textbook worked example</summary>
      ${sourceLessons[example.id].map((id, part) => {
        const section = ch.sections.find(section => section.id === id);
        return section ? renderScienceSourceLayout(section, getScienceSectionParagraphsWithTranslations(section,ch,'phys'),'en',`example-${index}-${part}`) : '';
      }).join('')}
    </details>`).join('');
}

'''.replace('\n',newline)
    path.write_bytes((text[:start]+helper+segment+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
