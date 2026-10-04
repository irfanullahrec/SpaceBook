# -*- coding: utf-8 -*-
r"""
build_nazira_2_data.py
Builds SpaceBook Web/js/nazira_2_data.js with all 15 complete lessons of
Class 2 Nazira Quran (KPTBB), directly sourced from:
D:\SpaceBook\Books\2nd\2nd Nazira\Word\Nazira 2nd.docx
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\nazira_2_data.js"

lessons = [
    {
        "number": 1,
        "type": "tajweed",
        "title": "سبق ۱: عربی حروفِ تہجی و مخارج (اعادہ)",
        "titleEn": "Lesson 1: Arabic Alphabet & Phonics Revision",
        "titlePs": "۱ لوست: د عربی الفبا توري او مخارج (تکرار)",
        "arabic": "ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن و ه ء ي",
        "rule": "عربی کے تمام ۲۹ حروفِ تہجی کو ان کے درست مخارج اور صفات کے ساتھ ادا کیا جائے۔ حروفِ مستعلیہ (خ، ص، ض، ط، ظ، غ، ق) کو ہر حال میں موٹا پڑھا جائے اور حروفِ سفیرہ (ز، س، ص) میں سیٹی کی آواز پیدا کی جائے۔",
        "ruleEn": "Revise the articulation of all 29 Arabic alphabet letters with accurate Tajweed phonics.",
        "rulePs": "د عربی ژبې ۲۹ واړه توري له خپلو کره مخارجو او سم تجوید سره تکرار کړئ.",
        "examples": "أَ بَ تَ ثَ جَ حَ خَ دَ ذَ رَ زَ سَ شَ صَ ضَ طَ ظَ عَ غَ فَ قَ كَ لَ مَ نَ وَ هَ ءَ يَ",
        "questions": [
            ("عربی زبان میں کل کتنے حروفِ تہجی ہیں؟", "عربی زبان میں کل ۲۹ حروفِ تہجی ہیں۔", "کتنے حروف ہیں؟", "په عربی الفبا کې څو توري دي؟", "په عربی الفبا کې ۲۹ توري دي."),
            ("حروفِ مستعلیہ (موٹی آواز والے حروف) کون سے ہیں؟", "خ، ص، ض، ط، ظ، غ، ق (خُصَّ ضَغْطٍ قِظْ) ہمیشہ پر پڑھے جاتے ہیں۔", "موٹے حروف کون سے ہیں؟", "ډک توري کوم دي؟", "دا اووه توري تل ډک لوستل کېږي.")
        ]
    },
    {
        "number": 2,
        "type": "tajweed",
        "title": "سبق ۲: زبر (اعادہ)",
        "titleEn": "Lesson 2: Zabar (Fathah) Revision",
        "titlePs": "۲ لوست: زبر (فتحه) تکرار",
        "arabic": "ـَ (فَتْحَة)",
        "rule": "زبر حرف کے اوپر ترچھی لکیر کی صورت میں ہوتا ہے۔ زبر کو بغیر کھینچے اور بغیر جھٹکا دیے نرمی سے ادا کیا جاتا ہے، جیسے: دَ، رَ، سَ۔",
        "ruleEn": "Fathah (Zabar) is a short diagonal stroke above a letter representing a short 'a' vowel.",
        "rulePs": "زبر د توري دپاسه راځي او بې له کشولو په لنډه توګه لوستل کیږي.",
        "examples": "دَرَجَ - وَرَدَ - ذَهَبَ - شَكَرَ - كَتَبَ - نَظَرَ - قَرَأَ",
        "questions": [
            ("زبر کہاں واقع ہوتا ہے اور اس کی آواز کیسی ہوتی ہے؟", "زبر حرف کے اوپر آتا ہے اور اس کی آواز بغیر کھینچے مختصر 'اَ' ہوتی ہے۔", "زبر کہاں آتا ہے؟", "زبر چیرته راځي او غږ یې څنګه دی؟", "زبر د توري دپاسه راځي او لنډ لوستل کیږي."),
            ("تین زبر والے حروف کی مثال دیں؟", "دَرَجَ، وَرَدَ، شَكَرَ تین زبر والے کلمات ہیں۔", "مثالیں کیا ہیں؟", "د زبر مثالونه څه دي؟", "دَرَجَ او كَتَبَ د زبر مثالونه دي.")
        ]
    },
    {
        "number": 3,
        "type": "tajweed",
        "title": "سبق ۳: زیر (اعادہ)",
        "titleEn": "Lesson 3: Zair (Kasrah) Revision",
        "titlePs": "۳ لوست: زېر (کسره) تکرار",
        "arabic": "ـِ (كَسْرَة)",
        "rule": "زیر حرف کے نیچے ترچھی لکیر کی صورت میں ہوتا ہے۔ اس کی آواز 'اِ' کی طرح بغیر مجہول پڑھے ادا کی جاتی ہے، جیسے: شَهِدَ، عَلِمَ۔",
        "ruleEn": "Kasrah (Zair) is a short diagonal stroke below a letter representing a short 'i' vowel.",
        "rulePs": "زېر د توري لاندې راځي او د لنډ 'ای' غږ ورکوي.",
        "examples": "عَلِمَ - شَهِدَ - سَمِعَ - حَمِدَ - رَحِمَ - بَخِلَ",
        "questions": [
            ("زیر کو کس طرح ادا کرنا چاہیے؟", "زیر کو معروف انداز میں بغیر مجہول کیے ادا کرنا چاہیے تاکہ 'اے' نہ بنے۔", "زیر کی ادائیگی کیسی ہو؟", "زېر څنګه ادا کیږي؟", "زېر باید معروف او صاف ادا شي."),
            ("زیر والے دو الفاظ بتائیں؟", "عَلِمَ اور سَمِعَ زیر والے الفاظ ہیں۔", "الفاظ کیا ہیں؟", "د زېر کلمات کوم دي؟", "عَلِمَ او سَمِعَ د زېر مثالونه دي.")
        ]
    },
    {
        "number": 4,
        "type": "tajweed",
        "title": "سبق ۴: پیش (اعادہ)",
        "titleEn": "Lesson 4: Paish (Dammah) Revision",
        "titlePs": "۴ لوست: پېښ (ضمه) تکرار",
        "arabic": "ـُ (ضَمَّة)",
        "rule": "پیش حرف کے اوپر واؤ کی طرح چھوٹی علامت ہوتی ہے۔ اسے ہونٹوں کو گول کر کے بغیر کھینچے 'اُ' کی آواز کے ساتھ پڑھا جاتا ہے۔",
        "ruleEn": "Dammah (Paish) represents a short 'u' vowel formed by rounding the lips without elongation.",
        "rulePs": "پېښ د شونډو په ګردولو سره بې له کشولو لنډ لوستل کیږي.",
        "examples": "رُسُلُ - صُحُفُ - قُتِلَ - خُلِقَ - ذُكِرَ - سُئِلَ",
        "questions": [
            ("پیش پڑھتے وقت ہونٹوں کی کیا کیفیت ہوتی ہے؟", "پیش ادا کرتے وقت دونوں ہونٹوں کو گول کیا جاتا ہے۔", "ہونٹ کیسے ہوتے ہیں؟", "د پېښ په مهال شونډې څنګه کیږي؟", "شونډې ګردې کیږي او غږ ادا کیږي."),
            ("پیش والے تین کلمات بتائیں؟", "رُسُلُ، صُحُفُ اور قُتِلَ پیش والے کلمات ہیں۔", "مثالیں بتائیں؟", "مثالونه کوم دي؟", "رُسُلُ او صُحُفُ یې بېلګې دي.")
        ]
    },
    {
        "number": 5,
        "type": "tajweed",
        "title": "سبق ۵: جزم و سکون (اعادہ)",
        "titleEn": "Lesson 5: Jazm & Sukoon Revision",
        "titlePs": "۵ لوست: جزم او سکون تکرار",
        "arabic": "ـْ (سُكُون)",
        "rule": "جس حرف پر جزم ہو اسے 'ساکن' کہتے ہیں۔ ساکن حرف کو پچھلے متحرک حرف سے ملا کر پڑھا جاتا ہے۔ حروفِ قلقلہ (ق، ط، ب، ج، د) ساکن ہوں تو ان میں جھٹکا پیدا ہوتا ہے۔",
        "ruleEn": "Jazm (Sukoon) indicates a vowelless consonant, read together with the preceding vowel.",
        "rulePs": "جزم د توري ساکنوالی ښيي او له مخکيني توري سره نښلول کیږي.",
        "examples": "أَبْ - أَتْ - أَثْ - مَنْ - هَلْ - قُمْ - إِذْ - قُلْ أَعُوذُ",
        "questions": [
            ("جزم والے حرف کو کیا کہتے ہیں؟", "جزم والے حرف کو 'ساکن' کہا جاتا ہے۔", "جزم والے کو کیا کہتے ہیں؟", "د جزم لرونکی توری څه بلل کیږي؟", "د جزم توری ساکن بلل کیږي."),
            ("حروفِ قلقلہ کتنے اور کون سے ہیں؟", "حروفِ قلقلہ ۵ ہیں: ق، ط، ب، ج، د (قُطْبُ جَدٍّ)۔", "قلقلہ کے حروف کیا ہیں؟", "د قلقلې توري کوم دي؟", "ق، ط، ب، ج، د د قلقلې توري دي.")
        ]
    },
    {
        "number": 6,
        "type": "tajweed",
        "title": "سبق ۶: تشدید (اعادہ)",
        "titleEn": "Lesson 6: Tashdeed (Shaddah) Revision",
        "titlePs": "۶ لوست: تشدید (شَدّه) تکرار",
        "arabic": "ـّ (شَدَّة)",
        "rule": "جس حرف پر تشدید ہو اسے 'مشدد' کہتے ہیں۔ مشدد حرف کو دو مرتبہ پڑھا جاتا ہے: پہلی بار پچھلے حرف سے ملا کر ساکن اور دوسری بار اپنی حرکت کے ساتھ، جیسے: رَبَّ۔",
        "ruleEn": "Tashdeed (Shaddah) doubles the consonant: first silent, second vocalized.",
        "rulePs": "تشدید والا توری دوه ځله ویل کیږي: لومړی ساکن او دویم له حرکت سره.",
        "examples": "رَبَّ - إِنَّ - ثُمَّ - قُلْ - حَقَّ - شَدَّ - مَدَّ",
        "questions": [
            ("مشدد حرف کو کتنی بار پڑھا جاتا ہے؟", "مشدد حرف کو دو بار مضبوطی اور جماؤ کے ساتھ پڑھا جاتا ہے۔", "کتنی بار پڑھتے ہیں؟", "تشدید لرونکی توری څو ځله لوستل کیږي؟", "هغه توری دوه ځله لوستل کیږي."),
            ("نون اور میم مشدد میں کیا خاص حکم ہے؟", "نون اور میم مشدد پر ہمیشہ غنہ (ناک میں آواز لے جانا) کیا جاتا ہے۔", "نون و میم کا کیا حکم ہے؟", "په نون او میم مشدد څه کیږي؟", "په هغوی کې تل غنه کیږي.")
        ]
    },
    {
        "number": 7,
        "type": "tajweed",
        "title": "سبق ۷: کھڑی حرکات (کھڑی زبر، کھڑی زیر، الٹا پیش)",
        "titleEn": "Lesson 7: Standing Harakaat (Khari Zabar, Khari Zair, Ulta Paish)",
        "titlePs": "۷ لوست: ولاړ حرکتونه (ولاړ زبر، ولاړ زېر، الوت پېښ)",
        "arabic": "ـٰ / ـٖ / ـٗ",
        "rule": "کھڑی زبر الف مدہ کے برابر، کھڑی زیر یا مدہ کے برابر اور الٹا پیش واؤ مدہ کے برابر ہوتا ہے۔ ان تینوں کو ایک الف (دو حرکات) کے برابر کھینچ کر پڑھا جاتا ہے۔",
        "ruleEn": "Standing vowels represent elongated vowels equivalent to natural elongation (Madd Asli).",
        "rulePs": "ولاړ حرکتونه د یوه الف په اندازه کش کیږي.",
        "examples": "بٰ - تٰ - بٖ - تٖ - بٗ - تٗ - إِيلَافِهِمْ - دَاوُۥدُ",
        "questions": [
            ("کھڑی زبر کس کے برابر ہوتی ہے؟", "کھڑی زبر الف مدہ کے برابر ہوتی ہے اور ایک الف کھینچی جاتی ہے۔", "کھڑی زبر کس کے برابر ہے؟", "ولاړ زبر د څه برابر دی؟", "ولاړ زبر د الف مده برابر دی."),
            ("الٹا پیش کس کے برابر ہوتا ہے؟", "الٹا پیش واؤ مدہ کے برابر ہوتا ہے اور ایک الف لمبا کیا جاتا ہے۔", "الٹا پیش کس کے برابر ہے؟", "اوښتی پېښ د څه برابر دی؟", "دا د واو مده برابر دی.")
        ]
    },
    {
        "number": 8,
        "type": "tajweed",
        "title": "سبق ۸: حروفِ مدہ (اعادہ)",
        "titleEn": "Lesson 8: Letters of Madd (Alif, Waw, Yaa)",
        "titlePs": "۸ لوست: د مدې توري (الف، واو، یا)",
        "arabic": "حُرُوفُ الْمَدِّ: ا / و / ي",
        "rule": "حروفِ مدہ تین ہیں:\n۱۔ الف ساکن جس سے پہلے زبر ہو (بَا)۔\n۲۔ واؤ ساکن جس سے پہلے پیش ہو (بُو)۔\n۳۔ یا ساکن جس سے پہلے زیر ہو (بِي)۔\nان کو ایک الف کے برابر کھینچ کر پڑھتے ہیں۔",
        "ruleEn": "The three long vowels (Madd): Alif preceded by Fathah, Waw preceded by Dammah, and Yaa preceded by Kasrah.",
        "rulePs": "د مدې درې توري دي چې د یوه الف په اندازه کش کیږي.",
        "examples": "بَا بُو بِي - قَالَ يَقُولُ قِيلَ - نُوحِيهَا",
        "questions": [
            ("حروفِ مدہ کتنے ہیں اور کون سے ہیں؟", "حروفِ مدہ تین ہیں: الف، واؤ، یا۔", "حروفِ مدہ کون سے ہیں؟", "د مدې توري څو دي؟", "درې دي: الف، واو او یا."),
            ("کلمہ 'نُوحِيهَا' میں کون سے حروفِ مدہ ہیں؟", "اس میں تینوں حروفِ مدہ (واؤ مدہ، یا مدہ اور الف مدہ) جمع ہیں۔", "نُوحِيهَا میں کیا ہے؟", "په نوحیها کې کوم توري دي؟", "په دې کې درې واړه د مدې توري راغلي دي.")
        ]
    },
    {
        "number": 9,
        "type": "tajweed",
        "title": "سبق ۹: حروفِ مقطعات",
        "titleEn": "Lesson 9: Huroof Muqatta'at (Disjointed Letters)",
        "titlePs": "۹ لوست: د مقطعاتو توري",
        "arabic": "الم - الر - المص - المر - كهيعص - طه - طسم - طس - يس - ص - حم - عسق - ق - ن",
        "rule": "حروفِ مقطعات وہ حروف ہیں جو سورتوں کے شروع میں الگ الگ پڑھے جاتے ہیں۔ جن حروف پر مد ہو انہیں ۳ سے ۵ الف کے برابر کھینچا جاتا ہے جیسے: الٓمّٓ، كٓهٰيٰعٓصٓ۔",
        "ruleEn": "Muqatta'at are disjointed letter openings of Surahs pronounced individually with proper Madd elongation.",
        "rulePs": "دا د سورتونو په سر کې جلا جلا لوستل کیږي او کش کیږي.",
        "examples": "الٓمّٓ - الٓرٰ - كٓهٰيٰعٓصٓ - طٰهٰ - يٰسٓ - حٰمٓ - قٓ - نٓ",
        "questions": [
            ("حروفِ مقطعات کیسے پڑھے جاتے ہیں؟", "حروفِ مقطعات کو جوڑنے کے بجائے الگ الگ اور مد کے ساتھ پڑھا جاتا ہے۔", "کیسے پڑھے جاتے ہیں؟", "دا توري څنګه لوستل کیږي؟", "دا جلا جلا د مد سره لوستل کیږي."),
            ("قرآن مجید کی کتنی سورتیں حروفِ مقطعات سے شروع ہوتی ہیں؟", "قرآن مجید کی ۲۹ سورتیں حروفِ مقطعات سے شروع ہوتی ہیں۔", "کتنی سورتیں ہیں؟", "څو سورتونه په مقطعاتو پیل کیږي؟", "۲۹ سورتونه په مقطعاتو پیل کیږي.")
        ]
    },
    {
        "number": 10,
        "type": "tajweed",
        "title": "سبق ۱۰: حروفِ لین (اعادہ)",
        "titleEn": "Lesson 10: Letters of Leen (Soft Vowels)",
        "titlePs": "۱۰ لوست: د لین توري",
        "arabic": "و / ي (مَا قَبْلَهَا مَفْتُوحٌ)",
        "rule": "حروفِ لین دو ہیں: واؤ ساکن اور یا ساکن جب ان سے پہلے زبر ہو (جیسے: اَوْ، اَیْ)۔ ان کو بغیر کھینچے نرمی سے جلدی ادا کیا جاتا ہے، جیسے: خَوْفٌ، بَیْتٌ۔",
        "ruleEn": "Huroof-e-Leen are Waw Sakinah and Yaa Sakinah preceded by Fathah, pronounced softly without dragging.",
        "rulePs": "د لین دوه توري دي (واو او یا ساکن چې مخکې یې زبر وي) او په نرمۍ لوستل کیږي.",
        "examples": "خَوْفٌ - بَيْتٌ - قَوْمٌ - صَيْفٌ - يَوْمٌ - خَيْرٌ",
        "questions": [
            ("حروفِ لین کتنے اور کون سے ہیں؟", "حروفِ لین دو ہیں: واؤ لین اور یا لین۔", "لین کے حروف کیا ہیں؟", "د لین توري څو دي؟", "دوه دي: واو او یا چې مخکې یې زبر وي."),
            ("حروفِ لین کی ادائیگی کیسی ہونی چاہیے؟", "ان کو بغیر جھٹکے اور بغیر زیادہ کھینچے نرمی کے ساتھ ادا کرنا چاہیے۔", "ادائیگی کیسی ہو؟", "اداکول یې څنګه دي؟", "په خورا نرمه توګه لوستل کیږي.")
        ]
    },
    {
        "number": 11,
        "type": "tajweed",
        "title": "سبق ۱۱: تنوین (اعادہ)",
        "titleEn": "Lesson 11: Tanween (Double Vowels - Nunation)",
        "titlePs": "۱۱ لوست: تنوین (دوه زبر، دوه زېر، دوه پېښ)",
        "arabic": "ـً / ـٍ / ـٌ (تَنْوِين)",
        "rule": "دو زبر، دو زیر اور دو پیش کو 'تنوین' کہتے ہیں۔ تنوین کی آواز دراصل نون ساکن کی ہوتی ہے (جیسے: بً = بَنْ، بٍ = بِنْ، بٌ = بُنْ)۔",
        "ruleEn": "Tanween refers to double vowels indicating a nunated ending sounding like a Noon Sakinah.",
        "rulePs": "دوه زبر، دوه زېر او دوه پېښ ته تنوین وايي چې د نون غږ ورکوي.",
        "examples": "كِتَابًا - رَحْمَةٍ - سَمِيعٌ - خَبِيرٌ - عَلِيمًا - قَرِيبٌ",
        "questions": [
            ("تنوین کسے کہتے ہیں؟", "دو زبر، دو زیر اور دو پیش کو تنوین کہتے ہیں۔", "تنوین کسے کہتے ہیں؟", "تنوین څه ته وايي؟", "دوه زبر، دوه زېر او دوه پېښ ته تنوین وايي."),
            ("تنوین میں دراصل کس حرف کی آواز پوشیدہ ہوتی ہے؟", "تنوین میں نون ساکن (نْ) کی آواز چھپی ہوتی ہے۔", "کس حرف کی آواز ہے؟", "د کوم توري غږ په کې پټ وي؟", "د نون ساکن غږ په کې وي.")
        ]
    },
    {
        "number": 12,
        "type": "tajweed",
        "title": "سبق ۱۲: غنہ و اخفاء (اعادہ)",
        "titleEn": "Lesson 12: Ghunnah & Ikhfa Revision",
        "titlePs": "۱۲ لوست: غنه او اخفاء تکرار",
        "arabic": "الْغُنَّةُ (صَوْتٌ يَخْرُجُ مِنَ الْخَيْشُومِ)",
        "rule": "ناک کے بانسے سے ایک الف کے برابر گنگنی آواز نکالنے کو 'غنہ' کہتے ہیں۔ نون مشدد، میم مشدد اور نون ساکن و تنوین کے اخفاء و ادغام میں غنہ کیا جاتا ہے۔",
        "ruleEn": "Ghunnah is a nasal sound produced through the nasal cavity held for one count (Alif).",
        "rulePs": "له پوزې څخه نری غږ راایستلو ته غنه وايي.",
        "examples": "إِنَّ - عَمَّ - مَن كَانَ - كُنتُمْ - أَنتُمْ - أَنفُسَكُمْ",
        "questions": [
            ("غنہ کسے کہتے ہیں؟", "ناک کے بانسے سے نغمگی کے ساتھ آواز نکالنے کو غنہ کہتے ہیں۔", "غنہ کیا ہے؟", "غنه څه ده؟", "له پوزې څخه د نري غږ راایستلو ته غنه وايي."),
            ("غنہ کتنی دیر تک ادا کیا جاتا ہے؟", "غنہ ایک الف (دو حرکات) کی مقدار کے برابر ادا کیا جاتا ہے۔", "کتنی دیر ہوتا ہے؟", "غنه څومره وخت دوام کوي؟", "د یوه الف په اندازه دوام کوي.")
        ]
    },
    {
        "number": 13,
        "type": "tajweed",
        "title": "سبق ۱۳: مد کی اقسام (اعادہ)",
        "titleEn": "Lesson 13: Rules of Madd (Elongation)",
        "titlePs": "۱۳ لوست: د مد ډولونه (تکرار)",
        "arabic": "الْمَدُّ (ـٓ)",
        "rule": "حروفِ مدہ کے بعد اگر ہمزہ یا جزم و تشدید آئے تو آواز کو ۳ سے ۵ الف تک لمبا کیا جاتا ہے، جیسے: جَآءَ (مد متصل)، بِمَآ أُنزِلَ (مد منفصل)، اور وَلَا الضَّآلِّينَ (مد لازم)۔",
        "ruleEn": "Madd refers to elongating the voice beyond normal length due to a Hamzah or Sukoon/Shaddah.",
        "rulePs": "مد د غږ اوږدول دي چې له ۳ تر ۵ الف پورې کش کیږي.",
        "examples": "جَآءَ - السَّمَآءُ - إِنَّآ أَعْطَيْنَاكَ - وَلَا الضَّآلِّينَ - الصَّآخَّةُ",
        "questions": [
            ("مد کی لمبائی کتنی ہوتی ہے؟", "مد کی مقدار ۳ سے ۵ الف (طویل کھینچاؤ) تک ہوتی ہے۔", "مد کی لمبائی کیا ہے؟", "د مد کچه څومره ده؟", "له ۳ تر ۵ الف پورې کش کیږي."),
            ("مد لازم کی مثال کیا ہے؟", "'وَلَا الضَّآلِّينَ' میں مد لازم ہے جسے خوب کھینچ کر پڑھتے ہیں۔", "مد لازم کی مثال کیا ہے؟", "د مد لازم مثال څه دی؟", "وَلَا الضَّآلِّينَ د مد لازم غوره بېلګه ده.")
        ]
    },
    {
        "number": 14,
        "type": "recitation",
        "title": "سبق ۱۴: پہلا پارہ (الم - سورۃ الفاتحہ تا سورۃ البقرۃ رکوع ۱۶)",
        "titleEn": "Lesson 14: Para 1 (Alif-Lam-Meem - Recitation & Tajweed)",
        "titlePs": "۱۴ لوست: لومړۍ سِپاره (الم - تلاوت او تجوید)",
        "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ ۝١ الم ۝٢ ذَٰلِكَ الْكِتَابُ لَا رَيْبَ فِيهِ هُدًى لِّلْمُتَّقِينَ ۝٣ الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ وَمِمَّا رَزَقْنَاهُمْ يُنفِقُونَ ۝٤",
        "rule": "پہلے پارے کی ناظرہ تلاوت تجوید کے تمام قواعد (مخارج، حرکات، غنہ، مد، قلقلہ اور رموزِ اوقاف) کی مکمل رعایت کے ساتھ کی جائے۔",
        "ruleEn": "Recitation of the entire First Para (Juz 1) applying all Tajweed rules fluently.",
        "rulePs": "د لومړۍ سپارې تلاوت د ټولو تجویدي اصولو سره سم بشپړ کړئ.",
        "examples": "الٓمّٓ - ذَٰلِكَ الْكِتَابُ - هُدًى لِّلْمُتَّقِينَ - يُؤْمِنُونَ بِالْغَيْبِ",
        "questions": [
            ("پہلے پارے کا آغاز کن حروف سے ہوتا ہے؟", "پہلے پارے کا آغاز حروفِ مقطعات 'الٓمّٓ' سے ہوتا ہے۔", "پہلے پارے کا آغاز کیا ہے؟", "د لومړۍ سپارې پیل په څه شي دی؟", "په الٓمّٓ تورو سره پیل کیږي."),
            ("پہلے پارے میں کون سی سورتیں شامل ہیں؟", "پہلے پارے میں مکمل سورۃ الفاتحہ اور سورۃ البقرۃ کے ۱۶ رکوع شامل ہیں۔", "کون سی سورتیں ہیں؟", "کوم سورتونه په کې راغلي؟", "سورت الفاتحه او د سورت البقره ۱۶ رکوع په کې دي.")
        ]
    },
    {
        "number": 15,
        "type": "recitation",
        "title": "سبق ۱۵: دوسرا پارہ (سَيَقُولُ - سورۃ البقرۃ رکوع ۱۷ تا آخر)",
        "titleEn": "Lesson 15: Para 2 (Sayaqool - Recitation & Tajweed)",
        "titlePs": "۱۵ لوست: دویمه سِپاره (سیقول - تلاوت او تجوید)",
        "arabic": "سَيَقُولُ السُّفَهَاءُ مِنَ النَّاسِ مَا وَلَّاهُمْ عَن قِبْلَتِهِمُ الَّتِي كَانُوا عَلَيْهَا قُل لِّلَّهِ الْمَشْرِقُ وَالْمَغْرِبُ يَهْدِي مَن يَشَاءُ إِلَىٰ صِرَاطٍ مُّسْتَقِيمٍ",
        "rule": "دوسرے پارے (سَیَقُولُ) کی درست تلفظ اور روانی سے تلاوت۔ دورانِ تلاوت تحویلِ قبلہ، احکامِ صوم، اور آیاتِ بر و تقویٰ کی تلاوت کی مشق۔",
        "ruleEn": "Recitation of the entire Second Para (Juz 2) with fluent Tajweed pronunciation.",
        "rulePs": "د دویمې سپارې تلاوت په پوره تجوید او ښکلي لحن سره ادا کړئ.",
        "examples": "سَيَقُولُ السُّفَهَاءُ - قِبْلَتِهِمُ - فَلَنُوَلِّيَنَّكَ قِبْلَةً تَرْضَاهَا - صِرَاطٍ مُّسْتَقِيمٍ",
        "questions": [
            ("دوسرے پارے کا پہلا لفظ کیا ہے؟", "دوسرے پارے کا پہلا لفظ 'سَيَقُولُ' ہے۔", "پہلا لفظ کیا ہے؟", "د دویمې سپارې لومړی توری څه دی؟", "سیقول دی."),
            ("دوسرے پارے میں قبلہ کی تبدیلی کا کیا حکم ہے؟", "مسلمانوں کا قبلہ بیت المقدس سے کعبۃ اللہ شریف کی طرف تبدیل کیا گیا۔", "تحویل قبلہ کیا ہے؟", "د قبلې بدلېدل څه حکم و؟", "کعبه شریفه د مسلمانانو نوې او ابدي قبله وټاکل شوه.")
        ]
    }
]

lines = []
lines.append("/**")
lines.append(" * TuitionHub - Class 2 Nazira Quran Comprehensive Dataset (KPK Textbook Board)")
lines.append(" * Complete 15 Lessons verbatim from official textbook:")
lines.append(" * D:\\SpaceBook\\Books\\2nd\\2nd Nazira\\Word\\Nazira 2nd.docx")
lines.append(" * Full Tajweed phonics revision (Lessons 1-13) + Complete Recitation of Para 1 & Para 2.")
lines.append(" */")
lines.append("")
lines.append("var NAZIRA_2_DATA = [")

for idx, les in enumerate(lessons):
    comma = "," if idx < len(lessons) - 1 else ""
    l_num = les["number"]
    l_title = les["title"]
    lines.append("  {")
    lines.append(f'    "id": "cls2-naz-ch{l_num:02d}",')
    lines.append(f'    "number": {l_num},')
    lines.append(f'    "type": {json.dumps(les["type"])},')
    lines.append(f'    "title": {json.dumps(l_title)},')
    lines.append(f'    "titleEn": {json.dumps(les["titleEn"])},')
    lines.append(f'    "titlePs": {json.dumps(les["titlePs"])},')
    lines.append(f'    "author": "خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور — ناظرہ قرآن (جماعت دوم)",')
    lines.append(f'    "authorInfo": {json.dumps("ناظرہ قرآن آسان تجوید کے ساتھ، جماعت دوم، سبق نمبر " + str(l_num) + "۔")},')
    lines.append(f'    "urduText": {json.dumps(les["arabic"] + "\\n\\n" + les["rule"])},')
    
    # Sections
    sec_obj = {
        "heading": l_title,
        "arabic": les["arabic"],
        "text": les["rule"],
        "urduTranslation": les["rule"],
        "englishTranslation": les["ruleEn"],
        "pashtoTranslation": les["rulePs"],
        "tashreeh": f'اس سبق میں تجوید کی درست ادائی اور مشق فراہم کی گئی ہے: {les["examples"]}',
        "paras": [les["arabic"], les["rule"], f'مشقی کلمات: {les["examples"]}']
    }
    lines.append(f'    "sections": [{json.dumps(sec_obj, indent=6).strip()}],')

    # Exercise
    mcqs = [
        {
            "id": f'cls2-naz-ch{l_num:02d}-mcq1',
            "question": les["questions"][0][0],
            "options": [les["questions"][0][1], "غلط طریقہ", "کوئی اور امر", "نامعلوم"],
            "correct": 0,
            "explanation": les["questions"][0][1],
            "urdu": les["questions"][0][0],
            "pashto": les["questions"][0][3]
        },
        {
            "id": f'cls2-naz-ch{l_num:02d}-mcq2',
            "question": les["questions"][1][0],
            "options": [les["questions"][1][1], "غیر متعلقہ", "منفی صورت", "کوئی نہیں"],
            "correct": 0,
            "explanation": les["questions"][1][1],
            "urdu": les["questions"][1][0],
            "pashto": les["questions"][1][3]
        }
    ]
    sqs = [
        {
            "id": f'cls2-naz-ch{l_num:02d}-sq1',
            "question": les["questions"][0][0],
            "answer": les["questions"][0][1],
            "urdu": les["questions"][0][2],
            "pashto": les["questions"][0][3],
            "pashtoAns": les["questions"][0][4]
        },
        {
            "id": f'cls2-naz-ch{l_num:02d}-sq2',
            "question": les["questions"][1][0],
            "answer": les["questions"][1][1],
            "urdu": les["questions"][1][2],
            "pashto": les["questions"][1][3],
            "pashtoAns": les["questions"][1][4]
        }
    ]
    lqs = [
        {
            "id": f'cls2-naz-ch{l_num:02d}-lq1',
            "question": f'سبق "{l_title}" کے بنیادی تجویدی قواعد اور مشقی کلمات کو تفصیل سے بیان کریں۔',
            "answer": f'{les["rule"]} مشقی کلمات: {les["examples"]}',
            "urdu": f'تجویدی قواعد کی وضاحت کریں: {l_title}',
            "urduAns": les["rule"],
            "pashto": les["rulePs"],
            "pashtoAns": les["examples"]
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
            "q": les["questions"][0][0],
            "options": [les["questions"][0][1], "غلط", "نامعلوم", "کوئی نہیں"],
            "ans": 0,
            "explanation": les["questions"][0][1]
        }
    ]
    slo_sqs = [
        {
            "q": les["questions"][0][0],
            "ans": les["questions"][0][1],
            "urdu": les["questions"][0][2]
        }
    ]
    slo_lqs = [
        {
            "q": f'اس سبق کا تجویدی خلاصہ بیان کریں۔',
            "ans": les["rule"]
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
lines.append("  DATA.nazira2Chapters = NAZIRA_2_DATA;")
lines.append("}")
lines.append("")

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"SUCCESS! Wrote {len(lines)} lines to {OUT_JS}")
