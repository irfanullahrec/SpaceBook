from chemlib import *
c=cell
def eqn(n,key,latex,text):
    return dict(id=f'chem11-p{n}-{key}',latex=latex,accessible=text,formatSourceNotation=True,nativeLines={l:[[dict(text=text)]] for l in ('en','ur','ps')})
class Flow:
    def __init__(s_,s): s_.s=s; s_.s['equations']=[]; s_.f=[]
    def p(s_,*keys):
        s_.f.append(dict(type='paragraphs',ids=[f"chem11-p{s_.s['source']['pdfPage']}-{k}" for k in keys]))
    def e(s_,key,latex,text):
        s_.s['equations'].append(eqn(s_.s['source']['pdfPage'],key,latex,text)); s_.f.append(dict(type='equation',index=len(s_.s['equations'])-1))
    def tb(s_,i): s_.f.append(dict(type='table',index=i))
    def done(s_): s_.s['flow']=s_.f
def mk(n,title,ur,ps,sid): return page(n,'chem11-solutions-colloids',title,ur,ps,sid)

# ---------- 309 ----------
s=mk(309,'Table 10.1 Solubility of different Substances at different Temperatures · 10.1.5 Solubility and Heat of Solution · Self-Assessment','جدول 10.1 مختلف درجہ حرارت پر مختلف مادوں کی حلالیت · 10.1.5 حلالیت اور محلول کی حرارت · خود جائزہ','جدول 10.1 په بېلابېلو تودوخو کې د بېلابېلو موادو حلالیت · 10.1.5 حلالیت او د محلول تودوخه · ځان ارزونه','table101-heat-of-solution')
F=Flow(s)
rows=[('KNO₃',['13.3','20.9','31.6','45.8','63.9','85.5']),('Al₂(SO₄)₃',['31.2','33.5','36.4','40.4','46.1','52.2']),('AgNO₃',['122','170','222','300','376','455']),('NaCl',['35.7','35.8','36.00','36.3','36.6','37.0']),('Ce₂(SO₄)₃',['20.75','','10.08','6.79','','[scan obscured]']),('Li₂CO₃',['1.54','1.43','1.33','1.25','1.117','[scan obscured]']),('Na₂SO₄',['5.0','9.0','19.4','40.8','48.8','44.7'])]
hdr=[c('Substance','مادہ','مواد')]+[c(f'{t}K') for t in (273,283,293,303,313,323)]
s['tables']=[table('Table: 10.1 Solubility of different Substances at different Temperatures (Solubility in grams per 100 grams of water)','جدول 10.1 مختلف درجہ حرارت پر مختلف مادوں کی حلالیت (100 گرام پانی میں گراموں میں حلالیت)','جدول 10.1 په بېلابېلو تودوخو کې د بېلابېلو موادو حلالیت (په 100 ګرامه اوبو کې په ګرامو حلالیت)',hdr,[[c(n)]+[c(v) for v in vals] for n,vals in rows])]
s['tables'][0]['sourceGap']=dict(note='The right-hand columns (313 K, 323 K) are clipped and skewed by the page curl; the 323 K values for Ce₂(SO₄)₃ and Li₂CO₃ cannot be read reliably and are marked [scan obscured]. The 283 K entry for Ce₂(SO₄)₃ and the 313 K entry for Ce₂(SO₄)₃ are blank/dash on the scan and are left empty. Values are paired by row in printed order.')
head(s,'h','10.1.5. Solubility and Heat of Solution','10.1.5 حلالیت اور محلول کی حرارت','10.1.5 حلالیت او د محلول تودوخه')
add(s,'a1',f'The change in solubility with temperature is closely related to the heat of{SO} solution of the substance. The heat of solution can be determined by noting the{SO} rise or fall of the temperature of the solution. If the temperature of the solution{SO} increases, the heat is evolved and therefore, heat of solution is negative and if the{SO} temperature decreases the heat of solution is positive. Thus, for silver nitrate the{SO} heat of solution is positive. Whereas for lithium carbonate, it is negative.',f'درجہ حرارت کے ساتھ حلالیت میں تبدیلی مادے کی محلول کی حرارت سے گہرا تعلق رکھتی ہے {SO}۔ محلول کی حرارت محلول کے درجہ حرارت کے بڑھنے یا گھٹنے کو نوٹ کر کے معلوم کی جا سکتی ہے {SO}۔ اگر محلول کا درجہ حرارت بڑھ جائے تو حرارت خارج ہوتی ہے اور اس لیے محلول کی حرارت منفی ہے اور اگر {SO} درجہ حرارت گھٹ جائے تو محلول کی حرارت مثبت ہے۔ اس طرح سلور نائٹریٹ کے لیے {SO} محلول کی حرارت مثبت ہے۔ جبکہ لیتھیم کاربونیٹ کے لیے یہ منفی ہے۔',f'د تودوخې سره په حلالیت کې بدلون د مادې د محلول له تودوخې سره نژدې اړوند دی {SO}. د محلول تودوخه د محلول د تودوخې د لوړېدو یا ټیټېدو په یادښت سره ټاکل کېدای شي {SO}. که د محلول تودوخه لوړه شي نو تودوخه خوشې کېږي او نو د محلول تودوخه منفي ده او که {SO} تودوخه ټیټه شي نو د محلول تودوخه مثبته ده. په دې توګه د سلور نایټریټ لپاره {SO} د محلول تودوخه مثبته ده. پداسې حال کې چې د لیتیم کاربونیټ لپاره دا منفي ده.')
add(s,'a2',f'When the heat of solution is positive, the solubility of a substance increases with the increase in temperature and decreases with the decrease in temperature. But if the heat of solution is negative, the solubility of a substance decreases with the increase in temperature and vice versa.','جب محلول کی حرارت مثبت ہو تو کسی مادے کی حلالیت درجہ حرارت بڑھنے کے ساتھ بڑھتی ہے اور درجہ حرارت گھٹنے کے ساتھ گھٹتی ہے۔ لیکن اگر محلول کی حرارت منفی ہو تو کسی مادے کی حلالیت درجہ حرارت بڑھنے کے ساتھ گھٹتی ہے اور اس کے برعکس۔','کله چې د محلول تودوخه مثبته وي نو د یوې مادې حلالیت د تودوخې په زیاتېدو سره زیاتېږي او د تودوخې په کمېدو سره کمېږي. خو که د محلول تودوخه منفي وي نو د یوې مادې حلالیت د تودوخې په زیاتېدو سره کمېږي او برعکس.')
add(s,'t-h','Tidbit','معلومات','ځانګړې یادونه',kind='heading')
add(s,'t1',f'Although mass is the quantity of matter in an object and weight is force with which the earth pulls the object towards it, however, since W=mg, and acceleration due to gravity is almost same everywhere on the Earth, therefore, most of the books use these two terms interchangeably i.e. the term weight is mostly used for mass.',f'اگرچہ کمیت کسی شے میں مادے کی مقدار ہے اور وزن وہ قوت ہے جس سے زمین شے کو اپنی طرف کھینچتی ہے، تاہم چونکہ W=mg ہے، اور زمین پر ہر جگہ تقریباً ایک ہی ثقلی اسراع ہوتا ہے، اس لیے زیادہ تر کتابیں ان دونوں اصطلاحات کو ایک دوسرے کی جگہ استعمال کرتی ہیں یعنی لفظ وزن زیادہ تر کمیت کے لیے استعمال ہوتا ہے۔',f'که څه هم کتله په یوه شي کې د مادې مقدار دی او وزن هغه ځواک دی چې ځمکه شی ځان ته ورکاږي، خو ځکه چې W=mg دی، او د ځمکې په هر ځای کې د جاذبې تعجیل نږدې یو شان دی، نو ډېری کتابونه دا دوه اصطلاحات یو د بل پر ځای کاروي یعنې د وزن اصطلاح ډېری د کتلې لپاره کارول کېږي.')
add(s,'sa','Self-Assessment','خود جائزہ','ځان ارزونه',kind='heading')
add(s,'sa1','1. Differentiate between solution, suspension and colloids.','1۔ محلول، معلق اور کولائیڈز میں فرق کریں۔','1. د محلول، معلق او کلوایډونو ترمنځ توپیر وکړئ.',role='question')
add(s,'sa2','2. Give example of each type of solutions of liquids in liquids.','2۔ مائعات کے مائعات میں محلولوں کی ہر قسم کی مثال دیں۔','2. د مایعاتو په مایعاتو کې د محلولونو د هر ډول بېلګه ورکړئ.',role='question')
add(s,'sa3','3. Explain the effect of temperature and pressure on solubility.','3۔ حلالیت پر درجہ حرارت اور دباؤ کے اثر کی وضاحت کریں۔','3. په حلالیت د تودوخې او فشار اغېز تشریح کړئ.',role='question')
F.tb(0)
F.p('h','a1')
F.e('r1',r'\mathrm{AgNO_3(s)+H_2O\longrightarrow Solution}\qquad\Delta H=\text{positive (endothermic)}','AgNO₃(s) + H₂O → Solution   ΔH = positive (endothermic)')
F.e('r2',r'\mathrm{Li_2CO_3(s)+H_2O\longrightarrow Solution}\qquad\Delta H=\text{negative (exothermic)}','Li₂CO₃(s) + H₂O → Solution   ΔH = negative (exothermic)')
F.p('a2','t-h','t1','sa','sa1','sa2','sa3')
F.done()
s['sourceNote']='Printed folio 304. The right edge is clipped by the page curl on the table (313 K and 323 K columns) and on the 10.1.5 paragraph; clipped endings are marked [scan obscured] and not inferred. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping on the table and first paragraph.')
s['vocabulary']={'heat of solution':{'ur':'محلول کی حرارت','ps':'د محلول تودوخه'},'endothermic':{'ur':'حرارت جذب کرنے والا','ps':'تودوخه جذبوونکی'},'exothermic':{'ur':'حرارت خارج کرنے والا','ps':'تودوخه خوشې کوونکی'}}
save(s)

