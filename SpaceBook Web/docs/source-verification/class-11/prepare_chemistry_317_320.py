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
    def fg(s_,i): s_.f.append(dict(type='figure',index=i))
    def done(s_): s_.s['flow']=s_.f
def mk(n,title,ur,ps,sid): return page(n,'chem11-solutions-colloids',title,ur,ps,sid)
def tx(x,y,t,size=11,anchor='middle',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'

# ---------- 317 ----------
s=mk(317,'Vapour pressure lowering equations · 10.4 Colligative Properties of Dilute Solutions','بخارات دباؤ میں کمی کی مساواتیں · 10.4 ہلکے محلولوں کی ارتکاز پر منحصر خصوصیات','د بخار فشار د کمښت معادلې · 10.4 د رقیقو محلولونو همغږې ځانګړنې','colligative-intro')
F=Flow(s)
add(s,'a1',f'pure solvent and P is the vapour pressure of solution. According to Raoult\'s law{SO} vapour pressure P is given by','خالص محلل اور P محلول کا بخارات دباؤ ہے۔ راؤلٹ کے قانون کے مطابق بخارات دباؤ P اس سے دیا جاتا ہے','خالص محلل او P د محلول بخار فشار دی. د راؤلټ د قانون له مخې بخار فشار P په لاندې ډول ورکول کېږي')
add(s,'a2',f'Since X₁ in any solution is less than unity, P must always be less than P°. Consequently, a solute in a solvent tends to lower the vapour pressure of the pure solvent. Furthermore, if the solute is non-volatile it does not contribute to the total vapour pressure, and hence Eq. (10.2) gives the total vapour pressure above the solution, which in this case is due to solvent only and is always less than P°. The extent of the vapour pressure lowering ΔP is','چونکہ کسی بھی محلول میں X₁ اکائی سے کم ہوتا ہے، P ہمیشہ P° سے کم ہونا چاہیے۔ نتیجتاً محلل میں محلول شدہ شے خالص محلل کا بخارات دباؤ کم کرنے کا رجحان رکھتی ہے۔ مزید یہ کہ اگر محلول شدہ شے غیر اڑنے والی ہو تو وہ کل بخارات دباؤ میں حصہ نہیں لیتی، اور اس لیے مساوات (10.2) محلول کے اوپر کل بخارات دباؤ دیتی ہے، جو اس صورت میں صرف محلل کی وجہ سے ہے اور ہمیشہ P° سے کم ہے۔ بخارات دباؤ میں کمی ΔP کی حد ہے','ځکه چې په هر محلول کې X₁ له واحد څخه کم دی، P باید تل له P° څخه کم وي. په پایله کې په محلل کې محلول شوی مواد د خالص محلل بخار فشار کمولو تمایل لري. سربیره پر دې که محلول شوی مواد غیر الوتونکی وي نو دا په ټول بخار فشار کې برخه نه اخلي، او نو معادله (10.2) د محلول پورته ټول بخار فشار ورکوي، چې پدې حالت کې یوازې د محلل له امله دی او تل له P° څخه کم دی. د بخار فشار د کمښت اندازه ΔP ده')
add(s,'a3','According to Eq.(10.4), the lowering of vapour pressure of solution depends both on vapour pressure of pure solvent and the mole fraction of solute in solution. In other words, it depends on the nature of solvent and the concentration of solute, but not on the nature of solute. However, if we consider the relative lowering of vapour pressure i.e. the ratio ΔP/P°, then from Eq. (10.4).','مساوات (10.4) کے مطابق محلول کے بخارات دباؤ میں کمی خالص محلل کے بخارات دباؤ اور محلول میں محلول شدہ شے کے مول جزو دونوں پر منحصر ہوتی ہے۔ دوسرے لفظوں میں یہ محلل کی نوعیت اور محلول شدہ شے کے ارتکاز پر منحصر ہے، لیکن محلول شدہ شے کی نوعیت پر نہیں۔ تاہم اگر ہم بخارات دباؤ کی اضافی کمی یعنی نسبت ΔP/P° پر غور کریں تو مساوات (10.4) سے۔','د (10.4) معادلې له مخې د محلول د بخار فشار کمښت د خالص محلل د بخار فشار او په محلول کې د محلول شوې مادې مول برخې دواړو پورې اړه لري. په بل عبارت دا د محلل په ماهیت او د محلول شوې مادې په غلظت پورې اړه لري، خو د محلول شوې مادې په ماهیت نه. خو که موږ د بخار فشار نسبي کمښت یعنې نسبت ΔP/P° ته پام وکړو نو له (10.4) معادلې څخه.')
add(s,'a4','It shows that relative lowering of vapour pressure of the solution depends only on the mole fraction of solute and is completely independent of either the nature of solute or solvent. It is also independent of temperature. Those properties of solution which only depend on the amount of the solute or the number of solute particles are called colligative properties. Thus the lowering in vapour pressure is a colligative property.','یہ ظاہر کرتی ہے کہ محلول کے بخارات دباؤ کی اضافی کمی صرف محلول شدہ شے کے مول جزو پر منحصر ہے اور محلول شدہ شے یا محلل کی نوعیت سے مکمل طور پر آزاد ہے۔ یہ درجہ حرارت سے بھی آزاد ہے۔ محلول کی وہ خصوصیات جو صرف محلول شدہ شے کی مقدار یا محلول شدہ ذرات کی تعداد پر منحصر ہوں ارتکاز پر منحصر خصوصیات (کولیگیٹو) کہلاتی ہیں۔ اس طرح بخارات دباؤ میں کمی ایک کولیگیٹو خصوصیت ہے۔','دا ښيي چې د محلول د بخار فشار نسبي کمښت یوازې د محلول شوې مادې په مول برخه پورې اړه لري او د محلول شوې مادې یا محلل له ماهیت څخه بشپړ خپلواک دی. دا د تودوخې څخه هم خپلواک دی. د محلول هغه ځانګړنې چې یوازې د محلول شوې مادې په مقدار یا د محلول شویو ذراتو په شمېر پورې اړه لري همغږې ځانګړنې بلل کېږي. په دې توګه د بخار فشار کمښت یوه همغږې ځانګړنه ده.')
head(s,'h','10.4 Colligative Properties of Dilute Solutions','10.4 ہلکے محلولوں کی ارتکاز پر منحصر خصوصیات','10.4 د رقیقو محلولونو همغږې ځانګړنې')
add(s,'b1',f'Colligative (or collective) properties are those properties which depend only on the number of solute particles but not on the nature of the solute particles. The study of colligative properties is important especially because they provide methods for determining the molecular weight of dissolved substances. The colligative properties of a dilute solution containing a non-volatile non-electrolyte solute are:','کولیگیٹو (یا اجتماعی) خصوصیات وہ خصوصیات ہیں جو صرف محلول شدہ ذرات کی تعداد پر منحصر ہوتی ہیں لیکن محلول شدہ ذرات کی نوعیت پر نہیں۔ کولیگیٹو خصوصیات کا مطالعہ اس لیے خاص طور پر اہم ہے کہ یہ حل شدہ مادوں کا سالماتی وزن معلوم کرنے کے طریقے فراہم کرتی ہیں۔ غیر اڑنے والی غیر برق پاش محلول شدہ شے پر مشتمل ہلکے محلول کی کولیگیٹو خصوصیات یہ ہیں:','همغږې (یا ټولګیزې) ځانګړنې هغه ځانګړنې دي چې یوازې د محلول شویو ذراتو په شمېر پورې اړه لري خو د محلول شویو ذراتو په ماهیت نه. د همغږو ځانګړنو مطالعه په ځانګړې توګه ځکه مهمه ده چې دا د منحل شویو موادو د مالیکولي وزن د ټاکلو لارې برابروي. د یو غیر الوتونکي غیر الکترولایټ محلول شوې مادې لرونکي رقیق محلول همغږې ځانګړنې دا دي:')
F.p('a1')
F.e('e102',r'P=P^{\circ}X_1\qquad(10.2)','P = P°X₁   (10.2)')
F.p('a2')
F.e('e103',r'\Delta P=P^{\circ}-P\qquad(10.3)','ΔP = P° − P   (10.3)')
F.e('d1',r'\Delta P=P^{\circ}-P^{\circ}X_1','ΔP = P° − P°X₁')
F.e('d2',r'\Delta P=P^{\circ}(1-X_1)','ΔP = P°(1 − X₁)')
F.e('e104',r'\Delta P=P^{\circ}X_2\qquad(10.4)','ΔP = P°X₂   (10.4)')
F.p('a3')
F.e('e105',r'\frac{\Delta P}{P^{\circ}}=\frac{P^{\circ}X_2}{P^{\circ}}\qquad(10.5)','ΔP / P° = P°X₂ / P°   (10.5)')
F.e('e106',r'\frac{\Delta P}{P^{\circ}}=X_2\qquad(10.6)','ΔP / P° = X₂   (10.6)')
F.p('a4','h','b1')
F.done()
s['sourceNote']='Printed folio 312. The right edge is clipped by the page curl on the prose lines and on the pink italic text; clipped endings are marked [scan obscured] and not inferred (the first sentence is cut after "Raoult\'s law"). The last sentence continues on the next page with the list a–d. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; the sentence ends with a list that continues on the next page.')
s['vocabulary']={'colligative properties':{'ur':'ارتکاز پر منحصر خصوصیات','ps':'همغږې ځانګړنې'}}
save(s)

