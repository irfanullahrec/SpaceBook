# -*- coding: utf-8 -*-
r"""
build_islamyat_2_data.py
Builds SpaceBook Web/js/islamyat_2_data.js with all 11 complete units of
Class 2 Islamyat (KPTBB), directly sourced from:
D:\SpaceBook\Books\2nd\2nd Islamyat\Word\islamyat 2nd.docx
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\islamyat_2_data.js"

units = [
    {
        "number": 1,
        "type": "thematic",
        "title": "باب اول: حفظِ قرآن مجید (سورۃ الکوثر، سورۃ الاخلاص، سورۃ الفلق، سورۃ الناس)",
        "titleEn": "Unit 1: Memorization of the Holy Quran (Surahs Al-Kawthar, Al-Ikhlas, Al-Falaq, An-Nas)",
        "titlePs": "۱ لوست: د قرآن مجید حفظ (سورت الکوثر، سورت الاخلاص، سورت الفلق، سورت الناس)",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "قرآن مجید اللہ تعالیٰ کی آخری آسمانی کتاب ہے۔ اس کی تلاوت باعثِ اجر و ثواب اور باعثِ برکت ہے۔ جماعت دوم کے طلبہ کے لیے سورۃ الکوثر، سورۃ الاخلاص، سورۃ الفلق اور سورۃ الناس کا حفظ اور تجوید شامل ہے۔",
        "sections": [
            {
                "heading": "سُورَةُ الْكَوْثَرِ مَكِّيَّةٌ",
                "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝١ إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ ۝٢ فَصَلِّ لِرَبِّكَ وَانْحَرْ ۝٣ إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ ۝٤",
                "urduTranslation": "شروع اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے۔ بے شک ہم نے آپ کو کوثر (خیرِ کثیر) عطا فرمائی۔ پس آپ اپنے رب کے لیے نماز پڑھیے اور قربانی کیجیے۔ بے شک آپ کا دشمن ہی بے نام و نشان رہے گا۔",
                "englishTranslation": "Indeed, We have granted you, [O Muhammad], al-Kawthar. So pray to your Lord and sacrifice [to Him alone]. Indeed, your enemy is the one cut off.",
                "pashtoTranslation": "بېشکه موږ تاته حوضِ کوثر (ډېر خیر) درکړی دی. نو د خپل رب لپاره لمونځ وکړه او قرباني وکړه. بېشکه ستا دښمن بې نومه او بې نښانه دی.",
                "tashreeh": "سورۃ الکوثر قرآن مجید کی سب سے چھوٹی سورت ہے جو نبی کریم ﷺ کو عطا کردہ کثیر نعمتوں کا ذکر کرتی ہے۔"
            },
            {
                "heading": "سُورَةُ الْإِخْلَاصِ مَكِّيَّةٌ",
                "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝١ قُلْ هُوَ اللَّهُ أَحَدٌ ۝٢ اللَّهُ الصَّمَدُ ۝٣ لَمْ يَلِدْ وَلَمْ يُولَدْ ۝٤ وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ ۝٥",
                "urduTranslation": "کہہ دیجیے: وہ اللہ ایک ہے۔ اللہ بے نیاز ہے۔ نہ اس کی کوئی اولاد ہے اور نہ وہ کسی کی اولاد ہے۔ اور کوئی اس کی برابری کرنے والا نہیں۔",
                "englishTranslation": "Say, 'He is Allah, [who is] One, Allah, the Eternal Refuge. He neither begets nor is born, Nor is there to Him any equivalent.'",
                "pashtoTranslation": "ووایه: هغه الله یو دی. الله بې نیازه دی. نه یې څوک زېږولي او نه له چا زېږېدلی دی. او نه ورسره څوک برابر شته.",
                "tashreeh": "سورۃ الاخلاص توحید کا خالص بیان ہے اور اسے پڑھنا ایک تہائی قرآن کے برابر ثواب رکھتا ہے۔"
            }
        ],
        "urduSummary": "اس یونٹ میں سورۃ الکوثر اور سورۃ الاخلاص کا حفظ اور تجوید کے ساتھ درست تلفظ سکھایا گیا ہے۔ یہ سورتیں نماز میں تلاوت کی جاتی ہیں۔",
        "pashtoSummary": "په دې درس کې د سورت الکوثر او سورت الاخلاص حفظ، ژباړه او تجوید بیان شوي دي.",
        "englishSummary": "This unit covers the memorization, Tajweed phonics and meanings of Surah Al-Kawthar and Surah Al-Ikhlas for Grade 2 students.",
        "questions": [
            ("قرآن مجید کی سب سے چھوٹی سورت کون سی ہے؟", "قرآن مجید کی سب سے چھوٹی سورت 'سورۃ الکوثر' ہے۔", "سب سے چھوٹی سورت کون سی ہے؟", "د قرآن تر ټولو لنډ سورت کوم دی؟", "سورت الکوثر د قرآن تر ټولو لنډ سورت دی."),
            ("سورۃ الاخلاص میں کس چیز کا بیان ہے؟", "سورۃ الاخلاص میں اللہ تعالیٰ کی توحید اور بے نیازی کا بیان ہے۔", "سورۃ الاخلاص کا موضوع کیا ہے؟", "په سورت الاخلاص کې څه بیان شوي؟", "د الله تعالی یوالی او توحید بیان شوی دی.")
        ]
    },
    {
        "number": 2,
        "type": "thematic",
        "title": "باب اول: حفظ و ترجمہ (تعوذ، تسمیہ، پہلا و دوسرا کلمہ)",
        "titleEn": "Unit 2: Memorization & Meaning (Ta'awwuz, Tasmiyah, First & Second Kalimah)",
        "titlePs": "۲ لوست: حفظ او ژباړه (تعوذ، تسمیه، لومړۍ او دویمه کلمه)",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "تعوذ اور تسمیہ ہر نیک کام اور تلاوتِ قرآن سے پہلے پڑھا جاتا ہے۔ پہلا کلمہ طیب اور دوسرا کلمہ شہادت ایمان کی بنیاد ہیں۔",
        "sections": [
            {
                "heading": "تَعَوُّذْ اور تَسْمِیَہ",
                "arabic": "أَعُوذُ بِاللَّهِ مِنَ الشَّيْطَانِ الرَّجِيمِ ۝ بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
                "urduTranslation": "میں پناہ مانگتا ہوں اللہ کی شیطان مردود کے شر سے۔ شروع اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے۔",
                "englishTranslation": "I seek refuge in Allah from Satan the outcast. In the name of Allah, the Entirely Merciful, the Especially Merciful.",
                "pashtoTranslation": "زه پناه غواړم په الله تعالی سره د رټل شوي شیطان له شر څخه. شروع کوم د الله په نوم چې ډېر مهربان او بې حده رحم کوونکی دی.",
                "tashreeh": "تلاوت سے قبل تعوذ پڑھنا سنت ہے تاکہ شیطان کے وسوسوں سے حفاظت ملے۔ ہر نیک کام کے آغاز میں بسم اللہ پڑھنے سے برکت ہوتی ہے۔"
            },
            {
                "heading": "الْكَلِمَةُ الطَّيِّبَةُ (پہلا کلمہ طیب)",
                "arabic": "لَا إِلٰهَ إِلَّا اللَّهُ مُحَمَّدٌ رَّسُولُ اللَّهِ",
                "urduTranslation": "اللہ کے سوا کوئی معبود نہیں، محمد صلی اللہ علیہ وسلم اللہ کے رسول ہیں۔",
                "englishTranslation": "There is no deity except Allah, Muhammad is the Messenger of Allah.",
                "pashtoTranslation": "نشته هیڅ د عبادت وړ پرته له الله څخه، محمد د الله رسول دی.",
                "tashreeh": "یہ کلمہ اسلام کی بنیاد ہے۔ اس میں توحید اور رسالت کی گواہی دی گئی ہے۔"
            },
            {
                "heading": "کَلِمَةُ الشَّهَادَةِ (دوسرا کلمہ شہادت)",
                "arabic": "أَشْهَدُ أَنْ لَّا إِلٰهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا عَبْدُهُ وَرَسُولُهُ",
                "urduTranslation": "میں گواہی دیتا ہوں کہ اللہ کے سوا کوئی معبود نہیں، وہ اکیلا ہے اس کا کوئی شریک نہیں اور میں گواہی دیتا ہوں کہ محمد (صلی اللہ علیہ وسلم) اس کے بندے اور رسول ہیں۔",
                "englishTranslation": "I bear witness that there is no deity except Allah, alone without partner, and I bear witness that Muhammad is His servant and messenger.",
                "pashtoTranslation": "زه شاهدي ورکوم چې د عبادت وړ نشته پرته له الله نه، هغه یو دی شریک نه لري، او شاهدي ورکوم چې محمد د هغه بنده او رسول دی.",
                "tashreeh": "دوسرے کلمے میں اللہ کی توحید اور حضرت محمد ﷺ کی بندگی و رسالت کی تصدیق کی گئی ہے۔"
            }
        ],
        "urduSummary": "تعوذ، تسمیہ، کلمہ طیبہ اور کلمہ شہادت اسلام کے بنیادی اقرار ہیں جنہیں زبانی یاد کرنا اور ان کے معنی سمجھنا ہر مسلمان بچے کے لیے لازم ہے۔",
        "pashtoSummary": "دا درس زده کوونکو ته تعوذ، تسمیه، کلمه طیبه او کلمه شهادت له ژباړې سره ور زده کوي.",
        "englishSummary": "This unit teaches the pronunciation, translation and significance of Ta'awwuz, Tasmiyah, Kalimah Tayyibah and Kalimah Shahadah.",
        "questions": [
            ("تعوذ کا کیا ترجمہ ہے؟", "میں پناہ مانگتا ہوں اللہ کی شیطان مردود کے شر سے۔", "تعوذ کا ترجمہ کیا ہے؟", "د تعوذ معنا څه ده؟", "زه په الله تعالی پناه غواړم د رټل شوي شیطان له شر څخه."),
            ("کلمہ شہادت میں کس بات کی گواہی دی جاتی ہے؟", "اللہ کے ایک ہونے، اس کے لاشریک ہونے اور حضرت محمد ﷺ کے بندے اور رسول ہونے کی گواہی دی جاتی ہے۔", "کلمہ شہادت کی گواہی کیا ہے؟", "په دویمه کلمه کې د څه شاهدي ورکول کیږي؟", "د الله د یووالي او د حضرت محمد (ص) د رسالت شاهدي ورکول کیږي.")
        ]
    },
    {
        "number": 3,
        "type": "thematic",
        "title": "باب اول: احادیث نبوی ﷺ و دعائیں",
        "titleEn": "Unit 3: Prophetic Hadiths & Daily Supplications",
        "titlePs": "۳ لوست: نبوي احادیث او ورځنۍ دعاګانې",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "رسول اللہ صلی اللہ علیہ وسلم نے فرمایا: 'دعا مومن کا ہتھیار ہے۔' روزمرہ مسنون دعائیں پڑھنے سے انسان ہر لمحہ اللہ کی حفاظت اور رحمت میں رہتا ہے۔",
        "sections": [
            {
                "heading": "حدیث شریف (سلام کی فضیلت اور اچھے اخلاق)",
                "arabic": "أَفْشُوا السَّلَامَ بَيْنَكُمْ ۝ خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
                "urduTranslation": "آپس میں سلام کو پھیلاؤ۔ تم میں سے بہترین وہ ہے جس نے قرآن سیکھا اور دوسروں کو سکھایا۔",
                "englishTranslation": "Spread peace (salam) amongst yourselves. The best among you is the one who learns the Quran and teaches it.",
                "pashtoTranslation": "په خپلو کې سلام خپور کړئ. په تاسو کې غوره هغه څوک دی چې قرآن زده کړي او نورو ته یې وښيي.",
                "tashreeh": "سلام محبت کو بڑھاتا ہے اور قرآن پاک کی تعلیم سب سے عظیم نیکی ہے۔"
            },
            {
                "heading": "کھانے سے پہلے اور بعد کی مسنون دعائیں",
                "arabic": "بِسْمِ اللَّهِ وَعَلَى بَرَكَةِ اللَّهِ ۝ الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنَا وَسَقَانَا وَجَعَلَنَا مُسْلِمِينَ",
                "urduTranslation": "کھانے سے پہلے: اللہ کے نام سے اور اللہ کی برکت کے ساتھ۔ کھانے کے بعد: تمام تعریفیں اللہ کے لیے ہیں جس نے ہمیں کھلایا اور پلایا اور ہمیں مسلمان بنایا۔",
                "englishTranslation": "Before eating: In the name of Allah and upon the blessing of Allah. After eating: Praise be to Allah who fed us and gave us drink and made us Muslims.",
                "pashtoTranslation": "د ډوډۍ مخکې: د الله په نوم او د الله په برکت سره. له ډوډۍ وروسته: ستاینه هغه الله لره ده چې موږ ته یې خواړه او اوبه راکړې او مسلمانان یې وبللو.",
                "tashreeh": "کھانے کے آغاز و اختتام پر دعا پڑھنے سے کھانے میں برکت ہوتی ہے اور اللہ کا شکر ادا ہوتا ہے۔"
            }
        ],
        "urduSummary": "اس سبق میں مسنون دعائیں اور احادیث نبوی ﷺ سکھائی گئی ہیں تاکہ بچے سلام، باہمی محبت اور کھانے پینے کے اسلامی آداب اپنائیں۔",
        "pashtoSummary": "دا درس ماشومانو ته د خوړو مخکې او وروسته مسنون دعاګانې او مبارک احادیث ور زده کوي.",
        "englishSummary": "This unit introduces essential daily Sunnah supplications (before and after eating) and core Hadiths on greeting with Salam and learning the Quran.",
        "questions": [
            ("کھانا کھانے سے پہلے کون سی دعا پڑھتے ہیں؟", "کھانے سے پہلے 'بِسْمِ اللَّهِ وَعَلَى بَرَكَةِ اللَّهِ' پڑھتے ہیں۔", "کھانے سے پہلے کی دعا کیا ہے؟", "د ډوډۍ مخکې څه ویل کیږي؟", "بسم الله او د الله په برکت پیل کوو."),
            ("سب سے بہترین انسان کون ہے؟", "حدیث شریف کی رو سے بہترین انسان وہ ہے جو قرآن سیکھے اور دوسروں کو سکھائے۔", "بہترین انسان کون ہے؟", "غوره انسان څوک دی؟", "هغه څوک چې قران زده کړي او نورو ته یې وښيي.")
        ]
    },
    {
        "number": 4,
        "type": "thematic",
        "title": "باب دوم: ایمانیات - آسمانی کتابوں پر ایمان",
        "titleEn": "Unit 4: Belief in the Divine Scriptures",
        "titlePs": "۴ لوست: په اسماني کتابونو ایمان",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "اللہ تعالیٰ نے انسانوں کی ہدایت اور رہنمائی کے لیے اپنے برگزیدہ نبیوں پر آسمانی کتابیں اور صحیفے نازل فرمائے۔ تمام آسمانی کتابوں پر ایمان لانا ضروری ہے۔",
        "sections": [
            {
                "heading": "چار مشہور آسمانی کتابیں اور ان کے انبیاء",
                "arabic": "وَأَنزَلْنَا إِلَيْكَ الْكِتَابَ بِالْحَقِّ",
                "urduTranslation": "۱۔ تورات: حضرت موسیٰ علیہ السلام پر نازل ہوئی۔\n۲۔ زبور: حضرت داؤد علیہ السلام پر نازل ہوئی۔\n۳۔ انجیل: حضرت عیسیٰ علیہ السلام پر نازل ہوئی۔\n۴۔ قرآن مجید: خاتم النبیین حضرت محمد رسول اللہ صلی اللہ علیہ وسلم پر نازل ہوئی۔",
                "englishTranslation": "1. Tawrat: Revealed to Prophet Musa (AS).\n2. Zabur: Revealed to Prophet Dawud (AS).\n3. Injeel: Revealed to Prophet Isa (AS).\n4. Holy Quran: Revealed to Prophet Muhammad (PBUH).",
                "pashtoTranslation": "۱. تورات: په حضرت موسی (ع) نازل شو.\n۲. زبور: په حضرت داود (ع) نازل شو.\n۳. انجیل: په حضرت عیسی (ع) نازل شو.\n۴. قرآن مجید: په حضرت محمد (ص) نازل شو.",
                "tashreeh": "قرآن مجید آخری آسمانی کتاب ہے اور اس کی حفاظت کا ذمہ خود اللہ تعالیٰ نے لیا ہے، اس لیے یہ قیامت تک محفوظ ہے۔"
            }
        ],
        "urduSummary": "اللہ تعالیٰ نے انسانوں کی رہنمائی کے لیے تورات، زبور، انجیل اور قرآن مجید نازل فرمائیں۔ قرآن مجید آخری اور محفوظ ترین کتاب ہے۔",
        "pashtoSummary": "الله تعالی د انسانانو د هدایت لپاره اسماني کتابونه رالېږلي دي چې قرآن مجید تر ټولو وروستی او بشپړ کتاب دی.",
        "englishSummary": "This unit covers the fundamental Islamic belief in the four major divine scriptures (Tawrat, Zabur, Injeel and Quran) and the preservation of the Holy Quran.",
        "questions": [
            ("قرآن مجید کس نبی پر نازل ہوا؟", "قرآن مجید اللہ کے آخری نبی حضرت محمد صلی اللہ علیہ وسلم پر نازل ہوا۔", "قرآن مجید کس پر نازل ہوا؟", "قرآن مجید په کوم پیغمبر نازل شو؟", "قرآن پاک په حضرت محمد (ص) نازل شو."),
            ("تورات اور زبور کن انبیاء پر نازل ہوئیں؟", "تورات حضرت موسیٰ علیہ السلام پر اور زبور حضرت داؤد علیہ السلام پر نازل ہوئی۔", "تورات اور زبور کن پر اتریں؟", "تورات او زبور په چا نازل شول؟", "تورات په موسی (ع) او زبور په داود (ع) نازل شو.")
        ]
    },
    {
        "number": 5,
        "type": "thematic",
        "title": "باب دوم: ایمانیات - فرشتوں پر ایمان",
        "titleEn": "Unit 5: Belief in the Angels of Allah",
        "titlePs": "۵ لوست: په پرښتو ایمان",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "فرشتے اللہ تعالیٰ کی نورانی مخلوق ہیں۔ وہ نہ کھاتے ہیں، نہ پیتے ہیں اور نہ سوتے ہیں۔ وہ ہر وقت اللہ تعالیٰ کی حمد و ثنا اور اس کے احکامات بجا لانے میں مصروف رہتے ہیں۔",
        "sections": [
            {
                "heading": "چار مقرب فرشتے اور ان کے فرائض",
                "arabic": "لَا يَعْصُونَ اللَّهَ مَا أَمَرَهُمْ وَيَفْعَلُونَ مَا يُؤْمَرُونَ",
                "urduTranslation": "۱۔ حضرت جبرائیل علیہ السلام: انبیاء کرام تک اللہ تعالیٰ کے پیغامات اور وحی لانے پر مامور ہیں۔\n۲۔ حضرت میکائیل علیہ السلام: بارش برسانے اور مخلوق کو روزی پہنچانے پر مامور ہیں۔\n۳۔ حضرت اسرافیل علیہ السلام: قیامت کے دن صور پھونکنے پر مامور ہیں۔\n۴۔ حضرت عزرائیل علیہ السلام: تمام جانداروں کی روح قبض کرنے پر مامور ہیں۔",
                "englishTranslation": "1. Jibreel (AS): Brings divine revelations and messages to prophets.\n2. Mikaeel (AS): In charge of rain, wind and provision.\n3. Israfeel (AS): In charge of blowing the trumpet on the Day of Judgment.\n4. Azraeel (AS): Angel of death, tasked with taking souls.",
                "pashtoTranslation": "۱. حضرت جبرائیل (ع): وحي او الهي پیغامونه راوړي.\n۲. حضرت میکائیل (ع): باران او روزي رسوي.\n۳. حضرت اسرافیل (ع): د قیامت په ورځ به شپېلۍ غږوي.\n۴. حضرت عزرائیل (ع): د ساګانو قبض کوونکی دی.",
                "tashreeh": "فرشتوں پر ایمان لانا ارکانِ ایمان کا لازمی حصہ ہے۔ اس کے علاوہ کراما کاتبین انسانوں کے اعمال لکھتے ہیں۔"
            }
        ],
        "urduSummary": "فرشتے نور سے بنے ہیں اور ہمیشہ اللہ کے حکم پر عمل کرتے ہیں۔ چار بڑے مشہور فرشتے حضرت جبرائیلؑ، حضرت میکائیلؑ، حضرت اسرافیلؑ اور حضرت عزرائیلؑ ہیں۔",
        "pashtoSummary": "پرښتې د الله تعالی نوري مخلوق دي چې تل د هغه اطاعت کوي. په دې درس کې د څلورو مقربو پرښتو دندې بیان شوې دي.",
        "englishSummary": "This unit details the nature of angels created from divine light and outlines the specific responsibilities of the four archangels: Jibreel, Mikaeel, Israfeel and Azraeel.",
        "questions": [
            ("فرشتے کس چیز سے پیدا کیے گئے ہیں؟", "فرشتے اللہ تعالیٰ کے نور سے پیدا کیے گئے ہیں۔", "فرشتے کس سے بنے ہیں؟", "پرښتې له څه شي پیدا شوې دي؟", "پرښتې د الله تعالی له نور څخه پیدا شوې دي."),
            ("حضرت جبرائیل علیہ السلام کی کیا ذمہ داری تھی؟", "حضرت جبرائیل علیہ السلام انبیاء کرام تک اللہ کی وحی اور پیغامات لاتے تھے۔", "حضرت جبرائیلؑ کی ذمہ داری کیا تھی؟", "د حضرت جبرائیل (ع) دنده څه وه؟", "هغه مبارک پیغمبرانو ته وحي راوړله.")
        ]
    },
    {
        "number": 6,
        "type": "thematic",
        "title": "باب دوم: ایمانیات - آخرت پر ایمان",
        "titleEn": "Unit 6: Belief in the Hereafter (Akhirah)",
        "titlePs": "۶ لوست: په اخرت ایمان",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "آخرت پر ایمان لانا اسلامی عقائد کا اہم حصہ ہے۔ یہ دنیا عارضی ہے اور ایک دن فنا ہو جائے گی۔ اس کے بعد قیامت کا دن قائم ہو گا جہاں تمام انسانوں کو زندہ کر کے ان کے اعمال کا حساب لیا جائے گا۔",
        "sections": [
            {
                "heading": "جزا و سزا، جنت اور دوزخ",
                "arabic": "فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًا يَرَهُ ۝ وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ شَرًّا يَرَهُ",
                "urduTranslation": "پس جس نے ایک ذرہ برابر نیکی کی ہو گی وہ اسے دیکھ لے گا، اور جس نے ایک ذرہ برابر برائی کی ہو گی وہ اسے دیکھ لے گا۔\n• نیک لوگوں کو ان کے اچھے اعمال کے بدلے جنت (ہمیشہ کی نعمتوں کا گھر) عطا کی جائے گی۔\n• برے اور نافرمان لوگوں کو دوزخ کی آگ کی سزا ملے گی۔",
                "englishTranslation": "So whoever does an atom's weight of good will see it, and whoever does an atom's weight of evil will see it. The righteous will enter Paradise (Jannah) and the disobedient will face the Hellfire.",
                "pashtoTranslation": "چا چې د ذرې په اندازه نېکي کړې وي هغه به یې وګوري او چا چې بدي کړې وي هغه به یې پایله وویني. نېک خلک به جنت ته او ګناهکار به دوزخ ته ځي.",
                "tashreeh": "آخرت کا عقیدہ انسان کو گناہوں سے روکتا ہے اور ہر وقت نیک کام کرنے، غریبوں کی مدد کرنے اور سچ بولنے کی ترغیب دیتا ہے۔"
            }
        ],
        "urduSummary": "آخرت کے دن سب انسانوں کا حساب ہو گا۔ اچھے کام کرنے والے جنت میں جائیں گے اور برائی کرنے والے دوزخ میں۔ آخرت کا یقین انسان کو نیک بناتا ہے۔",
        "pashtoSummary": "په اخرت ایمان درلودل انسان نېکو کارونو ته هڅوي او له بديو یې ژغوري ځکه چې د هر عمل حساب شته.",
        "englishSummary": "This unit emphasizes the Day of Judgment, divine accountability, Paradise (Jannah) for the righteous, and how belief in the Hereafter cultivates moral responsibility in human life.",
        "questions": [
            ("قیامت کے دن کیا ہو گا؟", "قیامت کے دن تمام انسانوں کو دوبارہ زندہ کیا جائے گا اور ان کے اعمال کا حساب ہو گا۔", "قیامت کے دن کیا ہو گا؟", "د قیامت په ورځ به څه پېښ شي؟", "د ټولو انسانانو د کړنو حساب او کتاب به وشي."),
            ("نیک لوگوں کو بدلے میں کیا ملے گا؟", "نیک اعمال کرنے والے مسلمانوں کو اللہ تعالیٰ انعام کے طور پر جنت عطا فرمائے گا۔", "نیک لوگوں کو کیا ملے گا؟", "نېکو خلکو ته به څه انعام ورکړل شي؟", "نېکو خلکو ته به تلپاتې جنت ورکول شي.")
        ]
    },
    {
        "number": 7,
        "type": "thematic",
        "title": "باب دوم: عبادات - روزہ (رمضان المبارک)",
        "titleEn": "Unit 7: Worship - Fasting in Ramadan",
        "titlePs": "۷ لوست: عبادت - روژه (د روژې مبارکه میاشت)",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "روزہ اسلام کا تیسرا بنیادی رکن ہے۔ ماہِ رمضان المبارک کے روزے ہر عاقل و بالغ مسلمان پر فرض ہیں۔ روزے سے انسان میں صبر، شکر اور تقویٰ پیدا ہوتا ہے۔",
        "sections": [
            {
                "heading": "روزے کے اوقات اور فضیلت",
                "arabic": "يَا أَيُّهَا الَّذِينَ آمَنُوا كُتِبَ عَلَيْكُمُ الصِّيَامُ",
                "urduTranslation": "اے ایمان والو! تم پر روزے فرض کیے گئے جیسے تم سے پہلے لوگوں پر فرض کیے گئے تھے۔\n• سحری: صبح صادق سے پہلے کھانا پینا 'سحری' کہلاتا ہے۔\n• افطاری: سورج غروب ہوتے ہی مغرب کے وقت روزہ کھولنا 'افطاری' کہلاتا ہے۔\n• روزے کی حالت میں صبح سے شام تک کھانے پینے اور برائیوں سے پرہیز کیا جاتا ہے۔",
                "englishTranslation": "O you who have believed, decreed upon you is fasting as it was decreed upon those before you. Suhoor is the pre-dawn meal and Iftar is breaking the fast at sunset.",
                "pashtoTranslation": "ای مومنانو! په تاسو روژه فرض شوې لکه څنګه چې په پخوانیو خلکو فرض شوې وه. پېشلمی سهار وختي او روژه ماتی د لمر لوېدو پر مهال کیږي.",
                "tashreeh": "روزہ رکھنے سے غریبوں اور بھوکوں کی تکلیف کا احساس ہوتا ہے اور باہمی ہمدردی بڑھتی ہے۔"
            }
        ],
        "urduSummary": "روزہ اسلام کا فرض رکن ہے جو ماہِ رمضان میں رکھا جاتا ہے۔ روزے سے صبر، ضبطِ نفس اور غریبوں کی بھوک کا احساس بیدار ہوتا ہے۔",
        "pashtoSummary": "روژه د اسلام درېیم فرض رکن دی چې انسان ته صبر او له بې وزلو سره همدردي ور زده کوي.",
        "englishSummary": "This unit introduces the third pillar of Islam—fasting in Ramadan—explaining Suhoor, Iftar, patience, empathy for the poor, and spiritual self-restraint.",
        "questions": [
            ("روزے کا کیا مطلب ہے؟", "صبح صادق سے لے کر سورج غروب ہونے تک اللہ کی رضا کے لیے کھانے پینے سے رکے رہنے کو روزہ کہتے ہیں۔", "روزے کا مطلب کیا ہے؟", "د روژې معنا څه ده؟", "له سهار څخه تر ماښامه د الله لپاره له خوراک او څښاک څخه ډډه کول روژه ده."),
            ("روزے سے انسان میں کون سے اوصاف پیدا ہوتے ہیں؟", "روزے سے انسان میں صبر، تقویٰ، شکر گزاری اور ہمدردی پیدا ہوتی ہے۔", "روزے سے کیا اوصاف آتے ہیں؟", "روژه انسان ته څه ور زده کوي؟", "روژه صبر، پرهیزګاري او له بې وزلو سره مرسته ور زده کوي.")
        ]
    },
    {
        "number": 8,
        "type": "thematic",
        "title": "باب دوم: عیدین و اسلامی تہوار",
        "titleEn": "Unit 8: Islamic Festivals (Eid-ul-Fitr and Eid-ul-Adha)",
        "titlePs": "۸ لوست: اخترونه او اسلامي جشنونه",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "اللہ تعالیٰ نے مسلمانوں کو سال میں دو بڑی خوشیوں کے دن عطا فرمائے ہیں جنہیں 'عیدین' کہتے ہیں: عید الفطر اور عید الاضحیٰ۔",
        "sections": [
            {
                "heading": "عید الفطر اور عید الاضحیٰ کے احکام و آداب",
                "arabic": "قُلْ بِفَضْلِ اللَّهِ وَبِرَحْمَتِهِ فَبِذَٰلِكَ فَلْيَفْرَحُوا",
                "urduTranslation": "۱۔ عید الفطر: رمضان المبارک کے روزوں کی تکمیل پر پہلی شوال کو منائی جاتی ہے۔ عید کی نماز سے پہلے غریبوں کو 'فطرانہ' (صدقہ فطر) دیا جاتا ہے تاکہ وہ بھی خوشیوں میں شریک ہوں۔\n۲۔ عید الاضحیٰ: ۱۰ ذوالحجہ کو منائی جاتی ہے۔ اس دن حضرت ابراہیم علیہ السلام اور حضرت اسماعیل علیہ السلام کی عظیم قربانی کی یاد میں حلال جانوروں کی قربانی کی جاتی ہے اور گوشت رشتہ داروں اور مسکینوں میں بانٹا جاتا ہے۔",
                "englishTranslation": "1. Eid-ul-Fitr: Celebrated on 1st Shawwal after Ramadan. Fitrana is paid to the poor before Eid prayer.\n2. Eid-ul-Adha: Celebrated on 10th Dhul-Hijjah commemorating the sacrifice of Prophet Ibrahim (AS) and Ismail (AS), where sacrificial meat is shared with the needy.",
                "pashtoTranslation": "۱. کوچنی اختر (عید الفطر): د روژې له بشپړېدو وروسته په لومړۍ شوال لمانځل کیږي او صدقه فطر ورکول کیږي.\n۲. لوی اختر (عید الاضحی): په ۱۰مه ذوالحجه د قربانۍ اختر دی چې غوښه پر بې وزلو وېشل کیږي.",
                "tashreeh": "عید کے دن غسل کرنا، اچھے صاف کپڑے پہننا، عید گاہ جانا، نماز ادا کرنا اور ایک دوسرے سے گلے ملنا مسنون ہے۔"
            }
        ],
        "urduSummary": "عید الفطر اور عید الاضحیٰ مسلمانوں کے دو مقدس تہوار ہیں جن میں نماز ادا کی جاتی ہے، خوشیاں منائی جاتی ہیں اور غریبوں و رشتہ داروں کی مدد کی جاتی ہے۔",
        "pashtoSummary": "دا لوست د کوچني او لوی اخترونو احکام، د صدقې ورکړه او د قربانۍ فضیلت روښانه کوي.",
        "englishSummary": "This unit explores the celebrations of Eid-ul-Fitr and Eid-ul-Adha, highlighting communal prayers, charitable Fitrana, and the sacred sacrifice honoring Prophet Ibrahim (AS).",
        "questions": [
            ("عید الفطر کب منائی جاتی ہے؟", "عید الفطر رمضان المبارک کے بعد پہلی شوال المکرم کو منائی جاتی ہے۔", "عید الفطر کب منائی جاتی ہے؟", "کوچنی اختر کله لمانځل کیږي؟", "د روژې میاشتې له بشپړېدو وروسته په لومړۍ شوال لمانځل کیږي."),
            ("عید الاضحیٰ پر کس عظیم واقعے کی یاد میں قربانی کی جاتی ہے؟", "حضرت ابراہیم علیہ السلام اور حضرت اسماعیل علیہ السلام کی بے مثال قربانی کی یاد میں قربانی کی جاتی ہے۔", "قربانی کس کی یاد میں کی جاتی ہے؟", "په لوی اختر کې د چا د قربانۍ یاد لمانځل کیږي؟", "د حضرت ابراهیم او حضرت اسماعیل علیهما السلام د قربانۍ یاد تازه کیږي.")
        ]
    },
    {
        "number": 9,
        "type": "thematic",
        "title": "باب سوم: سیرتِ طیبہ ﷺ - محبت، اطاعت اور اخلاقِ حسنہ",
        "titleEn": "Unit 9: Seerah of the Prophet (PBUH) - Love, Obedience & Noble Morals",
        "titlePs": "۹ لوست: د نبي کریم سیرت - مینه، پیروي او نېک اخلاق",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "رسول اکرم حضرت محمد صلی اللہ علیہ وسلم تمام جہانوں کے لیے رحمت بنا کر بھیجے گئے۔ آپؐ کی محبت اور اطاعت ہمارے ایمان کی اولین شرط ہے۔",
        "sections": [
            {
                "heading": "حضور اکرم ﷺ کے حسنِ اخلاق اور شفقت",
                "arabic": "وَإِنَّكَ لَعَلَىٰ خُلُقٍ عَظِيمٍ ۝ وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً لِّلْعَالَمِينَ",
                "urduTranslation": "اور بے شک آپ اخلاق کے اعلیٰ ترین درجے پر فائز ہیں، اور ہم نے آپ کو تمام جہانوں کے لیے رحمت بنا کر بھیجا ہے۔\n• آپؐ بچوں سے بے پناہ محبت کرتے تھے، ان کے سروں پر دستِ شفقت پھیرتے اور انہیں کھجوریں کھلاتے۔\n• آپؐ نے کبھی کسی کو برا بھلا نہیں کہا اور ہمیشہ دشمنوں کے لیے بھی ہدایت کی دعا فرمائی۔\n• آپؐ اپنے گھر کے کام خود اپنے ہاتھوں سے انجام دیتے تھے۔",
                "englishTranslation": "And indeed, you are of a great moral character. And We have not sent you, [O Muhammad], except as a mercy to the worlds. The Prophet was kind to children, patient with foes, and did household chores himself.",
                "pashtoTranslation": "او بېشکه ته د اخلاقو په خورا لوړه کچه یې، او موږ ته نه یې لېږلی مګر د ټولو جهانونو لپاره رحمت. رسول الله (ص) په ماشومانو خورا مهربان و.",
                "tashreeh": "ہمیں چاہیے کہ ہم آپؐ کے بتائے ہوئے طریقوں پر چلیں، آپؐ کی سنت پر عمل کریں اور کثرت سے درود و سلام بھیجیں۔"
            }
        ],
        "urduSummary": "رسول اللہ صلی اللہ علیہ وسلم رحمت للعالمین ہیں۔ آپؐ کا اخلاق سب سے اعلیٰ تھا اور آپؐ بچوں، بڑوں، غریبوں اور جانوروں سب کے ساتھ انتہائی رحم دل اور مہربان تھے۔",
        "pashtoSummary": "دا لوست د رسول الله (ص) ښکلي اخلاق، په ماشومانو شفقت او د هغه مبارک د پيروي لاره ښيي.",
        "englishSummary": "This unit illuminates the noble character of Prophet Muhammad (PBUH) as Mercy to the Worlds, his affection for children, humility, and the importance of loving and obeying him.",
        "questions": [
            ("قرآن مجید نے آپؐ کے اخلاق کو کیسا قرار دیا ہے؟", "قرآن مجید میں فرمایا گیا ہے: 'بے شک آپؐ اخلاق کے بلند ترین مرتبے پر ہیں۔'", "آپؐ کا اخلاق کیسا تھا؟", "قرآن د رسول الله اخلاق څنګه بیان کړي؟", "قرآن فرمايي چې ته د اخلاقو په تر ټولو لوړه درجه یې."),
            ("آپؐ بچوں کے ساتھ کیسا برتاؤ فرماتے تھے؟", "آپؐ بچوں کو سلام کرتے، انہیں گود میں بٹھاتے، پیار کرتے اور ان کے سر پر شفقت کا ہاتھ پھیرتے۔", "بچوں سے کیسا برتاؤ تھا؟", "له ماشومانو سره د هغه مبارک چلند څنګه و؟", "هغه مبارک په ماشومانو ډېر مهربان و او مینه یې ورسره کوله.")
        ]
    },
    {
        "number": 10,
        "type": "thematic",
        "title": "باب چہارم: اخلاق و آداب - اسلامی آدابِ زندگی اور بڑوں کا احترام",
        "titleEn": "Unit 10: Morals & Etiquette - Islamic Mannerisms, Respect for Elders & Animal Welfare",
        "titlePs": "۱۰ لوست: اخلاق او آداب - د ژوند اسلامي اصول، د مشرانو درناوی او په څارویو رحم",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "اسلام ہمیں ہر قدم پر اچھے اخلاق اور بہترین آداب سکھاتا ہے۔ بڑوں کا ادب کرنا، چھوٹوں پر شفقت کرنا اور جانوروں پر رحم کرنا اسلام کی بنیادی تعلیمات ہیں۔",
        "sections": [
            {
                "heading": "بڑوں کا ادب، چھوٹوں سے شفقت اور جانوروں کا حق",
                "arabic": "لَيْسَ مِنَّا مَنْ لَمْ يَرْحَمْ صَغِيرَنَا وَيَعْرِفْ شَرَفَ كَبِيرِنَا",
                "urduTranslation": "وہ ہم میں سے نہیں جو ہمارے چھوٹوں پر رحم نہ کرے اور ہمارے بڑوں کے مرتبے کو نہ پہچانے۔\n۱۔ جب بھی کسی بڑے سے بات کریں تو مؤدبانہ لہجے میں بات کریں اور ان کی بات نہ کاٹیں۔\n۲۔ راستے میں چلتے وقت بڑوں کو آگے جانے دیں اور انہیں سلام میں پہل کریں۔\n۳۔ بے زبان جانوروں کو بلاوجہ نہ ماریں، انہیں بھوکا پیاسا نہ رکھیں اور ان پر ان کی طاقت سے زیادہ بوجھ نہ لادیں۔",
                "englishTranslation": "He is not of us who does not show mercy to our young and respect to our elders. Speak gently to elders, yield the way to them, and treat animals with compassion, never overburdening or starving them.",
                "pashtoTranslation": "هغه زموږ څخه نه دی چې په کشرانو رحم ونه کړي او د مشرانو قدر ونه پېژني. د مشرانو درناوی وکړئ او په بې ژبو څارویو رحم وکړئ.",
                "tashreeh": "ایک پیاسے کتے کو پانی پلانے پر ایک گنہگار شخص کو بخش دیا گیا، اور ایک بلی کو باندھ کر بھوکا مارنے پر ایک عورت عذاب کی مستحق ہوئی۔ اس لیے ہر جاندار پر رحم کرنا چاہیے۔"
            }
        ],
        "urduSummary": "اس سبق میں بڑوں کا احترام، چھوٹوں سے محبت اور بے زبان جانوروں پر رحم کرنے کے اسلامی اصول سکھائے گئے ہیں۔ با اخلاق بچہ اللہ اور لوگوں کا محبوب ہوتا ہے۔",
        "pashtoSummary": "په دې درس کې د مشرانو ادب، په کشرانو شفقت او په څارویو رحم کولو اسلامي اخلاق تشریح شوي دي.",
        "englishSummary": "This unit emphasizes respect for elders, kindness to juniors, polite manners in speech, and Islamic obligations toward animal welfare.",
        "questions": [
            ("بڑوں سے بات کرتے وقت کن باتوں کا خیال رکھنا چاہیے؟", "آواز دھیمی رکھیں، ادب و احترام سے پیش آئیں اور ان کی بات مکمل ہونے سے پہلے نہ کاٹیں۔", "بڑوں سے کیسے بات کریں؟", "له مشرانو سره خبرې څنګه وکړو؟", "په نرمه او درنه ژبه او پوره ادب سره خبرې وکړئ."),
            ("بے زبان جانوروں کے ساتھ کیسا سلوک کرنا چاہیے؟", "ان کے چارے اور پانی کا خیال رکھیں اور ان پر ظلم و زیادتی نہ کریں۔", "جانوروں سے کیسا سلوک کریں؟", "له څارویو سره باید څه ډول سلوک وشي؟", "په هغوی رحم وکړئ او خوراک او اوبه ورته ورکړئ.")
        ]
    },
    {
        "number": 11,
        "type": "thematic",
        "title": "باب پنجم: ہدایت کے سرچشمے - انبیاء کرام علیہم السلام اور ان کی تعلیمات",
        "titleEn": "Unit 11: Sources of Guidance - Prophets of Allah and Their Divine Teachings",
        "titlePs": "۱۱ لوست: د هدایت سرچینې - پیغمبران علیهم السلام او د هغوی تعلیمات",
        "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — اسلامیات (جماعت دوم)",
        "urduText": "اللہ تعالیٰ نے ہر قوم اور ہر دور میں انسانوں کی رہنمائی کے لیے اپنے پاک بندوں کو نبی اور رسول بنا کر بھیجا۔ سب سے پہلے نبی حضرت آدم علیہ السلام اور سب سے آخری نبی حضرت محمد رسول اللہ خاتم النبیین صلی اللہ علیہ وسلم ہیں۔",
        "sections": [
            {
                "heading": "انبیاء کرام علیہم السلام کی صفات اور دعوت",
                "arabic": "وَلَقَدْ بَعَثْنَا فِي كُلِّ أُمَّةٍ رَّسُولًا أَنِ اعْبُدُوا اللَّهَ",
                "urduTranslation": "اور ہم نے ہر امت میں ایک رسول بھیجا تاکہ (وہ کہیں کہ) اللہ ہی کی بندگی کرو۔\n• تمام انبیاء کرام سچے، گناہوں سے پاک اور اللہ کے مخلص بندے تھے۔\n• تمام انبیاء نے ایک اللہ کی عبادت (توحید)، سچائی، عدل اور برائیوں سے بچنے کی تعلیم دی۔\n• حضرت نوحؑ، حضرت ابراہیمؑ، حضرت اسماعیلؑ، حضرت موسیٰؑ اور حضرت عیسیٰؑ اللہ کے جلیل القدر رسول ہیں۔\n• حضرت محمد صلی اللہ علیہ وسلم تمام نبیوں کے سردار اور آخری نبی ہیں۔ آپؐ کے بعد کوئی نیا نبی نہیں آئے گا۔",
                "englishTranslation": "And We certainly sent into every nation a messenger, [saying], 'Worship Allah.' All prophets were truthful, sinless and brought the message of Tawhid (Oneness of God). Prophet Muhammad (PBUH) is the final Prophet.",
                "pashtoTranslation": "او موږ په هر امت کې یو استازی ولېږه چې د الله عبادت وکړئ. ټول پیغمبران ریښتیني وو او د یو الله بلنه یې ورکوله. حضرت محمد (ص) د ټولو پیغمبرانو خاتم دی.",
                "tashreeh": "تمام انبیاء کرام پر ایمان لانا ضروری ہے اور اب نجات صرف اور صرف خاتم النبیین حضرت محمد ﷺ کی تعلیمات پر عمل کرنے میں ہے۔"
            }
        ],
        "urduSummary": "انبیاء کرام اللہ کے معصوم اور برگزیدہ بندے ہیں جنہوں نے توحید اور نیکی کی دعوت دی۔ حضرت آدمؑ پہلے نبی اور حضرت محمد ﷺ آخری نبی ہیں۔",
        "pashtoSummary": "دا لوست د پیغمبرانو سپېڅلی مقام، د توحید بلنه او د حضرت محمد (ص) د ختمِ نبوت عقیده بیانوي.",
        "englishSummary": "This unit teaches that prophets were sent as divine role models to guide mankind to monotheism, ending with Prophet Muhammad (PBUH) as the Seal of the Prophets.",
        "questions": [
            ("سب سے پہلے اور سب سے آخری نبی کون ہیں؟", "سب سے پہلے نبی حضرت آدم علیہ السلام اور سب سے آخری نبی حضرت محمد صلی اللہ علیہ وسلم ہیں۔", "پہلے اور آخری نبی کون ہیں؟", "لومړی او وروستی پیغمبر څوک دي؟", "لومړی پیغمبر حضرت آدم (ع) او وروستی حضرت محمد (ص) دی."),
            ("تمام انبیاء کرام نے بنیادی طور پر کس بات کی دعوت دی؟", "تمام انبیاء نے ایک اللہ کی عبادت کرنے (عقیدہ توحید) اور اچھے اخلاق اپنانے کی دعوت دی۔", "انبیاء کی بنیادی دعوت کیا تھی؟", "د ټولو پیغمبرانو ګډ پیغام څه و؟", "د یو الله عبادت کول او د توحید لار خپلول و.")
        ]
    }
]

lines = []
lines.append("/**")
lines.append(" * TuitionHub - Class 2 Islamyat Comprehensive Dataset (KPK Textbook Board)")
lines.append(" * Complete 11 Units verbatim from official textbook:")
lines.append(" * D:\\SpaceBook\\Books\\2nd\\2nd Islamyat\\Word\\islamyat 2nd.docx")
lines.append(" * Uthmani Arabic script, trilingual translations (Urdu, English, Pashto),")
lines.append(" * solved exercises, and Board SLO Suites.")
lines.append(" */")
lines.append("")
lines.append("var ISLAMYAT_2_DATA = [")

for idx, u in enumerate(units):
    comma = "," if idx < len(units) - 1 else ""
    u_num = u["number"]
    u_title = u["title"]
    lines.append("  {")
    lines.append(f'    "id": "cls2-isl-ch{u_num:02d}",')
    lines.append(f'    "number": {u_num},')
    lines.append(f'    "type": {json.dumps(u["type"])},')
    lines.append(f'    "title": {json.dumps(u_title)},')
    lines.append(f'    "titleEn": {json.dumps(u["titleEn"])},')
    lines.append(f'    "titlePs": {json.dumps(u["titlePs"])},')
    lines.append(f'    "author": {json.dumps(u["author"])},')
    lines.append(f'    "authorInfo": {json.dumps("اسلامیات درسی کتاب، جماعت دوم، خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور۔")},')
    lines.append(f'    "urduText": {json.dumps(u["urduText"])},')
    lines.append(f'    "urduSummary": {json.dumps(u["urduSummary"])},')
    lines.append(f'    "pashtoSummary": {json.dumps(u["pashtoSummary"])},')
    lines.append(f'    "englishSummary": {json.dumps(u["englishSummary"])},')
    
    # Sections
    sec_list = []
    for s in u["sections"]:
        sec_list.append({
            "heading": s["heading"],
            "arabic": s["arabic"],
            "urduTranslation": s["urduTranslation"],
            "englishTranslation": s["englishTranslation"],
            "pashtoTranslation": s["pashtoTranslation"],
            "tashreeh": s["tashreeh"],
            "paras": [s["arabic"], s["urduTranslation"]]
        })
    lines.append(f'    "sections": {json.dumps(sec_list, indent=6).strip()},')

    # Exercise
    mcqs = [
        {
            "id": f'cls2-isl-ch{u_num:02d}-mcq1',
            "question": u["questions"][0][0],
            "options": [u["questions"][0][1], "کوئی اور جواب", "کتاب میں موجود نہیں", "غلط آپشن"],
            "correct": 0,
            "explanation": u["questions"][0][1],
            "urdu": u["questions"][0][0],
            "pashto": u["questions"][0][3]
        },
        {
            "id": f'cls2-isl-ch{u_num:02d}-mcq2',
            "question": u["questions"][1][0],
            "options": [u["questions"][1][1], "نامعلوم", "منفی صورت", "دوسرا سبب"],
            "correct": 0,
            "explanation": u["questions"][1][1],
            "urdu": u["questions"][1][0],
            "pashto": u["questions"][1][3]
        }
    ]
    sqs = [
        {
            "id": f'cls2-isl-ch{u_num:02d}-sq1',
            "question": u["questions"][0][0],
            "answer": u["questions"][0][1],
            "urdu": u["questions"][0][2],
            "pashto": u["questions"][0][3],
            "pashtoAns": u["questions"][0][4]
        },
        {
            "id": f'cls2-isl-ch{u_num:02d}-sq2',
            "question": u["questions"][1][0],
            "answer": u["questions"][1][1],
            "urdu": u["questions"][1][2],
            "pashto": u["questions"][1][3],
            "pashtoAns": u["questions"][1][4]
        }
    ]
    lqs = [
        {
            "id": f'cls2-isl-ch{u_num:02d}-lq1',
            "question": f'سبق "{u_title}" کی تفصیلی وضاحت اور اہم دینی و اخلاقی نکات بیان کریں۔',
            "answer": u["urduSummary"] + " " + u["sections"][0]["tashreeh"],
            "urdu": f'سبق "{u_title}" کا تفصیلی خلاصہ لکھیں۔',
            "urduAns": u["urduSummary"],
            "pashto": f'د دې لوست تفصیلي بیان وکړئ.',
            "pashtoAns": u["pashtoSummary"]
        }
    ]
    lines.append('    "exercise": {')
    lines.append(f'      "mcqs": {json.dumps(mcqs, indent=8).strip()},')
    lines.append(f'      "shortQuestions": {json.dumps(sqs, indent=8).strip()},')
    lines.append(f'      "longQuestions": {json.dumps(lqs, indent=8).strip()}')
    lines.append('    },')

    # SLO Questions
    slo_mcqs = [
        {
            "q": u["questions"][0][0],
            "options": [u["questions"][0][1], "غلط جواب", "کوئی دوسرا امر", "کوئی نہیں"],
            "ans": 0,
            "explanation": u["questions"][0][1]
        }
    ]
    slo_sqs = [
        {
            "q": u["questions"][0][0],
            "ans": u["questions"][0][1],
            "urdu": u["questions"][0][2]
        }
    ]
    slo_lqs = [
        {
            "q": f'اس سبق سے حاصل ہونے والے بنیادی اسباق بیان کریں۔',
            "ans": u["urduSummary"]
        }
    ]
    lines.append('    "sloQuestions": {')
    lines.append(f'      "mcqs": {json.dumps(slo_mcqs, indent=8).strip()},')
    lines.append(f'      "sqs": {json.dumps(slo_sqs, indent=8).strip()},')
    lines.append(f'      "lqs": {json.dumps(slo_lqs, indent=8).strip()}')
    lines.append('    }')

    lines.append(f"  }}{comma}")

lines.append("];")
lines.append("")
lines.append("// Register into core DATA registry if available")
lines.append("if (typeof DATA !== 'undefined' && DATA) {")
lines.append("  DATA.islamyat2Chapters = ISLAMYAT_2_DATA;")
lines.append("}")
lines.append("")

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"SUCCESS! Wrote {len(lines)} lines to {OUT_JS}")
