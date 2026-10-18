"""Exact source sentences: basic Maple commands, printed pages 2–4."""
TRANSLATIONS={}
def add(*sentences):
 TRANSLATIONS[' '.join(s[0] for s in sentences)]=[{'en':en,'ur':ur,'ps':ps} for en,ur,ps in sentences]
add(
 ('A MAPLE command is a statement of calculation followed by a semicolon or a colon.','MAPLE کا حکم حساب کا ایک بیان ہے جس کے آخر میں سیمی کولن یا کولن آتا ہے۔','د MAPLE امر د محاسبې یو بیان دی چې په پای کې یې سیمي کولن یا کولن راځي.'),
 ('Following are some commands followed by the displayed results.','ذیل میں چند احکامات اور ان کے دکھائے گئے نتائج دیے گئے ہیں۔','لاندې ځینې امرونه او د هغوی ښودل شوې پایلې ورکړل شوې دي.')
)
add(
 ('Enter the commands on your worksheet and verify the given results.','اپنی ورک شیٹ پر احکامات درج کریں اور دیے گئے نتائج کی تصدیق کریں۔','په خپله کاري پاڼه کې امرونه ولیکئ او ورکړل شوې پایلې تایید کړئ.'),
 ('When you get to "Save the file", select "Save" under the "File" menu or use CTRL-S to save your working.','جب آپ "Save the file" تک پہنچیں تو اپنا کام محفوظ کرنے کے لیے "File" مینیو سے "Save" منتخب کریں یا CTRL-S استعمال کریں۔','کله چې "Save the file" ته ورسېږئ، د خپل کار د خوندي کولو لپاره د "File" له مېنو څخه "Save" وټاکئ یا CTRL-S وکاروئ.'),
 ('For example,','مثلاً،','د بېلګې په توګه،')
)
add(('If you do not include a semicolon or colon at the end of a command, MAPLE will interpret the next command line as a continuation of the previous command.','اگر حکم کے آخر میں سیمی کولن یا کولن نہ لگائیں تو MAPLE اگلے حکم کی سطر کو پچھلے حکم کا تسلسل سمجھے گا۔','که د امر په پای کې سیمي کولن یا کولن ونه لګوئ، MAPLE به د راتلونکي امر کرښه د مخکیني امر دوام وګڼي.'))
add(('The symbol +, -, *, / and ^ (or **) denote addition, subtraction, multiplication, division and exponential (4^2 = 4**2 = 4² = 16).','علامتیں +، -، *، / اور ^ (یا **) بالترتیب جمع، تفریق، ضرب، تقسیم اور قوت کو ظاہر کرتی ہیں (4^2 = 4**2 = 4² = 16)۔','نښې +، -، *، / او ^ (یا **) په ترتیب سره جمع، تفریق، ضرب، تقسیم او توان ښيي (4^2 = 4**2 = 4² = 16).'))
add(
 ('When a string of operations are specified in a command, MAPLE first does exponentiations then multiplication and divisions, then additions and subtractions.','جب ایک حکم میں کئی عملیات دیے جائیں تو MAPLE پہلے قوتیں، پھر ضرب اور تقسیم، اور پھر جمع اور تفریق انجام دیتا ہے۔','کله چې په یوه امر کې د عملیاتو لړۍ ورکړل شي، MAPLE لومړی توانونه، بیا ضرب او تقسیم، او وروسته جمع او تفریق ترسره کوي.'),
 ('To change the order, we use parentheses.','ترتیب بدلنے کے لیے ہم قوسین استعمال کرتے ہیں۔','د ترتیب بدلولو لپاره موږ قوسونه کاروو.')
)
add(('To save a variable in our current MAPLE session to a file, type the following at the command prompt.','MAPLE کے موجودہ سیشن میں کسی متغیر کو فائل میں محفوظ کرنے کے لیے حکم درج کرنے کی جگہ پر درج ذیل لکھیں۔','د MAPLE په اوسنۍ کاري ناسته کې په دوتنه کې د متحول د خوندي کولو لپاره د امر د ننویستلو په ځای کې لاندې ولیکئ.'))
add(('Replace the variable name with your variable name and replace the file name with your file name, but keep .m extension.','متغیر کی جگہ اپنے متغیر کا نام اور فائل کی جگہ اپنی فائل کا نام لکھیں، لیکن .m توسیع برقرار رکھیں۔','د متحول نوم د خپل متحول په نوم او د دوتنې نوم د خپلې دوتنې په نوم بدل کړئ، خو د .m وروستاړی وساتئ.'))
add(
 ('The Save command saves the variable as a MAPLE assignment statement.','Save حکم متغیر کو MAPLE کے تفویضی بیان کی صورت میں محفوظ کرتا ہے۔','د Save امر متحول د MAPLE د ارزښت د ټاکنې د بیان په بڼه خوندي کوي.'),
 ('If the value of your variable depends on other variables, you must save them as well.','اگر آپ کے متغیر کی قیمت دوسرے متغیرات پر منحصر ہو تو انہیں بھی محفوظ کرنا ضروری ہے۔','که ستاسو د متحول ارزښت په نورو متحولونو پورې تړلی وي، هغوی هم باید خوندي کړئ.')
)
add(('You can save more than one variable by giving all variable names to the save command.','Save حکم میں تمام متغیرات کے نام دے کر ایک سے زیادہ متغیر محفوظ کیے جا سکتے ہیں۔','د Save امر ته د ټولو متحولونو د نومونو په ورکولو سره له یوه څخه ډېر متحولونه خوندي کولای شئ.'))
add(('If you make a mistake in a command or want to change a command, you can go back and edit the command.','اگر حکم میں کوئی غلطی ہو جائے یا آپ اسے بدلنا چاہیں تو واپس جا کر حکم میں ترمیم کر سکتے ہیں۔','که په امر کې تېروتنه وکړئ یا یې بدلول غواړئ، بېرته تللای او امر سمولای شئ.'))
add(('MAPLE calculates fractions (exact arithmetic) unless you specify that you want decimals (floating-point arithmetic) with the evalf function.','MAPLE کسروں کی صورت میں عین حساب کرتا ہے، جب تک آپ evalf تفاعل کے ذریعے اعشاری یعنی فلوٹنگ پوائنٹ حساب کی درخواست نہ کریں۔','MAPLE د کسرونو په بڼه دقیق حساب کوي، مګر دا چې د evalf تابع په وسیله اعشاري، یعنې فلوټینګ پواینټ حساب وغواړئ.'))
add(('("evalf" stands for "evaluate using floating-point arithmetic").','("evalf" کا مطلب ہے "فلوٹنگ پوائنٹ حساب کے ذریعے قیمت معلوم کرنا")۔','("evalf" د "فلوټینګ پواینټ حساب په وسیله د ارزښت معلومولو" لنډون دی).'))
add(
 ('The argument 4 in the evalf command specifies the number of significant figures you want in the result.','evalf حکم میں دلیل 4 نتیجے کے مطلوبہ معنی خیز ہندسوں کی تعداد بتاتی ہے۔','د evalf په امر کې د 4 آرګومېنټ په پایله کې د غوښتل شوو با ارزښته رقمونو شمېر ټاکي.'),
 ('If you omit this command, you will get ten significant figures:','اگر آپ یہ حکم چھوڑ دیں تو دس معنی خیز ہندسے ملیں گے:','که دا امر پرېږدئ، لس با ارزښته رقمونه به ترلاسه کړئ:')
)
add(
 ('To clear the internal memory during a maple session.','میپل کے سیشن کے دوران اندرونی حافظہ صاف کرنے کے لیے۔','د میپل د کاري ناستې پر مهال د داخلي حافظې د پاکولو لپاره.'),
 ("We use 'restart' command or click the restart icon on the tool bar of the worksheet.",'ہم restart حکم استعمال کرتے ہیں یا ورک شیٹ کی ٹول بار پر restart آئیکن پر کلک کرتے ہیں۔','موږ د restart امر کاروو یا د کاري پاڼې د وسایلو په پټه کې د restart پر نښه کلیک کوو.'),
 ('e.g.','مثلاً،','د بېلګې په توګه،')
)
add(
 ('when you enter this command, the maple session returns to its startup state.','یہ حکم درج کرنے پر میپل کا سیشن اپنی ابتدائی حالت میں واپس آ جاتا ہے۔','کله چې دا امر ولیکئ، د میپل کاري ناسته خپل لومړني حالت ته ستنېږي.'),
 ('All the values reset to their initial values.','تمام قیمتیں اپنی ابتدائی قیمتوں پر واپس آ جاتی ہیں۔','ټول ارزښتونه خپلو لومړنیو ارزښتونو ته بېرته ګرځي.')
)
add(
 ('Use the colon-equal symbol (:=) to define variables that is, to assign values to them.','متغیرات کی تعریف یعنی انہیں قیمتیں دینے کے لیے کولن اور مساوی کی علامت (:=) استعمال کریں۔','د متحولونو د تعریف، یعنې هغوی ته د ارزښتونو د ټاکلو لپاره د کولن او مساوي نښه (:=) وکاروئ.'),
 ('Once you have defined a variable, simply typing its name will show its value, and using the name in a formula will cause the value to be substituted.','متغیر کی تعریف کرنے کے بعد صرف اس کا نام لکھنے سے اس کی قیمت ظاہر ہوگی، اور فارمولے میں نام استعمال کرنے سے اس کی قیمت اس کی جگہ آ جائے گی۔','کله چې مو متحول تعریف کړ، یوازې د نوم په لیکلو یې ارزښت ښودل کېږي او په فورمول کې د نوم په کارولو یې ارزښت د نوم ځای نیسي.'),
 ('For example,','مثلاً،','د بېلګې په توګه،')
)
add(('If you want to string commands together on the same line, then:','اگر آپ کئی احکامات کو ایک ہی سطر میں لکھنا چاہیں تو:','که غواړئ څو امرونه په یوه کرښه کې سره ولیکئ، نو:'))
add(('You click-start, then select-program <Maple 18 <click-"Maple Calculator" to obtain:','Start پر کلک کریں، پھر Program، Maple 18 اور "Maple Calculator" منتخب کریں تاکہ یہ حاصل ہو:','پر Start کلیک وکړئ، بیا Program، Maple 18 او "Maple Calculator" وټاکئ، څو دا ترلاسه کړئ:'))
add(
 ('This graphical scientific calculator is available for use as part of your Maple(TM) installation or via a Web Server running MapleNet(TM).','یہ گرافیکی سائنسی کیلکولیٹر آپ کے نصب کردہ Maple(TM) کے حصے کے طور پر یا MapleNet(TM) چلانے والے ویب سرور کے ذریعے دستیاب ہے۔','دا ګرافیکي ساینسي حسابګر ستاسو د نصب شوي Maple(TM) د یوې برخې په توګه یا د MapleNet(TM) چلوونکي وېب سرور له لارې کارول کېدای شي.'),
 ('This calculator use Maple for calculations.','یہ کیلکولیٹر حساب کے لیے میپل استعمال کرتا ہے۔','دا حسابګر د محاسبو لپاره میپل کاروي.')
)
add(('use the "setting tab" to control the basic computation settings for the calculator.','کیلکولیٹر کی بنیادی حسابی ترتیبات بدلنے کے لیے "setting tab" استعمال کریں۔','د حسابګر د محاسبې د بنسټیزو تنظیماتو د بدلولو لپاره "setting tab" وکاروئ.'))
add(('use the "Math tab" to select the functions to apply, from basic functions to linear algebra to statistics.','بنیادی تفاعل سے خطی الجبرا اور شماریات تک مطلوبہ تفاعل منتخب کرنے کے لیے "Math tab" استعمال کریں۔','له بنسټیزو تابعونو تر خطي الجبر او احصایې پورې د کارېدونکو تابعونو د ټاکلو لپاره "Math tab" وکاروئ.'))
add(('use the "Graph tab" to control how graphs are displayed and what they display.','گراف کیسے دکھائے جائیں اور کیا دکھائیں، یہ طے کرنے کے لیے "Graph tab" استعمال کریں۔','د دې د ټاکلو لپاره چې ګرافونه څنګه او څه وښيي، "Graph tab" وکاروئ.'))
add(('use the "Data tab" to control the data used to produce a graph or the data to be tabulated directly.','گراف بنانے کے لیے استعمال ہونے والے ڈیٹا یا براہِ راست جدول میں دکھائے جانے والے ڈیٹا کو سنبھالنے کے لیے "Data tab" استعمال کریں۔','د ګراف د جوړولو لپاره د کارېدونکو معلوماتو یا په مستقیم ډول په جدول کې د ښودل کېدونکو معلوماتو د اداره کولو لپاره "Data tab" وکاروئ.'))
add(('use the "Variable tab" to control the variables you have assigned and their values.','جن متغیرات کو آپ نے قیمتیں دی ہیں، ان اور ان کی قیمتوں کو سنبھالنے کے لیے "Variable tab" استعمال کریں۔','د هغو متحولونو او ارزښتونو د اداره کولو لپاره چې تاسو ټاکلي دي، "Variable tab" وکاروئ.'))
add(
 ('To involve the graphical calculator, use your mouse to press the "Math tab" and select functions to apply.','گرافیکی کیلکولیٹر استعمال کرنے کے لیے ماؤس سے "Math tab" پر کلک کریں اور مطلوبہ تفاعل منتخب کریں۔','د ګرافیکي حسابګر د کارولو لپاره په موږک د "Math tab" پر ټب کلیک وکړئ او اړین تابعونه وټاکئ.'),
 ('This will build your expression in the input area, which is just below the session history area on the left side of the calculator.','اس سے آپ کی عبارت اندراج کے حصے میں بنے گی، جو کیلکولیٹر کے بائیں طرف سیشن کی سابقہ کارروائی کے حصے کے عین نیچے ہے۔','په دې سره به ستاسو عبارت د ننویستلو په برخه کې جوړ شي، چې د حسابګر په کیڼ لوري کې د کاري ناستې د مخینې د برخې سم لاندې ده.'),
 ('When you are ready to evaluate your expression, press ENTER key on your keyboard.','عبارت کی قیمت معلوم کرنے کے لیے تیار ہوں تو کی بورڈ پر ENTER دبائیں۔','کله چې د خپل عبارت د ارزښت معلومولو ته چمتو شئ، د کیبورډ ENTER کیلي کېکاږئ.'),
 ('Alternatively, you can press the "Graph button", to graph the expression, or the "data button", to tabulate values for the expression.','اس کے بجائے عبارت کا گراف بنانے کے لیے "Graph button" یا اس کی قیمتوں کا جدول بنانے کے لیے "data button" دبا سکتے ہیں۔','یا د عبارت د ګراف د جوړولو لپاره "Graph button" او د عبارت د ارزښتونو د جدول د جوړولو لپاره "data button" کېکاږئ.')
)
add(
 (r'Differentiate \(f(x)=x^2+4x+4\) with respect to x at a point x = 2.','مقام x = 2 پر x کے لحاظ سے f(x)=x²+4x+4 کا مشتق معلوم کریں۔','په x = 2 نقطه کې د x په نسبت د f(x)=x²+4x+4 مشتق ومومئ.'),
 ('The steps required for obtaining the graphing-calculator result are:','گرافیکی کیلکولیٹر سے نتیجہ حاصل کرنے کے مراحل یہ ہیں:','له ګرافیکي حسابګر څخه د پایلې د ترلاسه کولو اړین پړاوونه دا دي:')
)
add(('Click-Math tab < Click-Calculus < Click-Differentiate to obtain:','یہ حاصل کرنے کے لیے Math tab، پھر Calculus اور پھر Differentiate پر کلک کریں:','د دې د ترلاسه کولو لپاره پر Math tab، بیا Calculus او بیا Differentiate کلیک وکړئ:'))
add((r'Cursor “1” requires A: the expression \(x^2+4x+4\), X: the differentiation of \(f(x)\) with respect to x and P: the differentiation of \(f(x)\) at a point x=2.','کرسر “1” کے لیے A میں عبارت x²+4x+4، X میں وہ متغیر x جس کے لحاظ سے f(x) کا مشتق لینا ہے، اور P میں مقام x=2 درکار ہیں جہاں مشتق کی قیمت معلوم کرنی ہے۔','کرسر “1” ته A: د x²+4x+4 عبارت، X: هغه x متحول چې په نسبت یې د f(x) مشتق اخیستل کېږي، او P: هغه x=2 نقطه پکار ده چې د مشتق ارزښت پکې معلومېږي.'))
add(('Click-ENTER','ENTER پر کلک کریں۔','پر ENTER کلیک وکړئ.'))
add(
 (r'Integrate \(x^2+4x+4\), with respect to x over the interval [0,1].','وقفہ [0,1] پر x کے لحاظ سے x²+4x+4 کا تکمل معلوم کریں۔','په [0,1] واټن کې د x په نسبت د x²+4x+4 انتګرال ومومئ.'),
 ('The graphing – calculator result is as under:','گرافیکی کیلکولیٹر کا نتیجہ درج ذیل ہے:','د ګرافیکي حسابګر پایله لاندې ده:')
)
add((r'Cursor “1” requires A: the function \(x^2+4x+4\), X: the integration of \(f(x)\) with respect to x, P: the lower limit x = 0 and Q: the upper limit x = 1 of the integral.','کرسر “1” کے لیے A میں تفاعل x²+4x+4، X میں وہ متغیر x جس کے لحاظ سے f(x) کا تکمل لینا ہے، P میں نچلی حد x=0 اور Q میں تکمل کی بالائی حد x=1 درکار ہیں۔','کرسر “1” ته A: د x²+4x+4 تابع، X: هغه x متحول چې په نسبت یې د f(x) انتګرال اخیستل کېږي، P: د انتګرال ښکته حد x=0 او Q: پورته حد x=1 پکار دي.'))
add(('To use maple as a calculator simply type in your worksheet command prompt e.g.','میپل کو کیلکولیٹر کے طور پر استعمال کرنے کے لیے اپنی ورک شیٹ میں حکم درج کرنے کی جگہ پر لکھیں، مثلاً:','د حسابګر په توګه د میپل د کارولو لپاره د خپلې کاري پاڼې د امر د ننویستلو په ځای کې ولیکئ، د بېلګې په توګه:'))
add(('Then you will see the unit calculator as shown in the Figure 1.3.','پھر اکائیوں کا کیلکولیٹر شکل 1.3 کے مطابق دکھائی دے گا۔','بیا به د واحدونو حسابګر ووینئ، لکه په 1.3 شکل کې چې ښودل شوی دی.'))
add(
 ('You can get help with MAPLE syntax by using the HELP menu, as described previously.','جیسا کہ پہلے بیان کیا گیا، HELP مینیو کے ذریعے MAPLE کے نحوی قواعد کی مدد حاصل کر سکتے ہیں۔','لکه مخکې چې بیان شوي، د HELP مېنو په کارولو د MAPLE د نحوي قواعدو په اړه مرسته ترلاسه کولای شئ.'),
 ('If you have a question about a particular command, you can quickly get help by typing a question mark followed by the name (no semicolon).','اگر کسی خاص حکم کے بارے میں سوال ہو تو سوالیہ نشان کے بعد اس کا نام لکھ کر فوراً مدد حاصل کریں؛ سیمی کولن نہ لگائیں۔','که د یوه ځانګړي امر په اړه پوښتنه لرئ، د پوښتنې نښې وروسته یې د نوم په لیکلو ژر مرسته ترلاسه کولای شئ؛ سیمي کولن مه لیکئ.'),
 ('For example,','مثلاً،','د بېلګې په توګه،')
)
add(
 ('will open a window containing information about what the “addition” does and how to use it as shown in Figure 1.4.','اس سے ایک ونڈو کھلے گی جس میں “addition” کے کام اور استعمال کی معلومات ہوں گی، جیسا کہ شکل 1.4 میں دکھایا گیا ہے۔','دا به داسې کړکۍ پرانیزي چې د “addition” د کار او کارولو په اړه معلومات پکې وي، لکه په 1.4 شکل کې چې ښودل شوي دي.'),
 ('Click on the little “Cross” box at the upper left of the window to close down the little window.','چھوٹی ونڈو بند کرنے کے لیے اس کے اوپر بائیں جانب موجود چھوٹے “Cross” خانے پر کلک کریں۔','د کوچنۍ کړکۍ د تړلو لپاره د کړکۍ په پاس کیڼ لوري کې د “Cross” پر کوچني بکس کلیک وکړئ.')
)
