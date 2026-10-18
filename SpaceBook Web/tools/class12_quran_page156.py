"""Mutalia-e-Quran XII PDF156: p.153 — Lesson 15 exercise Q3, activities, teachers' guidance. Run: python class12_quran_page156.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p156():
    b = Builder()
    b.p(*Q3)
    AR(b, f'(1a) {words(47, 2)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah Muhammad.', 'سُوْرَةُ مُحَمَّدٍ کا تعارف تحریر کریں۔', 'د سورة محمد پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(47, 4, 33, 40)} {words(47, 5)} {words(47, 6)}', 'Write the translation of the verses.', 'آیات کریمہ کا ترجمہ تحریر کریں۔', 'د آیتونو ژباړه ولیکئ.')
    AR(b, '(2b)', 'Write some basic themes of Surah Muhammad.', 'سُوْرَةُ مُحَمَّدٍ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة محمد ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(47, 12)}', *TR)
    AR(b, f'(3b) {words(47, 15, 1, 27)}', 'What attributes of Paradise have been stated in the verse?', 'آیت کریمہ میں جنت کی کیا صفات بیان ہوئی ہیں؟', 'په آیت کې د جنت کوم صفتونه بیان شوي؟')
    b.h(*ACT)
    L(b, [('In Surah Muhammad the rivers of Paradise are mentioned. Search for some noble hadith related to the rivers of Paradise.', 'سُوْرَةُ مُحَمَّدٍ میں جنت کی نہروں کا ذکر ہے۔ جنت کی نہروں سے متعلق کوئی حدیث شریف تلاش کریں۔', 'په سورة محمد کې د جنت د ویالو یادونه ده؛ د جنت د ویالو په اړه کوم حدیث شریف ولټوئ.'),
          ('Search for some blessed hadiths about the impermanence of the world.', 'دنیا کی ناپائیداری کے حوالے سے چند احادیثِ مبارکہ تلاش کریں۔', 'د دنیا د ناپایښت په اړه ځینې مبارک حدیثونه ولټوئ.')])
    b.h(*TCH)
    L(b, [('One name of Surah Muhammad is also Surat al-Qital. In this surah there are verses on the commands of fighting in the way of Allah, the excellence of the mujahidin, the good end of the martyrs and encouragement to fighting; have the students identify them.', 'سُوْرَةُ مُحَمَّدٍ کا ایک نام سُوْرَةُ الْقِتَالِ بھی ہے۔ اس سورت میں قتال فی سبیل اللہ کے احکام، مجاہدین کی فضیلت، شہداء کا حسین انجام اور قتال کی ترغیب پر جو آیات وارد ہوئی ہیں ان کی نشان دہی کروائیں۔', 'د سورة محمد یو نوم سورة القتال هم دی. په دې سورت کې د الله په لار کې د قتال د حکمونو، د مجاهدینو د فضیلت، د شهیدانو د ښکلې پایلې او قتال ته د هڅونې په اړه کوم آیتونه راغلي، زده‌کوونکو ته یې په ګوته کړئ.'),
          ('Have a list made of the weaknesses of the hypocrites stated in this surah and assess the harms of those weaknesses. Further, get a few weaknesses found in our society identified and give proposals for their reform.', 'اس سورت میں بیان کی گئی منافقین کی خامیوں کی ایک فہرست بنوائیں اور ان خامیوں کے نقصانات کا جائزہ لیں۔ نیز ہمارے معاشرہ میں پائی جانے والی ایسی چند خامیوں کی نشان دہی کروا کر ان کی اصلاح کے لیے تجاویز دیں۔', 'په دې سورت کې د منافقانو د بیان شویو کمزوریو لړلیک جوړ کړئ او د دې کمزوریو زیانونه وڅېړئ؛ همدارنګه زموږ په ټولنه کې د داسې ځینو کمزوریو په ګوته کولو سره د هغو د اصلاح لپاره وړاندیزونه ورکړئ.')])
    BOOK.save(156, [(15, rec(b, 15, 156, 156, kind='exercise'))], complete_units=[15], issues=[{'id': 'mq12-pdf156', 'unit': 15, 'printedPage': 153,
               'description': 'Q3 2a quotes the end of 47:4 and verses 5–6. Lower part of p.153 blank. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p156()
