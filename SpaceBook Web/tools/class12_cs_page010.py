"""Computer Science XII PDF10 (spread): printed pp.8–9 — 1.1.3 Types of OS: a. batch processing; b. multiprogramming; Fig 1.6; advantages of multiprogramming."""
from class12_cs_common import BOOK, Builder
from class12_cs_figs import fig_1_6

t = Builder()
P = t.p
H = t.h
H('1.1.3 Types of Operating Systems', '1.1.3 آپریٹنگ سسٹمز کی اقسام', '۱.۱.۳ د عملیاتي سیسټمونو ډولونه')
P('Operating system can be divided into different types which are given below.', 'آپریٹنگ سسٹم کو مختلف اقسام میں تقسیم کیا جا سکتا ہے جو درج ذیل ہیں۔', 'عملیاتي سیسټم په بېلابېلو ډولونو وېشل کېدای شي چې لاندې ورکړل شوي.')
H('a. Batch processing operating system', 'a. بیچ پراسیسنگ آپریٹنگ سسٹم', 'a. ډله‌ییز پروسس عملیاتي سیسټم')
P('Batch processing system is that type of operating system which collects jobs in batches before being processed by the CPU. A job is a piece of work usually consisting of a program and the data to be run. All the Jobs are stored in job queues until the computer is ready to process them.',
  'بیچ پراسیسنگ سسٹم آپریٹنگ سسٹم کی وہ قسم ہے جو CPU کے پراسیس کرنے سے پہلے کاموں (jobs) کو گروہوں (batches) میں جمع کرتی ہے۔ جاب کام کا ایک حصہ ہے جو عموماً ایک پروگرام اور چلائے جانے والے ڈیٹا پر مشتمل ہوتا ہے۔ تمام جابز اس وقت تک جاب قطاروں (job queues) میں محفوظ رہتی ہیں جب تک کمپیوٹر انھیں پراسیس کرنے کے لیے تیار نہ ہو۔',
  'ډله‌ییز پروسس سیسټم د عملیاتي سیسټم هغه ډول دی چې د CPU له پروسس مخکې دندې (jobs) په ډلو (batches) کې راټولوي. دنده د کار یوه برخه ده چې عموماً له یوه پروګرام او د چلولو له ډېټا جوړه وي. ټولې دندې تر هغه په د دندو کتارونو (job queues) کې ساتل کېږي چې کمپیوټر یې پروسس ته چمتو شي.')
P('Once the CPU gets ready and fetches a job from the job queue, then there is no interaction of the user with the computer to interrupt the processing of the job until its completion.',
  'جب CPU تیار ہو کر جاب قطار سے ایک جاب حاصل کر لیتا ہے تو اس کی تکمیل تک جاب کی پراسیسنگ میں مداخلت کے لیے صارف کا کمپیوٹر سے کوئی تعامل نہیں ہوتا۔',
  'کله چې CPU چمتو شي او له کتار یوه دنده راواخلي، نو د هغې تر بشپړېدو پورې د دندې په پروسس کې د مداخلې لپاره د کاروونکي او کمپیوټر ترمنځ هېڅ تعامل نه وي.')
P('Batches of jobs are formed by collecting jobs during working hours and then executed during the evening time or at the end of each day or whenever the computer is available. Once a batch job begins, it continues until it is completed or until an error occurs.',
  'کام کے اوقات میں جابز جمع کر کے ان کے گروہ بنائے جاتے ہیں اور پھر انھیں شام کے وقت یا ہر دن کے آخر میں یا جب بھی کمپیوٹر دستیاب ہو، چلایا جاتا ہے۔ جب بیچ جاب شروع ہو جائے تو وہ مکمل ہونے یا کوئی خرابی پیش آنے تک جاری رہتی ہے۔',
  'د کار په ساعتونو کې د دندو په راټولولو سره ډلې جوړېږي او بیا د ماښام پر مهال یا د هرې ورځې په پای کې یا هر کله چې کمپیوټر وزګار وي، چلول کېږي. کله چې ډله‌ییزه دنده پیل شي، تر بشپړېدو یا د کومې تېروتنې تر پېښېدو پورې دوام کوي.')
