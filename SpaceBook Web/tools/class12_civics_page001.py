"""Civics XII front matter: PDF1 cover; PDF2 advertisement (excluded, no record); PDF3 imprint (right) + contents (left); PDF4 contents; PDF5 contents end (right).
PDF5's left page (p.1, Chapter 1 opener) is in class12_civics_page005.py which calls contents_end() from here.
Run: python class12_civ_page001.py N (1, 3, 4)."""
import sys
from class12_civics_common import BOOK, Builder

FM = ('Front matter', 'ابتدائیہ', 'سریزه')

# (en, ur, ps, page); a leading '#' in en marks a chapter row
TOC = [
 ('#Chapter 1: The System of Government of Pakistan', 'باب ۱: پاکستان کا نظامِ حکومت', '۱ څپرکی: د پاکستان د حکومت نظام', '1'),
 ('A. Government of Pakistan', 'الف۔ حکومتِ پاکستان', 'الف. د پاکستان حکومت', '2'),
 ('Foundations of the structure of the Government of Pakistan', 'حکومتِ پاکستان کی ساخت کی بنیادیں', 'د پاکستان د حکومت د جوړښت بنسټونه', '2'),
 ('Comparison of democracy and dictatorship in Pakistan', 'پاکستان میں جمہوریت اور آمریت کا موازنہ', 'په پاکستان کې د ډیموکراسۍ او دیکتاتورۍ پرتله', '4'),
 ('Role of democratic governments in meeting public needs in Pakistan', 'پاکستان میں عوامی ضروریات کی تکمیل کیلئے جمہوری حکومتوں کا کردار', 'په پاکستان کې د خلکو د اړتیاوو په پوره کولو کې د ډیموکراتیکو حکومتونو رول', '9'),
 ('Ways of making the government in Pakistan more democratic', 'پاکستان میں حکومت کو مزید جمہوری بنانے کے طریقے', 'په پاکستان کې د حکومت لا ډیموکراتیکه کولو لارې', '11'),
 ('B. Institutions of government', 'ب۔ حکومت کے ادارے', 'ب. د حکومت ادارې', '15'),
 ('Functions or duties of the legislature in Pakistan', 'پاکستان میں مقننہ کے افعال یا فرائض', 'په پاکستان کې د مقننې دندې یا فرایض', '16'),
 ('Duties of the executive or administration in Pakistan', 'پاکستان میں عاملہ یا انتظامیہ کے فرائض', 'په پاکستان کې د اجرائیې یا ادارې فرایض', '19'),
 ('Functions or duties of the Supreme Court in Pakistan', 'پاکستان میں سپریم کورٹ کے افعال یا فرائض', 'په پاکستان کې د سترې محکمې دندې یا فرایض', '23'),
 ('Comparison of the executive, legislature and judiciary in periods of democracy and dictatorship', 'عاملہ، مقننہ اور عدلیہ کا جمہوریت اور آمریت کے ادوار میں موازنہ', 'د ډیموکراسۍ او دیکتاتورۍ په دورو کې د اجرائیې، مقننې او قضا پرتله', '25'),
 ('Comparison of the powers of the President and the Prime Minister under the Constitution of 1973', 'دستور 1973ء کے تحت صدر اور وزیرِ اعظم کے اختیارات کا موازنہ', 'د ۱۹۷۳ کال د اساسي قانون له مخې د ولسمشر او لومړي وزیر د واکونو پرتله', '27'),
 ('Responsibilities of the police', 'پولیس کی ذمہ داریاں', 'د پولیسو مسؤلیتونه', '28'),
 ('Role of the army as a government institution', 'بطور حکومتی ادارہ فوج کا کردار', 'د حکومتي ادارې په توګه د پوځ رول', '30'),
 ('#Chapter 2: Rights of Children and Women', 'باب ۲: بچوں اور خواتین کے حقوق', '۲ څپرکی: د ماشومانو او ښځو حقونه', '36'),
 ('Children', 'بچے', 'ماشومان', '37'),
 ('Need for a convention on the rights of the child', 'بچوں کے حقوق پر معاہدہ کی ضرورت', 'د ماشومانو د حقونو پر تړون اړتیا', '37'),
 ('Rights of children in the CRC', 'سی آر سی میں بچوں کے حقوق', 'په CRC کې د ماشومانو حقونه', '38'),
 ('Participation rights of children in the CRC', 'سی آر سی میں بچوں کی شرکت کے حقوق', 'په CRC کې د ماشومانو د ګډون حقونه', '42'),
 ('Basic principles of the Convention on the Rights of the Child', 'بچوں کے حقوق کے کنونشن کے بنیادی اصول', 'د ماشومانو د حقونو د کنوانسیون بنسټیز اصول', '44'),
 ('Comparison of the rights given in the Convention on the Rights of the Child and the rights of children in Islam', 'بچوں کے حقوق کے کنونشن میں دیئے گئے حقوق اور اسلام میں بچوں کے حقوق کا موازنہ', 'د ماشومانو د حقونو په کنوانسیون کې ورکړل شویو حقونو او په اسلام کې د ماشومانو د حقونو پرتله', '45'),
 ('Responsibilities of parents', 'والدین کی ذمہ داریاں', 'د مور او پلار مسؤلیتونه', '47'),
 ('Rights of women', 'خواتین کے حقوق', 'د ښځو حقونه', '49'),
 ('Sex and Gender', 'نر مادہ (Sex) اور مذکر مونث (Gender)', 'نر او ښځه (Sex) او مذکر او مؤنث (Gender)', '50'),
 ('The Convention on the Elimination of Discrimination against Women and the rights of women in Islam', 'خواتین کے خلاف امتیازات ختم کرنے کا کنونشن اور اسلام میں خواتین کے حقوق', 'د ښځو پر وړاندې د تبعیض د له منځه وړلو کنوانسیون او په اسلام کې د ښځو حقونه', '50'),
 ('#Chapter 3: Political Economy', 'باب ۳: سیاسی اقتصادیات', '۳ څپرکی: سیاسي اقتصاد', '56'),
 ('Positive and negative effects of economic globalisation on the economy of Pakistan', 'پاکستان کی معیشت پر اقتصادی عالمگیریت کے مثبت اور منفی اثرات', 'د پاکستان پر اقتصاد د اقتصادي نړیوالتوب مثبت او منفي اغېزې', '59'),
 ('Requirements of an economy based on self-reliance', 'خود انحصاری پر مبنی اقتصادیات کے لوازمات', 'د ځان‌بسیاینې پر بنسټ د اقتصاد اړتیاوې', '60'),
 ('International financial institutions (duties and objectives)', 'عالمی مالیاتی ادارے (فرائض اور مقاصد)', 'نړیوالې مالي ادارې (فرایض او موخې)', '62'),
 ('Political effects of international economic and financial institutions', 'بین الاقوامی اقتصادی و مالیاتی اداروں کے سیاسی اثرات', 'د نړیوالو اقتصادي او مالي ادارو سیاسي اغېزې', '66'),
 ('Proposals for change in international economic institutions', 'بین الاقوامی معاشی اداروں میں تبدیلی کی تجاویز', 'په نړیوالو اقتصادي ادارو کې د بدلون وړاندیزونه', '68'),
 ('Pakistan and world trade', 'پاکستان اور عالمی تجارت', 'پاکستان او نړیواله سوداګري', '71'),
 ('Effects of world trade agreements on Pakistan.', 'عالمی تجارت کے معاہدات کا پاکستان پر اثرات۔', 'پر پاکستان د نړیوالې سوداګرۍ د تړونونو اغېزې.', '72'),
 ('Difficulties of Pakistan in achieving economic stability', 'معاشی استحکام کے حصول میں پاکستان کی مشکلات', 'د اقتصادي ثبات په ترلاسه کولو کې د پاکستان ستونزې', '74'),
 ('Economic development and freedom from debt.', 'معاشی ترقی اور قرض سے چھٹکارا۔', 'اقتصادي پرمختګ او له پور خلاصون.', '76'),
 ('#Chapter 4: International Conflicts and their Resolution', 'باب ۴: بین الاقوامی تنازعات اور حل', '۴ څپرکی: نړیوالې شخړې او حل', '81'),
 ('Historical background of present world conflicts', 'موجودہ عالمی تنازعات کا تاریخی پس منظر', 'د اوسنیو نړیوالو شخړو تاریخي شالید', '82'),
 ('Use of negotiation for resolving conflicts at the world level', 'عالمی سطح پر تنازعات کے حل کے لیے گفت و شنید کا استعمال', 'په نړیواله کچه د شخړو د حل لپاره د خبرو اترو کارونه', '89'),
 ('Causes of world conflicts', 'عالمی تنازعات کی وجوہات', 'د نړیوالو شخړو لاملونه', '90'),
 ('Effective strategies for resolving conflicts', 'تنازعات کے حل کے لیے موثر حکمت عملیاں', 'د شخړو د حل لپاره اغېزمنې تګلارې', '92'),
 ('Functions of the International Court of Justice', 'عالمی عدالتِ انصاف کے فرائض', 'د عدالت نړیوالې محکمې فرایض', '95'),
 ('Role of individuals in mediation and negotiation in international conflicts', 'بین الاقوامی تنازعات میں ثالثی اور گفت و شنید کیلئے افراد کا کردار', 'په نړیوالو شخړو کې د منځګړیتوب او خبرو اترو لپاره د افرادو رول', '96'),
 ('Qualities of a good mediator and negotiator', 'ایک اچھے ثالث اور گفت و شنید کرنے والے کے خواص', 'د یوه ښه منځګړي او خبرې اترې کوونکي ځانګړنې', '97'),
 ('How the characteristics of a good mediator and negotiator can be adopted. Suggestions', 'اچھے ثالث و گفت و شنید کرنے والے کی خصوصیات کیسے اپنائی جاسکتی ہیں۔ تجاویز', 'د ښه منځګړي او خبرې اترې کوونکي ځانګړنې څنګه غوره کېدای شي. وړاندیزونه', '98'),
 ('#Chapter 5: Intellectual Skills', 'باب ۵: علمی مہارتیں', '۵ څپرکی: علمي مهارتونه', '103'),
 ('Use of websites', 'ویب سائٹس کا استعمال', 'د وېبپاڼو کارونه', '104'),
 ('Reading information from websites and identifying it for achieving a purpose', 'ویب سائٹس سے معلومات پڑھنا اور مقصد کے حصول کیلئے اُن کی نشاندہی', 'له وېبپاڼو معلومات لوستل او د موخې د ترلاسه کولو لپاره یې پېژندنه', '105'),
 ('Collecting and arranging information and reaching a conclusion', 'معلومات کو جمع کر کے ترتیب دینا اور نتیجے تک پہنچنا', 'معلومات راټولول، ترتیبول او پایلې ته رسېدل', '106'),
 ('Building arguments on the basis of collected information', 'جمع شدہ معلومات کی بنیاد پر دلیل سازی', 'د راټولو شویو معلوماتو پر بنسټ دلیل جوړول', '107'),
 ('Methods of solving problems in the light of information', 'معلومات کی روشنی میں مسائل حل کرنے کے طریقے', 'د معلوماتو په رڼا کې د ستونزو د حل لارې', '108'),
 ('Proposing government policy for solving problems', 'مسائل کے حل کے لیے سرکاری پالیسی کی تجویز', 'د ستونزو د حل لپاره د دولتي پالیسۍ وړاندیز', '109'),
 ('Methods of spreading information and news', 'معلومات اور اطلاعات کے پھیلاؤ کے طریقے', 'د معلوماتو او خبرونو د خپرولو لارې', '111'),
 ('#Chapter 6: Political Parties and Social Movements', 'باب ۶: سیاسی جماعتیں اور سماجی تحاریک', '۶ څپرکی: سیاسي ګوندونه او ټولنیز خوځښتونه', '115'),
 ('Political parties', 'سیاسی جماعتیں', 'سیاسي ګوندونه', '116'),
 ('Structure and composition of political parties.', 'سیاسی جماعتوں کی ساخت اور بناوٹ۔', 'د سیاسي ګوندونو جوړښت او بڼه.', '118'),
 ('Performance of a political party’s government in the light of its manifesto', 'سیاسی جماعت کی حکومت کا اُسکے منشور کی روشنی میں کارکردگی', 'د یوه سیاسي ګوند د حکومت کړنې د هغه د منشور په رڼا کې', '121'),
 ('Social movement', 'سماجی تحریک', 'ټولنیز خوځښت', '123'),
 ('Importance of social movements in making Pakistan an Islamic, democratic and welfare state', 'پاکستان کو بطورِ اسلامی، جمہوری اور فلاحی ریاست کے بنانے میں سماجی تحاریک کی اہمیت', 'د پاکستان د اسلامي، ډیموکراتیک او هوساینې دولت په جوړولو کې د ټولنیزو خوځښتونو اهمیت', '125'),
 ('Causes of social movements', 'سماجی تحاریک کے وجوہات', 'د ټولنیزو خوځښتونو لاملونه', '127'),
 ('Ways of promoting peace at the local level', 'مقامی سطح پر امن کے فروغ کے طریقے', 'په سیمه‌ییزه کچه د سولې د ودې لارې', '129'),
 ('#Chapter 7: Peace and Diversity', 'باب ۷: امن اور تنوع', '۷ څپرکی: سوله او تنوع', '134'),
 ('Peace', 'امن', 'سوله', '135'),
 ('Importance of a peaceful society', 'پُرامن معاشرے کی اہمیت', 'د سوله‌ییزې ټولنې اهمیت', '135'),
 ('Characteristics of a peaceful society', 'پُرامن معاشرہ کے خصوصیات', 'د سوله‌ییزې ټولنې ځانګړنې', '136'),
 ('Causes of conflicts and wars at the local, national and world level', 'مقامی قومی اور عالمی سطح پر تنازعات اور جنگوں کی وجوہات', 'په سیمه‌ییزه، ملي او نړیواله کچه د شخړو او جګړو لاملونه', '13…'),
 ('Consequences and effects of conflicts and wars at the local, national and world level', 'مقامی قومی اور عالمی سطح پر تنازعات اور جنگوں کے نتائج اور اثرات', 'په سیمه‌ییزه، ملي او نړیواله کچه د شخړو او جګړو پایلې او اغېزې', '139'),
 ('Identifying groups affected by conflicts and wars at the local, national and world level', 'مقامی، قومی اور عالمی سطح پر تنازعات اور جنگوں سے متاثر ہونے والے گروہوں کی نشاندہی', 'په سیمه‌ییزه، ملي او نړیواله کچه له شخړو او جګړو د اغېزمنو ډلو پېژندنه', '141'),
 ('Discrimination', 'امتیازات', 'تبعیضونه', '143'),
 ('Diversity', 'تنوع', 'تنوع', '144'),
 ('Stereotype', 'سٹیریو ٹائپ', 'کلیشه (سټیریوټایپ)', '145'),
 ('Prejudice', 'فرضی تصور وار', 'مخکېنی قضاوت', '146'),
 ('Characteristics of diverse societies', 'متنوع معاشروں کے خصوصیات', 'د متنوعو ټولنو ځانګړنې', '146'),
 ('Problems arising from diversity in Pakistani society', 'پاکستانی معاشرہ میں تنوع سے پیدا ہونے والے مسائل', 'په پاکستاني ټولنه کې له تنوع څخه راپیدا شوې ستونزې', '147'),
 ('Role of different cultures, values and beliefs in our life and society', 'ہماری زندگی اور معاشرہ میں مختلف ثقافتوں، اقدار اور عقائد کا کردار', 'زموږ په ژوند او ټولنه کې د بېلابېلو کلتورونو، ارزښتونو او عقیدو رول', '148'),
 ('Difference between Pakistani culture and world culture with reference to diversity', 'تنوع کے حوالے سے پاکستانی ثقافت اور عالمی ثقافت میں فرق', 'د تنوع په اړه د پاکستاني کلتور او نړیوال کلتور توپیر', '150'),
 ('Diversity at the world level (the need to highlight it)', 'عالمی سطح پر تنوع (اُجاگر کرنے کی ضرورت)', 'په نړیواله کچه تنوع (د راڅرګندولو اړتیا)', '151'),
 ('Ways of strengthening diversity at the world level', 'عالمی سطح پر تنوع کو مضبوط بنانے کے طریقے', 'په نړیواله کچه د تنوع د پیاوړي کولو لارې', '152'),
 ('Ways of promoting diversity of values in Pakistan', 'پاکستان میں اقداری تنوع کے فروغ کے طریقے', 'په پاکستان کې د ارزښتونو د تنوع د ودې لارې', '153'),
 ('Promotion of diversity and tolerance in society and way of life', 'معاشرے میں تنوع اور رواداری کا فروغ اور انداز زندگی', 'په ټولنه کې د تنوع او زغم وده او د ژوند طرز', '154'),
 ('#Chapter 8: Active and Responsible Citizenship', 'باب ۸: فعال اور ذمہ دار شہریت', '۸ څپرکی: فعاله او مسؤله تابعیت', '157'),
 ('Learning through role play.', 'تلبیس کے ذریعے سیکھنا۔', 'د رول لوبولو له لارې زده‌کړه.', '158'),
 ('Public service message.', 'عوامی خدمت کا پیغام۔', 'د عامه خدمت پیغام.', '161'),
 ('Signature campaign.', 'دستخطی مہم۔', 'د لاسلیک کمپاین.', '163'),
 ('Community service.', 'کیمونٹی سروس۔', 'ټولنیز خدمت.', '163'),
 ('Tragedy or accident', 'سانحہ یا حادثہ', 'غمیزه یا پېښه', '165'),
 ('Management of tragedies.', 'سانحات کا انتظام۔', 'د غمیزو مدیریت.', '165'),
 ('#Special terms (Glossary)', 'مخصوص اصطلاحات', 'ځانګړې اصطلاحګانې', '170'),
 ('#Something about the author', 'کچھ مصنف کے بارے میں', 'د لیکوال په اړه یو څه', '181'),
]


