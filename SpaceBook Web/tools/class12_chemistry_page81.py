"""PDF81 printed154–155: reactivity effects, Table 16.5 orientation/reactivity, making polysubstituted benzenes."""
from class12_chemistry_opening import pair,section,SOURCE
from class12_chemistry_sync import save
from class12_chemistry_rings import Fig
F=Fig('arrow81');t=F.t;line=F.line;ring=F.ring
paras=[];layout=[];blocks=[]
def add(e,u,p,kind='paragraph'):
 layout.append({'type':kind,'indices':[len(paras)]});paras.append(pair(e,u,p))
def visual(identity,fn):
 blocks.append({'id':identity,'svg':fn('en'),'svgUrdu':fn('ur'),'svgPashto':fn('ps')});layout.append({'type':'visual','blockId':identity})
N={'benzene':('بینزین','بنزین'),'bromobenzene':('برومو بینزین','بروموبنزین'),'o-bromonitrobenzene':('o-برومو نائٹرو بینزین','o-برومونایټروبنزین'),'p-bromonitrobenzene':('p-برومو نائٹرو بینزین','p-برومونایټروبنزین'),
   'nitrobenzene':('نائٹرو بینزین','نایټروبنزین'),'m-bromonitrobenzene':('m-برومو نائٹرو بینزین','m-برومونایټروبنزین'),'phenol':('فینول','فینول'),
   '2,4,6-trinitrophenol (picric acid)':('2،4،6-ٹرائی نائٹرو فینول (پکرک ایسڈ)','2،4،6-ټرای نایټروفینول (پکریک اسید)'),'conc. HNO₃':('مرتکز HNO₃','غلیظ HNO₃')}
def lb(lang,v):return v if lang=='en' else N[v][0 if lang=='ur' else 1]
def reag(x1,x2,y,lines):
 s=line(x1,y,x2,y,2,'#222','marker-end="url(#arrow81)"')+t((x1+x2)/2,y-9,lines[0],12)
 for i,l in enumerate(lines[1:]):s+=t((x1+x2)/2,y+17+14*i,l,12)
 return s
def brom_first(lang):
 s=F.start(190)+ring(70,80,26)+t(70,135,lb(lang,'benzene'),12)+reag(105,195,80,['Br₂','FeBr₃','−HBr'])
 s+=ring(240,80,26,subs={0:'Br'})+t(240,135,lb(lang,'bromobenzene'),12)+reag(285,375,80,['HNO₃','H₂SO₄','−H₂O'])
 s+=ring(450,80,26,subs={0:'Br',1:'NO₂'})+t(450,135,lb(lang,'o-bromonitrobenzene'),12)+t(560,86,'+',20)+ring(650,80,26,subs={0:'Br',3:'NO₂'})+t(650,158,lb(lang,'p-bromonitrobenzene'),12)
 return s+'</svg>'
def nitro_first(lang):
 s=F.start(160)+ring(100,85,26)+t(100,140,lb(lang,'benzene'),12)+reag(140,280,85,['HNO₃','H₂SO₄, 60°C','−H₂O'])
 s+=ring(340,85,26,subs={0:'NO₂'})+t(340,140,lb(lang,'nitrobenzene'),12)+reag(385,520,85,['Br₂','FeBr₃','−HBr'])
 s+=ring(600,85,26,subs={0:'Br',2:'NO₂'})+t(600,140,lb(lang,'m-bromonitrobenzene'),12)
 return s+'</svg>'
def picric(lang):
 s=F.start(170)+ring(150,80,28,subs={0:'OH'})+t(150,135,lb(lang,'phenol'),12)+F.arrow(230,370,80,lb(lang,'conc. HNO₃'),'25°C')
 s+=ring(470,80,28,subs={0:'OH',1:'NO₂',3:'NO₂',5:'O₂N'})+t(470,158,lb(lang,'2,4,6-trinitrophenol (picric acid)'),12)+t(620,87,'+ 3H₂O',18)
 return s+'</svg>'

