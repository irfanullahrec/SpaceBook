"""Mutalia-e-Quran XII PDF180: p.177 — Lesson 18 exercise Q2 item 7, Q3, activities, teachers' guidance. Run: python class12_quran_page180.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p180():
    b = Builder()
    AR(b, f'(7) {words(57, 29)}', 'Which wrong idea of the People of the Book has been refuted in the verse?', 'آیت کریمہ میں اہلِ کتاب کے کس غلط خیال کی تردید کی گئی ہے؟', 'په آیت کې د اهل کتابو کوم ناسم فکر رد شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(57, 4)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Hadid.', 'سُوْرَةُ الْحَدِيْدِ کا تعارف تحریر کریں۔', 'د سورة الحدید پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(57, 9)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Hadid.', 'سُوْرَةُ الْحَدِيْدِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الحدید ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(57, 22)}', *TR)
    AR(b, f'(3b) {words(57, 10, 1, 26)}', 'In the verse, which two groups have been compared?', 'آیت کریمہ میں کن دو گروہوں کا تقابل کیا گیا ہے؟', 'په آیت کې د کومو دوو ډلو پرتله شوې؟')
    b.h(*ACT)
    L(b, [('In Surah al-Hadid the condition of the believers and the hypocrites on the Day of Resurrection and their mutual dialogue are stated. Draw out important points from it and discuss them.', 'سُوْرَةُ الْحَدِيْدِ میں قیامت کے دن مومنین اور منافقین کی کیفیت اور باہمی مکالمہ بیان ہوا ہے اس سے اہم نکات اخذ کر کے مذاکرہ کریں۔', 'په سورة الحدید کې د قیامت په ورځ د مؤمنانو او منافقانو حالت او خپل منځي خبرې اترې بیان شوې؛ له هغو مهم ټکي راوباسئ او بحث وکړئ.'),
          ('In Surah al-Hadid one characteristic of iron, its use in war, has been mentioned explicitly. Arrange a list of its further characteristics and benefits and debate it among yourselves.', 'سُوْرَةُ الْحَدِيْدِ میں لوہے کی ایک خصوصیت جنگ میں کام آنے کی صراحت کے ساتھ ذکر کی گئی ہے۔ اس کی مزید خصوصیات اور فوائد کی فہرست مرتب کر کے آپس میں مباحثہ کریں۔', 'په سورة الحدید کې د اوسپنې یوه ځانګړنه، په جګړه کې کارېدل، په صراحت یاده شوې؛ د هغې د نورو ځانګړنو او ګټو لړلیک ترتیب کړئ او په خپل منځ کې بحث وکړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the excellence and importance of spending in the way of Allah and of qard hasan.', 'انفاق فی سبیل اللہ اور قرضِ حسنہ کی فضیلت اور اہمیت سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي د الله په لار کې د لګښت او ښه پور له فضیلت او اهمیت خبر کړئ.'),
          ('In Surah al-Hadid the Christians\' adoption of monasticism is mentioned. Explain to the students its background and the meaning of monasticism in detail.', 'سُوْرَةُ الْحَدِيْدِ میں عیسائیوں کے رہبانیت اختیار کرنے کا تذکرہ کیا گیا ہے۔ طلبہ کو اس کا پس منظر، رہبانیت کا مفہوم تفصیل سے سمجھائیں۔', 'په سورة الحدید کې د عیسویانو له خوا د رهبانیت د غوره کولو یادونه شوې؛ زده‌کوونکو ته یې شالید او د رهبانیت مانا په تفصیل وپوهوئ.')])
    BOOK.save(180, [(18, rec(b, 18, 180, 180, kind='exercise'))], complete_units=[18], issues=[{'id': 'mq12-pdf180', 'unit': 18, 'printedPage': 177,
               'description': 'Q3 parts are printed with the labels misaligned (1a/1b on 57:4 split across two lines; 2a/2b labels on the introduction and 57:9) — kept in the order 1a verse, 1b introduction, 2a verse, 2b themes. Lower part of p.177 blank.'}])


if __name__ == '__main__':
    p180()
