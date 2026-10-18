"""PDF66, printed124–125: isolated builder; root integrates sequentially."""
import html
from class12_chemistry_opening import pair,section,SOURCE

paras,layout,blocks=[],[],[]


def add(e,u,p,kind='paragraph'):
    layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))


def text(x,y,value,size=20,fill='#17212b'):
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" fill="{fill}">{html.escape(value)}</text>'


def line(x1,y1,x2,y2,width=1.8,color='#17212b'):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'


def arrow(x,y,length=100,above='',below=''):
    out=line(x,y,x+length,y,1.8,'#ad294e')+f'<path d="M{x+length-8} {y-4}L{x+length} {y}L{x+length-8} {y+4}Z" fill="#ad294e"/>'
    if above:out+=text(x+length/2,y-12,above,17)
    if below:out+=text(x+length/2,y+26,below,17)
    return out


def svg(body,height):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" role="img"><g font-family="Arial,sans-serif">'+body+'</g></svg>'


def visual(identity,body,height,labels=None,equations=None):
    s=svg(body,height);b={'id':identity,'svg':s,'svgUrdu':s,'svgPashto':s}
    for f,n in [('svgUrdu',0),('svgPashto',1)]:
        for source,translation in (labels or {}).items():b[f]=b[f].replace('>'+html.escape(source)+'</text>','>'+html.escape(translation[n])+'</text>')
    if equations:b['sourceEquations']=equations
    blocks.append(b);layout.append({'type':'visual','blockId':identity})


add('Ozonides are highly unstable and explosive and cannot be isolated. Ozonides are decomposed using reducing agents like zinc dust, to form carbonyl compounds. For example, cleavage of ethylene ozonide with zinc, yield two molecules of formaldehyde.',
    'اوزونائیڈز نہایت غیر مستحکم اور دھماکا خیز ہیں اور انہیں الگ نہیں کیا جا سکتا۔ زنک کے برادے جیسے اختزالی عاملوں سے اوزونائیڈز کو توڑ کر کاربونائل مرکبات بنائے جاتے ہیں۔ مثلاً زنک کے ساتھ ایتھیلین اوزونائیڈ کو توڑنے سے فارملڈیہائیڈ کے دو سالمے حاصل ہوتے ہیں۔',
    'اوزونایډونه ډېر ناثابت او چاودېدونکي دي او نه شي جلا کېدای. اوزونایډونه د زنک د پوډر په څېر د احیا کوونکو عاملونو په کارولو تجزیه کېږي، څو کاربونیل مرکبات جوړ کړي. د بېلګې په توګه، په زنک د ایتیلین اوزونایډ ماتول د فارملډیهایډ دوه مالیکولونه ورکوي.')
names={'ethylene ozonide':('ایتھیلین اوزونائیڈ','ایتیلین اوزونایډ'),'formaldehyde':('فارملڈیہائیڈ','فارملډیهایډ'),
       'ethene':('ایتھین','ایتین'),'polyethene':('پولی ایتھین','پولي ایتین'),'(polyethylene)':('(پولی ایتھیلین)','(پولي ایتیلین)'),
       'n-butane':('نارمل بیوٹین','نارمل بیوټان'),'isobutane':('آئسوبیوٹین','ایزوبیوټان')}
body=text(170,37,'O',23)+text(118,90,'H₂C',23)+text(222,90,'CH₂',23)+text(125,147,'O',23)+text(215,147,'O',23)
body+=line(156,43,132,66)+line(185,43,211,66)+line(121,98,123,124)+line(219,98,217,124)+line(139,140,201,140)
body+='<path d="M111 39C190 66 186 112 132 169M229 39C152 66 156 112 208 169" fill="none" stroke="#444" stroke-width="1.5" stroke-dasharray="5 5"/>'
body+=text(173,196,'ethylene ozonide',19)+text(317,91,'+ Zn',23)+arrow(378,84,110,'H₂O','100°C')
body+=text(523,91,'2',23)+text(623,42,'O',24)+line(618,52,618,76)+line(626,52,626,76)+text(623,101,'C',24)
body+=line(609,107,575,128)+line(638,107,670,128)+text(562,139,'H',23)+text(683,139,'H',23)+text(623,196,'formaldehyde',19)+text(785,91,'+ ZnO',23)
visual('chem12-p124-ozonide-cleavage',body,228,names,['ethylene ozonide + Zn → 2HCHO + ZnO (H₂O,100°C)'])
add('This conversion process of an alkene using ozone to carbonyl compounds is called ozonolysis. This reaction can be used for locating the position of the double bond in an unknown alkene.',
    'اوزون استعمال کر کے کسی الکین کو کاربونائل مرکبات میں تبدیل کرنے کا یہ عمل اوزونولائسز کہلاتا ہے۔ اس تعامل کو کسی نامعلوم الکین میں دوہرے بند کی جگہ معلوم کرنے کے لیے استعمال کیا جا سکتا ہے۔',
    'د اوزون په کارولو د یوه الکین په کاربونیل مرکباتو د بدلولو دې پروسې ته اوزونولیز ویل کېږي. دا تعامل په یوه نامعلوم الکین کې د دوه ګوني تړون د موقعیت د موندلو لپاره کارېدلی شي.')
