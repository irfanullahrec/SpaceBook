"""Pak Studies XII PDF48 (spread): printed pp.85–86 — Chapter 5 opening: federal institutions; President's status and powers."""
from class12_book_common import Book, Builder

BOOK = Book('pak')
t = Builder()
def P(*v): t.p(*v)
def H(*v): t.h(*v)
t.p('Chapter Five', 'بابِ پنجم', 'پنځم څپرکی')
H('Governmental Structure of Pakistan and Good Governance', 'پاکستان کا حکومتی ڈھانچہ اور اچھا نظامِ حکومت', 'د پاکستان حکومتي جوړښت او ښه حکومتولي')
H('Institutions of the federal government and their performance', 'وفاقی حکومت کے ادارے اور اُن کی کارکردگی', 'د فدرالي حکومت ادارې او د هغو کارکردګي')
P('Pakistan is a federal state, and according to the 1973 constitution powers are divided between the provinces and the centre. The federal government and the provincial governments work according to their constitutional powers.',
  'پاکستان ایک وفاقی مملکت ہے اور 1973ء کے آئین کی رُو سے اختیارات صوبوں اور مرکز میں منقسم ہیں۔ وفاقی حکومت اور صوبائی حکومتیں اپنے اپنے آئینی اختیارات کے مطابق کام کرتی ہیں۔',
  'پاکستان یو فدرالي هېواد دی، او د ۱۹۷۳ز د اساسي قانون له مخې واکونه د ولایتونو او مرکز ترمنځ وېشل شوي. فدرالي حکومت او ولایتي حکومتونه د خپلو اساسي واکونو سره سم کار کوي.')
P('The President has the status of the head of the country, while the head of government is the Prime Minister. To help the Prime Minister there is a cabinet. Each federal minister is responsible for one or more ministries (departments), for whose performance he is answerable. At the national level an elected Majlis-e-Shoora has been established for law-making, which consists of two houses, the National Assembly and the Senate. Besides these, there is a permanent government staff of employees, who implement the government’s policies. Each ministry has a Secretary who is its head. To help him every ministry has hundreds of junior and senior officers and other staff.',
  'ملک کے سربراہ کی حیثیت صدر کو حاصل ہوتی ہے جبکہ حکومت کا سربراہ وزیرِاعظم ہوتا ہے۔ وزیرِاعظم کی مدد کے لیے کابینہ ہوتی ہے۔ ہر وفاقی وزیر کے ذمے ایک یا ایک سے زیادہ وزارتیں (محکمے) ہوتی ہیں جن کی کارکردگی کا وہ ذمہ دار ہوتا ہے۔ قومی سطح پر قانون سازی کے لیے منتخب مجلسِ شوریٰ قائم ہے، جو دو ایوانوں قومی اسمبلی اور سینیٹ پر مشتمل ہے۔ اس کے علاوہ ملازمین کا مستقل سرکاری عملہ ہوتا ہے جو حکومت کی پالیسیوں پر عمل درآمد کرواتا ہے۔ ہر وزارت کا ایک سیکرٹری ہوتا ہے جو اس کا سربراہ ہوتا ہے۔ اس کی مدد کے لیے ہر وزارت میں سینکڑوں چھوٹے بڑے افسر اور دیگر عملہ ہوتا ہے۔',
  'د هېواد د مشر حیثیت ولسمشر ته حاصل دی، په داسې حال کې چې د حکومت مشر لومړی وزیر وي. د لومړي وزیر د مرستې لپاره کابینه وي. هر فدرالي وزیر یو یا له یوه زیات وزارتونه (څانګې) لري چې د کارکردګۍ مسؤول یې دی. په ملي کچه د قانون جوړونې لپاره ټاکل شوې مجلس شوری جوړه ده، چې له دوو جرګو، ملي اسمبلۍ او سنا، جوړه ده. سربېره پر دې د کارکوونکو دایمي دولتي کارکوونکي وي، چې د حکومت پالیسۍ پلي کوي. هر وزارت یو منشي (سکرتر) لري چې مشر یې دی. د هغه د مرستې لپاره په هر وزارت کې سلګونه وړه او لوی افسران او نور کارکوونکي وي.')
