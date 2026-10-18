"""Mutalia-e-Quran XII PDF179: p.176 — Lesson 18 exercise Q1, Q2 items 1–6. Run: python class12_quran_page179.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p179():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(57, 4, 1, 8), ('— according to this, Allah Almighty created the heavens and the earth in:', 'کی رو سے اللہ تعالیٰ نے آسمانوں اور زمین کو پیدا فرمایا:', '— له دې سره سم الله تعالی آسمانونه او ځمکه پیدا کړل په:'),
        [('six days', 'چھے دنوں میں', 'شپږو ورځو کې'), ('seven days', 'سات دنوں میں', 'اوو ورځو کې'), ('eight days', 'آٹھ دنوں میں', 'اتو ورځو کې'), ('nine days', 'نو دنوں میں', 'نهو ورځو کې')])
    MCQ(b, 2, 'ٱسْتَوَىٰ', ('— means:', 'کا مطلب ہے:', '— مطلب یې دی:'),
        [('He became manifest', 'وہ ظاہر ہوا', 'ښکاره شو'), ('He became prominent', 'وہ نمایاں ہوا', 'څرګند شو'), ('He established Himself (on the Throne)', 'وہ جلوہ افروز ہوا', 'مستوي شو'), ('He became high', 'وہ بلند ہوا', 'لوړ شو')])
    MCQ(b, 3, words(57, 12, 1, 9), ('— according to this, the light of the believing men and women on the Day of Resurrection will be running:', 'کی رو سے مومن مردوں اور خواتین کا نور قیامت کے دن دوڑ رہا ہوگا ان کے:', '— له دې سره سم د قیامت په ورځ به د مؤمنو نارینه وو او ښځو نور منډې وهي د هغوی:'),
        [('ahead and behind', 'آگے اور پیچھے', 'مخکې او شاته'), ('ahead and on the right', 'آگے اور دائیں', 'مخکې او ښي لوري ته'), ('right and left', 'دائیں اور بائیں', 'ښي او کیڼ لوري ته'), ('above and below', 'اوپر اور نیچے', 'پاس او لاندې')])
    MCQ(b, 4, 'سُورٍ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('pillar', 'ستون', 'ستن'), ('roof', 'چھت', 'چت'), ('wall', 'دیوار', 'دېوال'), ('door', 'دروازہ', 'دروازه')])
    MCQ(b, 5, 'ٱلْغَرُورُ', ('— means:', 'کا مطلب ہے:', '— مطلب یې دی:'),
        [('a great deceiver', 'بڑا دھوکے باز', 'لوی غولوونکی'), ('a great traitor', 'بڑا خائن', 'لوی خاین'), ('very grateful', 'بڑا ناشکرا', 'ډېر ناشکره'), ('very arrogant', 'بڑا متکبر', 'ډېر کبرجن')])
    MCQ(b, 6, words(57, 21, 1, 7), ('— in this, concerning forgiveness and Paradise, the command is:', 'میں مغفرت اور جنت کے متعلق حکم ہے:', '— په دې کې د بښنې او جنت په اړه حکم دی:'),
        [('to race ahead', 'سبقت کرنے کا', 'د مخکې کېدو'), ('to have longing', 'شوق رکھنے کا', 'د تلوسې لرلو'), ('to have knowledge', 'علم رکھنے کا', 'د پوهې لرلو'), ('to keep hope', 'امید رکھنے کا', 'د هیلې ساتلو')])
    MCQ(b, 7, words(57, 25, 13, 19), ('— according to this, Allah Almighty sent down, with severe military strength and other benefits:', 'کی رو سے اللہ تعالیٰ نے سخت جنگی طاقت اور دیگر فوائد کے لیے اتارا ہے:', '— له دې سره سم الله تعالی د سخت جنګي ځواک او نورو ګټو لپاره نازل کړی:'),
        [('brass', 'پیتل', 'ژېړ'), ('copper', 'تانبہ', 'مس'), ('lead', 'سیسہ', 'سرپ'), ('iron', 'لوہا', 'اوسپنه')])
    b.p(*Q2)
    AR(b, f'(1) {words(57, 3)}', 'What attributes of Allah Almighty have been stated in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کی کون سی صفات بیان ہوئی ہیں؟', 'په آیت کې د الله تعالی کوم صفتونه بیان شوي؟')
    AR(b, f'(2) {words(57, 11)}', 'What excellence of qard hasan (a goodly loan) has been stated in the verse?', 'آیت کریمہ میں قرضِ حسنہ کی کیا فضیلت بیان کی گئی ہے؟', 'په آیت کې د ښه پور کوم فضیلت بیان شوی؟')
    AR(b, f'(3) {words(57, 19, 1, 14)}', 'What glad tidings have been given in the verse to those who believe in Allah Almighty and His Messenger (peace and blessings of Allah be upon him)?', 'آیت کریمہ میں اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم پر ایمان لانے والوں کو کیا خوش خبری دی گئی ہے؟', 'په آیت کې پر الله تعالی او د هغه پر رسول صلی الله علیه وعلی آله واصحابه وسلم ایمان راوړونکو ته کوم زېری ورکړل شوی؟')
    AR(b, f'(4) {words(57, 23, 1, 9)}', 'What consolation has been given in the verse for the people of faith?', 'آیت کریمہ میں اہلِ ایمان کے لیے کیا تسلی ہے؟', 'په آیت کې د مؤمنانو لپاره څه تسلي ده؟')
    AR(b, f'(5) {words(57, 25, 1, 11)}', 'According to the verse, what purpose has been stated for sending down the Book and the Balance with the messengers?', 'آیت کریمہ کی رو سے رسولوں کے ساتھ کتاب اور میزان نازل کرنے کا کیا مقصد بیان کیا گیا ہے؟', 'د آیت له مخې له رسولانو سره د کتاب او میزان د نازلولو کومه موخه بیان شوې؟')
    AR(b, f'(6) {words(57, 27, 19, 31)}', 'What has been told in the verse about monasticism?', 'آیت کریمہ میں رہبانیت کے حوالے سے کیا بتایا گیا؟', 'په آیت کې د رهبانیت په اړه څه ویل شوي؟')
    BOOK.save(179, [(18, rec(b, 18, 179, 179, kind='exercise'))], issues=[{'id': 'mq12-pdf179', 'unit': 18, 'printedPage': 176,
               'description': 'Q1 Arabic quotations printed in faint blue; matched to the verses. Quoted verses drawn from the reference Uthmani text. No printed key. A reader\'s thumb at the right edge excluded.'}])


if __name__ == '__main__':
    p179()
