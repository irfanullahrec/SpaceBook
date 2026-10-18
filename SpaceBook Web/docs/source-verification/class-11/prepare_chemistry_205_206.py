from chemlib import *
c=cell
def bk(x,y,w,h,fill,col='#999'): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{col}" stroke-width="2"/>'
s=page(205,'chem11-solids','Figures 6.14, 6.15 · Table 6.7 · 6.5 Types of Crystalline Solids · 6.5.1 Ionic Solids','شکل 6.14، 6.15 · جدول 6.7 · 6.5 قلمی ٹھوس کی اقسام · 6.5.1 آئنی ٹھوس','شکلونه 6.14، 6.15 · جدول 6.7 · 6.5 د کرسټالي جامداتو ډولونه · 6.5.1 آیوني جامدات','crystalline-types')
head(s,'h65','6.5 Types of Crystalline solids','6.5 قلمی ٹھوس کی اقسام','6.5 د کرسټالي جامداتو ډولونه')
add(s,'t1','Crystalline solids are classified into categories according to the types of particles in the crystal and the bonding or interactions among them. The four categories are (1) ionic solids, (2) covalent solids (3) metallic solids, and (4) molecular solids.','قلمی ٹھوس کو قلم میں ذرات کی اقسام اور ان کے درمیان بندھن یا تعاملات کے مطابق زمروں میں تقسیم کیا جاتا ہے۔ چار زمرے یہ ہیں: (1) آئنی ٹھوس، (2) ہم ذرّی ٹھوس (3) دھاتی ٹھوس، اور (4) سالماتی ٹھوس۔','کرسټالي جامدات د کرسټال د ذراتو د ډولونو او د هغوی ترمنځ د بند یا تعاملاتو له مخې په ټولګیو ویشل کېږي. څلور ټولګي دا دي: (1) آیوني جامدات، (2) کوولنټ جامدات (3) فلزي جامدات، او (4) مالیکولي جامدات.')
add(s,'rc-h','Reading Check','مطالعہ کی جانچ','د لوستلو ازموینه',kind='heading')
add(s,'rc1','i. What is Crystal Lattice?','i. قلمی جالی کیا ہے؟','i. کرسټالي جالۍ څه ده؟',role='question')
add(s,'rc2',f'ii. Define unit cell. What are the different parameters of{SO} the unit cell?',f'ii. اکائی خانے کی تعریف کریں۔ اکائی خانے کے مختلف پیرامیٹرز کیا ہیں؟ {SO}',f'ii. واحد حجره تعریف کړئ. د واحد حجرې بېلابېل پیرامیټرونه کوم دي؟ {SO}',role='question')
head(s,'h651','6.5.1 Ionic Solids','6.5.1 آئنی ٹھوس','6.5.1 آیوني جامدات')
add(s,'i1',f'In an ionic crystal, the lattice is made of positive and negative ions. These are{SO} held together by ionic bonds. Ionic bonds are strong electrostatic attractions{SO} between oppositely charged ions. As a result, the cations and anions attract one{SO} another in such a manner so that the attractive forces maximize. The structure of an{SO}',f'آئنی قلم میں جالی مثبت اور منفی آئنوں سے بنی ہوتی ہے۔ یہ {SO} آئنی بندھنوں سے ایک ساتھ بندھے ہوتے ہیں۔ آئنی بندھن مخالف چارج والے آئنوں کے درمیان مضبوط برق سکونی کششیں ہیں {SO}۔ نتیجتاً کیٹائن اور اینائن ایک دوسرے کو اس طرح کھینچتے ہیں کہ کششی قوتیں زیادہ سے زیادہ ہو جائیں {SO}۔ ایک آئنی قلم کی ساخت {SO}',f'په آیوني کرسټال کې جالۍ له مثبتو او منفي آیونونو جوړه وي. دا {SO} د آیوني بندونو په واسطه یو ځای نیول شوي وي. آیوني بندونه د مخالف چارج لرونکو آیونونو ترمنځ قوي برېښنا ساکن جذبونه دي {SO}. په پایله کې کیټاینونه او انیاینونه یو بل داسې جذبوي چې جذبي ځواکونه تر ټولو لوړ شي {SO}. د یو آیوني کرسټال جوړښت {SO}',continuesOnPage=206)
fig1=bk(20,30,130,160,'#f4e9b8')+bk(190,30,130,160,'#eef')+'<path d="M45 70 q30-30 50 0 q20 30 40 5" fill="#cde" stroke="#68a"/>'+T(85,90,'Water',11,'middle',700)+T(85,110,'Ice cubes float on water',9)+'<rect x="215" y="140" width="80" height="45" fill="#9cd0e8" stroke="#468"/>'+T(255,70,'Benzene',11,'middle',700)+T(255,88,'Solid benzene sinks to',9)+T(255,100,'the bottom of liquid',9)+T(170,225,'Figure 6.14 Water and Benzene',12,'middle',700,'#a02040')
fig1=fig1.replace('<svg','<svg')
def ice():
    o='';pts=[(40,30),(90,10),(140,40),(190,15),(240,45),(60,90),(110,70),(160,95),(210,75),(260,100),(30,150),(80,135),(130,160),(180,140),(230,165)]
    for a,b in pts: o+=f'<circle cx="{a}" cy="{b}" r="6" fill="#d03050"/>'
    o+=''.join(f'<path d="M{pts[i][0]} {pts[i][1]} L{pts[i+1][0]} {pts[i+1][1]}" stroke="#d03050" stroke-width="2"/>' for i in range(14) if i%5!=4)
    return o+''.join(f'<path d="M{pts[i][0]} {pts[i][1]} L{pts[i+5][0]} {pts[i+5][1]}" stroke="#d03050" stroke-dasharray="4 3"/>' for i in range(10))
