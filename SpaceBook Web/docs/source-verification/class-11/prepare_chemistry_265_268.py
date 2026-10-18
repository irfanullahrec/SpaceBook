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
CH='chem11-acids-bases-salts'
def mk(n,title,ur,ps,sid): return page(n,CH,title,ur,ps,sid)
def tx(x,y,t,size=18,anchor='start',w=400,fill='#111'): return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-weight="{w}" fill="{fill}">{t}</text>'
arrow=lambda x1,x2,y: f'<path d="M{x1} {y} H{x2}" stroke="#111" stroke-width="2"/><path d="M{x2-9} {y-5} L{x2} {y} L{x2-9} {y+5}" fill="none" stroke="#111" stroke-width="2"/>'

# ---------- 265 ----------
s=mk(265,'Buffer action of NH₄OH/NH₄Cl · Applications of Buffers · Tidbit: Salt','NH₄OH/NH₄Cl کا بفر عمل · بفروں کے اطلاقات · معلومات: نمک','د NH₄OH/NH₄Cl د بفر عمل · د بفرونو کارونې · ځانګړې یادونه: مالګه','buffer-applications-salt')
F=Flow(s)
dg=(tx(20,40,'Addition of H⁺',14)+arrow(150,300,35)+tx(310,40,'H₂O',14)+'<rect x="20" y="55" width="330" height="140" fill="none" stroke="#c0305a" stroke-width="2"/>'+tx(35,95,'NH₄OH',16)+'<path d="M120 88 H170 M120 96 H170" stroke="#111" stroke-width="2"/>'+tx(185,95,'OH⁻ + NH₄⁺',16)+tx(35,170,'NH₄Cl',16)+'<path d="M120 163 H170 M120 171 H170" stroke="#111" stroke-width="2"/>'+tx(185,170,'NH₄⁺ + Cl⁻',16)+tx(20,230,'Addition of OH⁻',14)+arrow(150,300,225)+tx(310,230,'NH₄OH',14))
s['figures']=[fig(265,'diag',svg(420,250,'Buffer action diagram for NH4OH and NH4Cl: added H plus combines with hydroxide to form water, added hydroxide combines with ammonium to form ammonium hydroxide',dg),'Buffer action of the NH₄OH/NH₄Cl system','NH₄OH/NH₄Cl نظام کا بفر عمل','د NH₄OH/NH₄Cl سیسټم د بفر عمل',[lab('Addition of H⁺','H⁺ کا اضافہ','د H⁺ اضافه کول'),lab('Addition of OH⁻','OH⁻ کا اضافہ','د OH⁻ اضافه کول')])]
s['figures'][0]['sourceGap']=dict(note='Diagram redrawn as a schematic; connecting bracket lines are simplified.')
head(s,'h','Applications of Buffers','بفروں کے اطلاقات','د بفرونو کارونې')
add(s,'a1',f'i. The use of buffers is important in some industrial processes, which wou{SO} be interrupted by large change in pH. Examples are manufacture{SO} leather, photographic materials and dyes.',f'i. بعض صنعتی عمل میں بفروں کا استعمال اہم ہے، جو {SO} pH میں بڑی تبدیلی سے متاثر ہوں گے۔ مثالیں چمڑے، فوٹوگرافی کے سامان اور رنگوں کی تیاری ہیں {SO}۔',f'i. په ځینو صنعتي پروسو کې د بفرونو کارول مهم دی، چې {SO} د pH په لوی بدلون سره به ګډوډې شي. بېلګې د څرمن، عکاسۍ توکو او رنګونو جوړول دي {SO}.')
add(s,'a2',f'ii. In bacteriological research, culture media are generally buffered{SO} maintain a constant pH required for the growth of the bacteria bei{SO} studied.',f'ii. جراثیمیاتی تحقیق میں کلچر میڈیا عموماً بفر کیے جاتے ہیں {SO} تاکہ زیرِ مطالعہ جراثیم کی نشوونما کے لیے درکار مستقل pH برقرار رہے {SO}۔',f'ii. په باکتریولوژیکي څېړنه کې کلچر میډیا معمولاً بفر کېږي {SO} ترڅو د مطالعې لاندې باکتریاوو د ودې لپاره اړین ثابت pH وساتي {SO}.')
add(s,'a3',f'iii. Buffer is important in biological systems because biological reactions{SO} both plants and animals are often very sensitive to pH changes. Hum{SO} blood is buffered to a pH of 7.4 by means of bicarbonates, phosphat{SO} and complex protein systems.',f'iii. بفر حیاتیاتی نظاموں میں اہم ہے کیونکہ حیاتیاتی تعاملات {SO} پودوں اور جانوروں دونوں میں اکثر pH کی تبدیلیوں کے لیے بہت حساس ہوتے ہیں۔ انسانی {SO} خون بائی کاربونیٹس، فاسفیٹس {SO} اور پیچیدہ پروٹین نظاموں کے ذریعے 7.4 کے pH پر بفر کیا جاتا ہے۔',f'iii. بفر په ژوندیو سیسټمونو کې مهم دی ځکه چې ژوندي تعاملات {SO} په بوټو او څارویو دواړو کې ډېری وخت د pH بدلونونو ته ډېر حساس وي. د انسان {SO} وینه د بایکاربونیټونو، فاسفیټونو {SO} او پیچلو پروټین سیسټمونو په واسطه په 7.4 pH کې بفر کېږي.')
add(s,'a4',f'iv. Protein studies must be performed in buffered media because t{SO} magnitude and kind of electrical charge carried by protein molecul{SO} depend on the pH.',f'iv. پروٹین کے مطالعات بفر شدہ میڈیا میں کیے جانے چاہئیں کیونکہ {SO} پروٹین کے سالموں پر موجود برقی چارج کی مقدار اور نوعیت {SO} pH پر منحصر ہوتی ہے۔',f'iv. د پروټین مطالعات باید په بفر شویو میډیا کې ترسره شي ځکه چې {SO} د پروټین مالیکولونو لخوا وړل شوي برېښنايي چارج اندازه او ډول {SO} د pH پورې اړه لري.')
add(s,'rc-h','Reading Check','مطالعہ کی جانچ','د لوستلو ازموینه',kind='heading')
add(s,'rc1','What is buffer solution?','بفر محلول کیا ہے؟','بفر محلول څه دی؟',role='question')
add(s,'t-h','Tidbit','معلومات','ځانګړې یادونه',kind='heading')
add(s,'t0','Salt','نمک','مالګه',kind='heading')
add(s,'t1',f'A salt is formed when a base is neutralized by an acid. A salt consists of{SO} metallic and acidic radical. Examples are NaCl, NaNO₃, Na₂SO₄, KCl etc','نمک اس وقت بنتا ہے جب کسی اساس کو تیزاب سے معتدل کیا جائے۔ نمک دھاتی اور تیزابی جزو پر مشتمل ہوتا ہے۔ مثالیں NaCl، NaNO₃، Na₂SO₄، KCl وغیرہ ہیں۔','مالګه هغه مهال جوړېږي کله چې یو القلي د اسید په واسطه خنثی شي. مالګه له فلزي او اسیدي رادیکال څخه جوړه وي. بېلګې NaCl، NaNO₃، Na₂SO₄، KCl او نور دي.')
add(s,'t2','Salt are prepared by the following methods.','نمک درج ذیل طریقوں سے تیار کیے جاتے ہیں۔','مالګې په لاندې طریقو جوړېږي.')
add(s,'t3','Neutralization of a base by an acid.','اساس کا تیزاب کے ذریعے تعدیل۔','د القلي خنثی کول د اسید په واسطه.')
add(s,'t4','Reaction of an acid with a reactive metal','تیزاب کا ایک فعال دھات کے ساتھ تعامل','د اسید تعامل له یوه فعال فلز سره')
add(s,'t5','Reaction of an acid with carbonate (CO₃²⁻) or bicarbonate (HCO₃⁻)','تیزاب کا کاربونیٹ (CO₃²⁻) یا بائی کاربونیٹ (HCO₃⁻) کے ساتھ تعامل','د اسید تعامل له کاربونیټ (CO₃²⁻) یا بایکاربونیټ (HCO₃⁻) سره')
F.fg(0)
F.p('h','a1','a2','a3','a4','rc-h','rc1','t-h','t0','t1','t2','t3')
F.e('s1',r'\mathrm{HCl_{(aq)}+NaOH_{(aq)}\longrightarrow NaCl_{(aq)}+H_2O_{(aq)}}','HCl(aq) + NaOH(aq) → NaCl(aq) + H₂O(aq)')
F.p('t4')
F.e('s2',r'\mathrm{Zn+H_2SO_4\longrightarrow ZnSO_4+H_2}','Zn + H₂SO₄ → ZnSO₄ + H₂')
F.p('t5')
F.done()
s['sourceNote']='Printed folio 260. The right edge is clipped by the page curl on the numbered applications and the first Tidbit line; clipped endings are marked [scan obscured] and not inferred. The last line ("Reaction of an acid with carbonate … or bicarbonate …") continues with its equation on the next page. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping; diagram redrawn as a schematic; equation for the last method continues on the next page.')
s['vocabulary']={'salt':{'ur':'نمک','ps':'مالګه'}}
save(s)

