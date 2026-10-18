import math
from class12_source_review import upsert,section,checkpoint,sync_companions
from class12_physics_page013 import SOURCE,svg
from class12_physics_field_figures import arrow
MAIN=[
 ('Now putting the value of E in Eq (11.22) we have','اب مساوات (11.22) میں E کی قیمت رکھنے پر ہمارے پاس ہے','اوس په معادله (11.22) کې د E ارزښت په ایښودلو سره لرو'),
 (r'\(\Delta W=\frac1{4\pi\varepsilon_o}\frac{Qq}{r^2}\Delta r\)',)*3,
 (r'Let the test charge is at a large distance \(r_A\) from charge Q. Electric field does not remain constant but varies as the square of the distance from the charge.',r'آزمائشی بار کو بار Q سے بڑے فاصلے \(r_A\) پر فرض کریں۔ برقی میدان مستقل نہیں رہتا بلکہ بار سے فاصلے کے مربع کے ساتھ بدلتا ہے۔',r'فرض کړئ ازمایښتي چارج له چارج Q څخه په لوی واټن \(r_A\) کې دی. برېښنايي میدان ثابت نه پاتې کېږي، بلکې له چارج څخه د واټن له مربع سره بدلېږي.'),
 (r'We divide the distance between \(r_A\) and \(r_B\) into infinitesimally small displacement so that the field intensity over each displacement remains constant.',r'ہم \(r_A\) اور \(r_B\) کے درمیان فاصلے کو انتہائی چھوٹی نقل مکانیوں میں تقسیم کرتے ہیں، تاکہ ہر نقل مکانی پر میدان کی شدت مستقل رہے۔',r'د \(r_A\) او \(r_B\) ترمنځ واټن په بې نهایت کوچنیو بېځایه کېدنو وېشو، څو پر هرې بېځایه کېدنې د میدان شدت ثابت پاتې شي.'),
 (r'Work done between point \(r_A\) and \(r_1\) is',r'نقطے \(r_A\) اور \(r_1\) کے درمیان کیا گیا کام یہ ہے',r'د \(r_A\) او \(r_1\) نقطو ترمنځ ترسره شوی کار دا دی'),
 (r'\(\Delta W_{r_A\to r_1}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac{r_A-r_1}{r_Ar_1}\right)\)',)*3,
]
BOX=[
 (r'At the beginning of the first displacement E varies as \(1/r_A^2\) and at the end E varies as \(1/r_1^2\) since the average \(1/r^2\) over each small displacement is',r'پہلی نقل مکانی کے آغاز پر E، \(1/r_A^2\) اور آخر پر E، \(1/r_1^2\) کے مطابق بدلتا ہے، چونکہ ہر چھوٹی نقل مکانی پر \(1/r^2\) کی اوسط یہ ہے',r'د لومړۍ بېځایه کېدنې په پیل کې E د \(1/r_A^2\) او په پای کې E د \(1/r_1^2\) له مخې بدلېږي، ځکه چې پر هرې کوچنۍ بېځایه کېدنې د \(1/r^2\) منځنی ارزښت دا دی'),
 (r'\(\frac1{\langle r^2\rangle}=\frac1{\langle rr\rangle}\)',)*3,
 (r'Therefore one r is replaced by \(r_A\) and another by \(r_1\).',r'لہٰذا ایک r کی جگہ \(r_A\) اور دوسرے کی جگہ \(r_1\) رکھا جاتا ہے۔',r'له همدې امله د یوه r پر ځای \(r_A\) او د بل پر ځای \(r_1\) ایښودل کېږي.'),
 (r'\(\frac1{\langle r^2\rangle}=\frac1{r_Ar_1}\)',)*3,
 (r'Replacing \(1/r^2=1/r_Ar_1\) and \(\Delta r=r_A-r_1\) in above equation we get:',r'اوپر کی مساوات میں \(1/r^2=1/r_Ar_1\) اور \(\Delta r=r_A-r_1\) رکھنے پر حاصل ہوتا ہے:',r'په پورته معادله کې د \(1/r^2=1/r_Ar_1\) او \(\Delta r=r_A-r_1\) په ایښودلو سره ترلاسه کوو:'),
]
CONTINUATION=[
 ('By division','تقسیم سے','په وېشلو سره'),
 (r'\(\therefore\left(\frac{r_A}{r_Ar_1}-\frac{r_1}{r_Ar_1}\right)=\left(\frac1{r_1}-\frac1{r_A}\right)\)',)*3,
 (r'\(\Delta W_{r_A\to r_1}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1{r_1}-\frac1{r_A}\right)\) ...(11.23)',)*3,
 (r'Similarly for second small displacement \(\Delta r=r_1-r_2\). Work done is',r'اسی طرح دوسری چھوٹی نقل مکانی \(\Delta r=r_1-r_2\) کے لیے کیا گیا کام یہ ہے',r'په همدې ډول د دویمې کوچنۍ بېځایه کېدنې \(\Delta r=r_1-r_2\) لپاره ترسره شوی کار دا دی'),
 (r'\(\Delta W_{r_1\to r_2}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1{r_2}-\frac1{r_1}\right)\)',)*3,
 ('And','اور','او'),
 (r'\(\Delta W_{r_n\to r_B}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1{r_B}-\frac1{r_n}\right)\) ...(11.24)',)*3,
 (r'The total work done in moving a charge q from \(r_A\) to \(r_B\) can be calculated by taking its sum.',r'بار q کو \(r_A\) سے \(r_B\) تک منتقل کرنے کا کل کام ان کا مجموعہ لے کر معلوم کیا جا سکتا ہے۔',r'د چارج q له \(r_A\) څخه \(r_B\) ته د لېږدولو ټول کار د دې کارونو په جمع کولو محاسبه کېدای شي.'),
 (r'\(\Delta W_{r_A\to r_B}=\frac{Qq}{4\pi\varepsilon_o}\left(-\frac1{r_A}+\frac1{r_1}-\frac1{r_1}+\frac1{r_2}-\frac1{r_2}+\ldots+\frac1{r_B}\right)\)',)*3,
 (r'\(\Delta W_{r_A\to r_B}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1{r_B}-\frac1{r_A}\right)\) ...(11.25)',)*3,
 ('The work done to move a test charge q from infinity to a distance r from Q is','آزمائشی بار q کو لامحدود فاصلے سے Q سے فاصلے r تک منتقل کرنے کا کام یہ ہے','د ازمایښتي چارج q له نامحدود واټن څخه له Q څخه تر r واټن پورې د لېږدولو کار دا دی'),
 (r'\(W_{r_A\to r_B}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1{r_B}-\frac1\infty\right)\)',)*3,
 (r'\(W_{r_A\to r_B}=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1{r_B}\right)\) ...(11.26)',)*3,
 ('The electric potential energy at distance r from Q is','Q سے فاصلے r پر برقی مخزونی توانائی یہ ہے','له Q څخه په r واټن کې برېښنايي پوتانشیلي انرژي دا ده'),
 (r'\(U=\frac{Qq}{4\pi\varepsilon_o}\left(\frac1r\right)\) ...(11.27)',)*3,
]

