from physics_agent2_sequential import save_page
from physics_agent2_translations import TRANSLATIONS, TITLES
from physics_agent2_layout import LAYOUT

def line_diagram(ident, signs, distances):
    svg=f'<svg viewBox="0 0 520 125" role="img" aria-label="Three collinear point charges" style="width:100%;max-width:560px"><defs><marker id="{ident}" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8Z" fill="#334155"/></marker></defs>'
    for index, (x, sign) in enumerate(zip([65,245,445], signs),1):
        svg+=f'<circle cx="{x}" cy="70" r="18" fill="{"#f9a8d4" if sign=="+" else "#cffafe"}" stroke="#334155"/><text x="{x-6}" y="76" font-size="20">{sign}</text><text x="{x-10}" y="35">q{index}</text>'
    for lo,hi,label in [(85,225,distances[0]),(265,425,distances[1])]:
        svg+=f'<line x1="{lo}" y1="70" x2="{hi}" y2="70" stroke="#334155" marker-start="url(#{ident})" marker-end="url(#{ident})"/><text x="{(lo+hi)//2-16}" y="55">{label}</text>'
    return svg+'</svg>'

MEDIA=[
 r'Obviously the \(\varepsilon_r\) is dimensionless constant and its value is always greater than unity for various dielectrics. The values of relative permittivity for various dielectrics are given in table 11.1.',
 r'The force in a medium of relative permittivity \(\varepsilon_r\) is given by',
 r'\(\vec F_{\mathrm{med}}=\frac{1}{4\pi\varepsilon_0\varepsilon_r}\frac{q_1q_2}{r^2}\hat r\) … (11.7)',
 r'\(\vec F_{\mathrm{med}}=\frac{\vec F_{\mathrm{vac}}}{\varepsilon_r}\) … (11.8)',
]
ROWS=[['Material','εr'],['Vacuum','1'],['Air','1.0006'],['Benzene','2.284'],['Germinium','16'],['Water','78.5'],['Glass','4.8–10'],['Mica','3–7.5'],['Paraffine paper','2'],['Rubber','2.94'],['Ammonia (liquid)','22–25']]
PROBLEM=r'Three charges \(q_1=-5\,\mu\mathrm C\), \(q_2=+10\,\mu\mathrm C\) and \(q_3=-12\,\mu\mathrm C\) are placed in a line as shown in figure. Calculate the net electrostatic force on charge \(q_2\) due to the other two charges.'
GIVEN=[r'Charge \(q_1=-5\,\mu\mathrm C=-5\times10^{-6}\,\mathrm C\)',r'Charge \(q_2=+10\,\mu\mathrm C=+10\times10^{-6}\,\mathrm C\)',r'Charge \(q_3=-12\,\mu\mathrm C=-12\times10^{-6}\,\mathrm C\)',r'\(k=9\times10^9\;\mathrm{N\,m^2\,C^{-2}}\)',r'The distance between charge \(q_1\) and \(q_2\): \(r_{12}=6\,\mathrm{cm}=0.06\,\mathrm m=6\times10^{-2}\,\mathrm m\)',r'The distance between charge \(q_2\) and \(q_3\): \(r_{23}=4\,\mathrm{cm}=0.04\,\mathrm m=4\times10^{-2}\,\mathrm m\)']
EXAMPLE=[PROBLEM,'GIVEN',*GIVEN,'REQUIRED',r'The magnitude of net electrostatic force on charge \(q_2\): \(F_{\mathrm{net}}=?\)','The direction of electrostatic force = ?']
SOLUTION=[
 r'Electrostatic force on charge \(q_2\) due to charge \(q_1\): \(F_{21}=k\frac{q_1q_2}{r_{12}^2}\)',
 r'\(F_{21}=9.0\times10^9\;\mathrm{N\,m^2\,C^{-2}}\frac{(5\times10^{-6}\,\mathrm C)(10\times10^{-6}\,\mathrm C)}{(6\times10^{-2}\,\mathrm m)^2}\)',
 r'\(=9.0\times10^9\;\mathrm{N\,m^2\,C^{-2}}\frac{50\times10^{-12}\,\mathrm{C^2}}{36\times10^{-4}\,\mathrm{m^2}}=125\,\mathrm N\)',
 r'Electrostatic force on charge \(q_2\) due to \(q_3\):',
 r'\(F_{23}=9.0\times10^9\;\mathrm{N\,m^2\,C^{-2}}\frac{(10\times10^{-6}\,\mathrm C)(12\times10^{-6}\,\mathrm C)}{4\times10^{-2}\,\mathrm m}\)',
 r'\(=9.0\times10^9\;\mathrm{N\,m^2\,C^{-2}}\frac{120\times10^{-12}\,\mathrm{C^2}}{16\times10^{-4}\,\mathrm{m^2}}\)',
 r'\(=\frac{1080\times10^{-3}}{16\times10^{-4}}\,\mathrm N=675\,\mathrm N\)',
 r'The net electrostatic force on charge \(q_2\), printed as \(F_2=F_{21}-F_{23}\):',
 r'\(675\,\mathrm N-125\,\mathrm N=550\,\mathrm N\)',
 r'The direction of the net electrostatic force on charge \(q_2\) points towards charge \(q_3\) (points to the right).',
 r'Source clarification: the first printed substitution for \(F_{23}\) omits the square on the distance; the next line correctly uses \(16\times10^{-4}\,\mathrm{m^2}\). The printed net-force labels are reversed relative to the subtraction \(675-125\). Taking right as positive gives \(F_2=F_{23}-F_{21}=+550\,\mathrm N\). The original printed statements are retained above; these are textbook typographical inconsistencies.',
]
ASSIGNMENT=[r'Three charges \(+q_1=5\,\mu\mathrm C\), \(+q_2=10\,\mu\mathrm C\) and \(q_3\) are placed as shown in the figure. What is the electrostatic charge on \(q_3\) if the net electrostatic force on charge \(q_2\) is zero?',r'Printed answer: \(20\times10^{-6}\,\mathrm C\).']

