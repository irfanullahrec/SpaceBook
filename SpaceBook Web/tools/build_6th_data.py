# Script to generate datasets for Class 6th all 13 subjects from D:\SpaceBook\Books\6th
import docx
import json
import os
import sys

base_dir = r"D:\SpaceBook\Books\6th"
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
        f.write(f"// Class 6 {var_name} Dataset (KPTBB)\n")
        f.write(f"const {var_name} = " + json.dumps(units_data, ensure_ascii=False, indent=2) + ";\n\n")
        f.write(f"if (typeof DATA !== 'undefined' && DATA) {{ DATA.{data_prop} = {var_name}; }}\n")
        f.write(f"if (typeof window !== 'undefined') {{ window.{var_name} = {var_name}; }}\n")
    print(f"Generated {filename} ({len(units_data)} units)")

# 1. MATHEMATICS (11 Units)
def build_math():
    folder = os.path.join(base_dir, "Math", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Multiples and Factors", "اضعاف اور اجزائے ضربی", "Divisibility tests, prime and composite numbers, prime factorization, HCF and LCM word problems."),
        (2, "Integers", "صحیح اعداد", "Positive and negative integers, representation on number line, ordering and comparing integers."),
        (3, "Laws of Integers and Order of Operations", "قوانین اور حسابی ترتیبات", "Addition, subtraction, multiplication and division of integers, BODMAS rule and brackets."),
        (4, "Rate, Ratio and Percentage", "شرح، نسبت اور فیصد", "Concept of ratio, simplest form, direct and inverse proportion, percentage conversions and profit/loss."),
        (5, "Sets", "سیٹس", "Definition of set, elements, descriptive, tabular and set-builder notations, finite, infinite and empty sets."),
        (6, "Algebraic Expressions", "الجبرائی جملے", "Variables, constants, algebraic terms, addition and subtraction of polynomials, like and unlike terms."),
        (7, "Linear Expressions and Equations", "یک درجی مساوات", "Linear equations in one variable, solution by balancing method and transposing, word problems."),
        (8, "Surface Area and Volume", "سطحی رقبہ اور حجم", "Cubes and cuboids, formula for total surface area, volume calculation and capacity units."),
        (9, "Lines, Angles and Symmetry", "خطوط، زاویے اور تشاکل", "Types of angles, complementary and supplementary angles, line of symmetry and rotational symmetry."),
        (10, "Geometrical Constructions", "ہندسی اشکال کی بناوٹ", "Construction of line segments, angle bisectors, perpendicular bisectors, and triangles using compass."),
        (11, "Data Management", "اعداد و شمار کا انتظام", "Collection of data, frequency distribution table, bar graphs, pie charts and mean calculations.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Comprehensive study of {title} in accordance with KPK Class 6 Mathematics syllabus."
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
                    {"q": f"Define the fundamental concept of {title}.", "a": f"{title} forms a foundational pillar of Grade 6 mathematics. It provides rules, computational methods, and logical operations for real-world mathematical problem solving: {summary}"},
                    {"q": f"State two important mathematical properties or formulas learned in Unit {num}.", "a": f"1. Standard definition and identification methods for {title}.\n2. Systematic calculation procedures and verification steps applied in textbook exercises."}
                ],
                "longQuestions": [
                    {"q": f"Explain step-by-step how to solve complex practical problems in {title}.", "a": f"To solve problems involving {title}, first extract the given values and required unknown, formulate the corresponding mathematical expression, execute the operations following standard algebraic or arithmetic rules, and verify the final result."}
                ],
                "mcqs": [
                    {"q": f"Which mathematical concept is primary in Unit {num} ({title})?", "options": [title, "Biological classification", "Historical dates", "Linguistic grammar"], "answer": 0, "exp": f"Unit {num} focuses specifically on {title}."},
                    {"q": "In mathematics, verification of a solution is achieved by:", "options": ["Substituting the solution back into the original equation", "Guessing an approximate number", "Ignoring given conditions", "Changing the problem statement"], "answer": 0, "exp": "Substituting the result back ensures that both sides of the mathematical statement remain equal."}
                ]
            },
            "englishSummary": f"Unit {num} covers {title}, including {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کا احاطہ کرتا ہے جس میں درسی تصورات، حل شدہ مثالیں اور مشقی سوالات شامل ہیں۔"
        }
        units.append(unit_obj)
    write_dataset_file("MATH_6_DATA", "math6Chapters", "math_6_data.js", units)

# 2. GENERAL SCIENCE (11 Units)
def build_science():
    folder = os.path.join(base_dir, "General science", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Cellular Organization", "خلوی تنظیم", "Plant and animal cells, microscope, cell organelles, tissues, organs and organ systems."),
        (2, "Reproduction in Plants", "پودوں میں تولید", "Parts of flower, pollination, fertilization, seed structure, germination and dispersal."),
        (3, "Balanced Diet", "متوازن غذا", "Carbohydrates, proteins, fats, vitamins, minerals, water, roughage and nutritional disorders."),
        (4, "Human Digestive System", "انسانی نظام انہضام", "Teeth, mouth, esophagus, stomach, small intestine, large intestine, liver and digestion process."),
        (5, "Matter as Particles", "مادہ کے ذرات", "Particle model of matter, states of matter (solids, liquids, gases), expansion and contraction."),
        (6, "Elements and Compounds", "عناصر اور مرکبات", "Chemical symbols, atomic structure, molecules, differences between elements and compounds."),
        (7, "Mixtures", "مخلوط", "Homogeneous and heterogeneous mixtures, solutions, suspensions, separation techniques: filtration, distillation, evaporation."),
        (8, "Energy", "توانائی اور اس کی اقسام", "Forms of energy, kinetic and potential energy, law of conservation of energy, renewable energy sources."),
        (9, "Electricity", "بجلی اور برقی سرکٹس", "Electric current, simple electric circuit, series and parallel circuits, conductors and insulators."),
        (10, "Magnetism and Electromagnetism", "مقناطیسیت اور برقی مقناطیسیت", "Poles of magnet, magnetic field, making an electromagnet, uses of electromagnets in technology."),
        (11, "Technology in Everyday Life", "روزمرہ زندگی میں ٹیکنالوجی", "Simple machines, levers, pulleys, wheel and axle, technological inventions improving human welfare.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Scientific concepts, textbook observations, and principles of {title} for Class 6."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Textbook Concepts & Scientific Principles",
                    "headingUrdu": "درسی سائنسی تصورات و اصول",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"Define {title} and explain its scientific significance.", "a": f"{title} is a core topic in General Science: {summary}"},
                    {"q": f"Name three main components or principles discussed in Unit {num}.", "a": f"1. Core physical and biological processes involved in {title}.\n2. Real-world observations and scientific experiments.\n3. Applications in daily life and technology."}
                ],
                "longQuestions": [
                    {"q": f"Describe the detailed mechanism and functions of {title} with reference to the human environment.", "a": f"{title} plays a pivotal role in natural processes and technological applications. In this unit, students explore empirical experiments, molecular or biological structures, and energy transformations that govern these phenomena."}
                ],
                "mcqs": [
                    {"q": f"What is the main subject matter of Unit {num}?", "options": [title, "Prehistoric archaeology", "Linguistic syntax", "Ancient numismatics"], "answer": 0, "exp": f"Unit {num} covers {title}."},
                    {"q": "Which of the following is an empirical characteristic of science?", "options": ["Systematic observation and experimentation", "Unquestioned assumption", "Superstition", "Random chance"], "answer": 0, "exp": "Science develops theories based on observable, verifiable and testable experimental evidence."}
                ]
            },
            "englishSummary": f"Unit {num} details {title}, covering {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کے سائنسی اصول، مشاہدات اور مشقی سوالات کی وضاحت کرتا ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("GENERAL_SCIENCE_6_DATA", "genSci6Chapters", "general_science_6_data.js", units)

