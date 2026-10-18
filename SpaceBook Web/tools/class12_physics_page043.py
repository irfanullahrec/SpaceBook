"""Sequential source correction for PDF page 43 of Class 12 Physics."""
from class12_source_review import upsert, section, checkpoint, sync_companions
from html import escape
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def svg(body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 245" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:540px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

KCL=[
 pair('If we take the signs of currents flowing towards a point O as positive, then currents flowing away from point O will be assigned negative sign. Thus applying Kirchhoff’s current law to the junction',
  'اگر نقطہ O کی طرف آنے والی برقی روؤں کی علامت مثبت لیں تو نقطہ O سے دور جانے والی برقی روؤں کی علامت منفی ہو گی۔ یوں جوڑ پر کرخوف کا برقی رو کا قانون لگانے سے',
  'که د O نقطې پر لور د بهېدونکو جریانونو نښې مثبتې ونیسو، له O څخه د لرې بهېدونکو جریانونو نښې منفي ټاکل کېږي. نو پر پیوند د کرخوف د جریان قانون په پلي کولو'),
 pair(r'\((I_1)+(I_4)+(-I_2)+(-I_3)=0\)',r'\((I_1)+(I_4)+(-I_2)+(-I_3)=0\)',r'\((I_1)+(I_4)+(-I_2)+(-I_3)=0\)'),
 pair('Or','یا','یا'),
 pair(r'\(I_1+I_4=I_2+I_3\) ...(12.17)',r'\(I_1+I_4=I_2+I_3\) ...(12.17)',r'\(I_1+I_4=I_2+I_3\) ...(12.17)'),
 pair('i.e. sum of incoming currents = sum of outgoing current.', 'یعنی آنے والی برقی روؤں کا مجموعہ = جانے والی برقی روؤں کا مجموعہ۔','یعنې د راتلونکو جریانونو مجموعه = د وتونکو جریانونو مجموعه.'),
 pair('Hence, Kirchhoff’s current law may also be stated as the algebraic sum of currents flowing towards the junction in an electrical circuit is equal to the algebraic sum of currents flowing away from that junction.',
  'لہٰذا کرخوف کے برقی رو کے قانون کو یوں بھی بیان کیا جا سکتا ہے: برقی سرکٹ میں جوڑ کی طرف آنے والی برقی روؤں کا الجبری مجموعہ اس جوڑ سے دور جانے والی برقی روؤں کے الجبری مجموعے کے برابر ہے۔',
  'نو د کرخوف د جریان قانون داسې هم بیانېدای شي: په برېښنايي مدار کې د پیوند پر لور د جریانونو جبري مجموعه له پیوند څخه د لرې بهېدونکو جریانونو له جبري مجموعې سره برابره ده.'),
]
KVL=[
 pair('KIRCHOFF’S VOLTAGE LAW (KVL)','کرخوف کا وولٹیج کا قانون (KVL)','د کرخوف د ولتاژ قانون (KVL)'),
 pair('This law refers to e.m.f and voltage drops in a closed circuit or closed loop and may be stated as under:',
  'یہ قانون بند سرکٹ یا بند حلقے میں برقی محرکہ قوت اور وولٹیج ڈراپس سے متعلق ہے اور یوں بیان کیا جا سکتا ہے:',
  'دا قانون په تړلي مدار یا کړۍ کې له محرکې قوې او ولتاژ لوېدنو سره تړاو لري او داسې بیانېدای شي:'),
 pair('In any closed electrical circuit, the algebraic sum of all the electromotive force (e.m.f) and voltage drops in resistor is equal to zero i.e.',
  'کسی بھی بند برقی سرکٹ میں تمام برقی محرکہ قوتوں (e.m.f) اور مزاحم میں وولٹیج ڈراپس کا الجبری مجموعہ صفر ہوتا ہے، یعنی',
  'په هر تړلي برېښنايي مدار کې د ټولو محرکو قوو (e.m.f) او په مقاومت کې د ولتاژ لوېدنو جبري مجموعه صفر ده، یعنې'),
 pair('Algebraic sum of emf + algebraic sum of voltage drops = 0.', 'برقی محرکہ قوتوں کا الجبری مجموعہ + وولٹیج ڈراپس کا الجبری مجموعہ = 0۔','د محرکو قوو جبري مجموعه + د ولتاژ لوېدنو جبري مجموعه = 0.'),
 pair('The validity of Kirchhoff’s voltage law can be easily established by referring to the closed loop ABCDA shown in Figure 12.14. Starting from any point (say point A) in this closed circuit after going around the circuit and go back to this point (i.e. point A). The following convention is adopted to solve the circuit.',
  'شکل 12.14 کے بند حلقے ABCDA سے کرخوف کے وولٹیج قانون کی صحت آسانی سے قائم کی جا سکتی ہے۔ بند سرکٹ کے کسی بھی نقطے (مثلاً A) سے شروع کریں، سرکٹ کے گرد چکر لگانے کے بعد اسی نقطے (یعنی A) پر واپس آئیں۔ سرکٹ حل کرنے کے لیے درج ذیل قاعدہ اپنایا جاتا ہے۔',
  'د 12.14 شکل د ABCDA تړلې کړۍ ته په کتو د کرخوف د ولتاژ قانون اعتبار په اسانۍ څرګندېږي. په تړلي مدار کې له هرې نقطې (لکه A) پیل وکړئ، د مدار له شاوخوا تېر شئ او بېرته همدې نقطې (یعنې A) ته راشئ. د مدار د حل لپاره لاندې دود کارول کېږي.'),
 pair('i) A rise in potential is taken positive.', 'i) پوٹینشل میں اضافے کو مثبت لیا جاتا ہے۔','i) د پوتنشیال زیاتوالی مثبت نیول کېږي.'),
 pair('ii) A drop in potential is taken negative.', 'ii) پوٹینشل میں کمی کو منفی لیا جاتا ہے۔','ii) د پوتنشیال کمښت منفي نیول کېږي.'),
 pair('iii) For batteries, the positive end is always at higher potential.', 'iii) بیٹریوں میں مثبت سرا ہمیشہ بلند پوٹینشل پر ہوتا ہے۔','iii) په بیټریو کې مثبت پای تل په لوړ پوتنشیال وي.'),
 pair('iv) Current flows from high potential to the low potential.', 'iv) برقی رو بلند پوٹینشل سے کم پوٹینشل کی طرف بہتی ہے۔','iv) جریان له لوړ پوتنشیال څخه ټیټ پوتنشیال ته بهېږي.'),
 pair('v) Assume the direction of current either clock wise or counter clockwise.', 'v) برقی رو کی سمت گھڑی کی سمت یا گھڑی کی مخالف سمت فرض کریں۔','v) د جریان لوری د ساعت‌ګرځېدو یا د هغې د مخالف لوري په توګه فرض کړئ.'),
]
PROCEDURE=[
 pair('PROCEDURES OF APPLYING KIRCHHOFF’S LAWS FOR PROBLEM SOLUTION','مسئلے کے حل کے لیے کرخوف کے قوانین لگانے کے طریقے','د مسئلې د حل لپاره د کرخوف د قوانینو د پلي کولو کړنلارې'),
 pair('Moving along the direction of current flow through R₁, the fall in potential is −IR₁.', 'R₁ میں برقی رو کی سمت چلنے پر پوٹینشل میں کمی −IR₁ ہے۔','د R₁ له لارې د جریان د لوري په اوږدو کې د پوتنشیال کمښت −IR₁ دی.'),
 pair('Moving along the direction of current flow through R₂, the fall in potential is −IR₂.', 'R₂ میں برقی رو کی سمت چلنے پر پوٹینشل میں کمی −IR₂ ہے۔','د R₂ له لارې د جریان د لوري په اوږدو کې د پوتنشیال کمښت −IR₂ دی.'),
 pair('Moving from the negative terminal to the positive terminal, for rise in potential +ε₁.', 'منفی ٹرمینل سے مثبت ٹرمینل کی طرف جانے پر پوٹینشل میں اضافہ +ε₁ ہے۔','له منفي ترمینل څخه مثبت ترمینل ته د تګ پر مهال د پوتنشیال زیاتوالی +ε₁ دی.'),
 pair('Moving from the positive terminal to the negative terminal, for fall in potential −ε₂.', 'مثبت ٹرمینل سے منفی ٹرمینل کی طرف جانے پر پوٹینشل میں کمی −ε₂ ہے۔','له مثبت ترمینل څخه منفي ترمینل ته د تګ پر مهال د پوتنشیال کمښت −ε₂ دی.'),
 pair('Thus applying Kirchhoff’s law on Figure 12.14 we get','چنانچہ شکل 12.14 پر کرخوف کا قانون لگانے سے ملتا ہے:','نو پر 12.14 شکل د کرخوف قانون پلي کوو او ترلاسه کوو:'),
 pair(r'\(\epsilon_1-IR_1-\epsilon_2-IR_2=0\)',r'\(\epsilon_1-IR_1-\epsilon_2-IR_2=0\)',r'\(\epsilon_1-IR_1-\epsilon_2-IR_2=0\)'),
 pair(r'\(\Rightarrow\epsilon_1-\epsilon_2=IR_1+IR_2\)',r'\(\Rightarrow\epsilon_1-\epsilon_2=IR_1+IR_2\)',r'\(\Rightarrow\epsilon_1-\epsilon_2=IR_1+IR_2\)'),
 pair(r'\(\Rightarrow\epsilon_1-\epsilon_2=IR_1+IR_2\quad\text{or}\quad\sum\epsilon=\sum IR\) ...(12.18)',r'\(\Rightarrow\epsilon_1-\epsilon_2=IR_1+IR_2\quad\text{or}\quad\sum\epsilon=\sum IR\) ...(12.18)',r'\(\Rightarrow\epsilon_1-\epsilon_2=IR_1+IR_2\quad\text{or}\quad\sum\epsilon=\sum IR\) ...(12.18)'),
 pair('The sum of all the emf ε in a loop in a circuit is equal to the sum of all the IR voltage drops in that loop. KVL is in fact, a statement of the law of conservation of energy.',
  'سرکٹ کے حلقے میں تمام برقی محرکہ قوت ε کا مجموعہ اس حلقے میں IR وولٹیج ڈراپس کے مجموعے کے برابر ہوتا ہے۔ درحقیقت KVL توانائی کے بقائے کے قانون کا بیان ہے۔',
  'په مدار کې د یوې کړۍ د ټولو ε محرکو قوو مجموعه په هماغه کړۍ کې د ټولو IR ولتاژ لوېدنو له مجموعې سره برابره ده. KVL په حقیقت کې د انرژۍ د پایښت قانون بیانوي.'),
 pair('Tips','نکات','لارښوونې'),
 pair('1. The choice of loops is quite arbitrary, but it should be such that each resistance is included at least once in the selected loop. Kirchhoff’s voltage law can be applied to these closed loops to get the desired equations.',
  '1. حلقوں کا انتخاب کافی حد تک اختیاری ہے، لیکن منتخب حلقوں میں ہر مزاحمت کم از کم ایک بار شامل ہونی چاہیے۔ مطلوبہ مساواتیں حاصل کرنے کے لیے ان بند حلقوں پر کرخوف کا وولٹیج قانون لگایا جا سکتا ہے۔',
  '1. د کړیو ټاکنه تر ډېره اختیاري ده، خو په ټاکل شوې کړۍ کې باید هر مقاومت لږ تر لږه یو ځل شامل وي. د مطلوبو معادلو د ترلاسه کولو لپاره پر دغو تړلو کړیو د کرخوف د ولتاژ قانون پلي کېدای شي.'),
 pair('2. The direction in which currents are assumed to flow is not important, since if wrong direction is chosen, it will be indicated by a negative sign in the result.',
  '2. فرض کی گئی برقی رو کی سمت اہم نہیں، کیونکہ غلط سمت منتخب ہونے کی صورت میں نتیجے میں منفی علامت ظاہر ہو گی۔',
  '2. د جریانونو د تېرېدو فرض شوی لوری مهم نه دی؛ که ناسم لوری وټاکل شي، په پایله کې به منفي نښه ښکاره شي.'),
]

def make(identity,title,printed,pairs,layout,titles,pages,visual=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':43,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[{'pdfPage':43,'printedPage':n,'sourcePdf':SOURCE} for n in pages]
 if visual:s.update(visual);s['content']+=visual['diagramSvg']
 return r,s
def loop_svg(lang):
 L={'en':('Single loop circuit','FIGURE 12.14'),'ur':('واحد حلقی سرکٹ','شکل 12.14'),'ps':('یوه کړۍ مدار','12.14 شکل')}[lang]
 b=('<path d="M100 50H420V190H100V50" fill="none" stroke="#334155" stroke-width="3"/><text x="82" y="48" font-size="15">B</text><text x="425" y="48" font-size="15">A</text><text x="82" y="208" font-size="15">C</text><text x="425" y="208" font-size="15">D</text><path d="M175 50l10-11 13 22 13-22 13 22 13-11" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="198" y="30" font-size="13">R₁</text><path d="M235 190l10-11 13 22 13-22 13 22 13-11" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="256" y="222" font-size="13">R₂</text><path d="M100 92V133M88 92H112M92 84H108" stroke="#2563eb" stroke-width="3"/><text x="68" y="88" font-size="13">ε₂</text><path d="M420 80V123M408 80H432M412 72H428" stroke="#dc2626" stroke-width="3"/><text x="435" y="78" font-size="13">ε₁</text><path d="M145 68H300" stroke="#16a34a" stroke-width="2"/><path d="M290 62l12 6-12 6" fill="#16a34a"/><text x="305" y="64" font-size="13">I</text>')
 b+=f'<text x="325" y="25" font-size="13">{escape(L[1])}</text><text x="188" y="237" font-size="13">{escape(L[0])}</text>'
 return svg(b,L[1])
def procedure_svg(lang):
 L={'en':('Voltage change while traversing a circuit','Resistor drop','Battery rise','Battery fall'),'ur':('سرکٹ کے گرد چلنے پر وولٹیج کی تبدیلی','مزاحم میں کمی','بیٹری میں اضافہ','بیٹری میں کمی'),'ps':('د مدار په شاوخوا کې د تګ پر مهال د ولتاژ بدلون','په مقاومت کې لوېدنه','په بیټرۍ کې زیاتوالی','په بیټرۍ کې کمښت')}[lang]
 b=('<rect x="15" y="35" width="245" height="75" rx="8" fill="#fff7ed" stroke="#c2410c" stroke-width="2"/><path d="M35 70H80l9-10 14 20 14-20 14 20 14-10H235" fill="none" stroke="#334155" stroke-width="3"/><path d="M155 52H210" stroke="#2563eb" stroke-width="2"/><path d="M202 46l12 6-12 6" fill="#2563eb"/><text x="25" y="31" font-size="12">R₁ / R₂</text><rect x="280" y="35" width="245" height="75" rx="8" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/><path d="M300 70H350M380 70H500" stroke="#334155" stroke-width="3"/><path d="M350 54V86M365 60V80" stroke="#2563eb" stroke-width="3"/><path d="M410 52H480" stroke="#16a34a" stroke-width="2"/><path d="M472 46l12 6-12 6" fill="#16a34a"/><text x="310" y="32" font-size="12">ε₁ / ε₂</text>')
 b+=f'<text x="16" y="134" font-size="12">{escape(L[0])}</text><text x="20" y="158" font-size="12">{escape(L[1])}</text><text x="300" y="158" font-size="12">{escape(L[2])} / {escape(L[3])}</text>'
 return svg(b,L[0])

if __name__=='__main__':
 c=make('phys12-unit12-kcl-continuation76','Kirchhoff’s current law — sign convention',76,KCL,[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]}],('کرخوف کا برقی رو کا قانون — علامتی قاعدہ','د کرخوف د جریان قانون — د نښو دود'),[76])
 v=make('phys12-unit12-kvl-intro76','Kirchhoff’s voltage law and loop conventions',76,KVL,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'visual'},{'type':'list','indices':[5,6,7,8,9]}],('کرخوف کا وولٹیج قانون اور حلقے کے قواعد','د کرخوف د ولتاژ قانون او د کړۍ دودونه'),[76],{'diagramSvg':loop_svg('en'),'diagramSvgUrdu':loop_svg('ur'),'diagramSvgPashto':loop_svg('ps')})
 q_layout=[{'type':'heading','indices':[0]},{'type':'list','indices':[1,2,3,4]},{'type':'visual'},{'type':'paragraph','indices':[5]},{'type':'equation','indices':[6]},{'type':'equation','indices':[7]},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'heading','indices':[10]},{'type':'list','indices':[11,12]}]
 q=make('phys12-unit12-kvl-procedure77','Applying Kirchhoff’s laws — potential changes and tips',77,PROCEDURE,q_layout,('کرخوف کے قوانین کا اطلاق — پوٹینشل تبدیلیاں اور نکات','د کرخوف قوانینو پلي کول — د پوتنشیال بدلونونه او لارښوونې'),[77],{'diagramSvg':procedure_svg('en'),'diagramSvgUrdu':procedure_svg('ur'),'diagramSvgPashto':procedure_svg('ps')})
 records=[c[0],v[0],q[0]];sections=[c[1],v[1],q[1]]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,trim_sections=[{'id':'12.9','startsAt':'EXAMPLE 12.7','title':'Example 12.7 — pending source review'}],
  formulas=[{'id':'phys12-unit12-eq-12.17','name':'Kirchhoff’s current law at a junction','number':'12.17','formula':KCL[3][0],'latex':'I_1+I_4=I_2+I_3','sourceReferences':[{'pdfPage':43,'printedPage':76,'sourcePdf':SOURCE}]},
   {'id':'phys12-unit12-eq-12.18','name':'Kirchhoff’s voltage law around a loop','number':'12.18','formula':PROCEDURE[8][0],'latex':r'\sum\epsilon=\sum IR','sourceReferences':[{'pdfPage':43,'printedPage':77,'sourcePdf':SOURCE}]}],
  definitions=[{'term':'Kirchhoff’s current law','definition':KCL[4][0]+' '+KCL[5][0], 'definitionUrdu':KCL[4][1]+' '+KCL[5][1], 'definitionPashto':KCL[4][2]+' '+KCL[5][2], 'sourceReferences':[{'pdfPage':43,'printedPage':76,'sourcePdf':SOURCE}]},
   {'term':'Kirchhoff’s voltage law','definition':KVL[1][0]+' '+KVL[2][0]+' '+KVL[3][0], 'definitionUrdu':KVL[1][1]+' '+KVL[2][1]+' '+KVL[3][1], 'definitionPashto':KVL[1][2]+' '+KVL[2][2]+' '+KVL[3][2], 'sourceReferences':[{'pdfPage':43,'printedPage':76,'sourcePdf':SOURCE}]}])
 checkpoint(43,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 43, printed pages 76–77. Compared KCL sign convention, source algebraic equation and Eq. 12.17, incoming/outgoing-current explanations, KVL statement and five sign conventions, Figure 12.14, all four potential-rise/drop procedure panels, derivation through Eq. 12.18, conservation-of-energy text and both Tips. Rebuilt the loop and procedure schematics as translated SVG, synchronized formula cards and law definitions, and trimmed the covered legacy Kirchhoff prefix at the unchecked Example 12.7.',printed_pages=[76,77],chapter_number=12)