def figure(lang):
    body=''
    for i in range(8):
        a=i*math.pi/4;dx=math.cos(a);dy=math.sin(a);x=90+80*dx;y=215+80*dy
        body+=f'<path d="M90 215L{x} {y}" stroke="#b91c1c" stroke-width="2"/>'+arrow(x,y,dx,dy,'#b91c1c')
    body+='<path d="M90 215H620" stroke="#334155" stroke-width="2"/>'+arrow(620,215,1,0,'#334155')+'<circle cx="90" cy="215" r="14" fill="#fff" stroke="#334155"/><text x="84" y="220">+</text><text x="30" y="196">+Q</text>'
    for label,x,y in [('rₙ',245,30),('r₃',340,65),('r₂',390,100),('r₁',455,135),('r<tspan baseline-shift="sub" font-size="11">A</tspan>',530,170)]:
        body+=f'<path d="M120 {y}H{x} M{x} {y}V{y+25}" stroke="#334155" stroke-dasharray="2 4"/>'+arrow(120,y,-1,0,'#334155')+arrow(x,y,1,0,'#334155')+f'<text x="{x+3}" y="{y-5}">{label}</text>'
    body+='<path d="M90 234H215" stroke="#334155" stroke-dasharray="2 4"/>'+arrow(215,234,1,0,'#334155')+'<circle cx="215" cy="215" r="3"/><path d="M215 215V234" stroke="#334155"/><text x="204" y="197">B</text><text x="205" y="252">rᵦ</text><circle cx="530" cy="215" r="4"/><text x="516" y="195">A</text><text x="540" y="236">q</text><text x="627" y="210" font-size="32">∞</text><path d="M590 250H534" stroke="#b91c1c" stroke-width="2"/>'+arrow(534,250,-1,0,'#b91c1c')+'<path d="M473 236H530" stroke="#334155" stroke-dasharray="2 4"/>'+arrow(473,236,-1,0,'#334155')+arrow(530,236,1,0,'#334155')+'<text x="473" y="261">Δr</text>'
    cap={'en':'FIGURE 11.20: Work done on a test charge q in moving it towards source charge +Q','ur':'شکل 11.20: آزمائشی بار q کو منبع بار +Q کی طرف منتقل کرنے میں کیا گیا کام','ps':'شکل 11.20: د ازمایښتي چارج q د سرچینې چارج +Q لوري ته په لېږدولو کې ترسره شوی کار'}[lang]
    body=body.replace('rᵦ','r<tspan baseline-shift="sub" font-size="11">B</tspan>')
    return '<figure>'+svg(body,680,320,'Positive source Q, radial field, test charge q at A moved inward, points A/B, rA/rB and intermediate radii rn r3 r2 r1, infinity and delta r')+'<figcaption>'+cap+'</figcaption></figure>'

