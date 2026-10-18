"""Computer Science XII PDF17 (spread): printed pp.22–23 — 1.3 process management; 1.3.1 process; 1.3.2 process states a–e; Fig 1.10 (coded); 1.3.3 threads and processes (begins)."""
from class12_cs_common import BOOK, Builder
from class12_cs_figs import fig_1_10

t = Builder()
P = t.p
H = t.h
H('1.3 PROCESS MANAGEMENT', '1.3 پراسیس مینجمنٹ', '۱.۳ د پروسې اداره')
P('As discussed earlier, process management is one of the important functions of operating system. The following sections describe process in detail with a comparison to threads.',
  'جیسا کہ پہلے بیان ہوا، پراسیس مینجمنٹ آپریٹنگ سسٹم کے اہم افعال میں سے ایک ہے۔ درج ذیل حصے تھریڈز کے موازنے کے ساتھ پراسیس کو تفصیل سے بیان کرتے ہیں۔',
  'لکه څنګه چې مخکې وویل شول، د پروسې اداره د عملیاتي سیسټم له مهمو دندو څخه یوه ده. لاندې برخې د تارونو (threads) سره په پرتله پروسه په تفصیل بیانوي.')
H('1.3.1 Process', '1.3.1 پراسیس', '۱.۳.۱ پروسه')
P('Following are some definitions of process:', 'پراسیس کی کچھ تعریفیں درج ذیل ہیں:', 'د پروسې ځینې تعریفونه دا دي:')
t.group('list', [('A program under execution by the processor (CPU) is called process.', 'پروسیسر (CPU) کے ذریعے زیرِ عمل پروگرام کو پراسیس کہتے ہیں۔', 'هغه پروګرام چې د پروسېسر (CPU) له خوا د اجرا لاندې وي، پروسه بلل کېږي.'),
                 ('An instance of a program running on a computer is called process.', 'کمپیوٹر پر چلنے والے پروگرام کی ایک مثال (instance) کو پراسیس کہتے ہیں۔', 'په کمپیوټر د چلېدونکي پروګرام یوې بېلګې (instance) ته پروسه ویل کېږي.'),
                 ('The entity that can be assigned to and executed on a processor is termed as process.', 'وہ اکائی جسے پروسیسر کو تفویض کیا جا سکے اور اس پر چلایا جا سکے، پراسیس کہلاتی ہے۔', 'هغه واحد چې پروسېسر ته سپارل کېدای شي او پرې اجرا کېدای شي، پروسه بلل کېږي.')])
H('1.3.2 Process States', '1.3.2 پراسیس کی حالتیں', '۱.۳.۲ د پروسې حالتونه')
P('A process can be in one of the different states: new, ready, running, block, and exit. These states are usually represented in the form of models called process models.',
  'پراسیس مختلف حالتوں میں سے کسی ایک میں ہو سکتا ہے: نیا، تیار، چلتا ہوا، بلاک اور اختتام۔ ان حالتوں کو عموماً ماڈلز کی شکل میں ظاہر کیا جاتا ہے جنھیں پراسیس ماڈلز کہتے ہیں۔',
  'یوه پروسه په یوه له بېلابېلو حالتونو کې کېدای شي: نوی، چمتو، روان، بند او وتل. دا حالتونه عموماً د ماډلونو په بڼه ښودل کېږي چې د پروسې ماډلونه بلل کېږي.')
H('a. New State', 'a. نئی حالت', 'a. نوی حالت')
P('When a new process is created then it is said to be in new state.', 'جب نیا پراسیس بنایا جاتا ہے تو کہا جاتا ہے کہ وہ نئی حالت میں ہے۔', 'کله چې نوې پروسه جوړه شي، ویل کېږي چې په نوي حالت کې ده.')
H('b. Running State', 'b. چلنے کی حالت', 'b. روان حالت')
P('A process is said to be in running state if it is under execution by the CPU. This means that the process actually using the CPU at that particular time.',
  'پراسیس اس وقت چلنے کی حالت میں کہلاتا ہے جب وہ CPU کے ذریعے زیرِ عمل ہو۔ اس کا مطلب ہے کہ پراسیس اس خاص وقت پر واقعی CPU استعمال کر رہا ہے۔',
  'یوه پروسه هغه وخت په روان حالت کې ګڼل کېږي چې د CPU له خوا د اجرا لاندې وي. مطلب یې دا دی چې پروسه په هغه ځانګړي وخت کې په رښتیا CPU کاروي.')
