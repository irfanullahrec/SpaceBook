"""Mutalia-e-Quran XII PDF17: p.14 — Lesson 1 exercise: Q1 MCQs, Q2 short answers. Run: python class12_quran_page017.py"""
from class12_quran_common import BOOK, Builder, rec, AR, words


def mcq(b, n, ar, q, opts):
    AR(b, f'({n}) {ar}', q[0], q[1], q[2])
    b.group('list', [(f'{k[0]}. {o[0]}', f'{k[1]}: {o[1]}', f'{k[2]}. {o[2]}') for k, o in zip([('a', 'الف', 'الف'), ('b', 'ب', 'ب'), ('c', 'ج', 'ج'), ('d', 'د', 'د')], opts)])


def p17():
    b = Builder()
    b.h('Exercise', 'مشق', 'تمرین')
    b.p('Question 1: Put a tick (✓) on the correct answer:', 'سوال ۱: درست جواب پر صحیح (✓) کا نشان لگائیں:', '۱ پوښتنه: پر سم ځواب (✓) نښه ولګوئ:')
    mcq(b, 1, words(4, 1, 1, 4), ('— in it people are commanded to:', 'میں انسانوں کو حکم ہے:', '— په دې کې انسانانو ته حکم دی:'),
        [('spend', 'انفاق کا', 'د انفاق'), ('give charity', 'صدقہ دینے کا', 'د صدقې ورکولو'), ('be God-fearing', 'پرہیزگاری کا', 'د پرهېزګارۍ'), ('obey', 'اطاعت کا', 'د اطاعت')])
    mcq(b, 2, words(4, 4, 1, 4), ('— in this verse the command is to give the woman:', 'آیت کریمہ میں عورت کو دینے کا حکم ہے:', '— په دې آیت کې ښځې ته د ورکولو حکم دی:'),
        [('clothing', 'لباس', 'جامې'), ('housing', 'رہائش', 'استوګنځی'), ('food', 'کھانا', 'خواړه'), ('mahr', 'مہر', 'مهر')])
    mcq(b, 3, words(4, 10, 1, 11), ('— according to it the verse carries a warning for:', 'کی رو سے آیت میں وعید ہے:', '— له دې سره سم په آیت کې ګواښ دی:'),
        [('those who take bribes', 'رشوت لینے والوں کے لیے', 'بډې اخیستونکو ته'), ('those who lie', 'جھوٹ بولنے والوں کے لیے', 'درواغجنو ته'), ('those who wrongfully eat the wealth of orphans', 'یتیم کا مال ناحق کھانے والوں کے لیے', 'د یتیم د مال په ناحقه خوړونکو ته'), ('those who break promises', 'وعدہ خلافی کرنے والوں کے لیے', 'ژمنه ماتوونکو ته')])
    mcq(b, 4, words(4, 11, 6, 9), ('— according to it the share for a son is:', 'کے مطابق بیٹے کے لیے حصہ ہے:', '— له دې سره سم د زوی برخه ده:'),
        [('equal to one daughter', 'ایک بیٹی کے برابر', 'د یوې لور په اندازه'), ('equal to two daughters', 'دو بیٹیوں کے برابر', 'د دوو لوڼو په اندازه'), ('equal to three daughters', 'تین بیٹیوں کے برابر', 'د درېیو لوڼو په اندازه'), ('equal to four daughters', 'چار بیٹیوں کے برابر', 'د څلورو لوڼو په اندازه')])
    mcq(b, 5, words(4, 12, 30, 38), ('— according to the verse, the wife\'s share in inheritance when there are no children is:', 'آیت کریمہ کی رو سے بیوی کا اولاد نہ ہونے کی صورت میں وراثت میں حصہ ہے:', '— د آیت له مخې د اولاد د نه شتون په صورت کې په میراث کې د مېرمنې برخه ده:'),
        [('half', 'آدھا', 'نیمایي'), ('a quarter', 'چوتھائی', 'څلورمه'), ('a sixth', 'چھٹا', 'شپږمه'), ('an eighth', 'آٹھواں', 'اتمه')])
    mcq(b, 6, words(4, 24, 2, 2), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('unmarried women', 'کنواری عورتیں', 'نا واده شوې ښځې'), ('divorced women', 'طلاق والی عورتیں', 'طلاقې ښځې'), ('married women', 'شادی شدہ عورتیں', 'واده شوې ښځې'), ('old women', 'بوڑھی عورتیں', 'زړې ښځې')])
    mcq(b, 7, words(4, 25, 36, 37), ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('women keeping secret friendships', 'چھپی دوستی کرنے والیاں', 'پټې دوستۍ نیوونکې'), ('women who marry', 'نکاح کرنے والیاں', 'نکاح کوونکې'), ('women who disobey', 'نافرمانی کرنے والیاں', 'نافرمانه'), ('women who hate', 'نفرت کرنے والیاں', 'کرکه کوونکې')])
    b.p('Question 2: Give short answers to the following questions:', 'سوال ۲: مندرجہ ذیل سوالات کے مختصر جوابات دیجیے:', '۲ پوښتنه: لاندې پوښتنو ته لنډ ځوابونه ورکړئ:')
    AR(b, f'(1) {words(4, 1, 1, 17)}', 'What has the verse told about the multiplication of the human race?', 'آیت کریمہ میں انسانوں کی افزائش نسل کے حوالے سے کیا بتایا گیا ہے؟', 'په آیت کې د انسانانو د نسل د زیاتېدو په اړه څه ویل شوي؟')
    AR(b, f'(2) {words(4, 2, 10, 19)}', 'Which act has the verse declared a great sin?', 'آیت کریمہ میں بڑا گناہ کس عمل کو قرار دیا گیا ہے؟', 'په آیت کې کوم عمل لویه ګناه ګڼل شوی؟')
    AR(b, f'(3) {words(4, 3, 17, 21)}', 'In which situation has the verse given the instruction to be content with only one marriage?', 'آیت کریمہ میں ایک ہی نکاح پر اکتفا کرنے کی ہدایت کس صورت میں دی گئی ہے؟', 'په آیت کې پر یوازې یوې نکاح د بسنه کولو لارښوونه په کوم صورت کې شوې؟')
    AR(b, f'(4) {words(4, 6, 7, 13)}', 'According to the verse, when has it been emphasised to hand over to orphans their wealth?', 'آیت کریمہ کے مطابق یتیموں کو ان کے اموال کب حوالے کرنے کی تاکید کی گئی ہے؟', 'د آیت له مخې یتیمانو ته د هغوی د مالونو د سپارلو ټینګار کله شوی؟')
    AR(b, f'(5) {words(4, 8)}', 'What teaching has the verse given about non-heirs at the time of dividing the inheritance?', 'آیت کریمہ میں ترکے کی تقسیم کے وقت غیر وارثوں کے حوالے سے کیا تعلیم دی گئی ہے؟', 'په آیت کې د ترکې د وېش پر مهال د ناوارثانو په اړه څه لارښوونه شوې؟')
    BOOK.save(17, [(1, rec(b, 1, 17, 17, kind='exercise'))], issues=[{'id': 'mq12-pdf017', 'unit': 1, 'printedPage': 14,
               'description': 'Exercise questions quote verse fragments in Arabic; these are drawn word-for-word from the reference Uthmani text matching the printed fragments. No printed answer key.'}])


if __name__ == '__main__':
    p17()
