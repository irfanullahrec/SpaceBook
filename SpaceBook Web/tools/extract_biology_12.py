import zipfile
import xml.etree.ElementTree as ET
import sys
import re
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

BOOK_DIR = r"D:\SpaceBook\Books\12th\12th Biology\Word"
NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def get_para_style(p_tag):
    pPr = p_tag.find(f'{NS}pPr')
    if pPr is not None:
        pStyle = pPr.find(f'{NS}pStyle')
        if pStyle is not None:
            return pStyle.get(f'{NS}val', '')
    return ''

def is_bold(p_tag):
    for r in p_tag.iter(f'{NS}r'):
        rPr = r.find(f'{NS}rPr')
        if rPr is not None:
            b = rPr.find(f'{NS}b')
            if b is not None:
                val = b.get(f'{NS}val', '1')
                if val != '0':
                    return True
    return False

def get_para_texts(p_tag):
    texts = []
    for t in p_tag.iter(f'{NS}t'):
        if t.text:
            texts.append(t.text)
    return ''.join(texts).strip()

def load_all_paragraphs():
    docx_files = sorted([
        os.path.join(BOOK_DIR, f)
        for f in os.listdir(BOOK_DIR)
        if f.endswith('.docx')
    ])
    all_paras = []
    for docx_path in docx_files:
        print(f"Reading: {os.path.basename(docx_path)}", file=sys.stderr)
        with zipfile.ZipFile(docx_path) as z:
            tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{NS}p'):
            txt = get_para_texts(p_tag)
            style = get_para_style(p_tag)
            bold = is_bold(p_tag)
            all_paras.append({'text': txt, 'style': style, 'bold': bold})
    print(f"Total paragraphs: {len(all_paras)}", file=sys.stderr)
    return all_paras

def detect_chapter_boundaries(paras):
    """Find chapter start indices for chapters 14-27."""
    chapter_pattern = re.compile(r'^Chapter\s+(1[4-9]|2[0-7])\b', re.IGNORECASE)
    boundaries = []
    for i, p in enumerate(paras):
        txt = p['text']
        m = chapter_pattern.match(txt)
        if m and len(txt) < 120:  # short paragraph
            chap_num = int(m.group(1))
            boundaries.append({'idx': i, 'num': chap_num, 'title_para': txt})
            print(f"  [para {i}] Chapter {chap_num}: {txt!r}")
    return boundaries

def extract_chapter_content(paras, start_idx, end_idx, chap_num):
    """Extract sections, exercise data from para range."""
    chunk = paras[start_idx:end_idx]

    # Pull title (first non-empty para after chapter header)
    title = ''
    title_idx = 0
    for i, p in enumerate(chunk[:10]):
        t = p['text']
        if t and not re.match(r'^Chapter\s+\d+', t, re.IGNORECASE):
            title = t
            title_idx = i
            break

    sections = []
    exercise = {'mcqs': [], 'shortQuestions': [], 'longQuestions': []}

    # Identify section headings - short bold or ALL-CAPS lines or heading styles
    heading_pattern = re.compile(r'^[A-Z][A-Z\s\-/()]{3,}$')
    subheading_pattern = re.compile(r'^\d+\.\d+\s+\w')

    exercise_start = None
    for i, p in enumerate(chunk):
        t = p['text']
        if re.match(r'^(Exercise|EXERCISE|Self Assessment|SELF ASSESSMENT)', t, re.IGNORECASE):
            exercise_start = i
            break

    content_chunk = chunk[:exercise_start] if exercise_start else chunk
    exercise_chunk = chunk[exercise_start:] if exercise_start else []

    # Build sections
    current_section = None
    current_paras = []

    def save_section():
        nonlocal current_section, current_paras
        if current_section is not None:
            text_joined = ' '.join(p for p in current_paras if p)
            sections.append({
                'heading': current_section,
                'text': text_joined,
                'paras': [p for p in current_paras if p]
            })
        current_section = None
        current_paras = []

    for i, p in enumerate(content_chunk):
        t = p['text']
        if not t:
            continue

        # Skip title / chapter header
        if i <= title_idx + 1:
            continue

        is_heading = False
        style = p['style'].lower()
        bold = p['bold']

        # Heading detection heuristics
        if (style.startswith('heading') or
                (bold and len(t) < 80 and not t.endswith('.') and not re.match(r'^\d+[\.\)]\s', t)) or
                heading_pattern.match(t) or
                subheading_pattern.match(t)):
            is_heading = True

        if is_heading:
            save_section()
            current_section = t
        else:
            if current_section is None and t:
                current_section = 'Introduction'
            current_paras.append(t)

    save_section()

    # Parse exercise section
    if exercise_chunk:
        parse_exercise(exercise_chunk, exercise)

    return title, sections, exercise

