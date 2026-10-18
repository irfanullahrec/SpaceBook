# -*- coding: utf-8 -*-
"""Unit 1 part E — PDF 25-28 (printed 19-22): Key Points and Exercise."""
from bio9_tools import Section

KEY_POINTS = [
    ('Biology is one of the natural sciences which deals with life or living organisms.',
     'حیاتیات قدرتی علوم میں سے ایک ہے جو زندگی یا جانداروں سے متعلق ہے۔',
     'بیولوژي له طبیعي علومو څخه ده چې له ژوند یا ژوندیو موجوداتو سره سروکار لري.'),
    ('Biology is a multidisciplinary science, that requires a knowledge and understanding of chemistry, physics and mathematics.',
     'حیاتیات ایک کثیر شعبہ جاتی سائنس ہے جس کے لیے کیمیا، طبیعیات اور ریاضی کے علم اور سمجھ کی ضرورت ہوتی ہے۔',
     'بیولوژي څو رشتوي ساینس دی چې د کیمیا، فزیک او ریاضي پوهې او درک ته اړتیا لري.'),
    ('Career in biology can be immensely rewarding and exciting. There are several career paths for a biologist such as: horticulture, forestry, medicine etc.',
     'حیاتیات میں کیریئر بے حد فائدہ مند اور دلچسپ ہو سکتا ہے۔ ماہرِ حیاتیات کے لیے کئی پیشہ ورانہ راستے ہیں مثلاً باغبانی، جنگلات، طب وغیرہ۔',
     'په بیولوژي کې مسلک ډېر ګټور او په زړه پورې کېدای شي. د بیولوژیست لپاره څو مسلکي لارې شته لکه باغواني، ځنګلداري، طب او نور.'),
    ('16 out of the 92 naturally occurring elements are of significance in the bodies of living organisms.',
     'قدرتی طور پر پائے جانے والے 92 عناصر میں سے 16 جانداروں کے جسموں میں اہمیت رکھتے ہیں۔',
     'په طبیعي توګه موندل کېدونکو 92 عناصرو کې 16 یې د ژوندیو موجوداتو په بدنونو کې ارزښت لري.'),
    ('Six elements i.e Hydrogen, Carbon, Oxygen, Nitrogen, Phosphorus and Calcium are the essential elements of the living bodies.',
     'چھ عناصر یعنی ہائیڈروجن، کاربن، آکسیجن، نائٹروجن، فاسفورس اور کیلشیم جاندار جسموں کے لازمی عناصر ہیں۔',
     'شپږ عناصر یعنې هایدروجن، کاربن، اکسیجن، نایټروجن، فاسفورس او کلسیم د ژوندیو بدنونو اړین عناصر دي.'),
    ('In biological organizations the atoms form the elements, which are organized into compounds/molecules, compounds into cells, cells into tissues, tissues into organs, organs into system and system into an organism.',
     'حیاتیاتی تنظیم میں ایٹم عناصر بناتے ہیں، جو مرکبات/مالیکیولز میں، مرکبات خلیات میں، خلیات بافتوں میں، بافتیں اعضا میں، اعضا نظام میں اور نظام ایک جاندار میں منظم ہوتے ہیں۔',
     'په بیولوژیکي تنظیم کې اتومونه عناصر جوړوي چې په مرکبونو/مالیکولونو، مرکبونه په حجرو، حجرې په نسجونو، نسجونه په غړو، غړي په سیسټم او سیسټم په ژوندي موجود کې تنظیمېږي.'),
    ('Cell is the structural and functional unit of all living organisms.',
     'خلیہ تمام جانداروں کی ساختی اور فعلی اکائی ہے۔',
     'حجره د ټولو ژوندیو موجوداتو جوړښتي او دندیز واحد دی.'),
    ('Similar organisms which can interbreed and produce fertile offspring form the species.',
     'ایک جیسے جاندار جو آپس میں افزائشِ نسل کر کے زرخیز اولاد پیدا کر سکیں، نوع بناتے ہیں۔',
     'ورته موجودات چې سره نسل اخیستلای شي او حاصلخېز اولاد تولیدولای شي، نوع جوړوي.'),
    ('Members of the same species living together in close association in a particular area make a population.',
     'ایک ہی نوع کے ارکان جو کسی خاص علاقے میں قریبی تعلق کے ساتھ اکٹھے رہتے ہیں، آبادی بناتے ہیں۔',
     'د یوې نوعې غړي چې په یوه ځانګړې سیمه کې په نږدې اړیکه یوځای اوسېږي، نفوس جوړوي.'),
    ('Living together of different populations constitutes a community.',
     'مختلف آبادیوں کا اکٹھے رہنا کمیونٹی بناتا ہے۔',
     'د بېلابېلو نفوسو یوځای اوسېدل ټولنه جوړوي.'),
    ('Cellular organization can be of three types: Unicellular organization, colonial organization, multi-cellular organization.',
     'خلوی تنظیم تین اقسام کی ہو سکتی ہے: یک خلوی تنظیم، کالونیل تنظیم، کثیر خلوی تنظیم۔',
     'حجروي تنظیم درې ډوله کېدای شي: یو حجروي تنظیم، کلونیایي تنظیم، څو حجروي تنظیم.'),
    ('In division of labour the work of keeping an organism alive is often divided among the different parts of its body. Each part performs a specific job.',
     'تقسیمِ کار میں جاندار کو زندہ رکھنے کا کام اکثر اس کے جسم کے مختلف حصوں میں تقسیم ہوتا ہے۔ ہر حصہ ایک مخصوص کام انجام دیتا ہے۔',
     'د کار په وېش کې د ژوندي موجود د ژوندي ساتلو کار اکثراً د هغه د بدن په بېلابېلو برخو وېشل کېږي. هره برخه یوه ځانګړې دنده ترسره کوي.'),
]

