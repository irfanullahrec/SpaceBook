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
CH='chem11-acids-bases-salts'
def mk(n,title,ur,ps,sid): return page(n,CH,title,ur,ps,sid)
SUP=str.maketrans('0123456789-','⁰¹²³⁴⁵⁶⁷⁸⁹⁻')
def pw(k): return '1×10'+str(-k).translate(SUP) if k else '1×10⁻⁰'

# ---------- 253 ----------
s=mk(253,'Table 8.3 pH Values of Some Common Items · Table 8.4 Relationship of H₃O⁺, OH⁻, pH and pOH','جدول 8.3 کچھ عام اشیاء کے pH کی قیمتیں · جدول 8.4 H₃O⁺، OH⁻، pH اور pOH کا باہمی تعلق','جدول 8.3 د ځینو عامو توکو د pH ارزښتونه · جدول 8.4 د H₃O⁺، OH⁻، pH او pOH اړیکه','ph-tables')
items=[('Gastric juice','معدے کا رس','د معدې شیره','1 - 2'),('Lemon juice','لیموں کا رس','د لیمو شیره','2.3'),('Vinegar','سرکہ','سرکه','2.8 - 3'),('Soft drinks','سافٹ ڈرنکس','نرم څښاکونه','3'),('Orange juice','مالٹے کا رس','د مالټې شیره','3.5 - 3.7'),('Tomatoes','ٹماٹر','روميان','4 - 4.1'),('Rainwater','بارش کا پانی','د باران اوبه','6'),('Urine','پیشاب','متیازې','6.0'),('Milk','دودھ','شیدې','6.6'),('Pure water','خالص پانی','خالصې اوبه','7'),('Human blood','انسانی خون','د انسان وینه','7.3 - 7.4'),('Baking soda (aqueous)','بیکنگ سوڈا (آبی)','بیکنګ سوډا (اوبیز)','8.5'),('Ammonia','امونیا','امونیا','11 - 12'),('Washing soda (aqueous)','دھونے کا سوڈا (آبی)','مینځلو سوډا (اوبیز)','12')]
t1=table('Table 8.3 pH Values of Some Common Items','جدول 8.3 کچھ عام اشیاء کے pH کی قیمتیں','جدول 8.3 د ځینو عامو توکو د pH ارزښتونه',[c('Item','شے','توکی'),c('pH','pH','pH')],[[c(a,b,d),c(v)] for a,b,d,v in items])
t1['sourceGap']=dict(note='The value column is printed half a row lower than the item column on the skewed scan; values are paired with items in printed order. Some values are circled by hand on this copy (not part of the printed book).')
rows=[]
for k in range(14,-1,-1):
    rows.append([c('Basic' if k>7 else ('Neutral' if k==7 else 'Acidic'),'اساسی' if k>7 else ('معتدل' if k==7 else 'تیزابی'),'القلي' if k>7 else ('خنثی' if k==7 else 'اسیدي')),c(pw(k)),c(f'{k:02d}'),c(pw(14-k)),c(f'{14-k:02d}')])
t2=table('Table 8.4 Relationship of H₃O⁺, OH⁻, pH and pOH','جدول 8.4 H₃O⁺، OH⁻، pH اور pOH کا باہمی تعلق','جدول 8.4 د H₃O⁺، OH⁻، pH او pOH اړیکه',[c('Solution','محلول','محلول'),c('H₃O⁺'),c('pH'),c('OH⁻'),c('pOH')],rows)
t2['sourceGap']=dict(note='The left-hand labels Basic (top), Neutral (middle) and Acidic (bottom) are printed as vertical side labels spanning several rows; they are repeated per row here. The pH column is printed offset from the H₃O⁺ column on the skewed scan; each pH is paired by its exponent (pH = −exponent of H₃O⁺).')
s['tables']=[t1,t2]
s['flow']=[dict(type='table',index=0),dict(type='table',index=1)]
s['sourceNote']='Printed folio 248. The scan is skewed so the value columns appear offset from the labels; pairing follows the printed order. Some entries of Table 8.3 are circled by hand on this copy (not printed). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Skewed scan: value columns appear offset from the row labels in both tables.')
save(s)

