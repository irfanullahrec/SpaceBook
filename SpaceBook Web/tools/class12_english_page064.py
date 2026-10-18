"""PDF64 (printed 115–116): Unit 12 Oral; Vocabulary A word-meaning MCQ table; B second conditional 1–13; Sentence Structure — simple, compound, complex (start)."""
from class12_book_common import Book, Builder

BOOK = Book('english')
w = Builder()
w.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
w.p('Invite the students to select a stage role of their own choice and share its characteristics/traits as he observed with their peer.', 'طلبہ کو دعوت دیں کہ وہ اپنی پسند کا اسٹیج کا کوئی کردار منتخب کریں اور اپنے ساتھیوں کے ساتھ اس کی خصوصیات/عادات بیان کریں جیسا کہ انہوں نے مشاہدہ کیا۔', 'زده کوونکي وهڅوئ چې د خپلې خوښې د سټېج یو رول وټاکي او د هغه ځانګړنې/خویونه لکه څنګه چې یې لیدلي، له خپلو ملګرو سره شریک کړي.')
w.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
w.p('A. Following words have been taken from the above poem. Circle the word that closely matches the relevant word.', 'A. درج ذیل الفاظ مندرجہ بالا نظم سے لیے گئے ہیں۔ اس لفظ کے گرد دائرہ لگائیں جو متعلقہ لفظ سے سب سے زیادہ مطابقت رکھتا ہو۔', 'A. لاندې کلمې له پورتني شعر څخه اخیستل شوې. هغه کلمه په کړۍ کې ونیسئ چې له اړوندې کلمې سره تر ټولو ډېره سمون لري.')
MC = [['Mewling', 'a. sleeping', 'b. reading', 'c. talking', 'd. crying'], ['Satchel', 'a. table', 'b. bag for books', 'c. lemon', 'd. wide road'], ['Woeful', 'a. sad', 'b. dancing', 'c. intelligent', 'd. awesome'],
      ['Pard', 'a. barber', 'b. teacup', 'c. leopard', 'd. spoon'], ['Capon', 'a. fur', 'b. fat chicken', 'c. ribbons', 'd. bench'], ['Saws', 'a. sayings', 'b. tools', 'c. monkeys', 'd. cities'],
      ['Instances', 'a. technology', 'b. judgements', 'c. dress', 'd. ships'], ['Pantaloon', 'a. pants', 'b. bed', 'c. hot air balloon', 'd. thick book'], ['Shank', 'a. head', 'b. family', 'c. income', 'd. legs'],
      ['Treble', 'a. terrors', 'b. games', 'c. high pitched sound', 'd. musical instrument'], ['Oblivion', 'a. immortality', 'b- joy', 'c. wisdom', 'd. forgetfulness'], ['Sans', 'a. false', 'b. yellow', 'c. without', 'd. full of']]
w.table('eng12-u12-word-mcq', ['Word', 'a', 'b', 'c', 'd'], MC, ['لفظ', 'a', 'b', 'c', 'd'], ['کلمه', 'a', 'b', 'c', 'd'], MC, MC)
w.p('B. Complete with the Second Conditional', 'B. دوسرے شرطیہ کے ساتھ مکمل کریں', 'B. د دویم شرطي سره بشپړ کړئ')
SC = ['If we ____ (be) in Lahore today, we ____ (be) able to go to the concert in Shalimar Bagh.', 'If I ____ (have) million dollars, I ____ (give) a lot to charity.', 'If I ____ (win) the lottery, I ____ (buy) a big house.',
      'If my sister ____ (have) a degree, she ____ (love) working on animal conservation.', 'My parents ____ (not/drive), if public transport ____ (be) reliable.', 'If I ____ (be) you, I ____ (not/ ride) a motorcycle.',
      'If they ____ (tell) their father, he ____ (be) very angry.', 'She ____ (spend) a year in the USA if it ____ (be) easier to get a green card.', 'We ____ (help) you if we ____ (know) how.',
      'If I ____ (feel) better, I ____ (can) go to the cinema with you.', 'If you ____ (go) by bike more often, you ____ (not/ be) so flabby.', 'She ____ (not / call) you if she ____ (not/want).']
