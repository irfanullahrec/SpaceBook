"""Islamiat (Ikhtiari) XII PDF10: pp.10–11 — end of section A; exercise (Q1 long, Q2 fill-in-the-blanks); activities.
Run: python class12_iski_page010.py"""
from class12_iski_common import BOOK, Builder, rec, P, L


def p10():
    b = Builder()
    P(b, [('(continued from p.9) … when, after research, confirmed some Quranic reality, they entered the circle of Islam. The Quran al-Hakim is a permanent code of life for this reason too, that in it such treasures of knowledge and wisdom are hidden to which human research has not yet been able to obtain access. It is possible that in times to come academic research will bring the miraculous treasures of the Quran Pak in front of people.', '(ص 9 سے جاری) … جب تحقیق کر کے کسی قرآنی حقیقت کی تصدیق کی تو وہ دائرہ اسلام میں داخل ہو گئے۔ قرآنِ حکیم اس لیے بھی دائمی ضابطۂ حیات ہے کہ اس میں علم و حکمت کے ایسے ایسے خزانے پوشیدہ ہیں جن تک تاحال انسانی تحقیق کی رسائی حاصل نہیں ہو سکی۔ ممکن ہے آنے والے وقتوں میں علمی تحقیق قرآنِ پاک کے معجزانہ خزانوں کو لوگوں کے سامنے لے آئے۔', '(له ۹ مخ دوام) … کله یې چې په څېړنه کوم قرآني حقیقت تایید کړ، نو د اسلام دایرې ته ننوتل. قرآن حکیم ځکه هم د ژوند تلپاتې دستور دی چې په کې د علم او حکمت داسې خزانې پټې دي چې انساني څېړنه لا تر اوسه ورته نه ده رسېدلې. کېدای شي په راتلونکو وختونو کې علمي څېړنه د قرآن پاک معجزه‌یي خزانې د خلکو مخې ته راوړي.')])
    b.h('Exercise', 'مشق', 'تمرین')
    P(b, [('Question: Write detailed answers to the following questions.', 'سوال: درج ذیل سوالات کے تفصیلی جواب تحریر کریں۔', 'پوښتنه: د لاندې پوښتنو تفصیلي ځوابونه ولیکئ.')])
    L(b, [('i. Write a note on the eloquence and rhetoric of the Quran Majeed.', 'i۔ قرآن مجید کی فصاحت و بلاغت پر نوٹ لکھیں۔', 'i. د قرآن مجید پر فصاحت او بلاغت یادښت ولیکئ.'),
          ('ii. Discuss the world-wideness and universality of the Quran Majeed.', 'ii۔ قرآن مجید کی عالمگیریت اور ہمہ گیریت پر بحث کریں۔', 'ii. د قرآن مجید پر نړیوالتوب او هراړخیزتوب بحث وکړئ.'),
          ('iii. With regard to variety, what do you know about the Quran Majeed?', 'iii۔ تنوع کے لحاظ سے آپ قرآن مجید کے بارے میں کیا جانتے ہیں؟', 'iii. د تنوع له پلوه د قرآن مجید په اړه څه پوهېږئ؟'),
          ('iv. How can we prove that the Quran Majeed is a permanent code of life?', 'iv۔ ہم کیسے ثابت کر سکتے ہیں کہ قرآن مجید دائمی ضابطۂ حیات ہے؟', 'iv. موږ څنګه ثابتولی شو چې قرآن مجید د ژوند تلپاتې دستور دی؟')])
    P(b, [('Question 2: Fill in the blanks with suitable words. (style, al-Furqan, reader, Quran Majeed, treasures, ‘ajami, concepts)', 'سوال 2: مناسب الفاظ لگا کر خالی جگہ پر کریں۔ (اسلوب، الفرقان، قاری، قرآن مجید، خزانے، عجمی، تصورات)', '۲ پوښتنه: په مناسبو کلمو تشې ډکې کړئ. (اسلوب، الفرقان، لوستونکی، قرآن مجید، خزانې، عجمي، تصورات)')])
    L(b, [('i. The most printed book on the face of the earth is ________.', 'i۔ روئے زمین پر سب سے زیادہ چھپنے والی کتاب ________ ہے۔', 'i. د ځمکې پر مخ تر ټولو ډېر چاپ شوی کتاب ________ دی.'),
          ('ii. Because of being the book that distinguishes truth from falsehood, the Quran Pak is also called ________.', 'ii۔ حق و باطل میں فرق کرنے والی کتاب کی وجہ سے قرآن پاک کو ________ بھی کہا جاتا ہے۔', 'ii. د حق او باطل ترمنځ د توپیر کوونکي کتاب له امله قرآن پاک ته ________ هم ویل کېږي.'),
          ('iii. The Quran al-Hakim, by adopting the interrogative manner, has compelled the ________ to think.', 'iii۔ قرآنِ حکیم نے استفہامیہ انداز اختیار کر کے ________ کو سوچنے پر مجبور کر دیا ہے۔', 'iii. قرآن حکیم د پوښتنیز انداز په غوره کولو ________ فکر کولو ته اړ کړی.'),
          ('iv. Beginning a point by swearing an oath is a special ________ of the Quran Majeed.', 'iv۔ قسم کھا کر بات کا آغاز کرنا، قرآن مجید کا خاص ________ ہے۔', 'iv. په قسم سره د خبرې پیلول د قرآن مجید ځانګړی ________ دی.'),
          ('v. The Arabs used to call non-Arabs ________.', 'v۔ عرب لوگ غیر عرب کو ________ کہہ کر پکارتے تھے۔', 'v. عربانو غیرعربانو ته ________ ویل.'),
          ('vi. In the Quran Majeed ________ of knowledge and wisdom are hidden.', 'vi۔ قرآن مجید میں علم و حکمت کے ________ پوشیدہ ہیں۔', 'vi. په قرآن مجید کې د علم او حکمت ________ پټې دي.'),
          ('vii. The ________ of metaphysics exist in the Quran Majeed.', 'vii۔ مابعد الطبیعیات کے ________ قرآن مجید میں موجود ہیں۔', 'vii. د مابعدالطبیعه ________ په قرآن مجید کې شته.')])
    r1 = rec(b, 1, 10, 10, [10], kind='exercise')
    t = Builder()
    t.h('Activities', 'سرگرمیاں', 'فعالیتونه')
    L(t, [('i. What kind of example has the Quran al-Hakim given in Surah al-Baqarah about the one who devours interest?', 'i۔ قرآنِ حکیم نے سورۃ البقرہ میں سود خور کے بارے میں کیسی مثال دی ہے؟', 'i. قرآن حکیم په سورة البقره کې د سودخور په اړه څه ډول مثال ورکړی؟'),
          ('ii. Write the summary of the social teachings in Surah al-Hujurat in your own words.', 'ii۔ سورۃ الحجرات میں معاشرتی تعلیمات کا خلاصہ اپنے الفاظ میں لکھیں۔', 'ii. په سورة الحجرات کې د ټولنیزو لارښوونو لنډیز په خپلو ټکو ولیکئ.'),
          ('iii. Write any five injunctions from Surah an-Nur.', 'iii۔ سورہ نور میں سے کوئی سے پانچ احکام لکھیں۔', 'iii. له سورة النور څخه هر پنځه حکمونه ولیکئ.'),
          ('iv. Find some such verses in the thirtieth part in which Allah, the Lord of Honour, has sworn an oath.', 'iv۔ تیسویں پارے میں چند ایسی آیات تلاش کریں جس میں اللہ رب العزت نے قسم کھائی ہے۔', 'iv. په دېرشم پاره کې ځینې داسې آیتونه ولټوئ چې په کې الله رب العزت قسم یاد کړی.'),
          ('v. Study Surah an-Naml and tell what dialogue took place between Hazrat Sulaiman (peace be upon him) and the hoopoe.', 'v۔ سورۃ نمل کا مطالعہ کر کے بتائیں کہ حضرت سلیمان علیہ السلام اور ہُد ہُد میں کیا مکالمہ ہوا؟', 'v. د سورة النمل مطالعه وکړئ او ووایاست چې د حضرت سلیمان (ع) او هدهد ترمنځ څه خبرې وشوې؟')])
    BOOK.save(10, [(1, r1), (1, rec(t, 1, 11, 10, [11], kind='activities'))], issues=[{'id': 'iski12-pdf010', 'unit': 1, 'printedPage': 10,
               'description': 'Student handwriting (answers, page numbers, marks) on the exercise page excluded; blanks left empty. Rest of p.11 blank.'}])


if __name__ == '__main__':
    p10()
