import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 select source visuals\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    old="    if (block.type === 'visual') return lang === 'en' ? (sec.diagramSvg || '')"
    new="    if (block.type === 'visual') return lang === 'en' ? (block.blockId && sec.sourceBlocks ? (sec.sourceBlocks.find(item => item.id === block.blockId)?.svg || '') : (sec.diagramSvg || ''))"
    assert old in text
    file.write_text(text.replace(old,new,1),encoding='utf-8')
    file=ROOT/'js/data_phys.js'
    text=file.read_text(encoding='utf-8')
    old='''        section.sourceLayout.push(...fragment.sourceLayout.map(block => ({...block, indices: (block.indices || []).map(index => index + offset)})));
      }
      if (fragment.headingUrdu)'''
    new='''        section.sourceLayout.push(...fragment.sourceLayout.map(block => ({...block, indices: (block.indices || []).map(index => index + offset)})));
      } else if (section.sourceLayout) {
        const offset = section.paras.length;
        section.sourceLayout.push(...fragment.paras.map((_, index) => ({type: 'paragraph', indices: [offset + index]})));
        for (const block of fragment.blocks || []) {
          if (block.svg && block.id) section.sourceLayout.push({type: 'visual', blockId: block.id});
        }
      }
      if (fragment.headingUrdu)'''
    assert old in text
    file.write_text(text.replace(old,new,1),encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
