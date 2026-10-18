"""HPE XII PDF126–131: pp.122–127 — baseball exercise; invasion and territorial games: basketball (court, free-throw lane, court diagram, centre circle,
three-point area, backboard, ring and basket, ball, time; officials; start, points, equipment, dead/live ball, time-out, time-in, 3-second rule).
Run: python class12_hpe_page126.py N (126–131)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T

Q_ = lambda x: (x, x, x)


def p126():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('Choose and write the suitable answers.', 'موزوں جوابات منتخب کر کے لکھیں۔', 'مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('In baseball the in field consists of ________ bases.', 'بیس بال میں ان فیلڈ ________ بیسوں پر مشتمل ہوتی ہے۔', 'په بېس بال کې داخلي میدان له ________ بېسونو جوړ وي.'), [Q_('2'), Q_('3'), Q_('1'), Q_('4')]),
         (('In a baseball team there are in all ________ players.', 'بیس بال ٹیم میں کل ________ کھلاڑی ہوتے ہیں۔', 'د بېس بال په ټیم کې ټول ________ لوبغاړي وي.'), [Q_('6'), Q_('12'), Q_('9'), Q_('11')]),
         (('In baseball, when the umpire starts the game, he calls ________ .', 'بیس بال میں امپائر کھیل شروع کرتا ہے تو ________ پکارتا ہے۔', 'په بېس بال کې کله چې امپایر لوبه پیلوي، ________ وايي.'), [('Play', 'Play (پلے)', 'Play (لوبه)'), ('Time', 'Time (ٹائم)', 'Time (وخت)'), ('Top', 'Top (ٹاپ)', 'Top (سر)'), ('Balk', 'Balk (باک)', 'Balk (باک)')]),
         (('In baseball fielding there will be ________ players of one team.', 'بیس بال فیلڈنگ میں ایک ٹیم کے ________ کھلاڑی ہوں گے۔', 'د بېس بال په فیلډنګ کې به د یوه ټیم ________ لوبغاړي وي.'), [Q_('6'), Q_('7'), Q_('8'), Q_('9')]),
         (('The field of the game of baseball consists of ________ parts.', 'بیس بال کھیل کا میدان ________ حصوں پر مشتمل ہوتا ہے۔', 'د بېس بال د لوبې میدان له ________ برخو جوړ وي.'), [Q_('2'), Q_('3'), Q_('4'), Q_('6')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['i', 'ii', 'iii', 'iv', 'v'][i], q, o, per_line=4)
    e.p('Write the answers to the following questions.', 'درج ذیل سوالات کے جوابات لکھیں۔', 'د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. In baseball, when will the batter and runners be counted out?', 'i۔ بیس بال میں بیٹر اور رنرز کس وقت آؤٹ شمار ہوگا؟', 'i. په بېس بال کې بیټر او منډه وهونکي کله اوټ ګڼل کېږي؟'),
                      ('ii. Explain the scoring system in baseball.', 'ii۔ بیس بال میں سکورنگ سسٹم کی وضاحت کریں۔', 'ii. په بېس بال کې د نمرو سیستم روښانه کړئ.'),
                      ('iii. Define a Balk in baseball. In which cases is a Balk given?', 'iii۔ بیس بال میں Balk کی تعریف کریں۔ کن صورتوں میں Balk دیا جاتا ہے۔', 'iii. په بېس بال کې Balk تعریف کړئ. په کومو حالتونو کې Balk ورکول کېږي؟')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-baseball', 'Chapter 7 exercise: baseball', 'باب ۷: مشقی سوالات — بیس بال', '۷ څپرکی: تمریني پوښتنې — بېس بال', 126, [122])
    BOOK.save(126, [(7, r)], issues=[{'id': 'hpe12-pdf126', 'unit': 7, 'printedPage': 122, 'description': 'Owner ballpoint ticks are excluded. The right edge of the scan cuts the question numerals (“i”, “ii” …). Retained as printed.'}])


def bb_court(cap):
    b = ('<rect x="20" y="20" width="560" height="300" fill="#9f1239" stroke="#fff" stroke-width="3"/><line x1="300" y1="20" x2="300" y2="320" stroke="#fff" stroke-width="2"/>'
         '<circle cx="300" cy="170" r="36" fill="none" stroke="#fff" stroke-width="2"/>'
         '<rect x="20" y="120" width="116" height="100" fill="none" stroke="#fff" stroke-width="2"/><rect x="464" y="120" width="116" height="100" fill="none" stroke="#fff" stroke-width="2"/>'
         '<path d="M136 120 A50 50 0 0 1 136 220" fill="none" stroke="#fff" stroke-width="2"/><path d="M464 120 A50 50 0 0 0 464 220" fill="none" stroke="#fff" stroke-width="2"/>'
         '<path d="M20 38 L58 38 A140 140 0 0 1 58 302 L20 302" fill="none" stroke="#fff" stroke-width="2"/><path d="M580 38 L542 38 A140 140 0 0 0 542 302 L580 302" fill="none" stroke="#fff" stroke-width="2"/>'
         '<circle cx="48" cy="170" r="8" fill="none" stroke="#fff" stroke-width="2"/><circle cx="552" cy="170" r="8" fill="none" stroke="#fff" stroke-width="2"/>')
    for t, x, y in [('Side line 28m', 300, 340), ('Center line', 300, 300), ('1.80m', 300, 175), ('5.8m', 80, 240), ('4.20m', 100, 300), ('4.9m', 150, 170), ('0.9m', 60, 32), ('1.575m', 20, 112),
                    ('Basket ring', 520, 110), ('Restricted area', 520, 235), ('End line 15m', 595, 170), ('no charge semi circle area', 100, 60), ('5.05m', 10, 80), ('5.05m', 10, 270), ('0.375m', 70, 205), ('1.2m', 40, 190), ('1.8m', 470, 170)]:
        b += T(x, y, t, 10, 'bold', 'middle', '#ffffff' if 20 < x < 580 and 20 < y < 320 else '#1e293b')
    return svg(620, 360, b, cap)


def p127():
    b = Builder()
    b.h('Invasion and Territorial Games', 'ان ویژن اینڈ ٹیری ٹوریل گیمز', 'یرغل او سیمه‌ییزې لوبې')
    b.h('Basketball', 'باسکٹ بال', 'باسکټبال')
    b.h('Court', 'کورٹ', 'میدان')
    P(b, [('The surface of the court is level, hard and free from every kind of obstruction. The length of the court is 28 metres and breadth 15 metres. A line in the middle divides the court into two equal parts. This is called the centre line. The breadth of all the lines of the court is 5 centimetres.', 'کورٹ کی سطح ہموار، سخت اور ہر قسم کی رکاوٹوں سے پاک ہوتی ہے۔ کورٹ کی لمبائی 28 میٹر اور چوڑائی 15 میٹر ہوتی ہے۔ درمیان سے ایک لائن کورٹ کو دو برابر حصوں میں تقسیم کرتی ہے۔ اسے سنٹر لائن کہتے ہیں۔ کورٹ کی تمام لائنوں کی چوڑائی 5 سینٹی میٹر ہوتی ہے۔', 'د میدان سطحه هواره، کلکه او له هر ډول خنډ پاکه وي. د میدان اوږدوالی ۲۸ متره او پلنوالی ۱۵ متره وي. په منځ کې یوه کرښه میدان په دوو برابرو برخو وېشي. دې ته منځنۍ کرښه ویل کېږي. د میدان د ټولو کرښو پلنوالی ۵ سانتي متره وي.')])
    b.h('Free-throw line and restricted area', 'فری تھرو لائن اور محدود علاقہ', 'د وړیا غورځولو کرښه او محدوده سیمه')
    P(b, [('On both sides of the court, from the middle of the end line towards the court at a distance of 5.80 metres, a 4-metre-long line is drawn; it is called the free-throw line. On both sides of the court, from the middle of the end line, two marks are put on the right and left sides at a distance of 2 metres. The distance between these two marks will be 4 metres. These marks are joined with the ends of the free-throw line. This area is called the restricted area.', 'کورٹ کے دونوں طرف اینڈ لائن کے وسط سے کورٹ کی جانب 5.80 میٹر کے فاصلے پر 4 میٹر لمبی لائن لگائی جاتی ہے اسے فری تھرو لائن کہتے ہیں۔ کورٹ کے دونوں طرف اینڈ لائن کے وسط سے دائیں اور بائیں دونوں جانب 2 میٹر کے فاصلے پر دو نشان لگائے جاتے ہیں۔ ان دونوں نشانوں کا درمیانی فاصلہ 4 میٹر ہوگا۔ ان نشانات کو فری تھرو لائن کے سروں سے ملا دیا جاتا ہے۔ یہ علاقہ ممنوعہ علاقہ کہلاتا ہے۔', 'د میدان په دواړو خواوو کې د پای کرښې له منځه میدان ته په ۵.۸۰ متره واټن ۴ متره اوږده کرښه کښل کېږي چې د وړیا غورځولو کرښه ورته ویل کېږي. د میدان په دواړو خواوو کې د پای کرښې له منځه ښي او کیڼ لوري ته په ۲ متره واټن دوه نښې لګول کېږي. د دې دوو نښو ترمنځ واټن ۴ متره وي. دا نښې د وړیا غورځولو د کرښې له سرونو سره نښلول کېږي. دې سیمې ته منع شوې سیمه ویل کېږي.')])
    sv = [bb_court(c) for c in ('Basketball court (labels as printed)', 'باسکٹ بال کورٹ', 'د باسکټبال میدان')]
    b.visual('hpe12-fig-basketball-court', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 7, 46, 127)
    BOOK.save(127, [(7, r)], issues=[{'id': 'hpe12-pdf127', 'unit': 7, 'printedPage': 123,
               'description': 'The court photograph-diagram is reproduced as a coded schematic with its printed English labels; it labels the free-throw distance 5.8 m and the lane 4.9 m, while the text gives a 4 m lane width. Retained as printed.'}])


def p128():
    b = Builder()
    b.h('Centre circle', 'مرکزی دائرہ', 'منځنۍ دایره')
    P(b, [('This is a circle of 1.80 metres radius in the middle of the court.', 'یہ کورٹ کے درمیان میں 1.80 میٹر نصف قطر کا دائرہ ہوتا ہے۔', 'دا د میدان په منځ کې د ۱.۸۰ مترو نیم قطر دایره ده.')])
    b.h('Three-point area', 'تھری پوائنٹ ایریا', 'د درې نمرو سیمه')
    P(b, [('This area is outside the circle of 6.25 metres. If the ball is shot from outside this circle and is basketed correctly, three points are given, and if it is shot from inside this circle and is basketed correctly, two points are given, while for every successful free throw one point is given.', 'یہ علاقہ 6.25 میٹر کے سرکل کے باہر ہوتا ہے۔ اس سرکل کے باہر سے بال شوٹ کیا گیا ہو اور درست طریقے سے باسکٹ ہوا ہو تو تین پوائنٹ دیئے جاتے ہیں اور اگر اس سرکل کے اندر سے شوٹ کیا گیا ہو اور درست طریقے سے باسکٹ ہوا ہو تو دو پوائنٹ دیئے جاتے ہیں جبکہ ہر کامیاب فری تھرو پر ایک پوائنٹ دیا جاتا ہے۔', 'دا سیمه د ۶.۲۵ مترو له دایرې بهر ده. که له دې دایرې بهر توپ وویشتل شي او په سمه توګه باسکټ ته ولوېږي، درې نمرې ورکول کېږي او که له دې دایرې دننه وویشتل شي او سم باسکټ شي، دوه نمرې ورکول کېږي، په داسې حال کې چې په هره بریالۍ وړیا غورځونه یوه نمره ورکول کېږي.')])
    b.h('Backboard', 'بیک بورڈ', 'شاتنۍ تخته')
    P(b, [('The length of the backboard will be 1.80 metres, breadth 1.05 metres and thickness 3 centimetres. A rectangle is made on the backboard. Its length is 59 centimetres and breadth 45 centimetres. The distance from the floor to the lower end of the board is 2.90 metres. The pole will be at least one metre outside the end line, and 1.20 metres ahead of the end line (towards the court).', 'بیک بورڈ کی لمبائی 1.80 میٹر، چوڑائی 1.05 میٹر اور موٹائی 3 سینٹی میٹر ہوگی۔ بیک بورڈ پر ایک مستطیل بنائی جاتی ہے۔ اس کی لمبائی 59 سینٹی میٹر اور چوڑائی 45 سینٹی میٹر ہوتی ہے۔ فرش اور بورڈ کے نچلے سرے تک کا فاصلہ 2.90 میٹر ہوتا ہے۔ پول اینڈ لائن سے کم از کم ایک میٹر باہر ہوگا اور اینڈ لائن سے آگے 1.20 میٹر (کورٹ کی جانب) ہوگا۔', 'د شاتنۍ تختې اوږدوالی به ۱.۸۰ متره، پلنوالی ۱.۰۵ متره او پنډوالی ۳ سانتي متره وي. پر شاتنۍ تخته یو مستطیل جوړېږي. اوږدوالی یې ۵۹ سانتي متره او پلنوالی ۴۵ سانتي متره وي. له فرش تر تختې ښکتني سر واټن ۲.۹۰ متره وي. پول به له پای کرښې لږ تر لږه یو متر بهر او له پای کرښې ۱.۲۰ متره مخکې (میدان ته) وي.')])
    b.h('Ring and basket', 'رنگ اور باسکٹ', 'کړۍ او باسکټ')
    P(b, [('In the exact middle of the line of the lower end of the rectangle of the backboard a ring is fixed firmly. With this ring a basket made of thread is also fixed. The diameter of the ring is 45 centimetres (16 inches).', 'بیک بورڈ کی مستطیل کے نچلے سرے کی لکیر کے عین وسط میں ایک رنگ مضبوطی سے لگائی جاتی ہے۔ اسی رنگ کے ساتھ دھاگے سے بنی ہوئی باسکٹ بھی لگائی جاتی ہے۔ رنگ کا قطر 45 سینٹی میٹر (16 انچ) ہوتا ہے۔', 'د شاتنۍ تختې د مستطیل د ښکتني سر د کرښې په سم منځ کې یوه کړۍ کلکه لګول کېږي. له همدې کړۍ سره له تار جوړ باسکټ هم لګول کېږي. د کړۍ قطر ۴۵ سانتي متره (۱۶ انچه) وي.')])
    b.h('Ball', 'بال', 'توپ')
    P(b, [('The ball will be made of leather or rubber. Its weight will be 567 grams to 650 grams. The circumference is 74 to 78 centimetres.', 'بال چمڑے یا ربڑ کا بنا ہوگا۔ اس کا وزن 567 گرام تا 650 گرام ہوگا۔ محیط 74 سے 78 سینٹی میٹر ہوتا ہے۔', 'توپ به له څرمن یا رابړ جوړ وي. وزن به یې له ۵۶۷ تر ۶۵۰ ګرامه وي. محیط یې له ۷۴ تر ۷۸ سانتي متره وي.')])
    b.h('Time of the game', 'کھیل کا وقت', 'د لوبې وخت')
    P(b, [('The time of the game consists of four quarters of 10, 10 minutes. After the first quarter an interval of 2 minutes will be given. After half time an interval of 5 minutes will be given. At the end of the match time, if the score is equal, an extra five minutes will be given.', 'کھیل کا وقت 10،10 منٹ کے چار کوارٹر پر مشتمل ہوتا ہے۔ پہلے کوارٹر کے بعد 2 منٹ کا وقفہ دیا جائے گا۔ نصف وقت کے بعد 5 منٹ کا وقفہ دیا جائے گا۔ میچ کا وقت ختم ہونے پر اگر سکور برابر ہو تو اضافی پانچ منٹ دیے جائیں گے۔', 'د لوبې وخت د ۱۰، ۱۰ دقیقو له څلورو ربعو جوړ وي. له لومړۍ ربعې وروسته ۲ دقیقې وقفه ورکول کېږي. له نیم وخت وروسته ۵ دقیقې وقفه ورکول کېږي. د لوبې د وخت په پای کې که نمرې برابرې وي، اضافي پنځه دقیقې ورکول کېږي.')])
    r = rec(b, 7, 47, 128)
    BOOK.save(128, [(7, r)], issues=[{'id': 'hpe12-pdf128', 'unit': 7, 'printedPage': 124,
               'description': 'Owner ballpoint doodles in the middle of the page are excluded. Ring diameter “45 سینٹی میٹر (16 انچ)” and the half-time interval “5 منٹ” are retained as printed.'}])


def p129():
    b = Builder()
    b.h('Officials and their duties', 'عہدیداران اور ان کے فرائض', 'چارواکي او دندې یې')
    b.h('Referee', 'ریفری', 'ریفري')
    L(b, [('The referee will inspect all the equipment.', 'ریفری تمام سامان کا معائنہ کرے گا۔', 'ریفري به ټول سامان معاینه کوي.'), ('He will be responsible for implementing the rules of the game from beginning to end.', 'کھیل کے قوانین پر شروع سے آخر تک عمل درآمد کرنے کا ذمہ دار ہوگا۔', 'له پیله تر پایه به د لوبې د قوانینو د پلي کولو مسؤل وي.'),
          ('He will start the game.', 'کھیل کا آغاز کرے گا۔', 'لوبه به پیلوي.'), ('He will decide those matters on which the umpire and scorer do not agree.', 'جن معاملات پر امپائر اور سکورر متفق نہ ہوں تو ان کا فیصلہ دے گا۔', 'په هغو چارو چې امپایر او نمره لیکونکی پرې موافق نه وي، پرېکړه به کوي.')])
    b.h('Umpire', 'امپائر', 'امپایر')
    P(b, [('He is responsible for the ball being counted in play, the ball being dead, imposing penalties, ordering time-out, permitting substitute players, giving free throws, causing a jump ball, telling the scorer the number of the player on a foul, and deciding all other legal points.', 'بال کے کھیل میں شمار ہونے، بال مردہ ہونے، سزا لاگو کرنے، ٹائم آؤٹ کا حکم دینے متبادل کھلاڑی کی اجازت دینے، فری تھرو دینے، جمپ بال کرانے، فاؤل پر سکورر کو کھلاڑی کا نمبر بتانے اور دیگر تمام قانونی نقاط کا فیصلہ کرنے کا ذمہ دار ہوتا ہے۔', 'د توپ په لوبه کې د شمېرلو، د توپ د مړ کېدو، سزا پلي کولو، د ټایم اوټ حکم ورکولو، د بدیل لوبغاړي اجازه ورکولو، وړیا غورځونې ورکولو، جمپ بال کولو، په خطا کې نمره لیکونکي ته د لوبغاړي شمېره ویلو او نورو ټولو قانوني ټکو د پرېکړې مسؤل وي.')])
    b.h('Scorer', 'سکورر', 'نمره لیکونکی')
    P(b, [('The scorer is responsible for keeping account of the points, recording the account of personal and technical fouls, informing the referee on the 5 fouls of a player, signalling time-out, and keeping the record of the names and numbers of every player and of substitute players.', 'سکورر پوائنٹس کا حساب رکھنے، پرسنل اور ٹیکنیکل فاؤل کا حساب واندراج کرنے، کھلاڑی کے 5 فاؤلز ہونے پر ریفری کو بتانے، ٹائم آؤٹ کا اشارہ کرنے، ہر کھلاڑی کے ناموں اور نمبروں کا ریکارڈ رکھنے اور متبادل کھلاڑیوں کا ریکارڈ رکھنے کا ذمہ دار ہوتا ہے۔', 'نمره لیکونکی د نمرو د حساب ساتلو، د شخصي او تخنیکي خطاګانو د ثبتولو، د لوبغاړي په ۵ خطاګانو ریفري ته د ویلو، د ټایم اوټ اشارې، د هر لوبغاړي د نومونو او شمېرو او د بدیلو لوبغاړو د ریکارډ ساتلو مسؤل وي.')])
    b.h('Time keeper', 'ٹائم کیپر', 'وخت ساتونکی')
    P(b, [('Counting the time of the game and the time of the stopping of the game, running the time-out clock, informing at the end of every half or extra time by ringing the bell.', 'کھیل کے وقت کا، کھیل رکنے کے وقت کا شمار کرنا، ٹائم آؤٹ کی گھڑی چالو کرنا، ہر آدھے وقت یا زائد وقت کے اختتام کی گھنٹی بجا کر اطلاع کرنا۔', 'د لوبې د وخت او د لوبې د درېدو د وخت شمېرل، د ټایم اوټ ساعت چالانول، د هر نیم وخت یا اضافي وخت په پای کې د زنګ په وهلو خبرول.')])
    r = rec(b, 7, 48, 129)
    BOOK.save(129, [(7, r)])


def p130():
    b = Builder()
    b.h('Start of the game', 'کھیل کی ابتداء', 'د لوبې پیل')
    P(b, [('The referee will start the game through a jump ball from the central circle. At the time of the jump ball the remaining players will remain outside the circle.', 'کھیل کا آغاز ریفری وسطی دائرہ سے جمپ بال کے ذریعے کرائے گا۔ جمپ بال کے وقت باقی کھلاڑی دائرہ سے باہر رہیں گے۔', 'ریفري به لوبه له منځنۍ دایرې په جمپ بال پیلوي. د جمپ بال پر وخت پاتې لوبغاړي به له دایرې بهر وي.')])
    b.h('Point', 'پوائنٹ', 'نمره')
    P(b, [('When the ball thrown by some player enters the basket from above and comes down through the net, and during this no foul has been committed, then a point will be given. On basketing the ball from inside the three-point area 2, while on basketing the ball from outside the circle 3 points, and on a free throw one point will be given.', 'جب کسی کھلاڑی کا پھینکا ہوا بال باسکٹ میں اوپر سے داخل ہو اور جالی سے نیچے آئے اور اس دوران کوئی فاؤل سرزد نہ ہوا ہو تو پوائنٹ دیا جائے گا۔ تھری پوائنٹ ایریا کے اندر سے بال باسکٹ کرنے پر 2 جبکہ سرکل کے باہر سے بال باسکٹ کرنے پر 3 پوائنٹ اور فری تھرو پر ایک پوائنٹ دیا جائے گا۔', 'کله چې د کوم لوبغاړي غورځول شوی توپ له پاسه باسکټ ته ننوځي او له جالۍ ښکته راشي او په دې وخت کې کومه خطا نه وي شوې، نمره ورکول کېږي. د درې نمرو له سیمې دننه د باسکټ کولو په صورت ۲، له دایرې بهر د باسکټ په صورت ۳ نمرې او په وړیا غورځونه یوه نمره ورکول کېږي.')])
    b.h('Necessary equipment for the match', 'میچ کیلئے ضروری سامان', 'د لوبې لپاره اړین سامان')
    P(b, [('Stopwatch, score sheet, score board, time-out clock, a card for signalling 5 fouls, a card for signalling 7 fouls.', 'سٹاپ واچ، سکور شیٹ، سکور بورڈ، ٹائم آؤٹ کی گھڑی، 5 فاؤلز کے اشارہ کا کارڈ، 7 فاؤلز کے اشارہ کا کارڈ۔', 'سټاپ‌واچ، د نمرو پاڼه، د نمرو تخته، د ټایم اوټ ساعت، د ۵ خطاګانو د اشارې کارت، د ۷ خطاګانو د اشارې کارت.')])
    b.h('Dead ball', 'مردہ بال', 'مړ توپ')
    L(b, [('When there is a point or some breach of law has occurred.', 'جب پوائنٹ ہو یا کوئی قانون شکنی واقع ہو۔', 'کله چې نمره وي یا کومه قانون ماتونه شوې وي.'), ('When the whistle blows at the time of a live ball.', 'زندہ بال کے وقت جب سیٹی بجے۔', 'د ژوندي توپ پر وخت چې شپېلۍ وغږېږي.'),
          ('When the ball is held (held).', 'بال ہیلڈ (held) ہو۔', 'توپ ونیول شي (held).'), ('When half the time or the extra time ends.', 'وقت کا آدھا حصہ یا زائد وقت ختم ہو جائے۔', 'کله چې نیم وخت یا اضافي وخت پای ته ورسېږي.'), ('When there is the signal of 24 seconds.', 'جب 24 سیکنڈ کا اشارہ ہو۔', 'کله چې د ۲۴ ثانیو اشاره وي.')])
    b.h('Live ball', 'زندہ بال', 'ژوندی توپ')
    L(b, [('When the ball reaches its height at the time of the jump ball.', 'بال جب جمپ بال کے وقت بلندی کو پہنچے۔', 'کله چې توپ د جمپ بال پر وخت لوړوالي ته ورسېږي.'), ('When the umpire gives the ball to the player for the free throw.', 'جب امپائر فری تھرو کیلئے بال کھلاڑی کو دے۔', 'کله چې امپایر د وړیا غورځونې لپاره توپ لوبغاړي ته ورکړي.'),
          ('When the ball of the throw-in touches a player inside the court.', 'تھرو ان کا بال کورٹ کے اندر کھلاڑی کو چھو لے۔', 'کله چې د تھرو ان توپ د میدان دننه لوبغاړی ولمسوي.')])
    r = rec(b, 7, 49, 130)
    deco(r, 'Photographs of a basketball shoe, a portable basketball stand and a ball are decorative.')
    BOOK.save(130, [(7, r)], issues=[{'id': 'hpe12-pdf130', 'unit': 7, 'printedPage': 126,
               'description': 'The point rule credits 2 points for a basket from inside the three-point area and 3 points from outside “the circle”. Retained as printed.'}])


def p131():
    b = Builder()
    b.h('Time out', 'ٹائم آؤٹ', 'ټایم اوټ')
    P(b, [('When the officials stop the game for the following reasons:', 'جب عہدیدار درج ذیل وجوہات کی بنا پر کھیل کو روک دے:', 'کله چې چارواکي د لاندې لاملونو له امله لوبه ودروي:')])
    L(b, [('On some breach of the rules.', 'کسی ضابطہ شکنی پر۔', 'د کومې قاعدې په ماتولو.'), ('On the sounding of the 24-second signal.', '24 سیکنڈ کا اشارہ بجنے پر۔', 'د ۲۴ ثانیو د اشارې په غږېدو.'), ('On a player being injured.', 'کھلاڑی کے چوٹ آنے پر۔', 'د لوبغاړي په ټپي کېدو.')])
    b.h('Time in: time-in happens when', 'ٹائم ان: ٹائم ان تب ہوتا ہے جب!', 'ټایم ان: ټایم ان هغه وخت کېږي چې')
    L(b, [('there is time-in.', 'ٹائم ان ہوتا ہے۔', 'ټایم ان وي.'), ('there is a jump ball.', 'جب جمپ بال ہو۔', 'جمپ بال وي.'), ('after a time-out, when the game starts again.', 'ٹائم آؤٹ کے بعد جب کھیل دوبارہ شروع ہو۔', 'له ټایم اوټ وروسته چې لوبه بیا پیل شي.'),
          ('a free throw fails and play continues.', 'فری تھرو ناکام ہو اور کھیل جاری رہے۔', 'وړیا غورځونه ناکامه شي او لوبه دوام وکړي.'), ('with the throw-in ball.', 'تھرو ان کے بال کے ساتھ۔', 'له تھرو ان توپ سره.')])
    b.h('Time-out obtained (charged)', 'حاصل کردہ ٹائم آؤٹ', 'ترلاسه شوی ټایم اوټ')
    P(b, [('In every half of the game two time-outs are given to one team. For every extra time one time-out is given. The duration of a time-out is 30 seconds.', 'کھیل کے ہر آدھے حصے میں دو ٹائم آؤٹ ایک ٹیم کو دیئے جاتے ہیں۔ ہر زائد وقت کیلئے ایک ٹائم آؤٹ ہوتا ہے۔ ٹائم آؤٹ کا دورانیہ 30 سیکنڈ ہوتا ہے۔', 'د لوبې په هره نیمه برخه کې یوه ټیم ته دوه ټایم اوټه ورکول کېږي. د هر اضافي وخت لپاره یو ټایم اوټ وي. د ټایم اوټ موده ۳۰ ثانیې وي.')])
    b.h('Time-out taken', 'حاصل شدہ ٹائم آؤٹ', 'اخیستل شوی ټایم اوټ')
    P(b, [('When necessary the coach takes a time-out. A time-out is given on a dead ball.', 'جب ضروری ہو تو کوچ ٹائم آؤٹ لیتا ہے۔ مردہ بال پر ٹائم آؤٹ دیا جاتا ہے۔', 'کله چې اړتیا وي، روزونکی ټایم اوټ اخلي. ټایم اوټ په مړ توپ ورکول کېږي.')])
    b.h('The 3-second rule', '3 سیکنڈ کا قانون', 'د ۳ ثانیو قانون')
    P(b, [('When the ball is in the possession of some team, no other player of it can remain in the restricted area of the opposing team for more than 3 seconds. If he does so, the 3-second law will apply against him and the throw will be given to the opposing side.', 'جس وقت بال کسی ٹیم کے قبضے میں ہو تو اس کا کوئی دوسرا کھلاڑی مخالف ٹیم کے ممنوعہ علاقہ میں 3 سیکنڈ سے زیادہ نہیں رہ سکتا۔ اگر وہ ایسا کرے گا تو اس کے خلاف تین سیکنڈ کا قانون لاگو ہوگا اور مخالف کو سائیڈ تھرو دی جائے گی۔', 'کله چې توپ د کوم ټیم په واک کې وي، د هغه بل لوبغاړی د مخالف ټیم په منع شوې سیمه کې له ۳ ثانیو زیات نه شي پاتې کېدای. که داسې وکړي، د ۳ ثانیو قانون به یې پر وړاندې پلي کېږي او مخالف ته به د څنګ غورځونه ورکول کېږي.')])
    r = rec(b, 7, 50, 131)
    BOOK.save(131, [(7, r)], issues=[{'id': 'hpe12-pdf131', 'unit': 7, 'printedPage': 127,
               'description': 'An owner Urdu note at the top (“24 سیکنڈ …”) is excluded. The “time in” list opens with “ٹائم ان ہوتا ہے” (circular). Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 126
    {126: p126, 127: p127, 128: p128, 129: p129, 130: p130, 131: p131}[n]()
