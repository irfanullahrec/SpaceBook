"""PDF59 / printed110–111: bonding figures and organic reaction vocabulary."""
from html import escape
from math import cos, sin, radians, hypot
import re
from class12_chemistry_opening import pair, section, SOURCE
from class12_chemistry_sync import save


class Drawing:
    def __init__(self,w,h,title):
        self.items=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}"><rect width="{w}" height="{h}" fill="white"/>',
            '<defs><marker id="arrow59" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="none" stroke="context-stroke"/></marker><marker id="fish59" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0L6 3" fill="none" stroke="context-stroke"/></marker></defs>']
    def text(self,x,y,value,size=18,colour='#111'):
        self.items.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-family="Arial, sans-serif" fill="{colour}">{escape(value)}</text>')
    def path(self,d,colour='#111',width=1.8,fill='none',extra=''):
        # Explicit heads remain visible in SVG renderers lacking marker support.
        arrow='marker-end' in extra
        fish='fish59' in extra
        extra=re.sub(r'marker-end="[^"]+"','',extra)
        self.items.append(f'<path d="{d}" fill="{fill}" stroke="{colour}" stroke-width="{width}" {extra}/>')
        if arrow:
            values=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',d)]
            px,py,x,y=values[-4:];dx,dy=x-px,y-py;l=hypot(dx,dy)
            if l:
                ux,uy=dx/l,dy/l
                a=(x-7*ux+3.5*uy,y-7*uy-3.5*ux)
                b=(x-7*ux-3.5*uy,y-7*uy+3.5*ux)
                head=f'M{a[0]} {a[1]}L{x} {y}'+('' if fish else f'L{b[0]} {b[1]}')
                self.items.append(f'<path d="{head}" fill="none" stroke="{colour}" stroke-width="{width}"/>')
    def line(self,x1,y1,x2,y2,colour='#111',width=1.8,extra=''):
        self.path(f'M{x1} {y1}L{x2} {y2}',colour,width,extra=extra)
    def dot(self,x,y,r=3):self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#111"/>')
    def ellipse(self,x,y,rx,ry,colour,opacity=1):self.items.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{colour}" opacity="{opacity}"/>')
    def lobe(self,x,y,angle,length=43,width=15,colour='#f6a21b',stroke='#b14b15'):
        a=radians(angle);ux,uy=cos(a),sin(a);vx,vy=-uy,ux
        def point(t,s):return f'{x+t*ux+s*vx:.2f} {y+t*uy+s*vy:.2f}'
        self.path(f'M{x} {y}C{point(length*.25,width)} {point(length,width)} {point(length,0)}C{point(length,-width)} {point(length*.25,-width)} {x} {y}',stroke,1,colour)
    def wedge(self,x,y,tx,ty):
        dx,dy=tx-x,ty-y;l=hypot(dx,dy);wx,wy=-dy/l*4,dx/l*4
        self.path(f'M{x} {y}L{tx+wx} {ty+wy}L{tx-wx} {ty-wy}Z',fill='#111',width=0)
    def dash_wedge(self,x,y,tx,ty):
        dx,dy=tx-x,ty-y;l=hypot(dx,dy)
        for i in range(1,8):
            t=i/8;px,py=x+dx*t,y+dy*t;wx,wy=-dy/l*4*t,dx/l*4*t
            self.line(px-wx,py-wy,px+wx,py+wy,width=1.4)
    def finish(self):return ''.join(self.items)+'</svg>'


