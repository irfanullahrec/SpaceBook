"""Urdu XII PDF36 (spread): printed pp.62–63 — Lesson 7 'منظور' text end."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
t = Builder()
for x in [
    ('…There was no such medicine either. It was Manzoor — paralysed Manzoor, the lower half of whose body had become completely useless, who was under the happy illusion that signs of life were appearing in the lifeless lump of his flesh and skin.',
     '…کوئی دوائی ایسی نہیں تھی۔ وہ منظور تھا، مفلوج منظور، جس کا نچلا دھڑ بالکل ناکارہ ہو چکا تھا، جسے یہ خوش فہمی تھی کہ اس کے گوشت پوست کے بے جان لوتھڑے میں زندگی کے آثار پیدا ہو رہے ہیں۔',
     '…داسې کوم درمل هم نه وو. هغه منظور و، فلج منظور، چې د بدن لاندینۍ نیمایي یې بېخي بې‌کاره شوې وه، او دا خوش‌فهمي یې درلوده چې د هغه د غوښې او پوستکي په بې‌ساه ټوټه کې د ژوند نښې پیدا کېږي.'),
    ('The friendship of Akhtar and Manzoor had grown very deep. In his eyes Manzoor had the rank of a Messiah, who had given him life again and had removed from his heart and mind all those dark clouds in whose shadow he had lived so long a stifled life. His despair had turned into hope; he had come to take an interest in staying alive. He wanted to leave the hospital fully cured and begin to live a healthy life.',
     'اختر اور منظور کی دوستی بہت بڑھ گئی تھی۔ منظور کی ذات اس کی نظروں میں مسیحا کا رتبہ رکھتی تھی کہ جس نے اس کو دوبارہ زندگی عطا کی تھی اور اس کے دل و دماغ سے وہ تمام کالے بادل ہٹا دیے تھے۔ جن کے سائے میں وہ اتنی دیر تک گھٹی گھٹی زندگی بسر کرتا رہا تھا۔ اس کی قنوطیت، رجائیت میں تبدیل ہو گئی تھی، اسے زندہ رہنے سے دلچسپی ہو گئی تھی۔ وہ چاہتا تھا کہ بالکل ٹھیک ہو کر ہسپتال سے نکلے اور ایک صحت مند زندگی بسر کرنی شروع کر دے۔',
     'د اختر او منظور دوستي ډېره زیاته شوې وه. د منظور شخصیت د هغه په نظر کې د مسیحا مقام درلود چې هغه ته یې بیا ژوند ورکړی و او د هغه له زړه او ذهن څخه یې هغه ټولې تورې ورېځې لرې کړې وې چې د هغو په سیوري کې یې دومره وخت ځپلی ژوند تېر کړی و. د هغه نا امیدي په هیله بدله شوې وه؛ ژوندي پاتې کېدو ته یې لېوالتیا پیدا شوې وه. غوښتل یې چې بشپړ روغ له روغتونه ووځي او یو روغ ژوند پیل کړي.'),
    ('It troubled him greatly when he saw that Manzoor was just the same as before. Massage was done every day on the paralysed part of his body. As time passed, his cheerful nature grew ever more blooming. This was a cause of wonder and perplexity.',
     'اسے بڑی الجھن ہوتی تھی جب وہ دیکھتا تھا کہ منظور ویسے کا ویسا ہے۔ اس کے جسم کے مفلوج حصے پر ہر روز مالش ہوتی تھی۔ جوں جوں وقت گزرتا تھا، اس کی خوش رہنے والی طبیعت شگفتہ سے شگفتہ تر ہو رہی تھی۔ یہ بات حیرت اور الجھن کا باعث تھی۔',
     'هغه ته به ډېره پرېشاني پیدا شوه کله چې به یې لیدل چې منظور هماغسې دی. د هغه د بدن پر فلج برخه به هره ورځ مالش کېده. څومره چې وخت تېرېده، د هغه خوشحاله طبیعت لا غوړېدلی کېده. دا خبره د حیرانتیا او پرېشانۍ لامل وه.'),
    ('One day the senior doctor told Manzoor’s father that he should now take him home, because his treatment was not possible.',
     'ایک دن بڑے ڈاکٹر نے منظور کے باپ سے کہا کہ اب وہ اسے گھر لے جائے کیونکہ اس کا علاج نہیں ہو سکتا۔',
     'یوه ورځ لوی ډاکټر د منظور پلار ته وویل چې اوس دې کور ته یوسي، ځکه چې درملنه یې نه کېږي.'),
    ('Manzoor learnt only this much: that his treatment would now be at home instead of in hospital and he would get well very soon. But he received a severe shock. He did not want to go home. When Akhtar asked him why he wanted to stay in hospital, tears came into his eyes: “There I shall be alone. Abba goes to the shop; Mother goes to the neighbour’s to sew clothes. With whom shall I play there, with whom shall I talk?”',
     'منظور کو صرف اتنا پتہ چلا کہ اب اس کا علاج ہسپتال کے بجائے گھر پر ہوگا اور بہت جلد ٹھیک ہو جائے گا۔ مگر اسے سخت صدمہ پہنچا۔ وہ گھر جانا نہیں چاہتا تھا۔ اختر نے جب اس سے پوچھا کہ وہ ہسپتال میں کیوں رہنا چاہتا ہے تو اس کی آنکھوں میں آنسو آ گئے۔ ’’وہاں اکیلا رہوں گا۔ ابا دکان پر جاتا ہے، ماں ہمسائی کے ہاں جا کر کپڑے سیتی ہے، میں وہاں کس سے کھیلا کروں گا، کس سے باتیں کروں گا‘‘؟',
     'منظور یوازې دومره وپوهېد چې اوس به یې درملنه د روغتون پر ځای په کور کې کېږي او ډېر ژر به روغ شي. خو سخته صدمه یې ولیده. کور ته تلل یې نه غوښتل. کله چې اختر ترې وپوښتل چې ولې په روغتون کې پاتې کېدل غواړي، سترګې یې له اوښکو ډکې شوې: "هلته به یوازې یم. ابا دوکان ته ځي، مور د ګاونډۍ کور ته ځي او جامې ګنډي. هلته به له چا سره لوبې کوم، له چا سره به خبرې کوم؟"'),
    ('Akhtar said very lovingly: “When you get well, Manzoor mian — it is a matter of a few days — then you will play with your friends outside and go to school.”',
     'اختر نے بڑے پیار سے کہا: ’’تم اچھے جو ہو جاؤ گے منظور میاں۔ چند دن کی بات ہے پھر تم باہر اپنے دوستوں سے کھیلا کرنا۔ اسکول جایا کرنا‘‘۔',
     'اختر په ډېره مینه وویل: "کله چې روغ شې، منظور میاں — د څو ورځو خبره ده — بیا به بهر له خپلو ملګرو سره لوبې کوې او ښوونځي ته به ځې."'),
    ('“No, no.” Manzoor covered his ever-glowing face with the blanket and began to cry. Akhtar was very grieved. For a long time he kept soothing and coaxing him. At last his voice choked in his throat and he turned over.',
     '’’نہیں نہیں‘‘۔ منظور نے کمبل سے اپنا سدا تمتمانے والا چہرہ ڈھانپ کر رونا شروع کر دیا۔ اختر کو بہت دکھ ہوا۔ دیر تک وہ اسے چمکارتا پچکارتا رہا۔ آخر اس کی آواز گلے میں رندھ گئی اور اس نے کروٹ بدل لی۔',
     '"نه نه." منظور خپل تل ځلېدونکی مخ په کمبل پټ کړ او ژړا یې پیل کړه. اختر ډېر غمجن شو. ډېر وخت یې هغه ته تسلي ورکوله او نازوله. په پای کې یې غږ په ستوني کې بند شو او اړخ یې واړاوه.'),
    ('In the evening the house surgeon told Akhtar that the senior doctor sahib had given the order for his release; he could go in the morning. When Manzoor heard it he was very happy.',
     'شام کو ہاؤس سرجن نے اختر کو بتایا کہ بڑے ڈاکٹر صاحب نے اس کی ریلیز کا آرڈر دے دیا ہے۔ وہ صبح جا سکتا ہے۔ منظور نے سنا تو بہت خوش ہوا۔',
     'ماښام هاوس سرجن اختر ته وویل چې لوی ډاکټر صاحب د هغه د رخصت امر ورکړی؛ سهار تللی شي. منظور چې واورېدل، ډېر خوشحاله شو.'),
    ('He talked so much, so much that he grew tired. To every nurse, every student, every sweeper he told that Bhai jan Akhtar was going.',
     'اس نے اتنی باتیں کیں، اتنی باتیں کیں کہ تھک گیا۔ ہر نرس کو، ہر اسٹوڈنٹ کو، ہر جمعدار کو اس نے بتایا کہ بھائی جان اختر جا رہے ہیں۔',
     'هغه دومره خبرې وکړې، دومره خبرې وکړې چې ستړی شو. هرې نرسې ته، هر زده کوونکي ته، هر جارو کښ ته یې وویل چې ورورجان اختر ځي.'),
    ('At night too he talked with Akhtar for a long time, little innocent words full of joy. At last he fell asleep. Akhtar stayed awake thinking: when would Manzoor get well? Was there no such medicine in the world that would make this lovely child healthy? He prayed for his health with a sincere heart, but he was sure they would not be accepted, because how could his heart be as pure as Manzoor’s?',
     'رات کو بھی وہ اختر سے دیر تک خوشی سے بھرپور ننھی ننھی معصوم باتیں کرتا رہا۔ آخر سو گیا۔ اختر جاگتا رہا اور سوچتا رہا کہ منظور کب تک ٹھیک ہوگا۔ کیا دنیا میں کوئی ایسی دوا موجود نہیں جو اس پیارے سے بچے کو تندرست کر دے۔ اس نے اس کی صحت کے لیے صدقِ دل سے دعائیں مانگیں مگر اسے یقین تھا کہ یہ قبول نہیں ہوں گی، اس لیے کہ اس کا دل منظور کا سا پاک دل کیسے ہو سکتا ہے۔',
     'د شپې هم یې له اختر سره ډېر وخت له خوښۍ ډکې کوچنۍ معصومې خبرې وکړې. په پای کې ویده شو. اختر ویښ پاتې شو او فکر یې کاوه چې منظور به کله روغ شي. ایا په نړۍ کې داسې درمل نشته چې دا ګران ماشوم روغ کړي؟ هغه د هغه د روغتیا لپاره له رښتیني زړه دعاګانې وکړې، خو باور یې درلود چې قبولې به نه شي، ځکه چې د هغه زړه به څنګه د منظور په څېر پاک وي.'),
    ('Thinking of Manzoor and of their parting, he felt great sorrow. He could not believe that in the morning he would leave him and go away, and, busy building his new life, would wipe him from his heart and mind. How good it would have been if he had died before hearing Manzoor’s “Assalamu alaikum”. With what face would he carry this new life, which was Manzoor’s gift, out of the hospital?',
     'منظور اور اس کی جدائی کے بارے میں سوچتے ہوئے اسے بہت دکھ ہوتا تھا۔ اسے یقین نہیں آتا تھا کہ صبح اس کو وہ چھوڑ کر چلا جائے گا اور اپنی نئی زندگی تعمیر کرنے میں مصروف ہو کر اسے اپنے دل و دماغ سے محو کر دے گا۔ کیا ہی اچھا ہوتا کہ وہ منظور کی ’’السلام علیکم‘‘ سننے سے پہلے ہی مر جاتا۔ یہ نئی زندگی جو اس کی عطا کردہ تھی، وہ کس منہ سے اٹھا کر ہسپتال سے باہر لے جائے گا۔',
     'د منظور او د هغه د بېلتون په اړه په فکر کولو ډېر غمجن کېده. باور یې نه کېده چې سهار به هغه پرېږدي او لاړ به شي، او د خپل نوي ژوند په جوړولو بوخت به هغه له زړه او ذهنه ورک کړي. څومره به ښه وای که د منظور له "السلام علیکم" اورېدو مخکې مړ شوی وای. دا نوی ژوند چې د هغه ورکړه وه، په کوم مخ به یې له روغتونه بهر یوسي؟'),
    ('Thinking, Akhtar fell asleep. In the morning he woke late. The nurses were moving quickly here and there in the ward. Turning over, he looked towards Manzoor’s cot. On it, instead of him, lay an old man, a skeleton of bones. For a moment a hush came over Akhtar. A nurse was passing nearby; he almost shouted to her: “Where is Manzoor?”',
     'سوچتے سوچتے اختر سو گیا۔ صبح دیر سے اٹھا۔ نرسیں وارڈ میں ادھر ادھر تیزی سے چل پھر رہی تھیں۔ کروٹ بدل کر اس نے منظور کی چارپائی کی طرف دیکھا۔ اس پر اس کی بجائے ایک بوڑھا، ہڈیوں کا ڈھانچہ لیٹا ہوا تھا۔ ایک لحظے کے لیے اختر پر سناٹا طاری ہو گیا۔ ایک نرس پاس سے گزر رہی تھی، اس سے اس نے قریب قریب چلا کر پوچھا: ’’منظور کہاں ہے‘‘؟',
     'په فکر فکر کې اختر ویده شو. سهار ناوخته راویښ شو. نرسانې په وارډ کې په چټکۍ دلته او هلته ګرځېدې. اړخ یې واړاوه او د منظور کټ ته یې وکتل. پرې د هغه پر ځای یو زوړ سړی، د هډوکو یو جوړښت، پروت و. د یوې شېبې لپاره پر اختر چوپتیا راغله. یوه نرسه ترې تېرېده؛ نږدې په چیغه یې ترې وپوښتل: "منظور چېرته دی؟"'),
    ('The nurse stopped. After remaining silent for a little while she answered in a very sorrowful tone: “Poor thing! He died at half past five in the morning.”',
     'نرس رکی۔ تھوڑی دیر خاموش رہنے کے بعد اس نے بڑے افسوسناک لہجے میں جواب دیا۔ ’’بے چارہ! صبح ساڑھے پانچ بجے مر گیا‘‘۔',
     'نرسه ودرېده. لږ وخت له چوپتیا وروسته یې په ډېره خواشینې لهجه ځواب ورکړ: "بېچاره! سهار پنځه نیمې بجې مړ شو."'),
    ('On hearing this, Akhtar received such a shock that his heart began to sink. He thought that this was the last attack……',
     'یہ سن کر اختر کو اس قدر صدمہ پہنچا کہ اس کا دل بیٹھنے لگا۔ اس نے سمجھا کہ یہ آخری دورہ ہے……',
     'دا په اورېدو اختر ته دومره صدمه ورسېده چې زړه یې ډوبېدل پیل کړل. هغه وګڼل چې دا وروستۍ دوره ده……'),
]: t.p(*x)
rec = BOOK.record(t, 'urdu12-u7-text-5', 'Lesson text (5)', 'متنِ سبق (۵)', 'د لوست متن (۵)', 36, [62, 63])
issues = [{'id': 'urdu12-pdf036', 'unit': 7, 'printedPage': 62, 'description': 'Printed punctuation retained: question marks after the closing quote (“…باتیں کروں گا‘‘؟”, “’’منظور کہاں ہے‘‘؟”); “مسیحا کا رتبہ رکھتی تھی کہ جس نے”. The last paragraph continues on p.64 (“مگر اُس کا خیال غلط ثابت ہوا…”), given with PDF37.'}]

if __name__ == '__main__':
    BOOK.save(36, [(7, rec)], issues=issues)
