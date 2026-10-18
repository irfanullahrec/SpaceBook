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

# ---------- 313 ----------
s=mk(313,'Example 10.2 · Practice Problem 10.3 · 10.2.5 Parts per million, billion, and trillion · Example 10.3','مثال 10.2 · مشقی مسئلہ 10.3 · 10.2.5 فی ملین، فی بلین اور فی ٹریلین حصے · مثال 10.3','بېلګه 10.2 · د تمرین ستونزه 10.3 · 10.2.5 په ملیون، بلیون او ټریلیون برخې · بېلګه 10.3','example102-ppm')
F=Flow(s)
add(s,'a0','independent of temperature. Moreover, concentrations of more than one solutes can easily be expressed by this method.','درجہ حرارت سے آزاد ہے۔ مزید یہ کہ ایک سے زیادہ محلول شدہ اشیاء کے ارتکاز اس طریقے سے آسانی سے ظاہر کیے جا سکتے ہیں۔','د تودوخې څخه خپلواک دی. سربیره پر دې د یوې څخه ډېرو محلول شویو موادو غلظتونه په دې طریقه په اسانۍ ښودل کېدای شي.')
head(s,'e2','Example 10.2','مثال 10.2','بېلګه 10.2')
add(s,'q2','A solution contains 2.0 moles of alcohol and 3.0 moles of water. Calculate mole fractions of alcohol and water.','ایک محلول میں 2.0 مول الکحل اور 3.0 مول پانی ہے۔ الکحل اور پانی کے مول جزو معلوم کریں۔','یو محلول 2.0 مول الکول او 3.0 مول اوبه لري. د الکول او اوبو مول برخې محاسبه کړئ.')
head(s,'s2','Solution','حل','حل')
add(s,'s2a','Number of moles of water: (n₁) = 3.0 moles','پانی کے مولوں کی تعداد: (n₁) = 3.0 مول','د اوبو د مولونو شمېر: (n₁) = 3.0 مولونه')
add(s,'s2b','Number of moles of alcohol: (n₂) = 2.0 moles','الکحل کے مولوں کی تعداد: (n₂) = 2.0 مول','د الکول د مولونو شمېر: (n₂) = 2.0 مولونه')
add(s,'s2c','Mole fraction of water and alcohol are represented by X₁ and X₂ respectively.','پانی اور الکحل کے مول جزو بالترتیب X₁ اور X₂ سے ظاہر کیے جاتے ہیں۔','د اوبو او الکول مول برخې په ترتیب سره د X₁ او X₂ په واسطه ښودل کېږي.')
add(s,'s2d','Formula','فارمولا','فورمول')
head(s,'p3h','Practice problem 10.3','مشقی مسئلہ 10.3','د تمرین ستونزه 10.3')
add(s,'p3','Calculate the mole fraction of methyl alcohol in a solution composed of 1.46 mol of methyl alcohol and 2.19 mol of ethyl alcohol.','ایسے محلول میں میتھائل الکحل کا مول جزو معلوم کریں جو 1.46 مول میتھائل الکحل اور 2.19 مول ایتھائل الکحل پر مشتمل ہو۔','په داسې محلول کې د میتایل الکول مول برخه محاسبه کړئ چې له 1.46 مول میتایل الکول او 2.19 مول ایتایل الکول جوړ وي.')
head(s,'h5','10.2.5 Parts per million, billion, and trillion','10.2.5 فی ملین، فی بلین اور فی ٹریلین حصے','10.2.5 په ملیون، بلیون او ټریلیون برخې')
add(s,'i1','i) Parts per million (ppm)','i) حصے فی ملین (ppm)','i) برخې په ملیون (ppm)',kind='heading')
add(s,'i1t','It is defined as the number of parts (by mass or volume) of a solute per million parts (by mass or volume) of the solution. Parts per million is used for very low concentration of solution. The concentration of impurities of substances in water is expressed by this unit.','اس کی تعریف محلول کے فی ملین حصوں (کمیت یا حجم کے لحاظ سے) میں محلول شدہ شے کے حصوں (کمیت یا حجم کے لحاظ سے) کی تعداد کے طور پر کی جاتی ہے۔ حصے فی ملین محلول کے بہت کم ارتکاز کے لیے استعمال ہوتے ہیں۔ پانی میں مادوں کی ناخالصیوں کا ارتکاز اس یونٹ سے ظاہر کیا جاتا ہے۔','دا د محلول د هر ملیون برخو (د کتلې یا حجم له مخې) کې د محلول شوې مادې د برخو (د کتلې یا حجم له مخې) د شمېر په توګه تعریفېږي. په ملیون برخې د محلول د ډېر ټیټ غلظت لپاره کارول کېږي. په اوبو کې د موادو د ناپاکیو غلظت د دې واحد په واسطه ښودل کېږي.')
head(s,'e3','Example 10.3','مثال 10.3','بېلګه 10.3')
add(s,'q3','Sea water contain 5.65×10⁻³g of dissolved oxygen per kilogram of solution. Calculate the concentration of oxygen in parts per million in sea water.','سمندری پانی میں فی کلوگرام محلول 5.65×10⁻³g حل شدہ آکسیجن ہوتی ہے۔ سمندری پانی میں آکسیجن کا ارتکاز حصے فی ملین میں معلوم کریں۔','د سمندر اوبه په هر کیلوګرام محلول کې 5.65×10⁻³g منحل شوې اکسیجن لري. په سمندري اوبو کې د اکسیجن غلظت په ملیون برخو کې محاسبه کړئ.')
head(s,'s3','Solution','حل','حل')
add(s,'s3a','Mass of solute (dissolved oxygen) = 5.65×10⁻³g','محلول شدہ شے (حل شدہ آکسیجن) کی کمیت = 5.65×10⁻³g','د محلول شوې مادې (منحل شوې اکسیجن) کتله = 5.65×10⁻³g')
add(s,'s3b','Mass of solution = 1kg','محلول کی کمیت = 1kg','د محلول کتله = 1kg')
add(s,'s3c','Concentration of solute in ppm = ?','ppm میں محلول شدہ شے کا ارتکاز = ؟','په ppm کې د محلول شوې مادې غلظت = ؟')
F.p('a0','e2','q2','s2','s2a','s2b','s2c','s2d')
F.e('f1',r'\text{Mole fraction (water) }X_1=\frac{n_1}{n_1+n_2}=\frac{3.0}{3.0+2.0}=\frac{3}{5}','Mole fraction (water) X₁ = n₁ / (n₁ + n₂) = 3.0 / (3.0 + 2.0) = 3/5')
F.e('f2',r'\text{Mole fraction (alcohol) }X_2=\frac{n_2}{n_1+n_2}=\frac{2.0}{3.0+2.0}=\frac{2}{5}','Mole fraction (alcohol) X₂ = n₂ / (n₁ + n₂) = 2.0 / (3.0 + 2.0) = 2/5')
F.p('p3h','p3','h5','i1','i1t')
F.e('ppm',r'\mathrm{ppm}=\frac{\text{mass or vol. of solute}}{\text{mass or vol. of solution}}\times10^{6}','ppm = mass or vol. of solute / mass or vol. of solution × 10⁶')
F.p('e3','q3','s3','s3a','s3b','s3c')
F.done()
s['sourceNote']='Printed folio 308. The first line completes the sentence from the previous page. The right edge is slightly clipped on a few lines but the sentences are legible. The solution to Example 10.3 continues on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Slight right-edge clipping; Example 10.3 solution continues on the next page.')
s['vocabulary']={'parts per million':{'ur':'حصے فی ملین','ps':'په ملیون برخې'}}
save(s)

