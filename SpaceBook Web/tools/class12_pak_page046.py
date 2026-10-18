"""Pak Studies XII PDF46 (spread): printed pp.81–82 — Ch.4 UN Universal Declaration of Human Rights, 18 points."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
P('… rights, which are included in the United Nations declaration of universal human rights, in some context or other.',
  '… حقوق کا ذکر کسی نہ کسی حوالے سے ضرور کیا ہے جو اقوامِ متحدہ کے عالمگیر انسانی حقوق کے اعلان میں شامل ہیں۔',
  '… حقونو یادونه په یوه نه یوه حواله خامخا کړې، چې د ملګرو ملتونو د بشري حقونو په نړیوال اعلان کې شامل دي.')
H('The United Nations Universal Declaration of Human Rights', 'اقوامِ متحدہ کا عالمگیر انسانی حقوق کا اعلامیہ', 'د ملګرو ملتونو د بشري حقونو نړیوال اعلامیه')
P('On 10 December 1948 the General Assembly of the United Nations approved the Universal Declaration of Human Rights, and all member countries were asked to publicise this declaration and teach it in schools and other educational institutions, so that awareness of basic human rights could be created among people.',
  'اقوامِ متحدہ کی جنرل اسمبلی نے 10 دسمبر 1948ء کو عالمی انسانی حقوق کا اعلامیہ منظور کیا اور تمام رکن ممالک سے کہا گیا کہ وہ اس اعلامیے کو مشتہر کریں اور سکولوں اور دیگر تعلیمی اداروں میں پڑھائیں تاکہ لوگوں میں بنیادی انسانی حقوق کے بارے میں شعور پیدا کیا جا سکے۔',
  'د ملګرو ملتونو عمومي اسمبلۍ د ۱۹۴۸ز د ډسمبر په ۱۰مه د بشري حقونو نړیواله اعلامیه تصویب کړه، او له ټولو غړو هېوادونو وغوښتل شول چې دا اعلامیه خپره کړي او په ښوونځیو او نورو تعلیمي ادارو کې یې ولولي، څو په خلکو کې د بنسټیزو بشري حقونو په اړه پوهاوی پیدا شي.')
P('According to this declaration of the United Nations, a few of the rights available to all human beings of the world on the basis of equality are as follows.',
  'اقوامِ متحدہ کے اس اعلامیے کی رو سے دُنیا کے تمام انسانوں کو برابری کی بنیاد پر حاصل حقوق میں سے چند مندرجہ ذیل ہیں۔',
  'د ملګرو ملتونو د دې اعلامیې له مخې د نړۍ ټولو انسانانو ته د برابرۍ پر بنسټ د حاصلو حقونو ځینې دا دي:')
t.group('lines', [
 ('1. All human beings are born free and equal in dignity and rights.', '1۔ تمام انسان پیدائشی طور پر آزاد ہیں اور یکساں عزت اور حقوق کے مالک ہیں۔', '۱. ټول انسانان په زېږون کې ازاد دي او د یو شان عزت او حقونو خاوندان دي.'),
 ('2. All human beings of the world, without distinction of colour, race, nationality or religion, have equal fundamental rights.', '2۔ دُنیا کے تمام انسانوں کو بلا تفریق رنگ و نسل، قومیت، مذہب، یکساں بنیادی حقوق حاصل ہیں۔', '۲. د نړۍ ټولو انسانانو ته پرته د رنګ، نژاد، ملیت او دین له توپیره یو شان بنسټیز حقونه حاصل دي.'),
 ('3. Every human being has the right to defend his life, property and liberty.', '3۔ ہر انسان کو اپنی جان و مال اور آزادی کے دفاع کا حق حاصل ہے۔', '۳. هر انسان د خپل ځان، مال او ازادۍ د دفاع حق لري.'),
 ('4. Slavery and forced labour were prohibited.', '4۔ غلامی اور جبری مشقت کو ممنوع قرار دیا گیا۔', '۴. غلامي او جبري کار منع شول.'),
 ('5. No human being shall be subjected to torture or cruel punishment or inhuman treatment.', '5۔ کسی انسان کو تشدد، ظالمانہ سزا یا غیر انسانی سلوک کا نشانہ نہیں بنایا جائے گا۔', '۵. هېڅ انسان به د شکنجې، ظالمانه سزا یا غیر انساني چلند ښکار نه کېږي.'),
 ('6. All human beings are equal before the law and all have equal legal protection.', '6۔ تمام انسان قانون کی نظر میں برابر ہیں اور سب کو یکساں قانونی تحفظ حاصل ہے۔', '۶. ټول انسانان د قانون په وړاندې برابر دي او ټولو ته یو شان قانوني ساتنه حاصله ده.'),
 ('7. No one shall be arrested or exiled without justification.', '7۔ کسی کو بلا جواز نہ تو گرفتار کیا جائے گا نہ جلا وطن کیا جائے گا۔', '۷. هېڅوک به بې‌توجیه نه نیول کېږي او نه جلاوطن کېږي.'),
 ('8. In case of an offence being committed, every person shall be presumed innocent until his offence is proved, and during judicial proceedings every person shall have the full right to defend himself.', '8۔ جرم سرزد ہونے کی صورت میں ہر شخص اس وقت تک بے گناہ تصور ہوگا جب تک اس کا جرم ثابت نہیں ہو جاتا اور عدالتی کارروائی کے دوران ہر شخص کو اپنا دفاع کرنے کا پورا پورا حق حاصل ہوگا۔', '۸. د جرم د ترسره کېدو په صورت کې هر کس تر هغه بې‌ګناه ګڼل کېږي چې جرم یې ثابت نه شي، او د محکمې د بهیر پر مهال هر کس ته د خپل دفاع بشپړ حق حاصل وي.'),
 ('9. Every human being has the right, for any reason, to leave his country and to return to his country.', '9۔ ہر انسان کو کسی وجہ کی بنا پر اپنا ملک چھوڑنے اور ملک میں واپس آنے کا حق حاصل ہے۔', '۹. هر انسان د هر لامل له مخې د خپل هېواد د پرېښودو او بېرته ستنېدو حق لري.'),
 ('10. If not involved in crimes, every human being has the right to take refuge in another country and to obtain protection from persecution.', '10۔ جرائم میں ملوث نہ ہونے کی صورت میں ہر انسان کو کسی دوسرے ملک میں پناہ لینے اور ظلم سے تحفظ حاصل کرنے کا حق حاصل ہے۔', '۱۰. که په جرمونو کې ښکېل نه وي، هر انسان په بل هېواد کې د پناه اخیستو او له ظلمه د ساتنې حق لري.'),
 ('11. Every human being has the right to own property individually or collectively, and no one shall be deprived of his ownership of property.', '11۔ ہر انسان کو انفرادی یا اجتماعی صورت میں جائیداد رکھنے کا حق حاصل ہے اور کسی کو اُس کی ملکیت جائیداد سے محروم نہیں کیا جائے گا۔', '۱۱. هر انسان په فردي یا ټولیز ډول د ملکیت د لرلو حق لري، او هېڅوک به د خپل ملکیت له خاوندۍ بې‌برخې نه کېږي.'),
 ('12. Every human being has the right to adopt any ideology or religion, to hold religious beliefs, to preach and to worship.', '12۔ ہر انسان کو کوئی بھی نظریہ یا مذہب اختیار کرنے، مذہبی عقائد رکھنے، تبلیغ اور عبادات کا حق حاصل ہے۔', '۱۲. هر انسان د هرې نظریې یا دین د غوره کولو، دیني عقیدو د لرلو، تبلیغ او عبادتونو حق لري.'),
 ('13. Every human being has the right of freedom of expression, peaceful assembly and organisation.', '13۔ ہر انسان کو آزادیٔ اظہارِ رائے، پرامن اجتماع اور تنظیم سازی کا حق حاصل ہے۔', '۱۳. هر انسان د بیان ازادۍ، سوله‌ییزې غونډې او سازمان جوړولو حق لري.'),
 ('14. Every person has the right to take part in the system of government of his country directly or through his representatives and to benefit from state services.', '14۔ ہر شخص کو اپنے ملک کے حکومتی نظام میں براہِ راست یا اپنے نمائندوں کے ذریعے حصہ لینے اور ریاستی خدمات سے مستفید ہونے کا حق حاصل ہے۔', '۱۴. هر کس حق لري چې د خپل هېواد په حکومتي نظام کې مستقیم یا د خپلو استازو له لارې ګډون وکړي او له دولتي خدماتو ګټه واخلي.'),
 ('15. Every human being has the right to adopt the occupation of his choice, to obtain equal wages for equal work and to organise (form unions) to protect his professional interests.', '15۔ ہر انسان کو اپنی مرضی کا پیشہ اختیار کرنے، مساوی کام کے لیے مساوی اجرت حاصل کرنے اور اپنے پیشہ ورانہ مفادات کا تحفظ کرنے کے لیے تنظیم سازی (یونین سازی) کا حق حاصل ہے۔', '۱۵. هر انسان حق لري چې د خپلې خوښې مسلک غوره کړي، د برابر کار لپاره برابر معاش ترلاسه کړي او د خپلو مسلکي ګټو د ساتنې لپاره سازمان (اتحادیه) جوړ کړي.'),
 ('16. All human beings have the right to lead a good and decent standard of life and to have basic facilities for health and welfare, e.g. food, clothing, housing and medical facilities.', '16۔ تمام انسانوں کو اچھی اور معیاری زندگی بسر کرنے اور صحت اور بہبود کی بنیادی سہولیات مثلاً خوراک، لباس، رہائش اور طبی سہولیات میسر ہونے کا حق ہے۔', '۱۶. ټول انسانان حق لري چې ښه او معیاري ژوند تېر کړي او د روغتیا او هوساینې بنسټیزې اسانتیاوې لکه خواړه، جامې، استوګنځی او طبي اسانتیاوې ورته برابرې وي.'),
 ('17. All people have the right to acquire education. Basic education will be compulsory and provided free, while opportunities of higher education will be available to all equally on the basis of merit.', '17۔ تمام لوگوں کو تعلیم حاصل کرنے کا حق حاصل ہے۔ بنیادی تعلیم لازمی ہوگی اور مفت فراہم کی جائے گی۔ جبکہ اعلیٰ تعلیم کے مواقع اہلیت کی بنیاد پر سب کو یکساں طور پر میسر ہوں گے۔', '۱۷. ټول خلک د زده‌کړې د ترلاسه کولو حق لري. بنسټیزه زده‌کړه به لازمي او وړیا وي، په داسې حال کې چې د لوړو زده‌کړو فرصتونه به د وړتیا پر بنسټ ټولو ته یو شان برابر وي.'),
 ('18. Every human being has fundamental rights and freedom, but he will not interfere in the rights and freedom of other human beings.', '18۔ ہر انسان کو بنیادی حقوق اور آزادی حاصل ہے مگر وہ دوسرے انسانوں کے حقوق اور آزادی میں مداخلت نہیں کرے گا۔', '۱۸. هر انسان ته بنسټیز حقونه او ازادي حاصله ده، خو هغه به د نورو انسانانو په حقونو او ازادۍ کې لاسوهنه نه کوي.'),
])
P('Of the basic human rights guaranteed in this United Nations declaration of universal human rights, most are exactly in accordance with the teachings of our religion, Islam.',
  'اقوامِ متحدہ کے اس عالمگیر انسانی حقوق کے اعلان میں جن بنیادی انسانی حقوق کی ضمانت دی گئی ہے۔ اُن میں سے اکثر و بیشتر ہمارے مذہب اسلام کی تعلیمات کے عین مطابق ہیں۔',
  'د ملګرو ملتونو په دې نړیوال بشري حقونو اعلان کې چې د کومو بنسټیزو بشري حقونو تضمین ورکړل شوی، ډېری یې زموږ د اسلام دین له لارښوونو سره سم دي.')
rec = BOOK.record(t, 'pak12-ch4-text-9', 'Chapter 4 text (9)', 'بابِ چہارم — متن (۹)', 'څلورم څپرکی — متن (۹)', 46, [81, 82])

if __name__ == '__main__':
    BOOK.save(46, [(4, rec)])
