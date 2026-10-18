"""Mutalia-e-Quran XII PDF123: p.120 — verses 33:72 (begun on p.119)–73; matters of knowledge and action; vocabulary (rows 1–16). Run: python class12_quran_page123.py"""
from class12_quran_common import BOOK, Builder, rec, V, KA, L, VOC

VOCAB = [
    ('الْحَافِظِينَ', 'Men who guard', 'حفاظت کرنے والے مرد', 'ساتونکي نارینه'),
    ('الْخِيَرَةُ', 'Choice', 'اختیار', 'اختیار'),
    ('أَنْ تَخْشَاهُ', 'That you should fear Him', 'کہ آپ اُس سے ڈریں', 'چې له هغه ووېرېږئ'),
    ('يُبَلِّغُونَ', 'They convey', 'وہ پہنچاتے ہیں', 'رسوي'),
    ('بُكْرَةً وَأَصِيلًا', 'Morning and evening', 'صبح و شام', 'سهار او ماښام'),
    ('سِرَاجًا مُنِيرًا', 'A light-giving lamp', 'روشن چراغ', 'روښانه څراغ'),
    ('طَلَّقْتُمُوهُنَّ', 'You divorced them', 'تم انھیں طلاق دے دو', 'طلاق مو ورکړ'),
    ('أَنْ تَمَسُّوهُنَّ', 'That you touch them', 'کہ تم ان کو چھوؤ (ہاتھ لگاؤ)', 'چې لاس ورووړئ'),
    ('سَرِّحُوهُنَّ', 'Release them', 'تم انھیں خوشی سے رخصت کرو', 'په خوښۍ یې رخصت کړئ'),
    ('لَا تَدْخُلُوا', 'Do not enter', 'تم داخل نہ ہوا کرو', 'مه ننوځئ'),
    ('غَيْرَ نَاظِرِينَ', 'Not waiting', 'انتظار کرنے والے نہ ہوں', 'انتظار کوونکي مه یاست'),
    ('فَانْتَشِرُوا', 'Then disperse', 'پھر تم منتشر ہو جاؤ', 'بیا خپاره شئ'),
    ('مُسْتَأْنِسِينَ', 'Lingering for (talk)', 'دل چسپی لینے والے', 'لېوالتیا لرونکي'),
    ('أَنْ تُؤْذُوا', 'That you cause hurt', 'کہ تم تکلیف پہنچاؤ', 'چې تکلیف ورسوئ'),
    ('لَا جُنَاحَ', 'No blame (sin)', 'کوئی حرج (گناہ) نہیں', 'هېڅ حرج (ګناه) نشته'),
    ('إِخْوَانِهِنَّ', 'Their brothers', 'ان کے بھائی', 'د هغوی وروڼه'),
]


