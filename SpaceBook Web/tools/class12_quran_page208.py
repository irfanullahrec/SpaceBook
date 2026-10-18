"""Mutalia-e-Quran XII PDF208: p.205 — al-Jumu'ah matters of knowledge and action; Lesson 22 vocabulary. Run: python class12_quran_page208.py"""
from class12_quran_common import BOOK, Builder, rec, KA, L, VOC

VOCAB = [
    ('مَقْتًا', 'Something very hateful', 'سخت ناپسندیدہ بات', 'ډېره ناخوښه خبره'),
    ('يُحِبُّ', 'He loves', 'وہ محبت کرتا ہے', 'مینه کوي'),
    ('بُنْيَانٌ مَرْصُوصٌ', 'A solid structure (wall cast with lead)', 'سیسہ پلائی ہوئی دیوار', 'د سرپ ویلی دېوال'),
    ('لِمَ تُؤْذُونَنِي', 'Why do you hurt me', 'تم مجھے کیوں اذیت دیتے ہو', 'ما ته ولې اذیت راکوئ'),
    ('يُدْعَىٰ', 'He is called', 'وہ بلایا جاتا ہے', 'رابلل کېږي'),
    ('كَرِهَ', 'He was averse', 'وہ ناخوش ہوا', 'ناخوښه شو'),
    ('لِيُظْهِرَهُ', 'So that He may make it prevail', 'تاکہ وہ اس کو غالب کر دے', 'تر څو یې غالب کړي'),
    ('كُونُوا', 'Become', 'تم ہو جاؤ', 'شئ'),
    ('الْحَوَارِيُّونَ', 'The disciples (companions of Sayyiduna \'Isa)', 'حواریوں (سیدنا عیسیٰ علیہ السلام کے ساتھی)', 'حواریان (د سیدنا عیسی علیه السلام ملګري)'),
    ('بَعَثَ', 'He sent', 'اس نے بھیجا', 'ویې لېږه'),
    ('الْأُمِّيِّينَ', 'The unlettered people', 'ان پڑھ (بغیر پڑھے لکھے) لوگ', 'نالوستي خلک'),
    ('يُزَكِّيهِمْ', 'He purifies them', 'وہ ان کا تزکیہ کرتے ہیں', 'هغوی پاکوي'),
    ('حُمِّلُوا', 'They were laden', 'ان پر لادا گیا', 'پرې بار کړای شو'),
    ('الْحِمَارِ', 'The donkey', 'گدھا', 'خر'),
    ('أَسْفَارًا', 'Many books, a load', 'بہت سی کتابیں / بوجھ', 'ډېر کتابونه / بار'),
    ('لَا يَتَمَنَّوْنَهُ', 'They will not wish for it', 'وہ اس کی تمنا نہیں کریں گے', 'د هغه هیله به ونه کړي'),
    ('تَفِرُّونَ', 'You flee', 'تم بھاگتے ہو', 'تښتئ'),
    ('تُرَدُّونَ', 'You will be returned', 'تم لوٹائے جاؤ گے', 'ورګرځول به شئ'),
    ('فَإِذَا قُضِيَتِ', 'Then when it is completed', 'پھر جب وہ پوری ہو جائے', 'بیا کله چې پوره شي'),
    ('فَانْتَشِرُوا', 'Then disperse', 'تو تم پھیل جاؤ', 'نو خپاره شئ'),
    ('وَابْتَغُوا', 'And seek', 'اور تم تلاش کرو', 'او ولټوئ'),
    ('تُفْلِحُونَ', 'You will succeed', 'تم فلاح پاؤ گے', 'بریالي به شئ'),
]