add('16.5.7.8 Polymerization','16.5.7.8 پولیمرائزیشن','16.5.7.8 پولیمریزه کېدل','heading')
add('Polymerization is a process in which small molecules (monomers) chemically join together to form large molecules (polymers). Simple alkenes when subjected to high temperature and pressure in the presence of a catalyst, form long chain addition polymers. Polymerization of alkenes is essentially the conversion of pi bonds to sigma bonds, which is a thermodynamically favorable process. For example ethene polymerizes to form polyethene in different ways. One approach involves relatively high pressure (2000 atm) and high temperature (200 °C) and the use of a free radical initiator catalyst such as peroxides.',
    'پولیمرائزیشن وہ عمل ہے جس میں چھوٹے سالمے (مونومرز) کیمیائی طور پر باہم مل کر بڑے سالمے (پولیمرز) بناتے ہیں۔ سادہ الکینز کو عمل انگیز کی موجودگی میں زیادہ درجہ حرارت اور دباؤ پر رکھا جائے تو وہ طویل زنجیر والے اضافی پولیمر بناتے ہیں۔ الکینز کی پولیمرائزیشن بنیادی طور پر پائی بندوں کی سگما بندوں میں تبدیلی ہے، جو حر حرکی طور پر موافق عمل ہے۔ مثلاً ایتھین مختلف طریقوں سے پولیمرائز ہو کر پولی ایتھین بناتی ہے۔ ایک طریقے میں نسبتاً زیادہ دباؤ (2000 atm)، زیادہ درجہ حرارت (200 °C) اور پیرو آکسائیڈز جیسے آزاد ریڈیکل آغاز کرنے والے عمل انگیز کا استعمال شامل ہے۔',
    'پولیمریزه کېدل هغه پروسه ده چې پکې واړه مالیکولونه (مونومرونه) په کیمیاوي ډول سره یوځای کېږي او لوی مالیکولونه (پولیمرونه) جوړوي. ساده الکینونه چې د کتلېست په شتون کې له لوړې تودوخې او فشار سره مخ شي، اوږده ځنځیر لرونکي اضافي پولیمرونه جوړوي. د الکینونو پولیمریزه کېدل په اصل کې د پای تړونونو په سیګما تړونونو بدلېدل دي، چې له ترمودینامیکي پلوه مساعده پروسه ده. د بېلګې په توګه ایتین په بېلابېلو لارو پولیمریزه کېږي او پولي ایتین جوړوي. په یوه لاره کې نسبتاً لوړ فشار (2000 atm)، لوړه تودوخه (200 °C) او د پیرو اکسایډونو په څېر د ازاد رادیکال پیلوونکي کتلېست کارول شامل دي.')
body=text(176,86,'nH₂C = CH₂',25)+text(176,156,'ethene',20)+arrow(333,80,140,'RO·; 200°C','2000 atm')
body+=text(597,87,'CH₂',25)+line(625,79,690,79)+text(722,87,'CH₂',25)+line(526,79,566,79)+line(751,79,795,79)
body+='<path d="M567 38H557V123H567M751 38H761V123H751" fill="none" stroke="#17212b" stroke-width="2"/>'
body+=text(778,132,'n',21)+text(660,164,'polyethene',20)+text(660,190,'(polyethylene)',20)
visual('chem12-p124-ethene-polymerization',body,218,names,['nH₂C=CH₂ → [–CH₂–CH₂–]ₙ (RO·;200°C;2000 atm)'])
add('Polyethylene is used as plastic material in the industries. It is used in the manufacture of shopping bags, sport nets, dustbins, water pipes, packing materials and cable insulation.',
    'پولی ایتھیلین صنعتوں میں پلاسٹک کے مادے کے طور پر استعمال ہوتی ہے۔ اسے خریداری کے تھیلے، کھیلوں کے جال، کوڑے دان، پانی کے پائپ، پیکنگ کے سامان اور تاروں کی برقی موصلیت بنانے میں استعمال کیا جاتا ہے۔',
    'پولي ایتیلین په صنعتونو کې د پلاستیکي مادې په توګه کارول کېږي. دا د پېرودلو کڅوړو، د سپورټ جالونو، کثافت دانیو، د اوبو پایپونو، د بسته بندۍ موادو او د کېبلونو د عایق په جوړولو کې کارول کېږي.')
