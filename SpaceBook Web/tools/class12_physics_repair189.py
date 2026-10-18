"""PDF189: full source paragraphs and two independently coded source figures."""
from html import escape
from class12_source_review import ROOT, upsert, section, shared_class_data_lock, sync_companions
from class12_fidelity_repair import begin, stage_reference

SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
def ref(n): return {'pdfPage':189,'printedPage':n,'sourcePdf':SOURCE}
T=[]; L=[]
def add(kind,en,ur,ps):
    L.append({'type':kind,'indices':[len(T)]}); T.append((en,ur,ps))

add('paragraph',
 'The heat carried by coolant can run turbine to generate electricity. After exiting the turbine, the steam is condensed back into water that is returned to the heat exchanger.',
 'کولنٹ کے ذریعے منتقل ہونے والی حرارت ٹربائن چلا کر بجلی پیدا کر سکتی ہے۔ ٹربائن سے نکلنے کے بعد بھاپ کو تکثیف کے ذریعے دوبارہ پانی بنایا جاتا ہے، جسے حرارت کے مبادلہ کار میں واپس بھیج دیا جاتا ہے۔',
 'د سړوونکې مادې له خوا لېږدول شوې تودوخه توربین چلولی او برېښنا تولیدولی شي. له توربین څخه تر وتلو وروسته بخار بېرته په اوبو متراکمېږي او د تودوخې تبادله کوونکي ته ستنېږي.')
add('heading','E. SHIELDING','E. حفاظتی پردہ بندی','E. محافظتي پوښ')
add('paragraph',
 'Since neutrons and fission fragment in the nuclear reactor produce radiations which are harmful to life and environment. There must be some process of absorbing these radiations. Usually a concrete wall with lead of a few feet thickness is used as shielding.',
 'چونکہ نیوکلیائی ری ایکٹر میں نیوٹرون اور انشقاق کے ٹکڑے ایسی تابکاری پیدا کرتے ہیں جو زندگی اور ماحول کے لیے نقصان دہ ہوتی ہے۔ اس تابکاری کو جذب کرنے کا کوئی طریقہ ہونا چاہیے۔ عموماً حفاظتی پردے کے طور پر سیسے کے ساتھ کنکریٹ کی چند فٹ موٹی دیوار استعمال کی جاتی ہے۔',
 'ځکه چې په هستوي ریکټر کې نیوټرونونه او د انشقاق ټوټې داسې وړانګې تولیدوي چې ژوند او چاپېریال ته زیان رسوي. د دغو وړانګو د جذب لپاره باید یوه لاره وي. عموماً له سربو سره د کانکریټو څو فوټه پنډ دېوال د محافظتي پوښ په توګه کارول کېږي.')
add('heading','F. TYPES OF NUCLEAR REACTOR','F. نیوکلیائی ری ایکٹر کی اقسام','F. د هستوي ریکټر ډولونه')
add('paragraph','Basically there are two types of nuclear reactors based neutron energy.',
 'بنیادی طور پر نیوٹرون کی توانائی کی بنیاد پر نیوکلیائی ری ایکٹر کی دو اقسام ہیں۔',
 'په بنسټیز ډول د نیوټرون د انرژۍ له مخې هستوي ریکټرونه دوه ډوله دي.')
add('heading','i. Thermal reactors:','i. حرارتی ری ایکٹر:','i. حرارتي ریکټرونه:')
add('paragraph',
 'The reactors in which thermal energy neutrons are used are called thermal reactors. There are many designs of thermal reactor. Pressurized Water Reactor (PWR) is most commonly used reactor in the world. In this reactor the water is prevented from boiling at 100°C, by providing high pressure.',
 'جن ری ایکٹروں میں حرارتی توانائی والے نیوٹرون استعمال کیے جاتے ہیں انہیں حرارتی ری ایکٹر کہتے ہیں۔ حرارتی ری ایکٹر کے بہت سے ڈیزائن ہیں۔ دباؤ والے پانی کا ری ایکٹر (PWR) دنیا میں سب سے زیادہ استعمال ہونے والا ری ایکٹر ہے۔ اس ری ایکٹر میں بلند دباؤ فراہم کر کے پانی کو 100°C پر ابلنے سے روکا جاتا ہے۔',
 'هغه ریکټرونه چې د حرارتي انرژۍ نیوټرونونه پکې کارول کېږي، حرارتي ریکټرونه بلل کېږي. د حرارتي ریکټر ډېرې طرحې شته. د فشار لاندې اوبو ریکټر (PWR) په نړۍ کې تر ټولو ډېر کارېدونکی ریکټر دی. په دې ریکټر کې د لوړ فشار په برابرولو سره اوبه په 100°C کې له اېشېدو څخه ساتل کېږي.')
