"""Computer Science XII PDF9 (spread): printed pp.6–7 — Fig 1.3 Windows 7 desktop; c. UNIX; Fig 1.4 UNIX prompt; d. Mac OS; Fig 1.7 Mac OS desktop (all figures coded)."""
from class12_cs_common import BOOK, Builder
from class12_cs_figs import fig_1_3, fig_1_4, fig_1_7

t = Builder()
P = t.p
H = t.h
en, ur, ps = fig_1_3()
t.visual('cs12-fig-1-3', en, ur, ps, 480 / 300)
H('c. UNIX Operating System', 'c. یونکس آپریٹنگ سسٹم', 'c. د UNIX عملیاتي سیسټم')
P('UNIX is a multitasking and multi-user operating system that was developed by Ken Thompson, Dennis Ritchie and their group members at Bell Labs in 1969. It was first developed in assembly language. Later on, in 1973, it was re-developed in C language. This version of UNIX has facilitated its further development and support to other hardware.',
  'UNIX ایک ملٹی ٹاسکنگ اور ملٹی یوزر آپریٹنگ سسٹم ہے جسے کین تھامسن، ڈینس رچی اور ان کے گروپ کے اراکین نے 1969ء میں بیل لیبز میں تیار کیا۔ اسے پہلے اسمبلی لینگویج میں تیار کیا گیا۔ بعد ازاں 1973ء میں اسے C لینگویج میں دوبارہ تیار کیا گیا۔ UNIX کے اس ورژن نے اس کی مزید ترقی اور دوسرے ہارڈویئر کی معاونت کو آسان بنایا۔',
  'UNIX یو څو-دندیز او ډېر-کاروونکي عملیاتي سیسټم دی چې کېن تامسن، ډېنس ریچي او د هغوی د ډلې غړو په ۱۹۶۹ز کې په بیل لابز کې جوړ کړ. لومړی په اسمبلي ژبه جوړ شو. وروسته په ۱۹۷۳ز کې په C ژبه بیا جوړ شو. د UNIX دې نسخې د هغه نورې ودې او د نورو هارډویرونو ملاتړ ته لاره اسانه کړه.')
P('UNIX operating systems also have a graphical user interface (GUI) similar to Microsoft Windows which provides an easy to use environment for naive users.',
  'UNIX آپریٹنگ سسٹم میں بھی مائیکروسافٹ ونڈوز جیسا گرافیکل یوزر انٹرفیس (GUI) ہوتا ہے جو نئے صارفین کو استعمال میں آسان ماحول فراہم کرتا ہے۔',
  'د UNIX عملیاتي سیسټمونه هم د مایکروسافټ وینډوز په څېر ګرافیکي کاروونکي منځګړی (GUI) لري چې نوو کاروونکو ته د کارولو اسانه چاپېریال برابروي.')
P('Different versions of UNIX operating system have been developed so far which have some features in common. The most popular types of UNIX operating system are Sun Solaris, GNU/Linux and Mac OS X.',
  'اب تک UNIX آپریٹنگ سسٹم کے مختلف ورژن تیار کیے جا چکے ہیں جن کی کچھ خصوصیات مشترک ہیں۔ UNIX آپریٹنگ سسٹم کی سب سے مقبول اقسام Sun Solaris، GNU/Linux اور Mac OS X ہیں۔',
  'تر اوسه د UNIX عملیاتي سیسټم بېلابېلې نسخې جوړې شوې چې ځینې ځانګړنې یې ګډې دي. د UNIX عملیاتي سیسټم تر ټولو مشهور ډولونه Sun Solaris، GNU/Linux او Mac OS X دي.')
P('When you want to open the UNIX terminal window, click on Application menu and then select Terminal icon.',
  'جب آپ UNIX ٹرمینل ونڈو کھولنا چاہیں تو Application مینو پر کلک کریں اور پھر Terminal آئیکن منتخب کریں۔',
  'کله چې غواړئ د UNIX ټرمینل کړکۍ پرانیزئ، پر Application مینو کلیک وکړئ او بیا د Terminal نښه وټاکئ.')