# 3. COMPUTER EDUCATION (6 Units)
def build_computer():
    folder = os.path.join(base_dir, "Computer", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "ICT Fundamentals", "آئی سی ٹی کے بنیادی تصورات", "Hardware, software, input, output and storage devices, operating system basics and file management."),
        (2, "Digital Skills", "ڈیجیٹل مہارتیں اور ٹولز", "Word processing, document formatting, inserting tables and images, keyboard shortcuts and presentation basics."),
        (3, "Algorithmic Thinking & Problem Solving", "الگورتھمک سوچ اور مسئلہ کا حل", "Steps in problem solving, algorithm design, flowcharts, decision making and iterative thinking."),
        (4, "Visual Programming (Scratch)", "پروگرامنگ اور سکریچ", "Introduction to Scratch, sprites, blocks, events, motion, loops and creating interactive animations."),
        (5, "Digital Citizenship", "ڈیجیٹل شہریت اور اخلاقیات", "Internet safety, cyber ethics, privacy protection, passwords, netiquette and avoiding cyber threats."),
        (6, "Entrepreneurship in Digital Age", "ڈیجیٹل دور میں کاروبار کے مواقع", "How technology enables small businesses, freelancing basics, digital collaboration and innovation.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Computer science theory, practical applications, and hands-on skills in {title}."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Theory & Practical Computing Skills",
                    "headingUrdu": "نظریاتی و عملی کمپیوٹر مہارتیں",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"What is meant by {title} in modern computer education?", "a": f"{title} refers to {summary}"},
                    {"q": "State two key advantages of computing tools in education and daily life.", "a": "1. High processing speed and precision in calculations and document management.\n2. Effortless global communication and automated problem solving."}
                ],
                "longQuestions": [
                    {"q": f"Provide an in-depth explanation of {title} with practical computing examples.", "a": f"In {title}, users utilize digital tools and logical methods to execute tasks effectively. Understanding both hardware architecture and software logic enables students to become productive digital creators."}
                ],
                "mcqs": [
                    {"q": f"Which unit covers {title} in Class 6 Computer?", "options": [f"Unit {num}", "Unit 12", "Unit 20", "Unit 0"], "answer": 0, "exp": f"Unit {num} covers {title}."},
                    {"q": "Which computer device is primarily used to input textual data?", "options": ["Keyboard", "Monitor", "Printer", "Speaker"], "answer": 0, "exp": "The keyboard is the primary alphanumeric input peripheral."}
                ]
            },
            "englishSummary": f"Unit {num} provides conceptual and practical understanding of {title}: {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کی کمپیوٹر مہارتوں، مشقوں اور سوالات کی تفصیلی وضاحت کرتا ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("COMPUTER_6_DATA", "comp6Chapters", "computer_6_data.js", units)

# 4. GEOGRAPHY (4 Units)
def build_geography():
    folder = os.path.join(base_dir, "Geography", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Structure of Earth and Types of Rocks", "زمین کی ساخت اور چٹانوں کی اقسام", "Internal layers of Earth (crust, mantle, core), igneous, sedimentary and metamorphic rocks, rock cycle."),
        (2, "Mountains, Plateaus and Valleys", "پہاڑ، سطح مرتفع اور وادیاں", "Major landforms, fold, block and volcanic mountains, plateaus and valley formation, human life in highland regions."),
        (3, "Climatic Regions of the World", "دنیا کے موسمی خطے", "Equatorial, tropical, temperate, arid and polar climate zones, temperature, rainfall, natural vegetation and human adaptation."),
        (4, "Forests of the World", "دنیا کے جنگلات اور ماحولیات", "Tropical rainforests, coniferous forests, deciduous forests, deforestation causes and conservation of natural resources.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Geographical concepts, physical landforms, and human-environment interactions in {title}."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Geographical Concepts & Landform Analysis",
                    "headingUrdu": "جغرافیائی تصورات و خطوں کا جائزہ",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"Define {title} according to geographical principles.", "a": f"{title} examines the physical topography and environmental features of our planet: {summary}"},
                    {"q": f"Mention two major impacts of {title} on human society.", "a": "1. Direct influence on agricultural settlement, housing, and economic activities.\n2. Distribution of natural resources, water reserves, and climate conditions."}
                ],
                "longQuestions": [
                    {"q": f"Write a comprehensive geographical essay on {title}.", "a": f"{title} represents an integral element of the Earth's physical geography. Students analyze plate tectonics, weather systems, and vegetation distribution to understand environmental equilibrium and sustainable development."}
                ],
                "mcqs": [
                    {"q": f"What is the focus of Unit {num} in Class 6 Geography?", "options": [title, "Algebraic geometry", "Cell division", "Modern programming"], "answer": 0, "exp": f"Unit {num} covers {title}."},
                    {"q": "The outermost solid layer of the Earth is known as the:", "options": ["Crust", "Mantle", "Outer Core", "Inner Core"], "answer": 0, "exp": "The crust is the thin, solid outer shell of the Earth upon which life thrives."}
                ]
            },
            "englishSummary": f"Unit {num} explores {title}, highlighting {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کی جغرافیائی ساخت، خصوصیات اور درسی مشقوں پر مشتمل ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("GEOGRAPHY_6_DATA", "geo6Chapters", "geography_6_data.js", units)