def ethane(language):
    labels={
        'en':['sp³-hybrid orbitals','of C atoms','s orbitals of H atoms','C–H sigma bonds','(sp³–s overlap)','C–C sigma bond','(sp³–sp³ overlap)'],
        'ur':['کاربن ایٹموں کے','sp³ مخلوط آربیٹل','H ایٹموں کے s آربیٹل','C–H سگما بند','(sp³–s تداخل)','C–C سگما بند','(sp³–sp³ تداخل)'],
        'ps':['د C اټومونو','sp³ هایبرډ اوربیټالونه','د H اټومونو s اوربیټالونه','C–H سیګما تړونونه','(sp³–s تداخل)','C–C سیګما تړون','(sp³–sp³ تداخل)'],
    }[language]
    d=Drawing(980,320,'Figure 16.1 — ethane sigma-bond orbital overlaps')
    # Separated sp3 carbons, three available H s orbitals around each carbon.
    for x,angles in [(115,[-150,-60,10,105]),(245,[-170,-65,45,105])]:
        for a in angles:d.lobe(x,104,a,40,14)
        d.text(x,109,'C',15)
        for a in angles[:2]+angles[3:] if x==115 else angles[1:]:
            hx=x+60*cos(radians(a));hy=104+60*sin(radians(a));d.ellipse(hx,hy,14,16,'#9dc885',.65);d.text(round(hx,2),round(hy+6,2),'H',17)
    d.line(305,103,359,93,'#a51c46',1.7,'marker-end="url(#arrow59)"')
    # sp3–sp3 head-on overlap and the six sp3–s overlaps of ethane.
    for x,angles in [(455,[-155,-85,105,0]),(565,[-95,-10,70,180])]:
        for a in angles:d.lobe(x,104,a,57 if a in (0,180) else 44,16)
        d.text(x,109,'C',15)
        for a in angles[:3]:
            hx=x+48*cos(radians(a));hy=104+48*sin(radians(a));d.ellipse(hx,hy,14,17,'#9dc885',.63);d.text(round(hx,2),round(hy+6,2),'H',17)
    d.ellipse(510,104,15,11,'#d84f23',.45)
    # Printed wedge/dash structural representation at the right.
    d.text(787,113,'C',23);d.text(853,113,'C',23);d.line(801,107,839,107)
    d.line(781,94,770,64);d.text(767,53,'H',21)
    d.dash_wedge(775,109,740,116);d.text(729,123,'H',21)
    d.wedge(781,118,767,155);d.text(763,180,'H',21)
    d.line(859,94,873,66);d.text(879,54,'H',21)
    d.dash_wedge(866,111,901,127);d.text(917,137,'H',21)
    d.wedge(856,119,870,162);d.text(877,186,'H',21)
    d.line(152,111,175,203);d.line(207,101,175,203)
    d.text(175,228,labels[0],15);d.text(175,248,labels[1],15)
    d.line(428,129,363,194);d.line(431,82,363,194)
    d.text(362,219,labels[3],15);d.text(362,239,labels[4],15)
    d.line(510,118,510,204);d.text(550,228,labels[5],15);d.text(550,248,labels[6],15)
    d.line(230,180,293,277);d.text(330,303,labels[2],15)
    return d.finish()


def cyclopropane(language):
    labels={
        'en':['109.5° tetrahedral','angle','49.5° angle','compression','“bent bonds” nonlinear overlap'],
        'ur':['109.5° چہار سطحی','زاویہ','49.5° زاویے کا','دباؤ','“خمیدہ بند” غیر خطی تداخل'],
        'ps':['109.5° څلورمخیزه','زاویه','د 49.5° زاویې','فشار','“کږه تړونونه” غیر خطي تداخل'],
    }[language]
    d=Drawing(900,330,'Figure 16.2 — cyclopropane angle strain and bent orbital overlap')
    # Angle construction from the book: 109.5° contracts by49.5° to60°.
    d.path('M150 244L240 88L330 244Z');d.text(270,224,'60°',20)
    d.line(49,244,330,244,'#657578',1,'stroke-dasharray="3 3"')
    d.line(330,244,402,42,'#657578',1,'stroke-dasharray="3 3"')
    d.path('M82 241C79 105 232 27 384 84','#1e8e93',1.8,extra='marker-end="url(#arrow59)"')
    d.text(135,57,labels[0],15,'#167f87');d.text(135,76,labels[1],15,'#167f87')
    d.path('M249 112Q293 91 342 121','#a6224e',1.6,extra='marker-end="url(#arrow59)"')
    d.line(315,123,359,172);d.text(397,191,labels[2],15);d.text(397,213,labels[3],15)
    d.path('M296 243Q296 227 313 211','#a6224e',1.3,extra='marker-end="url(#arrow59)"')
    # Three bent C–C overlaps lie outside the internuclear triangle.
    pts=[(660,87),(580,226),(740,226)]
    for a,b,control in [(pts[0],pts[1],(550,112)),(pts[0],pts[2],(770,112)),(pts[1],pts[2],(660,305))]:
        d.line(*a,*b,'#333',1.5,'stroke-dasharray="4 3"')
        mx=(a[0]+b[0])/2;my=(a[1]+b[1])/2
        ox=(control[0]-mx)*.55;oy=(control[1]-my)*.55
        target=(mx+ox,my+oy)
        for p in (a,b):
            dx,dy=target[0]-p[0],target[1]-p[1];length=hypot(dx,dy);angle=__import__('math').degrees(__import__('math').atan2(dy,dx))
            d.lobe(*p,angle,length+8,17,'#e5f6f4','#168486')
        d.ellipse(*target,11,14,'#3f82b7',.65)
    for x,y in pts:d.ellipse(x,y,10,13,'white');d.text(x,y+7,'C',23)
    d.text(615,212,'60°',18);d.text(699,212,'60°',18)
    d.dash_wedge(652,78,628,29);d.text(622,22,'H',21)
    d.wedge(666,77,687,28);d.text(692,21,'H',21)
    d.dash_wedge(568,230,519,238);d.text(504,245,'H',21)
    d.wedge(573,237,535,276);d.text(521,295,'H',21)
    d.dash_wedge(752,230,802,238);d.text(818,246,'H',21)
    d.wedge(747,237,786,276);d.text(801,296,'H',21)
    d.text(660,326,labels[4],16)
    return d.finish()