add('Self-assessmnet','خود جانچ','ځان ارزونه','heading')
add('Draw the possible resonance structures for chlorobenzene and benzaldehyde.','کلورو بینزین اور بینز الڈیہائیڈ کی ممکنہ ریزونینس ساختیں بنائیں۔','د کلوروبنزین او بنزالدیهاید ممکنه ریزونانس جوړښتونه رسم کړئ.')
add('(B) Effect of Substituent on the Reactivity of the Benzene Ring','(B) بینزین حلقے کی تعامل پذیری پر متبادل کا اثر','(B) د بنزین د کړۍ پر تعامل وړتیا د بدیل اغېز','heading')
add('The substituent attached to the benzene ring also affects the reactivity of benzene ring in comparison with the unsubstituted benzene, this is called reactivity effect. Reactivity effect may be ring activating or deactivating.',
 'بینزین حلقے سے جڑا متبادل غیر متبادل بینزین کے مقابلے میں بینزین حلقے کی تعامل پذیری پر بھی اثر ڈالتا ہے، اسے تعامل پذیری کا اثر کہتے ہیں۔ تعامل پذیری کا اثر حلقے کو فعال کرنے والا یا غیر فعال کرنے والا ہو سکتا ہے۔',
 'له بنزیني کړۍ سره تړلی بدیل د بې بدیله بنزین په پرتله د بنزیني کړۍ پر تعامل وړتیا هم اغېز کوي، دې ته د تعامل وړتیا اغېز وايي. د تعامل وړتیا اغېز کېدای شي کړۍ فعالوونکی یا غیر فعالوونکی وي.')
add('i. Ring activating effect','i. حلقہ فعال کرنے کا اثر','i. د کړۍ فعالوونکی اغېز','heading')
add('The ortho/para directing groups release electrons to the ring by resonance making it electron rich. Thus, the attack of a second electrophile would be faster as compared to the benzene ring itself. Thus, the ortho/para directing species increase the reactivity of the benzene ring. They are ring activators and are referred to as activating groups. Halogens are the exceptions to this. It has been observed that halogens, though are ortho/para directing, are ring deactivators.',
 'اورتھو/پیرا سمت دینے والے گروپ ریزونینس کے ذریعے حلقے کو الیکٹران دے کر اسے الیکٹرانوں سے بھرپور بناتے ہیں۔ اس طرح دوسرے الیکٹروفائل کا حملہ خود بینزین حلقے کی نسبت تیز ہوتا ہے۔ یوں اورتھو/پیرا سمت دینے والی انواع بینزین حلقے کی تعامل پذیری بڑھاتی ہیں۔ یہ حلقہ فعال کرنے والے ہیں اور فعال کرنے والے گروپ کہلاتے ہیں۔ ہیلوجنز اس سے مستثنیٰ ہیں۔ دیکھا گیا ہے کہ ہیلوجنز اگرچہ اورتھو/پیرا سمت دینے والے ہیں، حلقہ غیر فعال کرنے والے ہیں۔',
 'اورتو/پارا لارښوونکي ګروپونه د ریزونانس له لارې کړۍ ته الکترونونه ورکوي او له الکترونونو یې ډکوي. نو د دویم الکتروفایل برید د پخپله بنزیني کړۍ په پرتله چټک وي. په دې ډول اورتو/پارا لارښوونکي ډولونه د بنزیني کړۍ تعامل وړتیا زیاتوي. دوی کړۍ فعالوونکي دي او فعالوونکي ګروپونه بلل کېږي. هالوجنونه له دې مستثنا دي. لیدل شوي چې هالوجنونه که څه هم اورتو/پارا لارښوونکي دي، د کړۍ غیر فعالوونکي دي.')
add('For example, the nitration of benzene (Section 16.8.5.2.2) requires concentrated nitric acid and sulfuric acid at 60°C, while nitration of phenol can easily occur with dilute nitric acid at 25°C as discussed earlier in this section. This is due to activating effect of –OH group.',
 'مثلاً بینزین کی نائٹریشن (حصہ 16.8.5.2.2) کے لیے 60°C پر مرتکز نائٹرک ایسڈ اور سلفیورک ایسڈ درکار ہیں، جبکہ فینول کی نائٹریشن 25°C پر ہلکے نائٹرک ایسڈ سے آسانی سے ہو سکتی ہے، جیسا کہ اس حصے میں پہلے بیان ہوا۔ یہ –OH گروپ کے فعال کرنے والے اثر کی وجہ سے ہے۔',
 'د بېلګې په توګه د بنزین نایټرېشن (برخه 16.8.5.2.2) په 60°C کې غلیظ نایټریک اسید او سلفوریک اسید غواړي، خو د فینول نایټرېشن په 25°C کې له رقیق نایټریک اسید سره په اسانۍ کېدای شي، لکه څنګه چې مخکې په دې برخه کې بحث شو. دا د –OH ګروپ د فعالوونکي اغېز له امله ده.')
