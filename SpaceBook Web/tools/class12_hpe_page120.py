"""HPE XII PDF120–125: pp.116–121 — baseball field, equipment, dress, officials, start, batting, strike zone, strike, ball, running, duration,
force play, scoring, batter out, runner out, fielding positions (diagram), pitching, balk. Run: python class12_hpe_page120.py N (120–125)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, svg, T


def p120():
    b = Builder()
    P(b, [('The in field consists of 4 bases, while the out field is the area outside the in-field bases, which is shown by 2 foul lines. In the in field there are 4 bases (Bases), of which one is called the home base (Home base). The home base is made of rubber consisting of 5 corners, while the remaining 3 bases are made of white canvas bags.', 'ان فیلڈ 4 بیسوں پر مشتمل ہوتا ہے جبکہ آؤٹ فیلڈ ان بیسوں کے باہر کا علاقہ ہوتا ہے جسے 2 فاؤل لائنز کے ذریعے ظاہر کیا جاتا ہے۔ ان فیلڈ میں 4 بیسز (Bases) ہوتی ہیں جن میں سے ایک کو ہوم بیس (Home base) کہتے ہیں۔ ہوم بیس 5 کونوں پر مشتمل ربڑ سے بنی ہوتی ہے جبکہ باقی 3 بیس سفید رنگ کے کینوس بیگ سے بنی ہوتی ہیں۔', 'داخلي میدان له ۴ بېسونو جوړ وي، په داسې حال کې چې بهرنی میدان له دې بېسونو بهر سیمه ده چې په ۲ فاول کرښو ښودل کېږي. په داخلي میدان کې ۴ بېسونه (Bases) وي چې یوه ته یې د کور بېس (Home base) ویل کېږي. د کور بېس له ۵ ګوټه رابړ جوړ وي، په داسې حال کې چې پاتې ۳ بېسونه له سپینو کنواس کڅوړو جوړ وي.')])
    b.h('Equipment and dress', 'سامان اور لباس', 'سامان او جامې')
    b.h('Bat', 'بیٹ (Bat)', 'بیټ (Bat)')
    P(b, [('The bat is made of wood and is round in shape. Its diameter at no part is more than 2.75 inches. The place of holding the bat is called the holding end (Holding End), whose length is at most 12 inches. The maximum length of the bat is 42 inches and the weight 940 grams.', 'بیٹ لکڑی کا اور گول شکل کا ہوتا ہے۔ اس کا قطر کسی بھی حصے سے 2.75 انچ سے زیادہ نہیں ہوتی۔ بیٹ پکڑنے کی جگہ کو ہولڈنگ اینڈ (Holding End) کہتے ہیں جس کی لمبائی زیادہ سے زیادہ 12 انچ ہوتی ہے۔ بیٹ کی زیادہ سے زیادہ لمبائی 42 انچ اور وزن 940 گرام ہوتا ہے۔', 'بیټ له لرګي او ګرد وي. قطر یې په هېڅ برخه کې له ۲.۷۵ انچه زیات نه وي. د بیټ د نیولو ځای ته د نیولو سر (Holding End) ویل کېږي چې اوږدوالی یې ډېر تر ډېره ۱۲ انچه وي. د بیټ ډېر تر ډېره اوږدوالی ۴۲ انچه او وزن ۹۴۰ ګرامه وي.')])
    b.h('Ball', 'بال (Ball)', 'توپ (Ball)')
    P(b, [('The inner layer of the ball is made of cork, while the outer layer is of leather or wound yarn (wound yarn). Its weight is at most 148.8 grams and at least 141.7 grams.', 'بال کی اندرونی تہہ کارک کی جبکہ بیرونی تہہ چمڑے یا (wound yarn) کی بنی ہوتی ہے۔ اس کا وزن زیادہ سے زیادہ 148.8 گرام اور کم سے کم 141.7 گرام ہوتا ہے۔', 'د توپ داخلي پوړ له کارک او بهرنی پوړ له څرمن یا (wound yarn) جوړ وي. وزن یې ډېر تر ډېره ۱۴۸.۸ ګرامه او لږ تر لږه ۱۴۱.۷ ګرامه وي.')])
    b.h('Dress of the players', 'کھلاڑیوں کا لباس', 'د لوبغاړو جامې')
    L(b, [("Helmet for the batter (Batter's Helment)", "بیٹر کے لیے ہیلمٹ (Batter's Helment)", "د بیټر لپاره خولۍ (Batter's Helment)"), ('Face mask for the catcher (Catcher) (Face Mask)', 'کیچر (Catcher) کے لیے فیس ماسک (Face Mask)', 'د کیچر (Catcher) لپاره د مخ ماسک (Face Mask)'),
          ('Chest protector (Chest Protector)', 'چسٹ پروٹیکٹر (Chest Protector)', 'د سینې ساتونکی (Chest Protector)'), ('Keeper gloves (Keeper gloves)', 'کیپرز گلوز (Keeper gloves)', 'د کیپر دستکشې (Keeper gloves)'), ('Knee and shin guard (Knee and Shin guard)', 'نی اینڈ شن گارڈ (Knee and Shin guard)', 'د زنګون او پنډۍ ساتونکی (Knee and Shin guard)')])
    r = rec(b, 7, 40, 120)
    BOOK.save(120, [(7, r)], issues=[{'id': 'hpe12-pdf120', 'unit': 7, 'printedPage': 116,
               'description': 'The dress list prints “Batter\'s Helment”; “قطر … زیادہ نہیں ہوتی”. Retained as printed.'}])


def p121():
    b = Builder()
    L(b, [('The dress of the players consists of trousers and a shirt, on which the numbers should be clear.', 'کھلاڑیوں کا لباس ٹراوزر اور شرٹ پر مشتمل ہوتا ہے جس پر نمبر واضح ہونے چاہئیں۔', 'د لوبغاړو جامې له پتلون او کمیس جوړې وي چې پرې شمېرې باید روښانه وي.'),
          ('Every fielder is allowed to wear a leather glove (Glove).', 'ہر فیلڈر کو اجازت ہے کہ وہ چمڑے کا دستانہ (Glove) پہنے۔', 'هر فیلډر ته اجازه ده چې د څرمن دستکشه (Glove) واغوندي.')])
    b.h('Officials of Match', 'کھیل کے عہدیداران (Officials of Match)', 'د لوبې چارواکي (Officials of Match)')
    L(b, [('Chief umpire (Chief Umpire)', 'چیف امپائر (Chief Umpire)', 'لوی امپایر (Chief Umpire)'), ('3 or 4 umpires', '3 یا 4 امپائرز', '۳ یا ۴ امپایران'), ('Official scorer', 'آفیشل سکورر', 'رسمي نمره لیکونکی')])
    b.h('Start of the game', 'کھیل کا آغاز', 'د لوبې پیل')
    P(b, [('The game always starts with the batting of the guest team, which is called The Top. The host team will take the second batting, which is called The bottom. When the umpire starts the game he calls “Play”, and if for some reason the game has to be stopped, he will call “Time”.', 'کھیل کا آغاز ہمیشہ مہمان ٹیم کی بیٹنگ سے ہوگا جسے The Top کہا جاتا ہے۔ میزبان ٹیم دوسری بیٹنگ لے گی جسے The bottom کہتے ہیں۔ جب امپائر کھیل کو شروع کرتا ہے تو وہ "Play" پکارتا ہے اور اگر کسی وجہ سے کھیل روکنا پڑے تو وہ "Time" پکارے گا۔', 'لوبه تل د مېلمه ټیم په بیټنګ پیلېږي چې The Top ورته ویل کېږي. کوربه ټیم به دویم بیټنګ اخلي چې The bottom ورته ویل کېږي. کله چې امپایر لوبه پیلوي، "Play" وايي او که په کوم دلیل لوبه درول پکار وي، "Time" به وايي.')])
    b.h('Batting', 'بیٹنگ (Batting)', 'بیټنګ (Batting)')
    P(b, [('Before the start of the game a list of the names of the players and the order of batting is provided to the umpire by the team manager. The players will bat according to this order. Every player on his turn will come into the batter’s box (Batter\'s box). The batter will try to make runs by hitting the ball in a powerful way.', 'کھیل کے آغاز سے قبل امپائر کو ٹیم منیجر کی جانب سے کھلاڑیوں کے ناموں اور بیٹنگ کی ترتیب کی فہرست مہیا کی جاتی ہے۔ کھلاڑی اس ترتیب کے مطابق بیٹنگ کریں گے۔ ہر کھلاڑی اپنی باری پر بیٹر باکس (Batter\'s box) میں آئے گا۔ بیٹر بال کو زوردار طریقے سے مارتے ہوئے رنز بنانے کی کوشش کرے گا۔', 'د لوبې له پیل مخکې امپایر ته د ټیم مدیر له خوا د لوبغاړو د نومونو او د بیټنګ د ترتیب لېست ورکول کېږي. لوبغاړي به د دې ترتیب سره سم بیټنګ کوي. هر لوبغاړی به په خپل وار د بیټر بکس (Batter\'s box) ته راځي. بیټر به په زوروره توګه توپ وهي او د منډو جوړولو هڅه به کوي.')])
    r = rec(b, 7, 41, 121)
    deco(r, 'A photograph of a baseball glove, helmet and bats is decorative.')
    BOOK.save(121, [(7, r)])


def p122():
    b = Builder()
    b.h('Strike Zone', 'سٹرائیک زون (Strike Zone)', 'سټرایک زون (Strike Zone)')
    P(b, [('The strike zone is that area which is below the shoulder and above the knee of the one batting at the home plate. The chief umpire will determine this area. Usually it is determined when the batter is standing straight.', 'سٹرائیک زون وہ ایریا ہے جو کہ ہوم پلیٹ میں بیٹنگ کرنے والے کے کندھے سے نیچے اور گھٹنے سے اوپر ہوتا ہے۔ اس علاقے کا تعین چیف امپائر کرے گا۔ عموماً جب بیٹر سیدھا کھڑا ہو تو اس علاقے کا تعین کیا جاتا ہے۔', 'سټرایک زون هغه سیمه ده چې د کور په پلېټ کې د بیټنګ کوونکي له اوږې لاندې او له زنګون پورته وي. دا سیمه به لوی امپایر ټاکي. عموماً کله چې بیټر نېغ ولاړ وي، دا سیمه ټاکل کېږي.')])
    b.h('Strike', 'سٹرائیک (Strike)', 'سټرایک (Strike)')
    P(b, [('When the batter does not hit the ball thrown by the pitcher (Pitcher), or swings the bat but the ball is wasted from him, then the umpire will call strike (Strike). The umpire will also call strike when the player hits the ball in such a way that it goes into the foul area.', 'جب بیٹر پچر (Pitcher) کی جانب سے پھینکی جانے والی بال کو ہٹ نہ کرے یا بیٹ کو گھمائے مگر بال اس سے ضائع ہو جائے تو امپائر سٹرائیک (Strike) پکارے گا۔ امپائر اس وقت بھی سٹرائیک پکارے گا جب کھلاڑی بال کو اس طرح ہٹ کرے کہ وہ فاؤل ایریا میں جا گرے۔', 'کله چې بیټر د پیچر (Pitcher) اچول شوی توپ ونه وهي یا بیټ وګرځوي خو توپ ترې ضایع شي، امپایر به سټرایک (Strike) اعلانوي. امپایر به هغه وخت هم سټرایک اعلانوي چې لوبغاړی توپ داسې ووهي چې د فاول سیمې ته ولوېږي.')])
    b.h('Ball', 'بال (Ball)', 'بال (Ball)')
    P(b, [('When the pitcher (Pitcher) throws four balls outside the strike zone and the batter does not play them, “ball” will be called. In such a case the batter will go to the second base.', 'جب پچر (Pitcher) سٹرائیک زون سے باہر چار بال پھینکے اور بیٹر اسے نہ کھیلے تو بال پکارا جائے گا۔ ایسی صورت میں بیٹر دوسری بیس پہ چلا جائے گا۔', 'کله چې پیچر (Pitcher) له سټرایک زون بهر څلور توپونه واچوي او بیټر یې ونه لوبوي، "بال" اعلانېږي. په داسې حال کې بیټر به دویم بېس ته ځي.')])
    b.h('Running', 'رننگ (Running)', 'منډه (Running)')
    P(b, [('The batter becomes a runner at that time when:', 'بیٹر اس وقت رنر بن جاتا ہے جب', 'بیټر هغه وخت منډه وهونکی کېږي چې:')])
    L(b, [('he has played the ball without the foul area.', 'اس نے بال کو بغیر فاؤل ایریا کے کھیلا ہو۔', 'توپ یې له فاول سیمې پرته لوبولی وي.'), ('when the keeper has dropped the catch.', 'جب کیپر نے کیچ ڈراپ کر دیا ہو۔', 'کله چې کیپر کیچ پرېښی وي.')])
    b.h('Duration of the game', 'کھیل کا دورانیہ', 'د لوبې موده')
    P(b, [('The game consists of specific innings, which is decided before the start of the match. The professional competitions of America consist of nine (9) innings. When all the players of each side have played on their turns, it will be counted one innings. A half innings will be counted when three players of some team are out. At the end of the decided innings, if the score is equal, extra innings will be played until a clear lead appears in the score of one team.', 'کھیل مخصوص انگز پر مشتمل ہوتا ہے۔ جس کا فیصلہ میچ کے آغاز سے قبل کیا جاتا ہے۔ امریکہ کے پروفیشنل مقابلے نو (9) انگز پر مشتمل ہوتے ہیں۔ ہر سائیڈ کے تمام کھلاڑی اپنی اپنی باری پر کھیلیں گے تو ایک انگز شمار ہوگی۔ ہاف انگز اس وقت شمار ہوگی جب کسی ٹیم کے تین کھلاڑی آؤٹ ہو جائیں۔ طے شدہ انگز کے اختتام پر اگر سکور برابر ہو جائے تو ایکسٹرا انگز کھیلی جائے گی تاوقتیکہ کسی ایک ٹیم کے سکور میں واضح برتری نہ ہو جائے۔', 'لوبه له ټاکلو اننګونو جوړه وي چې پرېکړه یې د لوبې له پیل مخکې کېږي. د امریکا مسلکي سیالۍ له نهو (۹) اننګونو جوړې وي. کله چې د هر اړخ ټول لوبغاړي په خپل وار لوبه وکړي، یو اننګ ګڼل کېږي. نیم اننګ هغه وخت ګڼل کېږي چې د کوم ټیم درې لوبغاړي اوټ شي. د ټاکلو اننګونو په پای کې که نمرې برابرې شي، اضافي اننګونه لوبول کېږي تر هغه چې د یوه ټیم په نمرو کې روښانه برتري رانه شي.')])
    r = rec(b, 7, 42, 122)
    BOOK.save(122, [(7, r)], issues=[{'id': 'hpe12-pdf122', 'unit': 7, 'printedPage': 118,
               'description': '“بیٹر دوسری بیس پہ چلا جائے گا” (a walk sends the batter to first base). Retained as printed.'}])


def p123():
    b = Builder()
    b.h('Force Play', 'فورس پلے (Force Play)', 'فورس پلې (Force Play)')
    P(b, [('A force play will be counted at that time when the batter, running (Running) from his first base, goes towards the second base (Base) and forces his partner player to go to the next base. If a player is already present on the second base, he will have to go to the third base.', 'فورس پلے اس وقت شمار ہوگی جب بیٹر اپنی پہلی بیس سے رننگ (Running) کرتا ہوا دوسری (Base) کی جانب جاتا ہے اور اپنے ساتھی کھلاڑی کو دوسری بیس پر جانے کے لیے فورس کرتا ہے۔ اگر دوسری بیس پر پہلے سے کھلاڑی موجود ہو تو اسے تیسری بیس پر جانا ہوگا۔', 'فورس پلې هغه وخت ګڼل کېږي چې بیټر له خپل لومړي بېسه منډه (Running) کوي، دویم (Base) ته ځي او خپل ملګری لوبغاړی دې ته اړ باسي چې بل بېس ته لاړ شي. که په دویم بېس کې له مخکې لوبغاړی وي، درېیم بېس ته باید لاړ شي.'),
          ('The run will be considered safe when he touches the base bag (Base Bag) before the ball or the fielder who has the ball.', 'رنز اس وقت محفوظ تصور ہوگا جب بیس بیگ (Base Bag) کو بال یا فیلڈر جس کے پاس بال ہے سے پہلے چھوئے۔', 'منډه هغه وخت خوندي ګڼل کېږي چې د بېس کڅوړه (Base Bag) له توپ یا هغه فیلډر مخکې ولمسوي چې توپ ورسره وي.')])
    b.h('Scoring', 'سکورنگ (Scoring)', 'نمرې (Scoring)')
    L(b, [('The team that makes more score will be declared the winner of the match.', 'جو ٹیم زیادہ سکور کرے گی میچ کی فاتح قرار دی جائے گی۔', 'هغه ټیم چې ډېرې نمرې جوړې کړي، د لوبې ګټونکی اعلانېږي.'),
          ('A run will be counted when the players run in the field.', 'رن اس وقت شمار ہوگا جب کھلاڑی فیلڈ کے درمیان دوڑیں گے۔', 'منډه هغه وخت ګڼل کېږي چې لوبغاړي د میدان په منځ کې منډه ووهي.'),
          ('When a player touches all the bases in turn, he will complete one circuit.', 'جب ایک کھلاڑی تمام بیسوں کو باری باری ٹچ کر کے ایک سرکٹ مکمل کرے گا۔', 'کله چې یو لوبغاړی ټول بېسونه په وار وار ولمسوي، یو سرکټ بشپړوي.'),
          ('If a player hits the ball so far into the out field that, running, he touches all the bases and comes back to his “home base”, then a “home in” will be counted.', 'اگر ایک کھلاڑی آؤٹ فیلڈ میں بال اتنی دور مارے کہ وہ دوڑتا ہوا تمام بیسوں کو ٹچ کر کے اپنی ”ہوم بیس“ پر آ جائے تو ”ہوم ان“ شمار ہوگا۔', 'که یو لوبغاړی په بهرني میدان کې توپ دومره لرې ووهي چې په منډه ټول بېسونه ولمسوي او خپل "کور بېس" ته راشي، "هوم ان" ګڼل کېږي.')])
    P(b, [('A home run (Home) will also be counted when the player plays the ball into the air in such a way that it goes beyond the boundary line of 250 feet.', 'ہوم رن (Home) اس وقت بھی شمار ہوگا جب کھلاڑی بال کو ہوا میں اس طرح کھیلے کہ وہ 250 فٹ کی باؤنڈری لائن سے باہر چلا جائے۔', 'هوم رن (Home) هغه وخت هم ګڼل کېږي چې لوبغاړی توپ په هوا کې داسې ولوبوي چې د ۲۵۰ فټو له پولې بهر لاړ شي.'),
          ('When players are present on all the bases and a player completes a home run, it is called a Grand Slam Home Run, which equals 4 runs.', 'جب تمام بیسوں پر کھلاڑی موجود ہوں اور کھلاڑی ہوم رن مکمل کرے تو اسے Grand Slam Home Run کہتے ہیں جو 4 رنز کے برابر ہوتا ہے۔', 'کله چې په ټولو بېسونو لوبغاړي شتون ولري او لوبغاړی هوم رن بشپړ کړي، Grand Slam Home Run ورته ویل کېږي چې له ۴ منډو سره برابر دی.')])
    L(b, [('Whenever some batter plays the ball into the out field, it will be necessary for him to run.', 'جب بھی کوئی بیٹر بال کو آؤٹ فیلڈ میں کھیلے گا تو اسے لازمی دوڑنا ہوگا۔', 'هر کله چې کوم بیټر توپ بهرني میدان ته ولوبوي، باید منډه ووهي.')])
    b.h('The batter will be counted out when', 'بیٹر اس وقت آؤٹ شمار ہوگا جب', 'بیټر به هغه وخت اوټ ګڼل کېږي چې')
    L(b, [('the throw reaches the base before him.', 'تھرو اس سے پہلے بیس پر پہنچ جائے۔', 'غورځول شوی توپ له هغه مخکې بېس ته ورسېږي.')])
    r = rec(b, 7, 43, 123)
    BOOK.save(123, [(7, r)])


def field_pos(cap):
    pos = [('CF CENTER FIELD', 8, 220, 50), ('LF LEFT FIELD', 7, 60, 110), ('RF RIGHT FIELD', 9, 380, 110), ('SS SHORTSTOP', 6, 160, 200), ('2B SECOND BASE', 4, 280, 200),
           ('3B THIRD BASE', 5, 110, 270), ('1B FIRST BASE', 3, 330, 270), ('P PITCHER', 1, 220, 290), ('C CATCHER', 2, 220, 390)]
    b = '<rect x="0" y="0" width="440" height="430" fill="#15803d"/><polygon points="220,180 320,290 220,400 120,290" fill="#fdba74" opacity="0.7"/>'
    for lab, n, x, y in pos:
        b += f'<circle cx="{x}" cy="{y}" r="11" fill="#fef08a" stroke="#7c2d12"/>' + T(x, y + 4, str(n), 12, 'bold') + T(x, y - 16, lab, 10, 'bold', 'middle', '#ffffff')
    return svg(440, 440, b, cap)


def p124():
    b = Builder()
    L(b, [('the fielder catches the ball played in the … area.', 'میں کھیلے گئے بال کو فیلڈر کیچ کر لے۔', 'په … سیمه کې لوبول شوی توپ فیلډر کیچ کړي.'),
          ('in the case of being caught in the foul area he will be counted out.', 'فاؤل ایریا میں کیچ ہونے کی صورت میں آؤٹ شمار ہوگا۔', 'په فاول سیمه کې د کیچ په صورت کې اوټ ګڼل کېږي.'),
          ('when he stops the ball in such a way that it goes into the foul area.', 'جب وہ بال کو اس طرح سے روکے کہ وہ فاؤل ایریا میں چلی جائے۔', 'کله چې توپ داسې ودروي چې فاول سیمې ته لاړ شي.'),
          ('when he fails to play three correct balls.', 'جب وہ تین درست بالوں کو کھیلنے میں ناکام ہو۔', 'کله چې په درېیو سمو توپونو لوبولو کې ناکام شي.'),
          ('when he deliberately plays the ball twice.', 'جب وہ جان بوجھ کر بال کو دو مرتبہ کھیلے۔', 'کله چې په قصد توپ دوه ځله ولوبوي.'),
          ('if he deliberately becomes the cause of obstruction for the fielder.', 'اگر وہ جان بوجھ کر فیلڈر کے لیے رکاوٹ کا سبب بنے۔', 'که په قصد د فیلډر لپاره د خنډ لامل شي.')])
    b.h('The runner will be counted out when', 'رنر (Runner) اس وقت آؤٹ شمار ہوگا جب', 'منډه وهونکی (Runner) به هغه وخت اوټ ګڼل کېږي چې')
    L(b, [('he is not on the base and the fielder who has the ball touches him.', 'وہ بیس پر نہ ہو اور فیلڈر جس کے پاس بال ہو اسے چھو لے۔', 'په بېس نه وي او هغه فیلډر چې توپ ورسره وي، ولمسوي یې.'),
          ('if, for fear that the fielder will touch him, he runs 3 feet away from the straight line.', 'اگر وہ اس خدشے سے کہ فیلڈر اسے چھو لے گا سیدھی لائن سے 3 فٹ دور بھاگے۔', 'که د دې وېرې له امله چې فیلډر به یې ولمسوي، له نېغې کرښې ۳ فټه لرې منډه ووهي.'),
          ('if the fielder with the ball reaches that base first towards which the batter was running.', 'اگر فیلڈر بال کے ساتھ اس بیس پر پہلے پہنچ جائے جس کی طرف بیٹر بھاگ رہا تھا۔', 'که فیلډر له توپ سره هغه بېس ته مخکې ورسېږي چې بیټر ورته منډه وهله.'),
          ('A “Double play” will be counted at that time when two are out consecutively.', 'اس وقت ڈبل پلے "Double play" شمار ہوگا جب دو مسلسل آؤٹ ہوں۔', '"Double play" به هغه وخت ګڼل کېږي چې دوه پرلپسې اوټ شي.')])
    b.h('Fielding positions in baseball', 'بیس بال میں فیلڈنگ پوزیشن', 'په بېس بال کې د فیلډنګ ځایونه')
    P(b, [('In baseball the nine players will field according to the outline below.', 'بیس بال میں نو کھلاڑی ذیل میں خاکے کے مطابق فیلڈنگ کریں گے۔', 'په بېس بال کې نهه لوبغاړي به د لاندې خاکې سره سم فیلډنګ کوي.')])
    sv = [field_pos(c) for c in ('Baseball fielding positions (labels as printed)', 'بیس بال میں فیلڈنگ پوزیشنیں', 'په بېس بال کې د فیلډنګ ځایونه')]
    b.visual('hpe12-fig-baseball-positions', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    r = rec(b, 7, 44, 124)
    BOOK.save(124, [(7, r)], issues=[{'id': 'hpe12-pdf124', 'unit': 7, 'printedPage': 120,
               'description': 'The right edge of the scan cuts the first words of several lines (“… میں کھیلے گئے”, “فاؤل ایریا”, “جب”), completed from context where possible; the first bullet’s opening word is lost and marked “…”. The fielding-positions diagram is reproduced as a coded schematic with the printed English labels and numbers.'}])


def p125():
    b = Builder()
    b.h('Pitching', 'پچنگ (Pitching)', 'پیچنګ (Pitching)')
    L(b, [('If the pitcher throws the ball from the Sit position or the Wind up position, it will be counted correct.', 'پچر Sit پوزیشن یا Wind up پوزیشن سے بال پھینکے گا تو وہ درست شمار ہوگی۔', 'که پیچر له Sit یا Wind up حالته توپ واچوي، سم ګڼل کېږي.'),
          ('The pitcher can rub (something) on his hands to make the ball shine, but if he rubs it on the ground or a rough surface, he will be stopped from pitching.', 'پچر بال کو چمکانے کے لیے ہاتھوں میں مل سکتا ہے لیکن وہ اسے زمین یا کھردری سطح پر رگڑے گا تو اسے پچنگ سے روک دیا جائے گا۔', 'پیچر د توپ ځلولو لپاره په لاسونو موښلی شي، خو که پر ځمکه یا زیږه سطحه یې وموښي، له پیچنګ به منع شي.'),
          ('If the pitcher throws the ball from in front of or behind the pitching line, a no ball will be given, which is called a balk (Balk).', 'اگر پچر پچنگ کی لکیر سے آگے یا پیچھے سے بال کو پھینکے تو نو بال دی جائے گی جسے باک (Balk) کہتے ہیں۔', 'که پیچر د پیچنګ له کرښې مخکې یا شا توپ واچوي، نو بال ورکول کېږي چې باک (Balk) ورته ویل کېږي.'),
          ('The pitcher will not throw the ball directly at the batter’s body.', 'پچر بیٹر کے جسم پر براہ راست بال نہیں پھینکے گا۔', 'پیچر به په مستقیم ډول د بیټر بدن ته توپ نه اچوي.'),
          ('The pitcher will have to throw every ball within 20 seconds of its coming into his hand.', 'پچر کو ہر بال اس کے ہاتھ میں آنے کے 20 سیکنڈ کے اندر پھینکنا ہوگی۔', 'پیچر باید هر توپ په لاس کې له راتګ وروسته په ۲۰ ثانیو کې واچوي.')])
    b.h('A balk will be given for the following reasons:', 'باک (Balk) مندرجہ ذیل وجوہات پہ دی جائے گی:', 'باک (Balk) به په لاندې لاملونو ورکول کېږي:')
    L(b, [('Throwing the ball without keeping the foot on the pitching plate.', 'پچنگ پلیٹ پر پاؤں رکھے بغیر بال پھینکنا۔', 'د پیچنګ پر پلېټ له پښې ایښودو پرته توپ اچول.'), ('Throwing the ball without facing the batter, turning the face away.', 'بیٹر کی جانب چہرے کا رخ نہ کرنا، منہ گھما کر بال پھینکنا۔', 'بیټر ته مخ نه اړول، مخ اړول او توپ اچول.'),
          ('The keeper not being in his place and throwing the ball.', 'کیپر کا اپنی جگہ نہ ہونا اور بال کا پھینک دینا۔', 'کیپر په خپل ځای کې نه وي او توپ اچول.'), ('The ball slipping from the hand during pitching.', 'پچنگ کے دوران بال کا ہاتھ سے چھوٹ جانا۔', 'د پیچنګ پر مهال له لاسه د توپ خوشې کېدل.'),
          ('Completing the act of pitching but not releasing the ball from the hand.', 'پچنگ کا عمل پورا کرنا مگر بال کو ہاتھ سے نہ چھوڑنا۔', 'د پیچنګ عمل بشپړول خو توپ له لاسه نه خوشې کول.')])
    r = rec(b, 7, 45, 125)
    deco(r, 'A photograph of a pitcher, batter, catcher and umpire at home plate is decorative.')
    BOOK.save(125, [(7, r)], issues=[{'id': 'hpe12-pdf125', 'unit': 7, 'printedPage': 121,
               'description': '“وجوہات پہ دی جائے گی”, “ہر بال … پھینکنا ہوگی”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    {120: p120, 121: p121, 122: p122, 123: p123, 124: p124, 125: p125}[n]()
