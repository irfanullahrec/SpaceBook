"""HPE XII PDF132–137: pp.128–133 — basketball 5/8/24-second rules, back court, personal/intentional/double/technical/coach fouls, multiple, five and
seven fouls; basketball exercise; netball court (measurements, diagram, shooting circle, centre circle). Run: python class12_hpe_page132.py N (132–137)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T

Q_ = lambda x: (x, x, x)


def p132():
    b = Builder()
    b.h('The 5-second rule', '5 سیکنڈ کا قانون', 'د ۵ ثانیو قانون')
    P(b, [('The player who has the ball is stopped from so close that he cannot pass for 5 seconds, cannot throw for a point, nor can he himself move forward; in such a case the 5-second law applies.', 'جس کھلاڑی کے پاس بال ہو اسے قریب سے ایسے روکا جائے کہ وہ 5 سیکنڈ تک پاس نہ کر سکے نہ پوائنٹ کیلئے پھینک سکے اور نہ ہی خود آگے لے جا سکے تو ایسی صورت میں 5 سیکنڈ کا قانون لاگو ہوتا ہے۔', 'هغه لوبغاړی چې توپ ورسره وي، له نږدې داسې ودرول شي چې ۵ ثانیې پاس ونه شي کړای، د نمرې لپاره یې ونه غورځوي او نه یې پخپله مخکې یوسي، په داسې حال کې د ۵ ثانیو قانون پلي کېږي.'),
          ('While making a side throw, if the ball is not thrown inside within 5 seconds, then too the 5-second law will apply. In case of obstruction the same team, while in case of delay the opposing team, will be given the side throw.', 'سائیڈ تھرو کرتے وقت اگر 5 سیکنڈ کے اندر اندر بال نہ پھینکا جائے تو بھی 5 سیکنڈ کا قانون لاگو ہوگا۔ رکاوٹ کی صورت میں اسی ٹیم کو جبکہ تاخیر کی صورت میں مخالف ٹیم کو سائیڈ تھرو دی جائے گی۔', 'د څنګ غورځونې پر وخت که توپ په ۵ ثانیو کې دننه ونه غورځول شي، بیا هم د ۵ ثانیو قانون پلي کېږي. د خنډ په صورت کې همغه ټیم ته، او د ځنډ په صورت کې مخالف ټیم ته د څنګ غورځونه ورکول کېږي.')])
    b.h('The 8-second rule', '8 سیکنڈ کا قانون', 'د ۸ ثانیو قانون')
    P(b, [('The team that gets possession of the ball in the back part of the court will have to bring the ball into the front part of the court within 8 seconds; otherwise the 8-second law will apply and the opposing team will be given a side throw.', 'جو ٹیم کورٹ کے پچھلے حصے میں بال پر قابض ہو جائے تو اسے بال کو 8 سیکنڈ کے اندر کورٹ کے اگلے حصے میں لانا ہوگا۔ بصورتِ دیگر 8 سیکنڈ کا قانون لاگو ہوگا۔ اور مخالف ٹیم کو سائیڈ تھرو دی جائے گی۔', 'هغه ټیم چې د میدان په شاتنۍ برخه کې پر توپ واک ترلاسه کړي، باید په ۸ ثانیو کې توپ د میدان مخکینۍ برخې ته راوړي؛ که نه، د ۸ ثانیو قانون پلي کېږي او مخالف ټیم ته د څنګ غورځونه ورکول کېږي.')])
    b.h('The 24-second rule', '24 سیکنڈ کا قانون', 'د ۲۴ ثانیو قانون')
    P(b, [('When the ball comes into the possession of a team, it should try to throw the ball for a point within 24 seconds. If some team fails to do so, the 24-second law will apply against that team and a throw-in will be given to the opposing team.', 'کسی ٹیم کے قبضہ میں بال آ جائے تو اسے 24 سیکنڈ کے اندر پوائنٹ کیلئے بال پھینکنے کی کوشش کرنی چاہیے۔ اگر ایسا کرنے میں کوئی ٹیم ناکام رہتی ہے تو اس ٹیم کے خلاف 24 سیکنڈ کا قانون لاگو ہوگا۔ اور مخالف ٹیم کو تھرو ان دی جائے گی۔', 'کله چې توپ د کوم ټیم واک ته راشي، باید په ۲۴ ثانیو کې د نمرې لپاره توپ وغورځوي. که کوم ټیم په دې کې ناکام شي، د هغه پر وړاندې د ۲۴ ثانیو قانون پلي کېږي او مخالف ټیم ته تھرو ان ورکول کېږي.')])
    b.h('Bringing the ball back into the back court', 'بال کو پچھلے کورٹ میں واپس لانا', 'شاتني میدان ته د توپ بېرته راوړل')
    P(b, [('The team in whose possession the ball is, as soon as it takes the ball into the front court, cannot throw it again into the back court. On doing so, a side throw will be given to the opposing team.', 'جس ٹیم کے قبضے میں بال ہو اور وہ جوں ہی بال کو اگلے کورٹ میں لے جائے تو دوبارہ پچھلے کورٹ میں نہیں پھینک سکتا۔ ایسا کرنے پر مخالف ٹیم کو سائیڈ تھرو دی جائے گی۔', 'هغه ټیم چې توپ یې په واک کې وي، څنګه چې توپ مخکیني میدان ته یوسي، بیا یې شاتني میدان ته نه شي غورځولی. په دې کار مخالف ټیم ته د څنګ غورځونه ورکول کېږي.')])
    b.h('Personal Foul', 'پرسنل فاؤل (Personal Foul)', 'شخصي خطا (Personal Foul)')
    P(b, [('A personal foul is given for the following errors of a player.', 'پرسنل فاؤل کھلاڑی کی مندرجہ ذیل غلطیوں پر دیا جاتا ہے۔', 'شخصي خطا د لوبغاړي په لاندې تېروتنو ورکول کېږي.')])
    L(b, [('Holding some player.', 'کسی کھلاڑی کو پکڑنا۔', 'کوم لوبغاړی نیول.'), ('Hitting the opponent with the shoulder or knee.', 'مخالف کو کندھا یا گھٹنا مارنا۔', 'مخالف ته اوږه یا زنګون وهل.'), ('Pushing the opposing player.', 'مخالف کھلاڑی کو دھکیلنا۔', 'مخالف لوبغاړي ته ټېله ورکول.'),
          ('Blocking in an illegal way when the body is colliding.', 'غیر قانونی طریقہ سے بلاکنگ کرنا جبکہ جسم ٹکرا رہا ہو۔', 'په غیر قانوني ډول بلاک کول کله چې بدن ټکر کوي.')])
    r = rec(b, 7, 51, 132)
    BOOK.save(132, [(7, r)], issues=[{'id': 'hpe12-pdf132', 'unit': 7, 'printedPage': 128,
               'description': 'The left edge of the scan cuts some line ends and the first letters of the headings (“5 سیکنڈ”, “پرسنل”), completed from context. Retained as printed.'}])


def p133():
    b = Builder()
    b.h('Penalty', 'سزا', 'سزا')
    P(b, [('If the foul is committed by such a player as was not throwing the ball for a point, then a side throw will be given. If he was attempting a point and the point is made, the goal will be accepted, and if not, then three free throws will be given. The personal foul will be recorded in the name of the player.', 'اگر فاؤل ایسے کھلاڑی سے واقع ہو جو بال پوائنٹ کیلئے نہیں پھینک رہا تو سائیڈ تھرو دی جائے گی۔ اگر پوائنٹ کی کوشش کر رہا ہو اور پوائنٹ ہو جائے تو گول تسلیم کر لیا جائے گا اور نہ ہونے کی صورت میں تین فری تھروز دی جائیں گی۔ کھلاڑی کے نام پر ذاتی فاؤل درج کر لیا جائے گا۔', 'که خطا له داسې لوبغاړي وشي چې د نمرې لپاره یې توپ نه غورځاوه، د څنګ غورځونه ورکول کېږي. که د نمرې هڅه یې کوله او نمره وشوه، ګول منل کېږي او که نه، درې وړیا غورځونې ورکول کېږي. د لوبغاړي په نوم شخصي خطا ثبتېږي.')])
    b.h('Intentional foul', 'ارادی فاؤل', 'قصدي خطا')
    P(b, [('That personal foul which is done deliberately and whose intensity is more than an ordinary personal foul is called an intentional foul. Ignoring the ball and colliding physically with the opposing player is called an intentional foul.', 'وہ ذاتی فاؤل جو جان بوجھ کر کیا جائے اور جس کی شدت عام ذاتی فاؤل سے زیادہ ہو تو ارادی فاؤل کہلاتا ہے۔ بال کو نظرانداز کر کے مخالف کھلاڑی سے جسمانی ٹکراؤ کرنا ارادی فاؤل کہلاتا ہے۔', 'هغه شخصي خطا چې په قصد وشي او شدت یې له عامې شخصي خطا ډېر وي، قصدي خطا بلل کېږي. توپ له پامه غورځول او له مخالف لوبغاړي سره بدني ټکر قصدي خطا بلل کېږي.')])
    b.h('Penalty', 'سزا', 'سزا')
    P(b, [('A foul will be recorded in the name of the player. The opponent will get 2 free throws.', 'کھلاڑی کے نام پر فاؤل درج ہوگا۔ مخالف کو 2 فری تھرو ملیں گی۔', 'د لوبغاړي په نوم خطا ثبتېږي. مخالف ته به ۲ وړیا غورځونې ورکول کېږي.')])
    b.h('Double foul', 'دوہرا فاؤل', 'دوه‌ګونې خطا')
    P(b, [('When two opposing players commit a foul against each other at the same time, it will be called a double foul. The game will start again with a jump ball and no free throw will be given.', 'جب دو مخالف کھلاڑی ایک دوسرے کے خلاف بیک وقت فاؤل کریں تو دوہرا فاؤل کہلائے گا۔ کھیل دوبارہ جمپ بال سے شروع ہوگا فری تھرو نہیں دی جائے گی۔', 'کله چې دوه مخالف لوبغاړي په یو وخت یو پر بل خطا وکړي، دوه‌ګونې خطا بلل کېږي. لوبه بیا په جمپ بال پیلېږي او وړیا غورځونه نه ورکول کېږي.')])
    b.h('Technical foul of a player', 'کھلاڑی کا ٹیکنیکل فاؤل', 'د لوبغاړي تخنیکي خطا')
    P(b, [('Such a breach of rules as is done intentionally and benefits the one committing the foul illegally is called a technical foul. A technical foul will be given in the following cases.', 'ایسی ضابطہ شکنی جو عمداً کی جائے اور وہ فاؤل کنندہ کو ناجائز فائدہ پہنچاتا ہو ٹیکنیکل فاؤل کہلاتا ہے۔ مندرجہ ذیل صورتوں میں ٹیکنیکل فاؤل دیا جائے گا۔', 'هغه قاعده ماتونه چې په قصد وشي او خطا کوونکي ته ناروا ګټه ورسوي، تخنیکي خطا بلل کېږي. په لاندې حالتونو کې تخنیکي خطا ورکول کېږي.')])
    L(b, [('Indecent behaviour with some official.', 'کسی عہدیدار سے ناشائستہ رویہ۔', 'له کوم چارواکي سره ناوړه چلند.'), ('Creating delay in the game without reason.', 'کھیل میں بلاوجہ تاخیر پیدا کرنا۔', 'په لوبه کې بې‌دلیله ځنډ پیدا کول.'),
          ('Using such words for the opposing player as hurt his feelings.', 'مخالف کھلاڑی کے لیے ایسے الفاظ استعمال کرنا جس سے اس کے جذبات کو ٹھیس پہنچے۔', 'د مخالف لوبغاړي لپاره داسې ټکي کارول چې احساسات یې ټپي کړي.'), ('Not raising the hand when the foul is committed.', 'فاؤل سرزد ہونے پر ہاتھ نہ اٹھانا۔', 'د خطا په صورت کې لاس نه پورته کول.')])
    r = rec(b, 7, 52, 133)
    BOOK.save(133, [(7, r)])


def p134():
    b = Builder()
    L(b, [('Changing the number without informing the referee and scorer.', 'ریفری اور سکورر کو بتائے بغیر نمبر تبدیل کرنا۔', 'ریفري او نمره لیکونکي ته له ویلو پرته شمېره بدلول.'), ('A substitute player entering or leaving the court without informing.', 'بتائے بغیر متبادل کھلاڑی کا کورٹ میں داخل ہونا اور کورٹ سے باہر جانا۔', 'له خبرولو پرته د بدیل لوبغاړي میدان ته ننوتل او له میدان وتل.')])
    b.h('Penalty', 'سزا', 'سزا')
    P(b, [('The foul will be written in the name of the player who committed it, and the opposing team will be given a free throw.', 'جس کھلاڑی سے فاؤل سرزد ہو اس کے نام فاؤل لکھا جائے گا۔ اور مخالف ٹیم کو فری تھرو دی جائے گی۔', 'د هغه لوبغاړي په نوم چې خطا یې کړې، خطا لیکل کېږي او مخالف ټیم ته وړیا غورځونه ورکول کېږي.')])
    b.h('Technical foul of coach and substitute players', 'کوچ اور متبادل کھلاڑیوں کا ٹیکنیکل فاؤل', 'د روزونکي او بدیلو لوبغاړو تخنیکي خطا')
    L(b, [('Coaching the team from outside.', 'ٹیم کو باہر سے کوچ کرنا۔', 'ټیم ته له بهر روزنه ورکول.'), ('Misbehaving with some official.', 'کسی عہدیدار سے بدتمیزی کرنا۔', 'له کوم چارواکي سره بې‌ادبي.'), ('Entering the court at the time of time-out.', 'ٹائم آؤٹ کے وقت کورٹ میں داخل ہونا۔', 'د ټایم اوټ پر وخت میدان ته ننوتل.'),
          ('The coach or substitute player entering the court to help some injured player without informing.', 'کوچ یا متبادل کھلاڑی کا بتائے بغیر کسی زخمی کھلاڑی کی مدد کیلئے کورٹ میں داخل ہونا۔', 'د روزونکي یا بدیل لوبغاړي له خبرولو پرته د ټپي لوبغاړي د مرستې لپاره میدان ته ننوتل.')])
    b.h('Penalty', 'سزا', 'سزا')
    P(b, [('A foul will be recorded against the trainer or substitute player, and the opposing team will be given a free throw.', 'تربیت کار یا متبادل کھلاڑی کے خلاف فاؤل درج ہوگا اور مخالف ٹیم کو فری تھرو دی جائے گی۔', 'د روزونکي یا بدیل لوبغاړي پر وړاندې خطا ثبتېږي او مخالف ټیم ته وړیا غورځونه ورکول کېږي.')])
    b.h('Multiple foul', 'متعدد فاؤل', 'څو ګونې خطا')
    P(b, [('When two or more players of some team commit a personal foul at the same time, it will be called a multiple foul. One personal foul will be counted against the one committing the foul, and the opposing team will be given two free throws. If a point has been made, the point will be counted.', 'جب کسی ٹیم کے دو یا دو سے زیادہ کھلاڑی بیک وقت ذاتی فاؤل کا ارتکاب کریں تو ملٹی پل (Multiple) فاؤل کہلائے گا۔ فاؤل کرنے والے کے خلاف ایک ذاتی فاؤل شمار ہوگا۔ اور مخالف ٹیم کو دو فری تھرو دی جائیں گی۔ پوائنٹ ہو چکا ہو تو پوائنٹ شمار ہوگا۔', 'کله چې د کوم ټیم دوه یا ډېر لوبغاړي په یو وخت شخصي خطا وکړي، څو ګونې (Multiple) خطا بلل کېږي. د خطا کوونکي پر وړاندې یوه شخصي خطا ګڼل کېږي او مخالف ټیم ته دوه وړیا غورځونې ورکول کېږي. که نمره شوې وي، نمره ګڼل کېږي.')])
    b.h('Five fouls', 'پانچ فاؤل', 'پنځه خطاګانې')
    P(b, [('The player who has committed five fouls, whether personal or technical, will be removed from the game. He cannot come again in that match.', 'جو کھلاڑی پانچ فاؤل کر چکا ہو خواہ ذاتی ہوں یا ٹیکنیکل اسے کھیل سے نکال دیا جائے گا۔ وہ اس میچ میں دوبارہ نہیں آ سکتا۔', 'هغه لوبغاړی چې پنځه خطاګانې یې کړې وي، که شخصي وي یا تخنیکي، له لوبې ایستل کېږي. په هغه لوبه کې بیا نه شي راتلی.')])
    b.h('Seven fouls', 'سات فاؤل', 'اوه خطاګانې')
    P(b, [('When seven fouls of some team in total are complete, then after that, on every foul, the opposing team will be given a free throw. (This is called “one by one”.)', 'جب کسی ٹیم کے مجموعی طور پر سات فاؤل پورے ہو جائیں تو اس کے بعد ہر فاؤل پر مخالف ٹیم کو فری تھرو دی جائے گی۔ (اس کو ”ون بائی ون“ کہتے ہیں)۔', 'کله چې د کوم ټیم په ټولیز ډول اوه خطاګانې پوره شي، له هغه وروسته په هره خطا مخالف ټیم ته وړیا غورځونه ورکول کېږي. (دې ته "ون بای ون" ویل کېږي).')])
    r = rec(b, 7, 53, 134)
    BOOK.save(134, [(7, r)])


def p135():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The game of basketball began in ________ .', 'باسکٹ بال کھیل کی ابتداء ________ سے ہوئی۔', 'د باسکټبال لوبه له ________ پیل شوه.'), [('America', 'امریکہ', 'امریکا'), ('England', 'انگلینڈ', 'انګلستان'), ('Germany', 'جرمنی', 'جرمني'), ('European Union', 'یورپی یونین', 'اروپايي اتحادیه')]),
         (('Basketball began in ________ .', 'باسکٹ بال کی ابتداء ________ میں ہوئی۔', 'باسکټبال په ________ کې پیل شو.'), [Q_('1889'), Q_('1891'), Q_('1893'), Q_('1895')]),
         (('The minimum weight of the basketball is ________ grams.', 'باسکٹ بال کا کم از کم وزن ________ گرام ہوتا ہے۔', 'د باسکټبال لږ تر لږه وزن ________ ګرامه وي.'), [Q_('563'), Q_('565'), Q_('567'), Q_('569')]),
         (('The length of the basketball court is ________ metres.', 'باسکٹ بال کورٹ کی لمبائی ________ میٹر ہوتی ہے۔', 'د باسکټبال د میدان اوږدوالی ________ متره وي.'), [Q_('24'), Q_('26'), Q_('28'), Q_('30')]),
         (('The breadth of the basketball court is ________ metres.', 'باسکٹ بال کورٹ کی چوڑائی ________ میٹر ہوتی ہے۔', 'د باسکټبال د میدان پلنوالی ________ متره وي.'), [Q_('15'), Q_('17'), Q_('19'), Q_('21')]),
         (('The thickness of all the lines of the basketball court is ________ centimetres.', 'باسکٹ کورٹ کی تمام لائنوں کی موٹائی ________ سینٹی میٹر ہوتی ہے۔', 'د باسکټبال د میدان د ټولو کرښو پنډوالی ________ سانتي متره وي.'), [Q_('3'), Q_('5'), Q_('7'), Q_('9')]),
         (('In basketball the radius of the centre circle is ________ .', 'باسکٹ بال میں سنٹر سرکل ________ کا نصف قطر ہوتا ہے۔', 'په باسکټبال کې د منځنۍ دایرې نیم قطر ________ وي.'), [('1.80 metres', '1.80 میٹر', '۱.۸۰ متره'), ('1.85 metres', '1.85 میٹر', '۱.۸۵ متره'), ('1.90 metres', '1.90 میٹر', '۱.۹۰ متره'), ('1.95 metres', '1.95 میٹر', '۱.۹۵ متره')]),
         (('In basketball the length of the backboard is ________ metres.', 'باسکٹ بال میں بیک بورڈ کی لمبائی ________ میٹر ہوتی ہے۔', 'په باسکټبال کې د شاتنۍ تختې اوږدوالی ________ متره وي.'), [('1.26', '1.26', '۱.۲۶'), ('1.24', '1.24', '۱.۲۴'), ('1.22', '1.22', '۱.۲۲'), ('1.20', '1.20', '۱.۲۰')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['i.', 'ii.', 'iii.', 'iv.', 'v.', 'vi.', 'vii.', 'viii.'][i], q, o, per_line=4)
    r = BOOK.record(e, 'hpe12-ch7-exercise-basketball-1', 'Chapter 7 exercise: basketball (1)', 'باب ۷: مشقی سوالات — باسکٹ بال (۱)', '۷ څپرکی: تمریني پوښتنې — باسکټبال (۱)', 135, [131])
    BOOK.save(135, [(7, r)], issues=[{'id': 'hpe12-pdf135', 'unit': 7, 'printedPage': 131,
               'description': 'Q(viii): none of the printed options (1.26, 1.24, 1.22, 1.20 m) matches the 1.80 m backboard length given on p.124; an owner has struck the options through and written “1.80” — the owner writing is excluded and the printed options are retained. Q(i)–(ii) ask about the origin of basketball, not covered in the text. Owner notes at the top are excluded.'}])


def nb_court(cap):
    b = ('<rect x="20" y="40" width="560" height="300" fill="#e5e7eb" stroke="#1e293b" stroke-width="2"/><rect x="60" y="70" width="480" height="240" fill="#3b82f6" stroke="#fff" stroke-width="2"/>'
         '<line x1="220" y1="70" x2="220" y2="310" stroke="#fff" stroke-width="2"/><line x1="380" y1="70" x2="380" y2="310" stroke="#fff" stroke-width="2"/><circle cx="300" cy="190" r="8" fill="none" stroke="#fff" stroke-width="2"/>'
         '<path d="M60 112 A78 78 0 0 1 60 268" fill="none" stroke="#fff" stroke-width="2"/><path d="M540 112 A78 78 0 0 0 540 268" fill="none" stroke="#fff" stroke-width="2"/>'
         '<circle cx="62" cy="190" r="4" fill="#dc2626"/><circle cx="538" cy="190" r="4" fill="#dc2626"/>')
    for t, x, y in [('30.50 metres', 300, 35), ('10.167m', 140, 85), ('10.167m', 300, 85), ('10.167m', 460, 85), ('15.25 metres', 45, 190), ('3.05m', 35, 55), ('3.05m', 565, 55), ('R=4.9m', 100, 185),
                    ('900mm', 300, 215), ('Goal Post', 75, 230), ('Goal Post', 525, 230), ('7.625m', 595, 130), ('7.625m', 595, 250), ('Obstacle free run-off zone', 300, 330)]:
        b += T(x, y, t, 10, 'bold', 'middle', '#ffffff' if 60 < x < 540 and 70 < y < 310 else '#1e293b')
    return svg(620, 360, b, cap)


def p136():
    e = Builder()
    e.mcq('ix.', ('In basketball the height of the basket above the ground is ________ feet.', 'باسکٹ بال میں زمین سے باسکٹ کی اونچائی ________ فٹ ہوتی ہے۔', 'په باسکټبال کې له ځمکې د باسکټ لوړوالی ________ فټه وي.'), [Q_('4'), Q_('6'), Q_('8'), Q_('10')], per_line=4)
    e.p('2. Write short notes on the following.', '۲۔ درج ذیل پر مختصر نوٹ لکھیں۔', '۲. پر لاندې لنډ یادښتونه ولیکئ.')
    e.group('lines', [('i. Time-out in basketball.', 'i۔ باسکٹ بال میں ٹائم آؤٹ۔', 'i. په باسکټبال کې ټایم اوټ.'), ('ii. The 24-second rule in basketball.', 'ii۔ باسکٹ بال میں 24 سیکنڈ کا قانون۔', 'ii. په باسکټبال کې د ۲۴ ثانیو قانون.'),
                      ('iii. Duties of the referee in basketball.', 'iii۔ باسکٹ بال میں ریفری کے فرائض۔', 'iii. په باسکټبال کې د ریفري دندې.'), ('iv. Technical foul of a player in basketball.', 'iv۔ باسکٹ بال میں کھلاڑی کا ٹیکنیکل فاؤل۔', 'iv. په باسکټبال کې د لوبغاړي تخنیکي خطا.'),
                      ('v. Make the basketball court.', 'v۔ باسکٹ بال کورٹ بنائیں۔', 'v. د باسکټبال میدان جوړ کړئ.'),
                      ('3. Write the duties of the officials in basketball.', '3۔ باسکٹ بال میں عہدیدار کے فرائض تحریر کریں۔', '3. په باسکټبال کې د چارواکو دندې ولیکئ.'),
                      ('4. Write in detail about fouls in basketball.', '4۔ باسکٹ بال میں فاؤلز کے بارے میں تفصیل سے لکھیں۔', '4. په باسکټبال کې د خطاګانو په اړه په تفصیل ولیکئ.')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-basketball-2', 'Chapter 7 exercise: basketball (2)', 'باب ۷: مشقی سوالات — باسکٹ بال (۲)', '۷ څپرکی: تمریني پوښتنې — باسکټبال (۲)', 136, [132])
    BOOK.save(136, [(7, r)], issues=[{'id': 'hpe12-pdf136', 'unit': 7, 'printedPage': 132, 'description': 'An owner tick is excluded. The rest of the page is blank in print.'}])


def p137():
    b = Builder()
    b.h('Netball', 'نیٹ بال (Net Ball)', 'نېټبال (Net Ball)')
    b.h('Measurements of the court:', 'کورٹ کی پیمائش:', 'د میدان اندازې:')
    b.group('lines', [('Length — 100 feet or 30.50 metres', 'لمبائی۔ 100 فٹ یا 30.50 میٹر', 'اوږدوالی — ۱۰۰ فټه یا ۳۰.۵۰ متره'), ('Breadth — 50 feet or 15.25 metres', 'چوڑائی۔ 50 فٹ یا 15.25 میٹر', 'پلنوالی — ۵۰ فټه یا ۱۵.۲۵ متره')])
    sv = [nb_court(c) for c in ('Netball court (labels as printed)', 'نیٹ بال کورٹ', 'د نېټبال میدان')]
    b.visual('hpe12-fig-netball-court', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Shooting circle:', 'شوٹنگ سرکل:', 'د ویشتو دایره:')
    P(b, [('Radius 16 feet from the middle of the goal line.', 'گول لائن کے وسط سے نصف قطر 16 فٹ۔', 'د ګول کرښې له منځه نیم قطر ۱۶ فټه.')])
    b.h('Centre circle:', 'سنٹر سرکل:', 'منځنۍ دایره:')
    P(b, [('A circle of 3 feet diameter in the centre of the court.', 'کورٹ کے مرکز میں 3 فٹ قطر کا دائرہ۔', 'د میدان په مرکز کې د ۳ فټو قطر دایره.')])
    r = rec(b, 7, 54, 137)
    BOOK.save(137, [(7, r)], issues=[{'id': 'hpe12-pdf137', 'unit': 7, 'printedPage': 133,
               'description': 'The netball court diagram is reproduced as a coded schematic with its printed English labels. Large owner ballpoint scribbles and notes around the heading and at the foot are excluded. The heading “سنٹر سرکل” is cut at the left edge.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 132
    {132: p132, 133: p133, 134: p134, 135: p135, 136: p136, 137: p137}[n]()
