"""Sequential source correction for PDF page 45 of Class 12 Physics."""
import json
from class12_source_review import ROOT, upsert, section, checkpoint, sync_companions
from html import escape
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps):return (en,ur,ps)
def ref(page):return {'pdfPage':45,'printedPage':page,'sourcePdf':SOURCE}
def svg(body,label):return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 300" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:560px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

WHEAT=[
 pair('From the balance condition,','توازن کی شرط سے','د توازن له شرط څخه'),
 pair(r'\(PX=RQ\)',r'\(PX=RQ\)',r'\(PX=RQ\)'),
 pair(r'\(\Rightarrow X=\frac{RQ}{P}\) ...(12.19)',r'\(\Rightarrow X=\frac{RQ}{P}\) ...(12.19)',r'\(\Rightarrow X=\frac{RQ}{P}\) ...(12.19)'),
 pair('Hence, if three resistances on the right side of equation 12.19 are known, the fourth resistance X can be calculated. This is the principle of determining unknown resistance by Wheatstone bridge.',
  'چنانچہ اگر مساوات 12.19 کے دائیں طرف کی تین مزاحمتیں معلوم ہوں تو چوتھی مزاحمت X معلوم کی جا سکتی ہے۔ یہی وہ اصول ہے جس کے ذریعے وہیٹ اسٹون برج سے نامعلوم مزاحمت معلوم کی جاتی ہے۔',
  'نو که د 12.19 معادلې ښي لوري درې مقاومتونه معلوم وي، څلورم مقاومت X محاسبه کېدای شي. دا د وېټسټون پُل په وسیله د نامعلوم مقاومت د معلومولو اصل دی.'),
]
POT=[
 pair('12.15 POTENTIOMETER','12.15 پوٹینشیومیٹر','12.15 پوتنشیومیتر'),
 pair('A potentiometer is a null type resistance network device for measuring potential differences.',
  'پوٹینشیومیٹر پوٹینشل فرق ناپنے کے لیے صفر قسم کا مزاحمتی نیٹ ورک آلہ ہے۔','پوتنشیومیتر د پوتنشیالي توپیر د اندازه کولو لپاره د صفر ډول مقاومتي شبکې وسیله ده.'),
 pair('For the accurate measurement of potential difference, current and resistance the potentiometer is most useful instrument. Its principle of action is that an unknown emf or potential difference is measured by balancing it, wholly or in part, against a known potential difference.',
  'پوٹینشل فرق، برقی رو اور مزاحمت کی درست پیمائش کے لیے پوٹینشیومیٹر بہت مفید آلہ ہے۔ اس کا اصول یہ ہے کہ نامعلوم محرکہ قوت یا پوٹینشل فرق کو معلوم پوٹینشل فرق کے مقابلے میں مکمل یا جزوی طور پر متوازن کر کے ناپا جاتا ہے۔',
  'د پوتنشیالي توپیر، جریان او مقاومت د کره اندازه کولو لپاره پوتنشیومیتر ډېره ګټوره وسیله ده. د کار اصل یې دا دی چې نامعلومه محرکه قوه یا پوتنشیالي توپیر د یوه معلوم پوتنشیالي توپیر پر وړاندې په بشپړ یا جزوي توازن کولو اندازه کوي.'),
 pair('A simplest potentiometer consists of wire AC of uniform cross-section stretched alongside a scale and connected across battery of potential V as shown in Figure 12.16.',
  'سادہ ترین پوٹینشیومیٹر میں یکساں رقبۂ مقطع والی تار AC ایک پیمانے کے ساتھ کھینچی جاتی ہے اور اسے وولٹیج V کی بیٹری کے پار جوڑا جاتا ہے، جیسا کہ شکل 12.16 میں دکھایا گیا ہے۔',
  'تر ټولو ساده پوتنشیومیتر د یو شان مقطع لرونکی AC سیم لري چې د یوې کچې ترڅنګ غځول شوی او د V ولتاژ لرونکې بیټرۍ سره نښلول شوی، لکه په 12.16 شکل کې.'),
 pair('The battery through the rheostat and slide wire supply the working current. The working current may vary by changing the setting of the rheostat.',
  'بیٹری ریوسٹیٹ اور سلائیڈ وائر کے ذریعے عملی برقی رو فراہم کرتی ہے۔ ریوسٹیٹ کی ترتیب بدل کر عملی برقی رو بدلی جا سکتی ہے۔',
  'بیټرۍ د ریوستات او ښویېدونکي سیم له لارې کاري جریان برابروي. د ریوستات د تنظیم په بدلولو کاري جریان بدلېدای شي.'),
 pair('A standard cell of known emf ε₁ is connected between A and terminal 1 of a two-way switch S.',
  'معلوم محرکہ قوت ε₁ والا معیاری سیل، A اور دو طرفہ کلید S کے ٹرمینل 1 کے درمیان جوڑا جاتا ہے۔',
  'د معلومې ε₁ محرکې قوې معیاري حجره د A او د دوه‌لارې S کیلي د 1 ترمینل ترمنځ نښلول کېږي.'),
 pair('Slider B is pressed momentarily against wire AC and its position is adjusted until the galvanometer deflection is zero when B is making contact with AC.',
  'سلائیڈر B کو لمحاتی طور پر تار AC سے لگایا جاتا ہے اور اس کی جگہ اس وقت تک بدلی جاتی ہے جب تک B کے AC سے رابطے پر گیلوانومیٹر کا انحراف صفر نہ ہو جائے۔',
  'ښویېدونکی B د یوې شېبې لپاره له AC سیم سره لګول کېږي او موقعیت یې تر هغه تنظیمېږي چې له AC سره د B د تماس پر مهال د ګالوانومیټر انحراف صفر شي.'),
 pair('Let l₁ be the corresponding distance between A and B. The fall of potential over length l₁ of the wire is then the same as the emf ε₁.',
  'فرض کریں کہ A اور B کے درمیان متعلقہ فاصلہ l₁ ہے۔ تب تار کی لمبائی l₁ پر پوٹینشل میں کمی محرکہ قوت ε₁ کے برابر ہوتی ہے۔',
  'فرض کړئ چې د A او B ترمنځ اړوند واټن l₁ دی. نو د سیم پر l₁ اوږدوالي د پوتنشیال لوېدنه له ε₁ محرکې قوې سره برابره ده.'),
 pair('Then move the switch to 2, thereby replacing the standard cell by another cell, the e.m.f. ε₂ of which is to be measured.',
  'پھر کلید کو 2 پر منتقل کریں، یوں معیاری سیل کی جگہ دوسرا سیل آ جاتا ہے جس کی محرکہ قوت ε₂ ناپنی ہے۔',
  'بیا کیلي 2 ته واړوئ، په دې سره معیاري حجره په بلې حجرې بدلېږي چې محرکه قوه ε₂ یې اندازه کېږي.'),
 pair('Adjust the slider B again to give zero deflection on G. If l₂ be the new distance between A and B, then',
  'سلائیڈر B کو دوبارہ اس طرح ایڈجسٹ کریں کہ G پر انحراف صفر ہو۔ اگر A اور B کے درمیان نیا فاصلہ l₂ ہو، تو',
  'B ښویېدونکی بیا داسې تنظیم کړئ چې پر G انحراف صفر شي. که د A او B ترمنځ نوی واټن l₂ وي، نو'),
 pair(r'\(\frac{\epsilon_2}{\epsilon_1}=\frac{l_2}{l_1}\) ...(12.20)',r'\(\frac{\epsilon_2}{\epsilon_1}=\frac{l_2}{l_1}\) ...(12.20)',r'\(\frac{\epsilon_2}{\epsilon_1}=\frac{l_2}{l_1}\) ...(12.20)'),
 pair(r'\(\epsilon_2=\frac{l_2}{l_1}\times\epsilon_1\)',r'\(\epsilon_2=\frac{l_2}{l_1}\times\epsilon_1\)',r'\(\epsilon_2=\frac{l_2}{l_1}\times\epsilon_1\)'),
 pair('Applications of potentiometer: following are the applications of potentiometer.', 'پوٹینشیومیٹر کے استعمال: پوٹینشیومیٹر کے استعمال درج ذیل ہیں۔','د پوتنشیومیتر کارونې: د پوتنشیومیتر کارونې دا دي.'),
 pair('1. Measurement of small e.m.f (upto 2V) and high e.m.f (say 250 V).','1. چھوٹی محرکہ قوت (2V تک) اور بڑی محرکہ قوت (مثلاً 250V) کی پیمائش۔','1. د کوچنۍ محرکې قوې (تر 2V پورې) او لوړې محرکې قوې (لکه 250V) اندازه کول.'),
 pair('2. Comparison of e.m.f of two cells.','2. دو سیلز کی محرکہ قوتوں کا موازنہ۔','2. د دوو حجرو د محرکو قوو پرتله کول.'),
 pair('3. Measurement of resistance and current.','3. مزاحمت اور برقی رو کی پیمائش۔','3. د مقاومت او جریان اندازه کول.'),
 pair('4. Calibration of ammeter and voltmeter.','4. ایمیٹر اور وولٹ میٹر کی کالیبریشن۔','4. د امیټر او ولټ‌مېټر کالیبراسیون.'),
]
EX128=[
 pair('EXAMPLE 12.8','مثال 12.8','بېلګه 12.8'),
 pair('Using a Weston cadium cell of 1.0183 V and a standard resistance of 0.1 Ω a potentiometer was adjusted so that 1.0183 m was equivalent to the e.m.f. of the cell; when a certain direct current was flowing through the standard resistance, the voltage across it corresponds to 150 cm. What was the value of current?',
  '1.0183 V والے ویسٹن کیڈمیم سیل اور 0.1 Ω کی معیاری مزاحمت استعمال کرتے ہوئے پوٹینشیومیٹر کو اس طرح ایڈجسٹ کیا گیا کہ 1.0183 m سیل کی محرکہ قوت کے برابر ہو؛ جب معیاری مزاحمت میں ایک خاص براہِ راست برقی رو بہتی تھی تو اس کے پار وولٹیج 150 cm کے مطابق تھا۔ برقی رو کی قدر کیا تھی؟',
  'د 1.0183 V ویسټن کډمیم حجرې او 0.1 Ω معیاري مقاومت په کارولو پوتنشیومیتر داسې تنظیم شو چې 1.0183 m د حجرې له محرکې قوې سره برابر و؛ کله چې له معیاري مقاومت څخه یوه ټاکلې مستقیمه برېښنايي جریان تېرېده، د هغه په دواړو سرونو ولتاژ له 150 cm سره برابر و. د جریان ارزښت څو و؟'),
 pair('GIVEN','معلوم ہے','ورکړل شوي'),
 pair(r'Emf of the cell \(\epsilon_1=1.0183\text{ V}\); \(l_1=1.0183\text{ m}\); \(l_2=150\text{ cm}=1.5\text{ m}\); resistance \(R=0.1\,\Omega\)',r'سیل کی محرکہ قوت \(\epsilon_1=1.0183\text{ V}\)؛ \(l_1=1.0183\text{ m}\)؛ \(l_2=150\text{ cm}=1.5\text{ m}\)؛ مزاحمت \(R=0.1\,\Omega\)',r'د حجرې محرکه قوه \(\epsilon_1=1.0183\text{ V}\)؛ \(l_1=1.0183\text{ m}\)؛ \(l_2=150\text{ cm}=1.5\text{ m}\)؛ مقاومت \(R=0.1\,\Omega\)'),
 pair('REQUIRED','مطلوب','غوښتل شوي'),
 pair(r'Current \(I_2=?\)',r'برقی رو \(I_2=?\)',r'جریان \(I_2=?\)'),
 pair('SOLUTION','حل','حل'),
 pair(r'\(\frac{\epsilon_2}{\epsilon_1}=\frac{l_2}{l_1}\)',r'\(\frac{\epsilon_2}{\epsilon_1}=\frac{l_2}{l_1}\)',r'\(\frac{\epsilon_2}{\epsilon_1}=\frac{l_2}{l_1}\)'),
 pair(r'\(\epsilon_2=\frac{l_2}{l_1}\times\epsilon_1=\frac{1.5}{1.0183}\times1.0183=1.5\text{ V}\)',r'\(\epsilon_2=\frac{l_2}{l_1}\times\epsilon_1=\frac{1.5}{1.0183}\times1.0183=1.5\text{ V}\)',r'\(\epsilon_2=\frac{l_2}{l_1}\times\epsilon_1=\frac{1.5}{1.0183}\times1.0183=1.5\text{ V}\)'),
 pair('Current flowing through the standard resistance,','معیاری مزاحمت میں بہنے والی برقی رو:','له معیاري مقاومت څخه تېرېدونکی جریان:'),
 pair(r'\(I_2=\frac{\epsilon_2}{R}=\frac{1.5}{0.1}=15\text{ A}\)',r'\(I_2=\frac{\epsilon_2}{R}=\frac{1.5}{0.1}=15\text{ A}\)',r'\(I_2=\frac{\epsilon_2}{R}=\frac{1.5}{0.1}=15\text{ A}\)'),
]
ASSIGN=[
 pair('ASSIGNMENT 12.4','اسائنمنٹ 12.4','دنده 12.4'),
 pair('A potentiometer wire of length 1 m is connected to a driver cell of emf 3 V. When a cell of 1.5 V emf is in secondary circuit the balance point is found to be at 60 cm. On replacing this cell and using a cell of unknown emf the balance point shifts to 80 cm. Calculate unknown emf of the cell.',
  '1 m لمبی پوٹینشیومیٹر تار 3 V محرکہ قوت والے ڈرائیور سیل سے منسلک ہے۔ جب 1.5 V محرکہ قوت والا سیل ثانوی سرکٹ میں ہو تو توازن کا نقطہ 60 cm پر ملتا ہے۔ اس سیل کو بدل کر نامعلوم محرکہ قوت والا سیل استعمال کرنے پر توازن کا نقطہ 80 cm پر منتقل ہو جاتا ہے۔ سیل کی نامعلوم محرکہ قوت معلوم کریں۔',
  'د 1 m اوږد پوتنشیومیتر سیم د 3 V محرکې قوې له چلوونکې حجرې سره نښلول شوی. کله چې په ثانوي مدار کې د 1.5 V محرکې قوې حجره وي، د توازن ټکی په 60 cm کې موندل کېږي. د دې حجرې په بدلولو او د نامعلومې محرکې قوې حجرې په کارولو د توازن ټکی 80 cm ته اوړي. د حجرې نامعلومه محرکه قوه محاسبه کړئ.'),
 pair('Answer (2 V)','جواب (2 V)','ځواب (2 V)'),
]

