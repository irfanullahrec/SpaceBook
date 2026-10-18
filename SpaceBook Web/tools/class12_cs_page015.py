"""Computer Science XII PDF15 (spread): printed pp.18–19 — memory management (end); file management; Fig 1.7 (explorer tree as code listing); Fig 1.8 hierarchy (coded); I/O system management."""
from class12_cs_common import BOOK, Builder, code
from class12_cs_figs import fig_1_8

t = Builder()
P = t.p
H = t.h
P('… available, which is to be allocated or de-allocated and how to move data among them. This overall function of operating system is called memory management.',
  '… دستیاب ہے، کون سی مختص یا آزاد کی جانی ہے اور ان کے درمیان ڈیٹا کیسے منتقل کیا جائے۔ آپریٹنگ سسٹم کے اس مجموعی فعل کو میموری مینجمنٹ کہتے ہیں۔',
  '… شته ده، کومه باید وټاکل شي یا خوشې شي او ډېټا یې ترمنځ څنګه ولېږدول شي. د عملیاتي سیسټم دې ټولیزې دندې ته د حافظې اداره ویل کېږي.')
H('File management', 'فائل مینجمنٹ', 'د فایلونو اداره')
P('The data is stored in computer memory in files which are further arranged and organized in sub directories and root directory resulting in a hierarchical file system. A module of operating system that organizes and keeps track of all the files in computers is called file manager and the process of managing these files is called file management. For example, a hierarchical file system, shown in figure 1.7 and 1.8 depict that how files are arranged into root directory and sub-directories. This hierarchical file system is also called files system.',
  'ڈیٹا کمپیوٹر میموری میں فائلوں میں محفوظ کیا جاتا ہے جنھیں مزید ذیلی ڈائریکٹریز اور روٹ ڈائریکٹری میں ترتیب اور منظم کیا جاتا ہے، جس سے درجہ وار فائل سسٹم بنتا ہے۔ آپریٹنگ سسٹم کا وہ ماڈیول جو کمپیوٹر میں تمام فائلوں کو منظم کرتا اور ان کا ریکارڈ رکھتا ہے فائل مینیجر کہلاتا ہے اور ان فائلوں کے انتظام کے عمل کو فائل مینجمنٹ کہتے ہیں۔ مثال کے طور پر شکل 1.7 اور 1.8 میں دکھایا گیا درجہ وار فائل سسٹم ظاہر کرتا ہے کہ فائلیں روٹ ڈائریکٹری اور ذیلی ڈائریکٹریز میں کیسے ترتیب دی جاتی ہیں۔ اس درجہ وار فائل سسٹم کو فائلز سسٹم بھی کہتے ہیں۔',
  'ډېټا د کمپیوټر په حافظه کې په فایلونو کې ساتل کېږي چې بیا په فرعي لارښودونو او ریښه لارښود کې ترتیب او تنظیمېږي، چې پایله یې درجه‌ییز فایل سیسټم دی. د عملیاتي سیسټم هغه ماډیول چې په کمپیوټرونو کې ټول فایلونه تنظیموي او ریکارډ یې ساتي، د فایل مدیر بلل کېږي او د دې فایلونو د ادارې بهیر ته د فایلونو اداره ویل کېږي. د بېلګې په توګه په ۱.۷ او ۱.۸ شکلونو کې ښودل شوی درجه‌ییز فایل سیسټم ښيي چې فایلونه څنګه په ریښه لارښود او فرعي لارښودونو کې ترتیبېږي. دې درجه‌ییز فایل سیسټم ته د فایلونو سیسټم هم ویل کېږي.')
code(t, r'''Documents ▸ CV                                   [Search CV]
Organize ▾   Open ▾   Print   E-mail   »

▾ Computer                      Name
  ▾ Local Disk (C:)               Curriculum Vitea
    ▾ Applications                Person Request
        Games
        Spread
    ▾ Documents
        CV
        Presentations
        Transcripts
  Curriculum Vitea''')
