"""Sequential source correction for PDF page 52 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(p):return {'pdfPage':52,'printedPage':p,'sourcePdf':SOURCE}
def svg(body,label):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 300" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:620px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

FLUX=[
 pair('13.3 MAGNETIC FLUX','13.3 مقناطیسی بہاؤ','13.3 مقناطیسي فلوکس'),
 pair('The scalar product of magnetic induction B and the area A is called magnetic flux Φ_B.','مقناطیسی القا B اور رقبے A کا عددی ضرب مقناطیسی بہاؤ Φ_B کہلاتا ہے۔','د مقناطیسي القا B او مساحت A سکالر ضرب مقناطیسي فلوکس Φ_B بلل کېږي.'),
 pair('Φ_B = B⃗ · A⃗ = BA cos θ','Φ_B = B⃗ · A⃗ = BA cos θ','Φ_B = B⃗ · A⃗ = BA cos θ'),
 pair('Magnetic induction tells us how close together magnetic field lines are, as it tells us the strength of the magnetic field. The number of magnetic field lines passing through a surface placed perpendicular to it is called magnetic flux.',
  'مقناطیسی القا بتاتی ہے کہ مقناطیسی میدان کی لکیریں کتنی قریب ہیں، اور یوں میدان کی قوت ظاہر ہوتی ہے۔ کسی سطح سے عموداً گزرنے والی مقناطیسی میدانی خطوط کی تعداد کو مقناطیسی بہاؤ کہتے ہیں۔',
  'مقناطیسي القا ښيي چې د مقناطیسي ساحې کرښې څومره نږدې دي او په دې توګه د ساحې شدت څرګندوي. له هغې سطحې څخه چې د ساحې پر لوري عمود وي د تېرېدونکو مقناطیسي کرښو شمېر مقناطیسي فلوکس بلل کېږي.'),
 pair('A. Maximum Flux: If area vector A is parallel to the magnetic field B, then the maximum number of magnetic field lines will pass through the surface. Therefore magnetic flux will be maximum.',
  'A. زیادہ سے زیادہ بہاؤ: اگر رقبے کا سمتیہ A مقناطیسی میدان B کے متوازی ہو تو زیادہ سے زیادہ میدانی خطوط سطح سے گزریں گی۔ لہٰذا مقناطیسی بہاؤ زیادہ سے زیادہ ہو گا۔',
  'A. اعظمي فلوکس: که د مساحت ویکتور A له مقناطیسي ساحې B سره موازي وي، د مقناطیسي ساحې تر ټولو ډېرې کرښې به له سطحې تېرې شي. نو مقناطیسي فلوکس به اعظمي وي.'),
 pair('Φ_B = BA cos 0°; since cos 0° = 1, therefore Φ_B = BA ...(1)','Φ_B = BA cos 0°؛ چونکہ cos 0° = 1، لہٰذا Φ_B = BA ...(1)','Φ_B = BA cos 0°؛ ځکه cos 0° = 1، نو Φ_B = BA ...(1)'),
 pair('B. Minimum Flux: If area vector A is perpendicular to magnetic field B, then no magnetic field lines will pass through the surface. Therefore magnetic flux will be zero or minimum.',
  'B. کم سے کم بہاؤ: اگر رقبے کا سمتیہ A مقناطیسی میدان B کے عموداً ہو تو کوئی میدانی خط سطح سے نہیں گزرے گی۔ لہٰذا مقناطیسی بہاؤ صفر یا کم سے کم ہو گا۔',
  'B. لږترلږه فلوکس: که د مساحت ویکتور A پر مقناطیسي ساحې B عمود وي، د ساحې هېڅ کرښه به له سطحې تېر نه شي. نو مقناطیسي فلوکس به صفر یا لږترلږه وي.'),
 pair('Φ_B = BA cos 90°; since cos 90° = 0, therefore Φ_B = 0 ...(2)','Φ_B = BA cos 90°؛ چونکہ cos 90° = 0، لہٰذا Φ_B = 0 ...(2)','Φ_B = BA cos 90°؛ ځکه cos 90° = 0، نو Φ_B = 0 ...(2)'),
 pair('C. Flux at any Angle: If area vector A makes any angle with magnetic field B, then magnetic flux will depend upon the angle θ between them.',
  'C. کسی بھی زاویے پر بہاؤ: اگر رقبے کا سمتیہ A مقناطیسی میدان B سے کوئی زاویہ بنائے تو مقناطیسی بہاؤ ان کے درمیان زاویہ θ پر منحصر ہو گا۔',
  'C. په هره زاویه فلوکس: که د مساحت ویکتور A له مقناطیسي ساحې B سره هره زاویه جوړه کړي، مقناطیسي فلوکس به د دوی ترمنځ د θ زاویې پورې تړلی وي.'),
 pair('Φ_B = BA cos θ ...(3)','Φ_B = BA cos θ ...(3)','Φ_B = BA cos θ ...(3)'),
 pair('FIGURE 13.8 — Magnetic flux','شکل 13.8 — مقناطیسی بہاؤ','13.8 شکل — مقناطیسي فلوکس'),
 pair('MAGNETIC FLUX THROUGH CURVED OR NON-UNIFORM MAGNETIC FIELD','خمیدہ یا غیر یکساں مقناطیسی میدان میں مقناطیسی بہاؤ','په کږه یا نا یوشان مقناطیسي ساحه کې مقناطیسي فلوکس'),
 pair('If the magnetic field is non-uniform or the area is curved, then we divide the whole curved surface into small patches, each of area ΔA, such that they are approximately flat and the magnetic field is almost uniform over each patch, as shown in Figure 13.9.',
  'اگر مقناطیسی میدان غیر یکساں ہو یا رقبہ خمیدہ ہو تو پوری خمیدہ سطح کو چھوٹے حصوں میں تقسیم کرتے ہیں، ہر حصے کا رقبہ ΔA ہوتا ہے، تاکہ وہ تقریباً ہموار ہوں اور ہر حصے پر میدان تقریباً یکساں ہو، جیسا کہ شکل 13.9 میں دکھایا گیا ہے۔',
  'که مقناطیسي ساحه نا یوشان وي یا سطح کږه وي، ټوله کږه سطح په کوچنیو ټوټو وېشو چې د هرې مساحت ΔA وي؛ ټوټې نږدې هوارې او پر هره ټوټه ساحه نږدې یوشان وي، لکه په 13.9 شکل کې.'),
]
PATCHES=[
 pair('For one of these small patches, the magnetic flux is','د دغو کوچنیو برخو د یوې برخې مقناطیسی بہاؤ یہ ہے:','د دغو کوچنیو ټوټو د یوې ټوټې مقناطیسي فلوکس داسې دی:'),
 pair('ΔΦ_B = B⃗_i · ΔA⃗_i = B_i ΔA_i cos θ_i','ΔΦ_B = B⃗_i · ΔA⃗_i = B_i ΔA_i cos θ_i','ΔΦ_B = B⃗_i · ΔA⃗_i = B_i ΔA_i cos θ_i'),
 pair('To calculate the flux through the whole surface, we add the flux from each patch, such that','پوری سطح سے بہاؤ معلوم کرنے کے لیے ہر حصے کا بہاؤ جمع کرتے ہیں، یوں کہ','د ټولې سطحې فلوکس د معلومولو لپاره د هرې ټوټې فلوکسونه سره جمع کوو، داسې چې'),
 pair('Φ_B = Σ(i=1 to n) ΔΦ_B = Σ(i=1 to n) B⃗_i · ΔA⃗_i = Σ(i=1 to n) B_i ΔA_i cos θ_i','Φ_B = Σ(i=1 to n) ΔΦ_B = Σ(i=1 to n) B⃗_i · ΔA⃗_i = Σ(i=1 to n) B_i ΔA_i cos θ_i','Φ_B = Σ(i=1 to n) ΔΦ_B = Σ(i=1 to n) B⃗_i · ΔA⃗_i = Σ(i=1 to n) B_i ΔA_i cos θ_i'),
 pair('Φ_B = B cos θ Σ ΔA = BA cos θ ...(13.3)','Φ_B = B cos θ Σ ΔA = BA cos θ ...(13.3)','Φ_B = B cos θ Σ ΔA = BA cos θ ...(13.3)'),
 pair('FIGURE 13.9 — Curved surface divided into small area patches','شکل 13.9 — خمیدہ سطح کو چھوٹے رقبوں میں تقسیم کرنا','13.9 شکل — کږه سطح په کوچنیو مساحتونو وېشل'),
 pair('UNIT OF MAGNETIC FLUX AND FLUX DENSITY','مقناطیسی بہاؤ اور بہاؤ کی کثافت کی اکائی','د مقناطیسي فلوکس او فلوکس کثافت واحد'),
 pair('The SI unit of magnetic flux is equal to the unit of magnetic field (1 T) times the unit of area (m²), 1 Wb = 1 T × m². This unit is called the weber (1 Wb), in honor of the German physicist Wilhelm Weber.',
  'مقناطیسی بہاؤ کی SI اکائی، مقناطیسی میدان کی اکائی (1 T) اور رقبے کی اکائی (m²) کے حاصلِ ضرب کے برابر ہے: 1 Wb = 1 T × m²۔ اس اکائی کو جرمن طبیعیات دان ولہلم ویبر کے نام پر ویبر (1 Wb) کہتے ہیں۔',
  'د مقناطیسي فلوکس SI واحد د مقناطیسي ساحې واحد (1 T) او د مساحت واحد (m²) د ضرب سره برابر دی: 1 Wb = 1 T × m². د جرمني فزیک‌پوه وېلهلم وېبر په ویاړ دې واحد ته وېبر (1 Wb) ویل کېږي.'),
 pair('1 Wb = 1 T × m² (1 T = 1 N/(A m))','1 Wb = 1 T × m² (1 T = 1 N/(A m))','1 Wb = 1 T × m² (1 T = 1 N/(A m))'),
 pair('So 1 Wb = 1 N m/A','لہٰذا 1 Wb = 1 N m/A','نو 1 Wb = 1 N m/A'),
 pair('The unit of magnetic induction can be written as T = Wb m⁻².','مقناطیسی القا کی اکائی کو T = Wb m⁻² لکھا جا سکتا ہے۔','د مقناطیسي القا واحد د T = Wb m⁻² په بڼه لیکل کېدای شي.'),
 pair('13.4 AMPERE CIRCUITAL LAW','13.4 ایمپیئر کا دوری قانون','13.4 د امپېر د کړۍ قانون'),
 pair('Ampere’s circuital law, given by Andre Marie Peter Ampere in 1826, relates the integrated magnetic field in a loop around a current-carrying wire to the current passing through the wire.',
  '1826 میں آندرے میری پیٹر ایمپیئر کا پیش کردہ دوری قانون، کرنٹ بردار تار کے گرد حلقے میں مقناطیسی میدان کے تکمل کو تار سے گزرنے والی برقی رو سے مربوط کرتا ہے۔',
  'د امپېر د کړۍ قانون، چې اندري ماري پېټر امپېر په 1826 کې ورکړ، د جریان‌لرونکي سیم شاوخوا په کړۍ کې مدغم مقناطیسي ساحه له هغه جریان سره تړي چې له سیم څخه تېرېږي.'),
 pair('Ampère’s circuital law states that, for any closed loop, the sum of each length element multiplied by the component of magnetic field parallel to that element is proportional to the current enclosed by the path.',
  'ایمپیئر کا دوری قانون کہتا ہے کہ کسی بھی بند حلقے میں ہر طولی عنصر اور اس عنصر کے متوازی مقناطیسی میدان کے جزو کے حاصلِ ضرب کا مجموعہ، اس راستے کے اندر محصور برقی رو کے متناسب ہوتا ہے۔',
  'د امپېر د کړۍ قانون وايي چې په هره تړلې کړۍ کې د هر اوږدوالي عنصر او له هغه عنصر سره موازي د مقناطیسي ساحې د جز د ضربونو مجموعه د لارې دننه محصور جریان سره متناسب ده.'),
 pair('Σ B⃗ · Δl⃗ = μ₀ I','Σ B⃗ · Δl⃗ = μ₀ I','Σ B⃗ · Δl⃗ = μ₀ I'),
]

def make(identity,title,printed,pairs,layout,titles,refs,diagram=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':52,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(x) for x in refs]
 if diagram:s.update(diagram);s['content']+=diagram['diagramSvg']
 return r,s
def flux_svg(lang):
 L={'en':('Magnetic field B','Area vector A','Magnetic flux'),'ur':('مقناطیسی میدان B','رقبے کا سمتیہ A','مقناطیسی بہاؤ'),'ps':('مقناطیسي ساحه B','د مساحت ویکتور A','مقناطیسي فلوکس')}[lang]
 b='<g stroke="#d4a72c" stroke-width="3"><path d="M25 74H185M25 105H185M25 136H185M25 167H185M25 198H185"/><path d="M225 74H385M225 105H385M225 136H385M225 167H385M225 198H385"/><path d="M425 74H595M425 105H595M425 136H595M425 167H595M425 198H595"/></g>'
 b+='<path d="M80 82L142 75 155 198 92 205Z" fill="#d8b4fe" stroke="#6b21a8" stroke-width="3"/><path d="M300 112L355 115 350 169 295 166Z" fill="#d8b4fe" stroke="#6b21a8" stroke-width="3"/><path d="M490 82L555 96 528 198 463 184Z" fill="#d8b4fe" stroke="#6b21a8" stroke-width="3"/>'
 b+='<path d="M155 140H202M323 140V80M515 140L556 83" stroke="#2563eb" stroke-width="3"/><path d="M194 132l12 8-12 8M315 92l8-12 8 12M546 88l13-7-2 15" fill="#2563eb"/>'
 b+='<text x="22" y="35" font-size="14">(a) Φ_B = BA</text><text x="221" y="35" font-size="14">(b) Φ_B = 0</text><text x="420" y="35" font-size="14">(c) Φ_B = BA cos θ</text><text x="25" y="255" font-size="13">'+L[0]+'</text><text x="235" y="255" font-size="13">'+L[1]+'</text><text x="455" y="255" font-size="13">'+L[2]+'</text>'
 return svg(b,'Figure 13.8: maximum, zero and angle-dependent magnetic flux through surfaces.')
def patches_svg(lang):
 L={'en':('Magnetic field B','Area patches ΔA','Curved surface'),'ur':('مقناطیسی میدان B','رقبے کے حصے ΔA','خمیدہ سطح'),'ps':('مقناطیسي ساحه B','د مساحت ټوټې ΔA','کږه سطح')}[lang]
 b='<path d="M35 70H580M35 110H580M35 150H580M35 190H580M35 230H580" stroke="#d4a72c" stroke-width="3"/><path d="M250 55L345 62 396 108 360 160 397 207 323 244 255 220 212 178 232 126 205 88Z" fill="#d8b4fe" stroke="#6b21a8" stroke-width="3"/>'
 b+='<path d="M255 95L210 60M322 115L325 58M360 165L420 120M312 203L340 270" stroke="#2563eb" stroke-width="3"/><path d="M216 66l-10-9 14 1M318 68l7-13 7 13M411 122l13-5-7 12M337 260l4 14-11-8" fill="#2563eb"/><path d="M35 55h80" stroke="#2563eb" stroke-width="3"/><path d="M107 48l12 7-12 7" fill="#2563eb"/><text x="24" y="35" font-size="14">'+L[0]+'</text><text x="220" y="285" font-size="14">'+L[1]+'</text><text x="405" y="35" font-size="14">'+L[2]+'</text><text x="235" y="95" font-size="12">ΔA₁</text><text x="333" y="52" font-size="12">ΔAᵢ</text><text x="422" y="116" font-size="12">ΔAₙ</text>'
 return svg(b,'Figure 13.9: curved surface divided into small area patches with local area vectors.')

if __name__=='__main__':
 layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'equation','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'visual'},{'type':'heading','indices':[11]},{'type':'paragraph','indices':[12]}]
 f=make('phys13-magnetic-flux94','13.3 Magnetic flux — area orientation and curved surfaces',94,FLUX,layout,('13.3 مقناطیسی بہاؤ — رقبے کی سمت اور خمیدہ سطحیں','13.3 مقناطیسي فلوکس — د مساحت لوری او کږې سطحې'),[94],{'diagramSvg':flux_svg('en'),'diagramSvgUrdu':flux_svg('ur'),'diagramSvgPashto':flux_svg('ps')})
 layout2=[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[5]},{'type':'visual'},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]},{'type':'equation','indices':[4]},{'type':'heading','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]},{'type':'heading','indices':[11]},{'type':'paragraph','indices':[12]},{'type':'paragraph','indices':[13]},{'type':'equation','indices':[14]}]
 p=make('phys13-curved-flux-units-ampere95','Curved-surface flux, Weber units and Ampere’s circuital law',95,PATCHES,layout2,('خمیدہ سطح کا بہاؤ، ویبر اکائیاں اور ایمپیئر کا دوری قانون','د کږې سطحې فلوکس، وېبر واحدونه او د امپېر د کړۍ قانون'),[95],{'diagramSvg':patches_svg('en'),'diagramSvgUrdu':patches_svg('ur'),'diagramSvgPashto':patches_svg('ps')})
 formulas=[
  {'id':'phys13-eq-magnetic-flux','name':'Magnetic flux','formula':FLUX[2][0],'latex':'Φ_B = B·A = BA cos θ','sourceReferences':[ref(94)]},
  {'id':'phys13-eq-flux-curved-surface-13.3','name':'Magnetic flux through a curved or non-uniform surface','number':'13.3','formula':PATCHES[4][0],'latex':'Φ_B = B cos θ ΣΔA = BA cos θ','sourceReferences':[ref(95)]},
  {'id':'phys13-ampere-circuital-law','name':'Ampere circuital law','formula':PATCHES[14][0],'latex':'Σ B·Δl = μ₀ I','sourceReferences':[ref(95)]},
 ]
 definitions=[
  {'term':'Magnetic flux','definition':FLUX[1][0],'definitionUrdu':FLUX[1][1],'definitionPashto':FLUX[1][2],'sourceReferences':[ref(94)]},
  {'term':'Weber','definition':PATCHES[7][0],'definitionUrdu':PATCHES[7][1],'definitionPashto':PATCHES[7][2],'sourceReferences':[ref(95)]},
  {'term':'Ampere’s circuital law','definition':PATCHES[12][0]+' '+PATCHES[13][0]+' '+PATCHES[14][0],'definitionUrdu':PATCHES[12][1]+' '+PATCHES[13][1]+' '+PATCHES[14][1],'definitionPashto':PATCHES[12][2]+' '+PATCHES[13][2]+' '+PATCHES[14][2],'sourceReferences':[ref(95)]},
 ]
 records=[f[0],p[0]];sections=[f[1],p[1]]
 with shared_class_data_lock():
  upsert(records,sections,chapter_index=2)
  sync_companions(chapter_index=2,retire_sections=['13.2'],trim_sections=[{'id':'13.3','startsAt':'Ampere law is the relation between magnetic','title':'Ampere-law continuation — first unchecked text on printed page 96'}],formulas=formulas,definitions=definitions)
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==52:
  checkpoint(52,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 52, printed pages 94–95. Compared the scalar-product definition and all three orientation cases/equations, Figures 13.8–13.9, curved/non-uniform-surface patch derivation through Eq. 13.3, Weber and tesla units, Ampere’s circuital-law explanation and line integral relation. Rebuilt both diagrams as translated inline SVG, synchronized formulas/definitions, retired the now-covered legacy force/flux continuation and retained the next unchecked Ampere-law explanation beginning on printed page 96.',printed_pages=[94,95],chapter_number=13)