add('16.6 Isomerism','16.6 آئسومرزم','16.6 ایزومېریزم','heading')
add('Many of the organic compounds have the same molecular formula but they are different from each other in their structure and properties. Such compounds are called isomers and this phenomenon is called isomerism.',
    'بہت سے نامیاتی مرکبات کا سالماتی فارمولا ایک ہی ہوتا ہے، مگر ان کی ساخت اور خصوصیات ایک دوسرے سے مختلف ہوتی ہیں۔ ایسے مرکبات آئسومر کہلاتے ہیں اور یہ مظہر آئسومرزم کہلاتا ہے۔',
    'ډېر عضوي مرکبات یو شان مالیکولي فورمول لري، خو په خپل جوړښت او ځانګړنو کې له یو بل سره توپیر لري. داسې مرکبات ایزومرونه بلل کېږي او دې پدیدې ته ایزومېریزم ویل کېږي.')
add('Tidbit','مختصر معلومات','لنډ معلومات','heading')
add('The prefix iso- is derived from Greek word isos, “the same”. The suffix –mer in the word “isomer” is derived from the Greek word meros, meaning “part”. Thus isomers are different molecules that have the same parts (elemental composition).',
    'سابقہ iso- یونانی لفظ isos سے اخذ کیا گیا ہے، جس کا مطلب ”ایک جیسا“ ہے۔ لفظ ”isomer“ میں لاحقہ –mer یونانی لفظ meros سے اخذ کیا گیا ہے، جس کا مطلب ”حصہ“ ہے۔ اس طرح آئسومر مختلف سالمے ہیں جن کے حصے (عنصری ترکیب) ایک جیسے ہوتے ہیں۔',
    'د iso- مختاړی له یوناني isos ټکي څخه اخیستل شوی چې «یو شان» معنا لري. په «isomer» ټکي کې د –mer وروستاړی له یوناني meros څخه اخیستل شوی چې «برخه» معنا لري. نو ایزومرونه بېلابېل مالیکولونه دي چې یو شان برخې (عنصري ترکیب) لري.')
add('There are two main types of isomerism i.e. Constitutional or Structural isomerism and Stereoisomerism. Each of these two main types of isomerism is further classified into different types as shown in Figure 16.5.',
    'آئسومرزم کی دو بنیادی اقسام ہیں، یعنی دستوری یا ساختی آئسومرزم اور اسٹیریو آئسومرزم۔ ان دونوں بنیادی اقسام کو مزید مختلف اقسام میں تقسیم کیا جاتا ہے، جیسا کہ شکل16.5 میں دکھایا گیا ہے۔',
    'د ایزومېریزم دوه اصلي ډولونه شته، یعنې کانسټیټیوشنل یا جوړښتي ایزومېریزم او سټیریوایزومېریزم. له دې دوو اصلي ډولونو څخه هر یو بیا په بېلابېلو ډولونو وېشل کېږي، لکه په شکل16.5 کې چې ښودل شوي.')


