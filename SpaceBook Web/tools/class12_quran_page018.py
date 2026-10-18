"""Mutalia-e-Quran XII PDF18: p.15 — Lesson 1 exercise (Q2 items 6–7, Q3), activities for students, guidance for teachers. Run: python class12_quran_page018.py"""
from class12_quran_common import BOOK, Builder, rec, AR, words, L


def p18():
    b = Builder()
    AR(b, f'(6) {words(4, 12, 2, 11)}', 'Write the husband\'s share according to the verse.', 'آیت کریمہ کی رو سے شوہر کا حصہ تحریر کریں۔', 'د آیت له مخې د مېړه برخه ولیکئ.')
    AR(b, f'(7) {words(4, 14)}', 'For what kind of person is there a warning of humiliating punishment in the verse?', 'آیت کریمہ میں کیسے شخص کے لیے ذلت آمیز عذاب کی وعید ہے؟', 'په آیت کې څه ډول کس ته د سپکوونکي عذاب ګواښ دی؟')
    b.p('Question 3: Give detailed answers to the following questions:', 'سوال ۳: مندرجہ ذیل سوالات کے تفصیلی جوابات دیجیے:', '۳ پوښتنه: لاندې پوښتنو ته تفصیلي ځوابونه ورکړئ:')
    AR(b, f'(1a) {words(4, 5)}', 'Write the translation of the verse.', 'آیت کریمہ کا ترجمہ لکھیں۔', 'د آیت ژباړه ولیکئ.')
    b.p('(1b) Write the introduction of Surah al-Nisa\'.', '(۱ب) سُوْرَةُ النِّسَآءِ کا تعارف تحریر کریں۔', '(۱ب) د سورة النساء پېژندنه ولیکئ.')
    AR(b, f'(2a) {words(4, 9)}', 'Write the translation of the verse.', 'آیت کریمہ کا ترجمہ تحریر کریں۔', 'د آیت ژباړه ولیکئ.')
    b.p('(2b) Write some basic themes of Surah al-Nisa\'.', '(۲ب) سُوْرَةُ النِّسَآءِ کے چند بنیادی مضامین تحریر کریں۔', '(۲ب) د سورة النساء ځینې بنسټیز مضامین ولیکئ.')
    AR(b, f'(3a) {words(4, 13)}', 'Write the translation of the verse.', 'آیت کریمہ کا ترجمہ تحریر کریں۔', 'د آیت ژباړه ولیکئ.')
    AR(b, f'(3b) {words(4, 22)}', 'From which marriage has the verse forbidden, and how has it been condemned?', 'آیت کریمہ میں کس نکاح سے منع کیا گیا ہے اور اس کی کیا مذمت کی گئی ہے؟', 'په آیت کې له کومې نکاح منع شوې او څنګه یې غندنه شوې؟')
    b.h('Activities for students', 'سرگرمیاں برائے طلبہ', 'د زده‌کوونکو لپاره فعالیتونه')
    L(b, [('Make a list of the commands stated in this lesson concerning orphans and treat orphans kindly.', 'اس سبق میں یتیموں کے متعلق بیان کردہ احکامات کی فہرست بنائیں اور یتیموں کے ساتھ حسنِ سلوک کا معاملہ کریں۔', 'په دې لوست کې د یتیمانو اړوند بیان شوي حکمونه لړلیک کړئ او له یتیمانو سره ښه چلند وکړئ.'),
          ('Arrange in the form of a chart the names of the heirs whose shares are stated in the verses of inheritance, and their fixed shares.', 'آیاتِ میراث میں جن ورثاء کے حصے بیان ہوئے ہیں، ان کے نام اور متعین حصے چارٹ کی صورت میں مرتب کریں۔', 'د میراث په آیتونو کې د کومو وارثانو برخې بیان شوې، د هغوی نومونه او ټاکلې برخې د چارټ په بڼه ترتیب کړئ.'),
          ('Write in two columns the women with whom marriage is permitted in this lesson and those with whom marriage is prohibited.', 'اس سبق میں جن عورتوں سے نکاح کی اجازت ہے اور جن سے نکاح کی ممانعت ہے، انھیں دو کالموں کی صورت میں تحریر کریں۔', 'په دې لوست کې له کومو ښځو سره د نکاح اجازه ده او له کومو سره منع ده، په دوو ستونونو کې یې ولیکئ.')])
    b.h('Guidance for teachers', 'ہدایات برائے اساتذہ کرام', 'د ښوونکو لپاره لارښوونې')
    L(b, [('Make the students aware of the importance and comprehensiveness of the Islamic law of inheritance.', 'اسلامی قانونِ میراث کی اہمیت اور جامعیت سے طلبہ کو آگاہ کریں۔', 'زده‌کوونکي د اسلامي میراث د قانون له اهمیت او جامعیت خبر کړئ.'),
          ('Highlight the right of inheritance of women, orphans and the weak in the light of this lesson, and make students aware of the warnings that have been given for those who are careless in this regard.', 'خواتین، یتیموں اور کمزوروں کے حق میراث کو اس سبق کی روشنی میں اجاگر کریں اور اس حوالے سے لاپرواہی برتنے والوں کے لیے جو وعیدیں ہیں ان سے طلبہ کو آگاہ کریں۔', 'د دې لوست په رڼا کې د ښځو، یتیمانو او کمزورو د میراث حق روښانه کړئ، او په دې اړه د بې‌پروايي کوونکو لپاره چې کوم ګواښونه دي، زده‌کوونکي ترې خبر کړئ.'),
          ('Make the students aware of the importance and necessity of a will (wasiyyah) and encourage them to act on it.', 'وصیت کی اہمیت اور ضرورت سے طلبہ کو آگاہ کریں اور اس پر عمل کی ترغیب دیں۔', 'زده‌کوونکي د وصیت له اهمیت او اړتیا خبر کړئ او پرې د عمل هڅونه یې وکړئ.')])
    BOOK.save(18, [(1, rec(b, 1, 18, 18, kind='exercise'))], complete_units=[1], issues=[{'id': 'mq12-pdf018', 'unit': 1, 'printedPage': 15,
               'description': 'Exercise items quote verses in Arabic, drawn from the reference Uthmani text. No printed answer key.'}])


if __name__ == '__main__':
    p18()
