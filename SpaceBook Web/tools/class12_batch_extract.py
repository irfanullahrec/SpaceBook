"""Batch extract selectable text and render a contiguous Class 12 source PDF range."""
from pathlib import Path
import argparse
import os
import shutil
import pymupdf

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
OUT=ROOT/'tmp/class12-review'
TESSERACT_DIR=Path(r'C:\Program Files\Tesseract-OCR')
if (TESSERACT_DIR/'tesseract.exe').exists():
    os.environ['PATH']=str(TESSERACT_DIR)+os.pathsep+os.environ.get('PATH','')
    tessdata=TESSERACT_DIR/'tessdata'
    if (tessdata/'eng.traineddata').exists():
        os.environ['TESSDATA_PREFIX']=str(tessdata)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--start',type=int,required=True,help='First one-based PDF page')
    parser.add_argument('--end',type=int,required=True,help='Last one-based PDF page')
    parser.add_argument('--scale',type=float,default=2.0)
    parser.add_argument('--text-only',action='store_true',help='Extract/OCR without rerendering existing page images')
    args=parser.parse_args()
    if args.start<1 or args.end<args.start: raise ValueError('Use an increasing, one-based contiguous range')
    OUT.mkdir(parents=True,exist_ok=True)
    blocks=[]
    with pymupdf.open(SOURCE) as doc:
        if args.end>len(doc): raise ValueError(f'PDF has only {len(doc)} pages')
        for number in range(args.start,args.end+1):
            page=doc[number-1]
            text=page.get_text('text',sort=True).strip()
            method='embedded text'
            if len(text)<32:
                try:
                    text=page.get_textpage_ocr(language='eng',dpi=220).extractText(sort=True).strip()
                    method='Tesseract OCR fallback' if shutil.which('tesseract') else 'OCR fallback'
                except Exception as exc:
                    method=f'text unavailable ({type(exc).__name__})'
            blocks.append(f'===== PDF PAGE {number} ({method}) =====\n{text}\n')
            if not args.text_only:
                page.get_pixmap(matrix=pymupdf.Matrix(args.scale,args.scale),alpha=False).save(OUT/f'page{number:03}.png')
    target=OUT/f'extract-{args.start:03}-{args.end:03}.txt'
    target.write_text('\n'.join(blocks),encoding='utf-8')
    print(f'Extracted/rendered {args.end-args.start+1} consecutive pages: {target}')

if __name__=='__main__': main()
