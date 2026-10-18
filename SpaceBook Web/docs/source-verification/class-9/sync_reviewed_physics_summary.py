import os
from pathlib import Path
ROOT=Path(r'D:\SpaceBook\SpaceBook Web');lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    data=ROOT/'js/data_phys.js';s=data.read_text(encoding='utf-8')
    old='  const sourceOrder = [...sections.keys()];'
    new='''  for (const link of reviewed.flatMap(page => page.formulaSourceLinks || [])) {
    const sources = link.blockIds.map(id => {
      const sourcePage = reviewed.find(page => page.sections?.some(section => section.blocks?.some(block => block.id === id)));
      const block = sourcePage?.sections.flatMap(section => section.blocks || []).find(block => block.id === id);
      return {block, sourcePage};
    }).filter(item => item.block);
    if (sources.length !== link.blockIds.length) continue;
    chapter.formulas ||= [];
    let formula = chapter.formulas.find(item => item.name === link.name);
    if (!formula) { formula = {name:link.name}; chapter.formulas.push(formula); }
    formula.formula = sources.map(({block}) => `<div style="max-width:${Math.round(520 * block.sourceWidthRatio)}px;">${block.svg.replace(/<svg\\b/, '<svg style="display:block;width:100%;height:auto;"')}</div>`).join('');
    formula.sourceBlockIds = link.blockIds;
    formula.sourceReferences = sources.map(({sourcePage}) => ({sourcePdf:sourcePage.sourcePdf,pdfPage:sourcePage.pdfPage,printedPage:sourcePage.printedPage}));
    formula.note = sources.map(({sourcePage}) => `Textbook: PDF page ${sourcePage.pdfPage}, printed page ${sourcePage.printedPage}`).join('; ');
  }
  const sourceOrder = [...sections.keys()];'''
    assert s.count(old)==1;s=s.replace(old,new)
    data.write_text(s,encoding='utf-8')
    app=ROOT/'js/app.js';s=app.read_text(encoding='utf-8')
    old='function renderScienceOrHumanitiesSummaryTab(subjKey, ch) {\n'
    new='''function renderScienceOrHumanitiesSummaryTab(subjKey, ch) {
  if (subjKey === 'phys' && state.selectedClass === 'cls9') {
    const keySections = (ch.sections || []).filter(section => /^source-u\\d+-key-points$/.test(section.code));
    if (keySections.length) {
      return `<div class="physics9-source-summary"><h3>Textbook Key Points &amp; Formulas</h3>${keySections.map((section, index) => {
        const pairs = getScienceSectionParagraphsWithTranslations(section, ch, subjKey);
        return `<section>${renderScienceSourceLayout(section,pairs,'en',300+index)}<details><summary>اردو</summary><div dir="rtl">${renderScienceSourceLayout(section,pairs,'ur',300+index)}</div></details><details><summary>پښتو</summary><div dir="rtl">${renderScienceSourceLayout(section,pairs,'ps',300+index)}</div></details></section>`;
      }).join('')}<div>${(ch.formulas || []).map(formula => `<article style="margin:1rem 0;padding:.7rem;border:1px solid #cbd5e1;border-radius:8px;"><h4>${sanitize(formula.name || formula.title || '')}</h4>${formula.formula || ''}<small>${sanitize(formula.note || '')}</small></article>`).join('')}</div></div>`;
    }
  }
'''
    assert s.count(old)==1;s=s.replace(old,new)
    app.write_text(s,encoding='utf-8')
finally:
    os.close(fd);lock.unlink()
print('Summary and formula views now reuse reviewed Class9 Physics source records.')
