import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 original-label syntax correction\n')
    file=ROOT/'js/app.js'
    text=file.read_text(encoding='utf-8')
    bad="'${sec.paras?.some(para => para.sourceLanguage && para.sourceLanguage !== 'en') ? 'Original Textbook Text (English • اردو • العربية)' : 'English Original'} (Hover for Word Meaning • Click Paragraph for Translation):'"
    good="((sec.paras?.some(para => para.sourceLanguage && para.sourceLanguage !== 'en') ? 'Original Textbook Text (English • اردو • العربية)' : 'English Original') + ' (Hover for Word Meaning • Click Paragraph for Translation):')"
    assert bad in text
    file.write_text(text.replace(bad,good,1),encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
