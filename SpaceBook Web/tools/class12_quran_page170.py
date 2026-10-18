"""Mutalia-e-Quran XII PDF170: p.167 — Lesson 17 vocabulary (end); exercise Q1, Q2 items 1–5. Run: python class12_quran_page170.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words

VOCAB = [
    ('شُعُوبًا', 'Nations', 'قومیں', 'قومونه'),
    ('لِتَعَارَفُوا', 'So that you may know one another', 'تاکہ تم ایک دوسرے کو پہچان سکو', 'تر څو یو بل وپېژنئ'),
    ('أَكْرَمَكُمْ', 'The most honoured of you', 'تم میں زیادہ عزت والا', 'ستاسو تر ټولو ډېر عزتمن'),
    ('لَمْ يَرْتَابُوا', 'They did not doubt', 'وہ شک میں نہ پڑیں', 'په شک کې ونه لوېدل'),
]


def p170():
    b = Builder()
    b.table('mq12-l17-vocab-2', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(49, 6, 4, 8), ('— according to this verse, on a sinful person bringing news the command is:', 'آیت کریمہ کی رو سے کسی فاسق شخص کے خبر لانے پر حکم ہے:', '— د دې آیت له مخې د کوم فاسق کس د خبر راوړلو پر مهال حکم دی:'),
        [('to spread it', 'پھیلانے کا', 'د خپرولو'), ('to investigate it', 'تحقیق کرنے کا', 'د څېړلو'), ('to hide it', 'چھپانے کا', 'د پټولو'), ('to ignore it', 'نظر انداز کرنے کا', 'د له پامه غورځولو')])
    MCQ(b, 2, words(49, 9, 30, 33), ('— according to this, Allah Almighty loves:', 'کی رو سے اللہ تعالیٰ پسند فرماتا ہے:', '— له دې سره سم الله تعالی خوښوي:'),
        [('those who sacrifice', 'قربانی کرنے والوں کو', 'قرباني کوونکي'), ('those who recite', 'تلاوت کرنے والوں کو', 'تلاوت کوونکي'), ('those who do justice', 'انصاف کرنے والوں کو', 'انصاف کوونکي'), ('those who repent', 'توبہ کرنے والوں کو', 'توبه کوونکي')])
    MCQ(b, 3, words(49, 11, 24, 26), ('— in this, what has been forbidden:', 'میں منع کیا گیا ہے:', '— په دې کې منع شوي:'),
        [('taunting', 'طعنہ دینے سے', 'پېغور ورکول'), ('suspicion', 'بدگمانی سے', 'بدګوماني'), ('spying', 'جاسوسی سے', 'جاسوسي'), ('mockery', 'مذاق سے', 'ملنډې')])
    MCQ(b, 4, words(49, 12, 13, 14), ('— in this, what has been forbidden:', 'میں منع کیا گیا ہے:', '— په دې کې منع شوي:'),
        [('backbiting', 'چغل خوری سے', 'چغلي'), ('false accusation', 'الزام تراشی سے', 'تور جوړول'), ('spying', 'جاسوسی کرنے سے', 'جاسوسي کول'), ('investigating', 'چھان بین کرنے سے', 'لټون کول')])
    MCQ(b, 5, 'لَحْمَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('flesh', 'گوشت', 'غوښه'), ('bone', 'ہڈی', 'هډوکی'), ('blood', 'خون', 'وینه'), ('skin', 'جلد', 'پوستکی')])
    MCQ(b, 6, words(49, 13, 8, 11), ('— according to this verse, Allah Almighty made nations and tribes:', 'آیت کریمہ کی رو سے اللہ تعالیٰ نے قومیں اور قبیلے بنائے:', '— د دې آیت له مخې الله تعالی قومونه او قبیلې جوړې کړې:'),
        [('for recognition', 'پہچان کے لیے', 'د پېژندګلوۍ لپاره'), ('for fame', 'شہرت کے لیے', 'د شهرت لپاره'), ('for competition', 'مقابلے کے لیے', 'د سیالۍ لپاره'), ('for superiority', 'برتری کے لیے', 'د لوړتیا لپاره')])
    MCQ(b, 7, words(49, 13, 13, 17), ('— according to this verse, the standard of honour is:', 'آیت کریمہ کی رو سے عزت کا معیار ہے:', '— د دې آیت له مخې د عزت معیار دی:'),
        [('wealth', 'دولت', 'شتمني'), ('piety', 'پرہیزگاری', 'پرهېزګاري'), ('tribe', 'قبیلہ', 'قبیله'), ('power', 'طاقت', 'ځواک')])
    b.p(*Q2)
    AR(b, f'(1) {words(49, 2, 1, 9)}', 'What etiquette of the court of the Prophet (peace and blessings of Allah be upon him) have the people of faith been taught in the verse?', 'آیت کریمہ میں اہلِ ایمان کو بارگاہِ نبوی صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کا کیا ادب سکھایا گیا ہے؟', 'په آیت کې مؤمنانو ته د نبوي دربار صلی الله علیه وعلی آله واصحابه وسلم کوم ادب ور زده کړل شوی؟')
    AR(b, f'(2) {words(49, 4)}', 'In the verse, which behaviour has been declared a sign of lack of understanding?', 'آیت کریمہ میں کس رویہ کو ناسمجھی کی علامت قرار دیا گیا ہے؟', 'په آیت کې کوم چلند د ناپوهۍ نښه ګرځول شوی؟')
    AR(b, f'(3) {words(49, 10, 1, 6)}', 'What have the people of faith been instructed in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کس بات کی تلقین کی گئی ہے؟', 'په آیت کې مؤمنانو ته د کومې خبرې لارښوونه شوې؟')
    AR(b, f'(4) {words(49, 11, 1, 22)}', 'Write the teachings stated in the verse.', 'آیت کریمہ میں بیان کردہ تعلیمات تحریر کریں۔', 'په آیت کې بیان شوې لارښوونې ولیکئ.')
    AR(b, f'(5) {words(49, 12, 1, 14)}', 'In the verse, the people of faith have been instructed to avoid what things?', 'آیت کریمہ میں اہلِ ایمان کو کس چیز سے بچنے کی ہدایت دی گئی ہے؟', 'په آیت کې مؤمنانو ته له کوم شي د ډډې لارښوونه شوې؟')
    BOOK.save(170, [(17, rec(b, 17, 170, 170, kind='exercise'))], issues=[{'id': 'mq12-pdf170', 'unit': 17, 'printedPage': 167,
               'description': 'Last four vocabulary rows (continued from p.166) rendered as a continuation table. Orange/yellow highlighter strokes and sticky marks by a reader excluded. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p170()
