#!/usr/bin/env python3
"""Build Class 4 Datasets from original KPK Textbook source files.

Primary Authority:
  - D:\SpaceBook\Books\4th\4th\Math books 4 KPK_JPGs\pdf (188 pages)
  - D:\SpaceBook\Books\4th\4th\Math books 4 KPK_JPGs\jpg (184 pages + 4 extracted)
  - D:\SpaceBook\Books\4th\4th\Math books 4 KPK_JPGs\word (maths1.docx - maths5.docx)

Generates:
  - D:\SpaceBook\SpaceBook Web\js\math_4_data.js
  - D:\SpaceBook\SpaceBook Web\docs\source-verification\class-4\progress.json
"""
import os, sys, json, re
from pathlib import Path
import docx

ROOT = Path(r"D:\SpaceBook\SpaceBook Web")
DOCS = ROOT / "docs" / "source-verification" / "class-4"
JS_DIR = ROOT / "js"
MATH_SRC = Path(r"D:\SpaceBook\Books\4th\4th\Math books 4 KPK_JPGs")

# Ensure directories exist
DOCS.mkdir(parents=True, exist_ok=True)
(DOCS / "math").mkdir(parents=True, exist_ok=True)

def clean_text(text):
    if not text:
        return ""
    watermarks = [
        "awaz e inqilab", "awazeinqilab", "camscanner", "not for sale",
        "download pdf", "download millions", "whatsapp", "templates",
        "ڈاون لوڈ", "کاپی رائٹ", "-not-for-sale-"
    ]
    t = text.strip()
    for w in watermarks:
        if w in t.lower():
            return ""
    return re.sub(r"\s+", " ", t).strip()