# 5. HISTORY (5 Units)
def build_history():
    folder = os.path.join(base_dir, "History", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "The Ancient Civilizations", "قدیم تہذیبیں (وادی سندھ اور میسوپوٹیمیا)", "Indus Valley Civilization (Mohenjo-daro, Harappa), urban planning, trade, script, and decline of ancient settlements."),
        (2, "Ancient Heritage and Cultures", "قدیم ورثہ اور ثقافتیں", "Ancient Egyptian and Mesopotamian civilizations, pyramids, writing systems, laws of Hammurabi, and societal heritage."),
        (3, "Persians, Greeks and Romans", "ایرانی، یونانی اور رومی تہذیبیں", "Achaemenid Persian Empire, Alexander the Great's campaigns, Greek city-states, Roman republic and empire contributions to civilization."),
        (4, "Aryans, Kushans, and Guptas", "آریہ، کشان اور گپتا ادوار", "Aryan migration, Vedic culture, Gandhara civilization, Kushan empire and Buddhism, Gupta golden age in South Asia."),
        (5, "Rise of Islamic Civilization", "اسلامی تہذیب کا عروج اور اثرات", "Advent of Islam in Arabia, Khulafa-e-Rashideen, scientific discoveries, architecture, trade routes and global influence of Muslim scholars.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Historical analysis, archaeological records, and timeline of {title}."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Historical Accounts & Civilizational Heritage",
                    "headingUrdu": "تاریخی حالات و تہذیبی ورثہ",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"What was the historical importance of {title}?", "a": f"{title} contributed significantly to human progress: {summary}"},
                    {"q": "State two major archaeological or cultural contributions of ancient societies.", "a": "1. Planned cities with grid patterns, drainage systems, and granaries.\n2. Inventions of writing, legal codes, and monumental architecture."}
                ],
                "longQuestions": [
                    {"q": f"Discuss the emergence, flourishing, and legacy of {title} in world history.", "a": f"The historical epoch of {title} demonstrates the evolution of organized human societies. Through agriculture, trade, political administration, and cultural synthesis, these civilizations laid the groundwork for modern social and legal structures."}
                ],
                "mcqs": [
                    {"q": f"Which historic era is examined in Unit {num}?", "options": [title, "Industrial Revolution", "Space Exploration", "Atomic Age"], "answer": 0, "exp": f"Unit {num} investigates {title}."},
                    {"q": "Mohenjo-daro and Harappa are major archaeological sites of which civilization?", "options": ["Indus Valley Civilization", "Roman Empire", "Inca Empire", "Mayan Civilization"], "answer": 0, "exp": "They represent the bronze age Indus Valley Civilization in Pakistan."}
                ]
            },
            "englishSummary": f"Unit {num} covers {title}, exploring {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کی تاریخی اہمیت، واقعات اور سوالات کے مکمل جوابات فراہم کرتا ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("HISTORY_6_DATA", "hist6Chapters", "history_6_data.js", units)

# 6. ENGLISH (10 Units)
def build_english():
    folder = os.path.join(base_dir, "English", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Character and Moral Values", "کردار اور اخلاقی اقدار", "Honesty, integrity, respect for elders, empathy, building upright character through daily actions."),
        (2, "Environmental Awareness & Conservation", "ماحولیاتی تحفظ اور صفائی", "Preserving nature, planting trees, reducing plastic waste, clean water, and combating global warming."),
        (3, "Health, Nutrition and Fitness", "صحت، متوازن خوراک اور تندرستی", "Healthy lifestyle, balanced food plate, physical exercise, personal hygiene and staying disease-free."),
        (4, "Wonders of Nature", "قدرت کے شاہکار اور مناظر", "Beauty of nature, changing seasons, mountains, rivers, wildlife and poetic appreciation."),
        (5, "Scientific Inventions & Discoveries", "سائنسی ایجادات اور انسانیت", "Key inventions that changed human life, wheel to computers, curiosity and systematic inquiry."),
        (6, "Dignity of Labour & Professions", "محنت کی عظمت اور پیشے", "Respect for all lawful jobs, hard work, craftsmen, farmers, teachers and self-reliance."),
        (7, "Cultural Heritage of Pakistan", "پاکستان کا ثقافتی ورثہ", "Rich cultural traditions of Khyber Pakhtunkhwa and Pakistan, historical sites, folk music, crafts."),
        (8, "Peace, Tolerance and Harmony", "امن، رواداری اور باہمی ہم آہنگی", "Living in peace, respecting diverse communities, conflict resolution through polite dialogue."),
        (9, "Inspiring Stories and Parables", "سبق آموز کہانیاں اور نصیحتیں", "Moral tales, parables showing wisdom, overcoming challenges with patience and courage."),
        (10, "Modern Communication and Technology", "جدید مواصلات اور ٹیکنالوجی", "Evolution of internet, smart devices, responsible communication and digital media tools.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Reading text, vocabulary expansion, comprehension, and grammar rules for {title}."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Reading Passage & Comprehension",
                    "headingUrdu": "درسی عبارت و تفہیمِ متن",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"What is the central theme of Unit {num} ({title})?", "a": f"The central theme emphasizes {summary}"},
                    {"q": "What moral lesson does the reading passage teach?", "a": "It teaches students to cultivate disciplined habits, express kindness, respect lawful norms, and strive for self-improvement."}
                ],
                "longQuestions": [
                    {"q": f"Write a well-structured summary of the lesson '{title}'.", "a": f"In '{title}', the author illustrates how {summary} affects our individual growth and community well-being. By internalizing these values, young students learn to communicate effectively and act with moral conviction."}
                ],
                "mcqs": [
                    {"q": f"What is the main subject of Unit {num}?", "options": [title, "Advanced Calculus", "Organic Chemistry", "Nuclear Physics"], "answer": 0, "exp": f"Unit {num} focuses on {title}."},
                    {"q": "A word that shows an action or state of being is called a:", "options": ["Verb", "Noun", "Adverb", "Preposition"], "answer": 0, "exp": "A verb expresses physical action, mental action, or a state of being."}
                ]
            },
            "englishSummary": f"Unit {num} focuses on {title}: {summary}.",
            "urduSummary": f"یہ یونٹ {titleUr} کے درسی سبق، ذخیرہ الفاظ، گرامر اور مشقوں پر مشتمل ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("ENGLISH_6_DATA", "eng6Chapters", "english_6_data.js", units)

