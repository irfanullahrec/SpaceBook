import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 preserve page structure\n')
    file=ROOT/'js/data_phys.js'
    text=file.read_text(encoding='utf-8')
    marker=text.index('// Agent 1 sequential Class 9 Physics source review\n')
    anchor='      const section = sections.get(fragment.code);\n      section.paras.push(...fragment.paras);'
    pos=text.index(anchor,marker)
    replacement='''      const section = sections.get(fragment.code);
      if (fragment.sourceLayout) {
        const offset = section.paras.length;
        section.sourceLayout ||= [];
        section.sourceLayout.push(...fragment.sourceLayout.map(block => ({...block, indices: (block.indices || []).map(index => index + offset)})));
      }
      if (fragment.headingUrdu) section.headingUrdu = fragment.headingUrdu;
      if (fragment.headingPashto) section.headingPashto = fragment.headingPashto;
      section.paras.push(...fragment.paras);'''
    file.write_text(text[:pos]+text[pos:].replace(anchor,replacement,1),encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
