"""PDF47 (printed 81–82): Unit 8 Glossary (flank … threshold); Reading Comprehension Q1–9; Writing; Oral; Vocabulary A economy words 1–11."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
B = '________'
g = Builder()
gloss(g, 'eng12-u08-gloss-b', [
    ('flank(n)', 'the right or left side of a body of people such as an army, a naval force, or a soccer team', 'لوگوں کے کسی گروہ جیسے فوج، بحری بیڑے یا فٹ بال ٹیم کا دایاں یا بایاں پہلو', 'د خلکو د یوې ډلې لکه لښکر، سمندري ځواک یا فوټبال ټیم ښی یا کیڼ اړخ'),
    ('ignominy(n)', 'Public shame or disgrace', 'عوامی شرمندگی یا رسوائی', 'عامه شرم یا رسوایي'),
    ('manoeuver(n)', 'a clever and planned action, movement or activities to gain advantage or avoid something', 'فائدہ حاصل کرنے یا کسی چیز سے بچنے کے لیے ہوشیاری سے منصوبہ بند عمل، حرکت یا سرگرمیاں', 'د ګټې ترلاسه کولو یا له یو شي د ډډې لپاره هوښیاره او پلان شوې کړنه، حرکت یا فعالیتونه'),
    ('pickets(n)', 'a soldier or small group of soldiers performing a particular duty, especially one sent out to watch for the enemy', 'ایک سپاہی یا سپاہیوں کا چھوٹا گروہ جو کوئی خاص فرض انجام دے، خاص طور پر دشمن پر نظر رکھنے کے لیے بھیجا گیا', 'یو سرتېری یا د سرتېرو کوچنۍ ډله چې یوه ځانګړې دنده ترسره کوي، په ځانګړي ډول د دښمن د څارنې لپاره لېږل شوې'),
    ('pincer movement', 'a movement by two separate bodies of troops converging on the enemy/ a situation involving pressure from two different sides or forces.', 'فوج کے دو الگ دستوں کی دشمن کی طرف یکجا ہونے والی حرکت/ ایسی صورتِ حال جس میں دو مختلف اطراف یا قوتوں سے دباؤ ہو۔', 'د لښکر د دوو جلا ډلو حرکت چې پر دښمن راټولېږي/ داسې حالت چې پکې له دوو بېلابېلو خواوو یا ځواکونو فشار وي.'),
    ('scimitar(n)', 'a short sword with a curved blade that broadens towards the point.', 'خمیدہ پھل والی چھوٹی تلوار جو نوک کی طرف چوڑی ہوتی جاتی ہے۔', 'لنډه توره چې کوږ تیغ لري او د څوکې خوا ته پلنېږي.'),
    ('seething(adj.)', 'filled with or characterized by intense but unexpressed emotions', 'شدید مگر غیر ظاہر جذبات سے بھرا ہوا', 'له شدیدو خو ناڅرګندو احساساتو ډک'),
    ('tambourine(n)', 'an instrument resembling a shallow drum with metal discs in slots around the edge, played by being shaken or hit with the hand.', 'اتھلے ڈھول جیسا ساز جس کے کنارے کے گرد خانوں میں دھاتی گول ٹکڑے ہوتے ہیں، اسے ہلا کر یا ہاتھ سے بجایا جاتا ہے۔', 'د پیکه ډول په څېر یوه اله چې د څنډې شاوخوا په خونو کې فلزي ټیکې لري، په ښورولو یا په لاس وهلو غږول کېږي.'),
    ('threshold(n)', 'A point of entry', 'داخلے کا مقام', 'د ننوتو ځای'),
])
gl = BOOK.record(g, 'eng12-u08-glossary-b', 'Glossary (2)', 'فرہنگ (2)', 'وییپانګه (2)', 47, [81])

q = Builder()
q.h('Reading Comprehension', 'مطالعہ اور فہم', 'لوستل او پوهه')
q.group('lines', [
    ('1. What was the composition of the army of the Qureish that marched to Madina to attack the Muslims?', '1. مسلمانوں پر حملے کے لیے مدینہ کی طرف بڑھنے والے قریش کے لشکر کی ترکیب کیا تھی؟', '1. د قریشو د هغه لښکر جوړښت څه و چې پر مسلمانانو د برید لپاره مدینې ته وخوځېد؟'),
    ('2. Why did the holy Rasool (ﷺ) suggest the defensive strategy in the the battle of a Uhud?', '2. رسولِ پاک (ﷺ) نے غزوۂ احد میں دفاعی حکمتِ عملی کیوں تجویز کی؟', '2. سپیڅلي رسول (ﷺ) د احد په غزا کې ولې دفاعي ستراتیژي وړاندیز کړه؟'),
    ('3. What was the opinion of youth with respect to facing the army of the Quraish?', '3. قریش کے لشکر کا سامنا کرنے کے بارے میں نوجوانوں کی کیا رائے تھی؟', '3. د قریشو له لښکر سره د مخامخ کېدو په اړه د ځوانانو نظر څه و؟'),
    ('4. Why did the holy Rasool (ﷺ) prefer the opinion of youths regarding facing the enemy in the battle of Uhud?', '4. رسولِ پاک (ﷺ) نے غزوۂ احد میں دشمن کا سامنا کرنے کے بارے میں نوجوانوں کی رائے کو کیوں ترجیح دی؟', '4. سپیڅلي رسول (ﷺ) د احد په غزا کې له دښمن سره د مخامخ کېدو په اړه د ځوانانو نظر ولې غوره کړ؟'),
    ('5. How did the course of the battle of Uhud change for a time in favour of the Quraish of Mecca?', '5. غزوۂ احد کا رخ کچھ دیر کے لیے مکہ کے قریش کے حق میں کیسے بدل گیا؟', '5. د احد د غزا بهیر د یو څه وخت لپاره د مکې د قریشو په ګټه څنګه واوښت؟'),
    ('6. What happened after the false rumour about the martyrdom of the holy Rasool (ﷺ) was spread by the Infidels?', '6. کافروں کی طرف سے رسولِ پاک (ﷺ) کی شہادت کی جھوٹی افواہ پھیلائے جانے کے بعد کیا ہوا؟', '6. له هغه وروسته چې کافرانو د سپیڅلي رسول (ﷺ) د شهادت دروغجنه اوازه خپره کړه، څه وشول؟'),
    ('7. What lesson does lie in the battle of Uhud for the Muslims in general?', '7. غزوۂ احد میں عمومی طور پر مسلمانوں کے لیے کیا سبق ہے؟', '7. د احد په غزا کې په عمومي ډول د مسلمانانو لپاره کوم لوست دی؟'),
    ('8. What would have been the result of the battle had the archers not left their high post?', '8. اگر تیر انداز اپنی بلند جگہ نہ چھوڑتے تو جنگ کا نتیجہ کیا ہوتا؟', '8. که غشي‌ویشتونکو خپل لوړ ځای نه وای پرېښی، د جګړې پایله به څه وای؟'),
    ('9. How would you relate the battle of Uhud to the battle of Badr?', '9. آپ غزوۂ احد کو غزوۂ بدر سے کیسے جوڑیں گے؟', '9. تاسو به د احد غزا د بدر له غزا سره څنګه وتړئ؟'),
])
q.h('Writing Suggestions', 'تحریری تجاویز', 'د لیکلو وړاندیزونه')
q.p('Narrate the whole event of the battle of Uhud giving it a proper beginning that may lead to the middle and then to its end.', 'غزوۂ احد کا پورا واقعہ بیان کریں، اسے ایک مناسب آغاز دیں جو درمیان اور پھر انجام تک لے جائے۔', 'د احد د غزا ټوله پېښه بیان کړئ او یو مناسب پیل ورکړئ چې منځ او بیا پای ته ورسوي.')
q.h('Oral Communication', 'زبانی ابلاغ', 'د خولې اړیکه')
q.p('Ask the students to present their written work under "Writing Suggestion" in front of the class.', 'طلبہ سے کہیں کہ ’’تحریری تجویز‘‘ کے تحت اپنا لکھا ہوا کام جماعت کے سامنے پیش کریں۔', 'له زده کوونکو وغواړئ چې د "د لیکلو وړاندیز" لاندې خپل لیکلی کار د ټولګي مخې ته وړاندې کړي.')
q.h('Vocabulary and Grammar', 'ذخیرۂ الفاظ اور قواعد', 'لغات او ګرامر')
q.p('A. Search the following words related to Economy in an authentic source and write the correct word in front of its meaning below.', 'A. معیشت سے متعلق درج ذیل الفاظ کسی مستند ذریعے میں تلاش کریں اور نیچے ہر معنی کے سامنے درست لفظ لکھیں۔', 'A. له اقتصاد سره تړلې لاندې کلمې په یوه معتبره سرچینه کې ولټوئ او لاندې د هرې مانا مخې ته سمه کلمه ولیکئ.')
WB = [['bankrupt', 'investment', 'budget', 'capital', 'cost'], ['Economics', 'consumer', 'fiscal', 'inflation', 'deposit'], ['deficit', 'finance', 'credit', 'currency', 'recession'], ['Stock', '', '', '', '']]
H = [''] * 5
q.table('eng12-u08-econ-box', H, WB, H, H, WB, WB, noHeader=True)
EC = [
    ('a continual increase in the price of goods and services', 'اشیاء اور خدمات کی قیمت میں مسلسل اضافہ', 'د توکو او خدمتونو په بیه کې دوامداره زیاتوالی'),
    ('a period of time in which there is a decrease in economic activity and many people do not have jobs', 'وہ دور جس میں معاشی سرگرمی کم ہو جائے اور بہت سے لوگ بے روزگار ہوں', 'هغه دوره چې پکې اقتصادي فعالیت کمېږي او ډېر خلک دندې نه لري'),
    ('a person who buys goods and services', 'وہ شخص جو اشیاء اور خدمات خریدتا ہے', 'هغه کس چې توکي او خدمتونه اخلي'),
    ('a science concerned with the process or system by which goods and services are produced, sold, and bought', 'وہ علم جو اس عمل یا نظام سے متعلق ہے جس کے ذریعے اشیاء اور خدمات پیدا، فروخت اور خریدی جاتی ہیں', 'هغه علم چې د هغه بهیر یا سیستم په اړه دی چې توکي او خدمتونه پرې تولیدېږي، پلورل کېږي او اخیستل کېږي'),
    ('an amount (such as an amount of money) that is less than the amount that is needed', 'ایسی مقدار (مثلاً رقم) جو ضرورت سے کم ہو', 'داسې اندازه (لکه د پیسو اندازه) چې له اړتیا کمه وي'),
    ('an amount of money available for spending that is based on a plan for how it will be spent', 'خرچ کے لیے دستیاب رقم جو اس منصوبے پر مبنی ہو کہ اسے کیسے خرچ کیا جائے گا', 'د لګښت لپاره شته پیسې چې د هغه پلان پر بنسټ وي چې څنګه به ولګول شي'),
    ('money that a bank or business will allow a person to use and then pay back in the future', 'وہ رقم جسے بینک یا کاروبار کسی شخص کو استعمال کرنے اور بعد میں واپس کرنے کی اجازت دے', 'هغه پیسې چې بانک یا سوداګري یو کس ته د کارولو اجازه ورکوي او وروسته بېرته ورکول کېږي'),
    ('money, property, etc., that is used to start or operate a business', 'رقم، جائیداد وغیرہ جو کاروبار شروع کرنے یا چلانے کے لیے استعمال ہو', 'پیسې، شتمني او نور چې د سوداګرۍ د پیل یا چلولو لپاره کارول کېږي'),
    ('of or relating to money and especially to the money a government, business, or organization earns, spends, and owes', 'رقم سے متعلق، خاص طور پر اس رقم سے جو کوئی حکومت، کاروبار یا ادارہ کماتا، خرچ کرتا اور جس کا مقروض ہوتا ہے', 'له پیسو سره تړلی، په ځانګړي ډول هغه پیسې چې یو حکومت، سوداګري یا سازمان ګټي، لګوي او پوروړی یې وي'),
    ('the act of using money to earn more money: the act of investing money', 'مزید رقم کمانے کے لیے رقم استعمال کرنے کا عمل: سرمایہ کاری کا عمل', 'د ډېرو پیسو د ګټلو لپاره د پیسو کارول: د پانګونې عمل'),
    ('the money that a country uses: a specific kind of money', 'وہ رقم جو کوئی ملک استعمال کرتا ہے: رقم کی ایک خاص قسم', 'هغه پیسې چې یو هېواد یې کاروي: د پیسو یو ځانګړی ډول'),
]
q.group('lines', [(f'{i}. {e} {B}', f'{i}. {u} {B}', f'{i}. {p} {B}') for i, (e, u, p) in enumerate(EC, 1)])
qs = BOOK.record(q, 'eng12-u08-comprehension', 'Reading Comprehension; Writing; Oral; Vocabulary A (1)', 'مطالعہ اور فہم؛ تحریر؛ زبانی ابلاغ؛ ذخیرۂ الفاظ A (1)', 'لوستل او پوهه؛ لیکنه؛ د خولې اړیکه؛ لغات A (1)', 47, [81, 82])
issues = [{'id': 'eng12-p81-82', 'unit': 8, 'printedPage': 81, 'description': 'Printed text retained: Q2 “the the battle of a Uhud”, Q7 “What lesson does lie”, spellings “Qureish / Quraish / Badr”.'}]

if __name__ == '__main__':
    BOOK.save(47, [(8, gl), (8, qs)], issues=issues)
