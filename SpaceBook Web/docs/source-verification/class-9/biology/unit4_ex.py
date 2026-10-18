# -*- coding: utf-8 -*-
"""Unit 4 — PDF 98-101 (printed 95-98): Key Points, Exercise, unlabeled cell Activity."""
from bio9_tools import Section
import unit4_figs as F

KEY_POINTS = [
    ('Microscopic examination of cork initiated the study of the cells in 1665 by Robert Hooke.', '1665ء میں رابرٹ ہُک کے کارک کے خوردبینی معائنے سے خلیوں کا مطالعہ شروع ہوا۔', 'په 1665 کې د رابرټ هوک لخوا د کارک مایکروسکوپي معاینې د حجرو مطالعه پیل کړه.'),
    ('The energy used in light microscope is light and in transmission electron microscope (TEM) it is electrons.', 'روشنی کی خوردبین میں استعمال ہونے والی توانائی روشنی ہے اور ٹرانسمیشن الیکٹران مائیکروسکوپ (TEM) میں الیکٹرانز۔', 'په رڼا مایکروسکوپ کې کارېدونکې انرژي رڼا او په لېږدونکي الکترون مایکروسکوپ (TEM) کې الکترونونه دي.'),
    ('Cell is the structural and functional unit of living organisms.', 'خلیہ جانداروں کی ساختی اور فعلی اکائی ہے۔', 'حجره د ژوندیو موجوداتو جوړښتي او دندیز واحد دی.'),
    ('The cell theory describes that all organisms are composed of one or more cells, the cell arise from pre-existing cells and the cell is the structural and functional unit of all organisms.', 'خلوی نظریہ بیان کرتا ہے کہ تمام جاندار ایک یا زیادہ خلیوں سے بنے ہیں، خلیہ پہلے سے موجود خلیوں سے بنتا ہے اور خلیہ تمام جانداروں کی ساختی اور فعلی اکائی ہے۔', 'حجروي تیوري وايي چې ټول موجودات له یوې یا ډېرو حجرو جوړ دي، حجره له مخکې موجودو حجرو پیدا کېږي او حجره د ټولو موجوداتو جوړښتي او دندیز واحد دی.'),
    ('The cell may be prokaryotic or eukaryotic.', 'خلیہ پروکیریوٹک یا یوکیریوٹک ہو سکتا ہے۔', 'حجره پروکاریوټیکه یا یوکاریوټیکه کېدای شي.'),
    ('The prokaryotic cell lacks most of the membrane bounded organelles.', 'پروکیریوٹک خلیے میں زیادہ تر جھلی دار عضیات نہیں ہوتے۔', 'پروکاریوټیکه حجره ډېری غشا لرونکي اورګانیلونه نه لري.'),
    ('All cells are bounded by the plasma membrane.', 'تمام خلیے پلازما جھلی سے گھرے ہوتے ہیں۔', 'ټولې حجرې په پلازما غشا را ګرځېدلې دي.'),
    ('Cell wall is an additional covering in plant cells out side the plasma membrane.', 'خلوی دیوار پودوں کے خلیوں میں پلازما جھلی کے باہر ایک اضافی غلاف ہے۔', 'د حجرې دېوال د بوټو په حجرو کې د پلازما غشا بهر اضافي پوښ دی.'),
    ('Fluid mosaic model is the most acceptable model of cell membrane.', 'فلوئڈ موزیک ماڈل خلوی جھلی کا سب سے زیادہ قابلِ قبول ماڈل ہے۔', 'د مایع موزاییک ماډل د حجرې د غشا تر ټولو منل شوی ماډل دی.'),
    ('Plasma membrane is a selectively permeable membrane.', 'پلازما جھلی ایک منتخب نفوذ پذیر جھلی ہے۔', 'پلازما غشا انتخابي نفوذ منونکې غشا ده.'),
    ('Cell wall in plants gives shape, protection and support to the cell.', 'پودوں میں خلوی دیوار خلیے کو شکل، تحفظ اور سہارا دیتی ہے۔', 'په بوټو کې د حجرې دېوال حجرې ته بڼه، ساتنه او ملاتړ ورکوي.'),
    ('Endoplasmic reticulum helps in the transport of materials between the cytoplasm and nucleus and also involved in the protein synthesis.', 'اینڈوپلازمک ریٹیکولم سائٹوپلازم اور مرکزے کے درمیان مادوں کی ترسیل میں مدد دیتا ہے اور پروٹین سازی میں بھی شامل ہے۔', 'انډوپلازمیک ریټیکولم د سایټوپلازم او هستې ترمنځ د موادو په لېږد کې مرسته کوي او د پروټین په جوړولو کې هم ونډه لري.'),
    ('Golgi apparatus is mainly concerned with storage of secretory products and are made up of vesicles arranged approximately parallel to each other.', 'گولجی اپریٹس بنیادی طور پر رطوبتی پیداوار کے ذخیرے سے متعلق ہے اور تقریباً متوازی ترتیب دی گئی ویسیکلز سے بنا ہوتا ہے۔', 'ګولجي اپراټس په اصل کې د افرازي محصولاتو له زېرمه کولو سره تړاو لري او له شاوخوا موازي ترتیب شویو ویسیکلونو جوړ دی.'),
    ('Mitochondria are the energy producing organelles hence called power houses of the cell.', 'مائٹوکونڈریا توانائی پیدا کرنے والے عضیات ہیں اس لیے انہیں خلیے کا پاور ہاؤس کہتے ہیں۔', 'مایټوکونډریا انرژي تولیدوونکي اورګانیلونه دي نو د حجرې د برېښنا کور بلل کېږي.'),
    ('Plastids are of three types i.e. chloroplast, chromoplast and leucoplast.', 'پلاسٹڈز تین اقسام کے ہیں یعنی کلوروپلاسٹ، کروموپلاسٹ اور لیوکوپلاسٹ۔', 'پلاسټیډونه درې ډوله دي یعنې کلوروپلاسټ، کروموپلاسټ او لیوکوپلاسټ.'),
    ('The largest and the most conspicuous structure or cell organelle is the double membrane bounded nucleus.', 'سب سے بڑا اور نمایاں ساخت یا عضیہ دوہری جھلی والا مرکزہ ہے۔', 'تر ټولو لوی او ښکاره جوړښت یا اورګانیل په دوه ګونې غشا را ګرځېدلې هسته ده.'),
    ('The two prominent structure present in the nucleus are chromosomes and nucleolus (nucleoli).', 'مرکزے میں موجود دو نمایاں ساختیں کروموسومز اور نیوکلیولس (نیوکلیولائی) ہیں۔', 'په هسته کې دوه ښکاره جوړښتونه کروموزومونه او نیوکلیولس (نیوکلیولونه) دي.'),
]

