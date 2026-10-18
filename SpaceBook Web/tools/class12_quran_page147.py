"""Mutalia-e-Quran XII PDF147: p.144 — Lesson 14 exercise Q1 item 7, Q2, Q3, activities, teachers' guidance. Run: python class12_quran_page147.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, L, Q2, Q3, TR, ACT, TCH, words


def p147():
    b = Builder()
    MCQ(b, 7, 'يَبْغُونَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('they revolt', 'وہ بغاوت کرتے ہیں', 'بغاوت کوي'), ('they search', 'وہ تلاش کرتے ہیں', 'لټون کوي'), ('they reach the extreme', 'وہ انتہا کو پہنچتے ہیں', 'پای ته رسېږي'), ('they rebel (transgress)', 'وہ سرکشی کرتے ہیں', 'سرکشي کوي')])
    b.p(*Q2)
    AR(b, f'(1) {words(42, 7, 1, 10)}', 'What purpose of the revelation of the Qur\'an-e-Hakim has been stated in the verse?', 'آیت کریمہ میں قرآنِ حکیم کے نزول کا کیا مقصد بیان کیا گیا ہے؟', 'په آیت کې د قرآن حکیم د نزول کوم موخه بیان شوې؟')
    AR(b, f'(2) {words(42, 15, 20, 31)}', 'In the verse, what has the Holy Prophet (peace and blessings of Allah be upon him) been instructed?', 'آیت کریمہ میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو کس بات کی تلقین کی گئی ہے؟', 'په آیت کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته د کومې خبرې لارښوونه شوې؟')
    AR(b, f'(3) {words(42, 29, 1, 10)}', 'In the verse, which things have been declared among the signs of Allah Almighty?', 'آیت کریمہ میں کن چیزوں کو اللہ تعالیٰ کی نشانیوں میں سے قرار دیا گیا ہے؟', 'په آیت کې کوم شیان د الله تعالی له نښو ګڼل شوي؟')
    AR(b, f'(4) {words(42, 37)}', 'Which excellent qualities of the people of faith are mentioned in the verse?', 'آیت کریمہ میں اہلِ ایمان کی کن عمدہ صفات کا ذکر ہے؟', 'په آیت کې د مؤمنانو د کومو غوره صفتونو یادونه ده؟')
    AR(b, f'(5) {words(42, 38)}', 'What qualities of the people of faith have been stated in the verse?', 'آیت کریمہ میں اہلِ ایمان کے کیا اوصاف بیان ہوئے ہیں؟', 'په آیت کې د مؤمنانو کوم صفتونه بیان شوي؟')
    AR(b, f'(6) {words(42, 43)}', 'In the verse, which deeds have been declared deeds of courage?', 'آیت کریمہ میں کن کاموں کو ہمت کے کام قرار دیا گیا ہے؟', 'په آیت کې کوم کارونه د همت کارونه ګڼل شوي؟')
    AR(b, f'(7) {words(42, 48, 13, 30)}', 'What general behaviour of man on receiving mercy and on being touched by evil is mentioned in the verse?', 'آیت کریمہ میں رحمت اور برائی پہنچنے پر انسان کے کس عمومی طرزِ عمل کا ذکر ہے؟', 'په آیت کې د رحمت او بدۍ د رسېدو پر مهال د انسان د کوم عمومي چلند یادونه ده؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(42, 13, 2, 25)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Shura.', 'سُوْرَةُ الشُّوْرٰی کا تعارف تحریر کریں۔', 'د سورة الشوری پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(42, 50)}', *TR)
    AR(b, '(2b)', 'State a summary of the basic themes of Surah al-Shura.', 'سُوْرَةُ الشُّوْرٰی کے بنیادی مضامین کا خلاصہ بیان کریں۔', 'د سورة الشوری د بنسټیزو مضامینو لنډیز بیان کړئ.')
    AR(b, f'(3a) {words(42, 51)}', *TR)
    AR(b, '(3b)', 'State the importance of consultation according to Surah al-Shura.', 'سُوْرَةُ الشُّوْرٰی کی رو سے مشورہ کی اہمیت بیان کریں۔', 'د سورة الشوری له مخې د مشورې اهمیت بیان کړئ.')
    b.h(*ACT)
    L(b, [(f'In the light of {words(42, 13, 20, 25)}, discuss the purpose of the sending of the noble Prophets (peace be upon them).', f'{words(42, 13, 20, 25)} کی روشنی میں انبیاء کرام علیہم السلام کی بعثت کے مقصد پر مباحثہ کریں۔', f'د {words(42, 13, 20, 25)} په رڼا کې د انبیاء کرامو علیهم السلام د بعثت پر موخه بحث وکړئ.'),
          ('Compare the Islamic system of consultation with the present national system. Learn the importance of consultation from your teachers.', 'اسلامی نظامِ مشاورت اور موجودہ ملکی نظام کا موازنہ کریں۔ مشورہ کی اہمیت اساتذہ کرام سے معلوم کریں۔', 'د مشورې اسلامي نظام او اوسني ملي نظام پرتله کړئ؛ د مشورې اهمیت له ښوونکو زده کړئ.')])
    b.h(*TCH)
    L(b, [('In the light of Surah al-Shura, make the students aware of the kinds of revelation.', 'سُوْرَةُ الشُّوْرٰی کی روشنی میں طلبہ کو وحی کی اقسام سے آگاہ کریں۔', 'د سورة الشوری په رڼا کې زده‌کوونکي د وحې له ډولونو خبر کړئ.'),
          ('Hold a discussion with the students on the harms of anger and the benefits of pardon and forbearance.', 'طلبہ کو غصے کے نقصانات اور عفو و درگزر کے فوائد پر مذاکرہ کرائیں۔', 'له زده‌کوونکو سره د غوسې د زیانونو او د بښنې او تېرېدو د ګټو په اړه بحث وکړئ.')])
    BOOK.save(147, [(14, rec(b, 14, 147, 147, kind='exercise'))], complete_units=[14], issues=[{'id': 'mq12-pdf147', 'unit': 14, 'printedPage': 144,
               'description': 'Q3 1a quotes 42:13 up to "وَلَا تَتَفَرَّقُوا فِيهِ" as printed. Q2 6 prints "وَلَمَنْ صَبَرَ وَغَفَرَ…" (42:43). Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p147()
