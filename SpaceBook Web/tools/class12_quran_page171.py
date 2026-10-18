"""Mutalia-e-Quran XII PDF171: p.168 — Lesson 17 exercise Q2 items 6–7, Q3, activities, teachers' guidance. Run: python class12_quran_page171.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p171():
    b = Builder()
    AR(b, f'(6) {words(49, 12, 15, 27)}', 'In what manner has backbiting been condemned in the verse?', 'آیت کریمہ میں غیبت کی کس انداز میں مذمت کی گئی ہے؟', 'په آیت کې غیبت په کوم انداز غندل شوی؟')
    AR(b, f'(7) {words(49, 15)}', 'Which qualities of the people of faith are mentioned in the verse?', 'آیت کریمہ میں اہلِ ایمان کی کن صفات کا ذکر ہے؟', 'په آیت کې د مؤمنانو د کومو صفتونو یادونه ده؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(49, 3)}', *TR)
    AR(b, f'(1b) {words(49, 7, 14, 30)}', 'According to the verse, love of which things has Allah Almighty placed in the hearts of the people of faith, and hatred of which things?', 'آیت کی رو سے اللہ تعالیٰ نے اہلِ ایمان کے دلوں میں کن چیزوں کی محبت اور کن کی نفرت ڈالی ہے؟', 'د آیت له مخې الله تعالی د مؤمنانو په زړونو کې د کومو شیانو مینه او د کومو کرکه اچولې؟')
    AR(b, f'(2a) {words(49, 11, 24, 42)}', *TR)
    AR(b, '(2b)', 'Write an introduction to Surah al-Hujurat.', 'سُوْرَةُ الْحُجُرَاتِ کا تعارف تحریر کریں۔', 'د سورة الحجرات پېژندنه ولیکئ.')
    AR(b, f'(3a) {words(49, 13)}', *TR)
    AR(b, '(3b)', 'Write some basic themes of Surah al-Hujurat.', 'سُوْرَةُ الْحُجُرَاتِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الحجرات ځینې بنسټیز مضامین ولیکئ.')
    b.h(*ACT)
    L(b, [('Prepare a chart containing the social evils stated in Surah al-Hujurat and their harms.', 'سُوْرَةُ الْحُجُرَاتِ میں بیان کی گئی معاشرتی برائیاں اور ان کے نقصانات پر مشتمل ایک چارٹ تیار کریں۔', 'په سورة الحجرات کې د بیان شویو ټولنیزو بدیو او د هغو د زیانونو یو چارټ جوړ کړئ.')])
    b.h(*TCH)
    L(b, [('In the light of verses 1 to 5 of Surah al-Hujurat, hold a discussion with the students on the etiquette of the court of the Holy Prophet (peace and blessings of Allah be upon him).', 'طلبہ سے سُوْرَةُ الْحُجُرَاتِ آیات: ۱ تا ۵ کی روشنی میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی بارگاہ کے آداب پر مذاکرہ کرائیں۔', 'له زده‌کوونکو سره د سورة الحجرات د ۱ تر ۵ آیتونو په رڼا کې د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د دربار پر آدابو بحث وکړئ.'),
          ('Make clear to the students, through a few blessed hadiths, the excellence of mutual unity and agreement among Muslims. Further, hold a discussion on how mutual unity among Muslims is possible.', 'طلبہ کو چند احادیثِ مبارکہ سے مسلمانوں کے باہمی اتحاد و اتفاق کی فضیلت واضح کریں۔ نیز مذاکرہ کرائیں کہ مسلمانوں کا باہمی اتحاد کیسے ممکن ہے؟', 'زده‌کوونکو ته د ځینو مبارکو حدیثونو په مرسته د مسلمانانو د خپل منځي یووالي او اتفاق فضیلت روښانه کړئ؛ همدارنګه بحث وکړئ چې د مسلمانانو خپل منځی یووالی څنګه ممکن دی؟')])
    BOOK.save(171, [(17, rec(b, 17, 171, 171, kind='exercise'))], complete_units=[17], issues=[{'id': 'mq12-pdf171', 'unit': 17, 'printedPage': 168,
               'description': 'Q3 1b quotes 49:7 from "وَلَٰكِنَّ اللَّهَ حَبَّبَ" to "هُمُ الرَّاشِدُونَ"; Q3 2a quotes 49:11 from "وَلَا تَلْمِزُوا". Quoted verses drawn from the reference Uthmani text. A reader\'s thumb at the right edge excluded.'}])


if __name__ == '__main__':
    p171()
