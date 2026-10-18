"""Urdu XII PDF96 (spread): p.182 Lesson 17 text end (source آبِ گم, summary); p.183 مشق Q1–Q3 (start)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
for x in [
    ('…“One doesn’t need to be an M.R.C.P. and F.R.C.S. and tap here and there with a tube to give it. I looked from Landi Kotal to Landhi and saw nobody more loving than you, more content himself and gladdening others; so I took a ticket and came to you — the rest was an excuse to scrape the rust off my spirit. The days I spent with you have added that much to my life. May God keep you ever cheerful and kind to me. Asking forgiveness for the trouble I caused must be one of those Lucknow formalities beyond an ignorant man like me.',
     '…’’اس کے لیے ایم آر سی پی اور ایف آر سی ایس ہونے اور جگہ بے جگہ ٹونٹی لگا کر دیکھنے کی ضرورت نہیں۔ میں نے لنڈی کوتل سے لانڈھی تک نگاہ ڈالی، آپ سے زیادہ محبتی، خود خرسند رہنے اور دوسروں کا دل شاد کرنے والا کوئی بندہ نظر نہیں آیا؛ چنانچہ میں ٹکٹ لے کر آپ کے پاس آ گیا، باقی جو کچھ ہوا وہ طبیعت کا زنگ اتارنے کا بہانہ تھا۔ جتنے دن آپ کے ساتھ گزرے اتنے دنوں سے میری زندگی بڑھ گئی۔ خدا آپ کو اسی طرح شادمان اور مجھ پر مہربان رکھے۔ آپ کو میری وجہ سے جو تکلیف ہوئی اس کی معافی مانگنا لکھنوی تکلفات میں شامل ہوگا، جو مجھ جیسے جاہل کے بس کا کام نہیں۔',
     '…"د دې لپاره د ایم.آر.سي.پي او ایف.آر.سي.ایس کېدو او دلته هلته د نل (سټیتوسکوپ) لګولو اړتیا نشته. ما له لنډي‌کوتل تر لانډي پورې وکتل؛ له تاسو ډېر مینه‌ناک، پخپله خوښ او د نورو زړه خوشحالوونکی بنده مې ونه لید؛ نو ټکټ مې واخیست او تاسو ته راغلم — نور هر څه چې وشول، د طبیعت د زنګ ایستلو بهانه وه. څومره ورځې چې له تاسو سره تېرې شوې، هومره زما ژوند اوږد شو. خدای دې تاسو همداسې خوشحاله او پر ما مهربانه وساتي. زما له امله چې تاسو ته کومه ستونزه ورسېده، د هغې بښنه غوښتل به د لکهنوي تکلفاتو برخه وي، چې زما په څېر جاهل یې له وسې بهر دي.'),
    ('“May this illness be ruined — the cup of life is spilling before it is full. Even while dictating this letter I run short of breath; for fear I cannot even cough properly. Your sister-in-law (bhābī) starts crying; hidden from me she rains tears every now and then with thunder and lightning. I keep telling her, my fortunate one, until I am quite unconscious I am not a man to admit defeat to illness. Bisharat Bhai! For such a man there is a very bad word in Pashto. Last week I began building a new house on University Road; in its hall there will be room for fifty Peshawari or a hundred Karachi poets to sit cross-legged.',
     '’’اس بیماری کا خانہ خراب ہو، عمر کا پیمانہ لبریز ہونے سے پہلے ہی چھلکا جا رہا ہے۔ خط لکھوانے میں بھی سانس اکھڑ جاتی ہے، ڈر کے مارے ٹھیک سے کھانس بھی نہیں سکتا۔ آپ کی بھابی رونے لگتی ہے، مجھ سے چھپ کر وقفے وقفے سے گرج چمک کے ساتھ اشک باری کرتی ہے۔ بہتیرا سمجھاتا ہوں کہ بختاور! جب تک بالکل بے ہوش نہ ہو جاؤں، میں بیماری سے ہار ماننے والا آدمی نہیں۔ بشارت بھائی! ایسے آدمی کے لیے پشتو میں بہت برا لفظ ہے۔ گزشتہ ہفتے یونیورسٹی روڈ پر ایک نیا مکان بنوانا شروع کر دیا ہے؛ دالان میں پشاور کے پچاس یا کراچی کے سو شاعروں کے دو زانو بیٹھنے کی گنجائش ہوگی۔',
     '"د دې ناروغۍ کور دې وران شي، د عمر پیاله له ډکېدو مخکې تويېږي. د لیک په لیکلو کې هم ساه راباندې بندېږي؛ له وېرې په سمه توګه ټوخی هم نه شم کولی. ستاسو ورندار ژړا پیلوي؛ له ما پټه وخت ناوخت د تالندې او برېښنا سره اوښکې تويوي. ډېر ورته وایم چې بختوره! تر هغه چې بالکل بې‌هوښه نه شم، زه هغه سړی نه یم چې ناروغۍ ته ماته ومني. بشارت وروره! د داسې سړي لپاره په پښتو کې ډېره بده کلمه ده. تېره اونۍ مې د پوهنتون پر سړک د یوه نوي کور جوړول پیل کړي؛ په دالان کې به یې د پېښور د پنځوسو یا د کراچۍ د سلو شاعرانو د زنګون‌ناستې ځای وي.'),
    ('“All else is well. To everyone, according to rank, salaams, prayers, love and scolding.”', '’’باقی سب خیریت ہے۔ سب کو درجہ بدرجہ سلام، دعا، پیار اور ڈانٹ ڈپٹ۔‘‘', '"نور ټول خیریت دی. ټولو ته د مرتبې سره سم سلام، دعا، مینه او ټکول."'),
    ('Bisharat left for Peshawar by the first train.', 'بشارت پہلی ٹرین سے پشاور روانہ ہو گئے۔', 'بشارت د لومړي ریل ګاډي په وسیله پېښور ته روان شو.'),
    ('(Aab-e-Gum)', '(آبِ گم)', '(آب ګم)'),
]: s.p(*x)
tx = BOOK.record(s, 'urdu12-u17-text-8', 'Lesson text — summary (8)', 'متنِ سبق — خلاصہ (۸)', 'د لوست متن — لنډیز (۸)', 96, [182])
tx['sourceGap'] = 'Mushtaq Ahmad Yousufi (d. 2018) — in copyright; paragraph-wise summary in the app, not verbatim. Printed p. 182 (lesson text runs pp. 169–182).'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions.', '۱۔ مندرجہ ذیل سوالات کے جوابات لکھیں۔', '۱. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) For what purpose had the Khan Sahib come to Karachi?', '(الف) خان صاحب کس مقصد کے لیے کراچی آئے تھے؟', '(الف) خان صاحب د کومې موخې لپاره کراچۍ ته راغلی و؟'),
    ("(b) Describe the Khan Sahib's love of good food in your own words.", '(ب) خان صاحب کی خوش خوراکی کا حال اپنے الفاظ میں لکھیں؟', '(ب) د خان صاحب د ښو خوړو مینه په خپلو کلمو ولیکئ؟'),
    ('(c) What defects did Bisharat point out in the timber sent by the Khan Sahib?', '(ج) بشارت نے خان صاحب کی بھیجی ہوئی لکڑی میں کیا نقائص گنوائے؟', '(ج) بشارت د خان صاحب په لېږل شویو لرګیو کې کومې نیمګړتیاوې وښودې؟'),
    ('(d) How was the dispute between Bisharat and the Khan Sahib settled?', '(د) بشارت اور خان صاحب کے درمیان تنازعہ کیسے طے ہوا؟', '(د) د بشارت او خان صاحب ترمنځ شخړه څنګه حل شوه؟'),
    ('(e) What had the Khan Sahib written in his letter?', '(ہ) خان صاحب نے اپنے خط میں کیا لکھا تھا؟', '(ه) خان صاحب په خپل لیک کې څه لیکلي وو؟'),
    ('(f) What meaning did the Khan Sahib give for “waṭṭa-saṭṭa”?', '(و) خان صاحب نے وٹہ سٹہ کا کیا مفہوم بتایا؟', '(و) خان صاحب د "وټه سټه" کومه مانا وښوده؟'),
])
e.p('2. Fill in the blanks.', '۲۔ خالی جگہ پُر کریں۔', '۲. تش ځایونه ډک کړئ.')
e.group('lines', [
    ("(a) Bisharat was ________ of the Khan Sahib's sincerity and hospitality.", '(الف) بشارت خان صاحب کے خلوص و مدارات کے ________ تھے۔', '(الف) بشارت د خان صاحب د اخلاص او مېلمه‌پالنې ________ و.'),
    ('(b) The Khan Sahib was a ________ and heavily built man.', '(ب) خان صاحب ________ اور بھاری بھرکم آدمی تھے۔', '(ب) خان صاحب ________ او درانه وجود سړی و.'),
    ("(c) He considered sniffing chloroform to be against men's ________ .", '(ج) کلوروفارم سونگھنے کو مردوں کی ________ کے خلاف سمجھتے تھے۔', '(ج) د کلوروفارم بویول یې د نارینه وو د ________ خلاف ګڼل.'),
    ('(d) In this war, whoever wins, the ________ is only the truth.', '(د) اس جنگ میں فتح کسی کی بھی ہو ________ صرف سچائی ہوتی تھی۔', '(د) په دې جګړه کې بریا د هر چا وي، ________ یوازې رښتیا وه.'),
    ('(e) In waṭṭa-saṭṭa each party thinks that he came off in ________ .', '(ہ) وٹہ سٹہ میں ہر فریق یہی سمجھتا ہے کہ وہ ________ میں رہا۔', '(ه) په وټه سټه کې هره غاړه همدا ګڼي چې هغه په ________ کې پاتې شوه.'),
    ('(f) The Khan Sahib gave Muneeza a gift of ________ on her birthday.', '(و) خان صاحب نے منیزہ کو اس کی سالگرہ پر ________ کا تحفہ دیا۔', '(و) خان صاحب منیزې ته د هغې په کلیزه د ________ ډالۍ ورکړه.'),
])
e.p('3. Explain the following sentences.', '۳۔ درج ذیل جملوں کی وضاحت کریں۔', '۳. لاندې جملې تشریح کړئ.')
e.group('lines', [
    ('(a) I never saw vegetables or fish on his table, the apparent reason for which is that brinjals and fish have no legs.', '(الف) اُن کے دسترخوان پر کبھی سبزی یا مچھلی نہیں دیکھی، جس کی وجہ بظاہر یہی معلوم ہوتی ہے کہ بینگن اور مچھلی کی ٹانگیں نہیں ہوتیں۔', '(الف) د هغه پر دسترخوان مې هېڅکله سبزي یا کب ونه لید، چې لامل یې ښکاره همدا ښکاري چې بانجان او کب پښې نه لري.'),
])
ex = BOOK.record(e, 'urdu12-u17-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 96, [183, 184])
ex['sourceNote'] = 'Q3(a) begins on p.183 and continues on p.184; it is recorded here whole.'
issues = [{'id': 'urdu12-pdf096', 'unit': 17, 'printedPage': 183, 'description': 'Q2(c) refers to sniffing chloroform (“کلوروفارم سونگھنے”), which does not occur in the printed excerpt pp.169–182 (from a passage of Aab-e-Gum omitted from the textbook) — retained as printed. Q2(d) prints “اس جنگ میں … ہوتی تھی” for the text’s “لفظوں کی جنگ میں … ہوتی ہے”. Q1(c): in the text the timber was found defective, but no list of defects is given.'}]

if __name__ == '__main__':
    BOOK.save(96, [(17, tx), (17, ex)], issues=issues)