NOTE = 'SpaceBook answer — the textbook prints no answer key for this exercise.'
MCQS = [
    ('i. Schleiden and Schwann proposed the cell theory on the basis of:', ['Their observation', 'Observations of Hooke and Brown', 'All observations on the cell', 'Observation made on the nucleus of the cell'], 0,
     NOTE + ' Section 4.2: Schleiden (plants, 1838) and Schwann (animals, 1839) summarized their observations into the cell theory.'),
    ('ii. The organelle which provides energy to the cell:', ['Golgi apparatus', 'Ribosome', 'Mitochondria', 'Nucleus'], 2, NOTE),
    ('iii. We obtain 2D images through:', ['Light microscope and SEM', 'SEM and TEM', 'Light microscope and TEM', 'Light microscope'], 2, NOTE + ' Table 4.1.'),
    ('iv. Inside the nucleus, granular material is called:', ['Cytoplasm', 'Protoplasm', 'Nucleoplasm', 'Cell sap'], 2, NOTE),
    ('v. The organelle involved in protein synthesis is:', ['Ribosome', 'Vacuole', 'Golgi apparatus', 'Plastids'], 0, NOTE),
    ('vi. The nervous tissue has the ability to:', ['Contract and relax', 'Transmit the impulses', 'Prepare secretion', 'Provide energy'], 1, NOTE),
    ('vii. In plants, which tissue makes new cells?', ['Meristematic tissue', 'Collenchyma tissue', 'Epidermal tissue', 'Ground tissue'], 0, NOTE),
    ('viii. Movement of molecules from lower to higher concentration with the expenditure of energy is:', ['Diffusion', 'Active transport', 'Facilitated transport', 'Osmosis'], 1, NOTE),
    ('ix. One of the following has both cytoplasm and cell wall:', ['Muscle cell', 'Red blood cell', 'Root hair cell', 'Xylem vessel'], 2, NOTE + ' Xylem vessels are dead and hollow; animal cells lack a cell wall.'),
    ('x. Cell membrane is made of:', ['Cellulose only', 'Proteins only', 'Lipids only', 'Lipids and proteins'], 3, NOTE + ' Fluid mosaic model.'),
    ('xi. Cell wall is present in the cells of:', ['Fungi only', 'Plants only', 'Plants and prokaryotes only', 'All of the above'], 3, NOTE + ' Cell wall is present in bacteria, plants, fungi and some protists.'),
    ('xii. Which organelles are covered with a double membrane?', ['Ribosomes', 'Vacuoles', 'Centrioles', 'Mitochondria'], 3, NOTE),
]
SQ = ['i. What proposed the cell theory and what are the main points of the cell theory?', 'ii. Differentiate between simple and compound tissues.',
      'iii. How cell membrane helps in maintaining equilibrium while exchanging materials with environment?', 'iv. Differentiate between endocytosis and exocytosis.',
      'v. How does turgor pressure develops in a plant cell?']