# 7. URDU (15 Lessons)
def build_urdu():
    folder = os.path.join(base_dir, "Urdu", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "حمد باری تعالیٰ", "حمد باری تعالیٰ", "اللہ تعالیٰ کی حمد و ثنا، کائنات کے حسن و نظام میں رب العزت کی قدرت کا مشاہدہ۔"),
        (2, "نعت رسول مقبول ﷺ", "نعت رسول مقبول ﷺ", "حضور خاتم النبیین ﷺ سے محبت و عقیدت، آپ ﷺ کی سیرتِ طیبہ اور روشن تعلیمات۔"),
        (3, "تاریخ کا ایک سنہرا باب", "تاریخ کا ایک سنہرا باب", "تحریک پاکستان کی تاریخ، عظیم رہنماؤں کی قربانیاں اور وطنِ عزیز کا قیام۔"),
        (4, "صحت اور صفائی", "صحت اور صفائی", "جسمانی و ماحولیاتی صفائی، ستھرائی کے دینی و طبی فوائد اور بیماریوں سے بچاؤ۔"),
        (5, "علامہ اقبال کا پیغام", "علامہ اقبال کا پیغام", "شاعر مشرق علامہ اقبال کی خودی کا تصور، نوجوانوں کو محنت اور شاہین جیسی بلند پروازی کی تلقین۔"),
        (6, "محنت کی عظمت", "محنت کی عظمت", "ہاتھ سے کام کرنے کی فضیلت، انبیاء کرام کی محنت پسندی اور ترقی کے اصول۔"),
        (7, "لالچ کا انجام برا", "لالچ کا انجام برا", "لالچ اور حرص کے نقصانات، قناعت پسندی کی اہمیت اور اخلاقی نصیحت۔"),
        (8, "کہیں دیر نہ ہو جائے", "کہیں دیر نہ ہو جائے", "وقت کی قدر و قیمت، پابندیٔ وقت کے فوائد اور لاپروائی کے تلخ نتائج۔"),
        (9, "ہمارے قومی تہوار", "ہمارے قومی تہوار", "یومِ آزادی، یومِ پاکستان، یومِ دفاع اور دیگر قومی تہواروں کی اہمیت و جوش و خروش۔"),
        (10, "دیگ دی ادھار", "دیگ دی ادھار", "ایک دلچسپ اور سبق آموز کہانی، ہوشیاری، سچائی اور حسِ مزاح کا امتزاج۔"),
        (11, "حکایاتِ سعدیؒ", "حکایاتِ سعدیؒ", "شیخ سعدی شیرازیؒ کی دانائی بھری حکایات اور عدل و انصاف کی ترغیب۔"),
        (12, "مادرِ ملت تجھے سلام", "مادرِ ملت تجھے سلام", "محترمہ فاطمہ جناح کی قائد اعظم کے شانہ بشانہ خدمات اور قومی کردار۔"),
        (13, "میرا دیس", "میرا دیس", "وطن کی خوبصورتی، وادیوں، دریاؤں اور کھیتوں پر مشتمل پر اثر ملی نظم۔"),
        (14, "نیکی کا بدلہ", "نیکی کا بدلہ", "دوسروں کے ساتھ حسنِ سلوک، نیکی اور بھلائی کا ہمیشہ اچھا بدلہ ملنے کا بیان۔"),
        (15, "اتفاق میں برکت ہے", "اتفاق میں برکت ہے", "اتحاد و یکجہتی کی طاقت، نا اتفاقی کے نقصانات اور مل جل کر رہنے کے فوائد۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"اردو درسی کتاب جماعت ششم: سبق نمبر {num} - {title} کا درسی متن اور اسباق۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "سبق کا متن و تدریسی نکات",
                    "headingUrdu": "سبق کا متن و تدریسی نکات",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"سبق '{title}' کا مرکزی خیال کیا ہے؟", "a": f"اس سبق کا بنیادی موضوع یہ ہے کہ: {summary}"},
                    {"q": "اس سبق سے ہمیں کیا اخلاقی و عملی سبق ملتا ہے؟", "a": "ہمیں چاہیے کہ ہم درسی ہدایات پر عمل کرتے ہوئے اپنی زندگی کو سنواریں، سچائی اور دیانت داری اپنائیں اور معاشرے کے مفید شہری بنیں۔"}
                ],
                "longQuestions": [
                    {"q": f"سبق '{title}' کا تفصیلی خلاصہ اپنے الفاظ میں تحریر کریں۔", "a": f"سبق '{title}' میں مصنف نے واضح کیا ہے کہ انسان کی کامیابی اور کردار سازی کے لیے ضروری ہے کہ وہ {summary} کو اپنا شعار بنائے۔ مصنف نے مختلف دلائل اور روزمرہ زندگی کی مثالوں سے اس حقیقت کو ثابت کیا ہے۔"}
                ],
                "mcqs": [
                    {"q": f"سبق نمبر {num} کا عنوان کیا ہے؟", "options": [title, "حیاتیاتی نظام", "الجبرا", "انگریزی شاعری"], "answer": 0, "exp": f"جماعت ششم اردو کا سبق نمبر {num} '{title}' ہے۔"},
                    {"q": "کسی شخص، جگہ یا چیز کے نام کو کیا کہتے ہیں؟", "options": ["اسم", "فعل", "حرف", "ضمیر"], "answer": 0, "exp": "اسم وہ کلمہ ہے جو کسی شخص، جگہ، چیز یا کیفیت کا نام ہو۔"}
                ]
            },
            "englishSummary": f"Lesson {num} covers '{title}', highlighting {summary}.",
            "urduSummary": f"سبق {num}: {titleUr}۔ {summary}"
        }
        units.append(unit_obj)
    write_dataset_file("URDU_6_DATA", "urdu6Chapters", "urdu_6_data.js", units)

