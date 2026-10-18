"""Mutalia-e-Quran XII PDF45: p.42 — Lesson 4 exercise Q2 items 5–7, Q3, activities, teachers' guidance. Run: python class12_quran_page045.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p45():
    b = Builder()
    AR(b, f'(5) {words(4, 116)}', 'What reality has been stated in the verse concerning shirk?', 'آیت کریمہ میں شرک کے حوالے سے کیا حقیقت بیان ہوئی ہے؟', 'په آیت کې د شرک په اړه کوم حقیقت بیان شوی؟')
    AR(b, f'(6) {words(4, 117)}', 'Which evil beliefs of the disbelievers have been stated in the verse?', 'آیت کریمہ میں کفار کے کن برے عقائد کا بیان کیا گیا ہے؟', 'په آیت کې د کافرانو کومې بدې عقیدې بیان شوې؟')
    AR(b, f'(7) {words(4, 127, 34, 42)}', 'What reality has been stated in the verse concerning good deeds?', 'آیت کریمہ میں نیک اعمال کے حوالے سے کیا حقیقت بیان کی گئی ہے؟', 'په آیت کې د نېکو عملونو په اړه کوم حقیقت بیان شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(4, 101)}', *TR)
    AR(b, f'(1b) {words(4, 114, 2, 17)}', 'According to the verse, which kind of secret talk has been declared the cause of a great reward?', 'آیت کریمہ کے مطابق کس قسم کی سرگوشی کو اجرِ عظیم کا باعث قرار دیا گیا ہے؟', 'د آیت له مخې کوم ډول پټې خبرې د لوی اجر لامل ګڼل شوې؟')
    AR(b, f'(2a) {words(4, 109)}', *TR)
    AR(b, f'(2b) {words(4, 115)}', 'Which person has been declared deserving of the warning mentioned in the verse?', 'آیت کریمہ میں ذکر کردہ وعید کا مستحق کس شخص کو قرار دیا گیا ہے؟', 'په آیت کې د یاد شوي ګواښ مستحق کوم کس ګڼل شوی؟')
    AR(b, f'(3a) {words(4, 131)}', *TR)
    AR(b, f'(3b) {words(4, 125)}', 'Whom has the verse declared the best person in respect of religion?', 'آیت کریمہ میں دین کے لحاظ سے سب سے بہتر شخص کس کو قرار دیا گیا ہے؟', 'په آیت کې د دین له پلوه تر ټولو غوره کس څوک ګڼل شوی؟')
    b.h(*ACT)
    L(b, [('Learn about the prayer of fear from your teachers.', 'نمازِ خوف کے بارے میں اپنے اساتذہ سے معلوم کریں۔', 'د وېرې د لمانځه په اړه له خپلو ښوونکو معلومات واخلئ.'),
          ('Arrange the beginning and ending times of the five prayers of one month, with regard to winter and summer, in the form of a chart.', 'ایک ماہ کی پانچوں نمازوں کی ابتدا انتہا کے اوقات کو سردی و گرمی کے اعتبار سے چارٹ کی صورت میں مرتب کریں۔', 'د یوې میاشتې د پنځو لمونځونو د پیل او پای وختونه د ژمي او اوړي له مخې د چارټ په بڼه ترتیب کړئ.'),
          ('Learn the masnun adhkar after prayer and make arrangements to recite them regularly.', 'نماز کے بعد کے مسنون اذکار معلوم کر کے انھیں باقاعدگی کے ساتھ پڑھنے کا اہتمام کریں۔', 'له لمانځه وروسته مسنون اذکار زده کړئ او په منظم ډول یې د ویلو اهتمام وکړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the commands of the shortened (qasr) prayer.', 'طلبہ کو نمازِ قصر کے احکام سے آگاہ کریں۔', 'زده‌کوونکي د قصر لمانځه له حکمونو خبر کړئ.'),
          ('Make the students aware of the various forms of involving people in one of the important aims of the devils, "فَلَيُغَيِّرُنَّ خَلْقَ اللَّهِ".', 'شیاطین کے ایک اہم ہدف ”فَلَيُغَيِّرُنَّ خَلْقَ اللّٰهِ“ میں مبتلا کرنے کی مختلف صورتوں سے طلبہ آگاہ کریں۔', 'زده‌کوونکي د شیطانانو د یوه مهم هدف «فَلَيُغَيِّرُنَّ خَلْقَ اللَّهِ» ته د اخته کولو له بېلابېلو بڼو خبر کړئ.'),
          ('Make the students aware of the excellence of bringing about reconciliation among people.', 'آپس میں صلح کرانے کی فضیلت سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي په خپل منځ کې د روغې جوړې د راوستلو له فضیلت خبر کړئ.')])
    BOOK.save(45, [(4, rec(b, 4, 45, 45, kind='exercise'))], complete_units=[4], issues=[{'id': 'mq12-pdf045', 'unit': 4, 'printedPage': 42,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p45()
