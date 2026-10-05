"""
Comprehensive Economics 12 content extractor.
Extracts chapters, sections, exercises for JS dataset generation.
"""
import zipfile, xml.etree.ElementTree as ET, sys, os, re, json

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Economics\Word"
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def extract_paragraphs(docx_path):
    paras = []
    with zipfile.ZipFile(docx_path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{W}p'):
            texts = [t.text for t in p_tag.iter(f'{W}t') if t.text]
            if texts:
                txt = ''.join(texts).strip()
                if txt:
                    paras.append(txt)
    return paras

docx_files = sorted([
    os.path.join(DOCX_DIR, f)
    for f in os.listdir(DOCX_DIR) if f.endswith('.docx')
])

all_paras = []
for docx_path in docx_files:
    paras = extract_paragraphs(docx_path)
    all_paras.extend(paras)

print(f"Total paragraphs: {len(all_paras)}", flush=True)

# ─────────────────────────────────────────────────────────────
# Identify chapter start indices using 'باب N' pattern
# ─────────────────────────────────────────────────────────────
BAB_PATTERN = re.compile(r'^باب\s*[1-9۱-۹]')

chapter_starts = []
for i, p in enumerate(all_paras):
    if BAB_PATTERN.match(p) and len(p) < 80:
        chapter_starts.append(i)

print(f"\nChapter start paragraphs ({len(chapter_starts)} found):")
for ci in chapter_starts:
    # Show a few paras around it
    snippet = all_paras[ci+1] if ci+1 < len(all_paras) else ""
    print(f"  [{ci}] {all_paras[ci]} | next: {snippet[:60]}")

# Add sentinel end
chapter_starts.append(len(all_paras))

# ─────────────────────────────────────────────────────────────
# For each chapter: find title, body paras, exercise section
# ─────────────────────────────────────────────────────────────
EXERCISE_KW = ['مشق', 'سوالات مشق', 'مختصر سوالات', 'کثیر الانتخاب', 'ماڈل پرچہ',
               'ذیل کے سوالات', 'طویل سوالات', 'یادداشت', 'نیچے دئیے',
               'درج ذیل سوال', '(A)', '(B)', '(C)', '(D)']
MCQ_OPT = re.compile(r'^\(([ABCD])\)\s*(.+)')
URDU_NUM = re.compile(r'^[۱۲۳۴۵۶۷۸۹]\s*[-۔]')
EN_NUM   = re.compile(r'^[1-9]\s*[-.]')

chapters_data = []

for ch_idx, start in enumerate(chapter_starts[:-1]):
    end = chapter_starts[ch_idx + 1]
    ch_paras = all_paras[start:end]

    # Title = first few meaningful paras
    title_ur = ""
    title_en = ""
    for p in ch_paras[:10]:
        if re.search(r'[a-zA-Z]', p) and not title_en and len(p) < 100:
            title_en = p
        elif not title_ur and len(p) < 80 and BAB_PATTERN.match(p) is None:
            if not re.match(r'^[\d\W]+$', p):
                title_ur = p

    # Find exercise section start
    exercise_start = len(ch_paras)
    for i, p in enumerate(ch_paras):
        if any(kw in p for kw in ['مشق', 'سوالات مشق', 'ماڈل پرچہ']) and i > 20:
            exercise_start = i
            break

    body_paras = ch_paras[:exercise_start]
    exer_paras = ch_paras[exercise_start:]

    # Extract MCQs from exercise
    mcqs = []
    i = 0
    while i < len(exer_paras):
        p = exer_paras[i]
        # Look for MCQ question: numbered or starts with Urdu question
        is_question = (URDU_NUM.match(p) or EN_NUM.match(p)) and '؟' in p
        if is_question and i + 4 < len(exer_paras):
            q_text = p
            opts = []
            j = i + 1
            while j < len(exer_paras) and len(opts) < 4:
                m = MCQ_OPT.match(exer_paras[j])
                if m:
                    opts.append(m.group(2).strip())
                elif exer_paras[j].strip() in ['(A)', '(B)', '(C)', '(D)']:
                    pass
                elif len(opts) > 0:
                    # Next non-option – stop
                    if not MCQ_OPT.match(exer_paras[j]):
                        break
                j += 1
            if len(opts) >= 2:
                mcqs.append({'q': q_text, 'opts': opts, 'ans': 0})
                i = j
                continue
        i += 1

    # Short questions (look for مختصر سوالات section)
    short_qs = []
    long_qs  = []
    in_short = False
    in_long  = False
    for p in exer_paras:
        if 'مختصر سوالات' in p or 'مختصر جوابی' in p:
            in_short = True; in_long = False; continue
        if 'تفصیلی سوالات' in p or 'طویل سوالات' in p or 'تشریحی سوالات' in p:
            in_long = True; in_short = False; continue
        if '؟' in p and len(p) > 10:
            if in_short:
                short_qs.append(p)
            elif in_long:
                long_qs.append(p)
            elif not in_short and not in_long and len(short_qs) == 0:
                short_qs.append(p)

    # Sections – group body into ~5 logical sections
    # Use heading-like paragraphs (short, colon-ending, or all urdu short lines)
    sections = []
    current_heading = ch_paras[0]
    current_paras   = []

    HEADING_PAT = re.compile(r'.{5,80}[:۔]$')
    for p in body_paras[1:]:
        is_heading = (
            len(p) < 100 and
            not re.search(r'[a-zA-Z]{4,}', p) and
            (p.endswith(':') or p.endswith('۔') or re.match(r'^[۱۲۳۴۵۶۷۸۹\-]-', p)) and
            len(current_paras) > 3
        )
        if is_heading:
            sections.append({'heading': current_heading, 'paras': current_paras})
            current_heading = p
            current_paras   = []
        else:
            current_paras.append(p)
    if current_paras:
        sections.append({'heading': current_heading, 'paras': current_paras})

    ch_data = {
        'chapter_idx': ch_idx + 1,
        'start_para' : start,
        'end_para'   : end,
        'title_ur'   : title_ur,
        'title_en'   : title_en,
        'total_paras': len(ch_paras),
        'body_paras' : len(body_paras),
        'exer_paras' : len(exer_paras),
        'sections'   : len(sections),
        'mcqs'       : len(mcqs),
        'short_qs'   : len(short_qs),
        'long_qs'    : len(long_qs),
    }
    chapters_data.append(ch_data)

    print(f"\n--- Chapter {ch_idx+1} ---")
    print(f"  Range: [{start}:{end}]  total={len(ch_paras)}")
    print(f"  Title (Ur): {title_ur}")
    print(f"  Title (En): {title_en}")
    print(f"  Body paras: {len(body_paras)}, Exercise paras: {len(exer_paras)}")
    print(f"  Sections grouped: {len(sections)}")
    print(f"  MCQs: {len(mcqs)}, Short Qs: {len(short_qs)}, Long Qs: {len(long_qs)}")
    if mcqs:
        print(f"  First MCQ: {mcqs[0]['q'][:80]}")
        print(f"  Opts: {mcqs[0]['opts']}")
    if short_qs:
        print(f"  First short Q: {short_qs[0][:80]}")

print("\n\nDone.")