# ---------- 310 ----------
s=mk(310,'10.2 Concentration Units · 10.2.1 Percentage Composition','10.2 ارتکاز کی اکائیاں · 10.2.1 فیصدی ترکیب','10.2 د غلظت واحدونه · 10.2.1 سلنه جوړښت','concentration-units')
F=Flow(s)
head(s,'h','10.2 Concentration Units','10.2 ارتکاز کی اکائیاں','10.2 د غلظت واحدونه')
add(s,'a1','The physical properties of solutions depend, to a large extent, upon the relative amounts of solute and solvent e.g. colour of a dye, the sweetness of a sugar solution or the saltish taste of common salt solution depends on the quantity of solute present. The amount of solute present in a given amount of solvent or solution is called concentration of a solution. Greater the amount of solute present in a solution the higher would be its concentration. The amount of solute, solvent and solution may be measured by volume, weight or number of moles. Accordingly, the concentration of a solution can be expressed in many ways.','محلولوں کی طبعی خصوصیات بڑی حد تک محلول شدہ شے اور محلل کی نسبتی مقداروں پر منحصر ہوتی ہیں مثلاً رنگ کا رنگ، چینی کے محلول کی مٹھاس یا عام نمک کے محلول کا نمکین ذائقہ موجود محلول شدہ شے کی مقدار پر منحصر ہوتا ہے۔ محلل یا محلول کی دی گئی مقدار میں موجود محلول شدہ شے کی مقدار محلول کا ارتکاز کہلاتی ہے۔ محلول میں موجود محلول شدہ شے کی مقدار جتنی زیادہ ہو اس کا ارتکاز اتنا ہی بلند ہوگا۔ محلول شدہ شے، محلل اور محلول کی مقدار حجم، وزن یا مولوں کی تعداد سے ناپی جا سکتی ہے۔ اسی کے مطابق محلول کا ارتکاز کئی طریقوں سے ظاہر کیا جا سکتا ہے۔','د محلولونو فزیکي ځانګړنې تر ډېرې اندازې د محلول شوې مادې او محلل په نسبي مقدارونو پورې اړه لري لکه د رنګ رنګ، د بورې د محلول خوږوالی یا د عادي مالګې د محلول مالګین خوند د شته محلول شوې مادې په مقدار پورې اړه لري. په ورکړل شوي محلل یا محلول کې د شته محلول شوې مادې مقدار د محلول غلظت بلل کېږي. په محلول کې د شته محلول شوې مادې مقدار څومره ډېر وي د هغه غلظت به هماغومره لوړ وي. د محلول شوې مادې، محلل او محلول مقدار په حجم، وزن یا د مولونو په شمېر اندازه کېدای شي. له همدې امله د محلول غلظت په ډېرو لارو ښودل کېدای شي.')
head(s,'h1','10.2.1 Percentage Composition','10.2.1 فیصدی ترکیب','10.2.1 سلنه جوړښت')
add(s,'b0','The percentage of solution is expressed in four ways.','محلول کی فیصد چار طریقوں سے ظاہر کی جاتی ہے۔','د محلول سلنه په څلورو لارو ښودل کېږي.')
add(s,'i1','i. Percentage by Mass (m/m% or mass to mass percentage)','i. کمیت کے لحاظ سے فیصد (m/m% یا کمیت بمقابلہ کمیت فیصد)','i. د کتلې له مخې سلنه (m/m% یا کتله په کتله سلنه)',kind='heading')
add(s,'i1t','It is the number of grams of solute dissolved in sufficient amount of solvent to make 100 g of solution e.g 10% solution of glucose by mass means that 10 g of glucose are dissolved in sufficient water so that solution mass is 100g.','یہ محلول شدہ شے کے گراموں کی وہ تعداد ہے جو محلل کی کافی مقدار میں حل ہو کر 100 g محلول بنائے، مثلاً کمیت کے لحاظ سے گلوکوز کا 10% محلول کا مطلب ہے کہ 10 g گلوکوز کافی پانی میں اس طرح حل کیا گیا ہے کہ محلول کی کمیت 100g ہو۔','دا د محلول شوې مادې د ګرامو هغه شمېر دی چې د محلل په کافي مقدار کې حل شي ترڅو 100 g محلول جوړ کړي، لکه د کتلې له مخې د ګلوکوز 10% محلول معنا لري چې 10 g ګلوکوز په کافي اوبو کې داسې حل شوي چې د محلول کتله 100g وي.')
add(s,'i2','ii. Mass by Volume Percentage (m/V% or mass to volume percent)','ii. کمیت بمقابلہ حجم فیصد (m/V% یا کمیت بمقابلہ حجم فیصد)','ii. د کتلې په حجم سلنه (m/V% یا کتله په حجم سلنه)',kind='heading')
add(s,'i2t','It is the mass of solute dissolved per 100 parts by volume of solution. 10g of NaOH dissolved per 100 cm³ of solution is 10% m/V solution of NaOH.','یہ محلول شدہ شے کی وہ کمیت ہے جو محلول کے 100 حجمی حصوں میں حل ہو۔ محلول کے فی 100 cm³ میں حل 10g NaOH، NaOH کا 10% m/V محلول ہے۔','دا د محلول شوې مادې هغه کتله ده چې د محلول په 100 حجمي برخو کې حل وي. د محلول په هر 100 cm³ کې حل شوې 10g NaOH، د NaOH 10% m/V محلول دی.')
add(s,'i3','iii. Volume by mass Percentage (V/m%)','iii. حجم بمقابلہ کمیت فیصد (V/m%)','iii. د حجم په کتله سلنه (V/m%)',kind='heading')
add(s,'i3t','It is the number of cm³ of a solute dissolved per 100 g of solution. If we dissolve 10 cm³ of alcohol in water and the total mass of solution is 100g then it is 10% V/m solution of alcohol in water.','یہ محلول شدہ شے کے cm³ کی وہ تعداد ہے جو محلول کے فی 100 g میں حل ہو۔ اگر ہم 10 cm³ الکحل پانی میں حل کریں اور محلول کی کل کمیت 100g ہو تو یہ پانی میں الکحل کا 10% V/m محلول ہے۔','دا د محلول شوې مادې د cm³ هغه شمېر دی چې د محلول په هر 100 g کې حل وي. که موږ 10 cm³ الکول په اوبو کې حل کړو او د محلول ټوله کتله 100g وي نو دا په اوبو کې د الکول 10% V/m محلول دی.')
add(s,'i4','iv. Volume by volume Percentage (V/V%)','iv. حجم بمقابلہ حجم فیصد (V/V%)','iv. د حجم په حجم سلنه (V/V%)',kind='heading')
add(s,'i4t','It is the volume of the solute present per 100 cm³ of the solution e.g. 10 cm³ of alcohol is dissolved in water so that the volume of solution is 100 cm³. It is 10% V/V solution of alcohol in water.','یہ محلول شدہ شے کا وہ حجم ہے جو محلول کے فی 100 cm³ میں موجود ہو، مثلاً 10 cm³ الکحل پانی میں اس طرح حل کیا جائے کہ محلول کا حجم 100 cm³ ہو۔ یہ پانی میں الکحل کا 10% V/V محلول ہے۔','دا د محلول شوې مادې هغه حجم دی چې د محلول په هر 100 cm³ کې شتون ولري، لکه 10 cm³ الکول په اوبو کې داسې حل شي چې د محلول حجم 100 cm³ وي. دا په اوبو کې د الکول 10% V/V محلول دی.')
F.p('h','a1','h1','b0','i1','i1t')
F.e('e1',r'\frac{m}{m}\%=\frac{\text{mass of solute}}{\text{mass of solution}}\times100','m/m % = mass of solute / mass of solution × 100')
F.p('i2','i2t')
F.e('e2',r'\frac{m}{V}\%=\frac{\text{mass of solute}}{\text{Volume of solution}}\times100','m/V % = mass of solute / Volume of solution × 100')
F.p('i3','i3t')
F.e('e3',r'\frac{V}{m}\%=\frac{\text{Volume of solute}}{\text{mass of solution}}\times100','V/m % = Volume of solute / mass of solution × 100')
F.p('i4','i4t')
F.done()
s['sourceNote']='Printed folio 305. The left edge is slightly clipped by the page curl (first letters of several lines) but the text is legible and read in full. The V/V% formula continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='First letters of several left-hand lines cut; V/V% formula continues on the next page.')
s['vocabulary']={'concentration':{'ur':'ارتکاز','ps':'غلظت'},'percentage composition':{'ur':'فیصدی ترکیب','ps':'سلنه جوړښت'}}
save(s)

