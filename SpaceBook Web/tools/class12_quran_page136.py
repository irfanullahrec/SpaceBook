"""Mutalia-e-Quran XII PDF136: p.133 — Lesson 13 exercise Q1 items 6–7, Q2, Q3. Run: python class12_quran_page136.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p136():
    b = Builder()
    MCQ(b, 6, 'مَّحِيصٍ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('a place to live', 'رہنے کی جگہ', 'د اوسېدو ځای'), ('a place to hide', 'چھپنے کی جگہ', 'د پټېدو ځای'), ('a place to flee', 'بھاگنے کی جگہ', 'د تېښتې ځای'), ('a place of rest', 'آرام کی جگہ', 'د آرام ځای')])
    MCQ(b, 7, words(41, 49, 7, 11), ('— according to this, when any harm touches man he becomes:', 'کی رو سے جب انسان کو کوئی تکلیف پہنچتی ہے تو وہ ہو جاتا ہے:', '— له دې سره سم کله چې انسان ته کوم تکلیف ورسېږي، نو شي:'),
        [('hopeless and hasty', 'نااُمید اور جلد باز', 'ناهیلی او بېړنی'), ('displeased and sad', 'ناخوش اور غمگین', 'ناخوښ او خپه'), ('despairing and hopeless', 'مایوس اور ناامید', 'مایوس او ناهیلی'), ('sad and hopeless', 'غمگین اور ناامید', 'خپه او ناهیلی')])
    b.p(*Q2)
    AR(b, f'(1) {words(41, 5)}', 'What reaction of the disbelievers to the call of Tawhid is mentioned in the verse?', 'آیت کریمہ میں توحید کی دعوت پر کفار کے کس ردِ عمل کا ذکر ہے؟', 'په آیت کې د توحید پر بلنه د کافرانو د کوم غبرګون یادونه ده؟')
    AR(b, f'(2) {words(41, 13)}', 'In the verse, of what kind of punishment have those who turn away been warned?', 'آیت کریمہ میں اعراض کرنے والوں کو کس قسم کے عذاب کی تنبیہ کی گئی ہے؟', 'په آیت کې مخ اړوونکي د کوم ډول عذاب څخه خبردار شوي؟')
    AR(b, f'(3) {words(41, 16, 1, 13)}', 'According to the verse, what was the end of the people of \'Ad?', 'آیت کریمہ کی رو سے قوم عاد کا کیا انجام ہوا؟', 'د آیت له مخې د عاد قوم پایله څه شوه؟')
    AR(b, f'(4) {words(41, 22, 1, 11)}', 'According to the verse, which limbs will testify against man on the Day of Resurrection?', 'آیت کریمہ کی رو سے روزِ قیامت انسان کے خلاف کون سے اعضا گواہی دیں گے؟', 'د آیت له مخې د قیامت په ورځ د انسان پر خلاف کوم غړي شاهدي ورکوي؟')
    AR(b, f'(5) {words(41, 26)}', 'What behaviour of the disbelievers at the time of the recitation of the Qur\'an-e-Hakim has been stated in the verse?', 'آیت کریمہ میں تلاوتِ قرآنِ حکیم کے وقت کفار کی کیا روش بیان کی گئی ہے؟', 'په آیت کې د قرآن حکیم د تلاوت پر مهال د کافرانو کوم چلند بیان شوی؟')
    AR(b, f'(6) {words(41, 33)}', 'According to the verse, whose speech is the best of all?', 'آیت کریمہ کے مطابق سب سے بہتر بات کس کی ہے؟', 'د آیت له مخې تر ټولو غوره خبره د چا ده؟')
    AR(b, f'(7) {words(41, 51)}', 'According to the verse, what attitude of man in happiness and in sorrow has been stated?', 'آیت کریمہ کی رو سے خوشی اور غمی میں انسان کا کیا رویہ بیان ہوا ہے؟', 'د آیت له مخې په خوښۍ او غم کې د انسان کوم چلند بیان شوی؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(41, 30)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah Ha Mim al-Sajdah.', 'سُوْرَةُ حٰمٓ السَّجْدَةِ کا تعارف تحریر کریں۔', 'د سورة حم السجده پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(41, 39)}', *TR)
    AR(b, '(2b)', 'Mention some basic themes of Surah Ha Mim al-Sajdah.', 'سُوْرَةُ حٰمٓ السَّجْدَةِ کے چند بنیادی مضامین ذکر کریں۔', 'د سورة حم السجده ځینې بنسټیز مضامین یاد کړئ.')
    AR(b, f'(3a) {words(41, 46)}', *TR)
    AR(b, f'(3b) {words(41, 21, 1, 13)}', 'What dialogue of man with his skin has been stated in the verse?', 'آیت کریمہ میں انسان کا اپنی جلد سے کیا مکالمہ بیان ہوا ہے؟', 'په آیت کې د انسان له خپل پوستکي سره کومې خبرې اترې بیان شوې؟')
    BOOK.save(136, [(13, rec(b, 13, 136, 136, kind='exercise'))], issues=[{'id': 'mq12-pdf136', 'unit': 13, 'printedPage': 133,
               'description': 'Pink sticky-note marks pasted over the Q2/Q3 headings (reader additions) excluded; the "سوال ۲" / "سوال ۳" labels partly hidden under them. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p136()
