import json
from class12_source_review import OUT, ROOT, upsert, section, checkpoint
from physics_agent2_translations import TRANSLATIONS, TITLES

SOURCE = 'Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
# Separate printed credit lines; no invented em dashes or punctuation.
CREDITS = [
 ('All rights reserved with the Leading Books Publishers, Peshawar.', 'تمام حقوق لیڈنگ بکس پبلشرز، پشاور کے پاس محفوظ ہیں۔', 'ټول حقوق له لیډنګ بکس خپرندویانو، پېښور سره خوندي دي.'),
 ('Reviewed and Approved by: Directorate of Curriculum and Teachers Education, Abbottabad vide NOC No: 2678-80/Physics-XII//F.01/Vol-1/NC-2006 Dated: 06.05.2021', 'جائزہ اور منظوری: نظامتِ نصاب و تعلیمِ اساتذہ، ایبٹ آباد؛ عدم اعتراض سرٹیفکیٹ نمبر 2678-80/Physics-XII//F.01/Vol-1/NC-2006، مورخہ 06.05.2021۔', 'کتنه او منظوري: د نصاب او د ښوونکو د روزنې ریاست، اېبټ اباد؛ د نه اعتراض سند شمېره 2678-80/Physics-XII//F.01/Vol-1/NC-2006، نېټه 06.05.2021.'),
 ('According to National Curriculum 2006', 'قومی نصاب 2006 کے مطابق', 'د 2006 کال له ملي نصاب سره سم'),
 ('Authors:', 'مصنفین:', 'لیکوالان:'),
 ('Prof. Shaukat Ali Taran', 'پروفیسر شوکت علی تران', 'پروفیسور شوکت علي تران'),
 ('Government Post Graduate College Timergara', 'گورنمنٹ پوسٹ گریجویٹ کالج، تیمرگرہ', 'دولتي پوسټ ګرېجویټ کالج، تیمرګره'),
 ('Shadah Gul, Assistant Prof.', 'شادہ گل، اسسٹنٹ پروفیسر', 'شاده ګل، مرستیال پروفیسور'),
 ('Government Post Graduate College, Lakki Marwat', 'گورنمنٹ پوسٹ گریجویٹ کالج، لکی مروت', 'دولتي پوسټ ګرېجویټ کالج، لکي مروت'),
 ('Dr. Naeem Khalid', 'ڈاکٹر نعیم خالد', 'ډاکټر نعیم خالد'),
 ('Dean of Sciences, Islamia College, Peshawer', 'ڈین آف سائنسز، اسلامیہ کالج، پشاور', 'د ساینس پوهنځیو مشر، اسلامیه کالج، پېښور'),
 ('Prof. Abdul Baseer', 'پروفیسر عبدالبصیر', 'پروفیسور عبدالبصیر'),
 ('Edwardes College, Peshawer', 'ایڈورڈز کالج، پشاور', 'اېډورډز کالج، پېښور'),
 ('Abdul Rehman, Lecturer', 'عبدالرحمان، لیکچرر', 'عبدالرحمان، استاد'),
 ('Akram Khan Durrani College Bannu', 'اکرم خان درانی کالج، بنوں', 'اکرم خان دراني کالج، بنو'),
 ('Aamir Ullah Khan', 'عامر اللہ خان', 'عامر الله خان'),
 ('Director, Pakistan Virtual College, Hayatabad Peshawar', 'ڈائریکٹر، پاکستان ورچوئل کالج، حیات آباد، پشاور', 'رئیس، پاکستان ورچول کالج، حیات اباد، پېښور'),
 ('Hafiz Mehar Elahi', 'حافظ مہر الٰہی', 'حافظ مهر الهي'),
 ('Peshawar Model Degree College, Peshawer', 'پشاور ماڈل ڈگری کالج، پشاور', 'پېښور ماډل ډګري کالج، پېښور'),
 ('Review Supervision:', 'جائزے کی نگرانی:', 'د کتنې څارنه:'),
 ('Gohar Ali Khan, Director, Curriculum and Teachers Education, Abbottabad.', 'گوہر علی خان، ڈائریکٹر، نصاب و تعلیمِ اساتذہ، ایبٹ آباد۔', 'ګوهر علي خان، د نصاب او د ښوونکو د روزنې رئیس، اېبټ اباد.'),
 ('Focal Person:', 'فوکل پرسن:', 'د اړیکو مسؤول:'),
 ('Zulfiqar Khan, Additional Director (Curriculum and Textbook Review) DCTE, Abbottabad.', 'ذوالفقار خان، ایڈیشنل ڈائریکٹر (نصاب و درسی کتب کا جائزہ)، ڈی سی ٹی ای، ایبٹ آباد۔', 'ذوالفقار خان، اضافي رئیس (د نصاب او درسي کتابونو کتنه)، ډي سي ټي اي، اېبټ اباد.'),
 ('Re-reviewers:', 'دوبارہ جائزہ لینے والے:', 'بیاکتونکي:'),
 ('[Editorial note: first reviewer name is faint; spelling unresolved.]', '[ادارتی نوٹ: پہلے جائزہ لینے والے کا نام مدھم ہے؛ ہجے ابھی واضح نہیں۔]', '[د سمونوال یادونه: د لومړي بیاکتونکي نوم تت دی؛ املا یې لا روښانه نه ده.]'),
 ('Associate Prof. G.P.G College Mandian, Abbottabad', 'ایسوسی ایٹ پروفیسر، گورنمنٹ پوسٹ گریجویٹ کالج منڈیاں، ایبٹ آباد', 'همکار پروفیسور، دولتي پوسټ ګرېجویټ کالج منډیان، اېبټ اباد'),
 ('[Editorial note: second reviewer name is faint; spelling unresolved.]', '[ادارتی نوٹ: دوسرے جائزہ لینے والے کا نام مدھم ہے؛ ہجے ابھی واضح نہیں۔]', '[د سمونوال یادونه: د دویم بیاکتونکي نوم تت دی؛ املا یې لا روښانه نه ده.]'),
 ('(Subject Specialist ) GHSS Bandi Dhundan, Abbottabad', '(مضمون کے ماہر) گورنمنٹ ہائر سیکنڈری سکول بانڈی ڈھونڈاں، ایبٹ آباد', '(د مضمون متخصص) دولتي لوړه ثانوي ښوونځی بانډي ډهونډان، اېبټ اباد'),
 ('Muhammad Arshid', 'محمد ارشد', 'محمد ارشد'),
 ('(Subject Specialist ) GHSS Lassan Thakral, Mansehra', '(مضمون کے ماہر) گورنمنٹ ہائر سیکنڈری سکول لساں ٹھکرال، مانسہرہ', '(د مضمون متخصص) دولتي لوړه ثانوي ښوونځی لسان تهکرال، مانسهره'),
 ('Shafqat Hussain', 'شفقت حسین', 'شفقت حسین'),
 ('(Subject Specialist ) Desk Officer, DCTE, Abbottabad', '(مضمون کے ماہر) ڈیسک افسر، ڈی سی ٹی ای، ایبٹ آباد', '(د مضمون متخصص) د څانګې افسر، ډي سي ټي اي، اېبټ اباد'),
 ('Nasir Kamal (Assistant Subject Specialist )', 'ناصر کمال (معاون ماہرِ مضمون)', 'ناصر کمال (د مضمون مرستیال متخصص)'),
 ('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
 ('Editor:', 'مدیر:', 'سمونوال:'),
 ('Nasir Kamal, Assistant Subject Specialist (Physics)', 'ناصر کمال، معاون ماہرِ مضمون (طبیعیات)', 'ناصر کمال، د مضمون مرستیال متخصص (فزیک)'),
 ('Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.'),
 ('Printing Supervision:', 'طباعت کی نگرانی:', 'د چاپ څارنه:'),
 ('Rashid khan Paindakhel (Chairman)', 'رشید خان پائندہ خیل (چیئرمین)', 'رشید خان پاینده خېل (مشر)'),
 ('Saeedur Rehman (Member E&P)', 'سعید الرحمان (رکن، ای اینڈ پی)', 'سعید الرحمان (د ای او پي غړی)'),
 ('Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.'),
 ('Academic Year 2021-22', 'تعلیمی سال 2021-22', 'تعلیمي کال 2021-22'),
 ('Email: membertbb@yahoo.com', 'ای میل: membertbb@yahoo.com', 'برېښنالیک: membertbb@yahoo.com'),
 ('Website: www.kptbb.gov.pk', 'ویب سائٹ: www.kptbb.gov.pk', 'وېبپاڼه: www.kptbb.gov.pk'),
 ('Phone: 091-9217159-60', 'فون: 091-9217159-60', 'ټیلیفون: 091-9217159-60'),
]

if __name__ == '__main__':
    record = {'id': 'phys12-front-publication', 'title': 'Publication information',
              'pdfPage': 4, 'printedPage': None, 'sourcePdf': SOURCE,
              'paragraphs': [pair[0] for pair in CREDITS],
              'sourceDefects': ['Two faint reviewer names remain unresolved; source images are local inspection evidence only.']}
    headings = {3, 18, 20, 22, 33, 36}
    layout = [{'type': 'heading' if i in headings else 'lines', 'indices': [i]} for i in range(len(CREDITS))]
    credits = section(record, CREDITS, layout, TITLES[record['id']])
    for i in (23, 25):
        credits['paras'][i]['isEditorial'] = True
        credits['paras'][i]['originalText'] = None
    old = json.loads((ROOT / 'docs/source-verification/physics-agent2-pages.json').read_text(encoding='utf-8'))
    preface = next(item for item in old if item['id'] == 'phys12-front-preface')
    preface['paragraphs'][2] = preface['paragraphs'][2].replace('For feedback and comment mail us at:', 'For feedback and comment mail us at :')
    preface_pairs = [(text, *pair) for text, pair in zip(preface['paragraphs'], TRANSLATIONS[preface['id']])]
    # The last two passages are consecutive source paragraphs, not one merged paragraph.
    preface_section = section(preface, preface_pairs,
                             [{'type': 'paragraph', 'indices': [i]} for i in range(4)], TITLES[preface['id']])
    upsert([record, preface], [credits, preface_section])
    checkpoint(4, 'corrected_unresolved', [record['id'], preface['id']],
               'Entire source spread inspected at 3x, author/reviewer crops at 6x, original JPG checked and split-source crop consulted. Raster reviewer crop removed from active source records and lesson visual fields. Printed credit headings, separate name/affiliation lines and column reading order reconstructed. Preface paragraph separation restored; English/Urdu/Pashto pairs checked. Two faint reviewer names explicitly marked as editorial unresolved locations, never guessed or presented as source text.',
               issues=['First and second re-reviewer names: complete PDF page 4, left printed page, immediately under Re-reviewers. Faint text remains insufficiently clear for exact spelling after local crop/JPG/split inspection.'])
