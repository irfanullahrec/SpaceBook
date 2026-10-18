import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 original source language\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    start=text.index('function getScienceSectionParagraphsWithTranslations(')
    end=text.index('\nfunction switchScienceLessonSubTab(',start)
    chunk=text[start:end]
    old="      pashto: p.pashto || p.ps || ''"
    new="      pashto: p.pashto || p.ps || '',\n      ...(p.sourceLanguage ? {sourceLanguage: p.sourceLanguage, english: p.english || p.en || ''} : {})"
    assert old in chunk
    text=text[:start]+chunk.replace(old,new,1)+text[end:]
    start=text.index('function renderScienceSourceLayout(')
    end=text.index('\nfunction renderClass9PhysicsFrontMatterBlocks(',start)
    chunk=text[start:end]
    old="    return result;\n  };"
    new='''    const sourceLanguage = paras[indices[0]]?.sourceLanguage;
    if ((sourceLanguage === 'ar' || sourceLanguage === 'ur') && indices.length === 1) {
      const english = paras[indices[0]]?.english;
      if (english) result = result.replace(/data-en="[^"]*"/g, () => `data-en="${sanitize(english)}" data-source-language="${sourceLanguage}"`);
      return `<span lang="${sourceLanguage}" dir="rtl" style="display:block;text-align:right;">${result}</span>`;
    }
    return result;
  };'''
    assert old in chunk
    chunk=chunk.replace(old,new,1)
    anchor="    if (block.type === 'list')"
    insertion='''    if (block.type === 'quotation') return `<blockquote style="border:1px solid #9f1239;border-radius:8px;padding:.8rem;margin:1rem 0;">${indices.map(index => `<p>${reading([index], `${blockIndex}-${index}`)}</p>`).join('')}</blockquote>`;
    if (block.type === 'parallelPhrases') return `<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.6rem;border:1px solid #9f1239;border-radius:8px;padding:.6rem;">${block.columns.map((column, col) => `<div>${column.map(index => `<p>${reading([index], `${blockIndex}-${col}-${index}`)}</p>`).join('')}</div>`).join('')}</div>`;
'''
    assert anchor in chunk
    chunk=chunk.replace(anchor,insertion+anchor,1)
    text=text[:start]+chunk+text[end:]
    start=text.index('function renderScienceLessonSubContent(')
    end=text.index('\nfunction renderScienceOrHumanitiesLessons(',start)
    chunk=text[start:end]
    chunk=chunk.replace('🇬🇧 English\n',"${sec.paras?.some(para => para.sourceLanguage && para.sourceLanguage !== 'en') ? '📖 Original' : '🇬🇧 English'}\n",1)
    old='English Original (Hover for Word Meaning • Click Sentence for Translation):'
    new="${sec.paras?.some(para => para.sourceLanguage && para.sourceLanguage !== 'en') ? 'Original Textbook Text (English • اردو • العربية)' : 'English Original'} (Hover for Word Meaning • Click Paragraph for Translation):"
    assert old in chunk
    chunk=chunk.replace(old,new,1)
    text=text[:start]+chunk+text[end:]
    file.write_text(text,encoding='utf-8')
    file=ROOT/'js/data_phys.js'
    text=file.read_text(encoding='utf-8')
    anchor="indices: (block.indices || []).map(index => index + offset)"
    new="indices: (block.indices || []).map(index => index + offset), ...(block.columns ? {columns: block.columns.map(column => column.map(index => index + offset))} : {})"
    assert anchor in text
    file.write_text(text.replace(anchor,new,1),encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
