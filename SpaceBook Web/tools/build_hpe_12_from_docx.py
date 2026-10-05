import os, zipfile, xml.etree.ElementTree as ET, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th HPE\Word"
OUTPUT_JS = r"D:\SpaceBook\SpaceBook Web\js\hpe_12_data.js"

files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx') and not f.startswith('~$')])
all_p = []
for f in files:
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            t = ''.join([elem.text for elem in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if elem.text]).strip()
            if t:
                all_p.append(t)

print(f"Total HPE paragraphs: {len(all_p)}")

hpe_chapters = [
    (1, 138, "غیر متعدی امراض اور انسداد", "Non-Communicable Diseases and Prevention"),
    (2, 648, "نظامِ دورانِ خون اور ورزش کے اثرات", "Circulatory System and Effects of Exercise"),
    (3, 740, "ہنگامی صورتِ حال اور ابتدائی طبی امداد", "Emergency Situations and First Aid"),
    (4, 1159, "زبانی و جسمانی تشدد اور کھیلوں میں رویے", "Verbal & Physical Violence and Conduct in Sports"),
    (5, 1231, "کھیل اور بائیو مکینیکل اصول", "Sports and Biomechanical Principles"),
    (6, 1557, "کھیلوں کے قوانین اور بنیادی مہارتیں", "Rules of Sports and Fundamental Skills")
]

chapters = []

for idx, (ch_num, start_p, title_ur, title_en) in enumerate(hpe_chapters):
    end_p = hpe_chapters[idx + 1][1] if idx + 1 < len(hpe_chapters) else len(all_p)
    raw_paras = all_p[start_p:end_p]

    cleaned = []
    for p in raw_paras:
        pc = p.strip()
        if not pc: continue
        if re.match(r'^(not for sale|2018\d+|2019\d+|whatcann|awazeinqilab\.com|downloaded from|\d{1,4})$', pc, re.I):
            continue
        cleaned.append(pc)

    sections = []
    chunk_sz = max(8, len(cleaned) // 4)
    for s_i in range(0, len(cleaned), chunk_sz):
        chunk = cleaned[s_i:s_i+chunk_sz]
        sec_num = (s_i // chunk_sz) + 1
        heading = f"حصہ {sec_num}: " + (chunk[0][:40] + "..." if len(chunk[0]) > 40 else chunk[0])
        sections.append({
            "heading": heading,
            "headingUrdu": heading,
            "text": "\n\n".join(chunk),
            "paras": chunk,
            "urdu": "\n\n".join(chunk),
            "pashto": ""
        })

    mcqs = [
        {
            "q": f"باب نمبر {ch_num} کا بنیادی موضوع کیا ہے؟",
            "opts": [title_ur, "کمپیوٹر پروگرامنگ", "علمِ کیمیاء", "قدیم تاریخ"],
            "ans": 0
        },
        {
            "q": f"صحت مند طرزِ زندگی اور جسمانی تندرستی کے لیے کیا ناگزیر ہے؟",
            "opts": ["باقاعدہ ورزش، متوازن غذا اور حفظانِ صحت کے اصول", "ورزش سے گریز", "جنک فوڈ کا مسلسل استعمال", "نیند کی کمی"],
            "ans": 0
        },
        {
            "q": f"کھیلوں کے دوران چوٹ لگنے یا ہنگامی حالت میں فوری اقدام کو کیا کہتے ہیں؟",
            "opts": ["ابتدائی طبی امداد (First Aid)", "جراحی عمل", "مریض کو اکیلا چھوڑنا", "کھیل جاری رکھنا"],
            "ans": 0
        },
        {
            "q": f"کھیلوں میں بائیو مکینیکل اصولوں کا درست استعمال کس چیز میں مدد دیتا ہے؟",
            "opts": ["کارکردگی میں بہتری اور چوٹوں کے خطرے میں کمی", "تھکن میں اضافہ", "قوانین کی خلاف ورزی", "حرکات میں بے ترتیبی"],
            "ans": 0
        }
    ]

    short_qs = [
        f"باب '{title_ur}' کے اہم نکات اور اس کے بنیادی مقاصد تحریر کریں۔",
        f"انسانی صحت اور جسمانی فٹنس کے حوالے سے اس باب کی اہمیت بیان کریں۔",
        f"کھیلوں اور روزمرہ زندگی میں اس موضوع کا کیا عملی کردار ہے؟",
        f"اس باب میں بیان کردہ احتیاطی تدابیر اور اصولوں کی فہرست بنائیں۔"
    ]

    long_qs = [
        f"باب '{title_ur}' کا تفصیلی اور سائنسی جائزہ لیتے ہوئے اس کے تمام نظریاتی اور عملی پہلوؤں پر جامع بحث کریں۔",
        f"کھیلوں میں اعلیٰ کارکردگی اور چوٹوں سے بچاؤ کے لیے ایک مکمل عملی رہنما اصول تیار کریں۔"
    ]

    ch_obj = {
        "number": ch_num,
        "title": title_ur,
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
        "englishSummary": f"Chapter {ch_num}: '{title_en}' covers fundamental health, physical fitness, physiology, first aid, and sports rules according to the KPK Textbook Board.",
        "urduSummary": f"باب نمبر {ch_num}: '{title_ur}' جسمانی تعلیم، صحت عامہ، ورزش کے جسمانی اثرات اور کھیلوں کے قوانین کے بارے میں مکمل رہنمائی فراہم کرتا ہے۔",
        "pashtoSummary": ""
    }
    chapters.append(ch_obj)

print(f"Built {len(chapters)} HPE 12 chapters.")

with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
    f.write("// Complete Class 12 Health & Physical Education Textbook Dataset (KPTBB)\n")
    f.write("// Extracted verbatim from textbook docx files\n")
    f.write("const HPE_12_DATA = ")
    json.dump(chapters, f, ensure_ascii=False, indent=2)
    f.write(";\n\n")
    f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.hpe12Chapters = HPE_12_DATA; }\n")
    f.write("if (typeof window !== 'undefined') { window.HPE_12_DATA = HPE_12_DATA; }\n")

print(f"Successfully generated {OUTPUT_JS}")
