"""Mutalia-e-Quran XII PDF181: p.178 — Lesson 19 Surah al-Mujadilah (1–22): naming and introduction, central theme, basic themes; surah heading; verses 58:1–2 (58:2 ends on p.179; recorded here). Run: python class12_quran_page181.py"""
from class12_quran_common import BOOK, Builder, rec, S, L, V

D = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
THEMES = [
    ('Shari\'ah commands concerning zihar and its solution', 'ظہار سے متعلق شرعی احکام اور اس کا حل', 'د ظهار په اړه شرعي حکمونه او د هغه حل'),
    ('Warning of severe punishment to those who oppose the commands of Allah Almighty and His Messenger (peace and blessings of Allah be upon him)', 'اللہ تعالیٰ اور اس کے رسول صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے احکام کی مخالفت کرنے والوں کو سخت سزا کی وعید', 'د الله تعالی او د هغه د رسول صلی الله علیه وعلی آله واصحابه وسلم د حکمونو مخالفانو ته د سختې سزا ګواښ'),
    ('Commands about secret counsels', 'سرگوشی کے بارے میں احکام', 'د پټو مشورو په اړه حکمونه'),
    ('Condemnation of the mischief of the hypocrites and their insult to the Messenger of Allah (peace and blessings of Allah be upon him)', 'منافقین کی شرارتوں اور رسول اللہ صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی توہین پر ان کی مذمت', 'د منافقانو د شرارتونو او د رسول الله صلی الله علیه وعلی آله واصحابه وسلم د سپکاوي له امله د هغوی غندنه'),
    ('Etiquette of gatherings', 'مجلس کے آداب', 'د مجلس آداب'),
    ('The excellence of the people of knowledge', 'اہلِ علم کی فضیلت', 'د علم والو فضیلت'),
    ('Reproach of the hypocrites for opposing Allah Almighty and the Holy Prophet (peace and blessings of Allah be upon him) and for secret counsels', 'اللہ تعالیٰ اور نبی کریم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کی مخالفت اور سرگوشیوں پر منافقین کی گرفت', 'د الله تعالی او نبي کریم صلی الله علیه وعلی آله واصحابه وسلم د مخالفت او پټو مشورو له امله پر منافقانو نیونه'),
    ('Mention of the party of Satan', 'شیطان کے گروہ کا تذکرہ', 'د شیطان د ډلې یادونه'),
    ('Announcement of the supremacy of the religion of Islam', 'دینِ اسلام کے غلبے کا اعلان', 'د اسلام د دین د غلبې اعلان'),
    ('The required qualities of the party of Allah', 'حزب اللہ کے مطلوبہ اوصاف', 'د حزب الله غوښتل شوي صفتونه'),
]


