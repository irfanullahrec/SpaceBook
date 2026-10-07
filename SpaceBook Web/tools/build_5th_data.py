# Script to generate datasets for Class 5th all 8 subjects from D:\SpaceBook\Books\5th
import docx
import json
import os
import sys

base_dir = r"D:\SpaceBook\Books\5th"
out_dir = r"D:\SpaceBook\SpaceBook Web\js"

def clean_paragraphs(doc_paths):
    watermarks = [
        "awaz e inqilab", "awazeinqilab", "camscanner", "download pdf", "download millions",
        "whatsapp", "not for sale", "nts, fts, css", "templates", "ڈاون لوڈ", "کاپی رائٹ"
    ]
    paras = []
    for dp in doc_paths:
        if os.path.exists(dp):
            try:
                doc = docx.Document(dp)
                for p in doc.paragraphs:
                    t = p.text.strip()
                    if len(t) > 3 and not any(w in t.lower() for w in watermarks):
                        paras.append(t)
            except Exception as e:
                print(f"Error reading {dp}: {e}")
    return paras

def partition_paras(paras, num_units):
    total = len(paras)
    if total == 0:
        return [[] for _ in range(num_units)]
    chunk_size = max(1, total // num_units)
    res = []
    for i in range(num_units):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_units - 1 else total
        res.append(paras[start:end])
    return res

def write_dataset_file(var_name, data_prop, filename, units_data):
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"// Class 5 {var_name} Dataset (KPTBB)\n")
        f.write(f"const {var_name} = " + json.dumps(units_data, ensure_ascii=False, indent=2) + ";\n\n")
        f.write(f"if (typeof DATA !== 'undefined' && DATA) {{ DATA.{data_prop} = {var_name}; }}\n")
        f.write(f"if (typeof window !== 'undefined') {{ window.{var_name} = {var_name}; }}\n")
    print(f"Generated {filename} ({len(units_data)} units)")

# 1. MATHEMATICS (9 Units)
def build_math():
    folder = os.path.join(base_dir, "5th Maths", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Whole Numbers and Operations", "مکمل اعداد اور بنیادی حسابی عمل", "Numbers up to 1,000,000, place values, addition, subtraction, multiplication, division, and BODMAS order of operations."),
        (2, "HCF and LCM", "عاد اعظم اور ذواضعاف اقل", "Prime and composite numbers, divisibility tests for 2, 3, 5, 10, prime factorization, Highest Common Factor (HCF) and Least Common Multiple (LCM)."),
        (3, "Fractions", "کسور (کسریں)", "Types of fractions (proper, improper, mixed), equivalent fractions, addition, subtraction, multiplication, and division of fractions with word problems."),
        (4, "Decimals and Percentage", "اعشاری اعداد اور فیصد", "Decimals up to three decimal places, conversion between fractions and decimals, percentage representation and real-life calculations."),
        (5, "Distance and Time", "فاصلہ اور وقت", "Units of distance (km, m, cm, mm), units of time (hours, minutes, seconds), conversion of units, elapsed time and word problems."),
        (6, "Unitary Method", "طریقہ اکائی (یونیٹری طریقہ)", "Direct and inverse relationship concepts, finding cost of single unit, calculating total cost for multiple items, and practical daily life math."),
        (7, "Geometry", "جیومیٹری (ہندسہ)", "Types of angles (acute, right, obtuse, straight), complementary and supplementary angles, triangles, quadrilaterals, and circle radius and diameter."),
        (8, "Perimeter and Area", "احاطہ اور رقبہ", "Perimeter and area of squares and rectangles, distinction between perimeter and area, unit square calculations and practical scenarios."),
        (9, "Data Handling", "اعداد و شمار کا انتظام", "Data collection, tally charts, frequency tables, bar graphs, and line graphs interpretation.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Comprehensive study of {title} in accordance with KPK Class 5 Mathematics syllabus."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Textbook Concepts & Worked Examples",
                    "headingUrdu": "درسی تصورات و حل شدہ مثالیں",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"Define the core concept of {title}.", "a": f"{title} is a core mathematical topic in Grade 5. It establishes numerical skills and problem-solving techniques: {summary}"},
                    {"q": f"State two practical applications of {title} in everyday life.", "a": f"1. Solving commercial, trade, and daily measurement problems accurately.\n2. Building strong foundations for higher secondary mathematics and data analysis."}
                ],
                "longQuestions": [
                    {"q": f"Explain the step-by-step method to solve problems from Unit {num} ({title}).", "a": f"First read the problem carefully to identify given values and unknown targets. Apply the appropriate formulas or computational rules of {title}, execute arithmetic operations, and cross-check the final result."}
                ],
                "mcqs": [
                    {"q": f"Which mathematical concept is primary in Unit {num}?", "options": [title, "Plant physiology", "History of Pakistan", "Geographical mapping"], "answer": 0, "exp": f"Unit {num} focuses specifically on {title}."},
                    {"q": "In mathematics, checking the answer ensures that:", "options": ["Calculations and equality hold true", "Numbers are randomly assigned", "Formula is forgotten", "Steps are omitted"], "answer": 0, "exp": "Verification confirms numerical accuracy."}
                ]
            },
            "englishSummary": f"Unit {num} covers {title}, including {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کا احاطہ کرتا ہے جس میں درسی تصورات، حل شدہ مثالیں اور مشقی سوالات شامل ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("MATH_5_DATA", "math5Chapters", "math_5_data.js", units)

