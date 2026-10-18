import math
from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
FLUX=[
 (r'\(\Phi_E=\frac{q}{4\pi\varepsilon_o}\frac1{r^2}(4\pi r^2)\)',)*3,
 (r'\(\Phi_E=\frac q{\varepsilon_o}\) ...(11.13)',)*3,
 ('The above equation shows that electric flux does not depend upon the shape or geometry of a closed surface. But it depends upon the medium and the charge enclosed by that surface.','اوپر دی گئی مساوات سے ظاہر ہوتا ہے کہ برقی بہاؤ بند سطح کی شکل یا ہندسی ساخت پر منحصر نہیں ہے۔ لیکن یہ واسطے اور اس سطح کے اندر محصور بار پر منحصر ہے۔','پورته معادله ښيي چې برېښنايي فلکس د تړلې سطحې په شکل یا هندسي جوړښت پورې اړه نه لري. خو دا په منځني چاپېریال او په هغې سطحې کې په محصور چارج پورې اړه لري.'),
 (r'In order to calculate the electric flux through irregular close surface S, enclosing point charges \(q_1,q_2,q_3,\ldots,q_n\) as shown in Fig 11.15 a. Then the total electric flux through that closed surface is',r'شکل 11.15 a میں دکھائی گئی بے قاعدہ بند سطح S کے اندر محصور نقطہ باروں \(q_1,q_2,q_3,\ldots,q_n\) سے برقی بہاؤ معلوم کرنے کے لیے، اس بند سطح سے کل برقی بہاؤ یہ ہے',r'د نامنظمې تړلې سطحې S له لارې د برېښنايي فلکس د محاسبې لپاره، چې نقطوي چارجونه \(q_1,q_2,q_3,\ldots,q_n\) پکې محصور دي لکه په شکل 11.15 a کې، د هغې تړلې سطحې له لارې ټول برېښنايي فلکس دا دی'),
 (r'\(\Phi_E=\frac{q_1}{\varepsilon_o}+\frac{q_2}{\varepsilon_o}+\frac{q_3}{\varepsilon_o}\ldots\frac{q_n}{\varepsilon_o}\)',)*3,
 (r'\(=\frac1{\varepsilon_o}(q_1+q_2+q_3+\ldots q_n)\)',)*3,
 (r'\(\Phi_E=\frac1{\varepsilon_o}\sum_{i=1}^{n}q_i\)',)*3,
 (r'\(=\frac1{\varepsilon_o}\) (total charge enclosed by a surface)',r'\(=\frac1{\varepsilon_o}\) (سطح کے اندر محصور کل بار)',r'\(=\frac1{\varepsilon_o}\) (په سطحه کې محصور ټول چارج)'),
 (r'\(=\frac Q{\varepsilon_o}\)',)*3,
 (r'Thus Gauss’s law shows that the electric flux through any closed surface is \(1/\varepsilon_o\) times the total charge enclosed in it.',r'پس گاؤس کا قانون ظاہر کرتا ہے کہ کسی بھی بند سطح سے برقی بہاؤ، اس میں محصور کل بار کا \(1/\varepsilon_o\) گنا ہے۔',r'نو د ګاوس قانون ښيي چې د هرې تړلې سطحې له لارې برېښنايي فلکس په هغې کې د محصور ټول چارج \(1/\varepsilon_o\) برابره دی.'),
]
CONDUCTOR=[
 ('Gauss’s law provides a convenient method to calculate E in the case of charge distribution.','گاؤس کا قانون بار کی تقسیم کی صورت میں E معلوم کرنے کا آسان طریقہ فراہم کرتا ہے۔','د ګاوس قانون د چارج د وېش په حالت کې د E د محاسبې لپاره یوه اسانه طریقه برابروي.'),
 (r'A conductor is a material with neutral atoms rather than a volume distribution of charge. Fig shows an imaginary Gaussian surface \(S_1\), lies just below the actual surface of the conductor; consequently, there is no net charge inside the conductor.',r'موصل ایسا مادہ ہے جس میں بار کی حجمی تقسیم کے بجائے غیر بار دار ایٹم ہوتے ہیں۔ شکل ایک فرضی گاؤسی سطح \(S_1\) دکھاتی ہے جو موصل کی اصل سطح سے ذرا نیچے واقع ہے؛ نتیجتاً موصل کے اندر کوئی خالص بار نہیں ہے۔',r'هادي هغه ماده ده چې د چارج د حجمي وېش پر ځای بې چارج اتومونه لري. شکل یوه خیالي ګاوسي سطحه \(S_1\) ښيي چې د هادي له اصلي سطحې لږ لاندې پرته ده؛ له همدې امله د هادي په دننه کې خالص چارج نشته.'),
 ('Therefore, there is no excess charge inside a conductor.','لہٰذا موصل کے اندر کوئی اضافی بار نہیں ہے۔','له همدې امله د هادي په دننه کې اضافي چارج نشته.'),
 (r'According to Gauss’s law \(\Phi_E=\sum\vec E\cdot\Delta\vec A=0\) as \(Q=0\).',r'گاؤس کے قانون کے مطابق \(\Phi_E=\sum\vec E\cdot\Delta\vec A=0\)، کیونکہ \(Q=0\) ہے۔',r'د ګاوس د قانون له مخې \(\Phi_E=\sum\vec E\cdot\Delta\vec A=0\)، ځکه چې \(Q=0\) دی.'),
 (r'Hence \(E=0\) inside a conductor.',r'پس موصل کے اندر \(E=0\) ہے۔',r'نو د هادي په دننه کې \(E=0\) دی.'),
 (r'If a conductor possesses excess charge, then the electric field is still zero. Thus \(E=0\) inside a conductor. Consequently any excess charge must lie on its surface. Another imaginary Gaussian surface \(S_2\) is shown by dotted line outside a conductor. At the surface of a charged conductor, the electric field is normal to the surface at every point. All the charge is deposited on the outer surface of the conductor. Thus the excess charge is not inside a conductor but it resides on the conductor’s surface.',r'اگر موصل پر اضافی بار ہو تو بھی برقی میدان صفر ہے۔ اس لیے موصل کے اندر \(E=0\) ہے۔ نتیجتاً ہر اضافی بار اس کی سطح پر ہونا چاہیے۔ ایک اور فرضی گاؤسی سطح \(S_2\)، موصل کے باہر نقطہ دار لکیر سے دکھائی گئی ہے۔ بار دار موصل کی سطح پر برقی میدان ہر نقطے پر سطح کے عمود پر ہوتا ہے۔ سارا بار موصل کی بیرونی سطح پر جمع ہوتا ہے۔ اس طرح اضافی بار موصل کے اندر نہیں بلکہ اس کی سطح پر ہوتا ہے۔',r'که هادي اضافي چارج ولري، بیا هم برېښنايي میدان صفر دی. نو د هادي په دننه کې \(E=0\) دی. په پایله کې هر اضافي چارج باید پر سطحه یې وي. بله خیالي ګاوسي سطحه \(S_2\) د هادي په بهر کې په ټکیو لرونکې کرښه ښودل شوې ده. د چارج لرونکي هادي پر سطحه برېښنايي میدان په هره نقطه کې د سطحې په عمود کې دی. ټول چارج د هادي پر بهرنۍ سطحه راټولېږي. په دې توګه اضافي چارج د هادي په دننه کې نه، بلکې پر سطحه یې وي.'),
 (r'Electric field E is shown by arrows, dotted pink line shows Gaussian surface \(S_2\) outside and dotted blue line shows Gaussian surface \(S_1\) inside',r'برقی میدان E تیروں سے دکھایا گیا ہے؛ گلابی نقطہ دار لکیر باہر کی گاؤسی سطح \(S_2\) اور نیلی نقطہ دار لکیر اندر کی گاؤسی سطح \(S_1\) دکھاتی ہے۔',r'برېښنايي میدان E په غشو ښودل شوی؛ ګلابي ټکیو لرونکې کرښه بهرنۍ ګاوسي سطحه \(S_2\) او آبي ټکیو لرونکې کرښه دننۍ ګاوسي سطحه \(S_1\) ښيي.'),
]