s['figures']=[fig(205,'fig6-14',svg(340,240,'Ice cubes floating in water, solid benzene sinking in liquid benzene',fig1),'Figure 6.14 Water and Benzene','شکل 6.14 پانی اور بینزین','شکل 6.14 اوبه او بنزین',[lab('Water: ice cubes float on water','پانی: برف کے ٹکڑے پانی پر تیرتے ہیں','اوبه: د یخ ټوټې په اوبو تیرېږي'),lab('Benzene: solid benzene sinks to the bottom of liquid','بینزین: ٹھوس بینزین مائع کی تہہ میں بیٹھ جاتا ہے','بنزین: جامد بنزین د مایع په ژورو کې ډوبېږي')]),
 fig(205,'fig6-15',svg(300,210,'Open hexagonal hydrogen-bonded network of ice',ice()+T(150,200,'Fig. 6.15 Structure of Ice',12,'middle',700,'#a02040')),'Fig. 6.15 Structure of Ice','شکل 6.15 برف کی ساخت','شکل 6.15 د یخ جوړښت',[lab('Hydrogen bonding','ہائیڈروجن بندھن','هایدروجني بند')])]
s['figures'][0]['sourceGap']=dict(note='Printed Figure 6.14 is a photograph of two beakers; redrawn as a coded schematic, label text on the photograph partly illegible.')
s['figures'][1]['sourceGap']=dict(note='Right edge of Fig. 6.15 is clipped and a side label (apparently "Hydrogen bonding") is unreadable; network redrawn as a schematic.')
rows=[('Argon (Ar)','−190','1.3'),('Benzene (C₆H₆)','5.5','10.9'),('Diethyl ether (C₂H₅OC₂H₅)','−116.2','6.90'),('Ethanol (C₂H₅OH)','−117.3','7.61'),('Mercury (Hg)','−39','23.4'),('Methane (CH₄)','−183','0.84'),('Water (H₂O)','0','6.02')]
ur={'Argon (Ar)':'آرگون (Ar)','Benzene (C₆H₆)':'بینزین (C₆H₆)','Diethyl ether (C₂H₅OC₂H₅)':'ڈائی ایتھائل ایتھر (C₂H₅OC₂H₅)','Ethanol (C₂H₅OH)':'ایتھانول (C₂H₅OH)','Mercury (Hg)':'پارہ (Hg)','Methane (CH₄)':'میتھین (CH₄)','Water (H₂O)':'پانی (H₂O)'}
ps={'Argon (Ar)':'ارګون (Ar)','Benzene (C₆H₆)':'بنزین (C₆H₆)','Diethyl ether (C₂H₅OC₂H₅)':'ډای ایتایل ایتر (C₂H₅OC₂H₅)','Ethanol (C₂H₅OH)':'ایتانول (C₂H₅OH)','Mercury (Hg)':'پارە (Hg)','Methane (CH₄)':'میتان (CH₄)','Water (H₂O)':'اوبه (H₂O)'}
s['tables']=[table('Table 6.7 Molar Heats of Fusion for Selected Substances','جدول 6.7 منتخب مادوں کی مولر حرارتِ پگھلاؤ','جدول 6.7 د غوره شویو موادو مولر د ویلې کېدو تودوخې',[c('Substance','مادہ','مواد'),c('Melting Point(°C)','نقطۂ پگھلاؤ (°C)','د ویلې کېدو نقطه (°C)'),c('ΔH_fus (kJ/mol)','ΔH_fus (kJ/mol)','ΔH_fus (kJ/mol)')],[[c(a,ur[a],ps[a]),c(b),c(d)] for a,b,d in rows])]
s['tables'][0]['sourceGap']=dict(note='Rows skewed by page curl; values paired in printed order. The right column header is clipped (reads "H_fus (kJ/mol)"). Mercury value 23.4 is as printed.')
s['flow']=[dict(type='figure',index=0),dict(type='figure',index=1),dict(type='table',index=0),dict(type='paragraphs',ids=ids(s))]
s['sourceNote']='Printed folio 200. Right-edge clipping marked [scan obscured]. Photographs redrawn as schematics. The ice structure figure is clipped at the right edge.'
s['vocabulary']={'ionic solid':{'ur':'آئنی ٹھوس','ps':'آیوني جامد'},'covalent':{'ur':'ہم ذرّی','ps':'کوولنټ'},'metallic':{'ur':'دھاتی','ps':'فلزي'},'molecular':{'ur':'سالماتی','ps':'مالیکولي'}}
save(s)

