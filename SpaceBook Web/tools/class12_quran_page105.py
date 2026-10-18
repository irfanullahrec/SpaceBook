"""Mutalia-e-Quran XII PDF105: p.102 — Lesson 10 vocabulary; exercise Q1 items 1–4. Run: python class12_quran_page105.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('الْمِصْبَاحُ', 'The lamp', 'چراغ', 'څراغ'),
    ('دُرِّيٌّ', 'Shining', 'چمکتا ہوا', 'ځلېدونکی'),
    ('بِقِيعَةٍ', 'In a barren plain', 'چٹیل میدان میں', 'په سپېره ډاګ کې'),
    ('الظَّمْآنُ', 'The thirsty one', 'پیاسا', 'تږی'),
    ('فَوَفَّاهُ', 'Then He pays him in full', 'تو وہ اسے پورا چکا دیتا ہے', 'نو پوره یې ورکوي'),
    ('لُجِّيٍّ', 'Deep', 'گہرا', 'ژور'),
    ('يَغْشَاهُ', 'Covering it', 'وہ اس پر چھائی ہوئی ہو', 'پرې خوره وي'),
    ('الطَّيْرُ صَافَّاتٍ', 'Birds with wings outspread', 'پر پھیلائے پرندے', 'وزرونه غوړولي مرغان'),
    ('يُزْجِي', 'He drives', 'وہ چلاتا ہے', 'چلوي یې'),
    ('يُؤَلِّفُ', 'He joins together', 'وہ ملا دیتا ہے', 'سره یوځای کوي'),
    ('رُكَامًا', 'In layers, heaped up', 'تہ بہ تہ', 'پر یو بل پرتې'),
    ('الْوَدْقَ', 'The raindrops', 'بارش کے قطرے', 'د باران څاڅکي'),
    ('خِلَالِهِ', 'Its midst', 'اس کے درمیان', 'د هغې منځ'),
    ('بَرَدٍ', 'Hail', 'اولے', 'ږلۍ'),
    ('يُقَلِّبُ', 'He alternates', 'وہ بدلتا رہتا ہے', 'اړوي راړوي'),
    ('الْأَعْرَجِ', 'The lame', 'لنگڑا', 'ګوډ'),
    ('مُعْجِزِينَ', 'Those who can frustrate', 'عاجز کرنے والے', 'عاجزوونکي'),
    ('الْقَوَاعِدُ', 'Elderly women staying at home', 'خانہ نشین بوڑھی عورتیں / عمر رسیدہ خواتین', 'کورناستې زړې ښځې / عمر خوړلې ښځې'),
    ('أَنْ يَضَعْنَ', 'That they lay aside', 'کہ وہ اتار دیں', 'چې لرې یې کړي'),
    ('ثِيَابَهُنَّ', 'Their (outer) garments', 'ان کے کپڑے', 'د هغوی جامې'),
    ('مُتَبَرِّجَاتٍ', 'Displaying (adornment)', 'ظاہر کرنے والیاں', 'ښکاره کوونکې'),
    ('أَنْ يَسْتَعْفِفْنَ', 'If they refrain (for modesty)', 'اگر وہ احتیاط رکھیں', 'که احتیاط وکړي'),
]


def p105():
    b = Builder()
    VOC(b, 'mq12-l10-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(24, 35, 13, 13), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('light', 'روشنی', 'رڼا'), ('torch', 'مشعل', 'مشعل'), ('ember', 'انگارہ', 'سکروټه'), ('lamp', 'چراغ', 'څراغ')])
    MCQ(b, 2, words(24, 35, 17, 20), ('— according to this, the lantern is a shining star as though:', 'کے مطابق وہ فانوس ایک چمکتا ہوا تارا ہے گویا:', '— له دې سره سم هغه فانوس یو ځلېدونکی ستوری دی ګواکې:'),
        [('like the moon', 'چاند کی طرح', 'د سپوږمۍ په څېر'), ('like the sun', 'سورج کی طرح', 'د لمر په څېر'), ('like a pearl', 'موتی کی طرح', 'د مرغلرې په څېر'), ('like gold', 'سونے کی طرح', 'د سرو زرو په څېر')])
    MCQ(b, 3, 'ٱلْأَعْرَجِ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('blind', 'اندھا', 'ړوند'), ('lame', 'لنگڑا', 'ګوډ'), ('deaf', 'بہرہ', 'کوڼ'), ('dumb', 'گونگا', 'ګونګی')])
    MCQ(b, 4, 'ٱلظَّمْـَٔانُ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('hungry', 'بھوکا', 'وږی'), ('thirsty', 'پیاسا', 'تږی'), ('sick', 'بیمار', 'ناروغ'), ('satiated', 'سیر', 'موړ')])
    BOOK.save(105, [(10, rec(b, 10, 105, 105, kind='exercise'))], issues=[{'id': 'mq12-pdf105', 'unit': 10, 'printedPage': 102,
               'description': 'Four-column vocabulary rendered as one two-column table (22 rows). MCQ 1 prints the word as ٱلْمِصْبَاحُ; quoted words drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p105()