P('Figure 1.7: File Structure in Computer', 'شکل 1.7: کمپیوٹر میں فائل کی ساخت', '۱.۷ شکل: په کمپیوټر کې د فایل جوړښت')
en, ur, ps, ratio = fig_1_8()
t.visual('cs12-fig-1-8', en, ur, ps, ratio)
H('Input/Output System Management', 'ان پٹ/آؤٹ پٹ سسٹم مینجمنٹ', 'د ننوتو/وتو د سیسټم اداره')
P('Every computer system has input/output devices such as keyboard, mouse, disk drives, printers, displays etc. All these devices need significant amount of management. The module of operating system used to manage input/output devices is called Input/Output manager or device manager and the process is called Input/Output management. I/O manager allocates resources on requests to applications to perform I/O operation. Device manager provides a convenient way for the use of input/output hardware and hides the hardware level complexities from the users.',
  'ہر کمپیوٹر سسٹم میں ان پٹ/آؤٹ پٹ آلات ہوتے ہیں جیسے کی بورڈ، ماؤس، ڈسک ڈرائیوز، پرنٹرز، ڈسپلے وغیرہ۔ ان سب آلات کو کافی انتظام کی ضرورت ہوتی ہے۔ آپریٹنگ سسٹم کا وہ ماڈیول جو ان پٹ/آؤٹ پٹ آلات کے انتظام کے لیے استعمال ہوتا ہے، ان پٹ/آؤٹ پٹ مینیجر یا ڈیوائس مینیجر کہلاتا ہے اور اس عمل کو ان پٹ/آؤٹ پٹ مینجمنٹ کہتے ہیں۔ I/O مینیجر ایپلیکیشنز کی درخواست پر I/O عمل انجام دینے کے لیے وسائل مختص کرتا ہے۔ ڈیوائس مینیجر ان پٹ/آؤٹ پٹ ہارڈویئر کے استعمال کا آسان طریقہ فراہم کرتا ہے اور ہارڈویئر کی سطح کی پیچیدگیاں صارفین سے چھپاتا ہے۔',
  'هر کمپیوټري سیسټم د ننوتو/وتو وسایل لري لکه کیبورډ، موږک، ډیسک ډرایوونه، پرنټرونه، ښودونکي او نور. دا ټول وسایل ډېرې ادارې ته اړتیا لري. د عملیاتي سیسټم هغه ماډیول چې د ننوتو/وتو وسایلو د ادارې لپاره کارول کېږي، د ننوتو/وتو مدیر یا د وسایلو مدیر بلل کېږي او بهیر ته یې د ننوتو/وتو اداره ویل کېږي. د I/O مدیر د کاريالونو په غوښتنه د I/O عملیې لپاره سرچینې ټاکي. د وسایلو مدیر د ننوتو/وتو هارډویر د کارونې اسانه لاره برابروي او د هارډویر د کچې پېچلتیاوې له کاروونکو پټوي.')
P('The input/output hardware of computer cannot be accessed or used directly by the users. To make them useable, device drivers software must be installed on the computer. It is the device manager module of the operating system that make use of device driver software to access and manage Input/output devices. The relationship of operating system with drivers and hardware is shown in Figure 1.9.',
  'کمپیوٹر کے ان پٹ/آؤٹ پٹ ہارڈویئر تک صارفین براہِ راست رسائی یا اسے استعمال نہیں کر سکتے۔ انھیں قابلِ استعمال بنانے کے لیے کمپیوٹر پر ڈیوائس ڈرائیورز سافٹ ویئر انسٹال ہونا ضروری ہے۔ یہ آپریٹنگ سسٹم کا ڈیوائس مینیجر ماڈیول ہے جو ان پٹ/آؤٹ پٹ آلات تک رسائی اور ان کے انتظام کے لیے ڈیوائس ڈرائیور سافٹ ویئر استعمال کرتا ہے۔ آپریٹنگ سسٹم کا ڈرائیورز اور ہارڈویئر سے تعلق شکل 1.9 میں دکھایا گیا ہے۔',
  'کاروونکي د کمپیوټر ننوتو/وتو هارډویر ته مستقیم لاسرسی نه شي موندلی یا یې نه شي کارولی. د کارونې وړ کولو لپاره یې باید پر کمپیوټر د وسایلو د چلوونکو (device drivers) سافټویر نصب شي. دا د عملیاتي سیسټم د وسایلو د مدیر ماډیول دی چې د ننوتو/وتو وسایلو ته د لاسرسي او ادارې لپاره د وسیلې د چلوونکي سافټویر کاروي. د عملیاتي سیسټم اړیکه له چلوونکو او هارډویر سره په ۱.۹ شکل کې ښودل شوې.')
rec = BOOK.record(t, 'cs12-u1-text-9', 'Unit 1 text (9)', 'یونٹ 1 — متن (۹)', '۱ څپرکی — متن (۹)', 15, [18, 19])
rec['sourceNote'] = 'The opening words continue from p.17. Figure 1.7 (a Windows Explorer screenshot) is reproduced as a text listing of its folder tree; Figure 1.8 is reproduced as a coded tree diagram.'
issues = [{'id': 'cs12-pdf015', 'unit': 1, 'printedPage': 18,
           'description': 'p.18 prints “depict that how files are arranged” and “files system”; Figures 1.7/1.8 label the CV file “Curriculum Vitea” (for “Vitae”); p.19 “device manager module … that make use”. All retained as printed. Owner pen marks excluded.'}]

if __name__ == '__main__':
    BOOK.save(15, [(1, rec)], issues=issues)
