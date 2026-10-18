from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
EXAMPLE7=[
 ('Figure shows a different combination of capacitors, if the total charge is 600μC. Then determine the values of V1, and C2.','شکل کیپیسٹروں کا ایک مختلف اتصال دکھاتی ہے۔ اگر کل بار 600 مائیکروکولومب ہو، تو V1 اور C2 کی قدریں معلوم کریں۔','شکل د کپاسیټرونو یو بل ترکیب ښيي. که ټول چارج 600 مایکروکولم وي، د V1 او C2 ارزښتونه معلوم کړئ.'),
 ('GIVEN','دی گئی معلومات','ورکړل شوي معلومات'),
 (r'total charge \(Q=600\mu\mathrm C\), capacitance \(C_1=15\mu\mathrm F\), capacitance \(C_3=8\mu\mathrm F\), potential \(V_2=20\mathrm V\)',r'کل بار \(Q=600\mu\mathrm C\)، گنجائش \(C_1=15\mu\mathrm F\)، گنجائش \(C_3=8\mu\mathrm F\)، پوٹینشل \(V_2=20\mathrm V\)',r'ټول چارج \(Q=600\mu\mathrm C\)، ظرفیت \(C_1=15\mu\mathrm F\)، ظرفیت \(C_3=8\mu\mathrm F\)، پوتانشیل \(V_2=20\mathrm V\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 (r'capacitance \(C_2=?\), Potential \(V_1=?\)',r'گنجائش \(C_2=?\)، پوٹینشل \(V_1=?\)',r'ظرفیت \(C_2=?\)، پوتانشیل \(V_1=?\)'),
 ('SOLUTION','حل','حل'),
 (r'P.D. across capacitor \(C_1\): \(V_1=\frac Q{C_1}=\frac{600\times10^{-6}}{15\times10^{-6}}=40\mathrm V\)',r'کیپیسٹر \(C_1\) پر فرقِ برق: \(V_1=\frac Q{C_1}=\frac{600\times10^{-6}}{15\times10^{-6}}=40\mathrm V\)',r'پر کپاسیټر \(C_1\) د پوتانشیل توپیر: \(V_1=\frac Q{C_1}=\frac{600\times10^{-6}}{15\times10^{-6}}=40\mathrm V\)'),
 (r'Total P.D.: \(V=V_1+V_2=40+20=60\mathrm V\)',r'کل فرقِ برق: \(V=V_1+V_2=40+20=60\mathrm V\)',r'ټول د پوتانشیل توپیر: \(V=V_1+V_2=40+20=60\mathrm V\)'),
 (r'Charge on capacitor \(C_3\) is: \(Q_3=C_3\times V_2\)',r'کیپیسٹر \(C_3\) پر بار: \(Q_3=C_3\times V_2\)',r'پر کپاسیټر \(C_3\) چارج: \(Q_3=C_3\times V_2\)'),
 (r'\(=(8\times10^{-6})\times20\)',)*3,
 (r'\(=160\times10^{-6}\mathrm C=160\mu\mathrm C\)',)*3,
 (r'Charge on capacitor \(C_2\) is: \(Q_2=600-160=440\mu\mathrm C\)',r'کیپیسٹر \(C_2\) پر بار: \(Q_2=600-160=440\mu\mathrm C\)',r'پر کپاسیټر \(C_2\) چارج: \(Q_2=600-160=440\mu\mathrm C\)'),
 (r'Capacitance of capacitor \(C_2=\frac{440\times10^{-6}}{20}=22\times10^{-6}\mathrm F=22\mu\mathrm F\)',r'کیپیسٹر \(C_2\) کی گنجائش \(=\frac{440\times10^{-6}}{20}=22\times10^{-6}\mathrm F=22\mu\mathrm F\)',r'د کپاسیټر \(C_2\) ظرفیت \(=\frac{440\times10^{-6}}{20}=22\times10^{-6}\mathrm F=22\mu\mathrm F\)'),
]
EXAMPLE8=[
 (r'A 6μF capacitor is charged to a P.D. of 200V and then connected in parallel with an un-charged 3μF capacitor. Calculate the P.D. across the parallel plate capacitors.',r'ایک 6μF کیپیسٹر کو 200 وولٹ کے فرقِ برق سے بار دیا جاتا ہے اور پھر اسے غیر بار دار 3μF کیپیسٹر کے متوازی جوڑا جاتا ہے۔ متوازی پلیٹوں کے کیپیسٹروں کے درمیان فرقِ برق معلوم کریں۔',r'یو 6μF کپاسیټر د 200 ولټه پوتانشیل توپیر سره چارج کېږي او بیا له یوه بې‌چارج 3μF کپاسیټر سره موازي نښلول کېږي. د موازي تختو کپاسیټرونو ترمنځ د پوتانشیل توپیر محاسبه کړئ.'),
 ('GIVEN','دی گئی معلومات','ورکړل شوي معلومات'),
 (r'Capacitance of charged capacitor \(C_1=6\mu\mathrm F\), Capacitance of un-charged capacitor \(C_2=3\mathrm{pF}\), P.D. of capacitor \(C_1\) is: \(V=200\mathrm V\)',r'بار دار کیپیسٹر کی گنجائش \(C_1=6\mu\mathrm F\)، غیر بار دار کیپیسٹر کی گنجائش \(C_2=3\mathrm{pF}\)، کیپیسٹر \(C_1\) کا فرقِ برق: \(V=200\mathrm V\)',r'د چارج شوي کپاسیټر ظرفیت \(C_1=6\mu\mathrm F\)، د بې‌چارج کپاسیټر ظرفیت \(C_2=3\mathrm{pF}\)، د کپاسیټر \(C_1\) د پوتانشیل توپیر: \(V=200\mathrm V\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 (r'P.D. across the parallel plate capacitors \(V=?\)',r'متوازی پلیٹوں کے کیپیسٹروں کا فرقِ برق \(V=?\)',r'د موازي تختو کپاسیټرونو د پوتانشیل توپیر \(V=?\)'),
 ('SOLUTION','حل','حل'),
 (r'Charge on capacitor \(C_1\) is: \(Q=C_1V=(6\times10^{-6})\times200=0.0012\mathrm C\)',r'کیپیسٹر \(C_1\) پر بار: \(Q=C_1V=(6\times10^{-6})\times200=0.0012\mathrm C\)',r'پر کپاسیټر \(C_1\) چارج: \(Q=C_1V=(6\times10^{-6})\times200=0.0012\mathrm C\)'),
 ('The equivalent capacitance of parallel combination of capacitors is','کیپیسٹروں کے متوازی اتصال کی مساوی گنجائش یہ ہے','د کپاسیټرونو د موازي نښلون معادل ظرفیت دا دی'),
 (r'\(C_{eq}=C_1+C_2=6+3=9\mu\mathrm F\)',)*3,
 ('The charge 0.0012 C is distributed between the two capacitors to have a common P.D.','مشترک فرقِ برق کے لیے 0.0012 کولومب بار دونوں کیپیسٹروں میں تقسیم ہوتا ہے۔','د ګډ پوتانشیل توپیر لپاره 0.0012 کولمب چارج د دواړو کپاسیټرونو ترمنځ وېشل کېږي.'),
 (r'P.D. across parallel plate capacitors: \(V=\frac Q{C_T}=\frac{0.0012}{9\times10^{-6}}=133.3\mathrm V\)',r'متوازی پلیٹوں کے کیپیسٹروں کا فرقِ برق: \(V=\frac Q{C_T}=\frac{0.0012}{9\times10^{-6}}=133.3\mathrm V\)',r'د موازي تختو کپاسیټرونو د پوتانشیل توپیر: \(V=\frac Q{C_T}=\frac{0.0012}{9\times10^{-6}}=133.3\mathrm V\)'),
 (r'[Editorial clarification: the source example statement and GIVEN box specify 3μF, but the GIVEN box later prints 3pF. The solution uses 3μF to obtain 9μF and 133.3V; both printed units are retained.]',r'[ادارتی وضاحت: مثال کے سوال اور GIVEN خانے میں 3μF ہے، لیکن GIVEN خانے میں آگے 3pF چھپا ہے۔ حل میں 3μF استعمال کر کے 9μF اور 133.3V حاصل ہوتے ہیں؛ دونوں چھپی اکائیاں محفوظ ہیں۔]',r'[د سمونوال وضاحت: د بېلګې په پوښتنه او GIVEN چوکاټ کې 3μF دي، خو په GIVEN چوکاټ کې وروسته 3pF چاپ شوی. حل 3μF کاروي او 9μF او 133.3V ترلاسه کوي؛ دواړه چاپ شوي واحدونه ساتل شوي دي.]'),
]
ENERGY=[
 ('Initially, the capacitor is uncharged when voltage is zero. When it is connected to source of potential difference V it is charged. Finally when charges +Q and -Q are deposited on the plates, the potential difference between the plates becomes V. The average voltage on the capacitor is V/2. Thus the energy stored in a capacitor is','ابتدا میں جب وولٹیج صفر ہے تو کیپیسٹر بے بار ہے۔ فرقِ برق V کے منبع سے جوڑنے پر اسے بار دیا جاتا ہے۔ آخر میں پلیٹوں پر +Q اور -Q بار جمع ہونے کے بعد ان کے درمیان فرقِ برق V ہو جاتا ہے۔ کیپیسٹر کا اوسط وولٹیج V/2 ہے۔ پس کیپیسٹر میں ذخیرہ توانائی یہ ہے','په پیل کې چې ولټاژ صفر وي، کپاسیټر بې‌چارج وي. کله چې د V پوتانشیل توپیر سرچینې سره ونښلول شي، چارج کېږي. په پای کې چې پر تختو +Q او -Q چارجونه کښېښودل شي، د تختو ترمنځ د پوتانشیل توپیر V شي. د کپاسیټر منځنی ولټاژ V/2 دی. نو په کپاسیټر کې زېرمه شوې انرژي دا ده'),
 (r'Energy \(=U=\frac{QV}2\) ...(11.37)',)*3,
 ('From Q = CV','Q = CV سے','له Q = CV څخه'),
]
MEMORY=[
 ('For your Information','آپ کی معلومات کے لیے','ستاسو د معلوماتو لپاره'),
 ('Energy stored in the large capacitor is used to preserve the memory of an electronic calculator when its battery is charged.','بڑے کیپیسٹر میں ذخیرہ توانائی، بیٹری چارج ہونے کے دوران برقی کیلکولیٹر کی یادداشت محفوظ رکھنے کے لیے استعمال ہوتی ہے۔','په لوی کپاسیټر کې زېرمه شوې انرژي د بېټرۍ د چارج کېدو پر مهال د برېښنايي حسابګر حافظه ساتلو لپاره کارول کېږي.'),
]

def circuit(lang):
    body='<path d="M30 60H380V220H30Z" fill="none" stroke="#334155" stroke-width="2"/><path d="M30 60H100M164 60H210M290 60H380" stroke="#334155" stroke-width="2"/><path d="M100 42V78M112 42V78M210 42V78M222 42V78" stroke="#334155" stroke-width="2"/><rect x="263" y="34" width="8" height="28" fill="#fef3c7" stroke="#334155"/><rect x="279" y="34" width="8" height="28" fill="#fef3c7" stroke="#334155"/><path d="M30 220H164M222 220H380" stroke="#334155"/><path d="M164 204V236M184 210V230" stroke="#334155" stroke-width="3"/>'
    body+='<text x="90" y="33">C₁</text><text x="204" y="33">C₂</text><text x="258" y="28">C₃</text><text x="35" y="200">V₁</text><text x="292" y="200">V₂</text><text x="345" y="200">20V</text><text x="193" y="252">V</text><text x="140" y="100">+</text><text x="173" y="100">−</text>'
    return '<figure>'+svg(body,410,265,'C1 in series with parallel C2 and C3; voltage V1 across C1 and V2 across parallel branch')+'<figcaption>FIGURE — capacitor combination</figcaption></figure>'

def board(lang):
    body='<rect x="15" y="20" width="440" height="250" fill="#1f2937" stroke="#334155"/>'
    for x in range(40,430,55):body+=f'<path d="M25 {x%180+35}H{x}V{x%210+50}H440" fill="none" stroke="#0f766e" stroke-width="3"/>'
    for x,y in [(70,70),(160,80),(260,60),(360,78),(95,170),(220,180),(350,170)]:
        body+=f'<rect x="{x}" y="{y}" width="42" height="34" fill="#475569" stroke="#cbd5e1"/><circle cx="{x+8}" cy="{y+9}" r="3" fill="#facc15"/><circle cx="{x+29}" cy="{y+9}" r="3" fill="#facc15"/>'
    body+='<ellipse cx="205" cy="122" rx="20" ry="26" fill="#111827" stroke="#e5e7eb"/><rect x="355" y="134" width="27" height="27" fill="#111827" stroke="#e5e7eb"/>'
    return '<figure>'+svg(body,475,290,'Coded electronic circuit board with capacitor components, memory retention context')+'<figcaption>Electronic calculator memory — schematic</figcaption></figure>'

if __name__=='__main__':
    specs=[('phys12-front-example11740','EXAMPLE 11.7',40,EXAMPLE7,('مثال 11.7','بېلګه 11.7'),circuit,[{'type':'paragraph','indices':[0]},{'type':'visual'},{'type':'heading','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'heading','indices':[5]}]+[{'type':'equation','indices':[i]} for i in range(6,13)]),('phys12-front-example11840','EXAMPLE 11.8',40,EXAMPLE8,('مثال 11.8','بېلګه 11.8'),None,[{'type':'paragraph','indices':[0]},{'type':'heading','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'heading','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]}]),('phys12-front-capacitor-energy41','11.12 ENERGY STORED IN A CAPACITOR',41,ENERGY,('11.12 کیپیسٹر میں ذخیرہ توانائی','11.12 په کپاسیټر کې زېرمه شوې انرژي'),None,[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[2]}]),('phys12-front-memory41','FOR YOUR INFORMATION — Calculator memory',41,MEMORY,('آپ کی معلومات کے لیے — کیلکولیٹر کی یادداشت','ستاسو د معلوماتو لپاره — د حسابګر حافظه'),board,[{'type':'heading','indices':[0]},{'type':'visual'},{'type':'paragraph','indices':[1]}])]
    records=[];sections=[]
    for identity,title,page,pairs,titles,visual,layout in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':25,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        if visual:revised.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));revised['content']+=visual('en')
        for para in revised['paras']:
            if para['text'].startswith('[Editorial'):para.update(isEditorial=True,originalText=None)
        records.append(record);sections.append(revised)
    upsert(records,sections)
    examples=[{'id':'textbook-example-7','num':'11.7','title':'Example 11.7','problem':EXAMPLE7[0][0],'given':[EXAMPLE7[2][0]],'required':[EXAMPLE7[4][0]],'steps':[p[0] for p in EXAMPLE7[6:]],'answer':EXAMPLE7[-1][0],'solutionOrigin':'textbook','sourceReferences':[{'pdfPage':25,'printedPage':40}]},{'id':'textbook-example-8','num':'11.8','title':'Example 11.8','problem':EXAMPLE8[0][0],'given':[EXAMPLE8[2][0]],'required':[EXAMPLE8[4][0]],'steps':[p[0] for p in EXAMPLE8[6:-1]],'answer':EXAMPLE8[-2][0],'solutionOrigin':'textbook','sourceReferences':[{'pdfPage':25,'printedPage':40}]}]
    sync_companions(trim_sections=[{'id':'11.15','startsAt':'11.12 ENERGY STORED IN A CAPACITOR','title':'Energy stored in a capacitor (continuation at PDF page 25)','clearSciNote':True}],worked_examples=examples,formulas=[{'id':'phys12-eq-11.37','name':'Capacitor stored energy','number':'11.37','formula':ENERGY[1][0],'latex':r'U=\frac{QV}2','sourceReferences':[{'pdfPage':25,'printedPage':41}]}])
    checkpoint(25,'corrected_verified',[r['id'] for r in records],'Original spread inspected at2.5x. Example11.7 complete series/parallel network solution preserved; Fig11.27 coded. Example11.8 full given/required/solution and common133.3V result transcribed; printed 3pF versus 3μF contradiction retained with clarification. Energy-stored introduction and Eq11.37 plus calculator-memory note coded. Native circuit-board illustration replaces scan. Legacy content trimmed to energy section after both complete examples.',printed_pages=[40,41])
