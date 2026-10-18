"""Islamiat (Ikhtiari) XII PDF53: p.96 — exercise Q3 + activities (end of ch.1); p.97 — Chapter 2 Hadith opening. Run: python class12_iski_page053.py"""
from class12_iski_common import BOOK, Builder, rec, P, L

A = [('Articles of faith', 'ایمانیات', 'ایمانیات'), ('Acts of worship', 'عبادات', 'عبادات'), ('Dealings', 'معاملات', 'معاملات'), ('Interest', 'سود', 'سود'),
     ('Debtor', 'قرض دار', 'پوروړی'), ('Forgetting and error', 'بھول چوک', 'هېره او تېروتنه'), ('Trial', 'آزمائش', 'ازموینه')]
B = [('Respite until ease', 'کشائش تک مہلت', 'تر پراخۍ پورې مهلت'), ('Social evil', 'معاشرتی برائی', 'ټولنیزه بدي'), ('Faith in Allah, the Messenger, the angels', 'اللہ، رسول، فرشتوں پر ایمان', 'پر الله، رسول او پرښتو ایمان'),
     ('Prayer, fasting, zakat, Hajj', 'نماز، روزہ، زکوٰۃ، حج', 'لمونځ، روژه، زکات، حج'), ('Buying and selling', 'خرید و فروخت کرنا', 'پېر و پلور'), ('According to strength', 'طاقت کے مطابق', 'د توان سره سم'), ('Forgiveness', 'مغفرت', 'بښنه')]


