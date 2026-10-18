"""PDF79 printed150–151: xylenes by alkylation, Friedel-Crafts acylation, substituent effects (introduction)."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow79');t=F.t;line=F.line
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'toluene':('ٹولوئین','تولوین'),'o-xylene (54%)':('o-زائلین (54%)','o-زایلین (54%)'),'m-xylene(17%)':('m-زائلین (17%)','m-زایلین (17%)'),'p-xylene (29%)':('p-زائلین (29%)','p-زایلین (29%)'),
   'methyl cation':('میتھائل کیٹائن','میتایل کاټیون'),'(Electrophile)':('(الیکٹروفائل)','(الکتروفایل)'),'benzene':('بینزین','بنزین'),'acetyl chloride':('ایسیٹائل کلورائیڈ','اسیټیل کلوراید'),
   'acetophenone':('ایسیٹو فینون','اسیټوفینون'),'p-methylacetophenone':('p-میتھائل ایسیٹو فینون','p-میتایل اسیټوفینون'),'acetyl cation':('ایسیٹائل کیٹائن','اسیټیل کاټیون'),
   'Monosubstituted product':('یک متبادل پیداوار','یو بدیلي محصول'),'ortho (40%)':('اورتھو (40%)','اورتو (40%)'),'meta (40%)':('میٹا (40%)','میټا (40%)'),'para (20%)':('پیرا (20%)','پارا (20%)')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
ring=F.ring
def xylenes(lang):
 s=F.start(200)+ring(70,95,28,subs={0:'CH₃'})+t(70,150,lb(lang,'toluene'),13)
 s+=line(115,95,215,95,2,'#222','marker-end="url(#arrow79)"')+t(165,85,'CH₃Cl',13)+t(165,112,'FeCl₃',13)+t(165,128,'−HCl',13)
 for k,(v,name) in enumerate(zip((1,2,3),('o-xylene (54%)','m-xylene(17%)','p-xylene (29%)'))):
  x=300+k*200;s+=ring(x,85,28,subs={0:'CH₃',v:'CH₃'})+t(x,172 if v==3 else 150,lb(lang,name),13)
  if k<2:s+=t(x+100,90,'+',20)
 return s+'</svg>'
def eqn(lang,left,right,labels):
 s=F.start(80)+t(220,35,left,18)+F.arrow(340,440,29)+t(600,35,right,18)
 for i,l in enumerate(labels):s+=t(580,55+i*16,lb(lang,l),13)
 return s+'</svg>'
def acetyl(x,y):return t(x,y-38,'O',15)+line(x-3,y-32,x-3,y-18)+line(x+3,y-32,x+3,y-18)+t(x,y,'H₃C — C — Cl',18)
def acylation(lang):
 s=F.start(150)+ring(130,80,28)+t(130,135,lb(lang,'benzene'),13)+t(200,87,'+',20)+acetyl(285,87)+t(285,112,lb(lang,'acetyl chloride'),13)
 s+=F.arrow(380,470,80,'AlCl₃')+ring(540,80,28,subs={1:'COCH₃'})+t(540,135,lb(lang,'acetophenone'),13)+t(690,87,'+ HCl',18)
 return s+'</svg>'
def toluacyl(lang):
 s=F.start(185)+ring(200,80,28,subs={0:'CH₃'})+t(200,135,lb(lang,'toluene'),13)
 s+=line(260,80,400,80,2,'#222','marker-end="url(#arrow79)"')+t(330,70,'CH₃COCl',13)+t(330,97,'FeCl₃',13)+t(330,113,'−HCl',13)
 s+=ring(480,80,28,subs={0:'CH₃',3:'COCH₃'})+t(480,175,lb(lang,'p-methylacetophenone'),13)
 return s+'</svg>'
def acylium(lang):
 s=F.start(100)+acetyl(170,60)+t(170,85,lb(lang,'acetyl chloride'),13)+t(275,60,'+',20)+F.arrow(300,400,54,'AlCl₃')
 s+=t(560,60,'H₃C — C⁺ = O  +  AlCl₄⁻',18)+t(520,80,lb(lang,'acetyl cation'),13)+t(520,96,lb(lang,'(Electrophile)'),13)
 return s.replace('viewBox="0 0 850 100"','viewBox="0 0 850 104"')+'</svg>'
def ortho(lang):
 s=F.start(200)+ring(60,80,26)+t(60,135,lb(lang,'benzene'),12)+F.arrow(95,150,80,'E₁⁺','−H⁺',12)
 s+=ring(195,80,26,subs={0:'E₁'})+t(195,135,lb(lang,'Monosubstituted product'),12)+F.arrow(240,300,80,'E₂⁺','−H⁺',12)
 for k,(v,name) in enumerate(zip((1,2,3),('ortho (40%)','meta (40%)','para (20%)'))):
  x=370+k*165;s+=ring(x,80,26,subs={0:'E₁',v:'E₂'})+t(x,165 if v==3 else 135,lb(lang,name),12)
  if k<2:s+=t(x+82,85,'+',18)
 return s+'</svg>'

visual('chem12-p79-xylenes',xylenes)
add('The electrophile in this reaction is a methyl cation (a carbocation) formed by reaction methyl chloride with aluminum chloride. The electrophile carbocation then attacks on benzene ring and forms substitution products.',
 'اس تعامل میں الیکٹروفائل میتھائل کیٹائن (ایک کاربوکیٹائن) ہے جو میتھائل کلورائیڈ کے ایلومینیم کلورائیڈ سے تعامل سے بنتا ہے۔ پھر الیکٹروفائل کاربوکیٹائن بینزین حلقے پر حملہ کرتا ہے اور تبادلے کی پیداواریں بناتا ہے۔',
 'په دې تعامل کې الکتروفایل میتایل کاټیون (یو کاربوکاټیون) دی چې د میتایل کلوراید له المونیم کلوراید سره له تعامل جوړېږي. بیا الکتروفایل کاربوکاټیون د بنزین پر کړۍ برید کوي او بدلون محصولات جوړوي.')
visual('chem12-p79-methyl-cation',lambda l:eqn(l,'CH₃Cl + AlCl₃','CH₃⁺ + AlCl₄⁻',['methyl cation','(Electrophile)']))
add('16.8.5.2.6 Fridel-Crafts Acylation','16.8.5.2.6 فریڈل-کرافٹس ایسائلیشن','16.8.5.2.6 فریډل-کرافټس اسایلېشن','heading')
add('Benzene reacts with acid halides (or anhydrides) in the presence of a Lewis acid catalyst to give aromatic ketones. For example, benzene reacts with acetyl chloride in the presence of aluminum chloride catalyst to form acetophenone.',
 'بینزین لیوس ایسڈ عمل انگیز کی موجودگی میں ایسڈ ہیلائیڈز (یا این ہائیڈرائیڈز) سے تعامل کر کے ارومیٹک کیٹونز دیتی ہے۔ مثلاً بینزین ایلومینیم کلورائیڈ عمل انگیز کی موجودگی میں ایسیٹائل کلورائیڈ سے تعامل کر کے ایسیٹو فینون بناتی ہے۔',
 'بنزین د لیوس اسید کتلست په شتون کې له اسید هالایډونو (یا انهایدرایډونو) سره تعامل کوي او اروماتیک کیټونونه ورکوي. د بېلګې په توګه بنزین د المونیم کلوراید کتلست په شتون کې له اسیټیل کلوراید سره تعامل کوي او اسیټوفینون جوړوي.')
visual('chem12-p79-acylation',acylation)
add('In acylation of toluene, virtually all the substitution occurs at 4-position (p-position). The reason that you get virtually none of the o-isomer in this instance is because of the size of the incoming acyl group is very large. For example, reaction of toluene with acetyl chloride in the presence of ferric chloride yield p-methylacetophenone.',
 'ٹولوئین کی ایسائلیشن میں تقریباً تمام تبادلہ 4-مقام (p-مقام) پر ہوتا ہے۔ اس صورت میں o-آئسومر تقریباً بالکل نہ ملنے کی وجہ یہ ہے کہ آنے والے ایسائل گروپ کا حجم بہت بڑا ہے۔ مثلاً فیرک کلورائیڈ کی موجودگی میں ٹولوئین کا ایسیٹائل کلورائیڈ سے تعامل p-میتھائل ایسیٹو فینون دیتا ہے۔',
 'د تولوین په اسایلېشن کې نږدې ټول بدلون په 4-موقعیت (p-موقعیت) کې کېږي. په دې حالت کې د o-ایزومر نږدې هېڅ نه ترلاسه کېدو لامل دا دی چې د راتلونکي اسایل ګروپ اندازه ډېره لویه ده. د بېلګې په توګه د فېریک کلوراید په شتون کې له اسیټیل کلوراید سره د تولوین تعامل p-میتایل اسیټوفینون ورکوي.')
visual('chem12-p79-toluene-acylation',toluacyl)
add('The electrophile in Friedel-Crafts acylation is a carbocation, generally called an acylium ion (RCO⁺). Acetyl cation (an acylium ion) is formed by reaction of acetyl chloride with aluminum chloride catalyst. The electrophile acylium ion attack on benzene ring and form aromatic ketone.',
 'فریڈل-کرافٹس ایسائلیشن میں الیکٹروفائل ایک کاربوکیٹائن ہے، جسے عموماً ایسائلیم آئن (RCO⁺) کہتے ہیں۔ ایسیٹائل کیٹائن (ایک ایسائلیم آئن) ایسیٹائل کلورائیڈ کے ایلومینیم کلورائیڈ عمل انگیز سے تعامل سے بنتا ہے۔ الیکٹروفائل ایسائلیم آئن بینزین حلقے پر حملہ کر کے ارومیٹک کیٹون بناتا ہے۔',
 'په فریډل-کرافټس اسایلېشن کې الکتروفایل یو کاربوکاټیون دی، چې عموماً اسایلیم ایون (RCO⁺) بلل کېږي. اسیټیل کاټیون (یو اسایلیم ایون) د اسیټیل کلوراید له المونیم کلوراید کتلست سره له تعامل جوړېږي. الکتروفایل اسایلیم ایون د بنزین پر کړۍ برید کوي او اروماتیک کیټون جوړوي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('Acylation can only be used to give aromatic ketones, but not aldehydes. This is because the formyl chloride (HCOCl) decomposes to CO and HCl under the reaction conditions.',
 'ایسائلیشن سے صرف ارومیٹک کیٹونز حاصل کیے جا سکتے ہیں، الڈیہائیڈز نہیں۔ اس کی وجہ یہ ہے کہ فارمائل کلورائیڈ (HCOCl) تعامل کی شرائط میں CO اور HCl میں تحلیل ہو جاتا ہے۔',
 'اسایلېشن یوازې د اروماتیکو کیټونونو د ترلاسه کولو لپاره کارېدای شي، نه د الدیهایډونو. دا ځکه چې فورمیل کلوراید (HCOCl) د تعامل په شرایطو کې په CO او HCl تجزیه کېږي.')
visual('chem12-p79-acylium',acylium)
add('16.8.5.2.7 Substituent Effects','16.8.5.2.7 متبادلات کے اثرات','16.8.5.2.7 د بدیلونو اغېزې','heading')
add('An electrophilic substitution reaction of benzene results only in the formation of one monosubstituted product because all hydrogen atoms of benzene ring are equivalent. However, second substituent can occupy any of the three remaining position to form three isomeric (ortho, meta and para) disubstituted products. It is expected that ortho, meta and para disubstituted products should be formed with ratio of 2:2:1, as given below.',
 'بینزین کا الیکٹروفائلی تبادلے کا تعامل صرف ایک یک متبادل پیداوار بناتا ہے کیونکہ بینزین حلقے کے تمام ہائیڈروجن ایٹم مساوی ہیں۔ تاہم دوسرا متبادل باقی تین میں سے کسی بھی جگہ پر آ کر تین ہم ترکیب (اورتھو، میٹا اور پیرا) دو متبادل پیداواریں بنا سکتا ہے۔ توقع کی جاتی ہے کہ اورتھو، میٹا اور پیرا دو متبادل پیداواریں 2:2:1 کے تناسب سے بنیں، جیسا کہ نیچے دیا گیا ہے۔',
 'د بنزین الکتروفایلي بدلون تعامل یوازې یو یو بدیلي محصول جوړوي ځکه چې د بنزین د کړۍ ټول هایدروجني اټومونه سره معادل دي. خو دویم بدیل کولی شي په پاتې دریو ځایونو کې په هر یوه کې ځای ونیسي او درې ایزومري (اورتو، میټا او پارا) دوه بدیلي محصولات جوړ کړي. تمه کېږي چې اورتو، میټا او پارا دوه بدیلي محصولات د 2:2:1 په تناسب جوړ شي، لکه څنګه چې لاندې ورکړل شوي.')
visual('chem12-p79-expected-ratio',ortho)
add('However, in actual practice the disubstituted products are not formed with the above expected percentages. This is because the first substituent (–E₁) effect the ring making the ortho, meta and para position non-equivalent for electrophilic attack. Similarly the first substituent may also increase or decrease the reactivity of ring for second substitution. These effects are called substitution effects.',
 'تاہم عملاً دو متبادل پیداواریں اوپر دی گئی متوقع فیصد کے مطابق نہیں بنتیں۔ اس کی وجہ یہ ہے کہ پہلا متبادل (–E₁) حلقے پر اثر ڈال کر اورتھو، میٹا اور پیرا مقامات کو الیکٹروفائلی حملے کے لیے غیر مساوی بنا دیتا ہے۔ اسی طرح پہلا متبادل دوسرے تبادلے کے لیے حلقے کی تعامل پذیری کو بڑھا یا گھٹا بھی سکتا ہے۔ ان اثرات کو تبادلے کے اثرات کہتے ہیں۔',
 'خو په عمل کې دوه بدیلي محصولات د پورته تمه شویو سلنو سره سم نه جوړېږي. دا ځکه چې لومړی بدیل (–E₁) پر کړۍ اغېز کوي او اورتو، میټا او پارا موقعیتونه د الکتروفایلي برید لپاره نامعادل کوي. همدارنګه لومړی بدیل کولی شي د دویم بدلون لپاره د کړۍ تعامل وړتیا زیاته یا کمه کړي. دې اغېزو ته د بدلون اغېزې وايي.')
add('Types of effects of Substituents','متبادلات کے اثرات کی اقسام','د بدیلونو د اغېزو ډولونه','heading')
add('Effect of a substituent already present on the benzene ring on further substitution can be divided into two categories i.e. Orientation Effect and Reactivity Effect.',
 'بینزین حلقے پر پہلے سے موجود متبادل کے مزید تبادلے پر اثر کو دو زمروں میں تقسیم کیا جا سکتا ہے، یعنی سمت دینے کا اثر اور تعامل پذیری کا اثر۔',
 'پر بنزیني کړۍ د مخکې شته بدیل اغېز پر نور بدلون په دوو ډلو وېشل کېدای شي، یعنې د لوري ورکولو اغېز او د تعامل وړتیا اغېز.')
add('(A) Directing or Orientation Effect','(A) رہنمائی یا سمت دینے کا اثر','(A) لارښوونکی یا د لوري ورکولو اغېز','heading')
add('The first substitutent may direct the incoming electrophile to ortho, meta or para position, depending on the nature of the first substituent. This is called the directing or orientation effect. It has been experimentally observed that some groups, when attached to the benzene ring, direct the second incoming substituent to either ortho and para positions or to the meta position. Thus, the substituents (groups) can be divided into two classes.',
 'پہلا متبادل اپنی نوعیت کے لحاظ سے آنے والے الیکٹروفائل کو اورتھو، میٹا یا پیرا مقام کی طرف بھیج سکتا ہے۔ اسے رہنمائی یا سمت دینے کا اثر کہتے ہیں۔ تجربات سے دیکھا گیا ہے کہ بعض گروپ بینزین حلقے سے جڑ کر دوسرے آنے والے متبادل کو یا تو اورتھو اور پیرا مقامات کی طرف یا میٹا مقام کی طرف بھیجتے ہیں۔ اس طرح متبادلات (گروپوں) کو دو جماعتوں میں تقسیم کیا جا سکتا ہے۔',
 'لومړی بدیل د خپل طبیعت پر بنسټ راتلونکی الکتروفایل اورتو، میټا یا پارا موقعیت ته لارښوونه کولی شي. دې ته لارښوونکی یا د لوري ورکولو اغېز وايي. په تجربو کې لیدل شوي چې ځینې ګروپونه کله چې له بنزیني کړۍ سره ونښلي، دویم راتلونکی بدیل یا اورتو او پارا موقعیتونو ته یا میټا موقعیت ته لېږي. نو بدیلونه (ګروپونه) په دوو ټولګیو وېشل کېدای شي.')

record=section('16.26','Xylenes, Friedel-Crafts acylation and substituent effects','زائلینز، فریڈل-کرافٹس ایسائلیشن اور متبادلات کے اثرات','زایلینونه، فریډل-کرافټس اسایلېشن او د بدیلونو اغېزې',paras,layout,blocks,'150–151')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':79,'printedPages':[150,151]}]
record['sourceContinuesOnPdfPage']=80
issues=[{'id':'chem12-p150-printed-spellings','printedPage':150,'description':'Printed "Fridel-Crafts", "substitutent" and "effect the ring" retained in English; xylene scheme printed with FeCl₃ (text says AlCl₃ for methyl chloride) — both retained.'}]
carry=[{'from':'16.26','to':'16.27','startsAt':'Ortho Para Directing substituents'}]
if __name__=='__main__':save(79,[record],carry=carry,issues=issues,chapter_number=16)