# ---------- 314 ----------
s=mk(314,'Example 10.3 solution · ii) Parts per billion (ppb) · Example 10.4 · iii) Parts per trillion (ppt)','مثال 10.3 کا حل · ii) حصے فی بلین (ppb) · مثال 10.4 · iii) حصے فی ٹریلین (ppt)','د بېلګې 10.3 حل · ii) برخې په بلیون (ppb) · بېلګه 10.4 · iii) برخې په ټریلیون (ppt)','ppb-ppt')
F=Flow(s)
add(s,'a1','As','چونکہ','لکه څنګه چې')
add(s,'i2','ii) Parts per billion (ppb)','ii) حصے فی بلین (ppb)','ii) برخې په بلیون (ppb)',kind='heading')
add(s,'i2t',f'It is defined as the number of parts (by mass or volume) of a solute per billion parts (by mass or volume) of the solution. Parts per billion is used for very low concentration of solution.','اس کی تعریف محلول کے فی بلین حصوں (کمیت یا حجم کے لحاظ سے) میں محلول شدہ شے کے حصوں (کمیت یا حجم کے لحاظ سے) کی تعداد کے طور پر کی جاتی ہے۔ حصے فی بلین محلول کے بہت کم ارتکاز کے لیے استعمال ہوتے ہیں۔','دا د محلول د هر بلیون برخو (د کتلې یا حجم له مخې) کې د محلول شوې مادې د برخو (د کتلې یا حجم له مخې) د شمېر په توګه تعریفېږي. په بلیون برخې د محلول د ډېر ټیټ غلظت لپاره کارول کېږي.')
head(s,'e4','Example 10.4','مثال 10.4','بېلګه 10.4')
add(s,'q4','A 2.0dm³ gas cylinder contains a mixture of various gases. If 5.0cm³ of H₂ gas is present in this mixture. Calculate the concentration of H₂ gas in parts per billion (ppb).','ایک 2.0dm³ کے گیس سلنڈر میں مختلف گیسوں کا آمیزہ ہے۔ اگر اس آمیزے میں 5.0cm³ H₂ گیس موجود ہو تو H₂ گیس کا ارتکاز حصے فی بلین (ppb) میں معلوم کریں۔','د 2.0dm³ ګاز سلنډر د بېلابېلو ګازونو مخلوط لري. که پدې مخلوط کې 5.0cm³ H₂ ګاز شتون ولري نو د H₂ ګاز غلظت په بلیون برخو (ppb) کې محاسبه کړئ.')
head(s,'s4','Solution','حل','حل')
add(s,'s4a','Volume of H₂ gas = 5.0cm³.','H₂ گیس کا حجم = 5.0cm³۔','د H₂ ګاز حجم = 5.0cm³.')
add(s,'s4b','Volume of cylinder = 2.0 dm³ = (2000 cm³).','سلنڈر کا حجم = 2.0 dm³ = (2000 cm³)۔','د سلنډر حجم = 2.0 dm³ = (2000 cm³).')
add(s,'s4c','Concentration of H₂ gas in ppb = ?','ppb میں H₂ گیس کا ارتکاز = ؟','په ppb کې د H₂ ګاز غلظت = ؟')
add(s,'i3','iii) Parts per trillion (ppt)','iii) حصے فی ٹریلین (ppt)','iii) برخې په ټریلیون (ppt)',kind='heading')
add(s,'i3t','It is defined as the number of parts (by mass or volume) of a solute per trillion parts (by mass or volume) of the solution. Parts per trillion is used for lower concentrations.','اس کی تعریف محلول کے فی ٹریلین حصوں (کمیت یا حجم کے لحاظ سے) میں محلول شدہ شے کے حصوں (کمیت یا حجم کے لحاظ سے) کی تعداد کے طور پر کی جاتی ہے۔ حصے فی ٹریلین کم ارتکازات کے لیے استعمال ہوتے ہیں۔','دا د محلول د هر ټریلیون برخو (د کتلې یا حجم له مخې) کې د محلول شوې مادې د برخو (د کتلې یا حجم له مخې) د شمېر په توګه تعریفېږي. په ټریلیون برخې د ټیټو غلظتونو لپاره کارول کېږي.')
F.p('a1')
F.e('c0',r'\text{Concentration (ppm)}=\frac{\text{mass of dissolved oxygen}}{\text{mass of solution}}\times10^{6}','Concentration (ppm) = mass of dissolved oxygen / mass of solution × 10⁶')
F.e('c1',r'\text{ppm of oxygen}=\frac{5.65\times10^{-3}\ \mathrm{g}}{1000\ \mathrm{g}}\times10^{6}','ppm of oxygen = 5.65×10⁻³ g / 1000 g × 10⁶')
F.e('c2',r'=\frac{5.65\times10^{-3}\ \mathrm{g}}{10^{3}\ \mathrm{g}}\times10^{6}=5.65\ \mathrm{ppm}','= 5.65×10⁻³ g / 10³ g × 10⁶ = 5.65 ppm')
F.p('i2','i2t')
F.e('c3',r'\text{Concentration (ppb)}=\frac{\text{mass or vol. of solute}}{\text{mass or vol. of solution}}\times10^{9}','Concentration (ppb) = mass or vol. of solute / mass or vol. of solution × 10⁹')
F.p('e4','q4','s4','s4a','s4b','s4c')
F.e('c4',r'\text{Concentration (ppb)}=\frac{\text{Vol. of H}_2\text{ in (cm}^3)}{\text{Vol. of solution in (cm}^3)}\times10^{9}','Concentration (ppb) = Vol. of H₂ in (cm³) / Vol. of solution in (cm³) × 10⁹')
F.e('c5',r'\text{Concentration of H}_2\text{ gas in ppb}=\frac{5.0\ \mathrm{cm^3}}{2000\ \mathrm{cm^3}}\times10^{9}','Concentration of H₂ gas in ppb = 5.0 cm³ / 2000 cm³ × 10⁹')
F.e('c6',r'=2.5\times10^{-3}\times10^{9}','= 2.5×10⁻³ × 10⁹')
F.e('c7',r'=2.5\times10^{6}\ \mathrm{ppb}','= 2.5×10⁶ ppb')
F.p('i3','i3t')
F.e('c8',r'\text{Parts per trillion (ppt)}=\frac{\text{mass or volume of solute}}{\text{mass or volume of solution}}\times10^{12}','Parts per trillion (ppt) = mass or volume of solute / mass or volume of solution × 10¹²')
F.done()
s['sourceNote']='Printed folio 309. The left edge is slightly clipped (first letters of the headings "Parts per billion", "Parts per trillion" and of several lines are cut) but the text is legible. A CamScanner watermark crosses the page.'
s['vocabulary']={'parts per billion':{'ur':'حصے فی بلین','ps':'برخې په بلیون'},'parts per trillion':{'ur':'حصے فی ٹریلین','ps':'برخې په ټریلیون'}}
save(s)