def toc_table(b, tid, rows):
    H = (['Topic', 'Page'], ['مضمون', 'صفحہ'], ['موضوع', 'مخ'])
    clean = lambda s: s.lstrip('#')
    b.table(tid, H[0], [[clean(e), p] for e, u, s, p in rows], H[1], H[2], [[u, p] for e, u, s, p in rows], [[s, p] for e, u, s, p in rows])


def p1():
    b = Builder()
    b.h('Civics — for Class Twelve', 'شہریت — برائے بارھویں جماعت', 'مدني زده‌کړه (تابعیت) — د دولسم ټولګي لپاره')
    b.p('Khyber Pakhtunkhwa Textbook Board, Peshawar', 'خیبر پختونخوا ٹیکسٹ بک بورڈ پشاور', 'د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور')
    b.p('Free From Government — NOT FOR SALE', 'Free From Government — NOT FOR SALE', 'Free From Government — NOT FOR SALE')
    b.paras[-1]['untranslatedByDesign'] = True
    r = BOOK.record(b, 'civ12-fm-cover', 'Front cover', 'سرورق', 'پښتۍ', 1, [None], unit_title=FM)
    r['sourceCoverIllustrationReview'] = 'Cover photographs (Parliament House, Islamabad and the National Assembly chamber) and the Board logo are decorative; not reproduced.'
    BOOK.save(1, [('FM', r)], issues=[{'id': 'civ12-pdf001', 'unit': 'FM', 'printedPage': None,
               'description': 'The download-site banner lines above and below every scan (“Downloaded from …”, WhatsApp number, download notice) are third-party additions and are excluded throughout. Owner pen marks on the cover excluded.'}])


