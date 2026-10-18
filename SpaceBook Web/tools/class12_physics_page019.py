import math
from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
SURFACES=[
 ('In pervious section electric field which was presented by imaginary lines around a source similarly we can represent electric potentials pictorially by drawing imaginary lines known as equipotential lines.','پچھلے حصے میں برقی میدان کو منبع کے گرد فرضی خطوط سے ظاہر کیا گیا تھا؛ اسی طرح برقی پوٹینشل کو ہم پوٹینشل خطوط کہلانے والے فرضی خطوط کھینچ کر تصویری طور پر ظاہر کر سکتے ہیں۔','په مخکینۍ برخه کې برېښنايي میدان د سرچینې شاوخوا په خیالي کرښو ښودل شوی و؛ په همدې ډول برېښنايي پوتانشیلونه د هم پوتانشیل کرښو په نوم د خیالي کرښو په رسمولو انځورولای شو.'),
 ('The surfaces which have equal electrostatic potential at each point are known as Equipotential Surfaces.','وہ سطحیں جن کے ہر نقطے پر برق سکونی پوٹینشل برابر ہو، ہم پوٹینشل سطحیں کہلاتی ہیں۔','هغه سطحې چې په هره نقطه کې برابر الکتروستاتیکي پوتانشیل لري، هم پوتانشیل سطحې بلل کېږي.'),
 ('These are imaginary surfaces surrounding a charge distribution. An equipotential line connects points in space where the potential of an electric field is the same. The work done to move any charge from one place to other place on an equipotential surface is zero as all the points have same potential.','یہ بار کی تقسیم کے گرد فرضی سطحیں ہیں۔ ہم پوٹینشل خط فضا کے ان نقاط کو ملاتا ہے جہاں برقی میدان کا پوٹینشل یکساں ہو۔ ہم پوٹینشل سطح پر کسی بار کو ایک جگہ سے دوسری جگہ منتقل کرنے کا کام صفر ہے کیونکہ تمام نقاط کا پوٹینشل یکساں ہے۔','دا د چارج د وېش شاوخوا خیالي سطحې دي. هم پوتانشیل کرښه په فضا کې هغه نقطې سره نښلوي چې د برېښنايي میدان پوتانشیل پکې یو شان وي. پر هم پوتانشیل سطحه هر چارج له یوې ځایه بل ځای ته د لېږدولو کار صفر دی، ځکه د ټولو نقطو پوتانشیل برابر دی.'),
 ('In Fig11.19 (a) electric field around a point charge is represented by pink arrows while equipotential surfaces are represented by orange dashed lines. If there are two or more charges present, then the potential at any point is the sum of the potentials due to each charge. Potential is a scalar quantity. However; potential can be either positive or negative, depending upon the sign of the charge.','شکل 11.19 (a) میں نقطہ بار کے گرد برقی میدان گلابی تیروں اور ہم پوٹینشل سطحیں نارنجی ٹوٹی ہوئی لکیروں سے ظاہر کی گئی ہیں۔ اگر دو یا زیادہ بار موجود ہوں، تو کسی نقطے پر پوٹینشل ہر بار کے پوٹینشل کا مجموعہ ہے۔ پوٹینشل عددی مقدار ہے۔ تاہم بار کی علامت کے لحاظ سے پوٹینشل مثبت یا منفی ہو سکتا ہے۔','په شکل 11.19 (a) کې د نقطوي چارج شاوخوا برېښنايي میدان په ګلابي غشو او هم پوتانشیل سطحې په نارنجي مات شویو کرښو ښودل شوې دي. که دوه یا ډېر چارجونه موجود وي، نو په هره نقطه کې پوتانشیل د هر چارج د پوتانشیلونو مجموعه ده. پوتانشیل سکالر مقدار دی. خو د چارج د علامت له مخې مثبت یا منفي کېدای شي.'),
]
EXAMPLE=[
 ('You have a 12.0-V motorcycle battery that can move 5000 C of charge, and a 12.0-V car battery that can move 60,000 C of charge. How much energy does each deliver?','آپ کے پاس 12.0 وولٹ کی موٹر سائیکل کی بیٹری ہے جو 5000 کولومب بار منتقل کر سکتی ہے، اور 12.0 وولٹ کی گاڑی کی بیٹری ہے جو 60,000 کولومب بار منتقل کر سکتی ہے۔ ہر بیٹری کتنی توانائی فراہم کرتی ہے؟','تاسو د موټرسایکل یوه 12.0 ولټه بېټرۍ لرئ چې 5000 کولمب چارج لېږدولای شي، او د موټر یوه 12.0 ولټه بېټرۍ چې 60,000 کولمب چارج لېږدولای شي. هره یوه څومره انرژي ورکوي؟'),
 ('GIVEN','دی گئی معلومات','ورکړل شوي معلومات'),
 (r'For the motorcycle battery, \(q=5000\mathrm C\) and \(\Delta V=12.0\mathrm V\)',r'موٹر سائیکل کی بیٹری کے لیے، \(q=5000\mathrm C\) اور \(\Delta V=12.0\mathrm V\)',r'د موټرسایکل د بېټرۍ لپاره، \(q=5000\mathrm C\) او \(\Delta V=12.0\mathrm V\)'),
 (r'For the car battery, \(q=60,000\mathrm C\) and \(\Delta V=12.0\mathrm V\)',r'گاڑی کی بیٹری کے لیے، \(q=60,000\mathrm C\) اور \(\Delta V=12.0\mathrm V\)',r'د موټر د بېټرۍ لپاره، \(q=60,000\mathrm C\) او \(\Delta V=12.0\mathrm V\)'),
 ('REQUIRED','مطلوب','غوښتل شوي'),
 (r'\(\Delta U_{\mathrm{cycle}}=?\quad\Delta U_{\mathrm{car}}=?\)',)*3,
 ('SOLUTION','حل','حل'),
 (r'\(\Delta U_{\mathrm{cycle}}=(5000\mathrm C)(12.0\mathrm V)=(5000\mathrm C)(12.0\mathrm{J/C})=6.00\times10^4\mathrm J.\)',)*3,
 (r'\(\Delta U_{\mathrm{car}}=(60,000\mathrm C)(12.0\mathrm V)=7.20\times10^5\mathrm J.\)',)*3,
]
ASSIGNMENT=[
 ('When a 12.0 V car battery powers a single 30.0-W headlight, how many electrons pass through it each second?','جب 12.0 وولٹ کی گاڑی کی بیٹری ایک 30.0 واٹ کی ہیڈلائٹ کو توانائی دیتی ہے، تو ہر سیکنڈ اس سے کتنے الیکٹران گزرتے ہیں؟','کله چې د موټر 12.0 ولټه بېټرۍ یوې 30.0 واټه مخکینۍ څراغ ته توان ورکوي، په هره ثانیه کې څو الکترونونه ترې تېرېږي؟'),
 (r'Answer (\(1.56\times10^{19}\) electrons)',r'جواب (\(1.56\times10^{19}\) الیکٹران)',r'ځواب (\(1.56\times10^{19}\) الکترونونه)'),
]
POINT=[
 (r'Like earth’s gravitational field every charge has electric field which theoretically expands upto infinity. Consider an isolated charge \(+Q\) fixed in space as shown in Fig11.20. The electric field intensity \(E\) is given by equation',r'زمین کے ثقلی میدان کی طرح ہر بار کا برقی میدان ہے جو نظری طور پر لامحدود فاصلے تک پھیلتا ہے۔ فضا میں ثابت الگ تھلگ بار \(+Q\) پر غور کریں، جیسا کہ شکل 11.20 میں ہے۔ برقی میدان کی شدت \(E\) اس مساوات سے دی جاتی ہے',r'د ځمکې د جاذبوي میدان په څېر هر چارج برېښنايي میدان لري چې په نظري ډول تر نامحدود واټن پورې غځېږي. په فضا کې ثابت جلا چارج \(+Q\) ته پام وکړئ، لکه په شکل 11.20 کې. د برېښنايي میدان شدت \(E\) په دې معادله ورکول کېږي'),
 (r'\(\vec E=\frac1{4\pi\varepsilon_o}\frac Q{r^2}\hat r\)',)*3,
 (r'As the test charge \(q\) is at infinity which is moved towards charge \(+Q\) a force of repulsion acts on it. Since external work is required to be done to bring charge from infinity to point A therefore negative sign is inserted in equation.',r'جب لامحدود فاصلے پر موجود آزمائشی بار \(q\) کو بار \(+Q\) کی طرف منتقل کیا جاتا ہے، تو اس پر دفع کی قوت عمل کرتی ہے۔ بار کو لامحدود فاصلے سے نقطہ A تک لانے کے لیے بیرونی کام درکار ہے، اس لیے مساوات میں منفی علامت ڈالی جاتی ہے۔',r'کله چې په نامحدود واټن کې ازمایښتي چارج \(q\) د چارج \(+Q\) لوري ته لېږدول کېږي، د دفعې قوه پرې عمل کوي. څرنګه چې له نامحدود واټن څخه A نقطې ته د چارج راوړلو لپاره بهرنی کار اړین دی، نو په معادله کې منفي نښه اچول کېږي.'),
 ('The work done is','کیا گیا کام یہ ہے','ترسره شوی کار دا دی'),
 (r'\(\Delta W=-q\vec E\cdot\Delta\vec r=qE\Delta r\cos180^\circ\)',)*3,
 (r'\(\Delta W=qE\Delta r\) ...(11.22)',)*3,
 (r'[Editorial clarification: the printed middle equality omits the leading minus sign needed when expanding \(-q\vec E\cdot\Delta\vec r\). The printed expression and positive result in Eq11.22 are both retained.]',r'[ادارتی وضاحت: چھپی ہوئی درمیانی مساوات میں وہ ابتدائی منفی علامت نہیں ہے جو \(-q\vec E\cdot\Delta\vec r\) کو کھولنے پر درکار ہے۔ اصل عبارت اور مساوات 11.22 کا مثبت نتیجہ دونوں محفوظ ہیں۔]',r'[د سمونوال وضاحت: چاپ شوې منځنۍ برابري هغه لومړنۍ منفي نښه نه لري چې د \(-q\vec E\cdot\Delta\vec r\) د پراخولو لپاره اړینه ده. چاپ شوی عبارت او د معادلې 11.22 مثبت حاصل دواړه ساتل شوي دي.]'),
]

