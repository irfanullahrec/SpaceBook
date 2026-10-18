"""Mutalia-e-Quran XII PDF16: p.13 — Lesson 1 matters of knowledge and action; vocabulary. Run: python class12_quran_page016.py"""
from class12_quran_common import BOOK, Builder, rec, S, L

VOCAB = [
    ('بَثَّ', 'He spread', 'اس نے پھیلا دیا', 'هغه خپاره کړل'),
    ('فَإِنْ خِفْتُمْ', 'So if you fear', 'پس اگر تمھیں اندیشہ ہو', 'نو که وېره لرئ'),
    ('نِحْلَةً', 'Willingly, gladly', 'خوش دلی سے', 'په خوښ زړه'),
    ('اكْسُوهُمْ', 'Clothe them', 'تم ان کو پہناؤ', 'جامې ورواغوندئ'),
    ('الْقِسْمَةَ', 'Division', 'تقسیم', 'وېش'),
    ('وَلْيَخْشَ', 'And let them fear', 'اور چاہیے کہ وہ ڈرے', 'او باید ووېرېږي'),
    ('قَوْلًا سَدِيدًا', 'A straight word', 'سیدھی بات', 'سمه خبره'),
    ('بُطُونِهِمْ', 'Their bellies', 'ان کے پیٹ', 'د هغوی ګېډې'),
    ('يَتَعَدَّ', 'He will transgress', 'وہ حد سے تجاوز کرے گا', 'له حد تېری کوي'),
    ('فَاحِشَةً وَمَقْتًا', 'An open shameful and hateful deed', 'کھلی بے حیائی اور غضب کا کام', 'ښکاره بې‌حیایي او د غضب کار'),
    ('الْمُحْصَنَاتُ', 'Married women', 'نکاح کرنے والی عورتیں', 'نکاح شوې ښځې'),
    ('حُوبًا', 'Sin, burden, crime', 'گناہ، وبال، جرم', 'ګناه، وبال، جرم'),
    ('صَدُقَاتِهِنَّ', 'Their dowers (mahr)', 'ان کے مہر', 'د هغوی مهرونه'),
    ('السُّفَهَاءَ', 'The foolish, the immature', 'ناسمجھ، بے وقوف', 'ناپوه، بې‌عقله'),
    ('فَإِنْ آنَسْتُمْ', 'So if you perceive', 'پس اگر تم پاؤ', 'نو که ومومئ'),
    ('قَوْلًا مَعْرُوفًا', 'A good word', 'اچھی بات', 'ښه خبره'),
    ('ذُرِّيَّةً ضِعَافًا', 'Weak offspring', 'کمزور اولاد', 'کمزوري اولادونه'),
    ('يَأْكُلُونَ', 'They eat', 'وہ کھاتے ہیں', 'هغوی خوري'),
    ('حَظِّ الْأُنْثَيَيْنِ', 'The share of two daughters', 'دو بیٹیوں کا حصہ', 'د دوو لوڼو برخه'),
    ('عَذَابٌ مُهِينٌ', 'A humiliating punishment', 'ذلیل و رسوا کرنے والا عذاب', 'سپکوونکی او رسوا کوونکی عذاب'),
    ('سَاءَ سَبِيلًا', 'A very evil way', 'بہت بُرا راستہ', 'ډېره بده لاره'),
    ('مُتَّخِذَاتِ أَخْدَانٍ', 'Women taking secret friends', 'چوری چھپی دوستی کرنے والی عورتیں', 'پټې دوستۍ نیوونکې ښځې'),
]


def p16():
    b = Builder()
    b.h('Matters of knowledge and action', 'علم و عمل کی باتیں', 'د علم او عمل خبرې')
    L(b, [('Allah Almighty has fixed a share in inheritance for both men and women from their parents and close relatives. We must act on it.', 'اللہ تعالیٰ نے مرد اور عورت دونوں کے لیے والدین اور قریبی رشتے داروں کی وراثت میں حصہ مقرر فرمایا ہے۔ ہمیں اس پر عمل کرنا چاہیے۔', 'الله تعالی نارینه او ښځې دواړو ته د مور و پلار او نږدې خپلوانو په میراث کې برخه ټاکلې ده؛ موږ باید پرې عمل وکړو.'),
          ('People, fearing Allah Almighty, should take care of the wealth of orphans just as they wish that after their death the wealth of their young and helpless children be cared for.', 'لوگ اللہ تعالیٰ سے ڈرتے ہوئے یتیموں کے مال کا اسی طرح خیال رکھیں جس طرح وہ چاہتے ہیں کہ ان کے مرنے کے بعد ان کی کم عمر اور بے بس اولاد کے مال کا خیال رکھا جائے۔', 'خلک دې له الله تعالی څخه په وېره د یتیمانو د مال همداسې پاملرنه وکړي لکه څنګه چې غواړي له مړینې وروسته یې د کم عمره او بې‌وسه اولاد د مال پاملرنه وشي.'),
          ('If one who has sinned in ignorance repents immediately, Allah Almighty certainly accepts such repentance.', 'نادانی میں گناہ کر بیٹھنے والا اگر فوراً توبہ کرے تو ایسی توبہ اللہ تعالیٰ ضرور قبول فرماتا ہے۔', 'که څوک په ناپوهۍ ګناه وکړي او سمدستي توبه وباسي، الله تعالی داسې توبه خامخا قبلوي.'),
          ('At the time when the state of death comes over one, neither is repentance accepted nor is believing beneficial. Therefore one must never delay in repenting, lest by persisting in sins the ability to repent be taken away or death come suddenly.', 'موت کی حالت طاری ہونے کے وقت نہ توبہ قبول ہوتی ہے اور نہ ہی ایمان لانا مفید ہوتا ہے۔ لہٰذا توبہ کرنے میں ہرگز تاخیر نہیں کرنی چاہیے، کہیں ایسا نہ ہو کہ گناہوں پر ڈٹے رہنے کی وجہ سے توبہ کی توفیق ہی سلب ہو جائے یا اچانک موت آ جائے۔', 'د مرګ د حالت د راتلو پر مهال نه توبه قبلېږي او نه ایمان راوړل ګټه کوي؛ نو په توبه کې باید هېڅکله ځنډ ونه شي، داسې نه چې پر ګناهونو د ټینګېدو له امله د توبې توفیق واخیستل شي یا ناڅاپه مرګ راشي.'),
          ('Men are commanded to treat their wives in the best way; they have been instructed to pay attention to the good qualities of their wives instead of their shortcomings.', 'مردوں کو حکم ہے کہ اپنی بیویوں کے ساتھ بہترین سلوک کریں، بیویوں کی خامیوں کے بجائے ان کی خوبیوں پہ توجہ دینے کی تلقین کی گئی ہے۔', 'نارینه وو ته حکم دی چې له خپلو مېرمنو سره غوره چلند وکړي؛ سپارښتنه شوې چې د مېرمنو د نیمګړتیاوو پر ځای د هغوی ښېګڼو ته پام وکړي.')])
    b.h('Vocabulary', 'ذخیرۂ الفاظ', 'د کلمو زېرمه')
    b.table('mq12-l1-vocab', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    BOOK.save(16, [(1, rec(b, 1, 16, 16))], issues=[{'id': 'mq12-pdf016', 'unit': 1, 'printedPage': 13,
               'description': 'The vocabulary is printed as a four-column table (word, meaning, word, meaning); rendered as one two-column table of 22 rows in printed order (right pair first, then left pair). The Arabic headwords keep the book\'s vowelling.'}])


if __name__ == '__main__':
    p16()