def classification(language):
    labels={
        'root':[['Isomerism'],['آئسومرزم'],['ایزومېریزم']],
        'constitution':[['Constitutional','isomerism'],['ساختی','آئسومرزم'],['جوړښتي','ایزومېریزم']],
        'stereo':[['Stereoisomerism'],['اسٹیریو آئسومرزم'],['سټیریوایزومېریزم']],
        'chain':[['Chain isomerism'],['زنجیری آئسومرزم'],['ځنځیري ایزومېریزم']],
        'position':[['Position isomerism'],['مقامی آئسومرزم'],['موقعیتي ایزومېریزم']],
        'functional':[['Functional group isomerism'],['فعلی گروپ کا آئسومرزم'],['د فعالي ګروپ ایزومېریزم']],
        'metamer':[['Metamerism'],['میٹامرزم'],['میټامېریزم']],
        'tautomer':[['Tautomerism'],['ٹاٹومرزم'],['ټاټومېریزم']],
        'conform':[['Conformational','isomerism'],['کنفارمیشنل','آئسومرزم'],['کنفورمېشنل','ایزومېریزم']],
        'config':[['Configurational','isomerism'],['کنفیگریشنل','آئسومرزم'],['کنفیګورېشنل','ایزومېریزم']],
        'geometry':[['Geometrical','isomerism'],['ہندسی','آئسومرزم'],['هندسي','ایزومېریزم']],
        'optical':[['Optical','isomerism'],['نوری','آئسومرزم'],['نوري','ایزومېریزم']],
    }
    body=''
    paths=['M149 230H183V139H215','M183 230V346H215','M371 139H410V39H450','M410 139V89H450','M410 139H450','M410 139V189H450','M410 139V239H450','M379 346H420V303H458','M420 346V389H458','M639 389H679V354H713','M679 389V439H713']
    for path in paths:body+=f'<path d="{path}" fill="none" stroke="#468b89" stroke-width="1.5"/>'
    for x,y in [(215,139),(215,346),(450,39),(450,89),(450,139),(450,189),(450,239),(458,303),(458,389),(713,354),(713,439)]:
        body+=f'<path d="M{x-7} {y-3}L{x} {y}L{x-7} {y+3}" fill="none" stroke="#468b89" stroke-width="1.5"/>'
    for key,x,y in [('root',84,236),('constitution',293,131),('stereo',295,352),('chain',585,45),('position',585,95),('functional',597,145),('metamer',585,195),('tautomer',585,245),('conform',548,295),('config',548,381),('geometry',803,346),('optical',803,431)]:
        for i,value in enumerate(labels[key][language]):body+=text(x,y+i*23,value,18)
    return svg(body,490)


blocks.append({'id':'chem12-figure16-5','svg':classification(0),'svgUrdu':classification(1),'svgPashto':classification(2)})
layout.append({'type':'visual','blockId':'chem12-figure16-5'})
add('Figure 16.5 Different types of isomerism.','شکل16.5 آئسومرزم کی مختلف اقسام۔','شکل16.5 د ایزومېریزم بېلابېل ډولونه.')
add('16.6.1 Constitutional isomerism','16.6.1 ساختی آئسومرزم','16.6.1 جوړښتي ایزومېریزم','heading')
add('In this type of isomerism, the isomers have the same molecular formula but different connectivity in structure. It is also called structural isomerism. Structural isomerism is of five types.',
    'آئسومرزم کی اس قسم میں آئسومروں کا سالماتی فارمولا ایک ہی ہوتا ہے، مگر ساخت میں ان کے ایٹموں کے باہمی اتصال مختلف ہوتے ہیں۔ اسے ساختی آئسومرزم بھی کہتے ہیں۔ ساختی آئسومرزم کی پانچ اقسام ہیں۔',
    'د ایزومېریزم په دې ډول کې ایزومرونه یو شان مالیکولي فورمول لري، خو په جوړښت کې یې د اټومونو نښلېدنه توپیر لري. دې ته جوړښتي ایزومېریزم هم ویل کېږي. جوړښتي ایزومېریزم پنځه ډولونه لري.')
