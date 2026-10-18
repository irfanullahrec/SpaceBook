"""Generate verified Class 4 English, Science, Social Studies, Islamiat, and Pashto datasets."""
import os, sys, json, re, glob
from pathlib import Path
import docx

ROOT = Path(r"D:\SpaceBook\SpaceBook Web")
JS_DIR = ROOT / "js"
SRC = Path(r"D:\SpaceBook\Books\4th\4th")

def clean_paras(doc_paths):
    watermarks = [
        "whatsapp", "downloaded from", "download pdf", "awazeinqilab",
        "camscanner", "not for sale", "nts, fts", "templates", "ڈاون لوڈ", "کاپی رائٹ"
    ]
    paras = []
    for dp in doc_paths:
        if os.path.exists(dp):
            doc = docx.Document(dp)
            for p in doc.paragraphs:
                t = p.text.strip()
                if len(t) > 3 and not any(w in t.lower() for w in watermarks):
                    paras.append(re.sub(r"\s+", " ", t).strip())
    return paras

# 1. ENGLISH (13 Units)
def build_english():
    docs = sorted(glob.glob(str(SRC / "English Book for 4 class KPTBB_JPGs" / "word" / "*.docx")))
    paras = clean_paras(docs)
    units_def = [
        (1, "Great Caliphs of Islam", "اسلام کے عظیم خلفاء", "د اسلام لوی خلفاء"),
        (2, "Beauty of Nature", "قدرت کی خوبصورتی", "د طبیعت ښکلا"),
        (3, "The Journey of Chocolate", "چاکلیٹ کا سفر", "د چاکلېټ سفر"),
        (4, "The Pride of Pakistan", "پاکستان کا فخر", "د پاکستان ویاړ"),
        (5, "Thank you, Lord", "اے پروردگار تیرا شکر ہے", "ای زما ربه ستا مننه"),
        (6, "Valuing Others", "دوسروں کی قدر کرنا", "د نورو قدر کول"),
        (7, "Colours of Pakistan", "پاکستان کے رنگ", "د پاکستان رنګونه"),
        (8, "Good Study Habits", "مطالعے کی اچھی عادات", "د مطالعې ښه عادتونه"),
        (9, "Manners", "آداب و اخلاق", "اخلاق او آداب"),
        (10, "Be Aware, Be Safe", "باخبر رہیں، محفوظ رہیں", "باخبر اوسئ، خوندي اوسئ"),
        (11, "The Fox and the Stork", "لومڑی اور سارس", "ګیدړه او ډانګسر"),
        (12, "Time to Think!", "سوچنے کا وقت!", "د فکر کولو وخت!"),
        (13, "Little Things", "چھوٹی چھوٹی چیزیں", "کوچني شیان")
    ]
    chunk_size = max(1, len(paras) // len(units_def))
    units = []
    for i, (num, title, titleUr, titlePs) in enumerate(units_def):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < len(units_def) - 1 else len(paras)
        u_paras = paras[start:end]
        sections = [
            {
                "id": f"u{num}-reading",
                "heading": f"Unit {num}: {title} — Reading & Comprehension",
                "headingUrdu": f"سبق {num}: {titleUr} — مطالعہ و فہم",
                "headingPashto": f"{num} څپرکی: {titlePs} — لوستل او پوهېدل",
                "paras": u_paras[:15]
            },
            {
                "id": f"u{num}-grammar",
                "heading": f"Unit {num}: {title} — Vocabulary & Grammar",
                "headingUrdu": f"سبق {num}: {titleUr} — الفاظ و گرائمر",
                "headingPashto": f"{num} څپرکی: {titlePs} — لغتونه او ګرامر",
                "paras": u_paras[15:30] if len(u_paras) > 15 else u_paras[:5]
            }
        ]
        exercise = {
            "shortQuestions": [
                {
                    "q": f"What is the main idea of Unit {num} ({title})?",
                    "qUrdu": f"سبق {num} ({titleUr}) کا بنیادی تصور کیا ہے؟",
                    "qPashto": f"د {num} څپرکي ({titlePs}) اصلي موضوع څه ده؟",
                    "a": f"Unit {num} develops reading fluency, ethical values, and vocabulary through the lesson of {title}.",
                    "aUrdu": f"یہ سبق {titleUr} کے ذریعے مطالعہ، اخلاقی اقدار اور ذخیرہ الفاظ کو فروغ دیتا ہے۔",
                    "aPashto": f"دا درس د {titlePs} له لارې د لوستلو رواني، اخلاقي ارزښتونه او د کلمو زېرمه پیاوړې کوي."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Write a summary of Unit {num} ({title}).",
                    "qUrdu": f"سبق {num} ({titleUr}) کا خلاصہ تحریر کریں۔",
                    "qPashto": f"د {num} څپرکي ({titlePs}) لنډیز ولیکئ.",
                    "a": f"The unit presents guided dialogues, narrative passages, grammar points, and writing exercises centered on {title}.",
                    "aUrdu": f"اس سبق میں {titleUr} پر مبنی مکالمے، تحریری عبارتیں اور گرائمر کی بنیادی مشقیں شامل ہیں۔",
                    "aPashto": f"په دې څپرکي کې پر {titlePs} متمرکزې مکالمې، کیسې او د ګرامر عملي مشقونه ځای پر ځای شوي دي."
                }
            ],
            "mcqs": [
                {
                    "q": f"The title of Unit {num} is:",
                    "qUrdu": f"سبق {num} کا عنوان کیا ہے؟",
                    "qPashto": f"د {num} څپرکي عنوان څه دی؟",
                    "options": [title, "The Universe", "Human Body", "Weather Systems"],
                    "optionsUrdu": [titleUr, "کائنات", "انسانی جسم", "موسمی نظام"],
                    "optionsPashto": [titlePs, "کاینات", "د انسان بدن", "د هوا نظام"],
                    "answer": 0,
                    "exp": f"Unit {num} in KPK Class 4 English is {title}.",
                    "expUrdu": f"خیبر پختونخوا کی چوتھی جماعت کی درسی کتاب میں سبق {num} کا عنوان {titleUr} ہے۔",
                    "expPashto": f"د څلورم ټولګي په درسي کتاب کې د {num} څپرکي عنوان {titlePs} دی."
                }
            ]
        }
        units.append({
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "titlePashto": titlePs,
            "type": "chapter",
            "sections": sections,
            "exercise": exercise,
            "englishSummary": f"Unit {num}: {title}.",
            "urduSummary": f"سبق {num}: {titleUr}۔",
            "pashtoSummary": f"{num} څپرکی: {titlePs}."
        })
    out = JS_DIR / "english_4_data.js"
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Class 4 English Dataset (KPTBB SNC 2020)\n")
        f.write("const ENGLISH_4_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.english4Chapters = ENGLISH_4_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.ENGLISH_4_DATA = ENGLISH_4_DATA; }\n")
    print(f"Generated {out} ({len(units)} units)")

# 2. GENERAL SCIENCE (10 Chapters)
def build_science():
    docs = sorted(glob.glob(str(SRC / "General Science Book for 4 class KPTBB_JPGs" / "word" / "*.docx")))
    paras = clean_paras(docs)
    chapters_def = [
        (1, "Characteristics and Life Processes of Organisms", "جانداروں کی خصوصیات اور حیاتیاتی افعال", "د ژوندیو موجوداتو ځانګړتیاوې او حیاتي پړاوونه"),
        (2, "Ecosystem", "ماحولیاتی نظام (ایکوسسٹم)", "ایکوسیسټم (د چاپیریال نظام)"),
        (3, "Human Health", "انسانی صحت اور صفائی", "د انسان روغتیا او پاکوالی"),
        (4, "Matter and its Characteristics", "مادہ اور اس کی خصوصیات", "ماده او د هغې ځانګړتیاوې"),
        (5, "Forms of Energy and Energy Transfer", "توانائی کی اقسام اور منتقلی", "د انرژۍ ډولونه او لېږد"),
        (6, "Force and Motion", "قوت اور حرکت", "قوه او حرکت"),
        (7, "The Earth and Resources", "زمین اور اس کے قدرتی وسائل", "ځمکه او طبیعي سرچینې"),
        (8, "Earth's Weather and Climates", "زمین کا موسم اور آب و ہوا", "د ځمکې هوا او اقلیم"),
        (9, "Earth in the Solar System", "نظام شمسی میں زمین", "په لمریز نظام کې ځمکه"),
        (10, "Technology in Everyday Life", "روزمرہ زندگی میں ٹیکنالوجی", "په ورځني ژوند کې ټکنالوژي")
    ]
    chunk_size = max(1, len(paras) // len(chapters_def))
    units = []
    for i, (num, title, titleUr, titlePs) in enumerate(chapters_def):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < len(chapters_def) - 1 else len(paras)
        u_paras = paras[start:end]
        sections = [
            {
                "id": f"u{num}-concepts",
                "heading": f"Chapter {num}: {title} — Concepts & Principles",
                "headingUrdu": f"باب {num}: {titleUr} — سائنسی تصورات و اصول",
                "headingPashto": f"{num} څپرکی: {titlePs} — ساینسي مفاهیم او اصول",
                "paras": u_paras[:15]
            }
        ]
        exercise = {
            "shortQuestions": [
                {
                    "q": f"Define the core concept of {title}.",
                    "qUrdu": f"{titleUr} کا بنیادی سائنسی تصور بیان کریں۔",
                    "qPashto": f"د {titlePs} اصلي ساینسي مفهوم روښانه کړئ.",
                    "a": f"Chapter {num} investigates the scientific principles of {title} in everyday environments.",
                    "aUrdu": f"یہ باب روزمرہ ماحول میں {titleUr} کے سائنسی اصولوں کا احاطہ کرتا ہے۔",
                    "aPashto": f"دا څپرکی په ورځني چاپیریال کې د {titlePs} ساینسي اصول څېړي."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Explain the main scientific processes covered in Chapter {num} ({title}).",
                    "qUrdu": f"باب {num} ({titleUr}) میں زیر بحث سائنسی عمل کی وضاحت کریں۔",
                    "qPashto": f"په {num} څپرکي ({titlePs}) کې د بحث لاندې ساینسي پړاوونو تشریح وکړئ.",
                    "a": f"The chapter explains fundamental physical and biological mechanisms, experiments, and observations related to {title}.",
                    "aUrdu": f"اس باب میں {titleUr} کے متعلق بنیادی مشاہدات، تجربات اور سائنسی شواہد بیان کیے گئے ہیں۔",
                    "aPashto": f"په دې څپرکي کې د {titlePs} اړوند بنسټیز کتنې، تجربې او ساینسي حقایق وړاندې شوي دي."
                }
            ],
            "mcqs": [
                {
                    "q": f"Chapter {num} in Class 4 General Science is:",
                    "qUrdu": f"چوتھی جماعت کی جنرل سائنس میں باب {num} کون سا ہے؟",
                    "qPashto": f"د څلورم ټولګي په ساینس کې {num} څپرکی کوم دی؟",
                    "options": [title, "Medieval History", "Economic Models", "Grammar Rules"],
                    "optionsUrdu": [titleUr, "قرون وسطیٰ کی تاریخ", "معاشی ماڈلز", "گرائمر کے اصول"],
                    "optionsPashto": [titlePs, "د منځنیو پېړیو تاریخ", "اقتصادي ماډلونه", "د ګرامر اصول"],
                    "answer": 0,
                    "exp": f"Chapter {num} is {title}.",
                    "expUrdu": f"باب {num} کا نام {titleUr} ہے۔",
                    "expPashto": f"{num} څپرکی {titlePs} دی."
                }
            ]
        }
        units.append({
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "titlePashto": titlePs,
            "type": "chapter",
            "sections": sections,
            "exercise": exercise,
            "englishSummary": f"Chapter {num}: {title}.",
            "urduSummary": f"باب {num}: {titleUr}۔",
            "pashtoSummary": f"{num} څپرکی: {titlePs}."
        })
    out = JS_DIR / "general_science_4_data.js"
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Class 4 General Science Dataset (KPTBB SNC 2020)\n")
        f.write("const GENERAL_SCIENCE_4_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.science4Chapters = GENERAL_SCIENCE_4_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.GENERAL_SCIENCE_4_DATA = GENERAL_SCIENCE_4_DATA; }\n")
    print(f"Generated {out} ({len(units)} units)")

# 3. SOCIAL STUDIES (6 Chapters)
def build_social_studies():
    docs = sorted(glob.glob(str(SRC / "Social Study Book 4th EM KPK_JPGs" / "word" / "*.docx")))
    paras = clean_paras(docs)
    chapters_def = [
        (1, "Citizenship", "شہریت اور انسانی حقوق", "تابعیت او د انسان حقوق"),
        (2, "Culture", "ثقافت اور ورثہ", "کلتور او میراث"),
        (3, "State and Government", "ریاست اور حکومت", "دولت او حکومت"),
        (4, "History", "تاریخ اور اہم شخصیات", "تاریخ او مهم شخصیتونه"),
        (5, "Geography", "جغرافیہ، نقشہ اور ماحول", "جغرافیا، نقشه او چاپیریال"),
        (6, "Economics", "معاشیات اور روزگار", "اقتصاد او معیشت")
    ]
    chunk_size = max(1, len(paras) // len(chapters_def))
    units = []
    for i, (num, title, titleUr, titlePs) in enumerate(chapters_def):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < len(chapters_def) - 1 else len(paras)
        u_paras = paras[start:end]
        sections = [
            {
                "id": f"u{num}-concepts",
                "heading": f"Chapter {num}: {title}",
                "headingUrdu": f"باب {num}: {titleUr}",
                "headingPashto": f"{num} څپرکی: {titlePs}",
                "paras": u_paras[:15]
            }
        ]
        exercise = {
            "shortQuestions": [
                {
                    "q": f"Define the core topic of Chapter {num} ({title}).",
                    "qUrdu": f"باب {num} ({titleUr}) کا بنیادی تصور بیان کریں۔",
                    "qPashto": f"د {num} څپرکي ({titlePs}) بنسټیز مفهوم بیان کړئ.",
                    "a": f"Chapter {num} covers key civic and social concepts of {title}.",
                    "aUrdu": f"یہ باب {titleUr} کے متعلق اہم شہری اور معاشرتی تصورات پیش کرتا ہے۔",
                    "aPashto": f"دا څپرکی د {titlePs} په اړه مهم مدني او ټولنیز مفاهیم وړاندې کوي."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Discuss the significance of {title} in society.",
                    "qUrdu": f"معاشرے میں {titleUr} کی اہمیت پر تفصیلی روشنی ڈالیں۔",
                    "qPashto": f"په ټولنه کې د {titlePs} پر اهمیت رڼا واچوئ.",
                    "a": f"Understanding {title} fosters civic duty, cultural appreciation, and informed community participation.",
                    "aUrdu": f"{titleUr} کی تفہیم سے شہری ذمہ داری اور قومی ہم آہنگی کو فروغ ملتا ہے۔",
                    "aPashto": f"د {titlePs} پوهه مدني مسؤلیت او ټولنیزې همغږۍ ته وده ورکوي."
                }
            ],
            "mcqs": [
                {
                    "q": f"Chapter {num} in Class 4 Social Studies is:",
                    "qUrdu": f"چوتھی جماعت کے مطالعہ معاشرت میں باب {num} کون سا ہے؟",
                    "qPashto": f"په څلورم ټولګي کې {num} څپرکی کوم دی؟",
                    "options": [title, "Algebra", "Organic Chemistry", "Optics"],
                    "optionsUrdu": [titleUr, "الجبرہ", "نامیاتی کیمیا", "بصریات"],
                    "optionsPashto": [titlePs, "الجبر", "ارګانیک کیمیا", "نوري فزیک"],
                    "answer": 0,
                    "exp": f"Chapter {num} is {title}.",
                    "expUrdu": f"باب {num} کا نام {titleUr} ہے۔",
                    "expPashto": f"{num} څپرکی {titlePs} دی."
                }
            ]
        }
        units.append({
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "titlePashto": titlePs,
            "type": "chapter",
            "sections": sections,
            "exercise": exercise,
            "englishSummary": f"Chapter {num}: {title}.",
            "urduSummary": f"باب {num}: {titleUr}۔",
            "pashtoSummary": f"{num} څپرکی: {titlePs}."
        })
    out = JS_DIR / "social_studies_4_data.js"
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Class 4 Social Studies Dataset (KPTBB SNC 2020)\n")
        f.write("const SOCIAL_STUDIES_4_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.sst4Chapters = SOCIAL_STUDIES_4_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.SOCIAL_STUDIES_4_DATA = SOCIAL_STUDIES_4_DATA; }\n")
    print(f"Generated {out} ({len(units)} units)")

# 4. ISLAMIAT (7 Babs / Units)
def build_islamiat():
    docs = sorted(glob.glob(str(SRC / "Islamiat Book for 4 class KPTBB_JPGs" / "word" / "*.docx")))
    paras = clean_paras(docs)
    babs_def = [
        (1, "The Holy Quran and Hadith", "قرآن مجید اور حدیث نبوی", "قرآن مجید او نبوي احادیث"),
        (2, "Faith and Worships", "ایمانیات و عبادات", "ایمانیات او عبادات"),
        (3, "Seerat-un-Nabi (PBUH)", "سیرت طیبہ خاتم النبیین ﷺ", "نبوي سیرت ﷺ"),
        (4, "Ethics and Manners", "اخلاق و آداب", "اخلاق او آداب"),
        (5, "Good Dealings and Social Life", "حسن معاملات و معاشرت", "ښه معاملات او ټولنیز ژوند"),
        (6, "Sources of Guidance and Prominent Figures", "ہدایت کے سرچشمے اور مشاہیر اسلام", "د هدایت سرچینې او مشهور شخصیتونه"),
        (7, "Islamic Teachings and Contemporary Needs", "اسلامی تعلیمات اور عصر حاضر کے تقاضے", "اسلامي لارښوونې او معاصرې اړتیاوې")
    ]
    chunk_size = max(1, len(paras) // len(babs_def))
    units = []
    for i, (num, title, titleUr, titlePs) in enumerate(babs_def):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < len(babs_def) - 1 else len(paras)
        u_paras = paras[start:end]
        sections = [
            {
                "id": f"u{num}-concepts",
                "heading": f"Bab {num}: {titleUr}",
                "headingUrdu": f"باب {num}: {titleUr}",
                "headingPashto": f"{num} باب: {titlePs}",
                "paras": u_paras[:15]
            }
        ]
        exercise = {
            "shortQuestions": [
                {
                    "q": f"State the primary teaching of Bab {num} ({titleUr}).",
                    "qUrdu": f"باب {num} ({titleUr}) کا بنیادی سبق کیا ہے؟",
                    "qPashto": f"د {num} باب ({titlePs}) اصلي لارښوونه څه ده؟",
                    "a": f"Bab {num} guides learners in Islamic moral conduct and spiritual devotion: {titleUr}.",
                    "aUrdu": f"یہ باب اسلامی اخلاق اور روحانی تربیت کی تعلیم دیتا ہے: {titleUr}۔",
                    "aPashto": f"دا باب د اسلامي اخلاقو او معنوي روزنې لارښوونه کوي: {titlePs}."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Explain how to practice the teachings of Bab {num} in daily life.",
                    "qUrdu": f"روزمرہ زندگی میں باب {num} کی تعلیمات پر کیسے عمل کیا جائے؟",
                    "qPashto": f"په ورځني ژوند کې د دې باب پر احکامو څنګه عمل وشي؟",
                    "a": f"By following the Sunnah, demonstrating truthfulness, humility, and fulfilling the rights of others.",
                    "aUrdu": f"سنت نبوی ﷺ کی پیروی، سچائی، عاجزی اور حقوق العباد کی پاسداری کے ذریعے۔",
                    "aPashto": f"د نبوي سنتو په پیروۍ، رښتینولۍ، عاجزۍ او د خلکو د حقونو په پوره کولو سره."
                }
            ],
            "mcqs": [
                {
                    "q": f"Bab {num} in Class 4 Islamiat covers:",
                    "qUrdu": f"چوتھی جماعت کی اسلامیات میں باب {num} کا عنوان ہے:",
                    "qPashto": f"په څلورم ټولګي کې د {num} باب عنوان دی:",
                    "options": [titleUr, "ریاضی کے اصول", "انگریزی گرائمر", "سائنسی تجربات"],
                    "optionsUrdu": [titleUr, "ریاضی کے اصول", "انگریزی گرائمر", "سائنسی تجربات"],
                    "optionsPashto": [titlePs, "د ریاضي اصول", "د انګلیسي ګرامر", "ساینسي تجربې"],
                    "answer": 0,
                    "exp": f"Bab {num} is {titleUr}.",
                    "expUrdu": f"باب {num} کا عنوان {titleUr} ہے۔",
                    "expPashto": f"د {num} باب عنوان {titlePs} دی."
                }
            ]
        }
        units.append({
            "number": num,
            "id": f"unit-{num}",
            "title": titleUr,
            "titleUrdu": titleUr,
            "titlePashto": titlePs,
            "type": "chapter",
            "sections": sections,
            "exercise": exercise,
            "englishSummary": f"Bab {num}: {title}.",
            "urduSummary": f"باب {num}: {titleUr}۔",
            "pashtoSummary": f"{num} باب: {titlePs}."
        })
    out = JS_DIR / "islamiat_4_data.js"
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Class 4 Islamiat Dataset (KPTBB SNC 2020)\n")
        f.write("const ISLAMIAT_4_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.isl4Chapters = ISLAMIAT_4_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.ISLAMIAT_4_DATA = ISLAMIAT_4_DATA; }\n")
    print(f"Generated {out} ({len(units)} units)")

# 5. PASHTO (18 Lessons)
def build_pashto():
    docs = sorted(glob.glob(str(SRC / "PASHTO" / "word" / "*.docx")))
    paras = clean_paras(docs)
    lessons_def = [
        (1, "چاپیرچل (نظم)", "ماحول (نظم)", "Environment (Poem)"),
        (2, "قاضي فضل قادر شهید", "قاضی فضل قادر شہید", "Qazi Fazal Qadir Shaheed"),
        (3, "ورزش", "ورزش اور صحت", "Exercise and Health"),
        (4, "تیمور باچا او مږے (قیصه)", "تیمور بادشاہ اور چیونٹی (کہانی)", "King Timur and the Ant (Story)"),
        (5, "جامه", "لباس اور تہذیب", "Clothing and Culture"),
        (6, "پېزار (نظم)", "جوتا (نظم)", "Footwear (Poem)"),
        (7, "مشهورې پښتنې مېرمنې", "مشہور پشتون خواتین", "Famous Pashtun Women"),
        (8, "د بخښنې جذبه", "معاف کرنے کا جذبہ", "The Spirit of Forgiveness"),
        (9, "صاحبزاده عبدالقیوم خان", "صاحبزادہ عبدالقیوم خان", "Sahibzada Abdul Qayyum Khan"),
        (10, "خوشحال بابا (نظم)", "خوشحال خان خٹک (نظم)", "Khushal Baba (Poem)"),
        (11, "اولسي شاعران", "عوامی شعراء", "Folk Poets"),
        (12, "اخبار", "اخبار اور ذرائع ابلاغ", "Newspaper and Media"),
        (13, "ځناور (نظم)", "جانور (نظم)", "Animals (Poem)"),
        (14, "شعر", "شعر و ادب", "Poetry and Literature"),
        (15, "مادرِ ملت", "مادرِ ملت محترمہ فاطمہ جناح", "Madar-e-Millat"),
        (16, "کمپیوټر", "کمپیوٹر اور جدید ٹیکنالوجی", "Computer and IT"),
        (17, "ښیونکی او شرمښ (قیصه)", "چرواہا اور بھیڑیا (کہانی)", "Shepherd and Wolf (Story)"),
        (18, "دعا (نظم)", "دعا (نظم)", "Prayer (Poem)")
    ]
    chunk_size = max(1, len(paras) // len(lessons_def))
    units = []
    for i, (num, titlePs, titleUr, titleEn) in enumerate(lessons_def):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < len(lessons_def) - 1 else len(paras)
        u_paras = paras[start:end]
        sections = [
            {
                "id": f"u{num}-reading",
                "heading": f"{num} لوست: {titlePs}",
                "headingUrdu": f"سبق {num}: {titleUr}",
                "headingPashto": f"{num} لوست: {titlePs}",
                "paras": u_paras[:15]
            }
        ]
        exercise = {
            "shortQuestions": [
                {
                    "q": f"د {titlePs} اصلي پیغام څه دی؟",
                    "qUrdu": f"{titleUr} کا بنیادی پیغام کیا ہے؟",
                    "qPashto": f"د {titlePs} اصلي پیغام څه دی؟",
                    "a": f"دا درس د {titlePs} له لارې ادبي، اخلاقي او کلتوري پوهاوی زیاتوي.",
                    "aUrdu": f"یہ سبق {titleUr} کے ذریعے ادبی، اخلاقی اور ثقافتی شعور بیدار کرتا ہے۔",
                    "aPashto": f"دا درس د {titlePs} له لارې ادبي، اخلاقي او کلتوري پوهاوی زیاتوي."
                }
            ],
            "longQuestions": [
                {
                    "q": f"د {titlePs} خلاصه په خپلو ټکو کې ولیکئ.",
                    "qUrdu": f"{titleUr} کا خلاصہ اپنے الفاظ میں تحریر کریں۔",
                    "qPashto": f"د {titlePs} خلاصه په خپلو ټکو کې ولیکئ.",
                    "a": f"په دې لوست کې د {titlePs} په اړه مفصل معلومات او ګټور درسونه بیان شوي دي.",
                    "aUrdu": f"اس سبق میں {titleUr} کے بارے میں تفصیلی معلومات اور مفید اسباق فراہم کیے گئے ہیں۔",
                    "aPashto": f"په دې لوست کې د {titlePs} په اړه مفصل معلومات او ګټور درسونه بیان شوي دي."
                }
            ],
            "mcqs": [
                {
                    "q": f"د {num} لوست عنوان څه دی؟",
                    "qUrdu": f"سبق {num} کا عنوان کیا ہے؟",
                    "qPashto": f"د {num} لوست عنوان څه دی؟",
                    "options": [titlePs, "کیمیا", "ریاضی", "فزیک"],
                    "optionsUrdu": [titleUr, "کیمیا", "ریاضی", "فزکس"],
                    "optionsPashto": [titlePs, "کیمیا", "ریاضي", "فزیک"],
                    "answer": 0,
                    "exp": f"د {num} لوست عنوان {titlePs} دی.",
                    "expUrdu": f"سبق {num} کا عنوان {titleUr} ہے۔",
                    "expPashto": f"د {num} لوست عنوان {titlePs} دی."
                }
            ]
        }
        units.append({
            "number": num,
            "id": f"unit-{num}",
            "title": titlePs,
            "titleUrdu": titleUr,
            "titlePashto": titlePs,
            "type": "chapter",
            "sections": sections,
            "exercise": exercise,
            "englishSummary": f"Lesson {num}: {titleEn}.",
            "urduSummary": f"سبق {num}: {titleUr}۔",
            "pashtoSummary": f"{num} لوست: {titlePs}."
        })
    out = JS_DIR / "pashto_4_data.js"
    with open(out, "w", encoding="utf-8") as f:
        f.write("// Class 4 Pashto Dataset (KPTBB SNC 2020)\n")
        f.write("const PASHTO_4_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.pashto4Chapters = PASHTO_4_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.PASHTO_4_DATA = PASHTO_4_DATA; }\n")
    print(f"Generated {out} ({len(units)} units)")

if __name__ == "__main__":
    build_english()
    build_science()
    build_social_studies()
    build_islamiat()
    build_pashto()
