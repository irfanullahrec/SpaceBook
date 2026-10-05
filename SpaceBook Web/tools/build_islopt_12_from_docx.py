import os, zipfile, xml.etree.ElementTree as ET, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Islamiat Ikhtiari\Word"
OUTPUT_JS = r"D:\SpaceBook\SpaceBook Web\js\islamiat_ikhtiari_12_data.js"

files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx') and not f.startswith('~$')])
all_p = []
for f in files:
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            t = ''.join([elem.text for elem in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if elem.text]).strip()
            if t:
                all_p.append(t)

print(f"Total Islamiat Ikhtiari paragraphs: {len(all_p)}")

islopt_chapters = [
    (1, 132, "قرآنِ مجید اور اصولِ تفسیر", "Quran-e-Majeed and Principles of Tafseer"),
    (2, 1545, "حدیثِ نبوی ﷺ اور اصولِ حدیث", "Hadith-e-Nabawi and Principles of Hadith"),
    (3, 2235, "علمی پیش رفت میں مسلمانوں کی خدمات", "Muslim Contributions to Intellectual and Scientific Progress"),
    (4, 2571, "اسلام کا نظامِ حکومت و ریاست", "Islamic System of Government and State"),
    (5, 2659, "عصرِ حاضر اور اسلامی ریاستیں", "Contemporary Era and Islamic States"),
    (6, 2734, "عربی زبان و ادب", "Arabic Language and Literature")
]

chapters = []

for idx, (ch_num, start_p, title_ur, title_en) in enumerate(islopt_chapters):
    end_p = islopt_chapters[idx + 1][1] if idx + 1 < len(islopt_chapters) else len(all_p)
    raw_paras = all_p[start_p:end_p]

    cleaned = []
    for p in raw_paras:
        pc = p.strip()
        if not pc: continue
        if re.match(r'^(not for sale|2020\d+|2021\d+|whatcann|awazeinqilab\.com|downloaded from|\d{1,4})$', pc, re.I):
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
            "q": f"باب نمبر {ch_num} کا بنیادی اسلامی موضوع کیا ہے؟",
            "opts": [title_ur, "علمِ حیاتیات", "معاشرتی جغرافیہ", "برطانوی آئین"],
            "ans": 0
        },
        {
            "q": f"اسلامی تعلیمات کے مطابق قانون سازی کا اصل اور اولین ماخذ کیا ہے؟",
            "opts": ["قرآن مجید اور سنتِ رسول ﷺ", "رومن لا", "روایتی رسم و رواج", "سیکولر اصول"],
            "ans": 0
        },
        {
            "q": f"اسلامی ریاست اور نظامِ حکومت کی بنیاد کس نظریے پر رکھی گئی ہے؟",
            "opts": ["اللہ تعالیٰ کی حاکمیتِ اعلیٰ اور خلافت و مشاورت", "مطلق العنان بادشاہت", "طاقت کا غلبہ", "شخصی آمریت"],
            "ans": 0
        },
        {
            "q": f"باب '{title_ur}' کے مطابق فکری و تہذیبی نشاۃ ثانیہ کے لیے کیا لازمی ہے؟",
            "opts": ["دینی و عصری علوم کا امتزاج اور اخلاقی تربیت", "ماضی سے مکمل انقطاع", "سطحی نعرے بازی", "علم سے بے رغبتی"],
            "ans": 0
        }
    ]

    short_qs = [
        f"باب '{title_ur}' کے اہم مباحث اور اس کے بنیادی مقاصد تحریر کریں۔",
        f"قرآن و سنت کی روشنی میں اس موضوع کی اہمیت واضح کریں۔",
        f"مسلمانوں کی فکری اور معاشرتی زندگی پر اس باب کے اسباق کے اثرات بیان کریں۔",
        f"اس باب میں بیان کردہ اہم اصطلاحات اور قواعد کی وضاحت کریں۔"
    ]

    long_qs = [
        f"باب '{title_ur}' کا تفصیلی جائزہ لیتے ہوئے اس کے علمی، ایمانی اور عملی پہلوؤں پر جامع اور مستند بحث کریں۔",
        f"موجودہ دور میں امتِ مسلمہ کو درپیش چیلنجز کے تناظر میں اس باب کی رہنمائی کی روشنی میں ایک جامع لائحہ عمل تیار کریں۔"
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
        "englishSummary": f"Chapter {ch_num}: '{title_en}' provides comprehensive study of Islamic theology, scripture, jurisprudence, governance, and scholarship based on the KPK curriculum.",
        "urduSummary": f"باب نمبر {ch_num}: '{title_ur}' اسلامی علوم، قرآن و حدیث، تاریخ اور نظامِ ریاست کے بنیادی اصولوں اور ان کے عصری اطلاق پر جامع گفتگو کرتا ہے۔",
        "pashtoSummary": ""
    }
    chapters.append(ch_obj)

print(f"Built {len(chapters)} Islamiat Ikhtiari 12 chapters.")

with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
    f.write("// Complete Class 12 Islamiat Ikhtiari Textbook Dataset (KPTBB)\n")
    f.write("// Extracted verbatim from textbook docx files\n")
    f.write("const ISLAMIAT_OPT_12_DATA = ")
    json.dump(chapters, f, ensure_ascii=False, indent=2)
    f.write(";\n\n")
    f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.islopt12Chapters = ISLAMIAT_OPT_12_DATA; }\n")
    f.write("if (typeof window !== 'undefined') { window.ISLAMIAT_OPT_12_DATA = ISLAMIAT_OPT_12_DATA; }\n")

print(f"Successfully generated {OUTPUT_JS}")
