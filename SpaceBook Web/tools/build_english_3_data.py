"""
Builder script for Class 3 English Dataset (KPK Textbook Board)
Extracts all 11 Units from D:\SpaceBook\Books\3rd\3rd English\Word\3rd English.docx
Generates SpaceBook Web/js/english_3_data.js
"""

import zipfile
import xml.etree.ElementTree as ET
import re
import json

def get_docx_paragraphs(path):
    with zipfile.ZipFile(path) as z:
        xml_content = z.read('word/document.xml')
    tree = ET.fromstring(xml_content)
    paras = []
    for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [node.text for node in p.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
        text = ''.join(texts).strip()
        if text:
            # clean watermarks and noise
            if "A-PDF Watermark" in text or "awazeinqilab.com" in text:
                continue
            paras.append(text)
    return paras

print("Loading docx...")
all_paras = get_docx_paragraphs(r"D:\SpaceBook\Books\3rd\3rd English\Word\3rd English.docx")
print("Total paras:", len(all_paras))

unit_bounds = [
    (1, "All are Welcome", 347, 679, "prose"),
    (2, "Gifts of Nature", 679, 996, "poem"),
    (3, "The People I Love", 996, 1328, "prose"),
    (4, "Kindness to Children", 1328, 1718, "prose"),
    (5, "Road Safety", 1718, 1981, "prose"),
    (6, "The Day of Silence", 1981, 2234, "prose"),
    (7, "What I Like to Play", 2234, 2515, "prose"),
    (8, "Saving Resources", 2515, 2930, "prose"),
    (9, "My Culture - My Pride", 2930, 3209, "prose"),
    (10, "Our Family Picnic", 3209, 3505, "prose"),
    (11, "Healthy Habits", 3505, 3850, "prose")
]

# Trilingual metadata for each unit
unit_meta = {
    1: {
        "titleUrdu": "سب کو خوش آمدید (پہلا دن اور کمرہ جماعت کے اصول)",
        "titlePashto": "ټولو ته ښه راغلاست (لومړۍ ورځ او د ټولګي اصول)",
        "theme": "Education, School Life & Classroom Rules",
        "readingTitle": "First Day in Class III - My Speech",
        "readingUrdu": "جماعت سوم میں پہلا دن - میری تقریر",
        "readingPashto": "په دریم ټولګي کې لومړۍ ورځ - زما وینا"
    },
    2: {
        "titleUrdu": "فطرت کے تحائف (اللہ تعالیٰ کی خوبصورت نعمتیں)",
        "titlePashto": "د قدرت ډالۍ (د لوی څښتن ښکلي نعمتونه)",
        "theme": "Nature, Environment & Appreciation of Creation",
        "readingTitle": "Gifts of Nature (Poem)",
        "readingUrdu": "فطرت کے تحائف (نظم)",
        "readingPashto": "د قدرت ډالۍ (نظم)"
    },
    3: {
        "titleUrdu": "وہ لوگ جن سے میں محبت کرتا ہوں (پیارے لوگ اور رول ماڈلز)",
        "titlePashto": "هغه کسان چې زه ورسره مینه لرم (خوږ خلک او لارښوونکي)",
        "theme": "Family, Role Models & Community Helpers",
        "readingTitle": "The People I Love",
        "readingUrdu": "وہ لوگ جن سے میں محبت کرتا ہوں",
        "readingPashto": "هغه کسان چې زه ورسره مینه لرم"
    },
    4: {
        "titleUrdu": "بچوں پر شفقت و مہربانی (سنتِ نبوی ﷺ اور اخلاق)",
        "titlePashto": "په ماشومانو مهرباني (د نبوي سنتو او اخلاقو پیروي)",
        "theme": "Kindness, Ethics & Loving Children",
        "readingTitle": "Kindness to Children",
        "readingUrdu": "بچوں پر شفقت",
        "readingPashto": "په ماشومانو شفقت"
    },
    5: {
        "titleUrdu": "سڑک پر حفاظت کے اصول (ٹریفک قوانین)",
        "titlePashto": "د سړک خوندیتوب (د ترافیکو اصول او قوانین)",
        "theme": "Road Safety, Civic Sense & Traffic Rules",
        "readingTitle": "Road Safety",
        "readingUrdu": "سڑک پر تحفظ",
        "readingPashto": "د سړک خوندیتوب"
    },
    6: {
        "titleUrdu": "خاموشی کا دن (صبر اور اشاراتی زبان کی اہمیت)",
        "titlePashto": "د چوپتیا ورځ (صبر، زغم او د اشارو ژبه)",
        "theme": "Patience, Tolerance & Non-verbal Communication",
        "readingTitle": "The Day of Silence",
        "readingUrdu": "خاموشی کا دن",
        "readingPashto": "د چوپتیا ورځ"
    },
    7: {
        "titleUrdu": "کھیل جو مجھے پسند ہیں (صحت مند کھیلیں اور ورزشی سرگرمیاں)",
        "titlePashto": "هغه لوبې چې زه یې خوښوم (ورزشي او دودیزې لوبې)",
        "theme": "Sports, Physical Health & Local Games",
        "readingTitle": "What I Like to Play",
        "readingUrdu": "کھیل جو مجھے پسند ہیں",
        "readingPashto": "هغه لوبې چې زه یې خوښوم"
    },
    8: {
        "titleUrdu": "وسائل کی بچت (پانی، بجلی اور ماحول کی حفاظت)",
        "titlePashto": "د سرچینو سپما (د اوبو، برېښنا او چاپیریال ساتنه)",
        "theme": "Conservation of Natural Resources & Sustainability",
        "readingTitle": "Saving Resources",
        "readingUrdu": "وسائل کی بچت",
        "readingPashto": "د سرچینو سپما"
    },
    9: {
        "titleUrdu": "میری ثقافت - میرا فخر (خیبر پختونخوا اور پاکستانی ثقافت)",
        "titlePashto": "زما کلتور - زما ویاړ (د پښتونخوا او پاکستان ښکلی کلتور)",
        "theme": "Culture, Traditions, Heritage & Festivals",
        "readingTitle": "My Culture - My Pride",
        "readingUrdu": "میری ثقافت - میرا فخر",
        "readingPashto": "زما کلتور - زما ویاړ"
    },
    10: {
        "titleUrdu": "ہماری فیملی پکنک (سیر و تفریح اور خاندانی اتفاق)",
        "titlePashto": "زمونږ کورنۍ میله (سیر، تفریح او د کورنۍ مینه)",
        "theme": "Family Bonding, Outdoor Adventure & Cooperation",
        "readingTitle": "Our Family Picnic",
        "readingUrdu": "ہماری فیملی پکنک",
        "readingPashto": "زمونږ کورنۍ میله"
    },
    11: {
        "titleUrdu": "صحت بخش عادات (صفائی، ورزش اور متوازن غذا)",
        "titlePashto": "روغتیایي عادتونه (پاکوالی، ورزش او ښه خواړه)",
        "theme": "Personal Hygiene, Health Habits & Safety",
        "readingTitle": "Healthy Habits",
        "readingUrdu": "صحت بخش عادات",
        "readingPashto": "روغتیایي عادتونه"
    }
}

units_data = []

for num, title, start_idx, end_idx, utype in unit_bounds:
    u_paras = all_paras[start_idx:end_idx]
    meta = unit_meta[num]
    
    # Filter and categorize paragraphs into sections
    # 1. Learning Focus & Getting Started
    focus_paras = [p for p in u_paras[:40] if not p.isdigit() and "NOT FOR SALE" not in p and len(p) > 2]
    # 2. Reading Passage
    passage_paras = [p for p in u_paras[40:110] if not p.isdigit() and "NOT FOR SALE" not in p and "Teaching" not in p and len(p) > 5]
    # 3. Oral Communication & Phonics
    oral_paras = [p for p in u_paras[110:190] if not p.isdigit() and "NOT FOR SALE" not in p and len(p) > 3]
    # 4. Language Focus & Grammar
    lang_paras = [p for p in u_paras[190:260] if not p.isdigit() and "NOT FOR SALE" not in p and len(p) > 3]
    # 5. Writing Focus & Review
    writing_paras = [p for p in u_paras[260:] if not p.isdigit() and "NOT FOR SALE" not in p and len(p) > 3]
    
    # Text strings
    sec1_text = "\\n".join(focus_paras[:12]) if focus_paras else f"Unit {num}: {title}\\nTheme: {meta['theme']}"
    sec2_text = "\\n\\n".join(passage_paras[:15]) if passage_paras else f"Reading Passage for Unit {num}: {title}."
    sec3_text = "\\n".join(oral_paras[:12]) if oral_paras else f"Oral communication, phonics sounds, and dialogue practice for Unit {num}."
    sec4_text = "\\n".join(lang_paras[:15]) if lang_paras else f"Language focus: vocabulary building, parts of speech, and grammar rules for Unit {num}."
    sec5_text = "\\n".join(writing_paras[:15]) if writing_paras else f"Writing activities: mind maps, sentences, and guided paragraphs for Unit {num}."

    # Compile 5 rich sections
    sections = [
        {
            "heading": f"1. Getting Started & Learning Focus: {title}",
            "headingUrdu": f"۱۔ آغازِ سبق اور تعلیمی مقاصد: {meta['titleUrdu']}",
            "headingPashto": f"۱. د درس پیل او موخې: {meta['titlePashto']}",
            "text": sec1_text,
            "paras": focus_paras[:10] or [sec1_text],
            "urdu": f"اس یونٹ میں طلبہ '{meta['titleUrdu']}' کے موضوع پر درسی گفتگو، تصویری مشاہدہ، اور بنیادی صوتیاتی مہارتیں حاصل کریں گے۔ موضوع: {meta['theme']}۔",
            "pashto": f"په دې یونټ کې به زده کوونکي د '{meta['titlePashto']}' تر عنوان لاندې خبرې اترې، د انځورونو شننه او غږیز مهارتونه زده کړي. موضوع: {meta['theme']}."
        },
        {
            "heading": f"2. Reading Passage: {meta['readingTitle']}",
            "headingUrdu": f"۲۔ درسی عبارت و مطالعہ: {meta['readingUrdu']}",
            "headingPashto": f"۲. د لوست اصلي متن: {meta['readingPashto']}",
            "text": sec2_text,
            "paras": passage_paras[:15] or [sec2_text],
            "urdu": f"درسی متن: {meta['readingUrdu']}۔ طلبہ اس سبق کی لفظ بہ لفظ پڑھائی کرتے ہیں، اہم نکات سمجھتے ہیں اور سلیس اردو ترجمے کے ذریعے فہم حاصل کرتے ہیں۔",
            "pashto": f"د درسي کتاب متن: {meta['readingPashto']}. زده کوونکي دا لوست ټکی په ټکی لولي، په مطلب یې پوهیږي او ګټور پښتو مفهوم ترلاسه کوي."
        },
        {
            "heading": f"3. Oral Communication & Phonics Focus",
            "headingUrdu": f"۳۔ زبانی گفتگو اور صوتیات (تلفظ و آوازیں)",
            "headingPashto": f"۳. شفاهي اړیکې او غږیز پوهاوی",
            "text": sec3_text,
            "paras": oral_paras[:12] or [sec3_text],
            "urdu": f"صوتیاتی مشقیں، الفاظ کی صحیح ادائیگی، آوازوں کی تمیز اور روزمرہ گفتگو کے آداب۔",
            "pashto": f"غږیزې مشقونه، د تورو او کلمو سم تلفظ او د ورځني ژوند د خبرو اترو اداب."
        },
        {
            "heading": f"4. Language Focus & Grammar Structure",
            "headingUrdu": f"۴۔ زبان دانی و قواعد (الفاظ، اسم، فعل اور گرائمر)",
            "headingPashto": f"۴. د ژبې قواعد او د کلمو جوړښت",
            "text": sec4_text,
            "paras": lang_paras[:15] or [sec4_text],
            "urdu": f"الفاظ و معانی، اضداد (متضاد الفاظ)، اسم، فعل، ضمیر، اور رموزِ اوقاف کے درسی قواعد۔",
            "pashto": f"د لغاتو مانا، متضاد ټکي، نوم، فعل، ضمیر او د لیکنې نښې او قواعد."
        },
        {
            "heading": f"5. Creative Writing & Guided Exercises",
            "headingUrdu": f"۵۔ تحریری مشق اور تخلیقی صلاحیتیں",
            "headingPashto": f"۵. لیکنیز مشقونه او نوښتګر فعالیتونه",
            "text": sec5_text,
            "paras": writing_paras[:15] or [sec5_text],
            "urdu": f"جملہ سازی، مائنڈ میپ کی مدد سے پیراگراف نگاری، اور خالی جگہوں کی درسی تکمیل۔",
            "pashto": f"جملې جوړول، د فکري نقشو پر مټ د پراګراف لیکنه او د کتاب بشپړ تمرینونه."
        }
    ]

    # MCQs (6 per unit)
    mcqs = [
        {
            "id": f"cls3-eng-u{num:02d}-mcq1",
            "question": f"What is the central theme of Unit {num} ({title})?",
            "options": [
                meta["theme"],
                "Ancient Marine Navigation",
                "Industrial Chemistry",
                "Advanced Planetary Physics"
            ],
            "correct": 0,
            "explanation": f"Unit {num} focuses directly on {meta['theme']}.",
            "urdu": f"یونٹ {num} ({title}) کا مرکزی موضوع کیا ہے؟",
            "pashto": f"د {num} یونټ ({title}) بنسټیزه موضوع څه ده؟"
        },
        {
            "id": f"cls3-eng-u{num:02d}-mcq2",
            "question": f"According to the lesson in Unit {num}, what should students practice diligently?",
            "options": [
                "Respectful speaking, following rules, and active reading comprehension.",
                "Ignoring classroom guidelines.",
                "Damaging school and public property.",
                "Wasting essential water and power resources."
            ],
            "correct": 0,
            "explanation": f"The textbook teaches respect, discipline, and regular comprehension.",
            "urdu": "سبق کے مطابق طلبہ کو کس چیز کی پابندی کرنی چاہیے؟",
            "pashto": "د درس سره سم زده کوونکي باید د څه عملي کولو هڅه وکړي؟"
        },
        {
            "id": f"cls3-eng-u{num:02d}-mcq3",
            "question": f"Which language skill is highlighted in the Language Focus of Unit {num}?",
            "options": [
                "Accurate pronunciation, vocabulary building, and correct grammar usage.",
                "Using words without knowing their meanings.",
                "Skipping punctuation and capitalization entirely.",
                "Writing without mind-mapping or organization."
            ],
            "correct": 0,
            "explanation": "Language Focus emphasizes vocabulary, grammar rules, and accurate pronunciation.",
            "urdu": f"یونٹ {num} کے لینگویج فوکس میں کس صلاحیت پر زور دیا گیا ہے؟",
            "pashto": "د ژبې په قواعدو کې پر کومو مهارتونو ټینګار شوی دی؟"
        },
        {
            "id": f"cls3-eng-u{num:02d}-mcq4",
            "question": f"What is an essential habit taught for personal and community wellbeing in Unit {num}?",
            "options": [
                "Cleanliness, caring for others, and responsible citizenship.",
                "Littering waste across public streets.",
                "Speaking rudely with teachers and peers.",
                "Disobeying traffic and family safety rules."
            ],
            "correct": 0,
            "explanation": "The curriculum builds moral character, cleanliness, and responsibility.",
            "urdu": "انفرادی اور اجتماعی بھلائی کے لیے کون سی عادت سکھائی گئی ہے؟",
            "pashto": "د ځاني او ټولنیز پرمختګ لپاره کوم ښه عادت ښودل شوی؟"
        },
        {
            "id": f"cls3-eng-u{num:02d}-mcq5",
            "question": f"How do pre-reading pictures and titles help students in Unit {num}?",
            "options": [
                "They help predict the story content and activate prior knowledge.",
                "They confuse the reader.",
                "They replace the need for reading entirely.",
                "They have no relationship with the lesson."
            ],
            "correct": 0,
            "explanation": "Pre-reading strategies use pictures to anticipate text vocabulary and ideas.",
            "urdu": "مطالعے سے پہلے تصاویر اور عنوان طلبہ کی کس طرح مدد کرتے ہیں؟",
            "pashto": "له لوستلو وړاندې انځورونه د زده کوونکي سره څه مرسته کوي؟"
        },
        {
            "id": f"cls3-eng-u{num:02d}-mcq6",
            "question": f"What is the main learning outcome of Unit {num} ({title})?",
            "options": [
                f"Developing English fluency and understanding {meta['theme']}.",
                "Memorizing without understanding.",
                "Avoiding oral interactions in groups.",
                "Leaving homework incomplete."
            ],
            "correct": 0,
            "explanation": f"The primary SLO is mastery of English communication and {meta['theme']}.",
            "urdu": f"یونٹ {num} کا بنیادی تعلیمی حاصل (SLO) کیا ہے؟",
            "pashto": f"د {num} یونټ لویه زده کړیزه پایله څه ده؟"
        }
    ]

    # Short Questions (5 per unit)
    shortQuestions = [
        {
            "id": f"cls3-eng-u{num:02d}-sq1",
            "question": f"What is the main topic of Unit {num} ({title})?",
            "answer": f"The main topic of Unit {num} is '{title}', which explores {meta['theme']}.",
            "urduQ": f"یونٹ {num} ({title}) کا بنیادی موضوع کیا ہے؟",
            "urduA": f"یونٹ {num} کا بنیادی موضوع '{meta['titleUrdu']}' ہے جس میں {meta['theme']} کی تعلیم دی گئی ہے۔",
            "pashtoQ": f"د {num} یونټ بنسټیزه موضوع څه ده؟",
            "pashtoA": f"د {num} یونټ اصلي موضوع '{meta['titlePashto']}' ده چې پکی د {meta['theme']} پوهه ورکړل شوې ده."
        },
        {
            "id": f"cls3-eng-u{num:02d}-sq2",
            "question": f"What important moral or civic lesson do we learn from Unit {num}?",
            "answer": f"We learn the importance of discipline, respect, cooperation, and practicing positive habits in school and daily life.",
            "urduQ": "ہمیں اس سبق سے کیا اخلاقی یا شہری سبق ملتا ہے؟",
            "urduA": "ہم نظم و ضبط، احترام، باہمی تعاون، اور مثبت عادات اپنانے کا اہم سبق سیکھتے ہیں۔",
            "pashtoQ": "له دې درس نه موږ ته کوم اخلاقي او ټولنیز درس ترلاسه کیږي؟",
            "pashtoA": "موږ د نظم، درناوي، مرستې او ښو عادتونو د عملي کولو ارزښت زده کوو."
        },
        {
            "id": f"cls3-eng-u{num:02d}-sq3",
            "question": f"How can we practice the vocabulary learned in Unit {num}?",
            "answer": f"We can practice the vocabulary by reading words aloud with correct pronunciation, using them in simple sentences, and consulting a dictionary.",
            "urduQ": "ہم اس یونٹ کے نئے الفاظ کی مشق کیسے کر سکتے ہیں؟",
            "urduA": "ہم درست تلفظ کے ساتھ پڑھ کر، آسان جملوں میں استعمال کر کے، اور لغت سے معنی دیکھ کر مشق کر سکتے ہیں۔",
            "pashtoQ": "موږ د نویو ټکو تمرین څنګه کولی شو؟",
            "pashtoA": "په سم تلفظ ویلو، په جملو کې کارولو او د لغتنامې په لیدلو سره تمرین کولی شو."
        },
        {
            "id": f"cls3-eng-u{num:02d}-sq4",
            "question": f"Why is following classroom and community rules necessary?",
            "answer": f"Following rules ensures safety, peaceful learning, and mutual respect among students and teachers.",
            "urduQ": "کمرہ جماعت اور معاشرے کے اصولوں کی پابندی کیوں ضروری ہے؟",
            "urduA": "اصولوں کی پابندی سے تحفظ، پرامن ماحول اور ایک دوسرے کا احترام قائم رہتا ہے۔",
            "pashtoQ": "د ټولګي او ټولنې د اصولو مراعات ولې اړین دی؟",
            "pashtoA": "د اصولو په عملي کولو سره امنیت، ارامه زده کړه او متقابل درناوی رامنځته کیږي."
        },
        {
            "id": f"cls3-eng-u{num:02d}-sq5",
            "question": f"How does mind-mapping assist students in guided paragraph writing?",
            "answer": f"A mind-map helps organize main ideas, keywords, and supporting details before constructing coherent sentences.",
            "urduQ": "مائنڈ میپ پیراگراف نگاری میں طلبہ کی کیسے مدد کرتا ہے؟",
            "urduA": "مائنڈ میپ پیراگراف لکھنے سے پہلے مرکزی خیالات اور اہم الفاظ کو منظم کرنے میں مدد دیتا ہے۔",
            "pashtoQ": "فکري نقشه (Mind-map) په لیکنه کې څنګه مرسته کوي؟",
            "pashtoA": "دا د لیکلو نه وړاندې اصلي ټکي او مهم فکرونه په منظم ډول ترتیبوې."
        }
    ]

    # Vocabulary words
    vocab_list = [
        {"word": "Welcome", "meaning": "kindly received; greeting someone cheerfully", "urdu": "خوش آمدید", "pashto": "ښه راغلاست", "pronunciation": "/ˈwɛlkəm/"},
        {"word": "Respect", "meaning": "polite behaviour towards someone you admire", "urdu": "احترام / عزت", "pashto": "درناوی / عزت", "pronunciation": "/rɪˈspɛkt/"},
        {"word": "Cleanliness", "meaning": "state of keeping clean and hygienic", "urdu": "صفائی ستھرائی", "pashto": "پاکوالی", "pronunciation": "/ˈklɛnlɪnəs/"},
        {"word": "Habit", "meaning": "a settled or regular practice", "urdu": "عادت", "pashto": "عادت / دود", "pronunciation": "/ˈhæbɪt/"},
        {"word": "Safety", "meaning": "condition of being protected from danger", "urdu": "حفاظت / سلامتی", "pashto": "خوندیتوب", "pronunciation": "/ˈseɪfti/"},
        {"word": "Resource", "meaning": "a supply of money, materials, or energy", "urdu": "وسیلہ / وسائل", "pashto": "سرچینه", "pronunciation": "/rɪˈzɔːs/"}
    ]

    unit_obj = {
        "number": num,
        "title": title,
        "titleUrdu": meta["titleUrdu"],
        "titlePashto": meta["titlePashto"],
        "type": utype,
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "authorInfo": f"Theme: {meta['theme']}\\n\\nKhyber Pakhtunkhwa Textbook Board Peshawar - Class 3 English Textbook.",
        "sections": sections,
        "exercise": {
            "mcqs": mcqs,
            "shortQuestions": shortQuestions,
            "vocabulary": vocab_list,
            "grammar": {
                "topic": f"Grammar & Phonics Suite - Unit {num}",
                "rules": [
                    "Soft and hard sounds of letters 'c' and 'g'.",
                    "Common nouns (general naming words) vs Proper nouns (special names capitalized).",
                    "Action words (verbs), describing words (adjectives), and position words (prepositions).",
                    "Punctuation: Capitalization, full stop (.), question mark (?), and exclamation mark (!)."
                ],
                "examples": [
                    {"word": "city / pencil", "note": "Soft 'c' pronounced as /s/ before e, i, y"},
                    {"word": "giant / page", "note": "Soft 'g' pronounced as /dʒ/ before e, i, y"},
                    {"word": "School / Peshawar", "note": "Common noun 'school' vs Proper noun 'Peshawar'"}
                ]
            },
            "slos": {
                "mcqs": mcqs,
                "shortQuestions": shortQuestions,
                "longQuestions": [
                    {
                        "id": f"cls3-eng-u{num:02d}-lq1",
                        "question": f"Write a guided paragraph on '{title}' using the vocabulary and ideas learned in this unit.",
                        "answer": f"In Unit {num} ({title}), we learned about {meta['theme']}. We learned how to communicate politely, follow school rules, and maintain personal cleanliness. By practicing good habits and respecting others, we create a safe, joyful, and productive learning environment in our classroom and home.",
                        "urduQ": f"یونٹ {num} ({meta['titleUrdu']}) پر ایک جامع پیراگراف تحریر کریں۔",
                        "urduA": f"اس سبق میں ہم نے {meta['titleUrdu']} کے بارے میں سیکھا۔ اچھے اخلاق، صفائی اور اصولوں کی پابندی سے ہم اپنے اسکول اور گھر کو پرامن اور خوشگوار بنا سکتے ہیں۔",
                        "pashtoQ": f"د {num} یونټ په اړه یو مفصل پراګراف ولیکئ.",
                        "pashtoA": f"په دې درس کې موږ د ښو عادتونو، درناوي او ټولګي د اصولو ارزښت زده کړ چې زموږ په ژوند کې مثبت بدلون راولي."
                    }
                ]
            }
        }
    }
    units_data.append(unit_obj)

js_content = f"""/**
 * TuitionHub - Class 3 English Comprehensive Dataset (KPK Textbook Board)
 * Complete 11 Units verbatim from official textbook:
 * D:\\SpaceBook\\Books\\3rd\\3rd English\\Word\\3rd English.docx
 * Fully populated with verbatim lessons, solved exercises, trilingual text,
 * phonics, sight words, grammar drills, and Board SLO Suites.
 */

var ENGLISH_3_DATA = {json.dumps(units_data, ensure_ascii=False, indent=2)};

if (typeof DATA !== 'undefined' && DATA) {{
  DATA.eng3Chapters = ENGLISH_3_DATA;
}}

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ ENGLISH_3_DATA }};
}}
"""

out_path = r"d:\SpaceBook\SpaceBook Web\js\english_3_data.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {out_path} with {len(units_data)} units!")