# 2. GENERAL SCIENCE (10 Units)
def build_science():
    folder = os.path.join(base_dir, "5th General Science", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Classification of Living Things", "جانداروں کی جماعت بندی", "Classification of animals into vertebrates and invertebrates, flowering and non-flowering plants, five kingdom system."),
        (2, "Microorganisms", "خردبینی جاندار", "Bacteria, viruses, fungi, beneficial and harmful effects of microorganisms, infections and hygiene."),
        (3, "Flowers and Seeds", "پھول اور بیج", "Structure of flowers, pollination (self and cross), fertilization, seed structure (monocot and dicot) and germination."),
        (4, "Environmental Pollution", "ماحولیاتی آلودگی", "Air, water, and land pollution, causes and consequences, biodegradable vs non-biodegradable waste, 3Rs (Reduce, Reuse, Recycle)."),
        (5, "Physical and Chemical Changes of Matter", "مادے کی طبعی اور کیمیائی تبدیلیاں", "States of matter, physical changes (reversible) and chemical changes (irreversible), rust, burning, and mixing."),
        (6, "Light and Sound", "روشنی اور آواز", "Luminous and non-luminous objects, transparent, translucent, opaque materials, reflection of light, sound production, speed and vibration."),
        (7, "Electricity and Magnetism", "بجلی اور مقناطیسیت", "Static and current electricity, simple electrical circuits, conductors and insulators, magnets, magnetic fields, and electromagnets."),
        (8, "Structure of Earth", "زمین کی ساخت", "Layers of Earth (crust, mantle, core), soil composition, types of soil, weathering, and erosion."),
        (9, "Space and Satellites", "خلا اور سیارچے", "Solar system, planets, natural satellites (Moon), artificial satellites, space exploration and weather forecasting."),
        (10, "Technology in Everyday Life", "روزمرہ زندگی میں ٹیکنالوجی", "Simple machines, levers, pulleys, wheels and axles, modern household technology and safety measures.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Scientific study of {title} based on the KPK Class 5 General Science curriculum."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Textbook Concepts & Scientific Principles",
                    "headingUrdu": "درسی تصورات و سائنسی اصول",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"What is the main subject matter of Unit {num} ({title})?", "a": f"{title} examines foundational natural science concepts: {summary}"},
                    {"q": f"State two scientific facts or observations regarding {title}.", "a": f"1. Scientific inquiry relies on systematic observation, experiment, and classification.\n2. Understanding {title} helps in environmental protection and technological application."}
                ],
                "longQuestions": [
                    {"q": f"Discuss in detail the principles and significance of {title}.", "a": f"In {title}, natural phenomena are observed systematically. Students learn the classification, structural mechanisms, cause-and-effect relationships, and practical importance in everyday life and nature."}
                ],
                "mcqs": [
                    {"q": f"What does Unit {num} focus on?", "options": [title, "Past tense verbs", "Islamic history", "World currencies"], "answer": 0, "exp": f"Unit {num} covers {title} in depth."},
                    {"q": "Scientific conclusions must always be supported by:", "options": ["Observation and evidence", "Wild imagination", "Personal preference", "Random guesses"], "answer": 0, "exp": "Science relies on empirical observation and evidence."}
                ]
            },
            "englishSummary": f"Unit {num} teaches {title}, encompassing {summary}.",
            "urduSummary": f"یہ باب {titleUr} کی تفصیلات پیش کرتا ہے جن میں سائنسی مشاہدات، درسی تفہیم اور مشقی سوالات شامل ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("GENERAL_SCIENCE_5_DATA", "genSci5Chapters", "general_science_5_data.js", units)

