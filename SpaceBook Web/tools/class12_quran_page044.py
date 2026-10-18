"""Mutalia-e-Quran XII PDF44: p.41 — Lesson 4 vocabulary (part 2); exercise Q1, Q2 items 1–4. Run: python class12_quran_page044.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words

VOCAB = [
    ('ضَلَالًا بَعِيدًا', 'Far-off misguidance', 'دور کی گم راہی', 'لرې ګمراهي'),
    ('شَيْطَانًا مَرِيدًا', 'A rebellious Satan', 'سرکش شیطان', 'سرکښ شیطان'),
    ('وَجْهَهُ', 'His face, his direction', 'اس کا رخ', 'خپل مخ'),
    ('يَدْعُونَ', 'They worship', 'وہ پوجتے ہیں', 'عبادت کوي'),
    ('خَلِيلًا', 'A friend', 'دوست', 'دوست'),
    ('وَأُحْضِرَتِ الْأَنْفُسُ', 'Souls have been brought near (to avarice)', 'نفس کو قریب کر دیا گیا', 'نفسونه (بخل ته) نږدې کړای شوي'),
]


def p44():
    b = Builder()
    b.table('mq12-l4-vocab-2', ['Word', 'Meaning'], [[w, e] for w, e, u, p in VOCAB], ['الفاظ', 'معانی'], ['کلمې', 'معناوې'],
            [[w, u] for w, e, u, p in VOCAB], [[w, p] for w, e, u, p in VOCAB])
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(4, 101, 1, 11), ('— according to it, the command to shorten the prayer is:', 'کے مطابق نماز قصر کرنے کا حکم ہے:', '— له دې سره سم د لمانځه د لنډولو حکم دی:'),
        [('in illness', 'بیماری میں', 'په ناروغۍ کې'), ('in rain', 'بارش میں', 'په باران کې'), ('in fatigue', 'تھکن میں', 'په ستړیا کې'), ('on a journey', 'سفر میں', 'په سفر کې')])
    MCQ(b, 2, words(4, 105, 1, 8), ('— according to it, the Qur\'an-e-Hakeem was revealed to the Noble Prophet (peace and blessings of Allah be upon him) so that between the people he may:', 'کی رو سے نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر قرآن حکیم اس لیے نازل فرمایا گیا تاکہ آپ لوگوں کے درمیان:', '— له دې سره سم پر نبي کریم صلی الله علیه وعلی آله واصحابه وسلم قرآن حکیم د دې لپاره نازل شو چې د خلکو ترمنځ:'),
        [('recite', 'تلاوت کریں', 'تلاوت وکړي'), ('judge', 'فیصلہ کریں', 'پرېکړه وکړي'), ('explain', 'بیان کریں', 'بیان وکړي'), ('preach', 'تبلیغ کریں', 'تبلیغ وکړي')])
    MCQ(b, 3, 'خَصِيمًا', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('partner', 'شراکت دار', 'شریک'), ('shareholder', 'حصے دار', 'برخه‌وال'), ('partisan', 'طرف دار', 'پلوی'), ('relative', 'رشتہ دار', 'خپلوان')])
    MCQ(b, 4, words(4, 107, 8, 15), ('— according to it, Allah Almighty does not like the great betrayer and:', 'کی رو سے اللہ تعالیٰ پسند نہیں فرماتا بڑے خیانت کرنے والے اور:', '— له دې سره سم الله تعالی لوی خیانتګر او ... نه خوښوي:'),
        [('the very miserly', 'سخت کنجوس کو', 'سخت شوم'), ('the great liar', 'بڑے جھوٹے کو', 'لوی درواغجن'), ('the great deceiver', 'بڑے دھوکے باز کو', 'لوی دوکه‌باز'), ('the grave sinner', 'سخت گناہ گار کو', 'سخت ګناهګار')])
    MCQ(b, 5, 'خَلِيلًا', ('— was said to:', 'کہا گیا ہے:', '— ویل شوی:'),
        [('Sayyiduna Ibrahim (peace be upon him)', 'سیدنا ابراہیم علیہ السلام کو', 'سیدنا ابراهیم علیه السلام ته'), ('Sayyiduna Isma\'il (peace be upon him)', 'سیدنا اسماعیل علیہ السلام کو', 'سیدنا اسماعیل علیه السلام ته'), ('Sayyiduna Ishaq (peace be upon him)', 'سیدنا اسحاق علیہ السلام کو', 'سیدنا اسحاق علیه السلام ته'), ('Sayyiduna Ya\'qub (peace be upon him)', 'سیدنا یعقوب علیہ السلام کو', 'سیدنا یعقوب علیه السلام ته')])
    MCQ(b, 6, words(4, 128, 20, 22), ('— according to it, the soul has been brought near to:', 'کے مطابق نفس کو قریب کر دیا گیا ہے:', '— له دې سره سم نفس ... ته نږدې کړای شوی:'),
        [('death', 'موت کے', 'مرګ'), ('trial', 'آزمائش کے', 'ازمېښت'), ('miserliness', 'بخل کے', 'بخل'), ('greed', 'لالچ کے', 'لالچ')])
    MCQ(b, 7, words(4, 132, 9, 11), ('— according to it, Allah Almighty alone is sufficient as:', 'کے مطابق اللہ تعالیٰ ہی کافی ہے بطور:', '— له دې سره سم یوازې الله تعالی بس دی د ... په توګه:'),
        [('ruler', 'حاکم', 'حاکم'), ('disposer of affairs', 'کارساز', 'کارساز'), ('owner', 'مالک', 'مالک'), ('friend', 'دوست', 'دوست')])
    b.p(*Q2)
    AR(b, f'(1) {words(4, 103, 1, 9)}', 'What has been instructed in the verse after the performance of prayer?', 'آیت کریمہ میں نماز کی ادائی کے بعد کیا تلقین کی گئی ہے؟', 'په آیت کې د لمانځه له ادا کولو وروسته څه سپارښتنه شوې؟')
    AR(b, f'(2) {words(4, 104, 1, 5)}', 'What instruction has been given in the verse regarding the pursuit of enemies?', 'آیت کریمہ میں دشمنوں کے تعاقب کے حوالے سے کیا ہدایت دی گئی ہے؟', 'په آیت کې د دښمنانو د تعقیب په اړه څه لارښوونه شوې؟')
    AR(b, f'(3) {words(4, 107)}', 'In the verse, from arguing in favour of whom has the Noble Prophet (peace and blessings of Allah be upon him) been commanded to refrain?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو کس سے بحث نہ کرنے کا حکم دیا گیا ہے؟', 'په آیت کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته د چا له لوري د بحث نه کولو حکم شوی؟')
    AR(b, f'(4) {words(4, 113, 21, 36)}', 'In the verse, which great favour of Allah Almighty upon the Noble Prophet (peace and blessings of Allah be upon him) is mentioned?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر اللہ تعالیٰ کے کس عظیم فضل کا ذکر ہے؟', 'په آیت کې پر نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د الله تعالی د کوم لوی فضل یادونه ده؟')
    BOOK.save(44, [(4, rec(b, 4, 44, 44, kind='exercise'))], issues=[{'id': 'mq12-pdf044', 'unit': 4, 'printedPage': 41,
               'description': 'Vocabulary continued from p.40. Quoted verses drawn from the reference Uthmani text. The Q2 label on p.41 is partly cut at the margin. No printed key.'}])


if __name__ == '__main__':
    p44()
