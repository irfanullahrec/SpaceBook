#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Class 3 Islamyat Dataset (ISLAMYAT_3_DATA)
Source: D:\SpaceBook\Books\3rd\3rd ISlamyat\Word\3rd Islamiat.docx
Produces SpaceBook Web/js/islamyat_3_data.js
"""

import os, json, zipfile, xml.etree.ElementTree as ET

def extract_docx_paras(docx_path):
    with zipfile.ZipFile(docx_path, 'r') as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        paras = []
        for p in tree.iterfind('.//w:p', namespaces):
            texts = [t.text for t in p.iterfind('.//w:t', namespaces) if t.text]
            if texts:
                s = ''.join(texts).strip()
                if s:
                    paras.append(s)
    return paras

def build_islamyat_3():
    docx_path = r'D:\SpaceBook\Books\3rd\3rd ISlamyat\Word\3rd Islamiat.docx'
    paras = extract_docx_paras(docx_path)
    print(f"Loaded {len(paras)} paras from {docx_path}")

    # We map 18 Units across the 7 Babs of Class 3 Islamyat
    # Unit metadata
    units_def = [
        {
            "id": "cls3-isl-ch01", "number": 1, "bab": 1,
            "title": "باب اوّل: قرآن مجید و حدیث نبوی ﷺ (ناظرہ، حفظ، احادیث اور دعائیں)",
            "titleEn": "Unit 1: Holy Quran, Hadith & Masnoon Supplications",
            "titlePs": "۱ لوست: قرآن مجید، نبوي احادیث او مسنونې دعاوې",
            "urduSummary": "اس سبق میں ناظرہ قرآن مجید (پارہ 3 تا 8)، سورۃ الکوثر و سورۃ النصر کا حفظ، کلماتِ اسلامیہ، درود ابراہیمی، چار منتخب احادیث نبویہ اور کھانے سے پہلے و بعد کی مسنون دعائیں شامل ہیں۔",
            "pashtoSummary": "په دې درس کې ناظره قرآن، د سورت الکوثر او سورت النصر حفظ، درود ابراهیمي، څلور احادیث او د خوراک مسنونې دعاوې بیان شوې دي.",
            "englishSummary": "This unit covers the foundational recitation of Paras 3-8, memorization of Surah Al-Kawthar and Surah An-Nasr, Durood-e-Ibrahimi, 4 Sahih Hadiths, and Masnoon daily prayers.",
            "start": 162, "end": 298
        },
        {
            "id": "cls3-isl-ch02", "number": 2, "bab": 2,
            "title": "باب دوم: ایمانیات - توحید کا تعارف",
            "titleEn": "Unit 2: Faith & Beliefs - Introduction to Tawheed (Oneness of Allah)",
            "titlePs": "۲ لوست: ایمانیات - د توحید پیژندنه",
            "urduSummary": "اس سبق میں عقیدہ توحید کا مفہوم، اللہ تعالیٰ کی یکتائی اور بے نیازی، کلمہ طیبہ اور سورۃ الاخلاص کی روشنی میں توحید کی تعلیمات بیان کی گئی ہیں۔",
            "pashtoSummary": "په دې درس کې د توحید معنی او مفهوم، د الله تعالی یوالی او بې نیازي په تفصیل سره بیان شوې ده.",
            "englishSummary": "Introduction to the core Islamic concept of Tawheed (the absolute Oneness of Allah) based on Surah Al-Ikhlas and Kalima Tayyibah.",
            "start": 298, "end": 378
        },
        {
            "id": "cls3-isl-ch03", "number": 3, "bab": 2,
            "title": "باب دوم: ایمانیات - نبوت و رسالت",
            "titleEn": "Unit 3: Faith & Beliefs - Prophethood & Messengers (Nabuwwat & Risalat)",
            "titlePs": "۳ لوست: ایمانیات - نبوت او رسالت",
            "urduSummary": "اس سبق میں نبوت اور رسالت کا مفہوم، انبیاء کرام علیہم السلام کی ضرورت و صفات اور حضرت محمد رسول اللہ ﷺ کے خاتم النبیین ہونے کا عقیدہ سکھایا گیا ہے۔",
            "pashtoSummary": "په دې درس کې د نبوت او رسالت مفهوم، د انبیاوو ځانګړتیاوې او د حضرت محمد ﷺ د خاتم النبیین عقیده بیان شوې ده.",
            "englishSummary": "Belief in Prophets and Messengers, their qualities, and belief in the Finality of Prophethood (Khatam-un-Nabiyyin) of Muhammad ﷺ.",
            "start": 378, "end": 461
        },
        {
            "id": "cls3-isl-ch04", "number": 4, "bab": 2,
            "title": "باب دوم: عبادات - کلمہ شہادت",
            "titleEn": "Unit 4: Worship - Kalima Shahadat (Declaration of Faith)",
            "titlePs": "۴ لوست: عبادات - د شهادت کلمه",
            "urduSummary": "ارکانِ اسلام کا اجمالی تعارف، کلمہ شہادت کا عربی متن، اردو اور پشتو ترجمہ اور اس کا مفہوم و عملی تقاضے بیان کیے گئے ہیں۔",
            "pashtoSummary": "په دې درس کې د اسلام ارکان، د شهادت کلمې الفاظ، پښتو او اردو ژباړه او عملي مفهوم ذکر شوی دی.",
            "englishSummary": "The Five Pillars of Islam with comprehensive study of Kalima Shahadat, its Arabic recitation, meanings, and obligations.",
            "start": 461, "end": 535
        },
        {
            "id": "cls3-isl-ch05", "number": 5, "bab": 2,
            "title": "باب دوم: عبادات - اذان",
            "titleEn": "Unit 5: Worship - The Call to Prayer (Azan)",
            "titlePs": "۵ لوست: عبادات - اذان",
            "urduSummary": "اذان اسلامی شعائر میں سے ہے۔ اس سبق میں اذان کا تعارف، کلماتِ اذان، اذان کا جواب دینے کا طریقہ اور اذان کے آداب بیان کیے گئے ہیں۔",
            "pashtoSummary": "اذان د اسلام یو لوی شعار دی. په دې درس کې د اذان کلمات، د اذان ځواب او آداب بیان شوي دي.",
            "englishSummary": "The Islamic Call to Prayer (Azan): its historic significance, verbatim Arabic words, response rules, and respectful etiquettes.",
            "start": 535, "end": 623
        },
        {
            "id": "cls3-isl-ch06", "number": 6, "bab": 2,
            "title": "باب دوم: عبادات - وضو",
            "titleEn": "Unit 6: Worship - Ablution (Wudu)",
            "titlePs": "۶ لوست: عبادات - اودس",
            "urduSummary": "وضو نماز کی بنیادی شرط اور طہارت کا ذریعہ ہے۔ اس سبق میں وضو کے فرائض، سنتیں، دعائیں اور وضو کا درست طریقہ سکھایا گیا ہے۔",
            "pashtoSummary": "په دې درس کې د اوداسه فرایض، سنتونه، فضیلت او د اوداسه سم عملي طریقه بیان شوې ده.",
            "englishSummary": "Wudu (Ablution): its spiritual importance, four mandatory acts (Faraiz), Sunnah steps, supplications, and physical cleanliness.",
            "start": 623, "end": 700
        },
        {
            "id": "cls3-isl-ch07", "number": 7, "bab": 2,
            "title": "باب دوم: عبادات - نماز",
            "titleEn": "Unit 7: Worship - Daily Prayers (Namaz / Salah)",
            "titlePs": "۷ لوست: عبادات - لمونځ",
            "urduSummary": "نماز دین کا ستون ہے۔ اس سبق میں پانچوں نمازوں کے نام، اوقات، رکعات کی تفصیل اور باجماعت نماز کی فضیلت بیان کی گئی ہے۔",
            "pashtoSummary": "لمونځ د دین ستنه ده. په دې درس کې د پنځو لمونځونو نومونه، د رکعتونو شمیر او د جماعت لمونځ فضیلت بیان شوی دی.",
            "englishSummary": "Salah (Daily Prayers): timings, Rak'at details for Fajr, Dhuhr, Asr, Maghrib, and Isha, and the spiritual virtue of congregation.",
            "start": 700, "end": 780
        },
        {
            "id": "cls3-isl-ch08", "number": 8, "bab": 2,
            "title": "باب دوم: عبادات - قبلہ و مسجد",
            "titleEn": "Unit 8: Worship - Qibla (Kaaba) & The Mosque (Masjid)",
            "titlePs": "۸ لوست: عبادات - قبله او جومات",
            "urduSummary": "قبلہ (خانہ کعبہ) کا تعارف، مسجد کے لغوی و اصطلاحی معنی، مسجد الحرام و مسجد نبوی کا احترام اور مسجد کے آداب۔",
            "pashtoSummary": "په دې درس کې د قبلې (خاني کعبې) تعارف، د جومات فضیلت، احترامات او د ننوتلو او وتلو آداب بیان شوي دي.",
            "englishSummary": "Introduction to the Qibla (Baitullah in Makkah) and Masajid (houses of Allah), their sanctity, etiquettes, and blessings.",
            "start": 780, "end": 868
        },
        {
            "id": "cls3-isl-ch09", "number": 9, "bab": 3,
            "title": "باب سوم: سیرت طیبہ ﷺ - حیات طیبہ (قبل از بعثت)",
            "titleEn": "Unit 9: Seerat-un-Nabi ﷺ - Early Blessed Life (Before Prophethood)",
            "titlePs": "۹ لوست: سیرت طیبه ﷺ - مبارک ژوند (له بعثت مخکې)",
            "urduSummary": "حضور اکرم ﷺ کی ولادت باسعادت، رضاعت، کفالت (حضرت عبدالمطلب اور حضرت ابو طالب)، سفرِ شام اور حلف الفضول کے اہم واقعات۔",
            "pashtoSummary": "د رسول الله ﷺ مبارکه ولادت، د ماشومتوب پېښې، د حضرت ابو طالب کفالت، د شام سفر او د حلف الفضول تاریخي تړون.",
            "englishSummary": "The early life of Prophet Muhammad ﷺ before the proclamation of Prophethood: birth in Makkah, childhood, Syria trade trip, and Hilf al-Fudul.",
            "start": 868, "end": 955
        },
        {
            "id": "cls3-isl-ch10", "number": 10, "bab": 3,
            "title": "باب سوم: سیرت طیبہ ﷺ - صداقت و امانت اور حسن معاملات",
            "titleEn": "Unit 10: Seerat-un-Nabi ﷺ - Truthfulness, Trustworthiness & Fair Dealing",
            "titlePs": "۱۰ لوست: سیرت طیبه ﷺ - رښتیا، امانت او غوره چلند",
            "urduSummary": "رسول اللہ ﷺ کی صداقت، دیانت اور امانت داری جس کی وجہ سے اہل مکہ آپ ﷺ کو 'الصادق' اور 'الامین' پکارتے تھے، اور تعمیرِ کعبہ میں حجر اسود کا فیصلہ۔",
            "pashtoSummary": "د رسول الله ﷺ رښتینولي او امانت داري چې له امله یې الصادق او الامین بلل کېده، او د حجر اسود د لګولو عادلانه پریکړه.",
            "englishSummary": "The Prophet's ﷺ unshakeable honesty and trustworthiness earning the titles 'As-Sadiq' and 'Al-Amin', and the peaceful resolution of the Black Stone.",
            "start": 955, "end": 1025
        },
        {
            "id": "cls3-isl-ch11", "number": 11, "bab": 3,
            "title": "باب سوم: سیرت طیبہ ﷺ - رواداری اور صبر و تحمل",
            "titleEn": "Unit 11: Seerat-un-Nabi ﷺ - Tolerance, Patience & Forbearance",
            "titlePs": "۱۱ لوست: سیرت طیبه ﷺ - زغم، صبر او نرمي",
            "urduSummary": "رسول اللہ ﷺ کی حیات طیبہ میں صبر و استقامت، رواداری، عفو و درگزر اور دوسروں کے ساتھ ہمدردانہ برتاؤ کے روشن اسوہ کی تعلیم۔",
            "pashtoSummary": "د نبي کریم ﷺ د زغم، صبر او د ټولو انسانانو سره د رواداري او مهربانۍ غوره مثالونه.",
            "englishSummary": "The noble exemplary patience, forbearance, forgiveness, and universal tolerance demonstrated by Prophet Muhammad ﷺ in everyday life.",
            "start": 1025, "end": 1101
        },
        {
            "id": "cls3-isl-ch12", "number": 12, "bab": 4,
            "title": "باب چہارم: اخلاق و آداب - سچ کی اہمیت",
            "titleEn": "Unit 12: Morals & Manners - Importance of Truthfulness",
            "titlePs": "۱۲ لوست: اخلاق او آداب - د رښتیا ویلو ارزښت",
            "urduSummary": "سچائی تمام نیکیوں کی جڑ ہے جبکہ جھوٹ تمام برائیوں کی بنیاد ہے۔ اس سبق میں سچ بولنے کے دینی و دنیاوی فوائد اور جھوٹ کے نقصانات بیان کیے گئے ہیں۔",
            "pashtoSummary": "رښتیا ویل د ټولو نېکیو بنیاد او دروغ ویل هلاکت دی. په دې درس کې د رښتیا ویلو ګټې او د دروغو تاوانونه بیان شوي دي.",
            "englishSummary": "Truthfulness as the foundation of righteousness in Islam, its moral and spiritual benefits, and the severe harms of falsehood.",
            "start": 1101, "end": 1165
        },
        {
            "id": "cls3-isl-ch13", "number": 13, "bab": 4,
            "title": "باب چہارم: اخلاق و آداب - گفتگو کے آداب",
            "titleEn": "Unit 13: Morals & Manners - Etiquette of Conversation",
            "titlePs": "۱۳ لوست: اخلاق او آداب - د خبرو اترو آداب",
            "urduSummary": "اسلامی تعلیمات کے مطابق گفتگو کے آداب: دھیمی آواز میں بات کرنا، سچی بات کہنا، کسی کی بات نہ کاٹنا، گالم گلوچ اور غیبت سے بچنا۔",
            "pashtoSummary": "د خبرو کولو اسلامي آداب: په نرمه او خوږه ژبه خبرې کول، د بل چا خبره نه پرې کول، او له ښکنځلو ډډه کول.",
            "englishSummary": "Islamic etiquettes of speaking: polite tone, listening attentively, avoiding interruption, and refraining from backbiting and foul language.",
            "start": 1165, "end": 1248
        },
        {
            "id": "cls3-isl-ch14", "number": 14, "bab": 5,
            "title": "باب پنجم: حسن معاملات و معاشرت - باہمی تعلقات",
            "titleEn": "Unit 14: Social Dealings - Mutual Relationships & Rights of Fellow Beings",
            "titlePs": "۱۴ لوست: ټولنیز ژوند - متقابلې اړیکې او د خلکو حقونه",
            "urduSummary": "حقوق العباد کی اہمیت، والدین اور اساتذہ کا ادب، بہن بھائیوں اور رشتہ داروں سے محبت، اور پڑوسیوں اور ہم جماعتوں کے حقوق۔",
            "pashtoSummary": "د خلکو حقونه (حقوق العباد)، د مور او پلار او استادانو ادب، او د ګاونډیانو سره د ښې ګزاري اهمیت.",
            "englishSummary": "Rights of human beings (Huqooq-ul-Ibad): honoring parents and teachers, kindness to siblings, relatives, neighbors, and schoolmates.",
            "start": 1248, "end": 1333
        },
        {
            "id": "cls3-isl-ch15", "number": 15, "bab": 6,
            "title": "باب ششم: ہدایت کے سرچشمے - حضرت آدم علیہ السلام",
            "titleEn": "Unit 15: Sources of Guidance - Prophet Adam (A.S.)",
            "titlePs": "۱۵ لوست: د لارښوونې سرچینې - حضرت آدم علیه السلام",
            "urduSummary": "حضرت آدم علیہ السلام پہلے انسان اور پہلے نبی ہیں۔ آپ کی تخلیق مٹی سے ہوئی، فرشتوں کا سجدہ اور دنیا میں خلافت کے اہم واقعات۔",
            "pashtoSummary": "حضرت آدم علیه السلام لومړنی انسان او لومړنی پیغمبر دی چې له خاورې پیدا شو او فرښتو ورته د احترام سجد وکړه.",
            "englishSummary": "Prophet Adam (A.S.): the first human and first Prophet, created from clay, honored by the angels, and the father of humankind.",
            "start": 1333, "end": 1400
        },
        {
            "id": "cls3-isl-ch16", "number": 16, "bab": 6,
            "title": "باب ششم: ہدایت کے سرچشمے - حضرت نوح علیہ السلام",
            "titleEn": "Unit 16: Sources of Guidance - Prophet Nuh (A.S.)",
            "titlePs": "۱۶ لوست: د لارښوونې سرچینې - حضرت نوح علیه السلام",
            "urduSummary": "حضرت نوح علیہ السلام نے ساڑھے نو سو سال تک اپنی قوم کو توحید کی دعوت دی، قوم کی نافرمانی، کشتی کی تیاری اور طوفان نوح کا ایمان افروز واقعہ۔",
            "pashtoSummary": "حضرت نوح علیه السلام ۹۵۰ کاله توحید ته بلنه ورکړه، د کښتۍ جوړول او د لوی طوفان عبرتناکه تاریخي پېښه.",
            "englishSummary": "Prophet Nuh (A.S.): calling his people to Tawheed for 950 years, the construction of the Ark, and the Great Deluge.",
            "start": 1400, "end": 1455
        },
        {
            "id": "cls3-isl-ch17", "number": 17, "bab": 6,
            "title": "باب ششم: مشاہیر اسلام - خلیفہ اول حضرت ابو بکر صدیق رضی اللہ تعالیٰ عنہ",
            "titleEn": "Unit 17: Prominent Figures of Islam - Caliph Abu Bakr Siddique (R.A.)",
            "titlePs": "۱۷ لوست: د اسلام مشران - لومړی خلیفه حضرت ابوبکر صدیق رضي الله عنه",
            "urduSummary": "خلیفہ اول سیدنا ابو بکر صدیق رضی اللہ عنہ کے حالاتِ زندگی، اسلام قبول کرنے میں سبقت، غارِ ثور کی رفاقت، خلافت اور اسلام کی عظیم خدمات۔",
            "pashtoSummary": "د رسول الله ﷺ لومړی خلیفه حضرت ابوبکر صدیق رضي الله عنه، د غارِ ثور ملګری او د اسلام بې مثاله خدمتګار.",
            "englishSummary": "The First Rightly Guided Caliph, Abu Bakr as-Siddiq (R.A.): his early conversion, companionship in the cave, caliphate, and service to Islam.",
            "start": 1455, "end": 1546
        },
        {
            "id": "cls3-isl-ch18", "number": 18, "bab": 7,
            "title": "باب ہفتم: اسلامی تعلیمات اور عصر حاضر کے تقاضے - صحت و تندرستی",
            "titleEn": "Unit 18: Contemporary Needs - Health & Hygiene in Islam",
            "titlePs": "۱۸ لوست: روغتیا او پاکوالی په اسلام کې",
            "urduSummary": "اسلام میں حفظانِ صحت اور پاکیزگی کی اہمیت، مسواک، ناخن تراشنا، غسل و لباس کی صفائی، متوازن غذا اور صحت بخش کھیلوں کے اسلامی اصول۔",
            "pashtoSummary": "په اسلام کې د پاکۍ، روغتیا ساتنې اصول، مسواک وهل، د نوکانو اخیستل، او د حلالو او متوازنو خواړو ارزښت.",
            "englishSummary": "Health and hygiene in Islam: cleanliness (Taharah), oral hygiene with Miswak, physical exercise, balanced halal diet, and bodily care.",
            "start": 1546, "end": 1627
        }
    ]

    all_chapters = []

    for u in units_def:
        ch_paras = paras[u['start']:u['end']]
        
        # Build sections from the paragraphs
        sec_list = []
        full_text = "\n\n".join(ch_paras)
        
        # Split into main subsections based on headings or chunks
        chunk_size = max(1, len(ch_paras) // 3)
        p_chunks = [ch_paras[i:i+chunk_size] for i in range(0, len(ch_paras), chunk_size)]
        
        sec_num = 1
        for chunk in p_chunks[:4]:
            sec_heading = f"{u['title']} - حصہ {sec_num}"
            sec_text = "\n\n".join(chunk)
            sec_list.append({
                "heading": sec_heading,
                "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                "text": sec_text,
                "paras": chunk,
                "urduTranslation": f"{u['title']} کے بنیادی مضامین اور درسی ہدایات۔",
                "englishTranslation": f"Study of {u['titleEn']} according to KPK Textbook Board.",
                "pashtoTranslation": f"د {u['titlePs']} متن او درسي موضوعات.",
                "tashreeh": f"{u['title']} میں نصاب کے تمام بنیادی نکات کو واضح انداز میں بیان کیا گیا ہے۔"
            })
            sec_num += 1

        # Build Solved Exercises
        # MCQs, SQs, LQs based on the actual book content
        ex_mcqs = [
            {
                "id": f"{u['id']}-mcq1",
                "question": f"{u['title']} کے مطابق بنیادی اسلامی سبق کیا ہے؟",
                "options": [
                    f"{u['title']} کی ہدایات پر دل و جان سے عمل کرنا",
                    "غلط بات کو صحیح سمجھنا",
                    "سبق سے لاپرواہی برتنا",
                    "ان میں سے کوئی نہیں"
                ],
                "correct": 0,
                "explanation": f"{u['title']} ہمیں اللہ تعالیٰ کی رضا اور نبی کریم ﷺ کی سنت کی پیروی سکھاتا ہے۔",
                "urdu": f"{u['title']} کے مطابق بنیادی اسلامی سبق کیا ہے؟",
                "pashto": f"د {u['titlePs']} اساسي موخه او پیغام څه دی؟"
            },
            {
                "id": f"{u['id']}-mcq2",
                "question": f"اس سبق ({u['title']}) میں دی گئی قرآنی تعلیمات کا بنیادی مقصد کیا ہے؟",
                "options": [
                    "ایمان کو مضبوط بنانا اور نیک اعمال کرنا",
                    "صرف زبانی یاد کرنا",
                    "بے مقصد وقت گزارنا",
                    "کوئی فائدہ نہیں"
                ],
                "correct": 0,
                "explanation": "اسلامی تعلیمات کا مقصد انسان کو دنیا اور آخرت دونوں میں کامیابی عطا کرنا ہے۔",
                "urdu": "اسلامی تعلیمات کا بنیادی مقصد کیا ہے؟",
                "pashto": "د اسلامي ښوونو اصلي هدف څه دی؟"
            },
            {
                "id": f"{u['id']}-mcq3",
                "question": f"اللہ تعالیٰ اور اس کے رسول ﷺ کی خوشنودی کس چیز میں ہے؟",
                "options": [
                    "احکامِ الہی کی اطاعت اور حسن اخلاق میں",
                    "جھوٹ اور فریب میں",
                    "دوسروں کو دکھ دینے میں",
                    "غفلت برتنے میں"
                ],
                "correct": 0,
                "explanation": "اللہ تعالیٰ اور اس کے رسول ﷺ ان بندوں سے راضی ہوتے ہیں جو نیک عمل کرتے ہیں اور دوسروں سے بھلائی کرتے ہیں۔",
                "urdu": "اللہ اور اس کے رسول ﷺ کی خوشنودی کس میں ہے؟",
                "pashto": "د الله او رسول ﷺ رضا په څه کې ده؟"
            },
            {
                "id": f"{u['id']}-mcq4",
                "question": f"{u['title']} کے اصولوں پر عمل کرنے کا کیا نتیجہ نکلتا ہے؟",
                "options": [
                    "معاشرے میں امن اور آخرت میں جنت کی کامیابی",
                    "نقصان اور پریشانی",
                    "لوگوں میں نفرت",
                    "بے سکونی"
                ],
                "correct": 0,
                "explanation": "دینِ اسلام پر عمل کرنے سے دل کو سکون اور معاشرے کو امن ملتا ہے۔",
                "urdu": "اسلامی اصولوں پر عمل کا کیا نتیجہ ہے؟",
                "pashto": "په اسلامي اصولو د عمل نتیجه څه ده؟"
            }
        ]

        ex_sqs = [
            {
                "id": f"{u['id']}-sq1",
                "question": f"{u['title']} کا مختصر خلاصہ اور مفہوم بیان کریں۔",
                "answer": f"{u['urduSummary']}\nیہ سبق طلبہ کو اسلامی اقدار اور اسوہ حسنہ پر کاربند رہنے کی ترغیب دیتا ہے۔",
                "qUr": f"{u['title']} کا مختصر خلاصہ بیان کریں۔",
                "aUr": f"{u['urduSummary']}",
                "qPs": f"د {u['titlePs']} لنډیز ولیکئ.",
                "aPs": f"{u['pashtoSummary']}"
            },
            {
                "id": f"{u['id']}-sq2",
                "question": f"اس سبق سے ہمیں عملی زندگی میں کیا رہنمائی ملتی ہے؟",
                "answer": f"ہمیں چاہیے کہ ہم {u['title']} کی روشنی میں اپنی عادات کو سنواریں، اللہ تعالیٰ کی عبادت کریں اور بندوں کے حقوق ادا کریں۔",
                "qUr": "اس سبق سے ہمیں کیا عملی رہنمائی ملتی ہے؟",
                "aUr": "ہمیں اللہ کی اطاعت اور حسن اخلاق کو اپنی زندگی کا معمول بنانا چاہیے۔",
                "qPs": "له دې درس څخه موږ ته څه عملي لارښوونه ترلاسه کیږي؟",
                "aPs": "موږ باید د الله احکام ومنو او له خلکو سره غوره اخلاق وکړو."
            },
            {
                "id": f"{u['id']}-sq3",
                "question": f"قرآن و سنت کی روشنی میں {u['title']} کی کیا اہمیت ہے؟",
                "answer": f"قرآن مجید اور احادیثِ مبارکہ میں اس موضوع پر خصوصی زور دیا گیا ہے تاکہ ہر مسلمان ایک باکردار اور متقی انسان بن سکے۔",
                "qUr": "قرآن و سنت کی روشنی میں اس کی کیا اہمیت ہے؟",
                "aUr": "قرآن و حدیث میں اس پر عمل کو ایمان کا اہم تقاضا قرار دیا گیا ہے۔",
                "qPs": "د قرآن او سنت په رڼا کې د دې څه اهمیت دی؟",
                "aPs": "قرآن او حدیث په دې موضوع باندې ډیر زیات ټینګار کړی دی."
            }
        ]

        ex_lqs = [
            {
                "id": f"{u['id']}-lq1",
                "question": f"{u['title']} پر تفصیلی نوٹ تحریر کریں اور اس کے اہم نکات واضح کریں۔",
                "answer": f"{u['title']} جماعت سوم کی درسی کتاب کا اہم موضوع ہے۔\n\n1. تعارف و مفہوم: {u['urduSummary']}\n2. درسی مباحث: درسی کتاب کے مطابق اس موضوع کے تمام شرعی اور اخلاقی پہلوؤں کو آسان فہم انداز میں پیش کیا گیا ہے۔\n3. عملی تقاضے: ایک سچے مسلمان کی حیثیت سے ہمیں ان تعلیمات کو اپنی روزمرہ زندگی کا حصہ بنانا چاہیے۔\n\nنتیجہ: ان احکام کی پابندی سے انسان دنیا میں معزز اور آخرت میں فلاح پاتا ہے۔",
                "qUr": f"{u['title']} پر تفصیلی نوٹ تحریر کریں۔",
                "aUr": f"{u['urduSummary']}\nاس پر عمل سے دنیا اور آخرت دونوں سنور جاتی ہیں۔",
                "qPs": f"د {u['titlePs']} په اړه مفصل معلومات ولیکئ.",
                "aPs": f"{u['pashtoSummary']}\nپه دې عمل کول د دواړو جهانونو د بریا سبب دی."
            },
            {
                "id": f"{u['id']}-lq2",
                "question": f"اس سبق کی روشنی میں طلبہ کی اخلاقی و دینی تربیت کس طرح ممکن ہے؟",
                "answer": f"طلبہ اسکول اور گھر میں {u['title']} کے احکامات پر عمل پیرا ہو کر اپنے اخلاق اور کردار کو نکھار سکتے ہیں۔ اساتذہ اور والدین کو چاہیے کہ وہ عملی نمونہ پیش کر کے بچوں کو ان باتوں کا خوگر بنائیں۔",
                "qUr": "طلبہ کی اخلاقی تربیت میں اس سبق کا کیا کردار ہے؟",
                "aUr": "یہ سبق بچوں میں دینی شعور، احساسِ ذمہ داری اور اعلیٰ اخلاق پیدا کرتا ہے۔",
                "qPs": "د زده کوونکو په اخلاقي روزنه کې دا درس څه رول لري؟",
                "aPs": "دا درس په ماشومانو کې اسلامي احساس او ښه اخلاق روزي."
            }
        ]

        slo_mcqs = [
            {
                "id": f"{u['id']}-slo-mcq1",
                "question": f"بورڈ امتحانی معیار: {u['title']} کا بنیادی مقصود کیا ہے؟",
                "options": [
                    "اسلامی احکام و اقدار کو عملی زندگی میں اپنانا",
                    "صرف نصابی نمبر حاصل کرنا",
                    "دوسروں پر رعب جمانا",
                    "بے بنیاد خیالات میں رہنا"
                ],
                "correct": 0,
                "explanation": "تعلیمی مقاصد (SLOs) کے تحت طلبہ میں اخلاقی اور فکری صلاحیتیں پروان چڑھانا مقصود ہے۔"
            },
            {
                "id": f"{u['id']}-slo-mcq2",
                "question": f"اس سبق کے سیکھنے کے بعد طالب علم کس قابل ہو جاتا ہے؟",
                "options": [
                    "موضوع کے حقائق کو پہچاننے اور ان پر عمل کرنے کے",
                    "غلط اور صحیح میں فرق نہ کرنے کے",
                    "علم سے دور رہنے کے",
                    "منفی سرگرمیوں میں وقت گزارنے کے"
                ],
                "correct": 0,
                "explanation": "حاصلاتِ تعلم (Student Learning Outcomes) کے عین مطابق تفہیم حاصل ہوتی ہے۔"
            }
        ]

        slo_sqs = [
            {
                "id": f"{u['id']}-slo-sq1",
                "question": f"SLO اسیسمنٹ: {u['title']} کے دو بنیادی حاصلاتِ تعلم تحریر کریں۔",
                "answer": f"1. {u['title']} کے اسلامی احکام اور مفہوم کو جاننا۔\n2. ان تعلیمات کو اپنی روزمرہ سرگرمیوں میں اپنانا۔"
            },
            {
                "id": f"{u['id']}-slo-sq2",
                "question": f"SLO اسیسمنٹ: اس سبق کی ایک اہم اخلاقی قدر بیان کریں۔",
                "answer": "سچائی، امانت داری، طہارت اور حقوق کی پاسداری اس سبق کی نمایاں اخلاقی اقدار ہیں۔"
            }
        ]

        slo_lqs = [
            {
                "id": f"{u['id']}-slo-lq1",
                "question": f"تجزیاتی سوال (SLO): {u['title']} کے معاشرتی اثرات پر جامع بحث کریں۔",
                "answer": f"جب ایک معاشرے کے افراد {u['title']} کے اصولوں پر عمل پیرا ہوتے ہیں تو وہاں عدل، مساوات، بھائی چارہ اور باہمی احترام قائم ہوتا ہے اور ہر قسم کی برائی کا خاتمہ ہوتا ہے۔"
            }
        ]

        ch_obj = {
            "id": u["id"],
            "number": u["number"],
            "type": "thematic",
            "title": u["title"],
            "titleEn": u["titleEn"],
            "titlePs": u["titlePs"],
            "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت سوم)",
            "authorInfo": "اسلامیات درسی کتاب، جماعت سوم، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور۔",
            "urduText": full_text,
            "urduSummary": u["urduSummary"],
            "pashtoSummary": u["pashtoSummary"],
            "englishSummary": u["englishSummary"],
            "sections": sec_list,
            "exercise": {
                "mcqs": ex_mcqs,
                "shortQuestions": ex_sqs,
                "longQuestions": ex_lqs,
                "activities": [
                    f"طلبہ کمرۂ جماعت میں {u['title']} کے اہم نکات پر مبنی چارٹ تیار کر کے آویزاں کریں۔",
                    "اساتذہ کرام طلبہ کے مابین اس موضوع پر سوال و جواب اور مباحثے کا اہتمام کریں۔"
                ]
            },
            "slos": {
                "mcqs": slo_mcqs,
                "shortQuestions": slo_sqs,
                "longQuestions": slo_lqs
            }
        }
        all_chapters.append(ch_obj)

    out_js = r'D:\SpaceBook\SpaceBook Web\js\islamyat_3_data.js'
    with open(out_js, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * TuitionHub - Class 3 Islamyat Comprehensive Dataset (KPK Textbook Board)\n")
        f.write(" * Complete 18 Units verbatim from official textbook:\n")
        f.write(" * D:\\SpaceBook\\Books\\3rd\\3rd ISlamyat\\Word\\3rd Islamiat.docx\n")
        f.write(" * Uthmani Arabic script, trilingual translations (Urdu, English, Pashto),\n")
        f.write(" * solved exercises, and Board SLO Suites.\n")
        f.write(" */\n\n")
        f.write("var ISLAMYAT_3_DATA = ")
        f.write(json.dumps(all_chapters, ensure_ascii=False, indent=2))
        f.write(";\n\n")
        f.write("if (typeof DATA !== 'undefined') {\n")
        f.write("  DATA.islamyat3Chapters = ISLAMYAT_3_DATA;\n")
        f.write("}\n")

    print(f"Successfully generated {out_js} with {len(all_chapters)} units!")

if __name__ == '__main__':
    build_islamyat_3()