# 8. ISLAMIAT (7 Abwab)
def build_islamiat():
    folder = os.path.join(base_dir, "Islamiat", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "باب اول: قرآن مجید و حدیث نبوی ﷺ", "باب اول: قرآن مجید و حدیث نبوی ﷺ", "قرآن مجید کا تعارف، تلاوت کے آداب، منتخب آیات کا ترجمہ و فہم اور منتخب احادیث نبویہ کا درس۔"),
        (2, "باب دوم: ایمانیات و عبادات", "باب دوم: ایمانیات و عبادات", "ایمان باللہ، ملائکہ، کتب سماویہ، رسالت، آخرت، نماز باجماعت کی اہمیت اور روزے کے فضائل و برکات۔"),
        (3, "باب سوم: سیرت طیبہ حضرت محمد ﷺ", "باب سوم: سیرت طیبہ حضرت محمد ﷺ", "مکی دور کی جدوجہد، ہجرت مدینہ، میثاق مدینہ، غزوات، فتح مکہ اور نبی کریم ﷺ کی شفقت و رحمت۔"),
        (4, "باب چہارم: اخلاق و آداب", "باب چہارم: اخلاق و آداب", "سچائی، دیانت، والدین و اساتذہ کا احترام، حیا، امانت داری، غیبت اور جھوٹ سے اجتناب۔"),
        (5, "باب پنجم: حسنِ معاملات و معاشرت", "باب پنجم: حسنِ معاملات و معاشرت", "پڑوسیوں کے حقوق، صلہ رحمی، یتیموں اور مسکینوں کی خبرگیری، باہمی رواداری اور دیانت دارانہ لین دین۔"),
        (6, "باب ششم: ہدایت کے سرچشمے اور مشاہیر اسلام", "باب ششم: ہدایت کے سرچشمے اور مشاہیر اسلام", "خلفائے راشدین، امہات المومنین حضرت خدیجہؓ و عائشہؓ، اور جلیل القدر صحابہ کرامؓ کے ایمان افروز واقعات۔"),
        (7, "باب ہفتم: اسلامی تعلیمات اور عصرِ حاضر کے تقاضے", "باب ہفتم: اسلامی تعلیمات اور عصرِ حاضر کے تقاضے", "جدید دور میں اسلامی اقدار کا نفاذ، وقت کی قدر، صفائی نصف ایمان، اور پرامن بقائے باہمی۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"اسلامیات جماعت ششم: {title} کا درسی متن اور قرآنی و نبوی تعلیمات۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "اسلامی تعلیمات و درسی تفصیلات",
                    "headingUrdu": "اسلامی تعلیمات و درسی تفصیلات",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"'{title}' سے ہمیں کیا رہنمائی ملتی ہے؟", "a": f"اس باب کی اہم تعلیمات یہ ہیں کہ: {summary}"},
                    {"q": "اسلام میں حسنِ اخلاق اور دیانت داری کی کیا اہمیت ہے؟", "a": "رسول اکرم ﷺ نے فرمایا کہ مومنوں میں کامل ترین ایمان اس کا ہے جس کا اخلاق سب سے اچھا ہو۔ دیانت داری دین کی بنیادی شرط ہے۔"}
                ],
                "longQuestions": [
                    {"q": f"قرآن و سنت کی روشنی میں '{title}' کے بنیادی نکات تفصیل سے بیان کریں۔", "a": f"اس باب میں قرآن مجید اور احادیثِ نبویہ ﷺ کی روشنی میں ثابت کیا گیا ہے کہ {summary}۔ اسلامی تعلیمات انسان کی انفرادی اور اجتماعی زندگی دونوں کو سنوارنے کے لیے مکمل ضابطہ حیات فراہم کرتی ہیں۔"}
                ],
                "mcqs": [
                    {"q": f"جماعت ششم کا باب نمبر {num} کس موضوع پر ہے؟", "options": [title, "سائنسی مشاہدات", "مغربی تاریخ", "حسابی فارمولے"], "answer": 0, "exp": f"یہ باب {title} پر مشتمل ہے۔"},
                    {"q": "اسلام کے کتنے بنیادی ارکان ہیں؟", "options": ["پانچ (5)", "تین (3)", "سات (7)", "دس (10)"], "answer": 0, "exp": "اسلام کے پانچ بنیادی ارکان ہیں: کلمہ طیبہ، نماز، روزہ، زکوٰۃ، اور حج۔"}
                ]
            },
            "englishSummary": f"Unit {num} covers '{title}', presenting {summary}.",
            "urduSummary": f"{titleUr}۔ {summary}"
        }
        units.append(unit_obj)
    write_dataset_file("ISLAMIAT_6_DATA", "isl6Chapters", "islamiat_6_data.js", units)

# 9. HPE (6 Abwab)
def build_hpe():
    folder = os.path.join(base_dir, "Hpe", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "صحت و صفائی اور متعدی بیماریاں", "صحت و صفائی اور متعدی بیماریاں", "ذاتی صفائی، متعدی اور غیر متعدی امراض، یرقان، پولیو اور وبائی امراض سے بچاؤ کے طریقے اور ویکسینیشن۔"),
        (2, "جسمانی نشوونما اور متوازن غذا", "جسمانی نشوونما اور متوازن غذا", "بڑھتے ہوئے بچوں کی جسمانی ضروریات، خوراک کے اہم اجزاء (پروٹین، نشاستہ، حیاتین) اور غذائی کمی کے اثرات۔"),
        (3, "ابتدائی طبی امداد اور حادثات سے بچاؤ", "ابتدائی طبی امداد اور حادثات سے بچاؤ", "ابتدائی طبی امداد (First Aid) کے اصول، پٹیاں باندھنا، نکسیر پھوٹنا، جلنے اور زخموں کا بروقت علاج۔"),
        (4, "کھیل اور ان کے بین الاقوامی قوانین", "کھیل اور ان کے بین الاقوامی قوانین", "ایتھلیٹکس (دوڑ، اونچی چھلانگ)، والی بال، فٹ بال اور بیڈمنٹن کے بنیادی اصول، کورٹ کی پیمائش اور اسپورٹس مین شپ۔"),
        (5, "جمناسٹک اور جسمانی لچک کی مشقیں", "جمناسٹک اور جسمانی لچک کی مشقیں", "وارم اپ اور کول ڈاؤن، جسمانی لچک اور توازن کی مشقیں، قلابازیاں اور قد بڑھانے والی جسمانی حرکات۔"),
        (6, "تفریحی سرگرمیاں اور صحت مند طرزِ زندگی", "تفریحی سرگرمیاں اور صحت مند طرزِ زندگی", "فارغ اوقات کا مثبت استعمال، کیمپنگ، صحت بخش تفریحات اور منشیات و سکرین کے منفی اثرات سے بچاؤ۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"صحت و جسمانی تعلیم جماعت ششم: باب نمبر {num} - {title}۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "صحت و جسمانی تعلیم کے اصول و مشقیں",
                    "headingUrdu": "صحت و جسمانی تعلیم کے اصول و مشقیں",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"'{title}' کی تعریف اور اس کے بنیادی مقاصد بیان کریں۔", "a": f"اس باب کا مقصد یہ ہے کہ: {summary}"},
                    {"q": "ورزش کرنے سے انسانی صحت پر کیا مثبت اثرات مرتب ہوتے ہیں؟", "a": "ورزش سے خون کی گردش بہتر ہوتی ہے، پٹھے اور ہڈیاں مضبوط ہوتی ہیں، ذہنی تناؤ کم ہوتا ہے اور جسم بیماریوں سے محفوظ رہتا ہے۔"}
                ],
                "longQuestions": [
                    {"q": f"'{title}' کے اہم اصول اور عملی طریقے تفصیل سے تحریر کریں۔", "a": f"اس باب میں واضح کیا گیا ہے کہ {summary}۔ جسمانی سرگرمیوں کو باقاعدہ اپنا کر طلبہ نہ صرف کھیلوں کے میدان میں کامیاب ہو سکتے ہیں بلکہ ایک چست اور صحت مند طرزِ زندگی بھی گزار سکتے ہیں۔"}
                ],
                "mcqs": [
                    {"q": f"جماعت ششم ایچ پی ای کا باب نمبر {num} کس سے متعلق ہے؟", "options": [title, "کیمیکل فارمولے", "قدیم سکے", "انگریزی شاعری"], "answer": 0, "exp": f"یہ باب {title} سے متعلق ہے۔"},
                    {"q": "ایک صحت مند جسم کے اندر کیسا دماغ ہوتا ہے؟", "options": ["صحت مند دماغ", "بیمار دماغ", "سست دماغ", "کوئی اثر نہیں ہوتا"], "answer": 0, "exp": "مشہور مقولہ ہے کہ ایک صحت مند جسم ہی میں صحت مند دماغ پایا جاتا ہے۔"}
                ]
            },
            "englishSummary": f"Unit {num} covers '{title}', including {summary}.",
            "urduSummary": f"{titleUr}۔ {summary}"
        }
        units.append(unit_obj)
    write_dataset_file("HPE_6_DATA", "hpe6Chapters", "hpe_6_data.js", units)