def make(identity,title,printed,pairs,layout,titles,pages):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':45,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(n) for n in pages];return r,s
def potentiometer_svg(lang):
 L={'en':('Battery','Rheostat','uniform wire AC','slider B','galvanometer G','switch S','standard cell ε₁','unknown cell ε₂','FIGURE 12.16','Simplest potentiometer circuit'),
 'ur':('بیٹری','ریوسٹیٹ','یکساں تار AC','سلائیڈر B','گیلوانومیٹر G','کلید S','معیاری سیل ε₁','نامعلوم سیل ε₂','شکل 12.16','سادہ ترین پوٹینشیومیٹر سرکٹ'),
 'ps':('بیټرۍ','ریوستات','یو شان AC سیم','ښویېدونکی B','ګالوانومیټر G','کیلي S','معیاري حجره ε₁','نامعلومه حجره ε₂','12.16 شکل','تر ټولو ساده پوتنشیومیتر مدار')}[lang]
 b=('<path d="M40 55H150M185 55H260M335 55H510V105" fill="none" stroke="#334155" stroke-width="3"/><path d="M150 35V75M165 43V67" stroke="#2563eb" stroke-width="3"/><path d="M260 55l10-10 15 20 15-20 15 20 15-10" fill="none" stroke="#f59e0b" stroke-width="3"/><text x="58" y="43" font-size="12">'+L[0]+'</text><text x="255" y="38" font-size="12">'+L[1]+'</text><path d="M45 112H510" stroke="#b45309" stroke-width="5"/><path d="M45 128H510" stroke="#334155" stroke-width="2"/><path d="M45 102V138M510 102V138" stroke="#334155" stroke-width="2"/><path d="M48 94H301M301 86H505" stroke="#16a34a" stroke-width="2"/><path d="M294 90l8 4-8 4M498 82l8 4-8 4" fill="#16a34a"/><text x="150" y="90" font-size="11">l₁</text><text x="390" y="82" font-size="11">l₂</text><text x="38" y="157" font-size="12">A / 0</text><text x="505" y="157" font-size="12">C</text><text x="142" y="153" font-size="11">50</text><text x="245" y="153" font-size="11">100</text><text x="348" y="153" font-size="11">150</text><text x="451" y="153" font-size="11">200</text><path d="M305 55V92" stroke="#2563eb" stroke-width="3"/><circle cx="305" cy="112" r="6" fill="#2563eb"/><text x="310" y="88" font-size="12">'+L[3]+'</text><path d="M305 118V177H220" stroke="#334155" stroke-width="2"/><circle cx="190" cy="177" r="22" fill="#fff" stroke="#2563eb" stroke-width="2"/><text x="184" y="182" font-size="14">G</text><path d="M168 177H95V200M95 200H55M95 200H135" fill="none" stroke="#334155" stroke-width="2"/><path d="M55 190V212M69 194V208M135 190V212M149 194V208" stroke="#2563eb" stroke-width="2"/><text x="48" y="233" font-size="12">ε₁</text><text x="129" y="233" font-size="12">ε₂</text><path d="M85 200H112" stroke="#334155" stroke-width="2"/><circle cx="112" cy="200" r="3" fill="#ef4444"/><text x="92" y="190" font-size="12">S</text><text x="10" y="19" font-size="12">'+L[8]+'</text><text x="320" y="236" font-size="12">'+L[9]+'</text><text x="15" y="255" font-size="11">'+L[2]+'; '+L[4]+'; '+L[5]+'; '+L[6]+' / '+L[7]+'</text>')
 return svg(b,L[9])

