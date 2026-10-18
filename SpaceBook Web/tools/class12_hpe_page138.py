"""HPE XII PDF138–143: pp.134–139 — netball goal post, ring, court lines, ball, dress, time, number of players, positions, centre pass, off side,
ball out of court, throw in, throw up, penalty shoot, free shoot, shooting, two lines cross, goal making, rules, officials. Run: python class12_hpe_page138.py N (138–143)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco


def p138():
    b = Builder()
    b.h('Goal post', 'گول پوسٹ', 'د ګول ستنه')
    P(b, [('The goal post will be made of wood or metal and will be placed in the middle of the goal line. With it a ring made of an iron rod one centimetre thick will be fixed. The diameter of the ring will be 38.10 centimetres. The height of the ring above the ground will be 3.05 metres or 10 feet. The ring will be fixed to the goal post with a strip of 6 inches or 15.24 centimetres, parallel to the ground.', 'گول پوسٹ لکڑی یا دھات کا بنا ہوگا اور گول لائن کے وسط میں رکھا جائے گا۔ اس کے ساتھ ایک سینٹی میٹر موٹی سلاخ سے بنا ہوا ایک چھلا لگا ہوگا۔ چھلے کا قطر 38.10 سینٹی میٹر ہوگا رنگ کی زمین سے اونچائی 3.05 میٹر یا 10 فٹ ہوگی۔ رِنگ گول پوسٹ کے ساتھ 6 انچ یا 15.24 سینٹی میٹر کی پٹی کے ساتھ زمین کے ساتھ متوازی لگایا جائے گا۔', 'د ګول ستنه له لرګي یا فلز جوړه وي او د ګول کرښې په منځ کې ایښودل کېږي. ورسره د یو سانتي متر پنډې میلې یوه کړۍ لګېدلې وي. د کړۍ قطر ۳۸.۱۰ سانتي متره وي. د کړۍ لوړوالی له ځمکې ۳.۰۵ متره یا ۱۰ فټه وي. کړۍ د ګول له ستنې سره د ۶ انچو یا ۱۵.۲۴ سانتي متره پټۍ سره ځمکې ته موازي لګول کېږي.')])
    b.h('Ring', 'رنگ', 'کړۍ')
    P(b, [('In netball the diameter of the ring is 38 centimetres.', 'نیٹ بال میں رنگ کا قطر 38 سینٹی میٹر۔', 'په نېټبال کې د کړۍ قطر ۳۸ سانتي متره.')])
    b.h('Lines of the court', 'کورٹ کی لکیریں', 'د میدان کرښې')
    P(b, [('All lines of the court will be 25 centimetres thick, which are part of the court. All lines will be drawn with lime.', 'کورٹ کی تمام لکیریں 25 سینٹی میٹر موٹی ہوں گی جو کورٹ کا حصہ ہوتی ہے۔ تمام لکیریں چونے کے ساتھ کھینچی جائے گی۔', 'د میدان ټولې کرښې به ۲۵ سانتي متره پنډې وي چې د میدان برخه وي. ټولې کرښې به په چونې کښل کېږي.')])
    b.h('Ball', 'بال', 'توپ')
    b.group('lines', [('The ball will be made of leather and will be of number 5.', 'بال چمڑے کا بنا ہوگا جو 5 نمبر کا ہوگا۔', 'توپ به له څرمن جوړ او ۵ نمبر به وي.'), ('Weight of the ball 397 to 454 grams.', 'بال کا وزن 397 سے 454 گرام۔', 'د توپ وزن ۳۹۷ تر ۴۵۴ ګرامه.'), ('Circumference of the ball — 27 to 28 inches.', 'بال کا محیط۔ 27 سے 28 انچ۔', 'د توپ محیط — ۲۷ تر ۲۸ انچه.')])
    b.h('Dress', 'لباس', 'جامې')
    P(b, [('Canvas shoes, shalwar qameez; it will not be allowed to wear any such thing from which there is a danger of the opposing player being injured.', 'کینوس شوز، شلوار قمیض، کوئی ایسی چیز پہننے کی اجازت نہیں ہوگی جس سے مخالف کھلاڑی کے زخمی ہونے کا خطرہ ہو۔', 'کینوس بوټان، شلوار کمیس؛ د داسې شي اغوستلو اجازه به نه وي چې د مخالف لوبغاړي د ټپي کېدو خطر ولري.')])
    b.h('Time', 'وقت', 'وخت')
    P(b, [('Four halves of fifteen, fifteen minutes; between the first and second half 3 minutes, while between the third and fourth half there will be an interval of 5 minutes. Time wasted in an accident or in any way will be included in the same half.', 'پندرہ پندرہ منٹ کے چار ہاف ہونگے پہلے اور دوسرے ہاف کے درمیان 3 منٹ جبکہ تیسرے اور چوتھے ہاف میں 5 منٹ کا وقفہ ہوگا حادثہ یا کسی طور پر ضائع شدہ وقت اسی ہاف میں شامل کیا جائے گا۔', 'د پنځلس پنځلس دقیقو څلور نیمایي (برخې) وي؛ د لومړۍ او دویمې برخې ترمنځ ۳ دقیقې، او د درېیمې او څلورمې برخې ترمنځ ۵ دقیقې وقفه وي. په پېښه یا په هر ډول ضایع شوی وخت په همغه برخه کې شاملېږي.')])
    r = rec(b, 7, 55, 138)
    deco(r, 'A photograph of a Gilbert netball is decorative.')
    BOOK.save(138, [(7, r)], issues=[{'id': 'hpe12-pdf138', 'unit': 7, 'printedPage': 134,
               'description': 'Court lines are printed as “25 سینٹی میٹر موٹی” (probably 5 cm); the four quarters are called “ہاف”. Line starts cut at the right edge (“گول پوسٹ”, “موٹی”, “(10) فٹ”) are completed from context. Retained as printed.'}])


def p139():
    b = Builder()
    b.h('Number of players', 'کھلاڑیوں کی تعداد', 'د لوبغاړو شمېر')
    P(b, [('In a team there are 12 players. A team with fewer than 7 players cannot take part in the game. A player coming late can join the game with the permission of the umpire after a goal is scored, provided the umpire was told before the game started.', 'ایک ٹیم میں 12 کھلاڑی ہوتے ہیں 7 کھلاڑیوں سے کم ٹیم کھیل میں حصہ نہیں لے سکتی۔ دیر سے آنے والے کھلاڑی امپائر کی اجازت سے گول بننے کے بعد کھیل میں شریک ہو سکتا ہے بشرطیکہ امپائر کو کھیل شروع ہونے سے پہلے بتایا جائے۔', 'په یوه ټیم کې ۱۲ لوبغاړي وي. له ۷ لوبغاړو کم ټیم په لوبه کې برخه نه شي اخیستی. ناوخته راغلی لوبغاړی د امپایر په اجازه له ګول وروسته لوبې ته ورګډېدای شي، په دې شرط چې امپایر ته د لوبې له پیل مخکې ویل شوي وي.')])
    b.h('Positions of the players', 'کھلاڑیوں کی پوزیشن', 'د لوبغاړو ځایونه')
    H = (['Position', 'Areas'], ['پوزیشن', 'علاقے'], ['ځای', 'سیمې'])
    rows = [('Goal shooter', 'گول شوٹر', 'ګول وېشتونکی', '1, 2'), ('Goal attack', 'گول اٹیک', 'ګول برید', '1, 2, 3'), ('Wing attack', 'ونگ اٹیک', 'وینګ برید', '4, 3'), ('Centre', 'سینٹر', 'منځنی', '3, 2, 4'),
            ('Wing defence', 'ونگ ڈیفنس', 'وینګ دفاع', '4, 3'), ('Goal defence', 'گول ڈیفنس', 'ګول دفاع', '4, 3, 5'), ('Goal keeper', 'گول کیپر', 'ګول ساتونکی', '4, 5')]
    b.table('hpe12-netball-positions', H[0], [[e, a] for e, u, p, a in rows], H[1], H[2], [[u, a.replace(', ', '،')] for e, u, p, a in rows], [[p, a] for e, u, p, a in rows])
    b.h('Center Pass', 'سنٹر پاس (Center Pass)', 'منځنی پاس (Center Pass)')
    L(b, [('After the umpire’s whistle the centre pass will be made within 3 seconds.', 'امپائر کی وسل ہو جانے کے بعد 3 سیکنڈ کے اندر اندر سنٹر پاس ہوگا۔', 'د امپایر له شپېلۍ وروسته به په ۳ ثانیو کې منځنی پاس کېږي.'), ('The centre pass can be given in any way.', 'سنٹر پاس کسی بھی طریقے سے دیا جا سکتا ہے۔', 'منځنی پاس په هره طریقه ورکول کېدای شي.'),
          ('The first centre pass can be taken only in the centre third.', 'پہلا سنٹر پاس سنٹر تھرڈ میں ہی لیا جا سکتا ہے۔', 'لومړی منځنی پاس یوازې په منځنۍ درېیمه برخه کې اخیستل کېدای شي.'), ('At the time of the centre pass the positions of all players should be correct.', 'سنٹر پاس کے وقت تمام کھلاڑیوں کی پوزیشن صحیح ہونی چاہیے۔', 'د منځني پاس پر وخت دې د ټولو لوبغاړو ځایونه سم وي.'),
          ('The centre pass can be given to any player among wing attack, wing defence, goal attack and goal defence.', 'ونگ اٹیک، ونگ ڈیفنس، گول اٹیک اور گول ڈیفنس میں سے کسی کھلاڑی کو سنٹر پاس دے سکتا ہے۔', 'منځنی پاس وینګ برید، وینګ دفاع، ګول برید او ګول دفاع له هر لوبغاړي ته ورکول کېدای شي.'),
          ('If the centre pass touches any player and reaches the goal attack or the goal shooter, then the shooter can make a goal.', 'سنٹر پاس کسی بھی کھلاڑی کو چھو جائے اور گول اٹیک یا گول شوٹر کے پاس چلی جائے تو شوٹر گول بنا سکتا ہے۔', 'که منځنی پاس کوم لوبغاړی ولمسوي او ګول برید یا ګول وېشتونکي ته ورسېږي، وېشتونکی ګول جوړولی شي.')])
    r = rec(b, 7, 56, 139)
    r['sourceNote'] = 'The positions list (position and area numbers) is given as a structured table.'
    BOOK.save(139, [(7, r)])


def p140():
    b = Builder()
    L(b, [('Both feet of the player taking the centre pass should be in the circle. At the time of the pass one foot can be kept outside.', 'سنٹر والے کھلاڑی کے دونوں پاؤں سرکل میں ہونے چاہئیں۔ پاس کے وقت ایک پاؤں باہر رکھ سکتا ہے۔', 'د منځني لوبغاړي دواړه پښې دې په دایره کې وي. د پاس پر وخت یوه پښه بهر ایښودلی شي.'),
          ('The opposing centre can stand anywhere in the centre third at a distance of 3 metres.', 'مخالف سنٹر 3 میٹر کے فاصلے پر سنٹر تھرڈ میں کسی بھی جگہ کھڑا ہو سکتا ہے۔', 'مخالف منځنی لوبغاړی په ۳ متره واټن د منځنۍ درېیمې برخې په هر ځای کې ودرېدای شي.'),
          ('Immediately after the centre pass every player can start throwing the ball within his own fixed limits.', 'سنٹر پاس کے فوراً بعد ہر کھلاڑی اپنی مقررہ حدود کے اندر بال پھینکنا شروع کر سکتا ہے۔', 'له منځني پاس سمدستي وروسته هر لوبغاړی د خپلو ټاکلو حدودو دننه توپ اچول پیلولی شي.'),
          ('After the interval the same player will take the centre pass who took the centre pass before the game stopped, provided there was no goal.', 'وقفے کے بعد وہی کھلاڑی سنٹر پاس لے گا جس نے کھیل بند ہونے سے پہلے سنٹر پاس لیا ہو بشرطیکہ گول نہ ہوا ہو۔', 'له وقفې وروسته همغه لوبغاړی منځنی پاس اخلي چې د لوبې له درېدو مخکې یې منځنی پاس اخیستی و، په دې شرط چې ګول نه وي شوی.')])
    b.h('Off side', 'آف سائیڈ (Off side)', 'اف سایډ (Off side)')
    L(b, [('When some player, with or without the ball, goes into some area other than his own area, he will be off side.', 'جب کوئی کھلاڑی گیند یا گیند کے بغیر اپنے علاقے کے علاوہ کسی دوسرے علاقہ میں چلا جائے تو وہ آف سائیڈ ہوگا۔', 'کله چې کوم لوبغاړی له توپ سره یا بې توپه له خپلې سیمې پرته بلې سیمې ته لاړ شي، اف سایډ دی.'),
          ('When some part of the body of a player touches another area other than his own area, then too he will be off side.', 'جب کسی کھلاڑی کے جسم کا کوئی حصہ اپنے علاقے کے علاوہ دوسرے علاقے کو چھو جائے تو وہ بھی آف سائیڈ ہوگا۔', 'کله چې د لوبغاړي د بدن کومه برخه له خپلې سیمې پرته بله سیمه ولمسوي، بیا هم اف سایډ دی.'),
          ('A player, remaining in his own area, can take the ball from another area by stretching the hand. This will not be off side, but the condition is that while doing so he does not touch the other area.', 'کھلاڑی اپنے علاقے میں رہ کر لمبے ہاتھ سے گیند دوسرے علاقے سے لے سکتا ہے۔ یہ آف سائیڈ نہ ہوگا مگر شرط یہ ہے کہ ایسا کرتے وقت وہ دوسرے کے علاقہ کو نہ چھوئے۔', 'لوبغاړی په خپله سیمه کې پاتې کېږي او په اوږد لاس له بلې سیمې توپ اخیستلی شي. دا اف سایډ نه دی، خو شرط دا دی چې د دې کار پر وخت بله سیمه ونه لمسوي.')])
    b.h('Penalty', 'سزا (Penalty)', 'سزا (Penalty)')
    P(b, [('A free pass will be given to the opposing team from the place of the off side. The free pass will be taken by that player who is authorised to go into that area.', 'آف سائیڈ والی جگہ سے مخالف ٹیم کو فری پاس دیا جائے گا۔ فری پاس وہ کھلاڑی لے گا جو اس علاقے میں جانے کا مجاز ہوگا۔', 'د اف سایډ له ځایه مخالف ټیم ته وړیا پاس ورکول کېږي. وړیا پاس به هغه لوبغاړی اخلي چې هغې سیمې ته د تګ واک لري.')])
    b.h('Ball out of court', 'گیند کا کورٹ سے باہر جانا (Ball out of court)', 'له میدان د توپ وتل (Ball out of court)')
    L(b, [('The ball touches the ground outside the court.', 'گیند کورٹ سے باہر زمین کو چھوئے۔', 'توپ له میدان بهر ځمکه ولمسوي.'), ('The ball touches some person or thing outside the court.', 'گیند کورٹ سے باہر کسی شخص یا چیز کو لگے۔', 'توپ له میدان بهر کوم کس یا شي ته ولګېږي.'),
          ('When the ball is in the player’s hand and he touches the ground outside.', 'جب گیند کھلاڑی کے ہاتھ میں ہو اور وہ باہر زمین کو چھولے۔', 'کله چې توپ د لوبغاړي په لاس کې وي او بهر ځمکه ولمسوي.')])
    b.h('Throw in', 'تھرو ان (Throw in)', 'تھرو ان (Throw in)')
    P(b, [('When the ball goes out of the court, then to bring it into the game again a throw-in will be given to the opposing team.', 'جب بال کورٹ سے باہر چلی جائے تو اُسے دوبارہ کھیل میں لانے کیلئے مخالف ٹیم کو تھرو ان دی جائے گی۔', 'کله چې توپ له میدان ووځي، بیا لوبې ته د راوستلو لپاره مخالف ټیم ته تھرو ان ورکول کېږي.')])
    r = rec(b, 7, 57, 140)
    BOOK.save(140, [(7, r)], issues=[{'id': 'hpe12-pdf140', 'unit': 7, 'printedPage': 136,
               'description': 'The right edge of the scan cuts the first letters of headings and bullets (“سنٹر”, “آف سائیڈ”, “گیند”, “تھرو”), completed from context.'}])


def p141():
    b = Builder()
    L(b, [('The ball will be given to the opponent of the team that last touched the ball.', 'جس ٹیم نے آخری بار بال کو چھوا ہو اس کے مخالف کو تھرو ان دی جائے گی۔', 'هغه ټیم چې وروستی ځل یې توپ لمسولی، مخالف ته یې تھرو ان ورکول کېږي.'), ('The throw-in will be given from the same place where the ball crossed the line.', 'جس لائن کو بال کراس کرے اسی جگہ سے تھرو ان دی جائے گی۔', 'له همغه ځایه چې توپ کرښه اوښتې، تھرو ان ورکول کېږي.'),
          ('The ball will have to be thrown in to the centre within 3 seconds.', '3 سیکنڈ کے اندر بال کو سینٹر میں تھرو ان کرنا ہوگا۔', 'په ۳ ثانیو کې باید توپ منځ ته تھرو ان شي.'), ('A player cannot throw in by running.', 'کھلاڑی بھاگ کر تھرو ان نہیں کر سکتا۔', 'لوبغاړی په منډه تھرو ان نه شي کولی.'),
          ('Players should throw the ball keeping a distance of 3 metres while making the throw-in.', 'کھلاڑی تھرو ان کرتے وقت 3 میٹر کا فاصلہ رکھ کر بال کو پھینکیں۔', 'لوبغاړي دې د تھرو ان پر وخت ۳ متره واټن وساتي او توپ وغورځوي.'), ('Touching or crossing the line while making the throw-in is a foul.', 'تھرو ان کرتے وقت لائن کو چھونا یا کراس کرنا فاؤل ہے۔', 'د تھرو ان پر وخت کرښه لمسول یا اوښتل خطا ده.'),
          ('A player making a throw-in of the ball without the whistle is a foul.', 'کھلاڑی کا بال کو بغیر وسل کے تھرو ان کرنا فاؤل ہے۔', 'له شپېلۍ پرته د لوبغاړي له خوا تھرو ان خطا ده.'), ('Until the ball leaves the hands the player will not enter the court.', 'جب تک بال ہاتھوں سے نکل نہ جائے کھلاڑی کورٹ میں داخل نہیں ہوگا۔', 'تر هغه چې توپ له لاسونو ونه وځي، لوبغاړی به میدان ته نه ننوځي.'),
          ('The player will have to throw in from the line of his own particular area.', 'کھلاڑی کو اپنے مخصوص علاقے کی لائن سے تھرو ان کرنا ہوگا۔', 'لوبغاړی باید د خپلې ځانګړې سیمې له کرښې تھرو ان وکړي.'), ('Before the throw-in the player should pause slightly.', 'تھرو ان کرنے سے پہلے کھلاڑی کو قدرے رُکنا چاہیے۔', 'له تھرو ان مخکې دې لوبغاړی لږ ودرېږي.')])
    b.h('Penalty', 'سزا (Penalty)', 'سزا (Penalty)')
    P(b, [('In case of violation a throw-in will be given to the opposing team.', 'خلاف ورزی کی صورت میں مخالف ٹیم کو تھرو ان دی جائے گی۔', 'د سرغړونې په صورت کې مخالف ټیم ته تھرو ان ورکول کېږي.')])
    b.h('Throw up', 'تھرو اپ (Throw up)', 'تھرو اپ (Throw up)')
    P(b, [('In the following cases play will be restarted with a “throw up”.', 'مندرجہ ذیل صورتوں میں کھیل کا اجراء ”تھرو اپ“ سے کیا جائے گا۔', 'په لاندې حالتونو کې به لوبه په "تھرو اپ" بیا پیلېږي.')])
    L(b, [('When two players are victims of some irregularity at the same time.', 'جب دو کھلاڑی بیک وقت کسی بے ضابطگی کا شکار ہوں۔', 'کله چې دوه لوبغاړي په یو وخت د کومې بې‌قاعدګۍ ښکار شي.'), ('The throw-up is given at that time when two opposing players hold the ball firmly at the same time.', 'تھرو اپ اس وقت دیا جاتا ہے جب دو مخالف کھلاڑی بیک وقت گیند کو مضبوطی سے پکڑ لے۔', 'تھرو اپ هغه وخت ورکول کېږي چې دوه مخالف لوبغاړي په یو وخت توپ کلک ونیسي.'),
          ('Two opposing players at the same time hit the ball with their hands and throw it outside the court.', 'بیک وقت دو مخالف کھلاڑی بال کو ہاتھوں سے مار کر کورٹ کے باہر پھینک دیں۔', 'دوه مخالف لوبغاړي په یو وخت توپ په لاسونو ووهي او له میدان بهر یې وغورځوي.'), ('The umpire cannot decide on some double error.', 'امپائر کسی ڈبل غلطی پر فیصلہ نہ کر پائیں۔', 'امپایر په کومه دوه‌ګونې تېروتنه پرېکړه ونه شي کولی.'),
          ('Two opposing players collide at one place and at one and the same time.', 'دو مخالف کھلاڑی ایک ہی جگہ اور ایک ہی وقت میں ٹکرا جائے۔', 'دوه مخالف لوبغاړي په یوه ځای او یوه وخت ټکر وکړي.')])
    r = rec(b, 7, 58, 141)
    BOOK.save(141, [(7, r)])


def p142():
    b = Builder()
    b.h('Penalty Shoot', 'پنلٹی شوٹ (Penalty Shoot)', 'پنالټي ویشتل (Penalty Shoot)')
    P(b, [('On committing an error deliberately, a penalty shoot will be given to the opposing team from the same place. At the time of the penalty shoot the player will stand 3 metres away.', 'جان بوجھ کر غلطی کرنے پر اسی جگہ سے مخالف ٹیم کو پنلٹی شوٹ دی جائے گی پنلٹی شوٹ کے وقت کھلاڑی 3 میٹر دور کھڑا ہوگا۔', 'په قصد د تېروتنې په کولو له همغه ځایه مخالف ټیم ته پنالټي ویشتل ورکول کېږي. د پنالټي پر وخت لوبغاړی ۳ متره لرې ولاړ وي.')])
    b.h('Free Shoot', 'فری شوٹ (Free Shoot)', 'وړیا ویشتل (Free Shoot)')
    P(b, [('On deliberately committing a foul inside the shooting circle, a free shoot will be given to the opposing team.', 'شوٹنگ سرکل کے اندر جان بوجھ کر فاؤل کرنے پر مخالف ٹیم کو فری شوٹ دی جائے گی۔', 'د ویشتو دایرې دننه په قصد د خطا کولو په صورت کې مخالف ټیم ته وړیا ویشتل ورکول کېږي.')])
    b.h('Shooting', 'شوٹنگ (Shooting)', 'ویشتل (Shooting)')
    P(b, [('Walking with the ball after receiving the ball is a foul, whereas the player, making one foot the pivot, can move the other foot forward and backward.', 'بال وصول کرنے کے بعد بال کے ساتھ چلنا فاؤل ہے۔ جبکہ کھلاڑی ایک پاؤں کو مرکز بنا کر دوسرا پاؤں آگے پیچھے کر سکتا ہے۔', 'له توپ اخیستو وروسته له توپ سره تګ خطا ده، په داسې حال کې چې لوبغاړی یوه پښه محور ګرځوي او بله پښه مخکې شا ته کولی شي.')])
    b.h('Penalty', 'سزا (Penalty)', 'سزا (Penalty)')
    P(b, [('In the case of this foul the ball will be given to the opposing player at the same place.', 'اس فاؤل کی صورت میں اسی جگہ مخالف کھلاڑی کو بال دیا جائے گا۔', 'د دې خطا په صورت کې په همغه ځای مخالف لوبغاړي ته توپ ورکول کېږي.')])
    b.h('Two Lines Cross', 'دو لائنیں عبور کرنا (Two Lines Cross)', 'دوه کرښې اوښتل (Two Lines Cross)')
    P(b, [('No player can throw the ball directly across two lines. If the ball in between touches some player or passes touching the ground, it will not be a foul.', 'کوئی کھلاڑی بال کو براہ راست دو لائن کراس کر کے نہیں پھینک سکتا۔ اگر بال درمیان میں کسی کھلاڑی کو ٹچ کر لے یا زمین کو چھو کر گزر جائے تو فاؤل نہیں ہوگا۔', 'هېڅ لوبغاړی توپ په مستقیم ډول له دوو کرښو اوښتو سره نه شي غورځولی. که توپ په منځ کې کوم لوبغاړی ولمسوي یا ځمکه ولمسوي او تېر شي، خطا نه ده.')])
    b.h('Penalty', 'سزا (Penalty)', 'سزا (Penalty)')
    P(b, [('In the case of this foul, the ball will be given to the opposing team from where the foul was committed.', 'اس فاؤل کی صورت میں جہاں سے فاؤل سرزد ہوا ہو۔ وہاں سے مخالف ٹیم کو بال دیا جائے گا۔', 'د دې خطا په صورت کې له هغه ځایه چې خطا شوې، مخالف ټیم ته توپ ورکول کېږي.')])
    b.h('Making a goal', 'گول بنانا', 'ګول جوړول')
    P(b, [('When some player passes the ball from above through the ring and no foul has been committed, it will be counted a goal. It is compulsory for the player to be inside the shooting circle. The shooter can make a goal by catching the ball again and again, provided no foul has been committed. Within 3 seconds goal …', 'جب کوئی کھلاڑی بال کو اوپر سے رِنگ میں گزارے اور کوئی فاؤل نہ ہوا ہو تو گول شمار ہوگا۔ کھلاڑی کا شوٹنگ سرکل کے اندر ہونا لازمی ہے۔ شوٹر بال کو بار بار پکڑ کر گول بنا سکتا ہے بشرطیکہ فاؤل نہ ہوا ہو۔ 3 سیکنڈ کے اندر گول …', 'کله چې کوم لوبغاړی توپ له پاسه کړۍ ته تېر کړي او کومه خطا نه وي شوې، ګول ګڼل کېږي. د لوبغاړي د ویشتو دایرې دننه کېدل اړین دي. وېشتونکی توپ بیا بیا نیولی او ګول جوړولی شي، په دې شرط چې خطا نه وي شوې. په ۳ ثانیو کې ګول …')])
    r = rec(b, 7, 59, 142)
    deco(r, 'A two-frame photograph of a player shooting and a ball dropping into the ring is decorative.')
    BOOK.save(142, [(7, r)])


def p143():
    b = Builder()
    P(b, [('… making is necessary. The player cannot make a goal by taking the support of the pole.', 'کرنا ضروری ہے۔ کھلاڑی پول کا سہارا لے کر گول نہیں کر سکتا۔', '… جوړول اړین دي. لوبغاړی د ستنې په ملاتړ ګول نه شي جوړولی.')])
    b.h('Rules of netball', 'نیٹ بال کے قوانین', 'د نېټبال قوانین')
    L(b, [('The pass will have to be made within three seconds.', 'تین سیکنڈ کے اندر اندر پاس کرنا ہوگا۔', 'په درېیو ثانیو کې باید پاس وشي.'), ('A player cannot throw the ball himself and play it again.', 'کھلاڑی خود بال پھینک کر دوبارہ اسے نہیں کھیل سکتا۔', 'لوبغاړی پخپله توپ نه شي غورځولی او بیا یې لوبولی.'),
          ('(One) should not be on the two parallel lines.', 'متوازی دو لائنوں کے اوپر نہ ہوں۔', 'پر دوو موازي کرښو دې نه وي.'), ('The player cannot bounce the ball forward.', 'بال کو کھلاڑی بڑھا نہیں سکتا۔', 'لوبغاړی توپ مخکې نه شي وړلی.'),
          ('He cannot deliberately kick the ball.', 'بال کو دانستہ طور پر ٹھوکر نہیں مار سکتا۔', 'په قصد توپ ته لغته نه شي وهلی.'), ('The player cannot take steps while throwing or catching the ball.', 'کھلاڑی بال کو پھینکتے یا پکڑتے وقت قدم نہیں لے سکتا۔', 'لوبغاړی د توپ غورځولو یا نیولو پر مهال قدم نه شي اخیستی.'),
          ('He will play keeping three feet away from the opposing player.', 'مخالف کھلاڑی سے تین فٹ دور رہ کر کھیلے گا۔', 'له مخالف لوبغاړي درې فټه لرې به لوبه کوي.'), ('It is necessary to play the ball in every third.', 'بال ہر تھرڈ میں کھیلنا ضروری ہے۔', 'په هره درېیمه برخه کې د توپ لوبول اړین دي.'),
          ('From the part of the court from which the ball goes out, the throw-in too will be from the same place.', 'بال کورٹ کے جس حصہ سے آؤٹ ہوگا اسی جگہ سے ان بھی ہوگا۔', 'توپ د میدان له کومې برخې ووځي، تھرو ان به هم له همغه ځایه وي.'), ('The player can neither shake the goal post nor make a goal taking its support.', 'کھلاڑی گول پوسٹ کو نہ ہلا سکتا ہے اور نہ ہی سہارا لے کر گول بنا سکتا ہے۔', 'لوبغاړی نه د ګول ستنه خوځولی شي او نه یې په ملاتړ ګول جوړولی شي.')])
    b.h('Game officials', 'کھیل کے عہدیداران (Game officials)', 'د لوبې چارواکي (Game officials)')
    b.h('Umpire', 'امپائر (Umpire)', 'امپایر (Umpire)')
    P(b, [('Two umpires will control the game. Their decision will be final, against which there will be no appeal. The umpire will have a special uniform.', 'دونوں امپائر گیم کو کنٹرول کریں گے۔ ان کا فیصلہ حتمی ہوگا جس کے خلاف کوئی اپیل نہیں ہوگی۔ امپائر کا مخصوص یونیفارم ہوگا۔', 'دواړه امپایران به لوبه کنټرولوي. پرېکړه یې وروستۍ وي او پر وړاندې یې استیناف نه وي. امپایر به ځانګړی یونیفورم ولري.')])
    b.h('Scorer', 'سکورر (Scorer)', 'نمره لیکونکی (Scorer)')
    P(b, [('For every game two scorers are appointed who keep the record of the score of the game. They keep in mind the centre pass.', 'ہر گیم کیلئے دو سکورر مقرر کیے جاتے ہیں جو گیم کے سکور کا ریکارڈ رکھتے ہیں۔ سنٹر پاس کا خیال رکھتے ہیں۔', 'د هرې لوبې لپاره دوه نمره لیکونکي ټاکل کېږي چې د لوبې د نمرو ریکارډ ساتي او منځني پاس ته پام کوي.')])
    r = rec(b, 7, 60, 143)
    BOOK.save(143, [(7, r)], issues=[{'id': 'hpe12-pdf143', 'unit': 7, 'printedPage': 139,
               'description': 'Rule “متوازی دو لائنوں کے اوپر نہ ہوں” has no subject in print; “بال کو کھلاڑی بڑھا نہیں سکتا” (probably bounce); “اسی جگہ سے ان بھی ہوگا”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 138
    {138: p138, 139: p139, 140: p140, 141: p141, 142: p142, 143: p143}[n]()