P('Payroll system and preparation of electricity, telephone and credit card bills are processed under the batch processing systems. In each of these systems, the individual wages, calls, units consumed and transactions performed are batched together and at the end of each month the total bill is calculated.',
  'تنخواہوں کا نظام اور بجلی، ٹیلیفون اور کریڈٹ کارڈ کے بلوں کی تیاری بیچ پراسیسنگ سسٹمز کے تحت ہوتی ہے۔ ان میں سے ہر نظام میں انفرادی اجرتیں، کالیں، استعمال شدہ یونٹس اور کی گئی لین دین کو اکٹھا کیا جاتا ہے اور ہر مہینے کے آخر میں کل بل کا حساب لگایا جاتا ہے۔',
  'د تنخوا سیسټم او د برېښنا، ټیلیفون او کریډټ کارډ د بلونو چمتو کول د ډله‌ییز پروسس سیسټمونو له مخې کېږي. په دې هر سیسټم کې جلا جلا معاشونه، زنګونه، مصرف شوي واحدونه او ترسره شوې راکړې ورکړې یوځای کېږي او د هرې میاشتې په پای کې ټول بل حسابېږي.')
P('The example of batch processing system is IBM’s OS 360.', 'بیچ پراسیسنگ سسٹم کی مثال IBM کا OS 360 ہے۔', 'د ډله‌ییز پروسس سیسټم بېلګه د IBM OS 360 دی.')
H('b. Multiprogramming operating system', 'b. ملٹی پروگرامنگ آپریٹنگ سسٹم', 'b. څو-پروګرامي عملیاتي سیسټم')
P('Simple batch operating system has the problem that the processor often remains idle when the process under execution is halt due to some external event. Also, Input/output devices are slow as compared to processor, therefore, most of the time the processor remains idle. To eliminate this problem the concept of multiprogramming operating systems was introduced.',
  'سادہ بیچ آپریٹنگ سسٹم میں یہ مسئلہ ہے کہ جب زیرِ عمل پراسیس کسی بیرونی واقعے کی وجہ سے رک جاتا ہے تو پروسیسر اکثر فارغ رہتا ہے۔ نیز ان پٹ/آؤٹ پٹ آلات پروسیسر کے مقابلے میں سست ہوتے ہیں، اس لیے زیادہ تر وقت پروسیسر فارغ رہتا ہے۔ اس مسئلے کو ختم کرنے کے لیے ملٹی پروگرامنگ آپریٹنگ سسٹمز کا تصور متعارف کرایا گیا۔',
  'ساده ډله‌ییز عملیاتي سیسټم دا ستونزه لري چې کله د اجرا لاندې پروسه د کومې بهرنۍ پېښې له امله ودرېږي، پروسېسر ډېری وخت وزګار پاتې کېږي. همداراز د ننوتو/وتو وسایل د پروسېسر په پرتله ورو دي، نو ډېری وخت پروسېسر وزګار وي. د دې ستونزې د لرې کولو لپاره د څو-پروګرامي عملیاتي سیسټمونو مفهوم معرفي شو.')
P('Multiprogramming operating system is that type of operating system which allows running of multiple computer programs simultaneously on a single processor. For example, you may be typing in MS Word, listening to music while in background Internet Explorer is downloading some pages from the Internet. Working in Windows 7, Vista, XP and Linux environment is multiprogramming.',
  'ملٹی پروگرامنگ آپریٹنگ سسٹم آپریٹنگ سسٹم کی وہ قسم ہے جو ایک ہی پروسیسر پر بیک وقت متعدد کمپیوٹر پروگرام چلانے کی اجازت دیتی ہے۔ مثلاً آپ MS Word میں ٹائپ کر رہے ہوں، موسیقی سن رہے ہوں جبکہ پس منظر میں Internet Explorer انٹرنیٹ سے کچھ صفحات ڈاؤن لوڈ کر رہا ہو۔ Windows 7، Vista، XP اور Linux کے ماحول میں کام کرنا ملٹی پروگرامنگ ہے۔',
  'څو-پروګرامي عملیاتي سیسټم د عملیاتي سیسټم هغه ډول دی چې پر یوه پروسېسر په یو وخت د ډېرو کمپیوټري پروګرامونو د چلولو اجازه ورکوي. د بېلګې په توګه تاسو کېدای شي په MS Word کې ټایپ کوئ، موسیقي اورئ، په داسې حال کې چې په شاليد کې Internet Explorer له انټرنېټ ځینې پاڼې ښکته کوي. د Windows 7، Vista، XP او Linux په چاپېریال کې کار کول څو-پروګرامي کار دی.')
