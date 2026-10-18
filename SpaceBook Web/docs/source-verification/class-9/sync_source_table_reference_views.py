import os
from pathlib import Path
ROOT=Path(r'D:\SpaceBook\SpaceBook Web');lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    app=ROOT/'js/app.js';s=app.read_text(encoding='utf-8')
    old='  const tblsHtml = tbls.length > 0 ? tbls.map(tbl => `'
    new='''  const sourceReferenceCell = cell => {
    if (!cell || typeof cell !== 'object' || !cell.blockId) return cell;
    const block = (ch.sections || []).flatMap(section => section.sourceBlocks || []).find(block => block.id === cell.blockId);
    return `<div style="max-width:${Math.round(520 * (block?.sourceWidthRatio || .2))}px;">${(block?.svg || '').replace(/<svg\\b/, '<svg style="display:block;width:100%;height:auto;"')}</div>`;
  };
  const tblsHtml = tbls.length > 0 ? tbls.map(tbl => `'''
    assert s.count(old)==1;s=s.replace(old,new)
    old='<tr>${(tbl.headers || []).map(h => `<th>${h}</th>`).join("")}</tr>'
    new='${tbl.noHeader ? \'\' : `<tr>${(tbl.headers || []).map(h => `<th>${h}</th>`).join("")}</tr>`}'
    assert s.count(old)==1;s=s.replace(old,new)
    old='${(tbl.rows || []).map(r => `<tr>${r.map(c => `<td>${c}</td>`).join("")}</tr>`).join("")}'
    new='${(tbl.rows || []).map(r => `<tr>${r.map(c => `<td>${sourceReferenceCell(c)}</td>`).join("")}</tr>`).join("")}'
    assert s.count(old)==1;s=s.replace(old,new)
    app.write_text(s,encoding='utf-8')
    data=ROOT/'js/data_phys.js';s=data.read_text(encoding='utf-8')
    old='    section.diagramSvg = section.sourceBlocks.filter(block => block.svg).map(block => block.svg).join(\'\');'
    new='''    const tableCellIds = new Set(section.sourceBlocks.filter(block => block.type === 'dataTable').flatMap(table => table.rows.flat().filter(cell => cell?.blockId).map(cell => cell.blockId)));
    const sourceTableCell = (cell, language = 'en') => {
      if (!cell || typeof cell !== 'object' || !cell.blockId) return cell;
      const block = section.sourceBlocks.find(block => block.id === cell.blockId);
      const svg = language === 'en' ? block?.svg || '' : language === 'اردو' ? block?.svgUrdu || '' : block?.svgPashto || '';
      return `<div style="max-width:${Math.round(520 * (block?.sourceWidthRatio || .2))}px;">${svg.replace(/<svg\\b/, '<svg style="display:block;width:100%;height:auto;"')}</div>`;
    };
    section.diagramSvg = section.sourceBlocks.filter(block => block.svg && !tableCellIds.has(block.id)).map(block => block.svg).join('');'''
    assert s.count(old)==1;s=s.replace(old,new)
    old='table.headers.map(header => `<th>${header}</th>`).join(\'\')'
    new='table.noHeader ? \'\' : table.headers.map(header => `<th>${header}</th>`).join(\'\')'
    assert s.count(old)==1;s=s.replace(old,new)
    old='row.map(cell => `<td>${cell}</td>`).join(\'\')'
    assert s.count(old)==2
    s=s.replace(old,'row.map(cell => `<td>${sourceTableCell(cell)}</td>`).join(\'\')',1)
    s=s.replace(old,'row.map(cell => `<td>${sourceTableCell(cell, translation.language)}</td>`).join(\'\')',1)
    old='translation.headers.map(header => `<th>${header}</th>`).join(\'\')'
    new='table.noHeader ? \'\' : translation.headers.map(header => `<th>${header}</th>`).join(\'\')'
    assert s.count(old)==1;s=s.replace(old,new)
    data.write_text(s,encoding='utf-8')
finally:
    os.close(fd);lock.unlink()
print('Synchronized coded table equations with Physics reference and fallback views.')
