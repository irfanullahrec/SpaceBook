"""Urdu XII PDF63 (spread): printed pp.116–117 — Lesson 12 summary end (source تارِ عنکبوت) and مشق Q1–Q6. Completes Lesson 12."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
for x in [
    ('“…This Pakistan of ours is just a big bus, and whatever any of us does, we are all its conductors; we just have to see that the vehicle keeps moving.” The narrator says he has said a great thing — even then he alone represented their circle, while the rest of them were “being ruined”. They laughed long over old memories.',
     '’’…یہ ہمارا پاکستان ایک بڑی سی بس ہی تو ہے؛ ہم سب جو کچھ بھی کریں، اس کے کنڈکٹر ہی تو ہیں۔ بس یہی خیال رکھنا ہے کہ گاڑی چلتی رہے۔‘‘ راوی کہتی ہے کہ تم نے بڑی زبردست بات کہہ دی — اُس وقت بھی ہمارے حلقے کی تم ہی نمائندگی کر رہے تھے، ہم سب تو خراب ہو رہے تھے۔ بڑی دیر تک وہ قہقہے لگا لگا کر ماضی کی باتیں کرتے رہے۔',
     '"…دا زموږ پاکستان یو لوی بس دی؛ موږ ټول هر څه چې کوو، د هغه کنډکټران یو. یوازې باید دا پام وساتو چې ګاډی روان وي." راوي وايي چې ډېره زبردسته خبره دې وکړه — هغه وخت هم زموږ د حلقې استازیتوب یوازې تا کاوه، موږ ټول خو "خرابېدو". ډېر وخت یې د تېر وخت خبرې په قهقهو وکړې.'),
    ('She seldom goes to Karachi; for years only news comes — that Lalu first joined a night school, then college, married a teacher, and now has built a house. She thinks his house was built long ago, on 14 August 1947, when he stood on a height, the singing waterfall coming down and the surging ocean reaching his small, history-making feet. And now all of them travel in a big bus at every door of which stands a conductor in his likeness. How much peace and attraction there is amid the sounds of the ocean, the waterfall and the moving bus!',
     'کراچی جانا کم ہی ہوتا ہے؛ کئی کئی سال بس خبریں ملتی ہیں — لالو نے پہلے نائٹ سکول، پھر کالج جوائن کیا، ایک ٹیچر سے بیاہ رچایا، اور اب گھر بنا لیا ہے۔ راوی سوچتی ہے کہ اس کا گھر تو کب کا بن گیا تھا — چودہ اگست ۱۹۴۷ء کو، جب وہ ایک بلندی پر کھڑا تھا، گاتی گنگناتی آبشار نیچے آئی تھی اور موّاج سمندر اس کے چھوٹے چھوٹے تاریخ ساز قدموں تک پہنچا تھا۔ اور اب ہم سب ایک بڑی سی بس میں سفر کر رہے ہیں جس کے ہر دروازے پر اس کا ہم شکل کنڈکٹر مستعدی سے کھڑا ہے۔ سمندر، آبشار اور چلتی بس کی آوازوں کے درمیان کتنا سکون ہے اور کتنی کشش!',
     'کراچۍ ته لږ تګ کېږي؛ کلونه کلونه یوازې خبرونه رسېږي — لالو لومړی شپني ښوونځي، بیا کالج ته شامل شو، له یوې ښوونکې سره یې واده وکړ، او اوس یې کور جوړ کړی. راوي فکر کوي چې د هغه کور خو ډېر پخوا جوړ شوی و — د ۱۹۴۷ز د اګسټ په ۱۴مه، کله چې هغه په یوه لوړه ولاړ و، سندرغاړی ابشار راښکته شوی و او څپانده سمندر د هغه کوچنیو، تاریخ‌جوړونکو پښو ته رسېدلی و. او اوس موږ ټول په یوه لوی بس کې سفر کوو چې په هره دروازه کې یې د هغه په څېر کنډکټر په چمتووالي ولاړ دی. د سمندر، ابشار او روان بس د غږونو ترمنځ څومره سکون او څومره کشش دی!'),
    ('(Tar-e-Ankaboot)', '(تارِ عنکبوت)', '(تار عنکبوت)'),
]: s.p(*x)
tx = BOOK.record(s, 'urdu12-u12-text-6', 'Lesson text — summary (6)', 'متنِ سبق — خلاصہ (۶)', 'د لوست متن — لنډیز (۶)', 63, [116])
tx['sourceGap'] = 'Altaf Fatima (d. 2018) — in copyright; paragraph-wise summary in the app, not verbatim. Printed p. 116.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions:', '۱۔ مندرجہ ذیل سوالات کے جوابات لکھیں:', '۱. لاندې پوښتنو ته ځوابونه ولیکئ:')
e.group('lines', [
    ('(a) What did the master say about Lalu?', '(الف) لالو کے بارے میں ماسٹر صاحب کیا کہتے تھے؟', '(الف) ماسټر صاحب د لالو په اړه څه ویل؟'),
    ('(b) Where did Lalu go when he disappeared from home?', '(ب) لالو گھر سے غائب ہو کر کہاں جاتا تھا؟', '(ب) لالو به له کوره ورک شو او چېرته به ته؟'),
    ('(c) From where did the master catch Lalu and his brother and bring them back?', '(ج) ماسٹر صاحب لالو اور اُس کے بھائی کو کہاں سے پکڑ کر لائے تھے؟', '(ج) ماسټر صاحب لالو او ورور یې له کومه ځایه نیولي راوستل؟'),
    ('(d) How did Lalu spend his life after the creation of Pakistan?', '(د) قیامِ پاکستان کے بعد لالو نے اپنی زندگی کیسے گزاری؟', '(د) د پاکستان له جوړېدو وروسته لالو خپل ژوند څنګه تېر کړ؟'),
    ("(e) What views did Lalu's father express about Lalu's activities?", '(ہ) لالو کی سرگرمیوں پر لالو کے والد نے کن خیالات کا اظہار کیا؟', '(ه) د لالو پلار د لالو د فعالیتونو په اړه کوم نظرونه څرګند کړل؟'),
    ('(f) Who was Lord Mountbatten?', '(و) لارڈ ماؤنٹ بیٹن کون تھے؟', '(و) لارډ ماونټ‌بیټن څوک و؟'),
])
e.p('2. Fill in the blanks:', '۲۔ خالی جگہ پُر کریں:', '۲. تش ځایونه ډک کړئ:')
e.group('lines', [
    ('(a) Now he has established ________ in Karachi.', '(الف) اب تو اُس نے کراچی میں ........ جما لیا', '(الف) اوس یې په کراچۍ کې ________ جوړ کړی.'),
    ("(b) The deep stamp of ________ was evident on Lalu's features.", '(ب) لالو کے خدوخال پر ........ کی گہری چھاپ نمایاں تھی۔', '(ب) د لالو پر څېره د ________ ژوره نښه ښکاره وه.'),
    ('(c) We mocked Lalu to show our ________ .', '(ج) ہم لوگ اپنی ........ جتانے کے لیے لالو کا مذاق اُڑاتے۔', '(ج) موږ د خپلې ________ ښودلو لپاره پر لالو ټوکې کولې.'),
    ('(d) There was a strange ________ in these slogans and processions.', '(د) اِن نعروں اور جلوسوں میں عجیب سی ........ تھی۔', '(د) په دې نارو او جلوسونو کې یو عجیب ________ و.'),
    ("(e) Now he would go madly to the ________ office.", '(ہ) اب وہ دیوانہ وار ........ کے دفتر جاتا', '(ه) اوس به په لېونتوب د ________ دفتر ته ته.'),
])
e.p('3. Explain the following sentences:', '۳۔ درج ذیل جملوں کی وضاحت کریں:', '۳. لاندې جملې تشریح کړئ:')
e.group('lines', [
    ('(1) Now we were seeking the causes of our defeat on the fields of Plassey and Seringapatam.', '(۱) اب ہم پلاسی اور سرنگاپٹم کے میدانوں میں اپنی شکست کے اسباب ڈھونڈ رہے تھے۔', '(۱) اوس موږ د پلاسي او سرنګاپټم په ډګرونو کې د خپلې ماتې لاملونه لټول.'),
    ('(2) Whom can we stop now? This is the voice of the times, the voice of the people.', '(۲) اب ہم کس کس کو روکیں گے؟ یہ تو وقت کی آواز ہے، زبانِ خلق ہے۔', '(۲) اوس به څوک څوک منع کړو؟ دا د وخت غږ دی، د خلکو ژبه ده.'),
    ('(3) Who knew that he was waiting.', '(۳) کسے خبر تھی کہ وہ انتظار کر رہا ہے۔', '(۳) چا خبر و چې هغه انتظار کوي.'),
])
e.p('4. Lalu would leave his studies and exams and join rallies and processions. Was it right for him to put his future at stake and go to rallies and processions like this?', '۴۔ لالو اپنی تعلیم اور امتحانوں کو چھوڑ کر جلسے جلوسوں میں شریک ہوتا۔ کیا اپنے مستقبل کو داؤ پر لگا کر اُس کا یوں جلسے جلوسوں میں جانا درست تھا؟', '۴. لالو به خپلې زده کړې او ازموینې پرېښودې او غونډو او جلوسونو ته به ورګډېده. ایا د خپل راتلونکي په لوبه کې اچولو سره د هغه داسې غونډو او جلوسونو ته تلل سم وو؟')
e.p('5. Write two examples each of all kinds of inferential (istidrākī) and causal (sababī) sentences. *', '۵۔ استدراکی اور سببی جملوں کی تمام اقسام کی دو دو مثالیں لکھیں۔ *', '۵. د استدراکي او سببي جملو د ټولو ډولونو دوه دوه بېلګې ولیکئ. *')
e.p('6. Identify the auxiliary verbs in the following sentences:', '۶۔ درج ذیل جملوں میں معاون افعال کی نشان دہی کریں:', '۶. په لاندې جملو کې مرستندوي فعلونه وپېژنئ:')
e.group('lines', [
    ('a. Abrar lost his dignity in society.', 'ا۔ ابرار معاشرے میں اپنا وقار کھو بیٹھا۔', 'ا. ابرار په ټولنه کې خپل وقار له لاسه ورکړ.'),
    ('b. In the crowd I began to suffocate.', 'ب۔ ہجوم میں تو میرا دم گھٹنے لگا تھا۔', 'ب. په ګڼه ګوڼه کې مې ساه بندېده.'),
    ('c. I wish you could win the match.', 'ج۔ کاش تم میچ جیت سکو۔', 'ج. کاشکې ته لوبه وګټلی شې.'),
    ('d. All the students spoke up with one voice.', 'د۔ تمام طلبہ یک زبان بول اُٹھے۔', 'د. ټولو زده کوونکو په یوه خوله وویل.'),
    ('e. The station officer flared up at the accused.', 'ہ۔ تھانیدار ملزم پر برس پڑا۔', 'ه. د تانې مشر پر تورن ورپرېوت (په غوسه شو).'),
])
ex = BOOK.record(e, 'urdu12-u12-exercise', 'Exercise', 'مشق', 'تمرین', 63, [116, 117])
issues = [{'id': 'urdu12-pdf063', 'unit': 12, 'printedPage': 117, 'description': 'Q5 carries an asterisk (*) as printed, with no matching note on these pages; istidrākī and sababī sentences are not explained in the book up to this point. Handwritten answers (Q1(d), Q1(f), Q2 blanks) and page references are owner notes, excluded.'}]

if __name__ == '__main__':
    BOOK.save(63, [(12, tx), (12, ex)], issues=issues, complete_units=[12])
