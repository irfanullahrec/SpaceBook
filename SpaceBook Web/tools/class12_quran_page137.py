"""Mutalia-e-Quran XII PDF137: p.134 — Lesson 13 activities and teachers' guidance. Run: python class12_quran_page137.py"""
from class12_quran_common import BOOK, Builder, rec, L, ACT, TCH


def p137():
    b = Builder()
    b.h(*ACT)
    L(b, [('Hold a dialogue with your family or friends on how we can do the work of inviting to the religion in our home, school and neighbourhood. Write down everyone\'s useful suggestions and also make your classmates aware of them.', 'اپنے گھر والوں یا دوستوں سے ایک مکالمہ کریں کہ ہم اپنے گھر، اسکول اور محلے میں دین کی دعوت کا کام کس طریقہ سے کر سکتے ہیں۔ سب کے مفید مشوروں کو تحریر کریں اور اپنے ہم جماعت دوستوں کو بھی ان سے آگاہ کریں۔', 'له خپلې کورنۍ یا ملګرو سره خبرې اترې وکړئ چې موږ په خپل کور، ښوونځي او ګاونډ کې د دین د بلنې کار څنګه کولی شو. د ټولو ګټور مشورې ولیکئ او خپل ټولګیوال ملګري هم ترې خبر کړئ.'),
          ('In the light of Surah Ha Mim al-Sajdah, search for the things stated about the earth and comment on them.', 'سُوْرَةُ حٰمٓ السَّجْدَةِ کی روشنی میں زمین کے بارے میں بیان ہونے والی باتیں تلاش کریں اور ان پر تبصرہ کریں۔', 'د سورة حم السجده په رڼا کې د ځمکې په اړه بیان شوې خبرې ولټوئ او پرې تبصره وکړئ.')])
    b.h(*TCH)
    L(b, [('Hold a discussion among the students on how today the Muslims are being distanced from the Qur\'an-e-Hakim; further, encourage the students to strengthen their connection with the Qur\'an-e-Hakim.', 'طلبہ کے مابین مذاکرہ کرائیں کہ آج مسلمانوں کو کس طرح قرآنِ حکیم سے دور کیا جا رہا ہے نیز طلبہ کو قرآنِ حکیم سے اپنا تعلق مضبوط کرنے کی ترغیب دیں۔', 'د زده‌کوونکو ترمنځ بحث وکړئ چې نن مسلمانان څنګه له قرآن حکیم لرې کېږي؛ همدارنګه زده‌کوونکي وهڅوئ چې له قرآن حکیم سره خپله اړیکه ټینګه کړي.')])
    BOOK.save(137, [(13, rec(b, 13, 137, 137, kind='exercise'))], complete_units=[13], issues=[{'id': 'mq12-pdf137', 'unit': 13, 'printedPage': 134,
               'description': 'Lower two-thirds of p.134 blank.'}])


if __name__ == '__main__':
    p137()
