"""Mutalia-e-Quran XII PDF186: p.183 — Lesson 19 vocabulary; exercise Q1 items 1–4. Run: python class12_quran_page186.py"""
from class12_quran_common import BOOK, Builder, rec, VOC, EX, MCQ, Q1, words

VOCAB = [
    ('سَمِعَ', 'He heard', 'اس نے سن لیا', 'واورېده'),
    ('تَحَاوُرَكُمَا', 'The conversation of you both', 'آپ دونوں کی گفت گو', 'ستاسو د دواړو خبرې'),
    ('يُظَاهِرُونَ', 'They pronounce zihar', 'وہ ظہار کرتے ہیں', 'ظهار کوي'),
    ('زُورًا', 'A falsehood', 'جھوٹ', 'دروغ'),
    ('أَنْ يَتَمَاسَّا', 'That they touch one another', 'کہ وہ ایک دوسرے کو ہاتھ لگائیں', 'چې یو بل ته لاس ور وړي'),
    ('فَتَحْرِيرُ رَقَبَةٍ', 'Then freeing a slave', 'تو ایک غلام (یا کنیز) آزاد کرنا', 'نو د یوه غلام آزادول'),
    ('شَهْرَيْنِ مُتَتَابِعَيْنِ', 'Two consecutive months', 'دو مہینے لگاتار', 'دوه پرله‌پسې میاشتې'),
    ('سِتِّينَ', 'Sixty', 'ساٹھ', 'شپېته'),
    ('كُبِتُوا', 'They were disgraced', 'وہ ذلیل کیے گئے', 'ذلیل کړای شول'),
    ('يَبْعَثُهُمْ', 'He will raise them', 'وہ ان کو اٹھائے گا', 'راپورته به یې کړي'),
    ('أَحْصَاهُ اللَّهُ', 'Allah has recorded it', 'اللہ نے وہ (سب) محفوظ کر رکھا ہے', 'الله هغه (ټول) خوندي ساتلي'),
    ('نَسُوهُ', 'They forgot it', 'وہ اُسے بھول گئے', 'هېر یې کړ'),
    ('نَجْوَىٰ', 'Secret counsel', 'سرگوشی', 'پټه مشوره'),
    ('مَعْصِيَتِ الرَّسُولِ', 'Disobedience to the Messenger', 'رسول (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) کی نافرمانی', 'د رسول (صلی الله علیه وعلی آله واصحابه وسلم) نافرماني'),
    ('تَنَاجَوْا', 'You hold secret counsel', 'تم سرگوشی کرو', 'پټه مشوره وکړئ'),
    ('فَقَدِّمُوا', 'Then offer beforehand', 'تم پہلے (صدقہ) پیش کرو', 'مخکې (صدقه) وړاندې کړئ'),
    ('جُنَّةً', 'A shield', 'ڈھال', 'ډال'),
    ('فَصَدُّوا', 'So they turned (others) away', 'پس انھوں نے روکا', 'نو منع یې کړل'),
    ('فَيَحْلِفُونَ', 'So they will swear', 'پس وہ قسمیں کھائیں گے', 'نو قسمونه به وخوري'),
    ('يَحْسَبُونَ', 'They will think', 'وہ گمان کریں گے', 'ګومان به کوي'),
    ('يُحَادُّونَ', 'They oppose', 'وہ مخالفت کرتے ہیں', 'مخالفت کوي'),
    ('لَأَغْلِبَنَّ', 'I will surely prevail', 'بیشک میں ضرور غالب آؤں گا', 'زه به خامخا غالب شم'),
]


def p186():
    b = Builder()
    VOC(b, 'mq12-l19-vocab', VOCAB)
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, '', ('At the beginning of Surah al-Mujadilah, the commands stated are those of:', 'سُوْرَةُ الْمُجَادَلَةِ کے آغاز میں احکام بیان ہوئے:', 'د سورة المجادله په پیل کې د کومو حکمونو بیان شوی:'),
        [('khul\'', 'خلع کے', 'د خلع'), ('zihar', 'ظہار کے', 'د ظهار'), ('bequest', 'وصیت کے', 'د وصیت'), ('inheritance', 'وراثت کے', 'د میراث')])
    MCQ(b, 2, 'تَحَاوُرَكُمَا', ('— means "of you both":', 'کا مطلب ہے تم دونوں کی:', '— مطلب یې دی ستاسو د دواړو:'),
        [('proposals', 'تجویز', 'وړاندیز'), ('trouble', 'تکلیف', 'تکلیف'), ('conversation', 'گفت گو', 'خبرې'), ('worry', 'فکر', 'فکر')])
    MCQ(b, 3, words(58, 3, 1, 10), ('— according to this, one form of the expiation of zihar is:', 'کے مطابق ظہار کے کفارہ کی ایک صورت ہے:', '— له دې سره سم د ظهار د کفارې یوه بڼه ده:'),
        [('freeing two slaves', 'دو غلام آزاد کرنا', 'دوه غلامان آزادول'), ('freeing one slave', 'ایک غلام آزاد کرنا', 'یو غلام آزادول'), ('fasting for one month', 'ایک مہینے کے روزے رکھنا', 'د یوې میاشتې روژې نیول'), ('feeding ten poor people', 'دس مسکینوں کو کھانا کھلانا', 'لسو مسکینانو ته خواړه ورکول')])
    MCQ(b, 4, 'نَجْوَىٰ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('whispering in secret', 'سرگوشی کرنا', 'پټې خبرې کول'), ('shouting', 'چیخنا', 'چیغې وهل'), ('conversing', 'گفت گو کرنا', 'خبرې کول'), ('announcing', 'اعلان کرنا', 'اعلان کول')])
    BOOK.save(186, [(19, rec(b, 19, 186, 186, kind='exercise'))], issues=[{'id': 'mq12-pdf186', 'unit': 19, 'printedPage': 183,
               'description': 'Four-column vocabulary rendered as one two-column table (22 rows). The exercise continues on p.184. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p186()