# ---------- 311 ----------
s=mk(311,'V/V% · 10.2.2 Molarity (M) · 10.2.3 Molality (m)','V/V% · 10.2.2 مولریت (M) · 10.2.3 مولیلٹی (m)','V/V% · 10.2.2 مولاریت (M) · 10.2.3 مولالیت (m)','molarity-molality')
F=Flow(s)
head(s,'h2','10.2.2. Molarity (M)','10.2.2 مولریت (M)','10.2.2 مولاریت (M)')
add(s,'a1','The molarity (M) of a solution is the number of moles of solute per dm³ of solution.','محلول کی مولریت (M) محلول کے فی dm³ میں محلول شدہ شے کے مولوں کی تعداد ہے۔','د محلول مولاریت (M) د محلول په هر dm³ کې د محلول شوې مادې د مولونو شمېر دی.')
add(s,'a2','Therefore,','اس لیے،','نو،')
add(s,'a3','For example, one molar solution (1M) of sugar, C₁₂H₂₂O₁₁, contains 1 mole or 342 g of sugar per dm³ of solution. It is prepared by adding 342 g of sugar in one dm³ volumetric flask and then by adding water first to dissolve and then dilute the solution until the level of the liquid reaches the etched mark i.e when the volume of the solution becomes exactly one dm³.','مثال کے طور پر چینی C₁₂H₂₂O₁₁ کا ایک مولر محلول (1M) محلول کے فی dm³ میں 1 مول یا 342 g چینی رکھتا ہے۔ یہ 342 g چینی کو ایک dm³ کے حجمی فلاسک میں ڈال کر اور پھر پہلے پانی ملا کر اسے حل کر کے اور پھر محلول کو اس وقت تک ہلکا کر کے تیار کیا جاتا ہے جب تک مائع کی سطح نشان زدہ لکیر تک نہ پہنچ جائے یعنی جب محلول کا حجم بالکل ایک dm³ ہو جائے۔','د بورې C₁₂H₂₂O₁₁ یو مولر محلول (1M) د محلول په هر dm³ کې 1 مول یا 342 g بوره لري. دا د 342 g بورې په یو dm³ حجمي فلاسک کې اچولو او بیا لومړی د اوبو په اضافه کولو سره د هغه د حل کولو او بیا محلول رقیق کولو سره جوړېږي تر هغې چې د مایع سطحه نښه شوې کرښې ته ورسېږي یعنې کله چې د محلول حجم دقیقاً یو dm³ شي.')
head(s,'h3','10.2.3 Molality (m)','10.2.3 مولیلٹی (m)','10.2.3 مولالیت (m)')
add(s,'b1','Molality is another concentration unit of solution. Molality is defined as the number of moles of solute present in 1kg of solvent. In other words the molality of a solution is equal to the number of moles of solute dissolved in 1000g of solvent.','مولیلٹی محلول کا ایک اور ارتکازی یونٹ ہے۔ مولیلٹی کی تعریف 1kg محلل میں موجود محلول شدہ شے کے مولوں کی تعداد کے طور پر کی جاتی ہے۔ دوسرے لفظوں میں محلول کی مولیلٹی 1000g محلل میں حل محلول شدہ شے کے مولوں کی تعداد کے برابر ہوتی ہے۔','مولالیت د محلول بل د غلظت واحد دی. مولالیت د 1kg محلل کې د شته محلول شوې مادې د مولونو د شمېر په توګه تعریفېږي. په بل عبارت د محلول مولالیت د 1000g محلل کې د حل شوې مادې د مولونو له شمېر سره مساوي دی.')
add(s,'b2','Or','یا','یا')
add(s,'b3','When 58.5grams (1 mole) of NaCl is dissolved in 1000 grams of water, the solution will be 1.0molal or 1.0m. Similarly, 1.0molal solution of glucose will contain 180g of glucose in 1000g of solvent. If 18g of glucose is dissolved in 1kg of water the molality (m) of glucose solution will be 0.1. Molality is independent of temperature.','جب 58.5 گرام (1 مول) NaCl کو 1000 گرام پانی میں حل کیا جائے تو محلول 1.0 مولل یا 1.0m ہوگا۔ اسی طرح گلوکوز کے 1.0 مولل محلول میں 1000g محلل میں 180g گلوکوز ہوگا۔ اگر 18g گلوکوز 1kg پانی میں حل کیا جائے تو گلوکوز محلول کی مولیلٹی (m) 0.1 ہوگی۔ مولیلٹی درجہ حرارت سے آزاد ہے۔','کله چې 58.5 ګرامه (1 مول) NaCl په 1000 ګرامه اوبو کې حل شي نو محلول به 1.0 مولال یا 1.0m وي. همدارنګه د ګلوکوز 1.0 مولال محلول به په 1000g محلل کې 180g ګلوکوز ولري. که 18g ګلوکوز په 1kg اوبو کې حل شي نو د ګلوکوز محلول مولالیت (m) به 0.1 وي. مولالیت د تودوخې څخه خپلواک دی.')
F.e('v',r'\frac{V}{V}\%=\frac{\text{Volume of solute}}{\text{Volume of solution}}\times100','V/V % = Volume of solute / Volume of solution × 100')
F.p('h2','a1')
F.e('m1',r'\text{Molarity (M)}=\frac{\text{Number of moles of solute}}{\text{Volume of solution (dm}^3)}','Molarity (M) = Number of moles of solute / Volume of solution (dm³)')
F.e('m2',r'1\ \mathrm{dm^3}=1000\ \mathrm{cm^3}=1\ \text{litre}','1 dm³ = 1000 cm³ = 1 litre')
F.e('m3',r'\text{Number of moles of solute}=\frac{\text{mass of solute in g}}{\text{Mol. mass of solute}}','Number of moles of solute = mass of solute in g / Mol. mass of solute')
F.p('a2')
F.e('m4',r'\text{Molarity (M)}=\frac{\text{mass of solute in g}}{\text{Mol. mass of solute}}\times\frac{1}{\text{volume of solution (dm}^3)}','Molarity (M) = mass of solute in g / Mol. mass of solute × 1 / volume of solution (dm³)')
F.p('a3','h3','b1')
F.e('l1',r'\text{Molality (m)}=\frac{\text{Number of moles of solute}}{\text{Number of kilogram of solvent}}','Molality (m) = Number of moles of solute / Number of kilogram of solvent')
F.p('b2')
F.e('l2',r'=\frac{\text{mass of solute}}{\text{mol. mass of solute}}\times\frac{1}{\text{Kilogram of solvent}}','= mass of solute / mol. mass of solute × 1 / Kilogram of solvent')
F.p('b3')
F.done()
s['sourceNote']='Printed folio 306. The right edge is clipped by the page curl on several lines of text ("…per dm³ of", "…contains 1 mole", "…in one dm³", "…defined as", "…in the solution", etc.); the sentences are legible and transcribed in full. The V/V% formula at the top completes the previous page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Slight right-edge clipping of word endings; V/V% formula completes the previous page.')
s['vocabulary']={'molarity':{'ur':'مولریت','ps':'مولاریت'},'molality':{'ur':'مولیلٹی','ps':'مولالیت'},'volumetric flask':{'ur':'حجمی فلاسک','ps':'حجمي فلاسک'}}
save(s)

