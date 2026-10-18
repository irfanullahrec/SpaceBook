"""Urdu XII PDF27 (spread): printed pp.44–45 — Lesson 5 text end (Jurat, Nasikh, Atish, Momin, Mir Amman, Sarur, Zauq, Ghalib, Azad; source نیرنگِ خیال) and مشق Q1–Q3."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ('No one paid any heed to Jurat, but when he struck up a strain in his sweet voice, everyone’s heads began to sway. Nasikh’s flower-work seemed familiar to the eye, and in most places its embroidery needed the spectacles of others; but Atish’s fiery expression did not leave it without burning it. Momin spoke little, but when he said something, he looked towards Jurat.',
     'جراتؔ کو کوئی خاطر میں نہ لاتا تھا مگر جب وہ میٹھی آواز سے ایک تان اُڑاتا تھا تو سب کے سر ہل ہی جاتے تھے۔ ناسخؔ کی گلکاری چشم آشنا معلوم ہوتی تھی اور اکثر جگہ قلمکاری اُس کی عینک کی محتاج تھی مگر آتشؔ کی آتش بیانی اُسے جلائے بغیر نہ چھوڑتی تھی۔ مومنؔ کم سخن تھے مگر جب کچھ کہتے تھے، جراتؔ کی طرف دیکھتے تھے۔',
     'جرات ته به چا پام نه کاوه، خو کله چې به یې په خوږ غږ سُر پورته کړ، د ټولو سرونه به وښورېدل. د ناسخ ګلکاري سترګو ته اشنا ښکارېده او په ډېرو ځایونو کې یې قلمکاري د عینکو محتاجه وه، خو د اتش اورین بیان هغه له سوځولو پرته نه پرېښوده. مومن لږ ویونکی و، خو کله چې به یې څه ویل، جرات ته به یې کتل.'),
    ('An aged old man, wearing the dress of Muhammad Shah’s court — a jāma, a pleated turban tied — came leaning on a staff, but a dandy of Lucknow followed behind him abusing him. The dandy would certainly have come to blows with him, but four humble ones and a fifth crowned one were with him; they used to protect him. The old man was Mir Amman of Delhi, author of “Bagh-o-Bahar (Char Darvesh)”, and the dandy was Mirza Sarur of “Fasana-e-Ajaib”. At Zauq’s arrival the court was perfumed with the fragrance of general approval. He came in and greeted all like a pupil. Sauda rose and placed the crown of poet laureate (malik-ush-shuʿarā) on his head. Ghalib, though behind everyone, was below no one. He came with great fanfare and beat a kettle-drum so loudly that he deafened everyone’s ears. Some understood and some did not, but all went on saying “Wah wah!” and “Subhan Allah!”',
     'ایک پیرِ مرد دیرینہ سال محمد شاہی دربار کا لباس، جامہ پہنے، کھڑکی دار پگڑی باندھے، جریب ٹیکتے آتے تھے مگر ایک لکھنؤ کے بانکے پیچھے پیچھے گالیاں دیتے تھے۔ بانکے صاحب ضرور اُن سے دست و گریباں ہو جاتے لیکن چار خاکسار اور پانچواں تاجدار ان کے ساتھ تھا۔ یہ بچا لیتے تھے۔ بڈھے میر امن دہلوی ’’چار درویش‘‘ کے مصنف تھے اور بانکے صاحب میرزا سرورؔ ’’فسانۂ عجائب‘‘ والے تھے۔ ذوقؔ کے آنے پر پسندِ عام کے عطر سے دربار مہک گیا۔ انھوں نے اندر آ کر شاگردانہ طور پر سب کو سلام کیا۔ سوداؔ نے اُٹھ کر ملک الشعرائی کا تاج ان کے سر پر رکھ دیا۔ غالبؔ اگرچہ سب سے پیچھے تھے، پر کسی سے نیچے نہ تھے۔ بڑی دھوم دھام سے آئے اور ایک نقارہ اس زور سے بجایا کہ سب کے کان گنگ کر دیے۔ کوئی سمجھا اور کوئی نہ سمجھا مگر سب واہ واہ اور سبحان اللہ کرتے رہ گئے۔',
     'یو زوړ سپین‌ږیری، د محمد شاه د دربار جامې یې اغوستې، جامه په تن، چینو لرونکې پګړۍ تړلې، په امسا تکیه راته، خو د لکهنو یو شوخ ځوان یې پسې کنځلې کولې. شوخ صاحب به خامخا ورسره لاس او ګرېوان شوی وای، خو څلور عاجزان او پنځم تاجدار ورسره وو؛ دوی به یې ژغوره. زوړ میر امن دهلوي د "څلور درویشان" لیکوال و، او شوخ صاحب میرزا سرور د "فسانه عجایب" خاوند و. د ذوق په راتګ دربار د عام خوښۍ په عطرو خوشبویه شو. هغه دننه راغی او د شاګرد په توګه یې ټولو ته سلام وکړ. سودا پاڅېد او د ملک الشعرا تاج یې د هغه پر سر کېښود. غالب که څه هم له ټولو وروسته و، خو له چا ټیټ نه و. په لوی شور راغی او یو نغاره یې په دومره زور ووهله چې د ټولو غوږونه یې کاڼه کړل. ځینې پوه شول او ځینې نه، خو ټولو "واه واه" او "سبحان الله" ویل.'),
    ('Now I saw that only one chair was empty, and that was all. Meanwhile a voice came: “Call Azad.” At once a voice came that perhaps he would not accept to sit in this assembly; but from there someone again said: “Among whichever people you seat him, he will sit.” Meanwhile a few persons raised an outcry that his pen had waged war with a whole world; he should not be given a place in the court of fame. Argument began over this case. I wanted to lift the veil from my face, step forward and say something, but my guide and companion, that is the angel of mercy, took my hand and said quietly: “It is not expedient yet.” Meanwhile my eyes opened. I forgot even that quarrel and thanked God that, whether or not I got a chair in the court, at least I came back among the living from among the dead.',
     'اب میں نے دیکھا کہ فقط ایک کرسی خالی ہے اور بس۔ اتنے میں آواز آئی کہ آزاد کو بلاؤ۔ ساتھ ہی آواز آئی کہ شاید وہ اس جرگے میں بیٹھنا قبول نہ کرے مگر وہاں سے پھر کوئی بولا کہ اسے جن لوگوں میں بٹھا دو گے، بیٹھ جائے گا۔ اتنے میں چند اشخاص نے غُل مچایا کہ اس کے قلم نے ایک جہان سے لڑائی باندھ رکھی ہے۔ اسے دربارِ شہرت میں جگہ نہ دینی چاہیے۔ اس مقدمے پر قیل و قال شروع ہوئی۔ میں چاہتا تھا کہ نقاب چہرے سے اُلٹ کر آگے بڑھوں اور کچھ بولوں کہ میرے ہادی ہمدم یعنی فرشتۂ رحمت نے ہاتھ پکڑ لیا اور چپکے سے کہا کہ ابھی مصلحت نہیں۔ اتنے میں آنکھ کھل گئی۔ میں اس جھگڑے کو بھی بھول گیا اور خدا کا شکر کیا کہ بلا سے دربار میں کرسی ملی یا نہ ملی، مُردوں میں سے زندوں تو آیا۔',
     'اوس مې ولیدل چې یوازې یوه څوکۍ تشه ده او بس. په دې کې غږ راغی چې ازاد راوبولئ. سمدستي بل غږ راغی چې ښايي هغه په دې جرګه کې کېناستل ونه مني، خو له هغه ځایه بیا چا وویل: "په هر چا کې چې یې کېنوئ، کېني به." په دې کې یو څو کسانو شور جوړ کړ چې د هغه قلم له یوې نړۍ سره جګړه تړلې؛ د شهرت په دربار کې باید ځای ورنه کړل شي. پر دې مسله بحث پیل شو. ما غوښتل چې له مخ نقاب پورته کړم، مخکې شم او یو څه ووایم، خو زما لارښود ملګري یعنې د رحمت پرښتې لاس راونیو او په ورو یې وویل: "لا مصلحت نه دی." په دې کې مې سترګې پرانیستل شوې. هغه شخړه مې هم هېره کړه او د خدای شکر مې وکړ چې پروا نه لري په دربار کې څوکۍ راکړل شوه که نه، له مړو څخه ژوندیو ته خو راغلم.'),
    ('(Nairang-e-Khayal)', '(نیرنگِ خیال)', '(نیرنګ خیال)'),
]: t.p(*x)
tx = BOOK.record(t, 'urdu12-u5-text-6', 'Lesson text (6)', 'متنِ سبق (۶)', 'د لوست متن (۶)', 27, [44])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. About which poet or writer were the following sentences said?', '۱۔ درج ذیل جُملے کس شاعر یا ادیب کے بارے میں کہے گئے؟', '۱. لاندې جملې د کوم شاعر یا ادیب په اړه ویل شوې؟')
e.group('lines', [
    ('(a) Some understood and some did not, but all went on saying “Wah wah!” and “Subhan Allah!”', '(الف) کوئی سمجھا کوئی نہ سمجھا مگر سب واہ واہ اور سبحان اللہ کرتے رہ گئے۔', '(الف) ځینې پوه شول، ځینې نه، خو ټولو "واه واه" او "سبحان الله" ویل.'),
    ('(b) With his enchanting expression he drew pictures of fairyland.', '(ب) اپنی سحر بیانی سے پرستان کی تصویر کھینچتے تھے۔', '(ب) په خپل جادويي بیان یې د پېریانو د ځمکې انځور کېښ.'),
    ('(c) His pen has waged war with a whole world.', '(ج) اس کے قلم نے ایک جہان سے لڑائی باندھ رکھی ہے۔', '(ج) د هغه قلم له یوې نړۍ سره جګړه تړلې.'),
    ('(d) But four humble ones and a fifth crowned one were with him.', '(د) لیکن چار خاکسار اور پانچواں فاصلہ تاجدار ان کے ساتھ تھے۔', '(د) خو څلور عاجزان او پنځم تاجدار ورسره وو.'),
    ('(e) A dandy of Lucknow followed behind abusing him.', '(د) ایک لکھنؤ کے بانکے پیچھے پیچھے گالیاں دیتے تھے۔', '(ه) د لکهنو یو شوخ ځوان یې پسې کنځلې کولې.'),
])
e.p('2. About which kings or celebrities are the following sentences?', '۲۔ درج ذیل جملے کن بادشاہان یا مشاہیر کے بارے میں ہیں:؟', '۲. لاندې جملې د کومو پاچاهانو یا مشهورو کسانو په اړه دي؟')
e.group('lines', [
    ('(a) He from whose clothes comes the smell of blood is a butcher.', '(الف) جس کے کپڑوں میں لہو کی بُو آئے، وہ قصاب ہے۔', '(الف) د چا له جامو چې د وینې بوی راځي، هغه قصاب دی.'),
    ('(b) He made one round from this end to that and went away.', '(ب) اِس سرے سے اُس سرے تک ایک گردش کی اور چلے گئے۔', '(ب) له دې سره تر هغه سره یې یو ګرځ وکړ او لاړ.'),
    ('(c) His colour was pale and he hung his head in shame.', '(ج) رنگ زرد تھا اور شرم سے سر جھکائے تھا۔', '(ج) رنګ یې ژېړ و او له شرمه یې سر ټیټ کړی و.'),
    ('(d) His countenance was bright and his face appeared blooming with spiritual joy.', '(د) قیافہ روشن اور چہرہ فرحتِ روحانی سے شگفتہ نظر آتا تھا۔', '(د) څېره یې روښانه او مخ یې له روحاني خوښۍ غوړېدلی ښکارېده.'),
    ('(e) Many precious jewels of Hindustan were in his hand.', '(ہ) ہندوستان کے بہت سے گراں بہا زیور اس کے ہاتھ میں تھے۔', '(ه) د هندوستان ډېر قیمتي ګاڼې د هغه په لاس کې وې.'),
])
e.p('3. Write answers to the following questions.', '۳۔ درج ذیل سوالات کے جوابات لکھیں۔', '۳. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) How many kinds of lasting immortality has the author described? Explain.', '(الف) مصنف نے بقائے دوام کی کتنی قسمیں بتائی ہیں؟ وضاحت کریں۔', '(الف) لیکوال د تل‌پاتې کېدو څو ډولونه بیان کړي؟ تشریح یې کړئ.'),
    ('(b) Who in reality were the beautiful women?', '(ب) خوبصورت عورتیں درحقیقت کون تھیں؟', '(ب) ښکلې ښځې په حقیقت کې څوک وې؟'),
    ('(c) Why were the Iranian poets not allowed into the court?', '(ج) ایرانی شعرا کو دربار میں کیوں نہیں آنے دیا گیا؟', '(ج) ایراني شاعرانو ته ولې دربار ته د راتلو اجازه ورنه کړل شوه؟'),
    ('(d) What is meant by “In kingship there is no inheritance”?', '(د) ’’سلطنت میں میراث نہیں چلتی‘‘ سے کیا مراد ہے؟', '(د) له "په پاچاهۍ کې میراث نه چلېږي" څخه څه مراد دی؟'),
    ('(e) What did Shaikh Saadi say as he went out?', '(ہ) شیخ سعدی کیا کہتے ہوئے باہر چلے گئے؟', '(ه) شیخ سعدي څه وویل او بهر لاړ؟'),
])
ex = BOOK.record(e, 'urdu12-u5-exercise-1', 'Exercise (1)', 'مشق (۱)', 'تمرین (۱)', 27, [45])
issues = [{'id': 'urdu12-pdf027', 'unit': 5, 'printedPage': 45, 'description': 'Exercise Q1 prints two items lettered (د) (the fifth should be (ہ)); Q1(d) prints “پانچواں فاصلہ تاجدار” where the lesson text has “پانچواں تاجدار”; Q2(e) says the jewels were “in his hand” (text: some in hand, some on shoulder) — all retained as printed. Q2 ends “ہیں:؟”.'}]

if __name__ == '__main__':
    BOOK.save(27, [(5, tx), (5, ex)], issues=issues)
