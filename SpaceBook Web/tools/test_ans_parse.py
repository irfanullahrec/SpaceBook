
# build_math_dataset.py
import docx, re, json

docs = {}
for i in [1, 2, 3, 4, 5]:
    d = docx.Document(f'D:/SpaceBook/Books/4th/4th/Math books 4 KPK_JPGs/word/maths{i}.docx')
    docs[i] = [p.text.strip() for p in d.paragraphs if p.text.strip()]

ans_lines = docs[5][380:]

def clean(p):
    if not p: return ''
    if any(m in p.lower() for m in ['awaz e inqilab', 'not for sale', 'not-for-sale', 'awazeinqilab', 'camscanner']):
        return ''
    if re.match(r'^\d{1,3}$', p):
        return ''
    return p.strip()

print('Answer lines loaded:', len(ans_lines))
