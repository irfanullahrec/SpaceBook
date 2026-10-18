"""Mutalia-e-Quran XII PDF78: p.75 — Lesson 7 exercise Q2 items 5–7, Q3, activities, teachers' guidance. Run: python class12_quran_page078.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p78():
    b = Builder()
    AR(b, f'(5) {words(5, 67, 2, 9)}', 'What command has been given to the Noble Prophet (peace and blessings of Allah be upon him) in the verse?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو کیا حکم دیا گیا ہے؟', 'په آیت کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته څه حکم شوی؟')
    AR(b, f'(6) {words(5, 73, 1, 15)}', 'How has the belief of the Trinity been refuted in the verse?', 'آیت کریمہ میں عقیدۂ تثلیث کا کس طرح رد کیا گیا ہے؟', 'په آیت کې د تثلیث عقیده څنګه رد شوې؟')
    AR(b, f'(7) {words(5, 75, 1, 17)}', 'What reality of Sayyiduna \'Isa (peace be upon him) and Sayyidah Maryam (peace be upon her) has been stated in the verse?', 'آیت کریمہ میں سیدنا عیسیٰ علیہ السلام اور سیدہ مریم علیہا السلام کی کیا حقیقت بیان کی گئی ہے؟', 'په آیت کې د سیدنا عیسی علیه السلام او سیده مریم علیها السلام کوم حقیقت بیان شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(5, 35)}', *TR)
    AR(b, f'(1b) {words(5, 45, 1, 16)}', 'According to the verse, what law of retaliation was stated in the Tawrah?', 'آیت کریمہ کی رو سے تورات میں قصاص کا کیا قانون بیان ہوا؟', 'د آیت له مخې په تورات کې د قصاص کوم قانون بیان شو؟')
    AR(b, f'(2a) {words(5, 55)}', *TR)
    AR(b, f'(2b) {words(5, 77)}', 'In the verse, from which things have the People of the Book been forbidden?', 'آیت کریمہ میں اہلِ کتاب کو کن باتوں سے منع کیا گیا ہے؟', 'په آیت کې اهل کتاب له کومو خبرو منع شوي؟')
    AR(b, f'(3a) {words(5, 69)}', *TR)
    AR(b, f'(3b) {words(5, 72)}', 'What belief of the Christians has been stated in the verse, and how did Sayyiduna \'Isa (peace be upon him) refute this false belief of theirs?', 'آیت کریمہ میں نصاریٰ کا کیا عقیدہ بیان ہوا ہے اور سیدنا عیسیٰ علیہ السلام نے ان کے اس باطل عقیدے کا کس طرح رد فرمایا؟', 'په آیت کې د نصاراوو کومه عقیده بیان شوې، او سیدنا عیسی علیه السلام د هغوی دا باطله عقیده څنګه رد کړه؟')
    b.h(*ACT)
    L(b, [('Learn the complete details concerning the belief of the Trinity from your teachers.', 'عقیدۂ تثلیث کے حوالے سے مکمل تفصیلات اپنے اساتذہ کرام سے معلوم کریں۔', 'د تثلیث د عقیدې په اړه بشپړ تفصیلات له خپلو ښوونکو زده کړئ.'),
          ('Prepare a list of the false beliefs and crimes of the Jews, and gather points refuting their false beliefs.', 'یہود کے باطل عقائد اور جرائم کی فہرست تیار کریں اور ان کے باطل عقائد کے رد پر نکات جمع کریں۔', 'د یهودو د باطلو عقیدو او جرمونو لړلیک جوړ کړئ او د هغوی د باطلو عقیدو د رد ټکي راټول کړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the life and events of Sayyiduna \'Isa (peace be upon him) and of the correct belief concerning him.', 'سیدنا عیسیٰ علیہ السلام کے حالات و واقعات اور ان کے متعلق صحیح عقیدے سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي د سیدنا عیسی علیه السلام له حالاتو او پېښو او د هغه په اړه له سمې عقیدې خبر کړئ.'),
          ('Explain to the students, with good clarity, the qualities of the believers stated in verses 54 to 56 of Surah al-Ma\'idah.', 'طلبہ کو سُوْرَةُ الْمَآئِدَةِ کی آیات ۵۴ تا ۵۶ میں بیان کردہ اہلِ ایمان کی عمدہ صفات وضاحت سے سمجھائیں۔', 'زده‌کوونکو ته د سورة المائده په ۵۴ تر ۵۶ آیتونو کې بیان شوي د مؤمنانو غوره صفتونه په وضاحت سره وپوهوئ.')])
    BOOK.save(78, [(7, rec(b, 7, 78, 78, kind='exercise'))], complete_units=[7], issues=[{'id': 'mq12-pdf078', 'unit': 7, 'printedPage': 75,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p78()
