"""PDF24 (printed 35–36): 'Truck Art' (end) — summary; About the author; Glossary (alteration … boom)."""
from class12_book_common import Book, Builder, gloss

BOOK = Book('english')
r = Builder()
S = [
    ('The festival truck, a Bedford chosen for showing several regional styles, became part of the Smithsonian’s permanent collection. Karachi is the main centre, but each region has its own idiom: Peshawar favours calligraphy, Rawalpindi and Islamabad use cut plastic patterns, Baluchistan and Peshawar are known for carved woodwork, Sindh for camel-bone inlay, and Sindh and the Punjab for steel peacock appliqués.',
     'فیسٹیول کا ٹرک، ایک بیڈفورڈ جسے کئی علاقائی انداز دکھانے کے لیے چنا گیا، اسمتھسونین کے مستقل ذخیرے کا حصہ بن گیا۔ کراچی مرکزی مرکز ہے، لیکن ہر علاقے کا اپنا انداز ہے: پشاور میں خطاطی پسند کی جاتی ہے، راولپنڈی اور اسلام آباد میں کٹے ہوئے پلاسٹک کے نقش، بلوچستان اور پشاور لکڑی پر نقش و نگار کے لیے مشہور ہیں، سندھ اونٹ کی ہڈی کی جڑاؤ کاری کے لیے، اور سندھ و پنجاب اسٹیل کے مور کے نقوش کے لیے۔',
     'د فستیوال ټرک، یو بیډفورډ چې د ګڼو سیمه‌ییزو بڼو د ښودلو لپاره ټاکل شوی و، د سمیتسونین د دایمي ټولګې برخه شو. کراچۍ اصلي مرکز دی، خو هره سیمه خپل سبک لري: پېښور خطاطي خوښوي، راولپنډۍ او اسلام اباد پرې شوي پلاستیکي نقشونه کاروي، بلوچستان او پېښور په لرګیو د کندنکارۍ لپاره مشهور دي، سند د اوښ د هډوکي د جوړښت لپاره، او سند او پنجاب د فولادي طاووس نقشونو لپاره.'),
    ('Truck art grew over the decades: in the 1940s companies painted logos so that mostly illiterate people could recognize them; after 1947 trucks showed national pride; in the 1950s Haji Hussain, once a palace muralist in Gujarat, began painting trucks with floral borders in Karachi; and the 1960s transport boom made the durable Bedford truck the favourite, its decoration growing ever more elaborate as owners prospered.',
     'ٹرک آرٹ دہائیوں میں پروان چڑھا: 1940 کی دہائی میں کمپنیوں نے لوگو بنائے تاکہ زیادہ تر ناخواندہ لوگ انہیں پہچان سکیں؛ 1947 کے بعد ٹرکوں نے قومی فخر کا اظہار کیا؛ 1950 کی دہائی میں حاجی حسین، جو پہلے گجرات کے محلات میں دیواری تصویریں بناتے تھے، نے کراچی میں ٹرکوں پر پھولوں کی کناریاں بنانا شروع کیں؛ اور 1960 کی دہائی کی نقل و حمل کی ترقی نے مضبوط بیڈفورڈ ٹرک کو پسندیدہ بنا دیا، جس کی سجاوٹ مالکان کی خوشحالی کے ساتھ مزید پیچیدہ ہوتی گئی۔',
     'د ټرک هنر د لسیزو په اوږدو کې وده وکړه: په 1940 لسیزه کې شرکتونو نښې رنګ کړې ترڅو ډېری نالوستي خلک یې وپېژني؛ له 1947 وروسته ټرکونو ملي ویاړ ښکاره کړ؛ په 1950 لسیزه کې حاجي حسین، چې پخوا یې د ګجرات په ماڼیو کې دېوالي انځورونه جوړول، په کراچۍ کې پر ټرکونو د ګلانو د څنډو رنګول پیل کړل؛ او د 1960 لسیزې د ترانسپورت ودې ټینګ بیډفورډ ټرک غوره کړ، چې ښکلا یې د مالکانو د سوکالۍ سره ډېره پېچلې شوه.'),
    ('In the twenty-first century truck art has reached a peak of colour and skill. Like all art, it offers lasting beauty; its static panels let passers-by step briefly from a passing world into a permanent one, and the author hopes the tradition will pass on to future artists.',
     'اکیسویں صدی میں ٹرک آرٹ رنگ اور مہارت کے عروج پر پہنچ گیا ہے۔ تمام فنون کی طرح یہ دیرپا خوبصورتی پیش کرتا ہے؛ اس کے ساکن تختے راہگیروں کو تھوڑی دیر کے لیے فانی دنیا سے دائمی دنیا میں لے جاتے ہیں، اور مصنفہ امید کرتی ہیں کہ یہ روایت آئندہ فنکاروں تک منتقل ہو گی۔',
     'په یوویشتمه پېړۍ کې د ټرک هنر د رنګ او مهارت لوړې څوکې ته رسېدلی. د ټولو هنرونو په څېر دا تلپاتې ښکلا وړاندې کوي؛ د هغه ثابت تختې تېرېدونکي د لنډ وخت لپاره له فاني نړۍ څخه تلپاتې نړۍ ته وړي، او لیکواله هیله لري چې دا دود به راتلونکو هنرمندانو ته ولېږدول شي.'),
]
for x in S: r.p(*x)
rd = BOOK.record(r, 'eng12-u04-text-summary-b', 'Reading text — summary (Truck Art, end)', 'متن — خلاصہ (ٹرک آرٹ، اختتام)', 'متن — لنډیز (د ټرک هنر، پای)', 24, [35, 36])
rd['sourceGap'] = 'Modern copyrighted essay (Rachel Redford); paragraph-wise summary, not verbatim.'