# ---------- 318 ----------
s=mk(318,'10.4.1 Vapour Pressure lowering · Equations 10.7–10.9','10.4.1 بخارات دباؤ میں کمی · مساواتیں 10.7–10.9','10.4.1 د بخار فشار کمښت · معادلې 10.7–10.9','vapour-pressure-lowering')
F=Flow(s)
for i,(e,u,p) in enumerate([('a. Lowering of vapour pressure.','الف۔ بخارات دباؤ میں کمی۔','الف. د بخار فشار کمښت.'),('b. Elevation of boiling point.','ب۔ نقطۂ جوش میں اضافہ۔','ب. د جوش د نقطې لوړېدل.'),('c. Depression in freezing point.','ج۔ نقطۂ انجماد میں کمی۔','ج. د ځمبېدو د نقطې ښکته کېدل.'),('d. Osmotic pressure.','د۔ اسموٹک دباؤ۔','د. اسموټیک فشار.')],1): add(s,f'l{i}',e,u,p)
head(s,'h','10.4.1 Vapour Pressure lowering','10.4.1 بخارات دباؤ میں کمی','10.4.1 د بخار فشار کمښت')
add(s,'a1','The lowering of vapour pressure can be used to calculate the molecular mass \'M\' of solute as follows.','بخارات دباؤ میں کمی کو محلول شدہ شے کی سالماتی کمیت \'M\' کا حساب لگانے کے لیے اس طرح استعمال کیا جا سکتا ہے۔','د بخار فشار کمښت د محلول شوې مادې د مالیکولي کتلې \'M\' د محاسبې لپاره په لاندې ډول کارېدای شي.')
add(s,'a2','Since','چونکہ','ځکه چې')
add(s,'a3','So Equation (10.6) becomes.','لہٰذا مساوات (10.6) بن جاتی ہے۔','نو معادله (10.6) کېږي.')
add(s,'a4','Eq. (10.7) represents another form of Raoult\'s law. If mass of pure solvent = W₁ and molecular mass = M₁, mass of pure solute = W₂ and molecular mass = M₂ then Eq. (10.7) becomes','مساوات (10.7) راؤلٹ کے قانون کی ایک اور شکل ظاہر کرتی ہے۔ اگر خالص محلل کی کمیت = W₁ اور سالماتی کمیت = M₁، خالص محلول شدہ شے کی کمیت = W₂ اور سالماتی کمیت = M₂ ہو تو مساوات (10.7) بن جاتی ہے','معادله (10.7) د راؤلټ د قانون بله بڼه ښيي. که د خالص محلل کتله = W₁ او مالیکولي کتله = M₁، د خالص محلول شوې مادې کتله = W₂ او مالیکولي کتله = M₂ وي نو معادله (10.7) کېږي')
add(s,'a5','For a very dilute solution n₂ << n₁ : therefore, (n₁ + n₂) = n₁. Thus W₂/M₂ can be neglected from the denominator.','بہت ہلکے محلول کے لیے n₂ << n₁ ہوتا ہے؛ لہٰذا (n₁ + n₂) = n₁۔ اس طرح W₂/M₂ کو نسب نما سے نظر انداز کیا جا سکتا ہے۔','د ډېر رقیق محلول لپاره n₂ << n₁ دی؛ نو (n₁ + n₂) = n₁. په دې توګه W₂/M₂ له مخرج څخه له پامه غورځول کېدای شي.')
add(s,'a6','The Eq. (10.8) then can be written as','مساوات (10.8) کو پھر اس طرح لکھا جا سکتا ہے','معادله (10.8) بیا داسې لیکل کېدای شي')
add(s,'a7','Eq. (10.9) can be used to calculate molecular mass of the dissolved substance if relative lowering of vapour pressure and the definite mass of solute in a given amount of solvent are known.','مساوات (10.9) حل شدہ مادے کی سالماتی کمیت کا حساب لگانے کے لیے استعمال کی جا سکتی ہے اگر بخارات دباؤ کی اضافی کمی اور محلل کی دی گئی مقدار میں محلول شدہ شے کی معین کمیت معلوم ہو۔','معادله (10.9) د منحل شوې مادې د مالیکولي کتلې د محاسبې لپاره کارېدای شي که د بخار فشار نسبي کمښت او په ورکړل شوې محلل مقدار کې د محلول شوې مادې ټاکلې کتله معلومه وي.')
F.p('l1','l2','l3','l4','h','a1','a2')
F.e('x2',r'X_2=\frac{n_2}{n_1+n_2}','X₂ = n₂ / (n₁ + n₂)')
F.p('a3')
F.e('x3',r'X_2=\frac{\Delta P}{P^{\circ}}','X₂ = ΔP / P°')
F.e('e107',r'\frac{P^{\circ}-P_s}{P^{\circ}}=\frac{\Delta P}{P^{\circ}}=\frac{n_2}{n_1+n_2}\qquad(10.7)','(P° − P_s) / P° = ΔP / P° = n₂ / (n₁ + n₂)   (10.7)')
F.p('a4')
F.e('e108',r'\frac{P^{\circ}-P_s}{P^{\circ}}=\frac{n_2}{n_1+n_2}=\frac{W_2/M_2}{W_1/M_1+W_2/M_2}\qquad(10.8)','(P° − P_s) / P° = n₂ / (n₁ + n₂) = (W₂/M₂) / (W₁/M₁ + W₂/M₂)   (10.8)')
F.p('a5','a6')
F.e('e109',r'\frac{P^{\circ}-P_s}{P^{\circ}}=\frac{W_2M_1}{W_1M_2}\qquad(10.9)','(P° − P_s) / P° = W₂M₁ / W₁M₂   (10.9)')
F.p('a7')
F.done()
s['sourceNote']='Printed folio 313. The page is legible; the left edge is slightly shadowed. A small fragment "P° − P_s" is printed above the first fraction of Eq. (10.8) (retained in the equation). A CamScanner watermark crosses the page.'
s['vocabulary']={}
save(s)