# 10. DRAWING / ART (6 Chapters)
def build_drawing():
    folder = os.path.join(base_dir, "Drawing", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "Basic Elements of Art", "فنونِ لطیفہ کے بنیادی عناصر", "Line, shape, form, texture, space, tonal values and mark-making using pencil grades (HB, 2B, 4B, 6B)."),
        (2, "Color Theory, Shading and Values", "رنگوں کا نظریہ، شیڈنگ اور ٹونز", "Primary, secondary and tertiary colors, warm and cool tones, color wheel, light and shadow, cross-hatching and blending."),
        (3, "Perspective & Still Life Drawing", "پرسپیکٹیو اور اسٹل لائف ڈرائنگ", "One-point and two-point perspective, vanishing point, horizon line, sketching domestic objects, jugs, books, and fruits."),
        (4, "Nature, Foliage and Landscape Drawing", "قدرتی مناظر، پودے اور پیڑ پودے", "Observational drawing of trees, leaves, flowers, mountain scenery, water reflections, and natural atmospheric depth."),
        (5, "Geometric Patterns & Symmetrical Art", "ہندسی نمونے اور متوازن ڈیزائن", "Use of geometry in art, circles, polygons, traditional Islamic tessellations, tile designs, and repeated motifs."),
        (6, "Islamic Calligraphy & Traditional Folk Art", "اسلامی خطاطی اور روایتی لوک فن", "Basic Arabic calligraphy scripts (Kufic, Naskh), Pakistani folk truck art, pottery decoration, and cultural crafts.")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"Art principles, practical drawing methods, and creative projects for {title}."
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "Art Techniques & Visual Fundamentals",
                    "headingUrdu": "فنی تکنیک و تصویری بنیادی اصول",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"Explain the fundamental technique of {title}.", "a": f"{title} teaches students core visual expression: {summary}"},
                    {"q": "Why is understanding light and shadow essential in drawing?", "a": "Light and shadow create the illusion of three-dimensional depth, solid volume, and realistic form on a two-dimensional surface."}
                ],
                "longQuestions": [
                    {"q": f"Provide a complete guide on how to practice and master {title}.", "a": f"Mastering {title} requires systematic pencil control, keen visual observation, and methodical execution. Students start with rough guidelines, establish accurate proportions, and apply gradual tonal shading."}
                ],
                "mcqs": [
                    {"q": f"Which chapter in Class 6 Art covers {title}?", "options": [f"Chapter {num}", "Chapter 15", "Chapter 20", "Chapter 0"], "answer": 0, "exp": f"Chapter {num} covers {title}."},
                    {"q": "Which pencil grade is soft and produces dark black tones?", "options": ["6B", "4H", "2H", "HB"], "answer": 0, "exp": "B pencils (like 6B) have soft graphite and produce rich dark shades."}
                ]
            },
            "englishSummary": f"Chapter {num} explores {title}: {summary}.",
            "urduSummary": f"یہ باب {titleUr} کی تکنیک، درسی مشقوں اور فنی اصولوں کی وضاحت کرتا ہے۔"
        }
        units.append(unit_obj)
    write_dataset_file("DRAWING_6_DATA", "drawing6Chapters", "drawing_6_data.js", units)

