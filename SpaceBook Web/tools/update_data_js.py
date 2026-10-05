import re

path = r'D:\SpaceBook\SpaceBook Web\js\data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update DATA.subjects.cls12 array in content
old_cls12_block = """    "cls12": [
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
    ]"""

new_cls12_block = """    "cls12": [
      {
        "id": "cls12-math",
        "name": "Mathematics",
        "emoji": "📐",
        "chapters": 12,
        "hasMath": true
      },
      {
        "id": "cls12-phy",
        "name": "Physics",
        "emoji": "⚡",
        "chapters": 10,
        "hasPhys": true
      },
      {
        "id": "cls12-chem",
        "name": "Chemistry",
        "emoji": "🧪",
        "chapters": 12,
        "hasChem": true
      },
      {
        "id": "cls12-stat",
        "name": "Statistics",
        "emoji": "📊",
        "chapters": 9,
        "hasStat": true
      },
      {
        "id": "cls12-eng",
        "name": "English",
        "nameUrdu": "انگریزی لازمی",
        "emoji": "📖",
        "chapters": 19,
        "hasEng": true,
        "hasEng12": true
      },
      {
        "id": "cls12-urdu",
        "name": "Urdu",
        "nameUrdu": "اردو لازمی",
        "emoji": "📗",
        "chapters": 22,
        "hasUrdu": true,
        "hasUrdu12": true
      },
      {
        "id": "cls12-bio",
        "name": "Biology",
        "nameUrdu": "حیاتیات",
        "emoji": "🧬",
        "chapters": 14,
        "hasBio": true,
        "hasBio12": true
      },
      {
        "id": "cls12-pak",
        "name": "Pakistan Studies",
        "nameUrdu": "مطالعہ پاکستان",
        "emoji": "🇵🇰",
        "chapters": 11,
        "hasPakStudy": true,
        "hasPakStudy12": true
      },
      {
        "id": "cls12-comp",
        "name": "Computer Science",
        "nameUrdu": "کمپیوٹر سائنس",
        "emoji": "💻",
        "chapters": 9,
        "hasComp": true,
        "hasComp12": true
      },
      {
        "id": "cls12-civics",
        "name": "Civics",
        "nameUrdu": "شہریت (سوکس)",
        "emoji": "🏛️",
        "chapters": 8,
        "hasCivics": true
      },
      {
        "id": "cls12-econ",
        "name": "Economics",
        "nameUrdu": "معاشیات",
        "emoji": "📈",
        "chapters": 12,
        "hasEcon": true
      },
      {
        "id": "cls12-hpe",
        "name": "Health & Physical Education",
        "nameUrdu": "صحت و جسمانی تعلیم",
        "emoji": "🏃",
        "chapters": 6,
        "hasHpe": true
      },
      {
        "id": "cls12-islopt",
        "name": "Islamiat Ikhtiari",
        "nameUrdu": "اسلامیات اختیاری",
        "emoji": "🕌",
        "chapters": 6,
        "hasIslopt": true
      },
      {
        "id": "cls12-islhist",
        "name": "Islamic History",
        "nameUrdu": "تاریخِ اسلام",
        "emoji": "📜",
        "chapters": 6,
        "hasIslhist": true
      },
      {
        "id": "cls12-quran",
        "name": "Mutalia-e-Quran",
        "nameUrdu": "ترجمۃ القرآن المجید",
        "emoji": "📖",
        "chapters": 8,
        "hasQuran": true
      }
    ]"""

# Normalize CRLF
content_norm = content.replace('\r\n', '\n')
if old_cls12_block in content_norm:
    content_norm = content_norm.replace(old_cls12_block, new_cls12_block)
    print("Replaced DATA.subjects.cls12")
else:
    print("WARNING: old_cls12_block not found in content!")

# 2. Update IIFE at bottom
iife_pattern = r"\(\(\) => \{\s*const cls = DATA\.classes\.find\(c => c\.id === 'cls12'\);[\s\S]*?\}\)\(\);"

