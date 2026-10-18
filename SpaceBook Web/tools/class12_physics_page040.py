"""Sequential source correction for PDF page 40 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def ref(page): return {'pdfPage':40,'printedPage':page,'sourcePdf':SOURCE}
def svg(body,label):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:520px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

EX125=[
 pair('SOLUTION','حل','حل'),
 pair(r'From Ohm’s law \(V=IR\) or \(I=\frac{V}{R}\)',r'اوم کے قانون سے \(V=IR\) یا \(I=\frac{V}{R}\)',r'د اوم له قانون څخه \(V=IR\) یا \(I=\frac{V}{R}\)'),
 pair(r'\(I=\frac{220\text{ V}}{20\,\Omega}=11\text{ A}\)',r'\(I=\frac{220\text{ V}}{20\,\Omega}=11\text{ A}\)',r'\(I=\frac{220\text{ V}}{20\,\Omega}=11\text{ A}\)'),
 pair('Now applying the formula','اب فارمولا استعمال کرتے ہوئے','اوس فورمول په کار راوړو'),
 pair(r'\(W=I^2Rt\)',r'\(W=I^2Rt\)',r'\(W=I^2Rt\)'),
 pair(r'\(W=(11\text{ A})^2(20\,\Omega)(10\text{ s})\)',r'\(W=(11\text{ A})^2(20\,\Omega)(10\text{ s})\)',r'\(W=(11\text{ A})^2(20\,\Omega)(10\text{ s})\)'),
 pair(r'\(W=24200\text{ J}\)',r'\(W=24200\text{ J}\)',r'\(W=24200\text{ J}\)'),
]
EX126=[
 pair('EXAMPLE 12.6','مثال 12.6','بېلګه 12.6'),
 pair('The following are the details of load and a circuit connected through a supply meter.',
      'سپلائی میٹر سے منسلک لوڈ اور سرکٹ کی تفصیل درج ذیل ہے۔',
      'د بار او مدار تفصیل چې د برېښنايي میټر له لارې نښلول شوي، په لاندې ډول ده.'),
 pair('(i) Six lamps of 40 watts each working for 4 hours per day.', '(i) 40 واٹ کے چھ بلب روزانہ 4 گھنٹے کام کرتے ہیں۔','(i) شپږ څراغونه چې هر یو 40 واټه دی، هره ورځ 4 ساعته کار کوي.'),
 pair('(ii) Two fluorescent tubes 125 watts each working for 2 hours per day.', '(ii) 125 واٹ کی دو فلوروسینٹ ٹیوبیں روزانہ 2 گھنٹے کام کرتی ہیں۔','(ii) دوه فلوروسېنټ ټیوبونه چې هر یو 125 واټه دی، هره ورځ 2 ساعته کار کوي.'),
 pair('(iii) 1000 watts heater working for 3 hours per day.', '(iii) 1000 واٹ کا ہیٹر روزانہ 3 گھنٹے کام کرتا ہے۔','(iii) د 1000 واټه هیټر هره ورځ 3 ساعته کار کوي.'),
 pair('Find the cost of electrical energy consumed in 30 days of a month when the rate of electricity is 7.0 Rs per unit.',
      'جب بجلی کی قیمت 7.0 روپے فی یونٹ ہو تو مہینے کے 30 دنوں میں استعمال ہونے والی برقی توانائی کی قیمت معلوم کریں۔',
      'کله چې د برېښنا بیه د هر یونټ لپاره 7.0 روپۍ وي، په 30 ورځو کې د مصرف شوې برېښنايي انرژۍ لګښت پیدا کړئ.'),
 pair('SOLUTION','حل','حل'),
 pair(r'Total watts for lamps \(=40\times6=240\) watts',r'بلبوں کے کل واٹ \(=40\times6=240\) واٹ',r'د څراغونو ټول واټونه \(=40\times6=240\) واټه'),
 pair(r'Total watts for tubes \(=125\times2=250\) watts',r'ٹیوبوں کے کل واٹ \(=125\times2=250\) واٹ',r'د ټیوبونو ټول واټونه \(=125\times2=250\) واټه'),
 pair('Heater = 1000 watts','ہیٹر = 1000 واٹ','هیټر = 1000 واټه'),
 pair('Energy consumed per day','روزانہ استعمال ہونے والی توانائی','په ورځ کې مصرفېدونکې انرژي'),
 pair(r'\(=(250\times4)+(250\times2)+(1000\times3)\)',r'\(=(250\times4)+(250\times2)+(1000\times3)\)',r'\(=(250\times4)+(250\times2)+(1000\times3)\)'),
 pair(r'\(=4460\) watt hours',r'\(=4460\) واٹ گھنٹے',r'\(=4460\) واټ‌ساعته'),
 pair(r'\(=4.46\text{ kWh}\)',r'\(=4.46\text{ kWh}\)',r'\(=4.46\text{ kWh}\)'),
 pair('Total energy consumed in the month of June','جون کے مہینے میں استعمال ہونے والی کل توانائی','په جون میاشت کې مصرف شوې ټوله انرژي'),
 pair(r'\(=4.46\times30=133.8\text{ kWh}\)',r'\(=4.46\times30=133.8\text{ kWh}\)',r'\(=4.46\times30=133.8\text{ kWh}\)'),
 pair('Bill for the month of June','جون کے مہینے کا بل','د جون میاشت بل'),
 pair(r'\(=7\times133.8=936.6\text{ Rs}\)',r'\(=7\times133.8=936.6\text{ روپے}\)',r'\(=7\times133.8=936.6\text{ روپۍ}\)'),
]
ASSIGNMENT=[
 pair('ASSIGNMENT 12.2','اسائنمنٹ 12.2','دنده 12.2'),
 pair('A heating coil is rated at 100W,220V. The coil is cut in half and two pieces are joined in parallel to the same source. Now what is the energy liberated per second?',
      'ایک ہیٹنگ کوائل کی درجہ بندی 100W,220V ہے۔ کوائل کو آدھا کاٹ کر دونوں ٹکڑوں کو اسی منبع کے ساتھ متوازی جوڑا جاتا ہے۔ اب فی سیکنڈ کتنی توانائی خارج ہوتی ہے؟',
      'د تودوخې کویل 100W,220V درجه‌بندي لري. کویل نیمایي کېږي او دواړه ټوټې له هماغې سرچینې سره په موازي ډول نښلول کېږي. اوس په هره ثانیه کې څومره انرژي ازادېږي؟'),
 pair('Answer (4×10²J)','جواب (4×10²J)','ځواب (4×10²J)'),
]
MAXPOWER=[
 pair('12.10 MAXIMUM POWER OUTPUT','12.10 زیادہ سے زیادہ طاقت کا اخراج','12.10 د اعظمي توان وتۍ'),
 pair('In many electronic circuits and systems it is important to have maximum transfer of power from the source to the load. For example, in radio or TV transmitting systems, it is desired to transfer the maximum power possible from the transmitting medium to the antenna systems. We want maximum power transfer from amplifier to speaker system. This is accomplished by proper matching of load resistance R and source resistance r.',
      'بہت سے برقی سرکٹس اور نظاموں میں منبع سے لوڈ تک طاقت کی زیادہ سے زیادہ منتقلی اہم ہوتی ہے۔ مثلاً ریڈیو یا ٹی وی کے ترسیلی نظاموں میں ترسیلی ذریعے سے اینٹینا نظام تک ممکنہ زیادہ سے زیادہ طاقت منتقل کرنا مطلوب ہوتا ہے۔ ایمپلی فائر سے اسپیکر نظام تک زیادہ سے زیادہ طاقت منتقل کرنا مقصود ہے۔ یہ لوڈ مزاحمت R اور منبع مزاحمت r کو مناسب طور پر ملانے سے حاصل ہوتا ہے۔',
      'په ډېرو برېښنايي مدارونو او سیستمونو کې له سرچینې څخه بار ته د توان اعظمي لېږد مهم دی. د بېلګې په توګه، په راډیو یا ټلوېزیون خپروونکو سیستمونو کې له خپروونکي منځني څخه انتن سیستم ته د امکان تر ټولو ډېر توان لېږدول مطلوب دي. له امپلیفایر څخه سپیکر ته د اعظمي توان لېږد غواړو. دا د بار مقاومت R او د سرچینې مقاومت r په سم برابرولو ترلاسه کېږي.'),
 pair('If the load resistance is less or greater than the source resistance, then the power delivered to the load will be minimum.',
      'اگر لوڈ مزاحمت منبع مزاحمت سے کم یا زیادہ ہو تو لوڈ کو دی جانے والی طاقت کم سے کم ہو گی۔',
      'که د بار مقاومت د سرچینې له مقاومت څخه کم یا زیات وي، بار ته ورکړل کېدونکی توان لږ تر لږه وي.'),
 pair('Consider the circuit of figure 12.11, as the current I flows through the load resistance R the charges flow from a point of higher potential to a point of lower potential. In this process, they lose potential energy. If V is the potential difference across R, the loss of potential energy per second is known as power delivered to R by the current I.',
      'شکل 12.11 کا سرکٹ دیکھیں۔ جب برقی رو I لوڈ مزاحمت R سے گزرتی ہے تو چارج زیادہ پوٹینشل کے نقطے سے کم پوٹینشل کے نقطے کی طرف بہتے ہیں۔ اس عمل میں وہ پوٹینشل توانائی کھو دیتے ہیں۔ اگر R کے پار پوٹینشل فرق V ہو تو فی سیکنڈ پوٹینشل توانائی کے نقصان کو برقی رو I کی طرف سے R کو دی جانے والی طاقت کہتے ہیں۔',
      'د 12.11 شکل مدار ته وګورئ؛ کله چې I جریان د بار له R مقاومت څخه تېرېږي، چارجونه له لوړ پوتنشیال څخه ټیټ پوتنشیال ته بهېږي. په دې بهیر کې دوی پوتنشیالي انرژي له لاسه ورکوي. که د R په دواړو غاړو کې پوتنشیالي توپیر V وي، په هره ثانیه کې د پوتنشیالي انرژۍ ضایع د هغه توان په توګه پېژندل کېږي چې د I جریان یې R ته ورکوي.'),
 pair('From electrical power','برقی طاقت سے','له برېښنايي توان څخه'),
 pair(r'\(P_{out}=IV\)',r'\(P_{out}=IV\)',r'\(P_{out}=IV\)'),
 pair(r'\(P_{out}=I^2R\)',r'\(P_{out}=I^2R\)',r'\(P_{out}=I^2R\)'),
 pair(r'\(P_{out}=\frac{\epsilon^2R}{(R+r)^2}\)',r'\(P_{out}=\frac{\epsilon^2R}{(R+r)^2}\)',r'\(P_{out}=\frac{\epsilon^2R}{(R+r)^2}\)'),
 pair(r'\(P_{out}=\frac{\epsilon^2R}{(R-r)^2+4Rr}\)',r'\(P_{out}=\frac{\epsilon^2R}{(R-r)^2+4Rr}\)',r'\(P_{out}=\frac{\epsilon^2R}{(R-r)^2+4Rr}\)'),
 pair(r'When \(R=r\), the denominator of the expression for \(P_{out}\) is minimum and so \(P_{out}\) is maximum.',
      r'جب \(R=r\) ہو تو \(P_{out}\) کی مساوات کا مخرج کم سے کم ہوتا ہے اور اس لیے \(P_{out}\) زیادہ سے زیادہ ہوتا ہے۔',
      r'کله چې \(R=r\) وي، د \(P_{out}\) د عبارت مخرج لږ تر لږه وي او له همدې امله \(P_{out}\) اعظمي وي.'),
 pair('Thus it can be concluded that maximum power is delivered to a load R when the internal resistance of the source of emf is equal to the load resistance, also called maximum power transfer theorem.',
      'یوں نتیجہ اخذ کیا جا سکتا ہے کہ لوڈ R کو زیادہ سے زیادہ طاقت اس وقت دی جاتی ہے جب برقی محرکہ قوت کے منبع کی اندرونی مزاحمت لوڈ مزاحمت کے برابر ہو۔ اسے زیادہ سے زیادہ طاقت کی منتقلی کا نظریہ بھی کہتے ہیں۔',
      'نو پایله دا ده چې بار R ته اعظمي توان هغه وخت ورکول کېږي چې د محرکې قوې سرچینې دننی مقاومت د بار له مقاومت سره برابر وي؛ دې ته د اعظمي توان لېږد قضیه هم ویل کېږي.'),
 pair('The value of the maximum output power is','د زیادہ سے زیادہ آؤٹ پٹ طاقت کی قدر یہ ہے:','د اعظمي وتۍ توان ارزښت دا دی:'),
 pair(r'\((P_{out})_{max}=\frac{\epsilon^2}{4r}=\frac{\epsilon^2}{4R}\) ...(12.15)',r'\((P_{out})_{max}=\frac{\epsilon^2}{4r}=\frac{\epsilon^2}{4R}\) ...(12.15)',r'\((P_{out})_{max}=\frac{\epsilon^2}{4r}=\frac{\epsilon^2}{4R}\) ...(12.15)'),
]

def make(identity,title,printed,pairs,layout,titles,pages):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':40,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(n) for n in pages]
 return r,s
def maxpower_svg(lang):
 L={'en':('emf ε','internal resistance r','load R','current I','FIGURE 12.11'),'ur':('برقی محرکہ قوت ε','اندرونی مزاحمت r','لوڈ R','برقی رو I','شکل 12.11'),'ps':('محرکه قوه ε','دننی مقاومت r','بار R','جریان I','12.11 شکل')}[lang]
 b=('<path d="M70 48H450V175H70V48" fill="none" stroke="#334155" stroke-width="3"/><rect x="100" y="66" width="95" height="88" rx="7" fill="#eff6ff" stroke="#334155" stroke-width="2"/><path d="M147 85V111M135 111H159M139 120H155" stroke="#2563eb" stroke-width="3"/><path d="M198 110l12-14 18 28 18-28 18 28 18-14" fill="none" stroke="#f59e0b" stroke-width="3"/><path d="M282 48V175" stroke="#334155" stroke-width="3"/><path d="M240 37H365" stroke="#16a34a" stroke-width="2"/><path d="M355 31l12 6-12 6" fill="#16a34a"/><text x="110" y="61" font-size="14">r</text><text x="111" y="168" font-size="14">ε</text><text x="230" y="142" font-size="14">R</text>')
 b+=f'<text x="75" y="208" font-size="12">{escape(L[0])} / {escape(L[1])}</text><text x="390" y="146" font-size="12">{escape(L[2])}</text><text x="268" y="30" font-size="13">{escape(L[3])}</text><text x="344" y="23" font-size="14">{escape(L[4])}</text>'
 return svg(b,L[4])

if __name__=='__main__':
 e=make('phys12-unit12-example125-solution70','Example 12.5 — heating-coil energy',70,EX125,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'equation','indices':[5]},{'type':'equation','indices':[6]}],('مثال 12.5 — ہیٹنگ کوائل کی توانائی','بېلګه 12.5 — د تودوخې کویل انرژي'),[70])
 x_layout=[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'list','indices':[2,3,4]},{'type':'paragraph','indices':[5]},{'type':'heading','indices':[6]},{'type':'equation','indices':[7]},{'type':'equation','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]},{'type':'equation','indices':[12]},{'type':'equation','indices':[13]},{'type':'paragraph','indices':[14]},{'type':'equation','indices':[15]},{'type':'paragraph','indices':[16]},{'type':'equation','indices':[17]}]
 x=make('phys12-unit12-example126-energy-cost70','Example 12.6 — monthly electricity cost',70,EX126,x_layout,('مثال 12.6 — ماہانہ بجلی کا خرچ','بېلګه 12.6 — د میاشتې د برېښنا لګښت'),[70])
 a=make('phys12-unit12-assignment12270','Assignment 12.2 — heating-coil power',70,ASSIGNMENT,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]}],('اسائنمنٹ 12.2 — ہیٹنگ کوائل کی طاقت','دنده 12.2 — د تودوخې کویل توان'),[70])
 m=make('phys12-unit12-maximum-power-output71','12.10 Maximum power output',71,MAXPOWER,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'equation','indices':[6]},{'type':'equation','indices':[7]},{'type':'equation','indices':[8]},{'type':'visual'},{'type':'paragraph','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'paragraph','indices':[11]},{'type':'equation','indices':[12]}],('12.10 زیادہ سے زیادہ طاقت کا اخراج','12.10 د اعظمي توان وتۍ'),[71],)
 m[1]['diagramSvg']=maxpower_svg('en');m[1]['diagramSvgUrdu']=maxpower_svg('ur');m[1]['diagramSvgPashto']=maxpower_svg('ps');m[1]['content']+=m[1]['diagramSvg']
 clarification_pairs=[pair('Editorial clarification: The printed solution states “Total watts for lamps = 40×6 = 240 watts”, but its daily-energy calculation uses 250×4 for the lamps. The source values conflict; both printed lines are preserved without substituting one for the other.',
  'ادارتی وضاحت: کتاب کے حل میں “بلبوں کے کل واٹ = 40×6 = 240 واٹ” لکھا ہے، لیکن روزانہ توانائی کے حساب میں بلبوں کے لیے 250×4 استعمال ہوا ہے۔ کتاب کی دونوں قدریں باہم متضاد ہیں؛ دونوں سطریں جوں کی توں رکھی گئی ہیں اور کسی ایک کو دوسری سے تبدیل نہیں کیا گیا۔',
  'ادارتي وضاحت: په چاپ شوي حل کې “د څراغونو ټول واټونه = 40×6 = 240 واټه” دي، خو د ورځنۍ انرژۍ په محاسبه کې د څراغونو لپاره 250×4 کارول شوي. د سرچینې ارزښتونه سره په ټکر کې دي؛ دواړه چاپ شوې کرښې هماغسې ساتل شوې او یوه پر بله نه ده بدله شوې.')]
 er={'id':'phys12-unit12-editorial-example126-lamps70','title':'Editorial clarification — Example 12.6 lamp calculation','kind':'editorial','pdfPage':40,'printedPage':70,'sourcePdf':SOURCE,'paragraphs':[clarification_pairs[0][0]]}
 es=section(er,clarification_pairs,[{'type':'paragraph','indices':[0]}],('ادارتی وضاحت — مثال 12.6 کے بلبوں کا حساب','ادارتي وضاحت — د 12.6 بېلګې د څراغونو محاسبه'));es['kind']='editorial';es['sourceReferences']=[ref(70)]
 records=[e[0],x[0],a[0],m[0],er];sections=[e[1],x[1],a[1],m[1],es]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,retire_sections=['12.6'],trim_sections=[{'id':'12.7','startsAt':'THERMOCOUPLES','title':'12.11 Thermocouples — continuation pending source review'}],
  formulas=[{'id':'phys12-unit12-eq-12.15','name':'Maximum output power','number':'12.15','formula':MAXPOWER[12][0],'latex':r'(P_{out})_{max}=\frac{\epsilon^2}{4r}=\frac{\epsilon^2}{4R}','sourceReferences':[ref(71)]}],
  definitions=[{'term':'Maximum power transfer theorem','definition':MAXPOWER[10][0]+' '+MAXPOWER[11][0]+' '+MAXPOWER[12][0],
   'definitionUrdu':MAXPOWER[10][1]+' '+MAXPOWER[11][1]+' '+MAXPOWER[12][1], 'definitionPashto':MAXPOWER[10][2]+' '+MAXPOWER[11][2]+' '+MAXPOWER[12][2], 'sourceReferences':[ref(71)]}],
  worked_examples=[{'id':'textbook-example-12-5','num':'12.5','title':'Example 12.5','problem':'A heating coil has a resistance of 20 Ω. It is designed to operate on 220 V. What electric energy in joules is supplied to the heater in 10 s?',
   'problemUrdu':'ایک ہیٹنگ کوائل کی مزاحمت 20 Ω ہے۔ اسے 220 V پر چلانے کے لیے بنایا گیا ہے۔ 10 s میں ہیٹر کو کتنی برقی توانائی جول میں فراہم ہوتی ہے؟',
   'problemPashto':'د تودوخې کویل 20 Ω مقاومت لري. دا د 220 V لپاره طرحه شوی. په 10 s کې هیټر ته څومره برېښنايي انرژي په جول رسېږي؟',
   'given':[r'R=20\,\Omega, V=220\text{ V}, t=10\text{ s}'],'required':['electric energy W=?'],'steps':[p[0] for p in EX125[1:]],'stepsUrdu':[p[1] for p in EX125[1:]],'stepsPashto':[p[2] for p in EX125[1:]],'answer':'24200 J','solutionOrigin':'textbook','sourceReferences':[ref(70)]},
   {'id':'textbook-example-12-6','num':'12.6','title':'Example 12.6','problem':EX126[1][0],'problemUrdu':EX126[1][1],'problemPashto':EX126[1][2],
    'given':[EX126[i][0] for i in (2,3,4)],'givenUrdu':[EX126[i][1] for i in (2,3,4)],'givenPashto':[EX126[i][2] for i in (2,3,4)],
    'required':[EX126[5][0]],'requiredUrdu':[EX126[5][1]],'requiredPashto':[EX126[5][2]],'steps':[EX126[i][0] for i in range(7,18)],'stepsUrdu':[EX126[i][1] for i in range(7,18)],'stepsPashto':[EX126[i][2] for i in range(7,18)],
    'answer':'936.6 Rs','solutionOrigin':'textbook','sourceReferences':[ref(70)]}],
  exercises=[{'id':'assignment-12-2','title':'Assignment 12.2','problems':[{'id':'assignment-12-2-q1','question':ASSIGNMENT[1][0],
   'questionUrdu':ASSIGNMENT[1][1],'questionPashto':ASSIGNMENT[1][2],'answer':'4×10²J','solutionOrigin':'textbook answer','sourceReferences':[ref(70)]}]}])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==40:
  checkpoint(40,'corrected_verified',[r['id'] for r in records], 'Rendered and inspected PDF page 40, printed pages 70–71. Compared the full Example 12.5 solution, Example 12.6 statement, all three load items, each printed solution line and result, Assignment 12.2 answer, the complete maximum-power explanation, Figure 12.11 and Eq. 12.15. Preserved the textbook’s conflicting lamp total/calculation and added a separate translated clarification. Rebuilt Figure 12.11 as translated SVG; synchronized both worked examples, the exercise, formula and theorem definition; retired covered legacy 12.6 and trimmed legacy 12.7 at the next unreviewed thermocouples heading.',printed_pages=[70,71],chapter_number=12)
