"""Mutalia-e-Quran XII PDF28: p.25 — Lesson 2 exercise Q3 (end), activities, teachers' guidance. Run: python class12_quran_page028.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, TR, ACT, TCH, words


def p28():
    b = Builder()
    AR(b, f'(2b) {words(4, 62)}', 'What cause of misfortune reaching the hypocrites is stated in the verse, and what reaction do they show to it?', 'آیت کریمہ میں منافقین کو مصیبت پہنچنے کا کیا سبب بیان ہوا ہے اور اس پر کس ردِ عمل کا اظہار کرتے ہیں؟', 'په آیت کې منافقانو ته د مصیبت د رسېدو کوم لامل بیان شوی او پر هغه کوم غبرګون ښیي؟')
    AR(b, f'(3a) {words(4, 66)}', *TR)
    AR(b, f'(3b) {words(4, 69)}', 'What has been told in the verse about the blessed servants of Allah Almighty, and who are they?', 'آیت کریمہ میں اللہ تعالیٰ کے انعام یافتہ بندوں کے بارے میں کیا بتایا گیا ہے اور وہ کون ہیں؟', 'په آیت کې د الله تعالی د انعام شویو بندګانو په اړه څه ویل شوي او هغوی څوک دي؟')
    b.h(*ACT)
    L(b, [('Learn the commands of tayammum and its method from your teachers.', 'تیمم کے احکامات اور اس کا طریقہ اپنے اساتذہ کرام سے معلوم کریں۔', 'د تیمم حکمونه او طریقه له خپلو ښوونکو زده کړئ.'),
          ('Collect information about the blessed servants of Allah Almighty stated in this lesson and discuss it.', 'اس سبق میں بیان کردہ اللہ تعالیٰ کے انعام یافتہ بندوں کے بارے میں معلومات جمع کر کے مذاکرہ کریں۔', 'په دې لوست کې د الله تعالی د بیان شویو انعام شویو بندګانو په اړه معلومات راټول کړئ او پرې بحث وکړئ.')])
    b.h(*TCH)
    L(b, [('Have the students prepare a list of the people with whom Allah Almighty has commanded kindness in this lesson, and discuss the various practical forms of kindness.', 'اس سبق میں اللہ تعالیٰ نے جن افراد کے ساتھ احسان کرنے کا حکم دیا ہے ان کی فہرست مرتب کرا کر احسان کی مختلف عملی صورتوں پر گفتگو کریں۔', 'په دې لوست کې الله تعالی له کومو کسانو سره د احسان حکم کړی، د هغوی لړلیک جوړ کړئ او د احسان پر بېلابېلو عملي بڼو خبرې وکړئ.'),
          ('Make the students well aware of the concept of taghut, and by pointing out its manifestations in the present age, encourage them to avoid it.', 'طلبہ کو طاغوت کے مفہوم سے اچھی طرح آگاہ کریں اور دورِ حاضر میں اس کے مظاہر کی نشان دہی کر کے اس سے بچنے کی ترغیب دیں۔', 'زده‌کوونکي د طاغوت له مفهوم ښه خبر کړئ او په اوسني عصر کې یې د بڼو په ښودلو ترې د ځان ساتلو هڅونه وکړئ.'),
          ('Acquaint the students with the broad concept of trust (wealth, position, secret, responsibility, knowledge, etc.) and make its importance clear from the Qur\'an and Hadith.', 'طلبہ کو امانت کے وسیع مفہوم (مال، منصب، راز، ذمہ داری، علم وغیرہ) سے روشناس کرائیں اور قرآن و حدیث سے اس کی اہمیت واضح کریں۔', 'زده‌کوونکي د امانت له پراخ مفهوم (مال، منصب، راز، مسؤلیت، علم او نور) سره بلد کړئ او له قرآن او حدیث یې اهمیت روښانه کړئ.')])
    BOOK.save(28, [(2, rec(b, 2, 28, 28, kind='exercise'))], complete_units=[2], issues=[{'id': 'mq12-pdf028', 'unit': 2, 'printedPage': 25,
               'description': 'Lower half of p.25 blank. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p28()
