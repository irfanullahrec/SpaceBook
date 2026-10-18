"""Islamiat (Ikhtiari) XII PDF78: pp.146–147 — hadith 50 (end); Hadith exercise Q1, Q2 MCQs. Run: python class12_iski_page078.py"""
from class12_iski_common import BOOK, Builder, rec, P, L

Q1 = [('i. Can a lie be told jokingly?', 'i۔ کیا مذاقاً جھوٹ بولا جا سکتا ہے؟', 'i. ایا په ټوکو دروغ ویل کېدای شي؟'),
      ('ii. How does Allah the Exalted grant understanding of the religion?', 'ii۔ اللہ تعالیٰ دین کی سمجھ کیسے عطا فرماتا ہے؟', 'ii. الله تعالی د دین پوهه څنګه ورکوي؟'),
      ('iii. What kind of treatment of parents has been urged?', 'iii۔ والدین کے ساتھ کیسا سلوک کرنے کی تلقین کی گئی ہے؟', 'iii. له مور و پلار سره د څه ډول چلند سپارښتنه شوې؟'),
      ('iv. What is meant by controlling the tongue?', 'iv۔ زبان پر قابو رکھنے سے کیا مراد ہے؟', 'iv. پر ژبه له واک ساتلو څه مراد دي؟'),
      ('v. Define backbiting.', 'v۔ غیبت کی تعریف کریں۔', 'v. د غیبت تعریف وکړئ.'),
      ('vi. What is slander called?', 'vi۔ بہتان کسے کہتے ہیں؟', 'vi. تهمت څه ته وايي؟'),
      ('vii. With whom will Allah the Exalted not speak on the Day of Judgement?', 'vii۔ روزِ قیامت اللہ تعالیٰ کن سے کلام نہیں کرے گا؟', 'vii. د قیامت په ورځ به الله تعالی له چا سره خبرې نه کوي؟'),
      ('viii. The service of parents has been declared equal to which act of worship?', 'viii۔ والدین کی خدمت کو کس عبادت کے برابر قرار دیا گیا ہے؟', 'viii. د مور و پلار خدمت له کوم عبادت سره برابر ګڼل شوی؟'),
      ('ix. Explain "a believer is a mirror for a believer".', 'ix۔ ”مومن مومن کے لیے آئینہ ہے“ وضاحت کریں۔', 'ix. «مؤمن د مؤمن لپاره هینداره ده» وضاحت وکړئ.'),
      ('x. What has been declared the best deed after the obligatory duties?', 'x۔ فرائض کے بعد افضل عمل کسے قرار دیا گیا ہے؟', 'x. له فرائضو وروسته غوره عمل کوم ګڼل شوی؟'),
      ('xi. What attitude should be adopted with one in hardship?', 'xi۔ تنگ دست کے ساتھ کیسا رویہ اختیار کرنا چاہیے؟', 'xi. له تنګلاسي سره باید څه ډول چلند وشي؟'),
      ('xii. What has been said about the heart?', 'xii۔ دل کے بارے میں کیا ارشاد ہوا ہے؟', 'xii. د زړه په اړه څه ارشاد شوی؟'),
      ('xiii. How did the Companion (may Allah be pleased with him) serve the guest of the Noble Prophet ﷺ?', 'xiii۔ صحابی رضی اللہ عنہ نے نبی اکرم صلی اللہ علیہ وآلہٖ وسلم کے مہمان کی خدمت کیسے کی؟', 'xiii. صحابي رضي الله عنه د نبي اکرم ﷺ د مېلمه خدمت څنګه وکړ؟'),
      ('xiv. For how many days can a Muslim remain displeased with his brother?', 'xiv۔ مسلمان اپنے بھائی سے کتنے دن ناراض رہ سکتا ہے؟', 'xiv. مسلمان له خپل ورور څو ورځې ناخوښ پاتې کېدای شي؟'),
      ('xv. Believers among themselves are like what thing?', 'xv۔ مومن آپس میں کس چیز کی مانند ہیں؟', 'xv. مؤمنان په خپل منځ کې د کوم شي په څېر دي؟')]