def nucleophiles(language):
    d=Drawing(760,85,{'en':'Nucleophile examples, including lone pairs','ur':'نیوکلیوفائل مثالیں، تنہا الیکٹرانی جوڑوں سمیت','ps':'د نیوکلیوفایل بېلګې، له یوازنیو الکتروني جوړو سره'}[language])
    for x,text in [(70,'Cl⁻'),(170,'OH⁻'),(285,'CH₃⁻'),(402,'NH₂⁻'),(520,'NH₃'),(650,'H₂O')]:d.text(x,53,text,26)
    # The neutral examples explicitly show the lone pair printed over N and O.
    d.dot(501,25);d.dot(509,25);d.dot(662,25);d.dot(670,25)
    return d.finish()


def fission(kind,language):
    title={'en':{'homolytic':'Homolytic fission: one electron moves to each atom','heterolytic':'Heterolytic fission: both bonding electrons move to one atom'},'ur':{'homolytic':'ہومولائٹک تقسیم: ہر ایٹم کو ایک الیکٹران','heterolytic':'ہیٹرولائٹک تقسیم: دونوں الیکٹران ایک ایٹم کو'},'ps':{'homolytic':'هومولیتیک وېش: هر اټوم ته یو الکترون','heterolytic':'هېټرولیتیک وېش: دواړه الکترونونه یوه اټوم ته'}}[language][kind]
    d=Drawing(650,240 if kind=='homolytic' else 285,title)
    rows=[('A','A'),('Cl','Cl')] if kind=='homolytic' else [('A','B'),('A','B'),('H','Cl')]
    for i,(a,b) in enumerate(rows):
        y=66+i*90;d.text(151,y,a,25);d.text(236,y,b,25);d.line(165,y-8,220,y-8)
        d.line(278,y-8,384,y-8,'#b4214d',1.6,'marker-end="url(#arrow59)"')
        d.text(451,y,a,25);d.text(508,y,'+',24);d.text(564,y,b,25)
        if kind=='homolytic':
            d.dot(191,y-17);d.dot(191,y+2)
            d.path(f'M193 {y-24}C197 {y-65} 233 {y-58} 233 {y-23}',extra='marker-end="url(#fish59)"')
            d.path(f'M191 {y+9}C183 {y+42} 134 {y+31} 139 {y-1}',extra='marker-end="url(#fish59)"')
            d.dot(451,y-25);d.dot(564,y-25)
        else:
            if i==1:
                d.path(f'M196 {y-13}C189 {y-50} 155 {y-50} 151 {y-19}',extra='marker-end="url(#arrow59)"')
                d.text(463,y-22,'⊖',20);d.text(578,y-22,'⊕',20)
            else:
                d.path(f'M195 {y-13}C201 {y-52} 233 {y-50} 236 {y-19}',extra='marker-end="url(#arrow59)"')
                d.text(463,y-22,'⊕',20);d.text(578,y-22,'⊖',20)
                if i==2:d.dot(191,y-17);d.dot(191,y+2)
    return d.finish()