def prepare():
    TITLES.update({
      'phys12-front-media6':('مادی واسطے میں قوت','په مادي منځني کې قوه'),
      'phys12-front-table111':('جدول 11.1: مختلف عازلوں کی نسبتی نفوذ پذیری','جدول 11.1: د بېلابېلو عایقونو نسبي نفوذپذیري'),
      'phys12-front-example111':('مثال 11.1: سوال اور دی گئی معلومات','بېلګه 11.1: پوښتنه او ورکړل شوي معلومات'),
      'phys12-front-solution111':('مثال 11.1: کتاب کا حل','بېلګه 11.1: د کتاب حل'),
      'phys12-front-assignment111':('تفویض کردہ سوال 11.1','سپارل شوې پوښتنه 11.1'),
    })
    TRANSLATIONS['phys12-front-media6']=[
      (r'نسبتی نفوذ پذیری \(\varepsilon_r\) بے بُعد مستقل ہے اور مختلف عازلوں کے لیے اس کی قیمت ایک سے زیادہ ہوتی ہے۔ مختلف عازلوں کی نسبتی نفوذ پذیری کی قیمتیں جدول 11.1 میں دی گئی ہیں۔',r'نسبي نفوذپذیري \(\varepsilon_r\) بې بُعده ثابت دی او د بېلابېلو عایقونو لپاره یې ارزښت له یو څخه زیات وي. د بېلابېلو عایقونو د نسبي نفوذپذیرۍ ارزښتونه په جدول 11.1 کې ورکړل شوي دي.'),
      (r'نسبتی نفوذ پذیری \(\varepsilon_r\) والے واسطے میں قوت یوں دی جاتی ہے:',r'د نسبي نفوذپذیرۍ \(\varepsilon_r\) لرونکي منځني کې قوه داسې ورکول کېږي:'),
      (MEDIA[2],MEDIA[2]),(MEDIA[3],MEDIA[3]),
    ]
    TRANSLATIONS['phys12-front-table111']=[
      ('مادہ — εr','ماده — εr'),('خلا — 1','تشه فضا — 1'),('ہوا — 1.0006','هوا — 1.0006'),('بینزین — 2.284','بینزین — 2.284'),('جرمینیم — 16','جرمینیم — 16'),('پانی — 78.5','اوبه — 78.5'),('شیشہ — 4.8–10','ښیښه — 4.8–10'),('ابرق — 3–7.5','میکا — 3–7.5'),('پیرافین کاغذ — 2','پارافین کاغذ — 2'),('ربڑ — 2.94','ربړ — 2.94'),('امونیا (مائع) — 22–25','امونیا (مایع) — 22–25'),
    ]
    TRANSLATIONS['phys12-front-example111']=[
      (r'تین بار \(q_1=-5\,\mu\mathrm C\)، \(q_2=+10\,\mu\mathrm C\) اور \(q_3=-12\,\mu\mathrm C\) شکل کے مطابق ایک سیدھی لکیر پر رکھے گئے ہیں۔ باقی دو باروں کی وجہ سے \(q_2\) پر خالص برقی سکونی قوت معلوم کریں۔',r'درې چارجونه \(q_1=-5\,\mu\mathrm C\)، \(q_2=+10\,\mu\mathrm C\) او \(q_3=-12\,\mu\mathrm C\) د شکل له مخې پر یوه نېغه کرښه ایښودل شوي. د نورو دوو چارجونو له امله پر \(q_2\) خالصه ساکنه برېښنايي قوه محاسبه کړئ.'),
      ('دی گئی معلومات','ورکړل شوي معلومات'),
      *[(text.replace('Charge','بار'),text.replace('Charge','چارج')) for text in GIVEN[:3]],
      (GIVEN[3],GIVEN[3]),
      (r'بار \(q_1\) اور \(q_2\) کے درمیان فاصلہ: \(r_{12}=6\,\mathrm{cm}=0.06\,\mathrm m=6\times10^{-2}\,\mathrm m\)',r'د \(q_1\) او \(q_2\) چارجونو ترمنځ واټن: \(r_{12}=6\,\mathrm{cm}=0.06\,\mathrm m=6\times10^{-2}\,\mathrm m\)'),
      (r'بار \(q_2\) اور \(q_3\) کے درمیان فاصلہ: \(r_{23}=4\,\mathrm{cm}=0.04\,\mathrm m=4\times10^{-2}\,\mathrm m\)',r'د \(q_2\) او \(q_3\) چارجونو ترمنځ واټن: \(r_{23}=4\,\mathrm{cm}=0.04\,\mathrm m=4\times10^{-2}\,\mathrm m\)'),
      ('مطلوب','غوښتل شوي'),
      (r'بار \(q_2\) پر خالص برقی سکونی قوت کی مقدار: \(F_{\mathrm{net}}=?\)',r'پر چارج \(q_2\) د خالصې ساکنې برېښنايي قوې مقدار: \(F_{\mathrm{net}}=?\)'),
      ('برقی سکونی قوت کی سمت = ؟','د ساکنې برېښنايي قوې لوری = ؟'),
    ]
    TRANSLATIONS['phys12-front-solution111']=[
      (r'بار \(q_1\) کی وجہ سے \(q_2\) پر برقی سکونی قوت: \(F_{21}=k\frac{q_1q_2}{r_{12}^2}\)',r'د \(q_1\) چارج له امله پر \(q_2\) ساکنه برېښنايي قوه: \(F_{21}=k\frac{q_1q_2}{r_{12}^2}\)'),
      (SOLUTION[1],SOLUTION[1]),(SOLUTION[2],SOLUTION[2]),
      (r'بار \(q_3\) کی وجہ سے \(q_2\) پر برقی سکونی قوت:',r'د \(q_3\) چارج له امله پر \(q_2\) ساکنه برېښنايي قوه:'),
      (SOLUTION[4],SOLUTION[4]),(SOLUTION[5],SOLUTION[5]),(SOLUTION[6],SOLUTION[6]),
      (r'بار \(q_2\) پر خالص قوت، کتاب میں \(F_2=F_{21}-F_{23}\) لکھی گئی ہے:',r'پر چارج \(q_2\) خالصه قوه، په کتاب کې \(F_2=F_{21}-F_{23}\) لیکل شوې ده:'),
      (SOLUTION[8],SOLUTION[8]),
      (r'بار \(q_2\) پر خالص برقی سکونی قوت کی سمت بار \(q_3\) کی طرف، یعنی دائیں جانب، ہے۔',r'پر چارج \(q_2\) د خالصې ساکنې برېښنايي قوې لوری د \(q_3\) چارج په لور، یعنې ښي خوا ته، دی.'),
      (r'اصل کتاب کی وضاحت: \(F_{23}\) میں پہلی بار قیمتیں رکھنے کی سطر میں فاصلے کا مربع چھوٹ گیا ہے؛ اگلی سطر میں درست طور پر \(16\times10^{-4}\,\mathrm{m^2}\) ہے۔ خالص قوت کے چھپے ہوئے نام تفریق \(675-125\) کے مقابل الٹ ہیں۔ دائیں سمت کو مثبت لینے پر \(F_2=F_{23}-F_{21}=+550\,\mathrm N\) حاصل ہوتا ہے۔ اصل چھپی عبارت اوپر محفوظ ہے؛ یہ کتاب کی طباعتی بے قاعدگیاں ہیں۔',r'د اصلي کتاب وضاحت: د \(F_{23}\) د ارزښتونو د ایښودلو په لومړۍ کرښه کې د واټن مربع پاتې شوی؛ په بله کرښه کې په سمه توګه \(16\times10^{-4}\,\mathrm{m^2}\) شته. د خالصې قوې چاپ شوي نومونه د \(675-125\) تفریق په پرتله سرچپه دي. د ښي لوري په مثبت نیولو \(F_2=F_{23}-F_{21}=+550\,\mathrm N\) ترلاسه کېږي. اصلي چاپ شوې عبارت پورته ساتل شوی؛ دا د کتاب چاپي ناسموالي دي.'),
    ]
    TRANSLATIONS['phys12-front-assignment111']=[
      (r'تین بار \(+q_1=5\,\mu\mathrm C\)، \(+q_2=10\,\mu\mathrm C\) اور \(q_3\) شکل کے مطابق رکھے گئے ہیں۔ اگر \(q_2\) پر خالص برقی سکونی قوت صفر ہو تو \(q_3\) پر برقی بار کتنا ہو گا؟',r'درې چارجونه \(+q_1=5\,\mu\mathrm C\)، \(+q_2=10\,\mu\mathrm C\) او \(q_3\) د شکل له مخې ایښودل شوي. که پر \(q_2\) خالصه ساکنه برېښنايي قوه صفر وي، نو د \(q_3\) برېښنايي چارج به څومره وي؟'),
      (r'کتاب میں دیا گیا جواب: \(20\times10^{-6}\,\mathrm C\)۔',r'په کتاب کې ورکړل شوی ځواب: \(20\times10^{-6}\,\mathrm C\).'),
    ]
    LAYOUT.update({
      'phys12-front-media6':[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'equation','indices':[3]}],
      'phys12-front-table111':[{'type':'table','indices':list(range(11))}],
      'phys12-front-example111':[{'type':'paragraph','indices':[0]},{'type':'heading','indices':[1]},{'type':'lines','indices':list(range(2,8))},{'type':'visual'},{'type':'heading','indices':[8]},{'type':'lines','indices':[9,10]}],
      'phys12-front-solution111':[{'type':'paragraph' if i in [0,3,7,9,10] else 'equation','indices':[i]} for i in range(11)],
      'phys12-front-assignment111':[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'visual'}],
    })

