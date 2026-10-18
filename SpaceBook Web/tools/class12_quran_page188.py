"""Mutalia-e-Quran XII PDF188: p.185 — Lesson 19 exercise Q3 (3), activities, teachers' guidance. Run: python class12_quran_page188.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, TR, ACT, TCH, words


def p188():
    b = Builder()
    AR(b, f'(3a) {words(58, 14)}', *TR)
    AR(b, f'(3b) {words(58, 9)}', 'What teaching have the people of faith been given in the verse concerning secret counsels?', 'آیت کریمہ میں اہلِ ایمان کو سرگوشیوں کے حوالے سے کیا تعلیم دی گئی ہے؟', 'په آیت کې مؤمنانو ته د پټو مشورو په اړه کومه لارښوونه شوې؟')
    b.h(*ACT)
    L(b, [('In Surah al-Mujadilah the etiquette of gatherings is mentioned. Search for further etiquette of gatherings from the blessed hadiths and discuss them among yourselves.', 'سُوْرَةُ الْمُجَادَلَةِ میں آدابِ مجلس کا تذکرہ ہے۔ احادیثِ مبارکہ سے مجلس کے مزید آداب تلاش کر کے آپس میں مذاکرہ کریں۔', 'په سورة المجادله کې د مجلس د آدابو یادونه ده؛ له مبارکو حدیثونو د مجلس نور آداب ولټوئ او په خپل منځ کې پرې بحث وکړئ.'),
          ('Search for a noble hadith about secret counsel.', 'سرگوشی کے حوالے سے کوئی ایک حدیث شریف تلاش کریں۔', 'د پټې مشورې په اړه کوم یو حدیث شریف ولټوئ.')])
    b.h(*TCH)
    L(b, [('Zihar is mentioned at the beginning of Surah al-Mujadilah. Explain well to the students the meaning and commands of zihar.', 'سُوْرَةُ الْمُجَادَلَةِ کے آغاز میں ظہار کا تذکرہ کیا گیا ہے۔ طلبہ کو ظہار کا مفہوم اور احکام اچھی طرح سمجھائیں۔', 'د سورة المجادله په پیل کې د ظهار یادونه شوې؛ زده‌کوونکو ته د ظهار مانا او حکمونه ښه وپوهوئ.'),
          ('In verse 11 of Surah al-Mujadilah the elevation of the ranks of the people of knowledge is mentioned. Hold a discussion among the students under the title "Knowledge is light".', 'سُوْرَةُ الْمُجَادَلَةِ کی آیت ۱۱ میں علم والوں کے درجات کی بلندی کا ذکر ہے۔ "علم روشنی ہے" کے عنوان پر طلبہ کے درمیان مذاکرہ کرائیں۔', 'د سورة المجادله په ۱۱ آیت کې د علم والو د درجو د لوړوالي یادونه ده؛ د «علم رڼا ده» تر سرلیک لاندې د زده‌کوونکو ترمنځ بحث وکړئ.'),
          ('In Surah al-Mujadilah Hizb Allah (the party of Allah) and Hizb al-Shaytan (the party of Satan) are mentioned. Make the students aware in detail about both groups.', 'سُوْرَةُ الْمُجَادَلَةِ میں حزب اللہ اور حزب الشیطان کا تذکرہ کیا گیا ہے۔ طلبہ کو دونوں گروہوں کے بارے میں تفصیل سے آگاہ کریں۔', 'په سورة المجادله کې د حزب الله او حزب الشیطان یادونه شوې؛ زده‌کوونکي د دواړو ډلو په اړه په تفصیل خبر کړئ.')])
    BOOK.save(188, [(19, rec(b, 19, 188, 188, kind='exercise'))], complete_units=[19], issues=[{'id': 'mq12-pdf188', 'unit': 19, 'printedPage': 185,
               'description': 'Lower half of p.185 blank. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p188()