def equipotential(lang):
    body=''
    for r in [30,55,80,105]:
        body+=f'<circle cx="220" cy="130" r="{r}" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="9 5"/>'
    for i in range(8):
        a=i*math.pi/4;dx=math.cos(a);dy=math.sin(a);x=220+125*dx;y=130+125*dy
        body+=f'<path d="M220 130L{x} {y}" stroke="#be185d" stroke-width="2"/>'+arrow(x,y,dx,dy,'#be185d')
    body+='<circle cx="220" cy="130" r="17" fill="#fff" stroke="#be185d"/><text x="211" y="137" font-size="25">+</text>'
    labels={'en':['Equipotential lines','(a) Equipotential lines/surfaces around positive charge','Equipotential surfaces','(b) Equipotential lines due to two opposite charges'],'ur':['ہم پوٹینشل خطوط','(a) مثبت بار کے گرد ہم پوٹینشل خطوط/سطحیں','ہم پوٹینشل سطحیں','(b) دو مخالف باروں کے ہم پوٹینشل خطوط'],'ps':['هم پوتانشیل کرښې','(a) د مثبت چارج شاوخوا هم پوتانشیل کرښې/سطحې','هم پوتانشیل سطحې','(b) د دوو مخالفو چارجونو هم پوتانشیل کرښې']}[lang]
    body+=f'<path d="M89 256L155 213" stroke="#334155"/><text x="30" y="278">{labels[0]}</text><text x="5" y="311" font-size="13">{labels[1]}</text>'
    # Source shows concentric contour families around both charges and curved field paths.
    for x in [130,310]:
        for r in [25,42,60,81,108]:body+=f'<ellipse cx="{x}" cy="515" rx="{r}" ry="{r}" fill="none" stroke="#ea580c" stroke-width="1.5"/>'
    for offset in [26,50,78,108,143]:
        for sign in [-1,1]:
            y=515+sign*offset
            body+=f'<path d="M310 515C{310+offset*.4} {y} {130-offset*.4} {y} 130 515" fill="none" stroke="#334155"/>'+arrow(220,515+.75*sign*offset, -1,0,'#334155')
    for x,sign,color in [(130,'−','#38bdf8'),(310,'+','#ec4899')]:
        body+=f'<circle cx="{x}" cy="515" r="12" fill="{color}" stroke="#334155"/><text x="{x-6}" y="521">{sign}</text>'
    body+='<path d="M440 515H325M295 515H145M115 515H0" stroke="#334155"/>'+arrow(220,515,-1,0,'#334155')+arrow(55,515,1,0,'#334155')+arrow(390,515,1,0,'#334155')
    body+=f'<text x="100" y="692">{labels[2]}</text><text x="5" y="733" font-size="13">{labels[3]}</text>'
    return '<figure>'+svg(body,450,755,'Figure11.19 positive point-charge radial field and concentric equipotentials; opposite-charge field and contour families')+'<figcaption>'+('FIGURE' if lang=='en' else 'شکل')+' 11.19</figcaption></figure>'

