"""Mutalia-e-Quran XII PDF36: p.33 — Lesson 3 exercise Q1 items 5–7, Q2, Q3 (start). Run: python class12_quran_page036.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p36():
    b = Builder()
    MCQ(b, 5, 'كِفْلٌ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('burden', 'بوجھ', 'بار'), ('benefit', 'فائدہ', 'ګټه'), ('fate', 'قسمت', 'برخلیک'), ('favour', 'احسان', 'احسان')])
    MCQ(b, 6, words(4, 94, 4, 9), ('— according to it, when the believers set out on a journey for jihad in the way of Allah Almighty they have been commanded:', 'کی رو سے اہلِ ایمان کو اللہ تعالیٰ کی راہ میں جہاد کے لیے سفر پر نکلتے وقت حکم دیا گیا ہے:', '— له دې سره سم مؤمنانو ته د الله تعالی په لار کې د جهاد لپاره د سفر پر مهال حکم شوی:'),
        [('to keep much wealth', 'زیادہ مال رکھنے کا', 'د ډېر مال ساتلو'), ('to verify well', 'خوب تحقیق کرنے کا', 'د ښه تحقیق کولو'), ('to keep the best mounts', 'بہترین سواری رکھنے کا', 'د غوره سپرلۍ ساتلو'), ('to keep war equipment', 'جنگی سامان رکھنے کا', 'د جنګي سامان ساتلو')])
    MCQ(b, 7, 'مُسْتَضْعَفِينَ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('poor', 'مسکین', 'مسکین'), ('helpless', 'بے بس', 'بې‌وسه'), ('orphan', 'یتیم', 'یتیم'), ('oppressed', 'مظلوم', 'مظلوم')])
    b.p(*Q2)
    AR(b, f'(1) {words(4, 71)}', 'What command has been given to the believers at the time of war in the verse?', 'آیت کریمہ میں اہلِ ایمان کو جنگ کے وقت کیا حکم دیا گیا ہے؟', 'په آیت کې مؤمنانو ته د جګړې پر مهال څه حکم شوی؟')
    AR(b, f'(2) {words(4, 74, 12, 23)}', 'According to the verse, which people will Allah Almighty grant a great reward?', 'آیت کریمہ کے مطابق اللہ تعالیٰ کن لوگوں کو اجرِ عظیم عطا فرمائے گا؟', 'د آیت له مخې الله تعالی به کومو خلکو ته لوی اجر ورکړي؟')
    AR(b, f'(3) {words(4, 78, 1, 9)}', 'What reality has been told about death in the verse?', 'آیت کریمہ میں موت کے بارے میں کیا حقیقت بتائی گئی ہے؟', 'په آیت کې د مرګ په اړه کوم حقیقت ویل شوی؟')
    AR(b, f'(4) {words(4, 79, 1, 13)}', 'What causes of suffering and good reaching (a person) have been stated in the verse?', 'آیت کریمہ میں دکھ اور سکھ پہنچنے کے کیا اسباب بیان کیے گئے ہیں؟', 'په آیت کې د تکلیف او ښېګڼې د رسېدو کوم لاملونه بیان شوي؟')
    AR(b, f'(5) {words(4, 83, 24, 32)}', 'According to the verse, what would have been the result if the grace of Allah Almighty were not there?', 'آیت کریمہ کے مطابق اللہ تعالیٰ کا فضل نہ ہونے کی صورت میں کیا نتیجہ نکلتا؟', 'د آیت له مخې که د الله تعالی فضل نه وای، څه پایله به وه؟')
    AR(b, f'(6) {words(4, 87)}', 'What attributes of Allah Almighty have been stated in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کی کیا صفات بیان کی گئی ہیں؟', 'په آیت کې د الله تعالی کوم صفتونه بیان شوي؟')
    AR(b, f'(7) {words(4, 94, 1, 17)}', 'What advice has been given to the believers in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا نصیحت کی گئی ہے؟', 'په آیت کې مؤمنانو ته څه نصیحت شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(4, 72)}', *TR)
    AR(b, f'(1b) {words(4, 76)}', 'Which contrast between the believers and the disbelievers has been mentioned in the verse?', 'آیت کریمہ میں اہلِ ایمان اور کفار کے کس تقابل کا ذکر کیا ہے؟', 'په آیت کې د مؤمنانو او کافرانو ترمنځ کوم پرتله یاده شوې؟')
    AR(b, f'(2a) {words(4, 73)}', *TR)
    AR(b, f'(2b) {words(4, 84)}', 'What instruction has been given to the Messenger of Allah (peace and blessings of Allah be upon him) in the verse?', 'آیت کریمہ میں رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کو کیا تلقین فرمائی گئی ہے؟', 'په آیت کې رسول الله صلی الله علیه وعلی آله واصحابه وسلم ته څه لارښوونه شوې؟')
    AR(b, f'(3a) {words(4, 88)}', *TR)
    BOOK.save(36, [(3, rec(b, 3, 36, 36, kind='exercise'))], issues=[{'id': 'mq12-pdf036', 'unit': 3, 'printedPage': 33,
               'description': 'Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p36()