paras=[];layout=[];blocks=[]
def add(en,ur,ps,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(en,ur,ps))
def figure(name,builder):
    identity='chem12-p59-'+name
    blocks.append({'id':identity,'svg':builder('en'),'svgUrdu':builder('ur'),'svgPashto':builder('ps')})
    layout.append({'type':'visual','blockId':identity})

figure('ethane-overlap',ethane)
add('Figure 16.1 Orbitals overlap description in formation of C–C and C–H sigma bonds of ethane.','شکل16.1 ایتھین کے C–C اور C–H سگما بندوں کی تشکیل میں آربیٹلوں کے تداخل کی وضاحت۔','شکل16.1 د ایتان د C–C او C–H سیګما تړونونو په جوړېدو کې د اوربیټالونو د تداخل تشریح.')
add('Self-assessment','خود جانچ','ځان ارزونه','heading')
add('Draw orbital hybridization model of propane and show different types of overlaps in formation of carbon-carbon and carbon-hydrogen sigma bonds.',
    'پروپین کا آربیٹل ہائبرڈائزیشن ماڈل بنائیں اور کاربن–کاربن اور کاربن–ہائیڈروجن سگما بندوں کی تشکیل میں تداخل کی مختلف قسمیں دکھائیں۔',
    'د پروپان د اوربیټال هایبرډایزېشن ماډل رسم کړئ او د کاربن–کاربن او کاربن–هایدروجن سیګما تړونونو په جوړېدو کې د تداخل بېلابېل ډولونه وښیئ.')
add('16.2.3.2 Structure of Cyclopropane','16.2.3.2 سائیکلوپروپین کی ساخت','16.2.3.2 د سایکلوپروپان جوړښت','heading')
add('In cyclopropane (C₃H₆), each carbon atom, like alkanes, is bonded to four other atoms, so it uses sp³-hybrid orbitals to form sigma bonds. However, in this case, the sp³–sp³ overlap of C–C bond is not maximum as in the case of alkanes. This is due to the fact that in cyclopropane the C–C–C bond angle is 60° and not 109.5° (tetrahedral angle) due to which orbitals do not overlap exactly along their axes (Figure.16.2), but overlap outside of inter-nuclear axes, and form bent bonds. The C–C bond of cyclopropane is therefore weaker than C–C bond of alkane, due to less effective overlap of sp³-hybrid orbitals of carbon in cycopropane. The C–H bonds are formed by overlap of sp³-hybrid orbital of carbon and 1s orbital of hydrogen.',
    'سائیکلوپروپین (C₃H₆) میں، الکینز کی طرح، ہر کاربن ایٹم چار دوسرے ایٹموں سے بند بناتا ہے، اس لیے وہ سگما بند بنانے کے لیے sp³ مخلوط آربیٹل استعمال کرتا ہے۔ تاہم، اس صورت میں C–C بند کا sp³–sp³ تداخل الکینز کی طرح زیادہ سے زیادہ نہیں ہوتا۔ اس کی وجہ یہ ہے کہ سائیکلوپروپین میں C–C–C بند کا زاویہ 60° ہوتا ہے، 109.5° (چہار سطحی زاویہ) نہیں؛ اس لیے آربیٹل اپنے محوروں کے عین ساتھ تداخل نہیں کرتے (شکل16.2)، بلکہ بین النوی محوروں کے باہر تداخل کر کے خمیدہ بند بناتے ہیں۔ چنانچہ سائیکلوپروپین میں کاربن کے sp³ مخلوط آربیٹلوں کا تداخل کم مؤثر ہونے کی وجہ سے اس کا C–C بند الکین کے C–C بند سے کمزور ہوتا ہے۔ C–H بند کاربن کے sp³ مخلوط آربیٹل اور ہائیڈروجن کے 1s آربیٹل کے تداخل سے بنتے ہیں۔',
    'په سایکلوپروپان (C₃H₆) کې د الکانونو په څېر هر کاربني اټوم له څلورو نورو اټومونو سره تړلی وي، نو د سیګما تړونونو د جوړولو لپاره sp³ هایبرډ اوربیټالونه کاروي. خو په دې حالت کې د C–C تړون sp³–sp³ تداخل د الکانونو په څېر اعظمي نه دی. لامل یې دا دی چې په سایکلوپروپان کې د C–C–C تړون زاویه 60° ده، نه 109.5° (څلورمخیزه زاویه)؛ له همدې امله اوربیټالونه کټ مټ پر خپلو محورونو تداخل نه کوي (شکل16.2)، بلکې له بین النووي محورونو بهر تداخل کوي او کږه تړونونه جوړوي. نو په سایکلوپروپان کې د کاربن د sp³ هایبرډ اوربیټالونو د لږ اغېزمن تداخل له امله د هغه C–C تړون د الکان له C–C تړون څخه کمزوری دی. د C–H تړونونه د کاربن د sp³ هایبرډ اوربیټال او د هایدروجن د 1s اوربیټال په تداخل جوړېږي.')
