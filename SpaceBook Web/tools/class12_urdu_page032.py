"""Urdu XII PDF32 (spread): p.54 Lesson 7 author note (سعادت حسن منٹو, 1912–1955); p.55 'منظور' text part 1 + hospital illustration."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
a.h('Saadat Hasan Manto', 'سعادت حسن منٹو', 'سعادت حسن منټو')
a.p('Born: 1912 · Died: 1955', 'ولادت: ۱۹۱۲ء · وفات: ۱۹۵۵ء', 'زېږېدنه: ۱۹۱۲ز · مړینه: ۱۹۵۵ز')
for x in [
    ("Saadat Hasan Manto was born in the village of Sambrala (Ludhiana). His father's name was Khwaja Ghulam Hasan. Manto's early education took place at home. Manto's academic record was not very good, and the surprising thing is that he often failed in Urdu. Manto was interested in literature from his student days. He began his literary life with translations of foreign stories, but soon began to write creative stories. Besides this he went on earning money by writing stories for radio and films. After the creation of Pakistan he moved from Bombay to Lahore. Manto's last years passed in great poverty.",
     'سعادت حسن منٹو موضع سمبرالا (لدھیانہ) میں پیدا ہوئے۔ والد کا نام خواجہ غلام حسن تھا۔ منٹو کی ابتدائی تعلیم گھر پر ہی ہوئی۔ منٹو کا تعلیمی ریکارڈ کچھ زیادہ اچھا نہ تھا اور حیرت کی بات یہ ہے کہ وہ اُردو میں اکثر فیل ہوتے تھے۔ منٹو کو زمانۂ طالب علمی سے ہی ادب سے دلچسپی تھی۔ اُنھوں نے ادبی زندگی کا آغاز غیر ملکی کہانیوں کے تراجم سے کیا لیکن جلد ہی وہ تخلیقی کہانیاں لکھنے لگے۔ اس کے علاوہ ریڈیو اور فلموں کے لیے کہانیاں لکھ کر پیسے کماتے رہے۔ قیامِ پاکستان کے بعد وہ بمبئی سے لاہور منتقل ہو گئے۔ منٹو کی آخری عمر بڑی کسمپرسی کی حالت میں گزری۔',
     'سعادت حسن منټو د سمبرالا (لدهیانه) کلي کې زېږېدلی. د پلار نوم یې خواجه غلام حسن و. د منټو لومړنۍ زده کړې په کور کې وشوې. د منټو تعلیمي ریکارډ ډېر ښه نه و، او د حیرانتیا خبره دا ده چې په اردو کې به ډېری وخت ناکام کېده. منټو ته د زده کړې له وخته ادب سره لېوالتیا وه. ادبي ژوند یې د بهرنیو کیسو په ژباړو پیل کړ، خو ژر یې تخلیقي کیسې لیکل پیل کړل. سربېره پر دې یې د راډیو او فلمونو لپاره کیسې لیکلې او پیسې یې ګټلې. د پاکستان له جوړېدو وروسته له بمبۍ لاهور ته کډه شو. د منټو وروستي کلونه په ډېره بېوزلۍ کې تېر شول.'),
    ('Manto is an important and controversial short-story writer of Urdu literature. Critics call him a progressive, but the Progressives refuse to accept him. He was fully aware of human life and its psychology. He made harsh reality his subject without mercy and startled readers. He was an artist of sensitive temperament and keen observation. Manto’s works and creations have been translated into various languages.',
     'منٹو اُردو ادب کا ایک اہم اور متنازعہ افسانہ نگار ہے۔ نقاد اُنھیں ترقی پسند کہتے ہیں لیکن ترقی پسند اُنھیں قبول کرنے سے انکاری ہیں۔ وہ انسانی زندگی اور اس کی نفسیات سے پوری طرح آگاہ ہیں۔ اُنھوں نے کھردری حقیقت کو بے رحمی سے موضوع بنایا اور قارئین کو چونکایا۔ وہ ایک حساس طبع اور باریک مشاہدے کا فنکار تھا۔ منٹو کی تصانیف اور تخلیقات مختلف زبانوں میں ترجمہ ہوئی ہیں۔',
     'منټو د اردو ادب یو مهم او شخړه‌لرونکی لنډې کیسې لیکونکی دی. نقادان یې پرمختګ‌پال بولي خو پرمختګ‌پال یې له منلو انکار کوي. هغه د انسان له ژوند او ارواپوهنې سره بشپړ اشنا دی. هغه زیږ حقیقت په بې‌رحمۍ سره موضوع کړ او لوستونکي یې حیران کړل. هغه د حساس طبیعت او دقیقې کتنې هنرمند و. د منټو تصنیفات او تخلیقات بېلابېلو ژبو ته ژباړل شوي.'),
    ('Works: Atish Pare, Manto ke Afsane, Dhuan, Lazzat-e-Sang, Chughad, Thanda Gosht, Yazid, Namrud ki Khudai, Badshahat ka Khatma, etc.', 'تصانیف: آتش پارے، منٹو کے افسانے، دھواں، لذتِ سنگ، چغد، ٹھنڈا گوشت، یزید، نمرود کی خُدائی، بادشاہت کا خاتمہ وغیرہ۔', 'تصنیفات: اتش پارې، د منټو افسانې، لوګی، لذت سنګ، چغد، سړه غوښه، یزید، د نمرود خدايي، د پاچاهۍ پای او نور.'),
]: a.p(*x)
UT = ('Manzoor', 'منظور', 'منظور', 'سعادت حسن منٹو')
au = BOOK.record(a, 'urdu12-u7-author', 'About the author: Saadat Hasan Manto', 'سعادت حسن منٹو (تعارف)', 'سعادت حسن منټو (پېژندنه)', 32, [54], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait of Manto and floral border are decorative; not reproduced.'

t = Builder()
t.h('Manzoor — Saadat Hasan Manto', 'منظور — سعادت حسن منٹو', 'منظور — سعادت حسن منټو')
for x in [
    ('When he was admitted to the hospital his condition was very bad. The first night he was put on oxygen. Nurse Jones was on duty; she thought this new patient would die before morning. His pulse was uncertain — sometimes it fluttered violently and sometimes it beat after long pauses.',
     'جب اسے ہسپتال میں داخل کیا گیا تو اس کی حالت بہت خراب تھی۔ پہلی رات اسے اوکسیجن پر رکھا گیا۔ جونز ڈیوٹی پر تھی، اس کا خیال تھا کہ یہ نیا مریض صبح سے پہلے پہلے مر جائے گا۔ اس کی نبض کی رفتار غیر یقینی تھی۔ کبھی زور زور سے پھڑ پھڑاتی اور کبھی لمبے لمبے وقفوں کے بعد چلتی تھی۔',
     'کله چې روغتون ته داخل شو، حالت یې ډېر خراب و. لومړۍ شپه یې پر اکسیجن کېښود. نرس جونز په دنده وه؛ هغې فکر کاوه چې دا نوی ناروغ به له سهاره مخکې مړ شي. د هغه نبض بې‌باوره و — کله به په زوره رپېده او کله به له اوږدو وقفو وروسته چلېده.'),
    ('His body was drenched in sweat; he found no rest even for a moment. Sometimes he turned on this side, sometimes on that. When his restlessness grew too great he would sit up and begin taking long, deep breaths. His colour was yellow like a lump of turmeric. His eyes were sunken. The bridge of his nose was like a lump of ice. His whole body trembled.',
     'پسینے میں اس کا بدن شرابور تھا، ایک لحظے کے لیے بھی اسے چین نہیں ملتا تھا۔ کبھی اس کروٹ لیٹتا، کبھی اس کروٹ۔ جب گھبراہٹ بہت زیادہ بڑھ جاتی تو اٹھ کر بیٹھ جاتا اور لمبے لمبے سانس لینے لگتا۔ رنگ اس کا ہلدی کی گانٹھ کی طرح زرد تھا۔ آنکھیں اندر دھنسی ہوئیں۔ ناک کا بانسا برف کی ڈلی۔ سارے بدن پر رعشہ تھا۔',
     'بدن یې له خولو لوند و؛ یوه شېبه هم ارام نه کېده. کله به په یوه اړخ پرېوت، کله په بل. کله چې به یې وارخطايي ډېره شوه، کېناست به او اوږده اوږده ساه به یې اخیسته. رنګ یې د زرچوبې د غوټې په څېر ژېړ و. سترګې یې ننوتې وې. د پوزې هډوکی یې د یخ ټوټه و. په ټول بدن یې رېږدېدنه وه.'),
]: t.p(*x)
tx = BOOK.record(t, 'urdu12-u7-text-1', 'Lesson text (1)', 'متنِ سبق (۱)', 'د لوست متن (۱)', 32, [55])
tx['sourceCoverIllustrationReview'] = 'Line drawing (p.55): a nurse in a head-covering stands beside a hospital bed in which a young man lies with a drip stand behind him. Illustrative only; not reproduced.'
issues = [{'id': 'urdu12-pdf032', 'unit': 7, 'printedPage': 54, 'description': 'Lesson 7 is Manto’s story “منظور” (the legacy dataset wrongly titled it “نیا قانون”). Manto died in 1955; under Pakistani copyright (life + 50 years) the story is public domain and is transcribed in full.'}]

if __name__ == '__main__':
    BOOK.save(32, [(7, au), (7, tx)], issues=issues)