if __name__=='__main__':
    specs=[('phys12-front-equipotential28','EQUIPOTENTIAL SURFACES',28,SURFACES,('ہم پوٹینشل سطحیں','هم پوتانشیل سطحې'),equipotential),('phys12-front-example115','EXAMPLE 11.5',29,EXAMPLE,('مثال 11.5','بېلګه 11.5'),None),('phys12-front-assignment112','ASSIGNMENT 11.2',29,ASSIGNMENT,('مشق 11.2','دنده 11.2'),None),('phys12-front-point29','11.7 ELECTRIC POTENTIAL ENERGY AND POTENTIAL DUE TO A POINT CHARGE',29,POINT,('11.7 نقطہ بار کی وجہ سے برقی مخزونی توانائی اور پوٹینشل','11.7 د نقطوي چارج له امله برېښنايي پوتانشیلي انرژي او پوتانشیل'),None)]
    records=[];sections=[]
    for identity,title,page,pairs,titles,visual in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':19,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        layout=[{'type':'heading' if p[0] in ['GIVEN','REQUIRED','SOLUTION'] else 'equation' if p[0].startswith(r'\(') else 'paragraph','indices':[i]} for i,p in enumerate(pairs)]
        if visual:layout.append({'type':'visual'})
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        if visual:
            revised.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));revised['content']+=visual('en')
        for para in revised['paras']:
            if para['text'].startswith('[Editorial'):para.update(isEditorial=True,originalText=None)
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(trim_sections=[{'id':'11.10','startsAt':'Now putting the value of E','title':'Point-charge potential (continued; source review starts at PDF page 20)','clearSciNote':True}],formulas=[{'id':'phys12-eq-11.22','name':'Work toward a point charge','number':'11.22','formula':POINT[5][0],'latex':r'\Delta W=qE\Delta r','note':'Textbook source equation; preceding equality has a documented sign inconsistency.','sourceReferences':[{'pdfPage':19,'printedPage':29}]}],definitions=[{'term':'Equipotential surfaces','def':SURFACES[1][0],'sourceReferences':[{'pdfPage':19,'printedPage':28}]}],worked_examples=[{'id':'textbook-example-5','num':'11.5','title':'Example 11.5','problem':EXAMPLE[0][0],'given':[p[0] for p in EXAMPLE[2:4]],'required':[EXAMPLE[5][0]],'steps':[p[0] for p in EXAMPLE[7:]],'answer':EXAMPLE[7][0]+' '+EXAMPLE[8][0],'solutionOrigin':'textbook','sourceReferences':[{'pdfPage':19,'printedPage':29}]}],exercises=[{'id':'assignment-11-2','title':'Assignment 11.2','problems':[{'id':'assignment-11-2-q1','question':ASSIGNMENT[0][0],'answer':ASSIGNMENT[1][0],'solutionOrigin':'textbook answer','sourceReferences':[{'pdfPage':19,'printedPage':29}]}]}])
    checkpoint(19,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected at2.5x. Full equipotential discussion and figure11.19 reconstructed; source pervious spelling retained. Example11.5 full statement, given, required and both energy substitutions upserted. Assignment11.2 question/source answer preserved without invented solution. Point-charge introduction and Eq11.22 retain printed sign inconsistency with translated editorial clarification. All paragraphs/headings/captions aligned in Urdu/Pashto. Covered legacy11.10 prefix trimmed to PDF20 continuation.',printed_pages=[28,29])