def p3():
    b = Builder()
    b.h('All rights reserved with Leading Publishers', 'جملہ حقوق بحق لیڈنگ پبلشرز محفوظ ہیں', 'ټول حقونه لیډنګ پبلشرز ته خوندي دي')
    for x in [
        ('Approved by: Directorate of Curriculum and Teacher Education Khyber Pakhtunkhwa, Abbottabad', 'منظور کردہ: نظامت نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد', 'منظور کړی: د خیبر پښتونخوا د نصاب او ښوونکو د روزنې ریاست، ایبټ اباد'),
        ('In accordance with: National Curriculum 2006', 'بمطابق: قومی نصاب 2006', 'له مخې: ملي نصاب 2006'),
        ('Letter No. 2272-75/SS-II dated 21-03-2013', 'مراسلہ نمبر 2272-75/SS-II مورخہ 21-03-2013', 'لیک شمېره 2272-75/SS-II نېټه 21-03-2013'),
        ('Author: Professor Bakhtiar', 'مصنف: پروفیسر بختیار', 'لیکوال: پروفیسر بختیار'),
        ('Review supervision committee: Syed Bashir Hussain Shah, Director, Directorate of Curriculum and Teacher Education Khyber Pakhtunkhwa, Abbottabad', 'نگران نظرِ ثانی کمیٹی: سید بشیر حسین شاہ ناظم، نظامت نصاب و تعلیمِ اساتذہ خیبر پختونخوا، ایبٹ آباد', 'د بیاکتنې د څارنې کمېټه: سید بشیر حسین شاه، رییس، د خیبر پښتونخوا د نصاب او ښوونکو د روزنې ریاست، ایبټ اباد'),
        ('Review: Professor Dr. Muhammad Azam, Political Science Department, Hazara University; Tariq Iqbal, Assistant Professor, Government Post Graduate College No. 1, Abbottabad; Muhammad Hanif Khan, Subject Specialist, Government Higher Secondary School Nawanshehr, Abbottabad; Fazal-ur-Rahman, Subject Specialist, Directorate of Curriculum and Teacher Education, Abbottabad; Muhammad Ilyas, Assistant Subject Specialist, Textbook Board, Peshawar',
         'نظرِ ثانی: پروفیسر ڈاکٹر محمد اعظم، پولیٹیکل سائنس ڈیپارٹمنٹ ہزارہ یونیورسٹی؛ طارق اقبال، اسسٹنٹ پروفیسر، گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1 ایبٹ آباد؛ محمد حنیف خان، ماہرِ مضمون، گورنمنٹ ہائیر سیکنڈری اسکول نواں شہر ایبٹ آباد؛ فضل الرحمٰن، ماہرِ مضمون، ڈائریکٹریٹ آف کریکولم اینڈ ٹیچر ایجوکیشن ایبٹ آباد؛ محمد الیاس، اسسٹنٹ ماہرِ مضمون، ٹیکسٹ بک بورڈ پشاور',
         'بیاکتنه: پروفیسر ډاکټر محمد اعظم، د هزارې پوهنتون د سیاسي علومو څانګه؛ طارق اقبال، اسسټنټ پروفیسر، حکومتي پوسټ ګرېجویټ کالج ۱ شمېره ایبټ اباد؛ محمد حنیف خان، د مضمون متخصص، حکومتي لوړ ثانوي ښوونځی نواں‌شهر ایبټ اباد؛ فضل الرحمن، د مضمون متخصص، د نصاب او ښوونکو د روزنې ریاست ایبټ اباد؛ محمد الیاس، مرستیال د مضمون متخصص، د درسي کتابونو بورډ پېښور'),
        ('Editor: Muhammad Hussain, Subject Specialist, Khyber Pakhtunkhwa Textbook Board, Peshawar.', 'ایڈیٹر: محمد حسین، ماہرِ مضمون، خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور۔', 'اېډیټر: محمد حسین، د مضمون متخصص، د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور.'),
        ('Under the supervision and guidance of: Rasheed Khan Paindakhel (Chairman); Saeed-ur-Rahman (Member E&P); Khyber Pakhtunkhwa Textbook Board, Peshawar', 'زیرِ نگرانی و رہنمائی: رشید خان پائندہ خیل (چیئرمین)؛ سعید الرحمٰن (ممبر ای اینڈ پی)؛ خیبر پختونخوا ٹیکسٹ بک بورڈ، پشاور', 'د څارنې او لارښوونې لاندې: رشید خان پاینده‌خېل (رییس)؛ سعید الرحمن (غړی E&P)؛ د خیبر پښتونخوا د درسي کتابونو بورډ، پېښور'),
        ('Academic year: 2021-22; Website: www.kptbb.gov.pk; E-mail: membertbb@yahoo.com; Telephone No.: 091-9217159-60', 'تعلیمی سال: 2021-22ء؛ ویب سائٹ: www.kptbb.gov.pk؛ ای میل: membertbb@yahoo.com؛ ٹیلی فون نمبر: 091-9217159-60', 'تعلیمي کال: 2021-22؛ وېبپاڼه: www.kptbb.gov.pk؛ برېښنالیک: membertbb@yahoo.com؛ د ټیلیفون شمېره: 091-9217159-60'),
    ]:
        b.p(*x)
    r1 = BOOK.record(b, 'civ12-fm-imprint', 'Imprint', 'طباعتی تفصیلات', 'د چاپ جزییات', 3, [None])
    c = Builder()
    c.h('Contents', 'فہرستِ مضامین', 'نیوولیک')
    toc_table(c, 'civ12-toc-1', TOC[:20])
    r2 = BOOK.record(c, 'civ12-fm-contents-1', 'Contents (1)', 'فہرستِ مضامین (۱)', 'نیوولیک (۱)', 3, [None])
    r2['sourceNote'] = 'The contents are reproduced as a structured table (topic, page); chapter rows are the banded rows of the printed list.'
    BOOK.save(3, [('FM', r1), ('FM', r2)])


def p4():
    c = Builder()
    toc_table(c, 'civ12-toc-2', TOC[20:66])
    r = BOOK.record(c, 'civ12-fm-contents-2', 'Contents (2)', 'فہرستِ مضامین (۲)', 'نیوولیک (۲)', 4, [None])
    BOOK.save(4, [('FM', r)], issues=[{'id': 'civ12-pdf004', 'unit': 'FM', 'printedPage': None,
               'description': 'The last digit of the page number for “مقامی قومی اور عالمی سطح پر تنازعات اور جنگوں کی وجوہات” is cut off at the gutter of the scan and is shown as “13…”. Contents spellings (e.g. “پُرامن معاشرہ کے خصوصیات”, “کچھ مصنف کے بارے میں”) are retained as printed.'}])


def contents_end():
    c = Builder()
    toc_table(c, 'civ12-toc-3', TOC[66:])
    return BOOK.record(c, 'civ12-fm-contents-3', 'Contents (3)', 'فہرستِ مضامین (۳)', 'نیوولیک (۳)', 5, [None])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    {1: p1, 3: p3, 4: p4}[n]()