NOTE = 'SpaceBook answer — the textbook prints no answer key for this exercise.'

# (question, options, correct index, note)
MCQS = [
    ('i. Ms. Aisha was busy in dissecting and analyzing the heart of frog. Probably she is a:',
     ['Cell biologist', 'Taxonomist', 'Histologist', 'Palaeontologist'], 2,
     NOTE + ' Of the four printed options, a histologist (tissue study) fits best; the book defines anatomy as the study of internal structures, which is not offered as an option.'),
    ('ii. How many people get lung cancer by smoking? This question can be answered through:',
     ['Biometry', 'Biophysics', 'Bio-economics', 'Biogeography'], 0,
     NOTE + ' Biometry applies statistical formulas to biological data (section 1.3.4).'),
    ('iii. Al-Qanun fil- Tibb is the famous book of:',
     ['Bu Ali Sina', 'Jabir bin Hayyan', 'Abdul Malik Asmai', 'Ibn Nafees'], 0,
     NOTE + ' Section 1.7.3: Bu Ali Sina\'s book “Al-Qanun-fit-Tibb”.'),
    ('iv. One of the following contain large number of cells but not a multicellular:',
     ['Frog', 'Volvox', 'Mushroom', 'Chlamydomonas'], 1,
     NOTE + ' Volvox is a colonial organism of hundreds of cells (section 1.9).'),
    ('v. According to five Kingdom System of classifications mushrooms belong to:',
     ['Plantae', 'Fungi', 'Animalia', 'Protista'], 1,
     NOTE + ' Section 1.5.3 lists mushrooms under Kingdom Fungi.'),
    ('vi. The level of organization which is represented by the heart of frog is:',
     ['Organ', 'Tissue', 'Organism', 'Organelle'], 0,
     NOTE + ' The heart is an organ (Level 6).'),
    ('vii. One of the following is not a macromolecule:',
     ['Glucose', 'Sucrose', 'Fatty acid', 'Protein'], 0,
     NOTE + ' The book names glucose as a micro-molecule (Level 2). As printed, sucrose and fatty acid are also small molecules, so only protein is clearly a macromolecule; glucose is the option the text itself names.'),
    ('viii. “The number of plants in desert are scarce”. This could be the statement of:',
     ['Palaeontologist', 'Social biologist', 'Biogeoghraphist', 'Taxonomist'], 2,
     NOTE + ' Biogeography studies the distribution of organisms in space and time (section 1.3.3). Option spelling kept as printed.'),
    ('ix. Which bio-element makes most of the composition of organism\'s body?',
     ['Hydrogen', 'Carbon', 'Oxygen', 'Nitrogen'], 2,
     NOTE + ' Figure 1.2: oxygen 65%.'),
    ('x. Which of the following cellular organization represents Volvox?',
     ['Unicellular', 'Multicellular', 'Bicellular', 'Colonial'], 3,
     NOTE + ' Section 1.9 (ii): colonial organization.'),
]

