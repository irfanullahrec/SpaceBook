"""Sequential source correction for PDF page 42 of Class 12 Physics."""
from html import escape
from class12_source_review import upsert, section, checkpoint, sync_companions

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def svg(body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 230" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:540px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

RTD=[
 pair('Resistance thermometers','مزاحمتی تھرمامیٹر','مقاومتي ترمامیترونه'),
 pair('Accurate temperature measurement is essential for food producers, hospitals, refineries, chemical plants, in research labs, and pharmaceutical manufacturers. That’s why a great many lab and industrial applications today pick reliable, accurate resistance temperature detectors (RTDs) as the temperature measurement instrument of choice.',
  'غذائی پیداوار کرنے والوں، ہسپتالوں، ریفائنریوں، کیمیائی کارخانوں، تحقیقی لیبارٹریوں اور ادویہ ساز اداروں کے لیے درجۂ حرارت کی درست پیمائش ضروری ہے۔ اسی لیے آج بہت سی لیبارٹریوں اور صنعتی استعمالات میں قابلِ اعتماد اور درست مزاحمتی درجۂ حرارت ڈیٹیکٹرز (RTDs) کو ترجیحی پیمائشی آلہ منتخب کیا جاتا ہے۔',
  'د خوړو تولیدوونکو، روغتونونو، چاڼځایونو، کیمیاوي فابریکو، څېړنیزو لابراتوارونو او درمل جوړوونکو لپاره د تودوخې کره اندازه کول اړین دي. له همدې امله نن سبا په ډېرو لابراتواري او صنعتي کارونو کې د تودوخې د اندازه کولو د غوره وسیلې په توګه باوري او کره مقاومتي د تودوخې کشفوونکي (RTDs) غوره کېږي.'),
 pair('Resistance thermometers, also called resistance temperature detectors (RTD’s), are sensors used to measure temperature by correlating the resistance of the RTD element with temperature.',
  'مزاحمتی تھرمامیٹر، جنہیں مزاحمتی درجۂ حرارت ڈیٹیکٹر (RTD’s) بھی کہتے ہیں، ایسے سینسر ہیں جو RTD عنصر کی مزاحمت کو درجۂ حرارت سے مربوط کر کے درجۂ حرارت ناپتے ہیں۔',
  'مقاومتي ترمامیترونه، چې مقاومتي د تودوخې کشفوونکي (RTD’s) هم بلل کېږي، هغه حسکوونکي دي چې د RTD عنصر مقاومت له تودوخې سره په تړلو تودوخه اندازه کوي.'),
 pair('Common RTD sensing elements constructed of platinum, copper or nickel have a unique, and repeatable and predictable resistance versus temperature relationship (R vs T) and operating temperature range.',
  'عام RTD حس کرنے والے عناصر پلاٹینم، تانبے یا نکل سے بنائے جاتے ہیں۔ ان کا مزاحمت بمقابلہ درجۂ حرارت تعلق (R بمقابلہ T) اور عملی درجۂ حرارت کی حد منفرد، دہرائی جا سکنے والی اور قابلِ پیش گوئی ہوتی ہے۔',
  'عام RTD حسکوونکي عناصر له پلاتین، مسو یا نکل څخه جوړېږي. د مقاومت او تودوخې (R د T په وړاندې) اړیکه او د کار تودوخې لړۍ یې ځانګړې، تکرارېدونکې او اټکل‌وړ وي.'),
 pair('The R vs T relationship is defined as the amount of resistance change of the sensor per degree of temperature change.',
  'R بمقابلہ T تعلق کی تعریف یہ ہے کہ درجۂ حرارت میں فی درجے تبدیلی پر سینسر کی مزاحمت میں کتنی تبدیلی آتی ہے۔',
  'د R او T اړیکه د تودوخې د هرې درجې بدلون په مقابل کې د حسکوونکي د مقاومت د بدلون د اندازې په توګه تعریفېږي.'),
 pair('Platinum is the best metal for RTDs because it follows a very linear resistance-temperature relationship and it follows the R vs T relationship in a highly repeatable manner over a wide temperature range. The unique properties of platinum make it the material of choice for temperature standards over the range of -272.5°C to 961.78°C. They are slowly replacing the use of thermocouples in many industrial applications below 600°C, due to higher accuracy and repeatability.',
  'پلاٹینم RTDs کے لیے بہترین دھات ہے کیونکہ اس کا مزاحمت-درجۂ حرارت تعلق بہت خطی ہے اور وسیع درجۂ حرارت کی حد میں R بمقابلہ T تعلق انتہائی قابلِ تکرار انداز میں قائم رہتا ہے۔ پلاٹینم کی منفرد خصوصیات اسے -272.5°C سے 961.78°C تک درجۂ حرارت کے معیارات کے لیے پسندیدہ مادہ بناتی ہیں۔ زیادہ درستی اور تکرار پذیری کی وجہ سے 600°C سے کم بہت سے صنعتی استعمالات میں یہ آہستہ آہستہ تھرموکپلز کی جگہ لے رہے ہیں۔',
  'پلاتین د RTD لپاره تر ټولو غوره فلز دی، ځکه د مقاومت-تودوخې اړیکه یې ډېره خطي ده او په پراخه تودوخې لړۍ کې د R او T اړیکه په ډېر تکرارېدونکي ډول ساتي. د پلاتین ځانګړنې دا د -272.5°C څخه تر 961.78°C پورې د تودوخې د معیارونو لپاره غوره ماده ګرځوي. د لوړې کره‌والي او تکرارېدنې له امله، په ډېرو صنعتي کارونو کې چې له 600°C څخه ټیټ وي، ورو ورو د ترموکوپلونو ځای نیسي.'),
]
BIO=[pair('Kirchhoff was a German physicist who made significant contributions to the fundamental understanding of black-body radiation emitted by heated objects, spectroscopy, and electrical circuits.',
 'کرخوف جرمن طبیعیات دان تھے جنہوں نے گرم اجسام سے خارج ہونے والی جسمِ سیاہ کی تابکاری، طیف پیمائی اور برقی سرکٹس کی بنیادی تفہیم میں نمایاں خدمات انجام دیں۔',
 'کرخوف یو جرمنی فزیک‌پوه و چې د تودو شوو اجسامو له خوا د تور جسم د وړانګو، سپېکټروسکوپۍ او برېښنايي مدارونو په بنسټیزه پوهه کې یې مهمې ونډې لرلې.')]
KCL=[
 pair('12.13 KIRCHOFF’S LAW','12.13 کرخوف کا قانون','12.13 د کرخوف قانون'),
 pair('Many complex circuits, where simplification by series and parallel combinations is impossible due to combination of more than one batteries in a circuit. Ohm’s law cannot be applied to solve such circuits. Circuits like this are known as multi-loop circuits.',
  'بہت سے پیچیدہ سرکٹس میں ایک سے زیادہ بیٹریوں کے اتصال کی وجہ سے سلسلہ وار اور متوازی امتزاج سے سادہ کرنا ممکن نہیں ہوتا۔ ایسے سرکٹس حل کرنے کے لیے اوم کا قانون لاگو نہیں کیا جا سکتا۔ اس طرح کے سرکٹس کثیر حلقی سرکٹس کہلاتے ہیں۔',
  'په ډېرو پېچلو مدارونو کې د یوې څخه د زیاتو بیټریو د یوځای کېدو له امله د لړۍ او موازي ترکیبونو په وسیله ساده کول ناشوني وي. د داسې مدارونو د حل لپاره د اوم قانون نه شي کارېدلی. دا ډول مدارونه څوکړۍ مدارونه بلل کېږي.'),
 pair('In order to find the current in all branches of a multi-loop circuit (or the emf of a battery or the value of a resistor) Robert Kirchhoff’s gave two laws, known as Kirchhoff’s laws. These laws also apply to very simple circuits.',
  'کثیر حلقی سرکٹ کی تمام شاخوں میں برقی رو (یا بیٹری کی محرکہ قوت یا مزاحم کی قدر) معلوم کرنے کے لیے رابرٹ کرخوف نے دو قوانین دیے، جنہیں کرخوف کے قوانین کہتے ہیں۔ یہ قوانین بہت سادہ سرکٹس پر بھی لاگو ہوتے ہیں۔',
  'د څوکړۍ مدار په ټولو څانګو کې د جریان (یا د بیټرۍ د محرکې قوې یا د مقاومت د ارزښت) د موندلو لپاره رابرټ کرخوف دوه قوانین ورکړل چې د کرخوف د قوانینو په نوم یادېږي. دا قوانین پر ډېرو ساده مدارونو هم پلي کېږي.'),
 pair('KIRCHOFF’S CURRENT LAW (KCL)','کرخوف کا برقی رو کا قانون (KCL)','د کرخوف د جریان قانون (KCL)'),
 pair('Kirchhoff’s current rule (the junction rule) is manifestation of the conservation of charge to a junction; it is illustrated in Figure 12.13. Current is the flow of charge, and charge is conserved. This law is related to the currents at the junctions of an electric circuit and may be stated as under:',
  'کرخوف کا برقی رو کا قاعدہ (جوڑ کا قاعدہ) جوڑ پر بار کے بقائے کی مظہر ہے؛ اسے شکل 12.13 میں دکھایا گیا ہے۔ برقی رو بار کا بہاؤ ہے اور بار محفوظ رہتا ہے۔ یہ قانون برقی سرکٹ کے جوڑوں پر برقی روؤں سے متعلق ہے اور یوں بیان کیا جا سکتا ہے:',
  'د کرخوف د جریان قاعده (د پیوند قاعده) په پیوند کې د چارج د پایښت څرګندونه ده؛ په 12.13 شکل کې ښودل شوی. جریان د چارج بهېدل دي او چارج ساتل کېږي. دا قانون د برېښنايي مدار د پیوندونو له جریانونو سره تړاو لري او داسې بیانېدای شي:'),
 pair('The algebraic sum of all the currents meeting at a junction in an electrical circuit is zero. ΣI=0',
  'برقی سرکٹ کے کسی جوڑ پر ملنے والی تمام برقی روؤں کا الجبری مجموعہ صفر ہوتا ہے۔ ΣI=0',
  'په برېښنايي مدار کې په یوه پیوند کې د ټولو یوځای کېدونکو جریانونو جبري مجموعه صفر ده. ΣI=0'),
 pair('A junction is a point in a circuit where two or more components are connected. As algebraic sum is one in which the sign of the quantity is taken into account. For example, consider four conductors carrying currents I₁, I₂, I₃ and I₄.',
  'جوڑ سرکٹ کا وہ نقطہ ہے جہاں دو یا زیادہ اجزا منسلک ہوتے ہیں۔ الجبری مجموعے میں مقدار کی علامت کو ملحوظ رکھا جاتا ہے۔ مثال کے طور پر، چار موصلوں پر غور کریں جن میں I₁، I₂، I₃ اور I₄ برقی رو بہتی ہیں۔',
  'پیوند په مدار کې هغه ټکی دی چېرې چې دوه یا ډېر اجزا سره نښلول شوي وي. په جبري مجموعه کې د مقدار نښه په پام کې نیول کېږي. د بېلګې په توګه، څلور هادي په پام کې ونیسئ چې I₁، I₂، I₃ او I₄ جریانونه پکې تېرېږي.'),
]

def make(identity,title,printed,pairs,layout,titles,pages,visual=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':42,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[{'pdfPage':42,'printedPage':n,'sourcePdf':SOURCE} for n in pages]
 if visual:s.update(visual);s['content']+=visual['diagramSvg']
 return r,s
def rtd_svg(lang):
 L={'en':('RTD resistance sensor','temperature probe'),'ur':('RTD مزاحمتی سینسر','درجۂ حرارت پروب'),'ps':('RTD مقاومتي حسکوونکی','د تودوخې پلټونکی')}[lang]
 b=('<path d="M38 172L180 60C214 36 286 30 332 60C380 91 378 145 338 177C300 208 236 201 205 170C179 143 194 105 227 87C255 72 295 79 307 103C318 123 307 144 289 151C273 157 255 148 254 134C253 122 263 114 274 114" fill="none" stroke="#334155" stroke-width="4"/><path d="M36 178L183 64" stroke="#dc2626" stroke-width="2"/><circle cx="274" cy="114" r="7" fill="#f59e0b"/><path d="M44 191H92" stroke="#2563eb" stroke-width="3"/><text x="105" y="215" font-size="14">'+L[0]+'</text><text x="22" y="163" font-size="13">'+L[1]+'</text>')
 return svg(b,L[0])
def kirchhoff_portrait(lang):
 L={'en':('Gustar Robert Kirchhoff (1824–1887)','Kirchhoff was a German physicist'),'ur':('گوستار رابرٹ کرخوف (1824–1887)','کرخوف جرمن طبیعیات دان تھے'),'ps':('ګوستار رابرټ کرخوف (1824–1887)','کرخوف جرمنی فزیک‌پوه و')}[lang]
 b=('<rect x="170" y="40" width="205" height="150" rx="5" fill="#fff7ed" stroke="#9a3412" stroke-width="4"/><ellipse cx="272" cy="92" rx="35" ry="42" fill="#475569"/><path d="M233 90Q236 42 273 46Q312 51 311 91L300 76 290 61 267 70 247 62Z" fill="#1e293b"/><path d="M218 177Q220 122 270 123Q323 122 330 177Z" fill="#1e3a5f"/><path d="M258 124L272 149 286 124" fill="#e2e8f0"/><path d="M160 200H385" stroke="#334155" stroke-width="3"/><text x="20" y="24" font-size="14">'+L[0]+'</text><text x="20" y="222" font-size="12">'+L[1]+'</text>')
 return svg(b,L[0])
def junction_svg(lang):
 L={'en':('Junction at O with four branches','incoming current','outgoing current','FIGURE 12.13'),'ur':('چار شاخوں والا جوڑ O','آنے والی برقی رو','جانے والی برقی رو','شکل 12.13'),'ps':('په O کې له څلورو څانګو سره پیوند','راتلونکی جریان','وتونکی جریان','12.13 شکل')}[lang]
 b=('<circle cx="270" cy="120" r="13" fill="#f97316" stroke="#7c2d12" stroke-width="2"/><path d="M440 42L283 112M75 120H253M283 120H465M440 202L283 130" stroke="#475569" stroke-width="3"/><path d="M297 106l-15 4 5-14" fill="#2563eb"/><path d="M92 113l-17 7 17 7" fill="#dc2626"/><path d="M445 113l17 7-17 7" fill="#dc2626"/><path d="M297 136l-15-4 5 14" fill="#2563eb"/><text x="430" y="32" font-size="16">I₁</text><text x="34" y="110" font-size="16">I₂</text><text x="467" y="110" font-size="16">I₃</text><text x="430" y="220" font-size="16">I₄</text><text x="259" y="105" font-size="16">O</text><text x="18" y="20" font-size="13">'+L[3]+'</text><text x="18" y="220" font-size="12">'+L[0]+'</text>')
 return svg(b,L[0])

if __name__=='__main__':
 r=make('phys12-unit12-resistance-thermometers74','Resistance thermometers (RTDs)',74,RTD,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'visual'}],('مزاحمتی تھرمامیٹر (RTDs)','مقاومتي ترمامیترونه (RTDs)'),[74],{'diagramSvg':rtd_svg('en'),'diagramSvgUrdu':rtd_svg('ur'),'diagramSvgPashto':rtd_svg('ps')})
 b=make('phys12-unit12-kirchhoff-biography75','Gustar Robert Kirchhoff — biography panel',75,BIO,[{'type':'paragraph','indices':[0]},{'type':'visual'}],('گوسٹار رابرٹ کرخوف — تعارفی پینل','ګوستار رابرټ کرخوف — پېژندنیز چوکاټ'),[75],{'diagramSvg':kirchhoff_portrait('en'),'diagramSvgUrdu':kirchhoff_portrait('ur'),'diagramSvgPashto':kirchhoff_portrait('ps')})
 k=make('phys12-unit12-kirchhoff-kcl-intro75','12.13 Kirchhoff’s law and current law introduction',75,KCL,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'heading','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'visual'}],('12.13 کرخوف کا قانون اور کرنٹ قانون کا تعارف','12.13 د کرخوف قانون او د جریان قانون سریزه'),[75],{'diagramSvg':junction_svg('en'),'diagramSvgUrdu':junction_svg('ur'),'diagramSvgPashto':junction_svg('ps')})
 records=[x[0] for x in (r,b,k)];sections=[x[1] for x in (r,b,k)]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,retire_sections=['12.8'],
  formulas=[{'id':'phys12-unit12-kcl','name':'Kirchhoff’s current law','formula':KCL[5][0],'latex':r'\sum I=0','sourceReferences':[{'pdfPage':42,'printedPage':75,'sourcePdf':SOURCE}]}],
  definitions=[{'term':'Resistance temperature detector (RTD)','definition':RTD[2][0]+' '+RTD[3][0]+' '+RTD[4][0],
    'definitionUrdu':RTD[2][1]+' '+RTD[3][1]+' '+RTD[4][1],'definitionPashto':RTD[2][2]+' '+RTD[3][2]+' '+RTD[4][2],
    'sourceReferences':[{'pdfPage':42,'printedPage':74,'sourcePdf':SOURCE}]},
   {'term':'Kirchhoff’s current law','definition':KCL[4][0]+' '+KCL[5][0], 'definitionUrdu':KCL[4][1]+' '+KCL[5][1], 'definitionPashto':KCL[4][2]+' '+KCL[5][2],
    'sourceReferences':[{'pdfPage':42,'printedPage':75,'sourcePdf':SOURCE}]}])
 checkpoint(42,'corrected_verified',[x['id'] for x in records],'Rendered and inspected PDF page 42, printed pages 74–75. Compared all text in the resistance-thermometer panel, its RTD illustration, the Kirchhoff-law introduction and biography panel, KCL heading and conservation explanation, the algebraic-sum statement, and Figure 12.13 branch directions/caption. Rebuilt the sensor, biography illustration and junction as translated SVG; paired all text and synchronized the KCL formula/definitions. Retired the covered legacy continuation.',printed_pages=[74,75],chapter_number=12)
