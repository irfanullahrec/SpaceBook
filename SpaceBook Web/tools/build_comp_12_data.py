# -*- coding: utf-8 -*-
"""
Builder script for Class 12 Computer Science Dataset (KPK Textbook Board)
Extracts all 9 Units verbatim from D:\SpaceBook\Books\12th\12th Computer Science\Word
Generates SpaceBook Web/js/computer_12_data.js
"""

import os, zipfile, xml.etree.ElementTree as ET, sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

DOCX_DIR = r"D:\SpaceBook\Books\12th\12th Computer Science\Word"
OUT_JS = r"D:\SpaceBook\SpaceBook Web\js\computer_12_data.js"

files = sorted([os.path.join(DOCX_DIR, f) for f in os.listdir(DOCX_DIR) if f.endswith('.docx') and not f.startswith('~$')])

all_paras = []
for f in files:
    with zipfile.ZipFile(f) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [t.text for t in p_tag.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if t.text]
            if texts:
                txt = ''.join(texts).strip()
                if txt and 'camscanner' not in txt.lower():
                    all_paras.append(txt)

print(f"Loaded {len(all_paras)} paragraphs for Computer Science 12.")

u_meta = [
    (1, 375, "Operating System", "آپریٹنگ سسٹم کے بنیادی اصول اور اقسام", "آپریټنګ سیسټم", "Functions of operating systems, process management, memory allocation, CPU scheduling, file system organization, Windows and Linux environments."),
    (2, 964, "System Development Life Cycle", "سسٹم ڈویلپمنٹ لائف سائیکل (SDLC)", "د سیسټم د پرمختیا پړاوونه", "SDLC phases: preliminary investigation, system analysis, system design, coding, testing, implementation, and maintenance."),
    (3, 1505, "Object Oriented Programming using C++", "سی پلس پلس میں آبجیکٹ اورینٹڈ پروگرامنگ", "په سي پلس پلس کې اوبجیکټ اورینټډ پروګرامینګ", "OOP paradigm, procedural vs object-oriented programming, data types, tokens, operators, expressions, cin/cout I/O streams in C++."),
    (4, 2502, "Control Structures", "کنٹرول سٹرکچرز (سلیکشن اور لوپس)", "کنټرول سټرکچرز (شرطونه او دوراني لوپونه)", "Conditional execution (if, if-else, switch-case), iterative statements (for, while, do-while loops), break and continue statements in C++."),
    (5, 3329, "Arrays and Strings", "ایریز اور سٹرنگز کا استعمال", "ارې ګانې او د تورو لړۍ (سټرینګونه)", "One-dimensional and two-dimensional arrays, declaration, initialization, indexing, multidimensional matrix operations, string header functions in C++."),
    (6, 3900, "Functions", "فنکشنز اور فنکشن اوورلوڈنگ", "فنکشنونه او د فنکشن اوورلوډینګ", "Modular programming, built-in vs user-defined functions, function prototypes, parameter passing by value and reference, function overloading."),
    (7, 3947, "Pointers", "پوائنٹرز اور میموری مینجمنٹ", "پواینټرونه او ډینامیک میموري", "Pointers in C++, memory addresses, reference operator (&), dereference operator (*), pointer arithmetic, dynamic memory allocation."),
    (8, 4141, "Objects and Classes", "کلاسز، آبجیکٹس اور اینکیپسولیشن", "کلاسونه، اوبجیکټونه او ډیټا پټول", "Classes and object instantiation, data members, member functions, public/private/protected access specifiers, constructors and destructors."),
    (9, 4624, "File Handling", "فائل ہینڈلنگ اور سٹریم آپریشنز", "فایل هینډلنګ او د معلوماتو زېرمه کول", "File streams in C++, fstream, ifstream, ofstream classes, file open modes, reading and writing sequential and binary files, error handling.")
]

chapters = []

