import math,re
from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg,closed
from class12_physics_field_figures import arrow
LAW=[
 (r'relationship between the net electrical flux \(\Phi\) through a closed surface and the net charge \(q\) enclosed by that surface.',r'بند سطح سے خالص برقی بہاؤ \(\Phi\) اور اس سطح کے اندر محصور خالص بار \(q\) کے درمیان تعلق۔',r'د تړلې سطحې له لارې د خالص برېښنايي فلکس \(\Phi\) او په هغې سطحې کې د محصور خالص چارج \(q\) ترمنځ اړیکه.'),
 (r'Gauss’ law states that the net electric flux through a closed surface is equal to the total charge \(q\) enclosed by the surface divided by the permittivity of free space.',r'گاؤس کا قانون بیان کرتا ہے کہ بند سطح سے خالص برقی بہاؤ، سطح کے اندر محصور کل بار \(q\) کو آزاد فضا کی برقی نفوذ پذیری سے تقسیم کرنے کے برابر ہے۔',r'د ګاوس قانون وايي چې د تړلې سطحې له لارې خالص برېښنايي فلکس د سطحې د محصور ټول چارج \(q\) او د ازادې فضا د برېښنايي نفوذپذیرۍ له نسبت سره برابر دی.'),
 (r'In order to derive the expression for Gauss’s Law consider the spherical closed surface of radius \(r\) having a point charge \(q\) at its center as shown in Fig.11.13 a.',r'گاؤس کے قانون کی مساوات اخذ کرنے کے لیے نصف قطر \(r\) کی کروی بند سطح پر غور کریں جس کے مرکز پر نقطہ بار \(q\) ہو، جیسا کہ شکل 11.13 a میں ہے۔',r'د ګاوس د قانون د عبارت د استنتاج لپاره د \(r\) شعاع لرونکې کروي تړلې سطحې ته پام وکړئ چې په مرکز کې یې نقطوي چارج \(q\) وي، لکه په شکل 11.13 a کې.'),
 (r'To calculate the electric flux through the whole surface, it is divided into n-number of small patches having area \(\Delta A_1,\Delta A_2,\Delta A_3,\Delta A_4,\ldots,\Delta A_n\). The intensity of electric field is same at every point as they are at equidistant from the charge.',r'پوری سطح سے برقی بہاؤ معلوم کرنے کے لیے اسے n چھوٹے حصوں میں تقسیم کیا جاتا ہے جن کے رقبے \(\Delta A_1,\Delta A_2,\Delta A_3,\Delta A_4,\ldots,\Delta A_n\) ہیں۔ برقی میدان کی شدت ہر نقطے پر یکساں ہے کیونکہ تمام نقاط بار سے یکساں فاصلے پر ہیں۔',r'د ټولې سطحې له لارې د برېښنايي فلکس د محاسبې لپاره دا په n کوچنیو ټوټو وېشل کېږي چې مساحتونه یې \(\Delta A_1,\Delta A_2,\Delta A_3,\Delta A_4,\ldots,\Delta A_n\) دي. د برېښنايي میدان شدت په هره نقطه کې یو شان دی، ځکه ټولې له چارج څخه په برابر واټن کې دي.'),
]
BIO=[
 ('Carl Friedrich Gauss (1777 - 1855)','کارل فریڈرک گاؤس (1777 - 1855)','کارل فریډریش ګاوس (1777 - 1855)'),
 ('Gauss was a German mathematician and scientist who contributed significantly to many fields, including number theory, statistics, analysis, differential geometry, geophysics, electrostatics, astronomy and optics.','گاؤس جرمن ریاضی دان اور سائنس دان تھے جنہوں نے نظریۂ اعداد، شماریات، تجزیہ، تفاضلی ہندسہ، ارضی طبیعیات، برق سکونیات، فلکیات اور بصریات سمیت کئی شعبوں میں نمایاں خدمات انجام دیں۔','ګاوس یو جرمني ریاضي پوه او ساینس پوه و چې د عددونو تیورۍ، احصایې، تحلیل، تفاضلي هندسې، ځمکپوهنیز فزیک، الکتروستاتیک، ستورپوهنې او نورپوهنې په ګډون یې په ډېرو برخو کې مهمې ونډې اخیستې دي.'),
]
DERIVE=[]
for index,eng,ur,ps in [
 ('1',r'The electric flux through the small elements \(\Delta A_1\) is',r'چھوٹے عناصر \(\Delta A_1\) سے برقی بہاؤ یہ ہے',r'د کوچنیو عناصرو \(\Delta A_1\) له لارې برېښنايي فلکس دا دی'),
 ('2',r'The electric flux through the other small element \(\Delta A_2\) is',r'دوسرے چھوٹے عنصر \(\Delta A_2\) سے برقی بہاؤ یہ ہے',r'د بل کوچني عنصر \(\Delta A_2\) له لارې برېښنايي فلکس دا دی'),
 ('n',r'Similarly the electric flux through \(\Delta A_n\) is',r'اسی طرح \(\Delta A_n\) سے برقی بہاؤ یہ ہے',r'په همدې ډول د \(\Delta A_n\) له لارې برېښنايي فلکس دا دی'),
]:
    DERIVE.append((eng,ur,ps))
    eq=rf'\(\Phi_{index}=\vec E_{index}\cdot\Delta\vec A_{index}=E_{index}\Delta A_{index}\cos0=E_{index}\Delta A_{index}\)'
    DERIVE.append((eq,)*3)
