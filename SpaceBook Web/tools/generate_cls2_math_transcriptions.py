# -*- coding: utf-8 -*-
"""generate_cls2_math_transcriptions.py
Generates the 167 page-by-page DSL transcription files for Class 2 Mathematics (KPTBB SNC 2020)
from D:\SpaceBook\Books\2nd\2nd Maths\Word\Maths 2nd.docx and Math Book for 2 class KPTBB.pdf.
Output: docs/source-verification/class-2/math/pages/p000.txt to p166.txt
"""
import docx
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'docs' / 'source-verification' / 'class-2' / 'tools'))
import figs2

PAGES_DIR = Path(r"D:\SpaceBook\SpaceBook Web\docs\source-verification\class-2\math\pages")
PAGES_DIR.mkdir(parents=True, exist_ok=True)

DOCX_PATH = r"D:\SpaceBook\Books\2nd\2nd Maths\Word\Maths 2nd.docx"
doc = docx.Document(DOCX_PATH)
paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
print(f"Loaded {len(paras)} non-empty paragraphs from Maths 2nd docx.")

# Unit metadata
UNITS = {
    1: ("Whole Numbers", "کامل اعداد", "بشپړ عددونه", 1, 28),
    2: ("Number Operations", "اعداد کے عمل", "د عددونو عملیې", 29, 93),
    3: ("Fractions", "کسور", "کسرونه", 94, 107),
    4: ("Measurement: Length, Mass and Capacity", "پیمائش: لمبائی، کمیت اور گنجائش", "اندازه: اوږدوالی، کتله او ظرفیت", 108, 127),
    5: ("Time", "وقت", "وخت", 128, 140),
    6: ("Geometry", "جیومیٹری", "هندسه", 141, 158),
}

# Generate front-matter (pages 0-5, PDF pages 1-6)
# Page 0 (PDF 1) - Front Cover
(PAGES_DIR / "p000.txt").write_text("""@status front-matter
@deco Cover illustration: colourful textbook cover with cheerful primary students and mathematical symbols.
# Mathematics 2 || ریاضی 2 || ریاضي 2
p Textbook of Mathematics for Class 2 based on Single National Curriculum 2020. || یکساں قومی نصاب 2020 پر مبنی جماعت دوم کی درسی کتاب ریاضی۔ || د 2020 یو شان ملي نصاب پر بنسټ د دویم ټولګي درسي کتاب ریاضي.
p Free from Government - Not for Sale. || حکومت کی طرف سے مفت - برائے فروخت نہیں۔ || د حکومت لخوا وړیا - د پلورلو لپاره نه دی.
p Khyber Pakhtunkhwa Textbook Board, Peshawar. || خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.
""", encoding='utf-8')

# Page 1 (PDF 2) - Advertisement / Awaz e Inqilab
(PAGES_DIR / "p001.txt").write_text("""@status front-matter
p Educational Notes and Textbook Distribution Notice. || تعلیمی نوٹس اور درسی کتب کی فراہمی۔ || ښوونیز نوټونه او د درسي کتابونو خبرتیا.
p Download PDF MCQs, Books and Notes for all primary, middle, and secondary levels. || تمام درجات کے لیے پی ڈی ایف کتابیں اور نوٹس۔ || د ټولو ټولګیو لپاره پی ډي ایف کتابونه او نوټونه.
""", encoding='utf-8')

# Page 2 (PDF 3) - Title Page
(PAGES_DIR / "p002.txt").write_text("""@status front-matter
# MATHEMATICS 2 || ریاضی 2 || ریاضي 2
p Based on Curriculum 2020. Approved by Directorate of Curriculum & Teacher Education (DCTE) Khyber Pakhtunkhwa. || نصاب 2020 پر مبنی۔ ڈائریکٹوریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن (DCTE) خیبر پختونخوا سے منظور شدہ۔ || د 2020 نصاب پر بنسټ د خیبر پښتونخوا د نصاب او ښوونکو روزنې ریاست لخوا تایید شوی.
p Khyber Pakhtunkhwa Textbook Board, Peshawar. || خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔ || د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.
""", encoding='utf-8')

