"""Pak Studies XII PDF50 (spread): printed pp.89–90 — Ch.5 National Assembly seats; judiciary (Supreme Court, High Court, Mohtasib, FSC, subordinate courts)."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
H('Lower House (National Assembly)', 'ایوانِ زیریں (قومی اسمبلی)', 'ښکته جرګه (ملي اسمبلي)')
P('The members of the National Assembly are elected for five years. The total number of its seats is 342. Their province-wise detail is as follows.',
  'قومی اسمبلی کے ممبران کو پانچ سال کے لیے منتخب کیا جاتا ہے۔ اس کی نشستوں کی کل تعداد 342 ہے۔ ان کی صوبہ وار تفصیل یوں ہے۔',
  'د ملي اسمبلۍ غړي د پنځو کلونو لپاره ټاکل کېږي. ټولې څوکۍ یې ۳۴۲ دي. ولایتي جزییات یې دا دي:')
rows = [('Province of Punjab', 'صوبہ پنجاب', 'پنجاب ولایت', '183'), ('Province of Sindh', 'صوبہ سندھ', 'سند ولایت', '75'),
        ('Province of Khyber Pakhtunkhwa (including newly merged districts)', 'صوبہ خیبر پختونخوا (بشمول نئے ضم شدہ اضلاع)', 'خیبر پښتونخوا ولایت (د نویو ګډو شویو ولسوالیو سره)', '55'),
        ('Province of Balochistan', 'صوبہ بلوچستان', 'بلوچستان ولایت', '17'), ('Federal capital', 'وفاقی دارالحکومت', 'فدرالي پلازمېنه', '2'), ('Minorities', 'اقلیتیں', 'لږکي', '10')]
t.table('pak12-na-seats', ['Unit', 'Seats'], [[r[0], r[3]] for r in rows], ['اکائی', 'نشستیں'], ['واحد', 'څوکۍ'], [[r[1], r[3]] for r in rows], [[r[2], r[3]] for r in rows])
P('The members of the Senate elect a Chairman and a Deputy Chairman from among themselves, while in the National Assembly a Speaker and a Deputy Speaker are elected.',
  'سینیٹ کے ممبران آپس میں سے ایک چیئرمین اور ایک ڈپٹی چیئرمین کا انتخاب کرتے ہیں جبکہ قومی اسمبلی میں سپیکر اور ڈپٹی سپیکر کا انتخاب کیا جاتا ہے۔',
  'د سنا غړي له خپل منځه یو رئیس او یو مرستیال رئیس ټاکي، په داسې حال کې چې په ملي اسمبلۍ کې سپیکر او مرستیال سپیکر ټاکل کېږي.')
H('Judiciary', 'عدلیہ:', 'قضا')
H('Supreme Court', 'سپریم کورٹ', 'ستره محکمه')
P('The Supreme Court has a distinguished position in the whole system of the judiciary. The Supreme Court not only interprets the constitution, but is also empowered to examine the constitutional status of the laws made by the legislature and of the orders and measures of the government. The permanent seat of the Supreme Court is in Islamabad; however, a permanent bench consisting of four members at Lahore and benches consisting of two members at Peshawar and Karachi also exist. According to the constitution the President appoints the Chief Justice of the Supreme Court, while in appointing the other judges the President consults the Chief Justice.',
  'عدلیہ کے پورے نظام میں سپریم کورٹ کو ممتاز مقام حاصل ہے۔ سپریم کورٹ نہ صرف آئین کی تشریح کرتی ہے بلکہ وہ مجلسِ قانون ساز کے بنائے ہوئے قوانین اور حکومت کے احکام اور اقدامات کی آئینی حیثیت کو جانچنے کی بھی مجاز ہے۔ سپریم کورٹ کی مستقل نشست تو اسلام آباد میں ہے۔ تاہم چار ارکان پر مشتمل ایک مستقل بنچ لاہور، دو ارکان پر مشتمل بنچ پشاور اور دو ارکان پر مشتمل بنچ کراچی میں بھی موجود ہے۔ آئین کے مطابق سپریم کورٹ کے چیف جسٹس کا تقرر صدر کرتا ہے جب کہ باقی ججوں کا تقرر کرتے وقت صدر، چیف جسٹس سے مشورہ کرتا ہے۔',
  'د قضا په ټول نظام کې سترې محکمې ته ممتاز مقام حاصل دی. ستره محکمه نه یوازې اساسي قانون تفسیروي، بلکې د قانون جوړوونکې ادارې د جوړو شویو قوانینو او د حکومت د امرونو او اقداماتو د اساسي حیثیت د ارزونې واک هم لري. د سترې محکمې دایمي ناسته په اسلام‌اباد کې ده، خو په لاهور کې د څلورو غړو یوه دایمي څانګه، او په پېښور او کراچۍ کې د دوو دوو غړو څانګې هم شته. د اساسي قانون سره سم د سترې محکمې لوی قاضي ولسمشر ټاکي، په داسې حال کې چې د نورو قاضیانو د ټاکلو پر وخت ولسمشر له لوی قاضي سره مشوره کوي.')
H('High Court', 'ہائی کورٹ', 'عالي محکمه')
P('According to the constitution of Pakistan a High Court has been established in each province. The High Court cannot be called a purely provincial court, because it is a part of the chain of the country’s judicial system. The President appoints all the judges of the High Court.',
  'پاکستان کے آئین کے مطابق ہر صوبہ میں ایک ہائی کورٹ قائم کی گئی ہے۔ ہائی کورٹ کو خالص صوبائی عدالت نہیں کہا جا سکتا کیونکہ وہ ملک کے عدالتی نظام کے سلسلہ کا ایک حصہ ہے۔ ہائی کورٹ کے تمام ججوں کا تقرر صدر کرتا ہے۔',
  'د پاکستان د اساسي قانون سره سم په هر ولایت کې یوه عالي محکمه جوړه شوې. عالي محکمې ته خالص ولایتي محکمه نه شي ویل کېدای، ځکه هغه د هېواد د قضايي نظام د لړۍ یوه برخه ده. د عالي محکمې ټول قاضیان ولسمشر ټاکي.')
H('Mohtasib-e-Aala (Ombudsman)', 'محتسبِ اعلیٰ', 'لوی محتسب')
P('For the prevention of bribery and malpractices in administration, a Mohtasib-e-Aala has been appointed at the federal level, while they have also been established at the provincial level.',
  'نظم و نسق میں رشوت ستانی اور دھاندلیوں کے تدارک کی خاطر وفاقی سطح پر محتسبِ اعلیٰ مقرر ہے، جب کہ صوبائی سطح پر بھی ان کا قیام عمل میں لایا گیا ہے۔',
  'په ادارې کې د بډو او درغلیو د مخنیوي لپاره په فدرالي کچه لوی محتسب ټاکل شوی، په داسې حال کې چې په ولایتي کچه هم جوړ شوي.')
H('Federal Shariat Court', 'وفاقی شرعی عدالت', 'فدرالي شرعي محکمه')
P('The President of Pakistan himself appoints the judges of the Federal Shariat Court. The term of the Chief Justice and the other judges is three years, but the President of Pakistan can reappoint them. The Federal Shariat Court reviews laws contrary to Islam.',
  'وفاقی شرعی عدالت کے ججوں کا تقرر صدرِ پاکستان خود کرتا ہے۔ چیف جسٹس اور دوسرے جج صاحبان کی میعاد تین سال ہے لیکن صدرِ پاکستان ان کی دوبارہ تقرری کر سکتا ہے۔ وفاقی شرعی عدالت اسلام کے منافی قوانین پر نظرِ ثانی کرتی ہے۔',
  'د فدرالي شرعي محکمې قاضیان د پاکستان ولسمشر پخپله ټاکي. د لوی قاضي او نورو قاضیانو موده درې کاله ده، خو د پاکستان ولسمشر یې بیا ټاکلی شي. فدرالي شرعي محکمه د اسلام خلاف قوانینو بیا کتنه کوي.')
H('Subordinate courts', 'ماتحت عدالتیں', 'ښکته محکمې')
P('In Pakistan separate courts have been established for civil and criminal cases, e.g. District and Sessions Courts, criminal courts, civil courts, revenue courts, executive courts and tribunals etc.',
  'پاکستان میں دیوانی اور فوجداری مقدمات کے لیے الگ الگ عدالتیں قائم ہیں۔ مثلاً ڈسٹرکٹ اینڈ سیشن کورٹ، فوجداری عدالتیں، دیوانی عدالتیں، مالگزاری عدالتیں، انتظامی عدالتیں اور ٹربیونل وغیرہ وغیرہ۔',
  'په پاکستان کې د مدني او جزايي قضیو لپاره جلا جلا محکمې جوړې دي؛ لکه د ولسوالۍ او سیشن محکمه، جزايي محکمې، مدني محکمې، د مالیې محکمې، اداري محکمې او ټربیونلونه او نور.')
rec = BOOK.record(t, 'pak12-ch5-text-3', 'Chapter 5 text (3)', 'بابِ پنجم — متن (۳)', 'پنځم څپرکی — متن (۳)', 50, [89, 90])
rec['sourceNote'] = 'Rows 4–8 of the Senate seat table at the top of p.89 are recorded with the table in PDF49. The National Assembly seat list is printed as a two-column list and is given as a structured table; the printed province figures (183+75+55+17+2+10=342) sum to the stated 342.'

if __name__ == '__main__':
    BOOK.save(50, [(5, rec)])
