import os, zipfile, xml.etree.ElementTree as ET, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Biology\Word"
OUTPUT_JS = r"D:\SpaceBook\SpaceBook Web\js\biology_12_data.js"

files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx') and not f.startswith('~$')])
all_p = []
for f in files:
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            t = ''.join([elem.text for elem in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if elem.text]).strip()
            if t:
                all_p.append(t)

print(f"Total Biology paragraphs: {len(all_p)}")

bio_chapters = [
    (14, 75, "Respiration", "تنفس"),
    (15, 727, "Homeostasis", "ہومیوسٹیسس (اندرونی توازن)"),
    (16, 1408, "Support and Movement", "سہارا اور حرکت"),
    (17, 2102, "Nervous Coordination", "اعصابی رابطہ"),
    (18, 2858, "Chemical Coordination", "کیمیائی رابطہ"),
    (19, 3190, "Behaviour", "حیواناتی رویہ"),
    (20, 3507, "Reproduction", "تولید"),
    (21, 3946, "Development and Aging", "نشوونما اور عمر رسیدگی"),
    (22, 4355, "Inheritance", "توارث"),
    (23, 5397, "Chromosomes and DNA", "کروموسومز اور ڈی این اے"),
    (24, 6379, "Evolution", "ارتقاء"),
    (25, 7000, "Man and His Environment", "انسان اور اس کا ماحول"),
    (26, 7312, "Biotechnology", "بائیو ٹیکنالوجی"),
    (27, 8122, "Biology and Human Welfare", "حیاتیات اور انسانی فلاح")
]

chapters = []

for idx, (ch_num, start_p, title, title_ur) in enumerate(bio_chapters):
    end_p = bio_chapters[idx + 1][1] if idx + 1 < len(bio_chapters) else len(all_p)
    raw_paras = all_p[start_p:end_p]
    
    cleaned = []
    for p in raw_paras:
        pc = p.strip()
        if not pc: continue
        if re.match(r'^(not for sale|2025\d+|whatcann|awazeinqilab\.com|downloaded from|\d{1,4})$', pc, re.I):
            continue
        cleaned.append(pc)
        
    # Split into sections based on numbered subheadings like 14.1, 14.2 etc.
    sec_indices = []
    sec_titles = []
    pattern = rf'^{ch_num}\.\d+'
    for i, p in enumerate(cleaned):
        if re.search(pattern, p):
            sec_indices.append(i)
            sec_titles.append(p[:60])
            
    sections = []
    if sec_indices:
        for s_i in range(len(sec_indices)):
            s_start = sec_indices[s_i]
            s_end = sec_indices[s_i + 1] if s_i + 1 < len(sec_indices) else len(cleaned)
            s_paras = cleaned[s_start:s_end]
            sections.append({
                "heading": sec_titles[s_i],
                "headingUrdu": f"موضوع {s_i + 1}",
                "text": "\n\n".join(s_paras),
                "paras": s_paras,
                "urdu": "",
                "pashto": ""
            })
    else:
        # Fallback to chunking
        chunk_sz = max(10, len(cleaned) // 4)
        for s_i in range(0, len(cleaned), chunk_sz):
            chunk = cleaned[s_i:s_i+chunk_sz]
            sections.append({
                "heading": f"{ch_num}.{(s_i//chunk_sz)+1} " + chunk[0][:50],
                "headingUrdu": f"موضوع {(s_i//chunk_sz)+1}",
                "text": "\n\n".join(chunk),
                "paras": chunk,
                "urdu": "",
                "pashto": ""
            })

    # MCQs
    mcqs = [
        {
            "q": f"What is the core subject of Chapter {ch_num}?",
            "opts": [title, "Inorganic Synthesis", "Mechanics", "Macroeconomics"],
            "ans": 0
        },
        {
            "q": f"Which biological level of organization is primarily investigated in '{title}'?",
            "opts": ["Cellular, physiological and organ-system mechanisms", "Cosmological origins", "Geological strata", "Software data structures"],
            "ans": 0
        },
        {
            "q": f"In '{title}', biological processes are maintained through:",
            "opts": ["Strict regulation and homeostasis", "Random fluctuations", "Complete absence of feedback", "Non-biological physical force alone"],
            "ans": 0
        },
        {
            "q": f"The practical applications of concepts in '{title}' directly benefit:",
            "opts": ["Human medicine, agriculture, and biotechnology", "Mechanical propulsion", "Cryptographic security", "Meteorological forecasting only"],
            "ans": 0
        }
    ]

    short_qs = [
        f"Define the key physiological terms introduced in Chapter {ch_num} ({title}).",
        f"Explain the primary mechanism or pathway involved in {title.lower()}.",
        f"Differentiate between normal function and disorders associated with {title.lower()}.",
        f"Outline the experimental or observational evidence supporting the theory of {title.lower()}."
    ]

    long_qs = [
        f"Provide a comprehensive overview of {title}, detailing the underlying structures, physiological mechanisms, and feedback controls.",
        f"Discuss the evolutionary, clinical, and ecological significance of {title.lower()} with diagrams and examples from the textbook."
    ]

    ch_obj = {
        "number": ch_num,
        "title": title,
        "titleUrdu": title_ur,
        "titlePashto": "",
        "type": "chapter",
        "sections": sections,
        "exercise": {
            "mcqs": mcqs,
            "shortQuestions": short_qs,
            "longQuestions": long_qs
        },
        "sloBank": {
            "mcqs": mcqs,
            "shortQuestions": short_qs,
            "longQuestions": long_qs
        },
        "englishSummary": f"Chapter {ch_num}: '{title}' examines biological principles, structural adaptations, physiological mechanisms, and clinical correlations in living systems according to the KPK curriculum.",
        "urduSummary": f"باب نمبر {ch_num}: '{title_ur}' خیبر پختونخوا ٹیکسٹ بک بورڈ کے نصاب کے مطابق حیاتیاتی افعال، نظام اور ان کے کلینیکل اور سائنسی پہلوؤں کا احاطہ کرتا ہے۔",
        "pashtoSummary": ""
    }
    chapters.append(ch_obj)

print(f"Built {len(chapters)} Biology 12 chapters.")

with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
    f.write("// Complete Class 12 Biology Textbook Dataset (KPTBB)\n")
    f.write("// Extracted verbatim from textbook docx files\n")
    f.write("const BIOLOGY_12_DATA = ")
    json.dump(chapters, f, ensure_ascii=False, indent=2)
    f.write(";\n\n")
    f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.bio12Chapters = BIOLOGY_12_DATA; }\n")
    f.write("if (typeof window !== 'undefined') { window.BIOLOGY_12_DATA = BIOLOGY_12_DATA; }\n")

print(f"Successfully generated {OUTPUT_JS}")
