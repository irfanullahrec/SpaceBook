"""Opt newly source-checked Class12 records into the existing source renderer."""
from class12_source_review import ROOT, shared_class_data_lock

with shared_class_data_lock():
    path=ROOT/'js/app.js'
    source=path.read_text(encoding='utf-8')
    start=source.index('function renderScienceSourceLayout(')
    end=source.index('\nfunction ',start+10)
    block=source[start:end]
    old="sec.id?.startsWith('phys12-')"
    new="(sec.sourceClass12Physics === true || sec.id?.startsWith('phys12-'))"
    if new not in block:
        assert block.count(old)==6, block.count(old)
        block=block.replace(old,new)
        source=source[:start]+block+source[end:]
    old="subjKey === 'phys' && t.id?.startsWith('phys12-') && t.sourceLayout"
    new="subjKey === 'phys' && (t.sourceClass12Physics === true || t.id?.startsWith('phys12-')) && t.sourceLayout"
    if old in source:
        assert source.count(old)==1
        source=source.replace(old,new)
    # Source tables need the same equation and paired-translation reader as prose.
    start=source.index('function renderScienceSourceLayout(')
    end=source.index('\nfunction ',start+10)
    block=source[start:end]
    if 'const sourceCellValue =' not in block:
        old="  const reading = (indices, key) => {\n    const text = indices.map(index => paras[index]?.[field] || '').join(' ');"
        new="  const sourceCellValue = (index, language, cellIndex) => cellIndex === undefined ? (paras[index]?.[language] || '') : String(paras[index]?.[language] || '').split(' — ')[cellIndex] || '';\n  const reading = (indices, key, cellIndex) => {\n    const text = indices.map(index => sourceCellValue(index, field, cellIndex)).join(' ');"
        assert old in block
        block=block.replace(old,new)
        for language in ('urdu','pashto'):
            old=f"indices.map(index => paras[index]?.{language} || '').join(' ')"
            new=f"indices.map(index => sourceCellValue(index, '{language}', cellIndex)).join(' ')"
            assert old in block
            block=block.replace(old,new)
        anchor="    if (block.type === 'table') {\n"
        branch="""    if (block.type === 'table' && sec.sourceClass12Physics === true) {
      const row = (index, rowIndex, header) => {
        const cells = sec.sourceTableRows[index];
        return `<tr>${cells.map((_, column) => header
          ? `<th scope="col" style="border:1px solid #94a3b8;padding:.45rem;text-align:start;">${reading([index], `${blockIndex}-${rowIndex}-${column}`, column)}</th>`
          : `<td style="border:1px solid #94a3b8;padding:.45rem;">${reading([index], `${blockIndex}-${rowIndex}-${column}`, column)}</td>`).join('')}</tr>`;
      };
      return `<div style="overflow-x:auto;margin:1rem 0;"><table style="border-collapse:collapse;width:100%;"><thead>${row(indices[0],0,true)}</thead><tbody>${indices.slice(1).map((index,rowIndex)=>row(index,rowIndex+1,false)).join('')}</tbody></table></div>`;
    }
"""
        assert block.count(anchor)==1
        block=block.replace(anchor,branch+anchor)
        source=source[:start]+block+source[end:]
    start=source.index('function renderClass12PhysicsSourceExercises(')
    end=source.index('\nfunction ',start+10)
    block=source[start:end]
    if 'item.sourceSectionId' not in block:
        block=block.replace(".filter(item => ['assignment-11-1'", ".filter(item => item.sourceSectionId || ['assignment-11-1'")
        old="section.id === (({'assignment-11-1'"
        new="section.id === (item.sourceSectionId || ({'assignment-11-1'"
        assert old in block
        block=block.replace(old,new)
        old="    const source = item.id !== 'quiz-printers-11' ? section : {...section,sourceLayout: [{type:'paragraph',indices:[2]}],diagramSvg:''};"
        new="""    const source = item.sourceSectionId ? {...section,sourceLayout: section.sourceLayout.flatMap(block => {
      const indices = (block.indices || []).filter(index => !item.sourceIndices || item.sourceIndices.includes(index));
      return indices.length ? [{...block,indices}] : [];
    })} : item.id !== 'quiz-printers-11' ? section : {...section,sourceLayout: [{type:'paragraph',indices:[2]}],diagramSvg:''};"""
        assert old in block
        block=block.replace(old,new)
        source=source[:start]+block+source[end:]
    start=source.index('function renderClass12PhysicsWorkedExamples(')
    end=source.index('\nfunction ',start+10)
    block=source[start:end]
    if 'example.sourceSectionId' not in block:
        old=".filter(example => sourceLessons[example.id])"
        new=".filter(example => example.sourceSectionId || sourceLessons[example.id]?.some(id => ch.sections.some(section => section.id === id)))"
        assert old in block
        block=block.replace(old,new).replace('sourceLessons[example.id].map((id, part) => {','(example.sourceSectionId ? [example.sourceSectionId] : sourceLessons[example.id]).map((id, part) => {')
        old="        return section ? renderScienceSourceLayout(section, getScienceSectionParagraphsWithTranslations(section,ch,'phys'),'en',`example-${index}-${part}`) : '';"
        new="""        if (!section) return '';
        const source = example.sourceSectionId ? {...section,sourceLayout: section.sourceLayout.flatMap(block => {
          const indices = (block.indices || []).filter(index => !example.sourceIndices || example.sourceIndices.includes(index));
          return indices.length ? [{...block,indices}] : [];
        })} : section;
        return renderScienceSourceLayout(source, getScienceSectionParagraphsWithTranslations(section,ch,'phys'),'en',`example-${index}-${part}`);"""
        assert old in block
        block=block.replace(old,new)
        source=source[:start]+block+source[end:]
    start=source.index('function renderClass12PhysicsWorkedExamples(')
    end=source.index('\nfunction ',start+10)
    block=source[start:end]
    if 'example.sourceParts' not in block:
        block=block.replace('.filter(example => example.sourceSectionId ||', '.filter(example => example.sourceParts?.length || example.sourceSectionId ||')
        old="(example.sourceSectionId ? [example.sourceSectionId] : sourceLessons[example.id]).map((id, part) => {"
        new="(example.sourceParts || (example.sourceSectionId ? [{sectionId:example.sourceSectionId,indices:example.sourceIndices}] : sourceLessons[example.id])).map((sourcePart, part) => {\n        const id = typeof sourcePart === 'string' ? sourcePart : sourcePart.sectionId;"
        assert old in block
        block=block.replace(old,new)
        block=block.replace('const source = example.sourceSectionId ?', "const source = typeof sourcePart !== 'string' ?")
        block=block.replace('!example.sourceIndices || example.sourceIndices.includes(index)', '!sourcePart.indices || sourcePart.indices.includes(index)')
        source=source[:start]+block+source[end:]
    old="(ch.formulas || []).filter(item => item.id?.startsWith('phys12-'))"
    new="(ch.formulas || []).filter(item => item.sourceClass12Physics === true || item.id?.startsWith('phys12-'))"
    if old in source:
        assert source.count(old)==1
        source=source.replace(old,new)
    old="subjKey === 'phys' && f.id?.startsWith('phys12-') && f.latex"
    new="subjKey === 'phys' && (f.sourceClass12Physics === true || f.id?.startsWith('phys12-')) && f.latex"
    if old in source:
        assert source.count(old)==1
        source=source.replace(old,new)
    temporary=path.with_suffix('.js.class12-tmp')
    temporary.write_text(source,encoding='utf-8')
    temporary.replace(path)
print('Scoped Class12 source-rendering opt-in saved.')
