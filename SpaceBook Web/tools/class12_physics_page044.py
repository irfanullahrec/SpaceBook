"""Sequential source correction for PDF page 44 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def ref(page): return {'pdfPage':44,'printedPage':page,'sourcePdf':SOURCE}
def svg(body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 255" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:540px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

EX127=[
 pair('EXAMPLE 12.7','مثال 12.7','بېلګه 12.7'),
 pair('Figure shows three resistors and two voltage sources. Use Kirchhoff’s voltage law to find the emf ε_ab.',
  'شکل میں تین مزاحم اور دو وولٹیج ذرائع دکھائے گئے ہیں۔ محرکہ قوت ε_ab معلوم کرنے کے لیے کرخوف کا وولٹیج قانون استعمال کریں۔',
  'شکل درې مقاومتونه او دوه ولتاژ سرچینې ښيي. د ε_ab محرکې قوې د موندلو لپاره د کرخوف د ولتاژ قانون وکاروئ.'),
 pair('GIVEN','معلوم ہے','ورکړل شوي'),
 pair(r'\(\epsilon_1=24\text{ V},\;R_1=2\text{ k}\Omega,\;R_2=1\text{ k}\Omega,\;R_3=3\text{ k}\Omega\)',r'\(\epsilon_1=24\text{ V},\;R_1=2\text{ k}\Omega,\;R_2=1\text{ k}\Omega,\;R_3=3\text{ k}\Omega\)',r'\(\epsilon_1=24\text{ V},\;R_1=2\text{ k}\Omega,\;R_2=1\text{ k}\Omega,\;R_3=3\text{ k}\Omega\)'),
 pair('REQUIRED','مطلوب','غوښتل شوي'),
 pair(r'e.m.f. \(\epsilon_{ab}=?\)',r'برقی محرکہ قوت \(\epsilon_{ab}=?\)',r'محرکه قوه \(\epsilon_{ab}=?\)'),
 pair('SOLUTION','حل','حل'),
 pair(r'Total circuit resistance, \(R_T=2+1+3=6\text{ k}\Omega\)',r'سرکٹ کی کل مزاحمت، \(R_T=2+1+3=6\text{ k}\Omega\)',r'د مدار ټول مقاومت، \(R_T=2+1+3=6\text{ k}\Omega\)'),
 pair(r'Circuit current, \(I=\frac{\epsilon}{R_T}=\frac{24\text{ V}}{6\text{ k}\Omega}=4\text{ mA}\)',r'سرکٹ کی برقی رو، \(I=\frac{\epsilon}{R_T}=\frac{24\text{ V}}{6\text{ k}\Omega}=4\text{ mA}\)',r'د مدار جریان، \(I=\frac{\epsilon}{R_T}=\frac{24\text{ V}}{6\text{ k}\Omega}=4\text{ mA}\)'),
 pair('Applying Kirchhoff’s voltage law to loop ABCDA, we have','حلقے ABCDA پر کرخوف کا وولٹیج قانون لگانے سے ملتا ہے:','پر ABCDA کړۍ د کرخوف د ولتاژ قانون پلي کوو او ترلاسه کوو:'),
 pair(r'\(\epsilon_1-IR_1-\epsilon_{ab}=0\)',r'\(\epsilon_1-IR_1-\epsilon_{ab}=0\)',r'\(\epsilon_1-IR_1-\epsilon_{ab}=0\)'),
 pair(r'\(24-4\text{ mA}\times2\text{ k}\Omega-\epsilon_{ab}=0\)',r'\(24-4\text{ mA}\times2\text{ k}\Omega-\epsilon_{ab}=0\)',r'\(24-4\text{ mA}\times2\text{ k}\Omega-\epsilon_{ab}=0\)'),
 pair(r'\(24-8-\epsilon_{ab}=0\quad\Rightarrow\quad\epsilon_{ab}=24-8=16\text{ V}\)',r'\(24-8-\epsilon_{ab}=0\quad\Rightarrow\quad\epsilon_{ab}=24-8=16\text{ V}\)',r'\(24-8-\epsilon_{ab}=0\quad\Rightarrow\quad\epsilon_{ab}=24-8=16\text{ V}\)'),
]
ASSIGNMENT=[
 pair('ASSIGNMENT 12.3','اسائنمنٹ 12.3','دنده 12.3'),
 pair('Circuit ABCDEF is shown in Figure. Calculate the current in each branch of the circuit using Kirchhoff’s Voltage law.',
  'سرکٹ ABCDEF شکل میں دکھایا گیا ہے۔ کرخوف کے وولٹیج قانون سے سرکٹ کی ہر شاخ میں برقی رو معلوم کریں۔',
  'ABCDEF مدار په شکل کې ښودل شوی. د کرخوف د ولتاژ قانون په کارولو د مدار د هرې څانګې جریان محاسبه کړئ.'),
 pair('Answer (0.163A and 0.05454 A)','جواب (0.163A اور 0.05454 A)','ځواب (0.163A او 0.05454 A)'),
]
WHEATSTONE=[
 pair('12.14 WHEATSTONE BRIDGE','12.14 وہیٹ اسٹون برج','12.14 د وېټسټون پُل'),
 pair('This bridge was first proposed by Wheatstone an English telegraph engineer for measuring accurately the value of an unknown resistance.',
  'یہ برج پہلی بار انگریز ٹیلی گراف انجینئر وہیٹ اسٹون نے نامعلوم مزاحمت کی قدر درست طور پر ناپنے کے لیے پیش کیا۔',
  'دا پُل لومړی د انګلیسي ټیلیګراف انجنیر وېټسټون له خوا د نامعلوم مقاومت د ارزښت د کره اندازه کولو لپاره وړاندیز شو.'),
 pair('It consist of four resistors (two fixed resistances P and Q which are known, one variable resistance R which is also known and one unknown resistance X whose value is to be found) as shown in figure 12.15. Across one pair of opposite junctions (A and C) battery is connected and across the other opposite pair of junctions (B and D), a galvanometer is connected.',
  'یہ چار مزاحمتوں پر مشتمل ہوتا ہے (دو مستقل مزاحمتیں P اور Q جن کی قدریں معلوم ہیں، ایک متغیر مزاحمت R جس کی قدر بھی معلوم ہے، اور ایک نامعلوم مزاحمت X جس کی قدر معلوم کرنی ہے)، جیسا کہ شکل 12.15 میں دکھایا گیا ہے۔ بالمقابل جوڑوں میں سے ایک جوڑے (A اور C) کے درمیان بیٹری، اور دوسرے بالمقابل جوڑے (B اور D) کے درمیان گیلوانومیٹر منسلک ہوتا ہے۔',
  'دا له څلورو مقاومتونو جوړ دی (دوه ثابت مقاومتونه P او Q چې ارزښتونه یې معلوم دي، یو متغیر مقاومت R چې ارزښت یې هم معلوم دی، او یو نامعلوم مقاومت X چې ارزښت یې موندل کېږي)، لکه په 12.15 شکل کې. د مقابل پیوندونو د یوې جوړې (A او C) ترمنځ بیټرۍ او د بلې جوړې (B او D) ترمنځ ګالوانومیټر نښلول کېږي.'),
 pair('The value of P and Q are properly fixed. When the key is switched on, the current I divide unequally between the two branches and the galvanometer shows current.',
  'P اور Q کی قدریں مناسب طور پر مقرر ہوتی ہیں۔ جب کلید آن کی جاتی ہے تو برقی رو I دونوں شاخوں میں غیر مساوی طور پر تقسیم ہوتی ہے اور گیلوانومیٹر برقی رو دکھاتا ہے۔',
  'د P او Q ارزښتونه سم ټاکل شوي وي. کله چې کیلي بنده شي، I جریان د دوو څانګو ترمنځ په نابرابره توګه وېشل کېږي او ګالوانومیټر جریان ښيي.'),
 pair('The value of resistance R is varied until the galvanometer shows zero current. Under such conditions, the bridge is said to be balance. The point at which the bridge is balanced is called null point.',
  'مزاحمت R کی قدر اس وقت تک بدلی جاتی ہے جب تک گیلوانومیٹر صفر برقی رو نہ دکھائے۔ ایسی حالت میں برج کو متوازن کہا جاتا ہے۔ جس نقطے پر برج متوازن ہو اسے صفر نقطہ کہتے ہیں۔',
  'د R مقاومت ارزښت تر هغه بدلېږي چې ګالوانومیټر صفر جریان وښيي. په داسې حالت کې پُل متوازن بلل کېږي. هغه ټکی چې پُل پکې متوازن وي د صفر ټکی بلل کېږي.'),
 pair('Let I₁ and I₂ be the currents through P and R respectively when the bridge is balanced.',
  'فرض کریں کہ برج متوازن ہونے پر I₁ اور I₂ بالترتیب P اور R سے گزرنے والی برقی روئیں ہیں۔',
  'فرض کړئ چې د پُل د توازن پر مهال I₁ او I₂ په ترتیب سره له P او R څخه تېرېدونکي جریانونه دي.'),
 pair('Since there is no current through Galvanometer, the current in Q and X are also I₁ and I₂ respectively. As the Galvanometer reads zero, points B and D are at the same potential. This means that voltage drops from A to B and A to D must be equal.',
  'چونکہ گیلوانومیٹر میں کوئی برقی رو نہیں بہتی، اس لیے Q اور X میں برقی روئیں بھی بالترتیب I₁ اور I₂ ہیں۔ گیلوانومیٹر صفر دکھاتا ہے، اس لیے نقاط B اور D ایک ہی پوٹینشل پر ہیں۔ اس کا مطلب ہے کہ A سے B اور A سے D تک وولٹیج ڈراپس برابر ہوں گے۔',
  'ځکه چې له ګالوانومیټر څخه جریان نه تېرېږي، په Q او X کې جریانونه هم په ترتیب سره I₁ او I₂ دي. ګالوانومیټر چې صفر ښيي، د B او D نقطې په یوه پوتنشیال دي. دا مانا لري چې له A څخه B او له A څخه D ته د ولتاژ لوېدنې باید برابرې وي.'),
 pair('Also voltage drops from B to C and D to C must be equal. Hence for balanced bridge the potential drop across AB = the potential drop across AD',
  'اسی طرح B سے C اور D سے C تک وولٹیج ڈراپس بھی برابر ہوں گے۔ لہٰذا متوازن برج کے لیے AB کے پار پوٹینشل ڈراپ = AD کے پار پوٹینشل ڈراپ۔',
  'همدارنګه له B څخه C او له D څخه C ته د ولتاژ لوېدنې باید برابرې وي. نو د متوازن پُل لپاره د AB په اوږدو کې پوتنشیالي لوېدنه = د AD په اوږدو کې پوتنشیالي لوېدنه.'),
 pair(r'\(I_1P=I_2R\) (i)',r'\(I_1P=I_2R\) (i)',r'\(I_1P=I_2R\) (i)'),
 pair('Similarly, the potential drop across BC = the potential drop across DC and', 'اسی طرح BC کے پار پوٹینشل ڈراپ = DC کے پار پوٹینشل ڈراپ اور','همدارنګه د BC په اوږدو کې پوتنشیالي لوېدنه = د DC په اوږدو کې پوتنشیالي لوېدنه، او'),
 pair(r'\(I_1Q=I_2X\) (ii)',r'\(I_1Q=I_2X\) (ii)',r'\(I_1Q=I_2X\) (ii)'),
 pair('Dividing Eq. (i) by Eq. (ii), we get','مساوات (i) کو مساوات (ii) پر تقسیم کرنے سے ملتا ہے:','د (i) معادله پر (ii) معادلې په وېشلو ترلاسه کوو:'),
 pair(r'\(\frac{P}{Q}=\frac{R}{X}\)',r'\(\frac{P}{Q}=\frac{R}{X}\)',r'\(\frac{P}{Q}=\frac{R}{X}\)'),
]

def make(identity,title,printed,pairs,layout,titles,pages):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':44,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(n) for n in pages]
 return r,s
def example_svg(lang):
 L={'en':('Complex circuit solution through Kirchhoff’s rule','FIGURE — Example 12.7'),'ur':('کرخوف کے قاعدے سے پیچیدہ سرکٹ کا حل','شکل — مثال 12.7'),'ps':('د کرخوف د قاعدې له مخې د پېچلي مدار حل','د 12.7 بېلګې شکل')}[lang]
 b=('<path d="M70 62H460V190H70V62" fill="none" stroke="#334155" stroke-width="3"/><path d="M70 102V142M58 102H82M62 94H78" stroke="#2563eb" stroke-width="3"/><text x="30" y="128" font-size="14">24V</text><path d="M115 62l10-12 16 24 16-24 16 24 16-12" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="138" y="40" font-size="14">R₁ = 2 kΩ</text><path d="M260 62l10-12 16 24 16-24 16 24 16-12" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="281" y="40" font-size="14">R₂ = 1 kΩ</text><path d="M460 85l-10 12 20 16-20 16 20 16-10 12" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="468" y="126" font-size="13">R₃ = 3 kΩ</text><path d="M260 62V190" stroke="#2563eb" stroke-width="2" stroke-dasharray="5 4"/><text x="265" y="95" font-size="13">+ a</text><text x="265" y="176" font-size="13">− b</text><text x="54" y="56" font-size="14">A</text><text x="245" y="55" font-size="14">B</text><text x="465" y="208" font-size="14">C</text><text x="54" y="208" font-size="14">D</text><text x="180" y="226" font-size="13">'+L[0]+'</text><text x="20" y="22" font-size="12">'+L[1]+'</text>')
 return svg(b,L[1])
def assignment_svg(lang):
 L={'en':('Assignment 12.3 circuit','4 V source'),'ur':('اسائنمنٹ 12.3 کا سرکٹ','4 V منبع'),'ps':('د 12.3 دندې مدار','4 V سرچینه')}[lang]
 b=('<path d="M80 48H455V195H80V48" fill="none" stroke="#334155" stroke-width="3"/><path d="M80 87V151M68 87H92M72 79H88" stroke="#2563eb" stroke-width="3"/><text x="30" y="126" font-size="14">4 V</text><path d="M128 48l9-12 14 24 14-24 14 24 14-12" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="150" y="27" font-size="13">5 Ω</text><path d="M285 48l9-12 14 24 14-24 14 24 14-12" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="309" y="27" font-size="13">10 Ω</text><path d="M267 48V195" stroke="#334155" stroke-width="3"/><path d="M255 93l12-9 12 9M255 145l12 9 12-9" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="275" y="126" font-size="13">20 Ω</text><path d="M455 72l-10 10 20 12-20 12 20 12-10 10" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="467" y="111" font-size="13">30 Ω</text><path d="M150 38H235" stroke="#16a34a" stroke-width="2"/><path d="M225 32l12 6-12 6" fill="#16a34a"/><text x="184" y="31" font-size="13">I₁</text><path d="M325 38H425" stroke="#2563eb" stroke-width="2"/><path d="M415 32l12 6-12 6" fill="#2563eb"/><text x="366" y="31" font-size="13">I₂</text><path d="M400 204H310M250 204H155" stroke="#64748b" stroke-width="2"/><path d="M316 198l-12 6 12 6M161 198l-12 6 12 6" fill="#64748b"/><text x="72" y="42" font-size="13">A</text><text x="260" y="42" font-size="13">B</text><text x="454" y="42" font-size="13">C</text><text x="454" y="214" font-size="13">D</text><text x="258" y="214" font-size="13">E</text><text x="72" y="214" font-size="13">F</text><text x="20" y="238" font-size="12">'+L[0]+' — '+L[1]+'</text>')
 return svg(b,L[0])
def wheatstone_svg(lang):
 L={'en':('Wheatstone bridge','galvanometer','battery','key K','FIGURE 12.15'),'ur':('وہیٹ اسٹون برج','گیلوانومیٹر','بیٹری','کلید K','شکل 12.15'),'ps':('وېټسټون پُل','ګالوانومیټر','بیټرۍ','کیلي K','12.15 شکل')}[lang]
 b=('<path d="M270 35L390 122L270 205L150 122Z" fill="none" stroke="#334155" stroke-width="4"/><circle cx="270" cy="35" r="6"/><circle cx="390" cy="122" r="6"/><circle cx="270" cy="205" r="6"/><circle cx="150" cy="122" r="6"/><path d="M205 73l12-10 15 20 15-20 15 20 12-10" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="214" y="67" font-size="15">P</text><path d="M294 73l12-10 15 20 15-20 15 20 12-10" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="330" y="67" font-size="15">Q</text><path d="M205 170l12-10 15 20 15-20 15 20 12-10" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="214" y="198" font-size="15">R</text><path d="M294 170l12-10 15 20 15-20 15 20 12-10" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="330" y="198" font-size="15">X</text><path d="M270 41V91M270 149V199" stroke="#334155" stroke-width="3"/><circle cx="270" cy="120" r="29" fill="#fff" stroke="#2563eb" stroke-width="3"/><text x="261" y="127" font-size="20">G</text><path d="M150 122V225H205M335 225H390V122" fill="none" stroke="#334155" stroke-width="3"/><path d="M252 215V235M268 215V235" stroke="#2563eb" stroke-width="3"/><path d="M335 225H365M368 219V231" stroke="#334155" stroke-width="3"/><text x="136" y="117" font-size="15">A</text><text x="265" y="25" font-size="15">B</text><text x="395" y="117" font-size="15">C</text><text x="265" y="226" font-size="15">D</text><text x="20" y="25" font-size="13">'+L[4]+'</text><text x="302" y="124" font-size="12">'+L[1]+'</text><text x="20" y="240" font-size="12">'+L[2]+' / '+L[3]+'</text>')
 return svg(b,L[4])

if __name__=='__main__':
 e=make('phys12-unit12-example12778','Example 12.7 — emf in a three-resistor circuit',78,EX127,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},{'type':'heading','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'heading','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'heading','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]},{'type':'equation','indices':[11]},{'type':'equation','indices':[12]}],('مثال 12.7 — تین مزاحموں کے سرکٹ میں محرکہ قوت','بېلګه 12.7 — په درې مقاومتونو مدار کې محرکه قوه'),[78],)
 e[1]['diagramSvg']=example_svg('en');e[1]['diagramSvgUrdu']=example_svg('ur');e[1]['diagramSvgPashto']=example_svg('ps');e[1]['content']+=e[1]['diagramSvg']
 a=make('phys12-unit12-assignment12378','Assignment 12.3 — branch currents',78,ASSIGNMENT,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},{'type':'paragraph','indices':[2]}],('اسائنمنٹ 12.3 — شاخوں کی برقی روئیں','دنده 12.3 — د څانګو جریانونه'),[78])
 a[1]['diagramSvg']=assignment_svg('en');a[1]['diagramSvgUrdu']=assignment_svg('ur');a[1]['diagramSvgPashto']=assignment_svg('ps');a[1]['content']+=a[1]['diagramSvg']
 w_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'visual'},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]},{'type':'paragraph','indices':[11]},{'type':'equation','indices':[12]}]
 w=make('phys12-unit12-wheatstone-bridge79','12.14 Wheatstone bridge and balance condition',79,WHEATSTONE,w_layout,('12.14 وہیٹ اسٹون برج اور توازن کی شرط','12.14 وېټسټون پُل او د توازن شرط'),[79])
 w[1]['diagramSvg']=wheatstone_svg('en');w[1]['diagramSvgUrdu']=wheatstone_svg('ur');w[1]['diagramSvgPashto']=wheatstone_svg('ps');w[1]['content']+=w[1]['diagramSvg']
 records=[e[0],a[0],w[0]];sections=[e[1],a[1],w[1]]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,retire_sections=['12.9'],
  trim_sections=[{'id':'12.10','startsAt':'NOT FOR SALE\n80','title':'Continuation from printed page 80 — pending source review'}],
  formulas=[{'id':'phys12-unit12-wheatstone-balance','name':'Wheatstone bridge balance condition','formula':WHEATSTONE[12][0],'latex':'P/Q=R/X','sourceReferences':[ref(79)]}],
  definitions=[{'term':'Wheatstone bridge','definition':WHEATSTONE[1][0]+' '+WHEATSTONE[2][0]+' '+WHEATSTONE[3][0]+' '+WHEATSTONE[4][0]+' '+WHEATSTONE[5][0],
   'definitionUrdu':WHEATSTONE[1][1]+' '+WHEATSTONE[2][1]+' '+WHEATSTONE[3][1]+' '+WHEATSTONE[4][1]+' '+WHEATSTONE[5][1],
   'definitionPashto':WHEATSTONE[1][2]+' '+WHEATSTONE[2][2]+' '+WHEATSTONE[3][2]+' '+WHEATSTONE[4][2]+' '+WHEATSTONE[5][2], 'sourceReferences':[ref(79)]}],
  worked_examples=[{'id':'textbook-example-12-7','num':'12.7','title':'Example 12.7','problem':EX127[1][0],'problemUrdu':EX127[1][1],'problemPashto':EX127[1][2],
   'given':[EX127[3][0]],'givenUrdu':[EX127[3][1]],'givenPashto':[EX127[3][2]],'required':[EX127[5][0]],'requiredUrdu':[EX127[5][1]],'requiredPashto':[EX127[5][2]],
   'steps':[EX127[i][0] for i in range(7,13)],'stepsUrdu':[EX127[i][1] for i in range(7,13)],'stepsPashto':[EX127[i][2] for i in range(7,13)],
   'answer':r'\epsilon_{ab}=16\text{ V}','solutionOrigin':'textbook','sourceReferences':[ref(78)]}],
  exercises=[{'id':'assignment-12-3','title':'Assignment 12.3','problems':[{'id':'assignment-12-3-q1','question':ASSIGNMENT[1][0],
    'questionUrdu':ASSIGNMENT[1][1],'questionPashto':ASSIGNMENT[1][2],'answer':'0.163A and 0.05454 A','solutionOrigin':'textbook answer','sourceReferences':[ref(78)]}]}])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==44:
  checkpoint(44,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 44, printed pages 78–79. Compared Example 12.7 data, requested emf, every substitution and answer; Assignment 12.3 wording and printed answer; Wheatstone bridge description, balance/null-point conditions, galvanometer/current relationships, equations (i)–(ii), ratio and Figure 12.15. Rebuilt both circuit examples and the bridge as translated SVG, synchronized the worked example, exercise, bridge formula and definition, retired the covered legacy Example 12.7 and trimmed old text at the unchecked printed page 80.',printed_pages=[78,79],chapter_number=12)