# ---------- 254 ----------
s=mk(254,'Example 8.1 · Example 8.2','مثال 8.1 · مثال 8.2','بېلګه 8.1 · بېلګه 8.2','examples-81-82')
F=Flow(s)
head(s,'e1','Example 8.1','مثال 8.1','بېلګه 8.1')
add(s,'q1','What is the pH and pOH of 0.001 M HCl solution?','0.001 M HCl محلول کا pH اور pOH کیا ہے؟','د 0.001 M HCl محلول pH او pOH څومره دی؟')
head(s,'s1','Solution','حل','حل')
add(s,'a1','The concentration of HCl = 0.001 = 10⁻³','HCl کا ارتکاز = 0.001 = 10⁻³','د HCl غلظت = 0.001 = 10⁻³')
add(s,'a2','You can write as, [H⁺] = 10⁻³','آپ لکھ سکتے ہیں، [H⁺] = 10⁻³','تاسو لیکلای شئ، [H⁺] = 10⁻³')
add(s,'a3','Taking negative log (– log) of both sides, you have,','دونوں اطراف کا منفی لوگ (– log) لینے پر ہمیں ملتا ہے،','د دواړو اړخونو منفي لوګ (– log) اخیستلو سره تاسو ترلاسه کوئ،')
add(s,'a4','As you have,','جیسا کہ آپ کے پاس ہے،','لکه څنګه چې تاسو لرئ،')
add(s,'a5','– log [H⁺] = pH, so you can write,','– log [H⁺] = pH، لہٰذا آپ لکھ سکتے ہیں،','– log [H⁺] = pH، نو تاسو لیکلای شئ،')
add(s,'a6','Since, you have equation (8.8),','چونکہ آپ کے پاس مساوات (8.8) ہے،','ځکه چې تاسو معادله (8.8) لرئ،')
add(s,'a7','or','یا','یا')
head(s,'e2','Example 8.2','مثال 8.2','بېلګه 8.2')
add(s,'q2','Determine the pH of 0.15M NaOH solution.','0.15M NaOH محلول کا pH معلوم کریں۔','د 0.15M NaOH محلول pH وټاکئ.')
head(s,'s2','Solution','حل','حل')
add(s,'b1','The concentration of NaOH = 0.15 = 1.5 × 10⁻¹','NaOH کا ارتکاز = 0.15 = 1.5 × 10⁻¹','د NaOH غلظت = 0.15 = 1.5 × 10⁻¹')
add(s,'b2','You can write as, [OH⁻] = 1.5 × 10⁻¹','آپ لکھ سکتے ہیں، [OH⁻] = 1.5 × 10⁻¹','تاسو لیکلای شئ، [OH⁻] = 1.5 × 10⁻¹')
add(s,'b3','Taking negative log (–log) of both sides, you have,','دونوں اطراف کا منفی لوگ (–log) لینے پر ہمیں ملتا ہے،','د دواړو اړخونو منفي لوګ (–log) اخیستلو سره تاسو ترلاسه کوئ،')
add(s,'b4','Or you can write, pOH = 0.8','یا آپ لکھ سکتے ہیں، pOH = 0.8','یا تاسو لیکلای شئ، pOH = 0.8')
add(s,'b5','as you have,','جیسا کہ آپ کے پاس ہے،','لکه څنګه چې تاسو لرئ،')
add(s,'b6','or','یا','یا')
F.p('e1','q1','s1','a1','a2','a3')
F.e('c1',r'-\log[\mathrm{H^+}]=-\log10^{-3}\qquad\text{as }(\log10=1)','– log [H⁺] = – log 10⁻³   as (log 10 = 1)')
F.p('a4','a5')
F.e('c2',r'\mathrm{pH}=-(-3)','pH = – (– 3)')
F.e('c3',r'\mathrm{pH}=3','pH = 3')
F.p('a6')
F.e('c4',r'\mathrm{pH}+\mathrm{pOH}=14','pH + pOH = 14')
F.p('a7')
F.e('c5',r'\mathrm{pOH}=14-\mathrm{pH}','pOH = 14 – pH')
F.e('c6',r'\mathrm{pOH}=14-3','pOH = 14 – 3')
F.e('c7',r'\mathrm{pOH}=11','pOH = 11')
F.p('e2','q2','s2','b1','b2','b3')
F.e('d1',r'-\log[\mathrm{OH^-}]=-\log1.5\times10^{-1}','– log [OH⁻] = –log 1.5 × 10⁻¹')
F.e('d2',r'-\log[\mathrm{OH^-}]=-(0.2-1)','– log[OH⁻] = – (0.2 – 1)')
F.e('d3',r'-\log[\mathrm{OH^-}]=-(-0.8)','– log[OH⁻] = – ( – 0.8)')
F.e('d4',r'-\log[\mathrm{OH^-}]=0.8','– log[OH⁻] = 0.8')
F.p('b4','b5')
F.e('d5',r'\mathrm{pH}+\mathrm{pOH}=14','pH + pOH = 14')
F.p('b6')
F.e('d6',r'\mathrm{pH}=14-\mathrm{pOH}','pH = 14 – pOH')
F.e('d7',r'=14-0.8','= 14 – 0.8')
F.done()
s['sourceNote']='Printed folio 249. Faint mirrored text from the reverse page shows through but is not part of this page. The last line of Example 8.2 ("= 14 – 0.8") continues on the next page. The printed step "–log 1.5×10⁻¹ = –(0.2 – 1)" is reproduced as printed (log 1.5 is taken as 0.2). A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='Example 8.2 final result continues on the next page; log 1.5 is printed as 0.2.')
save(s)