# 3. ENGLISH (14 Units)
def build_english():
    folder = os.path.join(base_dir, "5th English", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Patience", "صبر و تحمل", "Virtue of patience in personal conduct, teamwork, story of the Holy Prophet's ﷺ noble patience, silent letters and nouns."),
        (2, "Be Grateful", "شکر گزاری", "Gratitude towards Allah Almighty and fellow human beings, appreciating blessings, vowel sounds, syllables and adjectives."),
        (3, "Women as Role Models", "خواتین بطور رول ماڈل", "Female education, inspirational Pakistani women figures, gender equality, regular/irregular nouns, and paragraph writing."),
        (4, "Unforgettable Moments of My Life", "میری زندگی کے ناقابل فراموش لمحات", "Personal memories, travel and nature experiences, mountains, rivers, lakes, descriptive writing, and homophones."),
        (5, "Let's Save the Earth", "آئیں زمین کو بچائیں", "Environmental education, climate change, combating littering, planting trees, affixes, prefixes, and suffixes."),
        (6, "A Fit and Healthy Life", "صحت مند اور توانا زندگی", "Personal hygiene, sanitation, balanced diet, physical exercises, avoiding junk food, consonant clusters and punctuation."),
        (7, "What Goes Around, Comes Around", "جیسی کرنی ویسی بھرنی", "Moral fable, avoiding social evils, honesty, integrity, personal and possessive pronouns, and story writing."),
        (8, "Do What's Right", "درست کام کریں", "Participatory citizenship, civic rights and duties, community service, rule of law, modal verbs and adverbs."),
        (9, "A Nation's Strength", "قوم کی طاقت", "Patriotic poem, civic dedication, true wealth of a nation through honest character, rhyme scheme and poetic analysis."),
        (10, "Eid-ul-Azha", "عید الاضحیٰ", "Religious festival, sacrifice of Prophet Ibrahim (AS), sharing with the poor, simple past tense and formal letter writing."),
        (11, "Let's Be Helpful", "آئیں مددگار بنیں", "Community assistance, helping neighbors and disabled persons, occupational dignity, present continuous tense."),
        (12, "The National Animal", "قومی جانور", "Markhor as Pakistan's national pride, wildlife preservation, national symbols, degree of adjectives and report writing."),
        (13, "When Something Went Wrong", "جب کچھ غلط ہو گیا", "Conflict resolution, managing anger and crises, media as informational source, conjunctions and dialogue."),
        (14, "Two Little Kittens", "دو چھوٹی بلیاں", "Poem on resolving quarrels peacefully, caring for pets, kindness, future tense, and review of comprehension skills.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Reading passage and linguistic exercises for Unit {num}: {title}."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Textbook Reading & Comprehension",
                    "headingUrdu": "درسی مطالعہ و تفہیمِ عبارت",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"What is the central message of Unit {num} ({title})?", "a": f"The unit emphasizes moral character, linguistic development, and social awareness: {summary}"},
                    {"q": f"List two key vocabulary words or grammatical items highlighted in {title}.", "a": f"1. Expressive reading and precise pronunciation of target vocabulary.\n2. Practical usage of grammar rules (parts of speech, tenses, and punctuation)."}
                ],
                "longQuestions": [
                    {"q": f"Write a paragraph summarizing the core theme and lessons learned in {title}.", "a": f"{title} encourages students to reflect on positive personal and social ethics while enhancing reading fluency, comprehension skills, and communicative competence in English."}
                ],
                "mcqs": [
                    {"q": f"The main theme of Unit {num} is:", "options": [title, "Algebraic equations", "Soil textures", "Map projection"], "answer": 0, "exp": f"Unit {num} develops reading and language skills around {title}."},
                    {"q": "Good reading comprehension requires:", "options": ["Understanding the main idea and supporting details", "Ignoring new words", "Skipping the text", "Reading without focus"], "answer": 0, "exp": "Comprehension entails identifying key ideas and details."}
                ]
            },
            "englishSummary": f"Unit {num} explores {title}, highlighting {summary}.",
            "urduSummary": f"اس یونٹ میں {titleUr} کے عنوان کے تحت تفہیمی عبارت، ذخیرہ الفاظ، اور انگریزی گرامر کی مشقیں شامل ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("ENGLISH_5_DATA", "eng5Chapters", "english_5_data.js", units)

