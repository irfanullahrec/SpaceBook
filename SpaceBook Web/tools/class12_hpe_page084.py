"""HPE XII PDF84–89: pp.79–84 — straddle roll, Fosbury flop; long/high jump exercise; javelin throw (runway, sector, sector diagram, rules,
structure, measurements). Run: python class12_hpe_page084.py N (84–89)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T


def p84():
    b = Builder()
    b.h('3 Straddle roll', '3 سٹریڈل رول', '3 سټرېډل رول')
    P(b, [('In this method one lands on the foot opposite to that from which the jump is made. In this method too, while jumping, the opposite leg is brought up while kicking, and making the body parallel, landing is done on the other foot.',
           'اس طریقے میں جس پاؤں پر جمپ کیا جاتا ہے اس کے مخالف پاؤں پر اترا جاتا ہے۔ اس طریقہ میں بھی جمپ کرتے وقت مخالف ٹانگ کو کک کرتے ہوئے اوپر لایا جاتا ہے۔ اور جسم کو متوازی کرتے ہوئے لینڈنگ دوسرے پاؤں پر کی جاتی ہے۔',
           'په دې طریقه کې پر هغې پښې کېناستل کېږي چې د ټوپ له پښې مخالفه وي. په دې طریقه کې هم د ټوپ پر مهال مخالفه پښه په لغته پورته راوړل کېږي او بدن موازي کېږي او پر بله پښه کېناستل کېږي.')])
    b.h('4 Fosbury flop', '4 فاسبری فلاپ', '4 فاسبري فلاپ')
    P(b, [('This is the most modern method. In it, while landing, the face is turned towards the sky. While landing, the back is used instead of the feet. That is why it is called the flop.',
           'یہ جدید ترین طریقہ ہے۔ اس میں لینڈنگ کرتے ہوئے منہ آسمان کی طرف کیا جاتا ہے۔ لینڈنگ کرتے وقت بجائے پاؤں کے کمر کا استعمال کیا جاتا ہے۔ اسی لیے اسے فلاپ کہتے ہیں۔',
           'دا تر ټولو نوې طریقه ده. په کې د کېناستو پر مهال مخ اسمان ته کېږي. د کېناستو پر وخت د پښو پر ځای ملا کارول کېږي. له همدې امله فلاپ ورته ویل کېږي.')])
    r = rec(b, 7, 11, 84)
    deco(r, 'A drawing of a jumper in the straddle style and a four-frame image sequence of a Fosbury flop over the bar are decorative.')
    BOOK.save(84, [(7, r)])


def p85():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('In the long and high jump the turns of the players will be given by ________ .', 'لمبی اور اونچی چھلانگ میں کھلاڑیوں کو باریاں ________ سے دی جائیں گی۔', 'په اوږد او لوړ ټوپ کې لوبغاړو ته وارونه په ________ ورکول کېږي.'), [('toss', 'ٹاس', 'ټاس'), ('drawing lots', 'قرعہ اندازی', 'پچه'), ('choice', 'مرضی', 'خوښه'), ('force', 'زبردستی', 'زور')]),
         (('In the long and high jump, if the number of players is more than eight, then every player will be given ________ attempts.', 'لمبی اور اونچی چھلانگ میں اگر کھلاڑیوں کی تعداد آٹھ سے زیادہ ہو تو ہر کھلاڑی کو ________ کوششیں دی جائیں گی۔', 'په اوږد او لوړ ټوپ کې که د لوبغاړو شمېر له اتو زیات وي، هر لوبغاړي ته به ________ هڅې ورکول کېږي.'), [('six, six', 'چھ، چھ', 'شپږ شپږ'), ('four, four', 'چار، چار', 'څلور څلور'), ('three, three', 'تین، تین', 'درې درې'), ('two, two', 'دو، دو', 'دوه دوه')]),
         (('In the long and high jump, if the number of players is less than eight, then every player will be given ________ turns.', 'لمبی اور اونچی چھلانگ میں اگر کھلاڑیوں کی تعداد آٹھ سے کم ہو تو ہر کھلاڑی کو ________ باریاں دی جائیں گی۔', 'په اوږد او لوړ ټوپ کې که د لوبغاړو شمېر له اتو کم وي، هر لوبغاړي ته به ________ وارونه ورکول کېږي.'), [('three, three', 'تین، تین', 'درې درې'), ('six, six', 'چھ، چھ', 'شپږ شپږ'), ('four, four', 'چار، چار', 'څلور څلور'), ('five, five', 'پانچ، پانچ', 'پنځه پنځه')]),
         (('In the long jump the length of the runway is ________ metres.', 'لمبی چھلانگ میں رن وے کی لمبائی ________ میٹر ہوتی ہے۔', 'په اوږد ټوپ کې د منډې لارې اوږدوالی ________ متره وي.'), [('36 to 40', '36 تا 40', '36 تر 40'), ('38 to 40', '38 تا 40', '38 تر 40'), ('40 to 45', '40 تا 45', '40 تر 45'), ('24 to 45', '24 تا 45', '24 تر 45')]),
         (('In the long jump the length of the take-off board is ________ metres.', 'لمبی چھلانگ میں ٹیک آف بورڈ کی لمبائی ________ میٹر ہوتی ہے۔', 'په اوږد ټوپ کې د ټېک اف تختې اوږدوالی ________ متره وي.'), [('1.20', '1.20', '1.20'), ('1.22', '1.22', '1.22'), ('1.25', '1.25', '1.25'), ('1.27', '1.27', '1.27')]),
         (('In the long jump the breadth of the take-off board is ________ centimetres.', 'لمبی چھلانگ میں ٹیک آف بورڈ کی چوڑائی ________ سینٹی میٹر ہوتی ہے۔', 'په اوږد ټوپ کې د ټېک اف تختې پلنوالی ________ سانتي متره وي.'), [('10', '10', '10'), ('20', '20', '20'), ('30', '30', '30'), ('40', '40', '40')])]
    for i, (q, o) in enumerate(Q, 1):
        e.mcq(f'{i}.', q, o, per_line=4)
    r = BOOK.record(e, 'hpe12-ch7-exercise-jumps-1', 'Chapter 7 exercise: long and high jump (1)', 'باب ۷: مشقی سوالات — لمبی اور اونچی چھلانگ (۱)', '۷ څپرکی: تمریني پوښتنې — اوږد او لوړ ټوپ (۱)', 85, [80])
    BOOK.save(85, [(7, r)], issues=[{'id': 'hpe12-pdf085', 'unit': 7, 'printedPage': 80,
               'description': 'Owner ballpoint ticks and a crossed box on the options are excluded. Retained as printed.'}])


def p86():
    e = Builder()
    Q = [(('In the long jump the length of the pit is ________ metres.', 'لمبی چھلانگ میں اکھاڑے کی لمبائی ________ میٹر ہوتی ہے۔', 'په اوږد ټوپ کې د کندې اوږدوالی ________ متره وي.'), [('2.75', '2.75', '2.75'), ('5', '5', '5'), ('9', '9', '9'), ('9', '9', '9')]),
         (('In the long jump the breadth of the pit is ________ metres.', 'لمبی چھلانگ میں اکھاڑے کی چوڑائی ________ میٹر ہوتی ہے۔', 'په اوږد ټوپ کې د کندې پلنوالی ________ متره وي.'), [('2', '2', '2'), ('2.75', '2.75', '2.75'), ('3', '3', '3'), ('3.75', '3.75', '3.75')])]
    for i, (q, o) in enumerate(Q, 7):
        e.mcq(f'{i}.', q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. Make the runway and pit of the long jump.', 'i۔ لمبی چھلانگ کا رن وے اور اکھاڑہ بنائیں۔', 'i. د اوږد ټوپ د منډې لاره او کنده جوړه کړئ.'),
                      ('ii. Write the rules of the long and high jump competition.', 'ii۔ لمبی اور اونچی چھلانگ کے مقابلے کے قوانین تحریر کریں۔', 'ii. د اوږد او لوړ ټوپ د سیالۍ قوانین ولیکئ.'),
                      ('iii. Write the failures during the long and high jump competition.', 'iii۔ لمبی اور اونچی چھلانگ کے مقابلے کے دوران ناکامیاں لکھیں۔', 'iii. د اوږد او لوړ ټوپ د سیالۍ پر مهال ناکامۍ ولیکئ.')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-jumps-2', 'Chapter 7 exercise: long and high jump (2)', 'باب ۷: مشقی سوالات — لمبی اور اونچی چھلانگ (۲)', '۷ څپرکی: تمریني پوښتنې — اوږد او لوړ ټوپ (۲)', 86, [81])
    BOOK.save(86, [(7, r)], issues=[{'id': 'hpe12-pdf086', 'unit': 7, 'printedPage': 81,
               'description': 'Q7 prints the option “9” twice (ج and د). Owner ticks are excluded. Retained as printed.'}])


def p87():
    b = Builder()
    b.h('Javelin Throw', 'نیزہ پھینکنا (Javelin Throw)', 'نېزه غورځول (Javelin Throw)')
    P(b, [('In the competitions of the ancient Olympics the event of javelin throwing was included. In the modern Olympic competitions javelin-throwing competitions were included in 1908. The javelin is thrown by running. In its competitions throwing by gliding like shot put or swinging like the hammer is not permitted.',
           'قدیم اولمپکس کے مقابلوں میں نیزہ پھینکنے کا ایونٹ شامل تھا۔ جدید اولمپک مقابلوں میں نیزہ پھینکنے کے مقابلے 1908 میں شامل کیے گئے۔ نیزہ کو دوڑ کر پھینکا جاتا ہے۔ اس کے مقابلوں میں گولہ پھینکنے کی طرح گلائیڈنگ اور تھالی کی طرح جھلا کر پھینکنے کی اجازت نہیں ہے۔',
           'د لرغوني اولمپیک په سیالیو کې د نېزې غورځولو سیالي شامله وه. په عصري اولمپیک سیالیو کې د نېزې غورځولو سیالۍ په ۱۹۰۸ کې شاملې شوې. نېزه په منډه غورځول کېږي. په سیالیو کې یې د ګولې غورځولو په څېر ښوېدل او د تالۍ (ډیسکس) په څېر زنګول او غورځول اجازه نه لري.')])
    b.h('Runway', 'دوڑنے کا راستہ', 'د منډې لاره')
    P(b, [('For javelin throwing the length of the running path should not be less than 30 metres. The running path is marked with two parallel lines. The thickness of these lines is 5 centimetres. The breadth of the running path is 4 metres. The javelin is thrown from behind the arc made at the end of the running lines. The thickness of this arc is 7 centimetres. At both ends where the arc and the parallel lines meet, lines 75 centimetres long are drawn.',
           'نیزہ پھینکنے کیلئے دوڑنے کے راستے کی لمبائی 30 میٹر سے کم نہ ہو دوڑنے کے راستے کو دو متوازی لائنوں سے واضح کیا جاتا ہے۔ ان لائنوں کی موٹائی 5 سینٹی میٹر ہوتی ہے۔ دوڑنے کے راستے کی چوڑائی 4 میٹر ہوتی ہے۔ نیزہ دوڑنے کے لائنوں کے سرے پر بنی قوس کے پیچھے سے پھینکا جاتا ہے۔ اس قوس کی موٹائی 7 سینٹی میٹر ہوتی ہے۔ قوس اور متوازی لکیروں کے ملنے والے دونوں سروں پر 75 سینٹی میٹر لمبی لکیریں لگائی جاتی ہیں۔',
           'د نېزې غورځولو لپاره د منډې لارې اوږدوالی دې له ۳۰ متره کم نه وي. د منډې لاره په دوو موازي کرښو ښودل کېږي. د دې کرښو پنډوالی ۵ سانتي متره وي. د منډې لارې پلنوالی ۴ متره وي. نېزه د منډې د کرښو په سر جوړې کمان له شا غورځول کېږي. د دې کمان پنډوالی ۷ سانتي متره وي. د کمان او موازي کرښو د یوځای کېدو په دواړو سرونو ۷۵ سانتي متره اوږدې کرښې کښل کېږي.')])
    b.h('Method of making the sector of the javelin', 'نیزے کا سیکٹر بنانے کا طریقہ', 'د نېزې د سکټور د جوړولو طریقه')
    P(b, [('In the middle of the arc, at a distance of 8 metres backwards, a mark will be put on the running path. Then from the middle mark one line will be drawn to the right, forward, in the direction of the length. In the same way one line will be drawn to the left forward. The thickness of these lines will be 5 centimetres. The triangle formed in this way is called the sector. Besides the arc, the thickness of the remaining lines is 5 centimetres.',
           'قوس کے درمیان پیچھے کی طرف 8 میٹر کے فاصلے پر دوڑنے والے راستے پر نشان لگایا جائے گا۔ پھر درمیان والے نشان سے ایک لکیر دائیں آگے کی طرف لمبائی کے رخ لگائی جائے گی۔ اسی طرح ایک لکیر بائیں آگے کی طرف لگائی جائے گی۔ ان لکیروں کی موٹائی 5 سینٹی میٹر ہوگی۔ اس طرح بننے والی تکون سیکٹر کہلاتی ہے۔ قوس کے علاوہ باقی لکیروں کی موٹائی 5 سینٹی میٹر ہوتی ہے۔',
           'د کمان په منځ کې شا ته په ۸ متره واټن د منډې پر لاره نښه لګول کېږي. بیا له منځنۍ نښې یوه کرښه ښي لوري ته مخکې د اوږدوالي په لوري کښل کېږي. همداسې یوه کرښه کیڼ لوري ته مخکې کښل کېږي. د دې کرښو پنډوالی ۵ سانتي متره وي. په دې ډول جوړ شوي درې‌ګوټي ته سکټور ویل کېږي. له کمان پرته د نورو کرښو پنډوالی ۵ سانتي متره وي.')])
    r = rec(b, 7, 12, 87)
    deco(r, 'A five-figure drawing of the javelin throwing action is decorative.')
    BOOK.save(87, [(7, r)], issues=[{'id': 'hpe12-pdf087', 'unit': 7, 'printedPage': 82,
               'description': 'Owner ballpoint notes over the drawing and in the margin are excluded. Retained as printed.'}])


def sector(lab, cap):
    b = ('<rect x="20" y="150" width="150" height="40" fill="#fca5a5" stroke="#991b1b"/><path d="M170 120 L170 220" stroke="#1e293b" stroke-width="3"/>'
         '<polygon points="150,170 430,40 430,300" fill="#16a34a" stroke="#14532d" stroke-width="1.5" opacity="0.85"/>'
         '<path d="M330 120 Q345 170 330 220" stroke="#1e293b" fill="none"/><line x1="172" y1="25" x2="430" y2="25" stroke="#1e293b"/><line x1="440" y1="40" x2="440" y2="300" stroke="#1e293b"/>'
         '<line x1="20" y1="135" x2="170" y2="135" stroke="#1e293b"/>')
    b += T(300, 20, lab[0], 12, 'bold') + T(95, 128, lab[1], 12, 'bold') + T(15, 175, lab[2], 12, 'bold', 'end') + T(350, 172, '29°', 13, 'bold')
    b += T(455, 175, lab[3], 12, 'bold', 'start') + T(160, 240, lab[4], 12, 'bold', 'end') + T(180, 240, lab[5], 12, 'bold', 'start') + T(400, 320, lab[6], 12, 'bold', 'end')
    return svg(500, 340, b, cap)


def p88():
    b = Builder()
    E = ('100 m', 'Runway 36.5 m', '4 m', '25 m', 'Throwing arc', '70 mm', 'Sector line')
    U = ('100 میٹر', 'دوڑنے کا راستہ 36.5 میٹر', '4 میٹر', '25 میٹر', 'پھینکنے کی قوس', '70 ملی میٹر', 'سیکٹر لائن')
    S = ('۱۰۰ متره', 'د منډې لاره ۳۶.۵ متره', '۴ متره', '۲۵ متره', 'د غورځولو کمان', '۷۰ ملي متره', 'د سکټور کرښه')
    sv = [sector(E, 'Javelin runway and sector'), sector(U, 'نیزہ پھینکنے کا رن وے اور سیکٹر'), sector(S, 'د نېزې د منډې لاره او سکټور')]
    b.visual('hpe12-fig-javelin-sector', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Rules of javelin throwing', 'نیزہ پھینکنے کے قوانین', 'د نېزې غورځولو قوانین')
    L(b, [('The order of the turns of players will be fixed by drawing lots.', 'کھلاڑیوں کی باریوں کی ترتیب قرعہ اندازی سے مقرر کی جائیں گی۔', 'د لوبغاړو د وارونو ترتیب به په پچه ټاکل کېږي.'),
          ('If the number of players taking part is more than eight, every player will be given 3, 3 attempts. Then of them the eight best players will be given three more attempts each.', 'اگر حصہ لینے والے کھلاڑیوں کی تعداد آٹھ سے زیادہ ہو تو ہر کھلاڑی کو 3،3 کوششیں دی جائیں گی۔ پھر ان میں سے آٹھ بہترین کھلاڑیوں کو مزید تین تین کوششیں دی جائیں گی۔', 'که د ګډون کوونکو لوبغاړو شمېر له اتو زیات وي، هر لوبغاړي ته به ۳، ۳ هڅې ورکول کېږي. بیا له دوی اتو غوره لوبغاړو ته به نورې درې درې هڅې ورکول کېږي.'),
          ('If eight or fewer than eight players take part in the competition, then all will be given 6, 6 attempts.', 'مقابلے میں آٹھ یا آٹھ سے کم کھلاڑی شریک ہوں تو سب کو 6،6 کوششیں دی جائیں گی۔', 'که په سیالۍ کې اته یا له اتو کم لوبغاړي ګډون وکړي، ټولو ته به ۶، ۶ هڅې ورکول کېږي.'),
          ('The player will throw the javelin facing the front in any style.', 'کھلاڑی نیزے کو کسی بھی سٹائل سے سامنے رخ کر کے پھینکے گا۔', 'لوبغاړی به نېزه په هر سټایل مخامخ مخ کړي او غورځوي.'),
          ('Every correct attempt of the player will be measured.', 'کھلاڑی کی ہر درست کوشش کی پیمائش کی جائے گی۔', 'د لوبغاړي هره سمه هڅه به اندازه کېږي.'),
          ('The player cannot go out of the runway until the javelin touches the ground inside the sector.', 'کھلاڑی اس وقت تک رن وے سے باہر نہیں جا سکتا جب تک نیزہ سیکٹر کے اندر زمین کو نہ چھولے۔', 'لوبغاړی تر هغه له منډې لارې بهر نه شي وتلی چې نېزه د سکټور دننه ځمکې ته ونه لګېږي.'),
          ('Before the competition starts, all players will be given 2, 2 opportunities for practice under the supervision of the judge.', 'مقابلہ شروع ہونے سے پہلے تمام کھلاڑیوں کو جج کی نگرانی میں مشق کیلئے 2،2 مواقع دیے جائیں گے۔', 'د سیالۍ له پیل مخکې به ټولو لوبغاړو ته د قاضي تر څارنې لاندې د تمرین لپاره ۲، ۲ فرصتونه ورکول کېږي.'),
          ('After the competition starts, players will not be allowed to use the runway for practice.', 'مقابلہ شروع ہونے کے بعد کھلاڑیوں کو مشق کیلئے رن وے استعمال کرنے کی اجازت نہیں ہوگی۔', 'د سیالۍ له پیل وروسته لوبغاړو ته به د تمرین لپاره د منډې لارې د کارولو اجازه نه وي.'),
          ('The player can throw only the javelin provided by the administration.', 'کھلاڑی صرف انتظامیہ کی طرف سے مہیا کردہ نیزہ ہی پھینک سکتا ہے۔', 'لوبغاړی یوازې د ادارې له خوا برابره شوې نېزه غورځولی شي.'),
          ('A special powder (Rosin) can be applied to strengthen the grip of the hand on the javelin.', 'نیزہ پر ہاتھ کی گرفت کو مضبوط کرنے کے لیے مخصوص پاؤڈر (Rosin) لگا سکتا ہے۔', 'پر نېزه د لاس د نیولو د پیاوړي کولو لپاره ځانګړی پوډر (Rosin) لګولی شي.')])
    r = rec(b, 7, 13, 88)
    BOOK.save(88, [(7, r)], issues=[{'id': 'hpe12-pdf088', 'unit': 7, 'printedPage': 83,
               'description': 'The sector diagram is reproduced as a coded schematic with its printed figures (runway 36.5 m — the text on p.82 says at least 30 m —, width 4 m, arc 70 mm, 100 m, 25 m, 29°). “ترتیب … مقرر کی جائیں گی”. Retained as printed.'}])


def p89():
    b = Builder()
    L(b, [('While throwing the javelin, the player cannot touch the line of the arc or the ground ahead of it with any part of the body.', 'نیزہ پھینکتے وقت کھلاڑی قوس کی لکیر یا اس کے آگے زمین کو جسم کے کسی حصے سے نہیں چھو سکتا۔', 'د نېزې غورځولو پر مهال لوبغاړی د کمان کرښه یا له هغې مخکې ځمکه د بدن په هېڅ برخه نه شي لمسولی.'),
          ('The attempt should be started after the name is called and the judge signals. The player should start the attempt within one minute, otherwise it will be considered a failure. However, if the athlete wishes, he can stop his started attempt within that specified duration and come out of the runway, and then going back inside can start the attempt again. But this is possible only in that case when no irregularity has been committed by the player during the first attempt.', 'نام پکارے جانے اور جج کے اشارے کے بعد کوشش شروع کی جائے۔ کھلاڑی کو ایک منٹ کے اندر ہی کوشش شروع کرنی چاہیے ورنہ اسے ناکامی تصور کیا جائے گا۔ تاہم اگر اتھلیٹ چاہے تو اس مختص کردہ دورانیہ میں اپنی شروع کردہ کوشش روک کر دوڑنے کے راستے سے باہر آ سکتا ہے۔ اور پھر واپس اندر جا کر دوبارہ کوشش شروع کر سکتا ہے۔ لیکن یہ اسی صورت میں ممکن ہے جب پہلی کوشش کے دوران کھلاڑی سے کوئی بے ضابطگی سرزد نہ ہوئی ہو۔', 'د نوم له بللو او د قاضي له اشارې وروسته دې هڅه پیل شي. لوبغاړی باید په یوه دقیقه کې هڅه پیل کړي، که نه ناکامي ګڼل کېږي. خو که ورزشکار وغواړي، په همدې ټاکلې موده کې خپله پیل شوې هڅه درولی او له منډې لارې بهر راتلی شي او بیا بېرته ننوځي او هڅه بیا پیلولی شي. خو دا یوازې هغه وخت شونی دی چې د لومړۍ هڅې پر مهال له لوبغاړي کومه بې‌قاعدګي نه وي شوې.'),
          ('A javelin falling inside the inner lines of the sector will be counted correct.', 'سیکٹر کی اندرونی لائنوں کے اندر گرنے والا نیزہ درست شمار کیا جائے گا۔', 'د سکټور د داخلي کرښو دننه لوېدلې نېزه به سمه ګڼل کېږي.')])
    b.h('Structure and construction of the javelin', 'نیزہ کی بناوٹ اور ساخت', 'د نېزې جوړښت او بڼه')
    P(b, [('The javelin is made of wood or metal. The javelin has three parts. The pointed tip is made of metal, which is called the head (Head). The second part is called the shaft (Shaft), from where the javelin is held. The third part is called the tail (Tail).', 'نیزہ لکڑی یا دھات کا بنا ہوتا ہے۔ نیزہ کے تین حصے ہوتے ہیں۔ نوکدار سرا دھات کا بنا ہوتا ہے جسے ہیڈ (Head) کہتے ہیں۔ دوسرا حصہ شافٹ (Shaft) کہلاتا ہے جہاں سے نیزہ پکڑا جاتا ہے۔ تیسرا حصہ دُم (Tail) کہلاتا ہے۔', 'نېزه له لرګي یا فلز جوړه وي. نېزه درې برخې لري. تېره څوکه له فلز جوړه وي چې سر (Head) ورته ویل کېږي. دویمه برخه شافټ (Shaft) بلل کېږي چې نېزه ترې نیول کېږي. درېیمه برخه لکۍ (Tail) بلل کېږي.')])
    H = (['Measurement', 'Men', 'Women'], ['پیمائش', 'مردوں کیلئے', 'عورتوں کیلئے'], ['اندازه', 'نارینه', 'ښځې'])
    rows = [('Length', 'لمبائی', 'اوږدوالی', '2.60 m', '2.20 m'), ('Weight', 'وزن', 'وزن', '800 g', '600 g'), ('Length of the pointed head', 'نوکدار سرے کی لمبائی', 'د تېرې څوکې اوږدوالی', '250 mm', '250 mm'),
            ('Maximum thickness', 'موٹائی زیادہ سے زیادہ', 'ډېر تر ډېره پنډوالی', '25 mm', '25 mm')]
    b.table('hpe12-javelin-measure', H[0], [[e, m, w] for e, u, p, m, w in rows], H[1], H[2], [[u, m.replace(' m', ' میٹر').replace(' g', ' گرام').replace(' mm', ' ملی میٹر'), w.replace(' m', ' میٹر').replace(' g', ' گرام').replace(' mm', ' ملی میٹر')] for e, u, p, m, w in rows],
            [[p, m, w] for e, u, p, m, w in rows])
    r = rec(b, 7, 14, 89)
    r['sourceNote'] = 'The two printed lists “measurement of the javelin for men / for women” are combined into one structured table.'
    BOOK.save(89, [(7, r)])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 84
    {84: p84, 85: p85, 86: p86, 87: p87, 88: p88, 89: p89}[n]()
