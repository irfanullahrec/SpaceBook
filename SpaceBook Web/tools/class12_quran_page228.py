"""Mutalia-e-Quran XII PDF228: p.225 — Lesson 24 exercise Q1, Q2 items 1–5. Run: python class12_quran_page228.py"""
from class12_quran_common import BOOK, Builder, rec, EX, MCQ, AR, Q1, Q2, words


def p228():
    b = Builder()
    EX(b)
    b.p(*Q1)
    MCQ(b, 1, words(65, 2, 13, 15), ('— in this verse the command is to establish:', 'آیت کریمہ میں قائم کرنے کا حکم ہے:', '— په دې آیت کې د قائمولو حکم دی:'),
        [('prayer', 'نماز', 'لمونځ'), ('testimony', 'گواہی', 'شاهدي'), ('religion', 'دین', 'دین'), ('peace', 'امن', 'امن')])
    MCQ(b, 2, words(65, 4, 16, 21), ('— according to this verse, the waiting period of a pregnant woman is:', 'آیت کریمہ کی رو سے حاملہ عورت کی عدت ہے:', '— د دې آیت له مخې د امیندوارې ښځې عدت دی:'),
        [('until delivery', 'وضعِ حمل', 'تر وضع حمل'), ('three months', 'تین مہینے', 'درې میاشتې'), ('three menstrual periods', 'تین حیض', 'درې حیضونه'), ('four months and ten days', 'چار ماہ دس دن', 'څلور میاشتې لس ورځې')])
    MCQ(b, 3, words(65, 6, 1, 6), ('— according to this, during the waiting period the command is to provide the woman with:', 'کی رو سے دورانِ عدت عورت کو مہیا کرنے کا حکم ہے:', '— له دې سره سم د عدت پر مهال ښځې ته د برابرولو حکم دی:'),
        [('food', 'کھانا', 'خواړه'), ('clothing', 'لباس', 'جامې'), ('residence', 'رہائش', 'استوګنه'), ('financial help', 'مالی مدد', 'مالي مرسته')])
    MCQ(b, 4, words(65, 6, 28, 30), ('— in this verse the command has been given:', 'آیت کریمہ میں حکم دیا گیا:', '— په دې آیت کې حکم شوی:'),
        [('to consult', 'مشورہ کرنے کا', 'د مشورې'), ('to make peace', 'صلح کرنے کا', 'د سولې'), ('to separate', 'جدا کرنے کا', 'د جلا کولو'), ('to take back', 'رجوع کرنے کا', 'د رجوع')])
    MCQ(b, 5, 'نَبَّأَتْ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('she announced', 'اعلان کیا', 'اعلان یې وکړ'), ('she informed', 'خبر دی', 'خبر یې ورکړ'), ('she whispered', 'سرگوشی کی', 'پسپسې یې وکړې'), ('she helped', 'مدد کی', 'مرسته یې وکړه')])
    MCQ(b, 6, 'سَٰٓئِحَٰتٍ', ('— means:', 'کے معنی ہیں:', '— مانا یې ده:'),
        [('worshippers', 'عبادت گزار', 'عبادت کوونکې'), ('obedient', 'اطاعت گزار', 'اطاعت کوونکې'), ('submissive', 'فرماں بردار', 'فرمانبردارې'), ('fasting', 'روزے دار', 'روژه نیوونکې')])
    MCQ(b, 7, words(66, 9, 6, 7), ('— according to this, concerning the disbelievers and the hypocrites the command was given:', 'کی رو سے کفار اور منافقین کے بارے میں حکم دیا گیا:', '— له دې سره سم د کافرانو او منافقانو په اړه حکم وشو:'),
        [('be stern', 'سختی کیجیے', 'سختي وکړئ'), ('warn them', 'خبردار کیجیے', 'خبردار یې کړئ'), ('imprison them', 'قید کیجیے', 'بندي یې کړئ'), ('exile them', 'جلاوطن کیجیے', 'جلاوطنه یې کړئ')])
    MCQ(b, 8, words(66, 12, 15, 17), ('— in this verse the attribute of Sayyidah Maryam (peace be upon her) stated is:', 'آیت کریمہ میں سیدہ مریم علیہا السلام کی صفت بیان ہوئی ہے:', '— په دې آیت کې د سیدې مریم علیها السلام کوم صفت بیان شوی:'),
        [('fasting', 'روزہ دار', 'روژه نیوونکې'), ('obedient', 'اطاعت گزار', 'اطاعت کوونکې'), ('grateful', 'شکر گزار', 'شکر کوونکې'), ('worshipping', 'عبادت گزار', 'عبادت کوونکې')])
    b.p(*Q2)
    AR(b, f'(1) {words(65, 1, 1, 9)}', 'What advice has been given in the verse to husbands concerning divorce?', 'آیت کریمہ میں طلاق کے حوالے سے شوہروں کو کیا نصیحت کی گئی ہے؟', 'په آیت کې د طلاق په اړه مېړونو ته څه نصیحت شوی؟')
    AR(b, f'(2) {words(65, 2, 1, 12)}', 'What advice has been given in the verse to husbands concerning women reaching the end of the waiting period?', 'آیت کریمہ میں شوہروں کو عدت کی میعاد کو پہنچنے والی عورتوں کے حوالے سے کیا نصیحت کی گئی ہے؟', 'په آیت کې مېړونو ته د هغو ښځو په اړه چې د عدت مودې ته رسېږي څه نصیحت شوی؟')
    AR(b, f'{words(65, 2, 27, 32)} (3) {words(65, 3, 1, 5)}', 'What benefits of piety are mentioned in the verses?', 'آیاتِ کریمہ میں تقویٰ کے کیا فوائد ذکر ہوئے ہیں؟', 'په آیتونو کې د تقوا کومې ګټې یادې شوې؟')
    AR(b, f'(4) {words(65, 6, 7, 10)}', 'What has been commanded in the verse concerning divorced women?', 'آیت کریمہ میں مطلقہ عورتوں کے حوالے سے کس بات کا حکم دیا ہے؟', 'په آیت کې د طلاقې شوو ښځو په اړه د کومې خبرې حکم شوی؟')
    AR(b, f'(5) {words(65, 6, 22, 30)}', 'What has the husband been commanded in the verse concerning the divorced woman upon the birth of a child?', 'آیت کریمہ میں شوہر کو بچے کی پیدائش پر مطلقہ کے حوالے سے کیا حکم دیا ہے؟', 'په آیت کې مېړه ته د ماشوم د زېږون پر مهال د طلاقې ښځې په اړه کوم حکم شوی؟')
    BOOK.save(228, [(24, rec(b, 24, 228, 228, kind='exercise'))], issues=[{'id': 'mq12-pdf228', 'unit': 24, 'printedPage': 225,
               'description': 'Q2 item 3 quotes the end of 65:2 and the start of 65:3 as printed. Q1 Arabic quotations printed in faint blue; matched to the verses. Quoted verses drawn from the reference Uthmani text. No printed key.'}])


if __name__ == '__main__':
    p228()