# 11. ARABIC (8 Lessons)
def build_arabic():
    folder = os.path.join(base_dir, "Arabic", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "الدرس الاول: التحيات والتعارف", "الدرس الاول: التحيات والتعارف (سلام و تعارف)", "عربی زبان میں سلام، تعارف، نام اور حال پوچھنا، بنیادی مکالمہ اور ضمائر کا استعمال۔"),
        (2, "الدرس الثاني: المدرسة والصف", "الدرس الثاني: المدرسة والصف (اسکول اور کلاس روم)", "کلاس روم کی اشیاء (کتاب، قلم، کرسی، سبورہ)، اسم اشارہ (ہذا، ہذہ، ذلک) اور تعلیمی گفتگو۔"),
        (3, "الدرس الثالث: الاسرة والبيت", "الدرس الثالث: الاسرة والبيت (خاندان اور گھر)", "گھر کے افراد (اب، ام، اخ، اخت)، گھر کے کمرے اور روزمرہ گھریلو اشیاء کا عربی تلفظ۔"),
        (4, "الدرس الرابع: في السوق والتجارة", "الدرس الرابع: في السوق والتجارة (بازار اور خرید و فروخت)", "بازار میں خریداری، پھلوں اور سبزیوں کے عربی نام، قیمت معلوم کرنا اور عددی گنتی۔"),
        (5, "الدرس الخامس: الصلاة والمسجد", "الدرس الخامس: الصلاة والمسجد (نماز اور مسجد)", "مسجد کے آداب، اذان، نماز کے اوقات اور ارکان کی عربی اصطلاحات۔"),
        (6, "الدرس السادس: الطبيعة وفصول السنة", "الدرس السادس: الطبيعة وفصول السنة (قدرت اور موسم)", "موسم گرما، سرما، بہار، خزاں، سورج، چاند، بارش اور آسمان کے عربی کلمات۔"),
        (7, "الدرس السابع: الصحة والغذاء", "الدرس السابع: الصحة والغذاء (صحت اور خوراک)", "صحت مند خوراک، پانی پینے کے آداب، کھانے کی دعائیں اور صحت مند عادات۔"),
        (8, "الدرس الثامن: حب الوطن والاخلاق", "الدرس الثامن: حب الوطن والاخلاق (وطن سے محبت اور اخلاق)", "وطن سے محبت، سچائی اور نیکی کے عربی محاورات، اسلامی اخلاق اور دعا۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"عربی درسی کتاب جماعت ششم: {title} کا درسی متن اور مکالمہ۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "النص والحوار والتدريبات",
                    "headingUrdu": "درسی عبارت، مکالمہ اور قواعد",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"ما هو الموضوع الأساسي في {title}؟ (اس سبق کا بنیادی موضوع کیا ہے؟)", "a": f"موضوع هذا الدرس هو {summary}"},
                    {"q": "عربی میں 'یہ کتاب ہے' اور 'وہ قلم ہے' کا ترجمہ کیا ہوگا؟", "a": "'یہ کتاب ہے' کو عربی میں 'هذا كتابٌ' اور 'وہ قلم ہے' کو 'ذلك قلمٌ' کہتے ہیں۔"}
                ],
                "longQuestions": [
                    {"q": f"اكتب حواراً قصيراً أو ملخصاً عن {title}. (اس سبق سے متعلق ایک جامع خلاصہ تحریر کریں)", "a": f"في هذا الدرس يتعلم الطلاب المفردات العربية الأساسية وقواعد النحو البسيطة المتعلقة بـ {summary}، مما يساعدهم على المحادثة السليمة وفهم القرآن واللغة العربية."}
                ],
                "mcqs": [
                    {"q": f"عنوان الدرس رقم {num} هو:", "options": [title, "الفيزياء الحديثة", "تاريخ اوروبا", "الكيمياء"], "answer": 0, "exp": f"الدرس رقم {num} هو {title}."},
                    {"q": "معنى كلمة 'شُكْراً' في الأردية هو:", "options": ["شکریہ", "خدا حافظ", "خوش آمدید", "معاف کیجیے"], "answer": 0, "exp": "'شكراً' کا مطلب شکریہ (Thank you) ہے۔"}
                ]
            },
            "englishSummary": f"Lesson {num} covers '{title}', introducing {summary}.",
            "urduSummary": f"{titleUr}۔ {summary}"
        }
        units.append(unit_obj)
    write_dataset_file("ARABIC_6_DATA", "arabic6Chapters", "arabic_6_data.js", units)

# 12. MUTALIA-E-QURAN (8 Lessons)
def build_quran():
    folder = os.path.join(base_dir, "M-Q", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "تعارف قرآن مجید و سورۃ الفاتحہ", "تعارف قرآن مجید و سورۃ الفاتحہ", "قرآن مجید کی عظمت، نزول، حفاظت، تلاوت کے فضائل اور سورۃ الفاتحہ کا ترجمہ، تفسیر و مضامین۔"),
        (2, "سورۃ الانعام و قصص الانبیاء", "سورۃ الانعام و قصص الانبیاء", "سورۃ الانعام کا تعارف، توحیدِ باری تعالیٰ، شرک کی تردید اور حضرت ابراہیم علیہ السلام کا واقعہ۔"),
        (3, "سورۃ یوسف (قصہ حضرت یوسف علیہ السلام)", "سورۃ یوسف (قصہ حضرت یوسف علیہ السلام)", "احسن القصص، حضرت یوسف علیہ السلام کا صبر، پاکدامنی، حسنِ اخلاق، تعبیرِ رویا اور کامیابی۔"),
        (4, "سورۃ الکہف (اصحاب الکہف و اخلاقی اسباق)", "سورۃ الکہف (اصحاب الکہف و اخلاقی اسباق)", "اصحاب الکہف کا ایمان افروز قصہ، فتنوں سے حفاظت، حضرت موسیٰ و خضرؑ کا واقعہ اور جمعہ کے دن تلاوت کی فضیلت۔"),
        (5, "سورۃ مریم و طہ", "سورۃ مریم و طہ", "حضرت زکریاؑ، یحییٰؑ، اور مریمؑ کا تذکرہ، حضرت عیسیٰ علیہ السلام کی ولادت اور حضرت موسیٰ علیہ السلام کی دعوت۔"),
        (6, "سورۃ الانبیاء و الحج", "سورۃ الانبیاء و الحج", "انبیاء کرام کی امتِ واحدہ، کائنات میں اللہ کی نشانیاں، یومِ حساب کی یاددہانی اور شعائر اللہ کا احترام۔"),
        (7, "سورۃ الفرقان و الشعراء", "سورۃ الفرقان و الشعراء", "حق و باطل میں فرق، رحمن کے بندوں (عباد الرحمن) کی خصوصی صفات اور قرآنی فصاحت و بلاغت۔"),
        (8, "قصار السور و منتخب دعائیں", "قصار السور و منتخب دعائیں", "قرآن حکیم کی آخری چھوٹی سورتوں (المعوذتین، الاخلاص وغیرہ) کا ترجمہ، فضائل اور مسنون قرآنی دعائیں بارگاہِ الٰہی میں۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"مطالعہ قرآن حکیم برائے جماعت ششم: سبق نمبر {num} - {title}۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "قرآنی آیات، ترجمہ و تفسیری نکات",
                    "headingUrdu": "قرآنی آیات، ترجمہ و تفسیری نکات",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"'{title}' کا تعارف اور مرکزی پیغام کیا ہے؟", "a": f"اس سبق کا مرکزی پیغام یہ ہے کہ: {summary}"},
                    {"q": "قرآن حکیم پر غور و تدبر کرنے کا کیا حکم اور فائدہ ہے؟", "a": "اللہ تعالیٰ کا ارشاد ہے کہ یہ بابرکت کتاب اس لیے نازل کی گئی تاکہ لوگ اس کی آیات میں غور و فکر کریں اور عقل والے نصیحت حاصل کریں۔"}
                ],
                "longQuestions": [
                    {"q": f"'{title}' میں بیان کردہ قرآنی واقعات اور اسباق کی تفصیل تحریر کریں۔", "a": f"اس سبق میں طلبہ کو قرآن مجید کی منتخب سورتوں کے مضامین سے روشناس کرایا گیا ہے۔ اس میں {summary} کے ذریعے انسان کو توحید، استقامت، پاکدامنی اور شکر گزاری کی تلقین کی گئی ہے۔"}
                ],
                "mcqs": [
                    {"q": f"مطالعہ قرآن جماعت ششم کا سبق نمبر {num} کون سا ہے؟", "options": [title, "قومی ترانہ", "معاشیات", "فزکس فارمولے"], "answer": 0, "exp": f"سبق نمبر {num} '{title}' ہے۔"},
                    {"q": "قرآن مجید کی پہلی سورت کون سی ہے؟", "options": ["سورۃ الفاتحہ", "سورۃ البقرہ", "سورۃ الناس", "سورۃ الاخلاص"], "answer": 0, "exp": "سورۃ الفاتحہ قرآن مجید کی پہلی سورت اور ام الکتاب ہے۔"}
                ]
            },
            "englishSummary": f"Unit {num} covers '{title}', teaching {summary}.",
            "urduSummary": f"{titleUr}۔ {summary}"
        }
        units.append(unit_obj)
    write_dataset_file("MUTALIA_QURAN_6_DATA", "quran6Chapters", "mutalia_quran_6_data.js", units)

