"""Mutalia-e-Quran XII PDF163: p.160 — Lesson 16 vocabulary (end); exercise Q1, Q2 items 1–3 (question of item 3 on p.161). Run: python class12_quran_page163.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words

VOCAB = [
    ('تَحْتَ الشَّجَرَةِ', 'Under the tree', 'درخت کے نیچے', 'د ونې لاندې'),
    ('أَثَابَهُمْ', 'He rewarded them', 'اس نے انھیں انعام دیا', 'انعام یې ورکړ'),
    ('مَغَانِمَ', 'Spoils of war', 'اموالِ غنیمت', 'د غنیمت مالونه'),
    ('حَمِيَّةَ الْجَاهِلِيَّةِ', 'The bigotry of the age of ignorance', 'جاہلیت کا تعصب', 'د جاهلیت تعصب'),
    ('أَرْسَلَ', 'He sent', 'اس نے بھیجا', 'ویې لېږه'),
    ('بِالْهُدَىٰ', 'With guidance', 'ہدایت کے ساتھ', 'له هدایت سره'),
    ('لِيُظْهِرَهُ', 'So that He may make it prevail', 'تاکہ وہ اُسے غالب کر دے', 'تر څو یې غالب کړي'),
    ('أَشِدَّاءُ', 'Very strict', 'بڑے سخت', 'ډېر سخت'),
    ('رُحَمَاءُ', 'Very merciful', 'بہت رحم دل', 'ډېر مهربانه'),
    ('أَثَرِ السُّجُودِ', 'The trace of prostration', 'سجدوں کا اثر (نور)', 'د سجدو اثر (نور)'),
]


def p163():
    b = Builder()
    b.table('mq12-l16-vocab-2', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(48, 1), ('— in this, what has been called a clear victory:', 'میں فتحِ مبین کہا گیا ہے:', '— په دې کې ښکاره بریا ویل شوې:'),
        [('the battle of Badr', 'غزوۂ بدر کو', 'د بدر غزا'), ('the battle of the Trench', 'غزوۂ خندق کو', 'د خندق غزا'), ('the Treaty of Hudaybiyah', 'صلح حدیبیہ کو', 'د حدیبیې سوله'), ('the battle of Hunayn', 'غزوۂ حنین کو', 'د حنین غزا')])
    MCQ(b, 2, 'جُنُودُ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('armies', 'لشکر', 'لښکرې'), ('commander', 'سپہ سالار', 'سپه‌سالار'), ('a group', 'ایک گروہ', 'یوه ډله'), ('a detachment', 'ایک دستہ', 'یوه ټولګۍ')])
    MCQ(b, 3, words(48, 17, 1, 4), ('— according to this there is no blame for not taking part in jihad on:', 'کی رو سے جہاد میں شریک نہ ہونے کا کوئی حرج نہیں ہے:', '— له دې سره سم په جهاد کې د نه ګډون هېڅ حرج نشته پر:'),
        [('the sick', 'بیمار پر', 'ناروغ'), ('the old', 'بوڑھے پر', 'زاړه'), ('the blind', 'اندھے پر', 'ړانده'), ('women', 'عورت پر', 'ښځې')])
    MCQ(b, 4, 'مَغَانِمَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('jihad', 'جہاد', 'جهاد'), ('spending', 'انفاق', 'لګښت'), ('spoils of war', 'غنیمتیں', 'غنیمتونه'), ('victory', 'فتح', 'بریا')])
    MCQ(b, 5, 'حَمِيَّةَ ٱلْجَٰهِلِيَّةِ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('the enmity of ignorance', 'جاہلیت کی دشمنی', 'د جاهلیت دښمني'), ('the custom of ignorance', 'جاہلیت کی رسم', 'د جاهلیت رسم'), ('the bigotry of ignorance', 'جاہلیت کا تعصب', 'د جاهلیت تعصب'), ('the friendship of ignorance', 'جاہلیت کی دوستی', 'د جاهلیت دوستي')])
    MCQ(b, 6, words(48, 28, 1, 11), ('— according to this, one purpose of the sending of the Holy Prophet (peace and blessings of Allah be upon him) was:', 'کی رو سے نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی بعثت کا ایک مقصد تھا:', '— له دې سره سم د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د بعثت یوه موخه وه:'),
        [('establishing prayer', 'اقامت الصلوٰۃ', 'د لمانځه قائمول'), ('the supremacy of the true religion', 'غلبۂ دینِ حق', 'د حق دین غلبه'), ('preaching and admonition', 'وعظ و نصیحت', 'وعظ او نصیحت'), ('purification and reminding', 'تزکیہ و تذکیر', 'تزکیه او یادونه')])
    MCQ(b, 7, words(48, 29, 7, 11), ('— in this the qualities have been stated of:', 'میں صفات بیان ہوئی ہیں:', '— په دې کې د چا صفتونه بیان شوي:'),
        [('the noble Prophets (peace be upon them)', 'انبیاء کرام علیہم السلام کی', 'د انبیاء کرامو علیهم السلام'), ('the noble Companions (may Allah be pleased with them)', 'صحابہ کرام رضی اللہ عنہم کی', 'د صحابه کرامو رضي الله عنهم'), ('the angels', 'فرشتوں کی', 'د پرښتو'), ('the believers', 'مومنین کی', 'د مؤمنانو')])
    b.p(*Q2)
    AR(b, f'(1) {words(48, 1)}', 'Of what has the Holy Prophet (peace and blessings of Allah be upon him) been given glad tidings in the verse?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو کس بات کی خوش خبری دی گئی ہے؟', 'په آیت کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته د کومې خبرې زېری ورکړل شوی؟')
    AR(b, f'(2) {words(48, 8)}', 'What attributes of the Holy Messenger (peace and blessings of Allah be upon him) have been stated in the verse?', 'آیت کریمہ میں رسول کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی کیا صفات بیان ہوئی ہیں؟', 'په آیت کې د رسول کریم صلی الله علیه وعلی آله واصحابه وسلم کوم صفتونه بیان شوي؟')
    AR(b, f'(3) {words(48, 9)}', 'Which rights of Allah Almighty and of the Messenger (peace and blessings of Allah be upon him) are mentioned in the verse?', 'آیت کریمہ میں اللہ تعالیٰ اور رسالت مآب صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے کن حقوق کا تذکرہ ہے؟', 'په آیت کې د الله تعالی او رسالت مآب صلی الله علیه وعلی آله واصحابه وسلم د کومو حقونو یادونه ده؟')
    BOOK.save(163, [(16, rec(b, 16, 163, 163, kind='exercise'))], issues=[{'id': 'mq12-pdf163', 'unit': 16, 'printedPage': 160,
               'description': 'Last ten vocabulary rows (continued from p.159) rendered as a continuation table. The question of Q2 item 3 is printed at the top of p.161 and is kept with its verse here. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p163()
