# -*- coding: utf-8 -*-
import zipfile, xml.etree.ElementTree as ET, sys, re, os, json
sys.stdout.reconfigure(encoding='utf-8')

D = r"D:\SpaceBook\Books\12th\12th Biology\Word"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def p_text(p):
    return ''.join(t.text for t in p.iter(NS + 't') if t.text).strip()

def p_style(p):
    pPr = p.find(NS + 'pPr')
    if pPr is not None:
        s = pPr.find(NS + 'pStyle')
        if s is not None:
            return s.get(NS + 'val', '')
    return ''

def p_bold(p):
    for r in p.iter(NS + 'r'):
        rPr = r.find(NS + 'rPr')
        if rPr is not None and rPr.find(NS + 'b') is not None:
            v = rPr.find(NS + 'b').get(NS + 'val', '1')
            if v != '0':
                return True
    return False

files = sorted(f for f in os.listdir(D) if f.endswith('.docx') and not f.startswith('~$'))
paras = []
for fn in files:
    with zipfile.ZipFile(os.path.join(D, fn)) as z:
        root = ET.fromstring(z.read('word/document.xml'))
    for p in root.iter(NS + 'p'):
        t = p_text(p)
        if t:
            paras.append({'t': t, 'style': p_style(p), 'bold': p_bold(p), 'file': fn})

print('TOTAL paras:', len(paras))
print('styles:', sorted(set(x['style'] for x in paras))[:30])
print('bold count:', sum(1 for x in paras if x['bold']))

# Style distribution sample
from collections import Counter
print('style counts:', Counter(x['style'] for x in paras).most_common(10))

# Find chapter headers
for i, x in enumerate(paras):
    if re.match(r'^Chapter\s+\d+', x['t'], re.I) and len(x['t']) < 80:
        print(i, repr(x['t']), 'style=', x['style'], 'bold=', x['bold'])

# Characterize short lines (likely labels)
shorts = [x for x in paras if len(x['t']) < 40]
print('short lines:', len(shorts))
print('sample shorts:', [s['t'] for s in shorts[:60]])

# Watermark / noise patterns
noise = Counter()
for x in paras:
    t = x['t'].lower()
    if 'inqilab' in t: noise['inqilab'] += 1
    elif 'fig:' in t: noise['fig'] += 1
    elif 'table:' in t: noise['table'] += 1
    elif 'camscanner' in t: noise['camscanner'] += 1
    elif 'mdcat' in t or 'youseer' in t or 'future' in t: noise['mdcat'] += 1
    elif re.fullmatch(r'\d{1,4}', x['t']): noise['pagenum'] += 1
    elif 'chapter' in t and len(x['t']) < 30: noise['chapterhdr'] += 1
print('noise:', noise)

# bold short lines = probable headings
h = [x for x in paras if x['bold'] and len(x['t']) < 90]
print('bold short:', len(h))
print([x['t'] for x in h[:40]])
