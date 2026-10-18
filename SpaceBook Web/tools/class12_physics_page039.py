"""Sequential source correction for PDF page 39 of Class 12 Physics."""
from html import escape
import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def svg(body,label):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:520px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

INTERNAL=[
 pair(r'\(I=\frac{\epsilon}{R+r}\Rightarrow IR=\epsilon-Ir\)',r'\(I=\frac{\epsilon}{R+r}\Rightarrow IR=\epsilon-Ir\)',r'\(I=\frac{\epsilon}{R+r}\Rightarrow IR=\epsilon-Ir\)'),
 pair('But IR=V, the terminal voltage of the cell', 'لیکن IR=V، سیل کا ٹرمینل وولٹیج ہے۔','خو IR=V د حجرې ترمینلي ولتاژ دی.'),
 pair(r'\(V=\epsilon-Ir\)',r'\(V=\epsilon-Ir\)',r'\(V=\epsilon-Ir\)'),
 pair(r'Now, if \(r=0\) (OpenCircuit); \(I=0\) then \(V=\epsilon\)',r'اب، اگر \(r=0\) (اوپن سرکٹ) ہو؛ \(I=0\)، تو \(V=\epsilon\)',r'اوس، که \(r=0\) (پرانیستی مدار) وي؛ \(I=0\)، نو \(V=\epsilon\)'),
 pair('But, when the circuit is closed, the current move through it experiences an associated drop in potential equal to Ir. Thus when a current is flowing through a source, the Potential difference V between the terminals of the source is V=ε-Ir. The Potential V called the terminal voltage, is less than the e.m.f. (ε) because of the term Ir representing the Potential drop across the internal resistance r.',
      'لیکن جب سرکٹ بند ہو تو اس میں سے گزرنے والی برقی رو کو Ir کے برابر پوٹینشل ڈراپ کا سامنا ہوتا ہے۔ اس لیے جب منبع میں برقی رو بہتی ہے تو منبع کے ٹرمینلز کے درمیان پوٹینشل فرق V=ε−Ir ہوتا ہے۔ ٹرمینل وولٹیج کہلانے والا پوٹینشل V، برقی محرکہ قوت (ε) سے کم ہوتا ہے کیونکہ Ir اندرونی مزاحمت r پر پوٹینشل ڈراپ کو ظاہر کرتا ہے۔',
      'خو، کله چې مدار وتړل شي، په هغه کې تېرېدونکی جریان د Ir سره برابر پوتنشیالي لوېدنه تجربه کوي. نو کله چې د سرچینې له لارې جریان تېرېږي، د سرچینې د ترمینلونو ترمنځ پوتنشیالي توپیر V=ε−Ir وي. پوتنشیال V چې ترمینلي ولتاژ بلل کېږي، د ε برېښنايي محرکې قوې څخه کم وي، ځکه Ir پر دنني مقاومت r د پوتنشیال لوېدنه ښيي.'),
]
POWER=[
 pair('12.9 ELECTRIC POWER','12.9 برقی طاقت','12.9 برېښنايي توان'),
 pair('When voltage V is applied to a circuit, it causes current I to flow through the resistance R in time t. (Figure 12.10)',
      'جب سرکٹ پر وولٹیج V لگایا جاتا ہے تو یہ وقت t میں مزاحمت R سے برقی رو I گزارنے کا سبب بنتا ہے۔ (شکل 12.10)',
      'کله چې پر مدار V ولتاژ ولګېږي، په وخت t کې د R مقاومت له لارې د I جریان د تېرېدو لامل کېږي. (12.10 شکل)'),
 pair(r'The total charge Q flows in t second is \(Q=I\times t\) and \(V=\frac{W}{Q}\)',
      r't سیکنڈ میں بہنے والا کل چارج Q یہ ہے: \(Q=I\times t\)، اور \(V=\frac{W}{Q}\)',
      r'په t ثانیه کې تېرېدونکی ټول چارج Q داسې دی: \(Q=I\times t\)، او \(V=\frac{W}{Q}\)'),
 pair(r'\(W=QV=VIt\)',r'\(W=QV=VIt\)',r'\(W=QV=VIt\)'),
 pair('Clearly work is being done in moving the charges in the circuit.', 'واضح ہے کہ سرکٹ میں چارجز کو حرکت دینے میں کام ہو رہا ہے۔','ښکاره ده چې په مدار کې د چارجونو په خوځولو کار ترسره کېږي.'),
 pair('This work done in moving the charges in a unit time is called the electric power or the rate at which work is done in an electric circuit is called electric power.',
      'چارجز کو حرکت دینے میں فی اکائی وقت کیا گیا کام برقی طاقت کہلاتا ہے، یا سرکٹ میں کام ہونے کی شرح کو برقی طاقت کہتے ہیں۔',
      'د چارجونو په خوځولو کې په واحد وخت کې ترسره شوی کار برېښنايي توان بلل کېږي، یا په برېښنايي مدار کې د کار د ترسره کېدو کچه برېښنايي توان دی.'),
 pair(r'\(\text{Electric Power}=\frac{\text{Work done in electric circuit}}{\text{Time}}\)',
      r'\(\text{برقی طاقت}=\frac{\text{سرکٹ میں کیا گیا کام}}{\text{وقت}}\)',
      r'\(\text{برېښنايي توان}=\frac{\text{په مدار کې ترسره شوی کار}}{\text{وخت}}\)'),
 pair(r'\(P=\frac{W}{t}=\frac{VIt}{t}\)',r'\(P=\frac{W}{t}=\frac{VIt}{t}\)',r'\(P=\frac{W}{t}=\frac{VIt}{t}\)'),
 pair(r'\(P=VI\) ...(12.12)',r'\(P=VI\) ...(12.12)',r'\(P=VI\) ...(12.12)'),
 pair('using Eq V=IR we get','مساوات V=IR استعمال کرنے سے ملتا ہے:','د V=IR معادلې په کارولو ترلاسه کوو:'),
 pair('or','یا','یا'),
 pair(r'\(P=I^2R\) ...(12.13)',r'\(P=I^2R\) ...(12.13)',r'\(P=I^2R\) ...(12.13)'),
 pair('or','یا','یا'),
 pair(r'\(P=\frac{V^2}{R}\) ...(12.14)',r'\(P=\frac{V^2}{R}\) ...(12.14)',r'\(P=\frac{V^2}{R}\) ...(12.14)'),
 pair('The above three formulas are equally valid for calculation of electric power in a D.C. circuit. Which one is to be used depends simply on the known quantities.',
      'اوپر کے تینوں فارمولے ڈی سی سرکٹ میں برقی طاقت معلوم کرنے کے لیے یکساں طور پر درست ہیں۔ ان میں سے کون سا استعمال کرنا ہے، اس کا انحصار معلوم مقداروں پر ہے۔',
      'پورته درې واړه فورمولونه په ډي‌سي مدار کې د برېښنايي توان د محاسبې لپاره یو شان د اعتبار وړ دي. د کوم یوه کارول پر معلومو مقدارونو پورې اړه لري.'),
]
UNITS=[
 pair('UNIT OF ELECTRIC POWER: The SI unit of power is watt. A power of 1 watt is said to be consumed in a circuit if a potential difference of 1 volt causes a current of 1 ampere to flow through it.',
      'برقی طاقت کی اکائی: طاقت کی SI اکائی واٹ ہے۔ اگر 1 وولٹ کا پوٹینشل فرق سرکٹ میں 1 ایمپیئر برقی رو گزارے تو کہتے ہیں کہ سرکٹ میں 1 واٹ طاقت استعمال ہوئی۔',
      'د برېښنايي توان واحد: د توان SI واحد واټ دی. که د 1 ولټ پوتنشیالي توپیر په مدار کې د 1 امپیر جریان د تېرېدو لامل شي، په مدار کې 1 واټ توان مصرف شوی بلل کېږي.'),
 pair(r'\(1\text{ Watt}=1\text{ V}\times1\text{ A}\)',r'\(1\text{ واٹ}=1\text{ V}\times1\text{ A}\)',r'\(1\text{ واټ}=1\text{ V}\times1\text{ A}\)'),
 pair('The bigger units of power are kilowatt (kW) and mega watt (MW)', 'طاقت کی بڑی اکائیاں کلوواٹ (kW) اور میگاواٹ (MW) ہیں۔','د توان لوی واحدونه کیلوواټ (kW) او مېګاواټ (MW) دي.'),
 pair(r'\(1\text{ kW}=1000\text{ watts}=10^3\text{ watts}\)',r'\(1\text{ kW}=1000\text{ واٹ}=10^3\text{ واٹ}\)',r'\(1\text{ kW}=1000\text{ واټ}=10^3\text{ واټ}\)'),
 pair(r'\(1\text{ MW}=10^6\text{ watts}\)',r'\(1\text{ MW}=10^6\text{ واٹ}\)',r'\(1\text{ MW}=10^6\text{ واټ}\)'),
 pair('KILOWATT-HOURS: Electric energy is commonly consumed in very large quantity for the measurement of which Joule is a very small unit. Hence a large unit of energy is required which is called kilowatt-hour. One kilowatt-hour is commonly termed as one commercial unit of electrical energy. It is the amount of energy obtained by a power of 1 kilowatt in one hour.',
      'کلوواٹ گھنٹہ: برقی توانائی عموماً بہت زیادہ مقدار میں استعمال ہوتی ہے، جس کی پیمائش کے لیے جول بہت چھوٹی اکائی ہے۔ اس لیے توانائی کی ایک بڑی اکائی درکار ہے جسے کلوواٹ گھنٹہ کہتے ہیں۔ ایک کلوواٹ گھنٹے کو عام طور پر برقی توانائی کی ایک تجارتی اکائی کہا جاتا ہے۔ یہ وہ توانائی ہے جو 1 کلوواٹ طاقت ایک گھنٹے میں فراہم کرتی ہے۔',
      'کیلوواټ‌ساعت: برېښنايي انرژي عموماً په ډېر لوی مقدار مصرفېږي، چې د اندازه کولو لپاره یې جول ډېر کوچنی واحد دی. نو د انرژۍ لوی واحد ته اړتیا ده چې کیلوواټ‌ساعت بلل کېږي. یو کیلوواټ‌ساعت عموماً د برېښنايي انرژۍ یوه سوداګریزه واحده بلل کېږي. دا هغه انرژي ده چې د 1 کیلوواټ توان په یوه ساعت کې ورکوي.'),
 pair(r'\(1\text{ kWh}=1000\text{ W}\times3600\text{ s}=3.6\times10^6\text{ W s}\)',r'\(1\text{ kWh}=1000\text{ W}\times3600\text{ s}=3.6\times10^6\text{ W s}\)',r'\(1\text{ kWh}=1000\text{ W}\times3600\text{ s}=3.6\times10^6\text{ W s}\)'),
 pair(r'\(1\text{ kWh}=3.6\times10^6\text{ J}\quad\therefore1\text{ J}=1\text{ W}\times1\text{ s}\)',r'\(1\text{ kWh}=3.6\times10^6\text{ J}\quad\therefore1\text{ J}=1\text{ W}\times1\text{ s}\)',r'\(1\text{ kWh}=3.6\times10^6\text{ J}\quad\therefore1\text{ J}=1\text{ W}\times1\text{ s}\)'),
 pair('EXAMPLE 12.5','مثال 12.5','بېلګه 12.5'),
 pair('A heating coil has a resistance of 20 Ω. It is designed to operate on 220 V. What electric energy in joules is supplied to the heater in 10 s?',
      'ایک ہیٹنگ کوائل کی مزاحمت 20 Ω ہے۔ اسے 220 V پر چلانے کے لیے بنایا گیا ہے۔ 10 s میں ہیٹر کو کتنی برقی توانائی جول میں فراہم ہوتی ہے؟',
      'د تودوخې کویل 20 Ω مقاومت لري. دا د 220 V لپاره طرحه شوی. په 10 s کې هیټر ته څومره برېښنايي انرژي په جول رسېږي؟'),
 pair('GIVEN','معلوم ہے','ورکړل شوي'),
 pair(r'\(R=20\,\Omega,\;V=220\text{ V and }t=10\text{ s}\)',r'\(R=20\,\Omega,\;V=220\text{ V او }t=10\text{ s}\)',r'\(R=20\,\Omega,\;V=220\text{ V او }t=10\text{ s}\)'),
 pair('REQUIRED','مطلوب','غوښتل شوي'),
 pair('electric energy W=?','برقی توانائی W=?','برېښنايي انرژي W=?'),
]