if __name__=='__main__':
 w=make('phys12-unit12-wheatstone-principle80','Wheatstone bridge — unknown resistance',80,WHEAT,[{'type':'paragraph','indices':[0]},{'type':'equation','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]}],('وہیٹ اسٹون برج — نامعلوم مزاحمت','وېټسټون پُل — نامعلوم مقاومت'),[80])
 p=make('phys12-unit12-potentiometer80-81','12.15 Potentiometer — principle and applications',80,POT,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'visual'},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]},{'type':'equation','indices':[11]},{'type':'paragraph','indices':[12]},{'type':'list','indices':[13,14,15,16]}],('12.15 پوٹینشیومیٹر — اصول اور استعمال','12.15 پوتنشیومیتر — اصل او کارونې'),[80,81])
 p[1]['diagramSvg']=potentiometer_svg('en');p[1]['diagramSvgUrdu']=potentiometer_svg('ur');p[1]['diagramSvgPashto']=potentiometer_svg('ps');p[1]['content']+=p[1]['diagramSvg']
 x=make('phys12-unit12-example12881','Example 12.8 — current through standard resistance',81,EX128,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'heading','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'heading','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'heading','indices':[6]},{'type':'equation','indices':[7]},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]},{'type':'equation','indices':[10]}],('مثال 12.8 — معیاری مزاحمت میں برقی رو','بېلګه 12.8 — په معیاري مقاومت کې جریان'),[81])
 a=make('phys12-unit12-assignment12481','Assignment 12.4 — unknown cell emf',81,ASSIGN,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]}],('اسائنمنٹ 12.4 — نامعلوم سیل کی محرکہ قوت','دنده 12.4 — د حجرې نامعلومه محرکه قوه'),[81])
 records=[w[0],p[0],x[0],a[0]];sections=[w[1],p[1],x[1],a[1]]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,retire_sections=['12.10'],trim_sections=[{'id':'12.11','startsAt':'YEY\nPOINTS','title':'Key points — pending source review'}],
  formulas=[{'id':'phys12-unit12-eq-12.19','name':'Wheatstone bridge unknown resistance','number':'12.19','formula':WHEAT[2][0],'latex':'X=RQ/P','sourceReferences':[ref(80)]},
   {'id':'phys12-unit12-eq-12.20','name':'Potentiometer balance lengths','number':'12.20','formula':POT[9][0],'latex':r'\epsilon_2/\epsilon_1=l_2/l_1','sourceReferences':[ref(81)]}],
  definitions=[{'term':'Potentiometer','definition':POT[1][0]+' '+POT[2][0], 'definitionUrdu':POT[1][1]+' '+POT[2][1], 'definitionPashto':POT[1][2]+' '+POT[2][2], 'sourceReferences':[ref(80)]}],
  worked_examples=[{'id':'textbook-example-12-8','num':'12.8','title':'Example 12.8','problem':EX128[1][0],'problemUrdu':EX128[1][1],'problemPashto':EX128[1][2],
   'given':[EX128[3][0]],'givenUrdu':[EX128[3][1]],'givenPashto':[EX128[3][2]],'required':[EX128[5][0]],'requiredUrdu':[EX128[5][1]],'requiredPashto':[EX128[5][2]],
   'steps':[EX128[i][0] for i in range(7,11)],'stepsUrdu':[EX128[i][1] for i in range(7,11)],'stepsPashto':[EX128[i][2] for i in range(7,11)],'answer':'15 A','solutionOrigin':'textbook','sourceReferences':[ref(81)]}],
  exercises=[{'id':'assignment-12-4','title':'Assignment 12.4','problems':[{'id':'assignment-12-4-q1','question':ASSIGN[1][0], 'questionUrdu':ASSIGN[1][1], 'questionPashto':ASSIGN[1][2], 'answer':'2 V','solutionOrigin':'textbook answer','sourceReferences':[ref(81)]}]}])
 if json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))['nextPage']==45:
  checkpoint(45,'corrected_verified',[r['id'] for r in records],'Rendered and visually inspected PDF page 45, printed pages 80–81. Compared Wheatstone balance continuation and Eq. 12.19, the complete potentiometer definition/principle and Figure 12.16, balance procedure and Eq. 12.20, four applications, Example 12.8 data/calculations/result, and Assignment 12.4 answer. Rebuilt the potentiometer circuit as translated SVG, paired source paragraphs, synchronized formula/definition/example/exercise cards, retired the covered legacy section and trimmed the next legacy text at the first unchecked Key Points heading.',printed_pages=[80,81],chapter_number=12)