O = lambda e, u, p: (e, u, p)
MCQ = [(('(a) A woman was thrown into Hell because she:', 'الف۔ ایک عورت کو جہنم میں اس لئے ڈالا گیا کہ اس نے:', 'الف. یوه ښځه ځکه دوزخ ته واچول شوه چې هغې:'),
        [O('tied up a cat and killed it', 'بلی کو باندھ کر مار دیا تھا', 'پیشو یې وتړله او ویې وژله'), O('did not give water to a thirsty dog', 'پیاسے کتے کو پانی نہ پلایا', 'تږي سپي ته یې اوبه ورنه کړې'),
         O('harmed people by backbiting', 'غیبت کر کے لوگوں کو نقصان پہنچایا', 'په غیبت یې خلکو ته زیان ورساوه'), O('troubled Muslims', 'مسلمانوں کو تکلیف دی', 'مسلمانان یې وځورول')]),
       (('(b) If two Muslims quarrel, for how many days can they turn away from each other?', 'ب۔ اگر دو مسلمان آپس میں لڑ پڑیں تو کتنے دنوں تک ایک دوسرے سے اعراض کر سکتے ہیں؟', 'ب. که دوه مسلمانان سره وجنګېږي، څو ورځې له یو بل مخ اړولای شي؟'),
        [O('one day', 'ایک دن', 'یوه ورځ'), O('three days', 'تین دن', 'درې ورځې'), O('five days', 'پانچ دن', 'پنځه ورځې'), O('seven days', 'سات دن', 'اووه ورځې')]),
       (('(c) Helping widows and the needy is just like someone who:', 'ج۔ بیواؤں اور مسکینوں کی مدد کرنا ایسا ہی ہے جیسے کوئی:', 'ج. د کونډو او مسکینانو مرسته داسې ده لکه څوک چې:'),
        [O('gives charity in the way of Allah', 'اللہ کی راہ میں صدقہ کرے', 'د الله په لاره کې صدقه ورکړي'), O('visits the House of Allah', 'بیت اللہ کی زیارت کرے', 'د بیت الله زیارت وکړي'),
         O('strives in the way of Allah', 'اللہ کے راستے میں جہاد کرے', 'د الله په لاره کې جهاد وکړي'), O('fasts in the month of Ramadan', 'ماہِ رمضان کے روزے رکھے', 'د رمضان میاشتې روژې ونیسي')]),
       (('(d) A hadith qudsi is that in which the Noble Prophet ﷺ says that:', 'د۔ حدیثِ قدسی وہ ہوتی ہے جس میں نبی اکرم صلی اللہ علیہ وآلہٖ وسلم فرمائیں کہ', 'د. قدسي حدیث هغه دی چې په کې نبي اکرم ﷺ ووایي چې:'),
        [O('my followers will go to Paradise', 'میرے امتی جنت میں جائیں گے', 'زما امتیان به جنت ته ځي'), O('my Companions (may Allah be pleased with them) are people of excellence', 'میرے صحابہ رضی اللہ عنہم فضیلت والے ہیں', 'زما صحابه رضي الله عنهم د فضیلت خاوندان دي'),
         O('help the helpless', 'بے سہارا لوگوں کی مدد کرو', 'د بې‌سرپرسته خلکو مرسته وکړئ'), O('Allah the Exalted says thus', 'اللہ تعالیٰ یوں فرماتا ہے', 'الله تعالی داسې فرمایي')]),
       (('(e) The love of believers among themselves has been likened to what thing?', 'ہ۔ مومنین کی آپس میں محبت کی مثال کس چیز سے دی گئی ہے؟', 'ه. د مؤمنانو د متقابلې مینې مثال په کوم شي ورکړل شوی؟'),
        [O('body', 'جسم', 'بدن'), O('head', 'سر', 'سر'), O('limb', 'عضو', 'غړی'), O('wall', 'دیوار', 'دېوال')])]