# ---------- 266 ----------
s=mk(266,'Preparation of salts (continued) · 8.7 Salt Hydrolysis','نمکوں کی تیاری (جاری) · 8.7 نمک کی آبپاشیدگی (ہائیڈرولائسس)','د مالګو جوړول (دوام) · 8.7 د مالګې هایدرولیز','salt-hydrolysis')
F=Flow(s)
add(s,'a1','Reaction of soluble salts to produce insoluble salts','حل پذیر نمکوں کا تعامل جس سے غیر حل پذیر نمک بنتے ہیں','د حل کېدونکو مالګو تعامل چې غیر حل کېدونکې مالګې جوړوي')
add(s,'a2','Direct combination of a gas with metal','گیس کا دھات کے ساتھ براہِ راست اتصال','د ګاز مستقیم یوځای کېدل له فلز سره')
head(s,'h87','8.7 Salt Hydrolysis','8.7 نمک کی ہائیڈرولائسس','8.7 د مالګې هایدرولیز')
add(s,'b1','A salt is an ionic compound formed by the reaction between an acid and a base. Some salts are strong electrolytes that completely dissociate in water and in some cases partially dissociate in water.','نمک ایک آئنی مرکب ہے جو تیزاب اور اساس کے درمیان تعامل سے بنتا ہے۔ کچھ نمک مضبوط برق پاش ہیں جو پانی میں مکمل طور پر تفکیک ہو جاتے ہیں اور بعض صورتوں میں پانی میں جزوی طور پر تفکیک ہوتے ہیں۔','مالګه یو آیوني مرکب دی چې د اسید او القلي ترمنځ تعامل په واسطه جوړېږي. ځینې مالګې قوي الکترولایټونه دي چې په اوبو کې په بشپړ ډول تجزیه کېږي او په ځینو حالاتو کې په اوبو کې په جزوي ډول تجزیه کېږي.')
add(s,'b2','The term salt hydrolysis describes the reaction of an anion or a cation or both the ions of a salt with water to produce acidic, basic or neutral solutions.','نمک کی ہائیڈرولائسس کی اصطلاح نمک کے اینائن یا کیٹائن یا دونوں آئنوں کے پانی کے ساتھ تعامل کو بیان کرتی ہے جس سے تیزابی، اساسی یا معتدل محلول بنتے ہیں۔','د مالګې د هایدرولیز اصطلاح د مالګې د انیاین یا کیټاین یا دواړو آیونونو له اوبو سره تعامل بیانوي چې اسیدي، القلي یا خنثی محلولونه جوړوي.')
add(s,'b3','Hydrolysis is defined as, the reaction of an anion or cation with water accompanied by cleavage of H–O–H bond.','ہائیڈرولائسس کی تعریف اس طرح کی جاتی ہے کہ کسی اینائن یا کیٹائن کا پانی کے ساتھ تعامل جس کے ساتھ H–O–H بندھن ٹوٹتا ہے۔','هایدرولیز داسې تعریفېږي چې د یو انیاین یا کیټاین تعامل له اوبو سره چې د H–O–H بند د ماتېدو سره مل وي.')
add(s,'b4','When a salt is dissolved in water, it is dissociated into positive and negative ions. These ions separately react with water by breaking the H–OH bond. As a result, an acidic or basic solution is formed depending upon the nature of the dissolved salt.','جب نمک پانی میں حل ہوتا ہے تو وہ مثبت اور منفی آئنوں میں تفکیک ہو جاتا ہے۔ یہ آئن الگ الگ H–OH بندھن توڑ کر پانی کے ساتھ تعامل کرتے ہیں۔ نتیجتاً حل شدہ نمک کی نوعیت کے مطابق تیزابی یا اساسی محلول بنتا ہے۔','کله چې مالګه په اوبو کې حل شي نو دا په مثبتو او منفي آیونونو تجزیه کېږي. دا آیونونه جلا جلا د H–OH بند په ماتولو سره له اوبو سره تعامل کوي. په پایله کې د منحل شوې مالګې د ماهیت له مخې اسیدي یا القلي محلول جوړېږي.')
add(s,'b5','It may be noted that in anionic hydrolysis the solution becomes slightly basic due to the generation of excess OH⁻ ions.','یہ نوٹ کیا جا سکتا ہے کہ اینائنی ہائیڈرولائسس میں زائد OH⁻ آئنوں کے پیدا ہونے کی وجہ سے محلول قدرے اساسی ہو جاتا ہے۔','دا یادونه کېدای شي چې په انیاني هایدرولیز کې د زیاتو OH⁻ آیونونو د جوړېدو له امله محلول لږ القلي کېږي.')
add(s,'b6','In cationic hydrolysis, there is excess of H⁺ ions, which makes the solution slightly acidic.','کیٹائنی ہائیڈرولائسس میں H⁺ آئنوں کی زیادتی ہوتی ہے جو محلول کو قدرے تیزابی بنا دیتی ہے۔','په کیټاني هایدرولیز کې د H⁺ آیونونو زیاتوالی وي چې محلول لږ اسیدي کوي.')
F.e('s3',r'\mathrm{Na_2CO_3+2HCl\longrightarrow 2NaCl+H_2O+CO_2}','Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂')
F.p('a1')
F.e('s4',r'\mathrm{AgNO_3+NaCl\longrightarrow AgCl+NaNO_3}','AgNO₃ + NaCl → AgCl + NaNO₃')
F.p('a2')
F.e('s5',r'\mathrm{2Na+Cl_2\longrightarrow 2NaCl}','2Na + Cl₂ → 2NaCl')
F.p('h87','b1','b2','b3','b4','b5')
F.e('an',r'\mathrm{A^-}+\mathrm{H{-}O{-}H}\rightleftharpoons\mathrm{HA}+\mathrm{OH^-}','A⁻ + H–O–H ⇌ HA + OH⁻')
F.p('b6')
F.e('ca',r'\mathrm{B^+}+\mathrm{H{-}O{-}H}\rightleftharpoons\mathrm{BOH}+\mathrm{H^+}','B⁺ + H–O–H ⇌ BOH + H⁺')
F.done()
s['sourceNote']='Printed folio 261. The first equation (Na₂CO₃ + 2HCl → …) completes the "Reaction of an acid with carbonate or bicarbonate" item from the previous page. The left edge is slightly clipped (first letters of several lines of 8.7 are cut) but the sentences are legible. The two hydrolysis diagrams (wavy bond-cleavage lines and bracket arrows) are reduced to their equations. A CamScanner watermark crosses the page.'
s['vocabulary']={'hydrolysis':{'ur':'ہائیڈرولائسس','ps':'هایدرولیز'},'anionic hydrolysis':{'ur':'اینائنی ہائیڈرولائسس','ps':'انیاني هایدرولیز'},'cationic hydrolysis':{'ur':'کیٹائنی ہائیڈرولائسس','ps':'کیټاني هایدرولیز'}}
save(s)

