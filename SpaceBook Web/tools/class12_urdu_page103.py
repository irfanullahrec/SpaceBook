"""Urdu XII PDF103 (spread): p.196 Poem 2 'بڑھے چلو' last stanza (source لالۂ طور) + مشق Q1–Q2; p.197 مشق Q3–Q4 + note مسدس ترجیع بند."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.p('Stanza 4', 'بند ۴', 'بند ۴')
t.group('lines', [
    ('If a soldierly life is a fortunate lot,', 'سپاہیانہ زندگی جو قسمتِ سعید ہے', 'که سپاهیانه ژوند نېکمرغه برخه ده،'),
    ('then even death on the battlefield is a soldier’s Eid;', 'تو رزم گہ کی موت بھی سپاہیانہ عید ہے', 'نو د جګړې په ډګر کې مرګ هم سپاهیانه اختر دی؛'),
    ('if he lives, he is the pride of the nation; if he dies, he is a martyr;', 'جیا تو فخرِ قوم ہے، مرا تو وہ شہید ہے', 'که ژوندی پاتې شي، د قوم ویاړ دی؛ که مړ شي، شهید دی؛'),
    ('with shrouds tied to your heads, march on, march on.', 'سروں سے باندھ کر کفن بڑھے چلو، بڑھے چلو', 'پر سرونو کفنونه وتړئ، مخ ته ځئ، مخ ته ځئ.'),
])
t.group('lines', [('Brave swordsmen, march on, march on;', 'دلاورانِ تیغ زن بڑھے چلو، بڑھے چلو', 'تورې وهونکو زړورو، مخ ته ځئ، مخ ته ځئ؛'),
                  ('valiant rank-breakers, march on, march on.', 'بہادرانِ صف شکن بڑھے چلو، بڑھے چلو', 'لیکې ماتوونکو اتلانو، مخ ته ځئ، مخ ته ځئ.')])
t.p('(Lala-e-Toor: Part Three)', '(لالۂ طور: حصہ سوم)', '(لاله طور: درېیمه برخه)')
po = BOOK.record(t, 'urdu12-u19-poem-2', 'Poem text (2): last stanza', 'متنِ نظم (۲): آخری بند', 'د نظم متن (۲): وروستی بند', 103, [196])

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions according to the poem.', '۱۔ نظم کے مطابق درج ذیل سوالات کے جوابات لکھیں۔', '۱. د نظم سره سم لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) What things are we urged to sacrifice in the name of the homeland?', '(ا) وطن کے نام پر کن چیزوں کو قربان کر دینے کی تلقین کی گئی ہے؟', '(الف) د وطن په نوم د کومو شیانو د قربانولو تلقین شوی؟'),
    ('(b) Write the central idea of this poem.', '(ب) اس نظم کا مرکزی خیال تحریر کریں۔', '(ب) د دې نظم مرکزي فکر ولیکئ.'),
    ('(c) In the first stanza, in spite of which difficulties are we advised to go forward?', '(ج) پہلے بند میں کن کن مشکلات کے باوجود آگے بڑھنے کی نصیحت کی گئی ہے؟', '(ج) په لومړي بند کې د کومو ستونزو سره سره د مخ ته تګ نصیحت شوی؟'),
    ("(d) On what has the homeland's progress and decline been said to depend?", '(د) وطن کی ترقی و تنزلی کا انحصار کس چیز پر بیان کیا گیا ہے؟', '(د) د وطن پرمختګ او زوال پر کوم شي تړلی ښودل شوی؟'),
    ('(e) What is meant by “tying shrouds to the heads”?', '(ہ) ’’سروں پر کفن باندھنے‘‘ سے کیا مراد ہے؟', '(ه) "پر سرونو کفن تړل" څه مانا لري؟'),
])
e.p('2. Explain the meaning of the following compounds: sail-o-jūybār, marg-o-zīst, tegh-e be-amāṉ, qismat-e saʿīd, fakhr-e qaum, tegh-zan, razm-gāh, ṣaf-shikan.', '۲۔ مندرجہ ذیل مرکبات کا مفہوم واضح کریں: سیل و جوئبار۔ مرگ و زیست۔ تیغِ بے اماں۔ قسمتِ سعید۔ فخرِ قوم۔ تیغ زن۔ رزم گاہ۔ صف شکن۔', '۲. د لاندې مرکباتو مفهوم روښانه کړئ: سیل و جویبار، مرګ و زیست، بې‌امانه توره، نېکمرغه برخه، د قوم ویاړ، توره‌وهونکی، د جګړې ډګر، لیکه‌ماتوونکی.')
e.p('3. Put diacritics on the following words to make their pronunciation clear: ṣaf-shikan, kafan, razm, dasht, baḥr, dilāwar, iftikhār, bahādur.', '۳۔ درج ذیل الفاظ پر اعراب لگا کر تلفظ واضح کریں: صف شکن۔ کفن۔ رزم۔ دشت۔ بحر۔ دلاور۔ افتخار۔ بہادر۔', '۳. پر لاندې کلمو اعراب کېږدئ او تلفظ یې روښانه کړئ: صف‌شکن، کفن، رزم، دښت، بحر، دلاور، افتخار، بهادر.')
e.p('4. According to the poem, put a (✓) against correct sentences and a (✗) against wrong ones:', '۴۔ نظم کے مطابق درست جملوں کے سامنے (✓) اور غلط کے سامنے (✗) کا نشان لگائیں:', '۴. د نظم سره سم سمو جملو ته (✓) او ناسمو ته (✗) نښه کېږدئ:')
e.group('lines', [
    ('(a) Even if flowers and gardens come in the way, march on.', '(ا) گل و گلزار بھی راستے میں آئیں تو بڑھے چلو', '(الف) که ګلونه او ګلزارونه هم لارې ته راشي، مخ ته ځئ.'),
    ('(b) One should go forward after kindling a passion in one’s heart.', '(ب) دلوں میں ایک جذبہ پیدا کر کے آگے بڑھنا چاہیے۔', '(ب) باید په زړونو کې یوه جذبه پیدا کړو او مخ ته لاړ شو.'),
    ('(c) Brave people should raise the courage of cowards.', '(ج) بہادر لوگوں کو بزدلوں کا حوصلہ بڑھانا چاہیے۔', '(ج) زړور خلک باید د ډارنو زړه پیاوړی کړي.'),
    ('(d) One should sacrifice even one’s life in the pure name of the homeland.', '(د) وطن کے پاک نام پر اپنی جان بھی قربان کر دینی چاہیے۔', '(د) د وطن پر پاک نوم باید خپل ځان هم قربان کړو.'),
    ('(e) Even death on the battlefield is a cause of joy for a soldier.', '(ہ) میدانِ جنگ کی موت بھی سپاہی کے لیے خوشی کا باعث ہوتی ہے۔', '(ه) د جګړې په ډګر کې مرګ هم سپاهي ته د خوښۍ لامل دی.'),
    ('(f) The homeland is calling: march on.', '(و) وطن پکار رہا ہے کہ آگے بڑھے چلو۔', '(و) وطن غږ کوي چې مخ ته ځئ.'),
    ('(g) Rich people should help the poor.', '(ز) امیر لوگوں کو غریبوں کی مدد کرنی چاہیے۔', '(ز) شتمن خلک باید د بېوزلو مرسته وکړي.'),
])
ex = BOOK.record(e, 'urdu12-u19-exercise', 'Exercise', 'مشق', 'تمرین', 103, [196, 197])

n = Builder()
n.h('Musaddas tarjīʿ-band', 'مسدس ترجیع بند', 'مسدس ترجیع بند')
n.p('If the third couplet of every stanza of a musaddas (six-line stanza poem) is repeated word for word, it is called the refrain couplet (ṭeep kā shiʿr), and such a musaddas is called a musaddas tarjīʿ-band. The poem “Barhe Chalo” is also an example of a musaddas tarjīʿ-band.',
    'مسدس کے ہر بند کا تیسرا شعر اگر من و عن دُہرایا جائے تو اسے ٹیپ کا شعر اور ایسی مسدس کو مسدس ترجیع بند کہتے ہیں۔ ’’نظم بڑھے چلو‘‘ بھی مسدس ترجیع بند کی مثال ہے۔',
    'که د مسدس (شپږ مصرعیز بند لرونکي نظم) د هر بند درېیم بیت کټ مټ تکرار شي، هغه ته "د ټیپ بیت" او داسې مسدس ته "مسدس ترجیع بند" ویل کېږي. "مخ ته ولاړ شئ" نظم هم د مسدس ترجیع بند بېلګه ده.')
nt = BOOK.record(n, 'urdu12-u19-note', 'Note: musaddas tarjīʿ-band', 'مسدس ترجیع بند', 'مسدس ترجیع بند', 103, [197])
issues = [{'id': 'urdu12-pdf103', 'unit': 19, 'printedPage': 196, 'description': 'Source line printed “لالۂ طور: حصہ سوم”. Faint background drawing behind the exercise is decorative.'}]

if __name__ == '__main__':
    BOOK.save(103, [(19, po), (19, ex), (19, nt)], issues=issues, complete_units=[19])