add('heading','ii. Fast Reactors:','ii. تیز رفتار ری ایکٹر:','ii. چټک ریکټرونه:')
add('paragraph',
 r'The reactors in which fast energy neutrons are used are called fast reactors. Fast reactor make use of \({}^{238}\mathrm{U}\) which is about 99 % in nature. each atom of \({}^{238}\mathrm{U}\) absorb fast neutron and the following reactions occur.',
 r'جن ری ایکٹروں میں تیز توانائی والے نیوٹرون استعمال کیے جاتے ہیں انہیں تیز رفتار ری ایکٹر کہتے ہیں۔ تیز رفتار ری ایکٹر میں \({}^{238}\mathrm{U}\) استعمال ہوتا ہے، جو قدرت میں تقریباً 99 % ہے۔ \({}^{238}\mathrm{U}\) کا ہر ایٹم تیز نیوٹرون جذب کرتا ہے اور درج ذیل تعاملات ہوتے ہیں۔',
 r'هغه ریکټرونه چې د چټکې انرژۍ نیوټرونونه پکې کارول کېږي، چټک ریکټرونه بلل کېږي. چټک ریکټر \({}^{238}\mathrm{U}\) کاروي چې په طبیعت کې شاوخوا 99 % دی. د \({}^{238}\mathrm{U}\) هر اټوم چټک نیوټرون جذبوي او لاندې تعاملونه رامنځته کېږي.')
add('numberedList',
 r'1. Neutron absorption by uranium - 238     \({}^{1}_{0}\mathrm{n}+{}^{238}_{92}\mathrm{U}\rightarrow{}^{239}_{92}\mathrm{U}\)',
 r'1. یورینیم - 238 کے ذریعے نیوٹرون کا جذب     \({}^{1}_{0}\mathrm{n}+{}^{238}_{92}\mathrm{U}\rightarrow{}^{239}_{92}\mathrm{U}\)',
 r'1. د یورانیم - 238 له خوا د نیوټرون جذب     \({}^{1}_{0}\mathrm{n}+{}^{238}_{92}\mathrm{U}\rightarrow{}^{239}_{92}\mathrm{U}\)')
add('numberedList',
 r'2. Beta decay of uranium - 239     \({}^{239}_{92}\mathrm{U}\rightarrow{}^{239}_{93}\mathrm{Np}+{}^{0}_{-1}\beta+{}^{0}_{0}\bar{\nu}\)',
 r'2. یورینیم - 239 کا بیٹا زوال     \({}^{239}_{92}\mathrm{U}\rightarrow{}^{239}_{93}\mathrm{Np}+{}^{0}_{-1}\beta+{}^{0}_{0}\bar{\nu}\)',
 r'2. د یورانیم - 239 بېټا زوال     \({}^{239}_{92}\mathrm{U}\rightarrow{}^{239}_{93}\mathrm{Np}+{}^{0}_{-1}\beta+{}^{0}_{0}\bar{\nu}\)')
add('numberedList',
 r'3. Beta decay of neptunium - 239     \({}^{239}_{93}\mathrm{Np}\rightarrow{}^{239}_{94}\mathrm{Pu}+{}^{0}_{-1}\beta+{}^{0}_{0}\bar{\nu}\)',
 r'3. نیپٹونیم - 239 کا بیٹا زوال     \({}^{239}_{93}\mathrm{Np}\rightarrow{}^{239}_{94}\mathrm{Pu}+{}^{0}_{-1}\beta+{}^{0}_{0}\bar{\nu}\)',
 r'3. د نېپټونیم - 239 بېټا زوال     \({}^{239}_{93}\mathrm{Np}\rightarrow{}^{239}_{94}\mathrm{Pu}+{}^{0}_{-1}\beta+{}^{0}_{0}\bar{\nu}\)')
