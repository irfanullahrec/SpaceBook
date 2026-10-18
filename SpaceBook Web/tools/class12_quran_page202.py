"""Mutalia-e-Quran XII PDF202: p.199 — Lesson 21 exercise Q2, Q3, activities, teachers' guidance. Run: python class12_quran_page202.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q2, Q3, TR, ACT, TCH, words


def p202():
    b = Builder()
    b.p(*Q2)
    AR(b, f'(1) {words(60, 2)}', 'Which blameworthy intentions of the disbelievers have been stated?', 'کفار کے کن مذموم عزائم کا بیان ہے؟', 'د کافرانو د کومو ناوړه نیتونو بیان دی؟')
    AR(b, f'(2) {words(60, 3)}', 'Of the not benefiting of whom on the Day of Resurrection is mention made?', 'قیامت کے دن کس کس کے نفع نہ دینے کا ذکر ہے؟', 'د قیامت په ورځ د چا چا د ګټې نه رسولو یادونه ده؟')
    AR(b, f'(3) {words(60, 6, 1, 12)}', 'For which people is there an excellent example present in the verse?', 'آیت کریمہ میں کن لوگوں کے لیے اسوۂ حسنہ موجود ہے؟', 'په آیت کې د کومو خلکو لپاره غوره بېلګه شته؟')
    AR(b, f'(4) {words(60, 7)}', 'In the verse, between which people has Allah Almighty given news of love arising?', 'آیت کریمہ میں اللہ تعالیٰ نے کن لوگوں کے درمیان محبت پیدا ہونے کی خبر دی ہے؟', 'په آیت کې الله تعالی د کومو خلکو ترمنځ د مینې د پیدا کېدو خبر ورکړی؟')
    AR(b, f'(5) {words(60, 10, 14, 20)}', 'What guidance has been given to the people of faith concerning emigrant women?', 'ہجرت کرنے والی عورتوں کے بارے میں اہلِ ایمان کو کیا ہدایت دی گئی ہے؟', 'د هجرت کوونکو ښځو په اړه مؤمنانو ته څه لارښوونه شوې؟')
    AR(b, f'(6) {words(60, 10, 48, 53)}', 'In the verse, what command has been given to the Muslims and the disbelievers concerning the dower?', 'آیت کریمہ میں مسلمانوں اور کفار کو مہر کے حوالے سے کیا حکم دیا گیا ہے؟', 'په آیت کې مسلمانانو او کافرانو ته د مهر په اړه کوم حکم شوی؟')
    AR(b, f'(7) {words(60, 13)}', 'What advice has been given to the people of faith in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا نصیحت کی گئی ہے؟', 'په آیت کې مؤمنانو ته څه نصیحت شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(60, 5)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Mumtahanah.', 'سُوْرَةُ الْمُمْتَحِنَةِ کا تعارف تحریر کریں۔', 'د سورة الممتحنه پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(60, 8)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Mumtahanah.', 'سُوْرَةُ الْمُمْتَحِنَةِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة الممتحنه ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(60, 11)}', *TR)
    AR(b, f'(3b) {words(60, 12, 1, 30)}', 'In this verse, on which matters has the Holy Prophet (peace and blessings of Allah be upon him) been commanded to take the pledge from emigrant women?', 'اس آیت میں نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو مہاجر عورتوں سے کن باتوں پر بیعت کا حکم دیا گیا ہے؟', 'په دې آیت کې نبي کریم صلی الله علیه وعلی آله واصحابه وسلم ته د مهاجرو ښځو څخه پر کومو خبرو د بیعت حکم شوی؟')
    b.h(*ACT)
    L(b, [('Arrange a list of the matters on which taking a pledge is commanded in Surah al-Mumtahanah, and discuss them among yourselves.', 'سُوْرَةُ الْمُمْتَحِنَةِ میں جن امور پر بیعت لینے کا حکم ہے اس کی فہرست مرتب کر کے آپس میں مذاکرہ کریں۔', 'په سورة الممتحنه کې چې پر کومو چارو د بیعت اخیستلو حکم دی، د هغو لړلیک ترتیب کړئ او په خپل منځ کې پرې بحث وکړئ.'),
          ('Memorise orally the supplications of Sayyiduna Ibrahim (peace be upon him) mentioned in Surah al-Mumtahanah and make reciting them your routine.', 'سُوْرَةُ الْمُمْتَحِنَةِ میں سیدنا ابراہیم علیہ السلام کی ذکر کردہ دعائیں زبانی یاد کریں اور انھیں پڑھنے کا معمول بنائیں۔', 'په سورة الممتحنه کې د سیدنا ابراهیم علیه السلام یادې شوې دعاوې په یاد کړئ او د هغو ویل خپل معمول کړئ.')])
    b.h(*TCH)
    L(b, [('Make the students aware of the rights of non-Muslim minorities in an Islamic state.', 'اسلامی ریاست میں غیر مسلم اقلیتوں کے حقوق سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي په اسلامي دولت کې د غیر مسلمو لږکیو له حقونو خبر کړئ.'),
          ('In the light of Surah al-Mumtahanah, make clear to the students the internal and external principles and rules of an Islamic state.', 'سُوْرَةُ الْمُمْتَحِنَةِ کی روشنی میں اسلامی ریاست کے داخلی اور خارجی اصول و ضوابط طلبہ پر واضح کریں۔', 'د سورة الممتحنه په رڼا کې زده‌کوونکو ته د اسلامي دولت داخلي او خارجي اصول او قواعد روښانه کړئ.')])
    BOOK.save(202, [(21, rec(b, 21, 202, 202, kind='exercise'))], complete_units=[21], issues=[{'id': 'mq12-pdf202', 'unit': 21, 'printedPage': 199,
               'description': 'Q3 3b quotes 60:12 up to "فِي مَعْرُوفٍ". Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p202()