# ---------- 319 ----------
s=mk(319,'10.4.2 Boiling Point Elevation and Freezing Point Depression · (i) Boiling Point Elevation · Figure 10.3','10.4.2 نقطۂ جوش میں اضافہ اور نقطۂ انجماد میں کمی · (i) نقطۂ جوش میں اضافہ · شکل 10.3','10.4.2 د جوش د نقطې لوړېدل او د ځمبېدو د نقطې ښکته کېدل · (i) د جوش د نقطې لوړېدل · شکل 10.3','boiling-point-elevation')
F=Flow(s)
head(s,'h','10.4.2 Boiling Point Elevation and Freezing Point Depression','10.4.2 نقطۂ جوش میں اضافہ اور نقطۂ انجماد میں کمی','10.4.2 د جوش د نقطې لوړېدل او د ځمبېدو د نقطې ښکته کېدل')
add(s,'h1','(i) Boiling Point Elevation','(i) نقطۂ جوش میں اضافہ','(i) د جوش د نقطې لوړېدل',kind='heading')
add(s,'a1',f'Boiling point of a solution is the temperature at which its vapour pressure becomes equal to external pressure or atmospheric pressure. Since the presence of a non-volatile solute lowers the vapour pressure of the solution, therefore, boiling point must increase. This fact has been qualitatively expressed by Raoult\'s law.','محلول کا نقطۂ جوش وہ درجہ حرارت ہے جس پر اس کا بخارات دباؤ بیرونی دباؤ یا ماحولیاتی دباؤ کے برابر ہو جاتا ہے۔ چونکہ غیر اڑنے والی محلول شدہ شے کی موجودگی محلول کا بخارات دباؤ کم کرتی ہے، اس لیے نقطۂ جوش بڑھنا چاہیے۔ یہ حقیقت راؤلٹ کے قانون سے کیفی طور پر ظاہر ہوتی ہے۔','د محلول د جوش نقطه هغه تودوخه ده چې په هغې کې د هغه بخار فشار د بهرني فشار یا اتموسفیر فشار سره مساوي کېږي. ځکه چې د یو غیر الوتونکي محلول شوې مادې شتون د محلول بخار فشار کموي، نو د جوش نقطه باید لوړه شي. دا حقیقت د راؤلټ د قانون په واسطه په کیفي ډول ښودل شوی.')
add(s,'a2',f'According to Raoult\'s law the vapour pressure of solution containing non-volatile solutes is always less than that of pure solvent. As a result of lowering of vapour pressure the solution will boil at a temperature higher than the boiling point of the pure solvent at the atmospheric pressure. This difference in the boiling points of solution and its pure solvent is known as boiling point elevation of the solution. It depends on the nature of solvent and the concentration of solute. The boiling point elevation in dilute solution is independent of the nature of solute if it does not ionize, associate, or react with the solvent. For 1.0 mole of any solute if dissolved in 1 kg of pure solvent, the elevation of boiling point is called molal boiling elevation constant or ebullioscopic constant. If 1 mole of a solute is dissolved in 1 kg of pure water the solution now boils at 100.52°C instead of 100°C. The difference 0.52°C is the ebullioscopic constant, k_b, of water. Elevation of boiling point can be explained by plotting a graph, of vapour pressure verses temperature for pure water and an aqueous solution.',f'راؤلٹ کے قانون کے مطابق غیر اڑنے والی محلول شدہ اشیاء پر مشتمل محلول کا بخارات دباؤ ہمیشہ خالص محلل سے کم ہوتا ہے۔ بخارات دباؤ میں کمی کے نتیجے میں محلول ماحولیاتی دباؤ پر خالص محلل کے نقطۂ جوش سے بلند درجہ حرارت پر ابلے گا۔ محلول اور اس کے خالص محلل کے نقطۂ جوش کا یہ فرق محلول کا نقطۂ جوش میں اضافہ کہلاتا ہے۔ یہ محلل کی نوعیت اور محلول شدہ شے کے ارتکاز پر منحصر ہے۔ ہلکے محلول میں نقطۂ جوش میں اضافہ محلول شدہ شے کی نوعیت سے آزاد ہوتا ہے اگر وہ آئنائز، اجتماع یا محلل کے ساتھ تعامل نہ کرے۔ کسی بھی محلول شدہ شے کے 1.0 مول کو 1 kg خالص محلل میں حل کرنے پر نقطۂ جوش میں اضافہ مولل نقطۂ جوش اضافی مستقلہ یا ایبولیوسکوپک مستقلہ کہلاتا ہے۔ اگر کسی محلول شدہ شے کا 1 مول 1 kg خالص پانی میں حل کیا جائے تو محلول اب 100°C کی بجائے 100.52°C پر ابلتا ہے۔ فرق 0.52°C پانی کا ایبولیوسکوپک مستقلہ k_b ہے۔ نقطۂ جوش میں اضافے کی وضاحت خالص پانی اور آبی محلول کے لیے بخارات دباؤ بمقابلہ درجہ حرارت کا گراف بنا کر کی جا سکتی ہے۔','د راؤلټ د قانون له مخې د غیر الوتونکو محلول شویو موادو لرونکي محلول بخار فشار تل د خالص محلل په پرتله کم دی. د بخار فشار د کمښت په پایله کې به محلول په اتموسفیر فشار کې د خالص محلل له جوش نقطې څخه په لوړه تودوخه وجوشي. د محلول او د هغه د خالص محلل د جوش د نقطو دا توپیر د محلول د جوش د نقطې لوړېدل بلل کېږي. دا د محلل په ماهیت او د محلول شوې مادې په غلظت پورې اړه لري. په رقیق محلول کې د جوش د نقطې لوړېدل د محلول شوې مادې له ماهیت څخه خپلواک دی که چېرې دا آیونایز نشي، یوځای نشي یا له محلل سره تعامل ونه کړي. د هر محلول شوې مادې د 1.0 مول لپاره که په 1 kg خالص محلل کې حل شي نو د جوش د نقطې لوړېدل مولال د جوش د نقطې لوړېدو ثابت یا ایبولیوسکوپیک ثابت بلل کېږي. که د یوې محلول شوې مادې 1 مول په 1 kg خالصو اوبو کې حل شي نو محلول اوس په 100°C پر ځای په 100.52°C جوشېږي. توپیر 0.52°C د اوبو ایبولیوسکوپیک ثابت k_b دی. د جوش د نقطې لوړېدل د خالصو اوبو او اوبیز محلول لپاره د بخار فشار په مقابل د تودوخې ګراف رسمولو سره تشریح کېدای شي.')
add(s,'a3',f'Consider Fig. 10.3 the curve AB and CD represent vapour pressure of pure solvent and solution, respectively, as a function of temperature. Temperature T₁ on curve AB is boiling point of pure solvent. The solvent boils when its vapour pressure become equal to the external pressure represented by P°. T₂ on curve CD is the boiling point of solution. CD curve is lower than curve AB because vapour pressure of solution is less than that of pure solvent. Thus the solution will boil at higher temperature T₂ to equalize its vapour{SO}',f'شکل 10.3 پر غور کریں، منحنی AB اور CD بالترتیب خالص محلل اور محلول کے بخارات دباؤ کو درجہ حرارت کے تفاعل کے طور پر ظاہر کرتے ہیں۔ منحنی AB پر درجہ حرارت T₁ خالص محلل کا نقطۂ جوش ہے۔ محلل اس وقت ابلتا ہے جب اس کا بخارات دباؤ P° سے ظاہر کیے گئے بیرونی دباؤ کے برابر ہو جائے۔ منحنی CD پر T₂ محلول کا نقطۂ جوش ہے۔ منحنی CD منحنی AB سے نیچے ہے کیونکہ محلول کا بخارات دباؤ خالص محلل سے کم ہے۔ اس طرح محلول اپنے بخارات {SO} کو برابر کرنے کے لیے بلند درجہ حرارت T₂ پر ابلے گا',f'10.3 شکل ته پام وکړئ، منحنیګانې AB او CD په ترتیب سره د خالص محلل او محلول بخار فشار د تودوخې د تابع په توګه ښيي. په منحني AB کې تودوخه T₁ د خالص محلل جوش نقطه ده. محلل هغه مهال جوشېږي کله چې د هغه بخار فشار د P° په واسطه ښودل شوي بهرني فشار سره مساوي شي. په منحني CD کې T₂ د محلول جوش نقطه ده. منحني CD له AB منحني څخه ښکته ده ځکه چې د محلول بخار فشار له خالص محلل څخه کم دی. په دې توګه محلول به د خپل بخار {SO} د برابرولو لپاره په لوړه تودوخه T₂ وجوشي')
g=('<path d="M50 20 V190 H260" stroke="#222" stroke-width="2" fill="none"/>'
 '<path d="M60 150 C100 120 140 80 190 30" stroke="#c0305a" stroke-width="2" fill="none"/>'
 '<path d="M60 175 C110 150 160 100 215 30" stroke="#c0305a" stroke-width="2" fill="none"/>'
 '<path d="M50 45 H190" stroke="#c0305a" stroke-dasharray="4 3" fill="none"/><path d="M50 82 H175" stroke="#c0305a" stroke-dasharray="4 3" fill="none"/><path d="M190 45 V190 M205 70 V190" stroke="#222" fill="none"/><path d="M190 190 V45 M205 190 V82" stroke="#222" fill="none"/>'
 +tx(40,50,'P°',11,'end',700)+tx(40,86,'P',11,'end',700)+tx(65,145,'A',11,'start')+tx(190,28,'B',11,'start')+tx(65,172,'C',11,'start')+tx(218,28,'D',11,'start')+tx(180,50,'E',10,'end')+tx(200,98,'F',10,'start')+tx(212,76,'G',10,'start')
 +tx(195,208,'T₁',11,'middle')+tx(212,208,'T₂',11,'middle')+tx(22,105,'Vapour pressure →',11,'middle',700).replace('<text','<text transform="rotate(-90 22 105)"')+tx(150,222,'Temperature →',11,'middle',700)+tx(150,242,'Figure 10.3 Boiling Point Elevation',11,'middle',700,'#a02040'))
