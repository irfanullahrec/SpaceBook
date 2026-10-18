"""Urdu XII PDF120 (spread): p.230 Ghazal 12 author note (ناصر کاظمی, 1925–1972); p.231 Ghazal 12 full text (public domain) + مشق Q1–Q5."""
from class12_book_common import Book, Builder

BOOK = Book('urdu')
a = Builder()
a.h('Nasir Kazmi', 'ناصرؔ کاظمی', 'ناصر کاظمي')
a.p('Born: 1925 · Died: 1972', 'ولادت: ۱۹۲۵ء · وفات: ۱۹۷۲ء', 'زېږېدنه: ۱۹۲۵ز · مړینه: ۱۹۷۲ز')
for x in [
    ("Nasir Kazmi was born in Ambala. His father, Muhammad Sultan Kazmi, served in the Indian Army and was posted at various places, so Nasir Kazmi was educated in different cities. On completing his education he went back to Ambala and began looking after the family lands. After the creation of Pakistan he came to Lahore and was associated with various journalistic institutions. He was also chief editor of the monthly “Humayun”. For some time he worked at Radio Pakistan Lahore. Nasir Kazmi died in Lahore.",
     'ناصرؔ کاظمی انبالہ میں پیدا ہوئے۔ ان کے والد محمد سلطان کاظمی انڈین آرمی میں ملازم تھے اور اُن کی تعیناتی مختلف مقامات پر رہی۔ اس لیے ناصر کاظمی نے مختلف شہروں میں تعلیم حاصل کی۔ تعلیم کی تکمیل پر وہ واپس انبالہ چلے گئے اور زمینوں کی دیکھ بھال شروع کی۔ قیامِ پاکستان کے بعد وہ لاہور چلے آئے اور مختلف صحافتی اداروں سے منسلک رہے۔ وہ ماہنامہ ’’ہمایوں‘‘ کے چیف ایڈیٹر بھی رہے۔ کچھ عرصہ ریڈیو پاکستان لاہور میں بھی ملازمت کی۔ ناصرؔ کاظمی کا انتقال لاہور میں ہوا۔',
     'ناصر کاظمي په انباله کې زېږېدلی. پلار یې محمد سلطان کاظمي په هندي پوځ کې کارمند و او په بېلابېلو ځایونو کې ګومارل کېده، نو ناصر کاظمي په بېلابېلو ښارونو کې زده‌کړې وکړې. د زده‌کړو په بشپړېدو بېرته انبالې ته لاړ او د ځمکو څارنه یې پیل کړه. د پاکستان له جوړېدو وروسته لاهور ته راغی او له بېلابېلو ژورنالیستي ادارو سره تړلی و. د میاشتنۍ "همایون" لوی مدیر هم و. یو څه موده یې په راډیو پاکستان لاهور کې هم دنده وکړه. ناصر کاظمي په لاهور کې وفات شو.'),
    ("Nasir's ghazals show a blend of the classical colour and modern romantic attitudes. At the height of the Progressive Movement, when the naẓm was in full swing, Nasir upheld the prestige of the ghazal. In his ghazal, along with Mir's manner of expression, Mir's way of feeling is also found. The creation of Pakistan was on the one hand a great event for the Muslims, but on the other it had its tragic aspects — the worst riots, killing and plunder, terror, and migration from one's own soil. Like others, these circumstances left deep effects on Nasir Kazmi's heart and mind. His ghazals mourn the defeat of high values. Along with the feeling of sorrow, despair, deprivation and failure, the expression of satire and bitterness on the negative values of society is prominent in his ghazal. Nasir's poetry has simplicity and charm; he expresses his feelings in short metres and simple words.",
     'ناصرؔ کی غزلوں میں قدیم رنگ اور جدید رومانی رویوں کا امتزاج ملتا ہے۔ ترقی پسند تحریک کے عروج میں جب نظم زوروں پر تھی، ناصرؔ نے غزل کی ساکھ کو قائم رکھا۔ ان کی غزل میں میرؔ کے طرزِ ادا کے ساتھ ساتھ ان کا طرزِ احساس بھی ملتا ہے۔ پاکستان کا قیام ایک طرف تو مسلمانوں کے لیے ایک عظیم واقعہ ہے لیکن دوسری طرف بدترین فسادات، قتل و غارت گری، دہشت گردی اور اپنی مٹی سے ہجرت، اس کے الم ناک پہلو بھی ہیں۔ ان حالات نے اوروں کی طرح ناصرؔ کاظمی کے دل و دماغ پر بھی برے اثرات مرتب کیے۔ ان کی غزلوں میں اعلیٰ اقدار کی شکست کا ماتم ہے۔ حزن و یاس، محرومی اور ناکامی کے احساس کے ساتھ معاشرے کی منفی قدروں پر طنز اور تلخی کا اظہار ان کی غزل میں نمایاں ہے۔ ناصرؔ کی شاعری میں سادگی اور دلکشی ہے۔ چھوٹی چھوٹی بحروں اور سادہ الفاظ میں وہ اپنے جذبوں کا اظہار کرتے ہیں۔',
     'د ناصر په غزلو کې د زوړ رنګ او نویو رومانتیکو چلندونو ګډون موندل کېږي. د ترقي‌پسند غورځنګ په اوج کې چې نظم په زور کې و، ناصر د غزل وقار وساته. د هغه په غزل کې د میر د بیان له انداز سره د هغه د احساس انداز هم موندل کېږي. د پاکستان جوړېدل له یوې خوا د مسلمانانو لپاره لویه پېښه وه، خو له بلې خوا تر ټولو بدې بلواوې، وژنې او لوټمارۍ، ترهګري او له خپلې خاورې کډوالي یې دردناک اړخونه هم وو. دې حالاتو د نورو په څېر د ناصر کاظمي پر زړه او ذهن هم بد اغېز وکړ. د هغه په غزلو کې د لوړو ارزښتونو د ماتې ویر دی. د غم، نهیلۍ، محرومیت او ناکامۍ له احساس سره د ټولنې پر منفي ارزښتونو طنز او ترخه څرګندونه یې په غزل کې ښکاره ده. د ناصر په شاعرۍ کې سادګي او زړه‌راښکونتیا ده؛ په لنډو بحرونو او ساده کلمو خپل احساسات څرګندوي.'),
    ('Collections of poetry: Barg-e-Nai, Khushk Chashme ke Kinare, Diwan, Pehli Barish, Nishat-e-Khwab, Sur ki Chhaya.', 'مجموعہ ہائے کلام: برگِ نَے۔ خشک چشمے کے کنارے۔ دیوان۔ پہلی بارش۔ نشاطِ خواب۔ سُر کی چھایا۔', 'د کلام ټولګې: برګ نی، د وچې چینې پر غاړه، دیوان، لومړی باران، نشاط خواب، سر کي چهایا.'),
]: a.p(*x)
UT = ('Ghazal: I do not remember the journey to the night’s destination', 'غزل: سفرِ منزلِ شب یاد نہیں', 'غزل: د شپې د منزل سفر مې په یاد نه دی', 'ناصرؔ کاظمی')
au = BOOK.record(a, 'urdu12-u29-author', 'About the poet: Nasir Kazmi', 'ناصرؔ کاظمی (تعارف)', 'ناصر کاظمي (پېژندنه)', 120, [230], unit_title=UT)
au['sourceCoverIllustrationReview'] = 'Portrait photograph of Nasir Kazmi and floral border are decorative; not reproduced.'