def charges(lang):
    body='<path d="M72 26Q20 105 40 220L93 189Q202 179 248 107T189 22Q137 6 72 26Z" fill="#bae6fd" stroke="#334155"/>'
    for label,x,y in [('1',113,52),('2',75,73),('3',225,96),('4',171,147),('5',147,163),('6',62,153),('n',124,138)]:
        body+=f'<circle cx="{x}" cy="{y}" r="3"/><text x="{x-14}" y="{y-10}">q<tspan baseline-shift="sub" font-size="10">{label}</tspan></text>'
    body+='<path d="M168 40H190V56H168Z" fill="#fef08a" stroke="#334155"/><path d="M180 46L205 3M180 48L288 9" stroke="#334155" stroke-width="3"/>'+arrow(205,3,25,-43,'#334155')+arrow(288,9,108,-39,'#b91c1c')+'<text x="218" y="20">ΔA⃗</text><text x="285" y="32">E⃗</text>'
    cap={'en':'FIGURE 11.15 (a) Number of charges in a closed surface','ur':'شکل 11.15 (a) بند سطح میں کئی بار','ps':'شکل 11.15 (a) په تړلې سطحه کې څو چارجونه'}[lang]
    return '<figure>'+svg(body,325,240,'Multiple enclosed point charges and an outward differential area and field vector')+'<figcaption>'+cap+'</figcaption></figure>'

