import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
lock=ROOT/'tmp/class-content-shared.lock'
fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
try:
    os.write(fd,b'class-9 fresh review evidence status\n')
    file=ROOT/'js/data_phys.js'
    text=file.read_text(encoding='utf-8')
    marker=text.index('// Agent 1 sequential Class 9 Physics source review\n')
    old='  chapter.sourceReview = {complete: reviewed.some(page => page.chapterEnd), lastPdfPage: reviewed.at(-1).pdfPage};'
    pos=text.index(old,marker)
    new='''  const freshReviewed = reviewed.filter(page => page.id?.startsWith('cls9-physics-page-'));
  chapter.sourceReview = {
    complete: freshReviewed.length === reviewed.length && reviewed.some(page => page.chapterEnd) && !freshReviewed.some(page => page.unresolvedItems?.length),
    lastPdfPage: freshReviewed.at(-1)?.pdfPage || 0,
    freshReviewedPdfPages: freshReviewed.map(page => page.pdfPage),
    unresolvedPdfPages: freshReviewed.filter(page => page.unresolvedItems?.length).map(page => page.pdfPage),
    legacyCoverageLastPdfPage: reviewed.at(-1).pdfPage,
    legacyCoverageIsFreshEvidence: false
  };'''
    file.write_text(text[:pos]+text[pos:].replace(old,new,1),encoding='utf-8')
finally:
    os.close(fd)
    lock.unlink()
