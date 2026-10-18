"""PDF65 (printed 117–118): Unit 12 complex sentences (cont.), compound-complex sentences; C identification exercise 1–22 (unit end)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
for x in [
    ('If a sentence begins with a dependent clause, note the comma after this clause. If, on the other hand, the sentence begins with an independent clause, there is not a comma separating the two clauses.', 'اگر جملہ کسی تابع جملے سے شروع ہو تو اس جملے کے بعد کاما پر غور کریں۔ دوسری طرف اگر جملہ آزاد جملے سے شروع ہو تو دونوں جملوں کو الگ کرنے والا کاما نہیں ہوتا۔', 'که جمله په تابع جملې پیل شي، د دې جملې وروسته کامې ته پام وکړئ. له بلې خوا که جمله په خپلواکې جملې پیل شي، دواړه جملې بېلوونکې کامه نه وي.'),
    ('Here are a few examples:', 'یہاں چند مثالیں ہیں:', 'دلته څو بېلګې دي:'),
]: w.p(*x)
w.group('lines', [
    ('Although she completed her literature review, she still needed to work on her methods section.', 'اگرچہ اس نے اپنا ادبی جائزہ مکمل کر لیا، پھر بھی اسے اپنے طریقۂ کار والے حصے پر کام کرنا تھا۔', 'که څه هم هغې خپله ادبي بیاکتنه بشپړه کړه، لا یې هم د میتود په برخه کار ته اړتیا درلوده.'),
    ('Note the comma in this sentence because it begins with a dependent clause.', 'اس جملے میں کاما پر غور کریں کیونکہ یہ تابع جملے سے شروع ہوتا ہے۔', 'په دې جمله کې کامې ته پام وکړئ ځکه په تابع جملې پیل کېږي.'),
    ('Because he organized his sources by theme, it was easier for his readers to follow.', 'چونکہ اس نے اپنے ماخذ موضوع کے لحاظ سے ترتیب دیے، اس کے قارئین کے لیے سمجھنا آسان تھا۔', 'څرنګه چې هغه خپلې سرچینې د موضوع له مخې تنظیم کړې، د هغه لوستونکو ته تعقیبول اسانه وو.'),
    ('Note the comma in this sentence because it begins with a dependent clause.', 'اس جملے میں کاما پر غور کریں کیونکہ یہ تابع جملے سے شروع ہوتا ہے۔', 'په دې جمله کې کامې ته پام وکړئ ځکه په تابع جملې پیل کېږي.'),
    ('They studied APA rules for many hours as they were so interesting.', 'انہوں نے کئی گھنٹے اے پی اے کے قواعد پڑھے کیونکہ وہ بہت دلچسپ تھے۔', 'هغوی ډېر ساعتونه د APA قواعد ولوستل ځکه ډېر زړه‌راښکونکي وو.'),
    ('Note that there is no comma in this sentence because it begins with an independent clause.', 'نوٹ کریں کہ اس جملے میں کاما نہیں کیونکہ یہ آزاد جملے سے شروع ہوتا ہے۔', 'پام وکړئ چې په دې جمله کې کامه نشته ځکه په خپلواکې جملې پیل کېږي.'),
])
w.p('Using some complex sentences in writing allows for more sentence variety.', 'تحریر میں کچھ پیچیدہ جملے استعمال کرنے سے جملوں میں زیادہ تنوع آتا ہے۔', 'په لیکنه کې د ځینو پېچلو جملو کارول د جملو ډېر تنوع رامنځته کوي.')
w.h('4. Compound-Complex Sentences', '4. مرکب پیچیدہ جملے', '4. مرکبې-پېچلې جملې')
w.p('Sentence types can also be combined. A compound-complex sentence contains at least two independent clauses and at least one dependent clause.', 'جملوں کی اقسام کو یکجا بھی کیا جا سکتا ہے۔ مرکب پیچیدہ جملے میں کم از کم دو آزاد جملے اور کم از کم ایک تابع جملہ ہوتا ہے۔', 'د جملو ډولونه یوځای کېدای هم شي. مرکبه-پېچلې جمله لږ تر لږه دوه خپلواکې جملې او لږ تر لږه یوه تابع جمله لري.')
w.group('lines', [
    ('She completed her literature review, but she still needs to work on her methods section even though she finished her methods course last semester.', 'اس نے اپنا ادبی جائزہ مکمل کر لیا، لیکن اسے اب بھی اپنے طریقۂ کار والے حصے پر کام کرنا ہے حالانکہ اس نے پچھلے سمسٹر میں اپنا طریقۂ کار کا کورس مکمل کر لیا تھا۔', 'هغې خپله ادبي بیاکتنه بشپړه کړه، خو لا هم باید د میتود په برخه کار وکړي که څه هم تېر سمسټر یې د میتود کورس پای ته رسولی و.'),
    ('Although he organized his sources by theme, he decided to arrange them chronologically, and he carefully followed the MEAL plan for organization.', 'اگرچہ اس نے اپنے ماخذ موضوع کے لحاظ سے ترتیب دیے، اس نے انہیں زمانی ترتیب سے رکھنے کا فیصلہ کیا، اور اس نے تنظیم کے لیے MEAL منصوبے پر احتیاط سے عمل کیا۔', 'که څه هم هغه خپلې سرچینې د موضوع له مخې تنظیم کړې، پرېکړه یې وکړه چې د وخت په ترتیب یې کېږدي، او د تنظیم لپاره یې په پام سره د MEAL پلان تعقیب کړ.'),
    ('With pizza and soda at hand, they studied APA rules for many hours, and they decided that writing in APA made sense because it was clear, concise, and objective.', 'پیزا اور سوڈا ہاتھ میں لیے انہوں نے کئی گھنٹے اے پی اے کے قواعد پڑھے، اور انہوں نے فیصلہ کیا کہ اے پی اے میں لکھنا معقول ہے کیونکہ یہ واضح، مختصر اور معروضی ہے۔', 'د پیزا او سوډا سره، هغوی ډېر ساعتونه د APA قواعد ولوستل، او پرېکړه یې وکړه چې په APA کې لیکل معقول دي ځکه روښانه، لنډ او بې‌طرفه دي.'),
])
w.p('Using some complex-compound sentences in writing allows for more sentence variety. Pay close attention to comma usage in complex-compound sentences so that the reader is easily able to follow the intended meaning.', 'تحریر میں کچھ پیچیدہ مرکب جملے استعمال کرنے سے جملوں میں زیادہ تنوع آتا ہے۔ پیچیدہ مرکب جملوں میں کاما کے استعمال پر خاص توجہ دیں تاکہ قاری آسانی سے مطلوبہ معنی سمجھ سکے۔', 'په لیکنه کې د ځینو پېچلو-مرکبو جملو کارول د جملو ډېر تنوع رامنځته کوي. په پېچلو-مرکبو جملو کې د کامې کارونې ته ډېر پام وکړئ ترڅو لوستونکی په اسانۍ مطلوبه مانا تعقیب کړي.')
w.p('C. State whether the following sentences are simple, complex or compound.', 'C. بتائیں کہ درج ذیل جملے سادہ، پیچیدہ یا مرکب ہیں۔', 'C. ووایاست چې لاندې جملې ساده، پېچلې یا مرکبې دي.')
S = ['We met rather few people who spoke English.', 'I have been on rather too many planes and trains recently.', 'We drove right up to Karachi in two days.', "I don't care how expensive it is.",
     'Two minutes ago the child was fast asleep, but now he is wide awake.', 'He is not tall enough to be a soldier.', "I guess she just doesn't respect you.", 'I have got four sisters and each of them is quite different from the others.',
     'You can either come with me now or walk home.', "He will never leave home because he hasn't got the courage to.", 'When all else fails, read the user manual.', 'It was Saeed who paid for the drinks.',
     "We have to go to bed when the clock chimes ten o'clock.", "Arshad liked Salman's friend, and he also liked his cousin.", 'The big brown dog ran after the blue and red ball.', 'Zakariyya and Essa Khan rode their bicycles after they ate lunch.',
     'The teacher and the principal met in the hall near the library.', 'Many brave soldiers fought in the war, and they received medals.', 'The drummers played a long time, but the piano players stopped early.', 'Before the queen rode in the parade, she gave a speech.',
     'After midnight the ghosts will come out of the haunted attic.', 'She dropped the pan and the plate, but she held on to the spoon.']
w.group('lines', [(f'{i}. {s}',) * 3 for i, s in enumerate(S, 1)])
for p in w.paras[-len(S):]: p['untranslatedByDesign'] = True
rec = BOOK.record(w, 'eng12-u12-vocab-b', 'Sentence structure (2): complex, compound-complex; exercise C', 'جملے کی ساخت (2): پیچیدہ، مرکب پیچیدہ؛ مشق C', 'د جملې جوړښت (2): پېچلې، مرکبې-پېچلې؛ تمرین C', 65, [117, 118])
issues = [{'id': 'eng12-p117-118', 'unit': 12, 'printedPage': 117, 'description': 'Exercise C sentences are grammar items shown in English in all views. The text names the “MEAL plan” without defining it; printed as is.'}]

if __name__ == '__main__':
    BOOK.save(65, [(12, rec)], issues=issues, complete_units=[12])