add('16.6.1.1 Chain Isomerism or Skeletal Isomerism','16.6.1.1 زنجیری آئسومرزم یا ڈھانچے کا آئسومرزم','16.6.1.1 ځنځیري ایزومېریزم یا سکلیټي ایزومېریزم','heading')
add('Chain isomerism occurs when there is a difference in arrangement of the carbon atoms in main chain of a molecule. If two or more compounds having the same molecular formula with different carbon chains, then they are said to exhibit the property of Chain isomerism. This phenomenon is also called as skeletal isomerism. The number of possible chain isomers increases with number of carbon atoms. For example; butane has two isomers, pentane has three, hexane has five isomers and so on. The two chain isomers of butane (C₄H₁₀) are given below.',
    'زنجیری آئسومرزم اس وقت ہوتا ہے جب کسی سالمے کی مرکزی زنجیر میں کاربن ایٹموں کی ترتیب مختلف ہو۔ اگر دو یا زیادہ مرکبات کا سالماتی فارمولا ایک ہی ہو، مگر کاربن زنجیریں مختلف ہوں تو کہا جاتا ہے کہ وہ زنجیری آئسومرزم کی خاصیت دکھاتے ہیں۔ یہ مظہر ڈھانچے کا آئسومرزم بھی کہلاتا ہے۔ ممکنہ زنجیری آئسومروں کی تعداد کاربن ایٹموں کی تعداد کے ساتھ بڑھتی ہے۔ مثلاً بیوٹین کے دو آئسومر، پینٹین کے تین، ہیکسین کے پانچ آئسومر ہوتے ہیں، اور اسی طرح آگے۔ بیوٹین (C₄H₁₀) کے دو زنجیری آئسومر نیچے دیے گئے ہیں۔',
    'ځنځیري ایزومېریزم هغه وخت رامنځته کېږي چې د یوه مالیکول په اصلي ځنځیر کې د کاربني اټومونو په ترتیب کې توپیر وي. که دوه یا ډېر مرکبات یو شان مالیکولي فورمول خو بېلابېل کاربني ځنځیرونه ولري، ویل کېږي چې هغوی د ځنځیري ایزومېریزم ځانګړنه ښيي. دې پدیدې ته سکلیټي ایزومېریزم هم ویل کېږي. د ممکنه ځنځیري ایزومرونو شمېر د کاربني اټومونو له شمېر سره زیاتېږي. د بېلګې په توګه، بیوټان دوه ایزومرونه، پینټان درې، هېکسان پنځه ایزومرونه لري او داسې نور. د بیوټان (C₄H₁₀) دوه ځنځیري ایزومرونه لاندې ورکړل شوي دي.')
body=text(243,46,'CH₃ – CH₂ – CH₂ – CH₃',24)+text(243,119,'n-butane',20)
body+=text(663,46,'CH₃ – CH – CH₃',24)+line(663,55,663,78)+text(663,103,'CH₃',24)+text(663,147,'isobutane',20)
visual('chem12-p125-butane-chain-isomers',body,180,names)
add('16.6.1.2 Position Isomerism','16.6.1.2 مقامی آئسومرزم','16.6.1.2 موقعیتي ایزومېریزم','heading')
add('Position isomerism arises when there is a difference in the position of functional group. When the position of the functional groups with respect to main chain changes, the phenomenon is called as position isomerism. For example; position isomers of propyl alcohols and butylenes are given below.',
    'مقامی آئسومرزم اس وقت پیدا ہوتا ہے جب فعلی گروہ کی جگہ مختلف ہو۔ جب مرکزی زنجیر کے لحاظ سے فعلی گروہوں کی جگہ بدل جائے تو اس مظہر کو مقامی آئسومرزم کہتے ہیں۔ مثلاً پروپائل الکوحلوں اور بیوٹیلینز کے مقامی آئسومر نیچے دیے گئے ہیں۔',
    'موقعیتي ایزومېریزم هغه وخت رامنځته کېږي چې د فعالي ګروپ په موقعیت کې توپیر وي. کله چې د اصلي ځنځیر په نسبت د فعالي ګروپونو موقعیت بدل شي، دې پدیدې ته موقعیتي ایزومېریزم ویل کېږي. د بېلګې په توګه، د پروپیل الکولونو او بیوټیلینونو موقعیتي ایزومرونه لاندې ورکړل شوي دي.')

record=section('16.13','Ozonolysis, polymerization and types of isomerism',
               'اوزونولائسز، پولیمرائزیشن اور آئسومرزم کی اقسام','اوزونولیز، پولیمریزه کېدل او د ایزومېریزم ډولونه',paras,layout,blocks,'124–125')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':66,'printedPages':[124,125]}]
record['sourceChapterNumber']=16
record['sourceContinuesOnPdfPage']=67
issues=[{'id':'chem12-p124-ozonide-isolation','pdfPage':66,'printedPage':124,
         'description':'The source states categorically that ozonides cannot be isolated. Retained verbatim; scope of this statement needs scientific review.','status':'source_statement_retained_pending_review'}]

# Before replacing16.13, preserve PDF67+ legacy material by carry16.13→16.14
# starting at exact prefix "CH3-CH2-CH2-OH". No save() or shared writes here.

carry=[{'from':'16.13','to':'16.14','startsAt':'CH3-CH2-CH2-OH'}]
if __name__=='__main__':
    from class12_chemistry_sync import save
    save(66,[record],carry=carry,issues=issues,chapter_number=16)
