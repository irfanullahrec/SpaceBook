# Script to generate datasets for Class 9th missing subjects
import docx
import json
import os
import sys

def build_gen_science():
    folder = r"D:\SpaceBook\Books\9th\9th General Science\Word"
    paras = []
    for f in sorted(os.listdir(folder)):
        if f.endswith(".docx"):
            doc = docx.Document(os.path.join(folder, f))
            paras.extend([p.text.strip() for p in doc.paragraphs if p.text.strip()])
    
    bounds = [
        (1, "Introduction and Role of Science", "تعارف اور سائنس کا کردار", 106, 560),
        (2, "Chemistry and Life", "کیمسٹری اور زندگی", 560, 1161),
        (3, "Health, Diseases and Prevention", "صحت، بیماریاں اور بچاؤ", 1161, 2402),
        (4, "Population and Environment", "آبادی اور ماحول", 2402, 2874),
        (5, "Energy Sources", "توانائی کے ذرائع", 2874, len(paras))
    ]
    
    units = []
    for num, title, titleUr, start, end in bounds:
        u_paras = paras[start:end]
        clean_p = [p for p in u_paras if not any(w in p.lower() for w in ["awaz e inqilab", "camscanner", "download pdf", "whatsapp", "not for sale"]) and len(p) > 2]
        sec_paras = clean_p[:40]
        full_text = "\n\n".join(sec_paras[:15])
        
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Core Concepts & Principles",
                    "headingUrdu": "بنیادی تصورات و اصول",
                    "text": full_text,
                    "paras": sec_paras[:12]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"Explain the primary objective of {title}.", "a": f"{title} focuses on the foundational scientific principles, real-world applications in society, and analytical techniques relevant to 9th grade curriculum."},
                    {"q": f"List three major concepts discussed in Unit {num}.", "a": "1. Fundamental definitions and scope.\n2. Applications in daily life and technological development.\n3. Ethical and environmental dimensions."}
                ],
                "longQuestions": [
                    {"q": f"Provide a comprehensive analysis of {title} with contextual examples.", "a": f"In this unit, students explore the systematic development of {title}, examining how empirical evidence, technological progress, and social needs interact to improve human welfare."}
                ],
                "mcqs": [
                    {"q": f"What is the central focus of Unit {num} ({title})?", "options": ["Scientific foundations and principles", "Artistic drawing", "Language phonetics", "Physical exercises"], "answer": 0, "exp": f"Unit {num} covers scientific principles and real-world implications of {title}."},
                    {"q": "Scientific knowledge is characterized by being:", "options": ["Systematic and empirical", "Purely speculative", "Unchangeable dogma", "Random guess"], "answer": 0, "exp": "Science relies on verifiable observation, experimentation, and critical reasoning."}
                ]
            },
            "englishSummary": f"Unit {num} explores {title}, detailing core scientific foundations, real-world applications, and problem-solving perspectives for Grade 9 students.",
            "urduSummary": f"یہ یونٹ {titleUr} کے بنیادی تصورات، اطلاقات اور سائنسی اصولوں کی وضاحت کرتا ہے۔"
        }
        units.append(unit_obj)
    
    out_file = r"D:\SpaceBook\SpaceBook Web\js\general_science_9_data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Class 9 General Science Dataset (KPTBB)\n")
        f.write("const GENERAL_SCIENCE_9_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.genSci9Chapters = GENERAL_SCIENCE_9_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.GENERAL_SCIENCE_9_DATA = GENERAL_SCIENCE_9_DATA; }\n")
    print("Generated general_science_9_data.js!")