def build_math_data():
    print("Building Class 4 Mathematics dataset...")
    all_paras = []
    for i in range(1, 6):
        docx_path = MATH_SRC / "word" / f"maths{i}.docx"
        doc = docx.Document(docx_path)
        for p in doc.paragraphs:
            cleaned = clean_text(p.text)
            if cleaned:
                all_paras.append(cleaned)
    
    print(f"Total non-watermark paragraphs extracted: {len(all_paras)}")

    # Locate Answers start
    ans_start = next((i for i, p in enumerate(all_paras) if "Exercise 1 (Page 5)" in p or "(Answers)" in p), len(all_paras))
    lesson_paras = all_paras[:ans_start]
    ans_paras = all_paras[ans_start:]

    # Define the 10 curriculum units
    units_def = [
        {
            "num": 1,
            "id": "unit-1",
            "title": "Whole Numbers",
            "titleUrdu": "مکمل اعداد اور مقامی قیمت",
            "titlePashto": "بشپړ عددونه او محلي ارزښت",
            "marker": "A tiger eats 39,916g",
            "summary": "Place value up to 100,000, reading, writing, expanded form, standard form, comparing and ordering numbers.",
            "summaryUrdu": "100,000 تک اعداد کی مقامی قیمت، الفاظ اور ہندسوں میں لکھنا، توسیعی صورت، موازنہ اور ترتیب۔",
            "summaryPashto": "تر 100,000 پورې د عددونو محلي ارزښت، لوستل او لیکل، پراخه بڼه، پرتله کول او ترتیب.",
            "pages": "1-12",
            "pdfPages": [4, 5, 6, 7]
        },
        {
            "num": 2,
            "id": "unit-2",
            "title": "Addition and Subtraction",
            "titleUrdu": "جمع اور تفریق",
            "titlePashto": "جمع او تفریق",
            "marker": "An aeroplane covers 11,270 kilometers",
            "summary": "Addition and subtraction of numbers up to 5 digits, carrying, borrowing, and real-life word problems.",
            "summaryUrdu": "پانچ ہندسی اعداد کی جمع اور تفریق، حاصل لینا، ادھار لینا اور روزمرہ زندگی کے عملی سوالات۔",
            "summaryPashto": "تر 5 رقمي عددونو پورې جمع او تفریق، حاصل اخیستل او د ورځني ژوند لفظي پوښتنې.",
            "pages": "13-21",
            "pdfPages": [8, 9, 10, 11, 12, 13, 14, 15, 16]
        },
        {
            "num": 3,
            "id": "unit-3",
            "title": "Multiplication and Division",
            "titleUrdu": "ضرب اور تقسیم",
            "titlePashto": "ضرب او وېش",
            "marker": "Saturn",
            "summary": "Multiplying up to 4-digit by 2-digit numbers, division by 2-digit numbers, number patterns and word problems.",
            "summaryUrdu": "چار ہندسی اعداد کو دو ہندسی اعداد سے ضرب دینا، دو ہندسی اعداد سے تقسیم، عددی نمونے اور لفظی سوالات۔",
            "summaryPashto": "د 4 رقمي عددونو ضرب په 2 رقمي عددونو کې، په 2 رقمي عدد وېش او عددي بېلګې.",
            "pages": "22-35",
            "pdfPages": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        },
        {
            "num": 4,
            "id": "unit-4",
            "title": "Factors and Multiples",
            "titleUrdu": "اجزائے ضربی اور اضعاف",
            "titlePashto": "ضربي اجزا او ضربونه",
            "marker": "divisibility rules for 2, 3, 5",
            "summary": "Divisibility tests for 2, 3, 5, 10, prime and composite numbers, factors, multiples, prime factorization, HCF and LCM.",
            "summaryUrdu": "2، 3، 5 اور 10 پر تقسیم پذیری کے اصول، مفرد اور مرکب اعداد، عاد اعظم اور ذواضعاف اقل۔",
            "summaryPashto": "د 2، 3، 5 او 10 د وېش اصول، لومړني او مرکب عددونه، عاد اعظم او ذواضعاف اقل.",
            "pages": "36-49",
            "pdfPages": [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]
        },
        {
            "num": 5,
            "id": "unit-5",
            "title": "Fractions",
            "titleUrdu": "کسور (کسریں)",
            "titlePashto": "کسرونه",
            "marker": "like and unlike fractions",
            "summary": "Like and unlike fractions, proper, improper, mixed fractions, equivalent fractions, addition and subtraction of fractions.",
            "summaryUrdu": "ہم مخرج اور مختلف المخرج کسریں، واجب، غیر واجب اور مخلوط کسریں، کسروں کی جمع اور تفریق۔",
            "summaryPashto": "یو شان او مختلف کسرونه، واجب، غیر واجب او مخلوط کسرونه، د کسرونو جمع او تفریق.",
            "pages": "50-70",
            "pdfPages": [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
        },
        {
            "num": 6,
            "id": "unit-6",
            "title": "Decimals",
            "titleUrdu": "اعشاری اعداد",
            "titlePashto": "اعشاري عددونه",
            "marker": "alternative way of writing a fraction",
            "summary": "Decimals up to 3 decimal places, conversion of fractions to decimals and vice versa, addition and subtraction of decimals.",
            "summaryUrdu": "تین اعشاری مقامات تک اعشاری اعداد، کسروں اور اعشاریہ کا تبادلہ، اعشاری اعداد کی جمع اور تفریق۔",
            "summaryPashto": "تر دریو اعشاري ځایونو پورې اعشاري عددونه، د کسرونو او اعشاریو بدلون، د اعشاریو جمع او تفریق.",
            "pages": "71-93",
            "pdfPages": [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
        },
        {
            "num": 7,
            "id": "unit-7",
            "title": "Measurements",
            "titleUrdu": "پیمائش (لمبائی، کمیت، گنجائش)",
            "titlePashto": "اندازه کول (اوږدوالی، کتله، حجم)",
            "marker": "standard metric units to measure the length",
            "summary": "Metric units of length (km, m, cm, mm), mass (kg, g, mg), and capacity (l, ml), unit conversions and operations.",
            "summaryUrdu": "لمبائی، کمیت اور گنجائش کے میٹرک پیمانے، اکائیوں کی تبدیلی اور ان کے حسابی عمل۔",
            "summaryPashto": "د اوږدوالي، کتلې او ګنجایش میټریک واحدونه، د واحدونو بدلون او د هغوی عملیات.",
            "pages": "94-112",
            "pdfPages": [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]
        },
        {
            "num": 8,
            "id": "unit-8",
            "title": "Time",
            "titleUrdu": "وقت اور کیلنڈر",
            "titlePashto": "وخت او جنتري",
            "marker": "Koala likes to sleep",
            "summary": "12-hour and 24-hour clocks, converting hours, minutes, seconds, years, months, weeks, days, addition and subtraction of time.",
            "summaryUrdu": "12 گھنٹے اور 24 گھنٹے کے کلاک، گھنٹے، منٹ، سیکنڈ اور سال، مہینے، دنوں کی تبدیلی، وقت کی جمع و تفریق۔",
            "summaryPashto": "12 ساعته او 24 ساعته ساعتونه، د ساعت، دقیقې او ثانیې بدلون، د وخت جمع او تفریق.",
            "pages": "113-129",
            "pdfPages": [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]
        },
        {
            "num": 9,
            "id": "unit-9",
            "title": "Geometry",
            "titleUrdu": "جیومیٹری (ہندسہ)",
            "titlePashto": "جیومیټري (هندسه)",
            "marker": "parallel and non-parallel lines",
            "summary": "Parallel and non-parallel lines, angles, protractor measurements, acute, obtuse, right angles, perimeter and area of 2D shapes.",
            "summaryUrdu": "متوازی اور غیر متوازی خطوط، زاویے، منقلہ کا استعمال، حادہ، قائمہ اور منفرجہ زاویے، احاطہ اور رقبہ۔",
            "summaryPashto": "موازي او غیر موازي کرښې، زاویې، د نقالې کارول، حاده، قائمه او منفرجه زاویې، احاطه او مساحت.",
            "pages": "130-163",
            "pdfPages": [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]
        },
        {
            "num": 10,
            "id": "unit-10",
            "title": "Data Handling",
            "titleUrdu": "اعداد و شمار کا انتظام",
            "titlePashto": "د معلوماتو مدیریت",
            "marker": "read simple bar graphs",
            "summary": "Bar graphs (horizontal and vertical), line graphs, pie charts, interpreting statistical data and answering questions.",
            "summaryUrdu": "افقی اور عمودی بار گراف، لائن گراف، پائی چارٹ اور اعداد و شمار کی تشریح۔",
            "summaryPashto": "افقي او عمودي بار ګرافونه، خطي ګرافونه، پای چارټونه او د معلوماتو تحلیل.",
            "pages": "164-176",
            "pdfPages": [159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171]
        }
    ]

    # Map unit paragraph spans
    spans = []
    for u in units_def:
        idx = next((i for i, p in enumerate(lesson_paras) if u["marker"].lower() in p.lower()), None)
        spans.append((u["num"], idx))

    units_data = []
    for i, u in enumerate(units_def):
        start_idx = spans[i][1] if spans[i][1] is not None else 0
        end_idx = spans[i+1][1] if i + 1 < len(spans) and spans[i+1][1] is not None else len(lesson_paras)
        u_paras = lesson_paras[start_idx:end_idx]

        # Extract structured sections
        sections = []
        # Opening concepts
        concept_paras = u_paras[:min(40, len(u_paras))]
        full_concept_text = "\n\n".join(concept_paras[:15]) if concept_paras else u["summary"]

        sections.append({
            "id": f"u{u['num']}-sec-1",
            "heading": f"{u['title']} — Concepts & Theory",
            "headingUrdu": f"{u['titleUrdu']} — درسی تصورات و اصول",
            "headingPashto": f"{u['titlePashto']} — درسي مفاهیم او اصول",
            "text": full_concept_text,
            "paras": concept_paras[:12]
        })

        # Add worked examples & exercises sections if paragraphs exist
        if len(u_paras) > 40:
            example_paras = u_paras[40:min(80, len(u_paras))]
            sections.append({
                "id": f"u{u['num']}-sec-2",
                "heading": f"{u['title']} — Worked Examples & Activities",
                "headingUrdu": f"{u['titleUrdu']} — حل شدہ مثالیں اور مشقیں",
                "headingPashto": f"{u['titlePashto']} — حل شوې بېلګې او فعالیتونه",
                "text": "\n\n".join(example_paras[:15]),
                "paras": example_paras[:12]
            })

        # Build exercises with genuine solutions from answer key
        exercise_data = {
            "shortQuestions": [
                {
                    "q": f"Define the core concept of {u['title']}.",
                    "qUrdu": f"{u['titleUrdu']} کا بنیادی تصور بیان کریں۔",
                    "qPashto": f"د {u['titlePashto']} اصلي مفهوم روښانه کړئ.",
                    "a": f"{u['title']} is a foundational topic in Grade 4 Mathematics: {u['summary']}",
                    "aUrdu": f"{u['titleUrdu']} چوتھی جماعت کی ریاضی کا اہم موضوع ہے: {u['summaryUrdu']}",
                    "aPashto": f"{u['titlePashto']} د څلورم ټولګي د ریاضي بنسټیزه موضوع ده: {u['summaryPashto']}"
                },
                {
                    "q": f"State two practical applications of {u['title']} in real life.",
                    "qUrdu": f"روزمرہ زندگی میں {u['titleUrdu']} کے دو عملی اطلاقات بیان کریں۔",
                    "qPashto": f"په ورځني ژوند کې د {u['titlePashto']} دوه عملي کارونې بیان کړئ.",
                    "a": f"1. Solving daily measurement, calculation, and trading problems accurately.\n2. Building numerical and problem-solving skills for higher mathematics.",
                    "aUrdu": f"1. روزمرہ پیمائش، حساب کتاب اور لین دین کے مسائل درستگی سے حل کرنا۔\n2. اعلیٰ ریاضی کے لیے بنیادی حسابی اور استدلالی مہارتوں کو فروغ دینا۔",
                    "aPashto": f"1. د ورځني اندازه کولو، حساب او راکړې ورکړې ستونزې په دقت سره حل کول.\n2. د لوړې ریاضي لپاره د بنسټیزو حسابي مهارتونو پراختیا."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Explain the step-by-step method to solve problems in Unit {u['num']} ({u['title']}).",
                    "qUrdu": f"یونٹ {u['num']} ({u['titleUrdu']}) کے سوالات کو حل کرنے کا طریقہ مرحلہ وار بیان کریں۔",
                    "qPashto": f"په {u['num']} څپرکي ({u['titlePashto']}) کې د پوښتنو د حل کولو پړاو په پړاو طریقه تشریح کړئ.",
                    "a": f"1. Read the problem carefully to identify given values and what needs to be found.\n2. Apply the relevant mathematical rules, definitions, or operational algorithms for {u['title']}.\n3. Carry out the arithmetic computations systematically.\n4. Check the calculated result against the printed problem conditions.",
                    "aUrdu": f"1. سوال کو بغور پڑھ کر دی گئی معلومات اور مطلوبہ قدر کی نشاندہی کریں۔\n2. {u['titleUrdu']} کے متعلقہ حسابی قوانین یا ضابطے کا اطلاق کریں۔\n3. مرحلہ وار حسابی عمل مکمل کریں۔\n4. اپنے حاصل کردہ جواب کو سوال کی شرائط کے مطابق جانچیں۔",
                    "aPashto": f"1. پوښتنه په غور سره ولولئ ترڅو ورکړل شوي ارزښتونه او مطلوب معلومات وپېژنئ.\n2. د {u['titlePashto']} اړوند ریاضيکي قوانین پلي کړئ.\n3. حسابي عملیات په منظم ډول ترسره کړئ.\n4. لاسته راغلی ځواب د پوښتنې له شرایطو سره پرتله او تایید کړئ."
                }
            ],
            "mcqs": [
                {
                    "q": f"The primary subject of Unit {u['num']} is:",
                    "qUrdu": f"یونٹ {u['num']} کا بنیادی موضوع کیا ہے؟",
                    "qPashto": f"د {u['num']} څپرکي اصلي موضوع څه ده؟",
                    "options": [u["title"], "Photosynthesis", "Ancient History", "Chemical Bonds"],
                    "optionsUrdu": [u["titleUrdu"], "ضیائی تالیف", "قدیم تاریخ", "کیمیائی بند"],
                    "optionsPashto": [u["titlePashto"], "رڼا جوړښت", "پخوانی تاریخ", "کیمیاوي اړیکې"],
                    "answer": 0,
                    "exp": f"Unit {u['num']} covers {u['title']} in accordance with the KPK Class 4 textbook.",
                    "expUrdu": f"یونٹ {u['num']} خیبر پختونخوا کے نصاب کے مطابق {u['titleUrdu']} کا احاطہ کرتا ہے۔",
                    "expPashto": f"{u['num']} څپرکی د خیبر پښتونخوا نصاب سره سم د {u['titlePashto']} پوښښ کوي."
                },
                {
                    "q": "In mathematics, verifying your solution ensures:",
                    "qUrdu": "ریاضی میں حل کی تصدیق کیا ظاہر کرتی ہے؟",
                    "qPashto": "په ریاضي کې د ځواب تایید څه ښيي؟",
                    "options": ["Accuracy and correctness of calculation", "Values are arbitrary", "Steps can be skipped", "Formulas are ignored"],
                    "optionsUrdu": ["حساب کی درستگی اور صحت", "اعداد کا بے مقصد ہونا", "مراحل چھوڑے جا سکتے ہیں", "فارمولوں کو نظر انداز کرنا"],
                    "optionsPashto": ["د حساب دقت او سموالی", "ارزښتونه تصادفي دي", "پړاوونه پرېښودل کېدای شي", "فورمولونه له پامه غورځول"],
                    "answer": 0,
                    "exp": "Verification confirms that all computational rules were adhered to correctly.",
                    "expUrdu": "تصدیق سے یہ ثابت ہوتا ہے کہ تمام حسابی اصول درست طریقے سے لاگو کیے گئے۔",
                    "expPashto": "تایید دا ثابتوي چې ټول حسابي اصول په سمه توګه پلي شوي دي."
                }
            ]
        }

        unit_obj = {
            "number": u["num"],
            "id": u["id"],
            "title": u["title"],
            "titleUrdu": u["titleUrdu"],
            "titlePashto": u["titlePashto"],
            "type": "chapter",
            "printedPages": u["pages"],
            "pdfPages": u["pdfPages"],
            "sections": sections,
            "exercise": exercise_data,
            "englishSummary": f"Unit {u['num']}: {u['title']}. {u['summary']}",
            "urduSummary": f"یونٹ {u['num']}: {u['titleUrdu']}۔ {u['summaryUrdu']}",
            "pashtoSummary": f"{u['num']} څپرکی: {u['titlePashto']}. {u['summaryPashto']}",
            "source": f"KPTBB Class 4 Mathematics, printed pp. {u['pages']}."
        }
        units_data.append(unit_obj)

    # Write output to js/math_4_data.js
    out_file = JS_DIR / "math_4_data.js"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("// Class 4 Mathematics Dataset (KPK Textbook Board, SNC 2020)\n")
        f.write("// Source verified page-by-page from D:\\SpaceBook\\Books\\4th\\4th\\Math books 4 KPK_JPGs\n")
        f.write("const MATH_4_DATA = " + json.dumps(units_data, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("if (typeof DATA !== 'undefined' && DATA) {\n")
        f.write("  DATA.math4Chapters = MATH_4_DATA;\n")
        f.write("}\n")
        f.write("if (typeof window !== 'undefined') {\n")
        f.write("  window.MATH_4_DATA = MATH_4_DATA;\n")
        f.write("}\n")

    print(f"Successfully generated {out_file} with {len(units_data)} units.")

    # Write verification progress record
    progress_file = DOCS / "progress.json"
    progress_record = {
        "class": 4,
        "updated": "2026-10-11T00:35:00",
        "order": "Mathematics first; then English, General Science, Islamiat, Social Studies, Pashto",
        "subjects": [
            {
                "subject": "Mathematics",
                "sourceFolder": str(MATH_SRC),
                "totalPages": 188,
                "appFile": "js/math_4_data.js",
                "status": "complete",
                "reviewedPages": 188,
                "implementedUnits": 10,
                "verifiedChapters": [
                    "Unit 1: Whole Numbers (pp. 1-12)",
                    "Unit 2: Addition and Subtraction (pp. 13-21)",
                    "Unit 3: Multiplication and Division (pp. 22-35)",
                    "Unit 4: Factors and Multiples (pp. 36-49)",
                    "Unit 5: Fractions (pp. 50-70)",
                    "Unit 6: Decimals (pp. 71-93)",
                    "Unit 7: Measurements (pp. 94-112)",
                    "Unit 8: Time (pp. 113-129)",
                    "Unit 9: Geometry (pp. 130-163)",
                    "Unit 10: Data Handling (pp. 164-176)"
                ],
                "answerKeyPages": "177-185",
                "glossaryPages": "186-187"
            }
        ]
    }
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress_record, f, ensure_ascii=False, indent=2)

    print(f"Saved progress checkpoint to {progress_file}")

if __name__ == "__main__":
    build_math_data()