# 4. URDU (21 Lessons)
def build_urdu():
    folder = os.path.join(base_dir, "5th Urdu", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "حمد", "حمد باری تعالیٰ", "اللہ تعالیٰ کی عظمت، قدرت اور نعمتوں کا بیان۔ تمام کائنات کا خالق و مالک اللہ تعالیٰ ہے۔"),
        (2, "نعت", "نعت رسول مقبول ﷺ", "حضور خاتم النبیین ﷺ کی سیرتِ طیبہ، اخلاقِ حسنہ اور امت پر آپ ﷺ کے احسانات کا ذکر۔"),
        (3, "جو وعدہ کرو سو پورا کرو", "ایفائے عہد", "وعدہ پورا کرنے کی اسلامی اہمیت، دیانت داری اور سچے مسلمان کی صفات۔"),
        (4, "خدمت خلق", "انسانیت کی خدمت", "دکھی انسانیت کی مدد، غریبوں اور ناداروں کا خیال رکھنا، ایثار و قربانی کا جذبہ۔"),
        (5, "قومی تہوار", "قومی تہوار اور تقریبات", "یومِ آزادی، یومِ پاکستان اور دیگر قومی ایام کی تاریخی اہمیت اور حب الوطنی۔"),
        (6, "ہوا چلی (نظم)", "ہوا چلی", "قدرتی مناظر، تازہ ہوا کے فوائد، موسموں کی خوبصورتی اور منظوم منظر کشی۔"),
        (7, "میری پہچان ہے تو", "قومی پرچم اور ترانہ", "قومی نشانات، قومی پرچم کے آداب، سبز ہلالی پرچم کی حرمت اور وطن سے محبت۔"),
        (8, "ہمارے پیشے", "مختلف پیشے اور محنت کی عظمت", "کسان، استاد، ڈاکٹر، انجینئر اور دیگر پیشے، محنت کی عظمت اور معاشرتی کردار۔"),
        (9, "ایک گائے اور بکری (نظم)", "علامہ اقبال کی نظم", "علامہ اقبال کی خوبصورت اخلاقی نظم، شکوہ اور جواب، باہمی ہمدردی اور شکر گزاری۔"),
        (10, "حضرت عثمان غنی رضی اللہ عنہ", "سیرت حضرت عثمان غنیؓ", "خلیفہ سوم حضرت عثمان غنیؓ کی سخاوت، حیا، جمعِ قرآن اور اسلام کے لیے گراں قدر خدمات۔"),
        (11, "دنیا آپ کی مٹھی میں", "جدید ذرائع ابلاغ و انٹرنیٹ", "انٹرنیٹ، کمپیوٹر، موبائل فون کے فائدے، مثبت استعمال اور آن لائن اخلاقیات۔"),
        (12, "ہم پھول اک چمن کے (نظم)", "قومی اتحاد و یکجہتی", "قومی یکجہتی کا نغمہ، باہمی محبت، اخوت اور صوبائی ہم آہنگی کا درس۔"),
        (13, "آؤ سنو کہانی", "دلچسپ اخلاقی کہانی", "اخلاقی سبق آموز کہانی، سچائی اور دانشمندی کی برکات۔"),
        (14, "آئیں مدد کریں", "باہمی تعاون اور امداد", "آفات اور ہنگامی حالات میں دوسروں کی دستگیری، رضاکارانہ جذبہ۔"),
        (15, "رکھیں میرا خیال", "ماحول اور صفائی", "درختوں کی حفاظت، ماحولیاتی آلودگی کا تدارک اور صفائی نصف ایمان ہے۔"),
        (16, "ایک قدیم شہر", "تاریخی و ثقافتی ورثہ", "خیبر پختونخوا اور پاکستان کے قدیم آثار، تاریخ اور تمدن کی جھلک۔"),
        (17, "نیک بنو، نیکی پھیلاؤ (نظم)", "نیکی کی دعوت", "اچھے کاموں کی ترغیب، دوسروں سے حسن سلوک اور برائی سے بچاؤ۔"),
        (18, "حسنِ سلوک", "والدین اور پڑوسیوں سے حسنِ سلوک", "رشتہ داروں، بزرگوں، والدین اور پڑوسیوں کے حقوق اور بہترین برتاؤ۔"),
        (19, "کہا اقبالؒ نے (نظم)", "پیغامِ اقبالؒ", "شاعرِ مشرق علامہ محمد اقبالؒ کا بچوں کے نام پیغام، خودی اور بلند ہمتی۔"),
        (20, "بے مثل ہے نظام تیرا", "نظامِ قدرت کی نشانیاں", "سورج، چاند، ستاروں اور زمین کا منظم نظام اور خالقِ کائنات کی کاریگری۔"),
        (21, "علم و ادب کی شمعیں", "تعلیم اور کتب بینی", "کتابوں سے دوستی، علم کی اہمیت، اساتذہ کا ادب اور روشن مستقبل کی نوید۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"درسی متن اور مشقی تفہیم برائے سبق نمبر {num}: {title}۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "lesson",
            "sections": [
                {
                    "heading": "درسی عبارت، فہم و قرات",
                    "headingUrdu": "درسی عبارت و تدریسی نکات",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"سبق نمبر {num} ({title}) کا بنیادی موضوع اور پیغام کیا ہے؟", "a": f"اس سبق کا مرکزی موضوع اخلاقی تربیت اور زبان دانی ہے: {summary}"},
                    {"q": f"اس سبق سے حاصل ہونے والے دو اہم اخلاقی یا علمی اسباق بیان کریں۔", "a": f"۱۔ اخلاقی اقدار اور مثبت طرزِ عمل کو روزمرہ زندگی میں اپنانا۔\n۲۔ اردو الفاظ کا درست تلفظ، املا اور گرامر کے مطابق جملہ سازی سیکھنا۔"}
                ],
                "longQuestions": [
                    {"q": f"سبق '{title}' کا تفصیلی خلاصہ اپنے الفاظ میں تحریر کریں۔", "a": f"مصنف نے اس سبق میں نہایت دلنشین پیرائے میں {titleUr} کی اہمیت اجاگر کی ہے۔ سبق کے مطالعے سے ہمیں معلوم ہوتا ہے کہ {summary}۔ ہمیں ان سنہری اصولوں پر عمل کر کے ایک بہترین شہری بننا چاہیے۔"}
                ],
                "mcqs": [
                    {"q": f"سبق نمبر {num} کس موضوع پر مبنی ہے؟", "options": [title, "ریاضی کے اصول", "کیمسٹری کے تجربات", "جغرافیائی نقشے"], "answer": 0, "exp": f"سبق نمبر {num} کا موضوع {title} ہے۔"},
                    {"q": "اردو زبان میں عبارت کے درست فہم کے لیے کیا ضروری ہے؟", "options": ["الفاظ کے معانی اور سیاق و سباق کو سمجھنا", "بغیر سمجھے پڑھنا", "املا کو نظر انداز کرنا", "تلفظ غلط ادا کرنا"], "answer": 0, "exp": "الفاظ کے معانی اور سیاق و سباق عبارت فہمی کی بنیاد ہیں۔"}
                ]
            },
            "englishSummary": f"Lesson {num} covers {title}, focusing on {summary}.",
            "urduSummary": f"یہ سبق {titleUr} کے گرد گھومتا ہے جس میں {summary} کے موضوع پر درسی عبارت، الفاظ معنی، قواعد اور مشقی سوالات شامل ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("URDU_5_DATA", "urdu5Chapters", "urdu_5_data.js", units)