# ---------- 267 ----------
s=mk(267,'Types of salts by hydrolytic behaviour · Weak acid/strong base · Weak base/strong acid · Tidbit: Hydration and Hydrolysis','نمکوں کی ہائیڈرولائسس کے لحاظ سے اقسام · کمزور تیزاب/مضبوط اساس · کمزور اساس/مضبوط تیزاب · معلومات: آبیدگی اور ہائیڈرولائسس','د مالګو ډولونه د هایدرولیز له مخې · ضعیف اسید/قوي القلي · ضعیف القلي/قوي اسید · ځانګړې یادونه: هایدریشن او هایدرولیز','salt-types')
F=Flow(s)
add(s,'a0',f'The different salts may be classified into the following types accordin{SO} their hydrolytic behaviour:',f'مختلف نمکوں کو ان کے ہائیڈرولائسس رویے کے مطابق درج ذیل اقسام میں تقسیم کیا جا سکتا ہے {SO}:',f'بېلابېلې مالګې د هغوی د هایدرولیز چلند له مخې په لاندې ډولونو ویشل کېدای شي {SO}:')
add(s,'a1','(1) Salts of weak acids and strong bases','(1) کمزور تیزابوں اور مضبوط اساسوں کے نمک','(1) د ضعیفو اسیدونو او قوي القليو مالګې')
add(s,'a2','(2) Salts of weak bases and strong acids','(2) کمزور اساسوں اور مضبوط تیزابوں کے نمک','(2) د ضعیفو القليو او قوي اسیدونو مالګې')
add(s,'a3','(3) Salts of weak acids and weak bases','(3) کمزور تیزابوں اور کمزور اساسوں کے نمک','(3) د ضعیفو اسیدونو او ضعیفو القليو مالګې')
add(s,'a4','(4) Salts of strong acids and strong bases.','(4) مضبوط تیزابوں اور مضبوط اساسوں کے نمک۔','(4) د قوي اسیدونو او قوي القليو مالګې.')
head(s,'h1','1. Salts of Weak Acids and Strong Bases','1۔ کمزور تیزابوں اور مضبوط اساسوں کے نمک','1. د ضعیفو اسیدونو او قوي القليو مالګې')
add(s,'b1',f'When a salt of weak acid (CH₃COOH) and strong base (NaOH), for example, sodium acetate (CH₃COONa) is dissolved in water. It ionizes in aqueous{SO} solution, into CH₃COO⁻ and Na⁺.',f'جب کمزور تیزاب (CH₃COOH) اور مضبوط اساس (NaOH) کا نمک، مثلاً سوڈیم ایسیٹیٹ (CH₃COONa) پانی میں حل کیا جاتا ہے تو وہ آبی {SO} محلول میں CH₃COO⁻ اور Na⁺ میں آئنائز ہو جاتا ہے۔',f'کله چې د ضعیف اسید (CH₃COOH) او قوي القلي (NaOH) مالګه، د بېلګې په توګه سوډیم اسیټیټ (CH₃COONa) په اوبو کې حل شي. دا په اوبیز {SO} محلول کې په CH₃COO⁻ او Na⁺ آیونایز کېږي.')
add(s,'b2',f'Being the conjugate base of a weak acid, CH₃COOH, CH₃COO⁻ is{SO} relatively strong base. Thus, CH₃COO⁻ accepts H⁺ ion from water and underg{SO} hydrolysis.',f'ایک کمزور تیزاب CH₃COOH کا مزدوج اساس ہونے کی وجہ سے CH₃COO⁻ {SO} نسبتاً مضبوط اساس ہے۔ لہٰذا CH₃COO⁻ پانی سے H⁺ آئن قبول کرتا ہے اور ہائیڈرولائسس سے گزرتا ہے {SO}۔',f'د ضعیف اسید CH₃COOH مزدوج القلي په توګه، CH₃COO⁻ {SO} نسبتاً قوي القلي دی. نو CH₃COO⁻ له اوبو څخه H⁺ آیون منل کوي او هایدرولیز تېروي {SO}.')
add(s,'b3',f'The resulting solution is slightly basic due to excess OH⁻ ions present{SO}',f'نتیجتاً محلول زائد موجود OH⁻ آئنوں کی وجہ سے قدرے اساسی ہوتا ہے {SO}',f'پایله محلول د شته زیاتو OH⁻ آیونونو له امله لږ القلي دی {SO}')
head(s,'h2','2. Salts of Weak Bases and Strong Acids','2۔ کمزور اساسوں اور مضبوط تیزابوں کے نمک','2. د ضعیفو القليو او قوي اسیدونو مالګې')
add(s,'c1',f'When a salt of weak base (NH₄OH) and strong acid (HCl), for example, ammonium chloride (NH₄Cl) is dissolved in water. In aqueous solution, it ioniz{SO} into NH₄⁺ and Cl⁻.',f'جب کمزور اساس (NH₄OH) اور مضبوط تیزاب (HCl) کا نمک، مثلاً امونیم کلورائیڈ (NH₄Cl) پانی میں حل کیا جاتا ہے۔ آبی محلول میں وہ {SO} NH₄⁺ اور Cl⁻ میں آئنائز ہو جاتا ہے۔',f'کله چې د ضعیف القلي (NH₄OH) او قوي اسید (HCl) مالګه، د بېلګې په توګه امونیم کلوراید (NH₄Cl) په اوبو کې حل شي. په اوبیز محلول کې دا {SO} په NH₄⁺ او Cl⁻ آیونایز کېږي.')
add(s,'c2',f'NH₄⁺ is a Bronsted conjugate acid of the weak base NH₄OH. Therefore it{SO} is a relatively strong acid. It accepts OH⁻ ion from water (H₂O) and forms{SO} unionized NH₄OH and H⁺ ion.',f'NH₄⁺ کمزور اساس NH₄OH کا برونسٹڈ مزدوج تیزاب ہے۔ لہٰذا یہ {SO} نسبتاً مضبوط تیزاب ہے۔ یہ پانی (H₂O) سے OH⁻ آئن قبول کرتا ہے اور {SO} غیر آئنائز شدہ NH₄OH اور H⁺ آئن بناتا ہے۔',f'NH₄⁺ د ضعیف القلي NH₄OH برونسټډ مزدوج اسید دی. نو دا {SO} نسبتاً قوي اسید دی. دا له اوبو (H₂O) څخه OH⁻ آیون منل کوي او {SO} نه آیونایز شوی NH₄OH او H⁺ آیون جوړوي.')
add(s,'c3','The accumulation of H⁺ ions in solution makes it acidic.','محلول میں H⁺ آئنوں کا جمع ہونا اسے تیزابی بنا دیتا ہے۔','په محلول کې د H⁺ آیونونو راټولېدل هغه اسیدي کوي.')
add(s,'t-h','Tidbit','معلومات','ځانګړې یادونه',kind='heading')
add(s,'t0','Hydration and Hydrolysis','آبیدگی اور ہائیڈرولائسس','هایدریشن او هایدرولیز',kind='heading')
add(s,'t1',f'In hydrolysis H–OH bond is broken down; while in hydration wat{SO} molecules combine to a substance without H–OH bond breaking and beco{SO} part of that substance molecule.',f'ہائیڈرولائسس میں H–OH بندھن ٹوٹ جاتا ہے؛ جبکہ آبیدگی میں پانی {SO} کے سالمے کسی مادے کے ساتھ H–OH بندھن ٹوٹے بغیر مل جاتے ہیں اور اس مادے کے سالمے کا حصہ بن جاتے ہیں {SO}۔',f'په هایدرولیز کې H–OH بند ماتېږي؛ پداسې حال کې چې په هایدریشن کې د اوبو {SO} مالیکولونه له یوې مادې سره د H–OH بند له ماتېدو پرته یوځای کېږي او د هغه مادې د مالیکول برخه کېږي {SO}.')
F.p('a0','a1','a2','a3','a4','h1','b1')
F.e('r1',r'\mathrm{CH_3COONa\longrightarrow CH_3COO^-+Na^+}','CH₃COONa → CH₃COO⁻ + Na⁺')
F.p('b2')
F.e('r2',r'\mathrm{CH_3COO^-+H_2O\rightleftharpoons CH_3COOH+OH^-}','CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻')
F.p('b3','h2','c1')
F.e('r3',r'\mathrm{NH_4Cl\longrightarrow NH_4^++Cl^-}','NH₄Cl → NH₄⁺ + Cl⁻')
F.p('c2')
F.e('r4',r'\mathrm{NH_4^++H_2O\longrightarrow NH_4OH+H^+}','NH₄⁺ + H₂O → NH₄OH + H⁺')
F.p('c3','t-h','t0','t1')
F.done()
s['sourceNote']='Printed folio 262. The right edge is clipped by the page curl on most lines; clipped endings are marked [scan obscured] and not inferred. Handwritten notes on this copy ("pH > 7", "pH < 7", "strong C.B", circles and a margin star) are not part of the printed book and are ignored. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Right-edge clipping throughout; handwritten marks ignored.')
s['vocabulary']={'hydration':{'ur':'آبیدگی','ps':'هایدریشن'},'conjugate acid':{'ur':'مزدوج تیزاب','ps':'مزدوج اسید'},'conjugate base':{'ur':'مزدوج اساس','ps':'مزدوج القلي'}}
save(s)