add('In cyclopropane, the three carbon atoms occupy the corners of an equilateral triangle, which results in the C–C–C bond angles to be of 60°. Since the hybridization of carbon is sp³, these C–C–C bond angles should be 109.5°. This deviation from the normal tetrahedral angle of 109.5° to 60° causes a strain in molecule, called Angle strain. The H–C–H bond angle is approximately 115° and the C–C and C–H bond lengths are 151 pm and 108 pm respectively.',
    'سائیکلوپروپین میں تین کاربن ایٹم مساوی الاضلاع مثلث کے کونوں پر ہوتے ہیں، جس سے C–C–C بندوں کے زاویے 60° بنتے ہیں۔ چونکہ کاربن کی ہائبرڈائزیشن sp³ ہے، اس لیے یہ C–C–C زاویے 109.5° ہونے چاہییں۔ عام چہار سطحی زاویے 109.5° سے 60° تک یہ انحراف سالمے میں تناؤ پیدا کرتا ہے جسے زاویائی تناؤ کہتے ہیں۔ H–C–H بند کا زاویہ تقریباً 115°، جبکہ C–C اور C–H بندوں کی لمبائیاں بالترتیب 151 pm اور 108 pm ہیں۔',
    'په سایکلوپروپان کې درې کاربني اټومونه د متساوي الاضلاع مثلث په کونجونو کې وي، چې په پایله کې د C–C–C تړونونو زاویې 60° کېږي. څرنګه چې د کاربن هایبرډایزېشن sp³ دی، د C–C–C دغه زاویې باید 109.5° وي. له عادي څلورمخیزې زاویې 109.5° څخه 60° ته دغه انحراف په مالیکول کې فشار پیدا کوي چې زاویوي فشار بلل کېږي. د H–C–H تړون زاویه نږدې 115° ده، او د C–C او C–H تړونونو اوږدوالی په ترتیب 151 pm او 108 pm دی.')
figure('cyclopropane-overlap',cyclopropane)
add('Figure 16.2 Overlap between sp³-hybrid orbitals of carbon atoms in cyclopropane.','شکل16.2 سائیکلوپروپین میں کاربن ایٹموں کے sp³ مخلوط آربیٹلوں کے درمیان تداخل۔','شکل16.2 په سایکلوپروپان کې د کاربني اټومونو د sp³ هایبرډ اوربیټالونو ترمنځ تداخل.')
add('Some important terms','چند اہم اصطلاحات','ځینې مهم اصطلاحات','heading')
add('1. Electrophile (Electron loving)','1. الیکٹروفائل (الیکٹران دوست)','1. الکتروفایل (الکترون خوښوونکی)','heading')
add('A reagent which can accept an electron pair in a reaction is called an electrophile. An electrophile may be positive ion or neutral molecule with an electron-deficient center. Examples are; H⁺, Cl⁺, CH₃⁺, NO₂⁺, AlCl₃, BF₃, SO₃ etc.',
    'وہ عامل جو کسی تعامل میں الیکٹرانوں کا جوڑا قبول کر سکے، الیکٹروفائل کہلاتا ہے۔ الیکٹروفائل مثبت آئن یا ایسا غیر باردار سالمہ ہو سکتا ہے جس کا مرکز الیکٹرانوں کی کمی رکھتا ہو۔ مثالیں H⁺، Cl⁺، CH₃⁺، NO₂⁺، AlCl₃، BF₃، SO₃ وغیرہ ہیں۔',
    'هغه عامل چې په تعامل کې د الکترونونو جوړه منلی شي، الکتروفایل بلل کېږي. الکتروفایل مثبت ایون یا داسې بې چارج مالیکول کېدای شي چې مرکز یې د الکترونونو کمی ولري. بېلګې یې H⁺، Cl⁺، CH₃⁺، NO₂⁺، AlCl₃، BF₃، SO₃ او نور دي.')
