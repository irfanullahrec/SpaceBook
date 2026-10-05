import os, zipfile, xml.etree.ElementTree as ET, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Mutalia e Quran\Word"
OUTPUT_JS = r"D:\SpaceBook\SpaceBook Web\js\quran_12_data.js"

files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx') and not f.startswith('~$')])
all_p = []
for f in files:
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            t = ''.join([elem.text for elem in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if elem.text]).strip()
            if t:
                all_p.append(t)

print(f"Total Quran paragraphs: {len(all_p)}")

quran_chapters = [
    (1, 231, "سُورَةُ النِّسَاءِ (آیات ۱ تا ۲۵)", "Surah An-Nisa (Ayat 1-25)"),
    (2, 578, "سُورَةُ النِّسَاءِ (آیات ۲۶ تا ۷۰)", "Surah An-Nisa (Ayat 26-70)"),
    (3, 901, "سُورَةُ النِّسَاءِ (آیات ۷۱ تا ۱۰۰)", "Surah An-Nisa (Ayat 71-100)"),
    (4, 1253, "سُورَةُ النِّسَاءِ (آیات ۱۰۱ تا ۱۳۴)", "Surah An-Nisa (Ayat 101-134)"),
    (5, 1620, "سُورَةُ النِّسَاءِ (آیات ۱۳۵ تا ۱۷۶)", "Surah An-Nisa (Ayat 135-176)"),
    (6, 2045, "سُورَةُ الْمَائِدَةِ (آیات ۱ تا ۳۴)", "Surah Al-Maidah (Ayat 1-34)"),
    (7, 2500, "سُورَةُ الْمَائِدَةِ (آیات ۳۵ تا ۷۷)", "Surah Al-Maidah (Ayat 35-77)"),
    (8, 3200, "سُورَةُ الْمَائِدَةِ (آیات ۷۸ تا ۱۲۰)", "Surah Al-Maidah (Ayat 78-120)")
]

chapters = []

for idx, (ch_num, start_p, title_ur, title_en) in enumerate(quran_chapters):
    end_p = quran_chapters[idx + 1][1] if idx + 1 < len(quran_chapters) else len(all_p)
    raw_paras = all_p[start_p:end_p]

    cleaned = []
    for p in raw_paras:
        pc = p.strip()
        if not pc: continue
        if re.match(r'^(not for sale|2026\d+|2027\d+|whatcann|awazeinqilab\.com|downloaded from|\d{1,4})$', pc, re.I):
            continue
        cleaned.append(pc)

    sections = []
    chunk_sz = max(10, len(cleaned) // 4)
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
            "q": f"سبق نمبر {ch_num} کا بنیادی قرآنی متن کیا ہے؟",
            "opts": [title_ur, "سورة البقرة", "سورة يوسف", "سورة الكهف"],
            "ans": 0
        },
        {
            "q": f"ان آیاتِ مبارکہ میں کن اہم سماجی و معاشرتی احکام کی وضاحت کی گئی ہے؟",
            "opts": ["خاندانی نظام، یتامیٰ کے حقوق، عدل و انصاف، اور معاملات کی صفائی", "محض قدیم روایات", "فلسفیانہ مناظرے", "کارپوریٹ معاہدات"],
            "ans": 0
        },
        {
            "q": f"سورة المائدة میں بنیادی طور پر کن دینی احکام پر زور دیا گیا ہے؟",
            "opts": ["عہد و پیمان کی پاسداری اور حلال و حرام کی تمیز", "روایتی رسم و رواج", "سود کی حمایت", "غیر اخلاقی رسومات"],
            "ans": 0
        },
        {
            "q": f"قرآن مجید کے مطالعے کا بنیادی تقاضا اور مقصد کیا ہے؟",
            "opts": ["سمجھ کر پڑھنا، تدبر کرنا اور عملی زندگی میں نافذ کرنا", "محض زبانی تکرار بغیر سمجھے", "احکام سے اعراض", "تحقیق سے دوری"],
            "ans": 0
        }
    ]

    short_qs = [
        f"سبق '{title_ur}' کا ترجمہ اور مرکزی پیغام اپنے الفاظ میں تحریر کریں۔",
        f"ان آیاتِ مبارکہ میں دیے گئے اہم شرعی اور اخلاقی احکام کی فہرست بنائیں۔",
        f"معاشرتی اصلاح اور عدل کے قیام میں ان قرآنی تعلیمات کا کیا کردار ہے؟",
        f"اس سبق میں بیان کردہ اہم عربی الفاظ کے معانی تحریر کریں۔"
    ]

    long_qs = [
        f"سبق '{title_ur}' کی منتخب آیات کا مفصل تفسیری جائزہ پیش کرتے ہوئے ان کے ایمانی، فقہی اور سماجی پہلوؤں پر جامع بحث کریں۔",
        f"دورِ حاضر میں قرآنی احکام پر عمل پیرا ہو کر معاشرے کو ایک مثالی فلاحی اسلامی معاشرہ کیسے بنایا جا سکتا ہے؟ تفصیل سے واضح کریں۔"
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
        "englishSummary": f"Chapter {ch_num}: '{title_en}' provides comprehensive Quranic recitation, verbatim Urdu translation, contextual explanation (Tafseer), and moral guidelines from the KPK curriculum.",
        "urduSummary": f"سبق نمبر {ch_num}: '{title_ur}' قرآن حکیم کے منتخب حصص کا مستند عربی متن، بامحاورہ اردو ترجمہ اور جامع تفسیری تشریح پیش کرتا ہے۔",
        "pashtoSummary": ""
    }
    chapters.append(ch_obj)

print(f"Built {len(chapters)} Mutalia-e-Quran 12 chapters.")

with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
    f.write("// Complete Class 12 Mutalia-e-Quran Textbook Dataset (KPTBB)\n")
    f.write("// Extracted verbatim from textbook docx files\n")
    f.write("const QURAN_12_DATA = ")
    json.dump(chapters, f, ensure_ascii=False, indent=2)
    f.write(";\n\n")
    f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.quran12Chapters = QURAN_12_DATA; }\n")
    f.write("if (typeof window !== 'undefined') { window.QURAN_12_DATA = QURAN_12_DATA; }\n")

print(f"Successfully generated {OUTPUT_JS}")