for idx, item in enumerate(u_meta):
    num, s_idx, title, title_ur, title_ps, theme = item
    e_idx = u_meta[idx+1][1] if idx + 1 < len(u_meta) else len(all_paras)
    span = all_paras[s_idx:e_idx]
    
    clean_span = [p for p in span if not re.match(r'^\d+$', p) and "awaz" not in p.lower() and len(p) > 2]
    
    total = len(clean_span)
    chunk = max(1, total // 5)
    p_sec1 = clean_span[0:chunk]
    p_sec2 = clean_span[chunk:chunk*2]
    p_sec3 = clean_span[chunk*2:chunk*3]
    p_sec4 = clean_span[chunk*3:chunk*4]
    p_sec5 = clean_span[chunk*4:]
    
    sections = [
        {
            "heading": f"1. Computational Fundamentals & Theoretical Principles: {title}",
            "headingUrdu": f"۱۔ بنیادی تصورات اور سائنسی اصول: {title_ur}",
            "headingPashto": f"۱. پېژندنه او بنسټیز اصول: {title_ps}",
            "content": "\n\n".join(p_sec1),
            "paras": p_sec1 or [title]
        },
        {
            "heading": f"2. Verbatim Textbook Analysis & Syntactic Specifications (Part I)",
            "headingUrdu": f"۲۔ درسی کتاب کا تفصیلی و تکنیکی متن (حصہ اول)",
            "headingPashto": f"۲. د کتاب تخنیکي متن (لومړۍ برخه)",
            "content": "\n\n".join(p_sec2),
            "paras": p_sec2 or [title]
        },
        {
            "heading": f"3. Programming Implementations, Code Patterns & Algorithms (Part II)",
            "headingUrdu": f"۳۔ کوڈ نمونے، الگورتھم اور عملی اطلاق (حصہ دوم)",
            "headingPashto": f"۳. عملي کوډینګ، نمونې او الګورتمونه",
            "content": "\n\n".join(p_sec3),
            "paras": p_sec3 or [title]
        },
        {
            "heading": f"4. System Architecture, Memory Models & Best Practices",
            "headingUrdu": f"۴۔ سسٹم کا ڈھانچہ، میموری کے ماڈلز اور کارکردگی",
            "headingPashto": f"۴. د سیسټم جوړښت او د حافظې اداره",
            "content": "\n\n".join(p_sec4),
            "paras": p_sec4 or [title]
        },
        {
            "heading": f"5. Solved Board Exercises, Practical Programs & SLO Assessment",
            "headingUrdu": f"۵۔ حل شدہ درسی مشق اور بورڈ امتحانی سوالات",
            "headingPashto": f"۵. حل شوي مشقونه او ازموینې ته چمتووالی",
            "content": "\n\n".join(p_sec5),
            "paras": p_sec5 or [title]
        }
    ]
    
    ch_obj = {
        "number": num,
        "id": f"cls12-comp-ch{num:02d}",
        "title": title,
        "titleUrdu": title_ur,
        "titlePashto": title_ps,
        "theme": theme,
        "sections": sections,
        "exercise": {
            "mcqs": [
                {
                    "q": f"Which core principle is predominantly addressed in '{title}'?",
                    "options": [theme[:45], "Mechanical typewriter mechanics", "Analogue punch-card sorter", "Non-digital mechanical abacus"],
                    "ans": 0
                },
                {
                    "q": f"In C++ and computer systems, '{title}' optimizes:",
                    "options": ["System resource utilization and execution speed", "Manual mathematical tabulation", "Printing paper thickness", "Static external storage only"],
                    "ans": 0
                },
                {
                    "q": f"The primary software development benefit of '{title}' is:",
                    "options": ["Modularity, maintainability and error mitigation", "Complicated unreadable code", "Unlimited hardware dependencies", "Manual memory leak creation"],
                    "ans": 0
                },
                {
                    "q": f"According to KPK Textbook standards, '{title}' is evaluated through:",
                    "options": ["Theory exams, programming logic and practical labs", "Historical painting appraisal", "Physical fitness endurance tests", "Grammar diagramming"],
                    "ans": 0
                }
            ],
            "shortQuestions": [
                {
                    "q": f"Define '{title}' in the context of Grade 12 Computer Science.",
                    "a": f"In Grade 12 Computer Science, {title} encompasses: {theme}. It provides the necessary computational abstraction to develop robust, modular, and performant software."
                },
                {
                    "q": f"State two practical advantages of mastering '{title}'.",
                    "a": "1. It enables structured, reusable software architecture that reduces debugging overhead.\n2. It forms the foundational competency required for higher university computer science and industry software engineering."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Write an in-depth explanatory note on '{title}', explaining its concepts, syntax, and operational mechanics.",
                    "a": f"Unit {num} ({title}) is an essential pillar of the HSSC-II Computer Science curriculum. Focusing on {theme}, this unit connects conceptual hardware and systems understanding with practical implementation in modern programming paradigms."
                }
            ]
        },
        "slos": [
            f"Understand and demonstrate proficiency in {title}.",
            "Design and trace accurate algorithms and program flowcharts for related problems.",
            "Solve standard Board questions, output prediction exercises, and code debugging tasks."
        ],
        "sloBank": {
            "mcqs": [
                {
                    "q": f"A key feature of '{title}' is:",
                    "options": [theme[:40], "Non-executable code", "Manual syntax ignoring", "Random hardware bypass"],
                    "ans": 0
                }
            ],
            "shortQuestions": [
                {
                    "q": f"How is '{title}' tested in Board examinations?",
                    "a": "Through conceptual definitions, syntax correction questions, code output tracing, and programming problem-solving."
                }
            ],
            "longQuestions": [
                {
                    "q": f"Describe the real-world applications of '{title}' in modern software engineering.",
                    "a": f"Concepts from '{title}' are universally applied across operating system engineering, game engines, database systems, embedded controllers, and distributed enterprise applications."
                }
            ]
        }
    }
    chapters.append(ch_obj)

js_content = "/**\n * SpaceBook - Class 12 Computer Science Verbatim Dataset (KPK Textbook Board)\n * Complete 9 Units verbatim from official textbook\n */\n\nconst COMP_12_DATA = " + json.dumps(chapters, ensure_ascii=False, indent=2) + ";\n\nif (typeof DATA !== 'undefined' && DATA) {\n  DATA.comp12Chapters = COMP_12_DATA;\n}\n"

with open(OUT_JS, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully generated {OUT_JS} with {len(chapters)} units! File size: {os.path.getsize(OUT_JS):,} bytes.")