def patches(lang):
    shape='M68 25C123 8 187 48 228 77S309 133 305 164 209 202 132 164 25 112 29 73 48 37 68 25Z'
    curves=[[(68,25),(123,8),(187,48),(228,77)],[(228,77),(269,106),(309,133),(305,164)],[(305,164),(301,195),(209,202),(132,164)],[(132,164),(55,126),(25,112),(29,73)],[(29,73),(33,34),(48,37),(68,25)]]
    boundary=[]
    for points in curves:
        for i in range(41):
            t=i/40;u=1-t
            boundary.append(tuple(u**3*points[0][k]+3*u*u*t*points[1][k]+3*u*t*t*points[2][k]+t**3*points[3][k] for k in [0,1]))
    def inside(x,y):
        crossings=0
        for (ax,ay),(bx,by) in zip(boundary,boundary[1:]+boundary[:1]):
            if (ay>y)!=(by>y) and x<(bx-ax)*(y-ay)/(by-ay)+ax:crossings+=1
        return crossings%2==1
    def clipped(points):
        segments=[];active=[]
        for x,y in points:
            if inside(x,y):active.append((x,y))
            elif active:
                if len(active)>1:segments.append(active)
                active=[]
        if len(active)>1:segments.append(active)
        return ''.join('<path d="M'+'L'.join(f'{x:.2f} {y:.2f}' for x,y in seg)+'"/>' for seg in segments)
    body=f'<path d="{shape}" fill="#fde68a" stroke="#334155"/><g stroke="#334155" fill="none">'
    for x in range(20,331,13):body+=clipped([(x+80*(1-t)*t-18*t*t,140*(1-t)*t+200*t*t) for t in [i/300 for i in range(301)]])
    for y in range(5,211,12):body+=clipped([(290*(1-t)*t+350*t*t,y-84*(1-t)*t+20*t*t) for t in [i/300 for i in range(301)]])
    body+='</g>'
    cap={'en':'FIGURE 11.15 (b) Flux through an irregular close surface having number of patches','ur':'شکل 11.15 (b) کئی حصوں والی بے قاعدہ بند سطح سے بہاؤ','ps':'شکل 11.15 (b) د څو ټوټو لرونکې نامنظمې تړلې سطحې له لارې فلکس'}[lang]
    return '<figure>'+svg(body,350,220,'Irregular closed surface divided into many small differential patches')+'<figcaption>'+cap+'</figcaption></figure>'