# 13. PASHTO (12 Lessons)
def build_pashto():
    folder = os.path.join(base_dir, "Pashto", "word")
    doc_paths = [os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.endswith(".docx")]
    paras = clean_paragraphs(doc_paths)
    units_meta = [
        (1, "حمد (د عبد العظیم بابا)", "حمد (د عبد العظیم بابا)", "د الله تعالى ثنا او صفت، د کائناتو نظام، او د پالونکي رب نعمتونه۔"),
        (2, "نعت شریف (د خوږ نبي ﷺ صفت)", "نعت شریف (د خوږ نبي ﷺ صفت)", "د نبي کریم ﷺ سره مینه، د هغه مبارک اخلاق او بشریت لپاره رحمت۔"),
        (3, "زمونږ خوږ وطن پاکستان", "زمونږ خوږ وطن پاکستان", "د پاک وطن مینه، د ازادۍ قدر، تاریخي قربانۍ او د وطن ساتنه۔"),
        (4, "د علم او پوهې اهمیت", "د علم او پوهې اهمیت", "د پوهې او کتاب لوستلو فضیلت، د ناپوهۍ تاوانونه او روښانه راتلونکی۔"),
        (5, "د روغتیا ساتنه او صفائي", "د روغتیا ساتنه او صفائي", "د بدن او چاپېریال پاکوالی، د پاکوالي روغتیایي ګټې او ورزش۔"),
        (6, "د پښتونخوا تاریخي سیمې او کلتور", "د پښتونخوا تاریخي سیمې او کلتور", "د خیبر پښتونخوا تاریخي ځایونه، قلعې، د درہ خیبر تاریخ او ښکلي کلتور۔"),
        (7, "د محنت او مزدورۍ قدر", "د محنت او مزدورۍ قدر", "د لاس کار، د مزدورانو احترام، په خپل ځان تکیه کول او بریا۔"),
        (8, "مېلمه پالنه او د پښتنو دودونه", "مېلمه پالنه او د پښتنو دودونه", "پښتونولي، د مېلمه عزت کول، حجره، جرګه او ښه اخلاق۔"),
        (9, "رحمان بابا او د هغه شاعري", "رحمان بابا او د هغه شاعري", "د رحمان بابا ژوند، تصوف، د امن پیغام او پښتو ادب کښې د هغه مقام۔"),
        (10, "د اخلاقو او رښتیا ویلو ګټې", "د اخلاقو او رښتیا ویلو ګټې", "رښتیا ویل، د درواغو او فریب بدې پایلې او نېکې خبرې کول۔"),
        (11, "چاپېریال او د ونو کینول", "چاپېریال او د ونو کینول", "شنه بوټي، د ونو لګول، د ځنګلونو ساتنه او د چاپېریال ښکلا۔"),
        (12, "دعا او نېکې مشورې", "دعا او نېکې مشورې", "د خیر دعا، نصیحتونه، د مشرانو عزت کول او د ژوند نېکې لارې۔")
    ]
    chunks = partition_paras(paras, len(units_meta))
    units = []
    for (num, title, titleUr, summary), u_paras in zip(units_meta, chunks):
        sec_paras = u_paras[:35]
        full_text = "\n\n".join(sec_paras[:12]) if sec_paras else f"پښتو درسي کتاب شپږم ټولگی: سبق نمبر {num} - {title}۔"
        unit_obj = {
            "number": num,
            "id": f"unit-{num}",
            "title": title,
            "titleUrdu": titleUr,
            "type": "chapter",
            "sections": [
                {
                    "heading": "د درسي متن لوستل او مهم ټکي",
                    "headingUrdu": "د درسي متن لوستل او مهم ټکي",
                    "text": full_text,
                    "paras": sec_paras[:10]
                }
            ],
            "exercise": {
                "shortQuestions": [
                    {"q": f"د دې سبق ({title}) مرکزي خیال او مطلب څه دی؟", "a": f"د دې سبق مرام دا دی چې: {summary}"},
                    {"q": "د دې سبق نه موږ ته څه اخلاقي او نېک درس ملاویږي؟", "a": "موږ ته پکار دي چې په علم او نېکو کارونو کښې مخکې شو، د مشرانو عزت وکړو او تل رښتیا ووایو۔"}
                ],
                "longQuestions": [
                    {"q": f"د سبق '{title}' خلاصه په خپلو ټکو کښې ولیکئ۔", "a": f"په دې درسي سبق کښې مصنف یا شاعر ډېر ښکلی بیان کړی دی چې {summary}۔ د دې لوستلو سره د شاګردانو علم، پوهه او د پښتو ژبې ژور ادب لا ډېر پرمختګ کوي۔"}
                ],
                "mcqs": [
                    {"q": f"د شپږم ټولګي پښتو درسي سبق نمبر {num} نوم څه دی؟", "options": [title, "شمېرپوهنه", "کیمیا", "انګلیسي"], "answer": 0, "exp": f"دا سبق '{title}' دی."},
                    {"q": "په ژبه کښې د نوم پر ځای راتلونکی توری څه بلل کیږي؟", "options": ["ضمير", "صفت", "فعل", "قيد"], "answer": 0, "exp": "ضمير هغه کلمه ده چې د اسم یا نوم پر ځای وکارول شي."}
                ]
            },
            "englishSummary": f"Lesson {num} covers '{title}', teaching {summary}.",
            "urduSummary": f"{titleUr}۔ {summary}"
        }
        units.append(unit_obj)
    write_dataset_file("PASHTO_6_DATA", "pashto6Chapters", "pashto_6_data.js", units)

def main():
    print("Starting generation of Class 6th datasets...")
    build_math()
    build_science()
    build_computer()
    build_geography()
    build_history()
    build_english()
    build_urdu()
    build_islamiat()
    build_hpe()
    build_drawing()
    build_arabic()
    build_quran()
    build_pashto()
    print("Class 6th dataset generation finished successfully!")

if __name__ == "__main__":
    main()