LQ = ['i. Root hairs are adapted to absorption and xylem to support. Relate their functions to their structure.',
      'ii. Discuss different types of tissues found in plants. Elaborate your answer with relevant diagrams.', 'iii. Describe the nervous, muscular and epithelial tissues.',
      'iv. Write a note on the structures of cell wall, cell membrane, mitochondria and chloroplast of a plant cell.']
LAB = 'SpaceBook-authored answer based on this unit (the textbook prints no answers):\n'
SQ_ANS = ['Schleiden (1838, plants) and Schwann (1839, animals) proposed the cell theory; Virchow (1855) added that every cell comes from a cell. Main points: (i) all animals and plants are made up of cells and cell products; (ii) cells are the structural and functional units of living organisms; (iii) new cells arise from pre-existing cells by cell division.',
          'Simple tissues are composed of only one type of cells (meristematic and permanent tissues such as epidermal, ground, collenchyma, sclerenchyma). Compound tissues are composed of more than one type of cells performing a common function (xylem: vessels and tracheids; phloem: sieve tube cells and companion cells).',
          'The cell membrane is selectively (semi-) permeable. It controls the movement of molecules into and out of the cell by diffusion, facilitated diffusion, osmosis, filtration, active transport, endocytosis and exocytosis, and in this way maintains equilibrium inside as well as outside the cell.',
          'Endocytosis brings macromolecules, large particles and even small cells into the cell: the membrane folds inward, forms a pocket and then a vesicle that moves inside (phagocytosis for solids, pinocytosis for liquids). Exocytosis releases materials packed in vesicles: the vesicle membrane binds with the cell membrane, the contents are released outside and the vesicle membrane becomes part of the cell membrane.',
          'When a plant cell is surrounded by water or a hypotonic solution, water enters the vacuole by osmosis. The vacuole enlarges and pushes the cell contents against the cell wall. The pressure exerted by the cytoplasm against the cell wall is turgor pressure; the strong, relatively inelastic wall stops the cell from bursting.']