def p181():
    b = Builder()
    b.h('Lesson 19 — Surah al-Mujadilah (verses 1 to 22)', 'سبق ۱۹ — سُوْرَةُ الْمُجَادَلَةِ (آیات: ۱ تا ۲۲)', '۱۹ لوست — سورة المجادله (آیتونه ۱ تر ۲۲)')
    S(b, [(('Reason for the name and introduction', 'وجہ تسمیہ اور تعارف', 'د نوم وجه او پېژندنه'),
           ('"Surah al-Mujadilah" is a Madani surah. The name of this surah is taken from the word "tujadiluka" of the first verse. The literal meaning of "mujadalah" is "argument and repeated pleading". At the beginning of this surah a Companion, Sayyidah Khawlah bint Tha\'labah (may Allah be pleased with her), is mentioned, who presented before the Holy Prophet (peace and blessings of Allah be upon him) the matter of zihar that occurred to her from her husband with a complaint, and repeatedly pleaded on this issue. This pleading has been expressed with the word "mujadalah". With this connection the name of this surah has been kept "Surah al-Mujadilah". One characteristic of this surah is that it is the only surah of the Qur\'an Majid in every verse of which the name of the Exalted Lord "Allah" occurs. In the whole surah the name of the Exalted Lord "Allah" has come forty (40) times.',
            '"سُوْرَةُ الْمُجَادَلَةِ" مدنی سورت ہے۔ اس سورت کا نام پہلی آیت کے لفظ "تُجَادِلُكَ" سے ماخوذ ہے۔ مُجَادَلَةٌ کا لفظی معنی "بحث و تکرار" ہے۔ اس سورت کے شروع میں ایک صحابیہ سیدہ خولہ بنت ثعلبہ رضی اللہ تعالیٰ عنہا کا ذکر ہے جنھوں نے اپنے شوہر کی طرف سے پیش آنے والے واقعہ ظہار کا معاملہ نبی اکرم صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم کے سامنے پیش کر کے شکوہ کیا اور اس مسئلہ پر بار بار تکرار کیا۔ اسی تکرار کو لفظ "مُجَادَلَةٌ" سے تعبیر فرمایا گیا ہے۔ اسی مناسبت سے اس کا نام "سُوْرَةُ الْمُجَادَلَةِ" رکھا گیا ہے۔ اس سورت کی ایک خصوصیت یہ ہے کہ یہ قرآن مجید کی واحد سورت ہے جس کی ہر آیت میں اسم باری تعالیٰ "اللہ" آتا ہے۔ پوری سورت میں اسم باری تعالیٰ "اللہ" چالیس (۴۰) مرتبہ آیا ہے۔',
            '«سورة المجادله» مدني سورت دی. د دې سورت نوم د لومړي آیت له «تجادلک» کلمې اخیستل شوی. د «مجادله» لفظي مانا «بحث او تکرار» دی. د دې سورت په پیل کې د یوې صحابیې سیدې خوله بنت ثعلبه رضي الله عنها یادونه ده چې د خپل مېړه له لوري یې د ظهار پېښه نبي اکرم صلی الله علیه وعلی آله واصحابه وسلم ته وړاندې کړه، شکایت یې وکړ او پر دې مسئله یې څو ځله تکرار وکړ. همدا تکرار په «مجادله» کلمه بیان شوی؛ په همدې مناسبت یې نوم «سورة المجادله» ایښودل شوی. د دې سورت یوه ځانګړنه دا ده چې دا د قرآن مجید یوازینی سورت دی چې په هر آیت کې یې د باري تعالی نوم «الله» راغلی؛ په ټول سورت کې د باري تعالی نوم «الله» څلوېښت (۴۰) ځله راغلی.')),
          (('Central theme', 'مرکزی مضمون', 'مرکزي مضمون'),
           ('Social reform and the struggle for the supremacy of the religion', 'معاشرتی اصلاح اور غلبۂ دین کی جدوجہد', 'ټولنیز اصلاح او د دین د غلبې هڅې')),
          (('Basic themes', 'بنیادی مضامین', 'بنسټیز مضامین'), None)])
    L(b, [(f'{i}. {e}', f'{str(i).translate(D)}۔ {u}', f'{i}. {p}') for i, (e, u, p) in enumerate(THEMES, 1)])
    b.h('Surah al-Mujadilah (58) — Madani; order of revelation 105; verses 22, sections 3', 'سُوْرَةُ الْمُجَادَلَةِ ۵۸ — مَدَنِيَّةٌ ۱۰۵ — اٰیَاتُهَا ۲۲، رُکُوْعَاتُهَا ۳', 'سورة المجادله (۵۸) — مدني؛ د نزول ترتیب ۱۰۵؛ آیتونه ۲۲، رکوعونه ۳')
    b.p('بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nIn the name of Allah, the Beneficent, the Merciful.', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nاللہ کے نام سے شروع جو بڑا مہربان نہایت رحم فرمانے والا ہے', 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ\nد الله په نوم پیل چې ډېر مهربان، بې‌حده رحم کوونکی دی')
    b.paras[-1]['arabicSource'] = True
    V(b, 58, 1, 'یقیناً اللہ نے اُس عورت کی بات سن لی جو آپ (صلی اللہ علیہ وعلیٰ آلہٖ واصحابہٖ وسلم) سے اپنے شوہر کے بارے میں تکرار کر رہی تھی اور اللہ سے فریاد کر رہی تھی اور اللہ آپ دونوں کی گفت گو سن رہا تھا بے شک اللہ خوب سننے والا خوب دیکھنے والا ہے۔',
      'یقیناً الله د هغې ښځې خبره واورېده چې له تاسو (صلی الله علیه وعلی آله واصحابه وسلم) سره یې د خپل مېړه په اړه تکرار کاوه او الله ته یې فریاد کاوه؛ او الله ستاسو دواړو خبرې اورېدې؛ بې‌شکه الله ښه اورېدونکی، ښه لیدونکی دی.')
    V(b, 58, 2, 'تم میں سے جو لوگ اپنی بیویوں سے ظہار کرتے (ہوئے انھیں ماں کی پیٹھ سے تشبیہ دے بیٹھتے) ہیں وہ اُن کی (حقیقی) مائیں نہیں ہیں اُن کی مائیں تو صرف وہی ہیں جنھوں نے انھیں جنا ہے اور یقیناً وہ بُری اور جھوٹ بات کہتے ہیں اور یقیناً اللہ بہت معاف فرمانے والا بڑا ہی بخشنے والا ہے۔',
      'له تاسو هغه کسان چې له خپلو مېرمنو ظهار کوي (او هغوی د مور له شا سره تشبیه کوي)، هغوی د دوی (حقیقي) میندې نه دي؛ د دوی میندې خو یوازې هغه دي چې دوی یې زېږولي؛ او یقیناً دوی بده او دروغ خبره کوي؛ او یقیناً الله ډېر عفو کوونکی، ډېر بښونکی دی.')
    BOOK.save(181, [(19, rec(b, 19, 181, 181, first=True, pages_=[178, 179]))], issues=[{'id': 'mq12-pdf181', 'unit': 19, 'printedPage': 178,
               'description': 'Lesson 19 heading: Surah al-Mujadilah, verses 1 to 22. Ten basic themes printed as a run-on numbered paragraph; rendered as a list. Surah cartouche: al-Mujadilah 58, Madaniyyah 105, ayat 22, ruku 3. Verse 58:2 ends on the first line of p.179; recorded here.'}])


if __name__ == '__main__':
    p181()