def build_hpe():
    folder = r"D:\SpaceBook\Books\9th\9th  HPE\Word"
    paras = []
    for f in sorted(os.listdir(folder)):
        if f.endswith(".docx"):
            doc = docx.Document(os.path.join(folder, f))
            paras.extend([p.text.strip() for p in doc.paragraphs if p.text.strip()])
            
    bounds = [
        (1, "Non-Contagious Diseases (Obesity & Diabetes)", "غیر متعدی امراض (موٹاپا اور ذیابیطس)", 151, 311),
        (2, "Respiratory System", "نظام تنفس", 311, 418),
        (3, "Malnutrition", "ناقص غذا", 418, 536),
        (4, "Narcotics & Opium", "منشیات (افیون)", 536, 619),
        (5, "Landsliding & First Aid", "زمین کا کھسکاؤ اور ابتدائی طبی امداد", 619, 689),
        (6, "Bullying & Violence Prevention", "غنڈہ گردی اور انسداد تشدد", 689, 945),
        (7, "Biomechanical Principles", "بائیومکینیکل اصول", 945, 1058),
        (8, "Sports Skills & Strategies", "کھیلوں کی مہارتیں اور حکمت عملیاں", 1058, len(paras))
    ]
    
    units = []
    for num, title, titleUr, start, end in bounds:
        u_paras = paras[start:end]
        clean_p = [p for p in u_paras if not any(w in p.lower() for w in ["awaz e inqilab", "camscanner", "download pdf", "whatsapp", "not for sale", "youtube"]) and len(p) > 2]
        sec_paras = clean_p[:40]
        full_text = "\n\n".join(sec_paras[:15])
        
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Textbook Theory & Guidelines",
                    "headingUrdu": "درسی متن و ہدایات",
                    "text": full_text,
                    "paras": sec_paras[:12]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"{titleUr} کی تعریف اور اہمیت بیان کریں۔", "a": f"اس باب میں {titleUr} کی بنیادی خصوصیات، اس کے صحت اور تندرستی پر اثرات اور اس کے متعلق ضروری احتیاطی تدابیر بیان کی گئی ہیں۔"},
                    {"q": f"باب {num} کے دو اہم نکات بیان کریں۔", "a": "1. حفظان صحت اور جسمانی تندرستی کے اصول۔\n2. کھیل اور روزمرہ زندگی میں مثبت عادات اپنانا۔"}
                ],
                "longQuestions": [
                    {"q": f"{titleUr} پر تفصیلی نوٹ لکھیں۔", "a": f"اس باب کے مطالعے سے طلبہ {titleUr} کے سائنسی اور عملی پہلوؤں کو سمجھ کر اپنی روزمرہ زندگی میں تندرستی اور حفاظت کے رہنما اصول اپنا سکتے ہیں۔"}
                ],
                "mcqs": [
                    {"q": f"باب {num} ({titleUr}) کا بنیادی موضوع کیا ہے؟", "options": ["صحت و جسمانی تعلیم", "الجبرا", "تاریخی واقعات", "کیمیائی تعاملات"], "answer": 0, "exp": f"یہ باب صحت و جسمانی تعلیم کے عنوان {titleUr} کا احاطہ کرتا ہے۔"},
                    {"q": "باقاعدہ ورزش اور مناسب غذا کا کیا فائدہ ہے؟", "options": ["قوت مدافعت اور جسمانی چستی میں اضافہ", "سستی اور کاہلی", "بیماریوں کا خطرہ بڑھنا", "کوئی اثر نہیں"], "answer": 0, "exp": "صحت بخش طرز زندگی تندرستی اور لمبی عمر کی ضمانت ہے۔"}
                ]
            },
            "englishSummary": f"Unit {num} covers {title}, offering health guidelines, anatomical understanding, and practical physical wellness skills.",
            "urduSummary": f"یہ یونٹ {titleUr} کے متعلق درسی مواد، صحت مند زندگی کے رہنما اصول اور کھیلوں کی عملی مہارتیں فراہم کرتا ہے۔"
        }
        units.append(unit_obj)
        
    out_file = r"D:\SpaceBook\SpaceBook Web\js\hpe_9_data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Class 9 HPE Dataset (KPTBB)\n")
        f.write("const HPE_9_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.hpe9Chapters = HPE_9_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.HPE_9_DATA = HPE_9_DATA; }\n")
    print("Generated hpe_9_data.js!")

