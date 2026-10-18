"""Urdu XII PDF31 (spread): printed pp.52–53 — Lesson 6 summary end (source پگڈنڈی سے روڈ رولر تک) and مشق Q1–Q5. Completes Lesson 6."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
s = Builder()
for x in [
    ('(continuing) …but a whole, fully kneaded, complete thing with a personality, character and pace of its own.',
     '(جاری) …بلکہ بجائے خود ایک پوری طرح گندھی ہوئی، بھرپور شے ہے جس کی اپنی شخصیت، اپنا کردار اور اپنی رفتار ہے۔',
     '(دوام) …بلکې پخپله یو بشپړ اغږل شوی، ډک شی دی چې خپل شخصیت، خپل کردار او خپله چټکتیا لري.'),
    ('After about two hours he asks the driver to let him down; the driver offers to take him home on the roller, but he thanks him and says he must get home a little quickly, and walks off briskly. Yet he is now a different person: the road roller is no longer just a limb of existence but a self-governing, evergreen, beating and breathing manifestation of “presence”.',
     'تقریباً دو گھنٹے بعد وہ ڈرائیور سے کہتا ہے کہ اب اسے اتار دے؛ ڈرائیور روڈ رولر پر گھر چھوڑنے کی پیشکش کرتا ہے مگر وہ شکریہ ادا کر کے کہتا ہے کہ اسے ذرا جلدی گھر پہنچنا ہے، اور تیز قدموں سے روانہ ہو جاتا ہے۔ مگر اب وہ ایک اور ہی شخص ہے: اب روڈ رولر ’’ہست‘‘ کا محض ایک انگ نہیں بلکہ بجائے خود ایک خود مختار، سدابہار، دھڑکتی اور سانس لیتی ہوئی ’’موجودگی‘‘ کا مظہر ہے۔',
     'شاوخوا دوه ساعته وروسته ډرایور ته وايي چې اوس یې کښته کړي؛ ډرایور وړاندیز کوي چې پر روډ رولر به یې کور ته ورسوي، خو هغه مننه کوي او وايي چې باید یو څه ژر کور ته ورسېږي، او په چټکو ګامونو روانېږي. خو اوس هغه بل کس دی: روډ رولر نور د "وجود" یوازې یو غړی نه دی، بلکې پخپله د یو خپلواک، تل‌شین، درزېدونکي او ساه اخیستونکي "شتون" ښکارندویه دی.'),
    ('He reflects that every desire has a void inside which it wants to fill from the outside world, and once filled its breath stops and it dies; but the road roller is not hollow — it is a compact, solid being, complete in every respect, so what need has it of anything “outside”? It was a strange feeling, and suddenly the void in his own breast swelled like a balloon into a gleaming wish: “If only I too were a road roller!”',
     'وہ سوچتا ہے کہ ہر خواہش کے اندر ایک خلا ہوتا ہے جسے وہ باہر کے وجود سے بھر لینا چاہتی ہے اور جب بھر لیتی ہے تو اس کا سانس رک جاتا ہے اور وہ مر جاتی ہے؛ مگر روڈ رولر اندر سے خالی نہیں — یہ ایک گٹھا ہوا، ٹھوس، ہر اعتبار سے بھرپور وجود ہے، پھر اسے ’’باہر‘‘ کی کسی شے کی کیا ضرورت؟ یہ ایک عجیب سا احساس تھا اور پھر یکایک اس کے سینے کا خلا غبارے کی طرح پھول کر ایک دمکتی ہوئی خواہش میں تبدیل ہو گیا: ’’کاش! میں بھی ایک روڈ رولر ہوتا!‘‘',
     'هغه فکر کوي چې په هره هیله کې یوه تشه وي چې غواړي یې له بهرني وجود ډکه کړي، او کله چې یې ډکه کړي، ساه یې بندېږي او مري؛ خو روډ رولر له دننه تش نه دی — دا یو ټینګ، کلک، له هره پلوه بشپړ وجود دی، نو "بهر" ته د کوم شي اړتیا لري؟ دا یو عجیب احساس و، او ناڅاپه د هغه د سینې تشه د پوکاڼي په څېر وپړسېده او په یوې ځلانده هیلې بدله شوه: "کاشکې زه هم یو روډ رولر وای!"'),
    ('(Pagdandi se Road Roller tak)', '(پگڈنڈی سے روڈ رولر تک)', '(له پلې لارې تر روډ رولر پورې)'),
]: s.p(*x)
tx = BOOK.record(s, 'urdu12-u6-text-3', 'Lesson text — summary (3)', 'متنِ سبق — خلاصہ (۳)', 'د لوست متن — لنډیز (۳)', 31, [52])
tx['sourceGap'] = 'Modern copyrighted inshāʾiya (Dr Wazir Agha, d. 2010); paragraph-wise summary in the app, not verbatim. Printed p. 52.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions:', '۱۔ درج ذیل سوالات کے جوابات لکھیں:', '۱. لاندې پوښتنو ته ځوابونه ولیکئ:')
e.group('lines', [
    ('(a) What did the road roller look like?', '(الف) روڈ رولر کی شکل و صورت کیسی تھی؟', '(الف) د روډ رولر بڼه څنګه وه؟'),
    ('(b) At what speed was the road roller moving?', '(ب) روڈ رولر کس رفتار سے چل رہا تھا؟', '(ب) روډ رولر په کومه چټکتیا روان و؟'),
    ('(c) In the West, the owl is considered a symbol of what?', '(ج) مغرب میں اُلّو کو کس چیز کی علامت سمجھا جاتا ہے؟', '(ج) په لوېدیځ کې ګونګټ د څه نښه ګڼل کېږي؟'),
    ('(d) How long did the author travel on the road roller?', '(د) مصنف نے روڈ رولر پر کتنی دیر سفر کیا؟', '(د) لیکوال پر روډ رولر څومره وخت سفر وکړ؟'),
    ("(e) What thoughts did the author express about the road roller's speed?", '(ہ) مصنف نے روڈ رولر کی رفتار پر کن خیالات کا اظہار کیا؟', '(ه) لیکوال د روډ رولر د چټکتیا په اړه کوم فکرونه څرګند کړل؟'),
])
e.p('2. Fill in the blanks:', '۲۔ خالی جگہ پُر کریں:', '۲. تش ځایونه ډک کړئ:')
e.group('lines', [
    ('(a) The dogs welcomed the road roller by ________ .', '(الف) کتّوں نے ________ کر روڈ رولر کا استقبال کیا۔', '(الف) سپیو په ________ د روډ رولر هرکلی وکړ.'),
    ('(b) Rather, it became a ringing slice of ________ .', '(ب) بلکہ ________ کی ایک کھنکتی ہوئی قاش بن گئی۔', '(ب) بلکې د ________ یوه ټنګېدونکې ټوټه شوه.'),
    ('(c) Inside every desire there is a ________ .', '(ج) ہر خواہش کے اندر ایک ________ ہوتا ہے۔', '(ج) په هره هیله کې یوه ________ وي.'),
    ('(d) These things run backwards, displaying ________ .', '(د) یہ چیزیں ________ کا مظاہرہ کرتے ہوئے پیچھے بھاگتی ہیں۔', '(د) دا شیان د ________ په ښودلو شاته تښتي.'),
])
e.p('3. Explain the following sentences:', '۳۔ درج ذیل جملوں کی وضاحت کریں:', '۳. لاندې جملې تشریح کړئ:')
e.group('lines', [
    ('(a) Speed itself is disorder.', '(الف) رفتار ہی انتشار ہے۔', '(الف) چټکتیا پخپله ګډوډي ده.'),
    ('(b) In fact, change alone is permanent.', '(ب) واقعی تغیر کو ثبات ہے۔', '(ب) رښتیا هم یوازې بدلون ثابت دی.'),
    ('(c) I said, “Thank you! I have to get home a little early.”', '(ج) میں نے کہا شکریہ! مجھے ذرا جلدی گھر پہنچنا ہے۔', '(ج) ما وویل: "مننه! باید یو څه ژر کور ته ورسېږم."'),
])
e.p('4. Correct the following sentences according to the rules (of grammar).', '۴۔ درج ذیل جملوں کو قواعد کے مطابق درست کریں۔', '۴. لاندې جملې د قواعدو سره سم سمې کړئ.')
e.group('lines', [
    ('(a) “The old man had drunk the water of many ghats.” [as printed, to be corrected]', '(الف) بوڑھا شخص بہت سے گھاٹوں کا پانی پی چکا تھا۔', '(الف) "زوړ سړي د ډېرو ګودرونو اوبه څښلې وې." [لکه څنګه چې چاپ شوې، باید سمه شي]'),
    ('(b) “There is no shortage of manpower inside Pakistan.”', '(ب) پاکستان کے اندر افرادی قوّت کی کمی نہیں ہے۔', '(ب) "د پاکستان دننه د بشري ځواک کمښت نشته."'),
    ('(c) “I took advantage of my college library.”', '(ج) میں نے اپنے کالج کی لائبریری سے استفادہ حاصل کیا۔', '(ج) "ما د خپل کالج له کتابتون څخه ګټه ترلاسه کړه."'),
    ("(d) “The boy, afraid, entered the principal's office.”", '(د) لڑکا ڈرتا ڈرتا پرنسپل کے دفتر میں داخل ہوا۔', '(د) "هلک وېرېدونکی د پرنسپل دفتر ته ننوت."'),
    ('(e) “Multan is the land of saints.”', '(ہ) ملتان اولیاؤں کی سرزمین ہے۔', '(ه) "ملتان د اولیاوو ځمکه ده."'),
])
e.p('5. Put the punctuation marks in the appropriate places in the following sentences.', '۵۔ درج ذیل جملوں میں مناسب مقامات پر رموزِ اوقاف لگائیں۔', '۵. په لاندې جملو کې په مناسبو ځایونو کې رموزِ اوقاف کېږدئ.')
e.group('lines', [
    ('(a) He brought vegetables fruits pulses and meat from the market.', '(الف) وہ بازار سے سبزیاں پھل دالیں اور گوشت لایا۔', '(الف) هغه له بازاره سبزي مېوې دالونه او غوښه راوړه.'),
    ('(b) That person came like a fragrance swaying scattered happiness and went away.', '(ب) وہ شخص خوشبو کی طرح آیا جھوما خوشیاں بکھیریں اور چلا گیا۔', '(ب) هغه کس د خوشبو په څېر راغی ونڅېد خوښۍ یې خپرې کړې او لاړ.'),
    ('(c) Quaid-e-Azam the founder of Pakistan was a very great statesman.', '(ج) قائداعظم بانیٔ پاکستان بہت بڑے سیاست دان تھے۔', '(ج) قایداعظم د پاکستان بنسټګر ډېر لوی سیاستوال و.'),
    ('(d) How can we helpless humans face these circumstances.', '(د) ہم مجبور انسان اِن حالات کا مقابلہ کیسے کریں۔', '(د) موږ مجبور انسانان له دې حالاتو سره څنګه مقابله وکړو.'),
    ('(e) Whether you are good or bad scholar or ignorant religious or worldly you are yourself responsible for your deeds.', '(ہ) تم اچھے ہو یا بُرے عالم ہو یا جاہل دین دار ہو یا دُنیا دار اپنے اعمال کے خود ذمہ دار ہو۔', '(ه) که ښه یې که بد عالم یې که جاهل دیندار یې که دنیادار د خپلو اعمالو پخپله مسؤل یې.'),
])
ex = BOOK.record(e, 'urdu12-u6-exercise', 'Exercise', 'مشق', 'تمرین', 31, [52, 53])
issues = [{'id': 'urdu12-pdf031', 'unit': 6, 'printedPage': 53, 'description': 'Q4 sentences deliberately contain errors to be corrected (e.g. “استفادہ حاصل کیا”, “اولیاؤں”, “ڈرتا ڈرتا”); kept as printed. Q5 sentences are printed without the punctuation students must add. Q5 items lack opening brackets “الف)”. Handwritten answers in Q2 blanks are owner notes, excluded.'}]

if __name__ == '__main__':
    BOOK.save(31, [(6, tx), (6, ex)], issues=issues, complete_units=[6])
