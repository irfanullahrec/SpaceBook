"""Mutalia-e-Quran XII PDF164: p.161 — Lesson 16 exercise Q2 items 4–7, Q3, activities, teachers' guidance. Run: python class12_quran_page164.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p164():
    b = Builder()
    AR(b, f'(4) {words(48, 11, 1, 10)}', 'In the verse, what excuse did the desert Arabs who stayed behind from jihad present?', 'آیت کریمہ میں جہاد سے پیچھے رہ جانے والے دیہاتیوں نے کیا عذر پیش کیا؟', 'په آیت کې له جهاد شاته پاتې شویو کلیوالو کوم عذر وړاندې کړ؟')
    AR(b, f'(5) {words(48, 18)}', 'What rewards did Allah Almighty bestow upon the noble Companions (may Allah be pleased with them) who took part in Bay\'at al-Ridwan?', 'بیعتِ رضوان میں شامل صحابہ کرام رضی اللہ تعالیٰ عنہم پر اللہ تعالیٰ نے کیا انعامات فرمائے؟', 'الله تعالی د رضوان په بیعت کې پر ګډونوالو صحابه کرامو رضي الله عنهم کوم انعامونه وکړل؟')
    AR(b, f'(6) {words(48, 29, 5, 27)}', 'What attributes of the noble Companions (may Allah be pleased with them) have been stated in the verse?', 'آیت کریمہ میں صحابہ کرام رضی اللہ تعالیٰ عنہم کی کیا صفات بیان ہوئی ہیں؟', 'په آیت کې د صحابه کرامو رضي الله عنهم کوم صفتونه بیان شوي؟')
    AR(b, f'(7) {words(48, 29, 51, 60)}', 'What has Allah Almighty promised the people of faith in the verse?', 'آیت کریمہ میں اللہ تعالیٰ نے اہلِ ایمان سے کیا وعدہ فرمایا ہے؟', 'په آیت کې الله تعالی له مؤمنانو سره څه وعده کړې؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(48, 10)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Fath.', 'سُوْرَةُ الْفَتْحِ کا تعارف تحریر کریں۔', 'د سورة الفتح پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(48, 14)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Fath.', 'سُوْرَةُ الْفَتْحِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الفتح ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(48, 28)}', *TR)
    AR(b, '(3b)', 'Write the occasion of revelation of Surah al-Fath.', 'سُوْرَةُ الْفَتْحِ کا شانِ نزول تحریر کریں۔', 'د سورة الفتح د نزول شالید ولیکئ.')
    b.h(*ACT)
    L(b, [('Find out the details of the event of the Treaty of Hudaybiyah and identify its important points.', 'صلح حدیبیہ کے واقعہ کی تفصیلات معلوم کر کے اہم نکات کی نشان دہی کریں۔', 'د حدیبیې د سولې د پېښې تفصیلات معلوم کړئ او مهم ټکي یې په ګوته کړئ.'),
          ('Collect a few incidents of the noble Companions (may Allah be pleased with them) concerning respect and reverence for the Holy Prophet (peace and blessings of Allah be upon him).', 'نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے ادب و تعظیم کے حوالے صحابہ کرام رضی اللہ تعالیٰ عنہم کے چند واقعات جمع کریں۔', 'د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د ادب او درناوي په اړه د صحابه کرامو رضي الله عنهم ځینې پېښې راټولې کړئ.')])
    b.h(*TCH)
    L(b, [('Hold a discussion with the students on the events of Bay\'at al-Ridwan.', 'بیعتِ رضوان کے واقعات پر طلبہ کو مذاکرہ کرائیں۔', 'له زده‌کوونکو سره د رضوان د بیعت پر پېښو بحث وکړئ.'),
          ('In the light of Surah al-Fath, make the students aware of the role and status of Sayyiduna \'Uthman Dhu\'l-Nurayn (may Allah be pleased with him).', 'سُوْرَةُ الْفَتْحِ کی روشنی میں سیدنا عثمان ذوالنورین رضی اللہ تعالیٰ عنہ کے کردار اور مقام کے حوالے سے طلبہ کو آگاہ کریں۔', 'د سورة الفتح په رڼا کې زده‌کوونکي د سیدنا عثمان ذوالنورین رضي الله عنه له کړنو او مقام خبر کړئ.'),
          ('In Surah al-Fath the favours of the Exalted Lord upon the Holy Prophet (peace and blessings of Allah be upon him) and the noble Companions (may Allah be pleased with them) have been stated. Hold a discussion on this.', 'سُوْرَةُ الْفَتْحِ میں نبی اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم اور صحابہ کرام رضی اللہ تعالیٰ عنہم پر انعاماتِ باری تعالیٰ کا بیان فرمایا گیا ہے۔ اس پر مباحثہ کرائیں۔', 'په سورة الفتح کې پر نبي اکرم صلی الله علیه وعلی آله واصحابه وسلم او صحابه کرامو رضي الله عنهم د باري تعالی انعامونه بیان شوي؛ پر دې بحث وکړئ.')])
    BOOK.save(164, [(16, rec(b, 16, 164, 164, kind='exercise'))], complete_units=[16], issues=[{'id': 'mq12-pdf164', 'unit': 16, 'printedPage': 161,
               'description': 'Activity line 2 prints "کے ادب و تعظیم کے حوالے صحابہ کرام" (missing "سے"; kept). Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p164()