add('2. Nucleophile (Nucleus loving)','2. نیوکلیوفائل (مرکزہ دوست)','2. نیوکلیوفایل (هسته خوښوونکی)','heading')
add('A reagent which can donate an electron-pair to an electrophilic center, in a reaction is called a nucleophile. A nucleophile may be negative ion or neutral molecule with lone pair of electrons. Examples are; Cl⁻, OH⁻, CH₃⁻, NH₂⁻, NH₃, H₂O etc.',
    'وہ عامل جو کسی تعامل میں الیکٹروفائل مرکز کو الیکٹرانوں کا جوڑا دے سکے، نیوکلیوفائل کہلاتا ہے۔ نیوکلیوفائل منفی آئن یا تنہا الیکٹرانی جوڑا رکھنے والا غیر باردار سالمہ ہو سکتا ہے۔ مثالیں Cl⁻، OH⁻، CH₃⁻، NH₂⁻، NH₃، H₂O وغیرہ ہیں۔',
    'هغه عامل چې په تعامل کې الکتروفایلي مرکز ته د الکترونونو جوړه ورکولی شي، نیوکلیوفایل بلل کېږي. نیوکلیوفایل منفي ایون یا بې چارج مالیکول کېدای شي چې د الکترونونو یوازنۍ جوړه ولري. بېلګې یې Cl⁻، OH⁻، CH₃⁻، NH₂⁻، NH₃، H₂O او نور دي.')
figure('nucleophile-lone-pairs',nucleophiles)
add('3. Free Radicals','3. آزاد ریڈیکل','3. ازاد رادیکالونه','heading')
add('A free radical is an atom or group of atoms having unpaired electron(s). Free radicals are produced during the homolytic fission of a covalent bond. They are very reactive as they have strong tendency to pair up their unpaired electron with another electron from wherever available. Examples are; H•, Cl•, •CH₃ etc.',
    'آزاد ریڈیکل ایسا ایٹم یا ایٹموں کا گروپ ہے جس میں بے جوڑ الیکٹران ہو۔ آزاد ریڈیکل اشتراکی بند کی ہومولائٹک تقسیم کے دوران بنتے ہیں۔ یہ بہت زیادہ عامل ہوتے ہیں کیونکہ اپنے بے جوڑ الیکٹران کا جہاں سے بھی کوئی دوسرا الیکٹران دستیاب ہو، اس کے ساتھ جوڑا بنانے کا شدید رجحان رکھتے ہیں۔ مثالیں H•، Cl•، •CH₃ وغیرہ ہیں۔',
    'ازاد رادیکال یو اټوم یا د اټومونو ګروپ دی چې بې جوړې الکترونونه لري. ازاد رادیکالونه د اشتراکي تړون د هومولیتیک وېش پر مهال جوړېږي. دوی ډېر تعامل کوونکي دي، ځکه قوي تمایل لري چې خپل بې جوړې الکترون له بل الکترون سره جوړه کړي، له هر ځایه چې موجود وي. بېلګې یې H•، Cl•، •CH₃ او نور دي.')
add('4. Homolytic and Heterolytic bond fission','4. بند کی ہومولائٹک اور ہیٹرولائٹک تقسیم','4. د تړون هومولیتیک او هېټرولیتیک وېش','heading')
add('Bond breaking (fission) is an endothermic process. If sufficient amount of energy is available, a covalent bond can undergo fission in two ways.',
    'بند ٹوٹنا (تقسیم) حرارت جذب کرنے والا عمل ہے۔ اگر مناسب مقدار میں توانائی دستیاب ہو تو اشتراکی بند دو طریقوں سے تقسیم ہو سکتا ہے۔',
    'د تړون ماتېدل (وېش) یو تودوخه جذبوونکی بهیر دی. که کافي انرژي موجوده وي، اشتراکي تړون په دوو لارو وېشل کېدای شي.')
