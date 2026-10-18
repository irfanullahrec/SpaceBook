import os
from pathlib import Path
ROOT=Path(r'D:\SpaceBook\SpaceBook Web')
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    app=ROOT/'js/app.js'
    s=app.read_text(encoding='utf-8')
    old='grid-template-columns:repeat(3,minmax(0,1fr));gap:.6rem;border:1px solid #9f1239'
    new='grid-template-columns:repeat(${block.columns.length},minmax(0,1fr));gap:.6rem;border:1px solid #9f1239'
    assert s.count(old)==1
    s=s.replace(old,new)
    old='<div style="flex:0 1 180px;">${block.visualFirst === false ? text : figure}</div><div style="flex:1 1 230px;">${block.visualFirst === false ? figure : text}</div>'
    new='<div style="flex:${block.visualFirst === false ? \'1 1 230px\' : \'0 1 180px\'};">${block.visualFirst === false ? text : figure}</div><div style="flex:${block.visualFirst === false ? \'0 1 180px\' : \'1 1 230px\'};">${block.visualFirst === false ? figure : text}</div>'
    assert s.count(old)==1
    s=s.replace(old,new)
    app.write_text(s,encoding='utf-8')
    data=ROOT/'js/data_phys.js'
    s=data.read_text(encoding='utf-8')
    old='''      if (fragment.sourceLayout) {
        const offset = section.paras.length;
        section.sourceLayout ||= [];
        section.sourceLayout.push(...fragment.sourceLayout.map(block => ({...block, indices: (block.indices || []).map(index => index + offset), ...(block.columns ? {columns: block.columns.map(column => column.map(index => index + offset))} : {})})));
'''
    new='''      const continues = fragment.continuesPreviousParagraph && section.paras.length && fragment.paras.length;
      if (continues) {
        const previous = section.paras.at(-1), continuation = fragment.paras[0];
        for (const field of ['text', 'urdu', 'pashto']) previous[field] += ' ' + continuation[field];
        previous.continuedOnPdfPage = page.pdfPage;
      }
      if (fragment.sourceLayout) {
        const offset = section.paras.length - (continues ? 1 : 0);
        section.sourceLayout ||= [];
        section.sourceLayout.push(...fragment.sourceLayout.filter(block => !(continues && block.indices?.length === 1 && block.indices[0] === 0)).map(block => ({...block, indices: (block.indices || []).map(index => index + offset), ...(block.columns ? {columns: block.columns.map(column => column.map(index => index + offset))} : {})})));
'''
    assert s.count(old)==1
    s=s.replace(old,new)
    old='      section.paras.push(...fragment.paras);'
    new='      section.paras.push(...fragment.paras.slice(continues ? 1 : 0).map(para => typeof para === \'string\' ? para : {...para}));'
    assert s.count(old)==1
    data.write_text(s.replace(old,new),encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
print('Saved minimal Class 9 source paragraph-continuation and proportional layout corrections.')