def p78():
    b = Builder()
    P(b, [('In society the needy and the widow usually have no helper, and they are considered helpless. He ﷺ said to his followers that whoever helps them, is of use to them, his excellence is just like that of one who strove in the way of Allah, or spent the whole night in worship and the whole day fasting.', 'معاشرے میں مسکین اور بیوہ کے لیے عموماً کوئی مددگار نہیں ہوتا اور وہ بے سہارا سمجھے جاتے ہیں۔ آپ صلی اللہ علیہ وآلہٖ وسلم نے اپنے امتیوں کو ارشاد فرمایا کہ جو ان کی مدد کرے، ان کے کام آئے تو اس کی فضیلت ایسی ہی ہے جیسے اس نے اللہ کے راستے میں جہاد کیا۔ یا ساری رات عبادت میں گزاری اور سارا دن روزے سے رہا۔', 'په ټولنه کې مسکین او کونډه عموماً مرستندوی نه لري او بې‌سرپرسته ګڼل کېږي. هغه ﷺ خپلو امتیانو ته وفرمایل چې څوک د هغوی مرسته وکړي، د هغوی په کار راشي، د هغه فضیلت داسې دی لکه چې د الله په لاره کې یې جهاد کړی وي، یا یې ټوله شپه په عبادت او ټوله ورځ په روژه تېره کړې وي.'),
          ('In view of the excellence stated in this hadith, who would be so unfortunate as not to be of use to a widow or not to place his hand on the head of some needy person. We pray to Allah the Exalted that He grant us the ability to do good deeds and bless us with the honour of creating ease for others. (Amen)', 'اس حدیث میں بیان کی گئی فضیلت کے پیشِ نظر کون بدقسمت ہوگا جو بیوہ کے کام نہ آئے یا کسی مسکین کے سر پر ہاتھ نہ رکھے۔ اللہ تعالیٰ سے دعا ہے کہ وہ ہمیں نیک کام کرنے کی توفیق دے اور دوسروں کے لیے آسانیاں پیدا کرنے کا شرف عطا فرمائے۔ (آمین)', 'د دې حدیث د بیان شوي فضیلت په پام کې نیولو سره به څوک دومره بدبخته وي چې د کونډې په کار رانشي یا د کوم مسکین پر سر لاس کېنږدي. له الله تعالی دعا ده چې موږ ته د نېکو کارونو توفیق راکړي او د نورو لپاره د اسانتیاوو د پیدا کولو شرف راپه برخه کړي. (آمین)')])
    b.h('Exercise', 'مشق', 'تمرین')
    b.p('Question 1: Write the answers to the following questions in the light of the given blessed ahadith.', 'سوال 1: دی گئی احادیثِ مبارکہ کی روشنی میں درج ذیل سوالوں کے جواب لکھیں۔', 'پوښتنه ۱: د ورکړل شویو مبارکو احادیثو په رڼا کې د لاندې پوښتنو ځوابونه ولیکئ.')
    L(b, Q1[:11])
    r1 = rec(b, 2, 146, 78, [146], kind='exercise')
    t = Builder()
    L(t, Q1[11:])
    t.p('Question 2: Four answers are given for each of the following questions. Put a (✓) mark on the correct answer in the light of the blessed ahadith.', 'سوال 2: درج ذیل ہر سوال کے چار چار جواب دیے گئے ہیں۔ احادیثِ مبارکہ کی روشنی میں درست جواب پر (✓) کا نشان لگائیں؟', 'پوښتنه ۲: د لاندې هرې پوښتنې لپاره څلور څلور ځوابونه ورکړل شوي. د مبارکو احادیثو په رڼا کې پر سم ځواب (✓) نښه ولګوئ.')
    for q, o in MCQ:
        t.mcq('', q, o)
    BOOK.save(78, [(2, r1), (2, rec(t, 2, 147, 78, [147], kind='exercise'))], issues=[{'id': 'iski12-pdf078', 'unit': 2, 'printedPage': 146,
               'description': 'Student handwriting (page numbers 118–133 written beside each question of Q1) excluded. MCQ options printed i–iv; no ticks printed (no key).'}])


if __name__ == '__main__':
    p78()