add('heading','FIGURE 20.19','شکل 20.19','شکل 20.19')
L.append({'type':'visual','blockId':'phys20-189-breeding'})
add('paragraph','An induced nuclear reaction is shown in which Uranium - 238 is transmuted into the plutonium-239',
 'ایک پیدا کیا گیا نیوکلیائی تعامل دکھایا گیا ہے جس میں یورینیم - 238 پلٹونیم-239 میں تبدیل ہو جاتا ہے',
 'یو القا شوی هستوي تعامل ښودل شوی چې پکې یورانیم - 238 په پلوتونیم-239 بدلېږي')
add('paragraph',
 r'Absorption of a neutron by uranium-238 followed by two beta-decay reactions produces plutonium-239, which can also be used as a fission fuel. Fission can be generated in plutonium-239 by fast neutrons therefore no moderator is required in these reactors. The core of fast reactor consists of mixture of plutonium and uranium dioxide surrounded by \({}^{238}\mathrm{U}\) blanket. Thus any neutron escaping from the core interact with \({}^{238}\mathrm{U}\) to produce \({}^{239}\mathrm{Pu}\). Thus natural uranium is used to generate more nuclear fuel by the reaction as shown in the figure 20.19.',
 r'یورینیم-238 کے نیوٹرون جذب کرنے کے بعد بیٹا زوال کے دو تعاملات سے پلٹونیم-239 پیدا ہوتا ہے، جسے انشقاق کے ایندھن کے طور پر بھی استعمال کیا جا سکتا ہے۔ تیز نیوٹرون پلٹونیم-239 میں انشقاق پیدا کر سکتے ہیں، اس لیے ان ری ایکٹروں میں کسی موڈریٹر کی ضرورت نہیں ہوتی۔ تیز رفتار ری ایکٹر کا قلب پلٹونیم اور یورینیم ڈائی آکسائیڈ کے آمیزے پر مشتمل ہوتا ہے، جس کے گرد \({}^{238}\mathrm{U}\) کی تہہ ہوتی ہے۔ یوں قلب سے نکلنے والا کوئی بھی نیوٹرون \({}^{238}\mathrm{U}\) کے ساتھ تعامل کر کے \({}^{239}\mathrm{Pu}\) پیدا کرتا ہے۔ اس طرح قدرتی یورینیم سے، شکل 20.19 میں دکھائے گئے تعامل کے ذریعے، مزید نیوکلیائی ایندھن پیدا کیا جاتا ہے۔',
 r'د یورانیم-238 له خوا د نیوټرون جذب او ورپسې د بېټا زوال دوه تعاملونه پلوتونیم-239 تولیدوي، چې د انشقاق د سون توکي په توګه هم کارېدلی شي. چټک نیوټرونونه په پلوتونیم-239 کې انشقاق رامنځته کولی شي، نو په دې ریکټرونو کې وروکوونکي ته اړتیا نشته. د چټک ریکټر زړه د پلوتونیم او یورانیم ډای اکسایډ له مخلوط څخه جوړ دی چې د \({}^{238}\mathrm{U}\) پوښ ترې چاپېر دی. نو له زړه څخه وتونکی هر نیوټرون له \({}^{238}\mathrm{U}\) سره تعامل کوي او \({}^{239}\mathrm{Pu}\) تولیدوي. په دې توګه طبیعي یورانیم د هغه تعامل له لارې د نورو هستوي سون توکو د تولید لپاره کارېږي چې په 20.19 شکل کې ښودل شوی دی.')
