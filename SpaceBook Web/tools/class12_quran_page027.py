"""Mutalia-e-Quran XII PDF27: p.24 — Lesson 2 exercise Q1 items 5–7, Q2, Q3 (start). Run: python class12_quran_page027.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p27():
    b = Builder()
    MCQ(b, 5, words(4, 52, 6, 12), ('— according to it, for the one whom Allah Almighty curses there will be no:', 'کی رو سے جس پر اللہ تعالیٰ لعنت کرے اس کے لیے کوئی نہ ہو گا:', '— له دې سره سم چا ته چې الله تعالی لعنت وکړي، هېڅ به ورته نه وي:'),
        [('one who gives refuge', 'پناہ دینے والا', 'پناه ورکوونکی'), ('one who shows mercy', 'رحم کرنے والا', 'رحم کوونکی'), ('one who gives security', 'امن دینے والا', 'امن ورکوونکی'), ('helper', 'مدد کرنے والا', 'مرستندوی')])
    MCQ(b, 6, 'يَعِظُكُم', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('He gives you honour', 'وہ تمھیں عزت دیتا ہے', 'تاسو ته عزت درکوي'), ('He advises you', 'وہ تمھیں نصیحت کرتا ہے', 'تاسو ته نصیحت کوي'), ('He gives you greatness', 'وہ تمھیں عظمت دیتا ہے', 'تاسو ته عظمت درکوي'), ('He gives you guidance', 'وہ تمھیں ہدایت دیتا ہے', 'تاسو ته هدایت درکوي')])
    MCQ(b, 7, words(4, 62, 8, 11), ('— in this verse the conduct of the hypocrites is stated: they', 'آیت کریمہ میں منافقین کی روش بیان ہوئی:', '— په دې آیت کې د منافقانو چلند بیان شوی: هغوی'),
        [('oppose', 'مخالفت کرتے ہیں', 'مخالفت کوي'), ('deceive', 'دھوکہ دیتے ہیں', 'دوکه کوي'), ('are lazy', 'سستی کرتے ہیں', 'سستي کوي'), ('swear oaths', 'قسمیں اٹھاتے ہیں', 'قسمونه خوري')])
    b.p(*Q2)
    AR(b, f'(1) {words(4, 34, 16, 22)}', 'Write the qualities of righteous wives in the light of the verse.', 'آیت کریمہ کی روشنی میں نیک بیویوں کی صفات تحریر کریں۔', 'د آیت په رڼا کې د نېکو مېرمنو صفتونه ولیکئ.')
    AR(b, f'(2) {words(4, 36, 2, 26)}', 'In the verse, what things has Allah Almighty commanded?', 'آیت کریمہ میں اللہ تعالیٰ نے کن باتوں کا حکم دیا ہے؟', 'په آیت کې الله تعالی د کومو خبرو حکم کړی؟')
    AR(b, f'(3) {words(4, 40)}', 'Which favours of Allah Almighty are mentioned in the verse?', 'آیت کریمہ میں اللہ تعالیٰ کے کن احسانات کا ذکر ہے؟', 'په آیت کې د الله تعالی د کومو احسانونو یادونه ده؟')
    AR(b, f'(4) {words(4, 42)}', 'According to the verse, what will the disbelievers and those who disobeyed the Messenger of Allah (peace and blessings of Allah be upon him) wish on the Day of Resurrection?', 'آیت کریمہ کے مطابق کفار اور رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی نافرمانی کرنے والے قیامت کے دن کیا آرزو کریں گے؟', 'د آیت له مخې کافران او د رسول الله صلی الله علیه وعلی آله واصحابه وسلم نافرمانان به د قیامت په ورځ څه ارمان وکړي؟')
    AR(b, f'(5) {words(4, 56)}', 'How, in the verse, will those who deny the verses of Allah Almighty be made to taste continuous punishment?', 'آیت کریمہ میں اللہ تعالیٰ کی آیات کو جھٹلانے والوں کو مسلسل عذاب کا مزہ کیسے چکھایا جائے گا؟', 'په آیت کې د الله تعالی د آیتونو درواغ‌ګڼونکو ته به څنګه د پرله‌پسې عذاب خوند ورڅکول کېږي؟')
    AR(b, f'(6) {words(4, 61)}', 'What conduct of the hypocrites is stated in the verse?', 'آیت کریمہ میں منافقین کا کیا طرزِ عمل بیان ہوا ہے؟', 'په آیت کې د منافقانو کوم چلند بیان شوی؟')
    AR(b, f'(7) {words(4, 65)}', 'What teaching has been given in the verse concerning obedience to the Messenger (peace and blessings of Allah be upon him)?', 'آیت کریمہ میں اطاعتِ رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے حوالے سے کیا تعلیم دی گئی ہے؟', 'په آیت کې د رسول صلی الله علیه وعلی آله واصحابه وسلم د اطاعت په اړه څه لارښوونه شوې؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(4, 26)}', *TR)
    AR(b, f'(1b) {words(4, 31)}', 'What reward has been stated in the verse for avoiding major sins?', 'آیت کریمہ میں بڑے گناہوں سے بچنے پر کیا انعام بیان کیا گیا ہے؟', 'په آیت کې له لویو ګناهونو د ځان ساتلو کوم انعام بیان شوی؟')
    AR(b, f'(2a) {words(4, 33)}', *TR)
    BOOK.save(27, [(2, rec(b, 2, 27, 27, kind='exercise'))], issues=[{'id': 'mq12-pdf027', 'unit': 2, 'printedPage': 24,
               'description': 'Quoted verses drawn from the reference Uthmani text; the printed quotation in Q2(2) stops at "وَمَا مَلَكَتْ أَيْمَانُكُمْ" (end of the verse). No printed key.'}])


if __name__ == '__main__':
    p27()
