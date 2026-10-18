"""Pak Studies XII PDF60 (spread): printed pp.109–110 — Ch.5 institutions for good governance; obstacles (education, planning, parties, federal deviation, extremism, rule of law); remedies intro."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
P('To make better governance effective, the following institutions have so far been established:',
  'بہتر اسلوبِ حکمرانی کو مؤثر بنانے کے لیے تاحال مندرجہ ذیل ادارے قائم کیے گئے ہیں۔',
  'د ښې حکومتولۍ د اغېزمنې کولو لپاره تر اوسه لاندې ادارې جوړې شوې:')
t.group('lines', [('1. National Security Council', '1۔ قومی سلامتی کونسل', '۱. د ملي امنیت شورا'), ('2. Federal Cabinet', '2۔ وفاقی کابینہ', '۲. فدرالي کابینه'),
                  ('3. Provincial Governors', '3۔ صوبائی گورنر', '۳. ولایتي والیان'), ('4. Provincial Cabinets', '4۔ صوبائی کابینہ', '۴. ولایتي کابینې'),
                  ('5. National Reconstruction Bureau', '5۔ قومی تعمیرِ نو بیورو', '۵. د ملي بیارغونې اداره'), ('6. National Accountability Bureau', '6۔ قومی احتساب بیورو', '۶. د ملي حساب‌ورکونې اداره'),
                  ('7. National Monitoring System', '7۔ قومی نظام نگرانی', '۷. ملي څارنیز نظام'), ('8. National Command Authority', '8۔ نیشنل کمانڈ اتھارٹی', '۸. نېشنل کمانډ اتهارټي')])
H('Obstacles in the way of good governance and reform', 'بہتر اسلوبِ حکمرانی کی راہ میں درپیش رکاوٹیں اور اصلاح', 'د ښې حکومتولۍ په لاره کې خنډونه او اصلاح')
P('In Pakistan the following obstacles stand in the way of good governance.',
  'پاکستان میں بہتر اسلوبِ حکمرانی کی راہ میں مندرجہ ذیل رکاوٹیں درپیش ہیں۔',
  'په پاکستان کې د ښې حکومتولۍ په لاره کې لاندې خنډونه شته.')
H('Lack of education', 'تعلیم کی کمی', 'د زده‌کړې کمښت')
P('Even after so much time has passed since independence, there is a lack of education in Pakistan, because of which political, economic and social problems are increasing day by day. According to the latest Economic Survey, 58% of people in Pakistan are literate. This rate is very low by international standards.',
  'آزادی کے بعد اتنا عرصہ گزرنے کے باوجود بھی پاکستان میں تعلیم کی کمی ہے۔ جس کی وجہ سے سیاسی، اقتصادی اور معاشرتی مسائل میں روز بروز اضافہ ہو رہا ہے۔ آخری معاشی جائزے (Economic Survey) کے مطابق پاکستان میں 58% لوگ خواندہ ہیں۔ یہ شرح بین الاقوامی اصولوں کے مطابق بہت کم ہے۔',
  'له خپلواکۍ وروسته د دومره وخت تېرېدو سره سره په پاکستان کې د زده‌کړې کمښت دی، چې له امله یې سیاسي، اقتصادي او ټولنیزې ستونزې ورځ تر بلې زیاتېږي. د وروستي اقتصادي سروې (Economic Survey) له مخې په پاکستان کې ۵۸٪ خلک لوستي دي. دا کچه د نړیوالو معیارونو له مخې ډېره ټیټه ده.')
H('Absence of standard planning', 'معیاری منصوبہ بندی کا فقدان', 'د معیاري پلان جوړونې نشتوالی')
P('In Pakistan not only have experiments been taking place in the field of politics, but economic planning here has also been defective. Its effect fell on both the people and the rulers, as a result of which the concept of the welfare state faded.',
  'پاکستان میں نہ صرف سیاست کے میدان میں تجربات ہوتے رہے ہیں بلکہ یہاں معاشی منصوبہ بندی بھی ناقص رہی ہے۔ جس کا اثر عوام اور حکمرانوں دونوں پر پڑا۔ جس کے نتیجے میں فلاحی ریاست کا تصور ماند پڑ گیا۔',
  'په پاکستان کې نه یوازې د سیاست په ډګر کې تجربې شوې، بلکې دلته اقتصادي پلان جوړونه هم نیمګړې وه. اغېز یې پر خلکو او واکمنانو دواړو ولوېد، چې په پایله کې یې د هوساینې دولت تصور کمرنګه شو.')
H('Increase in the number of parties', 'پارٹیوں کی تعداد میں اضافہ', 'د ګوندونو په شمېر کې زیاتوالی')
P('In Pakistan not only is the number of political parties increasing day by day, but the old parties too have fallen victim to break-up for various reasons. Political leaders do not take interest in solving the problems of the people, the consequence of which all the people have to suffer.',
  'پاکستان میں نہ صرف سیاسی پارٹیوں کی تعداد میں دن بدن اضافہ ہو رہا ہے بلکہ پرانی پارٹیاں بھی مختلف وجوہات کی بناء پر ٹوٹ پھوٹ کا شکار ہیں۔ سیاسی لیڈر عوام کے مسائل حل کرنے میں دلچسپی نہیں لیتے، جس کا نتیجہ تمام عوام کو بھگتنا پڑتا ہے۔',
  'په پاکستان کې نه یوازې د سیاسي ګوندونو شمېر ورځ تر بلې زیاتېږي، بلکې زاړه ګوندونه هم د بېلابېلو لاملونو له امله د ماتېدو ښکار دي. سیاسي مشران د خلکو د ستونزو په حل کې لېوالتیا نه ښيي، چې پایله یې ټول خلک ګالي.')
H('Deviation from federal principles', 'وفاقی اصولوں سے انحراف', 'له فدرالي اصولو انحراف')
P('Pakistan is a federal state, but the ruling class kept deviating from federal principles according to the constitution, and instead of making federal democratic principles effective and active, every ruler kept using the constitution and the government for his own political and personal purposes, because of which an atmosphere of chaos kept arising in the country.',
  'پاکستان ایک وفاقی مملکت ہے لیکن حکمران طبقہ آئین کے مطابق وفاقی اصولوں سے انحراف کرتا رہا اور بجائے وفاقی جمہوری اصولوں کو مؤثر اور فعال بنانے کے ہر حکمران اپنے سیاسی اور ذاتی مقاصد کے لیے آئین اور حکومت کو استعمال کرتا رہا۔ جس سے ملک میں افراتفری کی فضا پیدا ہوتی رہی۔',
  'پاکستان یو فدرالي دولت دی، خو واکمنې طبقې د اساسي قانون سره سم له فدرالي اصولو انحراف کاوه، او د فدرالي ولسواکو اصولو د اغېزمن او فعال کولو پر ځای هر واکمن اساسي قانون او حکومت د خپلو سیاسي او شخصي موخو لپاره کاراوه، چې له امله یې په هېواد کې د ګډوډۍ فضا پیدا کېده.')
H('Religious extremism', 'مذہبی انتہا پسندی', 'مذهبي افراطیت')
P('For some time religious extremism has been increasing in Pakistan, because of which sectarianism has taken hold. Because of all these things the country kept growing weaker politically and economically.',
  'پاکستان میں کچھ عرصے سے مذہبی انتہا پسندی بڑھ رہی ہے۔ جس کی وجہ سے فرقہ واریت نے زور پکڑا ہے۔ ان تمام باتوں کی وجہ سے ملک سیاسی اور معاشی طور پر کمزور ہوتا چلا گیا۔',
  'په پاکستان کې د یو څه وخت راهیسې مذهبي افراطیت زیاتېږي، چې له امله یې فرقه‌پالنې زور اخیستی. د دې ټولو خبرو له امله هېواد سیاسي او اقتصادي پلوه کمزوری کېږي.')
H('Not upholding the law', 'قانون کی پاسداری نہ کرنا', 'د قانون نه درناوی')
P('In principle all people are equal in the eyes of the law, but in our country obtaining justice and upholding the law in practice is a very difficult matter. The judicial system is extremely complex and expensive, in which there is a great waste of money and time.',
  'اصولی طور پر قانون کی نظر میں تمام لوگ یکساں ہوتے ہیں لیکن ہمارے ملک میں عملی طور پر انصاف کا حصول اور قانون کی پاسداری بڑی مشکل بات ہے۔ عدالتی نظام نہایت ہی پیچیدہ اور مہنگا ہے۔ جس میں پیسے اور وقت کا کافی ضیاع ہوتا ہے۔',
  'په اصولي ډول د قانون په نظر کې ټول خلک برابر وي، خو زموږ په هېواد کې په عمل کې د عدالت ترلاسه کول او د قانون درناوی ډېره ستونزمنه خبره ده. قضايي نظام ډېر پېچلی او ګران دی، چې پکې د پیسو او وخت ډېر ضایع کېږي.')
H('Remedy', 'تدارک', 'درملنه')
P('The following measures are necessary for good governance.',
  'بہتر اسلوبِ حکمرانی کے لیے مندرجہ ذیل اقدامات ضروری ہیں۔',
  'د ښې حکومتولۍ لپاره لاندې ګامونه اړین دي.')
rec = BOOK.record(t, 'pak12-ch5-text-13', 'Chapter 5 text (13)', 'بابِ پنجم — متن (۱۳)', 'پنځم څپرکی — متن (۱۳)', 60, [109, 110])
issues = [{'id': 'pak12-pdf060', 'unit': 5, 'printedPage': 110, 'description': 'p.110 is printed on a decorative floral border with pink heading panels (page ornament, not content); not reproduced.'}]

if __name__ == '__main__':
    BOOK.save(60, [(5, rec)], issues=issues)
