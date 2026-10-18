"""HPE XII PDF60–65: pp.55–60 — biomechanical principles in netball (catching, speed and height of ball, direction, passing, pivot pass, shooting)
and volleyball (service kinds, digging, boosting, smashing). Run: python class12_hpe_page060.py N (60–65)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p60():
    b = Builder()
    b.h('Biomechanical principles for increasing ability in different games', 'مختلف کھیلوں میں صلاحیت بڑھانے کے لیے بائیو مکینیکل اصول', 'په بېلابېلو لوبو کې د وړتیا د زیاتولو لپاره بایومیخانیکي اصول')
    b.h('Netball', 'نیٹ بال', 'نېټبال')
    b.h('Increase in performance in netball through biomechanical principles:', 'نیٹ بال میں بائیو مکینیکل اصولوں سے کارکردگی میں اضافہ:', 'په نېټبال کې د بایومیخانیکي اصولو له لارې د کړنو زیاتوالی:')
    P(b, [('Netball is played in a court of rectangular shape. Its length is 30.50 metres and breadth 15.25 metres. In it the player scores by putting the ball into a ring 10 feet high from the ground. For it the following skills are necessary.',
           'نیٹ بال ایک مستطیل شکل کے کورٹ میں کھیلا جاتا ہے۔ اس کی لمبائی 30.50 میٹر اور چوڑائی 15.25 میٹر ہوتی ہے۔ اس میں کھلاڑی زمین سے 10 فٹ اونچے رِنگ میں بال ڈال کر سکور کرتا ہے۔ اس کے لیے مندرجہ ذیل مہارتیں ضروری ہیں۔',
           'نېټبال په یوه مستطیل ډوله میدان کې لوبول کېږي. اوږدوالی یې ۳۰.۵۰ متره او پلنوالی یې ۱۵.۲۵ متره وي. په کې لوبغاړی له ځمکې ۱۰ فټه لوړ کړۍ (رنګ) ته توپ اچوي او نمره اخلي. د دې لپاره لاندې مهارتونه اړین دي.')])
    L(b, [('Catching the ball', 'بال کو پکڑنا', 'توپ نیول'), ('Passing', 'پاس کرنا', 'پاس کول'), ('Passing the ball through the ring', 'رنگ سے بال گزارنا', 'له کړۍ توپ تېرول')])
    b.h('Catching the ball', 'بال پکڑنا', 'توپ نیول')
    P(b, [('To catch a pass given by one’s fellow player it is necessary to take care of three things.', 'اپنے ساتھی کھلاڑی کی جانب سے دیے گئے پاس کو پکڑنے کے لیے تین باتوں کا خیال رکھنا ضروری ہے۔', 'د خپل ملګري لوبغاړي له خوا ورکړل شوي پاس د نیولو لپاره درې خبرو ته پام اړین دی.')])
    b.h('Speed of the ball', 'بال کی رفتار', 'د توپ سرعت')
    P(b, [('To gain possession of the ball it is necessary that the speed of the ball be estimated. The faster the ball comes towards you, the more the collision will arise. Here the third law of motion applies, i.e. the reaction of an action is equal but in the opposite direction. Therefore as soon as the ball touches the player’s hands, he should move the arms backwards while closing the hands; otherwise the fast ball, striking the hands, will go away in the opposite direction with the same speed.',
           'بال پر قبضہ حاصل کرنے کے لیے ضروری ہے کہ بال کی رفتار کا اندازہ لگایا جائے۔ جتنی تیزی سے بال آپ جانب آئے گا اتنا ہی ٹکراؤ پیدا ہوگا۔ یہاں حرکت کا تیسرا قانون لاگو ہوگا۔ یعنی عمل کا رد عمل برابر مگر مخالف سمت میں ہوتا ہے۔ لہٰذا جیسے ہی بال کھلاڑی کے ہاتھوں کو چھوئے تو وہ ہاتھوں کو بند کرتے ہوئے بازوؤں کو پیچھے کی جانب حرکت دے دوسری صورت میں تیز رفتار بال ہاتھوں سے ٹکرا کر اتنی رفتار سے مخالف سمت میں چلا جائے گا۔',
           'پر توپ د واک ترلاسه کولو لپاره اړینه ده چې د توپ سرعت اټکل شي. څومره چې توپ په چټکۍ ستاسو خوا ته راشي، هومره ټکر پیدا کېږي. دلته د حرکت درېیم قانون پلي کېږي، یعنې د عمل غبرګون برابر خو مخالف لوري ته وي. نو کله چې توپ د لوبغاړي لاسونو ته ورسېږي، لاسونه دې بند کړي او مټې دې شا ته وخوځوي، که نه نو چټک توپ له لاسونو سره ټکر کوي او په همغه سرعت مخالف لوري ته ځي.')])
    b.h('Height of the ball', 'بال کی سطح', 'د توپ لوړوالی')
    P(b, [('If the ball is coming high towards the player, then the player will have to jump and catch the ball. In this case it is necessary to maintain balance.', 'بال اگر کھلاڑی کی جانب اونچی آ رہی ہو تو کھلاڑی کو جمپ لگا کر بال کو پکڑنا ہوگا۔ اس صورت میں توازن کو برقرار رکھنا ضروری ہے۔', 'که توپ لوبغاړي ته لوړ راځي، لوبغاړی باید ټوپ ووهي او توپ ونیسي. په دې صورت کې د توازن ساتل اړین دي.')])
    r = rec(b, 6, 3, 60)
    BOOK.save(60, [(6, r)], issues=[{'id': 'hpe12-pdf060', 'unit': 6, 'printedPage': 55,
               'description': 'Line ends at the left edge of the scan are cut (“چوڑائی”, “اس کے”, “سمت میں”, “توازن”) and completed from context. An owner pen line down the page is excluded. “بال آپ جانب آئے گا”, “بال … اونچی آ رہی ہو”. Retained as printed.'}])


def p61():
    b = Builder()
    b.h('Direction of the ball', 'بال کی سمت', 'د توپ لوری')
    P(b, [('According to the direction of the ball it is necessary to adjust one’s body immediately; here too the principle of balance will apply.', 'بال کی سمت کے مطابق فوری طور پر اپنے جسم کو ایڈجسٹ کرنا ضروری ہے یہاں بھی توازن کا اصول لاگو ہوگا۔', 'د توپ د لوري سره سم سمدستي د خپل بدن برابرول اړین دي؛ دلته هم د توازن اصل پلي کېږي.')])
    sil = ''.join(f'<g transform="translate({40 + i * 70},0)"><circle cx="20" cy="{70 - i * 8}" r="9" fill="#e5a46a"/><rect x="10" y="{82 - i * 8}" width="20" height="55" rx="6" fill="#1e3a8a"/>'
                  f'<line x1="14" y1="{137 - i * 8}" x2="10" y2="180" stroke="#1e293b" stroke-width="7"/><line x1="26" y1="{137 - i * 8}" x2="30" y2="180" stroke="#1e293b" stroke-width="7"/>'
                  f'<line x1="20" y1="{90 - i * 8}" x2="{20 + i * 2}" y2="{60 - i * 14}" stroke="#e5a46a" stroke-width="6"/><circle cx="{24 + i * 2}" cy="{52 - i * 14}" r="9" fill="#ea580c"/></g>' for i in range(6))
    from class12_hpe_common import svg
    sv = [svg(460, 210, sil, c) for c in ('Sequence of a jump shot', 'جمپ شاٹ کے مراحل', 'د ټوپ شاټ پړاوونه')]
    b.visual('hpe12-fig-jump-shot', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Passing the ball', 'بال کو پاس کرنا', 'توپ پاس کول')
    P(b, [('The player can pass the ball in the following ways.', 'کھلاڑی مندرجہ ذیل طریقوں سے بال کو پاس کر سکتا ہے۔', 'لوبغاړی په لاندې طریقو توپ پاس کولی شي.')])
    b.h('i. Passing with both hands', 'i۔ دونوں ہاتھوں سے پاس کرنا', 'i. په دواړو لاسونو پاس کول')
    P(b, [('The player can pass the ball while holding it in both hands with equal strength of both arms. While doing so the second law of motion applies. When a force is applied on a body, it moves in the same direction and acceleration is produced in it. Therefore while passing the ball force should be applied keeping in view the distance of one’s fellow player.',
           'کھلاڑی بال کو دونوں ہاتھوں میں تھامتے ہوئے دونوں بازوؤں کی مساوی طاقت سے بال کو پاس کر سکتا ہے۔ ایسا کرتے ہوئے حرکت کا دوسرا قانون لاگو ہوتا ہے۔ جب کسی جسم پر قوت لگائی جائے تو وہ اسی سمت میں حرکت کرتا ہے اور اس میں اسراع پیدا ہوتا ہے۔ اس لیے بال کو پاس کرتے وقت اپنی ساتھی کھلاڑی کے فاصلے کو مد نظر رکھتے ہوئے قوت لگانی چاہیے۔',
           'لوبغاړی توپ په دواړو لاسونو کې نیسي او د دواړو مټو په برابر ځواک یې پاس کولی شي. په دې کار کې د حرکت دویم قانون پلي کېږي. کله چې پر یوه جسم ځواک ولګول شي، په همغه لوري خوځي او تعجیل پکې پیدا کېږي. نو د توپ د پاس پر وخت دې د ملګري لوبغاړي واټن ته په کتو ځواک ولګول شي.')])
    r = rec(b, 6, 4, 61)
    BOOK.save(61, [(6, r)], issues=[{'id': 'hpe12-pdf061', 'unit': 6, 'printedPage': 56,
               'description': 'The six-frame photograph of a basketball player taking a jump shot is reproduced as a coded schematic sequence. An owner Urdu ballpoint note under it is excluded. “اپنی ساتھی کھلاڑی”. Retained as printed.'}])


def p62():
    b = Builder()
    b.h('ii. Pivot Pass', 'ii۔ پیوٹ پاس (Pivot Pass)', 'ii. پیوټ پاس (Pivot Pass)')
    P(b, [('In the pivot pass the ball is passed by turning on one foot. In this method one foot remains with the ground. Since in this action force is also applied on the ball while turning quickly, therefore the principle of balance applies here.', 'پیوٹ پاس میں ایک پاؤں پر گھوم کر بال پاس کیا جاتا ہے۔ اس طریقے میں ایک پاؤں زمین کے ساتھ رہتا ہے چونکہ اس عمل میں تیزی سے گھومتے ہوئے بال پر قوت بھی لگائی جاتی ہے اس لیے توازن کا اصول یہاں پر لاگو ہوتا ہے۔', 'په پیوټ پاس کې پر یوه پښه تاو کېږي او توپ پاس کېږي. په دې طریقه کې یوه پښه له ځمکې سره پاتې کېږي؛ څرنګه چې په دې عمل کې په چټکۍ تاوېدو سره پر توپ ځواک هم لګول کېږي، نو دلته د توازن اصل پلي کېږي.')])
    b.h('Passing the ball through the ring', 'رنگ سے بال گزارنا', 'له کړۍ توپ تېرول')
    P(b, [('The player, while scoring, passes the ball through the ring. With one hand or with both hands, with the help of the wrists, the ball is thrown towards the ring. During this action, determining the direction and keeping the distance in view, force should be applied on the ball. Here the laws of motion will apply.', 'کھلاڑی سکور کرتے ہوئے بال کو رنگ سے گزارتا ہے۔ ایک ہاتھ سے یا دونوں ہاتھوں سے کلائی کی مدد سے بال کو رنگ کی جانب پھینکا جاتا ہے اس عمل کے دوران سمت کا تعین کرتے ہوئے اور فاصلے کو مدِ نظر رکھتے ہوئے بال پر قوت لگانی چاہیے۔ یہاں حرکت کے قوانین لاگو ہوں گے۔', 'لوبغاړی د نمرې اخیستو پر مهال توپ له کړۍ تېروي. په یوه یا دواړو لاسونو د مړوندونو په مرسته توپ کړۍ ته غورځول کېږي؛ د دې عمل پر مهال دې د لوري ټاکلو او واټن ته په پام سره پر توپ ځواک ولګول شي. دلته د حرکت قوانین پلي کېږي.')])
    b.h('Biomechanical principles in volleyball', 'والی بال میں بائیو مکینیکل اصول', 'په والیبال کې بایومیخانیکي اصول')
    P(b, [('In the game of volleyball the following skills are of importance; by using biomechanical principles in them performance can be increased.', 'والی بال کے کھیل میں مندرجہ ذیل مہارتیں اہمیت کی حامل ہیں ان میں بائیو مکینیکل اصولوں کو استعمال کر کے کارکردگی میں اضافہ کیا جا سکتا ہے۔', 'د والیبال په لوبه کې لاندې مهارتونه اهمیت لري؛ په دوی کې د بایومیخانیکي اصولو په کارولو کړنې زیاتېدای شي.')])
    L(b, [('Service (Service)', 'سروس کرنا (Service)', 'سرویس (Service)'), ('Lifting the ball (Digging)', 'بال کو اٹھانا (Digging)', 'توپ پورته کول (Digging)'), ('Boosting (Boosting)', 'بوسٹنگ (Boosting)', 'بوسټینګ (Boosting)'), ('Smashing (Smashing)', 'سمیش کرنا (Smashing)', 'سمیش کول (Smashing)')])
    b.h('i. Serving', 'i۔ سروس کرنا', 'i. سرویس کول')
    P(b, [('In volleyball service is of extreme importance. Attack can be made through service. Points can be obtained through good service. But weak service brings the team to a defensive position. The following are the methods of service.', 'والی بال میں سروس انتہائی اہمیت کی حامل ہے۔ سروس سے اٹیک کی جا سکتی ہے۔ اچھی سروس سے پوائنٹ حاصل کیا جا سکتا ہے۔ لیکن کمزور سروس ٹیم کو دفاعی پوزیشن پر لے آتی ہے۔ سروس کے مندرجہ ذیل طریقے ہیں۔', 'په والیبال کې سرویس ډېر اهمیت لري. له سرویس برید کېدای شي. په ښه سرویس نمره ترلاسه کېدای شي. خو کمزوری سرویس ټیم دفاعي حالت ته راولي. د سرویس لاندې طریقې دي.')])
    r = rec(b, 6, 5, 62)
    BOOK.save(62, [(6, r)], issues=[{'id': 'hpe12-pdf062', 'unit': 6, 'printedPage': 57,
               'description': 'The first lines of p.57 are cut at the left edge (“زمین کے ساتھ”, “یہاں پر لاگو”, “مدد سے”, “بال پر”) and completed from context. Retained as printed.'}])


def p63():
    b = Builder()
    L(b, [('Under Hand Service', 'انڈر ہینڈ سروس (Under Hand Service)', 'لاندې لاس سرویس (Under Hand Service)'), ('Over Hand Service', 'اوور ہینڈ سروس (Over Hand Service)', 'پورته لاس سرویس (Over Hand Service)'),
          ('Round Hand Service', 'راونڈ ہینڈ سروس (Round Hand Service)', 'ګرد لاس سرویس (Round Hand Service)'), ('Smash Service', 'سمیش سروس (Smash Service)', 'سمیش سرویس (Smash Service)')])
    b.h('Under hand service', 'انڈر ہینڈ سروس', 'لاندې لاس سرویس')
    P(b, [('While serving, the player’s face is towards the net. The feet should be so placed in the service area that between the front foot and the back foot there is a distance equal to the shoulders. The player will toss the ball in the air with one hand and will hit the ball from below with the other hand. Both laws of force will apply. According to the first law the ball will not come into motion until an external force is applied by the other hand, while according to the second law, when some force acts on a body, acceleration is produced in it. Therefore the greater the force with which the ball is hit, the faster the ball will go into the opposite court.',
           'سروس کرتے وقت کھلاڑی کا منہ نیٹ کی طرف ہوتا ہے۔ پاؤں سروس ایریا میں اس طرح رکھے ہوں کہ اگلے پاؤں اور پچھلے پاؤں کے درمیان کندھے کے برابر فاصلہ ہو۔ کھلاڑی ایک ہاتھ سے بال کو ہوا میں اچھالے گا اور دوسرے ہاتھ سے نیچے سے بال کو مارے گا۔ قوت کے دونوں قوانین لاگو ہوں گے۔ پہلے قانون کے مطابق بال اس وقت تک حرکت میں نہیں آئے گا جب تک دوسرے ہاتھ سے بیرونی قوت نہ لگے۔ جب کہ دوسرے قانون کے مطابق جب کوئی قوت کسی جسم پر عمل کرتی ہے تو اس میں اسراع پیدا ہوتا ہے۔ لہٰذا جتنی قوت سے بال کو مارا جائے گا اتنی ہی تیزی سے مخالف کورٹ میں بال جائے گا۔',
           'د سرویس پر وخت د لوبغاړي مخ جال ته وي. پښې دې د سرویس په ساحه کې داسې کېښودل شي چې د مخکینۍ او شاتنۍ پښې ترمنځ د اوږو په اندازه واټن وي. لوبغاړی به په یوه لاس توپ هوا ته پورته کړي او په بل لاس به یې له لاندې ووهي. د ځواک دواړه قوانین پلي کېږي. د لومړي قانون له مخې توپ تر هغه نه خوځي چې په بل لاس بهرنی ځواک پرې ونه لګېږي، په داسې حال کې چې د دویم قانون له مخې کله چې ځواک پر جسم عمل وکړي، تعجیل پکې پیدا کېږي. نو په څومره ځواک چې توپ ووهل شي، هومره په چټکۍ به مخالف میدان ته لاړ شي.')])
    b.h('Over Hand Service', 'اوور ہینڈ سروس (Over Hand Service)', 'پورته لاس سرویس (Over Hand Service)')
    P(b, [('In this service the player’s face will be towards the net; the feet in the service area will be forward and backward. The ball will be tossed in the air with one hand and the ball will be hit with force from above the head with the other hand.', 'اس سروس میں کھلاڑی کا منہ نیٹ کی طرف ہوگا پاؤں سروس ایریا میں آگے پیچھے ہوں گے ایک ہاتھ سے بال کو ہوا میں اچھالا جائے گا دوسرے ہاتھ سے بال کو سر کے اوپر سے قوت کے ساتھ مارا جائے گا۔', 'په دې سرویس کې د لوبغاړي مخ جال ته وي؛ پښې د سرویس په ساحه کې مخکې وروسته وي؛ په یوه لاس توپ هوا ته پورته کېږي او په بل لاس له سر پورته په ځواک وهل کېږي.')])
    r = rec(b, 6, 6, 63)
    deco(r, 'Drawings of a player making an underhand serve and of a player making an overhand serve are decorative.')
    BOOK.save(63, [(6, r)])


def p64():
    b = Builder()
    P(b, [('… performance can be increased by applying the laws of motion.', 'حرکت کے قوانین لاگو کرنے سے کارکردگی میں اضافہ کیا جا سکتا ہے۔', '… د حرکت د قوانینو په پلي کولو کړنې زیاتېدای شي.')])
    b.h('Round Service', 'راونڈ سروس (Round Service)', 'ګرد سرویس (Round Service)')
    P(b, [('The shoulder will be towards the net and the face towards the side line. The feet will be parallel to the service line. Bending the front slightly, hit the ball while tossing it in the air. The first and second laws of motion will apply.', 'نیٹ کی جانب کندھا ہوگا اور منہ سائیڈ لائن کی طرف ہوگا۔ پاؤں سروس لائن پر متوازی ہوں گے۔ اگلا تھوڑا سا جھکا کر بال کو ہوا میں اچھالتے ہوئے ماریں۔ حرکت کا پہلا اور دوسرا قانون لاگو ہوگا۔', 'اوږه به جال ته وي او مخ به د څنګ کرښې ته وي. پښې به د سرویس پر کرښه موازي وي. مخکینۍ (پښه/بدن) لږ کوږ کړئ او توپ هوا ته پورته کوئ او ووهئ. د حرکت لومړی او دویم قانون پلي کېږي.')])
    b.h('Smash Service', 'سمیش سروس (Smash Service)', 'سمیش سرویس (Smash Service)')
    P(b, [('The player, from behind the service line, tossing the ball in the air inside the service area, taking a few steps towards the net and jumping, will hit the ball in the manner of a smash. In this activity the third law of force and the state of balance will apply, because to jump the player will apply force on the surface of the ground with the legs. As a result of the reaction, the body of the player will go up into the air to the same height.',
           'کھلاڑی سروس لائن سے پیچھے سروس ایریا کے اندر بال کو ہوا میں اچھال کر چند قدم نیٹ کی جانب لے کر جمپ کرتے ہوئے سمیش کے انداز میں بال کو مارے گا۔ اس سرگرمی میں قوت کا تیسرا قانون اور توازن کی حالت کا اطلاق ہوگا۔ کیونکہ جمپ کرنے کے لیے زمین کی سطح پر کھلاڑی ٹانگوں سے قوت لگائے گا۔ نتیجتاً ردِ عمل کے طور پر کھلاڑی کا جسم اتنا ہی اونچا ہوا میں جائے گا۔',
           'لوبغاړی له سرویس کرښې شا، د سرویس په ساحه کې توپ هوا ته پورته کوي، جال ته څو قدمه اخلي او ټوپ وهي او د سمیش په بڼه توپ وهي. په دې فعالیت کې د ځواک درېیم قانون او د توازن حالت پلي کېږي، ځکه د ټوپ لپاره لوبغاړی په پښو پر ځمکه ځواک لګوي؛ په پایله کې د غبرګون په توګه د لوبغاړي بدن هومره لوړ هوا ته ځي.')])
    b.h('Lifting the ball and biomechanical principles (Digging)', 'بال کو اٹھانا، اور بائیو مکینیکل اصول (Digging)', 'توپ پورته کول او بایومیخانیکي اصول (Digging)')
    P(b, [('To lift the ball of the service, the fingers of both hands are joined to each other; the thumbs should be together and parallel. Lengthen the arms; as soon as the ball comes near, bending the body forward, lift the ball on the arms in such a way that the ball comes over the head of the booster.',
           'سروس کا بال اٹھانے کے لیے دونوں ہاتھوں کی انگلیاں آپس میں ملائی جاتی ہیں انگوٹھے اکٹھے اور متوازی ہوں۔ چاہئیں۔ بازوؤں کو لمبا کریں جونہی بال نزدیک آئے جسم کو آگے جھکاتے ہوئے بازوؤں پر بال کو اس طرح اٹھائیں کہ بال بوسٹر کے سر پر آ جائے۔',
           'د سرویس د توپ د پورته کولو لپاره د دواړو لاسونو ګوتې سره یوځای کېږي؛ ګوتې (غټې ګوتې) دې یوځای او موازي وي. مټې اوږدې کړئ؛ څنګه چې توپ نږدې شي، بدن مخکې کوږ کړئ او توپ پر مټو داسې پورته کړئ چې د بوسټر سر ته راشي.'),
          ('Remember, if the service has been done in the smash way, then the speed of the ball is very fast. According to the second law of motion, material bodies want to maintain their state of rest or motion. Therefore under the law of inertia, to reduce the resistance of the ball to change in motion, as soon as the ball strikes the hands they should be moved backwards …',
           'یاد رکھیں سروس اگر سمیش طریقے سے کی گئی ہو تو بال کی رفتار بہت تیز ہوتی ہے۔ حرکت کے دوسرے قانون کے مطابق مادی اجسام اپنی حالتِ سکون یا حرکت کو برقرار رکھنا چاہتے ہیں۔ لہٰذا جمود کے قانون کے تحت بال حرکت میں تبدیلی کی مزاحمت کو کم کرنے کے لیے جیسے ہی بال ہاتھوں سے ٹکرائے تو انھیں پیچھے کی جانب حرکت …',
           'یاد ولرئ که سرویس په سمیش طریقه شوی وي، د توپ سرعت ډېر چټک وي. د حرکت د دویم قانون له مخې مادي جسمونه غواړي د سکون یا حرکت حالت وساتي. نو د جمود د قانون له مخې د توپ په حرکت کې د بدلون د مقاومت د کمولو لپاره څنګه چې توپ له لاسونو ټکر وکړي، شا ته یې خوځول …')])
    r = rec(b, 6, 7, 64)
    deco(r, 'A line drawing of two volleyball players jumping at the net is decorative.')
    BOOK.save(64, [(6, r)], issues=[{'id': 'hpe12-pdf064', 'unit': 6, 'printedPage': 59,
               'description': 'The digging paragraph attributes the tendency to keep a state of rest or motion to “the second law of motion” and then calls it the law of inertia (the first law). Line ends at the left edge are cut and completed from context. “متوازی ہوں۔ چاہئیں۔”. Retained as printed.'}])


def p65():
    b = Builder()
    P(b, [('… should be given, and the hands and arms should be kept loose. If the hands or arms strike the ball with stiffness, then as a result of the action a reaction will arise in the opposite direction, and the ball will go back towards the opposite court, through which the team receiving the service will lose the chance of attack.',
           'جائے۔ اور ہاتھوں اور بازوؤں کو ڈھیلا رکھیں اگر ہاتھ یا بازو سختی سے بال سے ٹکرائیں گے تو عمل کے نتیجے میں مخالف سمت میں ردعمل پیدا ہوگا۔ اور بال واپس مخالف کورٹ کی طرف جائے گا جس سے سروس وصول کرنے والی ٹیم حملے کا موقع گنوا دے گی۔',
           '… ورکړل شي او لاسونه او مټې سستې وساتئ. که لاسونه یا مټې په سختۍ له توپ سره ټکر وکړي، د عمل په پایله کې مخالف لوري ته غبرګون پیدا کېږي او توپ بېرته مخالف میدان ته ځي چې له امله یې سرویس اخیستونکی ټیم د برید فرصت له لاسه ورکوي.')])
    b.h('Biomechanical principles in the action of Boosting', 'بوسٹنگ (Boosting) کے عمل میں بائیو مکینیکل اصول', 'د بوسټینګ (Boosting) په عمل کې بایومیخانیکي اصول')
    P(b, [('Boosting is the action of preparing the ball for the smash. In other words, tossing the ball near the net for the smash is called boosting. As soon as the ball comes over the head of the booster, the booster, making the shape of a cup with his fingers, lifts the ball up over the net. In this action too Newton’s laws apply.',
           'بوسٹنگ بال کو سمیش کے لیے تیار کرنے کا عمل ہے۔ دوسرے لفظوں میں نیٹ کے قریب بال کو سمیش کے لیے اچھالنا بوسٹنگ کہلاتا ہے۔ جوں ہی بال بوسٹر کے سر پر آتا ہے تو بوسٹر اپنی انگلیوں سے پیالے کی شکل بناتے ہوئے بال کو نیٹ سے اوپر اٹھاتا ہے۔ اس عمل میں بھی نیوٹن کے قوانین کا اطلاق ہوتا ہے۔',
           'بوسټینګ توپ د سمیش لپاره د چمتو کولو عمل دی. په بل عبارت، د جال تر څنګ د سمیش لپاره د توپ پورته کولو ته بوسټینګ ویل کېږي. څنګه چې توپ د بوسټر سر ته راشي، بوسټر په ګوتو د پیالې بڼه جوړوي او توپ له جال پورته پورته کوي. په دې عمل کې هم د نیوټن قوانین پلي کېږي.')])
    b.h('Smashing and biomechanical principles', 'سمیشنگ اور بائیو مکینیکل اصول', 'سمیش او بایومیخانیکي اصول')
    P(b, [('In the action of smashing, jumping and hitting the ball are included. To jump and hit the ball, the player, bringing his centre of gravity (Center of Gravity) down, initially spends force on the surface of the ground and jumps and smashes the ball, and according to the third law of motion, as much force as he spends on the ball, as a reaction the ball will go towards the other court. The player, while jumping and coming back to the ground, will also maintain his balance.',
           'سمیشنگ کے عمل میں اچھلنا اور بال کو مارنا شامل ہے۔ اچھلنے اور بال کو مارنے کے لیے کھلاڑی اپنے مرکزِ ثقل (Center of Gravity) کو نیچے لاتے ہوئے ابتدائی طور پر زمین کی سطح پر قوت صرف کر کے جمپ کرے گا اور بال کو سمیش کرتے ہوئے حرکت کے تیسرے قانون کے مطابق جتنی قوت بال پر صرف کرے گا ردِ عمل کے طور پر بال دوسرے کورٹ کی جانب جائے گا۔ کھلاڑی اچھلنے اور واپس زمین پر آتے وقت اپنے توازن کو بھی برقرار رکھے گا۔',
           'د سمیش په عمل کې ټوپ وهل او توپ وهل شامل دي. د ټوپ او توپ وهلو لپاره لوبغاړی خپل د جاذبې مرکز (Center of Gravity) ښکته کوي، په پیل کې پر ځمکه ځواک لګوي او ټوپ وهي او توپ سمیش کوي؛ د حرکت د درېیم قانون له مخې څومره ځواک چې پر توپ ولګوي، د غبرګون په توګه توپ بل میدان ته ځي. لوبغاړی د ټوپ او بېرته ځمکې ته د راتګ پر مهال خپل توازن هم ساتي.')])
    r = rec(b, 6, 8, 65)
    BOOK.save(65, [(6, r)], issues=[{'id': 'hpe12-pdf065', 'unit': 6, 'printedPage': 60,
               'description': 'A small owner ballpoint mark at the foot of the text is excluded. The smash paragraph says the ball goes to the other court “as a reaction” to the force spent on it. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    {60: p60, 61: p61, 62: p62, 63: p63, 64: p64, 65: p65}[n]()
