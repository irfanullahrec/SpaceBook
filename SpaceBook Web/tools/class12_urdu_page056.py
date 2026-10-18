"""Urdu XII PDF56 (spread): printed pp.102–103 — Lesson 11 'محسنِ محلّہ' summary end and مشق Q1."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
for x in [
    ('The master spent a night somehow under the transformer and next day went to the mansion of Shaikh Karim Nawaz to ask for a loan of two hundred rupees; the Shaikh, thinking him a good-hearted, simple, harmless soul, put him off, since it is unwise to lend much to such fools. Ismail the cloth-merchant refused even a hundred and fifty. Barber, confectioner, butcher, doctor, hakim, lawyer — he left none untried, but all refused, pleading severe inflation.',
     'ماسٹر صاحب نے ایک رات جوں توں کر کے ٹرانسفارمر کے نیچے گزاری اور اگلے دن شیخ کریم نواز کی حویلی جا کر دو سو روپے ادھار مانگے؛ شیخ صاحب نے انھیں نیک دل، سادہ لوح اور مرنجان مرنج سمجھ کر ٹرخا دیا کیونکہ ایسے احمقوں کو زیادہ رقم دینا اچھا نہیں ہوتا۔ اسماعیل بزاز نے ڈیڑھ سو پر بھی معذرت کر لی۔ محلے کا کوئی نائی، حلوائی، قصائی، ڈاکٹر، وید، وکیل انھوں نے نہ چھوڑا، مگر ہر طرف سے شدید مہنگائی کا بہانہ کر کے انکار ملا۔',
     'ماسټر صاحب یوه شپه څنګه نا څنګه د ټرانسفارمر لاندې تېره کړه او بله ورځ د شیخ کریم نواز حویلۍ ته لاړ او دوه سوه روپۍ پور یې وغوښت؛ شیخ صاحب هغه نېک‌زړی، ساده او بې‌ازاره وګاڼه او ټال یې کړ، ځکه چې داسې احمقانو ته ډېرې پیسې ورکول ښه نه دي. اسماعیل بزاز حتی یو سل او پنځوس ته هم بښنه وغوښته. د محلې هیڅ نایي، حلوايي، قصاب، ډاکټر، حکیم، وکیل یې پاتې نه کړ، خو هر یوه د سختې ګرانۍ په پلمه انکار وکړ.'),
    ('On his eighth day sleeping under the transformer he showed his pulse to a homeopathic doctor, who diagnosed pneumonia, gave him powders and told him to see someone else too. He went to Jabbar the confectioner for hot milk and begged for a loan of two hundred rupees; Jabbar, who rarely laughed, burst out laughing at the impossible request of such a fool.',
     'جس دن ماسٹر الیاس نے ہومیو پیتھک ڈاکٹر کو نبض دکھائی، اس روز انھیں ٹرانسفارمر کے نیچے سوتے آٹھواں دن تھا؛ ڈاکٹر نے نمونیہ بتایا، پڑیا دی اور کسی اور کو بھی دکھانے کو کہا۔ وہ گرم دودھ پینے جبار حلوائی کی دکان پر گئے اور گڑگڑا کر دو سو روپے قرض مانگے؛ جبار، جو عام زندگی میں بہت کم ہنستا تھا، ایسے الّو کی اس انہونی فرمائش پر ہنس پڑا۔',
     'په هغه ورځ چې ماسټر الیاس هومیوپاتیک ډاکټر ته نبض وښود، د ټرانسفارمر لاندې یې د خوب اتمه ورځ وه؛ ډاکټر نمونیا وویله، پوډرونه یې ورکړل او ویې ویل چې بل چا ته هم ځان وښيي. هغه د تودو شیدو لپاره د جبار حلوايي دوکان ته لاړ او په زارۍ یې دوه سوه روپۍ پور وغوښت؛ جبار چې په عادي ژوند کې ډېر لږ خندل، د داسې احمق په دې ناشوني غوښتنه وخندل.'),
    ('For three days the master sat on his cot with his quilt over his head like an igloo; every passer-by greeted him and asked, “Basking in the sun, Master ji?”, and he answered in a muffled voice, “Yes, I was feeling a little cold.” On the fourth day, at the dawn call to prayer, he died, and everyone in Mohsin Mohalla was deeply shocked.',
     'مسلسل تین دن ماسٹر الیاس اپنی رضائی سر پر اگلو کی طرح اوڑھے چارپائی پر بیٹھے رہے؛ جو گزرتا السلام علیکم کہہ کر پوچھتا ’’کیوں جی ماسٹر جی، دھوپ سینکی جا رہی ہے؟‘‘ اور وہ اندر سے بند آواز میں جواب دیتے ’’ہاں جی، تھوڑی سردی لگ رہی تھی۔‘‘ چوتھے روز فجر کی اذان کے وقت ماسٹر صاحب فوت ہو گئے تو محسن محلّہ کے ایک ایک شخص کو بڑا صدمہ ہوا۔',
     'درې ورځې پرلپسې ماسټر الیاس خپله بړستن د ایګلو په څېر پر سر اغوستې پر کټ ناست و؛ هر چا چې تېرېده سلام به یې اچاوه او پوښتل به یې: "ماسټر جي، لمر تودوئ؟" او هغه به له دننه په بند غږ ځواب ورکاوه: "هو جي، لږ یخني مې کېده." په څلورمه ورځ د سهار د اذان پر مهال ماسټر صاحب مړ شو، او د محسن محلې هر کس ته لویه صدمه ورسېده.'),
    ('Wrapped in silence and grief, everyone stood in the sun; the master’s quails were given a bowlful of millet and his cock a cupful of dough pellets. Shaikh Karim Nawaz came and sat under the transformer on a large rug, with fresh newspapers; he gave two hundred rupees to Saeed and Bilal to arrange the grave and three hundred to Babu Jalal for the shroud, camphor, rose-water and flowers; Jabbar sent a pot of tea; and in no time the people of Mohsin Mohalla collected eight hundred and eleven rupees for the master’s qul ceremony and deposited it with Shaikh Karim Nawaz.',
     'ہر شخص خاموشی اور دکھ میں لپٹا دھوپ میں جا کھڑا ہوا؛ ماسٹر جی کے بٹیروں کو کٹورہ بھر کنگنی اور مرغے کو آٹے کی آبخورہ بھر گولیاں ڈالی گئیں۔ شیخ کریم نواز حویلی سے نکل کر ٹرانسفارمر کے نیچے بڑی سی دری پر آ بیٹھے، تازہ اخبار رکھے گئے؛ انھوں نے دو سو روپے سعید اور بلال کو قبر کے بندوبست کے لیے اور تین سو روپے بابو جلال کو لٹھے، کافور، عرقِ گلاب اور پھولوں کے لیے دیے؛ جبار حلوائی نے دودھ پتی کا پتیلا بھیجا؛ اور دیکھتے دیکھتے محسن محلّہ کے لوگوں نے ماسٹر صاحب کی رسمِ قل کے لیے آٹھ سو گیارہ روپے جمع کر کے شیخ کریم نواز کے پاس محفوظ کرا دیے۔',
     'هر څوک په چوپتیا او غم کې نغښتی لمر ته ودرېد؛ د ماسټر جي بټېرو ته یو کاسه کنګني (ارزن) او چرګ ته یو جام د اوړو ګولۍ واچول شوې. شیخ کریم نواز له حویلۍ ووت او د ټرانسفارمر لاندې پر یوه لویه بوریا کېناست، تازه ورځپاڼې کېښودل شوې؛ هغه سعید او بلال ته د قبر د بندوبست لپاره دوه سوه روپۍ او بابو جلال ته د کفن، کافورو، ګلابو اوبو او ګلانو لپاره درې سوه روپۍ ورکړې؛ جبار حلوايي د چایو یو دېګ ولېږه؛ او په لیدو لیدو کې د محسن محلې خلکو د ماسټر صاحب د قل مراسمو لپاره اته سوه یوولس روپۍ راټولې کړې او د شیخ کریم نواز سره یې خوندي کړې.'),
]: s.p(*x)
tx = BOOK.record(s, 'urdu12-u11-text-2', 'Lesson text — summary (2)', 'متنِ سبق — خلاصہ (۲)', 'د لوست متن — لنډیز (۲)', 56, [102, 103])
tx['sourceGap'] = 'Ashfaq Ahmad (d. 2004) — in copyright; paragraph-wise summary in the app, not verbatim. Printed pp. 102–103.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the questions.', '۱۔ سوالات کے جوابات لکھیں۔', '۱. د پوښتنو ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) What did the people of Mohsin Mohalla know about the master?', '(ا) محسن محلّہ کے لوگ ماسٹر صاحب کے بارے میں کیا جانتے تھے؟', '(ا) د محسن محلې خلک د ماسټر صاحب په اړه څه پوهېدل؟'),
    ('(b) What kind of man was the master?', '(ب) ماسٹر صاحب کس طرح کے آدمی تھے؟', '(ب) ماسټر صاحب څه ډول سړی و؟'),
    ('(c) Why did people not like to make friends with the master?', '(ج) لوگ ماسٹر صاحب سے دوستی کرنا کیوں پسند نہیں کرتے تھے؟', '(ج) خلکو ولې له ماسټر صاحب سره دوستي نه خوښوله؟'),
    ('(d) How did the landlord treat the master?', '(د) مالک مکان نے ماسٹر صاحب سے کیا سلوک کیا؟', '(د) د کور مالک له ماسټر صاحب سره څه چلند وکړ؟'),
    ("(e) What attitude did people adopt after the master's death?", '(ہ) ماسٹر صاحب کے مرنے کے بعد لوگوں نے کیا طرزِ عمل اپنایا؟', '(ه) د ماسټر صاحب له مړینې وروسته خلکو کوم چلند غوره کړ؟'),
    ('(f) What was the fate of the master?', '(و) ماسٹر صاحب کا کیا انجام ہوا؟', '(و) د ماسټر صاحب برخلیک څه شو؟'),
    ('(g) Write the central idea of this story.', '(ز) اس افسانے کا مرکزی خیال لکھیں۔', '(ز) د دې افسانې مرکزي فکر ولیکئ.'),
])
ex = BOOK.record(e, 'urdu12-u11-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 56, [103])

if __name__ == '__main__':
    BOOK.save(56, [(11, tx), (11, ex)])