s=page(206,'chem11-solids','Figure 6.16 Sodium Chloride Lattice · Properties of Ionic Solids','شکل 6.16 سوڈیم کلورائیڈ جالی · آئنی ٹھوس کی خصوصیات','شکل 6.16 د سوډیم کلوراید جالۍ · د آیوني جامداتو ځانګړنې','ionic-properties')
add(s,'c1','ionic crystal depends on the charges on the cation and anion and on their radii. Examples of ionic solids are NaCl, MgO, NaBr etc. In sodium chloride lattice, each ion is surrounded by opposite charge and there are no separate molecules as shown in figure 6.16.','آئنی قلم کی ساخت کیٹائن اور اینائن کے چارجوں اور ان کے نصف قطروں پر منحصر ہوتی ہے۔ آئنی ٹھوس کی مثالیں NaCl، MgO، NaBr وغیرہ ہیں۔ سوڈیم کلورائیڈ جالی میں ہر آئن مخالف چارج سے گھرا ہوتا ہے اور الگ سالمے نہیں ہوتے جیسا کہ شکل 6.16 میں دکھایا گیا ہے۔','د آیوني کرسټال جوړښت د کیټاین او انیاین په چارجونو او د هغوی په وړانګو پورې اړه لري. د آیوني جامداتو بېلګې NaCl، MgO، NaBr او نور دي. د سوډیم کلوراید په جالۍ کې هر آیون د مخالف چارج لخوا محاصره دی او جلا مالیکولونه نشته لکه څنګه چې په 6.16 شکل کې ښودل شوي.',continuesFromPage=205)
head(s,'pi-h','Properties of Ionic Solids','آئنی ٹھوس کی خصوصیات','د آیوني جامداتو ځانګړنې')
add(s,'pi0','Some of the properties of Ionic solids are,','آئنی ٹھوس کی کچھ خصوصیات یہ ہیں،','د آیوني جامداتو ځینې ځانګړنې دا دي،')
pr=[('In ionic solids, the cations and anions are closely packed into a compact specific geometrical shape and have strong ionic bond.','آئنی ٹھوس میں کیٹائن اور اینائن کثیف انداز میں ایک مخصوص ہندسی شکل میں بھرے ہوتے ہیں اور ان میں مضبوط آئنی بندھن ہوتا ہے۔','په آیوني جامداتو کې کیټاینونه او انیاینونه په یوه ځانګړې هندسي بڼه کې ګنډ ډک وي او قوي آیوني بند لري.'),
('They are solid and usually very hard at room temperature. They never exist in liquid or gaseous form at ordinary temperature and pressure.','یہ ٹھوس اور عموماً کمرے کے درجہ حرارت پر بہت سخت ہوتے ہیں۔ یہ عام درجہ حرارت اور دباؤ پر کبھی مائع یا گیسی شکل میں نہیں پائے جاتے۔','دا جامد او معمولاً د خونې په تودوخه کې ډېر کلک وي. دا په عادي تودوخه او فشار کې هېڅکله په مایع یا ګازي بڼه نه موجود وي.'),
('Ionic solids are brittle. They shatter easily by hammering as shown in figure 6.17.','آئنی ٹھوس ٹوٹنے والے (بھربھرے) ہوتے ہیں۔ یہ ہتھوڑے سے مارنے پر آسانی سے ٹوٹ جاتے ہیں جیسا کہ شکل 6.17 میں دکھایا گیا ہے۔','آیوني جامدات ماتېدونکي دي. دا د چکوش په وهلو په اسانۍ سره ماتېږي لکه څنګه چې په 6.17 شکل کې ښودل شوي.'),
('Ionic solids have high melting points and heats of fusion (ΔH_fus).','آئنی ٹھوس کے نقطۂ پگھلاؤ اور حرارتِ پگھلاؤ (ΔH_fus) بلند ہوتے ہیں۔','آیوني جامدات لوړې د ویلې کېدو نقطې او د ویلې کېدو تودوخې (ΔH_fus) لري.'),
('These solids do not conduct heat and electricity because the ions can vibrate only about their fixed positions. However, in the molten state (that is, when melted) or dissolved in water, they conduct electricity.','یہ ٹھوس حرارت اور بجلی نہیں گزارتے کیونکہ آئن صرف اپنی مقررہ جگہوں کے گرد ارتعاش کر سکتے ہیں۔ تاہم پگھلی ہوئی حالت میں (یعنی جب پگھلائے جائیں) یا پانی میں حل ہو کر یہ بجلی گزارتے ہیں۔','دا جامدات تودوخه او برېښنا نه تېروي ځکه چې آیونونه یوازې د خپلو ټاکلو ځایونو شاوخوا لړزېدای شي. خو په ویلې شوې حالت کې (یعنې کله چې ویلې شي) یا په اوبو کې حل کېدو سره برېښنا تېروي.'),
('They are soluble in polar solvent like water.','یہ پانی جیسے قطبی محلل میں حل پذیر ہیں۔','دا په قطبي محلل لکه اوبو کې حل کېدونکي دي.')]
for i,(e,u,p) in enumerate(pr,1): add(s,f'p{i}',f'{i}. {e}',f'{i}۔ {u}',f'{i}. {p}')
ions=''
import itertools
pts={}
for k in range(3):
    for j in range(3):
        for i in range(3):
            x=60+i*100+k*50;y=250+k*-30-j*80
            big=(i+j+k)%2==0
            ions+=f'<circle cx="{x}" cy="{y}" r="{16 if big else 8}" fill="{"#2a9a8a" if big else "#d03050"}" stroke="#145"/>'