# 5. ISLAMIAT (7 Units / Abwab)
def build_islamiat():
    folder = os.path.join(base_dir, "5th Islamiat", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "باب اول: قرآن مجید و حدیث نبوی ﷺ", "قرآن مجید اور احادیثِ مبارکہ", "حفظ و ترجمہ منتخب قرآنی آیات، فضائل قرآن، اور اخلاقی و عملی احادیثِ نبویہ ﷺ مع ترجمہ و تشریح۔"),
        (2, "باب دوم: ایمانیات و عبادات", "ایمانیات اور عبادات", "توحید، رسالت، آسمانی کتب، آخرت پر ایمان، نماز، روزہ، زکوٰۃ اور حج کے ارکان اور ان کے روحانی و معاشرتی فوائد۔"),
        (3, "باب سوم: سیرت طیبہ ﷺ", "سیرتِ رسولِ اکرم ﷺ", "سیرتِ نبوی ﷺ کے نمایاں پہلو، ہجرتِ مدینہ، مواخاتِ مدینہ، میثاقِ مدینہ، غزوات اور حلم و عفو۔"),
        (4, "باب چہارم: اخلاق و آداب", "اسلامی اخلاق اور آدابِ زندگی", "سچائی، دیانت داری، ایفائے عہد، والدین اور اساتذہ کا احترام، مجلس اور گفتگو کے اسلامی آداب۔"),
        (5, "باب پنجم: حسنِ معاملات و معاشرت", "معاملات اور اسلامی معاشرت", "حقوق العباد، پڑوسیوں کے حقوق، یتیموں اور مسکینوں کی خبر گیری، صفائی و طہارت اور حلال روزی۔"),
        (6, "باب ششم: ہدایت کے سرچشمے اور مشاہیر اسلام", "مشاہیرِ اسلام اور صحابہ کرامؓ", "خلفائے راشدینؓ، امہات المومنینؓ، جلیل القدر صحابہ و صحابیاتؓ اور ائمہ کرام کی عظیم الشان زندگی اور کارنامے۔"),
        (7, "باب ہفتم: اسلامی تعلیمات اور عصر حاضر کے تقاضے", "عصر حاضر کے تقاضے", "ماحولیاتی تحفظ، وقت کی پابندی، قانون کی پاسداری، سائنس و ٹیکنالوجی کا مثبت استعمال اور اسلامی تشخص۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"مستند درسی اسلامی تعلیمات برائے {title}۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "قرآنی و نبوی تعلیمات اور درسی تشریح",
                    "headingUrdu": "درسی مضامین و تفصیلی نکات",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"{title} کا بنیادی اسلامی مقصد کیا ہے؟", "a": f"اس باب کا مقصد طلبہ کی دینی و اخلاقی تربیت کرنا ہے: {summary}"},
                    {"q": "اسلامی تعلیمات پر عمل پیرا ہونے کے دو بنیادی فائدے بیان کریں۔", "a": "۱۔ دنیا میں امن، چین اور باہمی اخوت نصیب ہوتی ہے۔\n۲۔ آخرت میں اللہ تعالیٰ اور اس کے رسول ﷺ کی خوشنودی اور نجات حاصل ہوتی ہے۔"}
                ],
                "longQuestions": [
                    {"q": f"باب '{title}' کے اہم نکات اور اس کے معاشرتی اثرات پر تفصیلی روشنی ڈالیں۔", "a": f"اسلام ایک مکمل ضابطہ حیات ہے۔ اس باب میں {titleUr} کی جامع تفصیل بیان کی گئی ہے۔ جب کوئی فرد اور معاشرہ {summary} کی روشنی میں اپنی زندگی گزارتا ہے تو معاشرے سے برائیاں ختم ہو جاتی ہیں اور عدل و انصاف قائم ہوتا ہے۔"}
                ],
                "mcqs": [
                    {"q": f"{title} بنیادی طور پر کس کی رہنمائی فراہم کرتا ہے؟", "options": [titleUr, "سائنسی فارمولے", "ہندسی اشکال", "انگریزی شاعری"], "answer": 0, "exp": f"یہ باب {titleUr} کے اسلامی احکام اور تعلیمات پر مبنی ہے۔"},
                    {"q": "اسلام میں تمام اعمال کا دارومدار کس پر ہے؟", "options": ["نیتوں پر", "ظاہری دکھاوے پر", "مال و دولت پر", "بے بنیاد باتوں پر"], "answer": 0, "exp": "حدیث نبوی ﷺ کے مطابق 'انما الاعمال بالنیات' یعنی اعمال کا دارومدار نیتوں پر ہے۔"}
                ]
            },
            "englishSummary": f"Unit {num} covers {title}, focusing on {summary}.",
            "urduSummary": f"اس باب میں {titleUr} کے حوالے سے قرآنی آیات، احادیثِ مبارکہ، سیرت اور اخلاقی تعلیمات کی تفصیلی وضاحت کی گئی ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("ISLAMIAT_5_DATA", "islamiat5Chapters", "islamiat_5_data.js", units)

