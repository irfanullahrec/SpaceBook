/* ======================================================================
 *  data.js - core registry (SHARED FILE - maintainers own it)
 *  Contains: stats, classes, subjects, roadmap chapter map, studyPlan, books
 *
 *  Per-subject curriculum data lives in sibling files so that each
 *  contributor edits exactly one file (see CONTRIBUTING.md):
 *    data_chem.js  data_phys.js  data_eng.js  data_bio.js
 * ====================================================================== */
const DATA = {
  "stats": [
    {
      "label": "Active Units",
      "value": "9 Units",
      "icon": "🧬",
      "color": "#e0f2fe"
    },
    {
      "label": "Textbook MCQs",
      "value": "96 MCQs",
      "icon": "🎯",
      "color": "#f0fdf4"
    },
    {
      "label": "Short Questions",
      "value": "52 SQs",
      "icon": "✏️",
      "color": "#fefce8"
    },
    {
      "label": "Detailed Questions",
      "value": "36 LQs",
      "icon": "📝",
      "color": "#f5f3ff"
    }
  ],
  "classes": [
    {
      "id": "cls-pg",
      "name": "Play Group",
      "emoji": "🎨",
      "subjects": 4
    },
    {
      "id": "cls-nur",
      "name": "Nursery",
      "emoji": "🧸",
      "subjects": 4
    },
    {
      "id": "cls-kg",
      "name": "KG",
      "emoji": "🎈",
      "subjects": 4
    },
    {
      "id": "cls1",
      "name": "Class 1",
      "emoji": "✏️",
      "subjects": 8
    },
    {
      "id": "cls2",
      "name": "Class 2",
      "emoji": "📖",
      "subjects": 8
    },
    {
      "id": "cls3",
      "name": "Class 3",
      "emoji": "📚",
      "subjects": 7
    },
    {
      "id": "cls4",
      "name": "Class 4",
      "emoji": "🎒",
      "subjects": 6
    },
    {
      "id": "cls5",
      "name": "Class 5",
      "emoji": "🔬",
      "subjects": 6
    },
    {
      "id": "cls6",
      "name": "Class 6",
      "emoji": "📐",
      "subjects": 7
    },
    {
      "id": "cls7",
      "name": "Class 7",
      "emoji": "🧪",
      "subjects": 7
    },
    {
      "id": "cls8",
      "name": "Class 8",
      "emoji": "⚛️",
      "subjects": 7
    },
    {
      "id": "cls9",
      "name": "Class 9",
      "emoji": "🏫",
      "subjects": 9
    },
    {
      "id": "cls10",
      "name": "Class 10",
      "emoji": "🏫",
      "subjects": 8
    },
    {
      "id": "cls11",
      "name": "Class 11",
      "emoji": "🏛️",
      "subjects": 5
    },
    {
      "id": "cls12",
      "name": "Class 12",
      "emoji": "🎓",
      "subjects": 6
    }
  ],
  "subjects": {
    "cls-pg": [
      { "id": "cls-pg-eng",  "name": "English Basics", "nameUrdu": "بنیادی انگریزی", "emoji": "🔤", "chapters": 8 },
      { "id": "cls-pg-urdu", "name": "Urdu Haroof",    "nameUrdu": "حروفِ تہجی",     "emoji": "📗", "chapters": 8 },
      { "id": "cls-pg-math", "name": "Basic Math",     "nameUrdu": "بنیادی ریاضی",   "emoji": "🔢", "chapters": 8 },
      { "id": "cls-pg-art",  "name": "Art & Rhymes",   "nameUrdu": "رنگ و نظمیں",    "emoji": "🎨", "chapters": 6 }
    ],
    "cls-nur": [
      { "id": "cls-nur-eng",  "name": "English",           "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 10 },
      { "id": "cls-nur-urdu", "name": "Urdu",              "nameUrdu": "اردو",           "emoji": "📗", "chapters": 10 },
      { "id": "cls-nur-math", "name": "Mathematics",       "nameUrdu": "ریاضی",          "emoji": "🔢", "chapters": 10 },
      { "id": "cls-nur-gk",   "name": "General Knowledge", "nameUrdu": "واقفیتِ عامہ",   "emoji": "🌍", "chapters": 8 }
    ],
    "cls-kg": [
      { "id": "cls-kg-eng",  "name": "English",           "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 12 },
      { "id": "cls-kg-urdu", "name": "Urdu",              "nameUrdu": "اردو",           "emoji": "📗", "chapters": 12 },
      { "id": "cls-kg-math", "name": "Mathematics",       "nameUrdu": "ریاضی",          "emoji": "🔢", "chapters": 12 },
      { "id": "cls-kg-gk",   "name": "General Knowledge", "nameUrdu": "واقفیتِ عامہ",   "emoji": "🌱", "chapters": 10 }
    ],
    "cls1": [
      { "id": "cls1-eng",  "name": "English",           "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 11, "hasEng": true, "hasEng1": true },
      { "id": "cls1-urdu", "name": "Urdu",              "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 12 },
      { "id": "cls1-math", "name": "Mathematics",       "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 6 },
      { "id": "cls1-gk",   "name": "General Knowledge", "nameUrdu": "واقفیتِ عامہ",   "emoji": "🌍", "chapters": 10 },
      { "id": "cls1-isl",  "name": "Islamyat",          "nameUrdu": "اسلامیات",            "emoji": "🕌", "chapters": 10, "hasIsl": true, "hasIsl1": true },
      { "id": "cls1-nazira", "name": "Nazira Quran",    "nameUrdu": "ناظرہ قرآن",          "emoji": "📖", "chapters": 17, "hasNazira": true, "hasNazira1": true },
      { "id": "cls1-pashto", "name": "Pashto",          "nameUrdu": "پښتو (لازمي)",        "emoji": "📚", "chapters": 23, "hasPashto": true, "hasPashto1": true },
      { "id": "cls1-drawing", "name": "Drawing",         "nameUrdu": "تخلیقی فنون و ڈرائنگ", "emoji": "🎨", "chapters": 32, "hasDrawing": true }
    ],
    "cls2": [
      { "id": "cls2-eng",     "name": "English",           "nameUrdu": "انگریزی",             "emoji": "📖", "chapters": 12, "hasEng": true, "hasEng2": true },
      { "id": "cls2-urdu",    "name": "Urdu",              "nameUrdu": "اردو لازمی",          "emoji": "📗", "chapters": 22, "hasUrdu": true, "hasUrdu2": true },
      { "id": "cls2-math",    "name": "Mathematics",       "nameUrdu": "ریاضی",               "emoji": "📐", "chapters": 6,  "hasMath": true, "hasMath2": true },
      { "id": "cls2-gk",      "name": "General Knowledge", "nameUrdu": "واقفیتِ عامہ",        "emoji": "🌍", "chapters": 16, "hasGk": true, "hasGk2": true },
      { "id": "cls2-isl",     "name": "Islamyat",          "nameUrdu": "اسلامیات",            "emoji": "🕌", "chapters": 11, "hasIsl": true, "hasIsl2": true },
      { "id": "cls2-nazira",  "name": "Nazira Quran",      "nameUrdu": "ناظرہ قرآن",          "emoji": "📖", "chapters": 15, "hasNazira": true, "hasNazira2": true },
      { "id": "cls2-pashto",  "name": "Pashto",            "nameUrdu": "پښتو (لازمي)",        "emoji": "📚", "chapters": 28, "hasPashto": true, "hasPashto2": true },
      { "id": "cls2-drawing", "name": "Drawing",           "nameUrdu": "تخلیقی فنون و ڈرائنگ", "emoji": "🎨", "chapters": 32, "hasDrawing": true }
    ],
    "cls3": [
      { "id": "cls3-eng",     "name": "English",         "nameUrdu": "انگریزی",             "emoji": "📖", "chapters": 14 },
      { "id": "cls3-urdu",    "name": "Urdu",            "nameUrdu": "اردو لازمی",          "emoji": "📗", "chapters": 14 },
      { "id": "cls3-math",    "name": "Mathematics",     "nameUrdu": "ریاضی",               "emoji": "📐", "chapters": 10 },
      { "id": "cls3-sci",     "name": "General Science", "nameUrdu": "جنرل سائنس",          "emoji": "🔬", "chapters": 10 },
      { "id": "cls3-isl",     "name": "Islamyat",        "nameUrdu": "اسلامیات",            "emoji": "🕌", "chapters": 18, "hasIsl": true, "hasIsl3": true },
      { "id": "cls3-nazira",  "name": "Nazira Quran",    "nameUrdu": "ناظرہ قرآن",          "emoji": "📖", "chapters": 16, "hasNazira": true, "hasNazira3": true },
      { "id": "cls3-drawing", "name": "Drawing",         "nameUrdu": "تخلیقی فنون و ڈرائنگ", "emoji": "🎨", "chapters": 32, "hasDrawing": true }
    ],
    "cls4": [
      { "id": "cls4-eng",  "name": "English",         "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 14 },
      { "id": "cls4-urdu", "name": "Urdu",            "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 14 },
      { "id": "cls4-math", "name": "Mathematics",     "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 10 },
      { "id": "cls4-sci",  "name": "General Science", "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 10 },
      { "id": "cls4-sst",  "name": "Social Studies",  "nameUrdu": "معاشرتی علوم",   "emoji": "🗺️", "chapters": 8 },
      { "id": "cls4-isl",  "name": "Islamyat",        "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 10 }
    ],
    "cls5": [
      { "id": "cls5-eng",  "name": "English",         "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 15 },
      { "id": "cls5-urdu", "name": "Urdu",            "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 15 },
      { "id": "cls5-math", "name": "Mathematics",     "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 10 },
      { "id": "cls5-sci",  "name": "General Science", "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 10 },
      { "id": "cls5-sst",  "name": "Social Studies",  "nameUrdu": "معاشرتی علوم",   "emoji": "🗺️", "chapters": 8 },
      { "id": "cls5-isl",  "name": "Islamyat",        "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 10 }
    ],
    "cls6": [
      { "id": "cls6-eng",  "name": "English",             "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 15 },
      { "id": "cls6-urdu", "name": "Urdu",                "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 15 },
      { "id": "cls6-math", "name": "Mathematics",         "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 12 },
      { "id": "cls6-sci",  "name": "General Science",     "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 12 },
      { "id": "cls6-hg",   "name": "History & Geography", "nameUrdu": "تاریخ و جغرافیہ", "emoji": "🌍", "chapters": 10 },
      { "id": "cls6-comp", "name": "Computer Education",  "nameUrdu": "کمپیوٹر",        "emoji": "💻", "chapters": 8 },
      { "id": "cls6-isl",  "name": "Islamyat",            "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 12 }
    ],
    "cls7": [
      { "id": "cls7-eng",  "name": "English",             "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 15 },
      { "id": "cls7-urdu", "name": "Urdu",                "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 15 },
      { "id": "cls7-math", "name": "Mathematics",         "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 12 },
      { "id": "cls7-sci",  "name": "General Science",     "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 12 },
      { "id": "cls7-hg",   "name": "History & Geography", "nameUrdu": "تاریخ و جغرافیہ", "emoji": "🌍", "chapters": 10 },
      { "id": "cls7-comp", "name": "Computer Education",  "nameUrdu": "کمپیوٹر",        "emoji": "💻", "chapters": 8 },
      { "id": "cls7-isl",  "name": "Islamyat",            "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 12 }
    ],
    "cls8": [
      { "id": "cls8-eng",  "name": "English",             "nameUrdu": "انگریزی",        "emoji": "📖", "chapters": 15 },
      { "id": "cls8-urdu", "name": "Urdu",                "nameUrdu": "اردو لازمی",     "emoji": "📗", "chapters": 15 },
      { "id": "cls8-math", "name": "Mathematics",         "nameUrdu": "ریاضی",          "emoji": "📐", "chapters": 12 },
      { "id": "cls8-sci",  "name": "General Science",     "nameUrdu": "جنرل سائنس",     "emoji": "🔬", "chapters": 12 },
      { "id": "cls8-hg",   "name": "History & Geography", "nameUrdu": "تاریخ و جغرافیہ", "emoji": "🌍", "chapters": 10 },
      { "id": "cls8-comp", "name": "Computer Education",  "nameUrdu": "کمپیوٹر",        "emoji": "💻", "chapters": 8 },
      { "id": "cls8-isl",  "name": "Islamyat",            "nameUrdu": "اسلامیات",       "emoji": "🕌", "chapters": 12 }
    ],
    "cls9": [
      {
        "id": "cls9-math",
        "name": "Mathematics",
        "emoji": "📐",
        "chapters": 17,
        "hasMath": true
      },
      {
        "id": "cls9-phy",
        "name": "Physics",
        "emoji": "⚛️",
        "chapters": 9,
        "hasPhys": true
      },
      {
        "id": "cls9-chem",
        "name": "Chemistry",
        "emoji": "🧪",
        "chapters": 8,
        "hasChem": true
      },
      {
        "id": "cls9-bio",
        "name": "Biology",
        "emoji": "🧬",
        "chapters": 9,
        "hasBio": true
      },
      {
        "id": "cls9-eng",
        "name": "English",
        "emoji": "📖",
        "chapters": 15,
        "hasEng": true
      },
      {
        "id": "cls9-urdu",
        "name": "Urdu",
        "emoji": "📗",
        "chapters": 19,
        "hasUrdu": true
      },
      {
        "id": "cls9-isl",
        "name": "Islamyat",
        "emoji": "🕌",
        "chapters": 15,
        "hasIsl": true
      },
      {
        "id": "cls9-comp",
        "name": "Computer Science",
        "emoji": "💻",
        "chapters": 7,
        "hasComp": true
      },
      {
        "id": "cls9-pakstudy",
        "name": "Pakistan Studies",
        "nameUrdu": "مطالعہ پاکستان",
        "emoji": "🇵🇰",
        "chapters": 4,
        "hasPakStudy": true
      }
    ],
    "cls10": [
      {
        "id": "cls10-math",
        "name": "Mathematics",
        "emoji": "📐",
        "chapters": 13,
        "hasMath": true
      },
      {
        "id": "cls10-phy",
        "name": "Physics",
        "emoji": "⚡",
        "chapters": 9,
        "hasPhys10": true
      },
      {
        "id": "cls10-chem",
        "name": "Chemistry",
        "emoji": "🧪",
        "chapters": 8,
        "hasChem10": true
      },
      {
        "id": "cls10-bio",
        "name": "Biology",
        "emoji": "🧬",
        "chapters": 9,
        "hasBio10": true
      },
      {
        "id": "cls10-eng",
        "name": "English",
        "emoji": "📖",
        "chapters": 15,
        "hasEng": true,
        "hasEng10": true
      },
      {
        "id": "cls10-pakstudy",
        "name": "Pakistan Studies",
        "nameUrdu": "مطالعہ پاکستان",
        "emoji": "🇵🇰",
        "chapters": 4,
        "hasPakStudy": true,
        "hasPakStudy10": true
      },
      {
        "id": "cls10-isl",
        "name": "Islamyat",
        "emoji": "🕌",
        "chapters": 18,
        "hasIsl": true,
        "hasIsl10": true
      },
      {
        "id": "cls10-urdu",
        "name": "Urdu",
        "nameUrdu": "اردو لازمی",
        "emoji": "📗",
        "chapters": 22,
        "hasUrdu": true,
        "hasUrdu10": true
      }
    ],
    "cls11": [
      {
        "id": "cls11-math",
        "name": "Mathematics",
        "emoji": "📐",
        "chapters": 14
      },
      {
        "id": "cls11-phy",
        "name": "Physics",
        "emoji": "⚡",
        "chapters": 11
      },
      {
        "id": "cls11-chem",
        "name": "Chemistry",
        "emoji": "🧪",
        "chapters": 11
      },
      {
        "id": "cls11-bio",
        "name": "Biology",
        "emoji": "🧬",
        "chapters": 10
      },
      {
        "id": "cls11-eng",
        "name": "English",
        "emoji": "📖",
        "chapters": 9
      }
    ],
    "cls12": [
      {
        "id": "cls12-math",
        "name": "Mathematics",
        "emoji": "📐",
        "chapters": 7
      },
      {
        "id": "cls12-phy",
        "name": "Physics",
        "emoji": "⚡",
        "chapters": 10
      },
      {
        "id": "cls12-chem",
        "name": "Chemistry",
        "emoji": "🧪",
        "chapters": 16
      },
      {
        "id": "cls12-bio",
        "name": "Biology",
        "emoji": "🧬",
        "chapters": 13
      },
      {
        "id": "cls12-eng",
        "name": "English",
        "emoji": "📖",
        "chapters": 8
      },
      {
        "id": "cls12-pak",
        "name": "Pak Studies",
        "emoji": "🌙",
        "chapters": 6
      }
    ]
  },
  "chapters": {
    "cls9-math": [
      {
        "num": 1,
        "name": "Matrices and Determinants",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Real and Complex Numbers",
        "topics": "3 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Logarithms",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 4,
        "name": "Algebraic Expressions",
        "topics": "4 Topics",
        "status": "progress"
      },
      {
        "num": 5,
        "name": "Factorization",
        "topics": "5 Topics",
        "status": "progress"
      },
      {
        "num": 6,
        "name": "Algebraic Manipulation",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Linear Equations & Inequalities",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Linear Graphs & Equations",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 9,
        "name": "Coordinate Geometry",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 10,
        "name": "Congruent Triangles",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 11,
        "name": "Parallelograms & Triangles",
        "topics": "3 Topics",
        "status": "upcoming"
      }
    ],
    "cls9-phy": [
      {
        "num": 1,
        "name": "Physical Quantities & Measurement",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Kinematics",
        "topics": "6 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Dynamics",
        "topics": "5 Topics",
        "status": "progress"
      },
      {
        "num": 4,
        "name": "Turning Effect of Forces",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 5,
        "name": "Gravitation",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 6,
        "name": "Work and Energy",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Properties of Matter",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Thermal Properties of Matter",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 9,
        "name": "Transfer of Heat",
        "topics": "3 Topics",
        "status": "upcoming"
      }
    ],
    "cls9-chem": [
      {
        "num": 1,
        "name": "Fundamentals of Chemistry",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Structure of Atoms",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Periodic Table & Periodicity",
        "topics": "4 Topics",
        "status": "progress"
      },
      {
        "num": 4,
        "name": "Structure of Molecules",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 5,
        "name": "Physical States of Matter",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 6,
        "name": "Solutions",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Electrochemistry",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Chemical Reactivity",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 9,
        "name": "Biochemistry",
        "topics": "3 Topics",
        "status": "upcoming"
      }
    ],
    "cls12-phy": [
      {
        "num": 1,
        "name": "Electrostatics",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Current Electricity",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Electromagnetism",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 4,
        "name": "Electromagnetic Induction",
        "topics": "5 Topics",
        "status": "progress"
      },
      {
        "num": 5,
        "name": "Alternating Current",
        "topics": "4 Topics",
        "status": "progress"
      },
      {
        "num": 6,
        "name": "Physics of Solids",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Electronics",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Dawn of Modern Physics",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 9,
        "name": "Atomic Spectra",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 10,
        "name": "Nuclear Physics",
        "topics": "5 Topics",
        "status": "upcoming"
      }
    ],
    "cls12-chem": [
      {
        "num": 1,
        "name": "Periodic Classification & Periodicity",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "s-Block Elements",
        "topics": "3 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Group IIIA and IVA Elements",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 4,
        "name": "Group VA and VIA Elements",
        "topics": "4 Topics",
        "status": "progress"
      },
      {
        "num": 5,
        "name": "The Halogens and Noble Gases",
        "topics": "3 Topics",
        "status": "progress"
      },
      {
        "num": 6,
        "name": "Transition Elements",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Fundamental Principles of Organic Chemistry",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Aliphatic Hydrocarbons",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 9,
        "name": "Aromatic Hydrocarbons",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 10,
        "name": "Alkyl Halides",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 11,
        "name": "Alcohols, Phenols and Ethers",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 12,
        "name": "Aldehydes and Ketones",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 13,
        "name": "Carboxylic Acids",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 14,
        "name": "Macromolecules",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 15,
        "name": "Common Chemical Industries in Pakistan",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 16,
        "name": "Environmental Chemistry",
        "topics": "3 Topics",
        "status": "upcoming"
      }
    ],
    "cls12-bio": [
      {
        "num": 1,
        "name": "Homeostasis",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Support and Movement",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Coordination and Control",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 4,
        "name": "Reproduction",
        "topics": "5 Topics",
        "status": "progress"
      },
      {
        "num": 5,
        "name": "Growth and Development",
        "topics": "3 Topics",
        "status": "progress"
      },
      {
        "num": 6,
        "name": "Chromosomes and DNA",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Cell Cycle",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Variation and Genetics",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 9,
        "name": "Biotechnology",
        "topics": "4 Topics",
        "status": "upcoming"
      },
      {
        "num": 10,
        "name": "Evolution",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 11,
        "name": "Ecosystem",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 12,
        "name": "Some Major Ecosystems",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 13,
        "name": "Man and His Environment",
        "topics": "3 Topics",
        "status": "upcoming"
      }
    ],
    "cls12-math": [
      {
        "num": 1,
        "name": "Functions and Limits",
        "topics": "5 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Differentiation",
        "topics": "6 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Integration",
        "topics": "6 Topics",
        "status": "progress"
      },
      {
        "num": 4,
        "name": "Introduction to Analytic Geometry",
        "topics": "5 Topics",
        "status": "progress"
      },
      {
        "num": 5,
        "name": "Linear Inequalities and Linear Programming",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 6,
        "name": "Conic Sections",
        "topics": "5 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "Vectors",
        "topics": "4 Topics",
        "status": "upcoming"
      }
    ],
    "cls12-eng": [
      {
        "num": 1,
        "name": "Twenty Minutes with Mrs. Oakentubb",
        "topics": "3 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Reflections on the Re-Awakening East",
        "topics": "3 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "The Day the Dam Broke",
        "topics": "3 Topics",
        "status": "progress"
      },
      {
        "num": 4,
        "name": "Pakistan and the Modern World",
        "topics": "3 Topics",
        "status": "progress"
      },
      {
        "num": 5,
        "name": "Act III of the Silver Box",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 6,
        "name": "The World As I See It",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 7,
        "name": "The Devoted Friend",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 8,
        "name": "Grammar & Composition",
        "topics": "4 Topics",
        "status": "upcoming"
      }
    ],
    "cls12-pak": [
      {
        "num": 1,
        "name": "Islam and Pakistan",
        "topics": "3 Topics",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Political & Constitutional Development",
        "topics": "4 Topics",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Administrative Structure of Pakistan",
        "topics": "3 Topics",
        "status": "progress"
      },
      {
        "num": 4,
        "name": "Foreign Policy of Pakistan",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 5,
        "name": "Economic Planning & Development",
        "topics": "3 Topics",
        "status": "upcoming"
      },
      {
        "num": 6,
        "name": "Culture and Society of Pakistan",
        "topics": "3 Topics",
        "status": "upcoming"
      }
    ],
    "cls9-eng": [
      {
        "num": 1,
        "name": "Hazrat Muhammad (SAW) the Model of Tolerance",
        "topics": "7 Words · 0 SQs · 5 MCQs",
        "status": "done"
      },
      {
        "num": 2,
        "name": "Iqbal's Message to Youth",
        "topics": "6 Words · 0 SQs · 5 MCQs",
        "status": "done"
      },
      {
        "num": 3,
        "name": "Quaid — A Great Leader",
        "topics": "5 Words · 0 SQs · 3 MCQs",
        "status": "done"
      },
      {
        "num": 4,
        "name": "The Daffodils",
        "topics": "8 Words · 0 SQs · 3 MCQs",
        "status": "done"
      },
      {
        "num": 5,
        "name": "The Madina Charter",
        "topics": "8 Words · 0 SQs · 3 MCQs",
        "status": "done"
      },
      {
        "num": 6,
        "name": "Nasiruddin",
        "topics": "16 Words · 7 SQs · 0 MCQs",
        "status": "done"
      },
      {
        "num": 7,
        "name": "The Two Bargains",
        "topics": "11 Words · 9 SQs · 5 MCQs",
        "status": "done"
      },
      {
        "num": 8,
        "name": "Hope is the Thing with Feathers",
        "topics": "8 Words · 8 SQs · 5 MCQs",
        "status": "done"
      },
      {
        "num": 9,
        "name": "The Fantastic Shoemaker",
        "topics": "22 Words · 10 SQs · 4 MCQs",
        "status": "done"
      },
      {
        "num": 10,
        "name": "Technology in Everyday Life",
        "topics": "11 Words · 7 SQs · 5 MCQs",
        "status": "done"
      },
      {
        "num": 11,
        "name": "Safety First",
        "topics": "9 Words · 5 SQs · 4 MCQs",
        "status": "done"
      },
      {
        "num": 12,
        "name": "The Old Woman",
        "topics": "4 Words · 7 SQs · 5 MCQs",
        "status": "done"
      },
      {
        "num": 13,
        "name": "Letter to the Newspaper Editor",
        "topics": "10 Words · 6 SQs · 0 MCQs",
        "status": "done"
      },
      {
        "num": 14,
        "name": "Biodiversity in Pakistan",
        "topics": "9 Words · 6 SQs · 0 MCQs",
        "status": "done"
      },
      {
        "num": 15,
        "name": "Abou Ben Adhem",
        "topics": "8 Words · 6 SQs · 5 MCQs",
        "status": "done"
      }
    ],
    "cls10-bio": [
      {
        "num": 10,
        "name": "Gaseous Exchange",
        "topics": "5 Topics · Pages 1 – 15",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 11,
        "name": "Homeostasis",
        "topics": "5 Topics · Pages 16 – 31",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 12,
        "name": "Coordination and Control",
        "topics": "4 Topics · Pages 32 – 55",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 13,
        "name": "Support and Movement",
        "topics": "5 Topics · Pages 56 – 70",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 14,
        "name": "Reproduction",
        "topics": "3 Topics · Pages 71 – 96",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 15,
        "name": "Inheritance",
        "topics": "4 Topics · Pages 97 – 116",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 16,
        "name": "Man and His Environment",
        "topics": "4 Topics · Pages 117 – 149",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 17,
        "name": "Biotechnology",
        "topics": "4 Topics · Pages 150 – 163",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 18,
        "name": "Pharmacology",
        "topics": "4 Topics · Pages 164 – 186",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      }
    ],
    "cls10-phy": [
      {
        "num": 10,
        "name": "Simple Harmonic Motion and Waves",
        "topics": "3 Topics · 7 Numericals · Pages 1 – 26",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 11,
        "name": "Sound",
        "topics": "4 Topics · 8 Numericals · Pages 27 – 51",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 12,
        "name": "Geometrical Optics",
        "topics": "4 Topics · 8 Numericals · Pages 52 – 103",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 13,
        "name": "Electrostatics",
        "topics": "4 Topics · 7 Numericals · Pages 108 – 135",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 14,
        "name": "Current Electricity",
        "topics": "4 Topics · 7 Numericals · Pages 134 – 170",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 15,
        "name": "Electromagnetism",
        "topics": "4 Topics · 7 Numericals · Pages 171 – 197",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 16,
        "name": "Introductory Electronics",
        "topics": "4 Topics · 0 Numericals · Pages 198 – 214",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 17,
        "name": "Information and Communication Technology",
        "topics": "4 Topics · 0 Numericals · Pages 215 – 235",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      },
      {
        "num": 18,
        "name": "Radioactivity and Nuclear Physics",
        "topics": "4 Topics · 6 Numericals · Pages 236 – 266",
        "status": "ready",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 10–18)"
      }
    ],
    "cls10-chem": [
      {
        "num": 9,
        "name": "Chemical Equilibrium",
        "topics": "4 Topics (11 Subtopics) · 4 Numericals · Pages 1 – 20 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Chemical Equilibrium"
      },
      {
        "num": 10,
        "name": "Acids, Bases and Salts",
        "topics": "3 Topics (11 Subtopics) · 6 Numericals · Pages 21 – 48 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Acids, Bases and Salts"
      },
      {
        "num": 11,
        "name": "Organic Chemistry",
        "topics": "5 Topics (11 Subtopics) · Pages 49 – 74 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Organic Chemistry"
      },
      {
        "num": 12,
        "name": "Hydrocarbons",
        "topics": "4 Topics (8 Subtopics) · Pages 75 – 100 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Hydrocarbons"
      },
      {
        "num": 13,
        "name": "Biochemistry",
        "topics": "5 Topics (10 Subtopics) · Pages 101 – 125 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Biochemistry"
      },
      {
        "num": 14,
        "name": "Environmental Chemistry I: Atmosphere",
        "topics": "5 Topics (9 Subtopics) · Pages 126 – 156 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Environmental Chemistry I: Atmosphere"
      },
      {
        "num": 15,
        "name": "Environmental Chemistry II: Water",
        "topics": "5 Topics (11 Subtopics) · Pages 157 – 186 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Environmental Chemistry II: Water"
      },
      {
        "num": 16,
        "name": "Chemical Industries",
        "topics": "4 Topics (8 Subtopics) · 2 Numericals · Pages 187 – 212 (Book)",
        "status": "done",
        "progress": 100,
        "isVerified": true,
        "verifiedTag": "KPK Textbook Board (Units 9–16)",
        "title": "Chemical Industries"
      }
    ],
    "cls10-eng": [
      {
            "num": 1,
            "unit": 1,
            "name": "Simplicity and Humility of Hazrat Muhammad (PBUH)",
            "title": "Simplicity and Humility of Hazrat Muhammad (PBUH)",
            "topics": "12 Words · 5 SQs · 5 MCQs",
            "status": "done"
      },
      {
            "num": 2,
            "unit": 2,
            "name": "The Champions",
            "title": "The Champions",
            "topics": "7 Words · 5 SQs · 5 MCQs",
            "status": "done"
      },
      {
            "num": 3,
            "unit": 3,
            "name": "Dreams",
            "title": "Dreams",
            "topics": "5 Words · 5 SQs · 5 MCQs",
            "status": "done"
      },
      {
            "num": 4,
            "unit": 4,
            "name": "Population Growth and its Impact on Environment",
            "title": "Population Growth and its Impact on Environment",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 5,
            "unit": 5,
            "name": "The Great Masjid of Cordoba and Iqbal",
            "title": "The Great Masjid of Cordoba and Iqbal",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 6,
            "unit": 6,
            "name": "In Spite of War",
            "title": "In Spite of War",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 7,
            "unit": 7,
            "name": "The Aged Mother",
            "title": "The Aged Mother",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 8,
            "unit": 8,
            "name": "Women's Role in the Pakistan Movement",
            "title": "Women's Role in the Pakistan Movement",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 9,
            "unit": 9,
            "name": "Equipment",
            "title": "Equipment",
            "topics": "5 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 10,
            "unit": 10,
            "name": "Water Scarcity in Pakistan",
            "title": "Water Scarcity in Pakistan",
            "topics": "6 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 11,
            "unit": 11,
            "name": "Genetically Modified Organisms (GMOs)",
            "title": "Genetically Modified Organisms (GMOs)",
            "topics": "6 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 12,
            "unit": 12,
            "name": "They Have Cut Down the Pines",
            "title": "They Have Cut Down the Pines",
            "topics": "5 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 13,
            "unit": 13,
            "name": "Hazrat Umar (R.A)",
            "title": "Hazrat Umar (R.A)",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 14,
            "unit": 14,
            "name": "The Model Millionaire",
            "title": "The Model Millionaire",
            "topics": "7 Words · 4 SQs · 4 MCQs",
            "status": "done"
      },
      {
            "num": 15,
            "unit": 15,
            "name": "Opportunity",
            "title": "Opportunity",
            "topics": "6 Words · 4 SQs · 4 MCQs",
            "status": "done"
      }
]
  },
  "studyPlan": [
    {
      "day": "Day 1 — Concepts & Topics",
      "subject": "Biology — Read Theory & Notes",
      "time": "4:00 PM – 5:30 PM",
      "progress": 90
    },
    {
      "day": "Day 2 — Definitions & Diagrams",
      "subject": "Biology — Draw Diagrams & Tables",
      "time": "4:00 PM – 5:30 PM",
      "progress": 80
    },
    {
      "day": "Day 3 — Textbook Short Questions",
      "subject": "Biology — Write & Memorize SQs",
      "time": "3:30 PM – 5:00 PM",
      "progress": 85
    },
    {
      "day": "Day 4 — Textbook Long Questions",
      "subject": "Biology — Structure Long Question Notes",
      "time": "4:00 PM – 5:30 PM",
      "progress": 70
    },
    {
      "day": "Day 5 — MCQs & Chapter Test",
      "subject": "Biology — Solve MCQs & Self-Assessment",
      "time": "4:00 PM – 5:30 PM",
      "progress": 60
    }
  ],
  "books": [
    {
      "id": "b-cls1-eng",
      "classId": "cls1",
      "class_id": "cls1",
      "className": "Class 1",
      "class_name": "Class 1",
      "subject": "English (Compulsory)",
      "title": "English 1st Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "9.47 MB",
      "pages": "Complete 11 Units & 4 Reviews",
      "pdfPath": "assets/books/Class-1-English-KPK.pdf",
      "pdf_path": "assets/books/Class-1-English-KPK.pdf",
      "color": "#4f46e5",
      "icon": "📖",
      "available": true,
      "action": "cls1-eng",
      "hub_action": "cls1-eng",
      "subject_id": 1
    },
    {
      "id": "b-cls1-isl",
      "classId": "cls1",
      "class_id": "cls1",
      "className": "Class 1",
      "class_name": "Class 1",
      "subject": "Islamyat (Compulsory)",
      "title": "Islamyat 1st Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "15.34 MB",
      "pages": "Complete 10 Units (5 Babs)",
      "pdfPath": "assets/books/Class-1-Islamyat-KPK.pdf",
      "pdf_path": "assets/books/Class-1-Islamyat-KPK.pdf",
      "color": "#0d9488",
      "icon": "🕌",
      "available": true,
      "action": "cls1-isl",
      "hub_action": "cls1-isl",
      "subject_id": 5
    },
    {
      "id": "b-cls1-nazira",
      "classId": "cls1",
      "class_id": "cls1",
      "className": "Class 1",
      "class_name": "Class 1",
      "subject": "Nazira Quran",
      "title": "Nazira Quran 1st Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "12.16 MB",
      "pages": "Complete 17 Lessons (Tajweed & Surahs)",
      "pdfPath": "assets/books/Class-1-Nazira-KPK.pdf",
      "pdf_path": "assets/books/Class-1-Nazira-KPK.pdf",
      "color": "#059669",
      "icon": "📖",
      "available": true,
      "action": "cls1-nazira",
      "hub_action": "cls1-nazira",
      "subject_id": 6
    },
    {
      "id": "b-cls1-pashto",
      "classId": "cls1",
      "class_id": "cls1",
      "className": "Class 1",
      "class_name": "Class 1",
      "subject": "Pashto (Compulsory)",
      "title": "Pashto 1st Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "29.17 MB",
      "pages": "Complete 23 Units (88 Pages)",
      "pdfPath": "assets/books/Class-1-Pashto-KPK.pdf",
      "pdf_path": "assets/books/Class-1-Pashto-KPK.pdf",
      "color": "#0d9488",
      "icon": "📚",
      "available": true,
      "action": "cls1-pashto",
      "hub_action": "cls1-pashto",
      "subject_id": 7
    },
    {
      "id": "b-cls10-eng",
      "classId": "cls10",
      "class_id": "cls10",
      "className": "Class 10",
      "class_name": "Class 10",
      "subject": "English (Compulsory)",
      "title": "English 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "25.9 MB",
      "pages": "Complete 15 Units (161 Pages)",
      "pdfPath": "assets/books/Class-10-English-KPK.pdf",
      "pdf_path": "assets/books/Class-10-English-KPK.pdf",
      "color": "#0284c7",
      "icon": "📖",
      "available": true,
      "action": "cls10-eng",
      "hub_action": "cls10-eng",
      "subject_id": 21
    },
    {
      "id": "b-cls9-bio",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "Biology",
      "title": "Biology 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "28.4 MB",
      "pages": "Complete 9 Units",
      "pdfPath": "assets/books/Class-9-Biology-KPK.pdf",
      "color": "#10b981",
      "icon": "🧬",
      "available": true,
      "action": "cls9-bio"
    },
    {
      "id": "b-cls9-chem",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "Chemistry",
      "title": "Chemistry 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "58.5 MB",
      "pages": "Complete 8 Units",
      "pdfPath": "assets/books/Class-9-Chemistry-KPK.pdf",
      "color": "#0284c7",
      "icon": "🧪",
      "available": true,
      "action": "cls9-chem"
    },
    {
      "id": "b-cls9-phys",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "Physics",
      "title": "Physics 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "32.5 MB",
      "pages": "9 Chapters + 33 Numericals",
      "pdfPath": "assets/books/Class-9-Physics-KPK.pdf",
      "color": "#7c3aed",
      "icon": "⚛️",
      "available": true,
      "action": "cls9-phy"
    },
    {
      "id": "b-cls9-eng",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "English (Compulsory)",
      "title": "English 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "18.4 MB",
      "pages": "Complete 15 Units",
      "pdfPath": "assets/books/Class-9-English-KPK.pdf",
      "color": "#f59e0b",
      "icon": "📖",
      "available": true,
      "action": "cls9-eng"
    },
    {
      "id": "b-cls9-math",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "Mathematics",
      "title": "Mathematics 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "11.9 MB",
      "pages": "Complete 11 Units",
      "pdfPath": "assets/books/Class-9-Mathematics-KPK.pdf",
      "color": "#ef4444",
      "icon": "📐",
      "available": true,
      "action": "cls9-math"
    },
    {
      "id": "b-cls9-urdu",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "Urdu (Compulsory)",
      "title": "Urdu 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "26.8 MB",
      "pages": "Complete 15 Lessons & Poetry",
      "pdfPath": "assets/books/Class-9-Urdu-KPK.pdf",
      "color": "#16a34a",
      "icon": "📗",
      "available": true,
      "action": "cls9-urdu"
    },
    {
      "id": "b-cls9-isl",
      "classId": "cls9",
      "className": "Class 9",
      "subject": "Islamyat (Compulsory)",
      "title": "Islamyat 9th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "21.8 MB",
      "pages": "Surah Al-Anfal, Ahadith & Thematic Study",
      "pdfPath": "assets/books/Class-9-Islamyat-KPK.pdf",
      "color": "#0d9488",
      "icon": "🕌",
      "available": true,
      "action": "cls9-isl"
    },
    {
      "id": "b-cls10-isl",
      "classId": "cls10",
      "className": "Class 10",
      "subject": "Islamyat (Compulsory) - Part B",
      "title": "Islamyat 10th Class Textbook (Part B)",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "21.8 MB",
      "pages": "Surah Al-Ahzab, Surah Al-Mumtahina, Ahadith & Thematic Study",
      "pdfPath": "assets/books/Class-9-Islamyat-KPK.pdf",
      "color": "#0f766e",
      "icon": "🕌",
      "available": true,
      "action": "cls10-isl"
    },
    {
      "id": "b-cls10-phys",
      "classId": "cls10",
      "className": "Class 10",
      "subject": "Physics",
      "title": "Physics 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "Syllabus Ready",
      "pages": "10 Chapters (10–19)",
      "pdfPath": "",
      "color": "#0284c7",
      "icon": "⚡",
      "available": false,
      "action": "cls10-phy"
    },
    {
      "id": "b-cls10-chem",
      "class_id": "cls10",
      "class_name": "Class 10",
      "subject": "Chemistry",
      "title": "Chemistry 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "icon": "🧪",
      "color": "#0284c7",
      "size": "48.9 MB",
      "pages": "8 Units (9–16) Complete",
      "pdf_path": "assets/books/Class-10-Chemistry-KPK.pdf",
      "available": true,
      "subject_id": 8,
      "hub_action": "cls10-chem",
      "classId": "cls10",
      "className": "Class 10",
      "action": "cls10-chem",
      "pdfPath": "assets/books/Class-10-Chemistry-KPK.pdf"
    },
    {
      "id": "b-cls10-bio",
      "classId": "cls10",
      "className": "Class 10",
      "subject": "Biology",
      "title": "Biology 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "Syllabus Ready",
      "pages": "9 Chapters (10–18)",
      "pdfPath": "",
      "color": "#8b5cf6",
      "icon": "🔬",
      "available": false,
      "action": "cls10-bio"
    },
    {
      "id": "b-cls10-math",
      "classId": "cls10",
      "className": "Class 10",
      "subject": "Mathematics",
      "title": "Mathematics 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "19.5 MB",
      "pages": "Complete 13 Units",
      "pdfPath": "assets/books/Class-10-Mathematics-KPK.pdf",
      "color": "#2563eb",
      "icon": "📐",
      "available": true,
      "action": "cls10-math"
    },
    {
      "id": "b-cls10-pakstudy",
      "classId": "cls10",
      "className": "Class 10",
      "subject": "Pakistan Studies",
      "title": "Pakistan Studies 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "16.2 MB",
      "pages": "Complete 4 Chapters",
      "pdfPath": "assets/books/Class-10-Pakistan-Studies-KPK.pdf",
      "color": "#0d9488",
      "icon": "🇵🇰",
      "available": true,
      "action": "cls10-pakstudy"
    },
    {
      "id": "b-cls10-urdu",
      "classId": "cls10",
      "className": "Class 10",
      "subject": "Urdu (Compulsory)",
      "title": "Urdu 10th Class Textbook",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "24.5 MB",
      "pages": "Complete 22 Lessons & Poetry",
      "pdfPath": "assets/books/Class-10-Urdu-KPK.pdf",
      "color": "#0891b2",
      "icon": "📗",
      "available": true,
      "action": "cls10-urdu"
    },
    {
      "id": "b-cls11-phys",
      "classId": "cls11",
      "className": "Class 11",
      "subject": "Physics",
      "title": "Physics 11th Class (HSSC-I)",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "Syllabus Ready",
      "pages": "10 Chapters",
      "pdfPath": "",
      "color": "#7209b7",
      "icon": "🧭",
      "available": false,
      "action": "cls11-phy"
    },
    {
      "id": "b-cls12-phys",
      "classId": "cls12",
      "className": "Class 12",
      "subject": "Physics",
      "title": "Physics 12th Class (HSSC-II)",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "Syllabus Ready",
      "pages": "10 Chapters",
      "pdfPath": "",
      "color": "#059669",
      "icon": "⚛️",
      "available": false,
      "action": "cls12-phy"
    },
    {
      "id": "b-cls12-chem",
      "classId": "cls12",
      "className": "Class 12",
      "subject": "Chemistry",
      "title": "Chemistry 12th Class (HSSC-II)",
      "board": "Khyber Pakhtunkhwa Textbook Board, Peshawar",
      "size": "Syllabus Ready",
      "pages": "16 Chapters",
      "pdfPath": "",
      "color": "#0284c7",
      "icon": "🧪",
      "available": false,
      "action": "cls12-chem"
    }
  ],
};
