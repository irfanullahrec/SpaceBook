"""Urdu XII PDF43 (spread): printed pp.76–77 — Lesson 8 مشق Q1–Q6. Completes Lesson 8."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write short answers to the following questions:', '1. مندرجہ ذیل سوالات کے مختصر جوابات لکھیں:', '1. لاندې پوښتنو ته لنډ ځوابونه ولیکئ:')
e.group('lines', [
    ('i. People of what ages were among the clerks?', 'i. کلرکوں میں کس عمر کے لوگ شامل تھے؟', 'i. په کلرکانو کې د کوم عمر خلک شامل وو؟'),
    ('ii. Why did Sharif Husain set off that day towards the Jama Masjid instead of home?', 'ii. شریف حسین اس دن گھر کے بجائے جامع مسجد کی طرف کیوں چل پڑا؟', 'ii. شریف حسین هغه ورځ د کور پر ځای جامع جومات ته ولې روان شو؟'),
    ('iii. What use did Sharif Husain think of for the piece of marble?', 'iii. شریف حسین نے سنگِ مرمر کے ٹکڑے کا کیا مصرف سوچا؟', 'iii. شریف حسین د مرمر د ټوټې لپاره کومه ګټه وسنجوله؟'),
    ('iv. What did Sharif Husain feel on seeing his name carved on the piece of marble?', 'iv. سنگِ مرمر کے ٹکڑے پر اپنا نام کھدا ہوا دیکھ کر شریف حسین نے کیا محسوس کیا؟', 'iv. د مرمر پر ټوټه د خپل نوم په لیدو شریف حسین څه احساس کړل؟'),
    ('v. What moral lesson is learnt from this story?', 'v. اس افسانے سے کیا اخلاقی سبق حاصل ہوتا ہے؟', 'v. له دې افسانې څه اخلاقي درس ترلاسه کېږي؟'),
])
e.p('2. With reference to the lesson, explain the following sentences:', '2. سبق کے حوالے سے مندرجہ ذیل جملوں کی وضاحت کریں:', '2. د لوست په حواله لاندې جملې تشریح کړئ:')
e.group('lines', [
    ('i. By day the bustle of this area is generally confined within the four walls of the rooms.', 'i. دن کے وقت اس علاقے کی چہل پہل اور گہما گہمی عموماً کمروں کی چار دیواری ہی میں محدود رہتی ہے۔', 'i. د ورځې د دې سیمې ګڼه ګوڼه معمولاً د کوټو په څلورو دیوالونو کې محدوده وي.'),
    ('ii. All the things in the world and people of every manner and sort were found here.', 'ii. دنیا بھر کی چیزیں اور ہر وضع اور ہر قماش کے لوگ یہاں ملتے تھے۔', 'ii. د نړۍ هر شی او د هر ډول او هر طبیعت خلک دلته پیدا کېدل.'),
    ('iii. He is most Forgiving and Merciful — who knows, his days may change.', 'iii. وہ بڑا غفور الرحیم ہے کیا عجب اس کے دن پھر جائیں۔', 'iii. هغه ډېر بښونکی او مهربان دی — څه عجب چې ورځې یې واوړي.'),
    ('iv. Whenever a colleague in the office sought his guidance in some matter, his eyes shone with a sense of his superiority.', 'iv. دفتر میں جب کبھی اس کا کوئی ساتھی کسی معاملے میں اس کی رہنمائی کا جویا ہوتا تو اپنی برتری کے احساس سے اس کی آنکھیں چمک اٹھتیں۔', 'iv. په دفتر کې به چې کله کوم ملګري په کومه مسله کې د هغه لارښوونه غوښته، د خپلې لوړتیا له احساسه به یې سترګې وځلېدې.'),
    ('v. Promotion comes by unseen grace; nothing will be gained by enduring hard toil and wearing oneself out.', 'v. ترقی لطیفۂ غیبی سے نصیب ہوتی ہے، کڑی محنت جھیلنے اور جان کھپانے سے کچھ حاصل نہ ہوگا۔', 'v. ترفیع په غیبي بخت کېږي؛ د سخت زیار او ځان ستړي کولو څخه به هیڅ ترلاسه نه شي.'),
])
e.p('3. To complete the following sentences, put (✓) against the correct answer from those given.', '3. مندرجہ ذیل جملوں کی تکمیل کے لیے دیے ہوئے جوابات میں سے درست جواب کے سامنے (✓) کا نشان لگائیں۔', '3. د لاندې جملو د بشپړولو لپاره له ورکړل شویو ځوابونو د سم ځواب مخې ته (✓) نښه کېږدئ.')
M = [
    ('i. Sharif Husain got the piece of marble ________', 'i. شریف حسین کو سنگِ مرمر کا ٹکڑا ________', 'i. شریف حسین ته د مرمر ټوټه ________',
     [('a. by inheritance', 'ا۔ وراثت میں ملا', 'ا. په میراث کې ورکړل شوه'), ('b. lying on the road', 'ب۔ راستے میں پڑا ہوا ملا', 'ب. په لاره کې پرته وموندل شوه'), ('c. as a gift from a friend', 'ج۔ کسی دوست کی طرف سے تحفے میں ملا', 'ج. د یو ملګري له خوا ډالۍ شوه'), ('d. from a junk shop', 'د۔ کباڑی کی دکان سے ملا', 'د. د کباړي له دوکانه وموندل شوه')]),
    ('ii. Sharif Husain bought the piece of marble because ________', 'ii. شریف حسین نے سنگِ مرمر کا ٹکڑا اس لیے خریدا کہ ________', 'ii. شریف حسین د مرمر ټوټه ځکه واخیسته چې ________',
     [('a. his wife had asked for it', 'ا۔ اس کی بیوی نے فرمائش کی تھی', 'ا. مېرمن یې غوښتې وه'), ('b. its price was very low', 'ب۔ اس کی قیمت بہت کم تھی', 'ب. بیه یې ډېره ټیټه وه'), ('c. he wanted to have it fixed on the door of his house', 'ج۔ وہ اسے اپنے گھر کے دروازے پر نصب کرانا چاہتا تھا', 'ج. غوښتل یې د خپل کور په دروازه یې ولګوي'), ('d. on asking the price, the junk-dealer pursued him', 'د۔ قیمت پوچھنے پر کباڑی اس کے پیچھے پڑ گیا تھا', 'د. د بیې په پوښتلو کباړي پسې ونښت')]),
    ('iii. In Sharif Husain’s mind the use of the marble was that ________', 'iii. شریف حسین کے خیال میں سنگِ مرمر کا مصرف یہ تھا کہ ________', 'iii. د شریف حسین په فکر د مرمر ګټه دا وه چې ________',
     [('a. it should be presented to an officer as a gift', 'ا۔ اسے افسر کو تحفے کے طور پر دے دیا جائے', 'ا. افسر ته د ډالۍ په توګه ورکړل شي'), ('b. it should be displayed on the cornice', 'ب۔ اسے کارنس پر سجا دیا جائے', 'ب. پر طاق (کارنس) کېښودل شي'), ('c. his name should be carved on it and it should be fixed on the door of his house', 'ج۔ اس پر اپنا نام کھدوا کر مکان کے دروازے پر لگا دیا جائے', 'ج. خپل نوم پرې وکندي او د کور په دروازه یې ولګوي'), ('d. it should be put on the study table', 'د۔ اسے مطالعے کی میز پر رکھ دیا جائے', 'د. د مطالعې پر مېز کېښودل شي')]),
    ('iv. After Sharif Husain’s death the piece of marble ________', 'iv. شریف حسین کی موت کے بعد سنگِ مرمر کا ٹکڑا ________', 'iv. د شریف حسین له مړینې وروسته د مرمر ټوټه ________',
     [('a. lay in the house just like that', 'ا۔ یونہی گھر میں پڑا رہا', 'ا. همداسې په کور کې پرته وه'), ('b. got lost somewhere', 'ب۔ کہیں گم ہو گیا', 'ب. چېرته ورکه شوه'), ('c. was sold', 'ج۔ بیچ دیا گیا', 'ج. وپلورل شوه'), ('d. was fixed on his grave', 'د۔ اس کی قبر پر لگا دیا گیا', 'د. د هغه پر قبر ولګول شوه')]),
]
for q, qu, qp, opts in M:
    e.p(q, qu, qp)
    e.group('lines', opts)
e.group('lines', [
    ('4. Write the summary of “Kutba”.', '4. ’’کتبہ‘‘ کا خلاصہ لکھیں۔', '4. د "کتبې" لنډیز ولیکئ.'),
    ('5. Write a biographical and critical note on Ghulam Abbas.', '5. غلام عباس پر سوانحی و تنقیدی نوٹ لکھیں۔', '5. د غلام عباس په اړه ژوندلیکي او نقدي یادښت ولیکئ.'),
    ('6. Use the following words and phrases in sentences of your own:', '6. مندرجہ ذیل الفاظ و تراکیب کو اپنے جملوں میں استعمال کریں:', '6. لاندې کلمې او ترکیبونه په خپلو جملو کې وکاروئ:'),
])
e.p('mustaqbil (future), maʿmūl (routine), asāsa (belongings), adnā-o-aʿlā (low and high), be-maṣraf (useless)', 'مستقبل، معمول، اثاثہ، ادنیٰ و اعلیٰ، بے مصرف۔', 'مستقبل (راتلونکی)، معمول (عادت)، اثاثه (شتمني)، ادنی او اعلی (ټیټ او لوړ)، بې‌مصرف (بې‌ګټې)')
ex = BOOK.record(e, 'urdu12-u8-exercise', 'Exercise', 'مشق', 'تمرین', 43, [76, 77])
issues = [{'id': 'urdu12-pdf043', 'unit': 8, 'printedPage': 76, 'description': 'Exercise is board-written and transcribed in full; Q2 quotes single sentences from the story (short quotations for study). Q1 numbering uses Latin digits and Roman numerals as printed.'}]

if __name__ == '__main__':
    BOOK.save(43, [(8, ex)], issues=issues, complete_units=[8])