add('ii. Ring deactivating effect','ii. حلقہ غیر فعال کرنے کا اثر','ii. د کړۍ غیر فعالوونکی اغېز','heading')
add('All meta directing groups and halogens (F, Cl, Br, I) withdraw electrons from the ring making it electron deficient. Thus in the presence of meta directing species, the attack of a second electrophile would be slower as compared to the benzene ring. Hence, these groups are ring deactivators.',
 'تمام میٹا سمت دینے والے گروپ اور ہیلوجنز (F، Cl، Br، I) حلقے سے الیکٹران کھینچ کر اسے الیکٹرانوں کی کمی والا بنا دیتے ہیں۔ اس طرح میٹا سمت دینے والی انواع کی موجودگی میں دوسرے الیکٹروفائل کا حملہ بینزین حلقے کی نسبت سست ہوتا ہے۔ لہٰذا یہ گروپ حلقہ غیر فعال کرنے والے ہیں۔',
 'ټول میټا لارښوونکي ګروپونه او هالوجنونه (F، Cl، Br، I) له کړۍ الکترونونه راکاږي او د الکترونونو کمښت پکې راولي. نو د میټا لارښوونکو ډولونو په شتون کې د دویم الکتروفایل برید د بنزیني کړۍ په پرتله ورو وي. له همدې امله دا ګروپونه د کړۍ غیر فعالوونکي دي.')
add('For example, the nitration of benzene (Section 16.8.5.2.2) requires concentrated nitric acid and sulfuric acid at 60°C, while nitration of nitrobenzene can be even slower with concentrated nitric acid and sulfuric acid at 100°C as discussed earlier in this section. This is due to deactivating effect of –NO₂ group.',
 'مثلاً بینزین کی نائٹریشن (حصہ 16.8.5.2.2) کے لیے 60°C پر مرتکز نائٹرک ایسڈ اور سلفیورک ایسڈ درکار ہیں، جبکہ نائٹرو بینزین کی نائٹریشن 100°C پر مرتکز نائٹرک ایسڈ اور سلفیورک ایسڈ کے ساتھ بھی زیادہ سست ہو سکتی ہے، جیسا کہ اس حصے میں پہلے بیان ہوا۔ یہ –NO₂ گروپ کے غیر فعال کرنے والے اثر کی وجہ سے ہے۔',
 'د بېلګې په توګه د بنزین نایټرېشن (برخه 16.8.5.2.2) په 60°C کې غلیظ نایټریک اسید او سلفوریک اسید غواړي، خو د نایټروبنزین نایټرېشن په 100°C کې له غلیظ نایټریک اسید او سلفوریک اسید سره هم لا ورو کېدای شي، لکه څنګه چې مخکې په دې برخه کې بحث شو. دا د –NO₂ ګروپ د غیر فعالوونکي اغېز له امله ده.')
