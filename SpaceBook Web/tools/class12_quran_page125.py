"""Mutalia-e-Quran XII PDF125: p.122 — Lesson 12 exercise Q2 items 3–7, Q3. Run: python class12_quran_page125.py"""
from class12_quran_common import BOOK, Builder, rec, AR, Q3, TR, words


def p125():
    b = Builder()
    AR(b, f'(3) {words(33, 53, 55, 75)}', 'In the verse, from which two things concerning the Holy Prophet (peace and blessings of Allah be upon him) have the people of faith been forbidden?', 'آیت کریمہ میں اہلِ ایمان کو نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے متعلق کن دو باتوں سے منع کیا گیا ہے؟', 'په آیت کې مؤمنان د نبي کریم صلی الله علیه وعلی آله واصحابه وسلم په اړه له کومو دوو خبرو منع شوي؟')
    AR(b, f'(4) {words(33, 56)}', 'What command has been given in the verse to the people of faith concerning durud and salam?', 'آیت کریمہ میں اہلِ ایمان کو درود و سلام کے حوالے سے کیا حکم دیا گیا ہے؟', 'په آیت کې مؤمنانو ته د درود او سلام په اړه کوم حکم شوی؟')
    AR(b, f'(5) {words(33, 59, 1, 11)}', 'What commands have been given in the verse concerning purdah?', 'آیت کریمہ میں پردے کے حوالے سے کیا احکامات دیے گئے ہیں؟', 'په آیت کې د پردې په اړه کوم حکمونه ورکړل شوي؟')
    AR(b, f'(6) {words(33, 59, 13, 23)}', 'What wisdom of purdah has been stated in the verse?', 'آیت کریمہ میں پردے کی کیا حکمت بیان کی گئی ہے؟', 'په آیت کې د پردې کوم حکمت بیان شوی؟')
    AR(b, f'(7) {words(33, 63, 1, 10)}', 'What answer has been given in the verse to the question asked concerning the Resurrection?', 'آیت کریمہ میں قیامت کے حوالے سے پوچھے گئے سوال کا کیا جواب دیا گیا ہے؟', 'په آیت کې د قیامت په اړه شوې پوښتنې ته څه ځواب ورکړل شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(33, 36)}', *TR)
    AR(b, f'(1b) {words(33, 49)}', 'What commands concerning the waiting period (iddah) have been stated in the verse?', 'آیت کریمہ میں عدت کے کیا احکام بیان ہوئے ہیں؟', 'په آیت کې د عدت کوم حکمونه بیان شوي؟')
    AR(b, f'(2a) {words(33, 40)} {words(33, 41)}', 'Write the translation of the verses.', 'آیات کریمہ کا ترجمہ تحریر کریں۔', 'د آیتونو ژباړه ولیکئ.')
    AR(b, f'(2b) {words(33, 55)}', 'According to the verse, from which people have the Pure Wives (may Allah be pleased with them) been exempted from observing purdah?', 'آیت کریمہ کے مطابق ازواجِ مطہرات رضی اللہ تعالیٰ عنہن کو کن لوگوں سے پردہ کرنے سے رخصت دی گئی ہے؟', 'د آیت له مخې پاکو مېرمنو رضي الله عنهن ته له کومو خلکو د پردې کولو رخصت ورکړل شوی؟')
    AR(b, f'(3a) {words(33, 58)}', *TR)
    AR(b, f'(3b) {words(33, 53, 1, 26)}', 'What teachings have been given to the people of faith in the verse?', 'آیت کریمہ میں اہلِ ایمان کو کیا تعلیمات دی گئی ہیں؟', 'په آیت کې مؤمنانو ته کومې لارښوونې شوې؟')
    BOOK.save(125, [(12, rec(b, 12, 125, 125, kind='exercise'))], issues=[{'id': 'mq12-pdf125', 'unit': 12, 'printedPage': 122,
               'description': 'Q3 2a quotes 33:40 and the opening of 33:41 as printed ("…اذْكُرُوا اللَّهَ ذِكْرًا كَثِيرًا"); both verses given in full here. Quoted verses drawn from the reference Uthmani text. Lower part of p.122 blank.'}])


if __name__ == '__main__':
    p125()
