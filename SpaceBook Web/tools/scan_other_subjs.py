import sys, os, zipfile, xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

def get_paras(docx_p):
    files = sorted([os.path.join(docx_p, f) for f in os.listdir(docx_p) if f.endswith('.docx')])
    all_paras = []
    for f in files:
        with zipfile.ZipFile(f) as z:
            tree = ET.fromstring(z.read('word/document.xml'))
            for p_tag in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
                texts = [t.text for t in p_tag.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
                if texts:
                    txt = ''.join(texts).strip()
                    if txt and 'camscanner' not in txt.lower():
                        all_paras.append(txt)
    return all_paras

for name, folder in [
    ('Civics', r'D:\SpaceBook\Books\12th\12th Civics\Word'),
    ('Economics', r'D:\SpaceBook\Books\12th\12th Economics\Word'),
    ('HPE', r'D:\SpaceBook\Books\12th\12th HPE\Word'),
    ('Islamiat Ikhtiari', r'D:\SpaceBook\Books\12th\12th Islamiat Ikhtiari\Word'),
    ('Islamic History', r'D:\SpaceBook\Books\12th\12th Islamic History\Word'),
    ('Mutalia e Quran', r'D:\SpaceBook\Books\12th\12th Mutalia e Quran\Word'),
]:
    p = get_paras(folder)
    print(f'=== {name} : {len(p)} paras ===')
    for i in range(min(140, len(p))):
        line = p[i]
        if any(w in line for w in ['باب', 'سبق', 'فہرست', 'مضامین', 'عنوان', 'Chapter', 'Unit']):
            print(f'   {i}: {line[:70]}')
