"""Mutalia-e-Quran XII PDF229: p.226 — Lesson 24 exercise Q2 items 6–8, Q3, activities, teachers' guidance. Run: python class12_quran_page229.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p229():
    b = Builder()
    AR(b, f'(6) {words(66, 8, 1, 8)}', 'What command has been given in the verse concerning repentance?', 'آیت کریمہ میں توبہ کے حوالے سے کیا حکم دیا گیا ہے؟', 'په آیت کې د توبې په اړه کوم حکم شوی؟')
    AR(b, f'(7) {words(66, 8, 9, 20)}', 'Of which rewards for those who make sincere repentance is mention made in the verse?', 'آیت کریمہ میں خالص توبہ کرنے والوں کے لیے کن انعامات کا ذکر ہے؟', 'په آیت کې د خالصې توبې کوونکو لپاره د کومو انعامونو یادونه ده؟')
    AR(b, f'(8) {words(66, 12)}', 'What attributes of Sayyidah Maryam (peace be upon her) have been stated in the verse?', 'آیت کریمہ میں سیدہ مریم علیہا السلام کی کیا صفات بیان کی گئی ہیں؟', 'په آیت کې د سیدې مریم علیها السلام کوم صفتونه بیان شوي؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(65, 3, 6, 21)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Talaq.', 'سُوْرَةُ الطَّلَاقِ کا تعارف تحریر کریں۔', 'د سورة الطلاق پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(65, 10)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Talaq.', 'سُوْرَةُ الطَّلَاقِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الطلاق ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(66, 5)}', *TR)
    AR(b, '(3b)', 'Write an introduction to Surah al-Tahrim.', 'سُوْرَةُ التَّحْرِيْمِ کا تعارف تحریر کریں۔', 'د سورة التحریم پېژندنه ولیکئ.')
    AR(b, f'(4a) {words(66, 6)}', *TR)
    AR(b, '(4b)', 'Write some basic themes of Surah al-Tahrim.', 'سُوْرَةُ التَّحْرِيْمِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة التحریم ځینې بنسټیز مضامین ولیکئ.')
    b.h(*ACT)
    L(b, [('Learn the basic commands concerning divorce and discuss them.', 'طلاق کے متعلق بنیادی احکامات معلوم کریں اور ان کا مذاکرہ کریں۔', 'د طلاق په اړه بنسټیز حکمونه زده کړئ او پرې بحث وکړئ.'),
          (f'Memorise with translation the supplication occurring in Surah al-Tahrim: "{words(66, 8, 36, 47)}".', f'سُوْرَةُ التَّحْرِيْمِ میں آنے والی دعا کو "{words(66, 8, 36, 47)}" کو ترجمہ کے ساتھ یاد کریں۔', f'په سورة التحریم کې راغلې دعا «{words(66, 8, 36, 47)}» له ژباړې سره په یاد کړئ.'),
          ('In verse 6 of Surah al-Tahrim there is the command to save oneself and one\'s household from the fire of Hell. In this regard learn at least three measures from your teachers.', 'سُوْرَةُ التَّحْرِيْمِ کی آیت: ۶ میں اپنے آپ کو اور اپنے گھر والوں کو جہنم کی آگ سے بچانے کا حکم ہے۔ اس حوالے سے کم سے کم تین اقدامات اپنے اساتذہ کرام سے معلوم کریں۔', 'د سورة التحریم په ۶ آیت کې د ځان او کورنۍ د دوزخ له اوره د ژغورلو حکم دی؛ په دې اړه لږ تر لږه درې ګامونه له خپلو ښوونکو زده کړئ.'),
          ('In Surah al-Tahrim the instruction is given to make sincere repentance. Research the literal and technical meaning of repentance and discuss the benefits of repentance.', 'سُوْرَةُ التَّحْرِيْمِ میں سچی توبہ کرنے کی تلقین کی گئی ہے۔ توبہ کے لغوی اور اصطلاحی معنیٰ کی تحقیق کریں اور توبہ کے فوائد پر مذاکرہ کریں۔', 'په سورة التحریم کې د رښتینې توبې لارښوونه شوې؛ د توبې لغوي او اصطلاحي مانا وڅېړئ او د توبې پر ګټو بحث وکړئ.')])
    b.h(*TCH)
    L(b, [('Have charts prepared on the different kinds of divorce, their commands and the waiting period.', 'طلاق کی مختلف اقسام، ان کے احکام اور عدت پر مبنی چارٹ تیار کروائیں۔', 'د طلاق د بېلابېلو ډولونو، د هغو د حکمونو او عدت پر بنسټ چارټونه جوړ کړئ.'),
          ('Identify at least three issues arising from divorce and give guidance from the Qur\'an-e-Hakim and the blessed hadiths.', 'طلاق کی وجہ سے پیدا ہونے والے کم از کم تین مسائل کا تعین کر کے قرآنِ حکیم اور احادیثِ مبارکہ سے رہنمائی کریں۔', 'د طلاق له امله لږ تر لږه درې پیدا کېدونکې ستونزې وټاکئ او له قرآن حکیم او مبارکو حدیثونو لارښوونه وکړئ.'),
          ('Briefly explain the attributes of the Pure Wives (may Allah be pleased with them) stated in Surah al-Tahrim. Further, narrate two incidents of the conduct of the Prophet (peace and blessings of Allah be upon him) with the Pure Wives (may Allah be pleased with them).', 'سُوْرَةُ التَّحْرِيْمِ میں ازواجِ مطہرات رضی اللہ عنہن کی جو صفات بیان ہوئی ہیں ان کی مختصر وضاحت کریں۔ نیز ازواجِ مطہرات رضی اللہ عنہن کے ساتھ آپ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے طرزِ عمل کے کوئی سے دو واقعات سنائیں۔', 'په سورة التحریم کې د پاکو مېرمنو رضي الله عنهن کوم صفتونه چې بیان شوي، په لنډه یې روښانه کړئ؛ همدارنګه له پاکو مېرمنو رضي الله عنهن سره د هغه صلی الله علیه وعلی آله واصحابه وسلم د چلند کومې دوه پېښې واورئ.')])
    BOOK.save(229, [(24, rec(b, 24, 229, 229, kind='exercise'))], complete_units=[24], issues=[{'id': 'mq12-pdf229', 'unit': 24, 'printedPage': 226,
               'description': 'Last lesson page. Q3 1a quotes 65:3 from "وَمَنْ يَتَوَكَّلْ"; Q3 2a quotes 65:10 in full. Activity line 2 prints "آنے والی دعا کو … کو ترجمہ کے ساتھ" (doubled "کو", kept). Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p229()