# ---------- 312 ----------
s=mk(312,'Example 10.1 · Practice Problems 10.1, 10.2 · 10.2.4 Mole Fraction (X)','مثال 10.1 · مشقی مسائل 10.1، 10.2 · 10.2.4 مول جزو (X)','بېلګه 10.1 · د تمرین ستونزې 10.1، 10.2 · 10.2.4 مول برخه (X)','example101-mole-fraction')
F=Flow(s)
head(s,'e','Example 10.1','مثال 10.1','بېلګه 10.1')
add(s,'q','4.5g of glucose are dissolved in 100g of water. Calculate the molality of solution. Molecular mass of glucose is 180g mol⁻¹.','4.5g گلوکوز 100g پانی میں حل کیا گیا ہے۔ محلول کی مولیلٹی معلوم کریں۔ گلوکوز کی سالماتی کمیت 180g mol⁻¹ ہے۔','4.5g ګلوکوز په 100g اوبو کې حل شوي. د محلول مولالیت محاسبه کړئ. د ګلوکوز مالیکولي کتله 180g mol⁻¹ ده.')
head(s,'s','Solution','حل','حل')
add(s,'s1','Mass of glucose = 4.5g.','گلوکوز کی کمیت = 4.5g۔','د ګلوکوز کتله = 4.5g.')
add(s,'s2','Mass of water = 100g.','پانی کی کمیت = 100g۔','د اوبو کتله = 100g.')
add(s,'s3','Molecular mass of glucose = 180g mol⁻¹','گلوکوز کی سالماتی کمیت = 180g mol⁻¹','د ګلوکوز مالیکولي کتله = 180g mol⁻¹')
add(s,'s4','Calculations','حسابات','محاسبې')
head(s,'p1h','Practice Problem 10.1','مشقی مسئلہ 10.1','د تمرین ستونزه 10.1')
add(s,'p1','A sample has 3.50 dm³ of solution that contains 90g of sodium chloride, NaCl. What is the molarity of that solution?','ایک نمونے میں 3.50 dm³ محلول ہے جس میں 90g سوڈیم کلورائیڈ NaCl ہے۔ اس محلول کی مولریت کیا ہے؟','یوه نمونه 3.50 dm³ محلول لري چې 90g سوډیم کلوراید NaCl لري. د هغه محلول مولاریت څومره دی؟')
head(s,'p2h','Practice Problem 10.2','مشقی مسئلہ 10.2','د تمرین ستونزه 10.2')
add(s,'p2','What is the molality of a solution containing 18.2g HCl and 250 g of water?','اس محلول کی مولیلٹی کیا ہے جس میں 18.2g HCl اور 250 g پانی ہو؟','د هغه محلول مولالیت څومره دی چې 18.2g HCl او 250 g اوبه لري؟')
head(s,'h4','10.2.4 Mole Fraction (X)','10.2.4 مول جزو (X)','10.2.4 مول برخه (X)')
add(s,'m1','Mole fraction of any component of a solution is defined as the number of moles of that particular component divided by the total number of moles of all the components in the solution. For example, if n₁ is the number of moles of solvent and n₂ is the number moles of solute. X₁ and X₂ are mole fractions of solvent and solute respectively, then mathematically X₁ and X₂ are expressed as','محلول کے کسی بھی جزو کا مول جزو اس خاص جزو کے مولوں کی تعداد کو محلول میں تمام اجزاء کے مولوں کی کل تعداد سے تقسیم کرنے سے متعین کیا جاتا ہے۔ مثال کے طور پر اگر n₁ محلل کے مولوں کی تعداد ہے اور n₂ محلول شدہ شے کے مولوں کی تعداد ہے۔ X₁ اور X₂ بالترتیب محلل اور محلول شدہ شے کے مول جزو ہیں، تو ریاضیاتی طور پر X₁ اور X₂ اس طرح ظاہر کیے جاتے ہیں','د محلول د هر جز مول برخه د هغه ځانګړي جز د مولونو شمېر په محلول کې د ټولو اجزاوو د مولونو په ټول شمېر ویشل په توګه تعریفېږي. د بېلګې په توګه که n₁ د محلل د مولونو شمېر وي او n₂ د محلول شوې مادې د مولونو شمېر وي. X₁ او X₂ په ترتیب سره د محلل او محلول شوې مادې مول برخې دي، نو ریاضیاتي ډول X₁ او X₂ داسې ښودل کېږي')
add(s,'m2','Note that the sum of the mole fractions is equal to one. The importance of mole fraction is, like molality, this method of expressing concentration is also','نوٹ کریں کہ مول اجزاء کا مجموعہ ایک کے برابر ہوتا ہے۔ مول جزو کی اہمیت یہ ہے کہ مولیلٹی کی طرح ارتکاز ظاہر کرنے کا یہ طریقہ بھی','پام وکړئ چې د مول برخو مجموعه له یو سره مساوي ده. د مول برخې اهمیت دا دی چې د مولالیت په څېر د غلظت د ښودلو دا طریقه هم')
F.p('e','q','s','s1','s2','s3','s4')
F.e('c1',r'\text{Moles of glucose}=\frac{4.5\ \mathrm{g}}{180\ \mathrm{g\,mol^{-1}}}=0.025\ \mathrm{mol}','Moles of glucose = 4.5 g / 180 g.mol⁻¹ = 0.025 mol')
F.e('c2',r'\text{mass of water in kilograms}=\frac{100\ \mathrm{g}}{1000}=0.1\ \mathrm{kg}','mass of water in kilograms = 100 g / 1000 = 0.1 kg')
F.e('c3',r'\text{molality (m)}=\frac{0.025}{0.1\ \mathrm{kg}}=0.25\ \mathrm{mol\,kg^{-1}}','molality (m) = 0.025 / 0.1 kg = 0.25 mol kg⁻¹')
F.p('p1h','p1','p2h','p2','h4','m1')
F.e('f1',r'\text{Mole fraction of solvent, }X_1=\frac{n_1}{n_1+n_2}','Mole fraction of solvent, X₁ = n₁ / (n₁ + n₂)')
F.e('f2',r'\text{Mole fraction of solute, }X_2=\frac{n_2}{n_1+n_2}','Mole fraction of solute, X₂ = n₂ / (n₁ + n₂)')
F.e('f3',r'X_1+X_2=\frac{n_1}{n_1+n_2}+\frac{n_2}{n_1+n_2}=1','X₁ + X₂ = n₁ / (n₁ + n₂) + n₂ / (n₁ + n₂) = 1')
F.p('m2')
F.done()
s['sourceNote']='Printed folio 307. The left edge of the Example 10.1 question and of the mole-fraction paragraph is slightly clipped but legible. The last sentence continues on the next page ("…also [independent of temperature]"). The Practice Problems have no answers printed. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Last sentence continues on the next page.')
s['vocabulary']={'mole fraction':{'ur':'مول جزو','ps':'مول برخه'}}
save(s)