# Page 3 (PDF 4) - Quranic Verses
(PAGES_DIR / "p003.txt").write_text("""@status front-matter
# Quranic Guidance || ارشاداتِ قرآنی || قرآني لارښوونې
p The believers are but brothers, so make settlement between your brothers. And fear Allah that you may receive mercy. (Surah Al-Hujurat: 10) || مومن تو آپس میں بھائی بھائی ہیں، پس اپنے دو بھائیوں کے درمیان صلح کراؤ اور اللہ سے ڈرو تاکہ تم پر رحم کیا جائے۔ (سورۃ الحجرات: 10) || مومنان خو په خپلو کې سره وروڼه دي، نو د خپلو وروڼو ترمنځ سوله وکړئ او له الله څخه ووېرېږئ څو پر تاسو رحم وشي. (سورت الحجرات: 10)
p O you who have believed, eat from the good things which We have provided for you and be grateful to Allah. (Surah Al-Baqarah: 172) || اے ایمان والو! ان پاکیزہ چیزوں میں سے کھاؤ جو ہم نے تم کو دی ہیں اور اللہ کا شکر ادا کرو۔ (سورۃ البقرہ: 172) || اې هغو کسانو چې ایمان مو راوړی دی! له هغو پاکو شیانو څخه وخورئ چې موږ تاسو ته درکړي دي او د الله شکر وباسئ. (سورت البقره: 172)
""", encoding='utf-8')

# Page 4 (PDF 5) - NOC and Credits
(PAGES_DIR / "p004.txt").write_text("""@status front-matter
# Textbook Approval and Editorial Board || درسی کتاب کی منظوری اور ادارتی بورڈ || د درسي کتاب تایید او ادبي بورډ
p This book is based on Curriculum 2020 and has been approved by DCTE Abbottabad vide NOC No. 1518-20/G-04/CTR/Maths-II Dated: 12-03-2021. || یہ کتاب نصاب 2020 کے تحت منظور شدہ ہے (این او سی مورخہ 12-03-2021)۔ || دا کتاب د 2020 نصاب له مخې تایید شوی دی.
- Author: Khalil Ahmad || مصنف: خلیل احمد || لیکوال: خلیل احمد
- Review Supervision: Gohar Ali Khan, Director DCTE Abbottabad || نگران: گوہر علی خان || څارونکی: ګوهر علي خان
- Focal Person: Zulfiqar Khan, Additional Director DCTE Abbottabad || فوکل پرسن: ذوالفقار خان || فوکل پرسن: ذوالفقار خان
- Subject Specialist (Maths): Dr. Badeya Danish || سبجیکٹ اسپیشلسٹ: ڈاکٹر بادیہ دانش || د مضمون متخصصه: ډاکټره بادیه دانش
""", encoding='utf-8')

# Page 5 (PDF 6) - Table of Contents
(PAGES_DIR / "p005.txt").write_text("""@status front-matter
# Table of Contents || فہرست مضامین || د مطالبو لړلیک
- Unit 1: Whole Numbers (Pages 1–28) || باب 1: کامل اعداد (صفحات 1 تا 28) || لومړی څپرکی: بشپړ عددونه (پاڼې 1–28)
- Unit 2: Number Operations (Pages 29–93) || باب 2: اعداد کے عمل (صفحات 29 تا 93) || دویم څپرکی: د عددونو عملیې (پاڼې 29–93)
-- Addition (Pages 29–46) || جمع (صفحات 29 تا 46) || جمع (پاڼې 29–46)
-- Subtraction (Pages 47–62) || تفریق (صفحات 47 تا 62) || منفي کول (پاڼې 47–62)
-- Multiplication (Pages 63–81) || ضرب (صفحات 63 تا 81) || ضرب (پاڼې 63–81)
-- Division (Pages 82–93) || تقسیم (صفحات 82 تا 93) || وېش (پاڼې 82–93)
- Unit 3: Fractions (Pages 94–107) || باب 3: کسر (صفحات 94 تا 107) || درېیم څپرکی: کسرونه (پاڼې 94–107)
- Unit 4: Measurement: Length, Mass and Capacity (Pages 108–127) || باب 4: پیمائش (صفحات 108 تا 127) || څلورم څپرکی: اندازه (پاڼې 108–127)
- Unit 5: Time (Pages 128–140) || باب 5: وقت (صفحات 128 تا 140) || پنځم څپرکی: وخت (پاڼې 128–140)
- Unit 6: Geometry (Pages 141–158) || باب 6: جیومیٹری (صفحات 141 تا 158) || شپږم څپرکی: هندسه (پاڼې 141–158)
- Answers to Exercises (Pages 159–160) || جوابات مشقیں (صفحات 159 تا 160) || د تمرینونو ځوابونه (پاڼې 159–160)
""", encoding='utf-8')

print("Generated front matter pages p000 to p005.")
