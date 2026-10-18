"""PDF69 (printed 125–126): Unit 13 Glossary (obsessed … vocational); Reading Comprehension Q1–5; Writing; Oral; Vocabulary A connotation exercise 1–7."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
B = '________'
g = Builder()
gloss(g, 'eng12-u13-gloss-b', [
    ('obsessed(v)', 'to completely fill your mind so that you cannot think of anything else, in a way that is not normal', 'آپ کے ذہن پر اس طرح چھا جانا کہ آپ کچھ اور نہ سوچ سکیں، غیر معمولی انداز میں', 'ستاسو ذهن په داسې ډول ډکول چې نور څه فکر ونه کړای شئ، په غیرعادي ډول'),
    ('oriented(v)', 'to direct somebody/something towards something; to make or adapt somebody/something for a particular purpose', 'کسی کو/کسی چیز کو کسی چیز کی طرف موڑنا؛ کسی خاص مقصد کے لیے بنانا یا ڈھالنا', 'یو څوک/یو شی یو شي ته اړول؛ د یوې ځانګړې موخې لپاره جوړول یا برابرول'),
    ('prompt(v)', 'to make somebody decide to do something; to cause something to happen', 'کسی کو کچھ کرنے کا فیصلہ کرنے پر آمادہ کرنا؛ کسی چیز کے ہونے کا سبب بننا', 'یو څوک یو کار کولو ته هڅول؛ د یو شي د پېښېدو لامل کېدل'),
    ('subsidise(v)', 'to give money to somebody or an organization to help pay for something; to give a subsidy', 'کسی شخص یا ادارے کو کسی چیز کی ادائیگی میں مدد کے لیے رقم دینا؛ سبسڈی دینا', 'یو چا یا سازمان ته د یو شي د لګښت په ورکولو کې د مرستې لپاره پیسې ورکول؛ سبسایډي ورکول'),
    ('sustainable(adj.)', 'that can continue or be continued for a long time', 'جو طویل عرصے تک جاری رہ سکے یا رکھا جا سکے', 'چې د اوږد وخت لپاره دوام ومومي یا وساتل شي'),
    ('tattered(adj.)', 'old and torn; in bad condition', 'پرانا اور پھٹا ہوا؛ خراب حالت میں', 'زوړ او شلېدلی؛ په بد حالت کې'),
    ('technical(adj.)', 'connected with the practical use of machines, methods, etc. in science and industry', 'سائنس اور صنعت میں مشینوں، طریقوں وغیرہ کے عملی استعمال سے متعلق', 'په ساینس او صنعت کې د ماشینونو، طریقو او نورو له عملي کارونې سره تړلی'),
    ('tertiary(n)', 'to give money to somebody or an organization to help pay for something; to give a subsidy', 'کسی شخص یا ادارے کو کسی چیز کی ادائیگی میں مدد کے لیے رقم دینا؛ سبسڈی دینا', 'یو چا یا سازمان ته د یو شي د لګښت په ورکولو کې د مرستې لپاره پیسې ورکول؛ سبسایډي ورکول'),
    ('vocational(adj.)', 'connected with the skills, knowledge, etc. that you need to have in order to do a particular job', 'ان مہارتوں، علم وغیرہ سے متعلق جو کسی خاص کام کو کرنے کے لیے درکار ہوں', 'له هغو مهارتونو، پوهې او نورو سره تړلی چې د یوې ځانګړې دندې د ترسره کولو لپاره اړین دي'),
])
gl = BOOK.record(g, 'eng12-u13-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 69, [125])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. Why do we need more technical education than general education in Pakistan?', '1. پاکستان میں ہمیں عمومی تعلیم سے زیادہ فنی تعلیم کی ضرورت کیوں ہے؟', '1. په پاکستان کې موږ ولې له عمومي زده کړې ډېرې تخنیکي زده کړې ته اړتیا لرو؟'),
    ('2. How did technical education help Japan and Germany recover their economy after World War II?', '2. فنی تعلیم نے دوسری جنگِ عظیم کے بعد جاپان اور جرمنی کی معیشت کی بحالی میں کیسے مدد کی؟', '2. تخنیکي زده کړې له دویمې نړیوالې جګړې وروسته د جاپان او جرمني د اقتصاد په بیا رغونه کې څنګه مرسته وکړه؟'),
    ('3. Why is a linkage between the industries and the technical education training centres necessary?', '3. صنعتوں اور فنی تعلیم کے تربیتی مراکز کے درمیان ربط کیوں ضروری ہے؟', '3. د صنعتونو او د تخنیکي زده کړې د روزنیزو مرکزونو ترمنځ اړیکه ولې اړینه ده؟'),
    ('4. What measures do you suggest for improving the technical education structure of Pakistan?', '4. پاکستان کے فنی تعلیم کے ڈھانچے کو بہتر بنانے کے لیے آپ کیا اقدامات تجویز کرتے ہیں؟', '4. د پاکستان د تخنیکي زده کړې د جوړښت د ښه کولو لپاره کوم اقدامات وړاندیز کوئ؟'),
    ('5. How can technical education help in strengthening the economy of Pakistan?', '5. فنی تعلیم پاکستان کی معیشت کو مضبوط بنانے میں کیسے مدد کر سکتی ہے؟', '5. تخنیکي زده کړه د پاکستان د اقتصاد په پیاوړتیا کې څنګه مرسته کولی شي؟'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p("Write an argumentative essay on 'Need for Technical Education in Our Country' by stating and opinion about the topic and list ideas that sport opinion.", 'موضوع کے بارے میں رائے بیان کر کے اور اس رائے کی تائید کرنے والے خیالات کی فہرست بنا کر ’’ہمارے ملک میں فنی تعلیم کی ضرورت‘‘ پر ایک استدلالی مضمون لکھیں۔', 'په موضوع د نظر په بیانولو او د هغه نظر د ملاتړ نظرونو په لست کولو د "زموږ په هېواد کې د تخنیکي زده کړې اړتیا" په اړه یوه استدلالي مقاله ولیکئ.')
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p('Pakistan needs skilled manpower through technical education for development, while everyone here wants to become an officer by getting general education. This trend must change. Make groups and Discuss.', 'پاکستان کو ترقی کے لیے فنی تعلیم کے ذریعے ہنرمند افرادی قوت کی ضرورت ہے، جبکہ یہاں ہر کوئی عمومی تعلیم حاصل کر کے افسر بننا چاہتا ہے۔ یہ رجحان بدلنا چاہیے۔ گروہ بنائیں اور بحث کریں۔', 'پاکستان د پرمختګ لپاره د تخنیکي زده کړې له لارې ماهر بشري ځواک ته اړتیا لري، په داسې حال کې چې دلته هر څوک غواړي د عمومي زده کړې په ترلاسه کولو افسر شي. دا رجحان باید بدل شي. ډلې جوړې کړئ او بحث وکړئ.')
q.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
q.p('A. Following are some words related to economics. Place each word in the given blanks that best define this word.', 'A. معاشیات سے متعلق کچھ الفاظ درج ذیل ہیں۔ ہر لفظ کو دی گئی خالی جگہوں میں اس طرح رکھیں کہ وہ اس کی بہترین تعریف کرے۔', 'A. لاندې له اقتصاد سره تړلې ځینې کلمې دي. هره کلمه په ورکړل شویو تشو ځایونو کې داسې کېږدئ چې تر ټولو ښه یې تعریف وکړي.')
CN = [
    ('1. client, customer', f'A {B} is someone who buys goods or services. A {B} receives professional services.'),
    ('2. career, job', f'A {B} is what someone does in exchange for money. A {B} is a professional trajectory that includes both past and present jobs.'),
    ('3. coworkers, colleagues', f'A {B} is someone who works on your team or for your company. A {B} is a professional who works in your industry, but not necessarily for the same company'),
    ('4. top-of-the-line, expensive, premium, overpriced', f'{B} simply means that something costs a lot. {B} means that something costs more than it should. {B} and {B} have a positive connotation and communicate that something is high quality.'),
    ('5. ordinary, standard, run-of-the-mill, , familiar, well-known, common', f'{B} and {B} have a neutral connotation. {B} and {B} have more of a negative connotation. {B} and {B} have a positive connotation.'),
    ('6. rich, well-off, well-to-do, wealthy', f'{B} is direct term that we often try to avoid. {B} is a more polite way to communicate that someone has a lot of money. {B} and {B} are euphemistic, indirect ways to communicate that someone has a lot of money.'),
    ('7. approach, method, Strategy, scheme, , plot,', f'{B} and {B} have a negative connotation. {B} and {B} sound more positive.'),
]
for head, body in CN:
    q.p(head, head, head); q.paras[-1]['untranslatedByDesign'] = True
    q.p(body, body, body); q.paras[-1]['untranslatedByDesign'] = True
qs = BOOK.record(q, 'eng12-u13-comprehension', 'Reading Comprehension; Writing; Oral; Vocabulary A (connotation)', 'مطالعہ اور فہم؛ تحریر؛ زبانی ابلاغ؛ ذخیرۂ الفاظ A (ضمنی معنی)', 'لوستل او پوهه؛ لیکنه؛ د خولې اړیکه؛ لغات A (ضمني مانا)', 69, [125, 126])
issues = [{'id': 'eng12-p125-126', 'unit': 13, 'printedPage': 125, 'description': 'Printed text retained: glossary “tertiary(n)” is given the meaning of “subsidise” (duplicated definition); writing task “by stating and opinion … list ideas that sport opinion”; word lists with doubled commas (“run-of-the-mill, , familiar”, “scheme, , plot,”). Connotation exercise items are vocabulary drills kept in English in all views.'}]

if __name__ == '__main__':
    BOOK.save(69, [(13, gl), (13, qs)], issues=issues)
