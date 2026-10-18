from physics_agent2_sequential import save_page
from physics_agent2_translations import TRANSLATIONS, TITLES
from physics_agent2_layout import LAYOUT

SOLUTION=[
 'REQUIRED: electric field E = ?',
 'SOLUTION: Using electric field intensity formulae',
 r'\(E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\)',
 r'\(=(9\times10^9\,\mathrm{N\,m^2\,C^{-2}})\frac{3\times10^{-6}\,\mathrm C}{(0.3\,\mathrm m)^2}\)',
 r'\(=3\times10^5\,\mathrm{N\,C^{-1}}\)',
]
LINES=[
 'In the previous section, the vector nature of the electric field strength was discussed. An electric field can be used in the pictorial form to describe the overall intensity of the field around it. This pictorial representation is called the electric field lines.',
 'An electric field line is an imaginary line or curve drawn through a region of empty space. The direction of the electric field at point A, B, C and D is tangent to the field line through that point.',
 'The electric field lines, point in the direction that a positive test charge would accelerate if placed upon the line. The arrows indicate the electric field at different points. The direction of these arrows is outward for positive charge and is inward for negative charge as shown in Fig: 11.4.',
 'The field lines starts from positive charge and terminate at negative charge as shown in Fig: (11.5)',
 'Fig: 11.6 show two infinitely large parallel plates separated by a very small distance. The upper plate has a uniform positive charge distribution while the lower plate has a negative one. If the plates are not of infinite length, the field lines at the ends of plates will be a little bulging out, showing that field is not uniform at the ends. The field such as at the ends of plates is called “fringing field”.',
 'Another interesting property of field lines can be explained with the help of Fig. 11.7. Suppose that a charge +q is placed near a metal plate. The positive charge will attract the negative charges (electrons) in the metal plate, resulting in the motion of these charges until some of them reach that surface of the metal which is near to +q charge where they will be at rest. The electric lines of force cannot pass through a conductor. Therefore electric field is zero inside a conductor.',
]
PHOTO=['PHOTOCOPIERS: The copying process of photocopier is called xerography. It consists of a drum which is made up of aluminum and is coated with selenium.']

