from pathlib import Path
import os
ROOT=Path(__file__).resolve().parents[1]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
os.write(fd,b'class12: reviewed exercise view'); os.close(fd)
try:
    path=ROOT/'js/app.js'; text=path.read_bytes().decode('utf-8')
    newline='\r\n' if '\r\n' in text else '\n'
    start=text.index('function renderSubjectExerciseTab(')
    end=text.index(newline+'function ',start+1)
    segment=text[start:end]
    segment=segment.replace("  const ex =", "  const reviewedPhysics = subjKey === 'phys' && typeof PHYS_12_DATA !== 'undefined' && PHYS_12_DATA.includes(ch);"+newline+"  const ex =",1)
    segment=segment.replace('✍️ Solved Textbook Exercises',"✍️ ${reviewedPhysics ? 'Textbook Exercises — Source Review' : 'Solved Textbook Exercises'}",1)
    segment=segment.replace('100% Verbatim Textbook Matched Solved Solutions for KPK Board',"${reviewedPhysics ? 'Review in progress. Reviewed source questions appear below; source defects are identified separately.' : '100% Verbatim Textbook Matched Solved Solutions for KPK Board'}",1)
    needle='${categories.length > 1 ?'
    assert segment.count(needle)==1
    segment=segment.replace(needle,"${reviewedPhysics ? renderClass12PhysicsSourceExercises(ch) : ''}"+newline+"      "+needle,1)
    helper='''function renderClass12PhysicsSourceExercises(ch) {
  return (ch.exercises || []).filter(item => ['assignment-11-1','quiz-printers-11'].includes(item.id)).map((item,index) => {
    const section = ch.sections.find(section => section.id === (item.id === 'assignment-11-1' ? 'phys12-front-assignment111' : 'phys12-front-inkjet13'));
    if (!section) return '';
    const source = item.id === 'assignment-11-1' ? section : {...section,sourceLayout: [{type:'paragraph',indices:[2]}],diagramSvg:''};
    return `<details class="physics-source-exercise" style="margin:1rem 0;padding:1rem;border:1px solid #cbd5e1;border-radius:8px;" open><summary>${sanitize(item.title)}</summary>${renderScienceSourceLayout(source,getScienceSectionParagraphsWithTranslations(section,ch,'phys'),'en',`exercise-${index}`)}</details>`;
  }).join('');
}

'''.replace('\n',newline)
    path.write_bytes((text[:start]+helper+segment+text[end:]).encode('utf-8'))
finally:
    lock.unlink()