# ---------- 315 ----------
s=mk(315,"Self-Assessment · 10.3 Raoult's Law · 10.3.1 Volatile solute and solvent",'خود جائزہ · 10.3 راؤلٹ کا قانون · 10.3.1 اڑنے والی محلول شدہ شے اور محلل','ځان ارزونه · 10.3 د راؤلټ قانون · 10.3.1 الوتونکی محلول شوی مواد او محلل','raoult-law')
F=Flow(s)
add(s,'sa','Self-Assessment','خود جائزہ','ځان ارزونه',kind='heading')
add(s,'sa1','1. In how many ways, percentage of solution can be expressed.','1۔ محلول کی فیصد کتنے طریقوں سے ظاہر کی جا سکتی ہے۔','1. د محلول سلنه په څو لارو ښودل کېدای شي.',role='question')
add(s,'sa2','2. Differentiate between molarity (M) and Molality (m).','2۔ مولریت (M) اور مولیلٹی (m) میں فرق کریں۔','2. د مولاریت (M) او مولالیت (m) ترمنځ توپیر وکړئ.',role='question')
head(s,'h3',"10.3 Raoult's Law",'10.3 راؤلٹ کا قانون','10.3 د راؤلټ قانون')
add(s,'a1',f'When a solid solute dissolves in a solvent, it changes the vapour pressure{SO} of the solvent. Similar effect is observed for a liquid solute in a liquid solvent{SO} However, there is a major difference; a solid solute is usually non-volatile while{SO} liquid solute is volatile. For example, if we analyse the vapour above a sugar{SO} solution in water, we would find only water vapours, whereas, the vapours above{SO} a solution of ethanol and water always contain both water and ethanol.',f'جب ٹھوس محلول شدہ شے کسی محلل میں حل ہوتی ہے تو وہ محلل کا بخارات دباؤ بدل دیتی ہے {SO}۔ مائع محلل میں مائع محلول شدہ شے کے لیے بھی ایسا ہی اثر مشاہدہ کیا جاتا ہے {SO}۔ تاہم ایک بڑا فرق ہے؛ ٹھوس محلول شدہ شے عموماً غیر اڑنے والی ہوتی ہے جبکہ {SO} مائع محلول شدہ شے اڑنے والی ہوتی ہے۔ مثال کے طور پر اگر ہم پانی میں چینی کے محلول کے اوپر بخارات کا تجزیہ کریں {SO} تو ہمیں صرف پانی کے بخارات ملیں گے، جبکہ ایتھانول اور پانی کے محلول کے اوپر کے بخارات {SO} میں ہمیشہ پانی اور ایتھانول دونوں ہوتے ہیں۔',f'کله چې یو جامد محلول شوی مواد په محلل کې حل شي نو د محلل د بخار فشار بدلوي {SO}. ورته اغېز په مایع محلل کې د مایع محلول شوې مادې لپاره هم لیدل کېږي {SO}. خو یو لوی توپیر شته؛ جامد محلول شوی مواد معمولاً غیر الوتونکی دی پداسې حال کې چې {SO} مایع محلول شوی مواد الوتونکی دی. د بېلګې په توګه که موږ په اوبو کې د بورې د محلول پورته بخار تحلیل کړو {SO} نو موږ به یوازې د اوبو بخارونه ومومو، پداسې حال کې چې د ایتانول او اوبو د محلول پورته بخارونه {SO} تل اوبه او ایتانول دواړه لري.')
add(s,'a2',f'This fact allows us to classify the solutions on the basis of solutes i.e. (i) the{SO} solution of volatile solute and solvent and (ii) the solution of non-volatile and non{SO} electrolyte solute in volatile solvent.',f'یہ حقیقت ہمیں محلول شدہ اشیاء کی بنیاد پر محلولوں کی درجہ بندی کرنے دیتی ہے یعنی (i) {SO} اڑنے والی محلول شدہ شے اور محلل کا محلول اور (ii) غیر اڑنے والی اور غیر {SO} برق پاش محلول شدہ شے کا اڑنے والے محلل میں محلول۔',f'دا حقیقت موږ ته اجازه راکوي چې محلولونه د محلول شویو موادو په بنسټ طبقه بندي کړو یعنې (i) {SO} د الوتونکي محلول شوې مادې او محلل محلول او (ii) د غیر الوتونکي او غیر {SO} الکترولایټ محلول شوې مادې په الوتونکي محلل کې محلول.')
add(s,'a3',f"The quantitative relationship between the vapour pressure of solution{SO} composition of components of solution was given by F. M. Raoult. The Raoult{SO} law states that the partial vapour pressure of any volatile component of{SO} solution is equal to the vapour pressure of the pure component multiplied by{SO} mole fraction of that component in solution. Those solutions which obey Raoult{SO} law are called ideal solutions.",f"محلول کے بخارات دباؤ اور محلول کے اجزاء کی ترکیب کے درمیان مقداری تعلق ایف ایم راؤلٹ نے دیا {SO}۔ راؤلٹ کا قانون کہتا ہے کہ محلول کے کسی بھی اڑنے والے جزو کا جزوی بخارات دباؤ {SO} خالص جزو کے بخارات دباؤ کو محلول میں اس جزو کے مول جزو سے ضرب دینے کے برابر ہوتا ہے {SO}۔ وہ محلول جو راؤلٹ کے قانون کی پیروی کرتے ہیں مثالی محلول کہلاتے ہیں {SO}۔",f"د محلول د بخار فشار او د محلول د اجزاوو د جوړښت ترمنځ کمیتي اړیکه د اف ایم راؤلټ په واسطه ورکړل شوه {SO}. د راؤلټ قانون وايي چې د محلول د هر الوتونکي جز جزوي بخار فشار {SO} د خالص جز د بخار فشار سره چې په محلول کې د هغه جز په مول برخه ضرب شوی مساوي دی {SO}. هغه محلولونه چې د راؤلټ قانون تعقیبوي ایډیال محلولونه بلل کېږي {SO}.")
add(s,'a4',f"Mathematically, Raoult's law can be written as P = P°X where P and P°{SO} the partial vapour pressure of the component and that of the pure compo{SO} respectively, and X is the mole fraction of the component in the solution.",f"ریاضیاتی طور پر راؤلٹ کا قانون P = P°X لکھا جا سکتا ہے جہاں P اور P° {SO} جزو کا جزوی بخارات دباؤ اور خالص جزو کا بخارات دباؤ بالترتیب ہیں {SO}، اور X محلول میں جزو کا مول جزو ہے۔",f"ریاضیاتي ډول د راؤلټ قانون P = P°X لیکل کېدای شي چېرته چې P او P° {SO} د جز جزوي بخار فشار او د خالص جز بخار فشار په ترتیب سره دي {SO}، او X په محلول کې د جز مول برخه ده.")
head(s,'h31','10.3.1 The solution of Volatile Solute and Solvent (both components are volatile)','10.3.1 اڑنے والی محلول شدہ شے اور محلل کا محلول (دونوں اجزاء اڑنے والے)','10.3.1 د الوتونکي محلول شوې مادې او محلل محلول (دواړه اجزا الوتونکي)')
add(s,'b1',f'Consider an ideal solution of two liquids A and B. According to Raoult{SO} law partial vapour pressure of both components A and B is given by:',f'دو مائعات A اور B کے ایک مثالی محلول پر غور کریں۔ راؤلٹ {SO} کے قانون کے مطابق دونوں اجزاء A اور B کا جزوی بخارات دباؤ اس سے دیا جاتا ہے:',f'د دوو مایعاتو A او B یو ایډیال محلول ته پام وکړئ. د راؤلټ {SO} د قانون له مخې د دواړو اجزاوو A او B جزوي بخار فشار په لاندې ډول ورکول کېږي:')
add(s,'b2',f'P°_A is the vapour pressure of pure component A and P°_B is vapour pres{SO} of pure component B. X_A and X_B are the mole fractions of components A a{SO} respectively. By applying Dalton\'s law of partial pressures, vapour pres{SO} solution is',f'P°_A خالص جزو A کا بخارات دباؤ ہے اور P°_B خالص جزو B کا بخارات دباؤ {SO} ہے۔ X_A اور X_B بالترتیب اجزاء A اور B کے مول جزو ہیں {SO}۔ ڈالٹن کے قانونِ جزوی دباؤ کے اطلاق سے محلول کا بخارات دباؤ {SO} ہے',f'P°_A د خالص جز A بخار فشار دی او P°_B د خالص جز B بخار فشار {SO} دی. X_A او X_B په ترتیب سره د اجزاوو A او B مول برخې دي {SO}. د ډالټن د جزوي فشارونو د قانون په تطبیق سره د محلول بخار فشار {SO} دی')
F.p('sa','sa1','sa2','h3','a1','a2','a3','a4','h31','b1')
F.e('pa',r'P_A=P_A^{\circ}X_A','P_A = P°_A X_A')
F.e('pb',r'P_B=P_B^{\circ}X_B','P_B = P°_B X_B')
F.p('b2')
F.e('pt',r'P_{Total}=P_A+P_B','P_Total = P_A + P_B')
F.e('e101',r'P_t=P_A^{\circ}X_A+P_B^{\circ}X_B\qquad(10.1)','P_t = P°_A X_A + P°_B X_B   (10.1)')
F.done()
s['sourceNote']='Printed folio 310. The right edge is clipped by the page curl on nearly every line of text from 10.3 downward; clipped endings are marked [scan obscured] and not inferred. The pink italic statement of Raoult\'s law is partly cut. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping throughout.')
s['vocabulary']={"raoult's law":{'ur':'راؤلٹ کا قانون','ps':'د راؤلټ قانون'},'ideal solutions':{'ur':'مثالی محلول','ps':'ایډیال محلولونه'},'volatile':{'ur':'اڑنے والا','ps':'الوتونکی'},'vapour pressure':{'ur':'بخارات دباؤ','ps':'بخار فشار'}}
save(s)

