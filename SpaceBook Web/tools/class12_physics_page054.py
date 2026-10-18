"""Sequential source correction for PDF page 54 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def ref(p): return {'pdfPage':54,'printedPage':p,'sourcePdf':SOURCE}
def svg(body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 390" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:720px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

SOLUTION=[
 pair('The net magnetic field is B_net = B₁ + B₂.','خالص مقناطیسی میدان B_net = B₁ + B₂ ہے۔','خالصه مقناطیسي ساحه B_net = B₁ + B₂ ده.'),
 pair('As the fields are opposite in the middle, therefore B_net = B₁ − B₂.','چونکہ وسط میں دونوں میدان مخالف سمتوں میں ہیں، اس لیے B_net = B₁ − B₂۔','ځکه چې په منځ کې ساحې مخالف لوري لري، نو B_net = B₁ − B₂.'),
 pair('Applying Ampere’s circuital law: B_net = μ₀ I₁/(2πr₁) − μ₀ I₂/(2πr₂).','ایمپیئر کا دوری قانون لگانے سے: B_net = μ₀ I₁/(2πr₁) − μ₀ I₂/(2πr₂)۔','د امپېر د کړۍ قانون په پلي کولو: B_net = μ₀ I₁/(2πr₁) − μ₀ I₂/(2πr₂).'),
 pair('Putting values: B_net = (4π × 10⁻⁷ T m/A)(8 A)/(2π × 0.03 m) − (4π × 10⁻⁷ T m/A)(2 A)/(2π × 0.03 m).','قدریں رکھنے سے: B_net = (4π × 10⁻⁷ T m/A)(8 A)/(2π × 0.03 m) − (4π × 10⁻⁷ T m/A)(2 A)/(2π × 0.03 m)۔','د ارزښتونو په ایښودلو: B_net = (4π × 10⁻⁷ T m/A)(8 A)/(2π × 0.03 m) − (4π × 10⁻⁷ T m/A)(2 A)/(2π × 0.03 m).'),
 pair('Therefore B_net = 4 × 10⁻⁵ T.','لہٰذا B_net = 4 × 10⁻⁵ T۔','نو B_net = 4 × 10⁻⁵ T.'),
]
ASSIGN=[
 pair('ASSIGNMENT 13.1 — MAGNETIC FIELD OF A LONG WIRE','مشق 13.1 — لمبے تار کا مقناطیسی میدان','دنده 13.1 — د اوږده سیم مقناطیسي ساحه'),
 pair('A long straight wire carries a current of 1 A. Find the magnitude of the magnetic field at a distance 1 m from it.','ایک لمبے سیدھے تار میں 1 A رو بہتی ہے۔ تار سے 1 m فاصلے پر مقناطیسی میدان کی مقدار معلوم کریں۔','په یوه اوږده نېغ سیم کې 1 A جریان تېرېږي. له سیم څخه په 1 m واټن کې د مقناطیسي ساحې اندازه ومومئ.'),
 pair('Printed answer: 2 × 10⁻⁵ T.','مطبوعہ جواب: 2 × 10⁻⁵ T۔','چاپ شوی ځواب: 2 × 10⁻⁵ T.'),
]
SOLENOID=[
 pair('A. MAGNETIC FIELD DUE TO A CURRENT-CARRYING SOLENOID','الف۔ کرنٹ بردار سولینائڈ کی وجہ سے مقناطیسی میدان','الف. د جریان‌لرونکي سولینایډ له امله مقناطیسي ساحه'),
 pair('A coil wound in the form of a spiral (helix) forms a solenoid. When current is passed through a solenoid, a reasonably uniform magnetic field can be produced. This field is strong along the axis of the solenoid and weaker outside, as shown in Figure 13.12.','حلزونی شکل میں لپٹی ہوئی کوائل سولینائڈ بناتی ہے۔ سولینائڈ میں رو گزارنے سے نسبتاً یکساں مقناطیسی میدان پیدا کیا جا سکتا ہے۔ یہ میدان سولینائڈ کے محور کے ساتھ مضبوط اور باہر کمزور ہوتا ہے، جیسا کہ شکل 13.12 میں ہے۔','په حلزوني بڼه تاو شوی کویل سولینایډ جوړوي. په سولینایډ کې د جریان په تېرولو نسبتاً یوشان مقناطیسي ساحه جوړېدای شي. دا ساحه د سولینایډ د محور په اوږدو کې پیاوړې او بهر کمزورې وي، لکه په 13.12 شکل کې.'),
 pair('Figure 13.12 — (a) Solenoid; (b) iron filings in the magnetic field due to a single loop of coil; (c) iron filings in the magnetic field due to a solenoid.','شکل 13.12 — (الف) سولینائڈ؛ (ب) کوائل کے ایک چکر کے مقناطیسی میدان میں لوہے کا برادہ؛ (ج) سولینائڈ کے مقناطیسی میدان میں لوہے کا برادہ۔','13.12 شکل — (الف) سولینایډ؛ (ب) د کویل د یوه تاو د مقناطیسي ساحې په برخه کې د اوسپنې براده؛ (ج) د سولینایډ د مقناطیسي ساحې په برخه کې د اوسپنې براده.'),
 pair('The magnetic field lines surrounding a loosely wound solenoid show that the lines in its interior are nearly parallel to one another, uniformly distributed, and close together.','د ڈھیلے لپٹے سولینائڈ کے گرد مقناطیسی میدان کی لکیریں دکھاتی ہیں کہ اندرونی لکیریں تقریباً متوازی، یکساں طور پر تقسیم اور ایک دوسرے کے قریب ہیں۔','د کم تاو لرونکي سولینایډ شاوخوا د مقناطیسي ساحې کرښې ښيي چې دننه کرښې نږدې موازي، په یوشان ډول وېشل شوې او سره نږدې دي.'),
 pair('For a tightly wound solenoid, the field in the interior space is very uniform and strong. The field lines resemble those of a bar magnet, meaning that the solenoid effectively has north and south poles.','گھنے لپٹے ہوئے سولینائڈ کے اندرونی حصے میں میدان بہت یکساں اور مضبوط ہوتا ہے۔ اس کی میدان لکیریں سلاخ نما مقناطیس جیسی ہوتی ہیں، یعنی سولینائڈ کے مؤثر شمالی اور جنوبی قطب ہوتے ہیں۔','په کلک تاو شوي سولینایډ کې دننه ساحه ډېره یوشان او پیاوړې وي. د ساحې کرښې یې د میله‌يي مقناطیس په څېر وي؛ یعنې سولینایډ په اغېزمنه توګه شمالي او جنوبي قطبونه لري.'),
 pair('As the length of the solenoid increases, the interior field becomes more uniform and the exterior field becomes weaker, as shown in Figure 13.13.','سولینائڈ کی لمبائی بڑھنے سے اندرونی میدان زیادہ یکساں اور بیرونی میدان کمزور ہوتا جاتا ہے، جیسا کہ شکل 13.13 میں ہے۔','د سولینایډ د اوږدوالي په زیاتېدو دننه ساحه لا یوشان او بهرنی ساحه کمزورې کېږي، لکه په 13.13 شکل کې.'),
 pair('Figure 13.13 — (a) Magnetic field lines for a loosely wound solenoid; (b) magnetic field lines for a tightly wound solenoid carrying a steady current.','شکل 13.13 — (الف) ڈھیلے لپٹے سولینائڈ کی مقناطیسی میدان کی لکیریں؛ (ب) مستقل رو والے گھنے لپٹے سولینائڈ کی مقناطیسی میدان کی لکیریں۔','13.13 شکل — (الف) کم تاو لرونکي سولینایډ د مقناطیسي ساحې کرښې؛ (ب) د ثابت جریان لرونکي کلک تاو شوي سولینایډ د مقناطیسي ساحې کرښې.'),
 pair('An ideal solenoid is approached when the turns are closely spaced and its length is much greater than the radius of its turns. In this case, the external field is close to zero and the interior field is uniform over a great volume.','مثالی سولینائڈ اس وقت حاصل ہوتا ہے جب چکر قریب قریب ہوں اور اس کی لمبائی چکروں کے رداس سے بہت زیادہ ہو۔ ایسی صورت میں بیرونی میدان تقریباً صفر اور اندرونی میدان ایک بڑے حجم میں یکساں ہوتا ہے۔','ایډیال سولینایډ هغه مهال رامنځته کېږي چې تاوونه سره نږدې وي او اوږدوالی یې د تاوونو له شعاع څخه ډېر زیات وي. په دې حالت کې بهرنی ساحه نږدې صفر او دننه ساحه په لوی حجم کې یوشان وي.'),
 pair('Ampere’s law can be used to obtain a quantitative expression for the interior magnetic field in an ideal solenoid.','ایمپیئر کے قانون سے مثالی سولینائڈ کے اندرونی مقناطیسی میدان کا مقداری تعلق حاصل کیا جا سکتا ہے۔','د امپېر قانون په وسیله د ایډیال سولینایډ دننه مقناطیسي ساحې لپاره مقداري اړیکه موندل کېدای شي.'),
]

def make(identity,title,printed,pairs,layout,titles,refs,diagram=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':54,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(x) for x in refs]
 if diagram: s.update(diagram);s['content']+=diagram['diagramSvg']
 return r,s

def fig12(lang):
 labels={'en':('Solenoid','Single current loop','Solenoid field pattern'),'ur':('سولینائڈ','برقی رو کا ایک چکر','سولینائڈ کا میدان'),'ps':('سولینایډ','د جریان یو تاو','د سولینایډ ساحه')}[lang]
 b='<path d="M24 65H224M24 105H224M24 145H224M24 185H224M24 225H224" stroke="#b45309" stroke-width="3"/><path d="M105 55V236M120 55V236M135 55V236M150 55V236" stroke="#7c2d12" stroke-width="6"/><path d="M105 55C165 45 165 245 105 236M150 55C90 45 90 245 150 236" fill="none" stroke="#2563eb" stroke-width="2"/><text x="28" y="285" font-size="14">(a) '+labels[0]+'</text>'
 b+='<circle cx="350" cy="145" r="48" fill="none" stroke="#7c2d12" stroke-width="7"/><g fill="none" stroke="#2563eb" stroke-width="2"><ellipse cx="350" cy="145" rx="85" ry="52"/><ellipse cx="350" cy="145" rx="110" ry="72"/><ellipse cx="350" cy="145" rx="132" ry="94"/></g><text x="258" y="285" font-size="14">(b) '+labels[1]+'</text>'
 b+='<path d="M508 80V212M520 80V212M532 80V212M544 80V212M556 80V212M568 80V212" stroke="#7c2d12" stroke-width="6"/><g fill="none" stroke="#2563eb" stroke-width="2"><path d="M508 82C455 45 455 247 508 210M568 82C621 45 621 247 568 210"/><path d="M520 82C470 62 470 230 520 210M556 82C606 62 606 230 556 210"/><path d="M508 95H568M508 125H568M508 155H568M508 185H568"/></g><text x="462" y="285" font-size="14">(c) '+labels[2]+'</text>'
 return svg(b,'Figure 13.12: solenoid, magnetic field around one current loop, and magnetic field of a solenoid.')

def fig13(lang):
 labels={'en':('Loosely wound: less uniform interior field','Tightly wound: strong, uniform interior field','N','S'),'ur':('ڈھیلے چکر: اندرونی میدان کم یکساں','گھنے چکر: اندرونی میدان مضبوط اور یکساں','ش','ج'),'ps':('کم تاوونه: دننه ساحه لږه یوشان','کلک تاوونه: دننه ساحه پیاوړې او یوشان','ش','ج')}[lang]
 b='<rect x="18" y="32" width="332" height="310" fill="#fff" stroke="#94a3b8"/><rect x="370" y="32" width="332" height="310" fill="#fff" stroke="#94a3b8"/>'
 for x in [150,205,260,555,575,595,615,635]:
  b+=f'<ellipse cx="{x}" cy="185" rx="9" ry="72" fill="none" stroke="#7c2d12" stroke-width="3"/>'
 for x in [75,110,145,180,215,250,285,320]:
  b+=f'<path d="M{x} 105C{x-44} 72 {x-44} 298 {x} 265" fill="none" stroke="#2563eb" stroke-width="2"/>'
  if x in [110,215,320]: b+=f'<path d="M{x-8} 115l8-10 8 10" fill="#2563eb"/>'
 for y in [115,145,175,205,235,265]:
  b+=f'<path d="M515 {y}H675" stroke="#2563eb" stroke-width="2"/><path d="M666 {y-7}l10 7-10 7" fill="#2563eb"/>'
 for x in [555,575,595,615,635]: b+=f'<path d="M{x} 100V270" stroke="#7c2d12" stroke-width="4"/>'
 b+=f'<text x="176" y="62" font-size="15">{labels[2]}</text><text x="176" y="325" font-size="15">{labels[3]}</text><text x="528" y="62" font-size="15">{labels[2]}</text><text x="528" y="325" font-size="15">{labels[3]}</text>'
 b+=f'<text x="28" y="365" font-size="13">(a) {labels[0]}</text><text x="380" y="365" font-size="13">(b) {labels[1]}</text>'
 return svg(b,'Figure 13.13: magnetic field lines of loosely and tightly wound current-carrying solenoids.')

if __name__=='__main__':
 PAGE54=SOLUTION+ASSIGN+SOLENOID[:6]+SOLENOID[7:]
 s1=make('phys13-example132-solution-assignment131-solenoid-intro98','Example 13.2 solution, Assignment 13.1 and introduction to a current-carrying solenoid',98,PAGE54,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]},{'type':'equation','indices':[4]},{'type':'heading','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'heading','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'visual'},{'type':'paragraph','indices':[10]},{'type':'paragraph','indices':[11]},{'type':'paragraph','indices':[12]},{'type':'paragraph','indices':[13]},{'type':'paragraph','indices':[14]},{'type':'paragraph','indices':[15]}],('مثال 13.2 کا حل، مشق 13.1 اور کرنٹ بردار سولینائڈ کا تعارف','د 13.2 بېلګې حل، 13.1 دنده او د جریان‌لرونکي سولینایډ پېژندنه'),[98,99],{'diagramSvg':fig12('en'),'diagramSvgUrdu':fig12('ur'),'diagramSvgPashto':fig12('ps')})
 sol=make('phys13-solenoid-field-pattern-figure1313-99','Figure 13.13 — magnetic field lines in loosely and tightly wound solenoids',99,[SOLENOID[6],SOLENOID[8]],[{'type':'paragraph','indices':[0]},{'type':'visual'},{'type':'paragraph','indices':[1]}],('شکل 13.13 — ڈھیلے اور گھنے سولینائڈ کے میدان کی لکیریں','13.13 شکل — د کم او کلک تاو لرونکو سولینایډونو د ساحې کرښې'),[99],{'diagramSvg':fig13('en'),'diagramSvgUrdu':fig13('ur'),'diagramSvgPashto':fig13('ps')})
 records=[s1[0],sol[0]];sections=[s1[1],sol[1]]
 work={'id':'phys12-example-13-2','title':'Magnetic field midway between two parallel wires','question':'Two long parallel wires 6 cm apart carry currents of 8 A and 2 A in the same direction. Find the magnetic field midway between them.','questionUrdu':'دو لمبی متوازی تاریں 6 cm کے فاصلے پر ہیں اور ان میں 8 A اور 2 A کی رو ایک ہی سمت میں بہتی ہے۔ درمیان میں مقناطیسی میدان معلوم کریں۔','questionPashto':'دوه اوږده موازي سیمونه 6 cm واټن لري او 8 A او 2 A جریانونه په یوه لوري لېږدوي. په منځ کې مقناطیسي ساحه ومومئ.','given':[ 'I₁ = 8 A; I₂ = 2 A', 'r₁ = r₂ = 6 cm/2 = 0.03 m'],'givenUrdu':['I₁ = 8 A؛ I₂ = 2 A','r₁ = r₂ = 6 cm/2 = 0.03 m'],'givenPashto':['I₁ = 8 A؛ I₂ = 2 A','r₁ = r₂ = 6 cm/2 = 0.03 m'],'required':['B_net = ?'],'requiredUrdu':['B_net = ؟'],'requiredPashto':['B_net = ؟'],'steps':[SOLUTION[0][0],SOLUTION[1][0],SOLUTION[2][0],SOLUTION[3][0],SOLUTION[4][0]],'stepsUrdu':[SOLUTION[0][1],SOLUTION[1][1],SOLUTION[2][1],SOLUTION[3][1],SOLUTION[4][1]],'stepsPashto':[SOLUTION[0][2],SOLUTION[1][2],SOLUTION[2][2],SOLUTION[3][2],SOLUTION[4][2]],'answer':'4 × 10⁻⁵ T','solutionOrigin':'textbook worked solution','sourceReferences':[ref(98)]}
 exercise={'id':'phys12-assignment-13-1','title':'Magnetic field of a long straight wire','question':ASSIGN[1][0],'questionUrdu':ASSIGN[1][1],'questionPashto':ASSIGN[1][2],'answer':'2 × 10⁻⁵ T','sourceAnswer':ASSIGN[2][0],'sourceReferences':[ref(98)]}
 formulas=[{'id':'phys13-long-wire-field','name':'Magnetic field around a long straight wire','formula':'B = (μ₀/2π)(I/r)','latex':'B = μ₀I/(2πr)','sourceReferences':[ref(98)]}]
 definitions=[{'term':'Solenoid','definition':SOLENOID[1][0],'definitionUrdu':SOLENOID[1][1],'definitionPashto':SOLENOID[1][2],'sourceReferences':[ref(98)]},{'term':'Ideal solenoid','definition':SOLENOID[7][0],'definitionUrdu':SOLENOID[7][1],'definitionPashto':SOLENOID[7][2],'sourceReferences':[ref(99)]}]
 with shared_class_data_lock():
  upsert(records,sections,chapter_index=2)
  sync_companions(chapter_index=2,retire_sections=['13.3'],trim_sections=[{'id':'13.4','startsAt':'Consider an closed Amperian path','title':'Solenoid Ampere-path derivation — first unchecked text on printed page 100'}],worked_examples=[work],exercises=[exercise],formulas=formulas,definitions=definitions)
 progress=json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))
 if progress['nextPage']==54:
  checkpoint(54,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 54, printed pages 98–99. Compared Example 13.2 solution including opposing midpoint fields and the printed 4 × 10⁻⁵ T answer; Assignment 13.1 question and printed 2 × 10⁻⁵ T answer; solenoid definition and field behavior; ideal-solenoid conditions; and Figures 13.12–13.13 and captions. Added aligned Urdu/Pashto text, coded translated SVG field diagrams, and synchronized the worked example, exercise, and solenoid definitions. The legacy section 13.3 was retired after its solution was covered; section 13.4 was trimmed at its first unchecked printed-page-100 derivation.',printed_pages=[98,99],chapter_number=13)
