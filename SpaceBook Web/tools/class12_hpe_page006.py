"""HPE XII PDF6–11: pp.1–6 — Chapter 1 opener (lung cancer and heart diseases), causes and symptoms of lung cancer; cardiac diseases (begins).
Run: python class12_hpe_page006.py N (6–11)."""
import sys
from class12_hpe_common import BOOK, Builder, rec, P, L, deco, fig_lung_tumour, fig_smoker


def p6():
    b = Builder()
    b.h('Chapter 1: Non-Communicable Diseases', 'باب نمبر ۱: غیر متعدی امراض', '۱ څپرکی: غیر ساري ناروغۍ')
    b.h('Lung cancer and heart diseases', 'پھیپھڑوں کا کینسر اور دل کے امراض', 'د سږو سرطان او د زړه ناروغۍ')
    b.p('After the study of this chapter the students will be able to:', 'اس باب کے مطالعہ کے بعد طلبہ اس قابل ہو جائیں گے کہ وہ:', 'د دې څپرکي له مطالعې وروسته به زده‌کوونکي دې ته وړ شي چې:')
    L(b, [('state the symptoms and causes of lung cancer.', 'پھیپھڑوں کے کینسر کی علامات اور وجوہات بیان کر سکیں۔', 'د سږو د سرطان نښې او لاملونه بیان کړي.'),
          ('state the protective measures for prevention of heart diseases.', 'دل کی بیماریوں سے بچاؤ کے حفاظتی اقدامات بیان کر سکیں۔', 'د زړه له ناروغیو د ژغورنې ساتنیز ګامونه بیان کړي.')])
    b.h('Causes and symptoms of lung cancer', 'پھیپھڑوں کے کینسر کی وجوہات اور علامات', 'د سږو د سرطان لاملونه او نښې')
    P(b, [('Cancer is the most dangerous and fatal of all diseases. This disease occurs through the uncontrolled division of some cells of the body. The body keeps the division of cells under control, so that new cells are produced only when they are needed. Because of a defect in this system the division of cells becomes uncontrolled. Through the uncontrolled division of cells a mass or lump is formed. This is called a tumour (Tumor).',
           'کینسر تمام بیماریوں میں سب سے خطرناک اور مہلک بیماری ہے۔ یہ بیماری جسم کے کچھ خلیوں کی بے قابو تقسیم سے ہوتی ہے۔ جسم خلیوں کی تقسیم کو قابو میں رکھتا ہے جس سے نئے خلیے تب ہی پیدا ہوتے ہیں جب ان کی ضرورت ہوتی ہے۔ اس نظام میں نقص کی وجہ سے خلیوں کی تقسیم بے قابو ہو جاتی ہیں۔ خلیوں کی بے قابو تقسیم سے ہجوم یا مادہ بن جاتا ہے۔ اسے رسولی (Tumor) کہتے ہیں۔',
           'سرطان په ټولو ناروغیو کې تر ټولو خطرناکه او وژونکې ناروغي ده. دا ناروغي د بدن د ځینو حجرو له بې‌کنټروله وېش رامنځته کېږي. بدن د حجرو وېش تر کنټرول لاندې ساتي چې له امله یې نوې حجرې یوازې هغه وخت پیدا کېږي چې اړتیا ورته وي. په دې نظام کې د نیمګړتیا له امله د حجرو وېش بې‌کنټروله کېږي. د حجرو له بې‌کنټروله وېش یوه ګڼه یا ماده جوړېږي. دې ته غوټه (Tumor) ویل کېږي.'),
          ('When this tumour (Tumor) is very malignant, it is called cancer. This tumour can be removed so that it does not reach the remaining parts of the body. If it starts to grow, it mixes into the blood and reaches other parts of the body. The process of the spreading of the tumour (Tumor) is called metastasis (Metastasis). Lung cancer too is the result of metastasis (Metastasis). This cancer is fatal and dangerous to life. Its treatment is very difficult because lung cancer can spread to any part or organ of the body, especially …',
           'یہ رسولی (Tumor) بہت مہلک ہوتی ہے، اسے کینسر کہتے ہیں۔ اس رسولی (Tumor) کو ہٹایا جا سکتا ہے تاکہ جسم کے باقی حصوں تک نہ پہنچ پائے۔ اگر یہ بڑھنے لگے تو یہ خون میں شامل ہو کر جسم کے دوسرے حصوں تک پہنچ جاتی ہیں۔ رسولی (Tumor) کے پھیلنے کے عمل کو میٹاسٹیسس (Metastasis) کہتے ہیں۔ پھیپھڑوں کا کینسر بھی میٹاسٹیسس (Metastasis) کا نتیجہ ہوتا ہے۔ یہ کینسر زندگی کیلئے مہلک اور خطرناک ہے۔ اس کا علاج بہت مشکل ہے کیونکہ پھیپھڑوں کا کینسر جسم کے کسی بھی حصے یا عضو میں پھیل سکتا ہے خاص کر …',
           'کله چې دا غوټه (Tumor) ډېره وژونکې وي، سرطان ورته ویل کېږي. دا غوټه لرې کېدای شي ترڅو د بدن نورو برخو ته ونه رسېږي. که لویېدل پیل کړي، په وینه کې ګډېږي او د بدن نورو برخو ته رسېږي. د غوټې (Tumor) د خپرېدو عمل ته میټاسټېسس (Metastasis) ویل کېږي. د سږو سرطان هم د میټاسټېسس (Metastasis) پایله وي. دا سرطان ژوند ته وژونکی او خطرناک دی. درملنه یې ډېره ستونزمنه ده، ځکه د سږو سرطان د بدن هرې برخې یا غړي ته خپرېدای شي، په ځانګړې توګه …')])
    r = rec(b, 1, 1, 6, first=True)
    BOOK.save(6, [(1, r)], issues=[{'id': 'hpe12-pdf006', 'unit': 1, 'printedPage': 1,
               'description': '“خلیوں کی تقسیم بے قابو ہو جاتی ہیں”, “یہ خون میں شامل ہو کر … پہنچ جاتی ہیں”. Retained as printed.'}])


