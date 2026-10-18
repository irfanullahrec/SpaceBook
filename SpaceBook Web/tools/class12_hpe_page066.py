"""HPE XII PDF66–71: pp.61–66 — hockey (stopping, dribbling, hitting, scoop); cricket (bowling, fast bowling, spin, batting, fielding); long jump
(approach). Run: python class12_hpe_page066.py N (66–71)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p66():
    b = Builder()
    b.h('Hockey', 'ہاکی (Hockey)', 'هاکي (Hockey)')
    P(b, [('Hockey is the national game of Pakistan. The following skills are included in it.', 'ہاکی پاکستان کا قومی کھیل ہے۔ اس میں مندرجہ ذیل مہارتیں شامل ہیں۔', 'هاکي د پاکستان ملي لوبه ده. په کې لاندې مهارتونه شامل دي.')])
    L(b, [('Stopping the ball (Stopping)', 'گیند روکنا (Stopping)', 'توپ درول (Stopping)'), ('Hitting (Hitting)', 'ہٹ لگانا (Hitting)', 'ګوزار (Hitting)'), ('Dribbling (Dribbling)', 'ڈربلنگ (Dribbling)', 'ډریبلنګ (Dribbling)'), ('Scoop (Scoping)', 'سکوپ (Scoping)', 'سکوپ (Scoping)')])
    b.h('Biomechanical principles in hockey skills:', 'ہاکی کی مہارتوں میں بائیو مکینیکل اصول:', 'د هاکي په مهارتونو کې بایومیخانیکي اصول:')
    b.h('Stopping the ball', 'بال روکنا', 'توپ درول')
    P(b, [('Keeping the balance of the body, keep the hockey stick in the direction of the ball. According to the direction and speed of the ball keep the hockey stick on the ground; when the ball strikes the hockey stick, let the stick come back a little so that the force of a powerful hit can be reduced. As a result of the striking of the hockey stick Newton’s third law applies. If the hockey stick is not taken back a little, then as a reaction the ball will roll far away in the opposite direction and will go out of the reach of the player.',
           'جسم کا توازن برقرار رکھتے ہوئے ہاکی کو بال کی سمت میں رکھیں۔ بال کی سمت اور رفتار کے مطابق ہاکی کو زمین پر رکھیں جب بال ہاکی کے ساتھ ٹکرائے تو ہاکی کو تھوڑا پیچھے آنے دیں۔ تاکہ زوردار ہٹ کا زور کم کیا جا سکے۔ ہاکی ٹکرانے کے عمل کے نتیجے میں نیوٹن کا تیسرا قانون لاگو ہوتا ہے۔ ہاکی کو اگر تھوڑا پیچھے نہ کیا جائے تو رد عمل کے طور پر بال مخالف سمت میں دور تک لڑھک جائے گی اور کھلاڑی کی پہنچ سے دور ہو جائے گی۔',
           'د بدن توازن ساتئ او هاکي د توپ لوري ته ونیسئ. د توپ د لوري او سرعت سره سم هاکي پر ځمکه کېږدئ؛ کله چې توپ له هاکي سره ټکر وکړي، هاکي ته اجازه ورکړئ چې لږ شا ته راشي ترڅو د زوروره ګوزار زور کم شي. د هاکي د ټکر په پایله کې د نیوټن درېیم قانون پلي کېږي. که هاکي لږ شا ته نه شي، د غبرګون په توګه به توپ مخالف لوري ته لرې وغړېږي او د لوبغاړي له لاسرسي به ووځي.')])
    b.h('Dribbling', 'ڈربلنگ', 'ډریبلنګ')
    P(b, [('Keeping the ball in one’s possession, dodging other players and moving to attack the opposing team is called dribbling. While dribbling, the player, bending his waist, keeps the ball near his body so that the players of the other team cannot snatch the ball easily. In this skill the laws of motion and the conditions of balance apply.',
           'بال کو اپنے قبضے میں رکھتے ہوئے دوسرے کھلاڑیوں کو ڈاج کرتے ہوئے مخالف ٹیم پر حملہ آور ہونے کو ڈربلنگ کہتے ہیں۔ ڈربلنگ کرتے ہوئے کھلاڑی اپنی کمر کو جھکاتے ہوئے بال کو اپنے جسم کے قریب رکھیں تاکہ دوسری ٹیم کے کھلاڑی بال آسانی سے چھین نہ سکیں۔ اس مہارت میں حرکت کے قوانین اور توازن کی شرائط کا اطلاق ہوتا۔',
           'توپ په خپل واک کې ساتل، نور لوبغاړي غولول (ډاج کول) او پر مخالف ټیم برید کولو ته ډریبلنګ ویل کېږي. د ډریبلنګ پر مهال لوبغاړی ملا کږه کړي او توپ خپل بدن ته نږدې وساتي ترڅو د بل ټیم لوبغاړي یې په اسانۍ وانه خلي. په دې مهارت کې د حرکت قوانین او د توازن شرطونه پلي کېږي.')])
    b.h('Hitting', 'ہٹ لگانا', 'ګوزار')
    P(b, [('For hitting, the distance of the player from the ball should be about 2 feet. Both feet of the player …', 'ہٹ لگانے کے لیے کھلاڑی کا گیند سے فاصلہ 2 فٹ کے قریب ہونا چاہیے۔ کھلاڑی کے دونوں پاؤں …', 'د ګوزار لپاره د لوبغاړي واټن له توپه نږدې ۲ فټه وي. د لوبغاړي دواړه پښې …')])
    r = rec(b, 6, 9, 66)
    deco(r, 'A photograph of a hockey stick is decorative.')
    BOOK.save(66, [(6, r)], issues=[{'id': 'hpe12-pdf066', 'unit': 6, 'printedPage': 61,
               'description': 'An owner ballpoint signature at the top right is excluded. The left edge of the scan cuts some line ends (“ہاکی کو”, “ہاکی”, “عمل کے”, “ہونے”, “تاکہ”), completed from context. “اطلاق ہوتا۔”. Retained as printed.'}])


def p67():
    b = Builder()
    P(b, [('… should be such that balance can be maintained. Lifting the hockey stick to the right side, hit the ball.', 'ہونے چاہئیں تاکہ توازن برقرار رہ سکے۔ ہاکی کو دائیں جانب اٹھا کر گیند کو ہٹ کریں۔', '… باید داسې وي چې توازن وساتل شي. هاکي ښي لوري ته پورته کړئ او توپ ووهئ.'),
          ('By the application of Newton’s second law there is improvement in the skill. According to this law, when force is spent on a stationary ball with the help of the hockey stick, it produces acceleration in the ball in the direction of the force. The magnitude of acceleration in the ball depends on the force applied with the hockey stick; therefore the more force is spent, the farther the ball will go in the same proportion.',
           'نیوٹن کے دوسرے قانون کے اطلاق سے مہارت میں بہتری آتی ہے۔ اس قانون کے مطابق جب ہاکی کی مدد سے ساکن بال پر قوت صرف ہوتی ہے تو یہ قوت کی سمت میں بال میں اسراع پیدا کرتی ہے۔ بال میں اسراع کی مقدار ہاکی سے لگائی جانے والی قوت پر ہے لہٰذا جتنی قوت صرف کی جائے گی بال اسی تناسب سے دور جائے گا۔',
           'د نیوټن د دویم قانون په پلي کولو مهارت ښه کېږي. د دې قانون له مخې کله چې د هاکي په مرسته پر ولاړ توپ ځواک ولګول شي، د ځواک په لوري په توپ کې تعجیل پیدا کوي. په توپ کې د تعجیل اندازه پر هغه ځواک ولاړه ده چې په هاکي لګول کېږي؛ نو څومره ځواک چې ولګول شي، توپ به په همغه تناسب لرې ځي.')])
    b.h('Biomechanical principles in the scoop', 'سکوپ میں بائیو مکینیکل اصول', 'په سکوپ کې بایومیخانیکي اصول')
    P(b, [('Throwing the ball far while tossing it in the air is called a scoop. Along with defensive strategy, it is also sometimes used for attacking. Keeping the ball stationary, bringing the flat part of the hockey stick under the ball, bending the arms and knees, toss the ball into the air with the force of the lower hand.',
           'بال کو ہوا میں اچھالتے ہوئے دور پھینکنے کو سکوپ کہتے ہیں یہ دفاعی حکمت عملی کے ساتھ ساتھ بعض اوقات حملہ کرنے کے لیے بھی استعمال ہوتی ہے۔ بال کو ساکن کرتے ہوئے ہاکی کا چپٹا حصہ بال کے نیچے لاتے ہوئے بازوؤں اور گھٹنوں میں خم ڈالیں اور بال کو نیچے والے ہاتھ کے زور سے ہوا میں اچھالیں۔',
           'توپ هوا ته پورته کول او لرې غورځول سکوپ بلل کېږي؛ دا د دفاعي تګلارې تر څنګ کله کله د برید لپاره هم کارول کېږي. توپ ودروئ، د هاکي هوار برخه د توپ لاندې راوړئ، مټې او زنګونونه کاږه کړئ او د لاندېني لاس په زور توپ هوا ته پورته کړئ.'),
          ('Under projectile motion (Projectile Motion) the ball will cover distance in the air. Under the law of force, the more force applied, the farther the ball will go.', 'بال پروجیکٹائل موشن (Projectile Motion) کے زیرِ اثر ہوا میں فاصلہ طے کرے گا۔ قوت کے قانون کے تحت جتنی قوت لگے گی بال اتنا ہی دور جائے گا۔', 'توپ د پروجیکټایل حرکت (Projectile Motion) تر اغېز لاندې په هوا کې واټن وهي. د ځواک د قانون له مخې څومره ځواک چې ولګېږي، توپ هومره لرې ځي.')])
    r = rec(b, 6, 10, 67)
    deco(r, 'A photograph of a hockey match in front of the goal (Beijing 2008) is decorative.')
    BOOK.save(67, [(6, r)], issues=[{'id': 'hpe12-pdf067', 'unit': 6, 'printedPage': 62,
               'description': 'The printed page number is overwritten in owner pen (“62” → “61”-looking); the scan sequence confirms p.62. Retained as printed.'}])


def p68():
    b = Builder()
    b.h('Cricket', 'کرکٹ', 'کرکټ')
    P(b, [('In cricket there are the following skills.', 'کرکٹ میں مندرجہ ذیل مہارتیں ہیں۔', 'په کرکټ کې لاندې مهارتونه دي.')])
    L(b, [('Bowling (Bowling)', 'باؤلنگ (Bowling)', 'بالنګ (Bowling)'), ('Batting (Batting)', 'بیٹنگ (Batting)', 'بیټنګ (Batting)'), ('Fielding (Fielding)', 'فیلڈنگ (Fielding)', 'فیلډنګ (Fielding)')])
    P(b, [('There are two big kinds of bowling.', 'باؤلنگ کی دو بڑی اقسام ہیں۔', 'بالنګ دوه لوی ډولونه لري.')])
    L(b, [('Fast bowling (Fast Bowling)', 'تیز باؤلنگ (Fast Bowling)', 'چټک بالنګ (Fast Bowling)'), ('Spin bowling (Spin Bowling)', 'سپن باؤلنگ (Spin Bowling)', 'سپین بالنګ (Spin Bowling)')])
    b.h('Fast Bowling', 'فاسٹ باؤلنگ (Fast Bowling)', 'چټک بالنګ (Fast Bowling)')
    P(b, [('In fast bowling the bowler, using the clean and rough part of the ball, can turn the ball inwards; this is called In Swing, and turning it outwards is called Out Swing.',
           'فاسٹ باؤلنگ میں باؤلر بال کا صاف اور کھردرا حصہ استعمال کرتے ہوئے بال کو اندر کی طرف موڑ سکتا ہے اسے (In Swing) کہتے ہیں اور باہر کی طرف موڑنے کو (Out Swing) کہتے ہیں۔',
           'په چټک بالنګ کې بالر د توپ پاکه او زیږه برخه کاروي او توپ دننه خوا ته اړولی شي چې (In Swing) ورته ویل کېږي او بهر خوا ته اړولو ته (Out Swing) ویل کېږي.'),
          ('When the bowler keeps the rough part of the ball towards the outside, the air acts on the rough surface of the ball, while the clean part of the ball goes ahead compared to the rough part; because of the resistance of the air the rough part remains behind, and the ball swings outwards. Whereas for in-swing, when the player keeps the rough part towards the inside, the air, acting on the rough part of the ball, becomes the cause of resistance and the ball swings inwards.',
           'جب باؤلر گیند کا کھردرا حصہ باہر کی جانب رکھتا ہے تو ہوا بال کی کھردری سطح پر اثر کرتی ہے جب کہ بال کا صاف حصہ کھردرے حصے کی نسبت پہلے آگے جاتا ہے ہوا کی رکاوٹ کی وجہ سے کھردرا حصہ پیچھے رہتا ہے اور بال باہر کی طرف (Swing) کرتی ہے۔ جب کہ ان سوئنگ کے لیے کھردرے حصے کو کھلاڑی اندر کی جانب رکھتا ہے ہوا بال کے کھردرے حصے پر عمل کر کے رکاوٹ کا سبب بنتی ہے اور بال اندر کی جانب سوئنگ کرتی ہے۔',
           'کله چې بالر د توپ زیږه برخه بهر ته ساتي، هوا د توپ پر زیږه سطحه اغېز کوي، په داسې حال کې چې د توپ پاکه برخه د زیږې برخې په پرتله مخکې ځي؛ د هوا د خنډ له امله زیږه برخه شاته پاتې کېږي او توپ بهر ته (Swing) کوي. خو د ان سوینګ لپاره لوبغاړی زیږه برخه دننه ته ساتي؛ هوا د توپ پر زیږه برخه عمل کوي، د خنډ لامل کېږي او توپ دننه ته سوینګ کوي.')])
    b.h('Spin Bowling', 'سپن باؤلنگ (Spin Bowling)', 'سپین بالنګ (Spin Bowling)')
    P(b, [('There are two kinds of spin bowling.', 'سپن باؤلنگ کی دو اقسام ہیں۔', 'سپین بالنګ دوه ډولونه لري.')])
    L(b, [('Leg spin (Leg spin)', 'لیگ سپن (Leg spin)', 'لیګ سپین (Leg spin)'), ('Off spin (Off spin)', 'آف سپن (Off spin)', 'اف سپین (Off spin)')])
    r = rec(b, 6, 11, 68)
    BOOK.save(68, [(6, r)])


def p69():
    b = Builder()
    b.h('Leg Spin', 'لیگ سپن (Leg Spin)', 'لیګ سپین (Leg Spin)')
    P(b, [('The skill of turning the ball with the wrist is called leg spin. In leg spin the bowler, turning the hand in such a way, throws the ball from the back part of the hand that the ball, landing on the pitch at the leg, passes from the off side of the right-hand batsman.',
           'کلائی سے بال کو گھمانے کی مہارت کو لیگ سپن کہتے ہیں۔ لیگ سپن میں باؤلر ہاتھ کو اس انداز میں گھما کر بال کو ہاتھ کے پچھلے حصے سے پھینکتا ہے کہ بال پچ پر لگ کر رائیٹ ہینڈ بیٹسمین کے آف سائیڈ سے گزرتی ہے۔',
           'په مړوند د توپ د تاوولو مهارت ته لیګ سپین ویل کېږي. په لیګ سپین کې بالر لاس داسې تاووي او توپ د لاس له شاتنۍ برخې غورځوي چې توپ پر پیچ لګي او د ښي لاسي بیټسمن له اف اړخه تېرېږي.')])
    b.h('Off Spin', 'آف سپن (Off Spin)', 'اف سپین (Off Spin)')
    P(b, [('In off spin the ball is turned with the fingers in such a way that the ball, landing on the off stump of the right-hand batsman, comes towards the leg stump. In both kinds of bowling the action of projectile motion is involved. The better the parabola (Parabola), the more the possibilities of spin.',
           'آف سپن میں انگلیوں سے بال کو اس طرح گھمایا جاتا ہے کہ بال رائیٹ ہینڈ بیٹسمین کے آف سٹمپ پر پڑ کر لیگ سٹمپ کی جانب آتا ہے۔ دونوں طرح کی باؤلنگ میں پروجیکٹائل موشن کا عمل دخل ہے۔ جتنا اچھا پیرابولا (Parabola) ہوگا اتنی ہی سپن کے زیادہ امکانات ہوتے ہیں۔',
           'په اف سپین کې توپ په ګوتو داسې تاوول کېږي چې توپ د ښي لاسي بیټسمن پر اف سټمپ لګي او لیګ سټمپ ته راځي. په دواړو ډوله بالنګ کې د پروجیکټایل حرکت لاس دی. څومره چې پیرابولا (Parabola) ښه وي، هومره د سپین امکانات ډېر وي.')])
    b.h('Batting', 'بیٹنگ (Batting)', 'بیټنګ (Batting)')
    P(b, [('In the skill of batting there are the following components.', 'بیٹنگ کی مہارت میں مندرجہ ذیل اجزا ہیں۔', 'د بیټنګ په مهارت کې لاندې برخې دي.')])
    L(b, [('Foot work (Foot Work)', 'فٹ ورک (Foot Work)', 'د پښو کار (Foot Work)'), ('Timing (Timing)', 'ٹائمنگ (Timing)', 'وخت‌ټاکنه (Timing)')])
    b.h('Foot Work', 'فٹ ورک (Foot Work)', 'د پښو کار (Foot Work)')
    P(b, [('The batsman adjusting his body position according to the line and length (Line and Length) of the ball is called footwork.', 'بیٹسمین کا بال کی لائن اور لینتھ (Line and Length) کے مطابق اپنی باڈی پوزیشن کو ایڈجسٹ کرنا فٹ ورک کہلاتا ہے۔', 'د بیټسمن له خوا د توپ د لاین او لینتھ (Line and Length) سره سم د خپل بدن د حالت برابرول د پښو کار بلل کېږي.')])
    b.h('Timing', 'ٹائمنگ (Timing)', 'وخت‌ټاکنه (Timing)')
    P(b, [('The player hitting the ball at that time when he is in such a position that the ball is near his body and he succeeds in hitting the ball with the centre of the bat.', 'کھلاڑی کا بال کو اس وقت ہٹ کرنا جب وہ اس پوزیشن میں ہو کہ بال اس کی باڈی کے قریب ہو اور بال کو وہ بیٹ کے سینٹر سے مارنے میں کامیاب ہو۔', 'د لوبغاړي له خوا توپ په هغه وخت وهل چې په داسې حالت کې وي چې توپ یې بدن ته نږدې وي او توپ د بیټ له منځه په وهلو کې بریالی شي.')])
    r = rec(b, 6, 12, 69)
    deco(r, 'A photograph of a batsman sweeping in front of the wicketkeeper is decorative.')
    BOOK.save(69, [(6, r)])


def p70():
    b = Builder()
    P(b, [('Timing always comes from bringing the ball into the line and playing in a better manner. By playing across, the chances of the ball striking the edge of the bat and rising into the air increase. In batting the law of inertia applies. When the ball is thrown towards the batsman, it moves in a straight line, whereas after striking the bat resistance comes in its motion; but when the batsman plays it, he too spends force on it. Therefore as a reaction of the action the ball goes far.',
           'ٹائمنگ ہمیشہ بال کو لائن میں آ کر بہتر انداز سے کھیلنے سے آتی ہے۔ کراس کھیلنے سے بیٹ کے باہر کے کنارے سے بال ٹکرا کر ہوا میں اچھلنے کے امکانات بڑھ جاتے ہیں۔ بیٹنگ میں جمود کا قانون لاگو ہوتا ہے۔ جب بال بازو کی طرف سے پھینکی جاتی ہے تو وہ خطِ مستقیم میں حرکت کرتی ہے۔ جب کہ بیٹ سے ٹکرانے کے بعد اس کی حرکت میں مزاحمت آتی ہے لیکن جب بیٹسمین اسے کھیلتا ہے تو وہ بھی اس پر قوت صرف کرتا ہے۔ لہٰذا عمل کے رد عمل کے طور پر بال دور جاتا ہے۔',
           'وخت‌ټاکنه تل له لاین ته د راتګ او په ښه ډول لوبولو راځي. په کراس لوبولو د بیټ له بهرني څنډې د توپ د ټکر او هوا ته د پورته کېدو امکانات زیاتېږي. په بیټنګ کې د جمود قانون پلي کېږي. کله چې توپ (بیټسمن) ته غورځول کېږي، په مستقیمه کرښه حرکت کوي؛ له بیټ سره د ټکر وروسته یې په حرکت کې مقاومت راځي، خو کله چې بیټسمن یې لوبوي، هغه هم پرې ځواک لګوي. نو د عمل د غبرګون په توګه توپ لرې ځي.')])
    b.h('Fielding', 'فیلڈنگ (Fielding)', 'فیلډنګ (Fielding)')
    P(b, [('In fielding stopping the ball and catching are included. In both skills the law of absorption of force acts. To stop the ball and to catch, bringing the hands in line with the ball, motion is given backwards a little, so that the reaction of the action which occurs from the force of the ball on the hands may be reduced as much as possible in the opposite direction.',
           'فیلڈنگ میں بال کو روکنا اور کیچ کرنا شامل ہیں۔ دونوں مہارتوں میں قوت کے انجذاب کا قانون عمل ہے۔ بال کو روکنے اور کیچ کرنے کے لیے ہاتھوں کو بال کی سیدھ میں لاتے ہوئے تھوڑا پیچھے کی جانب حرکت دی جاتی تاکہ ہاتھوں پر بال کی قوت لگنے سے جو عمل وقوع پذیر ہوتا ہے اس کا ردِ عمل مخالف سمت میں کم سے کم کیا جا سکے۔',
           'په فیلډنګ کې توپ درول او کیچ نیول شامل دي. په دواړو مهارتونو کې د ځواک د جذب قانون فعال دی. د توپ د درولو او کیچ لپاره لاسونه د توپ په سیده کې راوړل کېږي او لږ شا ته خوځول کېږي ترڅو پر لاسونو د توپ د ځواک له لګېدو چې کوم عمل رامنځته کېږي، د هغه غبرګون په مخالف لوري تر ټولو کم شي.')])
    r = rec(b, 6, 13, 70)
    deco(r, 'A photograph of three fielders in the slips is decorative.')
    BOOK.save(70, [(6, r)], issues=[{'id': 'hpe12-pdf070', 'unit': 6, 'printedPage': 65,
               'description': 'Line ends at the left edge are cut (“کنارے”, “بازو”, “حرکت”, “طور”, “عمل”) and completed from context; “بازو کی طرف سے” read where the word is cut. “حرکت دی جاتی تاکہ”. Retained as printed.'}])


def p71():
    b = Builder()
    b.h('Long Jump', 'لانگ جمپ (Long Jump)', 'اوږد ټوپ (Long Jump)')
    P(b, [('In the long jump the following stages are included.', 'لانگ جمپ میں مندرجہ ذیل مراحل شامل ہیں۔', 'په اوږد ټوپ کې لاندې پړاوونه شامل دي.')])
    L(b, [('Approach (Approach)', 'اپروچ (Approach)', 'نږدې کېدل (Approach)'), ('Jumping (Take off)', 'جمپ کرنا (Take off)', 'ټوپ وهل (Take off)'), ('Flight (Flight)', 'اڑان (Flight)', 'الوتنه (Flight)'), ('Landing and recovery (Landing and recovery)', 'لینڈنگ اور ریکوری (Landing and recovery)', 'کېناستل او رغونه (Landing and recovery)')])
    b.h('Approach', 'اپروچ (Approach)', 'نږدې کېدل (Approach)')
    P(b, [('In the long jump the determination of the approach depends on the ability of the athlete. Some players jump using speed; they are called speed jumpers, and some players jump using strength; they are called power jumpers.', 'لانگ جمپ میں اپروچ (Approach) کا تعین اتھلیٹ کی اہلیت پر منحصر ہوتا ہے۔ کچھ کھلاڑی سپیڈ کو استعمال کرتے ہوئے جمپ کرتے ہیں انہیں سپیڈ جمپر کہتے ہیں اور کچھ کھلاڑی طاقت کا استعمال کر کے جمپ کرتے ہیں انہیں پاور جمپر کہتے ہیں۔', 'په اوږد ټوپ کې د اپروچ (Approach) ټاکنه د ورزشکار پر وړتیا ولاړه ده. ځینې لوبغاړي سرعت کاروي او ټوپ وهي، سپیډ جمپر ورته ویل کېږي او ځینې لوبغاړي ځواک کاروي او ټوپ وهي، پاور جمپر ورته ویل کېږي.'),
          ('In the approach the following three qualities should be present.', 'اپروچ (Approach) میں مندرجہ ذیل تین خوبیاں ہونی چاہئیں۔', 'په اپروچ (Approach) کې لاندې درې ځانګړنې باید وي.')])
    L(b, [('Optimal speed: that speed over which there is control.', 'اپٹیمل سپیڈ (Optimal speed) وہ رفتار جس پر کنٹرول ہو۔', 'غوره سرعت (Optimal speed): هغه سرعت چې کنټرول پرې وي.'), ('Rhythm (Rhythmic)', 'ردھم (Rhythmic)', 'ریتم (Rhythmic)'), ('Consistency (Consistent)', 'یکسانیت (Consistent)', 'یووالی (Consistent)')])
    b.h('Biomechanical principles in the Approach', 'اپروچ (Approach) میں بائیو مکینیکل اصول', 'په اپروچ (Approach) کې بایومیخانیکي اصول')
    P(b, [('For running, the player applies full force with his legs on the surface of the ground, as a reaction to which he moves forward. According to the third law of motion, the more force applied, the more will be the reaction in the opposite direction. Therefore the player should gain speed by applying force.', 'کھلاڑی دوڑنے کے لیے اپنی ٹانگوں سے بھرپور قوت زمین کی سطح پر لگاتا ہے جس کے رد عمل کے طور پر وہ آگے کی جانب حرکت کرتا ہے۔ حرکت کے تیسرے قانون کے مطابق جتنی قوت لگائی جائے گی اتنا ہی مخالف سمت میں رد عمل ہوگا۔ اس لیے کھلاڑی کو قوت لگا کر رفتار حاصل کرنی چاہیے۔', 'لوبغاړی د منډې لپاره په پښو بشپړ ځواک پر ځمکه لګوي چې د غبرګون په توګه مخکې خوځي. د حرکت د درېیم قانون له مخې څومره ځواک چې ولګول شي، هومره به مخالف لوري ته غبرګون وي. نو لوبغاړی باید په ځواک لګولو سرعت ترلاسه کړي.')])
    r = rec(b, 6, 14, 71)
    deco(r, 'A photograph of a long jumper in flight is decorative.')
    BOOK.save(71, [(6, r)], issues=[{'id': 'hpe12-pdf071', 'unit': 6, 'printedPage': 66,
               'description': 'An owner ballpoint signature over the photograph is excluded. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 66
    {66: p66, 67: p67, 68: p68, 69: p69, 70: p70, 71: p71}[n]()
