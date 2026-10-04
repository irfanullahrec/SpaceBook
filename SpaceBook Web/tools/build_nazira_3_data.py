#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder for Class 3 Nazira Quran Dataset (NAZIRA_3_DATA)
Source: D:\SpaceBook\Books\3rd\3rd Nazira\Word\3rd Nazira.docx
Produces SpaceBook Web/js/nazira_3_data.js
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

def build_nazira_3():
    docx_path = r'D:\SpaceBook\Books\3rd\3rd Nazira\Word\3rd Nazira.docx'
    paras = extract_docx_paras(docx_path)
    print(f"Loaded {len(paras)} paras from {docx_path}")

    bounds = [
        {
            "id": "cls3-naz-ch01", "number": 1,
            "title": "سبق ۱: صوتی طریقہ تدریس و قواعدِ تجوید (اعادہ تجوید)",
            "titleEn": "Lesson 1: Phonics Method & Tajweed Rules Revision",
            "titlePs": "۱ لوست: صوتي تدریس او د تجوید قواعد (تکرار)",
            "urduSummary": "اس سبق میں عربی حروفِ تہجی کے درست مخارج، حروفِ مستعلیہ، سفیرہ، حرکات، تنوین، سکون، قلقلہ، حروفِ مدہ و لین، غنہ، ادغام، اخفاء اور رموزِ اوقاف کا تفصیلی اعادہ کرایا گیا ہے۔",
            "pashtoSummary": "په دې درس کې د عربي ۲۹ تورو مخارج، مستعلیه توري، حرکات، تنوین، قلقله، مد، غنه، ادغام، اخفاء او د وقف نښې په تکراري توګه تدریس شوې دي.",
            "englishSummary": "Comprehensive Tajweed phonics revision covering articulation points (Makharij), heavy letters, vowels, Sukoon, Qalqalah, Madd, Ghunnah, and stop signs (Waqf).",
            "start": 174, "end": 642
        },
        {
            "id": "cls3-naz-ch02", "number": 2,
            "title": "سبق ۲: سورة البقرة وسورة آل عمران (سورة البقرة آيت 253 تا سورۃ آل عمران آیت 15) - پارہ 3",
            "titleEn": "Lesson 2: Surah Al-Baqarah & Surah Ali 'Imran (Al-Baqarah 253 to Ali 'Imran 15) - Para 3",
            "titlePs": "۲ لوست: سورة البقرة او سورة آل عمران (پاره ۳)",
            "urduSummary": "پارہ ۳ (تِلْكَ الرُّسُلُ) کا آغاز: آیت الکرسی، انفاق فی سبیل اللہ، حضرت ابراہیمؑ و نمرود کا مکالمہ اور سورۃ آل عمران کی ابتدائی ۱۵ آیات کی تجوید کے ساتھ تلاوت۔",
            "pashtoSummary": "د دریمې پارې تلاوت: آیت الکرسي، د انفاق احکام، د حضرت ابراهیم علیه السلام او نمرود مکالمه او د سورة آل عمران پیل.",
            "englishSummary": "Recitation of Para 3 (Tilkar-Rusul) including Ayat al-Kursi, charity in Allah's cause, and the opening 15 verses of Surah Ali 'Imran.",
            "start": 642, "end": 808
        },
        {
            "id": "cls3-naz-ch03", "number": 3,
            "title": "سبق ۳: سورة آل عمران (آیت 16 تا 77) - پارہ 3",
            "titleEn": "Lesson 3: Surah Ali 'Imran (Verses 16 to 77) - Para 3",
            "titlePs": "۳ لوست: سورة آل عمران (آیت ۱۶ تر ۷۷)",
            "urduSummary": "سورۃ آل عمران کی آیات ۱۶ تا ۷۷ کی تلاوت: توحید و عدل کی شہادت، حضرت مریمؑ کی ولادت، حضرت زکریاؑ کی دعا اور حضرت عیسیٰؑ کی بشارت۔",
            "pashtoSummary": "د سورة آل عمران تلاوت: د حضرت مریم علیها السلام ولادت، د حضرت زکریا علیه السلام دعا او د حضرت عیسی علیه السلام زیری.",
            "englishSummary": "Recitation of Surah Ali 'Imran verses 16-77: testimony of Tawheed, miraculous birth of Maryam, prayer of Zakariyya, and glad tidings of Isa (A.S.).",
            "start": 808, "end": 914
        },
        {
            "id": "cls3-naz-ch04", "number": 4,
            "title": "سبق ۴: سورة آل عمران (آیت 78 تا 132) - پارہ 3 و 4",
            "titleEn": "Lesson 4: Surah Ali 'Imran (Verses 78 to 132) - Para 3 & 4",
            "titlePs": "۴ لوست: سورة آل عمران (آیت ۷۸ تر ۱۳۲)",
            "urduSummary": "پارہ ۳ کا اختتام اور پارہ ۴ (لَنْ تَنَالُوا) کا آغاز: عہدِ الٰہی کی پاسداری، حبل اللہ کو مضبوطی سے تھامنا، امر بالمعروف و نہی عن المنکر اور تقویٰ کی تعلیمات۔",
            "pashtoSummary": "د دریمې پارې پای او د څلورمې پارې پیل: د الله له رسۍ منګولې لګول، د نېکۍ امر او له بدۍ منع.",
            "englishSummary": "Recitation spanning Paras 3 & 4: holding firmly to the rope of Allah, enjoining good and forbidding evil, and spiritual steadfastness.",
            "start": 914, "end": 1045
        },
        {
            "id": "cls3-naz-ch05", "number": 5,
            "title": "سبق ۵: سورة آل عمران (آیت 133 تا 186) - پارہ 4",
            "titleEn": "Lesson 5: Surah Ali 'Imran (Verses 133 to 186) - Para 4",
            "titlePs": "۵ لوست: سورة آل عمران (آیت ۱۳۳ تر ۱۸۶)",
            "urduSummary": "سورۃ آل عمران کی آیات ۱۳۳ تا ۱۸۶: مغفرت اور جنت کی طرف جلدی کرنا، غصہ پی جانا، غزوہ احد کے دروس اور مومنین کے لیے استقامت کی بشارت۔",
            "pashtoSummary": "د بخښنې او جنت لور ته بېړه کول، غوسه زغمل، او د احد د غزا درسونه او د مؤمنانو استقامت.",
            "englishSummary": "Recitation of Surah Ali 'Imran verses 133-186: hastening towards forgiveness, controlling anger, lessons of the Battle of Uhud, and patience.",
            "start": 1045, "end": 1148
        },
        {
            "id": "cls3-naz-ch06", "number": 6,
            "title": "سبق ۶: سورة آل عمران وسورة النساء (سورة آل عمران آیت 187 تا سورة النساء آیت 23) - پارہ 4",
            "titleEn": "Lesson 6: Surah Ali 'Imran & Surah An-Nisa (Ali 'Imran 187 to An-Nisa 23) - Para 4",
            "titlePs": "۶ لوست: سورة آل عمران او سورة النساء (پاره ۴)",
            "urduSummary": "سورۃ آل عمران کا اختتام اور سورۃ النساء کا آغاز: کائنات کی تخلیق میں غور و فکر کرنے والوں کی دعائیں، یتیموں کے حقوق، وراثت کے احکام اور محرماتِ نکاح۔",
            "pashtoSummary": "د سورة آل عمران پای او د سورة النساء پیل: د یتیمانو حقوق، د میراث تقسیم او محرمې ښځې.",
            "englishSummary": "Conclusion of Surah Ali 'Imran and start of Surah An-Nisa: contemplation on the creation, orphans' rights, inheritance laws, and prohibited relationships.",
            "start": 1148, "end": 1272
        },
        {
            "id": "cls3-naz-ch07", "number": 7,
            "title": "سبق ۷: سورة النساء (آیت 24 تا 75) - پارہ 5",
            "titleEn": "Lesson 7: Surah An-Nisa (Verses 24 to 75) - Para 5",
            "titlePs": "۷ لوست: سورة النساء (آیت ۲۴ تر ۷۵) - پاره ۵",
            "urduSummary": "پارہ ۵ (وَالْمُحْصَنَاتُ) کا آغاز: حلال و حرام معاملات، باہمی رضا مندی سے تجارت، اللہ اور اس کے رسول ﷺ کی اطاعت اور امانتوں کو ان کے اہل تک پہنچانا۔",
            "pashtoSummary": "د پنځمې پارې تلاوت: د حلالې سوداګرۍ اصول، د الله او رسول اطاعت او امانتونه خپل اهل ته سپارل.",
            "englishSummary": "Recitation of Para 5 (Wal-Muhsanat): lawful commerce, obedience to Allah and His Messenger, justice, and rendering trusts to their rightful owners.",
            "start": 1272, "end": 1380
        },
        {
            "id": "cls3-naz-ch08", "number": 8,
            "title": "سبق ۸: سورة النساء (آیت 76 تا 113) - پارہ 5",
            "titleEn": "Lesson 8: Surah An-Nisa (Verses 76 to 113) - Para 5",
            "titlePs": "۸ لوست: سورة النساء (آیت ۷۶ تر ۱۱۳)",
            "urduSummary": "سورۃ النساء کی آیات ۷۶ تا ۱۱۳: راہِ خدا میں جدوجہد، صلح و امان کی اہمیت، نمازِ خوف کا طریقہ، اور قرآن مجید میں غور و فکر کرنے کی تاکید۔",
            "pashtoSummary": "د سورة النساء تلاوت: د سولې او امن ارزښت، د ویرې د لمانځه (صلاة الخوف) طریقه او په قرآن کې غور کول.",
            "englishSummary": "Recitation of Surah An-Nisa verses 76-113: peaceful settlement, prayer during danger (Salat-ul-Khawf), and pondering upon the Holy Quran.",
            "start": 1380, "end": 1490
        },
        {
            "id": "cls3-naz-ch09", "number": 9,
            "title": "سبق ۹: سورة النساء (آیت 114 تا 170) - پارہ 5 و 6",
            "titleEn": "Lesson 9: Surah An-Nisa (Verses 114 to 170) - Para 5 & 6",
            "titlePs": "۹ لوست: سورة النساء (آیت ۱۱۴ تر ۱۷۰)",
            "urduSummary": "پارہ ۵ کا اختتام اور پارہ ۶ (لَا يُحِبُّ اللَّهُ) کا آغاز: عدل و انصاف کی گواہی، شرک کی مذمت، منافقین کی علامات اور رسولوں پر ایمان لانے کے احکام۔",
            "pashtoSummary": "د پنځمې پارې پای او د شپږمې پارې پیل: د عدالت ګواهي، د شرک غندنه او په ټولو پیغمبرانو ایمان راوړل.",
            "englishSummary": "Recitation spanning Paras 5 & 6: standing firmly for justice, condemnation of Shirk, hypocrites, and universal belief in all divine Messengers.",
            "start": 1490, "end": 1611
        },
        {
            "id": "cls3-naz-ch10", "number": 10,
            "title": "سبق ۱۰: سورة النساء وسورة المائدة (سورة النساء آيت 171 تا سورة المائدة آيت 36) - پارہ 6",
            "titleEn": "Lesson 10: Surah An-Nisa & Surah Al-Ma'idah (An-Nisa 171 to Al-Ma'idah 36) - Para 6",
            "titlePs": "۱۰ لوست: سورة النساء او سورة المائدة (پاره ۶)",
            "urduSummary": "سورۃ النساء کا اختتام اور سورۃ المائدہ کا آغاز: عہد و پیمان کی پاسداری، حلال و حرام جانور، طہارت (تیمم و وضو) اور ہابیل و قابیل کا تاریخی واقعہ۔",
            "pashtoSummary": "د سورة النساء پای او د سورة المائدة پیل: د تړونونو وفاء کول، د حلالو او حرامو ښکار احکام او د هابیل او قابیل کیسه.",
            "englishSummary": "Conclusion of Surah An-Nisa and beginning of Surah Al-Ma'idah: fulfilling covenants, dietary laws, purification (Wudu & Tayammum), and Abel and Cain.",
            "start": 1611, "end": 1714
        },
        {
            "id": "cls3-naz-ch11", "number": 11,
            "title": "سبق ۱۱: سورة المائدة (آيت 37 تا 75) - پارہ 6",
            "titleEn": "Lesson 11: Surah Al-Ma'idah (Verses 37 to 75) - Para 6",
            "titlePs": "۱۱ لوست: سورة المائدة (آیت ۳۷ تر ۷۵)",
            "urduSummary": "سورۃ المائدہ کی آیات ۳۷ تا ۷۵: تورات اور انجیل کی ہدایت، عدل کے ساتھ فیصلہ کرنا، مومنین کی باہمی دوستی اور اللہ کی نازل کردہ شریعت پر عمل۔",
            "pashtoSummary": "د سورة المائدة تلاوت: د تورات او انجیل رڼا، په عدل قضاوت کول او د مؤمنانو باهمي ملګرتیا.",
            "englishSummary": "Recitation of Surah Al-Ma'idah verses 37-75: divine guidance in earlier scriptures, judging with justice, and true brotherhood of believers.",
            "start": 1714, "end": 1842
        },
        {
            "id": "cls3-naz-ch12", "number": 12,
            "title": "سبق ۱۲: سورة المائدة وسورة الانعام (سورة المائدة آيت 76 تا سورۃ الانعام آیت 08) - پارہ 7",
            "titleEn": "Lesson 12: Surah Al-Ma'idah & Surah Al-An'am (Al-Ma'idah 76 to Al-An'am 8) - Para 7",
            "titlePs": "۱۲ لوست: سورة المائدة او سورة الانعام (پاره ۷)",
            "urduSummary": "پارہ ۷ (وَإِذَا سَمِعُوا) کا آغاز: حق سن کر آنکھوں سے آنسو جاری ہونا، قسموں کا کفارہ، خمر و میسر (شراب و جوئے) کی ممانعت اور سورۃ الانعام کا آغاز۔",
            "pashtoSummary": "د اوومې پارې پیل: د حق په اوریدو اوښکې بهول، د قسمونو کفاره، د شرابو او قمار ممانعت او د سورة الانعام پیل.",
            "englishSummary": "Recitation of Para 7 (Wa Iza Sami'u): tears upon hearing truth, expiation of oaths, prohibition of intoxicants and gambling, and opening of Surah Al-An'am.",
            "start": 1842, "end": 1948
        },
        {
            "id": "cls3-naz-ch13", "number": 13,
            "title": "سبق ۱۳: سورة الانعام (سورۃ الانعام آیت 9 تا آیت 73) - پارہ 7",
            "titleEn": "Lesson 13: Surah Al-An'am (Verses 9 to 73) - Para 7",
            "titlePs": "۱۳ لوست: سورة الانعام (آیت ۹ تر ۷۳)",
            "urduSummary": "سورۃ الانعام کی آیات ۹ تا ۷۳: زمین و آسمان میں اللہ تعالیٰ کی وحدانیت کی نشانیاں، غیب کی کنجیاں، دن اور رات کا نظام اور حضرت ابراہیمؑ کا مشرکین سے مناظرہ۔",
            "pashtoSummary": "د سورة الانعام تلاوت: د الله د توحید نښې، د غیبو کیلي ګانې او د حضرت ابراهیم علیه السلام او د هغه د قوم مناظره.",
            "englishSummary": "Recitation of Surah Al-An'am verses 9-73: signs of divine Oneness in nature, keys of the Unseen, day and night cycle, and Abraham's debate with idolaters.",
            "start": 1948, "end": 2046
        },
        {
            "id": "cls3-naz-ch14", "number": 14,
            "title": "سبق ۱۴: سورة الانعام (آیت 74 تا آیت 110) - پارہ 7 و 8",
            "titleEn": "Lesson 14: Surah Al-An'am (Verses 74 to 110) - Para 7 & 8",
            "titlePs": "۱۴ لوست: سورة الانعام (آیت ۷۴ تر ۱۱۰)",
            "urduSummary": "پارہ ۷ کا اختتام اور پارہ ۸ (وَلَوْ أَنَّنَا) کا آغاز: انبیاء کرامؑ کی فضیلت اور فہرست، بیج اور گٹھلی کو پھاڑنے والا اللہ، ستاروں اور بارش کے مناظر۔",
            "pashtoSummary": "د اوومې پارې پای او د اتمې پارې پیل: د ۱۸ پیغمبرانو مبارک نومونه، د دانې او زړي راشنه کوونکی الله.",
            "englishSummary": "Recitation spanning Paras 7 & 8: genealogy and honor of 18 noble Prophets, Allah as the cleaver of grain and date-seeds, and constellations.",
            "start": 2046, "end": 2115
        },
        {
            "id": "cls3-naz-ch15", "number": 15,
            "title": "سبق ۱۵: سورة الانعام وسورة الاعراف (سورۃ الانعام آیت 111 تا سورۃ الاعراف آیت 11) - پارہ 8",
            "titleEn": "Lesson 15: Surah Al-An'am & Surah Al-A'raf (Al-An'am 111 to Al-A'raf 11) - Para 8",
            "titlePs": "۱۵ لوست: سورة الانعام او سورة الاعراف (پاره ۸)",
            "urduSummary": "سورۃ الانعام کا اختتام اور سورۃ الاعراف کا آغاز: حلال و حرام ذبیحہ کے احکام، والدین کے ساتھ حسن سلوک، ناپ تول میں برابری، اور انسان کی تخلیق۔",
            "pashtoSummary": "د سورة الانعام پای او د سورة الاعراف پیل: د ذبحې احکام، د مور او پلار سره احسان او د حضرت آدم او ابلیس کیسه.",
            "englishSummary": "Conclusion of Surah Al-An'am and start of Surah Al-A'raf: dietary slaughter rules, parental respect, just weighing, and creation of Adam.",
            "start": 2115, "end": 2246
        },
        {
            "id": "cls3-naz-ch16", "number": 16,
            "title": "سبق ۱۶: سورۃ الاعراف (سورۃ الاعراف آیت 12 تا 87) - پارہ 8",
            "titleEn": "Lesson 16: Surah Al-A'raf (Verses 12 to 87) - Para 8",
            "titlePs": "۱۶ لوست: سورة الاعراف (آیت ۱۲ تر ۸۷) - پاره ۸",
            "urduSummary": "پارہ ۸ کا اختتام: ابلیس کی نافرمانی، لباس و زینت کے آداب، اہل جنت اور اہل جہنم کا مکالمہ، اور انبیاء کرام (نوحؑ، ہودؑ، صالحؑ، لوطؑ، شعیبؑ) کے سبق آموز واقعات۔",
            "pashtoSummary": "د اتمې پارې پای: د شیطان کبر، د جوماتونو لپاره پاک کالي، او د پخوانیو قومونو (عاد، ثمود، مدین) تاریخي پېښې.",
            "englishSummary": "Recitation concluding Para 8: defiance of Iblis, etiquettes of dress for prayer, dialog between people of Paradise and Hell, and historical stories of Nuh, Hud, Salih, Lut, and Shu'aib.",
            "start": 2246, "end": len(paras)
        }
    ]

    all_chapters = []

    for b in bounds:
        ch_paras = paras[b['start']:b['end']]
        full_text = "\n\n".join(ch_paras)
        
        # Build sections from the paragraphs
        chunk_size = max(1, len(ch_paras) // 3)
        p_chunks = [ch_paras[i:i+chunk_size] for i in range(0, len(ch_paras), chunk_size)]
        
        sec_list = []
        sec_num = 1
        for chunk in p_chunks[:4]:
            sec_heading = f"{b['title']} - حصہ {sec_num}"
            sec_text = "\n\n".join(chunk)
            sec_list.append({
                "heading": sec_heading,
                "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                "text": sec_text,
                "paras": chunk,
                "urduTranslation": f"{b['title']} کے بنیادی تجویدی قواعد اور آیاتِ قرآنیہ۔",
                "englishTranslation": f"Recitation and Tajweed phonics for {b['titleEn']}.",
                "pashtoTranslation": f"د {b['titlePs']} متن، تجوید او تلاوت.",
                "tashreeh": f"{b['title']} میں مخارج، غنہ، مد، اخفاء اور رموزِ اوقاف کے قواعد کی عملی مشق کروائی گئی ہے۔"
            })
            sec_num += 1

        ex_mcqs = [
            {
                "id": f"{b['id']}-mcq1",
                "question": f"{b['title']} کی تلاوت کے دوران کن قواعد کی پابندی ضروری ہے؟",
                "options": [
                    "تجوید کے قواعد، درست مخارج اور رموزِ اوقاف کی",
                    "بغیر سوچے سمجھے جلدی پڑھنے کی",
                    "اعراب چھوڑ دینے کی",
                    "ان میں سے کوئی نہیں"
                ],
                "correct": 0,
                "explanation": "قرآن مجید کی تلاوت ترتیل اور تجوید کے ساتھ کرنا اللہ تعالیٰ کا واضح حکم ہے۔",
                "urdu": "تلاوت کے دوران کن قواعد کا خیال رکھنا ضروری ہے؟",
                "pashto": "د قرآن د تلاوت په وخت کې د کومو قواعدو مراعت کول پکار دي؟"
            },
            {
                "id": f"{b['id']}-mcq2",
                "question": f"اس سبق میں دی گئی آیات کس پارے سے تعلق رکھتی ہیں؟",
                "options": [
                    "پارہ 3 تا پارہ 8 کے منتخب حصے سے",
                    "صرف پارہ 30 سے",
                    "صرف پارہ 1 سے",
                    "کسی بھی پارے سے نہیں"
                ],
                "correct": 0,
                "explanation": "جماعت سوم کے نصاب میں پارہ ۳ تا پارہ ۸ کی مکمل روانی اور تجوید کے ساتھ تلاوت شامل ہے۔",
                "urdu": "اس سبق کی آیات کا تعلق کن پاروں سے ہے؟",
                "pashto": "دا درس د کومو پارو اړوند دی؟"
            },
            {
                "id": f"{b['id']}-mcq3",
                "question": "قرآنی تلاوت میں 'وقف' کے کیا معنی ہیں؟",
                "options": [
                    "کلمہ کے آخر پر سانس اور آواز کو توڑ کر رکنا",
                    "مسلسل تیزی سے پڑھنا",
                    "حروف کو ملا دینا",
                    "آواز بند کر لینا"
                ],
                "correct": 0,
                "explanation": "وقف کے لغوی معنی ٹھہرنے کے ہیں، اور تجوید میں کلمے کے آخر پر سانس توڑ کر ٹھہرنا وقف کہلاتا ہے۔",
                "urdu": "تجوید میں وقف کے کیا معنی ہیں؟",
                "pashto": "په تجوید کې د وقف څه معنی ده؟"
            },
            {
                "id": f"{b['id']}-mcq4",
                "question": "جب نون مشدد یا میم مشدد آئے تو کیا کیا جاتا ہے؟",
                "options": [
                    "ایک الف کے برابر غنہ کیا جاتا ہے",
                    "جلدی سے پڑھا جاتا ہے",
                    "حرف کو چھوڑ دیا جاتا ہے",
                    "کوئی تبدیلی نہیں ہوتی"
                ],
                "correct": 0,
                "explanation": "نون اور میم پر جب تشدید (ّ) ہو تو غنہ کرنا واجب ہوتا ہے۔",
                "urdu": "نون مشدد اور میم مشدد پر کیا حکم ہے؟",
                "pashto": "په نون او میم مشدد باندې څه حکم دی؟"
            }
        ]

        ex_sqs = [
            {
                "id": f"{b['id']}-sq1",
                "question": f"{b['title']} کا تلاوتی و تجویدی خلاصہ بیان کریں۔",
                "answer": f"{b['urduSummary']}\nطلبہ کو اس سبق میں آیات کی روانی اور تجوید کی عملی مشق کروائی جاتی ہے۔",
                "qUr": f"{b['title']} کا تجویدی خلاصہ کیا ہے؟",
                "aUr": f"{b['urduSummary']}",
                "qPs": f"د {b['titlePs']} تجویدي لنډیز ولیکئ.",
                "aPs": f"{b['pashtoSummary']}"
            },
            {
                "id": f"{b['id']}-sq2",
                "question": "دورانِ تلاوت کن امور کا خیال رکھنا ضروری ہے؟",
                "answer": "باوضو ہونا، قبلہ رو بیٹھنا، تعوذ و تسمیہ پڑھنا، مخارج کی درستی اور رموزِ اوقاف کی پاسداری ضروری ہے۔",
                "qUr": "دورانِ تلاوت کن باتوں کا خیال رکھنا ضروری ہے؟",
                "aUr": "باوضو ہونا، ٹھہر ٹھہر کر پڑھنا اور تجوید کے اصولوں پر عمل کرنا۔",
                "qPs": "د تلاوت په وخت کوم شیان مهم دي؟",
                "aPs": "بااوداسه کیدل، په ادب کښیناستل او د تجوید سم مراعت کول."
            },
            {
                "id": f"{b['id']}-sq3",
                "question": "اس سبق سے متعلق تجوید کا ایک اہم قاعدہ تحریر کریں۔",
                "answer": "حروفِ مستعلیہ کو ہمیشہ پر (موٹا) پڑھا جاتا ہے اور حروفِ مدہ کو اپنی طبعی مقدار کے مطابق کھینچا جاتا ہے۔",
                "qUr": "تجوید کا ایک بنیادی اصول بیان کریں۔",
                "aUr": "حروف کو ان کے مخصوص مخارج سے صفات کے ساتھ ادا کرنا۔",
                "qPs": "د تجوید یو مهم قانون ولیکئ.",
                "aPs": "هر توری باید له خپل سم مخرج او صفت څخه وویل شي."
            }
        ]

        ex_lqs = [
            {
                "id": f"{b['id']}-lq1",
                "question": f"{b['title']} کے مطابق قرآنی آیات کی تجوید اور تلاوت کے آداب پر مفصل نوٹ لکھیں۔",
                "answer": f"{b['title']} جماعت سوم کے ناظرہ قرآن نصاب کا حصہ ہے۔\n\n1. تعارف: {b['urduSummary']}\n2. صوتی اصول: قرآنی حروف کی ادائیگی میں لب، زبان، دانت اور حلق کے مخارج کا کامل خیال رکھا جاتا ہے۔\n3. وقف کے قواعد: علاماتِ وقف جیسے م (وقف لازم)، ط (وقف مطلق)، ج (وقف جائز) اور لا (وقف ممنوع) پر درست طریقہ سے ٹھہرا جاتا ہے۔\n\nنتیجہ: تجوید کے ساتھ تلاوت سے قرآنی معانی محفوظ رہتے ہیں اور انسان اجر و ثواب کا مستحق بنتا ہے۔",
                "qUr": f"{b['title']} پر تجویدی نوٹ تحریر کریں۔",
                "aUr": f"{b['urduSummary']}\nتجوید کی رعایت سے تلاوت میں حسن اور درستگی پیدا ہوتی ہے۔",
                "qPs": f"د {b['titlePs']} په اړه مفصل تجویدي معلومات ولیکئ.",
                "aPs": f"{b['pashtoSummary']}\nپه تجوید قرآن لوستل د ثواب او برکت سبب ګرځي."
            },
            {
                "id": f"{b['id']}-lq2",
                "question": "ناظرہ قرآن مجید پڑھنے کی فضیلت اور برکات پر جامع روشنی ڈالیں۔",
                "answer": "رسول اللہ ﷺ نے ارشاد فرمایا: 'خَيْرُكُمْ مَّنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ' (تم میں سے بہترین شخص وہ ہے جو قرآن سیکھے اور سکھائے)۔ قرآن مجید کے ایک ایک حرف پر دس دس نیکیاں ملتی ہیں۔ روزانہ تلاوت سے دل کو سکون، گھر میں برکت اور آخرت میں شفاعت نصیب ہوتی ہے۔",
                "qUr": "قرآن مجید پڑھنے کی فضیلت کیا ہے؟",
                "aUr": "قرآن سیکھنے اور سکھانے والا بہترین انسان ہے اور ہر حرف پر دس نیکیاں ملتی ہیں۔",
                "qPs": "د قرآن مجید د تلاوت فضیلت څه دی؟",
                "aPs": "قرآن لوستونکی غوره انسان دی او په هر تورې لس نېکۍ ورکول کیږي."
            }
        ]

        slo_mcqs = [
            {
                "id": f"{b['id']}-slo-mcq1",
                "question": f"SLO اسیسمنٹ: {b['title']} کا بنیادی تعلیمی مقصد کیا ہے؟",
                "options": [
                    "طلبہ کی عربی صوتیات، تجوید اور روانی کے ساتھ تلاوت کی صلاحیت پیدا کرنا",
                    "صرف سرسری نظر ڈالنا",
                    "بغیر مخارج کے پڑھنا",
                    "کوئی خاص مقصد نہیں"
                ],
                "correct": 0,
                "explanation": "کے پی کے ٹیکسٹ بک بورڈ کے حاصلاتِ تعلم کے مطابق درست تجوید اور روانی مقصود ہے۔"
            },
            {
                "id": f"{b['id']}-slo-mcq2",
                "question": "رموزِ اوقاف کا لحاظ رکھنے سے تلاوت میں کیا فائدہ حاصل ہوتا ہے؟",
                "options": [
                    "معنی اور مفہوم میں بگاڑ پیدا نہیں ہوتا اور فصاحت قائم رہتی ہے",
                    "وقت ضائع ہوتا ہے",
                    "تلاوت مشکل ہو جاتی ہے",
                    "کوئی اثر نہیں پڑتا"
                ],
                "correct": 0,
                "explanation": "رموزِ اوقاف پر درست وقف کرنے سے کلامِ الٰہی کے معنی بالکل واضح اور محفوظ رہتے ہیں۔"
            }
        ]

        slo_sqs = [
            {
                "id": f"{b['id']}-slo-sq1",
                "question": f"SLO اسیسمنٹ: {b['title']} کے تحت دو بنیادی حاصلاتِ تعلم تحریر کریں۔",
                "answer": "1. آیاتِ قرآنیہ کی تجوید کے قواعد کے ساتھ درست ادائی۔\n2. رموزِ اوقاف اور علاماتِ وقف کا خیال رکھتے ہوئے تلاوت میں روانی حاصل کرنا۔"
            },
            {
                "id": f"{b['id']}-slo-sq2",
                "question": "SLO اسیسمنٹ: غنہ اور اخفاء میں کیا فرق ہے؟",
                "answer": "غنہ ناک کے بانسے سے آواز نکالنے کو کہتے ہیں، جبکہ اخفاء نون ساکن یا تنوین کی آواز کو ناک میں چھپا کر پڑھنے کو کہتے ہیں۔"
            }
        ]

        slo_lqs = [
            {
                "id": f"{b['id']}-slo-lq1",
                "question": f"تجزیاتی سوال (SLO): {b['title']} کے ذریعے طلبہ کی تلاوت میں بہتری کے عملی اقدامات تجویز کریں۔",
                "answer": "طلبہ کو روزانہ استاد کی نگرانی میں مشق کروائی جائے، غلط تلفظ کی فوری تصحیح کی جائے، آڈیو تلاوت سنوائی جائے اور تجوید کے قواعد کے چارٹس کی مدد سے عملی تربیت دی جائے۔"
            }
        ]

        ch_obj = {
            "id": b["id"],
            "number": b["number"],
            "type": "tajweed",
            "title": b["title"],
            "titleEn": b["titleEn"],
            "titlePs": b["titlePs"],
            "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — ناظرہ قرآن (جماعت سوم)",
            "authorInfo": "ناظرہ قرآن آسان تجوید کے ساتھ، جماعت سوم، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور۔",
            "urduText": full_text,
            "urduSummary": b["urduSummary"],
            "pashtoSummary": b["pashtoSummary"],
            "englishSummary": b["englishSummary"],
            "sections": sec_list,
            "exercise": {
                "mcqs": ex_mcqs,
                "shortQuestions": ex_sqs,
                "longQuestions": ex_lqs,
                "activities": [
                    f"طلبہ کمرۂ جماعت میں {b['title']} کی آیات کو ایک دوسرے کے سامنے تجوید کے ساتھ تلاوت کریں۔",
                    "استاد محترم طلبہ کو وقف اور غنہ کی عملی نشان دہی کروائیں۔"
                ]
            },
            "slos": {
                "mcqs": slo_mcqs,
                "shortQuestions": slo_sqs,
                "longQuestions": slo_lqs
            }
        }
        all_chapters.append(ch_obj)

    out_js = r'D:\SpaceBook\SpaceBook Web\js\nazira_3_data.js'
    with open(out_js, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * TuitionHub - Class 3 Nazira Quran Comprehensive Dataset (KPK Textbook Board)\n")
        f.write(" * Complete 16 Lessons verbatim from official textbook:\n")
        f.write(" * D:\\SpaceBook\\Books\\3rd\\3rd Nazira\\Word\\3rd Nazira.docx\n")
        f.write(" * Full Tajweed phonics revision (Lesson 1) + Complete Recitation of Paras 3 to 8.\n")
        f.write(" */\n\n")
        f.write("var NAZIRA_3_DATA = ")
        f.write(json.dumps(all_chapters, ensure_ascii=False, indent=2))
        f.write(";\n\n")
        f.write("if (typeof DATA !== 'undefined') {\n")
        f.write("  DATA.nazira3Chapters = NAZIRA_3_DATA;\n")
        f.write("}\n")

    print(f"Successfully generated {out_js} with {len(all_chapters)} lessons!")

if __name__ == '__main__':
    build_nazira_3()