# ---------- 316 ----------
s=mk(316,'Equations for Raoult\'s law · Figure 10.2 · 10.3.2 Non-Volatile and Non-Electrolyte Solute in Volatile Solvent','راؤلٹ کے قانون کی مساواتیں · شکل 10.2 · 10.3.2 اڑنے والے محلل میں غیر اڑنے والی اور غیر برق پاش محلول شدہ شے','د راؤلټ قانون معادلې · شکل 10.2 · 10.3.2 په الوتونکي محلل کې غیر الوتونکی او غیر الکترولایټ محلول شوی مواد','raoult-equations-fig')
F=Flow(s)
add(s,'a1','Since X_A + X_B = 1','چونکہ X_A + X_B = 1','ځکه چې X_A + X_B = 1')
add(s,'a2','Therefore X_A = (1 − X_B)','لہٰذا X_A = (1 − X_B)','نو X_A = (1 − X_B)')
add(s,'a3','The eq. (10.1) becomes','مساوات (10.1) بن جاتی ہے','معادله (10.1) کېږي')
add(s,'a4','On rearranging the above equation.','مندرجہ بالا مساوات کو دوبارہ ترتیب دینے پر۔','پورتنۍ معادله بیا ترتیبولو سره.')
add(s,'a5','This equation shows that when X_B = 0, X_A = 1 it means pure component A is present and P_Total becomes equal to P°_A and if X_A = 0, then X_B = 1 then pure component B is present, then P_Total becomes equal to P°_B.','یہ مساوات ظاہر کرتی ہے کہ جب X_B = 0، X_A = 1 ہو تو اس کا مطلب ہے کہ خالص جزو A موجود ہے اور P_Total، P°_A کے برابر ہو جاتا ہے اور اگر X_A = 0، تو X_B = 1 تو خالص جزو B موجود ہے، تب P_Total، P°_B کے برابر ہو جاتا ہے۔','دا معادله ښيي چې کله X_B = 0، X_A = 1 وي نو دا معنا لري چې خالص جز A شتون لري او P_Total له P°_A سره مساوي کېږي او که X_A = 0، نو X_B = 1 نو خالص جز B شتون لري، بیا P_Total له P°_B سره مساوي کېږي.')
add(s,'a6','The graph in Fig. 10.3 shows variation of total pressure (solid line) and partial vapour pressures of components (dotted lines) of solution with changes in concentration of both A and B components. At any concentration, the total pressure is the sum of the partial pressures of the two components.','شکل 10.3 کا گراف محلول کے کل دباؤ (ٹھوس لکیر) اور اجزاء کے جزوی بخارات دباؤ (نقطہ دار لکیریں) کی A اور B دونوں اجزاء کے ارتکاز میں تبدیلی کے ساتھ تبدیلی ظاہر کرتا ہے۔ کسی بھی ارتکاز پر کل دباؤ دونوں اجزاء کے جزوی دباؤ کا مجموعہ ہوتا ہے۔','د 10.3 شکل ګراف د محلول د ټول فشار (جامده کرښه) او د اجزاوو د جزوي بخار فشارونو (ټکي کرښې) بدلون د A او B دواړو اجزاوو د غلظت په بدلون سره ښيي. په هر غلظت کې ټول فشار د دواړو اجزاوو د جزوي فشارونو مجموعه ده.')
head(s,'h2','10.3.2 Non-Volatile and Non-Electrolyte Solute in Volatile Solvent','10.3.2 اڑنے والے محلل میں غیر اڑنے والی اور غیر برق پاش محلول شدہ شے','10.3.2 په الوتونکي محلل کې غیر الوتونکی او غیر الکترولایټ محلول شوی مواد')
add(s,'b1',f'In the case of solution of non-electrolyte and non-volatile solute the{SO} solute particles remain in the (un-dissociated) molecular form. Such solute lowers{SO} the vapour pressure of the solvent. The vapour pressure lowering, suffered by the{SO} solvent, can be readily understood in terms of Raoult\'s law.',f'غیر برق پاش اور غیر اڑنے والی محلول شدہ شے کے محلول کی صورت میں {SO} محلول شدہ شے کے ذرات (غیر تفکیک شدہ) سالماتی شکل میں رہتے ہیں۔ ایسی محلول شدہ شے محلل کا بخارات دباؤ کم کرتی ہے {SO}۔ محلل کو پہنچنے والی بخارات دباؤ کی کمی راؤلٹ کے قانون کے لحاظ سے آسانی سے سمجھی جا سکتی ہے {SO}۔',f'د غیر الکترولایټ او غیر الوتونکي محلول شوې مادې د محلول په حالت کې {SO} د محلول شوې مادې ذرات په (نه تجزیه شوې) مالیکولي بڼه کې پاتې کېږي. داسې محلول شوی مواد د محلل بخار فشار کموي {SO}. د بخار فشار کمښت چې محلل ته رسېږي د راؤلټ د قانون په اړه په اسانۍ سره پوهېدای شي {SO}.')
add(s,'b2',f'Let us consider a solution of component A and B where A is solvent of mole fraction X₁ and B is solute of mole fraction X₂. P° is the vapour pressure of{SO}',f'آئیے اجزاء A اور B کے ایک محلول پر غور کریں جہاں A محلل ہے جس کا مول جزو X₁ ہے اور B محلول شدہ شے ہے جس کا مول جزو X₂ ہے۔ P° کا بخارات دباؤ {SO} ہے',f'راځئ د اجزاوو A او B یو محلول ته پام وکړو چېرته چې A محلل دی چې مول برخه یې X₁ ده او B محلول شوی مواد دی چې مول برخه یې X₂ ده. P° د {SO} بخار فشار دی')
def ax(): return '<path d="M30 20 V210 H300" stroke="#222" stroke-width="2" fill="none"/><path d="M296 205 L302 210 L296 215" fill="none" stroke="#222"/>'
g=(ax()+'<path d="M30 70 L300 40" stroke="#c0305a" stroke-width="2" fill="none"/>'+'<path d="M30 70 L300 205" stroke="#222" stroke-dasharray="5 4" fill="none"/>'+'<path d="M30 205 L300 40" stroke="#222" stroke-dasharray="5 4" fill="none"/>'
 +tx(100,28,'T = constant',10,'start',700)+tx(25,72,"P°<tspan font-size='7' dy='3'>A</tspan>",10,'end',700)+tx(305,38,"P°<tspan font-size='7' dy='3'>B</tspan>",10,'start',700)
 +tx(150,52,'P total',10,'start',700)+tx(60,95,'P<tspan font-size="7" dy="3">A</tspan>',10,'start',700)+tx(240,100,'P<tspan font-size="7" dy="3">B</tspan>',10,'start',700)
 +tx(30,232,'X<tspan font-size="7" dy="3">A</tspan> → 1',10,'start')+tx(30,246,'X<tspan font-size="7" dy="3">B</tspan> → 0',10,'start')+tx(190,236,'← Composition →',11,'middle',700,'#c0305a')+tx(300,222,'0',10)+tx(300,236,'1',10)
 +tx(170,268,'Figure 10.2: Variation of vapour pressure of solution with a change in concentration of A and B',11,'middle',700,'#a02040'))