H('Status and powers of the President in the federation', 'وفاق میں صدر کی حیثیت اور اختیارات', 'په فدراسیون کې د ولسمشر حیثیت او واکونه')
P('According to the constitution the President of the state will be the head of the country and will represent the unity of the Republic. Under the constitution it is necessary for a presidential candidate to possess these qualifications:',
  'آئین کے مطابق صدرِ مملکت، ملک کا سربراہ ہوگا اور وہی جمہوریہ کی بطور وحدت نمائندگی کرے گا۔ آئین کے تحت صدارتی امیدوار کے لیے ضروری ہے کہ وہ ان اوصاف کا حامل ہو۔',
  'د اساسي قانون سره سم ولسمشر به د هېواد مشر وي او هماغه به د جمهوریت د یووالي استازیتوب کوي. د اساسي قانون له مخې د ولسمشرۍ نوماند لپاره ضروري ده چې دا ځانګړنې ولري:')
t.group('lines', [('i. He is a Muslim.', 'i۔ مسلمان ہو۔', 'i. مسلمان وي.'), ('ii. His age is not less than 45 years.', 'ii۔ اس کی عمر 45 سال سے کم نہ ہو۔', 'ii. عمر یې له ۴۵ کلونو کم نه وي.'),
                  ('iii. He is qualified to be elected a member of the National Assembly.', 'iii۔ وہ قومی اسمبلی کا رکن منتخب ہونے کی اہلیت رکھتا ہو۔', 'iii. د ملي اسمبلۍ د غړي ټاکل کېدو وړتیا ولري.')])
H('Powers of the President', 'صدر کے اختیارات', 'د ولسمشر واکونه')
H('Executive powers', 'انتظامی اختیارات', 'اجرايي واکونه')
P('The highest executive powers of the federation belong to the President of the state, which he will exercise according to the advice of the Prime Minister and his cabinet.',
  'وفاق کے اعلیٰ ترین انتظامی اختیارات صدرِ مملکت کو حاصل ہیں۔ جنھیں وہ وزیرِاعظم اور اس کی کابینہ کے مشورے کے مطابق سرانجام دے گا۔',
  'د فدراسیون تر ټولو لوړ اجرايي واکونه ولسمشر ته حاصل دي، چې د لومړي وزیر او د هغه د کابینې د مشورې سره سم به یې ترسره کوي.')
H('Formation of the cabinet', 'کابینہ کی تشکیل', 'د کابینې جوړښت')
P('In this connection the most important power is the appointment of the Prime Minister. According to the constitution the President will invite to form the cabinet that person who has the confidence of the majority of the National Assembly. On the advice of the Prime Minister, the President will appoint the other ministers of the cabinet and ministers of state.',
  'اس سلسلے میں سب سے اہم اختیار وزیرِاعظم کا تقرر ہے۔ آئین کے مطابق صدر ایسے شخص کو کابینہ کی تشکیل کی دعوت دے گا جسے قومی اسمبلی کی اکثریت کا اعتماد حاصل ہو۔ صدر، وزیرِاعظم کے مشورے پر کابینہ کے دیگر وزراء اور وزراءِ مملکت کا تقرر کرے گا۔',
  'په دې برخه کې تر ټولو مهم واک د لومړي وزیر ټاکل دي. د اساسي قانون سره سم ولسمشر به هغه کس ته د کابینې د جوړولو بلنه ورکوي چې د ملي اسمبلۍ د اکثریت باور ورسره وي. ولسمشر به د لومړي وزیر په مشوره د کابینې نور وزیران او دولتي وزیران ټاکي.')