tb={'id':'chem12-table16-5-orientation','headers':['Effect','Groups','Directing'],
 'rows':[['Activators — Strong','–OH, –NH₂, –NHR, –NR₂','ortho/para directors'],['Activators — Moderate','–OCOR, –NHCOR, –NRCOR','ortho/para directors'],['Activators — Weak','R–','ortho/para directors'],
         ['Deactivators — Weak','–X (F, Cl, Br, I)','ortho/para directors'],['Deactivators — Moderate','–CHO, –COR, –COOH, –CONH₂, –COOR','meta directors'],['Deactivators — Strong','–NO₂, –⁺NH₃, –⁺NR₃','meta directors']],
 'translations':[{'language':'اردو','headers':['اثر','گروپ','سمت'],'rows':[['فعال کرنے والے — طاقتور','–OH، –NH₂، –NHR، –NR₂','اورتھو/پیرا سمت دینے والے'],['فعال کرنے والے — درمیانے','–OCOR، –NHCOR، –NRCOR','اورتھو/پیرا سمت دینے والے'],['فعال کرنے والے — کمزور','R–','اورتھو/پیرا سمت دینے والے'],['غیر فعال کرنے والے — کمزور','–X (F، Cl، Br، I)','اورتھو/پیرا سمت دینے والے'],['غیر فعال کرنے والے — درمیانے','–CHO، –COR، –COOH، –CONH₂، –COOR','میٹا سمت دینے والے'],['غیر فعال کرنے والے — طاقتور','–NO₂، –⁺NH₃، –⁺NR₃','میٹا سمت دینے والے']]},
                 {'language':'پښتو','headers':['اغېز','ګروپونه','لوری'],'rows':[['فعالوونکي — قوي','–OH، –NH₂، –NHR، –NR₂','اورتو/پارا لارښوونکي'],['فعالوونکي — منځني','–OCOR، –NHCOR، –NRCOR','اورتو/پارا لارښوونکي'],['فعالوونکي — کمزوري','R–','اورتو/پارا لارښوونکي'],['غیر فعالوونکي — کمزوري','–X (F، Cl، Br، I)','اورتو/پارا لارښوونکي'],['غیر فعالوونکي — منځني','–CHO، –COR، –COOH، –CONH₂، –COOR','میټا لارښوونکي'],['غیر فعالوونکي — قوي','–NO₂، –⁺NH₃، –⁺NR₃','میټا لارښوونکي']]}]}
add('Table 16.5 Orientation and Reactivity Effect of Some Common Groups','جدول 16.5 بعض عام گروپوں کا سمت دینے اور تعامل پذیری کا اثر','جدول 16.5 د ځینو عامو ګروپونو د لوري ورکولو او تعامل وړتیا اغېز')
blocks.append(tb);layout.append({'type':'sourceDataTable','tableId':tb['id']})
add('16.8.5.2.8 Making Polysubstituted Benzenes','16.8.5.2.8 کثیر متبادل بینزینز کی تیاری','16.8.5.2.8 د څو بدیلي بنزینونو جوړول','heading')
add('Polysubstituted benzenes are the derivatives of benzene in which two or more hydrogen atoms have been substituted by other atoms or group of atoms. We have to keep in mind the activating and directing effect of first substituents on the ring while planning the synthesis of a polysubstituted benzene derivative.',
 'کثیر متبادل بینزینز بینزین کے وہ مشتقات ہیں جن میں دو یا زیادہ ہائیڈروجن ایٹم دوسرے ایٹموں یا ایٹموں کے گروپوں سے بدل دیے گئے ہوں۔ کثیر متبادل بینزین مشتق کی تیاری کی منصوبہ بندی کرتے وقت ہمیں حلقے پر پہلے متبادلات کے فعال کرنے اور سمت دینے کے اثر کو ذہن میں رکھنا ہوتا ہے۔',
 'څو بدیلي بنزینونه د بنزین هغه مشتقات دي چې پکې دوه یا ډېر هایدروجني اټومونه په نورو اټومونو یا د اټومونو په ګروپونو بدل شوي وي. د څو بدیلي بنزیني مشتق د جوړولو د پلان پر مهال باید پر کړۍ د لومړیو بدیلونو فعالوونکی او لارښوونکی اغېز په پام کې ونیسو.')
add('For example, the synthesis of bromonitrobenzene from benzene require the introduction of –NO₂ and –Br groups in two consecutive electrophilic substitution reactions i.e. nitration and bromination. Either of the two substituents can be introduced into the benzene ring first and then the other. If benzene is first brominated and then nitrated, we will get mainly a mixture of o- and p-bromonitrobenzene because bromo group is ortho/para orienting.',
 'مثلاً بینزین سے برومو نائٹرو بینزین کی تیاری کے لیے دو مسلسل الیکٹروفائلی تبادلے کے تعاملات، یعنی نائٹریشن اور برومینیشن، کے ذریعے –NO₂ اور –Br گروپ داخل کرنے ہوتے ہیں۔ دونوں میں سے کوئی بھی متبادل پہلے بینزین حلقے میں داخل کیا جا سکتا ہے اور پھر دوسرا۔ اگر بینزین کی پہلے برومینیشن اور پھر نائٹریشن کی جائے تو ہمیں زیادہ تر o- اور p-برومو نائٹرو بینزین کا آمیزہ ملے گا کیونکہ برومو گروپ اورتھو/پیرا سمت دینے والا ہے۔',
 'د بېلګې په توګه له بنزین څخه د برومونایټروبنزین جوړول په دوو پرله پسې الکتروفایلي بدلون تعاملونو، یعنې نایټرېشن او برومینېشن، کې د –NO₂ او –Br ګروپونو ورننویستل غواړي. د دواړو بدیلونو هر یو کولی شي لومړی بنزیني کړۍ ته ورننوځي او بیا بل. که بنزین لومړی برومین او بیا نایټرېټ شي، ډېری به د o- او p-برومونایټروبنزین ګډوله ترلاسه کړو ځکه چې برومو ګروپ اورتو/پارا لارښوونکی دی.')
