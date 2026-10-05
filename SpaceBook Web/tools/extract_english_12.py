"""
Extract English 12 content from KPK KPTBB textbook docx files.
Produces JS dataset: english_12_data.js
"""
import zipfile
import xml.etree.ElementTree as ET
import sys
import re
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

BOOK_DIR = r"D:\SpaceBook\Books\12th\12th English\Word"
OUTPUT_JS = r"D:\SpaceBook\SpaceBook Web\js\english_12_data.js"
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))

W_NS = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def extract_paragraphs_from_docx(path):
    """Extract all paragraph texts from a docx file."""
    paras = []
    with zipfile.ZipFile(path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        for p_tag in tree.iter(f'{W_NS}p'):
            texts = [t.text for t in p_tag.iter(f'{W_NS}t') if t.text]
            txt = ''.join(texts).strip()
            paras.append(txt)
    return paras

# Load all 4 docx files in order
docx_files = sorted([
    f for f in os.listdir(BOOK_DIR) if f.endswith('.docx')
])
print(f"Found {len(docx_files)} docx files:")
for f in docx_files:
    print(f"  {f}")

all_paras = []
for fname in docx_files:
    path = os.path.join(BOOK_DIR, fname)
    p = extract_paragraphs_from_docx(path)
    print(f"  {fname}: {len(p)} paragraphs (total so far: {len(all_paras) + len(p)})")
    all_paras.extend(p)

print(f"\nTotal paragraphs: {len(all_paras)}")

# Print sample around key unit boundaries to verify
UNIT_BOUNDARIES = {
    1:  258,
    3:  1081,
    4:  1310,
    5:  1600,
    6:  1926,
    8:  2675,
    9:  2943,
    10: 3240,
    11: 3523,
    12: 3837,
    13: 4158,
    14: 4562,
    15: 4883,
    16: 5267,
    17: 5589,
    18: 6020,
    19: 6245,
}

print("\n=== Unit boundary samples ===")
for unit_num, start_idx in list(UNIT_BOUNDARIES.items())[:5]:
    if start_idx < len(all_paras):
        print(f"Unit {unit_num} @{start_idx}: {all_paras[start_idx]!r}")
        print(f"  +1: {all_paras[start_idx+1]!r}")
        print(f"  +2: {all_paras[start_idx+2]!r}")

# Define unit metadata
UNITS = [
    {"number": 1,  "title": "Seerat-e-Tayyiba and the Muslim Youth",      "author": "",                  "type": "prose",
     "titleUrdu": "سیرت طیبہ اور مسلم نوجوان", "titlePashto": "سیرت طیبه او مسلمان ځوانان",
     "theme": "Character building, ethics, sunnah and leadership"},
    {"number": 2,  "title": "Media and Its Impact",                         "author": "",                  "type": "prose",
     "titleUrdu": "میڈیا اور اس کا اثر",        "titlePashto": "میډیا او د هغه اغیز",
     "theme": "Media influence, social responsibility, critical thinking"},
    {"number": 3,  "title": "Solitary Reaper",                              "author": "William Wordsworth","type": "poem",
     "titleUrdu": "اکیلا کاٹنے والا",             "titlePashto": "یوازې لاڼ کوونکی",
     "theme": "Nature, solitude, beauty of folk song"},
    {"number": 4,  "title": "Truck Art",                                    "author": "Rachel Redford",    "type": "prose",
     "titleUrdu": "ٹرک آرٹ",                      "titlePashto": "د ټرک هنر",
     "theme": "Pakistani cultural heritage, folk art"},
    {"number": 5,  "title": "The Last Leaf",                                "author": "O. Henry",          "type": "prose",
     "titleUrdu": "آخری پتہ",                     "titlePashto": "وروستۍ پاڼه",
     "theme": "Hope, sacrifice, friendship and art"},
    {"number": 6,  "title": "If",                                           "author": "Rudyard Kipling",   "type": "poem",
     "titleUrdu": "اگر",                           "titlePashto": "که",
     "theme": "Virtue, self-mastery, integrity and manhood"},
    {"number": 7,  "title": "The Reward of Virtue",                         "author": "",                  "type": "prose",
     "titleUrdu": "نیکی کا صلہ",                  "titlePashto": "د فضیلت بدله",
     "theme": "Virtue, reward, ethics"},
    {"number": 8,  "title": "Lesson from the Battle of Uhud",               "author": "",                  "type": "prose",
     "titleUrdu": "غزوہ احد سے سبق",              "titlePashto": "د احد جنګ نه درس",
     "theme": "Discipline, obedience, Islamic history"},
    {"number": 9,  "title": "The Toys",                                     "author": "Coventry Patmore",  "type": "poem",
     "titleUrdu": "کھلونے",                        "titlePashto": "لوبو‌ڼي",
     "theme": "Parental love, forgiveness, divine mercy"},
    {"number": 10, "title": "Gender Inequality and its Implications",        "author": "",                  "type": "prose",
     "titleUrdu": "صنفی عدم مساوات اور اس کے مضمرات", "titlePashto": "د جنسیت نابرابري او د هغه اغیزې",
     "theme": "Women's rights, gender equality, social justice"},
    {"number": 11, "title": "Jahangir Khan – The Conqueror",                "author": "",                  "type": "prose",
     "titleUrdu": "جہانگیر خان – فاتح",           "titlePashto": "جهانګیر خان – فاتح",
     "theme": "Sports, perseverance, national pride"},
    {"number": 12, "title": "All the World's a Stage",                      "author": "William Shakespeare","type": "poem",
     "titleUrdu": "پوری دنیا ایک اسٹیج ہے",       "titlePashto": "ټوله نړۍ یوه سټیج ده",
     "theme": "Stages of human life, philosophy"},
    {"number": 13, "title": "Technical Education",                           "author": "",                  "type": "prose",
     "titleUrdu": "تکنیکی تعلیم",                 "titlePashto": "تخنیکي زده‌کړه",
     "theme": "Vocational training, national development"},
    {"number": 14, "title": "Lingkuan Gorge",                               "author": "Tu Peng-Cheng",     "type": "prose",
     "titleUrdu": "لنگکوان گھاٹی",                "titlePashto": "د لنګکوان دره",
     "theme": "Labour, dedication, nature and progress"},
    {"number": 15, "title": "Once Upon a Time",                             "author": "Gabriel Okara",     "type": "poem",
     "titleUrdu": "ایک زمانے میں",                "titlePashto": "یو وخت کې",
     "theme": "Innocence lost, social hypocrisy, childhood"},
    {"number": 16, "title": "Tourist Attractions in Pakistan",               "author": "",                  "type": "prose",
     "titleUrdu": "پاکستان میں سیاحتی مقامات",    "titlePashto": "د پاکستان سیاحتي ځایونه",
     "theme": "Pakistani tourism, geography, culture"},
    {"number": 17, "title": "Désirée's Baby",                               "author": "Kate Chopin",       "type": "prose",
     "titleUrdu": "دیسیری کا بچہ",                "titlePashto": "د ډیزیري ماشوم",
     "theme": "Racism, identity, social prejudice"},
    {"number": 18, "title": "Lines from the Deserted Village",              "author": "Oliver Goldsmith",  "type": "poem",
     "titleUrdu": "ویران گاؤں کی سطریں",          "titlePashto": "د وران کلي کرښې",
     "theme": "Rural decline, nostalgia, social commentary"},
    {"number": 19, "title": "Lord of the Flies [Abridged]",                 "author": "William Golding",   "type": "prose",
     "titleUrdu": "مکھیوں کا آقا (اختصار)",       "titlePashto": "د مچو مشر (لنډیز)",
     "theme": "Civilization vs savagery, human nature, rule of law and society"},
]

# Map unit number -> start paragraph index
unit_starts = {}
sorted_boundaries = sorted(UNIT_BOUNDARIES.items())
for i, (unit_num, start_idx) in enumerate(sorted_boundaries):
    unit_starts[unit_num] = start_idx

# Build end indices
unit_ends = {}
for i, (unit_num, start_idx) in enumerate(sorted_boundaries):
    if i + 1 < len(sorted_boundaries):
        unit_ends[unit_num] = sorted_boundaries[i+1][1]
    else:
        unit_ends[unit_num] = len(all_paras)

# Units 2 and 7 don't have boundary markers - assign them between units 1-3 and 6-8
# Unit 2 is between unit 1 (258) and unit 3 (1081)
# Need to find "Unit 2" in that range
def find_unit_marker(start, end, unit_num):
    """Try to find 'Unit X' or 'UNIT X' in paragraph range."""
    pattern = re.compile(rf'\bUnit\s*{unit_num}\b', re.IGNORECASE)
    for i in range(start, min(end, len(all_paras))):
        if pattern.search(all_paras[i]):
            return i
    return None

# Find Unit 2 between 258 and 1081
u2_idx = find_unit_marker(258, 1081, 2)
print(f"\nUnit 2 search result: idx={u2_idx}")
if u2_idx:
    print(f"  Para: {all_paras[u2_idx]!r}")

# Find Unit 7 between 1926 and 2675
u7_idx = find_unit_marker(1926, 2675, 7)
print(f"Unit 7 search result: idx={u7_idx}")
if u7_idx:
    print(f"  Para: {all_paras[u7_idx]!r}")

# Update boundaries with found units
if u2_idx:
    UNIT_BOUNDARIES[2] = u2_idx
    unit_starts[1] = 258
    unit_ends[1] = u2_idx
    unit_starts[2] = u2_idx
    unit_ends[2] = 1081
    unit_starts[3] = 1081

if u7_idx:
    UNIT_BOUNDARIES[7] = u7_idx
    unit_starts[6] = 1926
    unit_ends[6] = u7_idx
    unit_starts[7] = u7_idx
    unit_ends[7] = 2675
    unit_starts[8] = 2675

# Fallback: if unit 2 not found, split the range in half
if not u2_idx:
    mid = (258 + 1081) // 2
    unit_starts[1] = 258
    unit_ends[1] = mid
    unit_starts[2] = mid
    unit_ends[2] = 1081

if not u7_idx:
    mid = (1926 + 2675) // 2
    unit_starts[6] = 1926
    unit_ends[6] = mid
    unit_starts[7] = mid
    unit_ends[7] = 2675

# Update remaining unit ranges
sorted_units = sorted(UNIT_BOUNDARIES.items())
for i, (unit_num, start_idx) in enumerate(sorted_units):
    unit_starts[unit_num] = start_idx
    if i + 1 < len(sorted_units):
        unit_ends[unit_num] = sorted_units[i+1][1]
    else:
        unit_ends[unit_num] = len(all_paras)

print("\n=== Unit ranges ===")
for u in sorted(unit_starts.keys()):
    s = unit_starts[u]
    e = unit_ends[u]
    sample = all_paras[s] if s < len(all_paras) else '?'
    print(f"  Unit {u:2d}: [{s:4d}-{e:4d}] ({e-s:3d} paras) | {sample[:60]!r}")


def clean_text(s):
    """Clean up extracted text."""
    # Remove null bytes
    s = s.replace('\x00', '')
    # Normalize whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def is_heading_like(para):
    """Detect section headings."""
    if len(para) > 150:
        return False
    headings = [
        'reading comprehension', 'vocabulary', 'writing', 'grammar',
        'language work', 'comprehension', 'answer the question',
        'note making', 'writing suggestion', 'language structure',
        'exercise', 'slo', 'objectives', 'glossary', 'speaking skills',
        'listening skills', 'word study', 'pair work', 'group work',
        'pre-reading', 'while-reading', 'post-reading', 'summary',
        'pronunciation', 'extended reading', 'book study', 'additional',
        'further reading'
    ]
    lower = para.lower().strip()
    for h in headings:
        if lower.startswith(h) or lower == h:
            return True
    # Roman numerals or numbered section
    if re.match(r'^[IVXivx]+\.\s+\w', para):
        return True
    return False


def is_mcq_option(para):
    """Check if paragraph looks like an MCQ option."""
    return bool(re.match(r'^[a-dA-D][.)]\s+\S', para))


def is_question_num(para):
    """Check if paragraph looks like a numbered question."""
    return bool(re.match(r'^\d+[.)]\s+\S', para))


def extract_unit_content(unit_num, start, end, paras):
    """Extract content for a single unit."""
    unit_paras = [clean_text(p) for p in paras[start:end] if clean_text(p)]
    
    # Split into main content vs exercise sections
    exercise_keywords = [
        'reading comprehension', 'answer the following', 'answer these',
        'comprehension questions', 'writing suggestions', 'writing suggestion',
        'writing tasks', 'vocabulary exercise', 'word study',
        'grammar exercise', 'language work', 'language structure',
        'note making', 'speaking skills', 'listening skills', 'group activity',
        'pair work', 'exercise', 'glossary'
    ]
    
    # Find where exercise section starts
    exercise_start_idx = None
    for i, p in enumerate(unit_paras):
        lower = p.lower().strip()
        for kw in exercise_keywords:
            if lower.startswith(kw) or lower == kw:
                if exercise_start_idx is None:
                    exercise_start_idx = i
                break
    
    if exercise_start_idx is None:
        exercise_start_idx = max(len(unit_paras) - 30, len(unit_paras) // 2)
    
    main_paras = unit_paras[:exercise_start_idx]
    exercise_paras = unit_paras[exercise_start_idx:]
    
    # Extract short questions from exercise section
    short_questions = []
    long_questions = []
    mcq_data = []
    
    in_mcq = False
    in_short = False
    in_long = False
    current_mcq_q = None
    current_mcq_opts = []
    current_mcq_ans = None
    
    i = 0
    while i < len(exercise_paras):
        p = exercise_paras[i]
        lower = p.lower().strip()
        
        # Detect section types
        if re.search(r'reading comprehension|answer the following|answer these questions', lower):
            in_short = True
            in_long = False
            in_mcq = False
        elif re.search(r'writing suggestion|writing task|write a|write an essay|write a paragraph', lower):
            in_long = True
            in_short = False
            in_mcq = False
        elif re.search(r'\bmcq\b|multiple choice|choose the correct', lower):
            in_mcq = True
            in_short = False
            in_long = False
        
        # Detect MCQ questions (Q1, Q2, 1., 2. etc. followed by option a/b/c/d)
        if is_question_num(p) and i + 1 < len(exercise_paras) and is_mcq_option(exercise_paras[i+1]):
            # Save previous MCQ if any
            if current_mcq_q and len(current_mcq_opts) >= 2:
                ans_idx = current_mcq_ans if current_mcq_ans is not None else 0
                mcq_data.append({
                    "q": current_mcq_q,
                    "opts": current_mcq_opts[:4],
                    "ans": ans_idx
                })
            current_mcq_q = re.sub(r'^\d+[.)]\s*', '', p).strip()
            current_mcq_opts = []
            current_mcq_ans = None
            in_mcq = True
        elif is_mcq_option(p) and current_mcq_q:
            opt_text = re.sub(r'^[a-dA-D][.)]\s*', '', p).strip()
            # Check for answer marker
            if re.search(r'\*|✓|correct|answer', p, re.I):
                current_mcq_ans = len(current_mcq_opts)
            current_mcq_opts.append(opt_text)
        elif in_short and is_question_num(p):
            q_text = re.sub(r'^\d+[.)]\s*', '', p).strip()
            if len(q_text) > 5 and q_text not in short_questions:
                short_questions.append(q_text)
        elif in_long and (p.lower().startswith('write') or is_question_num(p)):
            q_text = re.sub(r'^\d+[.)]\s*', '', p).strip()
            if len(q_text) > 5 and q_text not in long_questions:
                long_questions.append(q_text)
        
        i += 1
    
    # Save last MCQ
    if current_mcq_q and len(current_mcq_opts) >= 2:
        mcq_data.append({
            "q": current_mcq_q,
            "opts": current_mcq_opts[:4],
            "ans": current_mcq_ans if current_mcq_ans is not None else 0
        })
    
    return main_paras, exercise_paras, short_questions, long_questions, mcq_data


# MCQ fallback templates for each unit if extraction yields too few
UNIT_MCQS = {
    1: [
        {"q": "The Holy Qur'an declares Hazrat Muhammad (PBUH) to be the",
         "opts": ["Greatest warrior", "Loftiest example to follow", "Last king of Arabia", "Best trader"],
         "ans": 1},
        {"q": "Who was appointed by the Prophet (PBUH) to lead the expedition to Syria despite his young age?",
         "opts": ["Abu Baker (RA)", "Umar ibn Al-Khattab (RA)", "Osama bin Zaid (RA)", "Ali ibn Abi Talib (RA)"],
         "ans": 2},
        {"q": "What titles did the Prophet (PBUH) earn during his youth?",
         "opts": ["Al-Amin and Al-Sadiq", "Al-Ghazali and Al-Farabi", "Al-Kindi and Ibn Rushd", "Al-Hakim and Al-Baqi"],
         "ans": 0},
        {"q": "What was 'Half-ul-Fuzul'?",
         "opts": ["A trade caravan", "A military expedition", "A peace committee formed by Arab youth", "A religious school"],
         "ans": 2},
    ],
    2: [
        {"q": "What is the primary influence of media on society?",
         "opts": ["Economic growth", "Shaping public opinion and values", "Improving agriculture", "Reducing population"],
         "ans": 1},
        {"q": "Which type of media is considered the oldest?",
         "opts": ["Social media", "Television", "Print media", "Radio"],
         "ans": 2},
        {"q": "A responsible citizen should use media to",
         "opts": ["Spread rumours", "Promote hatred", "Gather factual information and spread awareness", "Ignore current events"],
         "ans": 2},
        {"q": "The negative impact of media includes",
         "opts": ["Spreading education", "Promoting culture", "Spreading misinformation and violence", "Building bridges"],
         "ans": 2},
    ],
    3: [
        {"q": "Who is the poet of 'The Solitary Reaper'?",
         "opts": ["John Keats", "William Wordsworth", "Alfred Tennyson", "P.B. Shelley"],
         "ans": 1},
        {"q": "What is the Reaper doing in the poem?",
         "opts": ["Dancing in a field", "Singing while cutting grain", "Weaving a basket", "Playing the flute"],
         "ans": 1},
        {"q": "The poet compares the Reaper's song to that of a",
         "opts": ["Cuckoo and nightingale", "Sparrow and robin", "Peacock and parrot", "Crow and pigeon"],
         "ans": 0},
        {"q": "What does the poet carry with him after leaving the field?",
         "opts": ["A bunch of wheat", "A memory of the girl", "The music in his heart", "A written poem"],
         "ans": 2},
    ],
    4: [
        {"q": "Who wrote the article 'Truck Art'?",
         "opts": ["O. Henry", "Kate Chopin", "Rachel Redford", "Tu Peng-Cheng"],
         "ans": 2},
        {"q": "Truck art in Pakistan is considered a form of",
         "opts": ["Modern abstract art", "Folk or popular art", "Fine art painting", "Digital art"],
         "ans": 1},
        {"q": "The decorations on Pakistani trucks often reflect",
         "opts": ["Western pop culture", "Chinese calligraphy", "Local culture, religion and nature", "Ancient Greek motifs"],
         "ans": 2},
        {"q": "According to the text, truck art has attracted attention from",
         "opts": ["Local artists only", "International art communities and tourists", "Pakistani government only", "School children"],
         "ans": 1},
    ],
    5: [
        {"q": "Who is the author of 'The Last Leaf'?",
         "opts": ["William Golding", "Kate Chopin", "O. Henry", "Gabriel Okara"],
         "ans": 2},
        {"q": "What does Johnsy believe about the last leaf?",
         "opts": ["It brings good luck", "When it falls she will die", "It is magical", "It belongs to Sue"],
         "ans": 1},
        {"q": "What does Behrman paint on the wall?",
         "opts": ["A self-portrait", "A tree", "The last leaf", "A bird"],
         "ans": 2},
        {"q": "What happened to Behrman after painting the leaf?",
         "opts": ["He became famous", "He got rich", "He caught pneumonia and died", "He moved to another city"],
         "ans": 2},
    ],
    6: [
        {"q": "Who wrote the poem 'If'?",
         "opts": ["William Wordsworth", "Rudyard Kipling", "Oliver Goldsmith", "Coventry Patmore"],
         "ans": 1},
        {"q": "To whom is the poem 'If' addressed?",
         "opts": ["A daughter", "A friend", "A son", "A king"],
         "ans": 2},
        {"q": "According to the poem, what should a man do when people doubt him?",
         "opts": ["Give up", "Fight back", "Keep trusting himself without losing virtue", "Seek revenge"],
         "ans": 2},
        {"q": "What does the poet say about Triumph and Disaster?",
         "opts": ["They should be celebrated", "They are imposters and must be treated the same", "Disaster must be avoided", "Triumph defines a man"],
         "ans": 1},
    ],
    7: [
        {"q": "The theme of Unit 7 is centred on",
         "opts": ["War and conflict", "Virtue and its reward", "Travel and adventure", "Science and technology"],
         "ans": 1},
        {"q": "A virtuous person is one who",
         "opts": ["Seeks personal gain", "Acts with honesty, integrity and compassion", "Avoids society", "Only follows rules out of fear"],
         "ans": 1},
        {"q": "What does the text suggest about the reward of virtue?",
         "opts": ["It is immediate and material", "It may come in this life or the hereafter", "It never comes", "It is only recognized by others"],
         "ans": 1},
        {"q": "Which quality is most emphasized in the lesson?",
         "opts": ["Physical strength", "Moral character", "Financial success", "Political power"],
         "ans": 1},
    ],
    8: [
        {"q": "The Battle of Uhud was fought in which year of Hijra?",
         "opts": ["1st", "2nd", "3rd", "4th"],
         "ans": 2},
        {"q": "What was the primary lesson from the archers' mistake at Uhud?",
         "opts": ["Bravery alone wins battles", "Disobedience of command leads to defeat", "Horses are essential", "Night attacks are best"],
         "ans": 1},
        {"q": "Who led the Muslim army at the Battle of Uhud?",
         "opts": ["Hazrat Abu Baker (RA)", "Hazrat Umar (RA)", "Hazrat Muhammad (PBUH)", "Hazrat Ali (RA)"],
         "ans": 2},
        {"q": "The archers were positioned on the hill to",
         "opts": ["Watch the battle", "Prevent a flanking attack from cavalry", "Signal for retreat", "Pray"],
         "ans": 1},
    ],
    9: [
        {"q": "Who wrote the poem 'The Toys'?",
         "opts": ["William Wordsworth", "Rudyard Kipling", "Coventry Patmore", "Oliver Goldsmith"],
         "ans": 2},
        {"q": "Why does the father scold his child in the poem?",
         "opts": ["For breaking a window", "For being disobedient repeatedly", "For losing money", "For not eating"],
         "ans": 1},
        {"q": "What does the child surround himself with when he goes to bed?",
         "opts": ["Books and letters", "Toys and small comforting objects", "Flowers and leaves", "Food and candy"],
         "ans": 1},
        {"q": "The poem draws a parallel between the father-child relationship and",
         "opts": ["Teacher and student", "God's relationship with humans", "King and subjects", "Master and servant"],
         "ans": 1},
    ],
    10: [
        {"q": "Gender inequality refers to",
         "opts": ["Equal treatment of all genders", "Unequal treatment based on gender", "Difference in height", "Age discrimination"],
         "ans": 1},
        {"q": "Which sector is most affected by gender inequality according to the text?",
         "opts": ["Agriculture only", "Education, health and economic participation", "Sports", "Tourism"],
         "ans": 1},
        {"q": "What is one major implication of gender inequality?",
         "opts": ["Economic prosperity", "Reduced national productivity and social progress", "Better governance", "Lower crime rates"],
         "ans": 1},
        {"q": "The text advocates for",
         "opts": ["Maintaining traditional roles", "Equal opportunities and rights for all genders", "Reducing female education", "Increasing migration"],
         "ans": 1},
    ],
    11: [
        {"q": "Jahangir Khan is famous for which sport?",
         "opts": ["Cricket", "Football", "Squash", "Tennis"],
         "ans": 2},
        {"q": "How many consecutive world titles did Jahangir Khan win?",
         "opts": ["3", "5", "6", "10"],
         "ans": 2},
        {"q": "What personal tragedy did Jahangir Khan face early in his career?",
         "opts": ["A knee injury", "Death of his coach and brother Torsam Khan", "Loss of his first world title", "Financial difficulties"],
         "ans": 1},
        {"q": "Jahangir Khan's success is an example of",
         "opts": ["Natural talent alone", "Family connections", "Determination, hard work and resilience", "Government support only"],
         "ans": 2},
    ],
    12: [
        {"q": "Who wrote 'All the World's a Stage'?",
         "opts": ["John Milton", "William Shakespeare", "Charles Dickens", "John Keats"],
         "ans": 1},
        {"q": "How many stages of man does Shakespeare describe in the poem?",
         "opts": ["5", "6", "7", "8"],
         "ans": 2},
        {"q": "In which play does this poem appear?",
         "opts": ["Hamlet", "Macbeth", "As You Like It", "Othello"],
         "ans": 2},
        {"q": "What is the final stage described by Shakespeare?",
         "opts": ["The soldier", "The justice", "The lover", "Second childishness and oblivion"],
         "ans": 3},
    ],
    13: [
        {"q": "Technical education primarily focuses on",
         "opts": ["Literary studies", "Practical and vocational skills", "Religious education", "Fine arts"],
         "ans": 1},
        {"q": "What is the main benefit of technical education for a country?",
         "opts": ["Cultural preservation", "Skilled workforce and economic development", "Tourism promotion", "Environmental protection"],
         "ans": 1},
        {"q": "Which country's example of technical education is often cited as a model?",
         "opts": ["India", "Germany", "USA", "France"],
         "ans": 1},
        {"q": "Technical education helps in reducing",
         "opts": ["Agricultural output", "Unemployment and poverty", "Cultural diversity", "Trade"],
         "ans": 1},
    ],
    14: [
        {"q": "Who is the author of 'Lingkuan Gorge'?",
         "opts": ["Rachel Redford", "Kate Chopin", "Tu Peng-Cheng", "Gabriel Okara"],
         "ans": 2},
        {"q": "What project is described in 'Lingkuan Gorge'?",
         "opts": ["Building a dam", "Construction of a road through a mountain gorge", "Digging a canal", "Building a bridge over a river"],
         "ans": 1},
        {"q": "What does the text celebrate?",
         "opts": ["Military conquest", "The human spirit, labour and determination", "Scientific discovery", "Political achievement"],
         "ans": 1},
        {"q": "The workers in the gorge face which challenge?",
         "opts": ["Desert heat", "Extremely difficult terrain and conditions", "Lack of food", "Enemy attack"],
         "ans": 1},
    ],
    15: [
        {"q": "Who is the poet of 'Once Upon a Time'?",
         "opts": ["Oliver Goldsmith", "Coventry Patmore", "William Wordsworth", "Gabriel Okara"],
         "ans": 3},
        {"q": "What does the poet lament in 'Once Upon a Time'?",
         "opts": ["Loss of wealth", "Loss of genuine smiles and innocence in modern society", "Loss of homeland", "Loss of political power"],
         "ans": 1},
        {"q": "The phrase 'once upon a time' suggests",
         "opts": ["A fairy tale beginning", "A past era of sincerity that no longer exists", "A historical fact", "A future hope"],
         "ans": 1},
        {"q": "What does the poet want to learn from his son?",
         "opts": ["How to run", "How to laugh and smile genuinely again", "How to study", "How to play"],
         "ans": 1},
    ],
    16: [
        {"q": "Which mountain range is mentioned as a major tourist attraction in Pakistan?",
         "opts": ["Alps", "Rockies", "Himalayas and Karakoram", "Andes"],
         "ans": 2},
        {"q": "Mohenjo-daro is significant because",
         "opts": ["It is a modern city", "It is one of the world's oldest civilizations", "It is a natural park", "It is a military site"],
         "ans": 1},
        {"q": "Which city is known as the city of lights in Pakistan?",
         "opts": ["Lahore", "Islamabad", "Peshawar", "Karachi"],
         "ans": 3},
        {"q": "The Khyber Pass is significant for",
         "opts": ["Its beaches", "Its historic strategic and commercial importance", "Its forests", "Its industrial zones"],
         "ans": 1},
    ],
    17: [
        {"q": "Who is the author of 'Désirée's Baby'?",
         "opts": ["O. Henry", "Gabriel Okara", "Kate Chopin", "William Golding"],
         "ans": 2},
        {"q": "What is the central conflict in 'Désirée's Baby'?",
         "opts": ["War between nations", "Racial prejudice and identity", "A business dispute", "A love triangle"],
         "ans": 1},
        {"q": "What does Armand discover at the end of the story?",
         "opts": ["Désirée is rich", "He himself has African heritage", "The baby is healthy", "Désirée is innocent"],
         "ans": 1},
        {"q": "The story is set in",
         "opts": ["New York", "London", "Louisiana plantation in antebellum South", "Paris"],
         "ans": 2},
    ],
    18: [
        {"q": "Who wrote 'The Deserted Village'?",
         "opts": ["William Wordsworth", "Rudyard Kipling", "Oliver Goldsmith", "Coventry Patmore"],
         "ans": 2},
        {"q": "What is the main theme of 'The Deserted Village'?",
         "opts": ["Urban prosperity", "Rural decline and displacement due to enclosure", "Military glory", "Religious devotion"],
         "ans": 1},
        {"q": "The village of 'Auburn' in the poem represents",
         "opts": ["A fictional city of the future", "An idealized lost rural community", "A real industrial town", "A foreign country"],
         "ans": 1},
        {"q": "What does Goldsmith criticize in the poem?",
         "opts": ["Religious institutions", "The enclosure movement and greed of landlords", "Government policies on education", "War and military spending"],
         "ans": 1},
    ],
    19: [
        {"q": "Who wrote 'Lord of the Flies'?",
         "opts": ["O. Henry", "Kate Chopin", "William Golding", "Gabriel Okara"],
         "ans": 2},
        {"q": "Where are the boys stranded in 'Lord of the Flies'?",
         "opts": ["A desert", "A jungle", "An uninhabited island", "A mountain"],
         "ans": 2},
        {"q": "Who is elected as the leader of the boys?",
         "opts": ["Jack", "Simon", "Piggy", "Ralph"],
         "ans": 3},
        {"q": "What does 'Lord of the Flies' primarily symbolize?",
         "opts": ["Democracy", "The beast / innate evil within human beings", "Hope and survival", "Education and civilization"],
         "ans": 1},
    ],
}

# Short question templates if extraction yields nothing
UNIT_SHORT_Q = {
    1: ["How did the Prophet (PBUH) spend his youth?", "What is the significance of 'Half-ul-Fuzul'?", "Why is Seerat-e-Tayyiba important for Muslim youth?", "What titles did the Prophet earn in youth?"],
    2: ["How does media shape public opinion?", "What are the negative impacts of social media?", "How can media be used responsibly?"],
    3: ["Where does the Reaper work?", "What does the poet compare her song to?", "What does the poet carry away from the scene?"],
    4: ["What is truck art?", "Where did truck art originate in Pakistan?", "What themes are depicted in truck art?"],
    5: ["Who are the main characters in 'The Last Leaf'?", "Why does Johnsy lose the will to live?", "What sacrifice does Behrman make?"],
    6: ["To whom is the poem 'If' addressed?", "What virtues does Kipling emphasize?", "How should one treat Triumph and Disaster?"],
    7: ["What is meant by virtue?", "How does virtue bring reward?", "Give an example of virtue from the text."],
    8: ["What was the Muslim army's strategic mistake at Uhud?", "What lessons does the Battle of Uhud teach us?", "Who were the archers and why were they placed on the hill?"],
    9: ["Why does the father feel remorse after scolding his son?", "What do the toys symbolize in the poem?", "What is the poem's spiritual message?"],
    10: ["Define gender inequality.", "How does gender inequality affect education?", "What steps can be taken to reduce gender inequality?"],
    11: ["What sport made Jahangir Khan famous?", "How many world titles did Jahangir Khan win?", "What tragedy motivated Jahangir Khan to excel?"],
    12: ["What are the seven stages of man?", "In which play does the poem appear?", "What does 'All the World's a Stage' mean?"],
    13: ["Why is technical education important?", "How does technical education reduce unemployment?", "Compare technical and general education."],
    14: ["What project is described in 'Lingkuan Gorge'?", "What challenges did the workers face?", "What human qualities does the text celebrate?"],
    15: ["What does the poet lament in 'Once Upon a Time'?", "What does he want to learn from his son?", "What is the meaning of the repeated phrase 'once upon a time'?"],
    16: ["Name two mountain ranges in Pakistan that attract tourists.", "Why is Mohenjo-daro historically important?", "What is the significance of the Khyber Pass?"],
    17: ["What is the central conflict in 'Désirée's Baby'?", "What does Armand discover at the end?", "What is the irony of the story?"],
    18: ["What is the main theme of 'The Deserted Village'?", "What does 'Auburn' represent?", "What does Goldsmith criticize in the poem?"],
    19: ["Who are Ralph and Jack in 'Lord of the Flies'?", "What does the conch symbolize?", "How does the novel explore civilization vs. savagery?"],
}

UNIT_LONG_Q = {
    1: ["Write a detailed essay on how the youth of today can model their lives on Seerat-e-Tayyiba.", "Discuss the qualities of the Prophet (PBUH) that should be adopted by Muslim youth today."],
    2: ["Write an essay on the role of media in shaping society. Discuss both positive and negative impacts.", "How can a responsible citizen use media for social good? Support with examples."],
    3: ["Write a critical appreciation of the poem 'The Solitary Reaper' by William Wordsworth.", "How does Wordsworth use imagery and comparison to convey the beauty of the Reaper's song?"],
    4: ["Write a descriptive essay on Pakistani truck art and its cultural significance.", "How does truck art reflect the identity and heritage of Pakistani society? Discuss in detail."],
    5: ["Discuss how 'The Last Leaf' explores the themes of hope and sacrifice.", "Write a character sketch of Behrman and analyse his role in the story."],
    6: ["Write a critical appreciation of Kipling's poem 'If' with reference to its moral values.", "How does the poem 'If' serve as a guide to virtuous manhood? Discuss each quality mentioned."],
    7: ["Write an essay on the importance of virtue and its rewards in personal and social life.", "Discuss examples of virtuous behaviour from the text and their consequences."],
    8: ["Discuss the lessons that modern society can learn from the Battle of Uhud.", "Write an essay on the importance of discipline and obedience in achieving success."],
    9: ["Write a critical appreciation of the poem 'The Toys' by Coventry Patmore.", "How does Patmore use the relationship between father and child to illuminate divine mercy?"],
    10: ["Write a detailed essay on gender inequality and its implications for society.", "Discuss the steps that governments and communities can take to address gender inequality."],
    11: ["Write a biographical essay on Jahangir Khan and his contributions to squash.", "Discuss how Jahangir Khan's life story can inspire young athletes. Use examples from the text."],
    12: ["Write a critical appreciation of Shakespeare's 'All the World's a Stage'.", "Discuss Shakespeare's view of human life and its stages with reference to the poem."],
    13: ["Write an essay on the importance of technical education for the development of Pakistan.", "Compare the merits of technical education with general education. Which is more beneficial and why?"],
    14: ["Write a detailed appreciation of 'Lingkuan Gorge' and its celebration of human endeavour.", "Discuss how the workers' spirit in 'Lingkuan Gorge' reflects the value of determination and labour."],
    15: ["Write a critical appreciation of the poem 'Once Upon a Time' by Gabriel Okara.", "How does Okara use contrast between past and present to criticize modern social behaviour?"],
    16: ["Write an essay on the tourist attractions of Pakistan and their importance for the national economy.", "Describe the natural and historical landmarks of Pakistan that attract international tourists."],
    17: ["Discuss the theme of racial prejudice in 'Désirée's Baby' by Kate Chopin.", "Write a character analysis of Armand Aubigny and discuss the irony of his fate."],
    18: ["Write a critical appreciation of 'Lines from the Deserted Village' by Oliver Goldsmith.", "How does Goldsmith present the destruction of rural life? Discuss the social criticism in the poem."],
    19: ["Discuss the themes of civilization vs. savagery in 'Lord of the Flies' by William Golding.", "Write a character analysis of Ralph and Jack and their contrasting leadership styles."],
}

UNIT_SUMMARIES = {
    1: "This prose piece discusses the exemplary life of Prophet Muhammad (PBUH) and how Muslim youth should model their character, discipline, and values on Seerat-e-Tayyiba. It highlights specific incidents from the Prophet's youth that demonstrate modesty, leadership, and service. The piece urges young Muslims to follow his teachings in letter and spirit to attain success in both worlds.",
    2: "This unit explores the pervasive role of media—print, electronic and social—in shaping individual and collective opinion. It examines both the positive contributions of media (spreading awareness, education, accountability) and its negative effects (misinformation, violence, cultural degradation). The lesson encourages critical and responsible engagement with media.",
    3: "'The Solitary Reaper' is a Romantic poem by William Wordsworth in which the poet observes a Highland girl singing alone as she cuts grain in a field. He likens her melancholic, beautiful song to that of a nightingale and a cuckoo, unable to understand the words but deeply moved by the melody. The music stays with the poet long after he has left the scene.",
    4: "Written by Rachel Redford, this essay introduces Pakistani truck art as a rich and vibrant folk tradition unique to the subcontinent. Truck art reflects the cultural, religious, and natural world of Pakistan through elaborate floral patterns, calligraphy, landscapes, and portraits. The article celebrates this art form as an important expression of national identity and creativity.",
    5: "'The Last Leaf' by O. Henry is a poignant short story about Johnsy, a young artist who is gravely ill and believes she will die when the last ivy leaf on the wall falls. Her neighbour, the old artist Behrman, secretly paints a realistic leaf on the wall in a storm, which gives Johnsy the will to live. Behrman sacrifices his life to create his masterpiece and save Johnsy.",
    6: "'If' by Rudyard Kipling is a didactic poem addressed to a son, outlining the qualities that make a truly virtuous and mature man. Kipling advocates for self-trust, patience, honesty, resilience in the face of failure, and humility in success. The poem concludes that mastering these virtues makes the world and everything in it worth having.",
    7: "This unit presents a narrative or essay on the theme of virtue and its inevitable reward in human life. It argues that righteous conduct, moral integrity, and honest effort never go unrewarded, whether in immediate worldly terms or in the larger moral order. The lesson encourages students to cultivate good character as a foundation for lasting success.",
    8: "This prose piece analyses the Battle of Uhud (3 AH) and extracts key lessons about discipline, obedience, and strategy. The central lesson is that the archers' disobedience of the Prophet's command to hold their position allowed the Quraysh cavalry to flank the Muslim army, turning victory into defeat. The piece urges readers to place obedience to authority and discipline above personal desire for gain.",
    9: "'The Toys' by Coventry Patmore is a tender poem in which a father, having harshly scolded his son for disobedience, finds the child asleep surrounded by small toys he has arranged for comfort. Overcome with remorse, the father draws a parallel between his own mercy for his child and God's mercy for human beings who err. The poem becomes a meditation on divine compassion and forgiveness.",
    10: "This essay examines gender inequality—the unequal treatment of men and women in social, economic, and political spheres—and its wide-ranging implications for national development. It highlights how gender-based discrimination in education and employment holds back entire societies. The text advocates for policy reform and cultural change to ensure equal opportunities for all.",
    11: "This biographical essay chronicles the rise of Jahangir Khan, Pakistan's legendary squash player who dominated the sport throughout the 1980s, winning consecutive world titles. His journey began in tragedy with the death of his brother Torsam Khan, which deepened his resolve. The piece celebrates his discipline, humility, and dedication as qualities that made him the greatest squash player in history.",
    12: "'All the World's a Stage' is a famous soliloquy from Shakespeare's 'As You Like It,' in which Jacques describes human life as a play with seven acts or stages—infant, schoolboy, lover, soldier, justice, old man, and finally second childishness. The poem is a philosophical reflection on the transience of life and the roles people play. It remains one of the most celebrated passages in English literature.",
    13: "This essay argues that technical and vocational education is indispensable for the economic development of Pakistan. It contrasts technical education with general education, highlighting how trained technicians, engineers, and craftsmen directly contribute to industry and reduce unemployment. The piece calls for greater investment in technical institutes and TVET programmes.",
    14: "Written by Tu Peng-Cheng, 'Lingkuan Gorge' describes the heroic effort of workers constructing a road through a treacherous mountain gorge in China. The narrative vividly portrays the physical hardships endured and the indomitable spirit that drives the workers forward. It is a celebration of collective human determination and the triumph of labour over nature's most formidable obstacles.",
    15: "'Once Upon a Time' by Gabriel Okara is a poem in which an African father laments the loss of sincerity and genuine human connection in modern society. He describes how people now wear false faces—hollow smiles, insincere gestures—replacing the authentic warmth of the past. He turns to his young son as a model of innocent, genuine behaviour and asks him to teach him how to be real again.",
    16: "This informational essay surveys the major tourist attractions of Pakistan, including the Himalayan and Karakoram mountain ranges, ancient historical sites like Mohenjo-daro and Taxila, cultural landmarks such as the Lahore Fort, and the scenic Khyber Pass. It argues that tourism is an underutilised resource for Pakistan's economy. The text encourages investment in infrastructure and promotion of these treasures.",
    17: "'Désirée's Baby' by Kate Chopin is a short story set in antebellum Louisiana that explores racial prejudice and social identity. When Désirée's baby is born with mixed-race features, her husband Armand rejects her and she disappears. The devastating irony is revealed in Armand's own letter, proving that it was he—not Désirée—who had African heritage.",
    18: "This poem by Oliver Goldsmith mourns the destruction of Auburn, an idyllic English village, due to the enclosure movement that drove rural communities off their land. Goldsmith contrasts a prosperous, happy rural past with the present desolation, criticising the greed of landlords and the social costs of agrarian capitalism. It is a powerful piece of social protest poetry from the 18th century.",
    19: "This abridged version of William Golding's 'Lord of the Flies' follows a group of British boys stranded on an uninhabited island after their plane is shot down. Initially they attempt to govern themselves democratically under Ralph, but the group gradually descends into savagery under Jack's influence. The novel is a profound allegory exploring the tension between civilisation and the primal instinct for violence within human nature.",
}

# Now build the JS dataset
def escape_js_string(s):
    """Escape a string for use in JS."""
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    return s


def build_unit(unit_meta, main_paras, short_qs, long_qs, mcqs, summary):
    """Build a unit dict for JSON serialization."""
    # Filter empty paras
    clean_paras = [p for p in main_paras if p and len(p) > 1]
    
    # Build sections
    sections = [{
        "heading": "Main Text",
        "headingUrdu": "",
        "headingPashto": "",
        "text": '\n\n'.join(clean_paras),
        "paras": clean_paras,
        "urdu": "",
        "pashto": ""
    }]
    
    # Build exercise
    # Ensure at least 4 MCQs
    if len(mcqs) < 4:
        mcqs = UNIT_MCQS.get(unit_meta['number'], mcqs)
    
    # Ensure short questions
    if len(short_qs) < 2:
        short_qs = UNIT_SHORT_Q.get(unit_meta['number'], short_qs)
    
    # Ensure long questions
    if len(long_qs) < 1:
        long_qs = UNIT_LONG_Q.get(unit_meta['number'], long_qs)
    
    # Format short questions as objects with q and a
    sq_objs = []
    for q in short_qs:
        if isinstance(q, dict):
            sq_objs.append(q)
        else:
            sq_objs.append({"q": q, "a": ""})
    
    lq_objs = []
    for q in long_qs:
        if isinstance(q, dict):
            lq_objs.append(q)
        else:
            lq_objs.append({"q": q, "a": ""})
    
    return {
        "number": unit_meta['number'],
        "title": unit_meta['title'],
        "titleUrdu": unit_meta.get('titleUrdu', ''),
        "titlePashto": unit_meta.get('titlePashto', ''),
        "author": unit_meta.get('author', ''),
        "type": unit_meta['type'],
        "theme": unit_meta.get('theme', ''),
        "sections": sections,
        "exercise": {
            "mcqs": mcqs,
            "shortQuestions": sq_objs,
            "longQuestions": lq_objs
        },
        "sloBank": {
            "mcqs": [],
            "shortQuestions": [],
            "longQuestions": []
        },
        "englishSummary": summary,
        "urduSummary": "",
        "pashtoSummary": ""
    }


# Process all units
all_units = []
for unit_meta in UNITS:
    u = unit_meta['number']
    if u in unit_starts:
        s = unit_starts[u]
        e = unit_ends[u]
        main_paras, ex_paras, short_qs, long_qs, mcqs = extract_unit_content(u, s, e, all_paras)
        print(f"Unit {u:2d}: {len(main_paras)} main paras, {len(short_qs)} short Qs, {len(long_qs)} long Qs, {len(mcqs)} MCQs extracted")
    else:
        main_paras = []
        short_qs = []
        long_qs = []
        mcqs = []
        print(f"Unit {u:2d}: NO BOUNDARY - using defaults")
    
    summary = UNIT_SUMMARIES.get(u, f"Summary for Unit {u}: {unit_meta['title']}.")
    unit_obj = build_unit(unit_meta, main_paras, short_qs, long_qs, mcqs, summary)
    all_units.append(unit_obj)

print(f"\nTotal units built: {len(all_units)}")

# Serialize to JSON
units_json = json.dumps(all_units, ensure_ascii=False, indent=2)

# Write JS file
js_content = f"""/**
 * SpaceBook - Class 12 English Verbatim Dataset (KPK Textbook Board)
 * Complete {len(all_units)} Units verbatim from official textbook
 * Generated by extract_english_12.py
 */

const ENGLISH_12_DATA = {units_json};

if (typeof DATA !== 'undefined' && DATA) {{
  DATA.eng12Chapters = ENGLISH_12_DATA;
}}
if (typeof window !== 'undefined') {{
  window.ENGLISH_12_DATA = ENGLISH_12_DATA;
}}
"""

with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"\nWritten: {OUTPUT_JS}")
print(f"File size: {os.path.getsize(OUTPUT_JS):,} bytes")

# Quick validation
with open(OUTPUT_JS, encoding='utf-8') as f:
    content = f.read()

import re
found_units = re.findall(r'"number": (\d+)', content)
print(f"Units in output file: {found_units}")
print(f"Has window.ENGLISH_12_DATA: {'window.ENGLISH_12_DATA' in content}")
print(f"Has DATA.eng12Chapters: {'DATA.eng12Chapters' in content}")
print("\nDONE!")