# ---------- 255 ----------
s=mk(255,'Example 8.3 · Practice Problems 8.1, 8.2 · 8.4.3 Acid Ionization Constant Ka and pKa','مثال 8.3 · مشقی مسائل 8.1، 8.2 · 8.4.3 تیزابی آئنائزیشن مستقلہ Ka اور pKa','بېلګه 8.3 · د تمرین ستونزې 8.1، 8.2 · 8.4.3 د اسید د آیونایزیشن ثابت Ka او pKa','example-83-ka')
F=Flow(s)
head(s,'e3','Example 8.3','مثال 8.3','بېلګه 8.3')
add(s,'q1','Calculate the [H⁺] and [OH⁻] ions concentration of a solution, which has a pH of 4.','ایسے محلول کا [H⁺] اور [OH⁻] آئنوں کا ارتکاز معلوم کریں جس کا pH 4 ہے۔','د هغه محلول د [H⁺] او [OH⁻] آیونونو غلظت ومومئ چې pH یې 4 دی.')
head(s,'s','Solution','حل','حل')
add(s,'a1','pH of solution = 4','محلول کا pH = 4','د محلول pH = 4')
add(s,'a2','[H⁺] = ?,   [OH⁻] = ?','[H⁺] = ؟،   [OH⁻] = ؟','[H⁺] = ؟،   [OH⁻] = ؟')
add(s,'a3','Since you have the equation (8.6),','چونکہ آپ کے پاس مساوات (8.6) ہے،','ځکه چې تاسو معادله (8.6) لرئ،')
add(s,'a4','Putting the values, you get,','قیمتیں رکھنے پر ہمیں ملتا ہے،','ارزښتونه ایښودلو سره تاسو ترلاسه کوئ،')
add(s,'a5','As you have,','جیسا کہ آپ کے پاس ہے،','لکه څنګه چې تاسو لرئ،')
add(s,'a6','Putting the values, you get,','قیمتیں رکھنے پر ہمیں ملتا ہے،','ارزښتونه ایښودلو سره تاسو ترلاسه کوئ،')
head(s,'p1h','Practice Problem 8.1','مشقی مسئلہ 8.1','د تمرین ستونزه 8.1')
add(s,'p1','Calculate the pH of 0.002 M hydrochloric acid (HCl) solution.','0.002 M ہائیڈروکلورک ایسڈ (HCl) محلول کا pH معلوم کریں۔','د 0.002 M هایدروکلوریک اسید (HCl) محلول pH محاسبه کړئ.')
head(s,'p2h','Practice Problem 8.2','مشقی مسئلہ 8.2','د تمرین ستونزه 8.2')
add(s,'p2','Find the pH of 0.082 M NaOH solution.','0.082 M NaOH محلول کا pH معلوم کریں۔','د 0.082 M NaOH محلول pH ومومئ.')
head(s,'h843','8.4.3 Acid Ionization Constant, K_a and pK_a','8.4.3 تیزابی آئنائزیشن مستقلہ K_a اور pK_a','8.4.3 د اسید د آیونایزیشن ثابت K_a او pK_a')
add(s,'b1','Consider a weak monoprotic acid, HA. Its ionization in water is represented by','ایک کمزور یک پروٹانی تیزاب HA پر غور کریں۔ پانی میں اس کی آئنائزیشن اس طرح ظاہر کی جاتی ہے','یو ضعیف یو پروټوني اسید HA ته پام وکړئ. په اوبو کې د هغه آیونایزیشن په لاندې ډول ښودل کېږي')
add(s,'b2','The equilibrium expression for this ionization is','اس آئنائزیشن کے لیے توازنی اظہار یہ ہے','د دې آیونایزیشن لپاره د تعادل بیان دا دی')
add(s,'b3','Where for acid is, K_c.[H₂O] = K_a, so you can write the above equation as','جہاں تیزاب کے لیے K_c.[H₂O] = K_a ہے، اس لیے آپ مندرجہ بالا مساوات کو اس طرح لکھ سکتے ہیں','چېرته چې د اسید لپاره K_c.[H₂O] = K_a دی، نو تاسو کولای شئ پورتنۍ معادله داسې ولیکئ')
F.p('e3','q1','s','a1','a2','a3')
F.e('y1',r'[\mathrm{H^+}]=10^{-\mathrm{pH}}','[H⁺] = 10^(−pH)')
F.p('a4')
F.e('y2',r'[\mathrm{H^+}]=10^{-4}','[H⁺] = 10⁻⁴')
F.p('a5')
F.e('y3',r'[\mathrm{H^+}][\mathrm{OH^-}]=10^{-14}\qquad\text{or}\qquad[\mathrm{OH^-}]=\frac{[10^{-14}]}{[\mathrm{H^+}]}','[H⁺][OH⁻] = 10⁻¹⁴   or   [OH⁻] = [10⁻¹⁴] / [H⁺]')
F.p('a6')
F.e('y4',r'[\mathrm{OH^-}]=\frac{10^{-14}}{10^{-4}}','[OH⁻] = 10⁻¹⁴ / 10⁻⁴')
F.e('y5',r'[\mathrm{OH^-}]=10^{-14+4}=10^{-10}','[OH⁻] = 10⁻¹⁴⁺⁴ = 10⁻¹⁰')
F.p('p1h','p1','p2h','p2','h843','b1')
F.e('ha',r'\mathrm{HA_{(aq)}+H_2O_{(l)}\rightleftharpoons H_3O^+_{(aq)}+A^-_{(aq)}}','HA(aq) + H₂O(l) ⇌ H₃O⁺(aq) + A⁻(aq)')
F.p('b2')
F.e('e89',r'K_c=\frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{H_2O}][\mathrm{HA}]}\qquad(8.9)','K_c = [H₃O⁺][A⁻] / [H₂O][HA]   (8.9)')
F.e('e89b',r'K_c[\mathrm{H_2O}]=\frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]}','K_c [H₂O] = [H₃O⁺][A⁻] / [HA]')
F.p('b3')
F.e('e810',r'K_a=\frac{[\mathrm{H_3O^+}][\mathrm{A^-}]}{[\mathrm{HA}]}\qquad(8.10)','K_a = [H₃O⁺][A⁻] / [HA]   (8.10)')
F.done()
s['sourceNote']='Printed folio 250. The right edge is slightly clipped at the end of two lines ("…which has a pH of 4.", "…Its ionization in water is represented by") but the sentences are complete. The printed [OH⁻] = 10⁻¹⁴/10⁻⁴ line is partly garbled on the scan and is read as printed in the next line (10⁻¹⁴⁺⁴ = 10⁻¹⁰). A CamScanner watermark crosses the page.'
s['vocabulary']={'monoprotic':{'ur':'یک پروٹانی','ps':'یو پروټوني'}}
save(s)

