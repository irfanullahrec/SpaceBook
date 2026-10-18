import os
from pathlib import Path
ROOT=Path(r'D:\SpaceBook\SpaceBook Web');lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    app=ROOT/'js/app.js';s=app.read_text(encoding='utf-8')
    old="      const grouped = translation.headerGroups && translation.subHeaders;"
    new="""      const grouped = translation.headerGroups && translation.subHeaders;
      const sourceCell = cell => {
        if (!cell || typeof cell !== 'object' || !cell.blockId) return sanitize(cell);
        const item = sec.sourceBlocks?.find(item => item.id === cell.blockId);
        const svg = lang === 'en' ? item?.svg || '' : lang === 'ur' ? item?.svgUrdu || '' : item?.svgPashto || '';
        return `<div style="max-width:${Math.round(520 * (item?.sourceWidthRatio || .2))}px;">${svg.replace(/<svg\\b/, '<svg style="display:block;width:100%;height:auto;"')}</div>`;
      };"""
    assert s.count(old)==1;s=s.replace(old,new)
    old="const headers = (grouped ?"
    new="const headers = table.noHeader ? '' : (grouped ?"
    assert s.count(old)==1;s=s.replace(old,new)
    old='<div style="overflow-x:auto;margin:1rem 0;"><table class="diff-table"><thead>${headers}'
    new='<div style="overflow-x:auto;margin:1rem 0;${table.sourceWidthRatio ? `max-width:${Math.round(520 * table.sourceWidthRatio)}px;` : \'\'}"><table class="diff-table"><thead>${headers}'
    assert s.count(old)==1;s=s.replace(old,new)
    old='row.map(cell => `<td>${sanitize(cell)}</td>`).join(\'\')'
    new='row.map(cell => `<td>${sourceCell(cell)}</td>`).join(\'\')'
    assert s.count(old)==1;s=s.replace(old,new)
    app.write_text(s,encoding='utf-8')
finally:
    os.close(fd);lock.unlink()
print('Saved scoped semantic source-table equation cells and optional original headerless layout.')