s['figures']=[fig(319,'fig10-3',svg(290,250,'Vapour pressure curves of pure solvent AB and solution CD with boiling points T1 and T2',g),'Figure 10.3 Boiling Point Elevation','شکل 10.3 نقطۂ جوش میں اضافہ','شکل 10.3 د جوش د نقطې لوړېدل',[lab('Vapour pressure','بخارات دباؤ','بخار فشار'),lab('Temperature','درجہ حرارت','تودوخه'),lab('P°','P°','P°')])]
s['figures'][0]['sourceGap']=dict(note='Graph redrawn as a schematic; the caption is partly clipped at the right edge and the small ΔT_b label is not reproduced.')
F.p('h','h1','a1')
F.fg(0)
F.p('a2','a3')
F.done()
s['sourceNote']='Printed folio 314. The right edge is clipped by the page curl on the text and on the caption of Fig. 10.3; clipped endings are marked [scan obscured] and not inferred. The pink italic definitions are partly cut. The last sentence continues on the next page ("…its vapour pressure to P°"). The figure sits at the right of the text. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; figure redrawn; last sentence continues on the next page.')
s['vocabulary']={'boiling point elevation':{'ur':'نقطۂ جوش میں اضافہ','ps':'د جوش د نقطې لوړېدل'},'ebullioscopic constant':{'ur':'ایبولیوسکوپک مستقلہ','ps':'ایبولیوسکوپیک ثابت'}}
save(s)

