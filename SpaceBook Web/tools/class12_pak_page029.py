"""Pak Studies XII PDF29 (spread): printed pp.49–50 — Ch.3 communications; physical features of Pakistan; climate; climatic regions begins."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
def L(rows): t.group('lines', rows)
P('As a step towards a promising future, Pakistan has rapidly begun work to extend and modernise its system of roads, railways, ports and telecommunications etc. This will not only facilitate internal trade and traffic, but trade and traffic and economic links with Afghanistan and the Central Asian countries will also be expanded and strengthened, and these countries will be able to gain access to the Indian Ocean easily.',
  'ایک خوش آئند مستقبل کی جانب پیش قدمی کے طور پر پاکستان نے اپنی سڑکوں، ریلوں، بندرگاہوں اور ٹیلی مواصلات وغیرہ کے نظام کو وسیع اور جدید ترین بنانے کے لیے تیزی سے کام شروع کر دیا ہے۔ اس سے نہ صرف اندرونِ ملک تجارت اور آمد و رفت وغیرہ میں سہولت پیدا ہوگی بلکہ افغانستان اور وسطِ ایشیائی ممالک کے ساتھ تجارت و آمد و رفت اور اقتصادی روابط کو وسعت اور استحکام بھی نصیب ہوگا اور یہ ممالک آسانی سے بحرِ ہند تک رسائی حاصل کر سکیں گے۔',
  'د یوه ښه راتلونکي پر لور د ګام په توګه پاکستان د خپلو سړکونو، اورګاډو، بندرونو او مخابراتو او نورو د سیستم د پراخولو او عصري کولو لپاره په چټکۍ کار پیل کړی. له دې نه یوازې د هېواد په دننه کې سوداګري او تګ راتګ اسانېږي، بلکې له افغانستان او منځنۍ اسیا هېوادونو سره سوداګري، تګ راتګ او اقتصادي اړیکې به هم پراخې او ټینګې شي، او دا هېوادونه به په اسانۍ هند سمندر ته لاسرسی ومومي.')
P('Bharat urgently needs energy to advance its economy. It can obtain this energy from the reserves of oil and gas of the Central Asian states, Qatar and Iran. Pakistan has already given permission to pass a pipeline through its territory.',
  'بھارت کو اپنی معیشت آگے بڑھانے کے لیے توانائی کی اشد ضرورت ہے۔ یہ توانائی اسے وسطِ ایشیائی ریاستوں، قطر اور ایران کے تیل و گیس کے ذخائر سے حاصل ہو سکتی ہے۔ پاکستان اپنی سرزمین سے پائپ لائن گزارنے کی پہلے ہی سے اجازت دے چکا ہے۔',
  'بهارت ته د خپل اقتصاد د مخ ته وړلو لپاره انرژۍ ته سخته اړتیا ده. دا انرژي هغه ته د منځنۍ اسیا هېوادونو، قطر او ایران د تېلو او ګازو له زېرمو ترلاسه کېدای شي. پاکستان له مخکې د خپلې خاورې له لارې د نل‌لیکې د تېرولو اجازه ورکړې.')
H('Physical features of Pakistan', 'پاکستان کے طبعی خد و خال', 'د پاکستان طبیعي بڼه')
P('Pakistan is spread over a vast area; therefore its features are not all alike, and all these features have their own separate characteristics. In this respect the land of Pakistan can be divided into the following parts.',
  'پاکستان ایک وسیع علاقے میں پھیلا ہوا ہے۔ اس لیے اس کے خد و خال ایک جیسے نہیں، اور یہ سب خد و خال اپنی الگ الگ خاصیتیں رکھتے ہیں۔ اس لحاظ سے سرزمینِ پاکستان کو مندرجہ ذیل حصوں میں تقسیم کیا جا سکتا ہے۔',
  'پاکستان په یوه پراخه سیمه کې غځېدلی؛ نو بڼه یې یو شان نه ده، او دا ټولې بڼې خپلې جلا ځانګړنې لري. په دې لحاظ د پاکستان خاوره په لاندې برخو وېشل کېدای شي:')
L([('1. Northern mountain ranges', '1۔ شمالی پہاڑی سلسلے', '۱. شمالي غرنۍ لړۍ'), ('2. Western mountain ranges', '2۔ مغربی پہاڑی سلسلے', '۲. لوېدیځې غرنۍ لړۍ'),
   ('3. The Salt Range and the Potohar Plateau', '3۔ کوہستانِ نمک و سطحِ مرتفع پوٹھوہار', '۳. د مالګې غرنۍ لړۍ او د پوټوهار لوړه سطحه'), ('4. The plain of the River Indus', '4۔ دریائے سندھ کا میدانی علاقہ', '۴. د سند سیند هوار سیمه'),
   ('5. The Balochistan Plateau', '5۔ سطحِ مرتفع بلوچستان', '۵. د بلوچستان لوړه سطحه'), ('6. The Thal and Thar desert area', '6۔ تھل و تھر کا ریگستانی علاقہ', '۶. د تهل او تهر شګلنه سیمه'),
   ('7. The coastal area', '7۔ ساحلی علاقہ', '۷. ساحلي سیمه')])
P('1. Northern mountain ranges: the long and snow-covered mountains of the Himalaya, Karakoram and Hindu Kush are included. The Himalaya range has been divided into the following mountains:',
  '1۔ شمالی پہاڑی سلسلے میں ہمالیہ، قراقرم اور ہندوکش کے طویل اور برف پوش پہاڑ شامل ہیں۔ کوہِ ہمالیہ کے سلسلے کو مندرجہ ذیل پہاڑوں میں تقسیم کیا گیا ہے۔',
  '۱. په شمالي غرنیو لړیو کې د همالیا، قراقرم او هندوکش اوږده او واوره‌پوښ غرونه شامل دي. د همالیا لړۍ په لاندې غرونو وېشل شوې:')
L([('i. Siwaliks', 'i۔ شوالک', 'i. شوالک'), ('ii. Pir Panjal', 'ii۔ پیر پنجال', 'ii. پیر پنجال'), ('iii. Great Himalaya', 'iii۔ ہمالیہ کبیر', 'iii. لوی همالیا'), ('iv. Ladakh range', 'iv۔ کوہِ لداخ', 'iv. د لداخ غر')])
P('2. The western mountain ranges are spread over a vast area of Pakistan. The following famous mountains are included in them:',
  '2۔ مغربی پہاڑی سلسلے پاکستان کے ایک وسیع علاقے میں پھیلے ہوئے ہیں۔ ان میں مندرجہ ذیل مشہور پہاڑ شامل ہیں۔',
  '۲. لوېدیځې غرنۍ لړۍ د پاکستان په یوه پراخه سیمه کې غځېدلې دي. په هغو کې لاندې مشهور غرونه شامل دي:')
L([('i. Shandur or Hindu Raj (Hindu Kush)', 'i۔ شندور یا ہندو راج (ہندوکش)', 'i. شندور یا هندو راج (هندوکش)'), ('ii. Dir, Swat and Indus Kohistan', 'ii۔ دیر، سوات اور سندھ کوہستان', 'ii. دیر، سوات او سند کوهستان'),
   ('iii. Koh-e-Safed', 'iii۔ کوہِ سفید', 'iii. سپین غر'), ('iv. The mountains of Waziristan', 'iv۔ وزیرستان کے پہاڑ', 'iv. د وزیرستان غرونه'),
   ('v. Koh-e-Sulaiman', 'v۔ کوہِ سلیمان', 'v. د سلیمان غر'), ('vi. Kirthar range', 'vi۔ کوہِ کیرتھر', 'vi. د کیرتهر غر')])
P('3. The Salt Range and the Potohar Plateau: the Salt Range begins south of district Jhelum and meets Koh-e-Sulaiman in the west. The Potohar Plateau lies to the north of the Salt Range.',
  '3۔ کوہستانِ نمک و سطحِ مرتفع پوٹھوہار:- کوہستانِ نمک کا سلسلہ ضلع جہلم کے جنوب سے شروع ہو کر مغرب میں کوہِ سلیمان سے جا ملتا ہے۔ سطحِ مرتفع پوٹھوہار کوہِ نمک کے شمال میں واقع ہے۔',
  '۳. د مالګې غرنۍ لړۍ او د پوټوهار لوړه سطحه: د مالګې غرنۍ لړۍ د جهلم ولسوالۍ له سویله پیلېږي او په لوېدیځ کې له سلیمان غره سره یوځای کېږي. د پوټوهار لوړه سطحه د مالګې د غره په شمال کې پرته ده.')
P('4. The plain of the River Indus has been divided into upper and lower plains.', '4۔ دریائے سندھ کے میدانی علاقے کو بالائی اور زیریں میدانوں میں تقسیم کیا گیا ہے۔', '۴. د سند سیند هوار سیمه په پورتنیو او لاندینیو هوارو وېشل شوې.')
P('5. The Balochistan Plateau: a vast area spread over the south-western part of Pakistan.', '5۔ سطحِ مرتفع بلوچستان کا وسیع علاقہ پاکستان کے جنوب مغربی حصے میں پھیلا ہوا ہے۔', '۵. د بلوچستان لوړه سطحه: یوه پراخه سیمه چې د پاکستان په سویل لوېدیځه برخه کې غځېدلې.')
P('6. The Thal and Thar deserts:', '6۔ تھل و تھر کا ریگستان', '۶. د تهل او تهر شګلنې:')
L([('i. The desert area between the rivers Indus and Jhelum is called Thal.', 'i۔ دریائے سندھ اور جہلم کے درمیان ریگستانی علاقہ تھل کہلاتا ہے۔', 'i. د سند او جهلم سیندونو ترمنځ شګلنه سیمه تهل بلل کېږي.'),
   ('ii. The Thar desert area begins from Bahawalpur in the south-east of Pakistan and extends to the area of the Rann of Kutch.', 'ii۔ تھر کا ریگستانی علاقہ پاکستان کے جنوب مشرق میں بہاولپور سے شروع ہو کر رن کچھ کے علاقے تک چلا جاتا ہے۔', 'ii. د تهر شګلنه سیمه د پاکستان په سویل ختیځ کې له بهاولپور پیلېږي او د رن کچ تر سیمې پورې غځېږي.')])
P('7. Coastal areas: Pakistan’s coastal area begins from the Rann of Kutch and the Indian border in the province of Sindh and runs in the west to the border of Iran. It consists of two parts, i.e. the Sindh coast and the Makran coast.',
  '7۔ ساحلی علاقے:- پاکستان کا ساحلی علاقہ صوبہ سندھ میں رن کچھ اور بھارتی سرحد سے شروع ہو کر مغرب میں ایران کی سرحد تک چلا جاتا ہے۔ یہ دو حصوں یعنی ساحلِ سندھ اور ساحلِ مکران پر مشتمل ہے۔',
  '۷. ساحلي سیمې: د پاکستان ساحلي سیمه د سند په ولایت کې له رن کچ او بهارتي پولې پیلېږي او په لوېدیځ کې د ایران تر پولې پورې ځي. دا له دوو برخو یعنې د سند ساحل او د مکران ساحل جوړه ده.')
H('The climate of Pakistan', 'پاکستان کی آب و ہوا', 'د پاکستان اقلیم')
P('Pakistan lies above the Tropic of Cancer. Most of it is far from the sea; therefore the climate here is of the extreme type, which is called a continental climate. All four seasons come here, but two seasons, summer and winter, are important. The hot season lasts from May to September. In this season there is intense heat; at some places the temperature reaches 50 degrees Celsius, e.g. Sibi and Jacobabad are famous as among the hottest places in the whole world. In winter there is severe cold in Quetta, Ziarat, Murree, Chitral, Gilgit and Dir, and at some places the temperature falls even below freezing point. The notable difference between summer and winter is because most of the country is far from the sea coast.',
  'پاکستان خطِ سرطان کے اوپر واقع ہے۔ اس کا زیادہ حصہ سمندر سے دور ہے۔ اس لیے یہاں کی آب و ہوا شدید قسم کی ہے۔ جسے برّی قسم کی آب و ہوا کہتے ہیں۔ یہاں چاروں موسم آتے ہیں لیکن دو موسم گرما اور سرما اہم ہیں۔ موسمِ گرما مئی سے ستمبر تک ہوتا ہے۔ اس موسم میں شدید گرمی پڑتی ہے بعض مقامات پر درجہ حرارت 50 سینٹی گریڈ تک پہنچ جاتا ہے مثلاً سبی اور جیکب آباد دنیا بھر کے گرم ترین مقامات کے طور پر شہرت رکھتے ہیں۔ موسمِ سرما میں کوئٹہ، زیارت، مری، چترال، گلگت اور دیر میں سخت سردی پڑتی ہے اور بعض مقامات پر درجہ حرارت نقطۂ انجماد سے بھی نیچے گر جاتا ہے۔ موسمِ گرما اور موسمِ سرما میں نمایاں فرق کی وجہ ملک کے بیشتر حصے کا ساحلِ سمندر سے دور ہونا ہے۔',
  'پاکستان د سرطان له خط پورته پروت دی. ډېره برخه یې له سمندره لرې ده؛ نو دلته اقلیم سخت ډول دی چې وچه‌ییز اقلیم بلل کېږي. دلته څلور واړه موسمونه راځي، خو دوه موسمونه، اوړی او ژمی، مهم دي. اوړی له مۍ تر سپتمبر پورې وي. په دې موسم کې سخته ګرمي وي؛ په ځینو ځایونو کې د تودوخې درجه ۵۰ سانتي‌ګراد ته رسېږي، لکه سیبي او جېکب‌اباد چې د ټولې نړۍ د تر ټولو ګرمو ځایونو په توګه شهرت لري. په ژمي کې په کوټه، زیارت، مري، چترال، ګلګت او دیر کې سخته یخني وي او په ځینو ځایونو کې د تودوخې درجه له کنګل نقطې هم ښکته کېږي. د اوړي او ژمي ترمنځ د ښکاره توپیر لامل د هېواد د ډېرې برخې له سمندري ساحله لرې والی دی.')
H('Regions of Pakistan by climate', 'آب و ہوا کے لحاظ سے پاکستان کے خطے', 'د اقلیم له مخې د پاکستان سیمې')
P('By climate Pakistan can be divided into the following regions.', 'آب و ہوا کے لحاظ سے پاکستان کو مندرجہ ذیل خطوں میں تقسیم کیا جا سکتا ہے۔', 'د اقلیم له مخې پاکستان په لاندې سیمو وېشل کېدای شي.')
rec = BOOK.record(t, 'pak12-ch3-text-3', 'Chapter 3 text (3)', 'بابِ سوم — متن (۳)', 'درېیم څپرکی — متن (۳)', 29, [49, 50])

if __name__ == '__main__':
    BOOK.save(29, [(3, rec)])