lines='<g stroke="#2a6ab8" stroke-width="2" fill="none">'+''.join(f'<path d="M{60+i*100} {250-j*80} l100 0 M{60+i*100} {250-j*80} l0 -80" />' for i in range(3) for j in range(3))+'</g>'
body=lines+ions+'<circle cx="480" cy="40" r="8" fill="#d03050"/>'+T(500,45,'Na⁺',12,'start',700)+'<circle cx="480" cy="80" r="14" fill="#2a9a8a"/>'+T(500,85,'Cl⁻',12,'start',700)+T(260,300,'Figure 6.16 Sodium Chloride Crystal Lattice',13,'middle',700,'#a02040')
s['figures']=[fig(206,'fig6-16',svg(560,315,'Sodium chloride crystal lattice with alternating sodium and chloride ions',body),'Figure 6.16 Sodium Chloride Crystal Lattice','شکل 6.16 سوڈیم کلورائیڈ قلمی جالی','شکل 6.16 د سوډیم کلوراید کرسټالي جالۍ',[lab('Na⁺','Na⁺','Na⁺'),lab('Cl⁻','Cl⁻','Cl⁻')])]
s['figures'][0]['sourceGap']=dict(note='Rendered 3-D lattice redrawn as a schematic with a simplified 3×3×3 ion array.')
s['flow']=[dict(type='paragraphs',ids=ids(s,0,1)),dict(type='figure',index=0),dict(type='paragraphs',ids=ids(s,1))]
s['sourceNote']='Printed folio 201. Page fully legible. Figure 6.17 is referenced here and printed on a later page.'
s['vocabulary']={'brittle':{'ur':'بھربھرا','ps':'ماتېدونکی'},'molten':{'ur':'پگھلا ہوا','ps':'ویلې شوی'},'polar solvent':{'ur':'قطبی محلل','ps':'قطبي محلل'}}
save(s)
