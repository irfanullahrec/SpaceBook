"""Mutalia-e-Quran XII PDF26: p.23 — Lesson 2 vocabulary; exercise Q1 items 1–4. Run: python class12_quran_page026.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('سُنَنَ', 'Ways, methods', 'راستے، طریقے', 'لارې، طریقې'),
    ('تُنْهَوْنَ', 'You have been forbidden', 'تمھیں روکا گیا ہے', 'تاسو منع شوي یاست'),
    ('مُدْخَلًا كَرِيمًا', 'An honourable place', 'عزت والا مقام', 'د عزت ځای'),
    ('نَصِيبَهُمْ', 'Their share', 'ان کا حصہ', 'د هغوی برخه'),
    ('مِثْقَالَ ذَرَّةٍ', 'The weight of a particle', 'ذرہ برابر', 'د ذرې په اندازه'),
    ('لَدُنْهُ', 'From Him, from His presence', 'اس کے پاس', 'له هغه سره'),
    ('لَوْ تُسَوَّى', 'Would that it were levelled', 'کاش وہ برابر کر دی جائے', 'کاش برابره کړای شي'),
    ('سُكَارَى', 'In a state of intoxication, senseless', 'نشہ کی حالت، مدہوش ہونا', 'د نشې حالت، بې‌هوشه'),
    ('نُصْلِيهِمْ', 'We will scorch them', 'ہم انھیں جھلسا دیں گے', 'موږ به یې وسوځوو'),
    ('أَنْ تَحْكُمُوا', 'That you judge', 'کہ تم فیصلہ کرو', 'چې پرېکړه وکړئ'),
    ('يَصُدُّونَ', 'They turn away', 'وہ منہ موڑتے ہیں', 'مخ اړوي'),
    ('إِنْ تَجْتَنِبُوا', 'If you keep away', 'اگر تم بچتے رہو', 'که ځان وساتئ'),
    ('نُكَفِّرْ', 'We will forgive', 'ہم معاف کر دیں گے', 'موږ به یې وبښو'),
    ('مَوَالِيَ', 'Heirs', 'وارث', 'وارثان'),
    ('قَوَّامُونَ', 'Rulers, guardians', 'حاکم، نگہبان', 'حاکمان، ساتونکي'),
    ('يُضَاعِفْهَا', 'He doubles it', 'وہ اسے دوگنا کر دیتا ہے', 'هغه یې دوه چنده کوي'),
    ('يَوَدُّ', 'He will wish', 'وہ آرزو کرے گا', 'ارمان به کوي'),
    ('لَا يَكْتُمُونَ', 'They will not be able to hide', 'وہ نہیں چھپا سکیں گے', 'پټولی به یې نه شي'),
    ('يُزَكِّي', 'He purifies', 'وہ تزکیہ کرتا ہے', 'هغه پاکوي'),
    ('نَضِجَتْ جُلُودُهُمْ', 'Their skins are burnt through', 'ان کی کھالیں جل کر پک جائیں گی', 'څرمنې یې وسوځي او پخې شي'),
    ('يَعِظُكُمْ', 'He advises you', 'وہ تمھیں نصیحت کرتا ہے', 'هغه تاسو ته نصیحت کوي'),
    ('يَحْلِفُونَ', 'They swear', 'وہ قسمیں کھاتے ہیں', 'قسمونه خوري'),
]


def p26():
    b = Builder()
    VOC(b, 'mq12-l2-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(4, 28, 7, 9), ('— according to it, man has been created:', 'کے مطابق انسان پیدا کیا گیا ہے:', '— له دې سره سم انسان پیدا شوی:'),
        [('hasty', 'جلد باز', 'بېړناک'), ('weak', 'کمزور', 'کمزوری'), ('stubborn', 'ضدی', 'سرټمبه'), ('needy', 'محتاج', 'اړ')])
    MCQ(b, 2, words(4, 34, 2, 2), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('ruler', 'حاکم', 'حاکم'), ('guide', 'رہنما', 'لارښود'), ('protector', 'محافظ', 'ساتونکی'), ('helper', 'مدد گار', 'مرستندوی')])
    MCQ(b, 3, 'سُكَٰرَىٰ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('unconscious', 'بے ہوش', 'بې‌هوشه'), ('mad', 'مجنون', 'لېونی'), ('intoxicated', 'نشے میں', 'نشه'), ('sick', 'بیمار', 'ناروغ')])
    MCQ(b, 4, words(4, 49, 9, 12), ('— according to it, Allah Almighty grants to whom He wills:', 'کی رو سے اللہ تعالیٰ ہی جس کو چاہتا ہے عطا فرماتا ہے:', '— له دې سره سم الله تعالی چا ته چې وغواړي ورکوي:'),
        [('mercy', 'رحم دلی', 'زړه سوی'), ('refinement', 'شائستگی', 'شایستګي'), ('purity', 'پاکیزگی', 'پاکي'), ('gentleness', 'نرمی', 'نرمي')])
    BOOK.save(26, [(2, rec(b, 2, 26, 26, kind='exercise'))], issues=[{'id': 'mq12-pdf026', 'unit': 2, 'printedPage': 23,
               'description': 'Four-column vocabulary rendered as one two-column table (22 rows). In Q1(3) the printed headword "سُكَارٰى" is given in Uthmani spelling. No printed key.'}])


if __name__ == '__main__':
    p26()