def p123():
    b = Builder()
    V(b, 33, 72, 'بے شک ہم نے (احکام کی) امانت کو آسمانوں پر پیش کیا اور زمینوں پر اور پہاڑوں پر تو انھوں نے اس (ذمہ داری) کے اٹھانے سے انکار کر دیا اور وہ اس سے ڈر گئے اور انسان نے اسے اٹھا لیا بے شک وہ بڑا ظالم (اور) بڑا نادان ہے۔',
      'بې‌شکه موږ د (حکمونو) امانت پر آسمانونو، ځمکو او غرونو وړاندې کړ، نو هغوی د هغه (مسؤلیت) له پورته کولو انکار وکړ او ترې ووېرېدل، او انسان پورته کړ؛ بې‌شکه هغه ډېر ظالم (او) ډېر ناپوه دی.')
    V(b, 33, 73, 'تاکہ اللہ منافق مردوں اور منافق عورتوں کو عذاب دے اور مشرک مردوں اور مشرک عورتوں کو (بھی) اور اللہ مومن مردوں اور مومن عورتوں کی توبہ قبول فرمائے اور اللہ بہت بخشنے والا نہایت رحم فرمانے والا ہے۔',
      'تر څو الله منافقو نارینه وو او منافقو ښځو ته عذاب ورکړي، او مشرکو نارینه وو او مشرکو ښځو ته (هم)، او الله د مؤمنو نارینه وو او مؤمنو ښځو توبه ومني؛ او الله ډېر بښونکی، بې‌حده مهربان دی.')
    KA(b)
    L(b, [('We should remember Allah Almighty abundantly, and especially in the morning and evening state the glorification and sanctification of Allah Almighty. Allah Almighty sends down mercy upon such people, the angels pray for mercy for them, and Allah Almighty brings those engaged in His remembrance out of the darkness of sin into the light of obedience.', 'ہمیں کثرت سے اللہ تعالیٰ کا ذکر اور خصوصاً صبح و شام اللہ تعالیٰ کی تسبیح اور تقدیس بیان کرنی چاہیے۔ ایسے لوگوں پر اللہ تعالیٰ رحمت نازل فرماتا ہے، فرشتے ان کے لیے دعائے رحمت کرتے ہیں اور اللہ تعالیٰ اپنی یاد میں مشغول رہنے والوں کو معصیت کے اندھیروں سے اطاعت کی روشنی میں لے آتا ہے۔', 'موږ باید الله تعالی ډېر یاد کړو او په ځانګړي ډول سهار او ماښام د الله تعالی تسبیح او تقدیس بیان کړو. پر داسې خلکو الله تعالی رحمت نازلوي، پرښتې ورته د رحمت دعا کوي، او الله تعالی په خپل یاد کې بوخت کسان د ګناه له تیارو د اطاعت رڼا ته راولي.'),
          ('In social life a person should not look only at his own desire or need, but should also keep in mind that his behaviour does not become a cause of any trouble or distress for others, nor do his unnecessary words waste the time of others.', 'معاشرتی زندگی میں انسان کو صرف اپنی خواہش یا ضرورت کو ہی نہیں دیکھنا چاہیے بلکہ اس کو اس بات کا بھی خیال رکھنا چاہیے کہ اس کا رویہ دوسروں کے لیے نہ تو کسی تکلیف اور پریشانی کا باعث بنے اور نہ اس کی غیر ضروری باتیں دوسروں کا وقت ضائع کرنے والی ہوں۔', 'په ټولنیز ژوند کې انسان باید یوازې خپله غوښتنه یا اړتیا ونه ګوري، بلکې دا هم په پام کې ولري چې د هغه چلند نورو ته د کوم تکلیف او پرېشانۍ لامل نه شي، او نه یې غیر ضروري خبرې د نورو وخت ضایع کړي.'),
          ('When a Muslim woman goes out of her home for some need, her manner should be such that her dress is simple and her gait modest; further, her body should be covered with a large sheet. This is a sign that she is a modest woman, and the wisdom of this veil is to keep believing women safe from the harassment of mischievous people.', 'مسلمان عورت جب کسی ضرورت سے اپنے گھر سے باہر نکلے تو یہ کیفیت ہو کہ اس کا لباس سادہ اور چال حیادار ہو۔ مزید یہ کہ بڑی چادر سے جسم ڈھکا ہوا ہو۔ یہ علامت ہے کہ وہ ایک حیادار عورت ہے اور اس حجاب کی حکمت مومن عورتوں کو شریر لوگوں کی ایذا رسانیوں سے محفوظ رکھنا ہے۔', 'کله چې مسلمانه ښځه د کومې اړتیا لپاره له کوره بهر ووځي، نو حالت یې باید داسې وي چې جامې یې ساده او تګ یې حیاناک وي؛ همدارنګه بدن یې په لوی څادر پټ وي. دا نښه ده چې هغه یوه حیاناکه ښځه ده، او د دې حجاب حکمت دا دی چې مؤمنې ښځې د شریرو خلکو له ځورونو خوندي وساتي.')])
    VOC(b, 'mq12-l12-vocab', VOCAB)
    BOOK.save(123, [(12, rec(b, 12, 123, 123, pages_=[119, 120]))], issues=[{'id': 'mq12-pdf123', 'unit': 12, 'printedPage': 120,
               'description': 'Verse 33:72 begins on the last two lines of p.119; recorded here. Lesson verses end at 33:73; ruku sign (۹) not reproduced. Four-column vocabulary rendered as one two-column table; it continues on p.121.'}])


if __name__ == '__main__':
    p123()
