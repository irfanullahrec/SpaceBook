import zipfile, xml.etree.ElementTree as ET, sys, os, re, json

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r'D:\SpaceBook\Books\12th\12th Pak Studies\Word'
docx_files = sorted([
    os.path.join(DOCX_DIR, f)
    for f in os.listdir(DOCX_DIR) if f.endswith('.docx')
])

NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def extract_paragraphs(docx_path):
    paragraphs = []
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{NS}p'):
            style = ''
            pPr = p_tag.find(f'{NS}pPr')
            if pPr is not None:
                pStyle = pPr.find(f'{NS}pStyle')
                if pStyle is not None:
                    style = pStyle.get(f'{NS}val', '')
            texts = []
            for r in p_tag.iter(f'{NS}r'):
                rPr = r.find(f'{NS}rPr')
                if rPr is not None:
                    vanish = rPr.find(f'{NS}vanish')
                    if vanish is not None:
                        continue
                for t in r.iter(f'{NS}t'):
                    if t.text:
                        texts.append(t.text)
            txt = ''.join(texts).strip()
            if txt:
                paragraphs.append((txt, style))
    return paragraphs

all_paras = []
for docx_path in docx_files:
    paras = extract_paragraphs(docx_path)
    all_paras.extend(paras)

# Chapter boundaries (from scan)
# Format: (para_index, ordinal_name, chapter_title_index_offset)
bab_markers = []
bab_ordinals = ['اول','دوم','سوم','چہارم','پنجم','ششم','ہفتم','ہشتم','نہم','دہم','یازدہم']

for i, (txt, style) in enumerate(all_paras):
    if 'باب' in txt:
        for o in bab_ordinals:
            if o in txt:
                bab_markers.append((i, txt.strip()))
                break

print("Chapter markers found:")
for idx, (para_i, title) in enumerate(bab_markers):
    # Next title is usually the next non-empty para after the باب line
    next_title = ""
    if para_i + 1 < len(all_paras):
        next_title = all_paras[para_i + 1][0][:80]
    print(f"  Ch{idx+1}: para[{para_i}] '{title}' -> '{next_title}'")

# Build chapters
chapters = []
for idx, (para_i, bab_title) in enumerate(bab_markers):
    # Chapter ends just before next bab marker (or end)
    if idx + 1 < len(bab_markers):
        end_i = bab_markers[idx + 1][0]
    else:
        end_i = len(all_paras)
    
    # Chapter title = para after bab line
    ch_title = all_paras[para_i + 1][0] if para_i + 1 < len(all_paras) else bab_title
    
    # Content paragraphs
    content_paras = []
    exercise_start = None
    for j in range(para_i + 2, end_i):
        txt, style = all_paras[j]
        # Detect exercise section
        if exercise_start is None and ('مشق' in txt or ('سوالات' in txt and len(txt) < 30)):
            exercise_start = j
        content_paras.append((j, txt, style))
    
    chapters.append({
        'number': idx + 1,
        'bab': bab_title,
        'title': ch_title,
        'para_start': para_i,
        'para_end': end_i,
        'exercise_start': exercise_start,
        'content': content_paras
    })

# Print chapter summaries
print("\n=== CHAPTER SUMMARIES ===")
for ch in chapters:
    content_count = len(ch['content'])
    print(f"\nChapter {ch['number']}: {ch['bab']}")
    print(f"  Title: {ch['title'][:100]}")
    print(f"  Paras: {ch['para_start']} - {ch['para_end']} (content: {content_count})")
    if ch['exercise_start']:
        print(f"  Exercise starts at: {ch['exercise_start']}")
    # Print first 5 content paras
    print("  First 5 paras:")
    for j, txt, style in ch['content'][:5]:
        print(f"    [{j}] {txt[:100]}")
    print("  ...")
    # Print exercise paras if found
    if ch['exercise_start']:
        ex_paras = [(j,t,s) for j,t,s in ch['content'] if j >= ch['exercise_start']]
        print(f"  Exercise paras ({len(ex_paras)}):")
        for j, txt, style in ex_paras[:20]:
            print(f"    [{j}] {txt[:100]}")

# Save detailed output for building the JS
print("\n=== CHAPTER CONTENT FOR JS BUILDING ===")
for ch in chapters:
    print(f"\n### CHAPTER {ch['number']}: {ch['bab']} ###")
    print(f"TITLE: {ch['title']}")
    ex_start = ch['exercise_start']
    
    # Sections: group by subheadings (short paras that are potential headings)
    sections = []
    current_section = {'heading': '', 'paras': []}
    
    for j, txt, style in ch['content']:
        if ex_start and j >= ex_start:
            break
        # Potential heading: short, no ending punctuation
        is_heading = (len(txt) < 80 and not txt.endswith('۔') and not txt.endswith('،') 
                     and not txt.endswith('.') and not any(c.isdigit() for c in txt[:3]))
        if is_heading and len(txt.strip()) > 3:
            if current_section['paras']:
                sections.append(current_section)
            current_section = {'heading': txt, 'paras': []}
        else:
            current_section['paras'].append(txt)
    if current_section['paras']:
        sections.append(current_section)
    
    print(f"SECTIONS ({len(sections)}):")
    for s in sections:
        print(f"  HEADING: {s['heading'][:80]}")
        print(f"  PARAS: {len(s['paras'])}")
        for p in s['paras'][:3]:
            print(f"    - {p[:100]}")
    
    # Exercise
    if ex_start:
        ex_paras = [(j,t,s) for j,t,s in ch['content'] if j >= ex_start]
        print(f"EXERCISE ({len(ex_paras)} paras):")
        for j, txt, style in ex_paras[:30]:
            print(f"  [{j}] {txt[:120]}")