# ---------- 320 ----------
s=mk(320,'ΔTb = Kb m · Equations 10.10–10.12 · Example 10.5','ΔTb = Kb m · مساواتیں 10.10–10.12 · مثال 10.5','ΔTb = Kb m · معادلې 10.10–10.12 · بېلګه 10.5','dtb-example105')
F=Flow(s)
add(s,'a1','pressure to P°. Hence elevation of boiling point ΔT_b is given as,','دباؤ P° تک۔ لہٰذا نقطۂ جوش میں اضافہ ΔT_b اس طرح دیا جاتا ہے،','فشار P° ته. نو د جوش د نقطې لوړېدل ΔT_b په لاندې ډول ورکول کېږي،')
add(s,'a2','Increase in concentration of solute particles will increase the boiling point of the solution. So ΔT_b ∝ m where m is the molality of solution.','محلول شدہ ذرات کے ارتکاز میں اضافہ محلول کا نقطۂ جوش بڑھا دے گا۔ لہٰذا ΔT_b ∝ m جہاں m محلول کی مولیلٹی ہے۔','د محلول شویو ذراتو د غلظت زیاتوالی به د محلول جوش نقطه لوړه کړي. نو ΔT_b ∝ m چېرته چې m د محلول مولالیت دی.')
add(s,'a3','K_b is called molal boiling point elevation constant or ebullioscopic constant, when solution is 1 molal or m=1 then ΔT_b = K_b.','K_b کو مولل نقطۂ جوش اضافی مستقلہ یا ایبولیوسکوپک مستقلہ کہا جاتا ہے، جب محلول 1 مولل ہو یا m=1 تو ΔT_b = K_b۔','K_b ته مولال د جوش د نقطې د لوړېدو ثابت یا ایبولیوسکوپیک ثابت ویل کېږي، کله چې محلول 1 مولال وي یا m=1 نو ΔT_b = K_b.')
add(s,'a4','It means that if a solution is of unit molality its elevation of boiling point is called ebullioscopic constant.','اس کا مطلب ہے کہ اگر محلول اکائی مولیلٹی کا ہو تو اس کا نقطۂ جوش میں اضافہ ایبولیوسکوپک مستقلہ کہلاتا ہے۔','دا معنا لري چې که یو محلول د واحد مولالیت وي نو د هغه د جوش د نقطې لوړېدل ایبولیوسکوپیک ثابت بلل کېږي.')
add(s,'a5','The molality (m) of the solution containing W₂ gram of solute of molecular mass M₂ dissolved in W₁ gram of solvent of molecular mass M₁ is.','اس محلول کی مولیلٹی (m) جس میں سالماتی کمیت M₂ والی محلول شدہ شے کے W₂ گرام سالماتی کمیت M₁ والے محلل کے W₁ گرام میں حل ہوں یہ ہے۔','د هغه محلول مولالیت (m) چې په هغه کې د مالیکولي کتلې M₂ لرونکې محلول شوې مادې W₂ ګرامه د مالیکولي کتلې M₁ لرونکي محلل W₁ ګرامو کې حل وي دا دی.')
add(s,'a6','Substituting the value of "m" in Equation (10.10) we get.','مساوات (10.10) میں "m" کی قیمت رکھنے پر ہمیں ملتا ہے۔','په معادله (10.10) کې د "m" ارزښت ایښودلو سره موږ ترلاسه کوو.')
add(s,'a7','Thus if masses of solute and solvent are known along with ebullioscopic constant and elevation of boiling point then molecular mass of solute can be calculated.','اس طرح اگر محلول شدہ شے اور محلل کی کمیتیں ایبولیوسکوپک مستقلہ اور نقطۂ جوش میں اضافے کے ساتھ معلوم ہوں تو محلول شدہ شے کی سالماتی کمیت کا حساب لگایا جا سکتا ہے۔','په دې توګه که د محلول شوې مادې او محلل کتلې د ایبولیوسکوپیک ثابت او د جوش د نقطې د لوړېدو سره معلومې وي نو د محلول شوې مادې مالیکولي کتله محاسبه کېدای شي.')
head(s,'e5','Example 10.5','مثال 10.5','بېلګه 10.5')
add(s,'q5','The boiling point of 50g of carbon tetrachloride was raised by 0.402 K when 0.5126g of naphthalene (mol.mass = 128g/mol) was dissolved in it. Calculate ebullioscopic constant of carbon tetrachloride.','کاربن ٹیٹرا کلورائیڈ کے 50g کا نقطۂ جوش 0.402 K بڑھ گیا جب اس میں 0.5126g نیفتھلین (سالماتی کمیت = 128g/mol) حل کیا گیا۔ کاربن ٹیٹرا کلورائیڈ کا ایبولیوسکوپک مستقلہ معلوم کریں۔','د 50g کاربن ټیټراکلوراید د جوش نقطه 0.402 K لوړه شوه کله چې په هغې کې 0.5126g نیفتالین (مالیکولي کتله = 128g/mol) حل شو. د کاربن ټیټراکلوراید ایبولیوسکوپیک ثابت محاسبه کړئ.')
head(s,'s5','Solution','حل','حل')
add(s,'s5a','Mass of carbon tetrachloride = W₁ = 50g','کاربن ٹیٹرا کلورائیڈ کی کمیت = W₁ = 50g','د کاربن ټیټراکلوراید کتله = W₁ = 50g')
add(s,'s5b','Mass of naphthalene = W₂ = 0.5126g','نیفتھلین کی کمیت = W₂ = 0.5126g','د نیفتالین کتله = W₂ = 0.5126g')
add(s,'s5c','Molecular mass of naphthalene = M₂ = 128 g mol⁻¹','نیفتھلین کی سالماتی کمیت = M₂ = 128 g mol⁻¹','د نیفتالین مالیکولي کتله = M₂ = 128 g mol⁻¹')
add(s,'s5d','Boiling point elevation ΔT_b = 0.402K','نقطۂ جوش میں اضافہ ΔT_b = 0.402K','د جوش د نقطې لوړېدل ΔT_b = 0.402K')
add(s,'s5e','Ebullioscopic constant = K_b = ?','ایبولیوسکوپک مستقلہ = K_b = ؟','ایبولیوسکوپیک ثابت = K_b = ؟')
add(s,'s5f','As we have','جیسا کہ ہمارے پاس ہے','لکه څنګه چې موږ لرو')
F.p('a1')
F.e('t1',r'\Delta T_b=T_2-T_1','ΔT_b = T₂ − T₁')
F.p('a2')
F.e('e1010',r'\Delta T_b=K_bm\qquad(10.10)','ΔT_b = K_b m   (10.10)')
F.p('a3','a4','a5')
F.e('m',r'm=\frac{W_2}{M_2}\times\frac{1000}{W_1}','m = W₂ / M₂ × 1000 / W₁')
F.p('a6')
F.e('e1011',r'\Delta T_b=K_b\left(\frac{1000\,W_2}{M_2W_1}\right)\qquad(10.11)','ΔT_b = K_b (1000 W₂ / M₂ W₁)   (10.11)')
F.e('e1012',r'M_2=\frac{K_b}{\Delta T_b}\cdot\frac{W_2}{W_1}\cdot1000\qquad(10.12)','M₂ = K_b / ΔT_b · W₂ / W₁ · 1000   (10.12)')
F.p('a7','e5','q5','s5','s5a','s5b','s5c','s5d','s5e','s5f')
F.e('kb',r'K_b=\frac{\Delta T_b\cdot W_1\cdot M_2}{1000\,W_2}','K_b = ΔT_b · W₁ · M₂ / 1000 W₂')
F.done()
s['sourceNote']='Printed folio 315. The first line completes the sentence from the previous page. Eq. (10.11) is garbled on the scan (stray symbols) and is read as ΔT_b = K_b (1000 W₂ / M₂ W₁); Eq. (10.12) is the boxed rearrangement. The Example 10.5 question and solution lines are slightly clipped at the left but legible. The solution continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Eq. 10.11 is garbled on the scan and read from the surrounding derivation; the solution continues on the next page.')
s['vocabulary']={}
save(s)