def build_drawing():
    folder = r"D:\SpaceBook\Books\9th\9th Drawing\Word"
    paras = []
    for f in sorted(os.listdir(folder)):
        if f.endswith(".docx"):
            doc = docx.Document(os.path.join(folder, f))
            paras.extend([p.text.strip() for p in doc.paragraphs if p.text.strip()])
            
    bounds = [
        (1, "Fundamentals of Drawing, Painting and Design", "ڈرائنگ، پینٹنگ اور ڈیزائن کے بنیادی اصول", 109, 420),
        (2, "Elements of Art and Principles of Design", "آرٹ کے عناصر اور ڈیزائن کے اصول", 420, 923),
        (3, "Art Appreciation & Cultural Heritage", "فنون لطیفہ کی تحسین اور ثقافتی ورثہ", 923, 1319),
        (4, "Life Skills Through Art Education", "آرٹ کی تعلیم کے ذریعے عملی زندگی کی مہارتیں", 1319, len(paras))
    ]
    
    units = []
    for num, title, titleUr, start, end in bounds:
        u_paras = paras[start:end]
        clean_p = [p for p in u_paras if not any(w in p.lower() for w in ["awaz e inqilab", "camscanner", "download pdf", "whatsapp", "not for sale"]) and len(p) > 2]
        sec_paras = clean_p[:40]
        full_text = "\n\n".join(sec_paras[:15])
        
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Techniques & Artistic Studio Practice",
                    "headingUrdu": "تکنیک اور عملی مشقیں",
                    "text": full_text,
                    "paras": sec_paras[:12]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"State the primary concepts of {title}.", "a": f"This chapter covers foundational techniques, visual appreciation, materials and creative execution for {title}."},
                    {"q": f"What materials and media are essential in Unit {num}?", "a": "Pencils (HB to 6B), drawing sheets, wet and dry mediums, geometric tools, and color palettes."}
                ],
                "longQuestions": [
                    {"q": f"Discuss step-by-step techniques and aesthetic principles in {title}.", "a": f"Students learn perspective drawing, shading gradients, color harmony, and composition to produce expressive artwork."}
                ],
                "mcqs": [
                    {"q": f"What is the primary study in Chapter {num} ({title})?", "options": ["Artistic mediums, design principles, and composition", "Numerical algebra", "Chemical equations", "Microbiology"], "answer": 0, "exp": f"Chapter {num} teaches creative techniques in {title}."},
                    {"q": "Which color combination represents primary colors in art?", "options": ["Red, Yellow, Blue", "Green, Orange, Purple", "Black, White, Grey", "Brown, Pink, Teal"], "answer": 0, "exp": "Red, Yellow, and Blue cannot be created by mixing other colors."}
                ]
            },
            "englishSummary": f"Chapter {num} introduces {title}, training students in visual perception, creative media, and artistic studio skills.",
            "urduSummary": f"یہ باب {titleUr} کے فنکارانہ اصولوں، تکنیکوں اور عملی ڈرائنگ کی مہارتوں کی وضاحت کرتا ہے۔"
        }
        units.append(unit_obj)
        
    out_file = r"D:\SpaceBook\SpaceBook Web\js\drawing_9_data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Class 9 Art & Model Drawing Dataset (KPTBB)\n")
        f.write("const DRAWING_9_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.drawing9Chapters = DRAWING_9_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.DRAWING_9_DATA = DRAWING_9_DATA; }\n")
    print("Generated drawing_9_data.js!")

