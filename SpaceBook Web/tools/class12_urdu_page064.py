"""Urdu XII PDF64 (spread): p.118 Lesson 12 note '* مرکّب جملے: استدراکی، سببی'; p.119 Lesson 13 author note (فرحت اللہ بیگ, 1883–1947)."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
g = Builder()
g.h('* Compound sentences:', '* مرکّب جملے:', '* مرکبې جملې:')
g.h('Adversative (istidrākī) sentences:', 'استدراکی جملے:', 'استدراکي جملې:')
g.p('In these, two sentences are generally contrasted with each other. In such sentences magar, lekin, aur, par, balke, so (but, however, and, yet, rather, so) etc. are used. They are of three kinds.', 'اس میں عموماً دو جملوں کا باہم مقابلہ کیا جاتا ہے۔ اس طرح کے جملوں میں مگر، لیکن، اور، پر، بلکہ، سو وغیرہ استعمال ہوتے ہیں۔ اس کی تین قسمیں ہیں۔', 'په دې کې معمولاً د دوو جملو ترمنځ پرتله کېږي. په دې ډول جملو کې "مګر، لیکن، اور، پر، بلکې، سو" (خو، مګر، او، خو، بلکې، نو) او نور کارېږي. درې ډوله دي.')
g.p('(1) The second sentence is against the first or negates it, e.g.:', '(۱) دوسرا جملہ پہلے جملے کے خلاف یا اس کی نفی کرے مثلاً:', '(۱) دویمه جمله د لومړۍ خلاف وي یا یې نفي کړي، د بېلګې په توګه:')
g.group('lines', [('He progressed and reached so far, but I am where I was.', 'وہ ترقی کرتے ہوئے کہاں جا پہنچا مگر میں وہیں کا وہیں ہوں۔', 'هغه پرمختګ وکړ او چېرته ورسېد، خو زه هماغلته یم.'),
                  ('So great a scholar and so hard-hearted.', 'اتنا بڑا عالم اور اس قدر سنگ دِل', 'دومره لوی عالم او دومره سخت زړی.')])
g.group('list', [('Sometimes sentences of this kind begin with “agarche” (although), as:', 'بعض اوقات اس طرح کے جملے ’’اگرچہ‘‘ سے شروع ہوتے ہیں۔ جیسے:', 'ځینې وختونه دا ډول جملې په "اګرچه" (که څه هم) پیلېږي، لکه:')])
g.group('lines', [('Although he had ignored me, I will help him.', 'اگرچہ اُس نے مجھے نظر انداز کیا تھا لیکن میں اُس کی مدد کروں گا۔', 'که څه هم هغه زه له پامه غورځولی وم، خو زه به یې مرسته وکړم.')])
g.p('(2) The second sentence limits or restricts the first, as:', '(۲) دوسرا جملہ پہلے جملے کو محدود یا مقید کرے۔ جیسے:', '(۲) دویمه جمله لومړۍ محدودوي یا مقیدوي، لکه:')
g.group('lines', [('He does make promises, but does not remember them.', 'وہ وعدے تو کرتا ہے لیکن یاد نہیں رکھتا۔', 'ژمنې خو کوي خو یې په یاد نه ساتي.'), ('He is a friend indeed, but not a companion in hardship.', 'وہ دوست تو ہے پر مصیبت کا ساتھی نہیں۔', 'دوست خو دی، خو د مصیبت ملګری نه دی.')])
g.p('(3) The second statement expands or confirms the first, as:', '(۳) دوسرا بیان پہلے بیان کی توسیع یا تصدیق کرے۔ جیسے:', '(۳) دویمه وینا لومړۍ پراخوي یا یې تاییدوي، لکه:')
g.group('lines', [('He not only acted selfishly but also caused all kinds of hardship.', 'اُس نے صرف خود غرضی ہی نہیں کی بلکہ طرح طرح کی تکالیف بھی پہنچائیں۔', 'هغه یوازې ځان‌غوښتنه نه ده کړې بلکې ډول ډول ربړونه یې هم رسولي.')])
g.h('Causal (sababī) sentences:', 'سببی جملے:', 'سببي جملې:')
g.p('In these sentences the second sentence shows the reason, cause or result of the first. Before such sentences kyūnke (because), is liye, is wāste (therefore), lihāzā (hence), pas (so) etc. are used.', 'اِن جملوں میں دوسرا جملہ پہلے جملے کی وجہ، سبب یا نتیجے کو ظاہر کرے۔ ان جملوں سے پہلے کیوں کہ، اس لیے، اس واسطے، لہٰذا، پس وغیرہ کا استعمال ہوتا ہے۔', 'په دې جملو کې دویمه جمله د لومړۍ لامل، سبب یا پایله ښيي. له دې جملو مخکې "کیوں کہ" (ځکه چې)، "اس لیے، اس واسطے" (له دې امله)، "لہٰذا" (نو)، "پس" (نو) او نور کارېږي.')
g.group('lines', [
    ('(i) He is very rude, therefore I do not talk with him much.', '(i) وہ بہت بدتمیز ہے اس لیے میں اُس سے زیادہ بات چیت نہیں کرتا۔', '(i) هغه ډېر بې‌ادبه دی، نو زه ورسره ډېرې خبرې نه کوم.'),
    ('(ii) I believe what he says because he is truthful.', '(ii) مجھے اُس کی بات کا یقین ہے کیوں کہ وہ سچا ہے۔', '(ii) د هغه په خبره باور لرم ځکه چې رښتینی دی.'),
    ('(iii) Sometimes the word “chūnke” (since) is also used before such sentences, e.g.:', '(iii) بعض اوقات اس طرح کے جملوں سے پہلے لفظ ’’چونکہ‘‘ کا استعمال بھی ہوتا ہے۔ مثلاً:', '(iii) ځینې وختونه له دې ډول جملو مخکې د "چونکه" (څرنګه چې) کلمه هم کارېږي، د بېلګې په توګه:'),
    ('(iv) Since he is in the right, I will certainly support him.', '(iv) چونکہ وہ حق پر ہے اس لیے میں اُس کا ساتھ ضرور دوں گا۔', '(iv) څرنګه چې هغه په حق دی، نو زه به یې خامخا ملګرتیا وکړم.'),
])
gr = BOOK.record(g, 'urdu12-u12-grammar', 'Compound sentences: adversative and causal', 'مرکّب جملے: استدراکی اور سببی', 'مرکبې جملې: استدراکي او سببي', 64, [118])

a = Builder()
a.h('Farhatullah Baig', 'فرحت اللہ بیگ', 'فرحت الله بیګ')
a.p('Born: 1883 · Died: 1947', 'ولادت: ۱۸۸۳ء · وفات: ۱۹۴۷ء', 'زېږېدنه: ۱۸۸۳ز · مړینه: ۱۹۴۷ز')
for x in [
    ("Farhatullah Baig was born in Mohalla Chauri Walan of Delhi. His father's name was Mirza Hashmatullah Baig. Farhat was still young when his mother died; his paternal aunt Husn Jahan Begum brought him up. Farhat's early education took place at home. He did his B.A. from St. Stephen's College. His love of poetry arose in his student days.",
     'فرحت اللہ بیگ دِلّی کے محلّہ چوڑی والاں میں پیدا ہوئے۔ والد کا نام مرزا حشمت اللہ بیگ تھا۔ فرحت ابھی کم سِن ہی تھے کہ اُن کی والدہ کا انتقال ہو گیا۔ اُن کی پرورش اُن کی پھوپھی حُسن جہاں بیگم نے کی۔ فرحت کی ابتدائی تعلیم گھر پر ہوئی۔ اُنھوں نے سینٹ سٹیفنز کالج سے بی۔ اے کیا۔ شعر و شاعری کا شوق طالب علمی کے زمانے میں پیدا ہوا۔',
     'فرحت الله بیګ د ډهلي په چوړي والان محله کې زېږېدلی. د پلار نوم یې میرزا حشمت الله بیګ و. فرحت لا کوچنی و چې مور یې مړه شوه؛ ترور یې حسن جهان بېګم روزنه وکړه. د فرحت لومړنۍ زده کړې په کور کې وشوې. له سېنټ سټیفنز کالج څخه یې بي اې وکړ. د شعر او شاعرۍ شوق یې د زده کړې پر مهال پیدا شو.'),
    ('Farhatullah Baig had to go to Hyderabad (Deccan) for service, and there he stayed for good. Of his sixty-four years of life he spent forty in Hyderabad. This was the period when, after English domination, Delhi city was passing through a transitional phase culturally. Whenever Farhat came to Delhi he saw ever-new changes; Farhat was devoted to the old culture and found these changes hard to bear. That is why Farhat tried to preserve the old culture in his writings.',
     'فرحت اللہ بیگ کو ملازمت کے سلسلے میں حیدرآباد جانا پڑا۔ اور وہیں کے ہو کر رہ گئے۔ فرحت اللہ بیگ نے اپنی ۶۴ سالہ زندگی میں ۴۰ سال حیدرآباد میں گزارے۔ یہ وہ دور تھا جب انگریزی تسلط کے بعد دِلّی شہر تہذیبی لحاظ سے عبوری دور سے گزر رہا تھا۔ فرحت جب بھی دِلّی آتے اُس میں اُنھیں نت نئی تبدیلیاں نظر آتیں۔ فرحت پُرانی تہذیب کے دلدادہ تھے۔ اُنھیں یہ تبدیلیاں گراں گزرتیں یہی وجہ ہے کہ فرحت نے اپنی تحریروں میں پُرانی تہذیب کو محفوظ کرنے کی کوشش کی ہے۔',
     'فرحت الله بیګ د دندې په تړاو حیدراباد ته لاړ او هلته پاتې شو. فرحت الله بیګ د خپل ۶۴ کلن ژوند ۴۰ کاله په حیدراباد کې تېر کړل. دا هغه وخت و چې د انګرېزانو له واکمنۍ وروسته د ډهلي ښار له کلتوري پلوه د لېږد دوره تېروله. فرحت به چې کله ډهلي ته راغی، نوي نوي بدلونونه به یې پکې لیدل. فرحت د زاړه تهذیب مین و؛ دا بدلونونه ورته دروند و، همدا وجه ده چې فرحت په خپلو لیکنو کې د زاړه تهذیب د ساتلو هڅه کړې.'),
    ('As a humorist Farhatullah Baig has a special place. His writings are models of good humour and wit. Besides this, the pen-portraits (khāke) he wrote are read with great relish; these sketches hold a high place in Urdu literature. In these sketches, instead of endless true-and-false praise of the subject, real events and the subject’s merits, faults and weaknesses are commented on impartially.',
     'مزاح نگار کی حیثیت سے فرحت اللہ بیگ کا ایک خاص مقام ہے۔ اُن کی تحریریں خوش طبعی اور ظرافت کا نمونہ ہیں۔ اس کے علاوہ اُن کے تحریر کردہ خاکے بڑے ذوق و شوق سے پڑھے جاتے ہیں۔ یہ خاکے اُردو ادب میں بلند مقام رکھتے ہیں۔ اِن خاکوں میں ممدوح کی بے پناہ سچی جھوٹی تعریفوں کی بجائے حقیقی واقعات اور ممدوح کی خوبیوں، خامیوں اور کمزوریوں کے بارے میں غیر جانبداری سے تبصرہ کیا گیا ہے۔',
     'د طنز لیکوال په توګه فرحت الله بیګ ځانګړی مقام لري. لیکنې یې د خوش‌طبعۍ او ظرافت بېلګې دي. سربېره پر دې، د هغه لیکلي خاکې (شخصي انځورونه) په ډېر شوق لوستل کېږي؛ دا خاکې په اردو ادب کې لوړ مقام لري. په دې خاکو کې د ستایل شوي کس د بې‌حده رښتینو دروغو ستاینو پر ځای حقیقي پېښې او د هغه ښېګڼې، نیمګړتیاوې او کمزورۍ په بې‌پلوۍ تبصره شوې.'),
]: a.p(*x)
UT = ('Fulfilling a Will', 'ایک وصیّت کی تعمیل', 'د یوې وصیت پلي کول', 'فرحت اللہ بیگ')
au = BOOK.record(a, 'urdu12-u13-author', 'About the author: Farhatullah Baig', 'فرحت اللہ بیگ (تعارف)', 'فرحت الله بیګ (پېژندنه)', 64, [119], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait of Farhatullah Baig and floral border are decorative; not reproduced.'
issues = [{'id': 'urdu12-pdf064', 'unit': 13, 'printedPage': 119, 'description': 'Farhatullah Baig died 1947 — public domain; Lesson 13 will be transcribed in full. P.118 is the asterisked note for Lesson 12 Q5 (* مرکّب جملے); it is placed with Lesson 12. Printed “دوسرا ابیان پہلے بیان کی توسیع” retained as “دوسرا بیان”.'}]

if __name__ == '__main__':
    BOOK.save(64, [(12, gr), (13, au)], issues=issues)
