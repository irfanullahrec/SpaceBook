"""Mutalia-e-Quran XII PDF88: p.85 — Lesson 8 exercise Q1 items 4–7, Q2, Q3 (start). Run: python class12_quran_page088.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p88():
    b = Builder()
    MCQ(b, 4, words(5, 99, 1, 5), ('— in this verse the responsibility of the Messenger (peace and blessings of Allah be upon him) stated is:', 'آیت کریمہ میں آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی ذمہ داری بیان ہوئی ہے:', '— په دې آیت کې د رسول صلی الله علیه وعلی آله واصحابه وسلم مسؤلیت بیان شوی:'),
        [('conveying the message', 'پیغام پہنچانا', 'پیغام رسول'), ('bringing to guidance', 'ہدایت پر لانا', 'هدایت ته راوستل'), ('making them accept', 'بات منوانا', 'خبره منل'), ('taking revenge', 'بدلہ دینا', 'بدله ورکول')])
    MCQ(b, 5, words(5, 99, 7, 12), ('— according to it, Allah Almighty knows what you make apparent and what you:', 'کی رو سے اللہ تعالیٰ جانتا ہے جو تم ظاہر کرتے ہو اور جو تم:', '— له دې سره سم الله تعالی پوهېږي چې څه ښکاره کوئ او څه:'),
        [('see', 'دیکھتے ہو', 'وینئ'), ('speak', 'بولتے ہو', 'وایئ'), ('hide', 'چھپاتے ہو', 'پټوئ'), ('hear', 'سنتے ہو', 'اورئ')])
    MCQ(b, 6, words(5, 112, 10, 15), ('— according to it, the disciples requested Sayyiduna \'Isa (peace be upon him):', 'کی رو سے حواریوں نے سیدنا عیسیٰ علیہ السلام سے درخواست کی:', '— له دې سره سم حواریانو له سیدنا عیسی علیه السلام غوښتنه وکړه:'),
        [('to end the famine', 'قحط ختم کرنے کی', 'د قحطۍ د ختمولو'), ('to send down food', 'کھانا اتارنے کی', 'د خوړو د راکوزولو'), ('to raise the dead', 'مردے زندہ کرنے کی', 'د مړو د ژوندي کولو'), ('to send down angels', 'فرشتے اتارنے کی', 'د پرښتو د راکوزولو')])
    MCQ(b, 7, words(5, 119, 3, 7), ('— according to it, on the Day of Resurrection the truthful will be benefited by:', 'کے مطابق روزِ قیامت سچوں کو نفع دے گا:', '— له دې سره سم د قیامت په ورځ به رښتینو ته ګټه ورسوي:'),
        [('their truthfulness', 'ان کا سچ', 'د هغوی رښتیا'), ('their wealth', 'ان کا مال', 'د هغوی مال'), ('their patience', 'ان کا صبر', 'د هغوی صبر'), ('their intention', 'ان کی نیت', 'د هغوی نیت')])
    b.p(*Q2)
    AR(b, f'(1) {words(5, 78)}', 'According to the verse, by whom was the curse upon the Banu Isra\'il, and why?', 'آیت کریمہ کے مطابق بنی اسرائیل پر لعنت کس نے اور کیوں کی؟', 'د آیت له مخې پر بني اسرائیلو چا او ولې لعنت وکړ؟')
    AR(b, f'(2) {words(5, 79)}', 'Which evil of the Banu Isra\'il has been stated in the verse?', 'آیت کریمہ میں بنی اسرائیل کی کون سی برائی بیان ہوئی ہے؟', 'په آیت کې د بني اسرائیلو کومه بدي بیان شوې؟')
    AR(b, f'(3) {words(5, 82, 2, 10)}', 'Whom has the verse declared to be the most severe enemies of the Muslims?', 'آیت کریمہ میں مسلمانوں کا سب سے سخت دشمن کن کو قرار دیا گیا ہے؟', 'په آیت کې د مسلمانانو تر ټولو سخت دښمنان کوم ګڼل شوي؟')
    AR(b, f'(4) {words(5, 91, 1, 17)}', 'According to the verse, which aims does Satan want to achieve through gambling and wine?', 'آیت کریمہ کے مطابق شیطان جوئے اور شراب کے ذریعے کیا مقاصد حاصل کرنا چاہتا ہے؟', 'د آیت له مخې شیطان د قمار او شرابو له لارې کومې موخې ترلاسه کول غواړي؟')
    AR(b, f'(5) {words(5, 102)}', 'Which bad habit of previous nations has been stated in the verse?', 'آیت کریمہ میں سابقہ اقوام کی کون سی بُری عادت بیان ہوئی ہے؟', 'په آیت کې د پخوانیو قومونو کومه بده عادت بیان شوې؟')
    AR(b, f'(6) {words(5, 113)}', 'According to the verse, why did the disciples request Sayyiduna \'Isa (peace be upon him) to send down the table spread?', 'آیت کریمہ کے مطابق حواریوں نے سیدنا عیسیٰ علیہ السلام سے مائدہ کے نازل کرنے کی فرمائش کیوں کی؟', 'د آیت له مخې حواریانو له سیدنا عیسی علیه السلام د مائدې د نازلولو غوښتنه ولې وکړه؟')
    AR(b, f'(7) {words(5, 116, 1, 27)}', 'According to the verse, what will Allah Almighty ask Sayyiduna \'Isa (peace be upon him) on the Day of Resurrection, and what answer will he give?', 'آیت کریمہ کے مطابق اللہ تعالیٰ قیامت کے دن سیدنا عیسیٰ علیہ السلام سے کیا سوال کرے گا اور وہ کیا جواب دیں گے؟', 'د آیت له مخې الله تعالی به د قیامت په ورځ له سیدنا عیسی علیه السلام څه پوښتنه وکړي او هغه به څه ځواب ورکړي؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(5, 87)}', *TR)
    AR(b, f'(1b) {words(5, 90)}', 'In the verse, from which things have the believers been commanded to keep away?', 'آیت کریمہ میں ایمان والوں کو کن چیزوں سے بچنے کا حکم دیا گیا ہے؟', 'په آیت کې مؤمنانو ته له کومو شیانو د ځان ساتلو حکم شوی؟')
    AR(b, f'(2a) {words(5, 100)}', *TR)
    BOOK.save(88, [(8, rec(b, 8, 88, 88, kind='exercise'))], issues=[{'id': 'mq12-pdf088', 'unit': 8, 'printedPage': 85,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p88()
