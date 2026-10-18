import json
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
page=json.loads((OUT/'physics-page-007.json').read_text(encoding='utf-8'))
p=page['sections'][0]['paras'][5]
page['definitions']=[dict(term='Physics',defn=p['text'],definition=p['text'],urdu=p['urdu'],pashto=p['pashto'],sourcePdfPage=7,sourcePrintedPage=2)]
(OUT/'physics-page-007.json').write_text(json.dumps(page,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 canonical lesson and table paths\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    anchor='function renderTopicsAccordion(ch) {\n'
    replacement=anchor+"  if (state.selectedClass === 'cls9' && DATA.physChapters?.includes(ch)) return renderScienceLessonSubContent('phys', ch, 'translations');\n"
    assert anchor in text
    text=text.replace(anchor,replacement,1)
    start=text.index('function renderScienceSourceLayout(')
    end=text.index('\nfunction renderClass9PhysicsFrontMatterBlocks(',start)
    chunk=text[start:end]
    anchor="    if (block.type === 'table') {"
    insertion='''    if (block.type === 'sourceDataTable') {
      const table = sec.sourceBlocks?.find(item => item.id === block.tableId);
      if (!table) return '';
      const translation = lang === 'en' ? table : table.translations?.find(item => item.language === (lang === 'ur' ? 'اردو' : 'پښتو'));
      if (!translation) return '';
      return `<div style="overflow-x:auto;margin:1rem 0;"><table class="diff-table"><thead><tr>${translation.headers.map(header => `<th scope="col">${sanitize(header)}</th>`).join('')}</tr></thead><tbody>${translation.rows.map(row => `<tr>${row.map(cell => `<td>${sanitize(cell)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
    }
'''
    assert anchor in chunk
    chunk=chunk.replace(anchor,insertion+anchor,1)
    text=text[:start]+chunk+text[end:]
    # Preserve the default English label and class-12 source-label override.
    bad="((sec.paras?.some(para => para.sourceLanguage && para.sourceLanguage !== 'en') ? 'Original Textbook Text (English • اردو • العربية)' : 'English Original') + ' (Hover for Word Meaning • Click Paragraph for Translation):')"
    good="(state.selectedClass === 'cls9' && subjKey === 'phys' && sec.paras?.some(para => para.sourceLanguage && para.sourceLanguage !== 'en') ? 'Original Textbook Text (English • اردو • العربية) (Click Paragraph for Translation):' : 'English Original (Hover for Word Meaning • Click Sentence for Translation):')"
    assert bad in text
    text=text.replace(bad,good,1)
    file.write_text(text,encoding='utf-8')
    file=ROOT/'js/data_phys.js'
    text=file.read_text(encoding='utf-8')
    marker=text.index('// Agent 1 sequential Class 9 Physics source review\n')
    anchor='  for (const page of reviewed) {\n'
    pos=text.index(anchor,marker)
    insertion='''  for (const page of reviewed) {
    for (const definition of page.definitions || []) {
      const existing = (chapter.definitions || []).find(item => item.term === definition.term);
      if (existing) Object.assign(existing, definition, {def: definition.defn || definition.definition});
      else { chapter.definitions ||= []; chapter.definitions.push({...definition, def: definition.defn || definition.definition}); }
    }
'''
    text=text[:pos]+text[pos:].replace(anchor,insertion,1)
    file.write_text(text,encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