s['figures']=[fig(316,'fig10-2',svg(340,280,'Graph of total and partial vapour pressures against composition for an ideal solution of A and B',g),'Figure 10.2: Variation of vapour pressure of solution with a change in concentration of A and B','شکل 10.2 A اور B کے ارتکاز میں تبدیلی کے ساتھ محلول کے بخارات دباؤ میں تبدیلی','شکل 10.2 د A او B د غلظت په بدلون سره د محلول د بخار فشار بدلون',[lab('P total','کل دباؤ','ټول فشار'),lab('PA','PA','PA'),lab('PB','PB','PB'),lab('Composition','ترکیب','جوړښت'),lab('T = constant','T = مستقل','T = ثابت')])]
s['figures'][0]['sourceGap']=dict(note='Graph redrawn as a schematic from its visible lines. The text calls this figure "Fig. 10.3" while the printed caption reads "Figure 10.2"; both retained as printed.')
F.p('a1','a2')
F.p('a3')
F.e('e1',r'P_t=P_A^{\circ}(1-X_B)+P_B^{\circ}X_B','P_t = P°_A (1 − X_B) + P°_B X_B')
F.e('e2',r'P_t=P_A^{\circ}-P_A^{\circ}X_B+P_B^{\circ}X_B','P_t = P°_A − P°_A X_B + P°_B X_B')
F.p('a4')
F.e('e3',r'P_t=\left(P_B^{\circ}-P_A^{\circ}\right)X_B+P_A^{\circ}','P_t = (P°_B − P°_A) X_B + P°_A')
F.p('a5','a6')
F.fg(0)
F.p('h2','b1','b2')
F.done()
s['sourceNote']='Printed folio 311. The text refers to "Fig. 10.3" while the printed caption reads "Figure 10.2"; both retained. The left edge is slightly clipped but legible; the last sentence is cut at the right ("P° is the vapour pressure of …") and continues on the next page. In the last printed rearranged equation the final term is partly cut ("+ P°…"); the completion P°_A is read from the sentence below it. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Figure number mismatch (10.3 vs 10.2) retained; last sentence continues on the next page.')
s['vocabulary']={'non-electrolyte':{'ur':'غیر برق پاش','ps':'غیر الکترولایټ'},'non-volatile':{'ur':'غیر اڑنے والا','ps':'غیر الوتونکی'}}
save(s)