new_iife = """(() => {
  const cls = DATA.classes.find(c => c.id === 'cls12');
  const subjects = DATA.subjects.cls12 || (DATA.subjects.cls12 = []);
  const maps = [
    ['cls12-math', 'Mathematics', '📐', 12, 'file:///D:/SpaceBook/Books/12th/12th%20Maths/PDF/Math%20Book%20for%2012%20class%20KPTBB.pdf', { hasMath: true }],
    ['cls12-phy', 'Physics', '⚡', 10, 'file:///D:/SpaceBook/Books/12th/12th%20Physics/PDF/Physics%20Book%20for%2012%20class%20KPTBB.pdf', { hasPhys: true }],
    ['cls12-chem', 'Chemistry', '🧪', 12, 'file:///D:/SpaceBook/Books/12th/12th%20Chemistry/PDF/Chemistry%20Book%20for%2012%20class%20KPTBB.pdf', { hasChem: true }],
    ['cls12-stat', 'Statistics', '📊', 9, 'file:///D:/SpaceBook/Books/12th/12th%20Statistics/PDF/Statistics%20Book%20for%2012%20class%20KPTBB.pdf', { hasStat: true }],
    ['cls12-eng', 'English', '📖', 19, 'file:///D:/SpaceBook/Books/12th/12th%20English/PDF/English%20Book%20for%2012%20class%20KPTBB.pdf', { hasEng: true, hasEng12: true, nameUrdu: 'انگریزی لازمی' }],
    ['cls12-urdu', 'Urdu', '📗', 22, 'file:///D:/SpaceBook/Books/12th/12th%20Urdu/PDF/Urdu%20Book%20for%2012%20class%20KPTBB.pdf', { hasUrdu: true, hasUrdu12: true, nameUrdu: 'اردو لازمی' }],
    ['cls12-bio', 'Biology', '🧬', 14, 'file:///D:/SpaceBook/Books/12th/12th%20Biology/PDF/Biology%20Book%20for%2012%20class%20KPTBB.pdf', { hasBio: true, hasBio12: true, nameUrdu: 'حیاتیات' }],
    ['cls12-pak', 'Pakistan Studies', '🇵🇰', 11, 'file:///D:/SpaceBook/Books/12th/12th%20Pak%20Studies/PDF/Pak-study%20Book%20for%2012%20class%20KPTBB.pdf', { hasPakStudy: true, hasPakStudy12: true, nameUrdu: 'مطالعہ پاکستان' }],
    ['cls12-comp', 'Computer Science', '💻', 9, 'file:///D:/SpaceBook/Books/12th/12th%20Computer%20Science/PDF/Computer-Sc%20%20Book%20for%2012%20class%20KPTBB.pdf', { hasComp: true, hasComp12: true, nameUrdu: 'کمپیوٹر سائنس' }],
    ['cls12-civics', 'Civics', '🏛️', 8, 'file:///D:/SpaceBook/Books/12th/12th%20Civics/PDF/Civics%20Book%20for%2012%20class%20KPTBB.pdf', { hasCivics: true, nameUrdu: 'شہریت (سوکس)' }],
    ['cls12-econ', 'Economics', '📈', 12, 'file:///D:/SpaceBook/Books/12th/12th%20Economics/PDF/Economic%20Book%20for%2012%20class%20KPTBB.pdf', { hasEcon: true, nameUrdu: 'معاشیات' }],
    ['cls12-hpe', 'Health & Physical Education', '🏃', 6, 'file:///D:/SpaceBook/Books/12th/12th%20HPE/PDF/HPE%20book%20UM%2012th%20class%20KPK.pdf', { hasHpe: true, nameUrdu: 'صحت و جسمانی تعلیم' }],
    ['cls12-islopt', 'Islamiat Ikhtiari', '🕌', 6, 'file:///D:/SpaceBook/Books/12th/12th%20Islamiat%20Ikhtiari/PDF/Islamiat-Ikhtiari%20Book%20for%2012%20class%20KPTBB.pdf', { hasIslopt: true, nameUrdu: 'اسلامیات اختیاری' }],
    ['cls12-islhist', 'Islamic History', '📜', 6, 'file:///D:/SpaceBook/Books/12th/12th%20Islamic%20History/PDF/Islamic%20History%20book%2012th%20class%20KPK.pdf', { hasIslhist: true, nameUrdu: 'تاریخِ اسلام' }],
    ['cls12-quran', 'Mutalia-e-Quran', '📖', 8, 'file:///D:/SpaceBook/Books/12th/12th%20Mutalia%20e%20Quran/PDF/Mutlia_e_Quran_Book_KPK_12.pdf', { hasQuran: true, nameUrdu: 'ترجمۃ القرآن المجید' }]
  ];

  maps.forEach(([id, name, emoji, count, pdf, extra]) => {
    let subject = subjects.find(item => item.id === id);
    if (!subject) {
      subject = { id, name, emoji, chapters: count };
      subjects.push(subject);
    }
    subject.name = name;
    subject.emoji = emoji;
    subject.chapters = count;
    subject.pdf = pdf;
    if (extra) Object.assign(subject, extra);
  });
  if (cls) cls.subjects = subjects.length;

  const folderMap = {
    'cls12-math': '12th%20Maths',
    'cls12-phy': '12th%20Physics',
    'cls12-chem': '12th%20Chemistry',
    'cls12-stat': '12th%20Statistics',
    'cls12-eng': '12th%20English',
    'cls12-urdu': '12th%20Urdu',
    'cls12-bio': '12th%20Biology',
    'cls12-pak': '12th%20Pak%20Studies',
    'cls12-comp': '12th%20Computer%20Science',
    'cls12-civics': '12th%20Civics',
    'cls12-econ': '12th%20Economics',
    'cls12-hpe': '12th%20HPE',
    'cls12-islopt': '12th%20Islamiat%20Ikhtiari',
    'cls12-islhist': '12th%20Islamic%20History',
    'cls12-quran': '12th%20Mutalia%20e%20Quran'
  };

  const bookDetails = [
    ['cls12-math', 'Mathematics', 'b-cls12-math', 'Math Book for 12 class KPTBB.pdf', '12 Units', '#2563eb', '📐'],
    ['cls12-phy', 'Physics', 'b-cls12-phys', 'Physics Book for 12 class KPTBB.pdf', '10 Units', '#059669', '⚛️'],
    ['cls12-chem', 'Chemistry', 'b-cls12-chem', 'Chemistry Book for 12 class KPTBB.pdf', '12 Units', '#0284c7', '🧪'],
    ['cls12-stat', 'Statistics', 'b-cls12-stat', 'Statistics Book for 12 class KPTBB.pdf', '9 Units', '#7c3aed', '📊'],
    ['cls12-eng', 'English', 'b-cls12-eng', 'English Book for 12 class KPTBB.pdf', '19 Units', '#2563eb', '📖'],
    ['cls12-urdu', 'Urdu', 'b-cls12-urdu', 'Urdu Book for 12 class KPTBB.pdf', '22 Lessons', '#059669', '📗'],
    ['cls12-bio', 'Biology', 'b-cls12-bio', 'Biology Book for 12 class KPTBB.pdf', '14 Units', '#16a34a', '🧬'],
    ['cls12-pak', 'Pakistan Studies', 'b-cls12-pak', 'Pak-study Book for 12 class KPTBB.pdf', '11 Chapters', '#059669', '🇵🇰'],
    ['cls12-comp', 'Computer Science', 'b-cls12-comp', 'Computer-Sc  Book for 12 class KPTBB.pdf', '9 Units', '#4f46e5', '💻'],
    ['cls12-civics', 'Civics', 'b-cls12-civics', 'Civics Book for 12 class KPTBB.pdf', '8 Chapters', '#475569', '🏛️'],
    ['cls12-econ', 'Economics', 'b-cls12-econ', 'Economic Book for 12 class KPTBB.pdf', '12 Chapters', '#059669', '📈'],
    ['cls12-hpe', 'Health & Physical Education', 'b-cls12-hpe', 'HPE book UM 12th class KPK.pdf', '6 Chapters', '#ea580c', '🏃'],
    ['cls12-islopt', 'Islamiat Ikhtiari', 'b-cls12-islopt', 'Islamiat-Ikhtiari Book for 12 class KPTBB.pdf', '6 Chapters', '#15803d', '🕌'],
    ['cls12-islhist', 'Islamic History', 'b-cls12-islhist', 'Islamic History book 12th class KPK.pdf', '6 Chapters', '#b45309', '📜'],
    ['cls12-quran', 'Mutalia-e-Quran', 'b-cls12-quran', 'Mutlia_e_Quran_Book_KPK_12.pdf', '8 Chapters', '#059669', '📖']
  ];

  bookDetails.forEach(([action, subjectName, id, filename, pages, color, icon]) => {
    const folder = folderMap[action] || '12th%20Maths';
    const pdfPath = `file:///D:/SpaceBook/Books/12th/${folder}/PDF/${filename.replace(/ /g, '%20')}`;
    let book = DATA.books.find(item => item.id === id);
    if (!book) {
      book = { id, classId: 'cls12', className: 'Class 12', subject: subjectName, title: `${subjectName} 12th Class (HSSC-II)`, board: 'Khyber Pakhtunkhwa Textbook Board, Peshawar', color, icon, action };
      DATA.books.push(book);
    }
    Object.assign(book, { subject: subjectName, title: `${subjectName} 12th Class (HSSC-II)`, size: 'Complete textbook transcription', pages, pdfPath, color, icon, available: true, action });
  });

  const chapterTitles = {
    'cls12-math': ['Introduction to Symbolic Package, Maple','Functions and Limits','Differentiation','Higher Order Derivatives and Applications','Differentiation of Vector Functions','Integration','Plane Analytic Geometry: Straight Line','Conics I','Conics II','Differential Equations','Partial Differentiation','Introduction to Numerical Methods'],
    'cls12-phy': ['Electrostatics','Current Electricity','Electromagnetism','Electromagnetic Induction','Alternating Current','Physics of Solids','Electronics','Dawn of Modern Physics','Atomic Spectra','Nuclear Physics'],
    'cls12-chem': ['s and p-Block Elements','d and f-Block Elements: Transition Elements','Organic Compounds','Hydrocarbons','Alkyl Halides and Amines','Alcohols, Phenols and Ethers','Carbonyl Compounds I: Aldehydes and Ketones','Carbonyl Compounds II: Carboxylic Acids and Functional Derivatives','Biochemistry','Industrial Chemistry','Environmental Chemistry','Analytical Chemistry'],
    'cls12-stat': ['Probability','Random Variables and Probability Distributions','Special Discrete Probability Distributions','Special Continuous Probability Distributions','Sampling and Sampling Distributions','Estimation','Hypothesis Testing','Association of Attributes','Experimental Design'],
    'cls12-eng': ['Seerat-e-Tayyiba and the Muslim Youth','I Have a Dream','The Glory of the Himalayas','A Visit to the Doctor','The Last Lesson','The Model Millionaire','The World as I See It','The Daffodils','The Road Not Taken','Incident of the French Camp','Ozymandias','The Echoing Green','Say Not the Struggle Naught Availeth','A Dialogue on Social Evils','Technology and Human Values','The Importance of Media','National Pride and Civic Sense','A Review of Great Expectations','The Renaissance of Pakistan'],
    'cls12-urdu': ['مسلمانوں کا قدیم طرز تعلیم','محنت پسند دیوانہ','مرزا غالب کے عادات و خصائل','نواب محسن الملک','قومی ہمدردی','اکبری کی حماقتیں','سیرت فاطمۃ الزہرا رضی اللہ عنہا','خطوط غالب','علامہ اقبال کے خطوط','چغل خور','قرطبہ کا قاضی','مولوی نذیر احمد دہلوی','دستورِ حیات','سفرنامہ حجاز','قائداعظم کا خطاب','نعت رسول مقبول ﷺ','مردِ مسلمان','خضرِ راہ','پیغامِ اقبال','غزل ۱ (میر تقی میر)','غزل ۲ (مرزا اسد اللہ خاں غالب)','غزل ۳ (حسرت موہانی)'],
    'cls12-bio': ['Respiration','Homeostasis','Support and Locomotion','Nervous Coordination','Chemical Coordination','Behaviour','Reproduction','Development and Aging','Inheritance','Chromosome and DNA','Evolution','Biotechnology','Ecosystem','Some Major Ecosystems'],
    'cls12-pak': ['اسلامی جمہوریہ پاکستان کا قیام','پاکستان کی ابتدائی مشکلات','پاکستان کا جغرافیہ اور قدرتی وسائل','پاکستان کا آئینی ارتقاء','پاکستان کا انتظامی ڈھانچہ اور حکومت','پاکستان کی معاشی ترقی اور منصوبہ بندی','پاکستان کا معاشرہ اور ثقافت','پاکستان کی تعلیمی اور سماجی صورتحال','پاکستان کی خارجہ پالیسی','پاکستان اور عالم اسلام','پاکستان کا دفاع اور سیکیورٹی چیلنجز'],
    'cls12-comp': ['Operating System','System Development Life Cycle (SDLC)','Control Structures in C','Functions in C','Arrays and Strings','Pointers','File Handling in C','Information Technology and Database Management','Web Development and Cyber Security'],
    'cls12-civics': ['پاکستان کا نظام حکومت اور آئینی ڈھانچہ','وفاقی مقننہ (پارلیمنٹ) اور اس کے اختیارات','وفاقی انتظامیہ: صدر، وزیر اعظم اور کابینہ','پاکستان کا عدالتی نظام: سپریم کورٹ اور ہائی کورٹس','صوبائی حکومتیں اور مقامی انتظامیہ','پاکستان کا انتخابی نظام اور سیاسی جماعتیں','شہریوں کے بنیادی حقوق اور فرائض','عوامی رائے اور ذرائع ابلاغ'],
    'cls12-econ': ['قومی آمدنی کے بنیادی تصورات','زر (Money) کا مفہوم اور افعال','بینکاری نظام اور مرکزی بینک','سرکاری مالیات (Public Finance)','بین الاقوامی تجارت (International Trade)','پاکستان کی معیشت کا تعارف','زرعی شعبہ اور اس کے مسائل','صنعتی شعبہ اور معاشی ترقی','پاکستان کی تجارت خارجہ','معاشی منصوبہ بندی اور ترقیاتی حکمت عملی','افرادی قوت، روزگار اور بے روزگاری','پاکستان کے مالیاتی ادارے اور معاشی چیلنجز'],
    'cls12-hpe': ['غیر متعدی امراض اور انسداد','متعدی بیماریاں اور صحت عامہ','کھیل اور بین الاقوامی قواعد','جسمانی فٹنس اور ورزش کے سائنسی اصول','ابتدائی طبی امداد (First Aid) اور ہنگامی تدابیر','نشہ آور اشیاء اور ان کے ہلاکت خیز اثرات'],
    'cls12-islopt': ['قرآن مجید اور اصول تفسیر','منتخب قرآنی آیات کا تفسیری مطالعہ','حدیث نبوی ﷺ اور اصول حدیث','منتخب احادیث نبویہ کا تشریحی مطالعہ','فقہ اسلامی اور اجتہاد','اسلامی تہذیب و تمدن کے بنیادی خدوخال'],
    'cls12-islhist': ['خلافت بنو عباس کا قیام اور ابتدائی خلفاء','عہد عباسی کی علمی، ثقافتی اور سائنسی ترقیاں','بنو عباس کا زوال اور سقوط بغداد','اندلس (اسپین) میں اسلامی حکومت کا قیام','اندلس کا تمدنی عروج اور علمی کارنامے','سلطنت عثمانیہ کا قیام، فتوحات اور تاریخی اثرات'],
    'cls12-quran': ['سورة النساء: مطالعہ، ترجمہ اور بنیادی احکام','سورة المائدة: مطالعہ، ترجمہ اور احکام حلال و حرام','سورة الأنعام: توحید، نبوت اور عقائد اسلامی','سورة الأعراف: تاریخی اقوام کے عبرتناک اسباق','سورة الأنفال: جہاد فی سبیل اللہ، تقویٰ اور مال غنیمت','سورة التوبة: نفاق، براءت اور اسلامی جہاد کے تقاضے','سورة يونس: سنت الٰہیہ، صبر اور ایمان بالرسالت','سورة هود: استقامت فی الدین اور انبیاء کرام کے واقعات']
  };

  Object.entries(chapterTitles).forEach(([id, names]) => {
    const unitOffset = id === 'cls12-phy' ? 11 : id === 'cls12-bio' ? 14 : 1;
    DATA.chapters[id] = names.map((name, i) => ({ num: unitOffset + i, name, topics: 'Textbook lesson, concepts, exercises and exam questions', status: 'done' }));
  });
})();"""

if re.search(iife_pattern, content_norm):
    content_norm = re.sub(iife_pattern, new_iife, content_norm)
    print("Replaced IIFE")
else:
    print("WARNING: IIFE pattern not found!")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content_norm)
print("Saved data.js")
