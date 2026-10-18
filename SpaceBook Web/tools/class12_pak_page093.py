"""Pak Studies XII PDF93 (spread): printed pp.175–176 — Ch.9 First Plan review 4 (end)–8; Second Five-Year Plan (1960–65): aims, outlay, review; Third Plan (1965–70) aims 1–6."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
P = t.p
H = t.h
L = lambda rows: t.group('lines', rows)
P('… exports could not be increased; on the contrary, the quantity of imports increased. That is why the balance of payments became quite bad, so much so that during the first four years a deficit of 240 million rupees occurred in the balance of payments.',
  '… برآمدات کو نہ بڑھایا جا سکا بلکہ اُس کے برعکس درآمدات کی مقدار میں اضافہ ہو گیا۔ یہی وجہ ہے کہ توازنِ ادائیگی خاصا خراب ہو گیا۔ یہاں تک کہ پہلے چار سالوں کے دوران توازنِ ادائیگی میں 240 ملین روپے کا خسارہ واقع ہو گیا۔',
  '… صادرات زیات نه شول، بلکې برعکس د وارداتو اندازه زیاته شوه. همدا لامل دی چې د تادیاتو توازن ډېر خراب شو، تر دې چې په لومړیو څلورو کلونو کې د تادیاتو په توازن کې ۲۴۰ میلیونه روپۍ کسر رامنځته شو.')
L([('5. In the production of grain too, instead of nine per cent, only a four per cent increase could occur.', '5۔ اناج کی پیداوار میں بھی نو فیصد کی بجائے صرف چار فیصد اضافہ ہو سکا۔', '۵. د غلو په تولید کې هم د نهو سلنو پر ځای یوازې څلور سلنه زیاتوالی راغی.'),
   ('6. Because of bad weather conditions and some other reasons the production target of crops too could not be achieved.', '6۔ موسمی حالات کی خرابی و بعض دیگر وجوہات کی بنا پر فصلوں کا پیداواری ہدف بھی حاصل نہ کیا جا سکا۔', '۶. د موسمي حالاتو د خرابۍ او ځینو نورو لاملونو له امله د فصلونو تولیدي هدف هم ترلاسه نه شو.'),
   ('7. The target fixed for domestic savings too could not be fulfilled. The rate of national savings fell to minus 21 per cent.', '7۔ اندرونِ ملک بچتوں کا جو ہدف مقرر کیا گیا تھا وہ بھی پورا نہ ہو سکا۔ ملکی بچتوں کی شرح منفی 21 فیصد تک کم ہو گئی۔', '۷. د کورنیو سپمو لپاره ټاکل شوی هدف هم پوره نه شو. د ملي سپمو کچه تر منفي ۲۱ سلنې ټیټه شوه.'),
   ('8. In the industrial field, however, several industries were established, for example industries relating to paper, newsprint, cardboard, fertiliser and chemical goods etc.', '8۔ صنعتی میدان میں البتہ کئی صنعتیں قائم ہوئیں۔ مثلاً کاغذ، نیوز پرنٹ، گتہ، کھاد، کیمیائی اشیاء سے متعلق صنعتیں وغیرہ۔', '۸. په صنعتي ډګر کې خو څو صنعتونه جوړ شول، لکه د کاغذ، نیوز پرنټ، ګتې، سرې او کیمیاوي توکو اړوند صنعتونه او نور.')])
P('From the above statistics it can be estimated that the First Five-Year Plan failed in most fields. Despite this, it cannot be denied that by virtue of its experiences new thinking and a new way of thought were born, from which help was obtained in formulating future development plans.',
  'درج بالا اعداد و شمار سے اندازہ لگایا جا سکتا ہے کہ پہلا پانچ سالہ منصوبہ بیشتر میدانوں میں ناکام رہا۔ اس کے باوجود اس بات سے انکار نہیں کیا جا سکتا کہ اس کے تجربات کی بدولت نئی سوچ اور اندازِ فکر نے جنم لیا۔ جس سے آئندہ کے ترقیاتی منصوبہ جات کو تشکیل دینے میں مدد ملی۔',
  'له پورته شمېرو اټکل کېدای شي چې لومړی پنځه کلن پلان په ډېرو ډګرونو کې ناکام و. سره له دې له دې خبرې انکار نه شي کېدای چې د هغه د تجربو له برکته نوی فکر او د فکر نوی طرز وزېږېد، چې له امله یې د راتلونکو پراختیايي پلانونو په جوړولو کې مرسته وشوه.')
H('Second Five-Year Development Plan (1960 to 1965)', 'دوسرا پانچ سالہ ترقیاتی منصوبہ (1960ء تا 1965ء)', 'دویم پنځه کلن پراختیايي پلان (۱۹۶۰ تر ۱۹۶۵ز)')
P('The Second Five-Year Development Plan (1960 to 1965) was adopted on the completion of the term of the first plan. The major objectives of this plan and their targets were as follows:',
  'دوسرا پانچ سالہ ترقیاتی منصوبہ (1960ء تا 1965ء) پہلے منصوبے کی مدتِ اختتام پر اپنایا گیا۔ اس منصوبے کے بڑے بڑے مقاصد اور اُن کے اہداف درج ذیل تھے:۔',
  'دویم پنځه کلن پراختیايي پلان (۱۹۶۰ تر ۱۹۶۵ز) د لومړي پلان د مودې په پای کې غوره شو. د دې پلان لویې موخې او هدفونه یې دا وو:')
L([('1. Increasing national income by 24 per cent.', '1۔ قومی آمدنی میں 24 فیصد اضافہ کرنا۔', '۱. په ملي عاید کې ۲۴ سلنه زیاتوالی.'),
   ('2. Increasing per-capita income by 10 per cent.', '2۔ فی کس آمدنی میں 10 فی صد اضافہ کرنا۔', '۲. په سړي سر عاید کې ۱۰ سلنه زیاتوالی.'),
   ('3. Providing employment opportunities to 2.5 million new individuals.', '3۔ 2.5 ملین نئے افراد کو روزگار کے مواقع فراہم کرنا۔', '۳. ۲.۵ میلیونو نویو کسانو ته د روزګار فرصتونه برابرول.'),
   ('4. Increasing agricultural production by fourteen per cent.', '4۔ زرعی پیداوار میں چودہ فیصد اضافہ کرنا۔', '۴. په کرنیز تولید کې څوارلس سلنه زیاتوالی.'),
   ('5. Increasing the productive capacity of large and medium-scale industries by up to 14 per cent.', '5۔ بڑی اور اوسط درجے کی صنعتوں کی پیداواری صلاحیت میں 14 فیصد تک اضافہ کرنا۔', '۵. د لویو او منځنیو صنعتونو په تولیدي وړتیا کې تر ۱۴ سلنې زیاتوالی.'),
   ('6. Raising the production of cottage and small industries by up to 25 per cent.', '6۔ گھریلو اور چھوٹی صنعتوں کی پیداوار کو 25 فیصد تک بڑھانا۔', '۶. د کورنیو او وړو صنعتونو تولید تر ۲۵ سلنې لوړول.'),
   ('7. Increasing exports by three per cent annually.', '7۔ برآمدات میں سالانہ تین فی صد اضافہ کرنا۔', '۷. په صادراتو کې کلنۍ درې سلنه زیاتوالی.')])
P('To fulfil the objectives and targets of the Second Five-Year Plan, an estimate of 23 billion rupees had been made. Of this sum it was estimated that 12.40 billion rupees would be spent in the government sector, 3.80 billion rupees in the semi-government sector and 6.80 billion rupees in the private sector.',
  'دوسرے پانچ سالہ منصوبے کے مقاصد اور اہداف کو پورا کرنے کے لیے 23 بلین روپے کا تخمینہ لگایا گیا تھا۔ اس رقم میں سے 12.40 بلین روپے سرکاری شعبے میں 3.80 بلین روپے نیم سرکاری شعبے اور 6.80 بلین روپے نجی شعبے میں خرچ کرنے کا اندازہ لگایا گیا تھا۔',
  'د دویم پنځه کلن پلان د موخو او هدفونو د پوره کولو لپاره د ۲۳ میلیارده روپیو اټکل شوی و. له دې پیسو څخه اټکل شوی و چې ۱۲.۴۰ میلیارده روپۍ به په دولتي سکتور، ۳.۸۰ میلیارده روپۍ په نیمه دولتي سکتور او ۶.۸۰ میلیارده روپۍ په خصوصي سکتور کې ولګول شي.')
P('Despite the fact that in the Second Development Plan the establishment of heavy industry and its development was not given its proper place, and moreover dependence was placed on foreign capital and aid for this plan, the pace of the country’s economic progress under this plan remained quite satisfactory. In some sectors progress was even greater than its targets.',
  'باوجود اس بات کے کہ دوسرے ترقیاتی منصوبے میں بھاری صنعت کے قیام اور اُس کی ترقی کو اس کا صحیح مقام نہیں دیا گیا تھا۔ نیز اس منصوبے کے لیے غیر ملکی سرمائے اور امداد پر انحصار کیا جانا تھا، اس منصوبے کے تحت ملک کی معاشی ترقی کی رفتار خاصی تسلی بخش رہی۔ بعض شعبوں میں تو ترقی اپنے اہداف سے بھی زیادہ ہوئی۔',
  'سره له دې چې په دویم پراختیايي پلان کې د دروند صنعت جوړولو او پرمختګ ته خپل سم ځای نه و ورکړل شوی، او همداراز د دې پلان لپاره پر بهرنۍ پانګې او مرستې تکیه کېده، د دې پلان له مخې د هېواد د اقتصادي پرمختګ چټکتیا ډېره قناعت‌بښونکې وه. په ځینو برخو کې خو پرمختګ له خپلو هدفونو هم زیات و.')
P('From a review of the plan the following points become the centre of attention:',
  'منصوبے کا جائزہ لینے سے مندرجہ ذیل نکات توجہ کا مرکز بنتے ہیں:۔',
  'د پلان له کتنې لاندې ټکي د پاملرنې مرکز ګرځي:')
L([('1. The increase in national income rose even beyond 30 per cent.', '1۔ قومی آمدنی میں اضافہ 30 فیصد سے بھی بڑھ گیا۔', '۱. په ملي عاید کې زیاتوالی له ۳۰ سلنې هم واوښت.'),
   ('2. Exports increased at the rate of seven per cent annually.', '2۔ برآمدات میں سات فیصد سالانہ کے حساب سے اضافہ ہوا۔', '۲. صادرات په کلنۍ اووه سلنه حساب زیات شول.'),
   ('3. The industrial sector progressed by more than 40 per cent.', '3۔ شعبہ صنعت میں 40 فیصد سے زیادہ ترقی ہوئی۔', '۳. صنعتي برخې له ۴۰ سلنې زیات پرمختګ وکړ.'),
   ('4. Progress in the agricultural sector was more than 15 per cent.', '4۔ زرعی شعبے میں ترقی 15 فیصد سے زیادہ ہوئی۔', '۴. په کرنیزه برخه کې پرمختګ له ۱۵ سلنې زیات و.'),
   ('5. Employment opportunities could not be increased to the expected extent. Thus the pace of progress of this sector remained substandard.', '5۔ روزگار کے مواقع متوقع حد تک نہ بڑھائے جا سکے۔ اس طرح اس شعبے کی ترقی کی رفتار غیر معیاری رہی۔', '۵. د روزګار فرصتونه تر متوقع بریده زیات نه شول. په دې ډول د دې برخې د پرمختګ چټکتیا له معیاره ټیټه وه.')])
H('Third Five-Year Development Plan (1965 to 1970)', 'تیسرا پانچ سالہ ترقیاتی منصوبہ (1965ء تا 1970ء)', 'درېیم پنځه کلن پراختیايي پلان (۱۹۶۵ تر ۱۹۷۰ز)')
P('The major objectives of the third plan and their targets were as follows:',
  'تیسرے منصوبے کے بڑے بڑے مقاصد اور اُن کے اہداف درج ذیل تھے:۔',
  'د درېیم پلان لویې موخې او هدفونه یې دا وو:')
L([('1. Accelerating the pace of national progress and increasing national production by 37 per cent.', '1۔ ملکی ترقی کی رفتار کو تیز کرنا اور قومی پیداوار میں 37 فیصد اضافہ کرنا۔', '۱. د هېواد د پرمختګ چټکتیا ګړندۍ کول او په ملي تولید کې ۳۷ سلنه زیاتوالی.'),
   ('2. Increasing per-capita income by 20 per cent.', '2۔ فی کس آمدنی میں 20 فیصد اضافہ کرنا۔', '۲. په سړي سر عاید کې ۲۰ سلنه زیاتوالی.'),
   ('3. Providing employment to 5.5 million individuals.', '3۔ 5.5 ملین افراد کو روزگار مہیا کرنا۔', '۳. ۵.۵ میلیونو کسانو ته روزګار برابرول.'),
   ('4. Accelerating the pace of agricultural progress and increasing it by five per cent annually.', '4۔ زرعی ترقی کی رفتار کو تیز کرنا اور اس میں پانچ فیصد سالانہ اضافہ کرنا۔', '۴. د کرنیز پرمختګ چټکتیا ګړندۍ کول او پکې کلنۍ پنځه سلنه زیاتوالی.'),
   ('5. Raising the rate of industrial progress to thirteen per cent annually.', '5۔ صنعتی ترقی کی شرح تیرہ فیصد سالانہ تک بڑھانا۔', '۵. د صنعتي پرمختګ کچه کلنۍ دیارلس سلنې ته لوړول.'),
   ('6. Ending regional disparity.', '6۔ علاقائی تفاوت کو ختم کرنا۔', '۶. سیمه‌ییز توپیر له منځه وړل.')])
rec = BOOK.record(t, 'pak12-ch9-text-10', 'Chapter 9 text (10)', 'بابِ نہم — متن (۱۰)', 'نهم څپرکی — متن (۱۰)', 93, [175, 176])
rec['sourceNote'] = 'The opening words continue review item 4 from p.174. The Second Plan aims list runs across the page turn (items 1–6 on p.175, 7 on p.176). The Third Plan aims list continues on p.177 (PDF94).'

if __name__ == '__main__':
    BOOK.save(93, [(9, rec)])
