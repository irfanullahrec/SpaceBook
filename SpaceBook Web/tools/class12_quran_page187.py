"""Mutalia-e-Quran XII PDF187: p.184 — Lesson 19 exercise Q1 items 5–7, Q2, Q3 (1–2). Run: python class12_quran_page187.py"""
from class12_quran_common import BOOK, Builder, rec, MCQ, AR, Q2, Q3, TR, words


def p187():
    b = Builder()
    MCQ(b, 5, words(58, 9, 12, 14), ('— according to this the believers have been instructed to hold secret counsel:', 'کی رو سے مومنین کو سرگوشی کرنے کی تلقین ہے:', '— له دې سره سم مؤمنانو ته د پټې مشورې لارښوونه ده:'),
        [('for invitation and preaching', 'دعوت و تبلیغ کے لیے', 'د دعوت او تبلیغ لپاره'), ('for goodness and piety', 'نیکی و پرہیزگاری کے لیے', 'د نېکۍ او پرهېزګارۍ لپاره'), ('for justice and equity', 'عدل و انصاف کے لیے', 'د عدل او انصاف لپاره'), ('for buying and selling', 'خرید و فروخت کے لیے', 'د پېر و پلور لپاره')])
    MCQ(b, 6, words(58, 11, 19, 32), ('— according to this Allah Almighty raises the ranks of:', 'کی رو سے اللہ تعالیٰ درجات بلند کرتا ہے:', '— له دې سره سم الله تعالی د چا درجې لوړوي:'),
        [('the people of faith and the God-fearing', 'اہلِ ایمان اور متقین کے', 'د مؤمنانو او متقیانو'), ('the God-fearing and the righteous', 'متقین اور صالحین کے', 'د متقیانو او صالحانو'), ('the people of knowledge and action', 'اہلِ علم و عمل کے', 'د علم او عمل والو'), ('the people of faith and the people of knowledge', 'اہلِ ایمان اور اہلِ علم کے', 'د مؤمنانو او علم والو')])
    MCQ(b, 7, 'جُنَّةً', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('armour', 'زرہ', 'زغره'), ('spear', 'نیزہ', 'نېزه'), ('sword', 'تلوار', 'توره'), ('shield', 'ڈھال', 'ډال')])
    b.p(*Q2)
    AR(b, f'(1) {words(58, 2, 10, 26)}', 'Of what reality have those who pronounce zihar been made aware in the verse?', 'آیت کریمہ میں ظہار کرنے والوں کو کس حقیقت سے آگاہ کیا گیا ہے؟', 'په آیت کې ظهار کوونکي له کوم حقیقت خبر شوي؟')
    AR(b, f'(2) {words(58, 4, 1, 17)}', 'What expiation of zihar has been stated in the verse in case of not being able to free a slave?', 'آیت کریمہ میں غلام آزاد کرنے کی استطاعت نہ ہونے کی صورت میں ظہار کا کیا کفارہ بیان ہوا ہے؟', 'په آیت کې د غلام د آزادولو د وس نه لرلو په صورت کې د ظهار کومه کفاره بیان شوې؟')
    AR(b, f'(3) {words(58, 5)}', 'What end has been stated in the verse for those who oppose Allah Almighty and His Messenger (peace and blessings of Allah be upon him)?', 'آیت کریمہ میں اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی مخالفت کرنے والوں کا کیا انجام بیان کیا گیا ہے؟', 'په آیت کې د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د مخالفانو کومه پایله بیان شوې؟')
    AR(b, f'(4) {words(58, 10)}', 'What purposes of evil secret counsel have been stated in the verse?', 'آیت کریمہ میں بُری سرگوشی کے کیا مقاصد بیان ہوئے ہیں؟', 'په آیت کې د بدې پټې مشورې کومې موخې بیان شوې؟')
    AR(b, f'(5) {words(58, 16)}', 'What conduct and end of the hypocrites has been stated in the verse?', 'آیت کریمہ میں منافقین کا کیا طرزِ عمل اور انجام بیان ہوا ہے؟', 'په آیت کې د منافقانو کوم چلند او پایله بیان شوې؟')
    AR(b, f'(6) {words(58, 18)}', 'According to the verse, what will be the condition on the Day of Resurrection of the people over whom Satan has gained mastery?', 'آیت کریمہ کے مطابق شیطان نے جن لوگوں پر غلبہ پایا ہے قیامت میں ان کی کیا کیفیت ہوگی؟', 'د آیت له مخې هغه خلک چې شیطان پرې غلبه موندلې، د قیامت په ورځ به یې څه حال وي؟')
    AR(b, f'(7) {words(58, 21)}', 'According to the verse, for whom is real supremacy?', 'آیت کریمہ کے مطابق حقیقی غلبہ کس کے لیے ہے؟', 'د آیت له مخې حقیقي غلبه د چا لپاره ده؟')
    b.p(*Q3)
    AR(b, f'(1a) {words(58, 6)}', *TR)
    AR(b, '(1b)', 'Write an introduction to Surah al-Mujadilah.', 'سُوْرَةُ الْمُجَادَلَةِ کا تعارف تحریر کریں۔', 'د سورة المجادله پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(58, 12)}', *TR)
    AR(b, '(2b)', 'Write some basic themes of Surah al-Mujadilah.', 'سُوْرَةُ الْمُجَادَلَةِ کے چند بنیادی مضامین تحریر کریں۔', 'د سورة المجادله ځینې بنسټیز مضامین ولیکئ.')
    BOOK.save(187, [(19, rec(b, 19, 187, 187, kind='exercise'))], issues=[{'id': 'mq12-pdf187', 'unit': 19, 'printedPage': 184,
               'description': 'Q2 4 quotes 58:10 in full as printed. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p187()
