"""Mutalia-e-Quran XII PDF106: p.103 — Lesson 10 exercise Q1 items 5–7, Q2, Q3 (1–2). Run: python class12_quran_page106.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p106():
    b = Builder()
    MCQ(b, 5, words(24, 43, 18, 25), ('— according to this, Allah Almighty sends down from the mountain-like clouds:', 'کی رو سے اللہ تعالیٰ پہاڑ جیسے بادلوں سے برساتا ہے:', '— له دې سره سم الله تعالی د غرونو په څېر له ورېځو وروي:'),
        [('hail', 'اولے', 'ږلۍ'), ('snow', 'برف', 'واوره'), ('dew', 'شبنم', 'پرخه'), ('lightning', 'بجلی', 'برېښنا')])
    MCQ(b, 6, words(24, 45, 1, 6), ('— according to this, Allah Almighty created every living creature:', 'کے مطابق اللہ تعالیٰ نے ہر جاندار کو پیدا فرمایا:', '— له دې سره سم الله تعالی هر ژوندی پیدا کړ:'),
        [('from water', 'پانی سے', 'له اوبو'), ('from fire', 'آگ سے', 'له اوره'), ('from air', 'ہوا سے', 'له هوا'), ('from clay', 'مٹی سے', 'له خاورې')])
    MCQ(b, 7, words(24, 45, 8, 12), ('— according to this, some creatures are such as move:', 'کی رو سے بعض جاندار ایسے ہیں جو چلتے ہیں:', '— له دې سره سم ځینې ژوندي داسې دي چې ګرځي:'),
        [('on their heads', 'سر کے بل', 'پر سر'), ('on their backs', 'پیٹھ کے بل', 'پر شا'), ('on their bellies', 'پیٹ کے بل', 'پر خېټه'), ('on their hands', 'ہاتھوں کے بل', 'پر لاسونو')])
    b.p(*Q2)
    AR(b, f'(1) {words(24, 36, 1, 9)}', 'What has Allah Almighty said in the verse concerning mosques?', 'آیت کریمہ میں اللہ تعالیٰ نے مساجد کے حوالے سے کیا فرمایا ہے؟', 'په آیت کې الله تعالی د جوماتونو په اړه څه فرمایلي؟')
    AR(b, f'(2) {words(24, 41, 1, 12)}', 'According to the verse, who is engaged in the glorification of Allah Almighty?', 'آیت کریمہ کی رو سے کون اللہ تعالیٰ کی تسبیح میں مصروف ہے؟', 'د آیت له مخې څوک د الله تعالی په تسبیح بوخت دي؟')
    AR(b, f'(3) {words(24, 43, 1, 17)}', 'What power of Allah Almighty concerning the clouds has been stated in the verse?', 'آیت کریمہ میں بادلوں کے حوالے سے اللہ تعالیٰ کی کیا قدرت بیان ہوئی ہے؟', 'په آیت کې د ورېځو په اړه د الله تعالی کوم قدرت بیان شوی؟')
    AR(b, f'(4) {words(24, 52)}', 'What kind of people have been declared successful in the verse?', 'آیت کریمہ میں کیسے لوگوں کو کامیاب قرار دیا گیا ہے؟', 'په آیت کې کوم ډول خلک بریالي ګڼل شوي؟')
    AR(b, f'(5) {words(24, 54, 17, 19)}', 'What reward has been stated in the verse for obeying the Holy Prophet (peace and blessings of Allah be upon him)?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی اطاعت کرنے پر کیا انعام بیان کیا گیا ہے؟', 'په آیت کې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د اطاعت لپاره کوم انعام بیان شوی؟')
    AR(b, f'(6) {words(24, 59, 1, 11)}', 'What social etiquette has been stated in the verse concerning children?', 'آیت کریمہ میں بچوں کے حوالے سے کیا معاشرتی ادب بیان ہوا ہے؟', 'په آیت کې د ماشومانو په اړه کوم ټولنیز ادب بیان شوی؟')
    AR(b, f'(7) {words(24, 63, 18, 29)}', 'What end of opposing the Messenger of Allah (peace and blessings of Allah be upon him) has been stated in the verse?', 'آیت کریمہ میں رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی مخالفت کا کیا انجام بیان ہوا ہے؟', 'په آیت کې د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د مخالفت کومه پایله بیان شوې؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(24, 38)}', *TR)
    AR(b, f'(1b) {words(24, 37)}', 'What attributes of the servants of Allah Almighty have been mentioned in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کے بندوں کی کیا صفات ذکر کی گئی ہیں؟', 'په آیت کې د الله تعالی د بندګانو کومې صفتونه یاد شوي؟')
    AR(b, f'(2a) {words(24, 39)}', *TR)
    AR(b, f'(2b) {words(24, 58, 1, 28)}', 'Write the guidance stated in the verse.', 'آیت کریمہ میں بیان کردہ ہدایات تحریر کریں۔', 'په آیت کې بیان شوې لارښوونې ولیکئ.')
    BOOK.save(106, [(10, rec(b, 10, 106, 106, kind='exercise'))], issues=[{'id': 'mq12-pdf106', 'unit': 10, 'printedPage': 103,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p106()