def make(identity,title,printed,pairs,layout,titles,pages,visual=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':39,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[{'pdfPage':39,'printedPage':n,'sourcePdf':SOURCE} for n in pages]
 if visual:s.update(visual);s['content']+=visual['diagramSvg']
 return r,s
def internal_svg(lang):
 L={'en':('internal resistance r','emf ε','load R','current I','FIGURE 12.9'),'ur':('اندرونی مزاحمت r','برقی محرکہ قوت ε','لوڈ R','برقی رو I','شکل 12.9'),'ps':('دننی مقاومت r','محرکه قوه ε','بار R','جریان I','12.9 شکل')}[lang]
 b=('<path d="M65 55H455V175H65V55" fill="none" stroke="#334155" stroke-width="3"/><rect x="95" y="72" width="100" height="84" rx="8" fill="#eff6ff" stroke="#334155" stroke-width="2"/><path d="M140 91V119M128 119H152M132 127H148" stroke="#2563eb" stroke-width="3"/><path d="M200 112l12-14 18 28 18-28 18 28 18-14" fill="none" stroke="#f59e0b" stroke-width="3"/><path d="M295 55V175" stroke="#334155" stroke-width="3"/><path d="M245 44H355" stroke="#16a34a" stroke-width="2"/><path d="M345 38l12 6-12 6" fill="#16a34a"/><text x="104" y="65" font-size="13">r</text><text x="106" y="169" font-size="13">ε</text><text x="240" y="143" font-size="13">R</text>')
 b+=f'<text x="105" y="205" font-size="12">{escape(L[0])} / {escape(L[1])}</text><text x="390" y="145" font-size="12">{escape(L[2])}</text><text x="260" y="33" font-size="13">{escape(L[3])}</text><text x="345" y="25" font-size="14">{escape(L[4])}</text>'
 return svg(b,L[4])
def charge_svg(lang):
 L={'en':('Work done on a charge','current I','voltage V','FIGURE 12.10'),'ur':('چارج پر کیا گیا کام','برقی رو I','وولٹیج V','شکل 12.10'),'ps':('پر چارج ترسره شوی کار','جریان I','ولتاژ V','12.10 شکل')}[lang]
 b=('<circle cx="88" cy="115" r="5" fill="#334155"/><circle cx="425" cy="115" r="5" fill="#334155"/><path d="M88 115H190l13-14 18 28 18-28 18 28 18-14H425" fill="none" stroke="#334155" stroke-width="3"/><path d="M150 94H250" stroke="#2563eb" stroke-width="2"/><path d="M240 88l12 6-12 6" fill="#2563eb"/><path d="M190 142H360" stroke="#16a34a" stroke-width="2"/><path d="M350 136l12 6-12 6" fill="#16a34a"/><text x="78" y="105" font-size="15">A</text><text x="421" y="105" font-size="15">B</text><text x="225" y="90" font-size="15">I</text><text x="280" y="160" font-size="15">V</text><text x="208" y="188" font-size="14">'+L[0]+'</text><text x="40" y="28" font-size="14">'+L[3]+'</text>')
 return svg(b,L[3])

if __name__=='__main__':
 i=make('phys12-unit12-internal-resistance68','Internal resistance and terminal voltage',68,INTERNAL,[{'type':'equation','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'equation','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'visual'}],('اندرونی مزاحمت اور ٹرمینل وولٹیج','دننی مقاومت او ترمینلي ولتاژ'),[68],{'diagramSvg':internal_svg('en'),'diagramSvgUrdu':internal_svg('ur'),'diagramSvgPashto':internal_svg('ps')})
 p_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'equation','indices':[6]},{'type':'visual'},{'type':'equation','indices':[7]},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]},{'type':'paragraph','indices':[12]},{'type':'equation','indices':[13]},{'type':'paragraph','indices':[14]}]
 p=make('phys12-unit12-electric-power68-69','12.9 Electric power',68,POWER,p_layout,('12.9 برقی طاقت','12.9 برېښنايي توان'),[68,69],{'diagramSvg':charge_svg('en'),'diagramSvgUrdu':charge_svg('ur'),'diagramSvgPashto':charge_svg('ps')})
 u_layout=[{'type':'heading','indices':[0]},{'type':'equation','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'equation','indices':[3]},{'type':'equation','indices':[4]},{'type':'heading','indices':[5]},{'type':'equation','indices':[6]},{'type':'equation','indices':[7]},{'type':'heading','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'heading','indices':[10]},{'type':'paragraph','indices':[11]},{'type':'heading','indices':[12]},{'type':'paragraph','indices':[13]}]
 u=make('phys12-unit12-power-units-kwh-example12569','Power units, kilowatt-hour and Example 12.5 opening',69,UNITS,u_layout,('طاقت کی اکائیاں، کلوواٹ گھنٹہ اور مثال 12.5','د توان واحدونه، کیلوواټ‌ساعت او بېلګه 12.5'),[69])
 editorial_pairs=[pair('Editorial clarification: The printed line states “r = 0 (OpenCircuit); I = 0”. For an open circuit, the current is zero (I = 0); r = 0 instead describes an ideal source with zero internal resistance. The printed wording is retained above.',
  'ادارتی وضاحت: کتاب میں “r = 0 (OpenCircuit); I = 0” چھپا ہے۔ کھلے سرکٹ میں برقی رو صفر (I = 0) ہوتی ہے؛ r = 0 اس کے بجائے صفر اندرونی مزاحمت والے مثالی منبع کو ظاہر کرتا ہے۔ اوپر کتاب کا متن جوں کا توں رکھا گیا ہے۔',
  'ادارتي وضاحت: په کتاب کې “r = 0 (OpenCircuit); I = 0” چاپ شوی. په پرانیستي مدار کې جریان صفر (I = 0) وي؛ r = 0 بیا د صفر دنني مقاومت لرونکې مثالي سرچینه ښيي. د کتاب چاپ شوی متن پورته هماغسې ساتل شوی دی.')]
 er={'id':'phys12-unit12-editorial-open-circuit68','title':'Editorial clarification — open-circuit notation','kind':'editorial','pdfPage':39,'printedPage':68,'sourcePdf':SOURCE,'paragraphs':[editorial_pairs[0][0]]}
 es=section(er,editorial_pairs,[{'type':'paragraph','indices':[0]}],('ادارتی وضاحت — اوپن سرکٹ کی علامت','ادارتي وضاحت — د پرانیستي مدار نښه'));es['kind']='editorial';es['sourceReferences']=[{'pdfPage':39,'printedPage':68,'sourcePdf':SOURCE}]
 records=[i[0],p[0],u[0],er];sections=[i[1],p[1],u[1],es]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,trim_sections=[{'id':'12.6','startsAt':'SOLUTION','title':'Example 12.5 solution — pending source review'}],
  formulas=[{'id':'phys12-unit12-eq-12.12','name':'Electric power from voltage and current','number':'12.12','formula':POWER[8][0],'latex':'P=VI','sourceReferences':[{'pdfPage':39,'printedPage':69,'sourcePdf':SOURCE}]},
   {'id':'phys12-unit12-eq-12.13','name':'Electric power from current and resistance','number':'12.13','formula':POWER[11][0],'latex':'P=I^2R','sourceReferences':[{'pdfPage':39,'printedPage':69,'sourcePdf':SOURCE}]},
   {'id':'phys12-unit12-eq-12.14','name':'Electric power from voltage and resistance','number':'12.14','formula':POWER[13][0],'latex':'P=V^2/R','sourceReferences':[{'pdfPage':39,'printedPage':69,'sourcePdf':SOURCE}]}],
  definitions=[{'term':'Electric power','definition':POWER[5][0]+' '+POWER[6][0]+' '+POWER[8][0], 'definitionUrdu':POWER[5][1]+' '+POWER[6][1]+' '+POWER[8][1], 'definitionPashto':POWER[5][2]+' '+POWER[6][2]+' '+POWER[8][2], 'sourceReferences':[{'pdfPage':39,'printedPage':68,'sourcePdf':SOURCE}]},
   {'term':'Kilowatt-hour','definition':UNITS[5][0]+' '+UNITS[6][0]+' '+UNITS[7][0], 'definitionUrdu':UNITS[5][1]+' '+UNITS[6][1]+' '+UNITS[7][1], 'definitionPashto':UNITS[5][2]+' '+UNITS[6][2]+' '+UNITS[7][2], 'sourceReferences':[{'pdfPage':39,'printedPage':69,'sourcePdf':SOURCE}]}])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==39:
  checkpoint(39,'corrected_verified',[x['id'] for x in records], 'Rendered and inspected PDF page 39, printed pages 68–69. Compared the internal-resistance equations and prose, Figure 12.9, all electric-power derivation text and equations 12.12–12.14, Figure 12.10 labels/caption, watt/kW/MW units, the full kilowatt-hour box and Example 12.5 statement/given/required. Rebuilt both circuit visuals as translated inline SVG; preserved the source open-circuit line and added a separately labeled clarification. Synchronized formulas and definitions and trimmed covered legacy text at the still-unreviewed Example 12.5 solution.',printed_pages=[68,69],chapter_number=12)

