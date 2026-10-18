"""HPE XII PDF102–107: pp.97–102 — badminton net, shuttlecock, racket, players, toss, scoring, game, singles, faults, other rules, LET, officials,
skills (service, smash, rally, idea). Run: python class12_hpe_page102.py N (102–107)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L


def p102():
    b = Builder()
    b.h('Net', 'نیٹ (Net)', 'جال (Net)')
    b.group('lines', [('Length of the net = 6.65 metres', 'نیٹ کی لمبائی = 6.65 میٹر', 'د جال اوږدوالی = ۶.۶۵ متره'), ('Breadth of the net = 2′-6″ (0.76 metres)', 'نیٹ کی چوڑائی = 2′-6″ 0.76 میٹر', 'د جال پلنوالی = 2′-6″ (۰.۷۶ متره)'),
                      ('Height of the net = 5 feet in the middle and 5′-1″ at the poles', 'نیٹ کی اونچائی = درمیان میں 5 فٹ اور پول کے ساتھ 5′-1″', 'د جال لوړوالی = په منځ کې ۵ فټه او له ستنو سره 5′-1″')])
    b.h('Shuttlecock', 'شٹل کاک', 'شټل کاک')
    b.group('lines', [('Weight of the shuttlecock 4.7 to 5.5 grams', 'شٹل کاک کا وزن 4.7 سے 5.5 گرام', 'د شټل کاک وزن ۴.۷ تر ۵.۵ ګرامه'), ('Number of feathers 14–16 and length 2.8 inches', 'پروں کی تعداد 14–16 تک اور لمبائی 2.8 انچ', 'د بڼکو شمېر ۱۴–۱۶ او اوږدوالی ۲.۸ انچه')])
    b.h('Racket', 'ریکٹ', 'ریکټ')
    b.group('lines', [('Length of the racket 26 inches', 'ریکٹ کی لمبائی 26 انچ', 'د ریکټ اوږدوالی ۲۶ انچه'), ('Weight of the racket 128 grams', 'ریکٹ کا وزن 128 گرام', 'د ریکټ وزن ۱۲۸ ګرامه')])
    b.h('Players', 'کھلاڑی', 'لوبغاړي')
    P(b, [('In doubles 2, 2 players play and for singles there is one player each. The serving team is called “in” and the receiving one “out”.', 'ڈبلز میں 2،2 کھلاڑی کھیلتے ہیں اور سنگلز کیلئے ایک ایک کھلاڑی ہوتا ہے۔ سروس والی ٹیم کو ”ان“ اور وصول کرنے والی کو ”آؤٹ“ کہتے ہیں۔', 'په جوړه لوبه کې ۲، ۲ لوبغاړي لوبه کوي او په یوازې لوبه کې یو یو لوبغاړی وي. سرویس کوونکي ټیم ته "ان" او اخیستونکي ته "اوټ" ویل کېږي.')])
    b.h('Toss', 'ٹاس (Toss)', 'ټاس (Toss)')
    P(b, [('The team winning the toss has the right to take the service or the side.', 'ٹاس جیتنے والی ٹیم کو حق حاصل ہے کہ سروس لے یا سائیڈ لے۔', 'ټاس ګټونکی ټیم حق لري چې سرویس واخلي یا اړخ واخلي.')])
    b.h('Scoring', 'سکورنگ', 'نمرې')
    P(b, [('According to the new law of badminton the set will be of 21 points and five sets will be played. If 20, 20 points are equal, then the team making two consecutive points will win; a point will be given on every error.', 'بیڈمنٹن کے نئے قانون کے مطابق 21 پوائنٹ کا سیٹ ہوگا اور پانچ سیٹ کھیلے جائیں گے۔ اگر 20،20 پوائنٹ برابر ہوں تو دو پوائنٹ لگاتار بنانے والی ٹیم جیت جائے گی ہر غلطی پر پوائنٹ ملے گا۔', 'د بډمنټن د نوي قانون له مخې سیټ به د ۲۱ نمرو وي او پنځه سیټه به لوبول کېږي. که ۲۰، ۲۰ نمرې برابرې وي، هغه ټیم ګټي چې پرلپسې دوه نمرې جوړې کړي؛ په هره تېروتنه نمره ورکول کېږي.')])
    r = rec(b, 7, 25, 102)
    BOOK.save(102, [(7, r)], issues=[{'id': 'hpe12-pdf102', 'unit': 7, 'printedPage': 97,
               'description': 'The scoring rule says “five sets will be played” (as printed; the BWF format is best of three). Retained as printed.'}])


def p103():
    b = Builder()
    b.h('Game', 'کھیل', 'لوبه')
    L(b, [('After the toss, the player of the serving team will serve diagonally from the right service court to the opposing player in the right service court.', 'ٹاس کے بعد سروس کرنے والی ٹیم کا کھلاڑی دائیں سروس کورٹ سے مخالف کھلاڑی کو دائیں سروس کورٹ میں وتری سروس کرے گا۔', 'له ټاس وروسته د سرویس کوونکي ټیم لوبغاړی به له ښي سرویس میدان مخالف لوبغاړي ته په ښي سرویس میدان کې وتري (اریب) سرویس کوي.'),
          ('Only the receiver of the service will return the service. If his partner touches or plays the shuttle, a point will be scored for the serving team.', 'صرف سروس وصول کرنے والا سروس کو واپس کرے گا۔ اگر اس کے ساتھی نے شٹل کو چھوا یا کھیلا تو سروس کرنے والی ٹیم کا ایک پوائنٹ سکور ہو جائے گا۔', 'یوازې سرویس اخیستونکی به سرویس بېرته ورکوي. که ملګري یې شټل ولمسوه یا یې ولوباوه، د سرویس کوونکي ټیم یوه نمره جوړېږي.'),
          ('After the return of the service any player of the serving team can play the shuttle, and in this way the game will continue.', 'سروس کی واپسی کے بعد سروس کرنے والی ٹیم کا کوئی بھی کھلاڑی شٹل کو کھیل سکتا ہے۔ اور اسی طرح کھیل جاری رہے گا۔', 'د سرویس له بېرته راتګ وروسته د سرویس کوونکي ټیم هر لوبغاړی شټل لوبولی شي او همداسې لوبه دوام کوي.'),
          ('After returning the service the players can play at any position in their part of the court.', 'سروس واپس کرنے کے بعد کھلاڑی کورٹ کے اپنے حصے میں کسی بھی پوزیشن پر کھیل سکتے ہیں۔', 'د سرویس له بېرته ورکولو وروسته لوبغاړي د میدان په خپله برخه کې په هر ځای لوبه کولی شي.'),
          ('If the team receiving the service commits a foul, a point will be scored for the serving team and the server will serve again.', 'اگر سروس وصول کرنے والی ٹیم کوئی فاؤل کرتی ہے تو سروس کرنے والی ٹیم کا ایک پوائنٹ سکور ہوگا اور سروس کرنے والا دوبارہ سروس کرے گا۔', 'که سرویس اخیستونکی ټیم خطا وکړي، د سرویس کوونکي ټیم یوه نمره جوړېږي او سرویس کوونکی بیا سرویس کوي.'),
          ('When the service is given to the opposing team, they too will keep serving from the right and left sides. When the first service is lost, the second service will be given. The service will be returned to the player to whom it is given. If the service falls correctly in the opposing court touching the net, it will be declared LET.', 'جب سروس مخالف ٹیم کو دی جائے گی تو وہ بھی دائیں اور بائیں حصہ سے سروس کرتے رہیں گے۔ پہلی سروس ضائع ہونے پر دوسری سروس دی جائے گی۔ سروس جس کھلاڑی کی طرف کی جائے گی وہی واپس کرے گا اگر سروس نیٹ کو چھو کر مخالف کورٹ میں درست گرے تو LET قرار دی جائے گی۔', 'کله چې سرویس مخالف ټیم ته ورکړل شي، هغوی به هم له ښي او کیڼ اړخه سرویس کوي. د لومړي سرویس په ضایع کېدو دویم سرویس ورکول کېږي. سرویس چې کوم لوبغاړي ته کېږي، همغه به یې بېرته ورکوي. که سرویس جال ولمسوي او په مخالف میدان کې سم ولوېږي، LET اعلانېږي.')])
    b.h('The singles game', 'سنگلز کا کھیل', 'یوازینۍ لوبه')
    L(b, [('The start of the game, i.e. the service, will be made from the right court.', 'کھیل کا آغاز یعنی سروس دائیں کورٹ سے کیا جائے گا۔', 'د لوبې پیل، یعنې سرویس، به له ښي میدان کېږي.'),
          ('When the score is even the service will be from the right court and when odd from the left court.', 'جب سکور جفت ہوگا تو سروس دائیں کورٹ سے اور طاق ہو تو بائیں کورٹ سے سروس ہوگی۔', 'کله چې نمرې جفت وي، سرویس به له ښي میدان او کله چې طاق وي، له کیڼ میدان وي.'),
          ('If the player receiving the service commits some foul, it will be counted a point for the server, and he will now serve from the other court.', 'اگر سروس وصول کرنے والا کھلاڑی کوئی فاؤل کرے تو سروس کرنے والے کا ایک پوائنٹ شمار ہوگا اور وہ اب دوسرے کورٹ سے سروس کرے گا۔', 'که سرویس اخیستونکی لوبغاړی خطا وکړي، د سرویس کوونکي یوه نمره ګڼل کېږي او اوس به له بل میدان سرویس کوي.'),
          ('If the server commits some foul, the right to serve is given to the opposing player, and in this way no addition will be made in anyone’s score.', 'اگر سروس کرنے والا کوئی فاؤل کرتا ہے تو سروس کرنے کا حق مخالف کھلاڑی کو دیا جاتا ہے اور اس طرح کسی کے سکور میں کوئی اضافہ نہیں ہوگا۔', 'که سرویس کوونکی خطا وکړي، د سرویس حق مخالف لوبغاړي ته ورکول کېږي او په دې ډول د هېچا په نمرو کې زیاتوالی نه راځي.')])
    r = rec(b, 7, 26, 103)
    BOOK.save(103, [(7, r)], issues=[{'id': 'hpe12-pdf103', 'unit': 7, 'printedPage': 98,
               'description': 'The last singles rule (no point on a server’s fault) contradicts the rally-point scoring stated on p.97. Retained as printed.'}])


def p104():
    b = Builder()
    b.h('Faults', 'غلطیاں', 'تېروتنې')
    P(b, [('In the game of badminton, if the serving team commits some fault, the service will be given to the other team, and if the team receiving the service commits a fault, the serving team will get a point. According to the new law both the service and the point will be together, and on every fault the point will be given to the opposing team.',
           'بیڈمنٹن کے کھیل میں سروس کرنے والی ٹیم اگر کوئی غلطی کرے گا تو سروس دوسری ٹیم کو دی جائے گی اور اگر سروس وصول کرنے والی ٹیم غلطی کرے تو سروس کرنے والی ٹیم کو ایک پوائنٹ حاصل ہو جائیگا۔ نئے قانون کے مطابق سروس اور پوائنٹ دونوں ہوں گے اور ہر غلطی پر مخالف ٹیم کو پوائنٹ دیا جائے گا۔',
           'د بډمنټن په لوبه کې که سرویس کوونکی ټیم کومه تېروتنه وکړي، سرویس به بل ټیم ته ورکول کېږي او که سرویس اخیستونکی ټیم تېروتنه وکړي، سرویس کوونکی ټیم به یوه نمره ترلاسه کوي. د نوي قانون له مخې سرویس او نمره دواړه وي او په هره تېروتنه به مخالف ټیم ته نمره ورکول کېږي.'),
          ('The faults are as follows.', 'غلطیاں مندرجہ ذیل ہیں۔', 'تېروتنې دا دي.')])
    L(b, [('While serving, the shuttle is higher than the waist of the player.', 'سروس کرتے وقت شٹل کھلاڑی کی کمر سے اونچی ہو۔', 'د سرویس پر وخت شټل د لوبغاړي له ملا لوړ وي.'), ('After the service the shuttle goes into the wrong court.', 'سروس کے بعد شٹل غلط کورٹ میں جائے۔', 'له سرویس وروسته شټل ناسم میدان ته لاړ شي.'),
          ('The shuttle passes through or under the net.', 'شٹل نیٹ کے اندر سے یا نیچے سے گزرے۔', 'شټل له جال دننه یا لاندې تېر شي.'), ('The shuttle falls outside the boundaries of the court.', 'شٹل کورٹ کے حدود سے باہر گرے۔', 'شټل د میدان له پولو بهر ولوېږي.'),
          ('The shuttle touches the ceiling or the surrounding walls.', 'شٹل چھت یا اطراف کی دیواروں کو ٹچ کرے۔', 'شټل چت یا شاوخوا دېوالونه ولمسوي.'), ('It touches the body or uniform of the player.', 'کھلاڑی کے جسم یا وردی کو چھوئے۔', 'د لوبغاړي بدن یا جامې ولمسوي.'),
          ('It touches some thing outside or near the court.', 'کورٹ کے باہر یا قریب کسی چیز کو چھوئے۔', 'له میدان بهر یا نږدې کوم شی ولمسوي.'), ('The shuttle comes to rest on the racket.', 'شٹل ریکٹ پر ساکن ہو جائے۔', 'شټل پر ریکټ ودرېږي.'),
          ('The player plays the shuttle twice.', 'کھلاڑی شٹل کو دو مرتبہ کھیلے۔', 'لوبغاړی شټل دوه ځله ولوبوي.'), ('Deliberately delaying in serving.', 'جان بوجھ کر سروس کرنے میں تاخیر کریں۔', 'په قصد په سرویس کې ځنډ.'),
          ('The shuttle is played before it crosses the net.', 'شٹل کو نیٹ کراس ہونے سے پہلے کھیلا جائے۔', 'شټل له جال له تېرېدو مخکې ولوبول شي.'), ('The shuttle gets stuck in the net.', 'شٹل نیٹ کے اندر پھنس جائے۔', 'شټل په جال کې ونښلي.'),
          ('The server or his partner feints the opponent.', 'سروس کرنے والا یا اس کا ساتھی مخالف کو جھانسہ دے۔', 'سرویس کوونکی یا ملګری یې مخالف وغولوي.'), ('During the game the body or racket touches the net.', 'کھیل کے دوران جسم یا ریکٹ نیٹ کو ٹچ ہو جائے۔', 'د لوبې پر مهال بدن یا ریکټ جال ولمسوي.')])
    r = rec(b, 7, 27, 104)
    BOOK.save(104, [(7, r)], issues=[{'id': 'hpe12-pdf104', 'unit': 7, 'printedPage': 99, 'description': '“سروس کرنے والی ٹیم اگر کوئی غلطی کرے گا”. Retained as printed.'}])


def p105():
    b = Builder()
    L(b, [('If two partners hit the shuttle at the same time.', 'اگر دو ساتھی بیک وقت شٹل کو مارے۔', 'که دوه ملګري په یو وخت شټل ووهي.'), ('The feet of the server are not in the correct service court, or the feet of the receiver are not in his own court.', 'سروس کرنے والے کھلاڑی کے پاؤں درست سروس کورٹ میں نہ ہوں۔ یا سروس وصول کرنے والے کے پاؤں اپنے کورٹ میں نہ ہوں۔', 'د سرویس کوونکي پښې په سم سرویس میدان کې نه وي، یا د سرویس اخیستونکي پښې په خپل میدان کې نه وي.'),
          ('In singles the service falls inside the short service line or outside the side.', 'سنگل میں سروس شارٹ سروس لائن کے اندر گرے یا سائیڈ کے باہر گرے۔', 'په یوازینۍ لوبه کې سرویس د لنډ سرویس کرښې دننه یا د څنګ بهر ولوېږي.'), ('In doubles the service falls in the back gallery.', 'ڈبلز میں سروس بیک گیلری میں گرے۔', 'په جوړه لوبه کې سرویس په شاتنۍ ګالري کې ولوېږي.')])
    b.h('Other rules', 'دیگر قواعد', 'نور قواعد')
    L(b, [('During the second and third game there will be an interval of 5 minutes.', 'دوسری اور تیسری گیم کے دوران 5 منٹ کا وقفہ ہوگا۔', 'د دویمې او درېیمې لوبې ترمنځ به ۵ دقیقې وقفه وي.'),
          ('Without the permission of the umpire a player can neither come into the court nor go out.', 'امپائر کی اجازت کے بغیر نہ کھلاڑی کورٹ کے اندر آ سکتا ہے اور نہ باہر جا سکتا ہے۔', 'د امپایر له اجازې پرته لوبغاړی نه میدان ته راتلی شي او نه بهر وتلی شي.'),
          ('The game will be stopped only in such a state when it is beyond the authority of the umpire or the player.', 'کھیل صرف ایسی حالت میں روکا جائے گا جب امپائر یا کھلاڑی کے دائرہ اختیار سے باہر ہو۔', 'لوبه به یوازې په داسې حالت کې درول کېږي چې د امپایر یا لوبغاړي له واکه بهر وي.'),
          ('During the match no player is allowed advice from outside.', 'کسی کھلاڑی کو میچ کے دوران باہر سے مشورے کی اجازت نہیں۔', 'د لوبې پر مهال هېڅ لوبغاړي ته له بهر مشورې اجازه نشته.'),
          ('In the case of team points there will be two singles matches, then one match will be of doubles. If there is no decision, then a reverse singles match will be held. According to the new rules the players who played the first singles cannot take part in the reverse; in this way there will be 6 players in the team and two players will play the reverse.', 'ٹیم پوائنٹ کی صورت میں دو سنگلز کے مقابلے ہوں گے پھر ایک مقابلہ ڈبلز کا ہوگا۔ اگر فیصلہ نہ ہوا تو ریورس سنگلز کا مقابلہ ہوگا۔ نئے قوانین کے مطابق پہلے سنگلز کھیلنے والے ریورس میں حصہ نہیں لے سکتے اس طرح ٹیم میں 6 کھلاڑی ہوں گے اور ریورس دو کھلاڑی کھیلیں گے۔', 'د ټیم نمرو په صورت کې به دوه یوازینۍ سیالۍ وي، بیا یوه سیالي د جوړې وي. که پرېکړه ونه شوه، د معکوسې یوازینۍ سیالي به وي. د نویو قوانینو له مخې د لومړۍ یوازینۍ لوبې لوبغاړي په معکوسه کې برخه نه شي اخیستی؛ په دې ډول به په ټیم کې ۶ لوبغاړي وي او معکوسه به دوه لوبغاړي لوبوي.')])
    b.h('LET will be in the following cases', 'لیٹ LET درج ذیل صورتوں میں ہوگا', 'LET به په لاندې حالتونو کې وي')
    L(b, [('If the opposing player is not ready.', 'اگر مخالف کھلاڑی تیار نہ ہوں۔', 'که مخالف لوبغاړی چمتو نه وي.'), ('In the case of some accident.', 'کسی حادثہ کی صورت میں۔', 'د کومې پېښې په صورت کې.'),
          ('Because of outside interference.', 'بیرونی مداخلت کی وجہ سے۔', 'د بهرنۍ لاسوهنې له امله.'), ('If the shuttle breaks.', 'شٹل ٹوٹ جائے۔', 'که شټل مات شي.'), ('If the electricity goes off.', 'بجلی بند ہو جائے۔', 'که برېښنا ولاړه شي.')])
    r = rec(b, 7, 28, 105)
    BOOK.save(105, [(7, r)])


def p106():
    b = Builder()
    L(b, [('If the shuttle, touching the net, falls in the opposing straight court.', 'شٹل نیٹ کو ٹچ ہو کر مخالف راست کورٹ میں گر جائے۔', 'که شټل جال ولمسوي او په مخالف مستقیم میدان کې ولوېږي.'), ('If the shuttle strikes the ceiling.', 'شٹل چھت سے ٹکرا جائے۔', 'که شټل له چت سره ټکر وکړي.'),
          ('If the lineman for some reason cannot see the play, then the umpire will give the decision of LET.', 'اگر لائن مین کسی وجہ سے کھیل نہ دیکھ سکے تو امپائر LET کا فیصلہ دے گا۔', 'که لاین‌مین په کوم دلیل لوبه ونه شي لیدلی، امپایر به د LET پرېکړه وکړي.')])
    b.h('Officials', 'عہدیداران (Officials)', 'چارواکي (Officials)')
    b.h('Referee', 'ریفری', 'ریفري')
    P(b, [('The referee is the overall supervisor of the tournament. He appoints all court officials and his decision is final.', 'ریفری ٹورنامنٹ کا بحیثیت مجموعی نگران ہوتا ہے۔ وہ تمام کورٹ آفیشلز مقرر کرتا ہے اور اس کا فیصلہ حتمی ہوتا ہے۔', 'ریفري د ټورنمنټ عمومي څارونکی وي. د میدان ټول چارواکي ټاکي او پرېکړه یې وروستۍ وي.')])
    b.h('Umpire', 'امپائر', 'امپایر')
    P(b, [('The umpire is the supervisor of the court and its surrounding environment and works under the supervision of the referee. He is appointed for a particular match. He announces the score. He decides faults and LET and determines suspension in play. Reporting against a player, hearing appeals during the play, rejecting or acting on the decisions of the line judges and service judges, and deciding disputed matters in time are the important responsibilities of the umpire.',
           'امپائر کورٹ اور اس کے ارد گرد ماحول کا نگران ہوتا ہے اور ریفری کے زیر نگرانی کام کرتا ہے۔ کسی مخصوص میچ کیلئے مقرر ہوتا ہے۔ سکور کا اعلان کرتا ہے۔ غلطی اور لیٹ (LET) کا فیصلہ کرتا ہے کھیل میں تعطل کا تعین کرتا ہے۔ کھلاڑی کے خلاف رپورٹ دینا اور کھیل کے دوران اپیل سننا، لائن ججز اور سروس ججز کے فیصلوں پر عمل کرنا یا مسترد کرنا اور متنازعہ امور کا فیصلہ وقت پر کرنا امپائر کی اہم ذمہ داریاں ہیں۔',
           'امپایر د میدان او شاوخوا چاپېریال څارونکی وي او د ریفري تر څارنې لاندې کار کوي. د یوې ځانګړې لوبې لپاره ټاکل کېږي. نمرې اعلانوي. د تېروتنې او LET پرېکړه کوي او په لوبه کې د ځنډ ټاکنه کوي. د لوبغاړي پر وړاندې راپور ورکول، د لوبې پر مهال استیناف اورېدل، د کرښې او سرویس قاضیانو پر پرېکړو عمل یا یې ردول او په شخړه‌ییزو چارو په وخت پرېکړه کول د امپایر مهم مسؤلیتونه دي.')])
    b.h('Line judge', 'لائن جج', 'د کرښې قاضي')
    P(b, [('Working under the supervision of the umpire, deciding whether the shuttle has fallen inside or outside the court, and signalling correct and out.', 'شٹل کا کورٹ کے اندر یا باہر گرنے کا فیصلہ کرنا امپائر کے زیرِ نگرانی کام کرنا درست اور آؤٹ کا اشارہ دینا۔', 'د امپایر تر څارنې لاندې کار کول، د میدان دننه یا بهر د شټل د لوېدو پرېکړه کول او د سم او اوټ اشاره ورکول.')])
    b.h('Service judge', 'سروس جج', 'د سرویس قاضي')
    P(b, [('The service judge stands opposite the umpire. He identifies a wrong service and calls out loudly “fault”.', 'سروس جج امپائر کے مخالف سمت میں کھڑا ہوتا ہے۔ غلط سروس کی نشاندہی کرتا ہے اور با آواز بلند ”فالٹ“ پکارتا ہے۔', 'د سرویس قاضي د امپایر مخالف لوري ته ولاړ وي. ناسم سرویس په ګوته کوي او په لوړ غږ "فالټ" وايي.')])
    r = rec(b, 7, 29, 106)
    BOOK.save(106, [(7, r)])


def p107():
    b = Builder()
    b.h('Skills of badminton', 'بیڈمنٹن کی مہارتیں', 'د بډمنټن مهارتونه')
    b.h('Skill of service', 'سروس کی مہارت', 'د سرویس مهارت')
    b.p('Serving high with the right hand:', 'سیدھے ہاتھ سے اونچی سروس کرنا:', 'په ښي لاس لوړ سرویس کول:')
    L(b, [('The player should be standing in his service court.', 'کھلاڑی اپنے سروس کورٹ میں کھڑا ہو۔', 'لوبغاړی دې په خپل سرویس میدان کې ولاړ وي.'), ('Both feet of the player should be on the ground.', 'کھلاڑی کا دونوں پاؤں زمین پر ہو۔', 'د لوبغاړي دواړه پښې دې پر ځمکه وي.'), ('Seeing the opposing player get ready.', 'مخالف کھلاڑی کے تیار ہونے کو دیکھنا۔', 'د مخالف لوبغاړي چمتووالی کتل.')])
    b.h('Serving backhand', 'الٹے ہاتھ سے سروس کرنا', 'په شا لاس سرویس کول')
    P(b, [('This service should be done with the backhand. Service is done by hitting the shuttle with a racket backstroke.', 'یہ سروس الٹے ہاتھ سے کی جائیں۔ ریکٹ بیک سٹروک سے شٹل پر مار کر سروس کیا جاتا ہے۔', 'دا سرویس دې په شا لاس وشي. د ریکټ په شا ګوزار پر شټل وهلو سرویس کېږي.')])
    b.h('Smashing', 'سمیش کرنا', 'سمیش کول')
    P(b, [('With whatever speed the shuttle is coming from the opposing court through the air at a height, keeping the balance of your body, bend the body slightly backwards and then take the hand back and smash the shuttle with force.', 'جس رفتار سے شٹل مخالف کورٹ سے آ رہی ہوا گر اونچائی پر آ رہی ہو تو اپنے جسم کا توازن برقرار رکھتے ہوئے جسم کو ذرا پیچھے کی طرف جھکائیں اور پھر ہاتھ کو پیچھے لے جا کر زور سے شٹل کو سمیش لگائیں۔', 'په هر سرعت چې شټل له مخالف میدان په لوړوالي راځي، د خپل بدن توازن وساتئ، بدن لږ شا ته کوږ کړئ او بیا لاس شا ته یوسئ او په زور شټل سمیش کړئ.')])
    b.h('Rally', 'ریلی', 'رېلي')
    P(b, [('During the rally care should be taken of footwork and of the reach of the opponent. The shuttle should not be hit again and again on one side only; rather the position of the opposing player should be disturbed. The shuttle should be thrown right and left, behind and in front, in the opposing court. Avoid too long a rally.', 'ریلی کے دوران فٹ ورک اور مخالف کی پہنچ کا خیال رکھنا چاہیے شٹل کو بار بار ایک ہی سائیڈ پر نہیں مارنا چاہیے۔ بلکہ مخالف کھلاڑی کی پوزیشن کو ڈسٹرب کرنا چاہیے شٹل کو دائیں بائیں اور آگے پیچھے مخالف کورٹ میں پھینکنا چاہیے۔ زیادہ لمبی ریلی سے گریز کریں۔', 'د رېلي پر مهال د پښو کار او د مخالف لاسرسي ته پام پکار دی. شټل دې بیا بیا یوازې یوه اړخ ته ونه وهل شي، بلکې د مخالف لوبغاړي حالت دې ګډوډ شي. شټل دې په مخالف میدان کې ښي کیڼ او مخکې شا ته وغورځول شي. له ډېرې اوږدې رېلي ډډه وکړئ.')])
    b.h('Idea (placement)', 'آئیڈیا', 'مفکوره (ځای‌پرځای کول)')
    P(b, [('One should form an idea by seeing the position of the opposing player. If he is far from the net, the shuttle should be dropped slowly near the net; if the opponent is near the net, then the shuttle should be thrown into the back zone.', 'مخالف کھلاڑی کی پوزیشن کو دیکھ کر آئیڈیا کرنا چاہیے اگر وہ نیٹ سے دور ہو تو نیٹ کے قریب شٹل کو آہستہ گرانا چاہیے اگر مخالف نیٹ کے قریب ہو تو شٹل کو بیک زون میں پھینکنا چاہیے۔', 'د مخالف لوبغاړي حالت ته په کتو مفکوره جوړه کړئ؛ که له جال لرې وي، شټل دې جال ته نږدې ورو وغورځول شي؛ که مخالف جال ته نږدې وي، شټل دې شاتنۍ ساحې ته وغورځول شي.')])
    r = rec(b, 7, 30, 107)
    BOOK.save(107, [(7, r)], issues=[{'id': 'hpe12-pdf107', 'unit': 7, 'printedPage': 102,
               'description': 'Owner ballpoint marks are excluded. “سیدھے ہاتھ” (right/forehand), “کھلاڑی کا دونوں پاؤں”, “مخالف کورٹ سے آ رہی ہوا گر”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 102
    {102: p102, 103: p103, 104: p104, 105: p105, 106: p106, 107: p107}[n]()
