"""HPE XII PDF78–83: pp.73–78 — long jump (preparation, jump, take off, landing); high jump equipment (uprights, cross bar, landing area, runway),
rules, fouls, result sheet, skills (eastern roll, western roll). Run: python class12_hpe_page078.py N (78–83)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p78():
    b = Builder()
    b.h('Preparation for rising in the air', 'ہوا میں اُچھلنے کی تیاری', 'هوا ته د پورته کېدو چمتووالی')
    P(b, [('From the start of the run the athlete begins to check how he will hit the take-off board correctly, and according to that he creates less or more allowance in his steps. The preparation of take off begins from the last three or four steps. The one jumping straightens his body during this and also keeps up his speed.',
           'دوڑ کے آغاز سے ہی اتھلیٹ یہ جانچ شروع کر دیتا ہے کہ وہ ٹیک آف بورڈ کو کیسے صحیح انداز میں ہٹ کرے گا اور اسی کے مطابق وہ اپنے قدموں میں کم یا زیادہ گنجائش پیدا کرتا ہے۔ ٹیک آف کی تیاری آخری تین چار قدموں سے شروع ہوتی ہے۔ چھلانگ لگانے والا اس دوران اپنے جسم کو سیدھا کر لیتا ہے اور اپنی رفتار کو بھی برقرار رکھتا ہے۔',
           'د منډې له پیله ورزشکار دا ارزونه پیلوي چې د ټېک اف تختې ته به څنګه سم ګوزار وکړي او له همدې سره سم په خپلو قدمونو کې لږ یا ډېر ځای پیدا کوي. د ټېک اف چمتووالی له وروستیو درېیو څلورو قدمونو پیلېږي. ټوپ وهونکی په دې وخت کې خپل بدن نېغ کوي او خپل سرعت هم ساتي.')])
    b.h('Jump', 'اُچھلنا (Jump)', 'ټوپ (Jump)')
    P(b, [('This is an important stage. Jumping depends on the height of the athlete, the position of the body, and the manner of moving the arms, legs and trunk. The act of jumping starts from the last three or four steps. In jumping less vertical speed and more horizontal speed should be obtained.',
           'یہ اہم مرحلہ ہے۔ اچھلنے کا دار و مدار اتھلیٹ کے قد، جسم کی حالت، بازوؤں، ٹانگوں اور دھڑ کو حرکت دینے کے انداز پر منحصر ہے۔ اچھلنے کا عمل آخری تین چار قدموں سے شروع ہوتا ہے۔ اچھلنے میں کم عمودی رفتار اور زیادہ افقی رفتار حاصل کرنی چاہیے۔',
           'دا مهم پړاو دی. ټوپ د ورزشکار پر قد، د بدن پر حالت، د مټو، پښو او تنې د خوځولو پر طرز ولاړ دی. د ټوپ عمل له وروستیو درېیو څلورو قدمونو پیلېږي. په ټوپ کې دې لږ عمودي سرعت او ډېر افقي سرعت ترلاسه شي.'),
          ('As soon as the last step comes on the board of jumping, the hips are swung forward from behind. As a result of this the last step becomes short. As soon as the heel of the foot touches the board, from the combined force of the weight and speed of the body a momentary jerk arises. This helps in raising the body high. Because of this jerk the body and the knee bend a little and quickly rise up and change into the jump. Here the action of both legs is correct and timely so that the force of rising up can be increased. Along with this the action of fast-moving arms too proves helpful in rising up.',
           'آخری قدم جونہی اچھلنے کے تختے پر آتا ہے۔ کولہوں کو پیچھے سے آگے کی جانب جھلایا جاتا ہے۔ اس کے نتیجے میں آخری قدم چھوٹا ہو جاتا ہے۔ پاؤں کی ایڑی بورڈ سے چھوتے ہی جسم کے وزن اور رفتار کی مشترکہ طاقت سے جزوی جھٹکا پیدا ہوتا ہے۔ اس سے جسم کو اونچا اٹھنے میں مدد ملتی ہے۔ اس جھٹکے کی وجہ سے جسم اور گھٹنا تھوڑا سا جھکتا ہے اور جلد ہی اوپر اٹھتا ہے اور چھلانگ میں تبدیل ہو جاتا ہے۔ یہاں دونوں ٹانگوں کا عمل صحیح اور بروقت ہوتا کہ اوپر اٹھنے کی طاقت کو بڑھایا جا سکے۔ اس کے ساتھ ہی تیز رفتار بازوؤں کا عمل بھی اوپر اٹھنے میں مددگار ثابت ہوتا ہے۔',
           'څنګه چې وروستی قدم د ټوپ تختې ته راشي، کوناټې له شا مخکې ته زنګول کېږي. په پایله کې وروستی قدم لنډېږي. څنګه چې د پښې پوندۍ تختې ته ولګېږي، د بدن د وزن او سرعت له ګډ ځواک لنډ ټکان پیدا کېږي. دا د بدن په لوړېدو کې مرسته کوي. د دې ټکان له امله بدن او زنګون لږ کږېږي او ژر پورته کېږي او په ټوپ اوړي. دلته د دواړو پښو عمل سم او په وخت وي ترڅو د پورته کېدو ځواک زیات شي. ورسره د چټکو مټو عمل هم په پورته کېدو کې مرستندوی ثابتېږي.')])
    b.h('Take Off', 'اُڑان (Take Off)', 'الوتنه (Take Off)')
    P(b, [('During flight the whole action of flight and the purpose is, while keeping the balance of the body in the air, to come down on the ground in the correct manner and to obtain as much distance as possible from gravity. A good take-off provides a good flight.',
           'دوران پرواز اڑان کا سارا عمل اور مقصد ہوا میں جسم کے توازن کو برقرار رکھتے ہوئے درست انداز میں زمین پر اترنا اور کششِ ثقل سے ممکنہ حد تک زیادہ سے زیادہ دوری حاصل کرنا ہے۔ ایک اچھا ٹیک آف ایک اچھی اڑان مہیا کرتا ہے۔',
           'د الوتنې پر مهال د الوتنې ټول عمل او موخه دا ده چې په هوا کې د بدن توازن وساتل شي، په سمه توګه پر ځمکه کېناستل شي او له جاذبې تر وسه ډېر واټن ترلاسه شي. ښه ټېک اف ښه الوتنه برابروي.')])
    b.h('Landing', 'زمین پر اترنا (Landing)', 'پر ځمکه کېناستل (Landing)')
    P(b, [('When the legs come in front of the body, the act of landing on the ground begins. The heels generally touch the ground …', 'جب ٹانگیں جسم کے سامنے آ جاتی ہیں۔ تو زمین پر اترنے کا عمل شروع ہو جاتا ہے۔ ایڑیاں عام طور پر زمین کو …', 'کله چې پښې د بدن مخې ته راشي، پر ځمکه د کېناستو عمل پیلېږي. پوندۍ عموماً ځمکې ته …')])
    r = rec(b, 7, 5, 78)
    BOOK.save(78, [(7, r)], issues=[{'id': 'hpe12-pdf078', 'unit': 7, 'printedPage': 73,
               'description': 'The heading “اُڑان (Take Off)” is used for the flight stage (the previous heading “اُچھلنا (Jump)” covers take-off). “یہاں دونوں ٹانگوں کا عمل صحیح اور بروقت ہوتا کہ”. Retained as printed.'}])


def p79():
    b = Builder()
    P(b, [('… touch first. The athlete should try to keep the heels as high as possible. For this it is better for the long arms to be behind. After landing on the ground, to remove the effects of the jerk, the legs bend; at that time the hands should be swung forward. In such a case quick and timely movements are necessary to avoid sitting down in the pit. Try that both feet land on the ground together; it should not be that one foot is ahead and the other foot behind; this thing becomes the cause of loss in the distance of the jump.',
           'پہلے چھوتی ہیں۔ اتھلیٹ ایڑیاں ہر ممکن اونچی رکھنے کی کوشش کریں۔ اس لیے لمبے ہاتھوں کا پیچھے ہونا بہتر ہے۔ زمین پر اترنے کے بعد ٹانگیں جھٹکے کے اثرات کو زائل کرنے کیلئے مڑتی ہیں اس وقت ہاتھوں کو آگے کی طرف جھلایا جائے۔ ایسی صورت میں اکھاڑے میں بیٹھ جانے سے بچنے کیلئے تیز اور بروقت حرکات لازمی ہیں۔ یہ کوشش کریں کہ دونوں پاؤں ایک ساتھ زمین پر اتریں ایسا نہ ہو کہ ایک پاؤں آگے اور دوسرا پاؤں پیچھے ہو یہ چیز چھلانگ کے فاصلے میں نقصان کا باعث بنتی ہے۔',
           '… لومړی لګي. ورزشکار دې هڅه وکړي چې پوندۍ تر وسه لوړې وساتي. له همدې امله د اوږدو لاسونو شا ته کېدل غوره دي. پر ځمکه له کېناستو وروسته پښې د ټکان د اغېزو د لرې کولو لپاره کږېږي؛ هغه وخت دې لاسونه مخکې ته وزنګول شي. په داسې حال کې په کنده کې د کېناستو د مخنیوي لپاره چټک او په وخت حرکات اړین دي. هڅه وکړئ چې دواړه پښې یوځای پر ځمکه کېني؛ داسې نه چې یوه پښه مخکې او بله شا وي؛ دا شی د ټوپ په واټن کې د زیان لامل کېږي.')])
    sv = []
    from class12_hpe_common import svg, T
    figs = ''.join(f'<g transform="translate({20 + i * 72},{10 + (i == 3) * -10})"><circle cx="20" cy="15" r="8" fill="#334155"/><line x1="20" y1="23" x2="{18 + i * 2}" y2="60" stroke="#334155" stroke-width="5"/>'
                   f'<line x1="{18 + i * 2}" y1="60" x2="{5 + i * 4}" y2="90" stroke="#334155" stroke-width="5"/><line x1="{18 + i * 2}" y1="60" x2="{35 + i * 3}" y2="88" stroke="#334155" stroke-width="5"/>'
                   f'<line x1="20" y1="32" x2="{40 + i * 2}" y2="{20 + i * 3}" stroke="#334155" stroke-width="4"/></g>' for i in range(6))
    figs += '<line x1="10" y1="105" x2="450" y2="105" stroke="#1e293b" stroke-width="2"/><rect x="150" y="102" width="30" height="6" fill="#dc2626"/>'
    sv = [svg(460, 135, figs, c) for c in ('Phases of the long jump: run-up, take-off, flight, landing', 'لمبی چھلانگ کے مراحل: دوڑ، ٹیک آف، اڑان، لینڈنگ', 'د اوږد ټوپ پړاوونه: منډه، ټېک اف، الوتنه، کېناستل')]
    b.visual('hpe12-fig-longjump-phases', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 7, 6, 79)
    BOOK.save(79, [(7, r)], issues=[{'id': 'hpe12-pdf079', 'unit': 7, 'printedPage': 74,
               'description': 'The two-row drawing of long-jump phases and the close-up of a landing are reproduced as one coded schematic sequence. The page has a crease running down the middle (legible). An owner ballpoint note is excluded. Retained as printed.'}])


def p80():
    b = Builder()
    b.h('High Jump', 'اونچی چھلانگ (High Jump)', 'لوړ ټوپ (High Jump)')
    b.h('(a) Upright', '(الف) آپ رائٹ (Upright)', '(الف) ولاړې ستنې (Upright)')
    L(b, [('To keep the cross bar at different heights two uprights (Uprights) (poles, posts) made of iron, wood or any material are needed. It should be kept in mind that marks are placed on them to show the height and that they are strong.', 'کراس بار کو مختلف بلندی پر رکھنے کے لیے لوہے، لکڑی یا کسی بھی میٹریل سے بنے ہوئے دو آپ رائٹس (Uprights) (پول، کھمبے) کی ضرورت ہوتی ہے۔ اس بات کا خیال رکھا جائے کہ ان میں بلندی کو ظاہر کرنے کے لیے نشانات لگے ہوں اور وہ مضبوط ہوں۔', 'د کراس بار په بېلابېلو لوړوالیو د ایښودو لپاره له اوسپنې، لرګي یا کوم بل مواد جوړو دوو ولاړو ستنو (Uprights) (پول، ستنې) ته اړتیا وي. پام دې وي چې د لوړوالي د ښودلو نښې پرې لګېدلې وي او پیاوړې وي.'),
          ('The distance between the uprights (Uprights) should be at least 3.66 metres and at most 4.02 metres.', 'آپ رائٹس (Uprights) کا درمیانی فاصلہ کم از کم 3.66 میٹر اور زیادہ سے زیادہ 4.02 میٹر ہونا چاہیے۔', 'د ولاړو ستنو (Uprights) ترمنځ واټن دې لږ تر لږه ۳.۶۶ متره او ډېر تر ډېره ۴.۰۲ متره وي.'),
          ('The supports (Support) for the cross bar will be of rectangular shape and their length will be 60 millimetres and breadth 40 millimetres.', 'کراس بار کے لیے سہارے (Support) مستطیل شکل کے ہوں گے اور ان کی لمبائی 60 ملی میٹر اور چوڑائی 40 ملی میٹر ہوگی۔', 'د کراس بار لپاره ملاتړي (Support) به مستطیل ډوله وي او اوږدوالی به یې ۶۰ ملي متره او پلنوالی ۴۰ ملي متره وي.')])
    b.h('(b) Cross Bar', '(ب) کراس بار (Cross Bar)', '(ب) کراس بار (Cross Bar)')
    P(b, [('It should be made of any metal (iron), wood or suitable material. In the middle it can be round or triangular in shape, but its edges will be of rectangular shape so that placing it on the upright (fixing) is easy.', 'کسی بھی دھات (لوہے) یا لکڑی یا مناسب میٹریل سے بنا ہونا چاہیے۔ درمیان سے گول یا مثلث شکل کا ہو سکتا ہے لیکن اس کے کنارے مستطیل شکل کے ہوں گے تاکہ Upright پر لگانے (ایستادہ) کرنے میں آسانی ہو۔', 'دې له کوم فلز (اوسپنې)، لرګي یا مناسب موادو جوړ وي. په منځ کې ګرد یا درې‌ګوټیز کېدای شي، خو څنډې به یې مستطیل ډوله وي ترڅو پر Upright د ایښودو (درولو) کې اسانتیا وي.')])
    L(b, [('The length of the cross bar will be at least 3.64 and at most 4 metres.', 'کراس بار کی لمبائی کم سے کم 3.64 اور زیادہ سے زیادہ 4 میٹر ہوگی۔', 'د کراس بار اوږدوالی به لږ تر لږه ۳.۶۴ او ډېر تر ډېره ۴ متره وي.'),
          ('Its weight will be 2.2 kilograms.', 'اس کا وزن 2.2 کلو گرام ہوگا۔', 'وزن به یې ۲.۲ کیلوګرامه وي.'),
          ('The surface of those parts of the bar which will be placed on the supports (Support) should be smooth.', 'بار کے وہ حصے جو کہ (Support) پر رکھے جائیں گے ان کی سطح ہموار ہونی چاہیے۔', 'د بار هغه برخې چې پر ملاتړو (Support) ایښودل کېږي، سطحه یې دې هواره وي.')])
    b.h('(c) Landing Area', '(ج) لینڈنگ ایریا (Landing Area)', '(ج) د کېناستو ساحه (Landing Area)')
    L(b, [('The length of the landing area 5 metres.', 'لینڈنگ ایریا کی لمبائی 5 میٹر۔', 'د کېناستو د ساحې اوږدوالی ۵ متره.'), ('The breadth of the landing area 4 metres.', 'لینڈنگ ایریا کی چوڑائی 4 میٹر۔', 'د کېناستو د ساحې پلنوالی ۴ متره.')])
    r = rec(b, 7, 7, 80)
    BOOK.save(80, [(7, r)], issues=[{'id': 'hpe12-pdf080', 'unit': 7, 'printedPage': 75,
               'description': 'A large owner ballpoint cross and the word “سامان” beside the heading are excluded (no printed “Equipment” sub-heading). The page has a vertical crease (legible). Retained as printed.'}])


def p81():
    b = Builder()
    L(b, [('The height (thickness) of the landing area depends on what material has been used in its construction. Effort should be made that the player is not injured while landing after the jump.', 'لینڈنگ ایریا کی بلندی (موٹائی) اس بات پر منحصر ہے کہ اس کی بناوٹ میں کون سا میٹریل استعمال ہوا ہے۔ کوشش یہ کی جائے کہ کھلاڑی جمپ کے بعد لینڈنگ کرتے ہوئے زخمی نہ ہو۔', 'د کېناستو د ساحې لوړوالی (پنډوالی) پر دې ولاړ دی چې په جوړښت کې یې کوم مواد کارول شوي. هڅه دې وشي چې لوبغاړی له ټوپ وروسته د کېناستو پر مهال ټپي نه شي.')])
    b.h('(d) Runway', '(د) دوڑنے کا راستہ (Runway)', '(د) د منډې لاره (Runway)')
    L(b, [('Minimum length 15 metres.', 'کم از کم لمبائی 15 میٹر۔', 'لږ تر لږه اوږدوالی ۱۵ متره.'), ('The surface of the take off (Take off) area should be level.', 'ٹیک آف (Take off) ایریا کی سطح ہموار ہونی چاہیے۔', 'د ټېک اف (Take off) ساحې سطحه دې هواره وي.')])
    b.h('Rules of the high jump', 'اونچی چھلانگ کے قوانین', 'د لوړ ټوپ قوانین')
    b.group('lines', [
        ('i. The order of turns will be decided by drawing lots.', 'i۔ باری کی ترتیب کا فیصلہ قرعہ اندازی سے ہوگا۔', 'i. د وارونو ترتیب به په پچه ټاکل کېږي.'),
        ('ii. The player will be given the benefit of his best attempt.', 'ii۔ کھلاڑی کو اس کی بہترین کوشش کا فائدہ دیا جائے گا۔', 'ii. لوبغاړي ته به د هغه د غوره هڅې ګټه ورکول کېږي.'),
        ('iii. Every player will be given a chest number (Chest Number).', 'iii۔ ہر کھلاڑی کو چسٹ نمبر (Chest Number) دیا جائے گا۔', 'iii. هر لوبغاړي ته به د سینې شمېره (Chest Number) ورکول کېږي.'),
        ('iv. Before the competition starts the chief judge will announce the initial height. At the start of every round too the chief judge will announce the height.', 'iv۔ مقابلہ شروع ہونے سے پہلے چیف جج ابتدائی بلندی کا اعلان کرے گا۔ ہر راونڈ کے آغاز پر بھی بلندی کا اعلان چیف جج کرے گا۔', 'iv. د سیالۍ له پیل مخکې به لوی قاضي لومړنی لوړوالی اعلانوي. د هر پړاو په پیل کې هم لوی قاضي لوړوالی اعلانوي.'),
        ('v. After the start of the competition no player can use the landing area or runway for practice.', 'v۔ مقابلے کے آغاز کے بعد کوئی بھی کھلاڑی لینڈنگ ایریا اور رن وے کو پریکٹس کے لیے استعمال نہیں کر سکتا۔', 'v. د سیالۍ له پیل وروسته هېڅ لوبغاړی د تمرین لپاره د کېناستو ساحه او د منډې لاره نه شي کارولی.'),
        ('vi. The player will have to jump from one foot.', 'vi۔ کھلاڑی کو ایک پاؤں سے جمپ لینا ہوگا۔', 'vi. لوبغاړی باید په یوه پښه ټوپ ووهي.'),
        ('vii. The player will be given three opportunities at every height.', 'vii۔ کھلاڑی کو ہر بلندی پر تین تین مواقع دیے جائیں گے۔', 'vii. لوبغاړي ته به په هر لوړوالي درې درې فرصتونه ورکول کېږي.'),
        ('viii. On three consecutive failures the player will be out of the competition.', 'viii۔ تین متواتر ناکامیوں پر کھلاڑی مقابلے سے خارج ہو جائے گا۔', 'viii. په درېیو پرلپسې ناکامیو لوبغاړی له سیالۍ وځي.'),
        ('ix. If the player, reaching near the cross bar, decides that he will not jump, he is allowed to do so.', 'ix۔ اگر کھلاڑی کراس بار کے قریب پہنچ کر یہ فیصلہ کرے کہ اس نے جمپ نہیں کرنا تو اس کو اجازت ہے۔', 'ix. که لوبغاړی کراس بار ته نږدې ورسېږي او پرېکړه وکړي چې ټوپ نه وهي، اجازه لري.'),
        ('x. The player can decide not to jump at any height, but he cannot jump again at that same height.', 'x۔ کھلاڑی کسی بھی اونچائی پر جمپ نہ کرنے کا فیصلہ کر سکتا ہے لیکن وہ اسی اونچائی پر دوبارہ جمپ نہیں کر سکتا۔', 'x. لوبغاړی په هر لوړوالي د ټوپ نه وهلو پرېکړه کولی شي، خو په همغه لوړوالي بیا ټوپ نه شي وهلی.'),
        ('xi. The height of the bar will be raised by two centimetres after every round.', 'xi۔ بار کی اونچائی ہر راونڈ کے بعد دو سینٹی میٹر بڑھائی جائیگی۔', 'xi. د بار لوړوالی به له هر پړاو وروسته دوه سانتي متره لوړېږي.')])
    r = rec(b, 7, 8, 81)
    BOOK.save(81, [(7, r)], issues=[{'id': 'hpe12-pdf081', 'unit': 7, 'printedPage': 76,
               'description': 'Owner English and Urdu ballpoint notes in the left margin (“classic”, “Landing Area”) are excluded. Retained as printed.'}])


def p82():
    b = Builder()
    b.h('Fouls', 'فاؤلز', 'خطاګانې')
    b.group('lines', [('i. Knocking down the cross bar while jumping.', 'i۔ جمپ لگاتے وقت کراس بار کو گرا دینا۔', 'i. د ټوپ پر مهال کراس بار غورځول.'), ('ii. Jumping with both feet.', 'ii۔ دونوں پاؤں سے جمپ کرنا۔', 'ii. په دواړو پښو ټوپ وهل.'),
                      ('iii. Wasting one’s turn.', 'iii۔ اپنی باری کو ضائع کرنا۔', 'iii. خپل وار ضایع کول.'), ('iv. Wasting all three jumps at one height.', 'iv۔ ایک اونچائی پر تینوں جمپ ضائع کر دینا۔', 'iv. په یوه لوړوالي ټول درې ټوپونه ضایع کول.')])
    b.h('Result sheet', 'رزلٹ شیٹ', 'د پایلو پاڼه')
    P(b, [('The player who crosses the last height in the fewest attempts will be in first position; otherwise equality will be resolved in the following way. In case of equality, first of all the total failures will be counted. Whose number of failures is less will be in first position.',
           'جو کھلاڑی آخری بلندی کو کم کوشش میں عبور کرے وہ پہلی پوزیشن پر ہوگا بصورتِ دیگر برابری درج ذیل طریقہ سے حل کی جائے گی۔ برابری کی صورت میں سب سے پہلے کل ناکامیاں شمار کی جائیں گی۔ جن کی ناکامیوں تعداد کم ہوگی پہلی پوزیشن پر ہوگا۔',
           'هغه لوبغاړی چې وروستی لوړوالی په لږو هڅو تېر کړي، په لومړي مقام کې وي؛ که نه نو برابري به په لاندې ډول حلېږي. د برابرۍ په صورت کې تر ټولو لومړی ټولې ناکامۍ شمېرل کېږي. د چا چې د ناکامیو شمېر لږ وي، په لومړي مقام کې وي.'),
          ('If equality is still not resolved, then if the equality is for first position, the cross bar will be lowered two centimetres from the last height and one attempt each will be given. The one who crosses the height will be in first position.',
           'اگر پھر بھی برابری حل نہ ہو تو اگر برابری پہلی پوزیشن کے لیے ہے تو کراس بار کو آخری بلندی سے دو سینٹی میٹر نیچے کیا جائے گا اور ایک ایک کوشش دی جائے گی۔ جو بلندی عبور کرے گا وہ پہلی پوزیشن پر ہوگا۔',
           'که بیا هم برابري حل نه شي، که برابري د لومړي مقام لپاره وي، کراس بار به له وروستي لوړوالي دوه سانتي متره ښکته کېږي او یوه یوه هڅه ورکول کېږي. څوک چې لوړوالی تېر کړي، په لومړي مقام کې به وي.'),
          ('If the equality is for some other position, both players will be in the same position which they obtained; if second, then both will be counted second and third, both third.',
           'اگر برابری کسی دوسری پوزیشن کے لیے ہو تو دونوں کھلاڑی اسی پوزیشن پر ہوں گے جو انھوں نے حاصل کی اگر سیکنڈ ہے تو دونوں سیکنڈ اور تھرڈ ہو تو دونوں تھرڈ شمار کیے جائیں گے۔',
           'که برابري د کوم بل مقام لپاره وي، دواړه لوبغاړي به په همغه مقام کې وي چې ترلاسه کړی یې دی؛ که دویم وي، دواړه دویم او که درېیم وي، دواړه درېیم ګڼل کېږي.')])
    H = ['Name of player', '1.78cm', '1.82', '1.85', '1.88', '1.90', '1.94', 'Falier', 'Position']
    rows = [['A', '–', 'x0', '0', 'x0', '–', 'xxx', '4', '2='], ['B', '0', '0', '0', 'x–', 'x0', 'xxx', '4', '2='], ['C', '0', '0', 'x–', '0', 'xx0', 'xxx', '5', '4'], ['D', '0', '–', '–', 'xx0', 'xx0', 'xxx', '5', '1']]
    b.table('hpe12-highjump-result', H, rows, H, H, rows, rows)
    r = rec(b, 7, 9, 82)
    r['sourceNote'] = 'The sample result sheet is printed in English only and is reproduced as a structured table with its printed values (including the heading “Falier”).'
    BOOK.save(82, [(7, r)], issues=[{'id': 'hpe12-pdf082', 'unit': 7, 'printedPage': 77,
               'description': 'The sample result sheet is internally inconsistent as printed: D, with 5 failures, is placed 1st while A and B with 4 failures are “2=”; C with 5 failures is 4th. Header “Falier” (Failures). Owner pen strokes over the last column are excluded. “جن کی ناکامیوں تعداد”. Retained as printed.'}])


def p83():
    b = Builder()
    b.h('Skills of the high jump', 'اونچی چھلانگ کی مہارتیں', 'د لوړ ټوپ مهارتونه')
    P(b, [('The high jump is made in four different ways.', 'اونچی چھلانگ چار مختلف طریقوں سے لگائی جاتی ہے۔', 'لوړ ټوپ په څلورو بېلابېلو طریقو وهل کېږي.')])
    b.group('lines', [('1 Eastern roll', '1 ایسٹرن رول', '1 ختیځ رول'), ('2 Western roll', '2 ویسٹرن رول', '2 لوېدیځ رول'), ('3 Straddle roll', '3 سٹریڈل رول', '3 سټرېډل رول'), ('4 Fosbury flop', '4 فاسبری فلاپ', '4 فاسبري فلاپ')])
    b.h('1 Eastern roll', '1 ایسٹرن رول', '1 ختیځ رول')
    P(b, [('It is also called the scissors style. In it one leg goes forward and the other behind, moving like scissors, and the cross bar is crossed.', 'اسے قینچی سٹائل بھی کہتے ہیں۔ اس میں ایک ٹانگ آگے اور دوسری پیچھے قینچی کی طرح چلا کر کراس بار عبور کیا جاتا ہے۔', 'دې ته د قینچۍ سټایل هم ویل کېږي. په کې یوه پښه مخکې او بله شا ته د قینچۍ په څېر چلول کېږي او کراس بار تېرېږي.')])
    b.h('2 Western roll', '2 ویسٹرن رول', '2 لوېدیځ رول')
    P(b, [('In this style the jump is taken from the same foot on which one lands, and the help of both hands is obtained. The opposite foot of the foot from which the jump is made is brought over the cross bar with a powerful kick. The body is turned over the cross bar in such a way that the face turns towards the pit; landing is done on both feet.',
           'اس سٹائل میں جس پاؤں پر جمپ لیا جاتا ہے۔ اسی پر اترا جاتا ہے۔ اور دونوں ہاتھوں کی مدد حاصل کی جاتی ہے۔ جس پاؤں سے جمپ کیا جاتا ہے۔ اس کے مخالف پاؤں کو زوردار کک سے کراس بار کے اوپر لایا جاتا ہے۔ جسم کو کراس بار کے اوپر اس طرح موڑا جاتا ہے کہ منہ اکھاڑے کی طرف ہو جائے لینڈنگ دونوں پاؤں پر کی جاتی ہے۔',
           'په دې سټایل کې په کومه پښه چې ټوپ وهل کېږي، پر همغې کېناستل کېږي او د دواړو لاسونو مرسته اخیستل کېږي. د هغې پښې مخالفه پښه چې ټوپ پرې وهل کېږي، په زوروره لغته د کراس بار پاسه راوړل کېږي. بدن د کراس بار پاسه داسې اړول کېږي چې مخ یې کندې ته شي؛ کېناستل پر دواړو پښو کېږي.')])
    r = rec(b, 7, 10, 83)
    deco(r, 'Photographs of high jumpers clearing the bar (scissors style and a modern flop) are decorative.')
    BOOK.save(83, [(7, r)], issues=[{'id': 'hpe12-pdf083', 'unit': 7, 'printedPage': 78,
               'description': 'Owner Urdu ballpoint notes beside the list and at the foot are excluded. The western-roll description says landing is “on both feet” although it opens by saying one lands on the take-off foot. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 78
    {78: p78, 79: p79, 80: p80, 81: p81, 82: p82, 83: p83}[n]()