P('After selecting Terminal from the menu, the UNIX Terminal window will open having % prompt as shown in figure 1.4. The user will enter the command in this prompt to execute.',
  'مینو سے Terminal منتخب کرنے کے بعد UNIX ٹرمینل ونڈو % پرامپٹ کے ساتھ کھل جائے گی جیسا کہ شکل 1.4 میں دکھایا گیا ہے۔ صارف کمانڈ چلانے کے لیے اسے اس پرامپٹ میں درج کرے گا۔',
  'له مینو د Terminal له ټاکلو وروسته د UNIX ټرمینل کړکۍ د % پرامپټ سره پرانیستل کېږي لکه څنګه چې په ۱.۴ شکل کې ښودل شوي. کاروونکی به د چلولو لپاره امر په دې پرامپټ کې ولیکي.')
en, ur, ps = fig_1_4()
t.visual('cs12-fig-1-4', en, ur, ps, 480 / 170)
H('d. Mac OS', 'd. میک او ایس', 'd. Mac OS')
P('Mac OS stands for Macintosh operating system. It is a series of operating systems having graphical user interfaces that have been developed by Apple Inc. On January 24, 1984, Apple Computer Inc. manufactured its first Macintosh personal computer and developed a system software for it which was later on renamed to Mac OS.',
  'Mac OS سے مراد میکنٹوش آپریٹنگ سسٹم ہے۔ یہ گرافیکل یوزر انٹرفیس والے آپریٹنگ سسٹمز کا ایک سلسلہ ہے جو ایپل انکارپوریٹڈ نے تیار کیے ہیں۔ 24 جنوری 1984ء کو ایپل کمپیوٹر انکارپوریٹڈ نے اپنا پہلا میکنٹوش ذاتی کمپیوٹر تیار کیا اور اس کے لیے ایک سسٹم سافٹ ویئر بنایا جس کا نام بعد میں Mac OS رکھا گیا۔',
  'Mac OS د Macintosh عملیاتي سیسټم معنا لري. دا د ګرافیکي کاروونکي منځګړي لرونکو عملیاتي سیسټمونو یوه لړۍ ده چې Apple Inc. جوړه کړې. د ۱۹۸۴ز د جنوري په ۲۴مه Apple Computer Inc. خپل لومړی Macintosh شخصي کمپیوټر جوړ کړ او ورته یې سیسټم سافټویر جوړ کړ چې وروسته Mac OS ونومول شو.')
P('Mac OS can be divided into two groups which are: Mac OS Classic family and the Mac OS X family. So far, Mac OS has ten (10) versions with the names Mac OS 1, 2, 3, 4, 5, 6, 7, 8, 9 and X. Figure 1.5 shows the desktop interface of Mac OS.',
  'Mac OS کو دو گروپوں میں تقسیم کیا جا سکتا ہے: Mac OS Classic فیملی اور Mac OS X فیملی۔ اب تک Mac OS کے دس (10) ورژن Mac OS 1، 2، 3، 4، 5، 6، 7، 8، 9 اور X کے ناموں سے آ چکے ہیں۔ شکل 1.5 میں Mac OS کا ڈیسک ٹاپ انٹرفیس دکھایا گیا ہے۔',
  'Mac OS په دوو ډلو وېشل کېدای شي: د Mac OS Classic کورنۍ او د Mac OS X کورنۍ. تر اوسه د Mac OS لس (۱۰) نسخې د Mac OS 1، 2، 3، 4، 5، 6، 7، 8، 9 او X په نومونو راغلې دي. ۱.۵ شکل د Mac OS د ډیسکټاپ منځګړی ښيي.')
en, ur, ps = fig_1_7()
t.visual('cs12-fig-1-7', en, ur, ps, 480 / 290)
rec = BOOK.record(t, 'cs12-u1-text-3', 'Unit 1 text (3)', 'یونٹ 1 — متن (۳)', '۱ څپرکی — متن (۳)', 9, [6, 7])
rec['sourceNote'] = 'Figures 1.3, 1.4 and 1.7 are screenshots in print; they are reproduced as coded mock-ups carrying the printed callout labels.'
issues = [{'id': 'cs12-pdf009', 'unit': 1, 'printedPage': 7,
           'description': 'The text on p.7 refers to “Figure 1.5” for the Mac OS desktop, but the figure is captioned “Figure 1.7” (and there is no Figure 1.5/1.6); both retained as printed. p.6 prints “Applicationmenu” and “Terminalicon” without spaces; normalised in the transcription.'}]

if __name__ == '__main__':
    BOOK.save(9, [(1, rec)], issues=issues)