LQ_ANS = ['Root hair cells have a large surface area for the maximum absorption of water and salts. Xylem cells are tube-like with thick walls; vessels are dead, hollow cells joined into long tubes and tracheids are long slender cells, and lignin in their secondary walls gives support while they conduct water upward (sections 4.4, 4.7.1).',
          'A. Simple tissues: (a) meristematic tissues (apical meristem for primary growth, lateral meristem for secondary growth; Figure 4.25); (b) permanent tissues: epidermal, ground (parenchyma, mesophyll), and supporting tissues (collenchyma and sclerenchyma; Figure 4.26). B. Compound tissues: xylem (vessels, tracheids) and phloem (sieve tube cells, companion cells; Figure 4.27).',
          'Epithelial tissue forms continuous sheets of flattened, elongated cells in the skin and lines the gut, lungs and urinary tract. Muscular tissue has contractile fibres: skeletal (striated, multinucleate, voluntary), smooth (spindle-shaped, un-striated, involuntary, in walls of hollow organs) and cardiac (branched fibres, sustained involuntary contraction). Nervous tissue is made of neurons that transmit nerve impulses; it is found in brain, spinal cord and nerves.',
          'Cell wall: outside the membrane; primary wall of cellulose, some cells also have a secondary wall with cellulose and lignin; gives shape, strength, protection. Cell membrane: lipid bilayer with proteins (fluid mosaic model), selectively permeable. Mitochondria: double membrane, inner membrane folded into cristae, site of respiration producing ATP. Chloroplast: double membrane, thylakoids stacked into grana containing chlorophyll, stroma inside; site of photosynthesis.']


def blank(d):
    return {k: (v if k == 'title' else ([''] * len(v) if isinstance(v, list) else '')) for k, v in d.items()}


def keypoints_section():
    s = Section('bio4_keypoints', 'Key Points', 'Key Points', 'اہم نکات', 'مهم ټکي', [98])
    s.ul(KEY_POINTS)
    return s


def activity_section():
    s = Section('bio4_activity', 'Activity', 'Activity: Identify the cells', 'سرگرمی: خلیوں کی شناخت', 'فعالیت: د حجرو پېژندنه', [101])
    s.p('Identify the following cells and label the marked parts of cells.', 'درج ذیل خلیوں کی شناخت کریں اور خلیوں کے نشان زدہ حصوں کے نام لکھیں۔', 'لاندې حجرې وپېژنئ او د حجرو نښه شوې برخې ونوموئ.')
    pb = F.plant_cell(blank(dict(F.PC_EN, title='Activity: unlabeled cell 1')))
    ab = F.animal_cell(blank(dict(F.AC_EN, title='Activity: unlabeled cell 2')))
    s.fig('bio4-activity-cell1', pb, pb, pb, .6)
    s.p('________________', '________________', '________________')
    s.fig('bio4-activity-cell2', ab, ab, ab, .6)
    s.p('________________', '________________', '________________')
    return s


def exercise():
    return dict(sourcePdfPages=[99, 100, 101], sourcePrintedPages=[96, 97, 98], heading='A. Encircle the best suitable answers.',
                mcqs=[dict(q=q, options=o, correct=c, explanation=e, answerOrigin='SpaceBook') for q, o, c, e in MCQS],
                shortQuestions=[dict(q=q, answer=LAB + a, sourceSection='B. Give short answers to the following questions.') for q, a in zip(SQ, SQ_ANS)],
                detailedQuestions=[dict(q=q, answer=LAB + a, sourceSection='C. Give detailed answers to the following questions.') for q, a in zip(LQ, LQ_ANS)],
                activities=[dict(title='Activity (page 98)', desc='Identify the following cells and label the marked parts of cells. (Unlabeled plant cell and animal cell diagrams are reproduced in the lesson.)', sourcePrintedPage=98)])