t = Builder()
t.h('Ghazal — Nasir Kazmi', 'غزل — ناصرؔ کاظمی', 'غزل — ناصر کاظمي')
SH = [
 ('I do not remember the journey to the night’s destination; when people took their leave, I do not remember.', 'سفرِ منزلِ شب یاد نہیں ۔ لوگ رخصت ہوئے کب یاد نہیں', 'د شپې د منزل سفر مې په یاد نه دی؛ خلک کله رخصت شول، په یاد مې نه دي.'),
 ('In the ecstasy of the first nearness, how many longings there were that I no longer remember.', 'اوّلیں قُرب کی سرشاری میں ۔ کتنے ارماں تھے جو اب یاد نہیں', 'د لومړني نږدېکت په مستۍ کې، څومره ارمانونه وو چې اوس مې په یاد نه دي.'),
 ('There was a constant ache in the heart; whom I was longing for, I do not remember.', 'دل میں ہر وقت چبھن رہتی تھی ۔ تھی مجھے کس کی طلب یاد نہیں', 'په زړه کې به تل چوخ و؛ د چا غوښتنه مې وه، په یاد مې نه ده.'),
 ('Was it a star, or dew, or a flower? It was a strange face; I do not remember.', 'وہ ستارا تھی کہ شبنم تھی کہ پھول ۔ ایک صورت تھی عجب یاد نہیں', 'هغه ستوری وه که پرخه که ګل؟ یوه عجیبه څېره وه، په یاد مې نه ده.'),
 ('How desolate is the thoroughfare of thought, ever since I no longer remember that cheek and lip.', 'کیسی ویراں ہے گزر گاہِ خیال ۔ جب سے وہ عارض و لب یاد نہیں', 'د فکر لاره څومره ورانه ده، له هغه وخته چې هغه مخ او شونډې مې په یاد نه دي.'),
 ('The lands of the past are being forgotten; even when they come to mind, I do not remember them now.', 'بھولتے جاتے ہیں ماضی کے دیار ۔ یاد آئیں بھی تو اب یاد نہیں', 'د تېر وخت سیمې هېرېږي؛ که رایاد هم شي، اوس یې نه یادوم.'),
 ('The one whose thought was once the thread of my life — even her face I no longer remember.', 'رشتۂ جاں تھا کبھی جس کا خیال ۔ اُس کی صورت بھی تو اب یاد نہیں', 'د چا خیال چې یو وخت زما د ژوند تار و — اوس یې څېره هم په یاد نه ده.'),
 ('This is the truth: when did we ever remember our friends, that we should say we do not remember them now?', 'یہ حقیقت ہے کہ احباب کو ہم ۔ یاد ہی کب تھے کہ اب یاد نہیں', 'دا حقیقت دی چې ملګري موږ ته کله یاد وو، چې اوس یې یاد نه کړو؟'),
 ('Nasir, I remember the festival of lamps, but the cause of the heart’s going out, I do not remember.', 'یاد ہے سیرِ چراغاں ناصرؔ ۔ دل کے بجھنے کا سبب یاد نہیں', 'ناصره! د څراغانو ننداره مې یاده ده، خو د زړه د مړ کېدو لامل مې په یاد نه دی.'),
]
t.group('lines', SH)
t.p('(Barg-e-Nai)', '(برگِ نَے)', '(برګ نی)')
po = BOOK.record(t, 'urdu12-u29-ghazal', 'Ghazal text', 'متنِ غزل', 'د غزل متن', 120, [231])
po['sourceNote'] = 'Printed in two columns of half-lines; each couplet is given on one line with the two half-lines joined by “ ۔ ”.'