MCQ_PATTERN = re.compile(r'^[(\[{]?([a-dA-D])[)\].]?\s+.+')
OPTION_PATTERN = re.compile(r'^[(\[{]?([a-dA-D])[)\].]')
QUESTION_NUM_PATTERN = re.compile(r'^Q?\.?\s*\d+[\.\)]\s+.+', re.IGNORECASE)
SHORT_Q_PATTERN = re.compile(r'(?:short|brief)\s+(?:questions?|answers?)', re.IGNORECASE)
LONG_Q_PATTERN = re.compile(r'(?:long|detailed|essay)\s+(?:questions?|answers?)', re.IGNORECASE)
MCQ_SECTION_PATTERN = re.compile(r'(?:multiple\s*choice|MCQ|Choose\s+the\s+correct)', re.IGNORECASE)

def parse_exercise(chunk, exercise):
    mode = None  # 'mcq', 'short', 'long'
    current_q = None
    current_opts = []
    mcq_q_count = 0

    def flush_mcq():
        nonlocal current_q, current_opts
        if current_q:
            exercise['mcqs'].append({
                'q': current_q,
                'opts': current_opts[:4],
                'ans': 0
            })
            mcq_q_count_ref[0] += 1
        current_q = None
        current_opts = []

    mcq_q_count_ref = [0]

    for p in chunk:
        t = p['text']
        if not t:
            continue

        # Section header detection
        if MCQ_SECTION_PATTERN.search(t):
            flush_mcq()
            mode = 'mcq'
            continue
        if SHORT_Q_PATTERN.search(t):
            flush_mcq()
            mode = 'short'
            continue
        if LONG_Q_PATTERN.search(t):
            flush_mcq()
            mode = 'long'
            continue

        if mode == 'mcq':
            # Detect question vs option
            if re.match(r'^\s*\d+[\.\)]\s+', t):
                flush_mcq()
                current_q = re.sub(r'^\s*\d+[\.\)]\s+', '', t)
            elif OPTION_PATTERN.match(t):
                current_opts.append(re.sub(r'^[(\[{]?[a-dA-D][)\].]?\s*', '', t))
            elif current_q and not OPTION_PATTERN.match(t) and len(t) > 3:
                # continuation
                current_q += ' ' + t

        elif mode == 'short':
            if re.match(r'^\s*Q?\.?\s*\d+[\.\)]\s+', t, re.IGNORECASE):
                q = re.sub(r'^\s*Q?\.?\s*\d+[\.\)]\s+', '', t)
                exercise['shortQuestions'].append(q)
            elif t and exercise['shortQuestions']:
                # possible continuation
                pass

        elif mode == 'long':
            if re.match(r'^\s*Q?\.?\s*\d+[\.\)]\s+', t, re.IGNORECASE):
                q = re.sub(r'^\s*Q?\.?\s*\d+[\.\)]\s+', '', t)
                exercise['longQuestions'].append(q)

    flush_mcq()

CHAPTER_SUMMARIES = {
    14: "Homeostasis is the process by which living organisms maintain a stable internal environment despite changes in external conditions. It involves feedback mechanisms that regulate temperature, pH, blood glucose, and other physiological parameters. Key organs involved include the kidneys, liver, skin, and lungs.",
    15: "Osmoregulation is the control of water and solute balance in body fluids. Animals employ various mechanisms such as kidneys with nephrons, contractile vacuoles, and salt glands to regulate osmotic pressure. The process is critical for maintaining cell volume and proper biochemical function.",
    16: "The endocrine system consists of glands that secrete hormones directly into the bloodstream to regulate body functions. Major glands include the pituitary, thyroid, adrenal, and pancreas. Hormones act on target organs to control growth, metabolism, reproduction, and stress responses.",
    17: "The nervous system coordinates rapid responses to stimuli through electrical impulses transmitted by neurons. It is divided into the central nervous system (brain and spinal cord) and the peripheral nervous system. Neurons communicate via synapses using neurotransmitters.",
    18: "Sense organs, or receptors, detect stimuli from the environment and convert them into nerve impulses. Major sense organs include the eye (vision), ear (hearing and balance), nose (olfaction), tongue (taste), and skin (touch, pressure, pain). Each receptor is specialized for a particular type of stimulus.",
    19: "Animal behavior encompasses all actions and responses of animals to internal and external stimuli. Behaviors can be innate (genetically programmed) or learned through experience. Key concepts include taxes, reflexes, instincts, conditioning, imprinting, and social behavior.",
    20: "Reproduction ensures the continuation of species through either sexual or asexual means. In humans and many animals, sexual reproduction involves gametogenesis, fertilization, and development of the embryo. The male and female reproductive systems are specialized to produce, deliver, and nurture gametes.",
    21: "Development refers to the orderly series of changes an organism undergoes from a fertilized egg to an adult. Key stages include cleavage, gastrulation, organogenesis, and growth. Both genetic programs and environmental signals guide differentiation and morphogenesis.",
    22: "Genetics is the study of heredity and the variation of inherited characteristics. Mendel's laws of segregation and independent assortment describe how traits are passed from parents to offspring. Modern genetics covers DNA structure, gene expression, and molecular mechanisms of inheritance.",
    23: "Chromosomal aberrations are changes in chromosome number or structure that can cause genetic disorders. Examples include Down syndrome (trisomy 21), Turner syndrome (45,X), and Klinefelter syndrome (47,XXY). Human genetics also explores pedigree analysis and the inheritance of complex traits.",
    24: "Evolution is the change in heritable characteristics of populations over successive generations. Darwin's theory of natural selection explains how organisms with advantageous traits survive and reproduce more successfully. Evidence for evolution includes the fossil record, comparative anatomy, and molecular biology.",
    25: "An ecosystem consists of living organisms and their physical environment interacting as a system. Energy flows through ecosystems via food chains and food webs, while nutrients cycle through biogeochemical cycles. Ecology studies these interactions at population, community, and ecosystem levels.",
    26: "Biotechnology uses biological systems and organisms to develop products and processes for human benefit. Techniques such as recombinant DNA technology, gene cloning, and PCR have revolutionized medicine and agriculture. Genetic diseases result from mutations and can now be diagnosed and sometimes treated using biotechnological tools.",
    27: "Applied biology encompasses practical applications of biological knowledge to solve real-world problems. Areas include agriculture (crop improvement, pest control), medicine (vaccines, antibiotics), and environmental management. Bioremediation, aquaculture, and tissue culture are important applications of biology."
}

