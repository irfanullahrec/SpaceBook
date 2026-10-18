"""HPE XII PDF96–101: pp.91–96 — discus fouls (end), discus skills, result sheet; 1500 m race (rules, fouls); discus/1500 m exercise;
net and wall games — badminton court (measurements, court diagram). Run: python class12_hpe_page096.py N (96–101)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T


def p96():
    b = Builder()
    L(b, [('Going out from the front of the circle after throwing.', 'پھینکنے کے بعد دائرہ کے آگے سے نکلنا۔', 'له غورځولو وروسته د دایرې له مخې وتل.'),
          ('Leaving the circle before the discus falls on the ground.', 'ڈسکس کے زمین پر گرنے سے پہلے دائرہ کو چھوڑ دینا۔', 'د ډیسکس پر ځمکه له لوېدو مخکې دایره پرېښودل.'),
          ('Using any such thing as helps in throwing.', 'کوئی ایسی چیز استعمال کرنا جس سے پھینکنے میں مدد ملتی ہو۔', 'داسې شی کارول چې په غورځولو کې مرسته کوي.')])
    b.h('Skills of the discus throw', 'ڈسکس تھرو کی مہارتیں', 'د ډیسکس غورځولو مهارتونه')
    b.h('Grip', 'گرفت', 'نیول')
    P(b, [('There are two ways of holding the discus.', 'ڈسکس کو پکڑنے کے دو طریقے ہیں۔', 'د ډیسکس د نیولو دوه طریقې دي.')])
    L(b, [('Holding with the fingers spread as usual.', 'معمول کے مطابق انگلیاں پھیلا کر پکڑنا۔', 'د معمول سره سم ګوتې خورې کړئ او ونیسئ.'), ('Holding with the index and middle finger joined.', 'شہادت اور درمیانی انگلی ملا کر پکڑنا۔', 'د شهادت او منځنۍ ګوتې یوځای کولو سره نیول.')])
    b.h('Starting position', 'سٹارٹنگ پوزیشن', 'د پیل حالت')
    L(b, [('Standing in the circle opposite to the direction of throwing.', 'دائرہ میں پھینکنے کی سمت کے مخالف کھڑا ہونا۔', 'په دایره کې د غورځولو د لوري مخالف ودرېدل.'), ('Before swinging the discus, the weight of the body should be equally on both legs.', 'ڈسکس جھلانے سے پہلے جسم کا وزن برابر دونوں ٹانگوں پر ہو۔', 'د ډیسکس له زنګولو مخکې دې د بدن وزن پر دواړو پښو برابر وي.')])
    b.h('Swinging', 'جھلانا', 'زنګول')
    P(b, [('Creating motion in the stationary state, creating rotation in the shoulder and hip, swinging once or twice.', 'ساکن حالت میں حرکت پیدا کرنا کندھے اور کولہے میں گھماؤ پیدا کرنا، ایک یا دو بار جھلانا۔', 'په ولاړ حالت کې حرکت پیدا کول، په اوږه او کوناټي کې تاو پیدا کول، یو یا دوه ځله زنګول.')])
    b.h('Turning', 'مڑنا', 'تاوېدل')
    P(b, [('Turning from both feet onto one foot, bending the body somewhat and lifting it along with the turning. Spreading the arms and keeping balance.', 'دونوں پاؤں سے ایک پاؤں پر آ کر مڑنا، جسم قدرے جھکانا اور مڑنے کے ساتھ ہی اٹھانا۔ بازوؤں کو پھیلانا اور توازن قائم رکھنا۔', 'له دواړو پښو پر یوه پښه راتلل او تاوېدل، بدن لږ کږول او له تاوېدو سره پورته کول. مټې غځول او توازن ساتل.')])
    r = rec(b, 7, 20, 96)
    BOOK.save(96, [(7, r)], issues=[{'id': 'hpe12-pdf096', 'unit': 7, 'printedPage': 91, 'description': 'A vertical crease down the page is legible. Retained as printed.'}])


def p97():
    b = Builder()
    P(b, [('Planting the left foot on the ground. Keeping balance; both arms should be in the air. Releasing the discus from the hands, keeping balance so that one does not go out of the circle.', 'بائیں پاؤں کو زمین پر جما کر رکھنا۔ توازن قائم رکھنا دونوں بازو ہوا میں ہوں۔ ڈسکس کو اپنے ہاتھوں سے نکالنا توازن برقرار رکھنا تاکہ دائرہ سے باہر نہ نکلے۔', 'کیڼه پښه پر ځمکه ټینګه ساتل. توازن ساتل؛ دواړه مټې دې په هوا کې وي. ډیسکس له لاسونو خوشې کول او توازن ساتل ترڅو له دایرې بهر ونه وځي.')])
    b.h('Result/score sheet for 6 players', '6 کھلاڑیوں کیلئے رزلٹ / سکور شیٹ', 'د ۶ لوبغاړو لپاره د پایلو / نمرو پاڼه')
    H = ['Sr. No', 'I', 'II', 'III', 'IV', 'V', 'VI', 'Position']
    rows = [['A', '40.2', '×', '×', '×', '45.6', '44.7', '3rd'], ['B', '×', '46.4', '×', '×', '×', '×', 'Ist'], ['C', '38.4', '40.2', '40.4', '41.6', '×', '×', ''],
            ['D', '42.1', '42.7', '40.6', '43.7', '43.2', '41.9', ''], ['E', '38.6', '41.4', '42.0', '×', '46.2', '×', '2nd'], ['F', '×', '44.2', '×', '43.7', '45.2', '44.5', '']]
    b.table('hpe12-discus-result', H, rows, H, H, rows, rows)
    b.group('lines', [('Signature of judges: Judge No. 1 — Judge No. 2 — Judge No. 3', 'جج کے دستخط: جج نمبر 1 — جج نمبر 2 — جج نمبر 3', 'د قاضیانو لاسلیک: قاضي ۱ — قاضي ۲ — قاضي ۳')])
    r = rec(b, 7, 21, 97)
    deco(r, 'A six-frame drawing of a discus thrower turning in the circle is decorative.')
    BOOK.save(97, [(7, r)], issues=[{'id': 'hpe12-pdf097', 'unit': 7, 'printedPage': 92,
               'description': 'The sample score sheet is printed in English and reproduced as a structured table as printed: B (best throw 46.4) is “Ist”, E (46.2) “2nd” and A (45.6) “3rd”, while F (45.2) and D are unplaced; “Ist” is retained. The heading above the first line (“ڈسکس پھینکنا”) is faint at the top of the scan.'}])


def p98():
    b = Builder()
    b.h('1500-metre race', '1500 میٹر دوڑ', 'د ۱۵۰۰ مترو منډه')
    P(b, [('In the 1500-metre race every player covers the distance of 3 complete laps and one incomplete lap of 300 metres on the 400-metre standard track. The first lap will be the incomplete one of 300 metres and then three more complete laps of 400 metres. For the 300-metre incomplete lap, 100 metres are reduced from 400 metres and the starting point is put at that place. This starting line is drawn in the shape of a curve (Curve). Its method is that at the start of the second bend, where steps are given from 200 metres, there, at a distance of 8 inches from the inner line of the first lane, keeping the centre, an arc is drawn in 8 lanes at a distance of 100 metres backwards; this arc will be the starting line of the 1500-metre race. Instead of taking a start, the whole foot is used. The 1500-metre race starts from the international curve (Curve).',
           '1500 میٹر دوڑ میں ہر کھلاڑی 400 میٹر سٹینڈرڈ ٹریک پر 3 مکمل چکر اور ایک 300 میٹر کے نامکمل چکر کا فاصلہ طے کرتا ہے۔ پہلا چکر 300 میٹر کا نامکمل ہوگا اور پھر مزید 400 میٹر کے تین مکمل چکر ہوں گے۔ 300 میٹر نامکمل چکر 400 میٹر میں سے 100 میٹر کم کر کے اس جگہ پر سٹارٹنگ پوائنٹ لگائی جاتی ہے۔ یہ سٹارٹنگ لائن ایک کرو (Curve) کی شکل میں لگائی جاتی ہے۔ اس کا طریقہ کار یوں ہے کہ دوسری گولائی کے شروع میں جہاں سے 200 میٹر کے زینے دیے جاتے ہیں وہاں پر پہلی گلی کی اندرونی لائن سے 8 انچ کے فاصلے پر مرکز مان کر پیچھے کی طرف 100 میٹر کے فاصلے پر 8 گلیوں میں ایک قوس لگایا جاتا ہے یہی قوس 150 میٹر دوڑ کی سٹارٹنگ لائن ہوگی۔ سٹارٹ لینے کی بجائے پورے پاؤں کا استعمال ہوتا ہے۔ 1500 میٹر دوڑ کا آغاز انٹرنیشنل کرو (Curve) سے ہوتا ہے۔',
           'د ۱۵۰۰ مترو په منډه کې هر لوبغاړی د ۴۰۰ مترو پر معیاري ټریک ۳ بشپړ څرخه او د ۳۰۰ مترو یو نابشپړ څرخ وهي. لومړی څرخ به د ۳۰۰ مترو نابشپړ وي او بیا به د ۴۰۰ مترو درې نور بشپړ څرخونه وي. د ۳۰۰ مترو نابشپړ څرخ لپاره له ۴۰۰ مترو ۱۰۰ متره کمېږي او په هغه ځای کې د پیل ټکی لګول کېږي. دا د پیل کرښه د منحني (Curve) په بڼه کښل کېږي. طریقه یې دا ده چې د دویم ګولايي په پیل کې چې د ۲۰۰ مترو زینې ورکول کېږي، هلته د لومړۍ لیکې له داخلي کرښې ۸ انچه واټن کې مرکز ونیول شي او شا ته په ۱۰۰ متره واټن په ۸ لیکو کې یو کمان کښل کېږي؛ همدا کمان به د ۱۵۰ مترو (۱۵۰۰ مترو) منډې د پیل کرښه وي. د سټارټ اخیستو پر ځای ټوله پښه کارول کېږي. د ۱۵۰۰ مترو منډه له نړیوال منحني (Curve) پیلېږي.')])
    b.h('Rules of the 1500-metre race', '1500 میٹر دوڑ کے قوانین', 'د ۱۵۰۰ مترو منډې قوانین')
    b.group('lines', [
        ('i. There are no regular lanes for the 1500-metre race.', 'i۔ 1500 میٹر دوڑ کے لیے باقاعدہ گلیاں نہیں ہوتی۔', 'i. د ۱۵۰۰ مترو منډې لپاره منظمې لیکې نه وي.'),
        ('ii. The order of the lanes will be given by drawing lots.', 'ii۔ گلیوں کی ترتیب قرعہ اندازی سے دی جائے گی۔', 'ii. د لیکو ترتیب به په پچه ورکول کېږي.'),
        ('iii. Before taking the start no player can touch the ground ahead of the start line.', 'iii۔ سٹارٹ لینے سے پہلے کوئی کھلاڑی سٹارٹ لائن سے آگے کی زمین کو ٹچ نہیں کر سکتا۔', 'iii. له سټارټ مخکې هېڅ لوبغاړی د پیل کرښې مخې ته ځمکه نه شي لمسولی.'),
        ('iv. If some player, while running, pushes, holds or knocks down another player or becomes an obstruction in his race, he will be excluded from the competition.', 'iv۔ اگر کوئی کھلاڑی دوڑتے ہوئے کسی دوسرے کھلاڑی کو دھکیلے، پکڑے یا گرائے یا اس کی دوڑ میں رکاوٹ بنے تو اسے مقابلے سے خارج کر دیا جائے گا۔', 'iv. که کوم لوبغاړی د منډې پر مهال بل لوبغاړی ټېل وهي، ونیسي یا یې وغورځوي یا یې په منډه کې خنډ شي، له سیالۍ به وایستل شي.'),
        ('v. There will be separate competitions for men and women.', 'v۔ مردوں اور عورتوں کے الگ الگ مقابلے ہوں گے۔', 'v. د نارینه وو او ښځو جلا جلا سیالۍ به وي.'),
        ('vi. If in the opinion of the starter or recaller (Recaller) a false start has been taken, the recaller with a fire can call the players back to take the start again.', 'vi۔ اگر سٹارٹر یا ریکالر (Recaller) کی رائے میں غلط سٹارٹ لیا ہو تو ریکالر ایک اور فائر سے کھلاڑیوں کو دوبارہ سٹارٹ لینے کے لیے بُلا سکتا ہے۔', 'vi. که د سټارټر یا ریکالر (Recaller) په اند ناسم سټارټ اخیستل شوی وي، ریکالر په بل ډز لوبغاړي بیا سټارټ ته رابللی شي.')])
    r = rec(b, 7, 22, 98)
    deco(r, 'A photograph of middle-distance runners on a track is decorative.')
    BOOK.save(98, [(7, r)], issues=[{'id': 'hpe12-pdf098', 'unit': 7, 'printedPage': 93,
               'description': 'The paragraph says “یہی قوس 150 میٹر دوڑ کی سٹارٹنگ لائن ہوگی” — 150 for 1500 in print. “سٹارٹنگ پوائنٹ لگائی جاتی ہے”, “باقاعدہ گلیاں نہیں ہوتی”. Retained as printed.'}])


def p99():
    b = Builder()
    b.group('lines', [
        ('vii. In the 1500-metre race the start will be taken in the standing position. At the fire of the starter the players will take the start.', 'vii۔ 1500 میٹر دوڑ کا سٹارٹ کھڑی پوزیشن میں لیں گے۔ سٹارٹر کے فائر سے کھلاڑی سٹارٹ لیں گے۔', 'vii. د ۱۵۰۰ مترو منډې سټارټ به په ولاړ حالت کې اخیستل کېږي. د سټارټر په ډز به لوبغاړي سټارټ اخلي.'),
        ('viii. After taking the start, if a player goes out of the track, that player cannot be included in this race again.', 'viii۔ سٹارٹ لینے کے بعد اگر کھلاڑی ٹریک سے باہر جائے تو وہی کھلاڑی ٹریک میں دوبارہ آ کر اس دوڑ میں شامل نہیں ہو سکتا۔', 'viii. له سټارټ وروسته که لوبغاړی له ټریک ووځي، هغه لوبغاړی بیا په دې منډه کې نه شي شاملېدای.'),
        ('ix. No player can put any kind of mark on the track.', 'ix۔ کوئی بھی کھلاڑی ٹریک پر کسی قسم کا نشان نہیں لگا سکتا۔', 'ix. هېڅ لوبغاړی پر ټریک هېڅ ډول نښه نه شي لګولی.'),
        ('x. A player can take part in the competition without shoes too, or can run with spikes.', 'x۔ کھلاڑی بغیر جوتوں کے بھی مقابلے میں شریک ہو سکتا ہے یا سپائکس کے ساتھ دوڑ سکتا ہے۔', 'x. لوبغاړی له بوټانو پرته هم په سیالۍ کې ګډون کولی شي یا له سپایکس سره منډه وهلی شي.'),
        ('xi. Before the race starts, every player will be allotted a number by the administration, which the player will put on his chest and back.', 'xi۔ دوڑ شروع ہونے سے پہلے ہر ایک کھلاڑی کو انتظامیہ کی طرف سے نمبر الاٹ ہوگا جو کھلاڑی سینے اور پشت پر لگائے گا۔', 'xi. د منډې له پیل مخکې به هر لوبغاړي ته د ادارې له خوا شمېره ورکول کېږي چې لوبغاړی به یې پر سینه او شا لګوي.'),
        ('xii. The 1500-metre race will be on a 400-metre standard track.', 'xii۔ 1500 میٹر کا دوڑ 400 میٹر کے سٹینڈرڈ ٹریک پر ہوگا۔', 'xii. د ۱۵۰۰ مترو منډه به د ۴۰۰ مترو پر معیاري ټریک وي.'),
        ('xiii. The use of medicines to increase strength, power and speed is prohibited.', 'xiii۔ طاقت، قوت اور رفتار بڑھانے کے لیے ادویات کا استعمال ممنوع ہے۔', 'xiii. د ځواک، قوت او سرعت د زیاتولو لپاره د درملو کارول منع دي.'),
        ('xiv. If the number of players is greater, heats will be held.', 'xiv۔ اگر کھلاڑیوں کی تعداد زیادہ ہو تو ہیٹ کرائی جائیں گی۔', 'xiv. که د لوبغاړو شمېر ډېر وي، هیټونه به جوړېږي.'),
        ('xv. If the number of players is less than 8, the race will be a final.', 'xv۔ کھلاڑیوں کی تعداد 8 سے کم ہو تو دوڑ فائنل ہوگی۔', 'xv. که د لوبغاړو شمېر له ۸ کم وي، منډه به وروستۍ (فاینل) وي.'),
        ('xvi. If some player leaves the race of his own will, he will not be included in the race again.', 'xvi۔ کوئی کھلاڑی اپنی مرضی سے دوڑ چھوڑ دے تو اسے دوبارہ دوڑ میں شامل نہیں کیا جائے گا۔', 'xvi. که کوم لوبغاړی په خپله خوښه منډه پرېږدي، بیا به منډې ته نه شاملېږي.')])
    b.h('Fouls', 'فاؤلز', 'خطاګانې')
    b.group('lines', [('i. Running before the fire.', 'i۔ فائر سے پہلے دوڑنا۔', 'i. له ډز مخکې منډه.'), ('ii. Running without the chest number.', 'ii۔ چسٹ نمبر کے بغیر دوڑنا۔', 'ii. د سینې له شمېرې پرته منډه.'),
                      ('iii. Going out ahead from the left side.', 'iii۔ بائیں طرف سے آگے نکلنا۔', 'iii. له کیڼ اړخه مخکې وتل.'), ('iv. Pushing or knocking down another player.', 'iv۔ دوسرے کھلاڑی کو دھکا دینا یا گرانا۔', 'iv. بل لوبغاړي ته ټېله ورکول یا یې غورځول.'),
                      ('v. Adopting an indecent attitude with players or judges.', 'v۔ کھلاڑیوں یا ججز کے ساتھ ناشائستہ رویہ اختیار کرنا۔', 'v. له لوبغاړو یا قاضیانو سره ناوړه چلند کول.'), ('vi. Using such medicines or things as help in the race.', 'vi۔ ایسی ادویات یا اشیاء استعمال کرنا جو دوڑ میں مدد دیتی ہو۔', 'vi. داسې درمل یا توکي کارول چې په منډه کې مرسته کوي.'),
                      ('vii. Leaving the race incomplete.', 'vii۔ دوڑ کو نامکمل چھوڑنا۔', 'vii. منډه نابشپړه پرېښودل.')])
    r = rec(b, 7, 23, 99)
    BOOK.save(99, [(7, r)], issues=[{'id': 'hpe12-pdf099', 'unit': 7, 'printedPage': 94,
               'description': 'The list numbers vii–xvi at the right edge are faint in the scan. An owner ballpoint mark is excluded. Fouls item iii “بائیں طرف سے آگے نکلنا”. Retained as printed.'}])


def p100():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The angle of the sector of the discus throw is ________ degrees.', 'ڈسکس تھرو کے سیکٹر کا زاویہ ________ ڈگری ہوتا ہے۔', 'د ډیسکس د سکټور زاویه ________ درجې وي.'), [('34.92', '34.92', '34.92'), ('40.0', '40.0', '40.0'), ('35', '35', '35'), ('35.92', '35.92', '35.92')]),
         (('The inner diameter of the circle of the discus throw is ________ metres.', 'ڈسکس تھرو کے دائرے کا اندرونی قطر ________ میٹر ہوتا ہے۔', 'د ډیسکس د دایرې داخلي قطر ________ متره وي.'), [('2.50', '2.50', '2.50'), ('1.50', '1.50', '1.50'), ('3.50', '3.50', '3.50'), ('1.75', '1.75', '1.75')]),
         (('In the discus throw, if there are fewer than eight players, then ________ turns are given.', 'ڈسکس تھرو میں آٹھ سے کم کھلاڑی ہوں تو ________ باریاں دی جاتی ہیں۔', 'په ډیسکس کې که له اتو کم لوبغاړي وي، ________ وارونه ورکول کېږي.'), [('3', '3', '3'), ('2', '2', '2'), ('1', '1', '1'), ('6', '6', '6')]),
         (('The discus falling outside the sector is ________ .', 'ڈسکس کا سیکٹر سے باہر گرنا ________ ہے۔', 'له سکټور بهر د ډیسکس لوېدل ________ دي.'), [('a mistake', 'غلطی', 'تېروتنه'), ('a repeat turn', 'دوبارہ باری', 'بیا وار'), ('disqualification', 'نااہلی', 'نااهلي'), ('correct', 'درست', 'سم')]),
         (('In the discus throw there are ________ ways of gripping the discus.', 'ڈسکس تھرو میں ڈسکس کی گرفت کے ________ طریقے ہیں۔', 'په ډیسکس کې د ډیسکس د نیولو ________ طریقې دي.'), [('one', 'ایک', 'یوه'), ('two', 'دو', 'دوه'), ('three', 'تین', 'درې'), ('four', 'چار', 'څلور')]),
         (('For the 1500-metre race there are no regular ________ .', '1500 میٹر دوڑ کے لیے باقاعدہ ________ نہیں ہوتیں۔', 'د ۱۵۰۰ مترو منډې لپاره منظم ________ نه وي.'), [('ground', 'گراؤنڈ', 'میدان'), ('rules', 'قوانین', 'قوانین'), ('lanes', 'گلیاں', 'لیکې'), ('uniform', 'یونیفارم', 'یونیفورم')]),
         (('The 1500-metre race is run on a ________ -metre standard track.', '1500 میٹر دوڑ ________ میٹر کے سٹینڈرڈ ٹریک پر دوڑی جاتی ہے۔', 'د ۱۵۰۰ مترو منډه د ________ مترو پر معیاري ټریک وهل کېږي.'), [('200', '200', '200'), ('400', '400', '400'), ('600', '600', '600'), ('800', '800', '800')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii'][i], q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i Make the sector of the discus and record the fouls.', 'i ڈسکس کا سیکٹر بنائیں اور فاؤلز درج کریں۔', 'i د ډیسکس سکټور جوړ کړئ او خطاګانې ولیکئ.'),
                      ('ii Record the rules of the discus throw.', 'ii ڈسکس تھرو کے قوانین درج کریں۔', 'ii د ډیسکس قوانین ولیکئ.'),
                      ('iii Make a score sheet for finding the positions of 6 players in the discus throw.', 'iii ڈسکس تھرو میں 6 کھلاڑیوں کی پوزیشن نکالنے کیلئے سکور شیٹ بنائیں۔', 'iii په ډیسکس کې د ۶ لوبغاړو د مقامونو د موندلو لپاره د نمرو پاڼه جوړه کړئ.'),
                      ('iv State the rules and fouls of the 1500-metre race.', 'iv 1500 میٹر دوڑ کے قوانین اور فاؤلز بیان کریں۔', 'iv د ۱۵۰۰ مترو منډې قوانین او خطاګانې بیان کړئ.')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-discus', 'Chapter 7 exercise: discus throw and 1500 m', 'باب ۷: مشقی سوالات — ڈسکس تھرو اور 1500 میٹر', '۷ څپرکی: تمریني پوښتنې — ډیسکس او ۱۵۰۰ متره', 100, [95])
    BOOK.save(100, [(7, r)], issues=[{'id': 'hpe12-pdf100', 'unit': 7, 'printedPage': 95,
               'description': 'Owner ballpoint ticks and margin numerals are excluded. Retained as printed.'}])


def court(cap, labs):
    b = ('<rect x="40" y="70" width="560" height="290" fill="#fdba74" stroke="#1e293b" stroke-width="3"/>'
         '<line x1="320" y1="60" x2="320" y2="370" stroke="#1e293b" stroke-width="3" stroke-dasharray="6 4"/><circle cx="320" cy="70" r="6" fill="#1e293b"/><circle cx="320" cy="360" r="6" fill="#1e293b"/>'
         '<line x1="40" y1="88" x2="600" y2="88" stroke="#fff" stroke-width="2"/><line x1="40" y1="342" x2="600" y2="342" stroke="#fff" stroke-width="2"/>'
         '<line x1="72" y1="70" x2="72" y2="360" stroke="#fff" stroke-width="2"/><line x1="568" y1="70" x2="568" y2="360" stroke="#fff" stroke-width="2"/>'
         '<line x1="237" y1="70" x2="237" y2="360" stroke="#fff" stroke-width="2"/><line x1="403" y1="70" x2="403" y2="360" stroke="#fff" stroke-width="2"/>'
         '<line x1="40" y1="215" x2="237" y2="215" stroke="#fff" stroke-width="2"/><line x1="403" y1="215" x2="600" y2="215" stroke="#fff" stroke-width="2"/>'
         '<line x1="40" y1="40" x2="600" y2="40" stroke="#1e293b"/><line x1="620" y1="70" x2="620" y2="360" stroke="#1e293b"/><line x1="20" y1="88" x2="20" y2="342" stroke="#1e293b"/>')
    for t, x, y, a, rot in labs:
        b += f'<text x="{x}" y="{y}" text-anchor="{a}" font-size="11" font-weight="bold" fill="#1e293b" font-family="sans-serif"' + (f' transform="rotate({rot} {x} {y})"' if rot else '') + f'>{t}</text>'
    return svg(660, 400, b, cap)


def p101():
    b = Builder()
    b.h('Net and Wall Games', 'نیٹ اینڈ وال گیمز', 'جال او دېوال لوبې')
    b.h('Badminton', 'بیڈ منٹن (Badminton)', 'بډمنټن (Badminton)')
    b.h('Court', 'کورٹ', 'میدان')
    H = (['Measurement', 'Feet', 'Metres', 'Breadth'], ['پیمائش', 'فٹ', 'میٹر', 'چوڑائی'], ['اندازه', 'فټ', 'متره', 'پلنوالی'])
    rows = [('Length for doubles', 'ڈبلز کیلئے لمبائی', 'د جوړه لوبې لپاره اوږدوالی', '44 ft', '13.40 m', '20 ft'), ('Length for singles', 'سنگلز کیلئے لمبائی', 'د یوازې لوبې لپاره اوږدوالی', '44 ft', '13.40 m', '17 ft'),
            ('Back gallery', 'بیک گیلری', 'شاتنۍ ګالري', '2′-6″', '0.76 m', ''), ('Side gallery', 'سائیڈ گیلری', 'د څنګ ګالري', '1′-6″', '0.46 m', ''), ('Short service area', 'شارٹ سروس ایریا', 'د لنډ سرویس ساحه', '6′-6″', '2 m', '')]
    b.table('hpe12-badminton-court', H[0], [[e, f, m, w] for e, u, p, f, m, w in rows], H[1], H[2], [[u, f, m, w] for e, u, p, f, m, w in rows], [[p, f, m, w] for e, u, p, f, m, w in rows])
    labs = [('13.4m', 320, 34, 'middle', 0), ('side line for doubles', 150, 82, 'middle', 0), ('LEFT SERVICE COURT', 150, 150, 'middle', 0), ('RIGHT SERVICE COURT', 150, 290, 'middle', 0), ('Centre Line', 150, 210, 'middle', 0),
            ('RIGHT SERVICE COURT', 490, 150, 'middle', 0), ('LEFT SERVICE COURT', 490, 290, 'middle', 0), ('Centre Line', 490, 210, 'middle', 0), ('NET', 314, 215, 'middle', -90),
            ('Short Service Line', 232, 215, 'middle', -90), ('Short Service Line', 398, 215, 'middle', -90), ('long service line for doubles', 67, 215, 'middle', -90), ('long service line for doubles', 563, 215, 'middle', -90),
            ('boundary line and long service line for singles', 55, 215, 'middle', -90), ('5.2m - singles court', 16, 215, 'middle', -90), ('6.1m - doubles court', 636, 215, 'middle', -90),
            ('side line for singles', 320, 352, 'middle', 0), ('46 cm', 40, 380, 'middle', 0), ('76 cm', 56, 395, 'middle', 0), ('3.88m', 160, 380, 'middle', 0), ('1.98m', 280, 380, 'middle', 0),
            ('shuttle test marks (950mm, 530mm)', 590, 20, 'end', 0)]
    sv = [court(c, labs) for c in ('Badminton court (labels as printed)', 'بیڈمنٹن کورٹ', 'د بډمنټن میدان')]
    b.visual('hpe12-fig-badminton-court', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 7, 24, 101)
    r['sourceNote'] = 'The printed court measurements (feet “or” metres, with breadths) are given as a structured table; the court diagram is reproduced as a coded schematic with its printed English labels.'
    BOOK.save(101, [(7, r)])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 96
    {96: p96, 97: p97, 98: p98, 99: p99, 100: p100, 101: p101}[n]()