visual('chem12-p81-bromination-first',brom_first)
add('However, if we want to prepare m-bromonitrobenzene, we shall carry out the nitration first and then bromination, because the nitro group is meta orienting.',
 'تاہم اگر ہم m-برومو نائٹرو بینزین تیار کرنا چاہیں تو پہلے نائٹریشن اور پھر برومینیشن کریں گے، کیونکہ نائٹرو گروپ میٹا سمت دینے والا ہے۔',
 'خو که وغواړو m-برومونایټروبنزین جوړ کړو، لومړی به نایټرېشن او بیا برومینېشن ترسره کړو، ځکه چې نایټرو ګروپ میټا لارښوونکی دی.')
visual('chem12-p81-nitration-first',nitro_first)
add('Similarly, if we plan to synthesize nitro derivatives of phenol, we must do it by nitration of phenol. Nitration of phenol can be carried out by using dilute or concentrated nitric acid. Nitration with dilute nitric acid gives mainly ortho and para mono-nitrophenols (Section 16.8.5.2.7), but if we are using concentrated nitric acid, reaction cannot be stopped at mono-nitration stage and we get 2,4,6-trinitrophenol.',
 'اسی طرح اگر ہم فینول کے نائٹرو مشتقات تیار کرنا چاہیں تو یہ فینول کی نائٹریشن سے کرنا ہو گا۔ فینول کی نائٹریشن ہلکے یا مرتکز نائٹرک ایسڈ سے کی جا سکتی ہے۔ ہلکے نائٹرک ایسڈ سے نائٹریشن زیادہ تر اورتھو اور پیرا یک نائٹرو فینولز دیتی ہے (حصہ 16.8.5.2.7)، لیکن مرتکز نائٹرک ایسڈ استعمال کرنے پر تعامل یک نائٹریشن کے مرحلے پر نہیں رکتا اور ہمیں 2،4،6-ٹرائی نائٹرو فینول ملتا ہے۔',
 'همدارنګه که د فینول د نایټرو مشتقاتو د جوړولو پلان ولرو، باید د فینول د نایټرېشن له لارې یې وکړو. د فینول نایټرېشن د رقیق یا غلیظ نایټریک اسید په کارولو ترسره کېدای شي. له رقیق نایټریک اسید سره نایټرېشن ډېری اورتو او پارا یو نایټروفینولونه ورکوي (برخه 16.8.5.2.7)، خو که غلیظ نایټریک اسید وکاروو، تعامل د یو نایټرېشن په پړاو کې نه درېږي او 2،4،6-ټرای نایټروفینول ترلاسه کوو.')
visual('chem12-p81-picric-acid',picric)

record=section('16.28','Reactivity effects, Table 16.5 and making polysubstituted benzenes','تعامل پذیری کے اثرات، جدول 16.5 اور کثیر متبادل بینزینز کی تیاری','د تعامل وړتیا اغېزې، جدول 16.5 او د څو بدیلي بنزینونو جوړول',paras,layout,blocks,'154–155')
record['sourceReferences']=[{'sourcePdf':SOURCE,'pdfPage':81,'printedPages':[154,155]}]
record['sourceContinuesOnPdfPage']=82
issues=[{'id':'chem12-p154-table-layout','printedPage':154,'description':'Printed Table 16.5 uses merged Activators/Deactivators bands and merged ortho/para (Strong activator → Weak deactivator) and meta (Moderate/Strong deactivator) cells; flattened to one row per strength with the merged value repeated.'}]
carry=[{'from':'16.28','to':'16.29','startsAt':'Society. Technology And Science'}]
if __name__=='__main__':save(81,[record],carry=carry,issues=issues,chapter_number=16)