SQ = [
    'i. How the understanding of physics can help the biologist?',
    'ii. Which career would you like to adopt after studying biology and why?',
    'iii. Write the translation of any three verses of the Holy Quran related to the creation of mankind.',
    'iv. Name few Muslim Scientists and their contributions in the field of biology and medicine.',
    'v. What level of organization is represented by Volvox?',
]
LQ = [
    'i. How the understanding of biology can be improved through knowledge of geography, chemistry and statistics? Give examples.',
    'ii. Define biology. How can you describe your own body under different branches of biology?',
    'iii. Enlist the various levels of biological organization and explain it with example.',
    'iv. Explain the role of bio elements for living organisms.',
    'v. Who classify the living organisms into five kingdom. Explain each kingdom with the living organisms included in it.',
]

ACTIVITIES = [
    dict(title='Analysing and Interpreting (page 6)', desc='A group of class fellows is interested in various fields of biology. On the basis of your knowledge, analyse where they can make their careers. Fields: 1 Immunology, 2 Entomology, 3 Histology, 4 Parasitology. Career (may be 1 or more).', sourcePrintedPage=6),
    dict(title='Analysing and Interpreting (page 15)', desc='Enlist five tissues, organs and systems of human body.', sourcePrintedPage=15),
    dict(title='Activity (page 16)', desc='Write the levels against each example: Heart, Blood, C₆H₁₂O₅ (as printed), Mitochondria, Parenchyma, Neuron.', sourcePrintedPage=16),
    dict(title='Activity (page 18)', desc='Draw the diagrams of digestive and respiratory systems of man and label their main organs.', sourcePrintedPage=18),
]


def keypoints_section():
    s = Section('bio1_keypoints', 'Key Points', 'Key Points', 'اہم نکات', 'مهم ټکي', [25])
    s.ul(KEY_POINTS)
    return s


def exercise(old):
    """Build the textbook exercise; reuse earlier authored SQ/LQ answers, labelled as SpaceBook-authored."""
    lab = 'SpaceBook-authored answer (the textbook prints no answers):\n'
    old_sq = old.get('shortQuestions', [])
    old_lq = old.get('detailedQuestions', [])
    def ans(lst, i):
        a = (lst[i].get('answer') or lst[i].get('ans') or lst[i].get('solution') or '') if i < len(lst) else ''
        return lab + a if a else 'The textbook prints no answer for this question.'
    return dict(
        sourcePrintedPages=[20, 21, 22], sourcePdfPages=[26, 27, 28],
        heading='A. Encircle the best suitable answers.',
        mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
        shortQuestions=[dict(q=q, answer=ans(old_sq, i), sourceSection='B. Write short answers for the following questions.') for i, q in enumerate(SQ)],
        detailedQuestions=[dict(q=q, answer=ans(old_lq, i), sourceSection='C. Write detailed answers for the following questions.') for i, q in enumerate(LQ)],
        activities=ACTIVITIES,
    )
