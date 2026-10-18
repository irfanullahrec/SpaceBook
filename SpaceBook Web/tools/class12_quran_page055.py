"""Mutalia-e-Quran XII PDF55: p.52 — Lesson 5 exercise Q2 item 7, Q3, activities, teachers' guidance. Run: python class12_quran_page055.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, Q3, TR, ACT, TCH, words


def p55():
    b = Builder()
    AR(b, f'(7) {words(4, 164, 12, 15)}', 'According to the verse, with what special honour was Sayyiduna Musa (peace be upon him) blessed?', 'آیت کریمہ کے مطابق سیدنا موسیٰ علیہ السلام کو کس خاص شرف سے نوازا گیا؟', 'د آیت له مخې سیدنا موسی علیه السلام ته کوم ځانګړی شرف ورکړل شو؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(4, 137)}', *TR)
    AR(b, f'(1b) {words(4, 141, 1, 24)}', 'According to the verse, what conduct of the hypocrites on occasions of victory and defeat has been stated?', 'آیت کریمہ کے مطابق فتح اور شکست کے مواقع پر منافقین کا کیا طرزِ عمل بیان کیا گیا ہے؟', 'د آیت له مخې د بریا او ماتې پر وختونو د منافقانو کوم چلند بیان شوی؟')
    AR(b, f'(2a) {words(4, 144)}', *TR)
    AR(b, f'(2b) {words(4, 146)}', 'In the verse, which people have been declared companions of the believers?', 'آیت کریمہ میں کن لوگوں کو اہلِ ایمان کا ساتھی قرار دیا گیا ہے؟', 'په آیت کې کوم خلک د مؤمنانو ملګري ګڼل شوي؟')
    AR(b, f'(3a) {words(4, 149)}', *TR)
    AR(b, f'(3b) {words(4, 170)}', 'What teaching has been given to people by addressing them in the verse?', 'آیت کریمہ میں لوگوں کو مخاطب کر کے کیا تعلیم دی گئی ہے؟', 'په آیت کې خلکو ته د خطاب له لارې څه لارښوونه شوې؟')
    b.h(*ACT)
    L(b, [('Write, in the form of a chart, the names and titles of the Ulu al-\'Azm prophets who are mentioned in this lesson.', 'اس سبق میں جن اُولو العزم پیغمبروں کا تذکرہ کیا گیا ہے چارٹ کی صورت میں ان کے نام اور القاب تحریر کریں۔', 'په دې لوست کې د کومو اولوالعزم پیغمبرانو یادونه شوې، د چارټ په بڼه یې نومونه او لقبونه ولیکئ.'),
          ('Learn the meaning and sense of ghuluww (excess) from your teachers.', 'غلو کا معنی و مفہوم اپنے اساتذہ کرام سے معلوم کریں۔', 'د غلو (له حده اوښتلو) مانا او مفهوم له خپلو ښوونکو زده کړئ.')])
    b.h(*TCH)
    L(b, [('Make clear to the students the importance of true testimony in the light of the Qur\'an-e-Hakeem and the blessed hadiths.', 'سچی گواہی کی اہمیت قرآن حکیم و احادیثِ مبارکہ کی روشنی میں طلبہ پر واضح کریں۔', 'د قرآن حکیم او مبارکو احادیثو په رڼا کې زده‌کوونکو ته د رښتینې شاهدۍ اهمیت روښانه کړئ.'),
          ('Present before the students an explanation of the Christians\' wrong inference of the Trinity from words like "Kalimat Allah" and "Ruh Allah", and its refutation.', 'عیسائیوں کے ”کلمۃ اللہ“ اور ”روح اللہ“ جیسے الفاظ سے عقیدۂ تثلیث پر غلط استدلال کی وضاحت اور اس کی تردید طلبہ کے سامنے پیش کریں۔', 'د «کلمة الله» او «روح الله» غوندې کلمو څخه د تثلیث پر عقیده د عیسویانو د غلط استدلال وضاحت او رد زده‌کوونکو ته وړاندې کړئ.'),
          ('Make the students aware of the definition of kalalah and the details of the inheritance shares connected with it.', 'کلالہ کی تعریف اور اس سے متعلق وراثتی حصوں کی تفصیلات سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي د کلالې له تعریف او ورپورې اړوندو میراثي برخو له تفصیلاتو خبر کړئ.')])
    BOOK.save(55, [(5, rec(b, 5, 55, 55, kind='exercise'))], complete_units=[5], issues=[{'id': 'mq12-pdf055', 'unit': 5, 'printedPage': 52,
               'description': 'Quoted verses drawn from the reference Uthmani text. Lower part of p.52 blank.'}])


if __name__ == '__main__':
    p55()