# ---------- 268 ----------
s=mk(268,'3. Salts of Weak Acids and Weak Bases · 4. Salts of Strong Acids and Strong Bases · Self-Assessment','3۔ کمزور تیزابوں اور کمزور اساسوں کے نمک · 4۔ مضبوط تیزابوں اور مضبوط اساسوں کے نمک · خود جائزہ','3. د ضعیفو اسیدونو او ضعیفو القليو مالګې · 4. د قوي اسیدونو او قوي القليو مالګې · ځان ارزونه','salts-weak-strong')
F=Flow(s)
head(s,'h3','3. Salts of Weak Acids and Weak Bases','3۔ کمزور تیزابوں اور کمزور اساسوں کے نمک','3. د ضعیفو اسیدونو او ضعیفو القليو مالګې')
add(s,'a1','When a salt of weak acid (CH₃COOH) and weak base (NH₄OH), for example, ammonium acetate (CH₃COONH₄) is dissolved in water. It ionizes into CH₃COO⁻ and NH₄⁺. Since the acid and the base are both weak, their conjugate base (CH₃COO⁻) and conjugate acid (NH₄⁺) are relatively strong. They accept H⁺ and OH⁻ ions, respectively, from water and undergo considerable hydrolysis.','جب کمزور تیزاب (CH₃COOH) اور کمزور اساس (NH₄OH) کا نمک، مثلاً امونیم ایسیٹیٹ (CH₃COONH₄) پانی میں حل کیا جاتا ہے تو وہ CH₃COO⁻ اور NH₄⁺ میں آئنائز ہو جاتا ہے۔ چونکہ تیزاب اور اساس دونوں کمزور ہیں، ان کا مزدوج اساس (CH₃COO⁻) اور مزدوج تیزاب (NH₄⁺) نسبتاً مضبوط ہیں۔ وہ بالترتیب پانی سے H⁺ اور OH⁻ آئن قبول کرتے ہیں اور خاصی ہائیڈرولائسس سے گزرتے ہیں۔','کله چې د ضعیف اسید (CH₃COOH) او ضعیف القلي (NH₄OH) مالګه، د بېلګې په توګه امونیم اسیټیټ (CH₃COONH₄) په اوبو کې حل شي نو دا په CH₃COO⁻ او NH₄⁺ آیونایز کېږي. ځکه چې اسید او القلي دواړه ضعیف دي، د هغوی مزدوج القلي (CH₃COO⁻) او مزدوج اسید (NH₄⁺) نسبتاً قوي دي. دوی په ترتیب سره له اوبو څخه H⁺ او OH⁻ آیونونه منل کوي او پراخ هایدرولیز تېروي.')
add(s,'a2','The overall hydrolysis may be represented as,','مجموعی ہائیڈرولائسس کو اس طرح ظاہر کیا جا سکتا ہے،','ټوله هایدرولیز په لاندې ډول ښودل کېدای شي،')
add(s,'a3','The pH of the resulting solution will depend on the relative extent of anionic hydrolysis and cationic hydrolysis. The solution of such salt may be acidic, basic or neutral depending upon the K_a and K_b values of acid and base, respectively. If both the ions react to the same extent (as shown for CH₃COONH₄), [OH⁻] = [H⁺]. Then solution is neutral.','حاصل ہونے والے محلول کا pH اینائنی ہائیڈرولائسس اور کیٹائنی ہائیڈرولائسس کی اضافی حد پر منحصر ہوگا۔ ایسے نمک کا محلول تیزاب اور اساس کی بالترتیب K_a اور K_b قیمتوں کے مطابق تیزابی، اساسی یا معتدل ہو سکتا ہے۔ اگر دونوں آئن ایک ہی حد تک تعامل کریں (جیسا کہ CH₃COONH₄ کے لیے دکھایا گیا) تو [OH⁻] = [H⁺] ہوتا ہے۔ تب محلول معتدل ہوتا ہے۔','د پایلې محلول pH به د انیاني هایدرولیز او کیټاني هایدرولیز په نسبي اندازې پورې اړه ولري. د داسې مالګې محلول ښايي اسیدي، القلي یا خنثی وي د اسید او القلي د K_a او K_b ارزښتونو پورې په ترتیب سره. که دواړه آیونونه په یوه اندازه تعامل وکړي (لکه څنګه چې د CH₃COONH₄ لپاره ښودل شوي) نو [OH⁻] = [H⁺] وي. بیا محلول خنثی وي.')
head(s,'h4','4. Salts of Strong Acids and Strong Bases','4۔ مضبوط تیزابوں اور مضبوط اساسوں کے نمک','4. د قوي اسیدونو او قوي القليو مالګې')
add(s,'b1','The salts of strong acid (HCl) and strong base (NaOH) such as, NaCl, does not show hydrolysis. When NaCl is added into water, NaCl dissociates in water to give Na⁺ and Cl⁻ ions.','مضبوط تیزاب (HCl) اور مضبوط اساس (NaOH) کے نمک، جیسے NaCl، ہائیڈرولائسس نہیں دکھاتے۔ جب NaCl کو پانی میں ڈالا جاتا ہے تو NaCl پانی میں تفکیک ہو کر Na⁺ اور Cl⁻ آئن دیتا ہے۔','د قوي اسید (HCl) او قوي القلي (NaOH) مالګې، لکه NaCl، هایدرولیز نه ښيي. کله چې NaCl اوبو ته اضافه شي نو NaCl په اوبو کې تجزیه کېږي او Na⁺ او Cl⁻ آیونونه ورکوي.')
add(s,'b2','Since HCl is a strong acid, Cl⁻ is very weak conjugate base of HCl, Cl⁻ is unable to accept a proton (H⁺) from an acid, particularly water. That is why Cl⁻ does not hydrolyse. It cannot generate OH⁻ ions as follows','چونکہ HCl مضبوط تیزاب ہے، Cl⁻ HCl کا بہت کمزور مزدوج اساس ہے، Cl⁻ کسی تیزاب سے، خاص طور پر پانی سے، پروٹان (H⁺) قبول کرنے کے قابل نہیں۔ اسی لیے Cl⁻ ہائیڈرولائسس نہیں کرتا۔ یہ OH⁻ آئن پیدا نہیں کر سکتا جیسا کہ درج ذیل ہے','ځکه چې HCl قوي اسید دی، Cl⁻ د HCl ډېر ضعیف مزدوج القلي دی، Cl⁻ د اسید څخه، په ځانګړې توګه له اوبو څخه، پروټون (H⁺) منلو توان نه لري. له همدې امله Cl⁻ هایدرولیز نه کوي. دا OH⁻ آیونونه نشي جوړولای لکه څنګه چې لاندې ښودل شوي')
add(s,'b3','Similarly, in NaOH case, Na⁺ is not hydrolyzed because it is conjugate acid of strong base NaOH. Thus, the pH of sodium chloride solution remains unaffected and neutral.','اسی طرح NaOH کی صورت میں Na⁺ ہائیڈرولائسس نہیں کرتا کیونکہ یہ مضبوط اساس NaOH کا مزدوج تیزاب ہے۔ لہٰذا سوڈیم کلورائیڈ محلول کا pH متاثر نہیں ہوتا اور معتدل رہتا ہے۔','همدارنګه د NaOH په حالت کې Na⁺ هایدرولیز نه کېږي ځکه چې دا د قوي القلي NaOH مزدوج اسید دی. نو د سوډیم کلوراید محلول pH نه اغېزمنېږي او خنثی پاتې کېږي.')
head(s,'sa','Self-Assessment','خود جائزہ','ځان ارزونه')
for i,(e,u,p) in enumerate([('What is buffer action also write its application.','بفر عمل کیا ہے، اس کا اطلاق بھی لکھیں۔','د بفر عمل څه دی، د هغه کارونه هم ولیکئ.'),('What is hydrolysis? Explain why aqueous solutions of some salts are acidic or basic.','ہائیڈرولائسس کیا ہے؟ وضاحت کریں کہ کچھ نمکوں کے آبی محلول تیزابی یا اساسی کیوں ہوتے ہیں۔','هایدرولیز څه دی؟ تشریح کړئ چې د ځینو مالګو اوبیز محلولونه ولې اسیدي یا القلي دي.'),('Explain why the solution of a salt is not necessarily neutral.','وضاحت کریں کہ نمک کا محلول ضروری نہیں کہ معتدل ہو۔','تشریح کړئ چې د مالګې محلول ولې اړینه نه ده چې خنثی وي.')],1): add(s,f'sa{i}',f'{i}. {e}',f'{i}۔ {u}',f'{i}. {p}',role='question')
F.p('h3','a1')
F.e('r1',r'\mathrm{CH_3COO^-+H_2O\longrightarrow CH_3COOH+OH^-}','CH₃COO⁻ + H₂O → CH₃COOH + OH⁻')
F.e('r2',r'\mathrm{NH_4^++H_2O\longrightarrow NH_4OH+H^+}','NH₄⁺ + H₂O → NH₄OH + H⁺')
F.p('a2')
F.e('r3',r'\mathrm{CH_3COO^-+NH_4^++H_2O\longrightarrow CH_3COOH+NH_4OH}','CH₃COO⁻ + NH₄⁺ + H₂O → CH₃COOH + NH₄OH')
F.p('a3','h4','b1','b2')
F.e('r4',r'\mathrm{Cl^-+H_2O\;\not\longrightarrow\;HCl+OH^-}','Cl⁻ + H₂O ↛ HCl + OH⁻ (no reaction)')
F.p('b3','sa','sa1','sa2','sa3')
F.done()
s['sourceNote']='Printed folio 263. The left edge is slightly clipped (first letters of several lines cut) but the text is legible. The crossed arrow in the Cl⁻ + H₂O equation (no reaction) is written as ↛ in the accessible text. A CamScanner watermark crosses the page.'
s['vocabulary']={'hydrolyse':{'ur':'ہائیڈرولائسس کرنا','ps':'هایدرولیز کول'}}
save(s)
