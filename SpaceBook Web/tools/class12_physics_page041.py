"""Sequential source correction for PDF page 41 of Class 12 Physics."""
from html import escape
from class12_source_review import upsert, section, checkpoint, sync_companions

SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def svg(body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 245" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:540px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

THERMO=[
 pair('12.11 THERMOCOUPLES','12.11 تھرموکپلز','12.11 ترموکوپلونه'),
 pair('In early 1821, Thomas Seebeck searched experimentally for a relation between electricity and heat. A thermocouple consists of two dissimilar wires A and B that are joined at one end T₁ (the “hot” junction). The other end T₂ (the “cold” junction) is maintained at a constant reference temperature (usually the melting point of ice).',
  '1821 کے اوائل میں تھامس سیبیک نے بجلی اور حرارت کے تعلق کو تجرباتی طور پر تلاش کیا۔ تھرموکپل دو مختلف تاروں A اور B پر مشتمل ہوتا ہے، جو ایک سرے T₁ (“گرم” جوڑ) پر ملے ہوتے ہیں۔ دوسرا سرا T₂ (“سرد” جوڑ) مستقل حوالہ درجۂ حرارت (عموماً برف کے نقطۂ پگھلاؤ) پر رکھا جاتا ہے۔',
  'د 1821 کال په پیل کې توماس سیبېک د برېښنا او تودوخې ترمنځ اړیکه په تجربوي ډول وپلټله. ترموکوپل له دوو بېلابېلو A او B سیمونو جوړ دی چې په یوه پای T₁ (“ګرم” پیوند) کې سره نښلول شوي. بل پای T₂ (“سړه” پیوند) په ثابت مرجع تودوخې (عموماً د یخ د ویلې کېدو په تودوخه) ساتل کېږي.'),
 pair('The device connected at their ends shows a deflection. This is known as Seebeck Effect. The e.m.f. generated in the circuit is called thermoelectric e.m.f. In this process energy is directly converted into electrical energy. Figure 12.12 (a) shows an arrangement to study the effect of temperature difference between the two junctions in a Cu-Fe thermocouple.',
  'سروں پر جوڑا ہوا آلہ انحراف دکھاتا ہے۔ اسے سیبیک اثر کہتے ہیں۔ سرکٹ میں پیدا ہونے والی برقی محرکہ قوت کو حرارتی برقی محرکہ قوت کہتے ہیں۔ اس عمل میں توانائی براہِ راست برقی توانائی میں تبدیل ہوتی ہے۔ شکل 12.12 (a) میں Cu-Fe تھرموکپل کے دونوں جوڑوں کے درمیان درجۂ حرارت کے فرق کا اثر دیکھنے کا انتظام دکھایا گیا ہے۔',
  'په پایونو کې نښلول شوې وسیله انحراف ښيي. دې ته د سیبېک اغېز ویل کېږي. په مدار کې رامنځته شوې محرکه قوه حرارتي برېښنايي محرکه قوه بلل کېږي. په دې بهیر کې انرژي نېغ په نېغه برېښنايي انرژۍ ته بدلېږي. 12.12 (a) شکل د Cu-Fe ترموکوپل د دوو پیوندونو ترمنځ د تودوخې د توپیر د اغېز د مطالعې ترتیب ښيي.'),
 pair('Thus thermocouple is a temperature measuring device. In other words, it is a type of sensor used for measuring the temperature in the form of an electric current or the EMF.',
  'چنانچہ تھرموکپل درجۂ حرارت ناپنے کا آلہ ہے۔ دوسرے لفظوں میں، یہ ایک قسم کا سینسر ہے جو برقی رو یا EMF کی صورت میں درجۂ حرارت ناپتا ہے۔',
  'نو ترموکوپل د تودوخې د اندازه کولو وسیله ده. په بله وینا، دا یو ډول حسکوونکی دی چې تودوخه د برېښنايي جریان یا EMF په بڼه اندازه کوي.'),
 pair('The wire pairs can be composed of noble metals (such as platinum, iridium, silver, osmium, gold, and rhodium) or base metals, (such as copper, iron or nickel-copper alloy, lead and zinc). Thus it remains true for any pair of metals.',
  'تاروں کے جوڑے قیمتی دھاتوں (مثلاً پلاٹینم، اریڈیم، چاندی، اوسمیم، سونا اور روڈیم) یا بنیادی دھاتوں (مثلاً تانبا، لوہا یا نکل-تانبا مرکب، سیسہ اور زنک) سے بن سکتے ہیں۔ یوں یہ بات دھاتوں کے کسی بھی جوڑے کے لیے درست رہتی ہے۔',
  'د سیمونو جوړې له قیمتي فلزونو (لکه پلاتین، اېریډیم، سپین زر، اوسمیم، سره زر او روډیم) یا بنسټیزو فلزونو (لکه مس، اوسپنه یا د نکل-مس الیاژ، سرب او زنک) جوړېدای شي. نو دا د فلزونو د هرې جوړې لپاره سمه ده.'),
 pair('Thermocouples are the most widely used temperature sensors in industry due to their low cost, simplicity, size and useable temperature range. The electromotive force ε is a function of the temperature gradient. The thermo-e.m.f. produced is very small, of the order of mV per every degree of temperature difference. The Seebeck effect is reversible, i.e., if the hot and cold junctions are interchanged, the direction of e.m.f. (and hence current) reverses.',
  'کم قیمت، سادگی، چھوٹے حجم اور قابلِ استعمال درجۂ حرارت کی حد کے باعث صنعت میں تھرموکپلز سب سے زیادہ استعمال ہونے والے درجۂ حرارت کے سینسر ہیں۔ برقی محرکہ قوت ε درجۂ حرارت کے تدریج کا تابع ہے۔ پیدا ہونے والی حرارتی برقی محرکہ قوت بہت کم، یعنی ہر درجے کے فرقِ درجۂ حرارت پر چند mV کے درجے کی ہوتی ہے۔ سیبیک اثر قابلِ واپسی ہے؛ یعنی گرم اور سرد جوڑ بدل دیے جائیں تو محرکہ قوت (اور اس لیے برقی رو) کی سمت الٹ جاتی ہے۔',
  'د ټیټ لګښت، ساده‌والي، کوچنۍ اندازې او د کار وړ تودوخې د لړۍ له امله ترموکوپلونه په صنعت کې تر ټولو ډېر کارېدونکي د تودوخې حسکوونکي دي. برېښنايي محرکه قوه ε د تودوخې د تدریج تابع ده. تولیدېدونکې حرارتي محرکه قوه ډېره لږه وي، د تودوخې د توپیر د هرې درجې لپاره د څو mV په کچه. د سیبېک اغېز بېرته‌ګرځېدونکی دی؛ یعنې که ګرم او سړه پیوندونه بدل شي، د محرکې قوې (او ورسره د جریان) لوری اوړي.'),
 pair('The greater the separation of the metals forming the thermocouple in series, greater is the thermo e.m.f. produced.',
  'سلسلے میں تھرموکپل بنانے والی دھاتوں کی علیحدگی جتنی زیادہ ہو، پیدا ہونے والی حرارتی برقی محرکہ قوت اتنی ہی زیادہ ہوتی ہے۔',
  'څومره چې په لړۍ کې د ترموکوپل جوړوونکو فلزونو جلاوالی ډېر وي، تولیدېدونکې حرارتي محرکه قوه هم هغومره ډېره وي.'),
 pair('Its temperature dependence is given by','اس کا درجۂ حرارت پر انحصار یہ ہے:','پر تودوخې یې تړاو داسې دی:'),
 pair(r'\(\epsilon=\alpha T+\frac{1}{2}\beta T^2\) ...(12.16)',r'\(\epsilon=\alpha T+\frac{1}{2}\beta T^2\) ...(12.16)',r'\(\epsilon=\alpha T+\frac{1}{2}\beta T^2\) ...(12.16)'),
 pair('Where α and β are constants (called thermoelectric coefficients) which depends on the nature of the metals.',
  'جہاں α اور β مستقل ہیں (انہیں حرارتی برقی ضریب کہتے ہیں) اور ان کا انحصار دھاتوں کی نوعیت پر ہے۔',
  'چې α او β ثابتونه دي (حرارتي برېښنايي ضریبونه بلل کېږي) او د فلزونو پر طبیعت پورې اړه لري.'),
]
VARIATION=[
 pair('12.12 VARIATION IN THERMOELECTRIC e.m.f. WITH TEMPERATURE','12.12 درجۂ حرارت کے ساتھ حرارتی برقی محرکہ قوت میں تبدیلی','12.12 له تودوخې سره د حرارتي برېښنايي محرکې قوې بدلون'),
 pair('Keeping the junction B at 0°C, the temperature of junction A is increased. When both the junctions are at the same temperature, there is no thermo e.m.f. When the temperature at one junction is cold while at the other end is increased the thermo e.m.f. also increases with temperature and reaches a maximum value at a certain temperature, called the neutral temperature Tₙ.',
  'جوڑ B کو 0°C پر رکھتے ہوئے جوڑ A کا درجۂ حرارت بڑھایا جاتا ہے۔ جب دونوں جوڑ ایک ہی درجۂ حرارت پر ہوں تو حرارتی برقی محرکہ قوت نہیں ہوتی۔ جب ایک جوڑ سرد ہو اور دوسرے سرے کا درجۂ حرارت بڑھایا جائے تو حرارتی برقی محرکہ قوت بھی بڑھتی ہے اور ایک خاص درجۂ حرارت پر زیادہ سے زیادہ قدر تک پہنچتی ہے، جسے غیر جانب دار درجۂ حرارت Tₙ کہتے ہیں۔',
  'د B پیوند په 0°C ساتلو سره د A پیوند تودوخه لوړېږي. کله چې دواړه پیوندونه په یوه تودوخه وي، حرارتي محرکه قوه نه وي. کله چې یو پیوند سوړ وي او د بل پای تودوخه لوړه شي، حرارتي محرکه قوه هم له تودوخې سره زیاتېږي او په یوه ټاکلې تودوخه کې اعظمي ارزښت ته رسېږي چې بې‌طرفه تودوخه Tₙ بلل کېږي.'),
 pair('The value of the neutral temperature is constant for a thermocouple, depends on the nature of materials and is independent of the temperature of the cold junction. As the temperature of the hot junction is increased, the thermo e.m.f. starts decreasing instead of increasing.',
  'غیر جانب دار درجۂ حرارت کی قدر کسی تھرموکپل کے لیے مستقل ہوتی ہے، مادوں کی نوعیت پر منحصر ہوتی ہے اور سرد جوڑ کے درجۂ حرارت سے آزاد ہوتی ہے۔ گرم جوڑ کا درجۂ حرارت مزید بڑھانے پر حرارتی برقی محرکہ قوت بڑھنے کے بجائے کم ہونا شروع ہو جاتی ہے۔',
  'د بې‌طرفه تودوخې ارزښت د ترموکوپل لپاره ثابت وي، د موادو پر طبیعت پورې اړه لري او د سړې پیوند له تودوخې خپلواک وي. د ګرم پیوند د تودوخې په لا لوړېدو، حرارتي محرکه قوه د زیاتېدو پر ځای کمېدل پیلوي.'),
 pair('The particular temperature at which the thermo e.m.f. becomes zero is called the inversion temperature Figure 12.12 (b). The graph shows the variation of the thermo e.m.f. with the temperature of hot junction, with the cold junction.',
  'وہ خاص درجۂ حرارت جس پر حرارتی برقی محرکہ قوت صفر ہو جاتی ہے، الٹاؤ درجۂ حرارت کہلاتا ہے؛ شکل 12.12 (b) دیکھیں۔ گراف سرد جوڑ کے ساتھ گرم جوڑ کے درجۂ حرارت کے مطابق حرارتی برقی محرکہ قوت کی تبدیلی دکھاتا ہے۔',
  'هغه ځانګړې تودوخه چې حرارتي محرکه قوه پکې صفر کېږي، د اوښتون تودوخه بلل کېږي؛ 12.12 (b) شکل وګورئ. ګراف د سړې پیوند په شتون کې د ګرم پیوند د تودوخې له مخې د حرارتي محرکې قوې بدلون ښيي.'),
]

def make(identity,title,printed,pairs,layout,titles,pages,visual=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':41,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[{'pdfPage':41,'printedPage':n,'sourcePdf':SOURCE} for n in pages]
 if visual:s.update(visual);s['content']+=visual['diagramSvg']
 return r,s
def apparatus(lang):
 L={'en':('Hot junction T₁','Cold junction T₂','Wire A: copper','Wire B: iron','millivolts','(a) Variation of thermo emf with temperature','FIGURE 12.12'),
    'ur':('گرم جوڑ T₁','سرد جوڑ T₂','تار A: تانبا','تار B: لوہا','ملی وولٹ','(الف) درجۂ حرارت کے ساتھ حرارتی برقی محرکہ قوت میں تبدیلی','شکل 12.12'),
    'ps':('ګرم پیوند T₁','سړه پیوند T₂','A سیم: مس','B سیم: اوسپنه','ملي‌ولټ','(الف) له تودوخې سره د حرارتي محرکې قوې بدلون','12.12 شکل')}[lang]
 b=('<path d="M85 92L170 65H275H390V165H275H170L85 112" fill="none" stroke="#b45309" stroke-width="4"/><path d="M85 112L170 145H275H390V165" fill="none" stroke="#2563eb" stroke-width="4"/><circle cx="85" cy="102" r="9" fill="#ef4444"/><circle cx="275" cy="65" r="7" fill="#475569"/><circle cx="275" cy="145" r="7" fill="#475569"/><rect x="380" y="82" width="100" height="96" rx="8" fill="#fff7ed" stroke="#b45309" stroke-width="3"/><path d="M395 144A35 35 0 0 1 465 144" fill="none" stroke="#334155" stroke-width="4"/><path d="M430 144l19-27" stroke="#dc2626" stroke-width="3"/><path d="M74 127C64 112 68 104 85 99C99 108 99 118 89 129Z" fill="#fb923c"/><path d="M74 130h20v28H74z" fill="#38bdf8"/>')
 for x,y,t in [(15,84,L[0]),(180,36,L[1]),(170,88,L[2]),(170,178,L[3]),(390,72,L[4]),(12,218,L[5]),(390,22,L[6])]: b+=f'<text x="{x}" y="{y}" font-size="12">{escape(t)}</text>'
 return svg(b,L[6])
def graph(lang):
 L={'en':('Thermo emf','Temperature T','Neutral temperature','(b) Variation for copper-iron thermocouple','FIGURE 12.12'),
    'ur':('حرارتی برقی محرکہ قوت','درجۂ حرارت T','غیر جانب دار درجۂ حرارت','(ب) تانبے-لوہے کے تھرموکپل کے لیے تبدیلی','شکل 12.12'),
    'ps':('حرارتي محرکه قوه','تودوخه T','بې‌طرفه تودوخه','(ب) د مسو-اوسپنې ترموکوپل بدلون','12.12 شکل')}[lang]
 b=('<path d="M85 190V42M85 190H470" fill="none" stroke="#334155" stroke-width="3"/><path d="M88 187C130 112 175 57 235 57C300 58 350 116 425 187" fill="none" stroke="#b91c1c" stroke-width="3"/><path d="M235 58H85M235 58V190" stroke="#94a3b8" stroke-dasharray="5 4" stroke-width="2"/><path d="M80 48l5-10 5 10M464 185l10 5-10 5" fill="#334155"/><text x="35" y="36" font-size="12">'+L[0]+'</text><text x="430" y="218" font-size="12">'+L[1]+'</text><text x="240" y="210" font-size="11">Tₙ</text><text x="35" y="229" font-size="11">'+L[2]+'</text><text x="170" y="24" font-size="12">'+L[3]+'</text><text x="395" y="24" font-size="13">'+L[4]+'</text>')
 return svg(b,L[4])

if __name__=='__main__':
 t=make('phys12-unit12-thermocouples72-73','12.11 Thermocouples and temperature dependence',72,THERMO,[
  {'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'visual'},
  {'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},
  {'type':'paragraph','indices':[5]},{'type':'paragraph','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'equation','indices':[8]},{'type':'paragraph','indices':[9]}],
  ('12.11 تھرموکپلز اور درجۂ حرارت پر انحصار','12.11 ترموکوپلونه او پر تودوخې تړاو'),[72,73],
  {'diagramSvg':apparatus('en'),'diagramSvgUrdu':apparatus('ur'),'diagramSvgPashto':apparatus('ps')})
 v=make('phys12-unit12-thermoelectric-variation73','12.12 Variation in thermoelectric emf with temperature',73,VARIATION,[
  {'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'paragraph','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'visual'}],
  ('12.12 درجۂ حرارت کے ساتھ حرارتی برقی محرکہ قوت میں تبدیلی','12.12 له تودوخې سره د حرارتي برېښنايي محرکې قوې بدلون'),[73],
  {'diagramSvg':graph('en'),'diagramSvgUrdu':graph('ur'),'diagramSvgPashto':graph('ps')})
 records=[t[0],v[0]];sections=[t[1],v[1]]
 upsert(records,sections,chapter_index=1)
 sync_companions(chapter_index=1,retire_sections=['12.7'],
  trim_sections=[{'id':'12.8','startsAt':'Resistance thermometers','title':'Resistance thermometers — continuation pending source review'}],
  formulas=[{'id':'phys12-unit12-eq-12.16','name':'Thermoelectric emf versus temperature','number':'12.16','formula':THERMO[8][0],'latex':r'\epsilon=\alpha T+\frac{1}{2}\beta T^2','sourceReferences':[{'pdfPage':41,'printedPage':73,'sourcePdf':SOURCE}]}],
  definitions=[{'term':'Thermocouple','definition':THERMO[1][0]+' '+THERMO[2][0]+' '+THERMO[3][0],
   'definitionUrdu':THERMO[1][1]+' '+THERMO[2][1]+' '+THERMO[3][1],'definitionPashto':THERMO[1][2]+' '+THERMO[2][2]+' '+THERMO[3][2],
   'sourceReferences':[{'pdfPage':41,'printedPage':72,'sourcePdf':SOURCE}]}])
 checkpoint(41,'corrected_verified',[r['id'] for r in records], 'Rendered and visually inspected PDF page 41, printed pages 72–73. Compared the thermocouple construction and Seebeck description, metal-pair examples, use and reversibility, Figure 12.12(a), Eq. 12.16 and coefficient statement, neutral/inversion-temperature explanation and Figure 12.12(b). Rebuilt both figures as translated SVG, paired all source paragraphs in English/Urdu/Pashto, synchronized the formula/definition, retired the covered thermocouple fragment and trimmed the next legacy record at the first unchecked Resistance thermometers heading.',printed_pages=[72,73],chapter_number=12)