DERIVE += [
 ('The total flux through the entire surface is','پوری سطح سے کل بہاؤ یہ ہے','د ټولې سطحې له لارې ټول فلکس دا دی'),
 (r'\(\Phi_E=\Phi_1+\Phi_2+\Phi_3+\Phi_4+\ldots+\Phi_n\)',)*3,
 (r'\(\Phi_E=\sum_{\mathrm{surface}}E\Delta A\) ...(11.12)',)*3,
 ('But as electric field intensity E is constant over the surface of sphere','لیکن چونکہ کرہ کی سطح پر برقی میدان کی شدت E مستقل ہے','خو څرنګه چې د کرې پر سطحه د برېښنايي میدان شدت E ثابت دی'),
 ('Therefore,','لہٰذا،','له همدې امله،'),
 (r'\(\Phi_E=E\sum_{\mathrm{surface}}\Delta A\)',)*3,
 ('Since,','چونکہ،','ځکه چې،'),
 (r'\(E=\frac{q}{4\pi\varepsilon_o}\frac{1}{r^2}\)',)*3,
 ('Thus the above equation can be written as','پس اوپر دی گئی مساوات کو اس طرح لکھ سکتے ہیں','نو پورته معادله داسې لیکل کېدای شي'),
 (r'\(\Phi_E=\frac{q}{4\pi\varepsilon_o}\frac{1}{r^2}\sum_{\mathrm{surface}}\Delta A\)',)*3,
 (r'\(\sum_{\mathrm{surface}}\Delta A=\) total area enclosed by spherical surface \(=4\pi r^2\)',r'\(\sum_{\mathrm{surface}}\Delta A=\) کروی سطح سے محصور کل رقبہ \(=4\pi r^2\)',r'\(\sum_{\mathrm{surface}}\Delta A=\) د کروي سطحې محصور ټول مساحت \(=4\pi r^2\)'),
]

def sphere(lang):
    body='<ellipse cx="115" cy="105" rx="80" ry="95" fill="#38bdf8" stroke="#334155"/><circle cx="115" cy="105" r="4" fill="#fff" stroke="#334155"/><text x="102" y="124">q</text><path d="M115 105L153 24" stroke="#334155"/><text x="127" y="67">r</text><path d="M173 89H196V105H173Z" fill="#e11d48"/><path d="M185 94H218M185 104H263" stroke="#334155" stroke-width="2"/>'+arrow(218,94,1,0,'#334155')+arrow(263,104,1,0,'#334155')+'<text x="205" y="83">ΔA⃗</text><text x="259" y="88">E⃗</text><text x="35" y="213">a.</text>'
    grid=re.search(r'<svg.*?</svg>',closed('en')).group()
    grid=grid[:grid.index('<path d="M178 83')]+ '</svg>'
    body+='<g transform="translate(0 235)">'+grid+'<text x="35" y="225">b.</text></g>'
    caption={'en':'FIGURE 11.13: Flux through a close surface','ur':'شکل 11.13: بند سطح سے بہاؤ','ps':'شکل 11.13: د تړلې سطحې له لارې فلکس'}[lang]
    return '<figure>'+svg(body,350,485,'Central point charge, radial field and small outward area vector; sphere divided into patches')+'<figcaption>'+caption+'</figcaption></figure>'