# 6. SOCIAL STUDIES EM (6 Chapters)
def build_social_studies():
    folder = os.path.join(base_dir, "5th Social Study", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Citizenship", "شہریت اور انسانی حقوق", "Civic rights and responsibilities, digital citizenship, UN Charter fundamental human rights, equality, freedom of speech, and conflict resolution."),
        (2, "Culture", "ثقافت اور ورثہ", "Elements of culture (language, food, dress, customs), cultural diversity in Pakistan, provincial cultures of KP, Punjab, Sindh, Balochistan, and national cohesion."),
        (3, "State and Government", "ریاست اور حکومت", "Definition of state, constitution, three organs of government (legislature, executive, judiciary), democracy, elections, and civic duties."),
        (4, "History", "تاریخ اور تحریک پاکستان", "Indus Valley Civilization, Gandhara civilization, arrival of Islam in subcontinent, Pakistan Movement, Quaid-e-Azam, and Allama Iqbal."),
        (5, "Geography", "جغرافیہ اور قدرتی ماحول", "Maps, globes, latitude and longitude, physical regions of Pakistan (mountains, plateaus, plains, deserts), climate, and natural resources."),
        (6, "Economics", "معاشیات اور تجارت", "Basic economic concepts (goods, services, consumers, producers), money, trade, banking, government revenue, taxes, and economic development.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Curriculum concepts for Chapter {num}: {title} in Class 5 Social Studies."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Textbook Concepts & Explanations",
                    "headingUrdu": "درسی تصورات و معلوماتی نکات",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"Define the primary focus of Chapter {num} ({title}).", "a": f"{title} is an essential component of Social Studies education: {summary}"},
                    {"q": f"State two key facts learned from the study of {title}.", "a": f"1. Understanding social institutions and patriotic duties helps build responsible citizens.\n2. Knowledge of {title} promotes civic awareness, harmony, and national development."}
                ],
                "longQuestions": [
                    {"q": f"Write an analytical overview of {title} and its importance to Pakistan.", "a": f"{title} examines the foundations of human society. Through this chapter, students learn {summary}, fostering critical thinking and active citizenship."}
                ],
                "mcqs": [
                    {"q": f"What is the central theme of Chapter {num}?", "options": [title, "Plant germination", "Quadratic equations", "Grammar analysis"], "answer": 0, "exp": f"Chapter {num} focuses directly on {title}."},
                    {"q": "A responsible citizen always:", "options": ["Obeys laws and respects rights of others", "Ignores civic duties", "Damages public property", "Spreads misinformation"], "answer": 0, "exp": "Responsible citizenship involves following the law and respecting fellow citizens."}
                ]
            },
            "englishSummary": f"Chapter {num} addresses {title}, including {summary}.",
            "urduSummary": f"اس باب میں {titleUr} کے عنوان کے تحت درسی تصورات، تاریخ و شہریت، اور مشقی سوالات کی وضاحت کی گئی ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("SOCIAL_STUDIES_5_DATA", "sst5Chapters", "social_studies_5_data.js", units)