P('In multiprogramming operating systems, several programs, called jobs, are active at the same time in the main memory (RAM) of the computer. This means that multiple jobs are loaded into RAM and executed by a single processor. Figure 1.6 shows main memory partitioned into five (05) frames holding four (04) jobs.',
  'ملٹی پروگرامنگ آپریٹنگ سسٹمز میں کئی پروگرام، جنھیں جابز کہا جاتا ہے، کمپیوٹر کی مین میموری (RAM) میں بیک وقت فعال ہوتے ہیں۔ اس کا مطلب ہے کہ متعدد جابز RAM میں لوڈ ہوتی ہیں اور ایک ہی پروسیسر انھیں چلاتا ہے۔ شکل 1.6 میں مین میموری کو پانچ (05) فریمز میں تقسیم دکھایا گیا ہے جن میں چار (04) جابز ہیں۔',
  'په څو-پروګرامي عملیاتي سیسټمونو کې څو پروګرامونه چې دندې بلل کېږي، د کمپیوټر په اصلي حافظه (RAM) کې په یو وخت فعال وي. مطلب یې دا دی چې ډېرې دندې RAM ته ورپورته کېږي او یو پروسېسر یې چلوي. ۱.۶ شکل اصلي حافظه ښيي چې په پنځو (۰۵) چوکاټونو وېشل شوې او څلور (۰۴) دندې لري.')
en, ur, ps, ratio = fig_1_6()
t.visual('cs12-fig-1-6', en, ur, ps, ratio)
H('Advantages of multi-programming', 'ملٹی پروگرامنگ کے فوائد', 'د څو-پروګرامي کار ګټې')
P('Multiprogramming operating systems make efficient use of the processor by interleaving multiple actives jobs that reside in main memory. It also attempts to increase CPU utilization by always having something for the CPU to execute. Main memory (RAM) is efficiently utilized to hold more jobs at a time.',
  'ملٹی پروگرامنگ آپریٹنگ سسٹم مین میموری میں موجود متعدد فعال جابز کو باری باری چلا کر پروسیسر کا مؤثر استعمال کرتے ہیں۔ یہ CPU کے لیے ہمیشہ کچھ نہ کچھ چلانے کو رکھ کر اس کے استعمال کو بڑھانے کی کوشش بھی کرتا ہے۔ مین میموری (RAM) کو بیک وقت زیادہ جابز رکھنے کے لیے مؤثر طریقے سے استعمال کیا جاتا ہے۔',
  'څو-پروګرامي عملیاتي سیسټمونه په اصلي حافظه کې د شته ډېرو فعالو دندو په نوبتي چلولو سره له پروسېسر اغېزمنه ګټه اخلي. دا هڅه هم کوي چې CPU ته تل د چلولو لپاره څه وي او په دې ډول یې کارونه زیاته کړي. اصلي حافظه (RAM) په یو وخت د ډېرو دندو ساتلو لپاره په اغېزمن ډول کارول کېږي.')
rec = BOOK.record(t, 'cs12-u1-text-4', 'Unit 1 text (4)', 'یونٹ 1 — متن (۴)', '۱ څپرکی — متن (۴)', 10, [8, 9])
rec['sourceNote'] = 'Figure 1.6 is reproduced as a coded diagram. The multiprogramming paragraph runs across the page turn from p.8 to p.9.'
issues = [{'id': 'cs12-pdf010', 'unit': 1, 'printedPage': 9,
           'description': 'p.8 prints “is halt” (for “is halted”); p.9 prints “multiple actives jobs” and says memory is partitioned into five frames holding four jobs (Job 0–3); retained as printed. Owner pen circling/numbers on pp.8–9 excluded.'}]

if __name__ == '__main__':
    BOOK.save(10, [(1, rec)], issues=issues)
