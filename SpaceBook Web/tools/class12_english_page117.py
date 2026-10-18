"""PDF117 (printed 221–222): Lord of the Flies — Chapter 12 end; Glossary ascent–demoniac."""
from class12_english_lotf import BOOK, NOTE, T
from class12_book_common import Builder, gloss

s = Builder()
for x in [
    ('The officer is shocked that two were killed and offers to take them off the island. Asked who is boss, Ralph says he is; he does not know how many boys there are. The officer remarks that British boys should have “put up a better show”; Ralph says it was like that at first, when they were together.',
     'افسر دو کے مارے جانے پر حیران ہوتا ہے اور انہیں جزیرے سے لے جانے کی پیشکش کرتا ہے۔ یہ پوچھنے پر کہ سربراہ کون ہے، رالف کہتا ہے کہ وہ ہے؛ اسے معلوم نہیں کہ کتنے لڑکے ہیں۔ افسر کہتا ہے کہ برطانوی لڑکوں کو ’’بہتر کارکردگی‘‘ دکھانی چاہیے تھی؛ رالف کہتا ہے کہ شروع میں ایسا ہی تھا، جب وہ اکٹھے تھے۔',
     'افسر د دوو کسانو په وژل کېدو حیران کېږي او وړاندیز کوي چې له ټاپو یې یوسي. کله چې پوښتي مشر څوک دی، رالف وايي زه یم؛ نه پوهېږي چې څو هلکان دي. افسر وايي چې بریتانوي هلکانو باید "ښه کارنامه" ښودلې وای؛ رالف وايي چې په پیل کې همداسې و، کله چې یوځای وو.'),
    ('Ralph breaks down and weeps for the end of innocence, the darkness of man’s heart, and the loss of Simon and Piggy; the other boys sob too. The embarrassed officer turns away and looks at his trim cruiser in the distance. — END —',
     'رالف رو پڑتا ہے اور معصومیت کے خاتمے، انسان کے دل کی تاریکی، اور سائمن اور پگی کے بچھڑ جانے پر آنسو بہاتا ہے؛ دوسرے لڑکے بھی سسکنے لگتے ہیں۔ شرمندہ افسر منہ پھیر لیتا ہے اور دور اپنے صاف ستھرے جنگی جہاز کو دیکھتا ہے۔ — اختتام —',
     'رالف ژړا ته ماتېږي او د بې‌ګناهۍ پای، د انسان د زړه تیاره، او د سایمن او پګي د له لاسه ورکولو لپاره اوښکې تویوي؛ نور هلکان هم سلګۍ وهي. شرمېدلی افسر مخ اړوي او لرې خپلې پاکې جنګي کښتۍ ته ګوري. — پای —'),
]: s.p(*x)
r1 = BOOK.record(s, 'eng12-u19-ch12-c', *T('Chapter 12 (summary, 3)', 'باب 12 (خلاصہ، 3)', 'څپرکی 12 (لنډیز، 3)'), 117, [221])
r1['sourceGap'] = NOTE.format(221)

g = Builder()
g.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(g, 'eng12-u19-gloss-a', [
    ('ascent (n)', 'an upward slope or moment', 'اوپر کی طرف ڈھلوان یا حرکت', 'پورته خوا ته ژوروالی یا حرکت'),
    ('abominable(adj.)', 'detestable', 'قابلِ نفرت', 'د کرکې وړ'),
    ('astonishment(n)', 'surprise', 'حیرت', 'حیرانتیا'),
    ('agony(n)', 'acute physical or mental pain.', 'شدید جسمانی یا ذہنی درد۔', 'سخت جسمي یا ذهني درد.'),
    ('brandished(v)', 'waved aggressively', 'جارحانہ انداز میں لہرایا', 'په تېریدونکي ډول وښوراوه'),
    ('bulge(n)', 'swell outwards', 'باہر کی طرف پھولنا', 'بهر ته پړسېدل'),
    ('babble(v)', 'talk foolishly', 'بے وقوفانہ باتیں کرنا', 'احمقانه خبرې کول'),
    ('bough(n)', 'branches', 'شاخیں', 'څانګې'),
    ('bunched(adj.)', 'gathered together in a cluster', 'ایک گچھے میں اکٹھے', 'په یوه ګېډۍ کې سره راټول'),
    ('covert(n)', 'covering', 'چھپنے کی جگہ؛ پردہ', 'پټنځای؛ پوښ'),
    ('cascade (n)', 'shower', 'بوچھاڑ', 'ورښت'),
    ('corpulent(adj.)', 'excessively fat', 'بہت زیادہ موٹا', 'ډېر چاغ'),
    ('cinders(n)', 'a small piece of partly burnt coal or wood that has stopped giving off flames but still has combustible matter in it.', 'جزوی طور پر جلے کوئلے یا لکڑی کا چھوٹا ٹکڑا جس سے شعلے نکلنا بند ہو گئے ہوں لیکن اس میں ابھی جلنے والا مادہ ہو۔', 'د نیم سوځېدلي سکاره یا لرګي کوچنۍ ټوټه چې لمبې یې بندې شوې خو لا هم د سوځېدو توکي لري.'),
    ('clamoured(v)', 'loud cries made by many people.', 'بہت سے لوگوں کی بلند چیخ پکار۔', 'د ډېرو خلکو لوړې چیغې.'),
    ('contemptuously(adv.)', 'Scornfully', 'حقارت سے', 'په سپکاوي'),
    ('corkscrew(v)', 'move in a zigzag way', 'ٹیڑھے میڑھے انداز میں حرکت کرنا', 'په کږلېچه ډول حرکت کول'),
    ('camouflage(n)', 'modifying the appearance of something to hide its identity.', 'کسی چیز کی شناخت چھپانے کے لیے اس کی ظاہری شکل بدلنا۔', 'د یو شي د پېژندنې د پټولو لپاره د هغه بڼه بدلول.'),
    ('ceremonially(adj.)', 'in a formal manner', 'رسمی انداز میں', 'په رسمي ډول'),
    ('convulsive(adj.)', 'of violent and uncontrollable attack', 'شدید اور بے قابو دورے والا', 'د سخت او بې‌کنټروله حملې'),
    ('carcass(n)', 'the dead body of a slaughtered animal.', 'ذبح کیے گئے جانور کی لاش۔', 'د حلال شوي څاروي مړی.'),
    ('chants(n)', 'uttered with intonation', 'لے کے ساتھ ادا کیے گئے الفاظ', 'په غږ او سُر سره ویل شوي'),
    ('creepers(n)', 'any plant that grows by creeping', 'کوئی بھی پودا جو رینگ کر بڑھتا ہے', 'هر هغه بوټی چې په خزېدو وده کوي'),
    ('deserted( adj.)', 'uninhabited', 'غیر آباد', 'نامېشته'),
    ('demoniac(adj.)', 'as if possessed by a demon', 'جیسے کسی شیطان کے قبضے میں ہو', 'لکه چې د شیطان تر واک لاندې وي'),
])
r2 = BOOK.record(g, 'eng12-u19-glossary-a', 'Glossary (ascent – demoniac)', 'فرہنگ (ascent – demoniac)', 'وییپانګه (ascent – demoniac)', 117, [222])
BOOK.save(117, [(19, r1), (19, r2)], issues=[{'id': 'eng12-p221-222', 'unit': 19, 'printedPage': 222, 'description': 'Glossary retained as printed: “an upward slope or moment” (movement), “bulge(n)”/“clamoured(v)”/“ceremonially(adj.)”/“corkscrew(v)” with mismatched parts of speech, “chants(n) — uttered with intonation”.'}])
