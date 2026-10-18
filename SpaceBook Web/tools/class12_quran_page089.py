"""Mutalia-e-Quran XII PDF89: p.86 — Lesson 8 exercise Q3 (end), activities, teachers' guidance. Run: python class12_quran_page089.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, TR, ACT, TCH, words


def p89():
    b = Builder()
    AR(b, f'(2b) {words(5, 89, 1, 34)}', 'What commands concerning oaths have been stated in the verse?', 'آیت کریمہ میں قسم کے حوالے سے کیا احکام بیان ہوئے ہیں؟', 'په آیت کې د قسم په اړه کوم حکمونه بیان شوي؟')
    AR(b, f'(3a) {words(5, 117)}', *TR)
    AR(b, f'(3b) {words(5, 118)}', 'According to the verse, what will Sayyiduna \'Isa (peace be upon him) submit for his people in the court of Allah Almighty?', 'آیت کریمہ کے مطابق سیدنا عیسیٰ علیہ السلام اللہ تعالیٰ کی بارگاہ میں اپنی قوم کے لیے کیا عرض کریں گے؟', 'د آیت له مخې سیدنا عیسی علیه السلام به د الله تعالی په دربار کې د خپل قوم لپاره څه عرض وکړي؟')
    b.h(*ACT)
    L(b, [('Arrange a list of the miracles granted to Sayyiduna \'Isa (peace be upon him).', 'سیدنا عیسیٰ علیہ السلام کو عطا کردہ معجزات کی فہرست مرتب کریں۔', 'سیدنا عیسی علیه السلام ته د ورکړل شویو معجزو لړلیک ترتیب کړئ.'),
          ('Students: write the points of the dialogue between Allah Almighty and Sayyiduna \'Isa (peace be upon him) on the Day of Resurrection mentioned in verses 116 to 120 of Surah al-Ma\'idah.', 'طلبہ کو سُوْرَةُ الْمَآئِدَةِ کی آیات ۱۱۶ تا ۱۲۰ میں روزِ قیامت اللہ تعالیٰ اور سیدنا عیسیٰ علیہ السلام کے درمیان جس مکالمے کا ذکر ہے اس کے نکات تحریر کریں۔', 'د سورة المائده په ۱۱۶ تر ۱۲۰ آیتونو کې د قیامت په ورځ د الله تعالی او سیدنا عیسی علیه السلام ترمنځ د یادو شویو خبرو ټکي ولیکئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the beliefs of the disbelievers concerning "bahirah, sa\'ibah, wasilah and ham".', '”بَحِيْرَةٍ، سَآئِبَةٍ، وَصِيْلَةٍ اور حَامٍ“ کے متعلق کفار کے عقائد سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي د «بحیره، سائبه، وصیله او حام» په اړه د کافرانو له عقیدو خبر کړئ.'),
          ('In the light of verses 90 to 91 of Surah al-Ma\'idah, make the students aware of the prohibition of wine and its physical and spiritual harms.', 'طلبہ کو سُوْرَةُ الْمَآئِدَةِ کی آیات ۹۰ تا ۹۱ کی روشنی میں شراب کی حرمت، اس کے جسمانی اور روحانی نقصانات سے آگاہ کریں۔', 'زده‌کوونکي د سورة المائده د ۹۰ تر ۹۱ آیتونو په رڼا کې د شرابو له حرمت او د هغو له بدني او روحاني زیانونو خبر کړئ.')])
    BOOK.save(89, [(8, rec(b, 8, 89, 89, kind='exercise'))], complete_units=[8], issues=[{'id': 'mq12-pdf089', 'unit': 8, 'printedPage': 86,
               'description': 'Lower half of p.86 blank. The activity line "طلبہ کو ... تحریر کریں" is printed as addressed to students (kept). Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p89()