H('c. Blocked (or waiting) State', 'c. بلاک (یا انتظار) کی حالت', 'c. بند (یا انتظار) حالت')
P('A process is said to be in blocked state if it is waiting for some event to happen such as an Input/Output completion before it can proceed.',
  'پراسیس اس وقت بلاک حالت میں کہلاتا ہے جب وہ آگے بڑھنے سے پہلے کسی واقعے کے ہونے کا انتظار کر رہا ہو، جیسے ان پٹ/آؤٹ پٹ کی تکمیل۔',
  'یوه پروسه هغه وخت په بند حالت کې ګڼل کېږي چې د دوام مخکې د کومې پېښې د پېښېدو انتظار کوي، لکه د ننوتو/وتو بشپړېدل.')
H('d. Ready State', 'd. تیار حالت', 'd. چمتو حالت')
P('A process is said to be in ready state if it is ready to be assigned to the CPU for processing.', 'پراسیس اس وقت تیار حالت میں کہلاتا ہے جب وہ پراسیسنگ کے لیے CPU کو تفویض ہونے کے لیے تیار ہو۔', 'یوه پروسه هغه وخت په چمتو حالت کې ګڼل کېږي چې د پروسس لپاره CPU ته د سپارلو چمتو وي.')
H('e. Terminated state (or exit)', 'e. ختم شدہ حالت (یا اختتام)', 'e. پای ته رسېدلی حالت (یا وتل)')
P('A process is said to be in terminated state if the CPU has finished its execution.', 'پراسیس اس وقت ختم شدہ حالت میں کہلاتا ہے جب CPU اس کا عمل مکمل کر چکا ہو۔', 'یوه پروسه هغه وخت په پای ته رسېدلي حالت کې ګڼل کېږي چې CPU یې اجرا بشپړه کړې وي.')
P('An example of a five state process model is given below:', 'پانچ حالتوں والے پراسیس ماڈل کی ایک مثال ذیل میں دی گئی ہے:', 'د پنځو حالتونو د پروسې ماډل یوه بېلګه لاندې ورکړل شوې:')
en, ur, ps, ratio = fig_1_10()
t.visual('cs12-fig-1-10', en, ur, ps, ratio)
H('1.3.3 Threads and processes', '1.3.3 تھریڈز اور پراسیسز', '۱.۳.۳ تارونه او پروسې')
P('A thread can be defined as a dispatchable unit of a process that can be executed sequentially and is interruptible. It can also be defined as a single sequence stream within a process.',
  'تھریڈ کو پراسیس کی ایک ایسی قابلِ روانگی اکائی کے طور پر بیان کیا جا سکتا ہے جو ترتیب وار چلائی جا سکے اور جس میں رکاوٹ ڈالی جا سکے۔ اسے پراسیس کے اندر ایک واحد ترتیبی سلسلے کے طور پر بھی بیان کیا جا سکتا ہے۔',
  'تار (thread) د پروسې د لېږلو وړ داسې واحد په توګه تعریف کېدای شي چې په ترتیب سره اجرا کېدای شي او مداخله یې شونې وي. همداراز د پروسې دننه د یوه واحد ترتیبي بهیر په توګه هم تعریف کېدای شي.')
P('As threads are small independently executable units of processes, therefore, they have some of the properties of processes because of which they are sometimes called lightweight processes. In a process, threads allow multiple executions of streams.',
  'چونکہ تھریڈز پراسیسز کی چھوٹی آزادانہ طور پر قابلِ عمل اکائیاں ہیں، اس لیے ان میں پراسیسز کی کچھ خصوصیات ہوتی ہیں جس کی وجہ سے انھیں بعض اوقات ہلکے پراسیسز (lightweight processes) کہا جاتا ہے۔ ایک پراسیس میں تھریڈز سلسلوں کے متعدد عمل کی اجازت دیتے ہیں۔',
  'څرنګه چې تارونه د پروسو کوچني په خپلواک ډول د اجرا وړ واحدونه دي، نو د پروسو ځینې ځانګړنې لري چې له امله یې کله کله سپکې پروسې (lightweight processes) بلل کېږي. په یوه پروسه کې تارونه د بهیرونو ډېرې اجرا ګانې شونې کوي.')
rec = BOOK.record(t, 'cs12-u1-text-11', 'Unit 1 text (11)', 'یونٹ 1 — متن (۱۱)', '۱ څپرکی — متن (۱۱)', 17, [22, 23])
rec['sourceNote'] = 'Figure 1.10 is reproduced as a coded state diagram. The threads paragraph continues on p.24 (PDF18). The printed page number on p.22 is cut at the margin.'
issues = [{'id': 'cs12-pdf017', 'unit': 1, 'printedPage': 22,
           'description': 'p.22 prints “that the process actually using the CPU” (missing “is”) and lists the state “block” in the text but “Blocked” in the figure. Retained as printed. Owner pen circling excluded.'}]

if __name__ == '__main__':
    BOOK.save(17, [(1, rec)], issues=issues)