def conductor(lang):
    # Polar surface gives explicit outward normals for the electric field.
    def radius(a):return 99+17*math.cos(a)+10*math.sin(2*a)
    def outline(extra):
        pts=[(170+(radius(a)+extra)*math.cos(a),150+(radius(a)+extra)*math.sin(a)) for a in [i*math.pi/90 for i in range(181)]]
        return 'M'+'L'.join(f'{x:.2f} {y:.2f}' for x,y in pts)+'Z'
    body=f'<path d="{outline(0)}" fill="#f3b59e" stroke="#334155"/><path d="{outline(-13)}" fill="none" stroke="#2563eb" stroke-dasharray="2 4"/><path d="{outline(25)}" fill="none" stroke="#db2777" stroke-dasharray="2 4"/>'
    for i in range(18):
        a=i*math.pi/9;r=radius(a);dr=-17*math.sin(a)+20*math.cos(2*a)
        x=170+r*math.cos(a);y=150+r*math.sin(a)
        dx=r*math.cos(a)+dr*math.sin(a);dy=r*math.sin(a)-dr*math.cos(a);norm=math.hypot(dx,dy);dx/=norm;dy/=norm
        x2=x+18*dx;y2=y+18*dy
        body+=f'<path d="M{x:.2f} {y:.2f}L{x2:.2f} {y2:.2f}" stroke="#334155"/>'+arrow(x2,y2,dx,dy,'#334155')
    body+='<text x="210" y="215">S<tspan baseline-shift="sub" font-size="11">1</tspan></text><text x="285" y="244">S<tspan baseline-shift="sub" font-size="11">2</tspan></text><text x="233" y="262">E</text>'
    return '<figure>'+svg(body,350,310,'Charged conductor: blue Gaussian surface S1 inside, pink S2 outside, outward normal electric field E')+'</figure>'

if __name__=='__main__':
    specs=[
      ('phys12-front-gauss20','Gauss’s law — total enclosed charge',20,FLUX,[{'type':'equation' if i in [0,1,4,5,6,7,8] else 'paragraph','indices':[i]} for i in range(len(FLUX))]+[{'type':'visual','blockId':'charges'},{'type':'visual','blockId':'patches'}],('گاؤس کا قانون — کل محصور بار','د ګاوس قانون — ټول محصور چارج'),{'charges':charges,'patches':patches}),
      ('phys12-front-conductor21','11.5.1 APPLICATIONS OF GAUSS’S LAW',21,CONDUCTOR,[{'type':'equation' if i in [3,4] else 'paragraph','indices':[i]} for i in range(len(CONDUCTOR))]+[{'type':'visual','blockId':'conductor'}],('11.5.1 گاؤس کے قانون کے اطلاقات','11.5.1 د ګاوس د قانون کارونې'),{'conductor':conductor}),
    ]
    records=[];sections=[]
    for identity,title,page,pairs,layout,titles,visuals in specs:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':15,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        revised['sourceBlocks']=[{'id':key,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')} for key,fn in visuals.items()]
        revised['content']+=''.join(fn('en') for fn in visuals.values())
        records.append(record);sections.append(revised)
    upsert(records,sections)
    sync_companions(trim_sections=[{'id':'11.7','startsAt':'11.5.1.3 ELECTRIC FIELD INTENSITY','title':'Applications of Gauss’s law (continued; source review starts at PDF page 16)','clearSciNote':True}],
       formulas=[{'id':'phys12-eq-11.13','name':'Gauss’s law','number':'11.13','formula':FLUX[1][0],'latex':r'\Phi_E=\frac q{\varepsilon_o}','note':'Textbook source equation','sourceReferences':[{'pdfPage':15,'printedPage':20}]}])
    checkpoint(15,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected at 2.5x. Eq11.13 and every enclosed-charge derivation line preserved, including source omissions of plus signs before ellipses. Shape/medium discussion and full conductor application box with S1/S2/electric-field relationships transcribed and translated. Figures11.15a/b and conductor Gaussian surfaces recreated with SVG; outward field arrows calculated normal to curved conductor. Covered legacy11.7 prefix and duplicate sciNote removed while retaining PDF16 onward.',printed_pages=[20,21])
