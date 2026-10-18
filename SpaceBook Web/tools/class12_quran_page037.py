"""Mutalia-e-Quran XII PDF37: p.34 — Lesson 3 exercise Q3 (end), activities, teachers' guidance. Run: python class12_quran_page037.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, ACT, TCH, words


def p37():
    b = Builder()
    AR(b, f'(3b) {words(4, 93)}', 'What warning has been given in the verse for killing deliberately?', 'آیت کریمہ میں جان بوجھ کر قتل کرنے کی کیا وعید سنائی گئی ہے؟', 'په آیت کې د قصدي وژنې کوم ګواښ اورول شوی؟')
    b.h(*ACT)
    L(b, [('Learn the virtues and etiquette of salam and include it practically in your routine.', 'سلام کے فضائل اور آداب معلوم کریں اور عملی طور پر اس کو اپنے معمول میں شامل کریں۔', 'د سلام فضیلتونه او آداب زده کړئ او په عملي ډول یې په خپل ورځني کار کې شامل کړئ.'),
          ('Learn from your teachers the details of the four types of hypocrites mentioned in this lesson.', 'اس سبق میں جن چار اقسام کے منافقین کا تذکرہ آیا ہے، ان کی تفصیل اساتذہ کرام سے معلوم کریں۔', 'په دې لوست کې د یاد شویو څلورو ډوله منافقانو تفصیل له ښوونکو زده کړئ.')])
    b.h(*TCH)
    L(b, [('In the light of this lesson make students aware of the difference between unintentional killing and intentional killing, and of the Shari\'ah commands related to them.', 'اس سبق کی روشنی میں قتل خطا اور قتل عمد کا فرق اور ان کے شرعی احکام سے متعلق طلبہ کو آگاہ کریں۔', 'د دې لوست په رڼا کې زده‌کوونکي د ناقصدي او قصدي وژنې له توپیر او د هغوی له شرعي حکمونو خبر کړئ.'),
          ('In the light of "مَنْ يُطِعِ الرَّسُولَ فَقَدْ أَطَاعَ اللَّهَ" make clear to the students the importance of obeying the Messenger (peace and blessings of Allah be upon him) and of the Prophetic hadiths.', 'طلبہ کو ”مَنْ يُّطِعِ الرَّسُوْلَ فَقَدْ اَطَاعَ اللّٰهَ“ کی روشنی میں اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اور احادیثِ نبویہ کی اہمیت واضح کریں۔', 'زده‌کوونکو ته د «مَنْ يُطِعِ الرَّسُولَ فَقَدْ أَطَاعَ اللَّهَ» په رڼا کې د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت او د نبوي احادیثو اهمیت روښانه کړئ.')])
    BOOK.save(37, [(3, rec(b, 3, 37, 37, kind='exercise'))], complete_units=[3], issues=[{'id': 'mq12-pdf037', 'unit': 3, 'printedPage': 34,
               'description': 'Lower part of p.34 blank. Quoted verse drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p37()