def build_dataset(paras, boundaries):
    chapters = []
    for bi, boundary in enumerate(boundaries):
        chap_num = boundary['num']
        start_idx = boundary['idx']
        end_idx = boundaries[bi + 1]['idx'] if bi + 1 < len(boundaries) else len(paras)

        print(f"\nExtracting Chapter {chap_num} (paras {start_idx}-{end_idx})...", file=sys.stderr)
        title, sections, exercise = extract_chapter_content(paras, start_idx, end_idx, chap_num)

        # Fallback title
        if not title or re.match(r'^Chapter\s+\d+', title, re.IGNORECASE):
            title = boundary['title_para']

        print(f"  Title: {title!r}", file=sys.stderr)
        print(f"  Sections: {len(sections)}", file=sys.stderr)
        print(f"  MCQs: {len(exercise['mcqs'])}", file=sys.stderr)
        print(f"  Short Qs: {len(exercise['shortQuestions'])}", file=sys.stderr)
        print(f"  Long Qs: {len(exercise['longQuestions'])}", file=sys.stderr)

        chapters.append({
            'number': chap_num,
            'title': title,
            'type': 'chapter',
            'sections': sections,
            'exercise': exercise,
            'englishSummary': CHAPTER_SUMMARIES.get(chap_num, '')
        })

    return chapters

def main():
    paras = load_all_paragraphs()

    print("\n=== CHAPTER BOUNDARY DETECTION ===")
    boundaries = detect_chapter_boundaries(paras)

    if not boundaries:
        print("ERROR: No chapter boundaries found!", file=sys.stderr)
        # Print first 200 paras for debugging
        for i, p in enumerate(paras[:200]):
            if p['text']:
                print(f"  [{i}] style={p['style']!r} bold={p['bold']} text={p['text']!r}")
        return

    print(f"\nFound {len(boundaries)} chapter boundaries")

    chapters = build_dataset(paras, boundaries)

    # Output JSON for verification
    out = {'chapters': []}
    for ch in chapters:
        out['chapters'].append({
            'number': ch['number'],
            'title': ch['title'],
            'section_count': len(ch['sections']),
            'section_headings': [s['heading'] for s in ch['sections'][:5]],
            'mcq_count': len(ch['exercise']['mcqs']),
            'short_q_count': len(ch['exercise']['shortQuestions']),
            'long_q_count': len(ch['exercise']['longQuestions']),
            'first_mcq': ch['exercise']['mcqs'][0] if ch['exercise']['mcqs'] else None,
            'first_short_q': ch['exercise']['shortQuestions'][0] if ch['exercise']['shortQuestions'] else None,
        })

    print("\n=== CHAPTER SUMMARY JSON ===")
    print(json.dumps(out, indent=2, ensure_ascii=False))

    # Also output full data as JSON for JS builder
    out_path = r"D:\SpaceBook\SpaceBook Web\tools\biology_12_raw.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    print(f"\nFull JSON written to {out_path}", file=sys.stderr)

if __name__ == '__main__':
    main()