def build_islamiat_ikhtiari():
    folder = r"D:\SpaceBook\Books\9th\9th Islamiat Ikhtiari\Word"
    paras = []
    for f in sorted(os.listdir(folder)):
        if f.endswith(".docx"):
            doc = docx.Document(os.path.join(folder, f))
            paras.extend([p.text.strip() for p in doc.paragraphs if p.text.strip()])
            
    bounds = [
        (1, "The Holy Quran (Revelation & Preservation)", "باب اول: قرآن مجید (تعارف، وحی، حفاظت)", 145, 949),
        (2, "Worships in Islam (Ibadat)", "باب دوم: عبادات (نماز، زکوٰۃ، روزہ، حج)", 949, 1294),
        (3, "Seerat of the Holy Prophet (PBUH)", "باب سوم: سیرت رسول اکرم ﷺ", 1294, 1800),
        (4, "Selected Quranic Verses with Translation", "باب چہارم: منتخب قرآنی آیات مع ترجمہ و تشریح", 1800, 2200),
        (5, "Hadith and Sunnah (Foundations & Ethics)", "باب پنجم: حدیث اور سنت (حجیت، تدوین، اخلاق)", 2200, 2737),
        (6, "Islamic Civilization & Contributions of Muslims", "باب ششم: اسلامی تہذیب و تمدن اور مسلمانوں کے کارنامے", 2737, 3478),
        (7, "Arabic Language & Grammar Fundamentals", "باب ہفتم: عربی زبان و قواعد", 3478, len(paras))
    ]
    
    units = []
    for num, title, titleUr, start, end in bounds:
        u_paras = paras[start:end]
        clean_p = [p for p in u_paras if not any(w in p.lower() for w in ["awaz e inqilab", "camscanner", "download pdf", "whatsapp", "not for sale"]) and len(p) > 2]
        sec_paras = clean_p[:40]
        full_text = "\n\n".join(sec_paras[:15])
        
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "متن و دینی رہنمائی",
                    "headingUrdu": "متن و دینی رہنمائی",
                    "text": full_text,
                    "paras": sec_paras[:12]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"{titleUr} کے اہم نکات بیان کریں۔", "a": f"اس باب میں {titleUr} کے متعلق قرآن و سنت کی روشنی میں بنیادی تعلیمات اور احکام واضح کیے گئے ہیں۔"},
                    {"q": f"باب {num} سے حاصل ہونے والے دو عملی اسباق تحریر کریں۔", "a": "1. اخلاص نیت اور اطاعت الٰہی۔\n2. سیرت طیبہ اور اسلامی تعلیمات پر خلوص دل سے عمل پیرا ہونا۔"}
                ],
                "longQuestions": [
                    {"q": f"{titleUr} پر جامع و مفصل مضمون تحریر کریں۔", "a": f"اس باب کا مفصل مطالعہ اسلامی عقائد، عبادات اور اخلاقیات کو زندگی کے تمام شعبوں میں اپنانے کا شعور بخشتا ہے۔"}
                ],
                "mcqs": [
                    {"q": f"باب {num} ({titleUr}) کا بنیادی محور کیا ہے؟", "options": ["اسلامی علوم و تعلیمات", "سائنسی تجربات", "جغرافیائی سرحدیں", "شاعری کی بحور"], "answer": 0, "exp": f"یہ باب اسلامیات اختیاری کے تحت {titleUr} کا تفصیلی جائزہ پیش کرتا ہے۔"},
                    {"q": "قرآن مجید اور سنت نبوی ﷺ کی اطاعت کا کیا مقام ہے؟", "options": ["دین اسلام کی اساس اور ہدایت کا سرچشمہ", "اختیاری معاملہ", "صرف ماضی کے لیے", "کوئی خاص حیثیت نہیں"], "answer": 0, "exp": "قرآن و سنت تمام مسلمانوں کے لیے زندگی کے تمام شعبوں میں حتمی رہنمائی فراہم کرتے ہیں۔"}
                ]
            },
            "englishSummary": f"Unit {num} covers {title}, focusing on Quranic studies, Islamic jurisprudence, ethics, and civilizational values.",
            "urduSummary": f"یہ باب {titleUr} کے احکام، اسباق اور اسلامی تعلیمات کی مفصل تشریح پیش کرتا ہے۔"
        }
        units.append(unit_obj)
        
    out_file = r"D:\SpaceBook\SpaceBook Web\js\islamiat_ikhtiari_9_data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Class 9 Islamiat Ikhtiari Dataset (KPTBB)\n")
        f.write("const ISLAMIAT_IKHTIARI_9_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.islopt9Chapters = ISLAMIAT_IKHTIARI_9_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.ISLAMIAT_IKHTIARI_9_DATA = ISLAMIAT_IKHTIARI_9_DATA; }\n")
    print("Generated islamiat_ikhtiari_9_data.js!")

