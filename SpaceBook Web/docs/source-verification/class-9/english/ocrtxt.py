"""Print cached OCR text for PDF pages: python ocrtxt.py 7 14  (marks sidebar column lines with >>)"""
import json, sys, os
def printed_of(n):
    return '?'
import sys; sys.stdout.reconfigure(encoding="utf-8")
a=int(sys.argv[1]); b=int(sys.argv[2]) if len(sys.argv)>2 else a
for n in range(a,b+1):
    f=f'ocr/page-{n:03d}.json'
    if not os.path.exists(f): print(f'--- page {n}: OCR pending'); continue
    d=json.load(open(f,encoding='utf-8'))
    print(f'=== PDF {n} (printed {printed_of(n)}) ===')
    for l in d['lines']:
        tag='>>' if l['x']>900 else '  '
        print(f"{tag}{l['text']}")