def p7():
    b = Builder()
    P(b, [('… the adrenal glands, liver, brain and bones. Lung cancer becomes a cause of death. This cancer is found more in people of older age. About 70% of cancer has been diagnosed in people over 65 years of age, while 30% includes people younger than 45 years.',
           'ایڈرینل غدود، جگر، دماغ اور ہڈیاں۔ پھیپھڑوں کا کینسر موت کا باعث بنتا ہے۔ یہ کینسر بڑی عمر کے افراد میں زیادہ پایا جاتا ہے۔ قریباً 70% کینسر 65 سال سے زیادہ عمر کے افراد میں تشخیص ہوئی ہے۔ جبکہ 30% میں 45 سال سے کم عمر کے افراد شامل ہیں۔',
           '… اډرینال غدې، ځیګر، دماغ او هډوکي. د سږو سرطان د مرګ لامل کېږي. دا سرطان په زړو کسانو کې ډېر موندل کېږي. نږدې ۷۰٪ سرطان له ۶۵ کلونو زیات عمر لرونکو کسانو کې تشخیص شوی، په داسې حال کې چې ۳۰٪ کې له ۴۵ کلونو کم عمر لرونکي کسان شامل دي.')])
    sv = [fig_lung_tumour(('Lung', 'Tumour', 'Lungs with a tumour (enlarged view of the tumour)')),
          fig_lung_tumour(('Lung', 'Tumour', 'پھیپھڑے اور رسولی (رسولی کا بڑا منظر)')),
          fig_lung_tumour(('Lung', 'Tumour', 'سږي او غوټه (د غوټې لوی انځور)'))]
    b.visual('hpe12-fig-lung-tumour', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Causes', 'وجوہات', 'لاملونه')
    b.h('Smoking', 'تمباکو نوشی', 'تمباکو څکول')
    P(b, [('Lung cancer was not common before 1930. After that, as smoking has been increasing, the number of patients of lung cancer too has been increasing. In different countries, especially in developing countries, the number of its patients is increasing day by day. Not only those people who are addicted to tobacco are affected by smoking, but the people living in the surrounding environment also become victims of this disease.',
           'پھیپھڑوں کا کینسر 1930 سے پہلے عام نہیں تھا۔ اس کے بعد جوں جوں تمباکو نوشی بڑھ رہی ہے ساتھ ساتھ پھیپھڑوں کے کینسر کے مریضوں کی تعداد بھی بڑھ رہی ہے۔ مختلف ممالک میں خاص کر ترقی پذیر ممالک میں اس کے مریضوں کی تعداد روز بروز بڑھ رہی ہے۔ تمباکو نوشی سے صرف وہی لوگ متاثر نہیں ہو رہے جو تمباکو کے عادی ہیں بلکہ ارد گرد کے ماحول میں رہنے والے لوگ بھی اس بیماری کا شکار ہو جاتے ہیں۔',
           'د سږو سرطان له ۱۹۳۰ مخکې عام نه و. له هغه وروسته څومره چې تمباکو څکول زیاتېږي، د سږو د سرطان د ناروغانو شمېر هم زیاتېږي. په بېلابېلو هېوادونو کې، په ځانګړې توګه په پرمختیايي هېوادونو کې، د دې ناروغانو شمېر ورځ په ورځ زیاتېږي. له تمباکو څکولو یوازې هغه خلک نه اغېزمنېږي چې د تمباکو روږدي دي، بلکې په شاوخوا چاپېریال کې اوسېدونکي خلک هم د دې ناروغۍ ښکار کېږي.'),
          ('90% of lung cancer is caused by smoking. The risk of cancer increases with the duration of cigarette smoking. Doctors give this risk a term which is called (Pack-years of smoking History). The number of cigarette packets smoked daily is multiplied by the number of years for which cigarettes have been smoked. For example, if a person has been smoking 1 packet of cigarettes daily for ten (10) years, then in a year 360 packets and in ten (10) years 3600 packets were made.',
           '90% پھیپھڑوں کے کینسر کی وجہ تمباکو نوشی ہے۔ کینسر کا خطرہ سگریٹ نوشی کے دورانیہ کے ساتھ بڑھتا جاتا ہے۔ ڈاکٹر اس خطرے کو ایک اصطلاح دیتے ہیں۔ جسے (Pack-years of smoking History) کہتے ہیں۔ جتنے سگریٹ کے پیکٹ روز نوش کیے گئے ہوں ان کو جتنے سال سگریٹ نوش کیا گیا ہو سے ضرب دیں۔ مثال کے طور پر ایک شخص روزانہ 1 پیکٹ سگریٹ کے دس (10) سال تک پیتا رہا ہے تو سال کے 360 پیکٹ اور دس (10) سال کے 3600 پیکٹ بن گئے۔',
           'د سږو د سرطان ۹۰٪ لامل تمباکو څکول دي. د سرطان خطر د سګرټ څکولو له مودې سره زیاتېږي. ډاکټران دې خطر ته یوه اصطلاح ورکوي چې (Pack-years of smoking History) ورته وايي. د سګرټو د هغو پاکټونو شمېر چې ورځنی څکول شوي، د هغو کلونو په شمېر کې ضرب کړئ چې سګرټ پکې څکول شوي. د بېلګې په توګه که یو کس هره ورځ ۱ پاکټ سګرټ لس (۱۰) کاله څکولي، نو په کال کې ۳۶۰ پاکټه او په لسو (۱۰) کلونو کې ۳۶۰۰ پاکټه شول.')])
    r = rec(b, 1, 2, 7)
    BOOK.save(7, [(1, r)], issues=[{'id': 'hpe12-pdf007', 'unit': 1, 'printedPage': 2,
               'description': 'The lung-and-tumour illustration is reproduced as a coded labelled schematic (labels Lung, Tumour as printed in English). Extensive owner ballpoint writing around the illustration (names, English words, Urdu scribbles) is excluded. “قریباً 70% کینسر … تشخیص ہوئی ہے”, “1 پیکٹ … ایک سال کے 360 پیکٹ” (360 for 365 in print). Retained as printed.'}])


def p8():
    b = Builder()
    P(b, [('It means that such people have greater risks of lung cancer. People who use more than two packets of cigarettes daily — one in seven of them goes into the mouth of death because of cancer. Smoking is also done with a pipe and cigar besides cigarettes, but these means are not as common as cigarette smoking.',
           'اس کا مطلب ہے کہ ایسے افراد میں پھیپھڑوں کے کینسر کے زیادہ خطرات ہیں۔ جو لوگ روزانہ دو یا دو سے زیادہ پیکٹ سگریٹ کے استعمال کرتے ہیں۔ ان میں سات میں سے ایک فرد کینسر کی وجہ سے موت کے منہ میں چلا جاتا ہے۔ تمباکو نوشی سگریٹ کے علاوہ پائپ اور سگار سے بھی کی جاتی ہے لیکن سگریٹ نوشی کی نسبت یہ ذرائع اتنے عام نہیں ہے۔',
           'معنا یې دا ده چې په داسې کسانو کې د سږو د سرطان ډېر خطرونه دي. هغه خلک چې هره ورځ دوه یا له دوو زیات پاکټه سګرټ کاروي، له اوو څخه یې یو د سرطان له امله د مرګ خولې ته ځي. تمباکو له سګرټو پرته په پایپ او سګار هم څکول کېږي، خو دا وسایل د سګرټ څکولو په پرتله دومره عام نه دي.')])
    sv = [fig_smoker(('non-smoker', 'smoker', 'Lungs of a non-smoker and a smoker')), fig_smoker(('non-smoker', 'smoker', 'تمباکو نوشی نہ کرنے والے اور کرنے والے کے پھیپھڑے')),
          fig_smoker(('non-smoker', 'smoker', 'د نه څکوونکي او څکوونکي سږي'))]
    b.visual('hpe12-fig-smoker-lungs', sv[0][0], sv[1][0], sv[2][0], sv[0][1])
    b.h('Air pollution', 'فضائی آلودگی', 'هوايي ککړتیا')
    P(b, [('Dangerous gases emerging from vehicles, factories and different plants mix into the air and reach the lungs through the process of breathing. 1% to 2% of lung cancer is due to breathing polluted air. According to experts, the risk of lung cancer is greater in those who live and breathe in polluted air for a long time.',
           'گاڑیوں، فیکٹریوں اور مختلف پلانٹوں سے خطرناک گیس نکل کر ہوا میں شامل ہوتی ہیں جو سانس کے عمل سے پھیپھڑوں میں پہنچ جاتی ہیں۔ 1% سے 2% پھیپھڑوں کے کینسر کی وجہ آلودہ ہوا میں سانس لینا ہے۔ ماہرین کے مطابق لمبے عرصے کیلئے آلودہ فضا میں رہنے اور سانس لینے والوں میں پھیپھڑوں کے کینسر کا خطرہ زیادہ ہوتا ہے۔',
           'له موټرو، فابریکو او بېلابېلو فابریکو خطرناکې ګازې وځي او په هوا کې ګډېږي چې د ساه اخیستو په عمل سږو ته رسېږي. د سږو د سرطان ۱٪ تر ۲٪ لامل په ککړه هوا کې ساه اخیستل دي. د متخصصینو په وینا هغو کسانو کې چې تر اوږدې مودې په ککړه فضا کې اوسېږي او ساه اخلي، د سږو د سرطان خطر ډېر وي.')])
    b.h('Passive smoking', 'پیسیو (Passive) تمباکو نوشی', 'غیر فعاله (Passive) تمباکو څکول')
    P(b, [('Such people who do not smoke but are near people who smoke — they work together, live in one room, sit together while smoking — are called Passive smokers. In this way smoke enters their lungs through breathing. In such people too the risk of lung cancer is greater.',
           'ایسے افراد جو تمباکو نوشی نہیں کرتے لیکن وہ تمباکو نوشی کرنے والے افراد کے قریب ہوتے ہیں ساتھ کام کرتے ہیں، ایک ہی کمرے میں رہتے ہیں، تمباکو نوشی کرتے وقت ساتھ بیٹھتے ہیں۔ ان کو Passive smokers کہتے ہیں۔ اس طرح دھواں سانس کے ذریعے ان کے پھیپھڑوں میں داخل ہوتا ہے۔ ایسے افراد میں بھی پھیپھڑوں کے کینسر کا خدشہ زیادہ ہوتا ہے۔',
           'هغه کسان چې تمباکو نه څکوي، خو د تمباکو څکوونکو کسانو ته نږدې وي — یوځای کار کوي، په یوه کوټه کې اوسي، د تمباکو څکولو پر مهال یوځای کېني — Passive smokers ورته ویل کېږي. په دې ډول لوګی د ساه له لارې د دوی سږو ته ننوځي. په داسې کسانو کې هم د سږو د سرطان خطر ډېر وي.')])
    r = rec(b, 1, 3, 8)
    deco(r, 'A cartoon of a lung with a cigarette captioned “you take my breath away!” beside the passive-smoking paragraph is decorative.')
    BOOK.save(8, [(1, r)], issues=[{'id': 'hpe12-pdf008', 'unit': 1, 'printedPage': 3,
               'description': 'The photograph of a non-smoker and a smoker with healthy and blackened lungs is reproduced as a coded schematic with the printed labels “non - smoker” and “smoker”. “یہ ذرائع اتنے عام نہیں ہے”, “خطرناک گیس نکل کر ہوا میں شامل ہوتی ہیں”. Retained as printed.'}])


def p9():
    b = Builder()
    b.h('Asbestos fibers', 'ایسبیسٹوس فائبرز (Asbestos fibers)', 'اسبسټوس فایبرونه (Asbestos fibers)')
    P(b, [('This is a fibrous mineral metal. People who work in the asbestos (Asbestos) industry have chances of lung cancer. These people do not smoke, but because of asbestos (Asbestos) they become afflicted with cancer. If people working in this industry also smoke cigarettes, then in these people there is a risk of cancer growing quickly.',
           'یہ ریشہ دار معدنی دھات ہے جو لوگ ایسبیسٹوس (Asbestos) کی صنعت میں کام کرتے ہیں ان میں پھیپھڑوں کے کینسر کے امکانات ہوتے ہیں۔ یہ لوگ تمباکو نوشی نہیں کرتے لیکن ایسبیسٹوس (Asbestos) کی وجہ سے کینسر میں مبتلا ہو جاتے ہیں۔ اگر اس کی صنعت میں کام کرنے والے افراد سگریٹ نوشی بھی کریں تو ان افراد میں اور تیزی سے کینسر بڑھنے کا خطرہ ہوتا ہے۔',
           'دا تار لرونکی کاني فلز دی. هغه خلک چې د اسبسټوس (Asbestos) په صنعت کې کار کوي، په دوی کې د سږو د سرطان امکانات وي. دا خلک تمباکو نه څکوي، خو د اسبسټوس (Asbestos) له امله په سرطان اخته کېږي. که د دې صنعت کارکوونکي سګرټ هم وڅکوي، نو په دوی کې د سرطان د چټکې ودې خطر وي.')])
    b.h('Radon Gas', 'ریڈون گیس (Radon Gas)', 'رېډون ګاز (Radon Gas)')
    P(b, [('This gas is a product of uranium. This gas too becomes a cause of lung cancer. According to a careful estimate, the cause of cancer of 12% of people is radon gas. In America 21000 people annually become victims of death because of this poisonous gas.',
           'یہ گیس یورینیم کی پیداوار ہے۔ یہ گیس بھی پھیپھڑوں کے کینسر کا سبب بنتی ہے۔ ایک محتاط اندازے کے مطابق 12% افراد کے کینسر کا سبب ریڈون گیس ہے۔ امریکہ میں 21000 افراد سالانہ اس زہریلی گیس کی وجہ سے موت کا شکار ہو جاتے ہیں۔',
           'دا ګاز د یورانیم محصول دی. دا ګاز هم د سږو د سرطان لامل کېږي. د یوه محتاط اټکل له مخې د ۱۲٪ کسانو د سرطان لامل رېډون ګاز دی. په امریکا کې هر کال ۲۱۰۰۰ کسان د دې زهرجن ګاز له امله مري.')])
    b.h('Symptoms of lung cancer', 'پھیپھڑوں کے کینسر کی علامات', 'د سږو د سرطان نښې')
    P(b, [('In the early stages of this cancer there are no clear symptoms. When about 40 percent of people afflicted with this disease are diagnosed, it comes to be known that the disease has spread. If the following symptoms appear, then consult a doctor.',
           'اس کینسر کی ابتدائی مراحل میں واضح علامات نہیں ہوتی۔ اس مرض میں مبتلا تقریباً 40 فیصد افراد کی جب تشخیص ہوتی ہے تو پتہ چلتا ہے کہ یہ بیماری پھیل چکی ہے۔ اگر مندرجہ ذیل علامات ظاہر ہوں تو ڈاکٹر سے رجوع کریں۔',
           'د دې سرطان په لومړنیو پړاوونو کې روښانه نښې نه وي. کله چې په دې ناروغۍ اخته نږدې ۴۰ سلنه کسان تشخیص شي، معلومېږي چې ناروغي خپره شوې ده. که لاندې نښې ښکاره شي، ډاکټر ته مراجعه وکړئ.')])
    b.h('Cough that does not end', 'نہ ختم ہونے والی کھانسی', 'نه ختمېدونکې ټوخی')
    P(b, [('A cough which is due to a cold or a problem in the process of breathing ends in one or two weeks, but a cough which continues for a long time may be due to lung cancer; therefore a doctor should be consulted immediately.',
           'ایسی کھانسی جو سردی یا سانس کے عمل میں مسئلے کی وجہ سے ہو، وہ ہفتہ یا دو ہفتہ میں ختم ہو جاتی ہے لیکن جو کھانسی لمبے عرصے سے جاری ہو تو اس کی وجہ سے پھیپھڑوں کا کینسر ہو سکتا ہے اس لیے فوراً ڈاکٹر سے رجوع کرنا چاہیے۔',
           'هغه ټوخی چې د یخنۍ یا د ساه اخیستو په عمل کې د ستونزې له امله وي، په یوه یا دوو اونیو کې ختمېږي، خو هغه ټوخی چې تر اوږدې مودې روان وي، لامل یې د سږو سرطان کېدای شي، نو سمدستي ډاکټر ته مراجعه پکار ده.')])
    r = rec(b, 1, 4, 9)
    deco(r, 'A coloured drawing of a coughing boy beside the cough paragraph is decorative.')
    BOOK.save(9, [(1, r)], issues=[{'id': 'hpe12-pdf009', 'unit': 1, 'printedPage': 4,
               'description': '“اس کینسر کی ابتدائی مراحل میں واضح علامات نہیں ہوتی”; Asbestos described as “ریشہ دار معدنی دھات”; the cough paragraph “جو کھانسی لمبے عرصے سے جاری ہو تو اس کی وجہ سے پھیپھڑوں کا کینسر ہو سکتا ہے”. Retained as printed.'}])


def p10():
    b = Builder()
    b.h('Change in cough', 'کھانسی میں تبدیلی', 'په ټوخي کې بدلون')
    P(b, [('If there is a change in an old cough — it is mostly a persistent cough, during coughing a deep and heavy sound is produced, there is more than usual coughing, or blood and phlegm are coming with the cough — then consult a doctor. If in the family or among friends someone has the same problem, advise them too to consult a doctor as soon as possible.',
           'اگر پرانی کھانسی میں تبدیلی ہو، اکثر و بیشتر کھانسی ہو، کھانسی کے دوران گہری اور بھاری آواز پیدا ہو، معمول سے ہٹ کر کھانسی سے خون اور بلغم آ رہا ہو تو ڈاکٹر سے رجوع کریں۔ اگر خاندان میں یا دوستوں کو بھی ایسا ہی مسئلہ ہو تو ان کو بھی مشورہ دیں کہ جلد از جلد ڈاکٹر سے رجوع کریں۔',
           'که په زاړه ټوخي کې بدلون راشي، ډېری وخت ټوخی وي، د ټوخي پر مهال ژور او دروند غږ پیدا شي، له معمول بهر له ټوخي سره وینه او بلغم راځي، ډاکټر ته مراجعه وکړئ. که په کورنۍ یا ملګرو کې هم چا ته همداسې ستونزه وي، هغوی ته هم مشوره ورکړئ چې ژر تر ژره ډاکټر ته مراجعه وکړي.')])
    b.h('Change in the process of breathing', 'سانس کے عمل میں تبدیلی', 'د ساه اخیستو په عمل کې بدلون')
    P(b, [('Change in the process of breathing, i.e. difficulty arises in taking breath, because cancer is blocking the path of breath or a tumour is forming in the chest. If during work, while climbing stairs, the process of breathing is happening with difficulty, then do not ignore it.',
           'سانس کے عمل میں تبدیلی یعنی سانس لینے میں دشواری پیش آ رہی ہوتی ہے کیونکہ کینسر سانس کے راستے کو بلاک یا تنگ کر رہا ہوتا ہے یا چھاتی میں رسولی بن رہی ہوتی ہے۔ اگر کام کے دوران، سیڑھیاں چڑھتے ہوئے تکلیف سے سانس کا عمل ہو رہا ہو تو اس کو نظر انداز نہ کریں۔',
           'د ساه اخیستو په عمل کې بدلون، یعنې په ساه اخیستو کې ستونزه پېښېږي، ځکه سرطان د ساه لاره بندوي یا تنګوي یا په سینه کې غوټه جوړېږي. که د کار پر مهال، د زینو د ختلو پر وخت په تکلیف ساه اخیستل کېږي، له پامه یې مه غورځوئ.')])
    b.h('Pain in the chest', 'چھاتی میں درد', 'په سینه کې درد')
    P(b, [('Through lung cancer there is pain in the chest, shoulders and back. When pain begins in the chest, shoulders or back, then consult a doctor.',
           'پھیپھڑوں کے کینسر سے چھاتی، کندھے اور کمر میں درد ہوتا ہے۔ جب چھاتی کندھے یا کمر میں درد ہونا شروع ہو تو ڈاکٹر سے رجوع کریں۔',
           'د سږو له سرطان په سینه، اوږو او ملا کې درد کېږي. کله چې په سینه، اوږو یا ملا کې درد پیل شي، ډاکټر ته مراجعه وکړئ.')])
    b.h('Headache', 'سردرد', 'سر درد')
    P(b, [('Headache is a sign of cancer spreading to the brain. But not all headaches are due to Metastasis in the brain. Sometimes the pressure of the lung tumour is on the superior vena cava. This is a large vein which brings dirty blood from the upper parts of the body towards the heart. Because of this pressure there is headache.',
           'سردرد کینسر کے دماغ تک پھیلنے کی نشانی ہے۔ لیکن سارے سردرد دماغ میں Metastasis کی وجہ سے نہیں ہوتے۔ بعض دفعہ پھیپھڑوں کی رسولی کا دباؤ بالائی وینا کیوا پر ہوتا ہے۔ یہ بڑی ورید ہے جو جسم کے بالائی حصوں سے گندا خون دل کی طرف لاتی ہے۔ اس دباؤ کی وجہ سے سردرد ہوتا ہے۔',
           'سر درد دماغ ته د سرطان د خپرېدو نښه ده. خو ټول سر دردونه په دماغ کې د Metastasis له امله نه وي. کله کله د سږو د غوټې فشار پر پورتنۍ وینا کاوا وي. دا لویه وریده ده چې د بدن له پورتنیو برخو ناپاکه وینه زړه ته راوړي. د دې فشار له امله سر درد کېږي.')])
    r = rec(b, 1, 5, 10)
    BOOK.save(10, [(1, r)], issues=[{'id': 'hpe12-pdf010', 'unit': 1, 'printedPage': 5,
               'description': 'Owner pen strokes across the breathing paragraph are excluded. “بالائی وینا کیوا” (superior vena cava). Retained as printed.'}])


def p11():
    b = Builder()
    b.h('Cardiac Diseases', 'امراضِ قلب (Cardiac Diseases)', 'د زړه ناروغۍ (Cardiac Diseases)')
    P(b, [('Like other diseases, heart diseases too have always been connected with human life, but in the present age the rate of heart diseases in humans adopting a modern but unnatural way of life is as high today as perhaps never before in human history. In the following lines the causes and symptoms of heart diseases are being mentioned in detail.',
           'دوسری بیماریوں کی طرح امراضِ قلب کا بھی انسانی حیات کے ساتھ ہمیشہ سے تعلق رہا ہے مگر عصرِ حاضر کے جدید مگر غیر فطری طرزِ حیات کو اپنانے والے انسانوں میں امراضِ قلب کی شرح جس قدر آج بلند ہے شاید انسانی تاریخ میں پہلے کبھی نہ تھی۔ ذیل کے سطور میں تفصیل کے ساتھ امراضِ قلب کی وجوہات اور علامات کا تذکرہ کیا جا رہا ہے۔',
           'د نورو ناروغیو په څېر د زړه ناروغۍ هم تل له انساني ژوند سره تړلې پاتې شوې، خو په اوسني عصر کې د نوي خو غیر طبیعي ژوند طرز غوره کوونکو انسانانو کې د زړه د ناروغیو کچه نن هومره لوړه ده چې ښايي د انسان په تاریخ کې مخکې هېڅکله نه وه. په لاندې کرښو کې د زړه د ناروغیو لاملونه او نښې په تفصیل یادېږي.')])
    b.h('Important causes', 'اہم وجوہات', 'مهم لاملونه')
    L(b, [('Obesity and eating more than needed.', 'موٹاپا اور ضرورت سے زیادہ کھانا۔', 'چاغښت او له اړتیا زیات خوړل.'),
          ('Hereditary causes.', 'موروثی اسباب۔', 'میراثي لاملونه.'),
          ('Congenital defects.', 'پیدائشی طور پر نقائص۔', 'زېږنیزې نیمګړتیاوې.'),
          ('Fat forming a layer on the inner surface of the arteries and creating an obstruction in the passage of blood.', 'رگوں کی اندرونی سطح پر چربی کی تہہ بن کر خون کے گزرنے میں رکاوٹ پیدا کرنا۔', 'د رګونو پر داخلي سطحه د غوړ پوړ جوړېدل او د وینې په تېرېدو کې خنډ پیدا کول.'),
          ('Cholesterol increasing in the blood and thickening it.', 'خون میں کولیسٹرول بڑھ کر گاڑھا ہونا۔', 'په وینه کې د کولسټرول زیاتېدل او ټینګېدل.'),
          ('High blood pressure (High-B.P).', 'بلند فشارِ خون (High-B.P)۔', 'لوړ فشار (High-B.P).'),
          ('Use of tobacco.', 'تمباکو کا استعمال۔', 'د تمباکو کارول.'),
          ('Use of alcohol and other intoxicants.', 'شراب و دیگر منشیات کا استعمال۔', 'د شرابو او نورو نشه‌يي توکو کارول.'),
          ('Mental pressure and nervous tension.', 'ذہنی دباؤ اور اعصابی تناؤ۔', 'رواني فشار او عصبي کشش.'),
          ('Social injustice and the economic and psychological problems arising from it too are counted as an important cause of heart diseases.', 'معاشرتی ناانصافی اور اس کی وجہ سے پیدا ہونے والے معاشی اور نفسیاتی مسائل بھی امراضِ قلب میں ایک اہم وجہ شمار ہوتے ہیں۔', 'ټولنیزه بې‌عدالتي او له امله یې پیدا شوې اقتصادي او رواني ستونزې هم د زړه د ناروغیو یو مهم لامل ګڼل کېږي.')])
    r = rec(b, 1, 6, 11)
    deco(r, 'A photograph of a heart against an ECG grid, and a drawing of a heart wrapped in a cigarette, are decorative.')
    BOOK.save(11, [(1, r)], issues=[{'id': 'hpe12-pdf011', 'unit': 1, 'printedPage': 6,
               'description': 'Owner ballpoint names and doodles (birds, scribbles) in the left margin are excluded. “ذیل کے سطور”. Retained as printed.'}])


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    {6: p6, 7: p7, 8: p8, 9: p9, 10: p10, 11: p11}[n]()