def build_mutalia_quran():
    # 6 Units for Mutalia-e-Quran 9th (covering selected Surahs from Surah An-Nur to early Medinan surahs)
    surahs = [
        (1, "Surah Maryam (سورة مريم)", "سورة مريم", "Surah Maryam covers the miracles of Prophet Zakariya, Yahya, and Isa (AS), emphasizing Tawheed and Allah's majesty.", "سورة مريم میں حضرت زکریا، یحییٰ اور عیسیٰ علیہ السلام کے واقعات اور توحید کا بیان ہے۔"),
        (2, "Surah Ta-Ha (سورة طه)", "سورة طه", "Surah Ta-Ha recounts the detailed call of Prophet Musa (AS), his confrontation with Pharaoh, and patience in conveying the divine message.", "سورة طہ میں حضرت موسیٰ علیہ السلام کے واقعات، فرعون سے مکالمہ اور صبر و استقامت کا ذکر ہے۔"),
        (3, "Surah Al-Anbiya (سورة الأنبياء)", "سورة الأنبياء", "Surah Al-Anbiya details the unified mission of the prophets, the creation of heavens and earth, and the Day of Judgment.", "سورة الانبیاء میں انبیاء کرام کی دعوت، کائنات کی تخلیق اور روز جزا کے احوال بیان ہوئے ہیں۔"),
        (4, "Surah Al-Hajj (سورة الحج)", "سورة الحج", "Surah Al-Hajj details the rites of pilgrimage, sacrifice, struggle for truth, and moral purification.", "سورة الحج میں مناسک حج، قربانی، تقویٰ اور حق کے راستے میں جہاد کے اصول بیان کیے گئے ہیں۔"),
        (5, "Surah Al-Mu'minun (سورة المؤمنون)", "سورة المؤمنون", "Surah Al-Mu'minun outlines the qualities of successful believers, stages of human creation, and accountability.", "سورة المؤمنون میں کامیاب اہل ایمان کی صفات، انسان کے مراحل تخلیق اور آخرت میں جوابدہی کا بیان ہے۔"),
        (6, "Surah An-Nur (سورة النور)", "سورة النور", "Surah An-Nur highlights social ethics, modesty, family values, and the famous Verse of Light (Ayat an-Nur).", "سورة النور میں معاشرتی اخلاقیات، پردہ، عفت و عصمت اور آیت نور کے مضامین شامل ہیں۔")
    ]
    
    units = []
    for num, title, titleUr, enSum, urSum in surahs:
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "تعارف سورہ مبارکہ و مضامین",
                    "headingUrdu": "تعارف سورہ مبارکہ و مضامین",
                    "text": f"یہ سورت مبارکہ قرآن مجید کے اہم ترین پیغامات پر مشتمل ہے۔ اس میں {titleUr} کے بنیادی مضامین، مرکزی خیال، شان نزول اور قرآنی احکامات کا احاطہ کیا گیا ہے۔ طلبہ کو چاہیے کہ وہ آیات مبارکہ کو تجوید کے ساتھ پڑھیں، ان کے اردو ترجمے پر غور کریں اور روزمرہ زندگی میں ان قرآنی ہدایات کو عملی طور پر اپنائیں۔",
                    "paras": [
                        f"{titleUr} کا تعارف اور تاریخی پس منظر۔",
                        "سورت کے اہم موضوعات: توحید، رسالت، آخرت اور انسانی اخلاق۔",
                        "قرآنی قصص اور ان سے حاصل ہونے والے بصیرت افروز اسباق۔",
                        "عملی زندگی میں قرآنی تعلیمات کے نفاذ کے رہنما اصول۔"
                    ]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"{titleUr} کے بنیادی مضامین اور مرکزی خیال تحریر کریں۔", "a": f"{titleUr} میں اللہ تعالیٰ کی وحدانیت، انبیاء کی دعوت اور اخلاقی و روحانی تزکیہ کا مفصل تذکرہ موجود ہے۔"},
                    {"q": f"{titleUr} سے حاصل ہونے والے دو اہم اسباق بیان کریں۔", "a": "1. ہر حال میں اللہ تعالیٰ پر بھروسا اور دعا کا اہتمام۔\n2. حق پر استقامت اور پاکیزہ طرز زندگی اپنانا۔"}
                ],
                "longQuestions": [
                    {"q": f"{titleUr} کے پس منظر، مضامین اور احکامات پر تفصیلی روشنی ڈالیں۔", "a": f"اس سورت کا فہم طالب علموں کو قرآنی حکمت، ایمانی پختگی اور اسلامی طرز عمل سے آراستہ کرتا ہے۔"}
                ],
                "mcqs": [
                    {"q": f"{titleUr} کا مرکزی پیغام کیا ہے؟", "options": ["ایمان باللہ، اخلاق اور ہدایت قرآنی", "صرف قواعد زبان", "تجارت کے اصول", "قدیم داستانیں"], "answer": 0, "exp": "قرآن مجید کی تمام سورتیں انسان کی فکری و اخلاقی رہنمائی کا سرچشمہ ہیں۔"},
                    {"q": "قرآن مجید کے مطالعے کا بنیادی مقصد کیا ہے؟", "options": ["فہم، تدبر اور عملی زندگی میں نفاذ", "محض زبانی تلاوت بغیر سمجھ بوجھ", "دنیاوی شہرت", "کوئی خاص مقصد نہیں"], "answer": 0, "exp": "قرآن کریم تدبر، فہم اور عمل کے لیے نازل کیا گیا ہے۔"}
                ]
            },
            "englishSummary": enSum,
            "urduSummary": urSum
        }
        units.append(unit_obj)
        
    out_file = r"D:\SpaceBook\SpaceBook Web\js\mutalia_quran_9_data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Class 9 Mutalia-e-Quran Dataset (KPTBB)\n")
        f.write("const MUTALIA_QURAN_9_DATA = " + json.dumps(units, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) { DATA.quran9Chapters = MUTALIA_QURAN_9_DATA; }\n")
        f.write("if (typeof window !== 'undefined') { window.MUTALIA_QURAN_9_DATA = MUTALIA_QURAN_9_DATA; }\n")
    print("Generated mutalia_quran_9_data.js!")

if __name__ == "__main__":
    build_gen_science()
    build_hpe()
    build_drawing()
    build_islamiat_ikhtiari()
    build_mutalia_quran()
    print("All 5 datasets generated successfully!")
