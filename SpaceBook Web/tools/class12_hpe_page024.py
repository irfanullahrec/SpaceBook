"""HPE XII PDF24–29: pp.19–24 — portal and coronary circulation; effects of exercise on the circulatory system; benefits of exercise; chapter 2 exercise;
chapter 3 (Doping) opener, list of doping substances, CNS stimulants, narcotics, steroids (begins). Run: python class12_hpe_page024.py N (24–29)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p24():
    b = Builder()
    P(b, [('… are called. This impure blood they bring into the right atrium of the heart. In both right chambers of the heart there is impure blood (Deoxygenated blood).',
           'cava) کہتے ہیں یہ غیر صاف شدہ خون دل کے دائیں اُذن میں لے آتے ہیں۔ دل کے دائیں خانوں میں غیر صاف شدہ خون (Deoxygenated blood) ہوتا ہے۔',
           '… ویل کېږي. دا ناپاکه وینه د زړه ښي اذین ته راوړي. د زړه په ښي خونو کې ناپاکه وینه (Deoxygenated blood) وي.')])
    b.h('3. Portal Circulation', '3۔ پورٹل گردش (Portal Circulation)', '3. پورټل ګرځښت (Portal Circulation)')
    P(b, [('In this circulation of blood some arteries supply blood to the stomach, intestines, pancreas, liver and spleen. On return this blood enters the liver through the portal vein (Portal Vein). This portal vein in the liver changes into fine tubes, i.e. capillaries. Here the surplus food components present in the blood are stored in the cells and tissues of the liver, and the remaining food components it supplies according to the need of the body. Then from the liver this blood goes back through two veins, i.e. the hepatic vein (Hepatic Vein), joins the inferior vena cava and goes straight into the right atrium of the heart.',
           'خون کے اس گردش میں کچھ شریانیں معدے، انتڑیوں، لبلبے، جگر اور تلی کو خون پہنچاتی ہیں۔ واپسی پر یہ خون پورٹل وین (Portal Vein) کے ذریعے جگر میں داخل ہوتا ہے۔ یہ پورٹل ورید جگر میں باریک نالیوں یعنی عروقِ شعریہ میں تبدیل ہو جاتی ہیں۔ یہاں پر خون میں موجود فاضل غذائی اجزاء جگر کے خلیات اور بافتوں میں ذخیرہ ہو جاتے ہیں اور باقی ماندہ غذائی اجزاء جسم کی ضرورت کے مطابق سپلائی کرتا ہے۔ پھر جگر سے یہ خون واپس دو وریدوں یعنی ہیپیٹک وین (Hepatic Vein) کے ذریعے زیریں وینا کیوا میں شامل ہو کر سیدھا دل کے دائیں اُذن میں چلا جاتا ہے۔',
           'د وینې په دې ګرځښت کې ځینې شریانونه معدې، کولمو، پانکراس، ځیګر او توري ته وینه رسوي. په بېرته راتګ دا وینه د پورټل وین (Portal Vein) له لارې ځیګر ته ننوځي. دا پورټل ورید په ځیګر کې په نریو رګونو، یعنې شعریه رګونو اوړي. دلته په وینه کې اضافي غذايي اجزا د ځیګر په حجرو او نسجونو کې زېرمه کېږي او پاتې غذايي اجزا د بدن د اړتیا سره سم رسوي. بیا له ځیګر دا وینه د دوو وریدونو، یعنې هېپاټیک وین (Hepatic Vein)، له لارې ښکتنۍ وینا کاوا ته ګډېږي او نېغه د زړه ښي اذین ته ځي.')])
    b.h('4. Coronary Circulation', '4۔ کورونری گردش (Coronary Circulation)', '4. کورونري ګرځښت (Coronary Circulation)')
    P(b, [('The heart works more than ordinary organs; therefore the muscles of the heart need oxygen and food components. When the aorta (Aorta) comes out from the left ventricle of the heart, then at its end two small arteries, coming out right and left, enter the muscles of the heart. These same arteries, then dividing into capillaries, provide oxygen and food components to the muscles of the heart, and from here pure blood changes into impure blood; then this blood goes through the coronary vein directly into the right atrium of the heart, and from there the blood does not come back into the coronary vein. This cycle of blood is called coronary circulation.',
           'دل عام اعضاء کی نسبت زیادہ کام کرتا ہے۔ اس لیے دل کے عضلات کو آکسیجن اور غذائی اجزاء کی ضرورت پڑتی ہے۔ دل کے بائیں بطن سے جب اے اورٹا (Aorta) نکلتا ہے تو اس کے سرے پر دو چھوٹی شریانیں دائیں اور بائیں نکل کر دل کے عضلات میں داخل ہو جاتی ہیں۔ یہی شریانیں پھر عروقِ شعریہ میں تقسیم ہو کر دل کے عضلات کو آکسیجن اور غذائی اجزاء فراہم کرتی ہیں اور یہاں سے صاف خون غیر صاف شدہ خون میں تبدیل ہو جاتا ہے پھر یہ خون کورونری ورید کے ذریعے براہِ راست دل کے دائیں اُذن میں چلا جاتا ہے اور وہاں سے خون واپس کورونری ورید میں نہیں آتا۔ خون کے اس چکر کو کورونری گردش کہتے ہیں۔',
           'زړه د عامو غړو په پرتله ډېر کار کوي. له همدې امله د زړه عضلو ته اکسیجن او غذايي اجزاوو ته اړتیا وي. کله چې له کیڼ بطین اورټا (Aorta) وځي، د هغې په سر دوه واړه شریانونه ښي او کیڼ لوري ته وځي او د زړه عضلو ته ننوځي. همدا شریانونه بیا په شعریه رګونو وېشل کېږي او د زړه عضلو ته اکسیجن او غذايي اجزا برابروي او دلته پاکه وینه په ناپاکه وینه اوړي، بیا دا وینه د کورونري ورید له لارې نېغه د زړه ښي اذین ته ځي او له هغه ځایه وینه بېرته کورونري ورید ته نه راځي. د وینې دې څرخ ته کورونري ګرځښت ویل کېږي.')])
    r = rec(b, 2, 9, 24)
    BOOK.save(24, [(2, r)], issues=[{'id': 'hpe12-pdf024', 'unit': 2, 'printedPage': 19,
               'description': '“یہ پورٹل ورید … تبدیل ہو جاتی ہیں”; the page opens with the end of the bracket “(Inferior Vena cava)” from p.18. Retained as printed.'}])


def p25():
    b = Builder()
    b.h('Effects of Exercise on Circulatory System', 'نظامِ دورانِ خون پر ورزش کے اثرات (Effects of Exercise on Circulatory System)', 'د وینې د جریان پر سیستم د تمرین اغېزې (Effects of Exercise on Circulatory System)')
    P(b, [('Under this system pure blood from the heart delivers oxygen and food components through the arteries to all the organs of the body, and then through the veins impure blood comes back into the heart.',
           'اس نظام کے تحت دل سے صاف خون، آکسیجن اور غذائی اجزاء شریانوں کے ذریعے سارے جسم کے اعضاء کو پہنچاتا ہے اور پھر وریدوں کے ذریعے غیر صاف شدہ خون دل میں واپس آتا ہے۔',
           'د دې سیستم له مخې له زړه پاکه وینه، اکسیجن او غذايي اجزا د شریانونو له لارې د بدن ټولو غړو ته رسوي او بیا د وریدونو له لارې ناپاکه وینه زړه ته راستنېږي.'),
          ('By doing exercise this system becomes better. Through exercise the muscles of the heart become thick and strong, through which speed and increase occur in the flow of blood from the heart. The more blood is supplied to the body, the more the supply of oxygen and food components too is to the physical organs, which is the guarantee of better health and energy.',
           'ورزش کرنے سے یہ نظام بہتر ہوتا ہے۔ ورزش سے دل کے عضلات موٹے اور مضبوط ہو جاتے ہیں جس سے دل کی جانب سے خون کے بہاؤ میں تیزی اور اضافہ ہو جاتا ہے۔ جس قدر زیادہ خون جسم کو سپلائی ہوتا ہے اسی قدر آکسیجن اور غذائی اجزاء کی سپلائی بھی جسمانی اعضاء کو زیادہ ہوتی ہے جو بہتر صحت اور توانائی کی ضمانت ہے۔',
           'په تمرین سره دا سیستم ښه کېږي. له تمرین د زړه عضلې پنډې او پیاوړې کېږي چې له امله یې د زړه له لوري د وینې په بهیر کې چټکتیا او زیاتوالی راځي. څومره چې بدن ته ډېره وینه رسېږي، همغومره بدني غړو ته د اکسیجن او غذايي اجزاوو رسول هم ډېر وي چې د ښې روغتیا او انرژۍ تضمین دی.'),
          ('The process of the flow of blood is called cardiac output (Cardiac output). The flow of blood from the heart is according to the intensity of exercise. In the state of rest the heart supplies 4 to 6 litres of blood to the body in one minute, but by doing more exercise more blood is supplied to the body. One cycle of blood in the body is completed in 0.08 minutes. For example:',
           'خون کے بہاؤ کے عمل کو کارڈیک آؤٹ پٹ (Cardiac output) کہتے ہیں۔ دل سے خون کا بہاؤ ورزش کی شدت کے مطابق ہوتا ہے۔ آرام کی حالت میں دل ایک منٹ میں 4 سے 6 لیٹر خون جسم کو سپلائی کرتا ہے لیکن زیادہ ورزش کرنے سے زیادہ خون جسم کو سپلائی ہوتا ہے۔ جسم میں خون کا ایک چکر 0.08 منٹ میں مکمل ہوتا ہے۔ مثال کے طور پر',
           'د وینې د بهیر عمل ته کارډیک اوټپټ (Cardiac output) ویل کېږي. له زړه د وینې بهیر د تمرین د شدت سره سم وي. د استراحت په حالت کې زړه په یوه دقیقه کې له ۴ تر ۶ لیتره وینه بدن ته رسوي، خو په ډېر تمرین ډېره وینه بدن ته رسېږي. په بدن کې د وینې یو څرخ په ۰.۰۸ دقیقو کې بشپړېږي. د بېلګې په توګه:')])
    b.group('lines', [
        ('In the state of rest the heartbeat is 72 times per minute: 72 x 0.80 = 7.7 litres of blood per minute', 'دل کی دھڑکن آرام کی حالت میں 72 مرتبہ فی منٹ: 72 x 0.80 = 7.7 لٹر خون فی منٹ', 'د استراحت په حالت کې د زړه درزا په دقیقه کې ۷۲ ځله: 72 x 0.80 = 7.7 لیتره وینه په دقیقه کې'),
        ('During light exercise the heartbeat is 150 times per minute: 150 × 0.080 = 12 litres per minute', 'ہلکی ورزش کے دوران دل کی دھڑکن 150 مرتبہ فی منٹ: 150 × 0.080 = 12 لیٹر فی منٹ', 'د سپک تمرین پر مهال د زړه درزا په دقیقه کې ۱۵۰ ځله: 150 × 0.080 = 12 لیتره په دقیقه کې'),
        ('During moderate exercise 180 times: 180 × 0.080 = 14.5 litres per minute', 'درمیانی ورزش کے دوران 180 مرتبہ: 180 × 0.080 = 14.5 لیٹر فی منٹ', 'د منځني تمرین پر مهال ۱۸۰ ځله: 180 × 0.080 = 14.5 لیتره په دقیقه کې'),
        ('During intense exercise a person’s heartbeat reaches up to 220 times per minute.', 'تیز ورزش کے دوران انسان کے دل کی دھڑکن 220 مرتبہ فی منٹ تک پہنچ جاتی ہے۔', 'د سخت تمرین پر مهال د انسان د زړه درزا په دقیقه کې تر ۲۲۰ ځلو رسېږي.')])
    b.h('Benefits of exercise:', 'ورزش کے فوائد:', 'د تمرین ګټې:')
    L(b, [('By the habit of daily exercise there is no blood pressure.', 'روزانہ ورزش کی عادت سے بلڈ پریشر نہیں ہوتا۔', 'د ورځني تمرین په عادت د وینې فشار نه کېږي.'),
          ('Through exercise one can get relief from heart diseases.', 'ورزش سے دل کی بیماریوں سے نجات مل سکتی ہے۔', 'له تمرین د زړه له ناروغیو خلاصون ترلاسه کېدای شي.'),
          ('By doing exercise the heart becomes strong and healthy.', 'ورزش کرنے سے دل مضبوط اور صحت مند ہوتا ہے۔', 'په تمرین زړه پیاوړی او روغ کېږي.'),
          ('By doing exercise there is an increase in the number of red cells in the blood.', 'ورزش کرنے سے خون میں سرخ خلیوں کی تعداد میں اضافہ ہوتا ہے۔', 'په تمرین په وینه کې د سرو حجرو شمېر زیاتېږي.')])
    r = rec(b, 2, 10, 25)
    BOOK.save(25, [(2, r)], issues=[{'id': 'hpe12-pdf025', 'unit': 2, 'printedPage': 20,
               'description': 'The worked examples are retained as printed: the resting line uses “0.80” where the others use 0.080 (72 × 0.080 = 5.76, not 7.7); 150 × 0.080 = 12; 180 × 0.080 = 14.4 printed as 14.5; “0.08 منٹ” for one circulation cycle. A small owner pen mark at the top is excluded.'}])


def p26():
    b = Builder()
    L(b, [('During exercise, through the contraction and expansion of the muscles, there is an increase in the quantity of white cells in the blood.', 'ورزش کے دوران عضلات کے سکڑاؤ اور پھیلاؤ سے خون میں سفید خلیوں کی مقدار میں اضافہ ہوتا ہے۔', 'د تمرین پر مهال د عضلو د راټولېدو او غځېدو له امله په وینه کې د سپینو حجرو مقدار زیاتېږي.'),
          ('By doing exercise improvement comes in the power of resistance.', 'ورزش کرنے سے قوتِ مدافعت میں بہتری آتی ہے۔', 'په تمرین د دفاع په ځواک کې ښه والی راځي.'),
          ('By doing exercise the performance of all the remaining systems of the body becomes better, through which the body becomes energetic and strong.', 'ورزش کرنے سے جسم کے باقی سارے نظاموں کی کارکردگی بہتر ہوتی ہے جس سے جسم توانا اور مضبوط ہوتا ہے۔', 'په تمرین د بدن د نورو ټولو سیستمونو کړنې ښې کېږي چې له امله یې بدن ځواکمن او پیاوړی کېږي.')])
    r = rec(b, 2, 11, 26)
    deco(r, 'A collage (fruit and vegetables, a heart with a stethoscope, a crossed-out fast-food plate, a crossed-out cigarette and a walking woman before a clock face) fills the rest of the page and is decorative.')
    BOOK.save(26, [(2, r)])


def p27():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The human heart has ________ chambers.', 'انسانی دل کے ________ خانے ہوتے ہیں۔', 'د انسان زړه ________ خونې لري.'), [('2', '2', '2'), ('4', '4', '4'), ('6', '6', '6'), ('8', '8', '8')]),
         (('The weight of the heart is ________ grams.', 'دل کا وزن ________ گرام ہوتا ہے۔', 'د زړه وزن ________ ګرامه وي.'), [('230 grams', '230 گرام', '230 ګرامه'), ('240 grams', '240 گرام', '240 ګرامه'), ('270 grams', '270 گرام', '270 ګرامه'), ('290 grams', '290 گرام', '290 ګرامه')]),
         (('On the left side of the heart there is ________ blood.', 'دل کے بائیں طرف ________ خون ہوتا ہے۔', 'د زړه په کیڼ اړخ کې ________ وینه وي.'), [('dirty', 'گندہ', 'ناپاکه'), ('clean', 'صاف', 'پاکه'), ('both', 'دونوں', 'دواړه')]),
         (('The great artery (Aorta) arises from the ________ of the heart.', 'شریانِ اعظم (Aorta) دل کے ________ سے نکلتا ہے۔', 'لوی شریان (Aorta) د زړه له ________ وځي.'), [('ventricle', 'بطن', 'بطین'), ('atrium', 'اُذن', 'اذین'), ('from the lungs', 'پھیپھڑوں سے', 'له سږو'), ('veins', 'وریدوں', 'وریدونو')]),
         (('The lower chambers of the heart are called ________ .', 'دل کے نچلے خانوں کو ________ کہتے ہیں۔', 'د زړه ښکتنیو خونو ته ________ ویل کېږي.'), [('atria', 'اُذن', 'اذینونه'), ('ventricles', 'بطن', 'بطینونه'), ('veins', 'وریدیں', 'وریدونه'), ('arteries', 'شریانیں', 'شریانونه')]),
         (('In blood ________ kinds of cells are found.', 'خون میں ________ قسم کے خلیے پائے جاتے ہیں۔', 'په وینه کې ________ ډوله حجرې موندل کېږي.'), [('2', '2', '2'), ('3', '3', '3'), ('4', '4', '4'), ('5', '5', '5')]),
         (('The membrane of the heart is called ________ .', 'دل کی جھلی کو ________ کہتے ہیں۔', 'د زړه غشا ته ________ ویل کېږي.'), [('capillary', 'کیپیلری', 'کپیلري'), ('pericardium', 'پیری کارڈیم', 'پیریکارډیم'), ('veins', 'وینز', 'وینز'), ('artery', 'شریان', 'شریان')]),
         (('The upper chambers of the heart are called ________ .', 'دل کے اوپر کے خانوں کو ________ کہتے ہیں۔', 'د زړه پورتنیو خونو ته ________ ویل کېږي.'), [('ventricle', 'بطن', 'بطین'), ('artery', 'شریان', 'شریان'), ('atrium', 'اُذن', 'اذین'), ('portal vein', 'پورٹل ورید', 'پورټل ورید')])]
    for i, (q, o) in enumerate(Q, 1):
        e.mcq(f'{i}', q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. Define the circulatory system and state its kinds in detail.', 'i۔ نظامِ دورانِ خون کی تعریف کریں اور اس کے اقسام تفصیل سے بیان کریں۔', 'i. د وینې د جریان سیستم تعریف کړئ او ډولونه یې په تفصیل بیان کړئ.'),
                      ('ii. Write the structure of the heart and its work in detail.', 'ii۔ دل کی بناوٹ اور اس کا کام تفصیل سے لکھیں۔', 'ii. د زړه جوړښت او کار یې په تفصیل ولیکئ.')])
    r = BOOK.record(e, 'hpe12-ch2-exercise', 'Chapter 2 exercise', 'باب ۲: مشقی سوالات', '۲ څپرکی: تمریني پوښتنې', 27, [22])
    BOOK.save(27, [(2, r)], complete_units=[2], issues=[{'id': 'hpe12-pdf027', 'unit': 2, 'printedPage': 22,
               'description': 'Owner ballpoint ticks on the MCQ options and a scribble at the top are excluded. Q1(3) has only three options in print; Q1(7) “دل کی جھلی”. Retained as printed.'}])


def p28():
    b = Builder()
    b.h('Chapter 3: Doping', 'باب نمبر ۳: ڈوپنگ (Doping)', '۳ څپرکی: ډوپینګ (Doping)')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('define illegal medicines that increase physical strength, and state the causes and results of the use of doping among players.', 'جسمانی طاقت کو بڑھانے والی غیر قانونی ادویات کی تعریف کر سکیں۔ کھلاڑیوں میں ڈوپنگ کے استعمال کے وجوہات اور نتائج بیان کر سکیں۔', 'د بدني ځواک زیاتوونکي غیر قانوني درمل تعریف کړي او په لوبغاړو کې د ډوپینګ د کارونې لاملونه او پایلې بیان کړي.'),
          ('gain awareness about the results and effects of drinking alcohol and using doping.', 'شراب نوشی اور ڈوپنگ کے استعمال کے نتائج اور اثرات کے بارے میں آگاہی پیدا ہو سکے۔', 'د شرابو څښلو او ډوپینګ د کارونې د پایلو او اغېزو په اړه پوهاوی پیدا شي.')])
    b.h('Doping', 'ڈوپنگ', 'ډوپینګ')
    P(b, [('The use of prohibited medicines which increase performance in sports is called doping. In the world of sports doping is considered an unethical and illegal act. These have extremely harmful effects and sometimes become the cause of complicated diseases. With the permission of a doctor there is permission to use some medicines to some extent. For doping the following medicines and intoxicants are used.',
           'کھیلوں میں کارکردگی بڑھانے والی ممنوعہ ادویات کے استعمال کو ڈوپنگ کہتے ہیں۔ ڈوپنگ کھیلوں کی دنیا میں ایک غیر اخلاقی اور غیر قانونی عمل سمجھا جاتا ہے۔ یہ انتہائی مضر اثرات رکھتی ہیں اور بعض اوقات پیچیدہ امراض کا سبب بنتی ہے۔ ڈاکٹر کی اجازت سے کچھ ادویات استعمال کرنے کی کسی حد تک اجازت ہے۔ ڈوپنگ کے لیے درج ذیل ادویات اور منشیات استعمال ہوتے ہیں۔',
           'په لوبو کې د کړنو زیاتوونکو منع شویو درملو کارولو ته ډوپینګ ویل کېږي. ډوپینګ د لوبو په نړۍ کې یو غیر اخلاقي او غیر قانوني عمل ګڼل کېږي. دا ډېرې زیانمنې اغېزې لري او کله کله د پېچلو ناروغیو لامل کېږي. د ډاکټر په اجازه د ځینو درملو کارولو ته تر یوه حده اجازه ده. د ډوپینګ لپاره لاندې درمل او نشه‌يي توکي کارول کېږي.')])
    r = rec(b, 3, 1, 28, first=True)
    deco(r, 'A photograph of capsules, tablets and a syringe is decorative.')
    BOOK.save(28, [(3, r)], issues=[{'id': 'hpe12-pdf028', 'unit': 3, 'printedPage': 23,
               'description': 'A small owner pen mark is excluded. “یہ انتہائی مضر اثرات رکھتی ہیں”, “ادویات اور منشیات استعمال ہوتے ہیں”. Retained as printed.'}])


def p29():
    b = Builder()
    b.group('lines', [('i. CNS stimulant (Central Nervous System Stimulant)', 'i۔ CNS سٹیمولینٹ (Central Nervous System Stimulant)', 'i. CNS محرک (Central Nervous System Stimulant)'),
                      ('ii. Narcotics (Narcotics)', 'ii۔ منشیات (Narcotics)', 'ii. نشه‌يي توکي (Narcotics)'),
                      ('iii. Steroids (Steroids)', 'iii۔ سٹیرائیڈز (Steroids)', 'iii. سټیرایډونه (Steroids)'),
                      ('iv. Beta blockers (Beta blockers)', 'iv۔ بیٹا بلاکرز (Beta blockers)', 'iv. بېټا بلاکرونه (Beta blockers)'),
                      ('v. Alcohol (Alcohol)', 'v۔ شراب (Alcohol)', 'v. شراب (Alcohol)'),
                      ('vi. Diuretics (Diuretics)', 'vi۔ ڈیوریٹکس (Diuretics)', 'vi. ډیوریټیکونه (Diuretics)'),
                      ('vii. Blood doping (Blood doping)', 'vii۔ خون لگانا (Blood doping)', 'vii. وینه لګول (Blood doping)')])
    b.h('CNS Stimulant', 'سی این ایس سٹیمولینٹ (CNS Stimulant)', 'سي این اېس محرک (CNS Stimulant)')
    P(b, [('These activate the central nervous system. They make one able to bear hardship. They reduce pain. They help to concentrate attention. However they become the cause of high blood pressure. They make the heartbeat irregular. They create a shortage of water in the body and increase the temperature.',
           'یہ مرکزی اعصابی نظام کو فعال کرتے ہیں۔ مشقت برداشت کرنے کے قابل بناتے ہیں۔ درد کو کم کرتے ہیں۔ توجہ مرکوز کرنے میں مدد دیتے ہیں۔ البتہ بلند فشارِ خون کا باعث بنتے ہیں۔ دل کی دھڑکن کو بے قاعدہ کر دیتے ہیں۔ جسم میں پانی کی کمی پیدا کرتے ہیں اور درجہ حرارت کو بڑھاتے ہیں۔',
           'دا مرکزي عصبي سیستم فعالوي. د سختۍ زغملو ته وړ کوي. درد کموي. په پام متمرکزولو کې مرسته کوي. خو د لوړ فشار لامل کېږي. د زړه درزا بې‌قاعدې کوي. په بدن کې د اوبو کمښت پیدا کوي او تودوخه لوړوي.')])
    b.h('Narcotics', 'منشیات (Narcotics)', 'نشه‌يي توکي (Narcotics)')
    P(b, [('Opium, heroin and morphine are included in this. These become the cause of severe physical and nervous weakness. It increases the ability to concentrate attention. It slows the speed of the heartbeat and breathing. It reduces appetite.',
           'افیون، ہیروئن اور مارفین اس میں شامل ہیں۔ یہ شدید جسمانی اور اعصابی کمزوری کا باعث بنتے ہیں۔ توجہ مرکوز کرنے کی صلاحیت کو بڑھاتی ہے۔ دل کی دھڑکن اور سانس کی رفتار کو سست کرتی ہے۔ بھوک کم کرتی ہے۔',
           'تریاک، هیروین او مارفین په دې کې شامل دي. دا د سخت بدني او عصبي کمزورۍ لامل کېږي. د پام متمرکزولو وړتیا زیاتوي. د زړه درزا او د ساه سرعت ورو کوي. اشتها کموي.')])
    b.h('Steroids', 'سٹیرائیڈز (Steroids)', 'سټیرایډونه (Steroids)')
    P(b, [('These are in the form of tablets and injections. These temporarily increase the elasticity of the muscles and also increase strength. Through their use help is obtained in weight lifting, body building, throwing and jumping …',
           'یہ گولیوں اور انجکشن کی صورت میں ہوتے ہیں۔ یہ عضلات کی لچک میں وقتی طور پر اضافہ کرتے ہیں اور طاقت بھی بڑھاتے ہیں۔ اس کے استعمال سے وزن اٹھانے، باڈی بلڈنگ، تھرونگ اور جمپنگ میں مدد ملتی …',
           'دا د ګولیو او پیچکاریو په بڼه وي. دا د عضلو نرمښت لنډمهاله زیاتوي او ځواک هم زیاتوي. په کارولو یې د وزن پورته کولو، باډي بلډینګ، اچونې او ټوپ وهلو کې مرسته ترلاسه کېږي …')])
    r = rec(b, 3, 2, 29)
    deco(r, 'A cartoon of four muscle-men flexing beside the steroids paragraph is decorative.')
    BOOK.save(29, [(3, r)], issues=[{'id': 'hpe12-pdf029', 'unit': 3, 'printedPage': 24,
               'description': 'Owner ballpoint notes (Urdu in the left margin, numerals and marks over “مشقت”, “Narcotics”, “سٹیرائیڈز”) are excluded. The narcotics paragraph says they “increase the ability to concentrate” (توجہ مرکوز کرنے کی صلاحیت کو بڑھاتی ہے). Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    {24: p24, 25: p25, 26: p26, 27: p27, 28: p28, 29: p29}[n]()
