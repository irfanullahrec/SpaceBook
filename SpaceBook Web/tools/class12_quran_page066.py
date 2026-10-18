"""Mutalia-e-Quran XII PDF66: p.63 — Lesson 6 exercise Q1 items 5–7, Q2, Q3 (start). Run: python class12_quran_page066.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p66():
    b = Builder()
    MCQ(b, 5, words(5, 18, 1, 6), ('— according to it, the Jews and Christians call themselves:', 'کی رو سے یہود و نصاریٰ خود کو کہتے ہیں:', '— له دې سره سم یهود او نصارا ځانونه بولي:'),
        [('sons of Allah Almighty', 'اللہ تعالیٰ کے بیٹے', 'د الله تعالی زامن'), ('sons of Sayyiduna \'Isa (peace be upon him)', 'سیدنا عیسیٰ علیہ السلام کے بیٹے', 'د سیدنا عیسی علیه السلام زامن'), ('sons of Sayyidah Maryam (peace be upon her)', 'سیدہ مریم علیہا السلام کے بیٹے', 'د سیده مریم علیها السلام زامن'), ('sons of Sayyiduna Jibra\'il (peace be upon him)', 'سیدنا جبرائیل علیہ السلام کے بیٹے', 'د سیدنا جبرائیل علیه السلام زامن')])
    MCQ(b, 6, 'غُرَابًا', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('falcon', 'شاہین', 'شاهین'), ('pigeon', 'کبوتر', 'کوتره'), ('hawk', 'باز', 'باز'), ('crow', 'کوّا', 'کارغه')])
    MCQ(b, 7, words(5, 32, 18, 21), ('— in it the unjust killing of one human being has been declared:', 'میں ایک انسان کے ناحق قتل کو قرار دیا گیا ہے:', '— په دې کې د یوه انسان ناحقه وژنه ګرځول شوې:'),
        [('the killing of one person', 'ایک شخص کا قتل', 'د یوه کس وژنه'), ('the killing of a group', 'ایک گروہ کا قتل', 'د یوې ډلې وژنه'), ('the killing of a family', 'ایک خاندان کا قتل', 'د یوې کورنۍ وژنه'), ('the killing of all humanity', 'پوری انسانیت کا قتل', 'د ټول انسانیت وژنه')])
    b.p(*Q2)
    AR(b, f'(1) {words(5, 1, 1, 19)}', 'What teachings have been given to the believers in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا تعلیمات دی گئیں ہیں؟', 'په آیت کې مؤمنانو ته کومې لارښوونې شوې؟')
    AR(b, f'(2) {words(5, 3, 43, 53)}', 'What has been announced by Allah Almighty in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کی طرف سے کیا اعلان فرمایا گیا ہے؟', 'په آیت کې د الله تعالی له لوري څه اعلان شوی؟')
    AR(b, f'(3) {words(5, 4, 21)}', 'What commands have been given in the verse concerning hunting animals?', 'آیت کریمہ میں شکاری جانور کے حوالے سے کیا احکامات دیے گئے ہیں؟', 'په آیت کې د ښکاري ځناور په اړه کوم حکمونه شوي؟')
    AR(b, f'(4) {words(5, 6, 1, 17)}', 'What obligations of wudu have been stated in the verse?', 'آیت کریمہ میں وضو کے کیا فرائض بیان کیے گئے ہیں؟', 'په آیت کې د اودس کوم فرضونه بیان شوي؟')
    AR(b, f'(5) {words(5, 18, 1, 7)}', 'What false belief of the Jews and Christians has been stated in the verse?', 'آیت کریمہ میں یہود و نصاریٰ کا کیا باطل عقیدہ بیان کیا گیا ہے؟', 'په آیت کې د یهودو او نصاراوو کومه باطله عقیده بیان شوې؟')
    AR(b, f'(6) {words(5, 24)}', 'According to the verse, what answer did the Banu Isra\'il give to Sayyiduna Musa\'s (peace be upon him) demand for jihad?', 'آیت کریمہ کے مطابق بنی اسرائیل نے سیدنا موسیٰ علیہ السلام کو جہاد کے مطالبہ کا کیا جواب دیا؟', 'د آیت له مخې بني اسرائیلو د سیدنا موسی علیه السلام د جهاد غوښتنې ته څه ځواب ورکړ؟')
    AR(b, f'(7) {words(5, 26, 1, 11)}', 'According to the verse, what punishment was given to the Banu Isra\'il?', 'آیت کریمہ کے مطابق بنی اسرائیل کو کیا سزا دی گئی؟', 'د آیت له مخې بني اسرائیلو ته څه سزا ورکړل شوه؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(5, 11)}', *TR)
    b.p('(1b) Write the introduction of Surah al-Ma\'idah.', '(۱ب) سُوْرَةُ الْمَآئِدَةِ کا تعارف تحریر کریں۔', '(۱ب) د سورة المائده پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(5, 20)}', *TR)
    b.p('(2b) Write some basic themes of Surah al-Ma\'idah.', '(۲ب) سُوْرَةُ الْمَآئِدَةِ کے چند بنیادی مضامین تحریر کریں۔', '(۲ب) د سورة المائده ځینې بنسټیز مضامین ولیکئ.')
    BOOK.save(66, [(6, rec(b, 6, 66, 66, kind='exercise'))], issues=[{'id': 'mq12-pdf066', 'unit': 6, 'printedPage': 63,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p66()
