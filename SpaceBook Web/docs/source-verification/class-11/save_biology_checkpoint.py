import json, sys, datetime, re, pathlib
# usage: save_biology_checkpoint.py <lastScan> <chapter> <note>
last=int(sys.argv[1]); chapter=sys.argv[2]; note=sys.argv[3] if len(sys.argv)>3 else ''
src=pathlib.Path(r'D:\SpaceBook\SpaceBook Web\js\bio_11_data.js').read_text(encoding='utf-8')
done=sorted({int(m) for m in re.findall(r"bio11Page\('[^']+',\s*\{\s*scan:\s*(\d+)",src)})
rec={
 'subject':'Biology','class':11,'textbook':'KPTBB Biology Grade XI Test Edition',
 'sourceJpgDir':r'D:\SpaceBook\Books\11th\11th bio\jpg','totalScans':364,
 'sourcePdfs':'bio1-bio9.pdf: image-only Word exports (619x792) of the same scans; boundary scans repeat (bio2 p1=scan41, bio3 p1=scan81, bio4 p1=scan121, bio5 starts at scan151, bio6 p1=scan191, bio7 p1=scan241, bio8 p1=scan291, bio9 p1=scan341). No duplicate or separate edition.',
 'printedPageOffset':'printed page = scan - 3 (scan 4 = printed 1) through at least scan 8',
 'ocrCache':r'docs/source-verification/class-11/biology-ocr/page-NNN.txt (Tesseract eng, supporting aid only)',
 'inspectedAndRecordedScans':done,'lastFullyVerifiedScan':last,'nextScan':last+1,'currentChapter':chapter,
 'missingPages':['No credits/copyright page exists in the scan set.'],
 'updated':datetime.datetime.now().isoformat(timespec='seconds'),'note':note}
pathlib.Path('biology-progress.json').write_text(json.dumps(rec,indent=1,ensure_ascii=False),encoding='utf-8')
print('saved; recorded scans',len(done),'next',last+1)