def prepare():
 TITLES.update({'phys12-front-example112-solution':('مثال 11.2: حل','بېلګه 11.2: حل'),'phys12-front-field-lines':('11.2.1 خطوط کے ذریعے برقی میدان کی نمائندگی','11.2.1 د کرښو په وسیله د برېښنايي میدان ښودنه'),'phys12-front-photocopier-start':('برقِ سکونی کے اطلاقات: فوٹو کاپی مشین','د ساکنې برېښنا کارونې: فوټو کاپي ماشین')})
 TRANSLATIONS['phys12-front-example112-solution']=[('مطلوب: برقی میدان E = ؟','مطلوب: برېښنايي میدان E = ؟'),('حل: برقی میدان کی شدت کا فارمولا استعمال کرتے ہوئے','حل: د برېښنايي میدان د شدت د فورمول په کارولو سره')]+[(p,p) for p in SOLUTION[2:]]
 TRANSLATIONS['phys12-front-field-lines']=[
 ('پچھلے حصے میں برقی میدان کی شدت کی سمتی نوعیت بیان کی گئی۔ برقی میدان کو تصویری صورت میں دکھا کر اس کے گرد میدان کی مجموعی شدت بیان کی جا سکتی ہے۔ اس تصویری نمائندگی کو برقی میدان کے خطوط کہتے ہیں۔','په تېرې برخې کې د برېښنايي میدان د شدت ویکټوري ځانګړنه بیان شوه. برېښنايي میدان په انځوریزه بڼه ښودل کېدای شي څو د هغه شاوخوا د میدان ټولیز شدت بیان شي. دې انځوریزې ښودنې ته د برېښنايي میدان کرښې ویل کېږي.'),
 ('برقی میدان کا خط خالی فضا کے کسی خطے میں کھینچا گیا فرضی خط یا منحنی ہے۔ نقاط A، B، C اور D پر برقی میدان کی سمت اس نقطے سے گزرنے والے خطِ میدان کے مماس کی سمت ہوتی ہے۔','د برېښنايي میدان کرښه یوه خیالي کرښه یا منحني ده چې د تشې فضا په یوه سیمه کې رسمېږي. په A، B، C او D نقطو کې د برېښنايي میدان لوری د هغې نقطې د میدان کرښې د مماس لوری وي.'),
 ('برقی میدان کے خطوط اس سمت میں ہوتے ہیں جس میں خط پر رکھا گیا مثبت آزمائشی بار اسراع حاصل کرے گا۔ تیر مختلف نقاط پر برقی میدان ظاہر کرتے ہیں۔ مثبت بار کے لیے تیر باہر کی طرف اور منفی بار کے لیے اندر کی طرف ہوتے ہیں، جیسا کہ شکل 11.4 میں دکھایا گیا ہے۔','د برېښنايي میدان کرښې هغه لوری ښيي چې پر کرښه ایښودل شوی مثبت ازمایښتي چارج به پکې تعجیل واخلي. غشي په بېلابېلو نقطو کې برېښنايي میدان ښيي. د مثبت چارج لپاره غشي بهر ته او د منفي چارج لپاره دننه ته وي، لکه په شکل 11.4 کې.'),
 ('خطوطِ میدان مثبت بار سے شروع ہو کر منفی بار پر ختم ہوتے ہیں، جیسا کہ شکل 11.5 میں بیان کیا گیا ہے۔','د میدان کرښې له مثبت چارج څخه پیلېږي او پر منفي چارج پای ته رسېږي، لکه چې د شکل 11.5 په حواله بیان شوي دي.'),
 ('شکل 11.6 میں دو لامحدود بڑی متوازی تختیاں بہت کم فاصلے پر ہیں۔ اوپری تختی پر مثبت بار یکساں تقسیم ہے جبکہ نچلی تختی پر منفی بار ہے۔ اگر تختیاں لامحدود لمبی نہ ہوں تو سروں پر خطوطِ میدان کچھ باہر کو ابھرتے ہیں، جس سے ظاہر ہوتا ہے کہ سروں پر میدان یکساں نہیں ہے۔ تختیوں کے سروں پر اس قسم کے میدان کو کناروں کا میدان، یعنی فرنجنگ فیلڈ کہتے ہیں۔','په شکل 11.6 کې دوه نامحدوده لویې موازي تختې په ډېر لږ واټن کې دي. پر پورتنۍ تختې مثبت چارج په یوشان ډول وېشل شوی او پر لاندې تختې منفي چارج دی. که تختې نامحدودې اوږدې نه وي، د پایونو د میدان کرښې لږ بهر ته پړسېږي، چې ښيي هلته میدان یوشان نه دی. د تختو په پایونو کې دې ډول میدان ته څنډیز میدان یا فرېنجنګ فیلډ ویل کېږي.'),
 ('خطوطِ میدان کی ایک اور خاصیت شکل 11.7 سے سمجھائی جا سکتی ہے۔ فرض کریں بار +q ایک دھاتی تختی کے قریب رکھا جائے۔ مثبت بار تختی کے منفی باروں، یعنی الیکٹرانوں کو اپنی طرف کھینچے گا۔ یہ بار حرکت کرتے ہیں یہاں تک کہ کچھ اس سطح پر پہنچ جائیں جو +q کے قریب ہے، جہاں وہ ساکن ہو جاتے ہیں۔ برقی خطوطِ قوت موصل میں سے نہیں گزر سکتے۔ اس لیے موصل کے اندر برقی میدان صفر ہوتا ہے۔','د میدان د کرښو بله ځانګړنه د شکل 11.7 په مرسته تشریح کېدای شي. فرض کړئ +q چارج د یوې فلزي تختې ترڅنګ کېښودل شي. مثبت چارج د تختې منفي چارجونه، یعنې الکترونونه، جذبوي. دا چارجونه تر هغه حرکت کوي چې ځینې یې +q ته نږدې سطحې ته ورسېږي او هلته ساکن شي. د برېښنايي قوې کرښې له هادي څخه نه شي تېرېدای. له همدې امله د هادي دننه برېښنايي میدان صفر وي.'),
 ]
 TRANSLATIONS['phys12-front-photocopier-start']=[('فوٹو کاپی مشین: فوٹو کاپی کرنے کے عمل کو زیروگرافی کہتے ہیں۔ مشین میں ایلومینیم کا ڈرم ہوتا ہے جس پر سیلینیم کی تہہ چڑھی ہوتی ہے۔','فوټو کاپي ماشین: د فوټو کاپي کولو بهیر ته زېروګرافي ویل کېږي. په ماشین کې له المونیم څخه جوړ شوی ډرم وي چې د سېلینیم پوښ لري.')]
 LAYOUT['phys12-front-example112-solution']=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]}]+[{'type':'equation','indices':[i]} for i in range(2,5)]
 LAYOUT['phys12-front-field-lines']=[{'type':'paragraph','indices':[i]} for i in range(6)]+[{'type':'visual'}]
 LAYOUT['phys12-front-photocopier-start']=[{'type':'paragraph','indices':[0]}]

def records():
 figures=[{'src':f'assets/physics12/figure-{n}.png','alt':caption,'caption':f'Figure {n}: {caption}'} for n,caption in [('11.4','Two equal and opposite charges'),('11.5','Two equal and positive charges placed at certain distance'),('11.6','Uniform electric field between charged plates'),('11.7','Electric lines of force on the surface of metal plate')]]
 return [
 {'id':'phys12-front-example112-solution','printedPage':10,'title':'Example 11.2 — Solution','kind':'lesson','paragraphs':SOLUTION,'workedExamples':[{'id':'textbook-example-2','title':'Example 11.2','problem':'Find electric field at a distance of 30 cm from a 3 μC point charge.','given':['r = 0.3 m','q = 3 × 10⁻⁶ C'],'steps':SOLUTION[1:],'answer':'3 × 10⁵ N C⁻¹','solutionOrigin':'textbook','sourceReferences':[{'pdfPage':9,'printedPage':9},{'pdfPage':10,'printedPage':10}]}]},
 {'id':'phys12-front-field-lines','printedPage':[10,11],'title':'11.2.1 Representation of electric field by lines','kind':'lesson','paragraphs':LINES,'figures':figures,'sourceDefects':['The printed paragraph refers to Figure 11.5 for positive-to-negative field lines, but Figure 11.5 shows two positive charges; Figure 11.4 shows opposite charges. References retained as printed.'],'definitions':[{'term':'Electric field line','text':LINES[1]}]},
 {'id':'phys12-front-photocopier-start','printedPage':11,'title':'Applications of electrostatics — Photocopiers','kind':'lesson','paragraphs':PHOTO,'continuedOnNextPdfPage':11},
 ]

if __name__=='__main__':
 prepare()
 save_page(10,records())