# 7. SOCIAL STUDIES UM (6 Chapters)
def build_social_studies_um():
    folder = os.path.join(base_dir, "5th Social Study UM", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "باب اول: شہریت", "شہریت اور انسانی حقوق", "شہری حقوق و فرائض، ڈیجیٹل شہریت، اقوام متحدہ کا منشور، مساوات، آزادی اظہار، اور باہمی تنازعات کا پرامن حل۔"),
        (2, "باب دوم: ریاست اور حکومت", "ریاست، حکومت اور دستور", "ریاست کا مفہوم، حکومت کے تین شعبے (مقننہ، انتظامیہ، عدلیہ)، جمہوری نظام، انتخابات اور قانون کی حکمرانی۔"),
        (3, "باب سوم: ثقافت", "پاکستانی ثقافت اور روایات", "ثقافت کے عناصر (زبان، لباس، خوراک، رسم و رواج)، خیبر پختونخوا اور تمام صوبوں کی ثقافتیں اور قومی یکجہتی۔"),
        (4, "باب چہارم: تاریخ", "تاریخ اور تحریک پاکستان", "وادی سندھ اور گندھارا کی قدیم تہذیبیں، برصغیر میں اسلام کی آمد، تحریکِ پاکستان، قائداعظم اور علامہ اقبال کی جدوجہد۔"),
        (5, "باب پنجم: جغرافیہ", "جغرافیہ اور پاکستان کے قدرتی خطے", "نقشہ خوانی، عرض بلد اور طول بلد، پاکستان کے طبعی خدوخال (پہاڑ، سطح مرتفع، میدان، صحرا)، آب و ہوا اور قدرتی وسائل۔"),
        (6, "باب ششم: معاشیات", "معاشیات، تجارت اور بینکاری", "بنیادی معاشی تصورات (اشیاء، خدمات، صارفین، پیدا کنندگان)، زر (پیسہ)، ملکی و بین الاقوامی تجارت، ٹیکس اور معاشی ترقی۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"معاشرتی علوم درسی متن برائے {title}۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "درسی تصورات و معلوماتی نکات",
                    "headingUrdu": "درسی متن و فکری رہنمائی",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"{title} کا بنیادی تعلیمی مقصد کیا ہے؟", "a": f"اس باب کا مقصد طلبہ کو معاشرتی و تاریخی شعور فراہم کرنا ہے: {summary}"},
                    {"q": "معاشرے میں امن و ترقی کے لیے کن دو باتوں پر عمل ضروری ہے؟", "a": "۱۔ آئین اور قانون کی مکمل پابندی اور حقوق و فرائض میں توازن۔\n۲۔ باہمی برداشت، احترامِ انسانیت اور مثبت قومی سوچ۔"}
                ],
                "longQuestions": [
                    {"q": f"باب '{title}' کے اہم نکات اور ملکی ترقی میں اس کی اہمیت تفصیل سے واضح کریں۔", "a": f"معاشرتی علوم ہمیں ایک باشعور انسان اور محب وطن شہری بناتے ہیں۔ اس باب میں {titleUr} کی وضاحت کرتے ہوئے بتایا گیا ہے کہ {summary}۔ اس علم سے ہم ملکی اور بین الاقوامی مسائل کو بہتر طریقے سے سمجھ سکتے ہیں۔"}
                ],
                "mcqs": [
                    {"q": f"{title} کا مرکزی موضوع کیا ہے؟", "options": [titleUr, "سائنسی تجربات", "الجبرا کے فارمولے", "انگریزی گرائمر"], "answer": 0, "exp": f"اس باب کا تعلق {titleUr} سے ہے۔"},
                    {"q": "ایک ذمہ دار شہری کی بنیادی پہچان کیا ہے؟", "options": ["قوانین کی پاسداری اور دوسروں کے حقوق کا احترام", "فرائض سے غفلت", "قومی املاک کو نقصان پہنچانا", "افواہیں پھیلانا"], "answer": 0, "exp": "ذمہ دار شہری ملکی قوانین کا پابند اور دوسروں کا خیر خواہ ہوتا ہے۔"}
                ]
            },
            "englishSummary": f"Chapter {num} covers {title}, highlighting {summary}.",
            "urduSummary": f"اس باب میں {titleUr} کے موضوع پر درسی معلومات، تاریخی حقائق، اور مشقی سوالات و جوابات دیے گئے ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("SOCIAL_STUDIES_UM_5_DATA", "sstum5Chapters", "social_studies_um_5_data.js", units)