add('heading','20.14 NUCLEAR FUSION','20.14 نیوکلیائی امتزاج','20.14 هستوي امتزاج')
add('definition',
 'When two light nuclei combine to form a heavy nucleus, the process is called nuclear fusion. When two nuclei form a large nucleus the mass of larger nucleus is less than the mass of nuclei that formed it. This loss in mass appears in the form of energy. A self sustaining fusion reaction is also possible but the energy required is possible only in the environments of stars including sun. This cycle of reactions can be achieved at stars in two series of processes.',
 'جب دو ہلکے نیوکلئیس مل کر ایک بھاری نیوکلئیس بناتے ہیں تو اس عمل کو نیوکلیائی امتزاج کہتے ہیں۔ جب دو نیوکلئیس ایک بڑا نیوکلئیس بناتے ہیں تو بڑے نیوکلئیس کی کمیت اسے بنانے والے نیوکلئیسوں کی کمیت سے کم ہوتی ہے۔ کمیت کی یہ کمی توانائی کی صورت میں ظاہر ہوتی ہے۔ خود برقرار رہنے والا امتزاجی تعامل بھی ممکن ہے، لیکن اس کے لیے درکار توانائی صرف سورج سمیت ستاروں کے ماحول میں ممکن ہوتی ہے۔ تعاملات کا یہ چکر ستاروں میں عملوں کے دو سلسلوں سے حاصل ہو سکتا ہے۔',
 'کله چې دوه سپکې هستې سره یوځای شي او یوه درنه هسته جوړه کړي، دې بهیر ته هستوي امتزاج ویل کېږي. کله چې دوه هستې یوه لویه هسته جوړوي، د لویې هستې کتله د هغو هستو له کتلې کمه وي چې هغه یې جوړه کړې ده. د کتلې دا کمښت د انرژۍ په بڼه څرګندېږي. په خپله دوام کوونکی امتزاجي تعامل هم ممکن دی، خو اړینه انرژي یوازې د لمر په ګډون د ستورو په چاپېریال کې ممکنه ده. د تعاملونو دا دوره په ستورو کې د بهیرونو د دوو لړیو له لارې ترلاسه کېدای شي.')
add('heading','A. PROTON CYCLE','A. پروٹون چکر','A. د پروتون دوره')
add('paragraph',
 'In this process the direct collision of protons result in the formation of heavier nuclei whose collision in tern produces helium nuclei as shown in figure 20.20.',
 'اس عمل میں پروٹونوں کے براہ راست تصادم سے بھاری نیوکلئیس بنتے ہیں، جن کے بعد کے تصادم سے ہیلیم کے نیوکلئیس پیدا ہوتے ہیں، جیسا کہ شکل 20.20 میں دکھایا گیا ہے۔',
 'په دې بهیر کې د پروتونونو مستقیم ټکر درنې هستې جوړوي، چې د هغو ورپسې ټکر د هیلیم هستې تولیدوي، لکه په 20.20 شکل کې چې ښودل شوي دي.')
add('paragraph','The initial reaction in proton- proton cycle is',
 'پروٹون-پروٹون چکر کا ابتدائی تعامل یہ ہے',
 'د پروتون-پروتون په دوره کې لومړنی تعامل دا دی')
eq=r'\({}^{1}_{1}\mathrm{H}+{}^{1}_{1}\mathrm{H}\rightarrow{}^{2}_{1}\mathrm{H}+\beta^{+}+\nu\)'
add('equation',eq,eq,eq)
add('heading','FIGURE 20.20','شکل 20.20','شکل 20.20')
L.append({'type':'visual','blockId':'phys20-189-proton-chain'})
add('paragraph','The proton-proton chain','پروٹون-پروٹون سلسلہ','د پروتون-پروتون ځنځیر')

def text(x,y,value,size=19,anchor='middle'):
    return f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="{size}" text-anchor="{anchor}" fill="#172033">{escape(value)}</text>'
def isotope(x,y,a,z,symbol):
    return text(x-14,y-9,str(a),13,'end')+text(x-14,y+9,str(z),13,'end')+text(x-10,y+4,symbol,23,'start')
