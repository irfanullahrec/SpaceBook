"""Urdu XII PDF116 (spread): pp.222–223 — Ghazal 9 (Iqbal, public domain) full text + مشق Q1."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
t.h('Ghazal — Allama Iqbal', 'غزل — علامہ اقبالؒ', 'غزل — علامه اقبال')
SH = [
 [('Those whom I used to seek in the heavens and on the earths', 'جنھیں میں ڈھونڈتا تھا آسمانوں میں زمینوں میں', 'هغه چې ما به په اسمانونو او ځمکو کې لټول'),
  ('turned out to be the dwellers of my heart’s dark chamber.', 'وہ نکلے میرے ظلمت خانۂ دل کے مکینوں میں', 'زما د زړه د تیارې کوټې اوسېدونکي راووتل.')],
 [('O Majnun, have you ever looked at yourself too?', 'کبھی اپنا بھی نظارہ کیا ہے تو نے اے مجنوں', 'اې مجنونه، کله دې ځان ته هم کتلي؟'),
  ('For like Laila you too are among those seated in the litter.', 'کہ لیلیٰ کی طرح تو خود بھی ہے محمل نشینوں میں', 'چې د لیلا په څېر ته پخپله هم د کجاوې له ناستو یې.')],
 [('The months of union fly past like hours,', 'مہینے وصل کے گھڑیوں کی صورت اُڑتے جاتے ہیں', 'د وصال میاشتې د ګړیو په څېر الوزي،'),
  ('but the hours of separation pass like months.', 'مگر گھڑیاں جُدائی کی گزرتی ہیں مہینوں میں', 'خو د بېلتون ګړۍ په میاشتو کې تېرېږي.')],
 [('O boatman, will you stop me from drowning?', 'مجھے روکے گا تو اے ناخدا کیا غرق ہونے سے', 'اې ملاحه، ایا ته به ما له ډوبېدو منع کړې؟'),
  ('For those who are to drown, drown even in ships.', 'کہ جن کو ڈوبنا ہو ڈوب جاتے ہیں سفینوں میں', 'چې څوک باید ډوب شي، په کښتیو کې هم ډوبېږي.')],
 [('The wave of their breath can relight an extinguished candle —', 'جلا سکتی ہے شمعِ کشتہ کو موجِ نفس اُن کی', 'د هغوی د ساه څپه مړه شمع بیا بلولی شي —'),
  ('O God, what lies hidden in the breasts of the men of heart!', 'الٰہی کیا چھپا ہوتا ہے اہلِ دل کے سینوں میں', 'خدایه، د زړه والو په سینو کې څه پټ وي!')],
 [('Do not ask about these wearers of the patched cloak; if you have devotion, look at them:', 'نہ پُوچھ ان خرقہ پوشوں کی، ارادت ہو تو دیکھ ان کو', 'د دې خرقه‌پوشو پوښتنه مه کوه؛ که ارادت لرې، ورته وګوره:'),
  ('they sit holding the White Hand (of Moses) in their sleeves.', 'یدِ بیضا لیے بیٹھے ہیں اپنی آستینوں میں', 'په خپلو لستوڼو کې یې د موسیٰ سپین لاس نیولی ناست دي.')],
 [('For love, seek a heart that can break:', 'محبت کے لیے دل ڈھونڈ کوئی ٹوٹنے والا', 'د مینې لپاره داسې زړه ولټوه چې ماتېدونکی وي:'),
  ('this is the wine that is kept in delicate crystal flasks.', 'یہ وہ مے ہے جسے رکھتے ہیں نازک آبگینوں میں', 'دا هغه شراب دي چې په نازکو ښیښو کې ساتل کېږي.')],
 [('Become manifest and show them your beauty some day;', 'نمایاں ہو کے دکھلا دے کبھی اُن کو جمال اپنا', 'ښکاره شه او کله خپل جمال وروښیه؛'),
  ('for a long time you have been talked of among the subtle-sighted.', 'بہت مدّت سے چرچے ہیں ترے باریک بینوں میں', 'له ډېره وخته د باریک‌بینانو په منځ کې ستا خبرې دي.')],
 [('Be silent, O heart; it is not good to cry out in a crowded gathering;', 'خموش اے دل بھری محفل میں چلّانا نہیں اچھا', 'چوپ شه اې زړه، په ډکه غونډه کې چغې وهل ښه نه دي؛'),
  ('courtesy is the first of the proprieties of love.', 'ادب پہلا قرینہ ہے محبت کے قرینوں میں', 'ادب د مینې د اداب لومړی ادب دی.')],
 [('That I should think ill of them — that cannot be from me,', 'بُرا سمجھوں اُنھیں، مجھ سے تو ایسا ہو نہیں سکتا', 'چې هغوی بد وګڼم — دا له ما نه نه کېږي،'),
  ('for I myself, Iqbal, am among my own fault-finders.', 'کہ میں تو خود بھی ہوں اقبالؔ اپنے نکتہ چینوں میں', 'ځکه زه، اقباله، پخپله هم د خپلو نیوکه‌کوونکو په منځ کې یم.')],
]
for sh in SH:
    t.group('lines', sh)
t.p('(Bang-e-Dara)', '(بانگِ درا)', '(بانګ درا)')
po = BOOK.record(t, 'urdu12-u26-ghazal', 'Ghazal text', 'متنِ غزل', 'د غزل متن', 116, [222, 223])
po['sourceCoverIllustrationReview'] = 'Portrait of Allama Iqbal beside the title and a faint quill-and-inkpot drawing are decorative; not reproduced.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.p('1. Write answers to the following questions according to the ghazal.', '۱۔ غزل کے مطابق درج ذیل سوالات کے جوابات لکھیں۔', '۱. د غزل سره سم لاندې پوښتنو ته ځوابونه ولیکئ.')
e.group('lines', [
    ('(a) What does the poet search for in earth and sky?', '(ا) شاعر زمین و آسمان میں کیا ڈھونڈتا ہے؟', '(الف) شاعر په ځمکه او اسمان کې څه لټوي؟'),
    ('(b) Why does the time of union pass quickly?', '(ب) وصل کا وقت جلد کیوں بیت جاتا ہے؟', '(ب) د وصال وخت ولې ژر تېرېږي؟'),
    ('(c) Which people are meant by “ahl-e dil” (men of heart)?', '(ج) اہلِ دل سے کون سے لوگ مراد ہیں؟', '(ج) د "اهل دل" نه کوم خلک مراد دي؟'),
    ('(d) What is the very first lesson of love?', '(د) محبت کا اوّلین درس کون سا ہے؟', '(د) د مینې لومړنی درس کوم دی؟'),
    ('(e) What does finding fault with oneself mean?', '(ہ) خود پر نکتہ چینی کا کیا مطلب ہے؟', '(ه) پر ځان د نیوکې مانا څه ده؟'),
    ('(f) Explain “Yad-e Baiza” (the White Hand).', '(و) یدِ بیضا کی وضاحت کریں۔', '(و) "ید بیضا" (سپین لاس) تشریح کړئ.'),
])
ex = BOOK.record(e, 'urdu12-u26-exercise', 'Exercise', 'مشق', 'تمرین', 116, [223])
issues = [{'id': 'urdu12-pdf116', 'unit': 26, 'printedPage': 222, 'description': 'Ghazal 9 (Iqbal, d.1938) is public domain and transcribed in full (10 couplets). No separate author note is printed for Iqbal in the ghazal section (his note is with Poem 1).'}]

if __name__ == '__main__':
    BOOK.save(116, [(26, po), (26, ex)], issues=issues, complete_units=[26])
