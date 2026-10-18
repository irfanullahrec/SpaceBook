"""Urdu XII PDF81 (spread): printed pp.152–153 — Lesson 15 مشق Q1–Q6 and note on متحمل الضدین (double meaning)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions.', '۱۔ درج ذیل سوالات کے جوابات لکھیں۔', '۱. لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) Why did the author compare Zia Jafri to an old banyan tree?', '(الف) مصنف نے ضیا جعفری کو بوڑھے برگد سے کیوں تشبیہ دی؟', '(الف) لیکوال ضیا جعفري له زاړه بړ‌ونې سره ولې تشبیه کړ؟'),
    ("(b) Where was Zia Jafri's house situated?", '(ب) ضیا جعفری کا گھر کہاں واقع تھا؟', '(ب) د ضیا جعفري کور چېرته و؟'),
    ('(c) Who were the members of the Daira-e-Adabia?', '(ج) دائرۂ ادبیہ میں کون کون شامل تھے؟', '(ج) په دایره ادبیه کې څوک څوک شامل وو؟'),
    ('(d) Who was Abdul Wadood Qamar?', '(د) عبدالودود قمر کون تھے؟', '(د) عبدالودود قمر څوک و؟'),
    ("(e) How did Qamar Sahib maintain the Daira's rules and regulations?", '(ہ) قمر صاحب دائرہ کے اصول و ضوابط کیسے برقرار رکھتے تھے؟', '(ه) قمر صاحب د دایرې اصول او ضوابط څنګه ساتل؟'),
    ("(f) What were the author's feelings about poets?", '(و) شاعروں کے بارے میں مصنف کے کیا جذبات تھے؟', '(و) د شاعرانو په اړه د لیکوال احساسات څه وو؟'),
])
e.p('2. Fill in the blanks.', '۲۔ خالی جگہ پُر کریں۔', '۲. تش ځایونه ډک کړئ.')
e.group('lines', [
    ('(a) Zia Jafri was such a river that it was impossible to confine even in a ________ .', '(الف) ضیا جعفری ایسے دریا تھے جنھیں ________ میں بند کرنا بھی محال تھا۔', '(الف) ضیا جعفري داسې سیند و چې په ________ کې یې بندول هم ناشوني وو.'),
    ('(b) The gathering would ________ with his magical fragrance.', '(ب) محفل اُن کی طلسمی خوشبو سے ________ لگتی۔', '(ب) محفل به د هغه په جادويي خوشبو ________ .'),
    ('(c) When I gained ________ , I learned that these two gentlemen are famous poets.', '(ج) جب میں نے ________ سنبھالا تو پتا چلا کہ یہ دونوں حضرات مشہور شاعر ہیں۔', '(ج) کله چې ما ________ وساته، پوه شوم چې دا دواړه نامتو شاعران دي.'),
    ('(d) Zia Jafri was enlightened and ________ .', '(د) ضیا جعفری روشن خیال اور ________ تھے۔', '(د) ضیا جعفري روښانفکره او ________ و.'),
    ('(e) The friendship of Zia and Qamar was a ________ in the whole city.', '(ہ) ضیا اور قمر کی دوستی سارے شہر میں ________ تھی۔', '(ه) د ضیا او قمر دوستي په ټول ښار کې ________ وه.'),
    ('(f) In fact it was Qamar Sahib who taught me [to hold] the pen ________ .', '(و) درحقیقت مجھے قلم ________ قمر صاحب نے ہی سکھایا۔', '(و) په حقیقت کې ماته قلم ________ قمر صاحب ښودلی.'),
    ('(g) Even in serious conversation his vein of wit would ________ .', '(ز) سنجیدہ گفتگو میں بھی اُن کی رگِ ظرافت ________ اُٹھتی۔', '(ز) په جدي خبرو کې هم د هغه د ظرافت رګ ________ .'),
])
e.p('3. Put diacritics on the following words and write them in alphabetical order: naẓm-o-ẓabṭ, mushāʿara, maqālāt, talkh-kalāmī, jāzibiyyat.', '۳۔ درج ذیل الفاظ پر اعراب لگائیں اور الفبائی ترتیب سے لکھیں۔ نظم و ضبط، مشاعرہ، مقالات، تلخ کلامی، جاذبیت۔', '۳. پر لاندې کلمو اعراب کېږدئ او د الفبا په ترتیب یې ولیکئ: نظم و ضبط، مشاعره، مقالات، تلخ کلامي، جاذبیت.')
e.p('4. Put punctuation marks at the appropriate places in the following sentences.', '۴۔ درج ذیل جملوں میں مناسب مقامات پر رموزِ اوقاف لگائیں۔', '۴. په لاندې جملو کې په مناسبو ځایونو کې د تنقیط نښې کېږدئ.')
e.group('lines', [
    ('(a) Imran Khan who is a renowned son of Pakistan built a cancer hospital.', '(الف) عمران خان نے جو پاکستان کا نامور فرزند ہے کینسر ہسپتال بنایا۔', '(الف) عمران خان چې د پاکستان نامتو زوی دی د سرطان روغتون جوړ کړ.'),
    ('(b) Up to Lake Saiful Muluk which is all mountainous area the journey is not easy.', '(ب) جھیل سیف الملوک تک جو سارا پہاڑی علاقہ ہے سفر آسان نہیں ہے۔', '(ب) د سیف‌الملوک ډنډ پورې چې ټوله غرنۍ سیمه ده سفر اسانه نه دی.'),
    ('(c) Listen will you help me.', '(ج) سنو کیا تم میری مدد کرو گے۔', '(ج) واوره ایا ته به زما مرسته وکړې.'),
    ('(d) Mashallah what a clever girl she is.', '(د) ماشاء اللہ کتنی ذہین بچی ہے۔', '(د) ماشاالله څومره هوښیاره نجلۍ ده.'),
    ('(e) The children said uncle has come.', '(ہ) بچے بولے ماموں جان آ گئے۔', '(ه) ماشومانو وویل ماما جان راغی.'),
])
e.p('5. Correct the following sentences according to grammar.', '۵۔ درج ذیل جملوں کو قواعد کے مطابق درست کریں۔', '۵. لاندې جملې د قواعدو سره سمې کړئ.')
e.group('lines', [
    ("(a) Also write the poet's name as well. (nīz … bhī — redundant)", '(الف) نیز شاعر کا نام بھی لکھیں۔', '(الف) "نیز" او "بھی" دواړه — د شاعر نوم هم ولیکئ.'),
    ('(b) Our house is “wāqiʿa” (incident) in the city. (for wāqiʿ, situated)', '(ب) ہمارا گھر شہر میں واقعہ ہے۔', '(ب) زموږ کور په ښار کې "واقعه" (پېښه) دی — د "واقع" پر ځای.'),
    ("(c) Listen carefully to the elders' talk.", '(ج) بزرگوں کی بات کو غور سے سنو۔', '(ج) د مشرانو خبرې په غور واورئ.'),
    ('(d) When will you return back.', '(د) تم کب واپس لوٹو گے۔', '(د) ته به کله بېرته راوګرځې.'),
    ('(e) Why have you made a noise.', '(ہ) تم نے کیوں شور ڈالا ہے۔', '(ه) تا ولې شور جوړ کړی.'),
    ('(f) I am extremely thankful to you.', '(و) میں آپ کا بے حد مشکور ہوں۔', '(و) زه ستاسو بې‌حده مشکور یم.'),
])
e.p('6. Identify the idioms in this lesson.', '۶۔ اس سبق میں سے محاورات کی نشان دہی کریں۔', '۶. په دې لوست کې محاورې په نښه کړئ.')
ex = BOOK.record(e, 'urdu12-u15-exercise', 'Exercise', 'مشق', 'تمرین', 81, [152, 153])

g = Builder()
g.h('Double meaning (mutaḥammil-uẓ-ẓiddain)', '* متحمل الضدین', '* متحمل الضدین (دوه‌مانیز کلام)')
g.p('“Kal gadhe par jā kar naẓm paṛhnā aur bīs rupe kā chek lānā.” Saying something that can bear two meanings, each the opposite of the other, is called mutaḥammil-uẓ-ẓiddain. For example, one meaning of this sentence is: “Go tomorrow (kal) to Gadhe [a place] and recite a poem [and bring a cheque of twenty rupees]”; the other is: “Ride on a donkey (gadhā) and recite a poem.” Find and write five examples of this kind.',
    '’’کل گدھے پر جا کر نظم پڑھنا اور بیس روپے کا چیک لانا۔‘‘ ایسا کلام کہنا جس کے دو معنی نکل سکتے ہوں اور دونوں ایک دوسرے کے برعکس ہوں متحمل الضدین کہلاتا ہے۔ مثلاً اس جملے کا ایک مطلب تو یہ ہے کہ کل جانا اور ’’گدھے‘‘ پر نظم پڑھنا اور دوسرا مطلب یہ ہے کہ گدھے پر بیٹھ کر جانا اور نظم پڑھنا۔ اس طرح کی پانچ مثالیں تلاش کر کے لکھیں۔',
    '"سبا خره ته لاړ شه، نظم ووایه او د شلو روپیو چک راوړه." داسې کلام ویل چې دوه ماناوې ترې راوځي او دواړه یو د بل پر خلاف وي، "متحمل الضدین" بلل کېږي. د بېلګې په توګه د دې جملې یوه مانا دا ده چې سبا لاړ شه او د "خره" په اړه نظم ووایه، او بله مانا دا ده چې پر خره سپور لاړ شه او نظم ووایه. د دې ډول پنځه بېلګې ومومئ او ولیکئ.')
gr = BOOK.record(g, 'urdu12-u15-grammar', 'Note: double meaning (mutahammil-uz-ziddain)', 'متحمل الضدین', 'متحمل الضدین', 81, [153])
issues = [{'id': 'urdu12-pdf081', 'unit': 15, 'printedPage': 153, 'description': 'Q5 sentences are printed with deliberate errors to be corrected (e.g. “نیز … بھی”, “واقعہ” for “واقع”, “واپس لوٹو”, “مشکور”) — retained as printed. The note’s explanation of the double meaning (“کل جانا اور ’گدھے‘ پر نظم پڑھنا”) is translated by sense.'}]

if __name__ == '__main__':
    BOOK.save(81, [(15, ex), (15, gr)], issues=issues, complete_units=[15])