e = Builder()
e.h('Exercise', 'مشق', 'تمرین')
e.group('lines', [
    ('1. Write the rhymes and refrain (radīf) of this ghazal.', '۱۔ اس غزل کے قوافی اور ردیف لکھیں۔', '۱. د دې غزل قافیې او ردیف ولیکئ.'),
    ('2. Write the grammatical names of the following compounds: ʿāriẓ-o-lab, guzargāh-e khayāl, rishta-e jāṉ.', '۲۔ قواعد کی رُو سے درج ذیل مرکبات کے نام لکھیں: عارض و لب، گزرگاہِ خیال، رشتۂ جان۔', '۲. د قواعدو له مخې د لاندې مرکباتو نومونه ولیکئ: عارض و لب، د فکر لاره، د ژوند تار.'),
    ("3. Why is there always an ache in the poet's heart?", '۳۔ شاعر کے دل میں ہر وقت چبھن کیوں رہتی ہے؟', '۳. د شاعر په زړه کې ولې تل چوخ وي؟'),
    ('4. What complaint has the poet made against his friends?', '۴۔ شاعر نے احباب سے کیا گلہ کیا ہے؟', '۴. شاعر له ملګرو څه ګیله کړې؟'),
    ("5. Why has Nasir not told the reason for his heart's going out?", '۵۔ ناصرؔ نے دل کے بجھنے کی وجہ کیوں نہیں بتائی؟', '۵. ناصر د زړه د مړ کېدو لامل ولې ونه ښود؟'),
])
ex = BOOK.record(e, 'urdu12-u29-exercise', 'Exercise', 'مشق', 'تمرین', 120, [231])
issues = [{'id': 'urdu12-pdf120', 'unit': 29, 'printedPage': 230, 'description': 'Nasir Kazmi died 1972 → public domain in Pakistan; Ghazal 12 transcribed in full. The death-year digit on p.230 is unclear in the scan (۱۹۷۲/۱۹۷۳); the standard date (2 March 1972) is used.'}]

if __name__ == '__main__':
    BOOK.save(120, [(29, au), (29, po), (29, ex)], issues=issues, complete_units=[29])