def p53():
    b = Builder()
    b.p('Question 3: Match the columns according to meaning.', 'سوال 3: مفہوم کے اعتبار سے کالم ملائیں۔', 'پوښتنه ۳: د مفهوم له مخې ستونونه سره سمون کړئ.')
    b.table('iski12-match-2', ['Column A', 'Column B'], [[a[0], x[0]] for a, x in zip(A, B)], ['کالم الف', 'کالم ب'], ['الف ستون', 'ب ستون'],
            [[a[1], x[1]] for a, x in zip(A, B)], [[a[2], x[2]] for a, x in zip(A, B)])
    b.h('Activities', 'سرگرمیاں', 'فعالیتونه')
    L(b, [('i. What supplication do you make after the daily prayers?', 'i۔ آپ روزمرہ نمازوں کے بعد کیسے دعا مانگتے ہیں؟', 'i. تاسو د ورځنیو لمونځونو وروسته څنګه دعا کوئ؟'),
          ('ii. Which of your supplications have been accepted?', 'ii۔ آپ کی کون کون سی دعائیں قبول ہوئی ہیں؟', 'ii. ستاسو کومې دعاوې قبولې شوې دي؟'),
          ('iii. Like verse no. 286, write some other supplication from the Holy Quran, memorise it and recite it to your teacher.', 'iii۔ آیت نمبر 286 کی طرح قرآنِ مجید سے کوئی اور دعا لکھیں، یاد کریں اور اپنے معلم کو سنائیں۔', 'iii. د ۲۸۶ آیت په څېر له قرآن مجید څخه بله کومه دعا ولیکئ، یاده یې کړئ او خپل ښوونکي ته یې واورئ.')])
    r1 = rec(b, 1, 96, 53, [96], kind='exercise')
    t = Builder()
    t.h('Chapter Two: Hadith', 'بابِ دوم: حدیث', 'دویم څپرکی: حدیث')
    t.h('Teaching objectives', 'تدریسی مقاصد', 'تدریسي موخې')
    P(t, [('The purpose of this lesson is to enable the students that they:', 'اس سبق کا مقصد طلبہ اور طالبات کو اس قابل بنانا ہے کہ وہ:', 'د دې لوست موخه دا ده چې زده‌کوونکي دې ته وړ کړي چې:'),
          ('can study the text of the Hadith of the Messenger ﷺ and become acquainted with its comprehensiveness and eloquence.', 'حدیثِ رسول صلی اللہ علیہ وآلہٖ وسلم کے متن کا مطالعہ کر سکیں ان کی جامعیت اور بلاغت سے واقف ہو سکیں۔', 'د رسول ﷺ د حدیث متن مطالعه کړای شي او د هغه له جامعیت او بلاغت سره بلد شي.')])
    t.h('Literal meaning of Hadith', 'حدیث کا لغوی مفہوم', 'د حدیث لغوي مفهوم')
    P(t, [('The literal meaning of hadith is talk, conversation. If the word hadith is called the noun of "tahdith", then its meaning is to give news. One meaning of hadith is also "new", that is, the opposite of old. In short, in however many meanings it has, the sense of news is certainly present in them. In the Holy Quran the Quran too has been called "Ahsan al-Hadith" (the best discourse).', 'حدیث کا لغوی معنی ہے بات، گفتگو۔ اگر حدیث کے لفظ کو ”تحدیث“ کا اسم کہا جائے تو اس کا معنی ہے خبر دینا۔ حدیث کا ایک معنی جدید بھی ہے یعنی قدیم کا الٹ۔ غرض اس کے جتنے بھی معنی ہیں ان میں خبر کا مفہوم ضرور موجود ہے۔ قرآن مجید میں قرآن کو بھی ”احسن الحدیث“ کہا گیا ہے۔', 'د حدیث لغوي مانا ده خبره، خبرې‌اترې. که د حدیث کلمه د «تحدیث» اسم وبلل شي، نو مانا یې خبر ورکول دي. د حدیث یوه مانا «نوی» هم ده، یعنې د زاړه پر ضد. لنډه دا چې څومره ماناوې یې دي، په ټولو کې د خبر مفهوم خامخا شته. په قرآن مجید کې قرآن ته هم «احسن الحدیث» ویل شوي.')])
    t.h('Technical meaning of Hadith', 'حدیث کا اصطلاحی مفہوم', 'د حدیث اصطلاحي مفهوم')
    t.p('In terminology, hadith is that saying, deed, tacit approval (taqrir) or attribute which has been ascribed to the Messenger of Allah ﷺ.', 'اصطلاح میں حدیث وہ قول، فعل، تقریر و صفت ہے جس کی نسبت رسول اللہ صلی اللہ علیہ وآلہٖ وسلم کی طرف کی گئی ہو۔', 'په اصطلاح کې حدیث هغه قول، فعل، تقریر او صفت دی چې د الله رسول ﷺ ته منسوب شوی وي.')
    t.h('Hadith as a source of injunctions', 'حدیث بطور ماخذِ احکام', 'حدیث د احکامو د سرچینې په توګه')
    t.p('The Holy Quran is the first source of Islamic injunctions, and after the Quran the second source is the Prophetic ahadith. Allah the Exalted has sent down two kinds of revelation.', 'قرآن مجید اسلامی احکام کا پہلا ماخذ ہے اور قرآن کے بعد دوسرا ماخذ احادیثِ نبوی ہیں۔ اللہ تعالیٰ نے دو طرح کی وحی نازل فرمائی ہے۔', 'قرآن مجید د اسلامي احکامو لومړۍ سرچینه ده، او له قرآن وروسته دویمه سرچینه نبوي احادیث دي. الله تعالی دوه ډوله وحي نازله کړې ده.')
    L(t, [('1. Wahy matlu (recited revelation)', '۱۔ وحی متلو', '۱. وحي متلو (تلاوت کېدونکې وحي)'),
          ('2. Wahy ghayr matlu (unrecited revelation)', '۲۔ وحی غیر متلو', '۲. وحي غیر متلو (نه تلاوت کېدونکې وحي)')])
    BOOK.save(53, [(1, r1), (2, rec(t, 2, 97, 53, [97], first=True))], complete_units=[1], issues=[{'id': 'iski12-pdf053', 'unit': 1, 'printedPage': 96,
               'description': 'p.96 matching table: column B printed in jumbled order (exercise) — kept as printed; student lines and numbers drawing the matches excluded; no printed key. End of Chapter 1. p.97 opens Chapter 2 (Hadith); faded colour patch on the scan, text legible.'}])


if __name__ == '__main__':
    p53()