H('Special powers', 'خصوصی اختیارات', 'ځانګړي واکونه')
P('The President can order the cabinet to reconsider any matter in general or particular. These also include matters on which the Prime Minister or some minister has made a decision but which have not come under discussion in the cabinet. In the course of performing his duties the President can seek advice from the Prime Minister or any minister on any matter, but he will not be bound by their advice.',
  'صدر کسی بھی مسئلہ پر کابینہ کو عمومی طور پر یا خصوصی طور پر دوبارہ غور کرنے کا حکم دے سکتا ہے۔ ان میں ایسے معاملات بھی شامل ہیں جن پر فیصلہ وزیرِاعظم یا کسی وزیر نے کیا ہو لیکن وہ کابینہ میں زیرِ بحث نہ آیا ہو۔ صدر اپنے فرائض کی بجا آوری کے سلسلے میں کسی بھی معاملے پر وزیرِاعظم یا کسی وزیر سے مشورہ طلب کر سکتا ہے لیکن وہ ان کے مشورے کا پابند نہیں ہوگا۔',
  'ولسمشر کولی شي کابینې ته د هرې مسئلې په اړه په عمومي یا ځانګړي ډول د بیا غور امر وکړي. په دې کې داسې چارې هم شاملې دي چې لومړي وزیر یا کوم وزیر پرې پرېکړه کړې وي خو په کابینه کې تر بحث لاندې نه وي راغلې. ولسمشر د خپلو دندو د ترسره کولو په لړ کې پر هره چاره له لومړي وزیر یا کوم وزیر مشوره غوښتلی شي، خو د هغوی د مشورې پابند به نه وي.')
H('Appointments', 'تقرریاں', 'ټاکنې')
P('The President appoints the Prime Minister and the other federal ministers. The appointment of ambassadors to other countries, the Chief Election Commissioner and the judges of the superior courts are important powers of the President. Under the 17th Amendment of the constitution, the President appoints the Chairman of the Joint Chiefs of Staff Committee and the heads of all three armed forces on the advice of the Prime Minister. In case of the dissolution of the National Assembly, the President appoints a caretaker cabinet.',
  'صدر، وزیرِاعظم اور دیگر وفاقی وزراء کا تقرر کرتا ہے۔ دوسرے ممالک میں سفیروں کا تقرر، چیف الیکشن کمشنر اور اعلیٰ عدالتوں کے ججوں کا تقرر صدر کے اہم ترین اختیارات ہیں۔ آئین کی 17ویں ترمیم کے تحت صدر چیئرمین جوائنٹ چیف آف سٹاف کمیٹی اور تینوں مسلح افواج کے سربراہان کا تقرر وزیرِاعظم کے مشورے سے کرتا ہے۔ قومی اسمبلی تحلیل ہونے کی صورت میں صدر ایک نگران کابینہ مقرر کرتا ہے۔',
  'ولسمشر لومړی وزیر او نور فدرالي وزیران ټاکي. په نورو هېوادونو کې د سفیرانو، د ټاکنو د لوی کمېشنر او د لوړو محکمو د قاضیانو ټاکل د ولسمشر تر ټولو مهم واکونه دي. د اساسي قانون د ۱۷م تعدیل له مخې ولسمشر د ګډو لویو درستیزانو د کمېټې رئیس او د درېیو وسله والو ځواکونو مشران د لومړي وزیر په مشوره ټاکي. د ملي اسمبلۍ د منحل کېدو په صورت کې ولسمشر یوه سرپرسته کابینه ټاکي.')
UT = ('Governmental Structure of Pakistan and Good Governance', 'پاکستان کا حکومتی ڈھانچہ اور اچھا نظامِ حکومت', 'د پاکستان حکومتي جوړښت او ښه حکومتولي')
rec = BOOK.record(t, 'pak12-ch5-text-1', 'Chapter 5 text (1)', 'بابِ پنجم — متن (۱)', 'پنځم څپرکی — متن (۱)', 48, [85, 86], unit_title=UT)

if __name__ == '__main__':
    BOOK.save(48, [(5, rec)])
