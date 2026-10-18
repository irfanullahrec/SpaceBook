"""HPE XII PDF144–149: pp.140–145 — netball time keeper, team captain, skills (catching, passing); netball exercise; handball (court, goal area
line, court diagram, goal keeper line, free throw line, penalty line). Run: python class12_hpe_page144.py N (144–149)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T

Q_ = lambda x: (x, x, x)


def p144():
    b = Builder()
    P(b, [('… before, they enter the names of the players on the score sheet. When the umpire asks, they tell the account of the centre pass.', 'سے پہلے کھلاڑیوں کے نام سکور شیٹ پر درج کرتے ہیں۔ امپائر کے پوچھنے پر سنٹر پاس کا حساب بتاتے ہیں۔', '… مخکې د لوبغاړو نومونه د نمرو پر پاڼه ثبتوي. د امپایر په پوښتنه د منځني پاس حساب وايي.')])
    b.h('Time Keeper', 'ٹائم کیپر (Time Keeper)', 'وخت ساتونکی (Time Keeper)')
    P(b, [('For every game two time keepers are appointed who record the time of the start of every part of the game and keep account of the duration of the game.', 'ہر گیم کیلئے دو ٹائم کیپر مقرر کیے جاتے ہیں جو کھیل کے ہر حصے کے آغاز کا وقت درج کرتے ہیں اور کھیل کے دورانیہ کا حساب رکھتے ہیں۔', 'د هرې لوبې لپاره دوه وخت ساتونکي ټاکل کېږي چې د لوبې د هرې برخې د پیل وخت ثبتوي او د لوبې د مودې حساب ساتي.')])
    b.h('Team Captain', 'ٹیم کپتان (Team Captain)', 'د ټیم کپتان (Team Captain)')
    P(b, [('After winning the toss he informs the umpire about the choice of goal post and the decision of starting the game with the centre pass. During the game he informs the umpire of the decision of bringing in a substitute player and changing the position of a player. Only the captain is authorised to talk to the umpire.', 'ٹاس جیتنے کے بعد امپائر کو گول پوسٹ کے انتخاب اور سنٹر پاس سے گیم شروع ہونے کے فیصلے کے بارے میں آگاہ کرتا ہے۔ کھیل کے دوران متبادل کھلاڑی کا لانا اور کھلاڑی کی پوزیشن کو تبدیل کرنے کے فیصلے سے امپائر کو آگاہ کرتا ہے۔ صرف کپتان ہی امپائر سے بات کرنے کا مجاز ہوتا ہے۔', 'له ټاس ګټلو وروسته امپایر د ګول ستنې د ټاکنې او له منځني پاس د لوبې د پیل د پرېکړې په اړه خبروي. د لوبې پر مهال د بدیل لوبغاړي د راوستلو او د لوبغاړي د ځای د بدلولو له پرېکړې امپایر خبروي. یوازې کپتان له امپایر سره د خبرو واک لري.')])
    b.h('Skills of netball', 'نیٹ بال کی مہارتیں', 'د نېټبال مهارتونه')
    b.h('Catching the ball with both hands', 'دونوں ہاتھوں سے بال کو پکڑنا', 'په دواړو لاسونو توپ نیول')
    P(b, [('Open the fingers of both hands; extending both arms towards the ball, as soon as the ball comes into the hands, take your body and arms backwards. In this way the ball, instead of bouncing in the hands, will be gripped correctly. To save the fingers from injury do not create stiffness in the fingers.', 'دونوں ہاتھوں کی انگلیاں کھولیں دونوں بازوؤں کو گیند کی طرف بڑھا کر جونہی گیند ہاتھوں میں آئے اپنے جسم اور بازوؤں کو پیچھے کی طرف لے جائیں اس طرح گیند ہاتھوں میں اُچھلنے کی بجائے صحیح گرِپ ہوگا۔ انگلیوں کو چوٹ سے بچانے کیلئے انگلیوں میں اکڑاؤ پیدا نہ کریں۔', 'د دواړو لاسونو ګوتې خلاصې کړئ، دواړه مټې توپ ته وغځوئ او څنګه چې توپ لاسونو ته راشي، خپل بدن او مټې شا ته یوسئ. په دې ډول توپ په لاسونو کې د ټوپ وهلو پر ځای سم نیول کېږي. د ګوتو له ټپ د ژغورنې لپاره ګوتې مه کلکوئ.')])
    b.h('Catching the ball with one hand', 'ایک ہاتھ سے بال کو پکڑنا', 'په یوه لاس توپ نیول')
    P(b, [('In this skill the player stretches out one arm and catches the ball with the same hand, because with one hand the ball can be caught even from a greater distance.', 'اس مہارت میں کھلاڑی اپنا ایک بازو پھیلا کر اسی ہاتھ سے گیند پکڑتا ہے کیونکہ ایک ہاتھ سے گیند زیادہ دوری سے بھی پکڑا جا سکتا ہے۔', 'په دې مهارت کې لوبغاړی یوه مټ غځوي او په همغه لاس توپ نیسي، ځکه په یوه لاس توپ له ډېر لرې هم نیول کېدای شي.')])
    r = rec(b, 7, 61, 144)
    BOOK.save(144, [(7, r)], issues=[{'id': 'hpe12-pdf144', 'unit': 7, 'printedPage': 140,
               'description': 'The first line is cut at the top of the scan (“… سے پہلے”). An owner ballpoint signature and date are excluded.'}])


def p145():
    b = Builder()
    b.h('Passing with both hands', 'دونوں ہاتھوں سے پاس کرنا', 'په دواړو لاسونو پاس')
    P(b, [('With both hands give the ball to your partner in line with the shoulder; in this both hands should be behind the ball, and pass the ball with the equal strength of both arms.', 'دونوں ہاتھوں سے بال کو کندھے کی سیدھ سے اپنے ساتھی کو دیں اس میں دونوں ہاتھ بال کے پیچھے ہوں اور دونوں بازوؤں کی مساوی طاقت سے بال کو پاس کریں۔', 'په دواړو لاسونو توپ د اوږې په سیده خپل ملګري ته ورکړئ؛ په دې کې دواړه لاسونه دې د توپ شا ته وي او د دواړو مټو په برابر ځواک توپ پاس کړئ.')])
    b.h('Passing the ball with one hand', 'ایک ہاتھ سے بال کو پاس کرنا', 'په یوه لاس د توپ پاس')
    P(b, [('The pass is given from above the shoulder with force according to need. This pass is given for throwing far or at the time of a throw-in.', 'کندھے کے اوپر سے ضرورت کے مطابق زور سے پاس دیا جاتا ہے۔ دور پھینکنے یا تھرو ان کے وقت یہ پاس دیا جاتا ہے۔', 'له اوږې پورته د اړتیا سره سم په زور پاس ورکول کېږي. د لرې غورځولو یا تھرو ان پر وخت دا پاس ورکول کېږي.')])
    b.h('Pivot Pass', 'پیوٹ پاس (Pivot Pass)', 'پیوټ پاس (Pivot Pass)')
    P(b, [('In this the ball is given by turning on one foot, while the second foot remains with the ground.', 'اس میں ایک پاؤں پر گھوم کر بال دیا جاتا ہے جبکہ دوسرا پاؤں زمین کے ساتھ رہتا ہے۔', 'په دې کې پر یوه پښه تاوېږي او توپ ورکول کېږي، په داسې حال کې چې دویمه پښه له ځمکې سره پاتې کېږي.')])
    b.h('Bounce pass', 'ٹپہ پاس', 'ټپه پاس')
    P(b, [('Looking at the position of one’s player, the ball is bounced in such a way that the ball reaches one’s partner.', 'اپنے کھلاڑی کی پوزیشن کو دیکھتے ہوئے اس طرح بال کو ٹپہ دیا جاتا ہے کہ بال اپنے ساتھی کے پاس پہنچے۔', 'د خپل لوبغاړي ځای ته په کتو توپ داسې ټپه کېږي چې ملګري ته ورسېږي.')])
    r = rec(b, 7, 62, 145)
    BOOK.save(145, [(7, r)])


def p146():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The minimum weight of the netball is ________ grams.', 'نیٹ بال کا وزن کم سے کم ________ گرام ہوتا ہے۔', 'د نېټبال توپ لږ تر لږه وزن ________ ګرامه وي.'), [Q_('297'), Q_('397'), Q_('497'), Q_('597')]),
         (('In netball the diameter of the central circle is ________ feet.', 'نیٹ بال میں وسطی دائرہ کا قطر ________ فٹ ہوتا ہے۔', 'په نېټبال کې د منځنۍ دایرې قطر ________ فټه وي.'), [Q_('3'), Q_('5'), Q_('7'), Q_('9')]),
         (('In netball the game is started with ________ .', 'نیٹ بال میں کھیل کا آغاز ________ سے کیا جاتا ہے۔', 'په نېټبال کې لوبه په ________ پیلېږي.'), [('centre pass', 'سنٹر پاس', 'منځنی پاس'), ('centre third', 'سنٹر تھرڈ', 'منځنۍ درېیمه برخه'), ('centre forward', 'سنٹر فارورڈ', 'منځنی مخکښ'), ('goal throw', 'گول تھرو', 'ګول غورځونه')]),
         (('In the game of netball it is necessary to pass within ________ seconds.', 'نیٹ بال کے گیم میں ________ سیکنڈ کے اندر پاس کرنا ضروری ہے۔', 'د نېټبال په لوبه کې په ________ ثانیو کې پاس اړین دی.'), [Q_('3'), Q_('5'), Q_('7'), Q_('9')]),
         (('The breadth of the netball court is ________ feet.', 'نیٹ بال کورٹ کی چوڑائی ________ فٹ ہوتی ہے۔', 'د نېټبال د میدان پلنوالی ________ فټه وي.'), [Q_('40'), Q_('50'), Q_('60'), Q_('70')]),
         (('In the game of netball the number of players is ________ .', 'نیٹ بال کے کھیل میں کھلاڑیوں کی تعداد ________ ہوتی ہے۔', 'د نېټبال په لوبه کې د لوبغاړو شمېر ________ وي.'), [Q_('3'), Q_('5'), Q_('7'), Q_('9')]),
         (('The length of the netball court is ________ feet.', 'نیٹ بال کورٹ کی لمبائی ________ فٹ ہوتی ہے۔', 'د نېټبال د میدان اوږدوالی ________ فټه وي.'), [Q_('60'), Q_('80'), Q_('100'), Q_('120')]),
         (('The middle part of the netball court is called ________ .', 'نیٹ بال کورٹ کا درمیانی حصہ ________ کہلاتا ہے۔', 'د نېټبال د میدان منځنۍ برخه ________ بلل کېږي.'), [('centre third', 'سنٹر تھرڈ', 'منځنۍ درېیمه برخه'), ('wing defence', 'ونگ ڈیفنس', 'وینګ دفاع'), ('goal third', 'گول تھرڈ', 'د ګول درېیمه برخه'), ('centre', 'سنٹر', 'منځ')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['i.', 'ii.', 'iii.', 'iv.', 'v.', 'vi.', 'vii.', 'viii.'][i], q, o, per_line=4)
    r = BOOK.record(e, 'hpe12-ch7-exercise-netball-1', 'Chapter 7 exercise: netball (1)', 'باب ۷: مشقی سوالات — نیٹ بال (۱)', '۷ څپرکی: تمریني پوښتنې — نېټبال (۱)', 146, [142])
    BOOK.save(146, [(7, r)], issues=[{'id': 'hpe12-pdf146', 'unit': 7, 'printedPage': 142, 'description': 'Owner ballpoint ticks on the options are excluded. Retained as printed.'}])


def p147():
    e = Builder()
    Q = [(('The circumference of the ball in netball is ________ inches.', 'نیٹ بال میں بال کا محیط ________ انچ ہوتا ہے۔', 'په نېټبال کې د توپ محیط ________ انچه وي.'), [Q_('27″'), Q_('30″'), Q_('33″'), Q_('35')]),
         (('In netball the height of the ring is ________ feet.', 'نیٹ بال میں رنگ کی اونچائی ________ فٹ ہوتی ہے۔', 'په نېټبال کې د کړۍ لوړوالی ________ فټه وي.'), [Q_("6'"), Q_("8'"), Q_("10'"), Q_('12')]),
         (('In netball the radius of the shooting circle is ________ feet.', 'نیٹ بال میں شوٹنگ سرکل کا ________ فٹ نصف قطر ہوتا ہے۔', 'په نېټبال کې د ویشتو دایرې نیم قطر ________ فټه وي.'), [Q_("14'"), Q_("16'"), Q_("18'"), Q_('20')]),
         (('In netball the diameter of the ring is ________ centimetres.', 'نیٹ بال میں رنگ کا قطر ________ سینٹی میٹر ہوتا ہے۔', 'په نېټبال کې د کړۍ قطر ________ سانتي متره وي.'), [Q_('38'), Q_('40'), Q_('42'), Q_('44')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['ix', 'x.', 'xi.', 'xii.'][i], q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. Draw an outline of the netball court and make clear the positions of the players.', 'i۔ نیٹ بال کورٹ کا خاکہ بنا کر کھلاڑیوں کی پوزیشن واضح کریں۔', 'i. د نېټبال د میدان خاکه جوړه کړئ او د لوبغاړو ځایونه روښانه کړئ.'),
                      ('ii. Write the names and duties of the officials of the game of netball.', 'ii۔ نیٹ بال کھیل کے عہدیداران کے نام اور فرائض لکھیں۔', 'ii. د نېټبال د لوبې د چارواکو نومونه او دندې ولیکئ.'),
                      ('iii. Explain the following: 1) the centre pass in netball; 2) off side in netball.', 'iii۔ درج ذیل کی وضاحت کریں: 1) نیٹ بال میں سنٹر پاس 2) نیٹ بال میں آف سائیڈ', 'iii. لاندې روښانه کړئ: 1) په نېټبال کې منځنی پاس؛ 2) په نېټبال کې اف سایډ.')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-netball-2', 'Chapter 7 exercise: netball (2)', 'باب ۷: مشقی سوالات — نیٹ بال (۲)', '۷ څپرکی: تمریني پوښتنې — نېټبال (۲)', 147, [143])
    BOOK.save(147, [(7, r)], issues=[{'id': 'hpe12-pdf147', 'unit': 7, 'printedPage': 143,
               'description': 'A large owner Urdu scribble beside the questions and ticks are excluded. Q(ix) heading is faint at the top of the scan. Option marks (″, \') are printed inconsistently. Retained as printed.'}])


def hb_court(cap):
    b = ('<rect x="20" y="40" width="560" height="300" fill="#1e3a8a"/><rect x="40" y="60" width="520" height="260" fill="#3b82f6" stroke="#fff" stroke-width="2"/>'
         '<line x1="300" y1="60" x2="300" y2="320" stroke="#fff" stroke-width="2"/>'
         '<path d="M40 110 Q140 110 140 190 Q140 270 40 270" fill="#0f172a" stroke="#fff" stroke-width="2"/><path d="M560 110 Q460 110 460 190 Q460 270 560 270" fill="#0f172a" stroke="#fff" stroke-width="2"/>'
         '<path d="M40 85 Q190 85 190 190 Q190 295 40 295" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="6 4"/><path d="M560 85 Q410 85 410 190 Q410 295 560 295" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="6 4"/>'
         '<rect x="28" y="170" width="14" height="40" fill="#fff"/><rect x="558" y="170" width="14" height="40" fill="#fff"/>')
    for t, x, y in [('40m', 300, 30), ('GOAL KEEPER LINE', 120, 30), ('INTERCHANGE AREA', 300, 52), ('GOAL AREA', 470, 30), ('GOAL (2m HIGH)', 560, 30), ('20m', 12, 190), ('6m', 585, 140), ('3m', 585, 190),
                    ('PENALTY LINE', 160, 360), ('CENTRE LINE', 300, 360), ('FREE THROW LINE', 440, 360)]:
        b += T(x, y, t, 10, 'bold', 'middle', '#1e293b')
    return svg(620, 375, b, cap)


def p148():
    b = Builder()
    b.h('Handball', 'ہینڈ بال', 'هېنډبال')
    P(b, [('Handball is a game played between two teams. At the international level this game is played on an indoor court. Every team consists of at most 12 players, of whom seven (7) players can play during the match. The measurements of the rectangular court are as follows.', 'ہینڈ بال دو ٹیموں کے مابین کھیلا جانے والا کھیل ہے۔ بین الاقوامی سطح پر یہ کھیل ان ڈور کورٹ میں کھیلا جاتا ہے۔ ہر ٹیم زیادہ سے زیادہ 12 کھلاڑیوں پر مشتمل ہوتی ہے جن میں سے میچ کے دوران سات (7) کھلاڑی کھیل سکتے ہیں۔ مستطیل شکل کے کورٹ کی پیمائش مندرجہ ذیل ہے۔', 'هېنډبال د دوو ټیمونو ترمنځ لوبه ده. په نړیواله کچه دا لوبه په سرپټ میدان کې لوبول کېږي. هر ټیم ډېر تر ډېره له ۱۲ لوبغاړو جوړ وي چې د لوبې پر مهال یې اوه (۷) لوبغاړي لوبه کولی شي. د مستطیل ډوله میدان اندازې دا دي.')])
    b.group('lines', [('Length 40 metres', 'لمبائی 40 میٹر', 'اوږدوالی ۴۰ متره'), ('Breadth 20 metres', 'چوڑائی 20 میٹر', 'پلنوالی ۲۰ متره')])
    b.h('Goal area line', 'گول ایریا لائن', 'د ګول د سیمې کرښه')
    P(b, [('Parallel to the goal post, at a distance of six metres, a six-metre line is drawn. Then taking every goal post as the centre an arc of 6-metre radius will be drawn. Except for the goal keeper, the entry of all players into this area is prohibited.', 'گول پوسٹ کے متوازی، چھ میٹر کے فاصلے پر چھ میٹر لائن لگائی جاتی ہے۔ پھر ہر گول پوسٹ کو مرکز مان کر 6 میٹر نصف قطر کی قوس لگائی جائے گی گول کیپر کے علاوہ اس ایریا میں تمام کھلاڑیوں کا داخلہ ممنوع ہے۔', 'د ګول ستنې ته موازي، په شپږ متره واټن شپږ متره کرښه کښل کېږي. بیا هره ګول ستنه مرکز ګڼل کېږي او د ۶ مترو نیم قطر کمان کښل کېږي. له ګول ساتونکي پرته دې سیمې ته د ټولو لوبغاړو ننوتل منع دي.')])
    r = rec(b, 7, 63, 148)
    deco(r, 'A photograph of a handball player shooting at goal against defenders is decorative.')
    BOOK.save(148, [(7, r)])


def p149():
    b = Builder()
    sv = [hb_court(c) for c in ('Handball court (labels as printed)', 'ہینڈ بال کورٹ', 'د هېنډبال میدان')]
    b.visual('hpe12-fig-handball-court', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Goal keeper border line', 'گول کیپر بارڈر لائن', 'د ګول ساتونکي پوله کرښه')
    P(b, [('Parallel to the goal line at a distance of 4 metres a 15-centimetre-long line will be drawn. The goal keeper cannot come ahead of this line.', 'گول لائن کے متوازی 4 میٹر کے فاصلے پر 15 سینٹی میٹر لمبی لائن لگائی جائے گی۔ گول کیپر اس لائن سے آگے نہیں آ سکتا۔', 'د ګول کرښې ته موازي په ۴ متره واټن ۱۵ سانتي متره اوږده کرښه کښل کېږي. ګول ساتونکی له دې کرښې مخکې نه شي راتلی.')])
    b.h('Free throw line', 'فری تھرو لائن', 'د وړیا غورځونې کرښه')
    P(b, [('At a distance of 3 metres outside the goal area, at a distance of 9 metres from the goal line, a line will be drawn; this is a broken line.', 'گول ایریا کے باہر 3 میٹر کے فاصلے پر، گول لائن سے 9 میٹر کے فاصلے پر لائن لگائی جائے گی یہ ٹوٹی ہوئی لائن ہوتی ہے۔', 'د ګول له سیمې بهر په ۳ متره واټن، له ګول کرښې په ۹ متره واټن کرښه کښل کېږي؛ دا ماته (ټکي‌ټکي) کرښه وي.')])
    b.h('Penalty line or 7-metre line', 'پنلٹی لائن یا 7 میٹر لائن', 'د پنالټي کرښه یا ۷ متره کرښه')
    P(b, [('At a distance of 7 metres from the goal line, from the middle of the goal post, a 15-centimetre line is drawn inside the court.', 'گول لائن سے 7 میٹر کے فاصلے پر گول پوسٹ کے وسط سے 15 سینٹی میٹر کی لائن کورٹ کے اندر لگائی جاتی ہے۔', 'له ګول کرښې په ۷ متره واټن، د ګول ستنې له منځه ۱۵ سانتي متره کرښه د میدان دننه کښل کېږي.')])
    r = rec(b, 7, 64, 149)
    BOOK.save(149, [(7, r)], issues=[{'id': 'hpe12-pdf149', 'unit': 7, 'printedPage': 145,
               'description': 'The handball court illustration is reproduced as a coded schematic with its printed English labels. The goal-keeper line and penalty line are both given as 15 cm long. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 144
    {144: p144, 145: p145, 146: p146, 147: p147, 148: p148, 149: p149}[n]()
