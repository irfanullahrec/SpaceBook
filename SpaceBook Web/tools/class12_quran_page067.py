"""Mutalia-e-Quran XII PDF67: p.64 — Lesson 6 exercise Q3 (end), activities, teachers' guidance. Run: python class12_quran_page067.py"""
from class12_quran_common import BOOK, Builder, rec, AR, L, TR, ACT, TCH, words


def p67():
    b = Builder()
    AR(b, f'(3a) {words(5, 27)}', *TR)
    AR(b, f'(3b) {words(5, 33, 1, 24)}', 'What punishment has been stated in the verse for those who spread corruption in the land?', 'آیت کریمہ میں زمین میں فساد کرنے والوں کی کیا سزا بیان ہوئی ہے؟', 'په آیت کې په ځمکه کې د فساد کوونکو کومه سزا بیان شوې؟')
    b.h(*ACT)
    L(b, [('Learn from your teachers the commands of lawful and unlawful in relation to food, and the details of the forbidden things mentioned in the lesson.', 'غذا کے حوالے سے حلال و حرام کے احکام نیز سبق میں مذکور حرام اشیاء کی تفصیلات اپنے اساتذہ کرام سے معلوم کریں۔', 'د خوړو په اړه د حلال و حرام حکمونه او په لوست کې د یادو شویو حرامو شیانو تفصیلات له خپلو ښوونکو زده کړئ.'),
          ('Learn the story of Habil and Qabil and discuss it.', 'قصہ ہابیل اور قابیل کا واقعہ معلوم کر کے مذاکرہ کریں۔', 'د هابیل او قابیل کیسه زده کړئ او پرې بحث وکړئ.'),
          ('In the light of verse 2 of Surah al-Ma\'idah, "وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَى وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ", discuss the practical forms of cooperating in deeds of goodness and piety and of avoiding sin and transgression.', 'سُوْرَةُ الْمَآئِدَةِ کی آیت نمبر ۲ کی روشنی میں ”وَتَعَاوَنُوْا عَلَى الْبِرِّ وَالتَّقْوٰى وَلَا تَعَاوَنُوْا عَلَى الْاِثْمِ وَالْعُدْوَانِ“ نیکی اور تقویٰ کے کاموں میں تعاون اور گناہ اور زیادتی سے اجتناب کی عملی صورتوں پر مباحثہ کریں۔', 'د سورة المائده د ۲ آیت «وَتَعَاوَنُوا عَلَى الْبِرِّ وَالتَّقْوَى وَلَا تَعَاوَنُوا عَلَى الْإِثْمِ وَالْعُدْوَانِ» په رڼا کې د نېکۍ او تقوا په کارونو کې د مرستې او له ګناه او تېري د ډډې پر عملي بڼو بحث وکړئ.')])
    b.h(*TCH)
    L(b, [('While making clear to the students the importance of purification, make them aware of the obligations of wudu and tayammum, and also tell them in which circumstances tayammum may be done; also have them practise the practical method of tayammum.', 'طلبہ کو طہارت کی اہمیت واضح کرتے ہوئے وضو اور تیمم کے فرائض سے آگاہ کریں اور انھیں یہ بھی بتائیں کہ کن حالات میں تیمم کیا جا سکتا ہے۔ نیز انھیں تیمم کے عملی طریقے کی مشق بھی کرائیں۔', 'زده‌کوونکو ته د پاکۍ اهمیت روښانه کړئ، د اودس او تیمم له فرضونو یې خبر کړئ، او ورته ووایئ چې په کومو حالاتو کې تیمم کېدای شي؛ همدارنګه د تیمم د عملي طریقې تمرین هم ورته وکړئ.'),
          ('In the light of the blessed hadiths make the students aware of the condemnation of envy, its harms and its various forms, and encourage them in the ways of avoiding it.', 'طلبہ کو احادیثِ مبارکہ کی روشنی میں حسد کی مذمت، اس کے نقصانات اور اس کی مختلف صورتوں سے آگاہ کریں اور اس سے بچنے کے طریقوں کی ترغیب دیں۔', 'زده‌کوونکي د مبارکو احادیثو په رڼا کې د حسد له غندنې، زیانونو او بېلابېلو بڼو خبر کړئ او ترې د ځان ساتلو پر لارو یې وهڅوئ.'),
          ('Make the students aware of the various forms of "fasad fi al-ard" (corruption in the land) in the present age and instruct them to avoid them.', 'طلبہ کو دورِ حاضر میں فساد فی الارض کی مختلف صورتوں سے آگاہ کریں اور ان سے بچنے کی تلقین کریں۔', 'زده‌کوونکي په اوسني عصر کې د «فساد في الارض» له بېلابېلو بڼو خبر کړئ او ترې د ځان ساتلو سپارښتنه وکړئ.'),
          ('In the light of the Qur\'an and Hadith make the students aware of the condemnation of killing and the severe warnings that come upon it, and encourage them to avoid this major sin.', 'قرآن و حدیث کی روشنی میں قتل کی مذمت اور اس پر آنے والی سخت وعیدوں سے طلبہ کو آگاہ کریں اور اس گناہ کبیرہ سے بچنے کی ترغیب دیں۔', 'د قرآن او حدیث په رڼا کې زده‌کوونکي د وژنې له غندنې او پرې د راغلو سختو ګواښونو خبر کړئ او له دې کبیره ګناه د ځان ساتلو هڅونه یې وکړئ.')])
    BOOK.save(67, [(6, rec(b, 6, 67, 67, kind='exercise'))], complete_units=[6], issues=[{'id': 'mq12-pdf067', 'unit': 6, 'printedPage': 64,
               'description': 'Lower part of p.64 blank; page number cut off at the scan edge. Quoted verses drawn from the reference Uthmani text.'}])


if __name__ == '__main__':
    p67()