def arrow(x1,y1,x2,y2,color='#b91c1c'):
    import math
    angle=math.atan2(y2-y1,x2-x1)
    x=x2-10*math.cos(angle);y=y2-10*math.sin(angle)
    points=f'{x2},{y2} {x+4*math.sin(angle)},{y-4*math.cos(angle)} {x-4*math.sin(angle)},{y+4*math.cos(angle)}'
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="2.5"/><polygon points="{points}" fill="{color}"/>'
def svg(body,w,h,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" style="width:100%;height:auto"><rect width="{w}" height="{h}" fill="#fff"/>{body}</svg>'
def breeding(lang):
    out=''
    for x,a,z,s,c in [(100,238,92,'U','#dbeafe'),(285,239,92,'U','#dbeafe'),(500,239,93,'Np','#fce7f3'),(710,239,94,'Pu','#fef9c3')]:
        out+=f'<circle cx="{x}" cy="155" r="38" fill="{c}" stroke="#172033" stroke-width="2"/>'+isotope(x,157,a,z,s)
    out+=arrow(139,155,241,155)+arrow(326,155,455,155)+arrow(541,155,665,155)
    out+='<circle cx="30" cy="227" r="6" fill="#a21caf"/>'+arrow(40,215,72,183,'#172033')+isotope(31,264,1,0,'n')
    for x in [285,500]:
        out+=arrow(x+12,115,x+34,58,'#172033')+isotope(x+28,39,0,-1,'β')
        out+=arrow(x+39,123,x+80,85,'#15803d')+isotope(x+106,76,0,0,'ν̄')
    out+=text(393,133,{'en':'23.5 min','ur':'23.5 منٹ','ps':'23.5 دقیقې'}[lang],18)
    out+=text(610,133,{'en':'2.4 days','ur':'2.4 دن','ps':'2.4 ورځې'}[lang],18)
    return svg(out,780,290,{'en':'Neutron capture by uranium-238 and two beta decays to plutonium-239','ur':'یورینیم-238 کا نیوٹرون جذب اور دو بیٹا زوال سے پلٹونیم-239 بننا','ps':'د یورانیم-238 له خوا د نیوټرون جذب او د دوو بېټا زوالونو له لارې د پلوتونیم-239 تولید'}[lang])
def nucleon(x,y,proton=True):
    return f'<circle cx="{x}" cy="{y}" r="10" fill="{"#fef9c3" if proton else "#c026d3"}" stroke="#172033" stroke-width="1.4"/>'+(text(x,y+5,'+',17) if proton else '')
def nucleus(x,y,kind):
    points={'D':[(0,0,True),(15,-10,False)],'He3':[(-9,8,True),(0,-9,True),(11,8,False)],'He4':[(-9,-9,True),(10,-9,False),(-9,10,False),(10,10,True)]}[kind]
    return ''.join(nucleon(x+a,y+b,p) for a,b,p in points)
def burst(x,y):
    import math
    points=' '.join(f'{x+(20 if i%2==0 else 11)*math.cos(i*math.pi/10):.2f},{y+(20 if i%2==0 else 11)*math.sin(i*math.pi/10):.2f}' for i in range(20))
    return f'<polygon points="{points}" fill="#fef08a" stroke="#a16207"/>'
def wave(x1,y1,x2,y2):
    import math
    dx=x2-x1;dy=y2-y1;length=math.hypot(dx,dy)
    pts=[]
    for i in range(49):
        t=i/48;offset=4*math.sin(t*math.pi*16)
        pts.append((x1+dx*t-dy/length*offset,y1+dy*t+dx/length*offset))
    return '<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'" fill="none" stroke="#172033" stroke-width="2"/>'+arrow(x2-dx/length*7,y2-dy/length*7,x2,y2)+text(x2-7,y2-12,'γ',20)
def chain(lang):
    proton={'en':'Proton','ur':'پروٹون','ps':'پروتون'}[lang];neutron={'en':'Neutron','ur':'نیوٹرون','ps':'نیوټرون'}[lang]
    out=''
    for side in [-1,1]:
        y=255+side*155
        for off in [-30,30]:
            out+=nucleon(95,y+off)+text(75,y+off+5,proton,16,'end')+arrow(107,y+off,150,y+off/3)
        out+=burst(173,y)+arrow(196,y,239,y)
        out+='<circle cx="250" cy="'+str(y)+'" r="5" fill="#db2777"/>'+text(252,y-17 if side<0 else y+26,'β⁺',19)
        ny=y-side*51
        out+=arrow(190,y-side*12,235,ny)+nucleus(257,ny,'D')+isotope(287,ny-side*35,2,1,'H')
        out+=text(287,ny+side*20,neutron,16,'start')
        out+=arrow(279,ny-side*7,315,255+side*85)
        py=255+side*24
        out+=nucleon(257,py)+text(238,py+5,proton,16,'end')+arrow(270,py,315,255+side*65)
        out+=burst(339,255+side*75)+wave(358,255+side*85,432,255+side*135)
        out+=arrow(360,255+side*68,404,255+side*48)+nucleus(430,255+side*43,'He3')+isotope(474,255+side*49,3,2,'He')
        out+=arrow(452,255+side*31,505,255+side*10)
    out+=burst(538,255)+arrow(558,255,612,255)+nucleus(645,255,'He4')+isotope(688,254,4,2,'He')
    for side in [-1,1]:
        out+=arrow(557,255+side*14,608,255+side*57)+nucleon(634,255+side*69)+text(652,255+side*69+5,proton,17,'start')
    out+=wave(552,232,613,128)
    out+='<path d="M634 174 C627 8 270 4 111 70" stroke="#7f1d1d" stroke-width="2" fill="none"/>'+arrow(124,65,108,71)
    return svg(out,790,510,{'en':'The proton-proton chain with both fusion branches, outgoing positrons and gamma rays, helium-4 and two returned protons','ur':'پروٹون-پروٹون سلسلے کی دونوں شاخیں، پوزیٹرون، گاما شعاعیں، ہیلیم-4 اور واپس نکلنے والے دو پروٹون','ps':'د پروتون-پروتون ځنځیر دواړه څانګې، پوزیترونونه، ګاما وړانګې، هیلیم-4 او دوه بېرته وتونکي پروتونونه'}[lang])

record={'id':'phys20-reactor-shielding-types-and-fusion-366-367','title':'Reactor shielding and types; nuclear fusion','kind':'lesson','pdfPage':189,'printedPage':366,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
sec=section(record,T,L,('ری ایکٹر کی حفاظتی پردہ بندی، اقسام اور نیوکلیائی امتزاج','د ریکټر محافظتي پوښ، ډولونه او هستوي امتزاج'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[ref(366),ref(367)],sourceBlocks=[
 {'id':'phys20-189-breeding','type':'figure','svg':breeding('en'),'svgUrdu':breeding('ur'),'svgPashto':breeding('ps'),'sourceFigure':'20.19'},
 {'id':'phys20-189-proton-chain','type':'figure','svg':chain('en'),'svgUrdu':chain('ur'),'svgPashto':chain('ps'),'sourceFigure':'20.20'}])
if __name__=='__main__':
    begin()
    with shared_class_data_lock():
        upsert([record],[sec],chapter_index=9)
        sync_companions(chapter_index=9,definitions=[
          {'term':'Nuclear fusion','definition':T[16][0].split(' When two nuclei')[0],'sourceReferences':[ref(367)]},
          {'term':'Thermal reactor','definition':T[6][0].split(' There are')[0],'sourceReferences':[ref(366)]},
          {'term':'Fast reactor','definition':T[8][0].split(' Fast reactor')[0],'sourceReferences':[ref(366)]}])
    stage_reference(189,record,'Reinspected the full PDF189 spread (printed366–367). Restored every prose paragraph, heading, three numbered breeding equations, fusion equation and both figure captions; retained source grammar including “in tern”. Figure20.19 retains neutron capture, isotope numbers, beta/antineutrino branches and both times. Figure20.20 retains both proton branches, deuterium, helium-3/4, beta and gamma outputs, two emitted protons and return arrow. Urdu/Pashto paragraph pairs and figure labels are separately translated. Saved exact transcription for comparison to active data.')
    print('PDF189 full source correction staged; verification pending.')
