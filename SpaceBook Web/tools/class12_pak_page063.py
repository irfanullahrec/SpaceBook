"""Pak Studies XII PDF63 (spread): p.115 Ch.5 مشق Q3(iv)–(vii) (chapter 5 complete); p.116 Chapter 6 opening — definition and importance of culture."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
e = Builder()
e.group('lines', [
 ('(iv) Throw light on the Islamic background of good governance.', '(iv) بہتر اسلوبِ حکمرانی کے اسلامی پس منظر پر روشنی ڈالیں۔', '(iv) د ښې حکومتولۍ پر اسلامي شالید رڼا واچوئ.'),
 ('(v) Discuss the status and powers of the Prime Minister according to the Pakistani constitution.', '(v) پاکستانی آئین کے مطابق وزیرِ اعظم کی حیثیت اور اختیارات کے بارے میں بحث کریں۔', '(v) د پاکستان د اساسي قانون له مخې د لومړي وزیر د حیثیت او واکونو په اړه بحث وکړئ.'),
 ('(vi) What are the obstacles in the way of good governance in Pakistan?', '(vi) پاکستان میں بہتر اسلوبِ حکمرانی کی راہ میں کون سی رکاوٹیں ہیں؟', '(vi) په پاکستان کې د ښې حکومتولۍ په لاره کې کوم خنډونه دي؟'),
 ('(vii) What measures are necessary for good governance?', '(vii) بہتر اسلوبِ حکمرانی کے لیے کیا اقدامات ضروری ہیں؟', '(vii) د ښې حکومتولۍ لپاره کوم ګامونه اړین دي؟')])
ex = BOOK.record(e, 'pak12-ch5-exercise-2', 'Exercise (2)', 'مشق (۲)', 'تمرین (۲)', 63, [115])

t = Builder()
P = t.p
P('Chapter Six', 'بابِ ششم', 'شپږم څپرکی')
t.h('Culture of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کی ثقافت (کلچر)', 'د پاکستان اسلامي جمهوریت کلتور')
t.h('Definition of culture', 'ثقافت کی تعریف', 'د کلتور تعریف')
P('The importance of culture cannot be denied. The existence of human society and its progress rest on the foundation of culture. Culture is that fundamental thing by which we distinguish between man and animal. Various sociologists have defined culture from their own points of view as follows.',
  'ثقافت کی اہمیت سے انکار ممکن نہیں۔ انسانی معاشرے کا وجود اور اُس کی ترقی ثقافت کی بنیاد پر ہوتی ہے۔ ثقافت ہی وہ بنیادی شے ہے جس سے ہم انسان اور حیوان میں تمیز کرتے ہیں۔ مختلف ماہرینِ عمرانیات نے اپنے اپنے نقطۂ نظر سے ثقافت کی تعریفیں یوں کی ہیں۔',
  'د کلتور له اهمیته انکار نه شي کېدای. د انساني ټولنې شتون او پرمختګ یې د کلتور پر بنسټ وي. کلتور هماغه بنسټیز شی دی چې پرې موږ د انسان او حیوان ترمنځ توپیر کوو. بېلابېلو ټولنپوهانو له خپل خپل نظره د کلتور تعریفونه داسې کړي:')
P('Lenin says: “Culture is a social heritage which keeps being transferred from one generation to another generation through individual and collective experiences.”',
  'لینین کہتے ہیں۔ ’’ثقافت ایک معاشرتی ورثہ ہے جو ایک نسل سے دوسری نسل کو انفرادی اور اجتماعی تجربات سے منتقل ہوتا رہتا ہے۔‘‘',
  'لېنن وايي: "کلتور یو ټولنیز میراث دی چې له یوه نسل بل نسل ته د فردي او ټولیزو تجربو له لارې لېږدول کېږي."')
P('Tylor says: “By culture are meant all those forms — knowledge, belief, art, morals, law, custom and other capabilities and habits — which are acquired from society over a long time.”',
  'ٹیلر کہتے ہیں۔ ’’ثقافت سے مراد وہ تمام اشکال ہیں جو علم، عقیدے، فن، اخلاق، قانون، دستور اور دوسری صلاحیتوں اور عادات سے معاشرے کو ایک طویل وقت میں حاصل ہوتی ہیں۔‘‘',
  'ټېلر وايي: "له کلتور څخه مراد هغه ټولې بڼې دي چې د علم، عقیدې، هنر، اخلاقو، قانون، دود او نورو وړتیاوو او عادتونو څخه ټولنې ته په اوږده موده کې ترلاسه کېږي."')
P('Keeping the above definitions in view we can reach this conclusion: culture is an outline, model and method of the various activities occurring in life on which society acts and which it transfers from one generation to another.',
  'مندرجہ بالا تعریفوں کو مدِنظر رکھتے ہوئے ہم اس نتیجے پر پہنچ سکتے ہیں کہ ثقافت زندگی میں پیش آمدہ مختلف سرگرمیوں کا ایک خاکہ، نمونہ اور طریقہ ہے جس پر معاشرہ عمل پیرا ہوتا ہے اور اسے ایک سے دوسری نسل کو منتقل کرتا ہے۔',
  'د پورته تعریفونو په پام کې نیولو سره موږ دې پایلې ته رسېدای شو چې کلتور په ژوند کې د پېښېدونکو بېلابېلو فعالیتونو یو خاکه، بېلګه او طریقه ده چې ټولنه پرې عمل کوي او له یوه نسل یې بل ته لېږدوي.')
P('Culture is not individual but a collective act. Collective human behaviour and the whole of its daily life we can call culture. That is why the inhabitants of various regions of the world possess similar attitudes, morals and general dealings.',
  'ثقافت انفرادی نہیں بلکہ ایک اجتماعی عمل ہے۔ اجتماعی انسانی برتاؤ اور اس کی روزمرہ زندگی کو ایک مجموعے کی شکل میں ہم ثقافت کہہ سکتے ہیں۔ اس لیے دُنیا کے مختلف خطوں میں وہاں کے باسی ایک جیسے رویوں، اُخلاق اور عمومی معاملات کے مالک ہوتے ہیں۔',
  'کلتور فردي نه، بلکې ټولیز عمل دی. ټولیز انساني چلند او د هغه ورځنی ژوند د یوې مجموعې په بڼه کلتور بللی شو. له همدې امله د نړۍ په بېلابېلو سیمو کې هلته اوسېدونکي ورته چلندونه، اخلاق او عمومي چارې لري.')
t.h('Importance of culture', 'ثقافت کی اہمیت', 'د کلتور اهمیت')
P('Individuals obtain most of the cultural values of society by inheritance from their forefathers, they themselves devise some according to new needs, and some they borrow from other societies. Culture is evolutionary',
  'معاشرے کی زیادہ تر ثقافتی اقدار، افراد اپنے آباؤ اجداد سے وراثت میں پاتے ہیں، کچھ جدید ضروریات کے مطابق خود وضع کر لیتے ہیں اور کچھ دوسرے معاشروں سے مستعار لیتے ہیں۔ ثقافت ارتقا پذیر',
  'د ټولنې ډېری کلتوري ارزښتونه کسان له خپلو نیکونو په میراث کې ترلاسه کوي، ځینې د نویو اړتیاوو سره سم پخپله جوړوي، او ځینې له نورو ټولنو پور اخلي. کلتور د ودې وړ')
UT = ('Culture of the Islamic Republic of Pakistan', 'اسلامی جمہوریہ پاکستان کی ثقافت (کلچر)', 'د پاکستان اسلامي جمهوریت کلتور')
tx = BOOK.record(t, 'pak12-ch6-text-1', 'Chapter 6 text (1)', 'بابِ ششم — متن (۱)', 'شپږم څپرکی — متن (۱)', 63, [116], unit_title=UT)
tx['sourceNote'] = 'The importance-of-culture paragraph breaks mid-sentence at the foot of p.116 and continues on p.117 (PDF64).'
issues = [{'id': 'pak12-pdf063', 'unit': 6, 'printedPage': 116,
           'description': 'p.116 attributes the first definition of culture to “لینین” (Lenin); the classic “social heritage” definition is usually credited to Linton/Malinowski — retained as printed. Faint show-through of p.114 visible on p.115 is not content. The printed page number on p.115 is partly obscured.'}]

if __name__ == '__main__':
    BOOK.save(63, [(5, ex), (6, tx)], issues=issues, complete_units=[5])
