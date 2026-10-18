"""HPE XII PDF30–35: pp.25–30 — beta blockers, diuretics, alcohol, blood doping; effects of doping and alcohol on players; prevention and awareness;
chapter 3 exercise; chapter 4 (Emergency Situation) opener, causes of fire in school and home (cooking, fire appliances, smoking, electrical appliances,
gas leakage, children playing with fire, inflammable things, decoration items). Run: python class12_hpe_page030.py N (30–35)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p30():
    b = Builder()
    P(b, [('… are. Because of them tumours form in the body and they become the cause of high blood pressure. They make the liver and kidneys useless.',
           'ہیں۔ اس کی وجہ سے جسم میں رسولیاں بنتی ہیں اور بلند فشارِ خون کا باعث بنتے ہیں۔ جگر اور گردوں کو ناکارہ بناتے ہیں۔',
           '… . د دوی له امله په بدن کې غوټې جوړېږي او د لوړ فشار لامل کېږي. ځیګر او پښتورګي ناکاره کوي.')])
    b.h('6. Beta blockers', '6۔ بیٹا بلاکرز (Beta blockers)', '6. بېټا بلاکرونه (Beta blockers)')
    P(b, [('These are generally used by patients of high blood pressure. In sports in which concentration is needed, e.g. shooting and archery etc., players use these. These reduce blood pressure and the heartbeat. These affect the reproductive system.',
           'یہ عموماً بلند فشارِ خون کے مریض استعمال کرتے ہیں۔ جن کھیلوں میں توجہ کی ضرورت ہوتی ہے مثلاً نشانہ بازی اور تیر اندازی وغیرہ کے کھلاڑی یہ استعمال کرتے ہیں۔ یہ بلڈ پریشر اور دل کی دھڑکن کو کم کرتا ہے۔ یہ نظامِ تولید کو متاثر کرتے ہیں۔',
           'دا عموماً د لوړ فشار ناروغان کاروي. په هغو لوبو کې چې پام ته اړتیا وي، لکه نښه ویشتل او غشي ویشتل او نور، لوبغاړي یې کاروي. دا د وینې فشار او د زړه درزا کموي. دا پر تناسلي سیستم اغېز کوي.')])
    b.h('7. Diuretics', '7۔ ڈیوریٹکس (Diuretics)', '7. ډیوریټیکونه (Diuretics)')
    P(b, [('These are used in sports with weight categories. It is a urine-producing medicine. For boxing, karate and weight-lifting competitions they temporarily increase physical strength. These become the cause of decrease in the circulation of blood, muscular cramps, shortage of water in the body and diseases of the kidneys.',
           'یہ وزن کی درجہ بندی کے کھیلوں میں استعمال ہوتے ہیں۔ پیشاب آور دوا ہے۔ باکسنگ، کراٹے اور وزن اٹھانے کے مقابلوں کے لیے جسمانی طاقت میں وقتی طور پر اضافہ کرتے ہیں۔ یہ خون کی گردش میں کمی، عضلاتی کھچاؤ، جسم میں پانی کی کمی اور گردوں کے امراض کا باعث بنتے ہیں۔',
           'دا د وزن د درجه‌بندۍ په لوبو کې کارول کېږي. د متیازو راوستونکی درمل دی. د باکسینګ، کراټې او وزن پورته کولو د سیالیو لپاره بدني ځواک لنډمهاله زیاتوي. دا د وینې د ګرځښت د کمښت، عضلي کشش، په بدن کې د اوبو د کمښت او د پښتورګو د ناروغیو لامل کېږي.')])
    b.h('8. Alcohol', '8۔ شراب (Alcohol)', '8. شراب (Alcohol)')
    P(b, [('Its use too is prohibited in sports. It reduces white corpuscles. It makes the liver useless. It becomes the cause of decrease in balance and attention, because of which the intensity of injury and hard work is not felt.',
           'اس کا استعمال بھی کھیلوں میں ممنوع ہے۔ یہ سفید جسیموں کو کم کرتی ہے۔ جگر کو ناکارہ کرتی ہے توازن اور توجہ میں کمی کا باعث بنتی ہے۔ جس کی وجہ سے شدتِ چوٹ اور سخت کام کرنے کا پتہ نہیں چلتا۔',
           'کارول یې په لوبو کې هم منع دي. سپینې حجرې کموي. ځیګر ناکاره کوي؛ د توازن او پام د کمښت لامل کېږي چې له امله یې د ټپ شدت او د سخت کار احساس نه کېږي.')])
    b.h('9. Blood doping', '9۔ خون لگانا (Blood doping)', '9. وینه لګول (Blood doping)')
    P(b, [('Before training, players get blood taken out and preserved and get it put back before competitions, or transfer blood from some other person of their own blood group so that the number of red corpuscles increases. This is useful for long-distance runners. However it can become the cause of communicable diseases, e.g. hepatitis (B-C) and AIDS. It can also become the cause of allergy and heart attack.',
           'ٹریننگ سے قبل کھلاڑی خون نکال کر محفوظ کروالیتے ہیں اور مقابلوں سے قبل دوبارہ لگوالیتے ہیں یا اپنے خون کے گروپ کے کسی دوسرے فرد سے خون منتقل کرتے ہیں تاکہ سرخ جسیموں کی تعداد بڑھ جائے۔ یہ لمبی دوڑ والے کھلاڑی کے لیے مفید ہوتا ہے۔ تاہم متعدی امراض مثلاً ہیپاٹائٹس (B-C) اور AIDS جیسے امراض کا باعث بنتی ہے۔ الرجی اور دل کے دورے کا سبب بھی بن سکتی ہے۔',
           'لوبغاړي له روزنې مخکې وینه وباسي او خوندي یې کړي او له سیالیو مخکې یې بېرته ولګوي، یا د خپل د وینې ګروپ له بل کس وینه انتقالوي ترڅو د سرو حجرو شمېر زیات شي. دا د اوږدې منډې لوبغاړي ته ګټور وي. خو د ساري ناروغیو، لکه هېپاټایټس (B-C) او AIDS، لامل کېږي. د حساسیت او زړه د حملې لامل هم کېدای شي.')])
    r = rec(b, 3, 3, 30)
    BOOK.save(30, [(3, r)], issues=[{'id': 'hpe12-pdf030', 'unit': 3, 'printedPage': 25,
               'description': 'The numbering on this page runs 6, 7, 8 and then “7” again for blood doping (handwritten-looking print digits); the list on p.24 has blood doping as vii. Rendered 6–9 in sequence; noted. “یہ بلڈ پریشر … کو کم کرتا ہے”. Retained as printed otherwise.'}])


def p31():
    b = Builder()
    b.h('Effects of doping and alcohol on players', 'ڈوپنگ اور الکوحل کے کھلاڑیوں پر اثرات', 'پر لوبغاړو د ډوپینګ او الکول اغېزې')
    L(b, [('Temporarily fatigue is not felt; rather performance increases immediately.', 'وقتی تھکاوٹ محسوس نہیں ہوتی بلکہ فوراً کارکردگی بڑھاتی ہے۔', 'لنډمهاله ستړیا نه احساسېږي، بلکې سمدستي کړنې زیاتوي.'),
          ('They affect the physical system of players.', 'کھلاڑیوں کے جسمانی نظام کو متاثر کرتی ہیں۔', 'د لوبغاړو پر بدني سیستم اغېز کوي.'),
          ('They create mental anxiety, because of which attention is not concentrated.', 'ذہنی طور پر پریشانی پیدا کرتے ہیں جس کی وجہ سے توجہ مرکوز نہیں ہوتی۔', 'رواني اندېښنه پیدا کوي چې له امله یې پام نه متمرکزېږي.'),
          ('They create breathing troubles, because of which the player gets tired in a few minutes and starts to get out of breath.', 'سانس کی تکالیف پیدا کرتے ہیں جس کی وجہ سے کھلاڑی چند ہی منٹوں میں تھک جاتا ہے اور سانس پھولنے لگتی ہے۔', 'د ساه ستونزې پیدا کوي چې له امله یې لوبغاړی په څو دقیقو کې ستړی کېږي او ساه یې لنډېږي.'),
          ('They create a shortage in the blood, which affects the health of players.', 'خون میں کمی پیدا کرتے ہیں جو کھلاڑیوں کی صحت کو متاثر کرتا ہے۔', 'په وینه کې کمښت پیدا کوي چې د لوبغاړو روغتیا اغېزمنوي.'),
          ('The attitude of players becomes negative, which affects performance.', 'کھلاڑیوں کا رویہ منفی ہو جاتا ہے جو کارکردگی پر اثر انداز ہوتی ہے۔', 'د لوبغاړو چلند منفي کېږي چې پر کړنو اغېز کوي.')])
    b.h('Method of prevention and awareness campaign', 'بچاؤ کا طریقہ کار اور آگاہی مہم', 'د مخنیوي طریقه او د پوهاوي کمپاین')
    L(b, [('Players should be made aware of its negative effects.', 'کھلاڑیوں کو اس کے منفی اثرات سے آگاہی دلائی جائے۔', 'لوبغاړي دې د دې له منفي اغېزو خبر کړای شي.'),
          ('Players should be made acquainted with its effects on health and performance.', 'کھلاڑی کو اس کے صحت و پرفارمنس پر اثرات سے واقفیت دلائی جائے۔', 'لوبغاړي دې پر روغتیا او کړنو د دې له اغېزو خبر شي.'),
          ('In free time players should be given alternative activities.', 'فارغ اوقات میں کھلاڑیوں کو متبادل مشاغل دیے جائیں۔', 'په وزګار وخت کې لوبغاړو ته بدیل مشغولتیاوې ورکړل شي.'),
          ('Players should be made to practise increasing performance and achieving targets.', 'کھلاڑیوں کو کارکردگی بڑھانے اور ٹارگٹ حاصل کرنے کی مشق کروائی جائے۔', 'لوبغاړو ته دې د کړنو د زیاتولو او موخو د ترلاسه کولو تمرین ورکړل شي.'),
          ('Seminars should be arranged on alcohol and doping.', 'الکوحل اور ڈوپنگ پر سیمینار کرائے جائیں۔', 'پر الکول او ډوپینګ دې سیمینارونه جوړ شي.'),
          ('A walk should be organised to avoid the harmful effects of alcohol and doping.', 'الکوحل اور ڈوپنگ کے مضر اثرات سے بچنے کے لیے واک منعقد کروائی جائے۔', 'د الکول او ډوپینګ له زیانمنو اغېزو د ژغورنې لپاره دې مارچ جوړ شي.'),
          ('Some event should be organised against the negative effects of alcohol.', 'الکوحل کے منفی اثرات کے خلاف کوئی ایونٹ کروایا جائے۔', 'د الکول د منفي اغېزو پر وړاندې دې کومه پېښه (پروګرام) جوړه شي.'),
          ('A publicity campaign should be run on the harmful effects of alcohol.', 'الکوحل کے مضر اثرات کی تشہیری مہم چلائی جائے۔', 'د الکول د زیانمنو اغېزو تبلیغي کمپاین دې وچلول شي.'),
          ('Through print and electronic media the harmful effects of alcohol should be highlighted.', 'پرنٹ اور الیکٹرانک میڈیا کے ذریعہ الکوحل کے مضر اثرات کو اجاگر کیا جائے۔', 'د چاپي او برېښنايي رسنیو له لارې دې د الکول زیانمنې اغېزې راڅرګندې شي.')])
    r = rec(b, 3, 4, 31)
    BOOK.save(31, [(3, r)], issues=[{'id': 'hpe12-pdf031', 'unit': 3, 'printedPage': 26,
               'description': 'Owner ballpoint notes in the left margin (Urdu and “club”, “of my motion”) are excluded. “وقتی تھکاوٹ … بلکہ فوراً کارکردگی بڑھاتی ہے”, “کھلاڑیوں کا رویہ منفی ہو جاتا ہے جو کارکردگی پر اثر انداز ہوتی ہے”. Retained as printed.'}])


def p32():
    b = Builder()
    L(b, [('A dope test should be made compulsory before competition, and on proof the concerned players should be expelled from the game.', 'مقابلے سے قبل ڈوپ ٹیسٹ لازمی قرار دیا جائے اور ثابت ہونے پر متعلقہ کھلاڑیوں کو کھیل سے نکال دیا جائے۔', 'له سیالۍ مخکې دې ډوپ ټېسټ اړین وګرځول شي او په ثابتېدو دې اړوند لوبغاړي له لوبې وایستل شي.')])
    r = rec(b, 3, 5, 32)
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Give answers to the following questions.', '۱۔ درج ذیل سوالات کے جواب دیں۔', '۱. د لاندې پوښتنو ځوابونه ورکړئ.')
    e.group('lines', [('i. Define alcohol and record its negative effects on players.', 'i۔ الکوحل کی تعریف کریں اور کھلاڑیوں پر اس کے منفی اثرات درج کریں۔', 'i. الکول تعریف کړئ او پر لوبغاړو یې منفي اغېزې ولیکئ.'),
                      ('ii. What is doping? What effects does it have on players?', 'ii۔ ڈوپنگ کیا ہے؟ اس کے کھلاڑیوں پر کیا اثرات ہوتے ہیں۔', 'ii. ډوپینګ څه دی؟ پر لوبغاړو یې څه اغېزې وي؟'),
                      ('iii. What should be done for protection from alcohol and doping?', 'iii۔ الکوحل اور ڈوپنگ سے بچاؤ کے لیے کیا کیا جائے؟', 'iii. له الکول او ډوپینګ د ژغورنې لپاره څه وشي؟')])
    ex = BOOK.record(e, 'hpe12-ch3-exercise', 'Chapter 3 exercise', 'باب ۳: مشقی سوالات', '۳ څپرکی: تمریني پوښتنې', 32, [27])
    BOOK.save(32, [(3, r), (3, ex)], complete_units=[3], issues=[{'id': 'hpe12-pdf032', 'unit': 3, 'printedPage': 27,
               'description': 'The top of p.27 has a dark smudge from the scan over the word “کھیل” (legible). The rest of the page below the questions is blank in print.'}])


def p33():
    b = Builder()
    b.h('Chapter 4: Emergency Situation', 'باب نمبر ۴: ہنگامی صورتِ حال', '۴ څپرکی: بیړنی حالت')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('state the causes of fire breaking out in a school or home.', 'سکول یا گھر میں آگ لگنے کی وجوہات بیان کر سکیں۔', 'په ښوونځي یا کور کې د اور لګېدو لاملونه بیان کړي.'),
          ('demonstrate safe behaviour during and after a fire.', 'آگ لگنے کے دوران اور بعد میں محفوظ طرزِ عمل کا مظاہرہ کر سکیں۔', 'د اور لګېدو پر مهال او وروسته خوندي چلند وښيي.'),
          ('prepare protective guidelines for the prevention of fire in the home and school.', 'گھر اور سکول میں آگ کی روک تھام کے لیے حفاظتی گائیڈ لائن تیار کر سکیں۔', 'په کور او ښوونځي کې د اور د مخنیوي لپاره ساتنیز لارښود چمتو کړي.'),
          ('demonstrate first aid during an emergency situation.', 'کسی ہنگامی صورتِ حال کے دوران ابتدائی طبی امداد کا مظاہرہ کر سکیں۔', 'د بیړني حالت پر مهال لومړنۍ طبي مرسته وښيي.')])
    b.h('Causes of sudden fire in school and home', 'سکول اور گھر میں اچانک آگ لگنے کی وجوہات', 'په ښوونځي او کور کې د ناڅاپي اور لګېدو لاملونه')
    P(b, [('Accidents of fire in schools and homes are a serious danger. Every year about 3400 people are injured or die because of fire. By adopting precautionary measures protection from them is possible. Because of the following causes there is a danger of fire breaking out in homes, schools and other buildings.',
           'سکول اور گھروں میں آگ لگنے کے حادثات ایک سنجیدہ خطرہ ہے۔ ہر سال تقریباً 3400 لوگ آگ کی وجہ سے زخمی یا مر جاتے ہیں۔ احتیاطی تدابیر اختیار کر کے ان سے بچاؤ ممکن ہے۔ درج ذیل وجوہات کی وجہ سے گھروں، سکولوں اور دوسرے عمارتوں میں آگ لگنے کا خطرہ ہوتا ہے۔',
           'په ښوونځیو او کورونو کې د اور لګېدو پېښې یو جدي خطر دی. هر کال نږدې ۳۴۰۰ کسان د اور له امله ټپيان کېږي یا مري. د احتیاطي ګامونو په پورته کولو د دوی مخنیوی شونی دی. د لاندې لاملونو له امله په کورونو، ښوونځیو او نورو ودانیو کې د اور لګېدو خطر وي.')])
    r = rec(b, 4, 1, 33, first=True)
    deco(r, 'A band of flames along the foot of the page is decorative.')
    BOOK.save(33, [(4, r)], issues=[{'id': 'hpe12-pdf033', 'unit': 4, 'printedPage': 28,
               'description': 'Owner Urdu ballpoint notes beside the objectives and the heading are excluded. The heading and paragraph lines are cut at the right edge of the scan (“سکول”, “سے”, “سکولوں”) and completed from context. “دوسرے عمارتوں”. Retained as printed.'}])


def p34():
    b = Builder()
    b.h('1. Cooking', '1۔ کوکنگ (Cooking)', '1. پخلی (Cooking)')
    P(b, [('Often people are careless while cooking food and put things that catch fire, e.g. cloth, oil or other things, near the stove and go out of the kitchen, through which the danger of fire increases.',
           'اکثر لوگ کھانا پکانے کے دوران بے احتیاطی کرتے ہیں اور آگ پکڑنے والے چیزوں مثلاً کپڑا، تیل یا دوسرے اشیا کو چولہے کے قریب رکھ دیتے ہیں اور کچن سے باہر چلے جاتے ہیں جس سے آگ لگنے کا خطرہ بڑھ جاتا ہے۔',
           'ډېر خلک د خوړو د پخلي پر مهال بې‌احتیاطي کوي او اور اخیستونکي شیان، لکه ټوکر، تېل یا نور توکي، بټۍ ته نږدې ږدي او له پخلنځي بهر ځي چې له امله یې د اور لګېدو خطر زیاتېږي.')])
    b.h('Fire appliances', 'آگ کے آلات', 'د اور وسایل')
    P(b, [('In homes different appliances of fire are used. Among these appliances heaters, stoves, chimneys, gas cylinders etc. are included. These appliances should be checked by an expert technician at least once a year. Burnable things should be kept at a distance of one metre from these appliances, for example clothes, paper, books, curtains, furniture etc. Take care while drying clothes and shoes on the heater. Install fire alarms in homes and schools so that information is received in time.',
           'گھروں میں آگ کے مختلف آلات استعمال کیے جاتے ہیں۔ ان آلات میں ہیٹر، سٹوپ، چمنی، گیس سلنڈر وغیرہ شامل ہیں۔ یہ آلات ماہر ٹیکنیشن سے کم از کم سال میں ایک بار چیک کروائے جائیں۔ ان آلات سے جلنے والی اشیاء ایک میٹر کے فاصلے پر رکھی جائیں۔ مثال کے طور پر کپڑے، پیپر، کتابیں، پردے، فرنیچر وغیرہ۔ کپڑے اور جوتے ہیٹر پر خشک کرتے وقت احتیاط کریں۔ گھر اور سکولوں میں فائر الارم لگا دیں تاکہ بروقت اطلاع مل جائے۔',
           'په کورونو کې د اور بېلابېل وسایل کارول کېږي. په دې وسایلو کې هیټر، سټوپ، بخارۍ، ګاز سلنډر او نور شامل دي. دا وسایل دې لږ تر لږه په کال کې یو ځل د ماهر تخنیکر له خوا وکتل شي. سوځېدونکي توکي دې له دې وسایلو یو متر لرې کېښودل شي، لکه جامې، کاغذ، کتابونه، پردې، فرنیچر او نور. پر هیټر د جامو او بوټانو د وچولو پر مهال احتیاط وکړئ. په کور او ښوونځیو کې د اور خبرتیا (فایر الارم) ولګوئ ترڅو په وخت خبرتیا ترلاسه شي.')])
    b.h('Cigarette smoking', 'سگریٹ نوشی', 'سګرټ څکول')
    P(b, [('Some people smoke cigarettes carelessly. They throw cigarettes near burnable things and do not pay attention. From this the remaining things catch fire.',
           'بعض افراد بے احتیاطی سے سگریٹ نوشی کرتے ہیں۔ سگریٹ جلنے والی اشیا کے نزدیک پھینک کر توجہ نہیں دیتے۔ اس سے باقی اشیا آگ پکڑ لیتی ہیں۔',
           'ځینې کسان په بې‌احتیاطۍ سګرټ څکوي. سګرټ سوځېدونکو توکو ته نږدې غورځوي او پام نه کوي. له دې نور توکي اور اخلي.')])
    b.h('Electrical appliances', 'بجلی کے آلات', 'برېښنايي وسایل')
    P(b, [('A big cause of fire in homes is the use of defective electrical appliances and wires, from which often a short circuit happens and fire breaks out.',
           'گھروں میں آگ لگنے کی ایک بڑی وجہ ناقص آلات بجلی اور تاروں کا استعمال ہے۔ جس سے اکثر شارٹ سرکٹ ہو جاتا ہے اور آگ لگ جاتی ہے۔',
           'په کورونو کې د اور لګېدو یو لوی لامل د ناقصو برېښنايي وسایلو او مزو کارول دي چې له امله یې ډېری وخت شارټ سرکټ کېږي او اور لګي.')])
    r = rec(b, 4, 2, 34)
    deco(r, 'Photographs of a pot on a burning stove with a cloth alight, and of a burning plug in a wall socket, are decorative.')
    BOOK.save(34, [(4, r)], issues=[{'id': 'hpe12-pdf034', 'unit': 4, 'printedPage': 29,
               'description': 'Line ends at the left edge of the scan are cut (“گیس”, “جلنے”, “اور”, “نہیں”) and completed from context. “آگ پکڑنے والے چیزوں”, “سٹوپ”. Retained as printed.'}])


def p35():
    b = Builder()
    b.h('Gas leakage', 'گیس لیکیج', 'د ګاز لیکیدل')
    P(b, [('In homes gas pipes and stoves often leak. In winter people put gas heaters in rooms and then forget to turn them off, from which gas leaks and spreads in the whole room; during this, on striking a matchstick or turning on an electric switch, fire breaks out with an explosion.',
           'گھروں میں اکثر گیس کے پائپ اور چولہے لیک ہو جاتے ہیں۔ سردیوں میں لوگ کمروں میں گیس ہیٹر لگاتے ہیں اور پھر بند کرنا بھول جاتے ہیں۔ جس سے گیس لیک ہو کر سارے کمرے میں پھیل جاتی ہے اس دوران دیاسلائی یا بجلی کا بٹن آن کرنے پر دھماکہ سے آگ لگ جاتی ہے۔',
           'په کورونو کې ډېری وخت د ګاز پایپونه او بټۍ لیکېږي. په ژمي کې خلک په کوټو کې ګازي هیټرونه لګوي او بیا یې بندول هېروي، له امله یې ګاز لیکېږي او ټولې کوټې ته خپرېږي؛ په دې وخت کې د اورلګیت یا د برېښنا د سویچ په روښانه کولو په چاودنه اور لګي.')])
    b.h('Children playing with things that start fire', 'بچوں کا آگ لگانے والی اشیاء سے کھیلنا', 'د اور لګوونکو توکو سره د ماشومانو لوبې')
    P(b, [('Often children are playing with matches or lighters etc., and they light the matches and throw them, from which there is a danger of fire.',
           'اکثر بچے ماچس یا لائٹر وغیرہ سے کھیل رہے ہوتے ہیں۔ اور ماچس لگا کر پھینک دیتے ہیں جس سے آگ لگنے کا خطرہ ہوتا ہے۔',
           'ډېری وخت ماشومان له اورلګیت یا لایټر او نورو سره لوبې کوي او اورلګیت بل کړي او وې غورځوي چې له امله یې د اور لګېدو خطر وي.')])
    b.h('Inflammable things', 'شعلہ دینے والی اشیاء', 'لمبه ورکوونکي توکي')
    P(b, [('If fuel, paint, gunpowder and other things are stored carelessly, these become explosive. These things become the cause of an explosion, from which fire breaks out.',
           'ایندھن، پینٹ، بارود اور دوسرے اشیاء کو بے احتیاطی سے سٹور کیا جائے تو یہ دھماکہ خیز ہوتی ہیں۔ یہ اشیاء دھماکے کا باعث بنتی ہیں۔ جس سے آگ لگ جاتی ہے۔',
           'که سونګ توکي، رنګ، باروت او نور توکي په بې‌احتیاطۍ زېرمه شي، چاودېدونکي کېږي. دا توکي د چاودنې لامل کېږي چې له امله یې اور لګي.')])
    b.h('Decoration items', 'ڈیکوریشن کی اشیاء', 'د سینګار توکي')
    P(b, [('Nowadays lights that give light in different colours from electricity are available. Their wires are fine and delicate. If these wires pass near things that catch fire, they quickly catch fire.',
           'آج کل بجلی سے مختلف رنگوں میں روشنی دینے والی لائٹس دستیاب ہیں۔ ان کی تاریں باریک اور نازک ہوتی ہیں۔ اگر یہ تاریں آگ پکڑنے والی اشیاء سے گزریں تو وہ جلدی آگ پکڑ لیتی ہیں۔',
           'نن ورځ له برېښنا په بېلابېلو رنګونو رڼا ورکوونکي څراغونه شته. مزي یې نري او نازک وي. که دا مزي له اور اخیستونکو توکو تېر شي، ژر اور اخلي.')])
    r = rec(b, 4, 3, 35)
    deco(r, 'Photographs of a burning extension board and a tangle of coloured decoration lights are decorative.')
    BOOK.save(35, [(4, r)], issues=[{'id': 'hpe12-pdf035', 'unit': 4, 'printedPage': 30,
               'description': 'An owner Urdu ballpoint note above “شعلہ دینے والی اشیاء” is excluded. Line starts at the right edge of the decoration paragraph (“دینے”, “نازک”, “گزریں”) are cut in the scan and completed from context. “دوسرے اشیاء”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    {30: p30, 31: p31, 32: p32, 33: p33, 34: p34, 35: p35}[n]()
