import os, zipfile, xml.etree.ElementTree as ET, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')
docx_p = r"D:\SpaceBook\Books\12th\12th Urdu\Word"
files = sorted([os.path.join(docx_p, f) for f in os.listdir(docx_p) if f.endswith('.docx')])

all_paras = []
for f in files:
    with zipfile.ZipFile(f) as z:
        xml_content = z.read('word/document.xml')
        tree = ET.fromstring(xml_content)
        for p_tag in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p_tag.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                txt = ''.join(texts).strip()
                if txt and 'camscanner' not in txt.lower():
                    all_paras.append(txt)

print('Urdu 12 total paras:', len(all_paras))
for i in range(min(150, len(all_paras))):
    p = all_paras[i]
    if any(k in p for k in ['فہرست', 'سبق', 'نظم', 'غزل', 'باب', 'حصہ', 'عنوان']):
        print(f"{i}: {p}")
