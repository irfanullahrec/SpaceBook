"""Sequential source correction for PDF page 53 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(p):return {'pdfPage':53,'printedPage':p,'sourcePdf':SOURCE}
def svg(body,label):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 330" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:620px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

AMPERE=[
 pair('Ampere law is the relation between magnetic field and current near a current-carrying conductor. When no current is present in the wire, all compass needles point in the same direction (toward the Earth’s north pole). When the wire carries a strong current, the compass needles deflect in a direction tangent to the circle, which is the direction of the magnetic field created by the current. Now consider a test point P located at distance r from the current-carrying conductor, where we want to find the magnitude of magnetic induction B as shown in Figure 13.10. At point P, magnetic induction is directly proportional to the current I flowing through the conductor and inversely proportional to the distance r from the wire.',
  'ایمپیئر کا قانون کرنٹ بردار موصل کے قریب مقناطیسی میدان اور برقی رو کا تعلق ہے۔ تار میں رو نہ ہو تو قطب نما کی تمام سوئیاں ایک ہی سمت (زمین کے شمالی قطب کی طرف) اشارہ کرتی ہیں۔ تار میں تیز رو گزرنے پر سوئیاں دائرے کے مماس سمت میں مڑتی ہیں، جو رو کے پیدا کردہ مقناطیسی میدان کی سمت ہے۔ اب تار سے فاصلے r پر واقع آزمائشی نقطے P پر غور کریں جہاں شکل 13.10 کے مطابق مقناطیسی القا B کی مقدار معلوم کرنی ہے۔ نقطہ P پر B، تار میں بہنے والی رو I کے براہ راست اور تار سے فاصلے r کے الٹ متناسب ہے۔',
  'د امپېر قانون د جریان‌لرونکي هادي ته نږدې د مقناطیسي ساحې او جریان اړیکه ده. که په سیم کې جریان نه وي، د قطب‌نما ټولې ستنې یوې خوا (د ځمکې شمالي قطب) ته وي. کله چې په سیم کې پیاوړی جریان تېر شي، ستنې د دایرې پر مماس لوري اوړي؛ دا د جریان له خوا د جوړې شوې مقناطیسي ساحې لوری دی. اوس د سیم څخه په r واټن کې ازمېښتي ټکی P په پام کې ونیسئ، چې د 13.10 شکل له مخې پکې د مقناطیسي القا B اندازه موندل کېږي. په P کې B په سیم کې له جریان I سره مستقیم او له واټن r سره معکوس تناسب لري.'),
 pair('B ∝ I/r, or B = (μ₀/2π)(I/r) ...(1)','B ∝ I/r، یا B = (μ₀/2π)(I/r) ...(1)','B ∝ I/r، یا B = (μ₀/2π)(I/r) ...(1)'),
 pair('Where μ₀/2π is the constant of proportionality, and μ₀ is the permeability of a vacuum. Its value is 4π × 10⁻⁷ T m/A or 4π × 10⁻⁷ Wb/(A m). Since the sum of all the length elements Δl gives the circumference of a circle 2πr,','جہاں μ₀/2π تناسب کا مستقل ہے اور μ₀ خلا کی نفوذ پذیری ہے۔ اس کی قدر 4π × 10⁻⁷ T m/A یا 4π × 10⁻⁷ Wb/(A m) ہے۔ چونکہ تمام طولی عناصر Δl کا مجموعہ دائرے کا محیط 2πr دیتا ہے، اس لیے','دلته μ₀/2π د تناسب ثابت دی او μ₀ د تشې نفوذپذیري ده. ارزښت یې 4π × 10⁻⁷ T m/A یا 4π × 10⁻⁷ Wb/(A m) دی. ځکه د ټولو اوږدوالي عناصرو Δl مجموعه د دایرې محیط 2πr جوړوي، نو'),
 pair('Σ Δl = 2πr ...(2)','Σ Δl = 2πr ...(2)','Σ Δl = 2πr ...(2)'),
 pair('AMPERE (1775–1836)','ایمپیئر (1775–1836)','امپېر (1775–1836)'),
 pair('Ampère, a Frenchman, is credited with the discovery of electromagnetism — the relationship between electric currents and magnetic fields.',
  'فرانسیسی ایمپیئر کو برقی مقناطیسیت یعنی برقی روؤں اور مقناطیسی میدانوں کے تعلق کی دریافت کا سہرا دیا جاتا ہے۔','فرانسوی امپېر ته د برېښنا-مقناطیسیت، یعنې د برېښنايي جریانونو او مقناطیسي ساحو د اړیکې د موندلو کریډېټ ورکول کېږي.'),
 pair('FIGURE 13.10 — Ampere’s circuital law','شکل 13.10 — ایمپیئر کا دوری قانون','13.10 شکل — د امپېر د کړۍ قانون'),
 pair('PERMEABILITY (μ)','نفوذ پذیری (μ)','نفوذپذیري (μ)'),
 pair('The permeability of a vacuum (μ₀) is 4π × 10⁻⁷ Wb/(A·m) (webers/ampere-turn·meter) and is used as a reference. The relative permeability (μᵣ) of a material is the ratio of its absolute permeability to the permeability of a vacuum.',
  'خلا کی نفوذ پذیری (μ₀) ‏4π × 10⁻⁷ Wb/(A·m) (ویبر/ایمپیئر ٹرن·میٹر) ہے اور اسے حوالہ بنایا جاتا ہے۔ کسی مادے کی نسبتی نفوذ پذیری (μᵣ)، اس کی مطلق نفوذ پذیری اور خلا کی نفوذ پذیری کا تناسب ہے۔',
  'د تشې نفوذپذیري (μ₀) ‏4π × 10⁻⁷ Wb/(A·m) (وېبر/امپېر-تاو·متر) ده او د مرجع په توګه کارېږي. د مادې نسبي نفوذپذیري (μᵣ) د هغې د مطلقې نفوذپذیرۍ او د تشې د نفوذپذیرۍ نسبت دی.'),
 pair('μᵣ = μ/μ₀','μᵣ = μ/μ₀','μᵣ = μ/μ₀'),
 pair('Because it is a ratio of permeabilities, μᵣ is dimensionless. Typical magnetic materials, such as iron, have a relative permeability of a few hundred.',
  'چونکہ یہ نفوذ پذیریوں کا تناسب ہے، اس لیے μᵣ بے بُعد ہے۔ لوہے جیسے عام مقناطیسی مادوں کی نسبتی نفوذ پذیری چند سو ہوتی ہے۔','ځکه چې دا د نفوذپذیریو نسبت دی، μᵣ بې‌بعده ده. د اوسپنې په څېر د عادي مقناطیسي موادو نسبي نفوذپذیري څو سوه وي.'),
 pair('From equation 1 and equation 2, the dot product of B for any closed path Δl can be written as','له مساوات 1 اور مساوات 2 سے، کسی بھی بند راستے Δl پر B کا نقطی ضرب یوں لکھا جا سکتا ہے:','له 1 او 2 معادلو څخه، د هرې تړلې لارې Δl لپاره د B سکالر ضرب داسې لیکل کېدای شي:'),
 pair('Σ B⃗ · Δl⃗ = (μ₀I/2πr) Σ Δl','Σ B⃗ · Δl⃗ = (μ₀I/2πr) Σ Δl','Σ B⃗ · Δl⃗ = (μ₀I/2πr) Σ Δl'),
 pair('or Σ B⃗ · Δl⃗ = (μ₀I/2πr) × 2πr','یا Σ B⃗ · Δl⃗ = (μ₀I/2πr) × 2πr','یا Σ B⃗ · Δl⃗ = (μ₀I/2πr) × 2πr'),
 pair('hence Σ B⃗ · Δl⃗ = μ₀I ...(13.4)','لہٰذا Σ B⃗ · Δl⃗ = μ₀I ...(13.4)','نو Σ B⃗ · Δl⃗ = μ₀I ...(13.4)'),
 pair('Equation 13.4 is Ampere’s law. The closed path is called an Amperian path. In general, this law can be applied to any closed path around a current-carrying conductor, as shown in Figure 13.11. For any medium other than vacuum or air, the permeability μ of that material is used in the equation for Ampere’s law.',
  'مساوات 13.4 ایمپیئر کا قانون ہے۔ بند راستے کو ایمپیئر کا راستہ کہتے ہیں۔ یہ قانون کرنٹ بردار موصل کے گرد کسی بھی بند راستے پر لاگو کیا جا سکتا ہے، جیسا کہ شکل 13.11 میں ہے۔ خلا یا ہوا کے علاوہ کسی اور واسطے کے لیے ایمپیئر کے قانون میں اس مادے کی نفوذ پذیری μ استعمال ہوتی ہے۔',
  '13.4 معادله د امپېر قانون دی. تړلې لاره د امپېر لاره بلل کېږي. دا قانون د جریان‌لرونکي هادي شاوخوا پر هره تړلې لاره پلي کېږي، لکه په 13.11 شکل کې. له تشې یا هوا پرته د بل منځني لپاره د امپېر په معادله کې د هماغه موادو نفوذپذیري μ کارول کېږي.'),
 pair('FIGURE 13.11 — Amperian path','شکل 13.11 — ایمپیئر کا راستہ','13.11 شکل — د امپېر لاره'),
 pair('EXAMPLE 13.2 — MAGNETIC FIELD BETWEEN CURRENT-CARRYING WIRES','مثال 13.2 — کرنٹ بردار تاروں کے درمیان مقناطیسی میدان','بېلګه 13.2 — د جریان‌لرونکو سیمونو ترمنځ مقناطیسي ساحه'),
 pair('Two long parallel wires 6 cm apart carry currents of 8 A and 2 A in the same direction. What is the magnitude of the magnetic field midway between them?',
  'دو لمبی متوازی تاریں 6 cm کے فاصلے پر ہیں اور ان میں 8 A اور 2 A کی برقی رو ایک ہی سمت میں بہتی ہے۔ ان کے درمیان وسط میں مقناطیسی میدان کی مقدار کیا ہے؟',
  'دوه اوږده موازي سیمونه 6 cm واټن لري او 8 A او 2 A جریانونه په یوه لوري لېږدوي. د دوی ترمنځ په نیمایي کې د مقناطیسي ساحې اندازه څومره ده؟'),
 pair('GIVEN','معلوم','ورکړل شوي'),
 pair('Current due to wire 1: I₁ = 8 A; current due to wire 2: I₂ = 2 A.','تار 1 کی برقی رو: I₁ = 8 A؛ تار 2 کی برقی رو: I₂ = 2 A۔','د 1 سیم جریان: I₁ = 8 A؛ د 2 سیم جریان: I₂ = 2 A.'),
 pair('At midway between wires, r₁ = r₂ = 6 cm/2 = 0.03 m.','تاروں کے وسط میں r₁ = r₂ = 6 cm/2 = 0.03 m۔','د سیمونو په نیمایي کې r₁ = r₂ = 6 cm/2 = 0.03 m.'),
 pair('REQUIRED','مطلوب','اړین'),
 pair('Net magnetic field B_net = ?','خالص مقناطیسی میدان B_net = ؟','خالص مقناطیسي ساحه B_net = ؟'),
]

def make(identity,title,printed,pairs,layout,titles,refs,diagram=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':53,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(x) for x in refs]
 if diagram:s.update(diagram);s['content']+=diagram['diagramSvg']
 return r,s
def ampere10(lang):
 T={'en':('No current: needles point north','Current I: needles follow circular field','Amperian loop, radius r, test point P, element Δl'),'ur':('رو نہیں: سوئیاں شمال کی طرف','برقی رو I: سوئیاں دائرہ نما میدان کے ساتھ','ایمپیئر حلقہ، رداس r، نقطہ P، عنصر Δl'),'ps':('جریان نشته: ستنې شمال ته دي','جریان I: ستنې د دایروي ساحې لوری نیسي','د امپېر کړۍ، شعاع r، ټکی P، عنصر Δl')}[lang]
 b='<rect x="18" y="38" width="184" height="250" fill="#fff" stroke="#94a3b8"/><rect x="218" y="38" width="184" height="250" fill="#fff" stroke="#94a3b8"/><rect x="418" y="38" width="184" height="250" fill="#fff" stroke="#94a3b8"/>'
 for x in [110,310]:b+=f'<path d="M{x} 70V260" stroke="#7c2d12" stroke-width="8"/>'
 b+='<g fill="#fff" stroke="#334155" stroke-width="2"><circle cx="68" cy="105" r="16"/><circle cx="152" cy="105" r="16"/><circle cx="68" cy="205" r="16"/><circle cx="152" cy="205" r="16"/><circle cx="268" cy="105" r="16"/><circle cx="352" cy="105" r="16"/><circle cx="268" cy="205" r="16"/><circle cx="352" cy="205" r="16"/></g><path d="M68 93v24m84-24v24M68 193v24m84-24v24M268 105h20m84 0h-20m-84 100h-20m104 0h20" stroke="#dc2626" stroke-width="3"/>'
 b+='<circle cx="510" cy="165" r="66" fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="7 5"/><path d="M510 60V150M510 260V181" stroke="#7c2d12" stroke-width="7"/><circle cx="562" cy="165" r="5" fill="#dc2626"/><path d="M510 165H560M510 165V101" stroke="#16a34a" stroke-width="2"/><text x="540" y="155" font-size="13">P</text><text x="530" y="190" font-size="13">r</text><text x="515" y="94" font-size="12">Δl</text>'
 b+=f'<text x="24" y="24" font-size="12">(a) {T[0]}</text><text x="224" y="24" font-size="12">(b) {T[1]}</text><text x="424" y="24" font-size="12">(c) {T[2]}</text><text x="100" y="278">I = 0</text><text x="300" y="278">I</text>'
 return svg(b,'Figure 13.10: compasses near a wire and an Amperian circular path.')
def amperian_path(lang):
 L={'en':'Figure 13.11: current-carrying wire crossing a surface bounded by a closed Amperian path.','ur':'شکل 13.11: کرنٹ بردار تار سطح سے گزرتی ہے اور اس کی حد بند ایمپیئر راستہ ہے۔','ps':'13.11 شکل: جریان‌لرونکی سیم له سطحې تېرېږي او تړلې د امپېر لاره یې پوله جوړوي.'}[lang]
 b='<path d="M280 35V278" stroke="#7c2d12" stroke-width="9"/><path d="M280 60V35" stroke="#16a34a" stroke-width="3"/><path d="M272 48l8-14 8 14" fill="#16a34a"/><path d="M280 140C195 70 110 106 116 167C122 226 214 241 280 178C349 244 450 221 455 166C460 108 366 73 280 140Z" fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="8 5"/><path d="M363 102V125M350 116l13 12 13-12" stroke="#dc2626" stroke-width="2"/><text x="294" y="48" font-size="17">I</text><text x="372" y="108" font-size="14">Δl</text><text x="24" y="312" font-size="12">'+L+'</text>'
 return svg(b,L)

if __name__=='__main__':
 main_pairs=AMPERE[:16]
 layout=[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]},{'type':'heading','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'visual'},{'type':'heading','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'paragraph','indices':[11]},{'type':'equation','indices':[12]},{'type':'paragraph','indices':[13]},{'type':'equation','indices':[14]},{'type':'paragraph','indices':[15]}]
 r=make('phys13-ampere-law-long-wire-and-permeability96-97','Ampere’s circuital law, long-wire field and permeability',96,main_pairs,layout,('ایمپیئر کا دوری قانون، تار کا میدان اور نفوذ پذیری','د امپېر د کړۍ قانون، د سیم ساحه او نفوذپذیري'),[96,97],{'diagramSvg':ampere10('en'),'diagramSvgUrdu':ampere10('ur'),'diagramSvgPashto':ampere10('ps')})
 f11=make('phys13-amperian-path-figure1311-97','Figure 13.11 — Amperian path',97,[AMPERE[16]],[{'type':'paragraph','indices':[0]},{'type':'visual'}],('شکل 13.11 — ایمپیئر کا راستہ','13.11 شکل — د امپېر لاره'),[97],{'diagramSvg':amperian_path('en'),'diagramSvgUrdu':amperian_path('ur'),'diagramSvgPashto':amperian_path('ps')})
 ex_pairs=AMPERE[17:]
 ex_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'heading','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'heading','indices':[5]},{'type':'paragraph','indices':[6]}]
 ex=make('phys13-example132-setup97','Example 13.2 — magnetic field midway between two wires',97,ex_pairs,ex_layout,('مثال 13.2 — دو تاروں کے وسط میں مقناطیسی میدان','بېلګه 13.2 — د دوو سیمونو په نیمایي کې مقناطیسي ساحه'),[97])
 formulas=[
  {'id':'phys13-long-wire-field','name':'Magnetic field around a long straight wire','formula':AMPERE[1][0],'latex':'B = (μ₀/2π)(I/r)','sourceReferences':[ref(96)]},
  {'id':'phys13-ampere-law-13.4','name':'Ampere circuital law','number':'13.4','formula':AMPERE[14][0],'latex':'Σ B·Δl = μ₀I','sourceReferences':[ref(97)]},
 ]
 definitions=[
  {'term':'Permeability','definition':AMPERE[8][0],'definitionUrdu':AMPERE[8][1],'definitionPashto':AMPERE[8][2],'sourceReferences':[ref(97)]},
  {'term':'Relative permeability','definition':AMPERE[8][0]+' '+AMPERE[9][0]+' '+AMPERE[10][0],'definitionUrdu':AMPERE[8][1]+' '+AMPERE[9][1]+' '+AMPERE[10][1],'definitionPashto':AMPERE[8][2]+' '+AMPERE[9][2]+' '+AMPERE[10][2],'sourceReferences':[ref(97)]},
 ]
 with shared_class_data_lock():
  upsert([r[0],f11[0],ex[0]],[r[1],f11[1],ex[1]],chapter_index=2)
  sync_companions(chapter_index=2,trim_sections=[{'id':'13.3','startsAt':'SOLUTION\nThe net magnetic field is','title':'Example 13.2 solution — first unchecked text on printed page 98'}],formulas=formulas,definitions=definitions)
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==53:
  checkpoint(53,'corrected_verified',[r[0]['id'],f11[0]['id'],ex[0]['id']],'Rendered and inspected PDF page 53, printed pages 96–97. Compared the long-wire field proportionality and equations (1)–(2), Ampere biography text, vacuum/relative permeability definition and units, derivation through Eq. 13.4, Figures 13.10–13.11, and Example 13.2 statement/given/required. Rebuilt both field illustrations as translated inline SVG, synchronized formula and permeability cards, and trimmed the legacy OCR continuation at the unchecked worked solution on printed page 98.',printed_pages=[96,97],chapter_number=13)