if __name__=='__main__':
    records=[];sections=[]
    for identity,title,page,pairs,titles,visual in [('phys12-front-point30','Point-charge potential — incremental work',30,MAIN,('نقطہ بار کا پوٹینشل — چھوٹا کام','د نقطوي چارج پوتانشیل — کوچنی کار'),figure),('phys12-front-point-box30','Point-charge potential — small-displacement calculation',30,BOX,('نقطہ بار کا پوٹینشل — چھوٹی نقل مکانی کا حساب','د نقطوي چارج پوتانشیل — د کوچنۍ بېځایه کېدنې محاسبه'),None),('phys12-front-point31','Point-charge potential — summed work and energy',31,CONTINUATION,('نقطہ بار کا پوٹینشل — کل کام اور توانائی','د نقطوي چارج پوتانشیل — ټول کار او انرژي'),None)]:
        record={'id':identity,'title':title,'kind':'lesson','pdfPage':20,'printedPage':page,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
        layout=[{'type':'equation' if p[0].startswith(r'\(') else 'paragraph','indices':[i]} for i,p in enumerate(pairs)]
        if visual:layout.insert(2,{'type':'visual'})
        revised=section(record,pairs,layout,titles);revised['kind']='lesson'
        if visual:
            revised.update(diagramSvg=visual('en'),diagramSvgUrdu=visual('ur'),diagramSvgPashto=visual('ps'));revised['content']+=visual('en')
        records.append(record);sections.append(revised)
    upsert(records,sections)
    formulas=[]
    for num,index in [('11.23',2),('11.24',6),('11.25',9),('11.26',12),('11.27',14)]:
        formula=CONTINUATION[index][0]
        formulas.append({'id':'phys12-eq-'+num,'name':'Point-charge work and energy','number':num,'formula':formula,'latex':formula[2:formula.index(r'\)')],'note':'Textbook source equation','sourceReferences':[{'pdfPage':20,'printedPage':31}]})
    sync_companions(formulas=formulas,retire_sections=['11.10'],trim_sections=[{'id':'11.11','startsAt':'The electric potential at a point in an electric field','title':'Point-charge potential (continued; source review starts at PDF page 21)','clearSciNote':True}])
    checkpoint(20,'corrected_verified',[r['id'] for r in records],
      'Original spread inspected at2.5x; printed30 explanatory box and right text edge checked at5x/7x and matching JPG020_page1 consulted. Complete incremental-work calculation, original average notation, every summed-work line and Eq11.23–11.27 transcribed and aligned. Source varies as the square wording retained despite inverse-square equation. Figure11.20 reconstructed with Q/q, A/B, intermediate radii, infinity and inward displacement. Covered legacy11.10 retired and11.11 trimmed to PDF21.',printed_pages=[30,31])