# ---------- 256 ----------
s=mk(256,'Ka and pKa · Table 8.5 Ionization Constants of Some Weak Acids at 25°C','Ka اور pKa · جدول 8.5 کچھ کمزور تیزابوں کے آئنائزیشن مستقلے 25°C پر','Ka او pKa · جدول 8.5 د ځینو ضعیفو اسیدونو د آیونایزیشن ثابتونه په 25°C کې','ka-table85')
F=Flow(s)
add(s,'a1','Where K_a, the acid ionization or dissociation constant. It is the equilibrium constant for the ionization of an acid. At a given temperature, the strength of the acid HA is measured quantitatively by the magnitude of K_a. It is the ratio of product concentrations of dissociated ions to the undissociated acid molecules in aqueous solution. It represents the extent to which an acid is dissociated. The larger the value of K_a, the stronger will be the acid, that is, the greater will be the concentration of H⁺ ions at equilibrium due to its ionization. Keep in mind, however, that only weak acids have K_a values associated with them.','جہاں K_a تیزابی آئنائزیشن یا تفکیک مستقلہ ہے۔ یہ کسی تیزاب کی آئنائزیشن کا توازنی مستقلہ ہے۔ ایک دیے گئے درجہ حرارت پر تیزاب HA کی قوت کو K_a کی مقدار سے مقداری طور پر ناپا جاتا ہے۔ یہ آبی محلول میں تفکیک شدہ آئنوں کے ارتکازوں کے حاصل ضرب اور غیر تفکیک شدہ تیزاب کے سالموں کی نسبت ہے۔ یہ اس حد کو ظاہر کرتا ہے جس تک تیزاب تفکیک ہوتا ہے۔ K_a کی قیمت جتنی بڑی ہوگی تیزاب اتنا ہی مضبوط ہوگا، یعنی اس کی آئنائزیشن کی وجہ سے توازن پر H⁺ آئنوں کا ارتکاز اتنا ہی زیادہ ہوگا۔ تاہم یاد رکھیں کہ صرف کمزور تیزابوں کے ساتھ K_a کی قیمتیں وابستہ ہوتی ہیں۔','چېرته چې K_a د اسید د آیونایزیشن یا تجزیې ثابت دی. دا د یو اسید د آیونایزیشن د تعادل ثابت دی. په یوه ورکړل شوې تودوخه کې د اسید HA قوت د K_a د اندازې په واسطه کمیتي ډول اندازه کېږي. دا په اوبیز محلول کې د تجزیه شویو آیونونو د غلظتونو د حاصل ضرب او نه تجزیه شوو اسید مالیکولونو نسبت دی. دا هغه اندازه ښيي چې اسید تر کومې اندازې پورې تجزیه کېږي. د K_a ارزښت څومره لوی وي اسید به هماغومره قوي وي، یعنې د هغه د آیونایزیشن له امله په تعادل کې د H⁺ آیونونو غلظت به هماغومره ډېر وي. خو په یاد ولرئ چې یوازې ضعیف اسیدونه د K_a ارزښتونه لري.')
add(s,'a2','A negative logarithm of K_a is called pK_a. Since it is the negative logarithm, hence greater the value of pK_a, weaker would be the acid.','K_a کے منفی لوگارتھم کو pK_a کہتے ہیں۔ چونکہ یہ منفی لوگارتھم ہے اس لیے pK_a کی قیمت جتنی زیادہ ہوگی تیزاب اتنا ہی کمزور ہوگا۔','د K_a منفي لوګاریتم ته pK_a ویل کېږي. ځکه چې دا منفي لوګاریتم دی نو د pK_a ارزښت څومره ډېر وي اسید به هماغومره ضعیف وي.')
add(s,'a3','Table 8.5 lists a number of weak acids and their K_a values at 25°C in order of decreasing acid strength. Although all these acids are weak, within the group there is great variation in their strengths.','جدول 8.5 میں کئی کمزور تیزابوں کی فہرست 25°C پر ان کی K_a قیمتوں کے ساتھ تیزاب کی کم ہوتی قوت کی ترتیب میں دی گئی ہے۔ اگرچہ یہ تمام تیزاب کمزور ہیں، گروہ کے اندر ان کی قوتوں میں بہت فرق ہے۔','په 8.5 جدول کې د ډېرو ضعیفو اسیدونو لړلیک د 25°C په تودوخه کې د هغوی د K_a ارزښتونو سره د اسید د کمېدونکي قوت په ترتیب ورکړل شوی. که څه هم دا ټول اسیدونه ضعیف دي، په ګروپ کې د هغوی په قوتونو کې ډېر توپیر شته.')
rows=[('Acetic acid','ایسیٹک ایسڈ','اسیټیک اسید','CH₃COOH','1.7 × 10⁻⁵'),('Benzoic acid','بینزوئک ایسڈ','بنزوییک اسید','C₆H₅COOH','6.3 × 10⁻⁵'),('Boric acid','بورک ایسڈ','بوریک اسید','H₃BO₃','5.9 × 10⁻¹⁰'),('Carbonic acid','کاربونک ایسڈ','کاربونیک اسید','H₂CO₃','4.3 × 10⁻⁷'),('Cyanic acid','سائنک ایسڈ','سیانیک اسید','HOCN','3.5 × 10⁻⁴'),('Formic acid','فارمک ایسڈ','فارمیک اسید','HCOOH','1.7 × 10⁻⁴'),('Hydrocyanic acid','ہائیڈروسائنک ایسڈ','هایدروسیانیک اسید','HCN','4.9 × 10⁻¹⁰'),('Hydrofluoric acid','ہائیڈروفلورک ایسڈ','هایدروفلوریک اسید','HF','6.8 × 10⁻⁴'),('Hydrogen sulphide','ہائیڈروجن سلفائیڈ','هایدروجن سلفایډ','H₂S','8.9 × 10⁻⁸'),('Hypochlorus acid','ہائپوکلورس ایسڈ','هایپوکلورس اسید','HOCl','3.5 × 10⁻⁸'),('Nitrous acid','نائٹرس ایسڈ','نایټروس اسید','HNO₂','4.5 × 10⁻⁴'),('Oxalic acid','آکسیلک ایسڈ','اکسالیک اسید','(COOH)₂','5.6 × 10⁻²'),('Phosphoric acid','فاسفورک ایسڈ','فاسفوریک اسید','H₃PO₄','6.9 × 10⁻³'),('Phosphorus acid','فاسفورس ایسڈ','فاسفورس اسید','H₃PO₃','1.6 × 10⁻²'),('Propionic acid','پروپیونک ایسڈ','پروپیونیک اسید','C₃H₆O₂','1.4 × 10⁻⁵'),('Sulphurous acid','سلفیورس ایسڈ','سلفیورس اسید','H₂SO₃','1.3 × 10⁻²')]
s['tables']=[table('Table 8.5 Ionization Constants of Some Weak Acids at 25°C','جدول 8.5 کچھ کمزور تیزابوں کے آئنائزیشن مستقلے 25°C پر','جدول 8.5 د ځینو ضعیفو اسیدونو د آیونایزیشن ثابتونه په 25°C کې',[c('Substance','مادہ','مواد'),c('Formula','فارمولا','فورمول'),c('Ka','Ka','Ka')],[[c(a,b,d),c(f),c(k)] for a,b,d,f,k in rows])]
s['tables'][0]['sourceGap']=dict(note='Row labels are slightly skewed on the scan; values are paired with substances in printed order. "Hypochlorus" is printed as such. Some formulas (HOCN, HOCl, HNO₂) are circled by hand on this copy (not part of the printed book).')
F.p('a1')
F.e('ka',r'K_a=\frac{[\mathrm{H^+}][\mathrm{A^-}]}{[\mathrm{HA}]}','K_a = [H⁺][A⁻] / [HA]')
F.p('a2')
F.e('pka',r'\mathrm{p}K_a=-\log K_a\qquad(8.11)','pK_a = −log K_a   (8.11)')
F.p('a3')
F.tb(0)
s['flow']=[dict(type='equation',index=0)]+[]  # placeholder replaced below
F.done()
s['flow']=[dict(type='equation',index=0),dict(type='paragraphs',ids=['chem11-p256-a1']),dict(type='paragraphs',ids=['chem11-p256-a2']),dict(type='equation',index=1),dict(type='paragraphs',ids=['chem11-p256-a3']),dict(type='table',index=0)]
s['equations']=[eqn(256,'ka',r'K_a=\frac{[\mathrm{H^+}][\mathrm{A^-}]}{[\mathrm{HA}]}','K_a = [H⁺][A⁻] / [HA]'),eqn(256,'pka',r'\mathrm{p}K_a=-\log K_a\qquad(8.11)','pK_a = −log K_a   (8.11)')]
s['sourceNote']='Printed folio 251. The left edge is clipped by the page curl (the first letters of lines 2–8 of the first paragraph and of "hence"/"decreasing"/"there" are cut) but the sentences are legible and read in full. Handwritten underlines and circles on this copy are not part of the printed book. A CamScanner watermark crosses the page.'
s['sourceGap']=dict(note='First letters of several left-hand lines are cut by the page curl.')
s['vocabulary']={'monoprotic':{'ur':'یک پروٹانی','ps':'یو پروټوني'}}
save(s)