a = Builder()
a.h('About the author:', 'مصنفہ کے بارے میں:', 'د لیکوالې په اړه:')
a.p("Rachel Redford has extensive experience in English language and literature teaching and assessments. She is the author of the secondary textbook series Oxford English: An international approach from the Oxford University Press UK. She has also written two Student Books and a Teacher's Guide for Oxford University Press to accompany the General Certificate of Secondary Education (GCSE) syllabus in the UK. Her other publications include Texts from Other Cultures, a collection of extracts from writings across the world. Rachel Redford also reviews audio books for British journals. She lives in Carisbrooke on the Isle of Wight in England.",
    'ریچل ریڈفورڈ کو انگریزی زبان و ادب کی تدریس اور جائزوں کا وسیع تجربہ ہے۔ وہ آکسفورڈ یونیورسٹی پریس برطانیہ کی ثانوی درسی کتب کی سیریز ’’آکسفورڈ انگلش: این انٹرنیشنل اپروچ‘‘ کی مصنفہ ہیں۔ انہوں نے برطانیہ میں جنرل سرٹیفکیٹ آف سیکنڈری ایجوکیشن (GCSE) کے نصاب کے ساتھ آکسفورڈ یونیورسٹی پریس کے لیے دو طلبہ کی کتابیں اور ایک اساتذہ کی رہنما کتاب بھی لکھی ہے۔ ان کی دیگر تصانیف میں ’’ٹیکسٹس فرام ادر کلچرز‘‘ شامل ہے، جو دنیا بھر کی تحریروں کے اقتباسات کا مجموعہ ہے۔ ریچل ریڈفورڈ برطانوی رسائل کے لیے آڈیو کتابوں پر تبصرے بھی کرتی ہیں۔ وہ انگلستان کے جزیرۂ وائٹ پر کیرس بروک میں رہتی ہیں۔',
    'ریچل ریډفورډ د انګلیسي ژبې او ادب په تدریس او ارزونو کې پراخه تجربه لري. هغه د انګلستان د اکسفورډ پوهنتون پرېس د ثانوي درسي کتابونو د "اکسفورډ انګلیش: یو نړیوال لید" لړۍ لیکواله ده. هغې په انګلستان کې د ثانوي زده کړې د عمومي سند (GCSE) د نصاب سره د اکسفورډ پوهنتون پرېس لپاره دوه د زده کوونکو کتابونه او د ښوونکي لارښود هم لیکلي. د هغې نورو خپرونو کې "له نورو کلتورونو متنونه" شامل دي چې د نړۍ له لیکنو د اقتباسونو ټولګه ده. ریچل ریډفورډ د برتانوي مجلو لپاره پر غږیزو کتابونو بیاکتنې هم کوي. هغه د انګلستان د وایټ ټاپو په کېرس‌بروک کې اوسېږي.')
GL = [
    ('alteration(n)', 'a change to something that makes it different', 'کسی چیز میں ایسی تبدیلی جو اسے مختلف بنا دے', 'په یو شي کې داسې بدلون چې بېل یې کړي'),
    ('anthropology(n)', 'the study of the human race, especially of its origins, development, customs and beliefs', 'نسلِ انسانی کا مطالعہ، خاص طور پر اس کی ابتدا، ارتقا، رسوم اور عقائد کا', 'د انسان نسل مطالعه، په ځانګړي ډول د هغه د پیل، ودې، دودونو او باورونو'),
    ('apogee(n)', 'the highest point of something, where it is greatest or most successful', 'کسی چیز کا بلند ترین مقام جہاں وہ سب سے عظیم یا کامیاب ہو', 'د یو شي تر ټولو لوړ ټکی، چې هلته تر ټولو لوی یا بریالی وي'),
    ('appliqué(n)', 'a type of needlework in which small pieces of cloth are sewn or stuck in a pattern onto a larger piece', 'سوئی کاری کی ایک قسم جس میں کپڑے کے چھوٹے ٹکڑوں کو کسی بڑے ٹکڑے پر نقش کی صورت میں سیا یا چپکایا جاتا ہے', 'د ګنډلو یو ډول چې پکې د ټوکر کوچنۍ ټوټې د نقش په بڼه پر لویه ټوټه ګنډل یا سرېښل کېږي'),
    ('arabesque(n)', 'a type of design where lines wind around each other', 'ایک قسم کا نقش جس میں لکیریں ایک دوسرے کے گرد لپٹتی ہیں', 'د نقش یو ډول چې پکې کرښې یو د بل شاوخوا تاوېږي'),
    ('artefact(n)', 'an object that is made by a person, especially something of historical or cultural interest', 'انسان کی بنائی ہوئی شے، خاص طور پر تاریخی یا ثقافتی اہمیت کی حامل', 'د انسان جوړ کړی شی، په ځانګړي ډول د تاریخي یا کلتوري ارزښت لرونکی'),
    ('blaring(adj.)', 'to make a loud unpleasant noise', 'زور دار ناخوشگوار شور کرنا', 'لوړ ناخوښه غږ کول'),
    ('boom(n)', 'to have a period of rapid growth', 'تیز رفتار ترقی کا دور ہونا', 'د چټکې ودې دوره لرل'),
]
a.h('Glossary', 'فرہنگ', 'وییپانګه')
gloss(a, 'eng12-u04-gloss-a', GL)
ab = BOOK.record(a, 'eng12-u04-author-glossary-a', 'About the author; Glossary (1)', 'مصنفہ کے بارے میں؛ فرہنگ (1)', 'د لیکوالې په اړه؛ وییپانګه (1)', 24, [36])

if __name__ == '__main__':
    BOOK.save(24, [(4, rd), (4, ab)])
