"""Mutalia-e-Quran XII PDF54: p.51 — Lesson 5 exercise Q1, Q2 items 1–6. Run: python class12_quran_page054.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p54():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(4, 138), ('— according to it, the hypocrites have been given glad tidings of:', 'کے مطابق منافقین کو خوش خبری دی گئی ہے:', '— له دې سره سم منافقانو ته د ... زېری ورکړل شوی:'),
        [('disgrace', 'رسوائی کی', 'رسوایۍ'), ('failure', 'ناکامی کی', 'ناکامۍ'), ('painful punishment', 'دردناک عذاب کی', 'دردناک عذاب'), ('curse', 'لعنت کی', 'لعنت')])
    MCQ(b, 2, words(4, 142, 11, 12), ('— according to it, the hypocrites offer prayer:', 'کے مطابق منافقین نماز ادا کرتے ہیں:', '— له دې سره سم منافقان لمونځ کوي:'),
        [('with showing off', 'ریاکاری کے ساتھ', 'په ریا سره'), ('half-heartedly', 'بے دلی سے', 'بې‌زړه'), ('with laziness', 'سستی کے ساتھ', 'په سستۍ سره'), ('with inattention', 'بے توجہی سے', 'په بې‌پامۍ')])
    MCQ(b, 3, words(4, 145, 1, 7), ('— according to it, the hypocrites will be in the level of Hell:', 'کے مطابق منافقین جہنم کے طبقے میں ہوں گے:', '— له دې سره سم منافقان به د دوزخ په ... طبقه کې وي:'),
        [('highest', 'سب سے اوپر', 'تر ټولو پورته'), ('lowest', 'سب سے نچلے', 'تر ټولو ښکته'), ('in the middle', 'درمیان میں', 'په منځ کې'), ('above the lowest', 'نچلے سے اوپر', 'له ښکته پورته')])
    MCQ(b, 4, words(4, 153, 21, 23), ('— according to it, the people of Hazrat Musa (peace be upon him) were seized by:', 'کے مطابق حضرت موسیٰ علیہ السلام کی قوم کو پکڑ لیا:', '— له دې سره سم د حضرت موسی علیه السلام قوم ... ونیو:'),
        [('a storm', 'آندھی نے', 'توپان'), ('a cry', 'چیخ نے', 'چیغې'), ('a thunderbolt', 'کڑک نے', 'تندر'), ('an earthquake', 'زلزلہ نے', 'زلزلې')])
    MCQ(b, 5, 'ٱلْعِجْلَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('ram', 'دنبہ', 'ډمبه'), ('goat', 'بکرا', 'وز'), ('camel', 'اونٹ', 'اوښ'), ('calf', 'بچھڑا', 'سخی')])
    MCQ(b, 6, words(4, 176, 44, 45), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('the share of two women', 'دو عورتوں کا حصہ', 'د دوو ښځو برخه'), ('the share of three women', 'تین عورتوں کا حصہ', 'د درېیو ښځو برخه'), ('the share of four women', 'چار عورتوں کا حصہ', 'د څلورو ښځو برخه'), ('the share of many women', 'بہت سی عورتوں کا حصہ', 'د ډېرو ښځو برخه')])
    MCQ(b, 7, words(4, 174, 1, 7), ('— according to it, there has come to people from their Lord:', 'کے مطابق لوگوں کے پاس ان کے رب کی طرف سے آ چکی:', '— له دې سره سم خلکو ته د هغوی د رب له لوري راغلي:'),
        [('important advice', 'اہم نصیحت', 'مهم نصیحت'), ('a clear proof', 'کھلی دلیل', 'ښکاره دلیل'), ('clear guidance', 'واضح ہدایت', 'روښانه هدایت'), ('great news', 'عظیم خبر', 'لوی خبر')])
    b.p(*Q2)
    AR(b, f'(1) {words(4, 135, 2, 9)}', 'What guidance has been given to the believers in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا ہدایت کی گئی ہے؟', 'په آیت کې مؤمنانو ته څه لارښوونه شوې؟')
    AR(b, f'(2) {words(4, 136, 1, 16)}', 'In the verse, belief in which things has been commanded?', 'آیت کریمہ میں کن چیزوں پر ایمان لانے کا حکم دیا گیا ہے؟', 'په آیت کې پر کومو شیانو د ایمان راوړلو حکم شوی؟')
    AR(b, f'(3) {words(4, 136, 18)}', 'According to the verse, who falls into far-off misguidance?', 'آیت کریمہ کی رو سے کون دور کی گم راہی میں جا پڑتا ہے؟', 'د آیت له مخې څوک لرې ګمراهۍ ته لوېږي؟')
    AR(b, f'(4) {words(4, 140, 28, 35)}', 'According to the verse, which people will Allah Almighty gather in Hell?', 'آیت کریمہ کے مطابق اللہ تعالیٰ کن لوگوں کو جہنم میں جمع کرے گا؟', 'د آیت له مخې الله تعالی به کوم خلک په دوزخ کې راټول کړي؟')
    AR(b, f'(5) {words(4, 147)}', 'According to the verse, adopting which two qualities is mentioned for being saved from the punishment of Allah Almighty?', 'آیت کریمہ کے مطابق کن دو خوبیوں کو اختیار کر کے اللہ تعالیٰ کے عذاب سے بچنے کا تذکرہ کیا گیا ہے؟', 'د آیت له مخې د کومو دوو ښېګڼو په غوره کولو د الله تعالی له عذابه د ژغورل کېدو یادونه شوې؟')
    AR(b, f'(6) {words(4, 153, 1, 9)}', 'What demand of the People of the Book has been mentioned in the verse?', 'آیت کریمہ میں اہلِ کتاب کی کیا فرمائش ذکر کی گئی ہے؟', 'په آیت کې د اهل کتابو کومه غوښتنه یاده شوې؟')
    BOOK.save(54, [(5, rec(b, 5, 54, 54, kind='exercise'))], issues=[{'id': 'mq12-pdf054', 'unit': 5, 'printedPage': 51,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p54()