def irregular(lang):
    body='<path d="M90 35C140 20 240 45 247 120S203 230 143 220 63 152 71 92 60 43 90 35Z" fill="#a3d977" stroke="#334155"/>'
    for i in range(12):
        a=i*math.pi/6;dx=math.cos(a);dy=math.sin(a);x=156+125*dx;y=130+125*dy
        body+=f'<path d="M156 130L{x} {y}" stroke="#111827" stroke-width="2"/>'+arrow(x,y,dx,dy,'#111827')
    body+='<circle cx="156" cy="130" r="10" fill="#111827"/><text x="150" y="135" fill="#fff">+</text>'
    cap={'en':'FIGURE 11.14: Flux through an irregular close surface','ur':'شکل 11.14: بے قاعدہ بند سطح سے بہاؤ','ps':'شکل 11.14: د نامنظمې تړلې سطحې له لارې فلکس'}[lang]
    return '<figure>'+svg(body,320,270,'Radial field from positive charge crossing an irregular closed surface')+'<figcaption>'+cap+'</figcaption></figure>'

def portrait(lang):
    body='<path d="M35 220Q50 159 105 151Q165 159 179 220Z" fill="#334155"/><path d="M74 151L108 208 144 151" fill="#fff"/><path d="M93 172L106 188 128 168" fill="#bdb36b"/><ellipse cx="108" cy="90" rx="46" ry="61" fill="#f0c9a3"/><path d="M62 89Q45 61 74 31Q109 15 142 38L153 91 137 63 131 32 83 36 74 78Z" fill="#e5e7eb"/><path d="M73 72L89 69M120 70L136 73M103 88L100 106 112 107M90 124Q106 130 125 121" fill="none" stroke="#574032"/><circle cx="83" cy="80" r="2"/><circle cx="128" cy="80" r="2"/>'
    cap={'en':'Carl Friedrich Gauss — schematic portrait','ur':'کارل فریڈرک گاؤس — خاکہ','ps':'کارل فریډریش ګاوس — طرحه'}[lang]
    return '<figure>'+svg(body,220,230,'Schematic historical portrait of Carl Friedrich Gauss')+'<figcaption>'+cap+'</figcaption></figure>'

if __name__=='__main__':
    specs=[
      ('phys12-front-gauss18','Gauss’s law — statement and spherical surface',18,LAW,[{'type':'paragraph','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'visual','blockId':'sphere'},{'type':'paragraph','indices':[3]}],('گاؤس کا قانون — بیان اور کروی سطح','د ګاوس قانون — بیان او کروي سطحه'),{'sphere':sphere}),
      ('phys12-front-gauss-biography18','Carl Friedrich Gauss (1777 - 1855)',18,BIO,[{'type':'heading','indices':[0]},{'type':'visual','blockId':'portrait'},{'type':'paragraph','indices':[1]}],('کارل فریڈرک گاؤس (1777 - 1855)','کارل فریډریش ګاوس (1777 - 1855)'),{'portrait':portrait}),
      ('phys12-front-gauss19','Gauss’s law — flux derivation',19,DERIVE,[{'type':'equation' if i in [1,3,5,7,8,11,13,15,16] else 'paragraph','indices':[i]} for i in range(len(DERIVE))]+[{'type':'visual','blockId':'irregular'}],('گاؤس کا قانون — بہاؤ کا اخذ','د ګاوس قانون — د فلکس استنتاج'),{'irregular':irregular}),
    ]
    records=[];sections=[]
    for identity,title,page,pairs,layout,titles,visuals in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':14,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        revised['sourceBlocks']=[{'id':key,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')} for key,fn in visuals.items()]
        revised['content']+=''.join(fn('en') for fn in visuals.values())
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(retire_sections=['11.6'],trim_sections=[{'id':'11.7','startsAt':'q\nATE\nΦε','title':'Gauss’s law (continued; source review starts at PDF page 15)'}],
       formulas=[{'id':'phys12-eq-11.12','name':'Total flux over a surface','number':'11.12','formula':DERIVE[8][0],'latex':r'\Phi_E=\sum_{\mathrm{surface}}E\Delta A','note':'Textbook source equation','sourceReferences':[{'pdfPage':14,'printedPage':19}]}],
       definitions=[{'term':'Gauss’s law','def':LAW[1][0],'sourceReferences':[{'pdfPage':14,'printedPage':18}]}])
    checkpoint(14,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected visually at 2.5x. Page-break continuation completed; Gauss-law statement, spherical setup, differential-area subdivision, full historical biography and every derivation line through total spherical area transcribed with aligned Urdu/Pashto. Equation11.12 preserved. Native SVG replaces Figures11.13a/b and11.14 and a labeled schematic historical portrait. Covered legacy11.6 retired; covered prefix of11.7 trimmed while retaining PDF15 onward.',printed_pages=[18,19])
