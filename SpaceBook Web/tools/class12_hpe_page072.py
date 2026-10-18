"""HPE XII PDF72–77: pp.67–72 — long jump take off, flight, landing; chapter 6 exercise; chapter 7 (Rules and Skills of Games) opener;
target and field games — long jump rules, failures, runway diagram, mark, take-off board, landing area, strategy, running. Run: python class12_hpe_page072.py N (72–77)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, fig_longjump_runway


def p72():
    b = Builder()
    b.h('Take Off', 'ٹیک آف (Take Off)', 'ټېک اف (Take Off)')
    P(b, [('The act of converting the momentum obtained during the approach (Approach) into the jump is called take off (Take-off). In take off the third law of motion applies. The more force with which the player presses the take-off board, the faster his body will rise as a reaction.',
           'اپروچ (Approach) کے دوران حاصل کئے گئے مومینٹم کو جمپ میں تبدیل کرنے کے عمل کو ٹیک آف (Take-off) کہتے ہیں۔ ٹیک آف میں حرکت کا تیسرا قانون لاگو ہوتا ہے۔ کھلاڑی جتنی قوت کے ساتھ ٹیک آف بورڈ کو دبائے گا اس کا جسم ردِ عمل کے طور پر اتنی تیزی سے اٹھے گا۔',
           'د اپروچ (Approach) پر مهال ترلاسه شوي مومنټم په ټوپ اړولو عمل ته ټېک اف (Take-off) ویل کېږي. په ټېک اف کې د حرکت درېیم قانون پلي کېږي. لوبغاړی په څومره ځواک چې د ټېک اف تخته کیکاږي، د هغه بدن به د غبرګون په توګه هومره ژر پورته شي.')])
    b.h('Flight', 'اڑان (Flight)', 'الوتنه (Flight)')
    P(b, [('After take off comes the stage of flight. In this stage the following biomechanical principles are used.', 'ٹیک آف کے بعد اڑان کا مرحلہ آتا ہے۔ اس مرحلے میں مندرجہ ذیل بائیو مکینیکل اصول استعمال ہوتے ہیں', 'له ټېک اف وروسته د الوتنې پړاو راځي. په دې پړاو کې لاندې بایومیخانیکي اصول کارول کېږي.')])
    L(b, [('Correctness of the centre of gravity.', 'مرکزِ ثقل کا درست ہونا۔', 'د جاذبې د مرکز سموالی.'), ('Correctness of balance.', 'توازن کا درست ہونا۔', 'د توازن سموالی.')])
    b.h('Correctness of the centre of gravity', 'مرکز ثقل کا درست ہونا', 'د جاذبې د مرکز سموالی')
    P(b, [('In the stationary state the centre of gravity of the human body is at the navel, but at the time of flight it keeps changing with respect to the position of the body. Therefore irregularity in the centre of gravity can be prevented with the help of one’s style. Usually in the jump the hitch kick (Hitch Kick) and sailing (Sailing) styles are adopted, so that too much irregularity does not come into the centre of gravity.',
           'ساکن حالت میں انسانی جسم کا مرکزِ ثقل اس کی ناف پر ہوتا ہے لیکن اڑان کے وقت یہ جسم کی پوزیشن اعتبار سے تبدیل ہوتا رہتا ہے۔ اس لیے مرکزِ ثقل میں اپنے سٹائل کی مدد سے زیادہ بے قاعدگی آنے سے بچا جا سکتا۔ عموماً جمپ میں ہائیکنگ (Hitch Kick) اور سیلنگ (Sailing) کے سٹائل اپنائے جاتے ہیں۔ تاکہ مرکزِ ثقل میں بہت زیادہ حد تک بے قاعدگی نہ آئے۔',
           'په ولاړ حالت کې د انسان د بدن د جاذبې مرکز پر نامه وي، خو د الوتنې پر مهال د بدن د حالت سره سم بدلېږي. نو د خپل سټایل په مرسته د جاذبې په مرکز کې له ډېرې بې‌نظمۍ مخنیوی کېدای شي. عموماً په ټوپ کې د هچ کېک (Hitch Kick) او سېلنګ (Sailing) سټایلونه غوره کېږي ترڅو د جاذبې په مرکز کې ډېره بې‌نظمي رانه شي.')])
    b.h('Balance', 'توازن (Balance)', 'توازن (Balance)')
    P(b, [('To obtain more distance from the jump it is necessary to maintain balance, because during flight gravity, the resistance of the air and the force of take off act on the body of the player; therefore there is a need to improve one’s balance through practice.',
           'جمپ سے زیادہ فاصلہ حاصل کرنے کے لیے توازن برقرار رکھنا ضروری ہے کیونکہ اڑان کے دوران کھلاڑی کے جسم پر کشش ثقل، ہوا کی مزاحمت اور ٹیک آف کی قوت اثر انداز ہوتی ہے لہٰذا مشق سے اپنا توازن بہتر بنانے کی زیادہ ضرورت ہے۔',
           'له ټوپ ډېر واټن ترلاسه کولو لپاره د توازن ساتل اړین دي، ځکه د الوتنې پر مهال د لوبغاړي پر بدن جاذبه، د هوا مقاومت او د ټېک اف ځواک اغېز کوي؛ نو په تمرین د خپل توازن ښه کولو ته ډېره اړتیا ده.')])
    r = rec(b, 6, 15, 72)
    deco(r, 'A drawing of a jumper at take-off is decorative.')
    BOOK.save(72, [(6, r)], issues=[{'id': 'hpe12-pdf072', 'unit': 6, 'printedPage': 67,
               'description': '“ہائیکنگ (Hitch Kick)” (for hitch kick), “جسم کی پوزیشن اعتبار سے”, “بچا جا سکتا۔”. Line ends at the left edge are cut and completed from context. Retained as printed.'}])


def p73():
    b = Builder()
    b.h('Landing and Recovery', 'لینڈنگ اور ریکوری (Landing and Recovery)', 'کېناستل او رغونه (Landing and Recovery)')
    P(b, [('The end of the jump in the pit is on landing. According to the rules of the long jump the measurement of the player’s jump will be done from the take-off board up to that place where the first mark of his body is. Therefore, keeping in mind with extreme skill during landing Newton’s third law — that action and reaction are equal and in opposite directions — performance can be made better. When the body of the player strikes the surface of the landing area, a reaction as great as the force of the player’s body will arise, and the player will come backwards with the same speed; therefore during landing appropriate recovery is necessary so that the force of the reaction affects as little as possible.',
           'جمپ کا خاتمہ اکھاڑے میں لینڈنگ پر ہوتا ہے۔ لانگ جمپ کے قوانین کے مطابق کھلاڑی کے جمپ کی پیمائش ٹیک آف بورڈ سے اس جگہ تک کی جائے گی جہاں اس کے جسم کا پہلا نشان ہو۔ اس لیے لینڈنگ کے دوران انتہائی مہارت سے نیوٹن کے تیسرے قانون، عمل اور ردعمل برابر اور مخالف سمت میں ہوتے ہیں کا خیال رکھ کر پرفارمنس بہتر بنائی جا سکتی ہے۔ کھلاڑی کا جسم جب لینڈنگ ایریا کی سطح پر لگتا ہے۔ تو کھلاڑی کے جسم کی قوت سے اتنا ہی ردعمل پیدا ہوگا اور کھلاڑی اسی رفتار سے پیچھے کی جانب آئے گا لہٰذا لینڈنگ کے دوران مناسب ریکوری ضروری ہے تاکہ ردعمل کی قوت کم سے کم اثر انداز ہو۔',
           'د ټوپ پای په کنده کې په کېناستو وي. د اوږد ټوپ د قوانینو له مخې د لوبغاړي د ټوپ اندازه له ټېک اف تختې تر هغه ځایه کېږي چې د بدن لومړۍ نښه یې وي. نو د کېناستو پر مهال په ډېر مهارت د نیوټن درېیم قانون — عمل او غبرګون برابر او مخالف لوري ته وي — په پام کې نیولو سره کړنې ښې کېدای شي. کله چې د لوبغاړي بدن د کېناستو د ساحې پر سطحه ولګېږي، د بدن د ځواک په اندازه غبرګون پیدا کېږي او لوبغاړی په همغه سرعت شا ته راځي؛ نو د کېناستو پر مهال مناسبه رغونه اړینه ده ترڅو د غبرګون ځواک تر ټولو لږ اغېز وکړي.')])
    r = rec(b, 6, 16, 73)
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Write the answers to the following questions.', '۱۔ درج ذیل سوالات کے جوابات لکھیں۔', '۱. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('1) What are biomechanical principles and how do they work?', '1) بائیو مکینیکل اصول کیا ہیں اور کس طرح کام کرتے ہیں؟', '1) بایومیخانیکي اصول څه دي او څنګه کار کوي؟'),
                      ('2) Which principle is there for smashing in volleyball?', '2) والی بال میں سمیش کیلئے کونسا اصول ہوتا ہے۔', '2) په والیبال کې د سمیش لپاره کوم اصل وي؟'),
                      ('3) Write the biomechanical principles of stopping and hitting the ball in hockey.', '3) ہاکی میں بال روکنے اور ہٹ کرنے کی بائیو مکینیکل اصول لکھیں۔', '3) په هاکي کې د توپ درولو او وهلو بایومیخانیکي اصول ولیکئ.'),
                      ('4) Which principles of biomechanics work in the long jump?', '4) لانگ جمپ میں بائیو مکینیکل کے کون سے اصول کام کرتے ہیں۔', '4) په اوږد ټوپ کې د بایومیخانیک کوم اصول کار کوي؟'),
                      ('5) Which principles of biomechanics are at work in fielding and catching in cricket?', '5) کرکٹ میں فیلڈنگ اور کیچ میں بائیو مکینیکل کے کون سے اصول کارفرما ہوتے ہیں؟', '5) په کرکټ کې په فیلډنګ او کیچ کې د بایومیخانیک کوم اصول فعال وي؟')])
    ex = BOOK.record(e, 'hpe12-ch6-exercise', 'Chapter 6 exercise', 'باب ۶: مشقی سوالات', '۶ څپرکی: تمریني پوښتنې', 73, [68])
    BOOK.save(73, [(6, r), (6, ex)], complete_units=[6], issues=[{'id': 'hpe12-pdf073', 'unit': 6, 'printedPage': 68,
               'description': 'Owner ballpoint scribbles across the exercise heading are excluded. Q3 “بال روکنے اور ہٹ کرنے کی بائیو مکینیکل اصول”. Retained as printed.'}])


def p74():
    b = Builder()
    b.h('Chapter 7: Rules and Skills of Games', 'باب نمبر ۷: کھیلوں کے قوانین اور مہارتیں', '۷ څپرکی: د لوبو قوانین او مهارتونه')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('demonstrate ability in the rules, techniques and strategies of selected target and field games (long jump, high jump, javelin throw, discus throw).', 'منتخب ٹارگٹ اور فیلڈ گیمز کے قوانین، تکنیکوں اور حکمت عملیوں میں اہلیت کا مظاہرہ کر سکیں۔ (لمبی چھلانگ، اونچی چھلانگ، نیزہ پھینکنا، ڈسکس تھرو)', 'د ټاکلو هدف او میدان لوبو په قوانینو، تخنیکونو او تګلارو کې وړتیا وښيي (اوږد ټوپ، لوړ ټوپ، نېزه غورځول، ډیسکس غورځول).'),
          ('demonstrate ability in the rules, techniques and strategies of selected net and wall games (badminton).', 'منتخب نیٹ اور وال گیمز کے قوانین، تکنیکوں اور حکمت عملیوں میں اہلیت کا مظاہرہ کر سکیں۔ (بیڈمنٹن)', 'د ټاکلو جال او دېوال لوبو په قوانینو، تخنیکونو او تګلارو کې وړتیا وښيي (بډمنټن).'),
          ('demonstrate skill in the rules, techniques and strategies of selected striking and field games (cricket, baseball).', 'منتخب سٹرائیکنگ اور فیلڈ گیمز کے قوانین، تکنیکوں اور حکمت عملیوں میں مہارت کا مظاہرہ کر سکیں۔ (کرکٹ، بیس بال)', 'د ټاکلو وهلو او میدان لوبو په قوانینو، تخنیکونو او تګلارو کې مهارت وښيي (کرکټ، بیس بال).'),
          ('demonstrate skill in the rules, techniques and strategies of selected invasion and territorial games (basketball, netball, handball).', 'منتخب ان ویژن اور ٹیری ٹوریل گیمز کے قوانین، تکنیکوں اور حکمت عملیوں میں مہارت کا مظاہرہ کر سکیں۔ (باسکٹ بال، نیٹ بال، ہینڈ بال)', 'د ټاکلو یرغل او سیمه‌ییزو لوبو په قوانینو، تخنیکونو او تګلارو کې مهارت وښيي (باسکټبال، نېټبال، هېنډبال).')])
    r = rec(b, 7, 1, 74, first=True)
    deco(r, 'A six-photo collage (discus thrower, sprinters, high jumper, table tennis, a badminton racket and shuttlecock, cricket) is decorative.')
    BOOK.save(74, [(7, r)], issues=[{'id': 'hpe12-pdf074', 'unit': 7, 'printedPage': 69,
               'description': 'The page number band reads “69”; a small owner pen mark in the last objective is excluded. Retained as printed.'}])


def p75():
    b = Builder()
    b.h('Target and Field Games', 'ٹارگٹ اینڈ فیلڈ گیمز', 'هدف او میدان لوبې')
    b.h('Long Jump', 'لمبی چھلانگ (Long Jump)', 'اوږد ټوپ (Long Jump)')
    b.h('Rules of the long jump', 'لمبی چھلانگ کے قوانین', 'د اوږد ټوپ قوانین')
    L(b, [('The turn of players will be fixed by drawing lots.', 'کھلاڑیوں کی باری قرعہ اندازی سے مقرر کی جائے گی۔', 'د لوبغاړو وار به په پچه اچولو ټاکل کېږي.'),
          ('If more than eight players take part in the competition, then every player will be given three turns, and the best 8 players will be given 3, 3 more turns. In case of equality at the eighth position the concerned players will be given 3, 3 more attempts.', 'اگر مقابلے میں آٹھ سے زیادہ کھلاڑی شامل ہوں تو ہر کھلاڑی کو تین تین باریاں دی جائیں گی اور 8 بہترین کھلاڑیوں کو مزید 3،3 باریاں دی جائیں گی۔ آٹھویں پوزیشن پر برابری کی صورت میں متعلقہ کھلاڑیوں کو مزید 3،3 کوششیں دی جائیں گی۔', 'که په سیالۍ کې له اتو زیات لوبغاړي شامل وي، هر لوبغاړي ته به درې درې وارونه ورکول کېږي او ۸ غوره لوبغاړو ته به نور ۳، ۳ وارونه ورکول کېږي. په اتم مقام کې د برابرۍ په صورت کې اړوندو لوبغاړو ته به نورې ۳، ۳ هڅې ورکول کېږي.'),
          ('When the competition starts, players will not be allowed to use the runway for practice.', 'جب مقابلہ شروع ہو جائے تو کھلاڑیوں کو مشق کے لیے رن وے استعمال کرنے کی اجازت نہیں ہوگی۔', 'کله چې سیالي پیل شي، لوبغاړو ته به د تمرین لپاره د منډې لارې د کارولو اجازه نه وي.'),
          ('Before the competition starts, 2, 2 turns will be given for practice under the supervision of the judges.', 'مقابلہ شروع ہونے سے پہلے ججوں کی نگرانی میں 2،2 باریاں مشق کیلئے دی جائیں گی۔', 'د سیالۍ له پیل مخکې د قاضیانو تر څارنې لاندې د تمرین لپاره ۲، ۲ وارونه ورکول کېږي.'),
          ('Every player will be given the benefit of the correct attempt.', 'ہر کھلاڑی کو درست کوشش کا فائدہ دیا جائے گا۔', 'هر لوبغاړي ته به د سمې هڅې ګټه ورکول کېږي.'),
          ('Every player will be given a chest number.', 'ہر کھلاڑی کو چسٹ نمبر دیا جائے گا۔', 'هر لوبغاړي ته به د سینې شمېره ورکول کېږي.'),
          ('Every player will jump on his own turn.', 'ہر کھلاڑی اپنی باری پر جمپ کرے گا۔', 'هر لوبغاړی به په خپل وار ټوپ وهي.')])
    b.h('Failures', 'ناکامیاں', 'ناکامۍ')
    L(b, [('If beyond the take-off line there comes the mark of the player’s foot on the sand or plasticine (Plasticine) while running or jumping.', 'اگر اچھلنے والی لکیر سے آگے ریت یا پلاسٹی سین (Plasticine) پر کھلاڑی کے پاؤں کا نشان دوڑتے ہوئے یا چھلانگ لگاتے ہوئے آئے۔', 'که د ټوپ له کرښې هاخوا پر شګه یا پلاستیسین (Plasticine) د منډې یا ټوپ پر مهال د لوبغاړي د پښې نښه راشي.'),
          ('Jumping without one’s turn.', 'اپنی باری کے بغیر جمپ کرنا۔', 'له خپل واره پرته ټوپ وهل.'),
          ('Jumping without the chest number.', 'چسٹ نمبر کے بغیر جمپ کرنا۔', 'د سینې له شمېرې پرته ټوپ وهل.'),
          ('If the player takes off from outside the right or left edge of the take-off board, whether the foot is ahead of or behind the line of the board.', 'اگر کھلاڑی ٹیک آف بورڈ کے دائیں یا بائیں کنارے کے باہر سے ٹیک آف لے خواہ پاؤں بورڈ کی سیدھ سے آگے یا پیچھے ہی رہے۔', 'که لوبغاړی د ټېک اف تختې له ښي یا کیڼ څنډې بهر ټېک اف واخلي، که پښه د تختې له سیدې مخکې یا شا وي.'),
          ('If the player, after completing the jump, walks backwards in the pit.', 'اگر کھلاڑی چھلانگ مکمل کرنے کے بعد اکھاڑے میں پیچھے کو چل دے۔', 'که لوبغاړی له ټوپ بشپړولو وروسته په کنده کې شا ته ولاړ شي.')])
    r = rec(b, 7, 2, 75)
    BOOK.save(75, [(7, r)], issues=[{'id': 'hpe12-pdf075', 'unit': 7, 'printedPage': 70,
               'description': 'Owner English ballpoint writing in the margin (“Plastic … of my nation”) is excluded. Retained as printed.'}])


def p76():
    b = Builder()
    L(b, [('If the player uses any method of somersault (Summer Salt). If the player jumps from behind the take-off board, it will not be considered a failure. The measurement of the jump will be done perpendicularly from the take-off line to the mark that the body or part of the body makes in the pit, which is nearest to the take-off line.', 'اگر کھلاڑی قلابازی (Summer Salt) کا کوئی طریقہ استعمال کرے۔ اگر کھلاڑی ٹیک آف بورڈ سے پیچھے سے اچھلے تو اسے ناکامی نہیں سمجھا جائے گا۔ چھلانگ کی پیمائش ٹیک آف لائن سے لے کر اکھاڑہ میں جسم یا جسم کے کسی حصے سے لگنے والے اس نشان تک عموداً کی جائے گی جو ٹیک آف لائن سے قریب ترین ہوگا۔', 'که لوبغاړی د پلټۍ (Summer Salt) کومه طریقه وکاروي. که لوبغاړی د ټېک اف تختې شا ټوپ ووهي، ناکامي نه ګڼل کېږي. د ټوپ اندازه به له ټېک اف کرښې په کنده کې د بدن یا د بدن د کومې برخې تر هغې نښې عمودي اخیستل کېږي چې ټېک اف کرښې ته تر ټولو نږدې وي.')])
    b.h('Runway', 'رن وے', 'د منډې لاره')
    P(b, [('The minimum length of the runway should be 40 to 45 metres and the breadth 1.22 to 1.25 metres.', 'رن وے کی کم از کم لمبائی 40 تا 45 میٹر چوڑائی 1.22 تا 1.25 میٹر ہونی چاہیے۔', 'د منډې لارې لږ تر لږه اوږدوالی دې ۴۰ تر ۴۵ متره او پلنوالی ۱.۲۲ تر ۱.۲۵ متره وي.')])
    E = dict(pit_len='Length of pit 9 m', pit_w='Width of pit 2.75 m', gap='Pit to take-off board 1 m', board='Take-off board', board_len='Length 1.22 m', board_w='Width of board 20 cm',
             board_t='Thickness of board 10 cm', run_len='Length 40–45 m', run_w='Width 1.22 to 1.25 m')
    U = dict(pit_len='اکھاڑہ کی لمبائی 9 میٹر', pit_w='اکھاڑہ کی چوڑائی 2.75 میٹر', gap='اکھاڑہ سے ٹیک آف بورڈ کا فاصلہ 1 میٹر', board='ٹیک آف بورڈ', board_len='لمبائی 1.22 میٹر',
             board_w='چوڑائی ٹیک آف بورڈ 20 سینٹی میٹر', board_t='موٹائی ٹیک آف بورڈ 10 سینٹی میٹر', run_len='لمبائی 40=45 میٹر', run_w='چوڑائی 1.22 تا 1.25 میٹر')
    S = dict(pit_len='د کندې اوږدوالی ۹ متره', pit_w='د کندې پلنوالی ۲.۷۵ متره', gap='له کندې تر تختې ۱ متر', board='د ټېک اف تخته', board_len='اوږدوالی ۱.۲۲ متره',
             board_w='د تختې پلنوالی ۲۰ سانتي متره', board_t='د تختې پنډوالی ۱۰ سانتي متره', run_len='اوږدوالی ۴۰–۴۵ متره', run_w='پلنوالی ۱.۲۲ تر ۱.۲۵ متره')
    sv = [fig_longjump_runway('Long-jump runway, take-off board and pit', E), fig_longjump_runway('لمبی چھلانگ کا رن وے، ٹیک آف بورڈ اور اکھاڑہ', U),
          fig_longjump_runway('د اوږد ټوپ لاره، تخته او کنده', S)]
    b.visual('hpe12-fig-longjump-runway', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 7, 3, 76)
    BOOK.save(76, [(7, r)], issues=[{'id': 'hpe12-pdf076', 'unit': 7, 'printedPage': 71,
               'description': 'The runway diagram is reproduced as a coded labelled schematic; the printed runway label reads “لمبائی 40=45 میٹر” (for 40–45). “قلابازی (Summer Salt)” (somersault). Line ends cut at the left edge of the first bullet completed from context. Retained as printed.'}])


def p77():
    b = Builder()
    b.h('Mark', 'نشان (Mark)', 'نښه (Mark)')
    P(b, [('The player can put a mark in the path of running only of the type provided by the administration; if they cannot provide it, he can use his own mark. This mark can be put with sticking tape, but not with lime or chalk.', 'کھلاڑی صرف انتظامیہ کا مہیا کردہ نشان دوڑنے کے راستے میں لگا سکتا ہے اگر وہ مہیا نہ کر سکے تو اپنا نشان استعمال کیا جا سکتا ہے۔ یہ نشان چپکنے والے ٹیپ سے لگایا جا سکتا ہے لیکن چونا یا چاک سے نہیں۔', 'لوبغاړی یوازې د ادارې برابره کړې نښه د منډې په لاره کې لګولی شي؛ که دوی یې برابره نه کړي، خپله نښه کارولی شي. دا نښه په نښلونکې ټیپ لګېدای شي، خو په چونې یا چاک نه.')])
    b.h('Take Off Board', 'ٹیک آف بورڈ (Take Off Board)', 'د ټېک اف تخته (Take Off Board)')
    P(b, [('The jump will be made from the board of jumping. This board will be buried in the ground level with the surface of the running path and the pit. The edge of the board which is nearer to the pit is called the “take-off line”. The distance from the board to the pit should not be less than one metre, while the distance from the board to the far edge of the pit should be at least ten metres.', 'اچھلنے کے تختے سے چھلانگ لگائی جائے گی۔ یہ تختہ دوڑنے والے راستے اور اکھاڑے کی سطح کے برابر ہموار زمین میں گاڑھا جائے گا۔ تختہ کے کنارے کو جو اکھاڑے سے قریب تر ہوتا ہے ”ٹیک آف لائن“ کہتے ہیں۔ تختہ سے اکھاڑے تک کا فاصلہ ایک میٹر سے کم نہ ہو۔ جبکہ تختہ سے اکھاڑہ کے آخری کنارہ تک کا درمیانی فاصلہ کم از کم دس میٹر ہو۔', 'ټوپ به د ټوپ له تختې وهل کېږي. دا تخته د منډې لارې او کندې د سطحې سره برابره په هواره ځمکه کې ښخېږي. د تختې هغه څنډې ته چې کندې ته نږدې وي "د ټېک اف کرښه" ویل کېږي. له تختې تر کندې واټن دې له یوه متره کم نه وي، په داسې حال کې چې له تختې د کندې تر وروستۍ څنډې واټن دې لږ تر لږه لس متره وي.')])
    b.h('Landing Area', 'اکھاڑہ (Landing Area)', 'د کېناستو ساحه (Landing Area)')
    P(b, [('Its breadth should be 2.75 metres and length 9 metres. In the pit there should be soft and moist sand whose surface is level with the take-off board.', 'اس کی چوڑائی 2.75 میٹر اور لمبائی 9 میٹر ہونی چاہیے۔ اکھاڑہ میں نرم اور نمدار ریت ہو جس کی سطح ٹیک آف بورڈ کے برابر ہو۔', 'پلنوالی یې ۲.۷۵ متره او اوږدوالی ۹ متره وي. په کنده کې دې نرمه او لنده شګه وي چې سطحه یې د ټېک اف تختې سره برابره وي.')])
    b.h('Strategy', 'حکمت عملی (Strategy)', 'تګلاره (Strategy)')
    P(b, [('To succeed in the long jump the athlete should be physically fit. In it the presence of the three components of fitness, speed, strength and flexibility, is extremely necessary. Besides this, the muscles of the legs and abdomen should be strong and powerful. The four stages of the long jump are as follows.', 'لمبی چھلانگ میں کامیاب ہونے کیلئے اتھلیٹ جسمانی طور پر فٹ ہو۔ اس میں فٹنس کے تین اجزا رفتار، طاقت اور لچک کا ہونا بے حد ضروری ہے۔ اس کے علاوہ ٹانگوں اور پیٹ کے عضلات مضبوط اور طاقتور ہونے چاہئیں۔ لمبی چھلانگ کے چار مراحل درج ذیل ہیں۔', 'په اوږد ټوپ کې د بریالیتوب لپاره ورزشکار باید بدني روغ وي. په کې د فټنس درې برخې — سرعت، ځواک او نرمښت — ډېرې اړینې دي. سربېره پر دې د پښو او ګېډې عضلې دې پیاوړې او ځواکمنې وي. د اوږد ټوپ څلور پړاوونه دا دي.')])
    b.h('Running', 'دوڑ (Running)', 'منډه (Running)')
    P(b, [('The distance of the initial run differs with respect to the age, sex and individual ability of the player. Athletes who quickly attain their full speed need a shorter distance, while other athletes need a longer distance. The run of many athletes of the past and present is from 35 metres to 40 metres.', 'ابتدائی دوڑ کا فاصلہ کھلاڑی کی عمر، جنس اور اس کی انفرادی صلاحیت کے اعتبار سے مختلف ہوتا ہے جو اتھلیٹ جلد ہی اپنی پوری رفتار حاصل کر لیتے ہیں ان کیلئے کم فاصلہ درکار ہے۔ جبکہ دوسرے اتھلیٹ کیلئے لمبے فاصلے کی ضرورت ہوتی ہے۔ ماضی اور حال کے بہت سے اتھلیٹ کی دوڑ 35 میٹر سے 40 میٹر ہوتی ہے۔', 'د پیل منډې واټن د لوبغاړي د عمر، جنس او انفرادي وړتیا له مخې توپیر لري. هغه ورزشکاران چې ژر بشپړ سرعت ته رسېږي، لږ واټن ته اړتیا لري، په داسې حال کې چې نورو ورزشکارانو ته اوږد واټن پکار دی. د تېر او اوسني ډېرو ورزشکارانو منډه له ۳۵ متره تر ۴۰ متره وي.')])
    r = rec(b, 7, 4, 77)
    BOOK.save(77, [(7, r)], issues=[{'id': 'hpe12-pdf077', 'unit': 7, 'printedPage': 72,
               'description': 'Owner ballpoint scribbles beside the landing-area heading are excluded. “اگر وہ مہیا نہ کر سکے”, “گاڑھا جائے گا”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 72
    {72: p72, 73: p73, 74: p74, 75: p75, 76: p76, 77: p77}[n]()