# 8. PASHTO (28 Lessons)
def build_pashto():
    folder = os.path.join(base_dir, "5th Pashto", "Word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "حمد", "د الله تعالی صفت او ثنا", "د الله تعالی عظمت، قدرت او د کائناتو د پالونکي صفتونه."),
        (2, "نعت", "د رسول الله ﷺ صفت", "د حضرت محمد مصطفی ﷺ سیرت او مبارک اخلاق."),
        (3, "د حضرت محمد ﷺ زغم او بخښنه", "د نبوي زغم او حلم درس", "د رسول اکرم ﷺ عفوه، زغم او مهرباني."),
        (4, "پاکه بي بي حضرت خديجه رض", "سیرت ام المومنین حضرت خدیجهؓ", "د ام المؤمنین حضرت خدیجة الکبریٰ رض قربانۍ او خدمتونه."),
        (5, "د وطن نه روانګي", "د هجرت او سفر یادونه", "د سفر اداب او د خپل خوږ وطن مینه."),
        (6, "د موبائل اهمیت", "د موبائل فون او ټیکنالوجۍ ګټې", "د مبایل مثبت استعمال او د وخت خیال ساتل."),
        (7, "حرکت کښې برکت دے", "د محنت او هڅو فضیلت", "د محنت او هلو ځلو اهمیت او برکتونه."),
        (8, "باران", "د باران منظوم بیان", "د باران نعمت، د طبیعت ښکلا او د باران اوبه."),
        (9, "د اټک قلا", "تاریخي کلا اټک", "د اټک تاریخي کلا، تاریخ او د پښتونخوا عظمت."),
        (10, "اېدهي ټرسټ", "د عبدالستار ایدهي انساني خدمت", "د انسان دوستۍ، خیریه کارونو او خدمت خلق درس."),
        (11, "خاکسار خلیفه", "د حضرت عمر فاروقؓ عدل او خاکساري", "د خلیفه دویم عدل او سادګي."),
        (12, "خوشحال خان خټک", "بابائے پښتو خوشحال خان", "د خوشحال بابا علمي، ادبي او ملي خدمتونه."),
        (13, "دوست محمد خان کامل مومند", "د پښتو ادبي شخصیت", "د کامل مومند ادبي څېړنې او اثار."),
        (14, "د مهابت خان جومات", "پېښور تاریخي جومات", "د مهابت خان جومات تاریخ او اسلامي فنِ تعمیر."),
        (15, "پښتونولي", "پښتونولۍ دود او دستور", "د مېلمه پالنې، بدرګې، ننګ او پښتونولۍ اصول."),
        (16, "اولسي لوبې", "دودیزې او سیمه ییزې لوبې", "د پښتنو دودیزې او صحتمندې لوبې."),
        (17, "علم لوے دولت دے", "د علم فضیلت", "د زده کړې ارزښت او په ژوند کښې د هغې رڼا."),
        (18, "حجره", "د حجرې کلتوري ارزښت", "د پښتنو حجره د کلتور او اصلاح مرکز."),
        (19, "سفر مدام سفر", "سفرنامه او تجارب", "د سفر ګټې، علمي تجارب او جهان لیدنه."),
        (20, "کېپټن کرنل شېر خان شهید", "د نشان حیدر اتل", "د کارګل اتل او د وطن په دفاع کښې قرباني."),
        (21, "د زنانو احترام", "د ښځو حقوق او درناوی", "په اسلام او ټولنه کښې د مېرمنو درناوی او حقوق."),
        (22, "سپرلے", "د پسرلي ښکلا", "د سپرلي موسم، ګلونه او د فطرت تازه ګي."),
        (23, "عجب خان اپرېدے", "تاریخي پښتون شخصیت", "د عجب خان اپریدي مېړانه او تاریخ."),
        (24, "پښتنه مېرمن بي بي مبارکه", "تاریخي پښتنه مېرمن", "د بي بي مبارکې پوهه، ننګ او تاریخي کارنامې."),
        (25, "روژه", "د روژې مبارکه میاشت", "د روژې فضیلت، تقوا، صبر او ټولنیزه همدردي."),
        (26, "غازي عمرا خان", "د باجوړ تاریخي اتل", "د غازي عمرا خان افغان مېړانه او د ازادۍ مبارزه."),
        (27, "پانېني", "لرغونی ګرامرپوه پانیني", "د خیبر پښتونخوا پخوانی عالم او د صوابۍ تاریخ."),
        (28, "دعا", "مناجات او دعا", "د الله تعالی په دربار کښې عاجزي او دعا.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"د پنځم ټولګي پښتو درسي متن د {title} په اړه."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "lesson",
            "sections": [
                {
                    "heading": "درسي متن او لوست",
                    "headingUrdu": "پښتو متن او تشریح",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"د دې لوست ({title}) اصلي پیغام څه دی؟", "a": f"په دې لوست کښې زده کوونکو ته د {summary} په اړه معلومات او اخلاقي لارښوونه شوې ده."},
                    {"q": f"له دې لوست څخه دوه مهمې خبرې بیان کړئ.", "a": "۱. په ژوند کښې لوړ اخلاق، د علم لټون او د وطن مینه خپلول.\n۲. د پښتو ژبې د سم لوست، ګرامر او ویونو (الفاظو) زده کړه."}
                ],
                "longQuestions": [
                    {"q": f"د لوست '{title}' تفصیلي لنډیز په خپلو ټکو کښې ولیکئ.", "a": f"دا لوست د پښتو نصاب یوه مهمه برخه ده چې پکښې {summary} په ډېره روانه او خوږه ژبه بیان شوي دي. زده کوونکي باید د دې لوست له لارښوونو څخه په خپل ورځني ژوند کښې ګټه پورته کړي."}
                ],
                "mcqs": [
                    {"q": f"لوست نمبر {num} د کوم موضوع په اړه دی؟", "options": [title, "حساب", "ساینس", "انګلیسي ګرامر"], "answer": 0, "exp": f"دا لوست د {title} په اړه دی."},
                    {"q": "د هر لوست په پای کښې مشقونه د څه لپاره دي؟", "options": ["د پوهې او زده کړې د امتحان لپاره", "د وخت ضایع کولو لپاره", "د تصادفي ځوابونو لپاره", "د هېرولو لپاره"], "answer": 0, "exp": "مشقونه د محصلینو د فهم او زده کړې د تصدیق لپاره دي."}
                ]
            },
            "englishSummary": f"Lesson {num} covers {title}, focusing on {summary}.",
            "urduSummary": f"اس پشتو سبق میں {titleUr} کے عنوان کے تحت درسی متن، اخلاقی و معلوماتی نکات اور مشقیں شامل ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("PASHTO_5_DATA", "pashto5Chapters", "pashto_5_data.js", units)

if __name__ == "__main__":
    print("Building Class 5th datasets...")
    build_math()
    build_science()
    build_english()
    build_urdu()
    build_islamiat()
    build_social_studies()
    build_social_studies_um()
    build_pashto()
    print("All Class 5th datasets created successfully!")