add('a) Homolytic Bond Fission or Homolysis: In Homolytic fission, a chemical bond breaks in such a way that each of the two bonded atoms acquires one of the bonding electrons. Homolysis results in the formation of free radicals. The arrows in the following general example shows the movement of one electron each to both atoms.',
    'a) بند کی ہومولائٹک تقسیم یا ہومولائسز: ہومولائٹک تقسیم میں کیمیائی بند اس طرح ٹوٹتا ہے کہ بند بنانے والے دونوں ایٹموں میں سے ہر ایک، بند کے الیکٹرانوں میں سے ایک حاصل کرتا ہے۔ ہومولائسز کے نتیجے میں آزاد ریڈیکل بنتے ہیں۔ درج ذیل عمومی مثال کے تیر دونوں ایٹموں کی طرف ایک ایک الیکٹران کی حرکت دکھاتے ہیں۔',
    'a) د تړون هومولیتیک وېش یا هومولایسس: په هومولیتیک وېش کې کیمیاوي تړون داسې ماتېږي چې له دوو تړلو اټومونو څخه هر یو د تړون یو الکترون ترلاسه کوي. هومولایسس د ازادو رادیکالونو د جوړېدو لامل کېږي. د لاندې عمومي بېلګې غشي دواړو اټومونو ته د یوه یوه الکترون خوځښت ښيي.')
figure('homolytic',lambda language:fission('homolytic',language))
add('b) Heterolytic Bond Fission or Heterolysis: In Heterolytic fission the chemical bond breaks in such a way that one of the bonded atoms acquires both of the bonded electrons. The atom with high electronegativity, usually, acquires both the bonding electrons. Heterolysis results in the formation of ions (electrophile and nucleophile). The arrow in the following general example indicates the movement of sigma electrons towards a single atom.',
    'b) بند کی ہیٹرولائٹک تقسیم یا ہیٹرولائسز: ہیٹرولائٹک تقسیم میں کیمیائی بند اس طرح ٹوٹتا ہے کہ بند بنانے والے ایٹموں میں سے ایک بند کے دونوں الیکٹران حاصل کر لیتا ہے۔ عموماً زیادہ برقی منفیت والا ایٹم بند کے دونوں الیکٹران حاصل کرتا ہے۔ ہیٹرولائسز کے نتیجے میں آئن (الیکٹروفائل اور نیوکلیوفائل) بنتے ہیں۔ درج ذیل عمومی مثال کا تیر ایک ہی ایٹم کی طرف سگما الیکٹرانوں کی حرکت ظاہر کرتا ہے۔',
    'b) د تړون هېټرولیتیک وېش یا هېټرولایسس: په هېټرولیتیک وېش کې کیمیاوي تړون داسې ماتېږي چې له تړلو اټومونو څخه یو د تړون دواړه الکترونونه ترلاسه کوي. عموماً د لوړې برقي منفيت لرونکی اټوم د تړون دواړه الکترونونه ترلاسه کوي. هېټرولایسس د ایونونو (الکتروفایل او نیوکلیوفایل) د جوړېدو لامل کېږي. د لاندې عمومي بېلګې غشی یوه اټوم ته د سیګما الکترونونو خوځښت ښيي.')
figure('heterolytic',lambda language:fission('heterolytic',language))

record=section('16.6','Ethane and cyclopropane bonding; important terms','ایتھین اور سائیکلوپروپین کے بند؛ اہم اصطلاحات','د ایتان او سایکلوپروپان تړونونه؛ مهم اصطلاحات',paras,layout,blocks,'110–111')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':59,'printedPages':[110,111]}]
record['sourceFigureReview']='All instructional source figures reconstructed in SVG; final three-language source-fidelity review pending.'
issues=[{'id':'chem12-p110-cycopropane-spelling','printedPage':110,'description':'Printed spelling cycopropane in the final part of the first structure paragraph is retained; elsewhere the source uses cyclopropane.'}]
if __name__=='__main__':save(59,[record],issues=issues,chapter_number=16)