NUMS = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
w.group('lines', [(f'{n}. {s}',) * 3 for n, s in zip(NUMS, SC)])
for p in w.paras[-len(SC):]: p['untranslatedByDesign'] = True
w.h('Sentence Structure', 'جملے کی ساخت', 'د جملې جوړښت')
w.p('On the basis of Structure, there are four types of sentences.', 'ساخت کی بنیاد پر جملوں کی چار اقسام ہیں۔', 'د جوړښت پر بنسټ د جملو څلور ډولونه دي.')
w.h('1. Simple Sentences', '1. سادہ جملے', '1. ساده جملې')
w.p('A simple sentence contains a subject and a verb, and it may also have an object and modifiers. However, it contains only one independent clause.', 'سادہ جملے میں ایک فاعل اور ایک فعل ہوتا ہے، اور اس میں مفعول اور توصیفی الفاظ بھی ہو سکتے ہیں۔ تاہم اس میں صرف ایک آزاد جملہ (کلاز) ہوتا ہے۔', 'ساده جمله یو فاعل او یو فعل لري، او کېدای شي مفعول او صفتي کلمې هم ولري. خو یوازې یوه خپلواکه جمله (کلاز) لري.')
w.p('Here are a few examples:', 'یہاں چند مثالیں ہیں:', 'دلته څو بېلګې دي:')
w.group('lines', [('She wrote.', 'اس نے لکھا۔', 'هغې ولیکل.'), ('She completed her project on time.', 'اس نے اپنا منصوبہ وقت پر مکمل کیا۔', 'هغې خپله پروژه پر وخت بشپړه کړه.'),
                  ('He organized his sources by theme.', 'اس نے اپنے ماخذ موضوع کے لحاظ سے ترتیب دیے۔', 'هغه خپلې سرچینې د موضوع له مخې تنظیم کړې.'), ('They studied for many hours.', 'انہوں نے کئی گھنٹے پڑھائی کی۔', 'هغوی ډېر ساعتونه زده کړه وکړه.')])
w.h('2. Compound Sentences', '2. مرکب جملے', '2. مرکبې جملې')
w.p('A compound sentence contains at least two independent clauses. These two independent clauses can be combined with a comma and a coordinating conjunction or with a semicolon.', 'مرکب جملے میں کم از کم دو آزاد جملے ہوتے ہیں۔ یہ دو آزاد جملے کاما اور ایک عطفی حرف یا سیمی کولن کے ذریعے جوڑے جا سکتے ہیں۔', 'مرکبه جمله لږ تر لږه دوه خپلواکې جملې لري. دا دوه خپلواکې جملې د کامې او یوه عطفي توري یا سیمي‌کولن په واسطه سره یوځای کېدای شي.')
w.p('Here are a few examples:', 'یہاں چند مثالیں ہیں:', 'دلته څو بېلګې دي:')
w.group('lines', [('She completed her literature review, and she created her reference list.', 'اس نے اپنا ادبی جائزہ مکمل کیا، اور اس نے اپنے حوالوں کی فہرست بنائی۔', 'هغې خپله ادبي بیاکتنه بشپړه کړه، او د سرچینو لست یې جوړ کړ.'),
                  ('He organized his sources by theme; then, he updated his reference list.', 'اس نے اپنے ماخذ موضوع کے لحاظ سے ترتیب دیے؛ پھر اس نے اپنی حوالوں کی فہرست کو تازہ کیا۔', 'هغه خپلې سرچینې د موضوع له مخې تنظیم کړې؛ بیا یې د سرچینو لست تازه کړ.'),
                  ('They studied for many hours, but they realized there was still much to learn.', 'انہوں نے کئی گھنٹے پڑھائی کی، لیکن انہیں احساس ہوا کہ ابھی بہت کچھ سیکھنا باقی ہے۔', 'هغوی ډېر ساعتونه زده کړه وکړه، خو پوه شول چې لا ډېر څه د زده کړې پاتې دي.')])
w.h('3. Complex Sentences', '3. پیچیدہ جملے', '3. پېچلې جملې')
w.p('A complex sentence contains at least one independent clause and at least one dependent clause. Dependent clauses can refer to the subject (who, which) the sequence/time (since, while), or the causal elements (because, if) of the independent clause.', 'پیچیدہ جملے میں کم از کم ایک آزاد جملہ اور کم از کم ایک تابع جملہ ہوتا ہے۔ تابع جملے آزاد جملے کے فاعل (who, which)، ترتیب/وقت (since, while) یا سببی عناصر (because, if) کی طرف اشارہ کر سکتے ہیں۔', 'پېچلې جمله لږ تر لږه یوه خپلواکه جمله او لږ تر لږه یوه تابع جمله لري. تابع جملې کولی شي د خپلواکې جملې فاعل (who, which)، ترتیب/وخت (since, while) یا لاملي عناصرو (because, if) ته اشاره وکړي.')
rec = BOOK.record(w, 'eng12-u12-vocab-a', 'Oral; Vocabulary A (word meanings), B second conditional; Sentence structure (1)', 'زبانی ابلاغ؛ ذخیرۂ الفاظ A، B دوسرا شرطیہ؛ جملے کی ساخت (1)', 'د خولې اړیکه؛ لغات A، B دویم شرطي؛ د جملې جوړښت (1)', 64, [115, 116])
issues = [{'id': 'eng12-p115-116', 'unit': 12, 'printedPage': 115, 'description': 'Printed numbering retained: exercise B skips item 5 (1, 2, 3, 4, 6, 7 … 13). Also retained: oral task “as he observed with their peer”, option “b- joy”, “On the basis of Structure, there are four types of sentences” (only three are described before compound-complex).'}]

if __name__ == '__main__':
    BOOK.save(64, [(12, rec)], issues=issues)
