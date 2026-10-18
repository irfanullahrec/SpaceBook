"""Mutalia-e-Quran XII PDF219: p.216 — Lesson 23 exercise Q3, activities, teachers' guidance. Run: python class12_quran_page219.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p219():
    b = Builder()
    b.p(*Q3)
    AR(b, f'(1a) {words(63, 8)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Munafiqun.', 'سُوْرَةُ الْمُنٰفِقُوْنَ کا تعارف تحریر کریں۔', 'د سورة المنافقون پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(63, 11)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Munafiqun.', 'سُوْرَةُ الْمُنٰفِقُوْنَ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة المنافقون ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(64, 9)}', *TR)
    AR(b, '(3b)', 'Write an introduction to Surah al-Taghabun.', 'سُوْرَةُ التَّغَابُنِ کا تعارف تحریر کریں۔', 'د سورة التغابن پېژندنه ولیکئ.')
    AR(b, f'(4a) {words(64, 14)}', *TR)
    AR(b, '(4b)', 'Write some basic themes of Surah al-Taghabun.', 'سُوْرَةُ التَّغَابُنِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة التغابن ځینې بنسټیز مضامین ولیکئ.')
    b.h(*ACT)
    L(b, [('Collect information about the signs of hypocrisy, the character of the hypocrites of Madinah and their end, and discuss it.', 'نفاق کی علامات، منافقینِ مدینہ کا کردار اور ان کے انجام کے حوالے سے معلومات جمع کر کے مذاکرہ کریں۔', 'د نفاق د نښو، د مدینې د منافقانو د کړنو او د هغوی د پایلې په اړه معلومات راټول کړئ او پرې بحث وکړئ.'),
          ('Learn from your teachers the details of the matters declared beneficial for the people of faith in verses 14 to 18 of Surah al-Taghabun.', 'سُوْرَةُ التَّغَابُنِ کی آیت ۱۴ تا ۱۸ میں جن امور کو اہلِ ایمان کے لیے مفید قرار دیا گیا ہے ان کی تفصیل اپنے اساتذہ سے معلوم کریں۔', 'د سورة التغابن د ۱۴ تر ۱۸ آیتونو کې کومې چارې چې د مؤمنانو لپاره ګټورې ګرځول شوې، د هغو تفصیل له خپلو ښوونکو زده کړئ.'),
          ('Collect the attributes of Allah Almighty stated in Surah al-Taghabun and reflect on their meanings.', 'سُوْرَةُ التَّغَابُنِ میں بیان کردہ اللہ تعالیٰ کی صفات جمع کر کے ان کے معانی میں غور و فکر کریں۔', 'په سورة التغابن کې د الله تعالی بیان شوي صفتونه راټول کړئ او د هغو په ماناوو کې فکر وکړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the importance and virtues of spending in the way of Allah in the light of the Qur\'an and Sunnah.', 'طلبہ کو قرآن و سنت کی روشنی میں انفاق فی سبیل اللہ کی اہمیت اور فضائل سے آگاہ کریں۔', 'زده‌کوونکي د قرآن او سنت په رڼا کې د الله په لار کې د لګښت له اهمیت او فضیلتونو خبر کړئ.'),
          ('What should be the attitude of a believer in afflictions? Explain by giving some example from the Qur\'an Majid, the blessed hadiths and the Prophetic Sirah (peace and blessings of Allah be upon him).', 'مصائب پر مومن کا طرزِ عمل کیا ہونا چاہیے؟ قرآن مجید، احادیثِ مبارکہ اور سیرتِ نبوی صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم سے کوئی مثال دے کر وضاحت کریں۔', 'پر مصیبتونو د مؤمن چلند باید څنګه وي؟ له قرآن مجید، مبارکو حدیثونو او نبوي سیرت صلی الله علیه وعلی آله واصحابه وسلم څخه د کومې بېلګې په ورکولو سره یې روښانه کړئ.')])
    BOOK.save(219, [(23, rec(b, 23, 219, 219, kind='exercise'))], complete_units=[23], issues=[{'id': 'mq12-pdf219', 'unit': 23, 'printedPage': 216,
               'description': 'Lower part of p.216 blank. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p219()