def records():
    example_diagram=line_diagram('phys12-example111',['−','+','−'],['6 cm','4 cm'])
    refs=[{'pdfPage':8,'printedPage':6},{'pdfPage':8,'printedPage':7}]
    return [
      {'id':'phys12-front-media6','printedPage':6,'title':'Coulomb’s law in material media — Continued','kind':'lesson','paragraphs':MEDIA,'formulas':[{'number':'11.7','latex':r'\vec F_{\mathrm{med}}=\frac{q_1q_2}{4\pi\varepsilon_0\varepsilon_r r^2}\hat r'},{'number':'11.8','latex':r'\vec F_{\mathrm{med}}=\vec F_{\mathrm{vac}}/\varepsilon_r'}]},
      {'id':'phys12-front-table111','printedPage':6,'title':'Table 11.1: The relative permittivity of various dielectrics','kind':'lesson','paragraphs':[],'rows':ROWS},
      {'id':'phys12-front-example111','printedPage':6,'title':'Example 11.1 — Given and required','kind':'lesson','paragraphs':EXAMPLE,'diagramHtml':example_diagram,'diagrams':[{'type':'collinear-charges','chargesMicroC':[-5,10,-12],'distancesCm':[6,4]}]},
      {'id':'phys12-front-solution111','printedPage':7,'title':'Example 11.1 — Solution','kind':'lesson','paragraphs':SOLUTION,
       'workedExamples':[{'id':'textbook-example-1','num':'11.1','title':'Example 11.1','problem':PROBLEM,'given':GIVEN,'steps':SOLUTION[:10],'answer':'550 N towards q₃ (to the right)','solutionOrigin':'textbook','sourceReferences':refs,'sourceClarifications':[SOLUTION[10]],'diagramSvg':example_diagram}]},
      {'id':'phys12-front-assignment111','printedPage':7,'title':'Assignment 11.1','kind':'lesson','paragraphs':ASSIGNMENT,'diagramHtml':line_diagram('phys12-assignment111',['+','+','+'],['2 cm','4 cm']),
       'exercises':[{'id':'assignment-11-1','exercise':'Assignment 11.1','title':'Assignment 11.1','problems':[{'id':'assignment-11-1-q1','qNo':'1','question':ASSIGNMENT[0],'answer':r'20\times10^{-6}\,\mathrm C','solution':'The textbook supplies the answer only; no worked solution is printed here.','solutionOrigin':'textbook answer','sourceReferences':[{'pdfPage':8,'printedPage':7}],'diagramSvg':line_diagram('phys12-assignment111-exercise',['+','+','+'],['2 cm','4 cm'])}]}]},
    ]

if __name__ == '__main__':
    prepare()
    save_page(8,records())
