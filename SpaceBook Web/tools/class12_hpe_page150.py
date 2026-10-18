"""HPE XII PDF150–157: pp.146–147, 149–153 (p.148 missing from the scan) — handball ball, dress, officials, duration, throw-off, playing the ball,
prohibitions, free throw, 7-metre throw, penalties, skills; handball exercise; about the authors (p.153); back cover (national anthem).
Run: python class12_hpe_page150.py N (150–157)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco

Q_ = lambda x: (x, x, x)


def p150():
    b = Builder()
    b.h('Ball', 'بال', 'توپ')
    P(b, [('A ball made of leather consisting of 32 panels will be used for the game.', 'چمڑے کا بنا ہوا 32 پینل پر مشتمل بال کھیل کے لیے استعمال ہوگا۔', 'له څرمن جوړ ۳۲ ټوټه‌ییز توپ به د لوبې لپاره کارول کېږي.')])
    H = (['Item', 'Women', 'Men'], ['شے', 'عورتوں کے لیے', 'مردوں کے لیے'], ['شی', 'ښځې', 'نارینه'])
    rows = [('Weight of the ball', 'بال کا وزن', 'د توپ وزن', ('325–400 grams', '325-400 گرام', '۳۲۵–۴۰۰ ګرامه'), ('425–475 grams', '425-475 گرام', '۴۲۵–۴۷۵ ګرامه')),
            ('Circumference of the ball', 'بال کا محیط', 'د توپ محیط', ('54–56 centimetres', '54-56 سینٹی میٹر', '۵۴–۵۶ سانتي متره'), ('58–60 centimetres', '58-60 سینٹی میٹر', '۵۸–۶۰ سانتي متره'))]
    b.table('hpe12-handball-ball', H[0], [[a, w[0], m[0]] for a, u, p, w, m in rows], H[1], H[2], [[u, w[1], m[1]] for a, u, p, w, m in rows], [[p, w[2], m[2]] for a, u, p, w, m in rows])
    b.h('Dress of the players', 'کھلاڑیوں کا لباس', 'د لوبغاړو جامې')
    P(b, [('The dress of the players for international competitions will consist of shorts and a shirt, whose colour will be the same. On the shirt numbers from 1 to 20 will be put. The goal keeper will use a uniform different from the team.', 'کھلاڑیوں کا لباس بین الاقوامی مقابلوں کے لیے نیکر اور شرٹ پر مشتمل ہوگا جس کا رنگ ایک جیسا ہوگا۔ شرٹ پر 1 سے 20 تک نمبر لگے ہوں گے۔ گول کیپر ٹیم سے الگ یونیفارم استعمال کرے گا۔', 'د نړیوالو سیالیو لپاره د لوبغاړو جامې له نیکر او کمیس جوړې وي چې رنګ یې یو شان وي. پر کمیس به له ۱ تر ۲۰ شمېرې لګېدلې وي. ګول ساتونکی به له ټیم جلا یونیفورم کاروي.')])
    b.h('Officials of the match', 'مقابلے کے آفیشلز', 'د سیالۍ چارواکي')
    P(b, [('The following officials will perform duties during the match.', 'مندرجہ ذیل آفیشلز میچ کے دوران فرائض انجام دیں گے۔', 'لاندې چارواکي به د لوبې پر مهال دندې ترسره کوي.')])
    b.h('Referee', 'ریفری', 'ریفري')
    P(b, [('For every match there will be one court referee and the second a goal line referee.', 'ہر مقابلے کے لیے ایک کورٹ ریفری اور دوسرا گول لائن ریفری ہوگا۔', 'د هرې سیالۍ لپاره به یو د میدان ریفري او دویم د ګول کرښې ریفري وي.')])
    b.h('Score keeper', 'سکور کیپر', 'نمره ساتونکی')
    P(b, [('During the game he will keep account of the score and will record the suspension of players on the score sheet.', 'کھیل کے دوران سکور کا حساب رکھے گا اور کھلاڑیوں کی معطلی کو سکور شیٹ پر درج کرے گا۔', 'د لوبې پر مهال به د نمرو حساب ساتي او د لوبغاړو ځنډول به د نمرو پر پاڼه ثبتوي.')])
    b.h('Time keeper', 'ٹائم کیپر', 'وخت ساتونکی')
    P(b, [('He will be responsible for the following matters.', 'مندرجہ ذیل امور کا ذمہ دار ہوگا۔', 'د لاندې چارو مسؤل به وي.')])
    L(b, [('He will give a clear signal at the end of half time.', 'ہاف ٹائم کے خاتمے پر واضح اشارہ دے گا۔', 'د نیم وخت په پای کې به روښانه اشاره ورکوي.')])
    r = rec(b, 7, 65, 150)
    r['sourceNote'] = 'The ball weights and circumferences for women and men are given as a structured table.'
    BOOK.save(150, [(7, r)])


def p151():
    b = Builder()
    L(b, [('He will keep account of stoppages in the game.', 'کھیل میں رکاوٹ کا حساب رکھے گا۔', 'په لوبه کې د ځنډونو حساب به ساتي.'), ('He will signal the end of the interval after half time.', 'ہاف ٹائم کے بعد وقفے کے ختم ہونے کا اشارہ کرے گا۔', 'له نیم وخت وروسته د وقفې د پای اشاره به کوي.'),
          ('He will keep account of the time of the suspension of players.', 'کھلاڑیوں کی معطلی کے وقت کا حساب رکھے گا۔', 'د لوبغاړو د ځنډولو د وخت حساب به ساتي.')])
    b.h('Duration of the game', 'کھیل کا دورانیہ', 'د لوبې موده')
    P(b, [('International competitions consist of two halves of thirty (30 minutes), between which there is an interval of 10 minutes. In case the game is equal at the fixed time, if determining the winner in the decision of the match is necessary, then in this case an extra time of two halves of 5, 5 minutes will be given. If the match is equal in extra time too, then again 5, 5 minutes more time will be given. If even at this time the match is equal, the winner will be determined according to the rules.', 'بین الاقوامی مقابلے تیس (30 منٹ) کے دو ہاف پر مشتمل ہوتے ہیں۔ جن کے درمیان 10 منٹ کا وقفہ ہوتا ہے۔ مقررہ وقت پر کھیل برابر ہونے کی صورت میں اگر میچ کے فیصلے میں فاتح کا تعین لازمی ہو تو اس صورت میں 5,5 منٹ کے دو ہاف کا اضافی وقت دیا جائے گا۔ مقابلہ اضافی وقت میں بھی برابر ہو تو دوبارہ 5,5 منٹ کا مزید وقت دیا جائے گا۔ اس وقت میں بھی مقابلہ برابر ہو تو قوانین کی رو سے فاتح کا تعین کیا جائے گا۔', 'نړیوالې سیالۍ د دېرشو (۳۰ دقیقو) له دوو نیمایو جوړې وي چې ترمنځ یې ۱۰ دقیقې وقفه وي. په ټاکلي وخت کې د لوبې د برابرېدو په صورت کې که د لوبې په پرېکړه کې د ګټونکي ټاکل اړین وي، په دې صورت کې د ۵، ۵ دقیقو دوه نیمایي اضافي وخت ورکول کېږي. که سیالي په اضافي وخت کې هم برابره وي، بیا ۵، ۵ دقیقې نور وخت ورکول کېږي. که په دې وخت کې هم سیالي برابره وي، د قوانینو له مخې ګټونکی ټاکل کېږي.')])
    b.h('Throw off', 'تھرو آف', 'تھرو اف')
    P(b, [('The team starting the game after winning the toss will begin the game with a throw-off. At the time of the throw-off all players will be in their own halves. At the start of the second half the other team will start the game with a throw-off. In the case of a goal, that team will begin the game with a throw-off against which the goal was scored.', 'ٹاس جیت کر کھیل شروع کرنے والی ٹیم کھیل کا آغاز تھرو آف سے کرے گی۔ تھرو آف کے وقت تمام کھلاڑی اپنے اپنے ہاف میں ہوں گے۔ دوسرے ہاف کے آغاز پر دوسری ٹیم تھرو آف سے کھیل شروع کرے گی۔ گول ہونے کی صورت میں وہ ٹیم تھرو آف سے کھیل کی ابتدا کرے گی جس کے خلاف گول ہوا ہو۔', 'هغه ټیم چې ټاس ګټي او لوبه پیلوي، لوبه به په تھرو اف پیلوي. د تھرو اف پر وخت ټول لوبغاړي به په خپلو نیمایو کې وي. د دویمې نیمایي په پیل کې بل ټیم لوبه په تھرو اف پیلوي. د ګول په صورت کې هغه ټیم لوبه په تھرو اف پیلوي چې پر وړاندې یې ګول شوی وي.')])
    b.h('Playing the ball', 'بال کو کھیلنا', 'توپ لوبول')
    P(b, [('A player is allowed to:', 'ایک کھلاڑی کو اجازت ہے کہ وہ:', 'لوبغاړي ته اجازه ده چې:')])
    L(b, [('walk or run three steps with the ball.', 'بال کے ساتھ تین قدم چلے یا دوڑے۔', 'له توپ سره درې قدمه ولاړ شي یا منډه ووهي.'), ('keep the ball with himself for three seconds.', 'بال کو تین سیکنڈ تک اپنے پاس رکھے۔', 'توپ درې ثانیې له ځانه سره وساتي.'),
          ('dribble the ball and walk three steps.', 'بال کو ڈربل کرے اور تین قدم چلے۔', 'توپ ډریبل کړي او درې قدمه ولاړ شي.')])
    b.h('A player is not allowed to:', 'کھلاڑی کو اجازت نہیں کہ وہ:', 'لوبغاړي ته اجازه نشته چې:')
    L(b, [('stop the opposing player in a dangerous manner when he has the ball.', 'مخالف کھلاڑی کو خطرناک انداز سے روکے، جب اس کے پاس بال ہو۔', 'مخالف لوبغاړی په خطرناک ډول ودروي کله چې توپ ورسره وي.')])
    r = rec(b, 7, 66, 151)
    BOOK.save(151, [(7, r)], issues=[{'id': 'hpe12-pdf151', 'unit': 7, 'printedPage': 147,
               'description': 'Printed p.148 is missing from the source scan (the next scan, PDF152, is p.149); its text is logged as a source gap.'}])


def p152():
    b = Builder()
    L(b, [('On playing the player’s ball in a wrong way.', 'کھلاڑی کے بال کو غلط طریقے سے کھیلنے پر۔', 'د لوبغاړي توپ په ناسمه طریقه لوبولو.'), ('On deliberately throwing the ball outside the side line.', 'جان بوجھ کر بال کو سائیڈ لائن سے باہر پھینکنے پر۔', 'په قصد له څنګ کرښې بهر د توپ غورځولو.'),
          ('On wasting time.', 'وقت ضائع کرنے پر۔', 'د وخت په ضایع کولو.'), ('On indecent behaviour during the game.', 'کھیل کے دوران ناشائستہ رویہ پر۔', 'د لوبې پر مهال په ناوړه چلند.')])
    P(b, [('The free throw will be taken without the whistle and at the referee’s signal from the same place where the foul was committed. If the breach of law was committed by a defending player between the goal area and the free-throw line, the free throw will be from the line 9 metres outside the free-throw line. While making the free throw one foot of the player should be on the ground.', 'فری تھرو بغیر وسل اور ریفری کے اشارے پر اس جگہ سے لی جائے گی جہاں پر فاؤل سرزد ہوا ہو۔ اگر قانون شکنی دفاعی کھلاڑی سے گول ایریا اور فری تھرو لائن کے درمیان ہوئی ہو تو فری تھرو لائن کے باہر 9 میٹر لائن سے ہوگی۔ فری تھرو کرتے وقت کھلاڑی کا ایک پاؤں زمین پر ہونا چاہیے۔', 'وړیا غورځونه به له شپېلۍ پرته او د ریفري په اشاره له همغه ځایه اخیستل کېږي چې خطا پکې شوې. که قانون ماتونه د دفاعي لوبغاړي له خوا د ګول سیمې او وړیا غورځونې کرښې ترمنځ شوې وي، وړیا غورځونه به د وړیا غورځونې له کرښې بهر له ۹ متره کرښې وي. د وړیا غورځونې پر وخت دې د لوبغاړي یوه پښه پر ځمکه وي.')])
    b.h('Penalty throw or 7-metre throw', 'پنلٹی تھرو یا 7 میٹر تھرو', 'پنالټي غورځونه یا ۷ متره غورځونه')
    P(b, [('A 7-metre throw will be given in the following cases.', '7 میٹر تھرو مندرجہ ذیل صورتوں میں دی جائے گی۔', '۷ متره غورځونه به په لاندې حالتونو کې ورکول کېږي.')])
    L(b, [('When the defending team commits such a foul as wastes a clear chance of a goal.', 'جب دفاعی ٹیم ایسا فاؤل کرے جس سے واضح گول ہونے کا موقع ضائع ہو جائے۔', 'کله چې دفاعي ټیم داسې خطا وکړي چې د روښانه ګول فرصت ضایع شي.'), ('When the goal keeper takes the ball back into his own goal area.', 'جب گول کیپر بال کو اپنے گول ایریا میں واپس لے جائے۔', 'کله چې ګول ساتونکی توپ بېرته خپلې ګول سیمې ته یوسي.'),
          ('When some player intentionally throws the ball towards his own goal keeper and the goal keeper plays it.', 'جب کوئی کھلاڑی ارادتاً اپنے گول کیپر کی طرف بال پھینکے اور گول کیپر اسے کھیلے۔', 'کله چې کوم لوبغاړی په قصد خپل ګول ساتونکي ته توپ وغورځوي او ګول ساتونکی یې ولوبوي.'),
          ('If some defending player enters the goal area in such a way that he has taken advantage from it. In case of entering the goal area without taking advantage or losing balance, a free throw will be given which will be taken from the 9-metre line.', 'اگر کوئی دفاعی کھلاڑی اس طرح گول ایریا میں داخل ہو جس سے اس نے فائدہ حاصل کیا ہو۔ فائدہ حاصل کیے بغیر یا توازن کھو دینے کی صورت میں گول ایریا میں داخل ہونے کی صورت میں فری تھرو دی جائے گی جو 9 میٹر لائن سے لی جائے گی۔', 'که کوم دفاعي لوبغاړی ګول سیمې ته داسې ننوځي چې ګټه یې ترې اخیستې وي. له ګټې اخیستو پرته یا د توازن د له لاسه ورکولو په صورت کې ګول سیمې ته د ننوتلو په صورت کې وړیا غورځونه ورکول کېږي چې له ۹ متره کرښې اخیستل کېږي.'),
          ('While taking the 7-metre throw all players will be outside the free-throw line. The player taking the 7-metre throw must take the throw within 3 seconds of the referee’s whistle sounding. Any player of the attacking team can take the free throw.', '7 میٹر تھرو لیتے وقت تمام کھلاڑی فری تھرو لائن کے باہر ہوں گے۔ جو کھلاڑی 7 میٹر تھرو لے رہا ہے اس کے لیے ضروری ہے کہ وہ ریفری کی وسل بجنے کے 3 سیکنڈ کے اندر تھرو لے۔ فری تھرو حملہ آور ٹیم کا کوئی بھی کھلاڑی لے سکتا ہے۔', 'د ۷ متره غورځونې پر وخت ټول لوبغاړي به د وړیا غورځونې له کرښې بهر وي. هغه لوبغاړی چې ۷ متره غورځونه اخلي، باید د ریفري د شپېلۍ له غږېدو وروسته په ۳ ثانیو کې غورځونه وکړي. وړیا غورځونه د بریدګر ټیم هر لوبغاړی اخیستلی شي.')])
    r = rec(b, 7, 67, 152)
    BOOK.save(152, [(7, r)], issues=[{'id': 'hpe12-pdf152', 'unit': 7, 'printedPage': 149,
               'description': 'Printed p.148 is missing from the scan, so this page opens mid-list (the list of free-throw offences); its heading is on the missing page. Extensive owner handwriting (Urdu and English: “Giving of my state” etc.) and a blue pen line down the gutter are excluded.'}])


def p153():
    b = Builder()
    b.h('Penalties', 'سزائیں', 'سزاګانې')
    b.h('Warning', 'وارننگ', 'خبرداری')
    P(b, [('For a warning a yellow card will be used, which will be given for the following reasons.', 'وارننگ کے لیے زرد کارڈ استعمال کیا جائے گا۔ جو مندرجہ ذیل وجوہات پر دی جائے گی۔', 'د خبرداري لپاره ژېړ کارت کارول کېږي چې په لاندې لاملونو ورکول کېږي.')])
    L(b, [('When the opponent is making a throw and the defending team breaches some law.', 'جب مخالف تھرو کر رہا ہو تو دفاعی ٹیم کی کسی قانون کی خلاف ورزی پر۔', 'کله چې مخالف غورځونه کوي او دفاعي ټیم کوم قانون ماتوي.'), ('On playing a dangerous game.', 'خطرناک کھیل پیش کرنے پر۔', 'په خطرناکه لوبه.'), ('On negative and aggressive behaviour.', 'منفی و جارح رویہ پر۔', 'په منفي او تېریګر چلند.')])
    P(b, [('Individually one warning will be given to a player once and to the whole team three times. After this, on every dangerous foul a punishment of two-minute suspension will be given.', 'انفرادی طور پر ایک کھلاڑی کو ایک بار اور پوری ٹیم کو تین دفعہ وارننگ دی جائے گی۔ اس کے بعد ہر خطرناک فاؤل پر دو منٹ کی معطلی کی سزا دی جائے گی۔', 'په انفرادي ډول یوه لوبغاړي ته یو ځل او ټول ټیم ته درې ځله خبرداری ورکول کېږي. له دې وروسته په هره خطرناکه خطا د دوو دقیقو ځنډولو سزا ورکول کېږي.')])
    b.h('Disqualification and expulsion from the match', 'نااہلی اور مقابلے سے اخراج', 'نااهلي او له سیالۍ ایستل')
    P(b, [('When a player in one match has been suspended 3 times for 2 minutes, then for suspending him the third time a red card will be used. The disqualified player will immediately leave the field of play and the bench of the team, and the team will play with only 6 players for 2 minutes; however, on completion of 2 minutes a substitute player can play in place of the disqualified player.', 'جب کسی کھلاڑی کو ایک میچ میں 3 مرتبہ 2 منٹ کے لیے معطل کیا جائے تو تیسری بار معطل کرنے کے لیے سرخ کارڈ استعمال کیا جائے گا۔ نااہل کھلاڑی فوری طور پر کھیل کا میدان اور ٹیم کا بینچ چھوڑ دے گا اور ٹیم 2 منٹ تک صرف 6 کھلاڑیوں سے کھیلے گی تاہم 2 منٹ مکمل ہونے پر نااہل کھلاڑی کی جگہ متبادل کھلاڑی کھیل سکتا ہے۔', 'کله چې یو لوبغاړی په یوه لوبه کې ۳ ځله د ۲ دقیقو لپاره وځنډول شي، د درېیم ځل ځنډولو لپاره سور کارت کارول کېږي. نااهل لوبغاړی به سمدستي د لوبې میدان او د ټیم بنچ پرېږدي او ټیم به ۲ دقیقې یوازې په ۶ لوبغاړو لوبه کوي؛ خو د ۲ دقیقو په بشپړېدو د نااهل لوبغاړي پر ځای بدیل لوبغاړی لوبه کولی شي.')])
    b.h('Skills of handball', 'ہینڈ بال کی مہارتیں', 'د هېنډبال مهارتونه')
    b.h('Stopping the ball', 'بال کو روکنا', 'توپ درول')
    P(b, [('To stop the ball the player can use both hands. According to the direction and speed of the ball, bring both your hands into position in such a way that the whole ball comes into the hands. To stop a fast ball, as soon as the ball strikes the hands, move the hands backwards.', 'بال کو روکنے کے لیے کھلاڑی دونوں ہاتھوں کا استعمال کر سکتا ہے۔ بال کی سمت اور رفتار کے مطابق اپنے دونوں ہاتھوں کو اس طرح پوزیشن میں لائیں کہ پورا بال ہاتھوں میں آ جائے۔ تیز رفتار بال کو روکنے کے لیے بال ہاتھ میں ٹکراتے ہی ہاتھوں کو پیچھے کی جانب حرکت دیں۔', 'د توپ د درولو لپاره لوبغاړی دواړه لاسونه کارولی شي. د توپ د لوري او سرعت سره سم خپل دواړه لاسونه داسې برابر کړئ چې ټول توپ لاسونو ته راشي. د چټک توپ د درولو لپاره، څنګه چې توپ لاسونو ته ولګېږي، لاسونه شا ته وخوځوئ.')])
    r = rec(b, 7, 68, 153)
    BOOK.save(153, [(7, r)], issues=[{'id': 'hpe12-pdf153', 'unit': 7, 'printedPage': 150,
               'description': 'Owner Urdu ballpoint notes in the margin and a blue pen line down the page are excluded. Retained as printed.'}])


def p154():
    b = Builder()
    b.h('Dribbling', 'ڈربلنگ', 'ډریبلنګ')
    P(b, [('For dribbling, keep the ball close to the body and dribble the ball while bending the knees. Do not hit the ball on the court with force; in this way the ball can easily be snatched from your possession. Remember that after dribbling, when the ball becomes stationary in your hand, then pass it; dribbling a second time is a foul.', 'ڈربلنگ کرنے کے لیے بال کو جسم کے نزدیک رکھیں گھٹنے کو جھکاتے ہوئے بال کو ڈربل کریں۔ بال کو کورٹ پر زور سے نہ ماریں اس طرح کرنے سے بال آپ کے قبضے سے آسانی سے چھینا جا سکتا ہے۔ یاد رکھیں ڈربلنگ کے بعد جب بال آپ کے ہاتھ میں ساکن ہو جائے تو اسے پاس کریں دوسری بار ڈربلنگ کرنا فاؤل ہے۔', 'د ډریبلنګ لپاره توپ بدن ته نږدې وساتئ او زنګونونه کاږه کړئ او توپ ډریبل کړئ. توپ پر میدان په زور مه وهئ؛ په دې ډول توپ په اسانۍ ستاسو له واکه اخیستل کېدای شي. یاد ولرئ له ډریبلنګ وروسته کله چې توپ ستاسو په لاس کې ودرېږي، پاس یې کړئ؛ دویم ځل ډریبلنګ خطا ده.')])
    b.h('Method of dribbling', 'ڈربلنگ کا طریقہ', 'د ډریبلنګ طریقه')
    b.h('Passing with the wrist', 'کلائی سے پاس کرنا', 'په مړوند پاس')
    P(b, [('When defending players come in front of some player in such a way that he can neither play the ball towards the goal nor pass to his player in front, then he can give a pass to the side with the wrist. To make this pass the player brings one foot forward and, the hand in which the ball is, bringing it close to the body, passes with force towards the outside.', 'جب کسی کھلاڑی کے سامنے دفاع کرنے والے کھلاڑی اس صورت میں آ جائیں کہ وہ نہ تو گول کی طرف بال کو کھیل سکے اور نہ ہی سامنے اپنے کھلاڑی کو پاس کر سکے تو وہ کلائی سے سائیڈ کی جانب پاس دے سکتا ہے۔ یہ پاس کرنے کے لیے کھلاڑی اپنا ایک پاؤں آگے لے کر آئے اور جس ہاتھ میں بال ہو اسے جسم کے نزدیک لاتے ہوئے باہر کی جانب زور سے پاس کرے۔', 'کله چې د یوه لوبغاړي مخې ته دفاعي لوبغاړي داسې راشي چې نه ګول ته توپ لوبولی شي او نه مخې ته خپل لوبغاړي ته پاس کولی شي، نو په مړوند څنګ ته پاس ورکولی شي. د دې پاس لپاره لوبغاړی یوه پښه مخکې راوړي او هغه لاس چې توپ پکې وي، بدن ته نږدې کوي او بهر لوري ته په زور پاس کوي.')])
    b.h('Trying to snatch the ball', 'بال کو چھیننے کی کوشش کرنا', 'د توپ د اخیستو هڅه')
    P(b, [('To snatch the ball use the hands; the torso can be used to stop the opposing players, provided there is no danger of the opposing player being injured by it.', 'بال کو چھیننے کے لیے ہاتھوں کا استعمال کریں مخالف کھلاڑیوں کو روکنے کے لیے دھڑ کا استعمال کیا جا سکتا ہے بشرطیکہ اس سے مخالف کھلاڑی کے زخمی ہونے کا خدشہ نہ ہو۔', 'د توپ د اخیستو لپاره لاسونه وکاروئ؛ د مخالفو لوبغاړو د درولو لپاره تنه کارول کېدای شي، په دې شرط چې د مخالف لوبغاړي د ټپي کېدو وېره ونه لري.')])
    r = rec(b, 7, 69, 154)
    BOOK.save(154, [(7, r)], issues=[{'id': 'hpe12-pdf154', 'unit': 7, 'printedPage': 151,
               'description': 'Extensive owner Urdu and English handwriting (“of daddy dad’s”, scribbles) between the headings is excluded. The heading “ڈربلنگ کا طریقہ” has no text of its own in print. Retained as printed.'}])


def p155():
    e = Builder()
    e.h('Exercise questions', 'مشقی سوالات', 'تمریني پوښتنې')
    e.p('1. Choose and write the suitable answers.', '۱۔ موزوں جوابات منتخب کر کے لکھیں۔', '۱. مناسب ځوابونه وټاکئ او ولیکئ.')
    Q = [(('The length of the handball court is ________ metres.', 'ہینڈ بال کورٹ کی لمبائی ________ میٹر ہوتی ہے۔', 'د هېنډبال د میدان اوږدوالی ________ متره وي.'), [Q_('20'), Q_('40'), Q_('60'), Q_('80')]),
         (('The breadth of the handball court is ________ metres.', 'ہینڈ بال کورٹ کی چوڑائی ________ میٹر ہوتی ہے۔', 'د هېنډبال د میدان پلنوالی ________ متره وي.'), [Q_('20'), Q_('10'), Q_('15'), Q_('30')]),
         (('________ players of a handball team play in the court.', 'ہینڈ بال ٹیم کے ________ کھلاڑی کورٹ میں کھیلتے ہیں۔', 'د هېنډبال د ټیم ________ لوبغاړي په میدان کې لوبه کوي.'), [Q_('7'), Q_('6'), Q_('9'), Q_('11')]),
         (('In handball the goal keeper border line is ________ metres from the line.', 'ہینڈ بال میں گول کیپر بارڈر لائن سے ________ میٹر پر ہوتا ہے۔', 'په هېنډبال کې د ګول ساتونکي پوله له کرښې ________ متره وي.'), [Q_('2'), Q_('3'), Q_('4'), Q_('6')]),
         (('In handball the line of the penalty area is at ________ metres.', 'ہینڈ بال میں پنلٹی ایریا کی لائن ________ میٹر پر ہوتی ہے۔', 'په هېنډبال کې د پنالټي سیمې کرښه په ________ متره وي.'), [Q_('5'), Q_('6'), Q_('7'), Q_('8')]),
         (('The duration of the handball game is ________ minutes.', 'ہینڈ بال کھیل کا دورانیہ ________ منٹ ہوتا ہے۔', 'د هېنډبال د لوبې موده ________ دقیقې وي.'), [Q_('30'), Q_('40'), Q_('50'), Q_('60')])]
    for i, (q, o) in enumerate(Q):
        e.mcq(['i.', 'ii.', 'iii.', 'iv.', 'v.', 'vi.'][i], q, o, per_line=4)
    e.p('2. Write the answers to the following questions.', '۲۔ درج ذیل سوالات کے جوابات لکھیں۔', '۲. د لاندې پوښتنو ځوابونه ولیکئ.')
    e.group('lines', [('i. Make the handball court with measurements.', 'i۔ ہینڈ بال کا کورٹ بمعہ پیمائش بنائیں۔', 'i. د هېنډبال میدان له اندازو سره جوړ کړئ.'), ('ii. In which cases is a free throw given in handball?', 'ii۔ ہینڈ بال فری تھرو کن صورتوں میں دی جاتی ہے۔', 'ii. په هېنډبال کې وړیا غورځونه په کومو حالتونو کې ورکول کېږي؟'),
                      ('iii. Explain the throw-in, penalty throw and referee throw in handball.', 'iii۔ ہینڈ بال میں تھرو ان، پنلٹی تھرو اور ریفری تھرو کی وضاحت کریں۔', 'iii. په هېنډبال کې تھرو ان، پنالټي غورځونه او د ریفري غورځونه روښانه کړئ.')])
    r = BOOK.record(e, 'hpe12-ch7-exercise-handball', 'Chapter 7 exercise: handball', 'باب ۷: مشقی سوالات — ہینڈ بال', '۷ څپرکی: تمریني پوښتنې — هېنډبال', 155, [152])
    BOOK.save(155, [(7, r)], complete_units=[7], issues=[{'id': 'hpe12-pdf155', 'unit': 7, 'printedPage': 152,
               'description': 'Owner ballpoint ticks are excluded. Q(v) asks about “پنلٹی ایریا کی لائن” and Q(iii) about a “ریفری تھرو”, neither described in the surviving text. Retained as printed.'}])


AUTHORS = [('Malik Asif', 'ملک آصف', 'ملک آصف', 'Malik Asif obtained the M.Sc degree in Health and Physical Education (HPE) from Gomal University in 1983 and became associated with teaching. He served as DPE in different colleges and retired as Professor of HPE from Government Post Graduate College No. 1, Abbottabad in 2015. He is also the author of several books.',
            'ملک آصف نے 1983 میں گومل یونیورسٹی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی اور درس و تدریس کے شعبے سے وابستہ ہو گئے۔ آپ نے مختلف کالجوں میں بطور DPE خدمات سرانجام دیے اور 2015 میں گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد سے بطور پروفیسر HPE ریٹائرڈ ہوئے۔ آپ کئی کتابوں کے مصنف بھی ہیں۔',
            'ملک آصف په ۱۹۸۳ کې له ګومل پوهنتون د روغتیا او فزیکي زده‌کړې (HPE) د ایم اېس سي سند واخیست او له تدریس سره تړلی شو. په بېلابېلو کالجونو کې یې د DPE په توګه خدمت وکړ او په ۲۰۱۵ کې د ایبټ آباد له ۱ شمېره حکومتي پوسټ ګرېجوېټ کالج د HPE پروفیسر په توګه تقاعد شو. د څو کتابونو لیکوال هم دی.'),
           ('Arif Ali Shah', 'عارف علی شاہ', 'عارف علي شاه', 'Arif Ali Shah obtained the M.Sc degree in Health and Physical Education (HPE) from the University of Karachi in 2003 and won a gold medal. He has been associated with teaching since 2006. Nowadays he is serving as Chairman, HPE Department, Government Post Graduate College No. 1, Abbottabad.',
            'عارف علی شاہ نے 2003 میں یونیورسٹی آف کراچی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی اور گولڈ میڈل حاصل کیا۔ آپ 2006 سے درس و تدریس کے شعبے سے وابستہ ہے۔ آج کل گورنمنٹ پوسٹ گریجویٹ کالج نمبر 1، ایبٹ آباد میں بطور چیئرمین HPE ڈیپارٹمنٹ کے خدمات سرانجام دے رہے ہیں۔',
            'عارف علي شاه په ۲۰۰۳ کې د کراچۍ له پوهنتون د روغتیا او فزیکي زده‌کړې (HPE) د ایم اېس سي سند واخیست او د سرو زرو مډال یې وګاټه. له ۲۰۰۶ راهیسې له تدریس سره تړلی دی. اوس مهال د ایبټ آباد د ۱ شمېره حکومتي پوسټ ګرېجوېټ کالج د HPE څانګې د مشر په توګه دنده ترسره کوي.'),
           ('Samiullah Marwat', 'سمیع اللہ مروت', 'سمیع‌الله مروت', 'Samiullah Marwat obtained the M.Sc degree in Health and Physical Education (HPE) from Gomal University in 1996. He served as DPE in different schools. Nowadays he is serving as Director Physical Education and Sports in DCTE Abbottabad.',
            'سمیع اللہ مروت نے 1996 میں گومل یونیورسٹی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی۔ مختلف سکولوں میں بطور DPE کے خدمات سرانجام دیے ہیں۔ آج کل DCTE ایبٹ آباد میں بطور ڈائریکٹر فزیکل ایجوکیشن اینڈ سپورٹس کے خدمات سرانجام دے رہے ہیں۔',
            'سمیع‌الله مروت په ۱۹۹۶ کې له ګومل پوهنتون د روغتیا او فزیکي زده‌کړې (HPE) د ایم اېس سي سند واخیست. په بېلابېلو ښوونځیو کې یې د DPE په توګه خدمت کړی. اوس مهال د ایبټ آباد په DCTE کې د فزیکي زده‌کړې او لوبو د رییس په توګه دنده ترسره کوي.'),
           ('Rasheedullah', 'رشید اللہ', 'رشیدالله', 'Rasheedullah obtained the M.Sc degree in Health and Physical Education (HPE) from Gomal University in 1989. Since 1990 he has been serving as DPE in different colleges. Nowadays he is serving as Lecturer in Government Degree College Sherwan, Abbottabad.',
            'رشید اللہ نے 1989 میں گومل یونیورسٹی سے صحت و جسمانی تعلیم (HPE) میں ایم ایس سی کی ڈگری حاصل کی۔ 1990 سے مختلف کالجوں میں بطور DPE خدمات سرانجام دے رہے ہیں۔ آج کل گورنمنٹ ڈگری کالج شیروان، ایبٹ آباد میں بطور لیکچرر خدمات سرانجام دے رہے ہیں۔',
            'رشیدالله په ۱۹۸۹ کې له ګومل پوهنتون د روغتیا او فزیکي زده‌کړې (HPE) د ایم اېس سي سند واخیست. له ۱۹۹۰ راهیسې په بېلابېلو کالجونو کې د DPE په توګه دنده ترسره کوي. اوس مهال د ایبټ آباد د شېروان حکومتي ډګري کالج کې د لکچرر په توګه دنده ترسره کوي.')]


def p156():
    b = Builder()
    b.h('Introduction of the authors', 'مصنفین کا تعارف', 'د لیکوالانو پېژندنه')
    for en, ur, ps, de, du, dp in AUTHORS:
        b.h(en, ur, ps)
        b.p(de, du, dp)
    r = BOOK.record(b, 'hpe12-bm-authors', 'Introduction of the authors', 'مصنفین کا تعارف', 'د لیکوالانو پېژندنه', 156, [153], unit_title=('Back matter', 'ضمیمہ', 'ضمیمه'))
    BOOK.save(156, [('BM', r)], issues=[{'id': 'hpe12-pdf156', 'unit': 'BM', 'printedPage': 153,
               'description': 'The page is heavily covered with owner ballpoint handwriting (repeated names “محمد کامران”, scribbles); all excluded. “خدمات سرانجام دیے”, “آپ 2006 سے … وابستہ ہے”. Retained as printed.'}])


def p157():
    b = Builder()
    b.h('National Anthem', 'قومی ترانہ', 'ملي سرود')
    P(b, [('The national anthem of Pakistan (words by Hafeez Jalandhari) is printed in Urdu on the back cover. It praises the sacred land of Pakistan as the symbol of high resolve and the centre of faith, the strength of the brotherhood of the people, and prays that the nation, country and state remain lasting and shining; it calls the crescent-and-star flag the guide of progress and perfection, the interpreter of the past and the glory of the present, under the shade of God the Majestic.',
           'پشت سرورق پر پاکستان کا قومی ترانہ (کلام: حفیظ جالندھری) درج ہے۔ (ترانے کا مکمل متن یہاں نقل نہیں کیا گیا؛ دیکھیے ماخذ نوٹ۔) ترانہ پاک سرزمین کو عزمِ عالی شان کا نشان اور یقین کا مرکز کہتا ہے، عوام کی اخوت کی قوت کی بات کرتا ہے، قوم، ملک اور سلطنت کے پائندہ و تابندہ رہنے کی دعا کرتا ہے اور ہلالی پرچم کو ترقی و کمال کا رہبر، ماضی کا ترجمان اور حال کی شان قرار دیتا ہے۔',
           'په شاتنۍ پښتۍ د پاکستان ملي سرود (د حفیظ جالندهري کلام) چاپ دی. سرود د پاکستان سپېڅلې خاوره د لوړ هوډ نښه او د باور مرکز بولي، د خلکو د ورورګلوۍ له ځواک یادونه کوي، د ملت، هېواد او دولت د تل پاتې او ځلانده کېدو دعا کوي او د سپوږمۍ او ستوري بیرغ د پرمختګ او کمال لارښود، د تېر ترجمان او د اوسني شان بولي.')])
    b.p('University Book Printers & Publishers (Pvt) Ltd., 14-B, Small Industrial Estate, Jamrud Road, Hayatabad Peshawar. Code No.: PSP/EHD-50-236-1920(O); Quantity: 30,781; Printers: Ittehad Publishers and Printers (Lahore).',
        'یونیورسٹی بک پرنٹرز اینڈ پبلشرز (پرائیویٹ) لمیٹڈ، 14-B، سمال انڈسٹریل اسٹیٹ، جمرود روڈ، حیات آباد پشاور۔ کوڈ نمبر: PSP/EHD-50-236-1920(O)؛ تعداد: 30,781؛ پرنٹرز: اتحاد پبلیشرز اینڈ پرنٹرز (لاہور)۔',
        'یونیورسټي بک پرنټرز اینډ پبلشرز (خصوصي) لمیټډ، 14-B، سمال انډسټریل اسټېټ، جمرود سړک، حیات آباد پېښور. کوډ شمېره: PSP/EHD-50-236-1920(O)؛ شمېر: 30,781؛ چاپګر: اتحاد پبلشرز او پرنټرز (لاهور).')
    r = BOOK.record(b, 'hpe12-bm-back-cover', 'Back cover', 'پشت سرورق', 'شاتنۍ پښتۍ', 157, [None])
    r['sourceGap'] = 'The full words of the national anthem (Hafeez Jalandhari, d. 1982) are summarised rather than transcribed, following the project copyright rule for authors who died after 1975.'
    r['sourceDecorativeImages'] = 'A photograph of a stadium and the publisher’s logo are decorative.'
    BOOK.save(157, [('BM', r)], complete_units=['BM'])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    {150: p150, 151: p151, 152: p152, 153: p153, 154: p154, 155: p155, 156: p156, 157: p157}[n]()