def p208():
    b = Builder()
    KA(b)
    L(b, [('Prophethood and messengership are the bounty of Allah Almighty, and He favoured with this bounty whomever He willed. Accordingly Allah Almighty honoured Sayyiduna Muhammad, the Messenger of Allah (peace and blessings of Allah be upon him), with the distinction of Khatam al-Anbiya\' and Sayyid al-Mursalin. It is the bounty of Allah Almighty upon us that He granted us the honour of being the Ummah of the Holy Messenger (peace and blessings of Allah be upon him).', 'نبوت و رسالت اللہ تعالیٰ کا فضل ہے اور اس نے جسے چاہا اسے اس فضل سے نوازا۔ چناں چہ اللہ تعالیٰ نے سیدنا محمد رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو خاتم الانبیاء اور سید المرسلین کے اعزاز سے نوازا۔ ہم پر اللہ تعالیٰ کا فضل یہ ہے کہ ہمیں رسول اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اُمتی ہونے کا شرف بخشا۔', 'نبوت او رسالت د الله تعالی فضل دی، او چا ته یې چې وغوښتل په دې فضل یې ونازاوه. نو الله تعالی سیدنا محمد رسول الله صلی الله علیه وعلی آله واصحابه وسلم د خاتم الانبیاء او سید المرسلین په وياړ ونازاوه. پر موږ د الله تعالی فضل دا دی چې موږ ته یې د رسول اکرم صلی الله علیه وعلی آله واصحابه وسلم د امتي کېدو شرف راکړ.'),
          ('The example of the Jews who turn away from acting upon the commands of Allah Almighty has been given as that of a donkey, because even if books of philosophy are loaded onto a donkey, it does not become a philosopher by them. In the same way, the example of any nation that does not benefit from the divine Book is also like that of the donkey.', 'اللہ تعالیٰ کے احکامات پر عمل سے اعراض کرنے والے یہود کے لیے گدھے کی مثال اس لیے بیان کی گئی ہے کہ گدھے پر اگر فلسفہ کی کتابیں لاد دی جائیں تو وہ اس سے فلسفی نہیں بن جاتا۔ اسی طرح جو قوم کتابِ الٰہی سے استفادہ نہ کرے اس کی مثال بھی گدھے کی سی ہے۔', 'د الله تعالی د حکمونو له عمل مخ اړوونکو یهودو ته د خره مثال ځکه ورکړل شوی چې که پر خره د فلسفې کتابونه بار شي، نو په هغو فیلسوف نه جوړېږي. همداسې کوم قوم چې له الهي کتاب ګټه وانه خلي، د هغه مثال هم د خره په څېر دی.'),
          ('After the Friday adhan one should leave all occupations and go to offer the Friday prayer. The tragedy is that often people prefer play, amusement, trifles, economic activities and other occupations, and reach the Friday gathering late. It is necessary that with the Friday adhan one should leave buying and selling, business, employment and all other occupations and make arrangements to reach the mosque quickly to listen to the sermon early.', 'اذانِ جمعہ کے بعد تمام مصروفیات چھوڑ کر نمازِ جمعہ ادا کرنے کے لیے چلے جانا چاہیے۔ المیہ یہ ہے کہ اکثر لوگ کھیل تماشوں فضولیات، معاشی سرگرمیوں اور دیگر مصروفیات کو ترجیح دیتے ہیں اور اجتماعِ جمعہ میں دیر سے پہنچتے ہیں۔ ضروری ہے کہ جمعہ کی اذان کے ساتھ خرید و فروخت، کاروبار و ملازمت اور دیگر تمام مصروفیات وغیرہ چھوڑ کر جلد سے جلد خطبہ سننے کے لیے مسجد پہنچنے کا اہتمام کرنا چاہیے۔', 'د جمعې له اذان وروسته باید ټولې بوختیاوې پرېښودل شي او د جمعې لمانځه ته لاړ شي. غمیزه دا ده چې ډېر خلک لوبې، تماشې، بې‌ګټې کارونه، اقتصادي فعالیتونه او نورې بوختیاوې غوره ګڼي او د جمعې غونډې ته ناوخته رسېږي. اړینه ده چې د جمعې له اذان سره پېر و پلور، کاروبار، دنده او نورې ټولې بوختیاوې پرېښودل شي او د خطبې د اورېدو لپاره ژر تر ژره جومات ته د رسېدو اهتمام وشي.')])
    VOC(b, 'mq12-l22-vocab', VOCAB)
    BOOK.save(208, [(22, rec(b, 22, 208, 208))], issues=[{'id': 'mq12-pdf208', 'unit': 22, 'printedPage': 205,
               'description': 'Four-column vocabulary (covering both surahs of the lesson) rendered as one two-column table (22 rows). Third knowledge point prints "کھیل تماشوں فضولیات" without a comma (kept); "جمعہ کی اذان کے ساتھ … اہتمام کرنا چاہیے" printed with "ضروری ہے کہ … چاہیے" (kept).'}])


if __name__ == '__main__':
    p208()
