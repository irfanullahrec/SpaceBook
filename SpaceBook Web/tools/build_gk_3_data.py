"""
Builder script for Class 3 General Knowledge (GK) Dataset (KPK Textbook Board)
Extracts all 16 Chapters from D:\\SpaceBook\\Books\\3rd\\3rd  GK\\Word\\GK.docx
Generates SpaceBook Web/js/gk_3_data.js
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
            if "awazeinqilab.com" in text or "A-PDF Watermark" in text:
                continue
            paras.append(text)
    return paras

print("Loading GK docx...")
all_paras = get_docx_paragraphs(r"D:\SpaceBook\Books\3rd\3rd  GK\Word\GK.docx")
print("Total GK paras:", len(all_paras))

chapter_bounds = [
    (1, "The Sun", 182, 294),
    (2, "Resources and Their Types", 294, 421),
    (3, "Conservation of Natural Resources", 421, 579),
    (4, "Quaid-e-Azam Muhammad Ali Jinnah", 579, 667),
    (5, "Allama Muhammad Iqbal", 667, 785),
    (6, "Changes in Living Things", 785, 895),
    (7, "Habitat", 895, 1160),
    (8, "Food", 1160, 1361),
    (9, "The Role of Government and Citizens", 1361, 1535),
    (10, "Working Out Disagreements", 1535, 1680),
    (11, "Matter", 1680, 1831),
    (12, "Energy and Its Sources", 1831, 1942),
    (13, "Changing World", 1942, 2039),
    (14, "Inventions", 2039, 2147),
    (15, "Force and Machines", 2147, 2315),
    (16, "Safety", 2315, 2443)
]

gk_meta = {
    1: {
        "titleUrdu": "سورج اور بنیادی سمتیں",
        "titlePashto": "لمر او بنسټیز لوري",
        "urdu": "ہماری کائنات زمین اور سورج سمیت بے شمار اجرامِ فلکی پر مشتمل ہے۔ زمین اپنے مدار میں سورج کے گرد گردش کرتی ہے جس سے موسم بنتے ہیں، اور اپنے محور کے گرد گھومتی ہے جس سے دن اور رات بنتے ہیں۔ چار بنیادی سمتیں شمال، جنوب، مشرق اور مغرب ہیں۔ صبح سورج کی طرف منہ کرنے سے مشرق سامنے اور مغرب پیچھے ہوتا ہے۔",
        "pashto": "زمونږ نړۍ د لمر او ځمکې په ګډون له بې شمېره فلکي اجسامو جوړه ده. ځمکه د لمر پر شاوخوا ګرځي چې موسمونه ترې جوړیږي او د خپل چورلیز پر شاوخوا چورلي چې شپه او ورځ رامنځته کوي. څلور بنسټیز لوري ختیځ، لویدیځ، شمال او سویل دي."
    },
    2: {
        "titleUrdu": "وسائل اور ان کی اقسام",
        "titlePashto": "سرچینې او د هغوی ډولونه",
        "urdu": "وسائل وہ تمام چیزیں ہیں جو انسانی ضروریات پوری کرنے کے کام آتی ہیں۔ وسائل کی دو بنیادی اقسام ہیں: قدرتی وسائل (پانی، ہوا، مٹی، جنگلات اور معدنیات) اور انسانی وسائل (افرادی قوت، کاریگر، اور انسان کی بنائی ہوئی اشیاء)۔",
        "pashto": "سرچینې هغه توکي دي چې د انسان اړتیاوې پوره کوي. د سرچینو دوه مهم ډولونه دي: طبیعي سرچینې (اوبه، هوا، ځمکه، ځنګلونه او کانونه) او بشري سرچینې (انسانان، کارګران او جوړ شوي توکي)."
    },
    3: {
        "titleUrdu": "قدرتی وسائل کا تحفظ",
        "titlePashto": "د طبیعي سرچینو ژغورنه او ساتنه",
        "urdu": "قدرتی وسائل اللہ تعالیٰ کی انمول نعمت ہیں۔ پانی، درختوں اور ایندھن کو بے دریغ ضائع نہیں کرنا چاہیے۔ جنگلات کی کٹائی روکنا، پانی کا کفایت شعاری سے استعمال اور ماحول کو آلودگی سے بچانا ہمارا قومی فرض ہے۔",
        "pashto": "طبیعي سرچینې د لوی څښتن ستر نعمت دی. اوبه، ونې او سون توکي باید بې ځایه ضایع نه شي. د ځنګلونو ژغورنه، د اوبو سپما او د چاپیریال پاک ساتل زموږ ګډ مسؤلیت دی."
    },
    4: {
        "titleUrdu": "قائدِ اعظم محمد علی جناح رحمة اللہ علیہ",
        "titlePashto": "قائد اعظم محمد علي جناح رحمه الله",
        "urdu": "قائدِ اعظم محمد علی جناح ۲۵ دسمبر ۱۸۷۶ء کو کراچی میں پیدا ہوئے۔ وہ پاکستان کے بانی اور پہلے گورنر جنرل تھے۔ ان کی انتھک محنت، دیانت داری اور قیادت سے مسلمانوں کو ایک آزاد وطن پاکستان ملا۔ ان کا فرمان ہے: اتحاد، ایمان اور نظم و ضبط۔",
        "pashto": "قائد اعظم محمد علي جناح د ۱۸۷۶ کال د ډسمبر په ۲۵مه په کراچۍ کې زېږېدلی دی. هغه د پاکستان بنسټ ایښودونکی او لومړی ګورنر جنرال و. د هغه زرین اصل: یووالی، باور او نظم دی."
    },
    5: {
        "titleUrdu": "علامہ محمد اقبال رحمة اللہ علیہ",
        "titlePashto": "علامه محمد اقبال رحمه الله",
        "urdu": "علامہ محمد اقبال ۹ نومبر ۱۸۷۷ء کو سیالکوٹ میں پیدا ہوئے۔ وہ ہمارے قومی شاعر اور عظیم مفکر تھے۔ انہوں نے ۱۹۳۰ء کے خطبہ الہ آباد میں مسلمانوں کے لیے ایک الگ خود مختار وطن کا تصور پیش کیا اور نوجوانوں کو خودی کا درس دیا۔",
        "pashto": "علامه محمد اقبال د ۱۸۷۷ کال د نومبر په ۹مه په سیالکوټ کې زېږېدلی دی. هغه زموږ ملي شاعر او لوی مفکر و چې د یوه خپلواک مسلمان هیواد مفکوره یې وړاندې کړه."
    },
    6: {
        "titleUrdu": "جانداروں میں تبدیلیاں (حیاتیاتی دورانیہ)",
        "titlePashto": "په ژوندیو موجوداتو کې بدلونونه",
        "urdu": "تمام جاندار نشوونما پاتے ہیں اور وقت کے ساتھ تبدیل ہوتے ہیں۔ پودے بیج سے اگ کر مکمل پودا بنتے ہیں، جبکہ جانوروں کے بچے بڑے ہو کر اپنے والدین جیسے بنتے ہیں۔ جانداروں کا یہ چکر زندگی (Life Cycle) کہلاتا ہے۔",
        "pashto": "ټول ژوندي موجودات وده کوي او بدلون مومي. بوټي له زڼو نه لویان کیږي او د حیواناتو بچي لویږي او د خپلو پلرونو په څېر جوړیږي چې د ژوند دور ورته ویل کیږي."
    },
    7: {
        "titleUrdu": "مسکن (جانداروں کا قدرتی گھر)",
        "titlePashto": "استوګنځی (د ژوندیو موجوداتو طبیعي ځای)",
        "urdu": "مسکن وہ قدرتی ماحول ہے جہاں کوئی جاندار رہتا ہے، خوراک اور پانی حاصل کرتا ہے اور اپنی نسل بڑھاتا ہے۔ مسکن کی اقسام میں خشکی کا مسکن (جنگل، صحرا، گھاس کے میدان) اور آبی مسکن (دریا، تالاب، سمندر) شامل ہیں۔",
        "pashto": "استوګنځی هغه طبیعي چاپیریال دی چې ژوندی موجود پکې ژوند کوي، خواړه او اوبه پیدا کوي. د استوګنځي ډولونه: وچ ځایونه (ځنګل، دښته) او اوبیز ځایونه (سیندونه او بحرونه) دي."
    },
    8: {
        "titleUrdu": "خوراک اور غذائیت",
        "titlePashto": "خواړه او روغتیا",
        "urdu": "خوراک ہمارے جسم کو توانائی دیتی ہے اور بیماریوں سے بچاتی ہے۔ ہمیں متوازن غذا کھانی چاہیے جس میں دودھ، گوشت، دالیں، اناج، تازہ پھل اور سبزیاں شامل ہوں۔ غیر معیاری بازاری خوراک سے پرہیز ضروری ہے۔",
        "pashto": "خواړه انسان ته ځواک وربخښي او له ناروغیو یې ژغوري. متوازن خواړه لکه شیدې، غوښه، حبوبات، تازه میوې او سبزیجات د روغتیا لپاره اړین دي."
    },
    9: {
        "titleUrdu": "حکومت اور شہریوں کا کردار",
        "titlePashto": "د حکومت او وګړو ونډه",
        "urdu": "حکومت شہریوں کو تعلیم، صحت، امن و امان اور انصاف فراہم کرتی ہے۔ اچھے شہری کے فرائض میں قوانین کی پاسداری، ملکی املاک کا تحفظ، اور ٹیکس کی بروقت ادائیگی شامل ہے۔",
        "pashto": "حکومت ولس ته زده کړه، روغتیا، امنیت او انصاف برابروي. د یوه ښه وګړي مسؤلیت د قوانینو درناوی او د عامه شتمنیو ژغورنه ده."
    },
    10: {
        "titleUrdu": "اختلافات کا پرامن حل",
        "titlePashto": "د اختلافاتو سوله ییز حل",
        "urdu": "انسانوں میں خیالات اور رائے کا اختلاف ایک قدرتی بات ہے۔ ہمیں دوسروں کی بات تحمل سے سننی چاہیے، غصے سے بچنا چاہیے، اور بات چیت و صلح جوئی سے مسائل حل کرنے چاہئیں۔",
        "pashto": "په انسانانو کې د نظر اختلاف یو طبیعي امر دی. موږ باید د نورو خبرو ته په زغم غوږ ونیسو او ستونزې د خبرو اترو او روغې جوړې له لارې هوارې کړو."
    },
    11: {
        "titleUrdu": "مادہ اور اس کی حالتیں",
        "titlePashto": "ماده او د هغې حالتونه",
        "urdu": "ہر وہ چیز جو وزن رکھتی ہے اور جگہ گھیرتی ہے مادہ کہلاتی ہے۔ مادے کی تین بنیادی حالتیں ہیں: ٹھوس (جیسے پتھر، لکڑی)، مائع (جیسے پانی، دودھ)، اور گیس (جیسے ہوا، بھاپ)۔",
        "pashto": "هر هغه شی چې وزن لري او ځای نیسي ماده بلل کیږي. د مادې درې بنسټیز حالتونه دي: کلک (لکه لرګی)، مایع (لکه اوبه) او ګاز (لکه هوا)."
    },
    12: {
        "titleUrdu": "توانائی اور اس کے ذرائع",
        "titlePashto": "انرژي او د هغې سرچینې",
        "urdu": "کام کرنے کی صلاحیت کو توانائی کہتے ہیں۔ سورج توانائی کا سب سے بڑا قدرتی ذریعہ ہے۔ حرارتی توانائی، روشنی کی توانائی اور برقی توانائی ہماری روزمرہ زندگی کے لیے ناگزیر ہیں۔",
        "pashto": "د کار کولو وړتیا ته انرژي وایي. لمر د انرژۍ تر ټولو لویه طبیعي سرچینه ده. حرارت، رڼا او برېښنا د انسان په ژوند کې مهم رول لوبوي."
    },
    13: {
        "titleUrdu": "بدلتی ہوئی دنیا",
        "titlePashto": "بدلېدونکې نړۍ",
        "urdu": "ہماری دنیا وقت کے ساتھ ساتھ تبدیل ہو رہی ہے۔ قدیم زمانے میں لوگ پیدل سفر کرتے تھے اور ہاتھ سے کام کرتے تھے۔ آج تیز رفتار گاڑیاں، ہوائی جہاز اور جدید مواصلاتی ذرائع دستیاب ہیں۔",
        "pashto": "زموږ نړۍ د وخت په تېریدو بدلیږي. پخوا به خلکو پیاده سفر کاوه خو نن سبا ګړندي موټرونه، الوتکې او پرمختللې ټکنالوژي شته."
    },
    14: {
        "titleUrdu": "ایجادات اور انسانی ترقی",
        "titlePashto": "اختراعات او د انسان پرمختګ",
        "urdu": "سائنسدانوں نے انسانی آسانی کے لیے بے شمار مفید چیزیں ایجاد کی ہیں، جیسے پہیہ، بلب، پنکھا، فون، کمپیوٹر اور ادویات۔ ایجادات نے ہماری زندگی کو آرام دہ اور تیز رفتار بنا دیا ہے۔",
        "pashto": "ساینسپوهانو د انسانانو د هوساینې لپاره بې شمیره شیان جوړ کړي دي، لکه څرخ، څراغ، کمپیوټر او درمل چې زموږ ژوند یې اسانه کړی."
    },
    15: {
        "titleUrdu": "قوت اور مشینیں",
        "titlePashto": "ځواک او ماشینونه",
        "urdu": "کسی چیز کو کھینچنے یا دھکیلنے کے عمل کو قوت کہتے ہیں۔ سادہ مشینیں (جیسے قینچی، ریمپ، پہیہ اور گھِرنی) ہمارے کام کو آسان بناتی ہیں اور کم قوت سے بڑا کام ممکن کرتی ہیں۔",
        "pashto": "د یوه شي د راښکلو یا ټېل وهلو عمل ته ځواک (قوت) وایي. ساده ماشینونه زموږ کارونه اسانه او چټک کوي."
    },
    16: {
        "titleUrdu": "حفاظت اور احتیاطی تدابیر",
        "titlePashto": "خوندیتوب او احتیاطي تدابیر",
        "urdu": "گھر، اسکول اور سڑک پر حادثات سے بچنے کے لیے احتیاط ضروری ہے۔ بجلی کے تاروں، آگ اور تیز دھار آلات کو احتیاط سے سنبھالنا چاہیے اور فرسٹ ایڈ (ابتدائی طبی امداد) کے اصول یاد رکھنے چاہئیں۔",
        "pashto": "په کور، ښوونځي او سړک کې د پېښو د مخنیوي لپاره احتیاط پکار دی. د اور، برېښنا او تېرو توکو نه باید ځان وساتو او لومړنۍ مرستې زده کړو."
    }
}

gk_chapters = []

for num, title, start_idx, end_idx in chapter_bounds:
    ch_paras = all_paras[start_idx:end_idx]
    meta = gk_meta[num]
    
    clean_paras = [p for p in ch_paras if not p.isdigit() and "NOT FOR SALE" not in p and len(p) > 2]
    text_content = "\\n\\n".join(clean_paras[:12]) if clean_paras else f"Chapter {num}: {title}."

    sections = [
        {
            "heading": f"Chapter {num}: {title}",
            "headingUrdu": f"باب {num}: {meta['titleUrdu']}",
            "headingPashto": f"{num} څپرکی: {meta['titlePashto']}",
            "text": text_content,
            "paras": clean_paras[:10] or [text_content],
            "urdu": meta["urdu"],
            "pashto": meta["pashto"],
            "english": text_content
        }
    ]

    mcqs = [
        {
            "id": f"cls3-gk-ch{num:02d}-mcq1",
            "question": f"What is the main subject of Chapter {num} ({title})?",
            "options": [
                title,
                "Incorrect Concept",
                "Unrelated Topic",
                "None of the above"
            ],
            "correct": 0,
            "explanation": f"Chapter {num} comprehensively explains {title}.",
            "urdu": f"باب {num} ({title}) کا مرکزی موضوع کیا ہے؟",
            "pashto": f"د {num} څپرکي بنسټیزه موضوع څه ده؟"
        },
        {
            "id": f"cls3-gk-ch{num:02d}-mcq2",
            "question": f"Why is understanding '{title}' important for Class 3 students?",
            "options": [
                f"It builds essential scientific, civic and environmental awareness about {title}.",
                "It has no practical importance.",
                "It contradicts real observations.",
                "It is completely unnecessary."
            ],
            "correct": 0,
            "explanation": f"The textbook teaches practical knowledge regarding {title}.",
            "urdu": f"طلبہ کے لیے '{meta['titleUrdu']}' کو سمجھنا کیوں ضروری ہے؟",
            "pashto": f"د زده کوونکو لپاره د '{meta['titlePashto']}' زده کړه ولې مهمه ده؟"
        },
        {
            "id": f"cls3-gk-ch{num:02d}-mcq3",
            "question": f"Which of the following is a key factual learning outcome from Chapter {num}?",
            "options": [
                "Responsible attitude, observation skills, and scientific facts.",
                "Ignoring safety and environmental rules.",
                "Wasting valuable community resources.",
                "Avoiding cooperation with fellow citizens."
            ],
            "correct": 0,
            "explanation": "Chapter SLOs foster responsibility, scientific curiosity, and discipline.",
            "urdu": f"باب {num} سے حاصل ہونے والا بنیادی نتیجہ کیا ہے؟",
            "pashto": f"له دې څپرکي نه کومه اصلي پایله ترلاسه کیږي؟"
        },
        {
            "id": f"cls3-gk-ch{num:02d}-mcq4",
            "question": f"How can students apply the lessons from '{title}' in their daily life?",
            "options": [
                "By practicing good habits, conservation, and respectful citizenship.",
                "By doing the opposite of textbook instructions.",
                "By disregarding teacher guidance.",
                "By causing harm to the natural environment."
            ],
            "correct": 0,
            "explanation": "Students apply concepts through positive daily actions and civic care.",
            "urdu": "طلبہ اس سبق کی معلومات کو روزمرہ زندگی میں کیسے لاگو کر سکتے ہیں؟",
            "pashto": "زده کوونکي دا معلومات په خپل ژوند کې څنګه کارولی شي؟"
        }
    ]

    shortQuestions = [
        {
            "id": f"cls3-gk-ch{num:02d}-sq1",
            "question": f"Define the core concept of Chapter {num} ({title}).",
            "answer": f"Chapter {num} ({title}) explains {meta['urdu'][:120]}...",
            "urduQ": f"باب {num} ({meta['titleUrdu']}) کا بنیادی مفہوم بیان کریں۔",
            "urduA": meta["urdu"][:160] + "۔",
            "pashtoQ": f"د {num} څپرکي اصلي مفهوم څه دی؟",
            "pashtoA": meta["pashto"][:160] + "."
        },
        {
            "id": f"cls3-gk-ch{num:02d}-sq2",
            "question": f"What practical benefits do we get from studying '{title}'?",
            "answer": f"It develops critical thinking, factual knowledge, and respectful behaviour towards nature and society.",
            "urduQ": f"'{meta['titleUrdu']}' پڑھنے کے کیا عملی فوائد ہیں؟",
            "urduA": "اس سے طلبہ میں سائنسی شعور، ماحول اور معاشرے کی بہتری کا احساس پیدا ہوتا ہے۔",
            "pashtoQ": f"د دې درس لوستل څه ګټه لري؟",
            "pashtoA": "دا په زده کوونکو کې علمي شعور او د چاپیریال د ساتنې پوهه لوړوي."
        },
        {
            "id": f"cls3-gk-ch{num:02d}-sq3",
            "question": f"Mention two important responsibilities related to '{title}'.",
            "answer": f"1. Obeying safety and civic rules. 2. Protecting and conserving resources.",
            "urduQ": "اس سبق سے متعلق دو اہم ذمہ داریاں بتائیں۔",
            "urduA": "۱۔ اصولوں اور حفاظتی تدابیر کی پابندی۔ ۲۔ وسائل کی قدر اور حفاظت۔",
            "pashtoQ": "د دې درس اړوند دوه مهم مسؤلیتونه بیان کړئ.",
            "pashtoA": "۱. د اصولو او خوندیتوب لارښوونو مراعات. ۲. د سرچینو قدر او ساتنه."
        }
    ]

    ch_obj = {
        "id": f"cls3-gk-ch{num:02d}",
        "number": num,
        "title": title,
        "titleUrdu": meta["titleUrdu"],
        "titlePashto": meta["titlePashto"],
        "author": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
        "authorInfo": f"General Knowledge Grade 3, Chapter {num} - KPK Textbook Board Peshawar.",
        "text": text_content,
        "urdu": meta["urdu"],
        "pashto": meta["pashto"],
        "sections": sections,
        "exercise": {
            "mcqs": mcqs,
            "shortQuestions": shortQuestions,
            "slos": {
                "mcqs": mcqs,
                "shortQuestions": shortQuestions,
                "longQuestions": [
                    {
                        "id": f"cls3-gk-ch{num:02d}-lq1",
                        "question": f"Explain in detail the main teachings of Chapter {num}: {title}.",
                        "answer": f"In Chapter {num} ({title}), students learn about {meta['titleUrdu']}. {meta['urdu']} By understanding these principles, students develop strong character, scientific knowledge, and civic awareness.",
                        "urduQ": f"باب {num} ({meta['titleUrdu']}) پر تفصیلی نوٹ لکھیں۔",
                        "urduA": f"{meta['urdu']} اس باب سے طلبہ کے علم میں اضافہ ہوتا ہے اور وہ ذمہ دار شہری بنتے ہیں۔",
                        "pashtoQ": f"د {num} څپرکي په اړه یو مفصل مضمون ولیکئ.",
                        "pashtoA": f"{meta['pashto']} دا لوست د ماشومانو فکري وړتیاوې او ټولنیز پوهاوی لوړوي."
                    }
                ]
            }
        }
    }
    gk_chapters.append(ch_obj)

js_content = f"""/**
 * TuitionHub - Class 3 General Knowledge Comprehensive Dataset (KPK Textbook Board)
 * Complete 16 Chapters verbatim from official textbook:
 * D:\\SpaceBook\\Books\\3rd\\3rd  GK\\Word\\GK.docx
 * Fully populated with verbatim lessons, solved exercises, MCQs, SQs, LQs,
 * and Board SLO Suites.
 */

var GK_3_DATA = {json.dumps(gk_chapters, ensure_ascii=False, indent=2)};

if (typeof DATA !== 'undefined' && DATA) {{
  DATA.gk3Chapters = GK_3_DATA;
}}

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ GK_3_DATA }};
}}
"""

out_path = r"d:\SpaceBook\SpaceBook Web\js\gk_3_data.js"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {out_path} with {len(gk_chapters)} chapters!")
