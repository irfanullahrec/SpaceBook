"""Mutalia-e-Quran XII PDF209: p.206 — Lesson 22 exercise Q1, Q2 items 1–4. Run: python class12_quran_page209.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p209():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(61, 3), ('— according to this, what is severely hateful to Allah Almighty is:', 'کے مطابق اللہ تعالیٰ کو سخت ناپسند ہے:', '— له دې سره سم الله تعالی ته ډېر ناخوښ دي:'),
        [('slander', 'تہمت', 'تور'), ('malice', 'بغض', 'کینه'), ('contradiction of word and deed', 'قول و فعل کا تضاد', 'د خبرې او عمل تضاد'), ('envy', 'حسد', 'حسد')])
    MCQ(b, 2, 'بُنْيَٰنٌ مَّرْصُوصٌ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('a wall cast with lead', 'سیسہ پلائی ہوئی دیوار', 'د سرپ ویلی دېوال'), ('a wooden wall', 'لکڑی کی دیوار', 'د لرګي دېوال'), ('a cement wall', 'سیمنٹ کی دیوار', 'د سمنټو دېوال'), ('a stone wall', 'پتھر کی دیوار', 'د تیږې دېوال')])
    MCQ(b, 3, words(61, 5, 1, 7), ('— in this Sayyiduna Musa (peace be upon him) complained to his nation of their:', 'میں سیدنا موسیٰ علیہ السلام نے اپنی قوم سے شکایت کی:', '— په دې کې سیدنا موسی علیه السلام خپل قوم ته شکایت وکړ د هغوی:'),
        [('being heedless', 'غافل رہنے کی', 'د غفلت'), ('remaining ignorant', 'بے علم رہنے کی', 'د ناپوهۍ'), ('causing him hurt', 'اذیت دینے کی', 'د اذیت ورکولو'), ('remaining absent', 'غائب رہنے کی', 'د غیرحاضرۍ')])
    MCQ(b, 4, words(61, 6, 1, 17), ('— according to this, Sayyiduna \'Isa (peace be upon him) was a confirmer of:', 'کی رو سے سیدنا عیسیٰ علیہ السلام تصدیق کرنے والے تھے:', '— له دې سره سم سیدنا عیسی علیه السلام تصدیق کوونکی و:'),
        [('the Torah', 'تورات کی', 'د تورات'), ('the Zabur', 'زبور کی', 'د زبور'), ('the Scrolls of Ibrahim (peace be upon him)', 'صحفِ ابراہیم علیہ السلام کی', 'د ابراهیم علیه السلام د صحیفو'), ('the Qur\'an Majid', 'قرآن مجید کی', 'د قرآن مجید')])
    MCQ(b, 5, words(62, 2, 1, 6), ('— according to this, Allah Almighty sent the Messenger:', 'کی رو سے اللہ تعالیٰ نے رسول کو مبعوث فرمایا:', '— له دې سره سم الله تعالی رسول ولېږه:'),
        [('among a quarrelsome people', 'جھگڑالو قوم میں', 'په جنجالي قوم کې'), ('among a heedless people', 'غافل قوم میں', 'په غافل قوم کې'), ('among an unlettered people', 'ان پڑھ قوم میں', 'په نالوستي قوم کې'), ('among a civilised people', 'مہذب قوم میں', 'په متمدن قوم کې')])
    MCQ(b, 6, 'أَسْفَارًا', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('books', 'کتابیں', 'کتابونه'), ('sheets', 'اوراق', 'پاڼې'), ('newspapers', 'اخبارات', 'ورځپاڼې'), ('letters', 'خطوط', 'لیکونه')])
    MCQ(b, 7, 'تَفِرُّونَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('you stay', 'تم ٹھہرتے ہو', 'تم کېږئ'), ('you flee', 'تم بھاگتے ہو', 'تښتئ'), ('you sit', 'تم بیٹھتے ہو', 'کېنئ'), ('you stand', 'تم کھڑے ہوتے ہو', 'درېږئ')])
    MCQ(b, 8, words(62, 9, 10, 15), ('— according to this, at the time of going for the Friday prayer the command is to leave:', 'کی رو سے نمازِ جمعہ کے لیے جانے پر چھوڑنے کا حکم ہے:', '— له دې سره سم د جمعې لمانځه ته د تګ پر مهال د پرېښودو حکم دی:'),
        [('sleep and rest', 'نیند و آرام', 'خوب او آرام'), ('buying and selling', 'خرید و فروخت', 'پېر و پلور'), ('eating and drinking', 'کھانا پینا', 'خوړل څښل'), ('private gatherings', 'نجی مجالس', 'شخصي غونډې')])
    b.p(*Q2)
    AR(b, f'(1) {words(61, 2)}', 'Of what has the verse warned the people of faith?', 'آیت کریمہ میں اہلِ ایمان کو کس بات پر تنبیہ کی گئی ہے؟', 'په آیت کې مؤمنانو ته د کومې خبرې خبرداری شوی؟')
    AR(b, f'(2) {words(61, 4)}', 'What quality of the people beloved to Allah Almighty has been stated in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کے پسندیدہ افراد کی کیا صفت بیان کی گئی ہے؟', 'په آیت کې د الله تعالی د خوښو کسانو کوم صفت بیان شوی؟')
    AR(b, f'(3) {words(61, 9)}', 'What purpose of the sending of the Holy Prophet (peace and blessings of Allah be upon him) has been stated in the verse?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو مبعوث کرنے کا کیا مقصد بیان کیا گیا ہے؟', 'په آیت کې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د لېږلو کومه موخه بیان شوې؟')
    AR(b, f'(4) {words(61, 14, 1, 6)}', 'What have the people of faith been commanded in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا حکم دیا گیا ہے؟', 'په آیت کې مؤمنانو ته کوم حکم شوی؟')
    BOOK.save(209, [(22, rec(b, 22, 209, 209, kind='exercise'))], issues=[{'id': 'mq12-pdf209', 'unit': 22, 'printedPage': 206,
               'description': 'Eight MCQs printed (covering both surahs). Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p209()
