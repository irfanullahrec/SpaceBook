"""HPE XII PDF90–95: pp.85–90 — javelin stages (grip kinds, running, withdrawal, throwing, body control); javelin exercise; discus throw (circle,
measurements, sector diagram, rules, fouls). Run: python class12_hpe_page090.py N (90–95)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T


def p90():
    b = Builder()
    b.h('Stages of javelin throwing', 'نیزہ پھینکنے کے مراحل', 'د نېزې غورځولو پړاوونه')
    L(b, [('Holding the javelin', 'نیزہ پکڑنا', 'نېزه نیول'), ('Running', 'دوڑنا', 'منډه'), ('Throwing', 'پھینکنا', 'غورځول'), ('Control over the body', 'جسم پر کنٹرول', 'پر بدن کنټرول'),
          ('The stage of taking the javelin back behind the body', 'نیزے کو جسم سے پیچھے لے جانے کا مرحلہ', 'د نېزې د بدن شا ته وړلو پړاو')])
    b.h('Holding the javelin', 'نیزہ پکڑنا', 'نېزه نیول')
    P(b, [('The javelin is held at the last end of its binding. In this way a better grip on the centre of gravity of the javelin is obtained. There are 3 methods of holding the javelin.', 'نیزے کو اس کی پٹی کے آخری سرے سے پکڑا جاتا ہے۔ اس طرح نیزے کے مرکزِ ثقل پر بہتر گرفت میسر آتی ہے۔ نیزہ پکڑنے کے 3 طریقے ہیں۔', 'نېزه د پټۍ له وروستي سره نیول کېږي. په دې ډول د نېزې د جاذبې پر مرکز ښه نیول ترلاسه کېږي. د نېزې د نیولو ۳ طریقې دي.')])
    b.h('i. Pen-holding style grip', 'i۔ پن پکڑنے کی طرز کی گرپ', 'i. د قلم نیولو په ډول نیول')
    P(b, [('In this kind of grip the javelin is held like holding a pen, i.e. the index finger and the thumb are equal, and support is given to the javelin by the middle finger.', 'اس قسم کی گرپ میں نیزے کو پن پکڑنے کی طرح پکڑا جاتا ہے۔ یعنی شہادت والی انگلی اور انگوٹھا برابر ہوتے ہیں اور انگوٹھی والی انگلی سے نیزے کو سپورٹ دی جاتی ہے۔', 'په دې ډول نیولو کې نېزه د قلم په څېر نیول کېږي، یعنې د شهادت ګوته او غټه ګوته برابرې وي او د ګوتمۍ په ګوته نېزې ته ملاتړ ورکول کېږي.')])
    b.h('ii. V-shaped grip', 'ii۔ وی (V) شکل کی گرفت', 'ii. د وي (V) بڼې نیول')
    P(b, [('In this method the javelin is held in the index finger and the middle finger, from which a V shape is formed, and support is given with the thumb.', 'اس طریقہ میں نیزے کو انگشتِ شہادت اور درمیانی والی انگلی میں پکڑا جاتا ہے۔ جس سے (V) کی شکل بن جاتی ہے۔ اور انگوٹھے سے سپورٹ دی جاتی ہے۔', 'په دې طریقه کې نېزه د شهادت او منځنۍ ګوتې ترمنځ نیول کېږي چې د (V) بڼه جوړېږي او په غټه ګوته ملاتړ ورکول کېږي.')])
    b.h('iii. Fist-shaped grip', 'iii۔ مٹھی کی شکل کی گرفت', 'iii. د موټي بڼې نیول')
    P(b, [('In this method the javelin is held in the fist. After gripping the javelin well, it is lifted to the height of the forehead above the shoulder and parallel to the ground. Its point is turned slightly inward, while the elbow …', 'اس طریقہ میں نیزے کو مٹھی میں پکڑا جاتا ہے۔ نیزے کو اچھی طرح گرپ کرنے کے بعد اسے پیشانی کی اونچائی تک کندھے سے اوپر اور زمین کے متوازی اٹھایا جاتا ہے۔ اس کی نوک تھوڑی سی اندر کی طرف مڑی ہو جبکہ کہنی …', 'په دې طریقه کې نېزه په موټي کې نیول کېږي. له ښه نیولو وروسته د تندي تر لوړوالي له اوږې پورته او ځمکې ته موازي پورته کېږي. څوکه یې لږ دننه ته اوړې وي، په داسې حال کې چې څنګل …')])
    r = rec(b, 7, 15, 90)
    BOOK.save(90, [(7, r)], issues=[{'id': 'hpe12-pdf090', 'unit': 7, 'printedPage': 85,
               'description': 'The pen-holding grip says support is given by “انگوٹھی والی انگلی” (the ring finger) while the list order names the middle finger in the English; the Urdu is retained as printed.'}])


def grips(lab, cap):
    b = ''
    for i, x in enumerate((80, 230, 380)):
        b += f'<line x1="{x - 60}" y1="90" x2="{x + 60}" y2="30" stroke="#64748b" stroke-width="4"/><ellipse cx="{x}" cy="60" rx="34" ry="20" fill="#475569" transform="rotate(-27 {x} 60)"/>' + T(x, 125, lab[i], 12, 'bold')
    b += '<line x1="20" y1="60" x2="440" y2="60" stroke="#1e293b" stroke-dasharray="4 3"/>'
    return svg(460, 150, b, cap)


def p91():
    b = Builder()
    P(b, [('… will be facing forward. When the javelin is lifted in this position, it can be taken behind the body easily in one line. The purpose of lifting the elbow is to ensure a smooth run and to create ease in the act of throwing.', 'سامنے کو اٹھی ہوگی۔ جب نیزے کو اس کی اس حالت میں اٹھایا جائے تو اسے جسم کے پیچھے ایک سیدھ میں آسانی کے ساتھ لے جایا جا سکتا ہے۔ کہنی اٹھانے کا مقصد ہموار دوڑ کو یقینی بنانا اور پھینکنے کے عمل میں آسانی پیدا کرنا ہے۔', '… مخ ته پورته وي. کله چې نېزه په دې حالت کې پورته شي، د بدن شا ته په یوه کرښه په اسانۍ وړل کېدای شي. د څنګل د پورته کولو موخه هوار منډه ډاډمنول او د غورځولو په عمل کې اسانتیا پیدا کول دي.')])
    sv = [grips(('fist-shaped grip', 'pen-holding grip', 'V-shaped grip'), 'Three ways of gripping the javelin'), grips(('مٹھی کی شکل کی گرپ', 'پن پکڑنے کی طرز کی گرپ', 'وی کی شکل کی گرپ'), 'نیزہ پکڑنے کے تین طریقے'),
          grips(('د موټي بڼه', 'د قلم بڼه', 'د وي بڼه'), 'د نېزې د نیولو درې طریقې')]
    b.visual('hpe12-fig-javelin-grips', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Running', 'دوڑ', 'منډه')
    P(b, [('Good players keep their running under control. Their speed in running is good. Instead of the initial stage, benefit can be taken during the last steps of the run. The run should be with a loose body. Running should enable the thrower to throw the javelin powerfully in the last part of the run. Generally a distance of three metres is necessary for a player to obtain full speed; however the length of the run cannot be fixed the same for all players.',
           'اچھے کھلاڑی اپنی دوڑ کو کنٹرول میں رکھتے ہیں۔ دوڑنے سے رفتار اچھی ہوتی ہے۔ ابتدائی مرحلے کے بجائے دوڑ کے آخری قدموں کے دوران فائدہ اٹھایا جا سکتا ہے۔ دوڑ ڈھیلے جسم کے ساتھ دوڑنی چاہیے۔ جو پھینکنے والے کو دوڑ کے آخری حصے میں زوردار طریقے پر نیزہ پھینکنے کے قابل بنا دے۔ ایک کھلاڑی کو عام طور پر رفتار حاصل کرنے کیلئے تین میٹر کا فاصلہ ضروری ہوتا ہے تاہم دوڑ کی لمبائی کی حد تمام کھلاڑیوں کے لیے یکساں مقرر نہیں کی جا سکتی۔',
           'ښه لوبغاړي خپله منډه تر کنټرول لاندې ساتي. په منډه سرعت ښه وي. د پیل پړاو پر ځای د منډې په وروستیو قدمونو کې ګټه اخیستل کېدای شي. منډه دې په سست بدن ووهل شي ترڅو غورځونکی د منډې په وروستۍ برخه کې په زور نېزه وغورځوي. لوبغاړي ته عموماً د سرعت ترلاسه کولو لپاره درې متره واټن اړین وي، خو د منډې اوږدوالی د ټولو لوبغاړو لپاره یو شان نه شي ټاکل کېدای.')])
    b.h('The stage of taking the javelin back behind the body:', 'نیزے کو جسم سے پیچھے لے جانے کا مرحلہ:', 'د نېزې د بدن شا ته وړلو پړاو:')
    P(b, [('This stage starts from the second step of the five-step rhythm. At the third step the throwing arm is taken back in line with the axis of the shoulder. Raising upward the palm of the hand holding the javelin, the arm is spread out from the front part; then from the axis of the hip the body of the player clearly leans backwards. This is very important for the full use of strength during throwing.',
           'یہ مرحلہ پانچ قدمی ردھم کے دوسرے قدم سے شروع ہوتا ہے۔ تیسرے قدم پر پھینکنے والے بازو کو کندھے کے محور کی سیدھ میں پیچھے لے جایا جاتا ہے۔ نیزہ پکڑے ہوئے ہاتھ کی ہتھیلی کو اوپر کی جانب اٹھاتے ہوئے بازو اگلے حصے سے پھیلا دیا جاتا ہے تب کولہے کے محور سے کھلاڑی کا جسم واضح طور پر پیچھے کی جانب جھکتا ہے۔ جو پھینکنے کے دوران طاقت کے بھرپور استعمال کیلئے بڑا اہم ہوتا ہے۔',
           'دا پړاو د پنځه قدمي ریتم له دویم قدم پیلېږي. په درېیم قدم کې د غورځولو مټ د اوږې د محور په سیده شا ته وړل کېږي. د نېزې نیوونکي لاس ورغوی پورته کېږي او مټ له مخکینۍ برخې غځول کېږي؛ بیا د کوناټي له محوره د لوبغاړي بدن په ښکاره شا ته کږېږي چې د غورځولو پر مهال د ځواک بشپړې کارونې لپاره ډېر مهم دی.')])
    b.h('Throwing', 'پھینکنا', 'غورځول')
    P(b, [('The start of throwing the javelin is from spreading the right hip forward and upward from the joints of the knee and ankle of the right leg. The heel of the bent left leg touches the ground. The work of the left leg is first to give support and afterwards to lift the body upward. The axes of the shoulder and hip now become parallel. The bending of the waist increases. During this …',
           'نیزہ پھینکنے کی ابتداء دائیں کولہے کو دائیں ٹانگ کے گھٹنے اور ٹخنے کے جوڑوں سے آگے اور اوپر پھیلانے سے ہوتی ہے۔ بائیں مڑی ہوئی ٹانگ کی ایڑھی زمین پر لگتی ہے۔ بائیں ٹانگ کا کام شروع میں سہارا دینے اور بعد میں جسم کو اوپر اٹھانے کا ہوتا ہے۔ کندھے اور کولہے کے محور اب متوازی ہو جاتے ہیں۔ کمر کا جھکاؤ زیادہ سے زیادہ ہو جاتا ہے۔ اس …',
           'د نېزې غورځول د ښي کوناټي د ښې پښې د زنګون او بجلکې له بندونو مخکې او پورته غځولو پیلېږي. د کیڼې کږې پښې پونده پر ځمکه لګي. د کیڼې پښې کار په پیل کې ملاتړ او وروسته د بدن پورته کول دي. د اوږې او کوناټي محورونه اوس موازي کېږي. د ملا کږوالی تر ټولو ډېر کېږي. په دې …')])
    r = rec(b, 7, 16, 91)
    BOOK.save(91, [(7, r)], issues=[{'id': 'hpe12-pdf091', 'unit': 7, 'printedPage': 86,
               'description': 'The grip drawing (three hands on a javelin, labelled in Urdu) is reproduced as a coded schematic. The first line is faint at the top of the scan (“سامنے کو اٹھی ہوگی”). “ایک کھلاڑی کو … تین میٹر کا فاصلہ ضروری ہوتا ہے” (as printed). Retained as printed.'}])


def p92():
    b = Builder()
    P(b, [('… the centre of tension is in the region of the shoulders. During this the right leg is advanced forward. The heel is lifted up. The throwing arm is now in its preparation. The angle of throwing is between 32 and 34 degrees. One should try to keep the angle of the flight of the javelin correct.',
           'کے تناؤ کا مرکز کندھوں کے حصے میں ہوتا ہے۔ اس دوران دائیں ٹانگ آگے بڑھائی جاتی ہے۔ ایڑھی کو اوپر اٹھایا جاتا ہے۔ پھینکنے والا بازو اب اپنی تیاری میں ہوتا ہے۔ پھینکنے کا زاویہ 32 تا 34 ڈگری کے درمیان ہوتا ہے۔ نیزے کی اڑان کا زاویہ درست قائم رکھنے کی کوشش کرنی چاہیے۔',
           '… د کشش مرکز د اوږو په برخه کې وي. په دې وخت کې ښې پښه مخکې کېږي. پونده پورته کېږي. د غورځولو مټ اوس په چمتووالي کې وي. د غورځولو زاویه د ۳۲ او ۳۴ درجو ترمنځ وي. باید هڅه وشي چې د نېزې د الوتنې زاویه سمه وساتل شي.')])
    b.h('Control over the body', 'جسم پر کنٹرول', 'پر بدن کنټرول')
    P(b, [('After throwing the javelin the body leans forward. During this, control over the body is extremely necessary. If the body goes beyond the arc or touches it, it will be a foul. To avoid a foul, controlling the body as soon as the javelin is thrown is necessary.',
           'نیزہ پھینکنے کے بعد جسم آگے کی جانب جھک جاتا ہے۔ اس دوران جسم پر کنٹرول انتہائی ضروری ہے۔ اگر جسم قوس سے آگے چلا گیا یا چھو گیا تو فاؤل ہوگا۔ فاؤل سے بچنے کیلئے نیزہ پھینکتے ہی جسم کو کنٹرول کرنا لازمی ہے۔',
           'د نېزې له غورځولو وروسته بدن مخکې کږېږي. په دې وخت کې پر بدن کنټرول ډېر اړین دی. که بدن له کمانه مخکې لاړ شي یا یې ولمسوي، خطا ده. له خطا د ژغورنې لپاره د نېزې له غورځولو سره سم د بدن کنټرول اړین دی.')])
    r = rec(b, 7, 17, 92)
    deco(r, 'A drawing of three javelin throwers in successive throwing positions is decorative.')
    BOOK.save(92, [(7, r)])


def p93():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The angle of the sector of javelin throwing is ________ degrees.', 'نیزہ پھینکنے کے سیکٹر کا زاویہ ________ درجے کا ہوتا ہے۔', 'د نېزې غورځولو د سکټور زاویه ________ درجې وي.'), [('25°', '25°', '25°'), ('27°', '27°', '27°'), ('29°', '29°', '29°'), ('30°', '30°', '30°')]),
         (('The thickness of the arc is ________ centimetres.', 'قوس کی موٹائی ________ سینٹی میٹر ہوتی ہے۔', 'د کمان پنډوالی ________ سانتي متره وي.'), [('3', '3', '3'), ('5', '5', '5'), ('7', '7', '7'), ('9', '9', '9')]),
         (('The breadth of the running path is ________ metres.', 'دوڑنے والے راستے کی چوڑائی ________ میٹر ہوتی ہے۔', 'د منډې لارې پلنوالی ________ متره وي.'), [('2', '2', '2'), ('4', '4', '4'), ('6', '6', '6'), ('8', '8', '8')]),
         (('The length of the running path is ________ metres.', 'دوڑنے والے راستے کی لمبائی ________ میٹر ہوتی ہے۔', 'د منډې لارې اوږدوالی ________ متره وي.'), [('26', '26', '26'), ('28', '28', '28'), ('30', '30', '30'), ('32', '32', '32')]),
         (('In the modern Olympics javelin competitions were included in ________ .', 'جدید اولمپکس میں نیزہ کے مقابلے ________ میں شامل کیے گئے۔', 'په عصري اولمپیک کې د نېزې سیالۍ په ________ کې شاملې شوې.'), [('1904', '1904', '1904'), ('1906', '1906', '1906'), ('1908', '1908', '1908'), ('1910', '1910', '1910')]),
         (('Besides the arc, the thickness of the lines of the sector is ________ centimetres.', 'قوس کے علاوہ سیکٹر کی لائنوں کی موٹائی ________ سینٹی میٹر ہوتی ہے۔', 'له کمان پرته د سکټور د کرښو پنډوالی ________ سانتي متره وي.'), [('3', '3', '3'), ('5', '5', '5'), ('7', '7', '7'), ('9', '9', '9')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['i.', 'ii.', 'iii.', 'iv.', 'v.', 'vi.'][i], q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('(i) Make the sector of javelin throwing and record the fouls.', '(i) نیزہ پھینکنے کا سیکٹر بنائیں اور فاؤلز درج کریں۔', '(i) د نېزې غورځولو سکټور جوړ کړئ او خطاګانې ولیکئ.'),
                      ('(ii) Record the rules of javelin throwing.', '(ii) نیزہ پھینکنے کے قوانین درج کریں۔', '(ii) د نېزې غورځولو قوانین ولیکئ.')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-javelin', 'Chapter 7 exercise: javelin throw', 'باب ۷: مشقی سوالات — نیزہ پھینکنا', '۷ څپرکی: تمریني پوښتنې — نېزه غورځول', 93, [88])
    BOOK.save(93, [(7, r)], issues=[{'id': 'hpe12-pdf093', 'unit': 7, 'printedPage': 88,
               'description': 'Owner ballpoint ticks and an English scribble beside the heading are excluded. Retained as printed.'}])


def discus(lab, cap):
    b = ('<ellipse cx="220" cy="300" rx="95" ry="100" fill="none" stroke="#1e293b" stroke-width="3"/><path d="M168 216 A95 100 0 0 1 272 216" stroke="#1e293b" stroke-width="7" fill="none"/>'
         '<line x1="175" y1="210" x2="110" y2="40" stroke="#1e293b" stroke-width="6"/><line x1="265" y1="210" x2="330" y2="40" stroke="#1e293b" stroke-width="6"/>'
         '<line x1="220" y1="20" x2="220" y2="410" stroke="#64748b" stroke-dasharray="3 4"/><line x1="40" y1="300" x2="400" y2="300" stroke="#64748b" stroke-dasharray="3 4"/>'
         '<rect x="40" y="295" width="85" height="10" fill="#e5e7eb" stroke="#1e293b"/><rect x="315" y="295" width="85" height="10" fill="#e5e7eb" stroke="#1e293b"/>'
         '<line x1="150" y1="150" x2="290" y2="150" stroke="#1e293b" marker-end="url(#a)"/>')
    b += T(220, 140, lab[0], 13, 'bold') + T(240, 285, '90°', 12, 'bold', 'start') + T(220, 330, lab[1], 12, 'bold') + T(430, 300, lab[1], 12, 'bold', 'start')
    b += T(80, 280, lab[2], 12, 'bold') + T(80, 330, lab[3], 12, 'bold')
    return svg(470, 430, b, cap)


def p94():
    b = Builder()
    b.h('Discus Throw', 'ڈسکس تھرو (Discuss Throw)', 'ډیسکس غورځول (Discuss Throw)')
    b.h('Circle', 'دائرہ', 'دایره')
    b.group('lines', [('The inner diameter of the circle of the discus throw 2.50 metres.', 'ڈسکس تھرو کے دائرہ کا اندرونی قطر 2.50 میٹر', 'د ډیسکس د دایرې داخلي قطر ۲.۵۰ متره.'),
                      ('The line of the circle 5 centimetres wide and 75 centimetres long.', 'دائرہ کی لائن 5 سینٹی میٹر چوڑی اور 75 سینٹی میٹر لمبی', 'د دایرې کرښه ۵ سانتي متره پلنه او ۷۵ سانتي متره اوږده.'),
                      ('The angle will be 34.92° which will make the sector.', 'زاویہ 34.92° ہوگا جو سیکٹر بنائے گا۔', 'زاویه به ۳۴.۹۲° وي چې سکټور جوړوي.')])
    H = (['Item', 'For men', 'For women'], ['شے', 'مردوں کیلئے', 'عورتوں کیلئے'], ['شی', 'نارینه', 'ښځې'])
    rows = [('Weight of the discus', 'ڈسکس کا وزن', 'د ډیسکس وزن', ('2 kilograms', '2 کلو گرام', '۲ کیلوګرامه'), ('1 kilogram', '1 کلو گرام', '۱ کیلوګرام')),
            ('Diameter', 'قطر', 'قطر', ('219 to 221 millimetres', '219 تا 221 ملی میٹر', '۲۱۹ تر ۲۲۱ ملي متره'), ('180 to 182 millimetres', '180 تا 182 ملی میٹر', '۱۸۰ تر ۱۸۲ ملي متره'))]
    b.table('hpe12-discus-measure', H[0], [[a, m[0], w[0]] for a, u, p, m, w in rows], H[1], H[2], [[u, m[1], w[1]] for a, u, p, m, w in rows], [[p, m[2], w[2]] for a, u, p, m, w in rows])
    b.p('Weight for young children 1.5 kilograms.', 'نوعمر بچوں کیلئے وزن 1.5 کلو گرام', 'د ځوانو ماشومانو لپاره وزن ۱.۵ کیلوګرامه.')
    sv = [discus(('34.92°', '2.50m', '75cm', '5cm'), 'Discus throwing circle and sector'), discus(('34.92°', '2.50m', '75cm', '5cm'), 'ڈسکس تھرو کا دائرہ اور سیکٹر'), discus(('34.92°', '2.50m', '75cm', '5cm'), 'د ډیسکس دایره او سکټور')]
    b.visual('hpe12-fig-discus-circle', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 7, 18, 94)
    r['sourceNote'] = 'The printed weight and diameter lists for men and women are given as a structured table; the circle diagram is reproduced as a coded schematic with its printed measurements.'
    BOOK.save(94, [(7, r)], issues=[{'id': 'hpe12-pdf094', 'unit': 7, 'printedPage': 89,
               'description': 'The English heading prints “Discuss Throw”. “زاویہ 34.92° ہوگا”. Retained as printed.'}])


def p95():
    b = Builder()
    b.h('Rules of the discus', 'ڈسکس کے قوانین', 'د ډیسکس قوانین')
    L(b, [('The order of turns will be given by drawing lots.', 'باری کی ترتیب قرعہ اندازی سے دی جائے گی۔', 'د وارونو ترتیب به په پچه ورکول کېږي.'),
          ('If there are fewer than 8 players, then 6–6 turns will be given.', '8 سے کم کھلاڑی ہوں تو 6-6 باریاں دی جائیں گی۔', 'که له ۸ کم لوبغاړي وي، ۶–۶ وارونه به ورکول کېږي.'),
          ('If there are more than 8 players, first 3–3 turns will be given, and selecting the 8 best players, then 3–3 turns will be given.', '8 سے زیادہ کھلاڑی ہوں تو پہلے 3-3 باریاں دی جائیں گی اور 8 بہترین کھلاڑی منتخب کر کے پھر 3-3 باریاں دی جائیں گی۔', 'که له ۸ زیات لوبغاړي وي، لومړی ۳–۳ وارونه ورکول کېږي او ۸ غوره لوبغاړي ټاکل کېږي او بیا ۳–۳ وارونه ورکول کېږي.'),
          ('Every player will be given a chest number.', 'ہر کھلاڑی کو چسٹ نمبر دیا جائے گا۔', 'هر لوبغاړي ته به د سینې شمېره ورکول کېږي.'),
          ('Every player will be given the benefit of his best attempt.', 'ہر کھلاڑی کو اس کی بہترین کوشش کا فائدہ دیا جائے گا۔', 'هر لوبغاړي ته به د هغه د غوره هڅې ګټه ورکول کېږي.'),
          ('The player will remain in the circle until the discus falls in the sector.', 'کھلاڑی اس وقت تک دائرہ میں رہے گا جب تک ڈسکس سیکٹر میں نہ گرے۔', 'لوبغاړی به تر هغه په دایره کې پاتې وي چې ډیسکس په سکټور کې ونه لوېږي.'),
          ('Only the discus provided by the administration will be used.', 'انتظامیہ کی مہیا کردہ ڈسکس ہی استعمال ہوگی۔', 'یوازې د ادارې برابره کړې ډیسکس به کارول کېږي.'),
          ('The act of throwing will begin after taking a stationary state inside the circle.', 'پھینکنے کا عمل دائرہ کے اندر سے ساکن حالت اختیار کرنے کے بعد شروع ہوگا۔', 'د غورځولو عمل به د دایرې دننه له ولاړ حالت غوره کولو وروسته پیلېږي.'),
          ('Every player will throw the discus on his own turn.', 'ہر کھلاڑی اپنی باری پر ڈسکس تھرو کرے گا۔', 'هر لوبغاړی به په خپل وار ډیسکس غورځوي.'),
          ('Gloves (Gloves) cannot be used, but a suitable substance can be rubbed on the hands for a better grip.', 'گلاوز (Gloves) استعمال نہیں کر سکتا البتہ بہتر گرفت کیلئے ہاتھوں پر موزوں چیز مل سکتا ہے۔', 'دستکشې (Gloves) نه شي کارولی، خو د ښه نیولو لپاره پر لاسونو مناسب شی موښلی شي.'),
          ('The turn must be taken within one minute of the name being called.', 'نام پکارنے کے ایک منٹ کے اندر باری لینا ہوگی۔', 'د نوم له بللو په یوه دقیقه کې به وار اخیستل کېږي.'),
          ('If the discus falls inside the sector without a foul, the attempt will be counted correct.', 'اگر بغیر فاؤل کیے سیکٹر کے اندر ڈسکس گرے تو کوشش درست شمار ہوگی۔', 'که ډیسکس له خطا پرته د سکټور دننه ولوېږي، هڅه سمه ګڼل کېږي.'),
          ('The measurement of every attempt will be recorded.', 'ہر کوشش کی پیمائش درج کی جائے گی۔', 'د هرې هڅې اندازه به ثبتېږي.'),
          ('If some player is taking part in a field and a track event at the same time, he will tell the official and complete the track event first.', 'اگر کوئی کھلاڑی بیک وقت فیلڈ اور ٹریک میں شامل ہو تو آفیشل کو بتا کر وہ پہلے ٹریک ایونٹ مکمل کرے گا۔', 'که کوم لوبغاړی په یو وخت په میداني او ټریک سیالۍ کې ګډون کوي، چارواکي ته به ووايي او لومړی به د ټریک سیالي بشپړوي.')])
    b.h('Fouls', 'فاؤلز', 'خطاګانې')
    L(b, [('The discus falling outside the sector.', 'ڈسکس کا سیکٹر سے باہر گرنا۔', 'له سکټور بهر د ډیسکس لوېدل.'), ('Throwing without one’s turn and without the chest number.', 'اپنی باری کے بغیر اور چسٹ نمبر کے بغیر پھینکنا۔', 'له خپل وار او د سینې له شمېرې پرته غورځول.'),
          ('Touching the ground in front of the circle with the hand or foot.', 'دائرہ کے سامنے سے زمین کو ہاتھ یا پاؤں سے چھونا۔', 'د دایرې مخې ته ځمکه په لاس یا پښه لمسول.')])
    r = rec(b, 7, 19, 95)
    BOOK.save(95, [(7, r)], issues=[{'id': 'hpe12-pdf095', 'unit': 7, 'printedPage': 90,
               'description': 'The heading “ڈسکس کے قوانین” is partly cut at the top of the scan. “گلاوز … استعمال نہیں کر سکتا”, “موزوں چیز مل سکتا ہے”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 90
    {90: p90, 91: p91, 92: p92, 93: p93, 94: p94, 95: p95}[n]()
