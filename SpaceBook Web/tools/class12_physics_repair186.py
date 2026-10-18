"""PDF186 complete fission channels and printed energy calculation."""
import math
from class12_source_review import upsert, section, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, arrow, isotope, svg
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[];ROWS={}
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
def m(s):return r'\('+s+r'\)'
def eq(s):s=m(s);add('equation',s,s,s)
add('paragraph',r'Where \(({}^{236}\mathrm{U})^{*}\) is an intermediate excited state that lasts for only about \(10^{-12}\ \mathrm{s}\) before splitting into X and Y. The resulting nuclei X and Y are called fission fragments. There are many combinations of X and Y that satisfy the requirements of conservation of mass-energy, charge, and nucleon number as shown in figure 20.15.',
 r'یہاں \(({}^{236}\mathrm{U})^{*}\) ایک درمیانی برانگیختہ حالت ہے جو X اور Y میں تقسیم ہونے سے پہلے صرف تقریباً \(10^{-12}\ \mathrm{s}\) قائم رہتی ہے۔ حاصل ہونے والے نیوکلئیس X اور Y کو انشقاقی ٹکڑے کہتے ہیں۔ X اور Y کے بہت سے امتزاج کمیت و توانائی، بار اور نیوکلیونوں کی تعداد کی بقا کے تقاضے پورے کرتے ہیں، جیسا کہ شکل20.15 میں دکھایا گیا ہے۔',
 r'دلته \(({}^{236}\mathrm{U})^{*}\) یو منځنی تحریک شوی حالت دی چې په X او Y تر وېشل کېدو مخکې یوازې شاوخوا \(10^{-12}\ \mathrm{s}\) دوام کوي. رامنځته شوې هستې X او Y د انشقاق ټوټې بلل کېږي. د X او Y ډېر ترکیبونه د کتلې او انرژۍ، چارج او نیوکلیونونو د شمېر د بقا شرطونه پوره کوي، لکه په20.15 شکل کې چې ښودل شوي دي.')
add('paragraph','The process results in the production of several neutrons, typically two or three. On the average, about 2.5 neutrons are released per event. A typical reaction of this type is',
 'اس عمل سے کئی نیوٹرون پیدا ہوتے ہیں، عموماً دو یا تین۔ اوسطاً ہر واقعے میں تقریباً2.5 نیوٹرون خارج ہوتے ہیں۔ اس قسم کا ایک عام تعامل یہ ہے',
 'د دې بهیر په پایله کې څو نیوټرونونه، معمولاً دوه یا درې، تولیدېږي. په اوسط ډول په هره پېښه کې شاوخوا2.5 نیوټرونونه خوشې کېږي. د دې ډول یو عادي تعامل دا دی')
eq(r'{}^{1}_{0}\mathrm{n}+{}^{235}_{92}\mathrm{U}\rightarrow({}^{235}_{92}\mathrm{U})^{*}\rightarrow{}^{141}_{56}\mathrm{Ba}+{}^{92}_{36}\mathrm{Kr}+3\,{}^{1}_{0}\mathrm{n}+Q')
add('paragraph','where Q is the nuclear reaction energy.','جہاں Q نیوکلیائی تعامل کی توانائی ہے۔','چې Q د هستوي تعامل انرژي ده.')
add('heading','Lise Meitner (1878 - 1968)','لیزے مائٹنر (1878 - 1968)','لیزه مایټنر (1878 - 1968)')
add('paragraph','Lise Meitner (Austrian-Swedish) physicist who contributed to the discoveries of the element protactinium and nuclear fission.',
 'لیزے مائٹنر (آسٹریائی سویڈش) طبیعیات دان تھیں، جنہوں نے عنصر پروٹیکٹینیم اور نیوکلیائی انشقاق کی دریافتوں میں حصہ لیا۔',
 'لیزه مایټنر (اتریشي سویډنۍ) فزیکپوهه وه چې د پروټاکټینیم عنصر او هستوي انشقاق په کشفونو کې یې ونډه لرله.')
add('heading','FIGURE 20.15','شکل20.15','شکل20.15')
L.append({'type':'visual','blockId':'phys20-186-fission-channels'})
eq(r'{}^{1}_{0}\mathrm{n}+{}^{235}_{92}\mathrm{U}\rightarrow{}^{141}_{56}\mathrm{Ba}+{}^{92}_{36}\mathrm{Kr}+3\,{}^{1}_{0}\mathrm{n}+Q')
eq(r'{}^{1}_{0}\mathrm{n}+{}^{235}_{92}\mathrm{U}\rightarrow{}^{140}_{54}\mathrm{Xe}+{}^{94}_{38}\mathrm{Sr}+2\,{}^{1}_{0}\mathrm{n}+Q')
add('paragraph','The energy released in this fission can be calculated as','اس انشقاق میں خارج ہونے والی توانائی یوں حساب کی جا سکتی ہے','په دې انشقاق کې خوشې شوې انرژي داسې محاسبه کېدای شي')
rows=[(['Reactants','Products'],['متعامل مادے','حاصل شدہ مادے'],['تعامل کوونکي','محصولات'])]
left=[r'{}^{1}_{0}\mathrm{n}=1.0087\ \mathrm{u}',r'{}^{235}_{92}\mathrm{U}=235.439\ \mathrm{u}\quad+',r'=236.0526\ \mathrm{u}','']
right=[r'{}^{141}_{35}\mathrm{Ba}=140.9139\ \mathrm{u}',r'{}^{92}_{36}\mathrm{Kr}=91.8973\ \mathrm{u}',r'3\,{}^{1}_{0}\mathrm{n}=3.0261\ \mathrm{u}\quad+',r'=235.8373\ \mathrm{u}']
for a,b in zip(left,right):rows.append(tuple([m(a) if a else '',m(b)] for _ in range(3)))
start=len(T)
for row in rows:ROWS[len(T)]=row[0];T.append(tuple(' — '.join(cells) for cells in row))
L.append({'type':'table','indices':list(range(start,len(T)))})
add('paragraph','Since Q is the rest mass difference','چونکہ Q سکونی کمیت کا فرق ہے','ځکه چې Q د سکون کتلې توپیر دی')
eq(r'Q=236.0265\ \mathrm{u}-235.8373\ \mathrm{u}')
eq(r'Q=0.2153\ \mathrm{u}=200.44\ \mathrm{MeV}')
add('paragraph',r'When one atom of \({}^{235}\mathrm{U}\) undergoes this type of fission about 200 MeV energy is released. About 85% of this energy appears in the form of kinetic energy in the heavy fragments. This energy is very large compared to the energy released in chemical processes. For example, the energy released in the combustion of one molecule of octane used in gasoline engines is about one-millionth the energy released in a single uranium fission event.',
 r'جب \({}^{235}\mathrm{U}\) کا ایک ایٹم اس قسم کے انشقاق سے گزرتا ہے تو تقریباً200 MeV توانائی خارج ہوتی ہے۔ اس توانائی کا تقریباً85% بھاری ٹکڑوں میں حرکی توانائی کی صورت میں ظاہر ہوتا ہے۔ کیمیائی عملوں میں خارج ہونے والی توانائی کی نسبت یہ توانائی بہت زیادہ ہے۔ مثلاً پٹرول کے انجنوں میں استعمال ہونے والے آکٹین کے ایک سالمے کے احتراق سے خارج ہونے والی توانائی، یورینیم کے ایک انشقاقی واقعے میں خارج ہونے والی توانائی کا تقریباً دس لاکھواں حصہ ہے۔',
 r'کله چې د \({}^{235}\mathrm{U}\) یو اټوم له دې ډول انشقاق څخه تېر شي، شاوخوا200 MeV انرژي خوشې کېږي. د دې انرژۍ نږدې85% په درنو ټوټو کې د حرکي انرژۍ په بڼه څرګندېږي. دا انرژي په کیمیاوي بهیرونو کې د خوشې شوې انرژۍ په پرتله ډېره زیاته ده. د بېلګې په توګه، د پټرولي انجنونو د اوکټان د یوه مالیکول په سوځېدو کې خوشې شوې انرژي د یورانیم د یوې انشقاقي پېښې د خوشې شوې انرژۍ شاوخوا یو میلیونمه برخه ده.')
add('heading','A. FISSION CHAIN REACTION','A. انشقاقی زنجیری تعامل','A. د انشقاق ځنځیري تعامل')
add('definition','When one nuclear reaction causes an average of one or more nuclear reactions, thus a self-propagating series of these reactions is achieved and is called Fission Chain Reaction.',
 'جب ایک نیوکلیائی تعامل اوسطاً ایک یا زیادہ نیوکلیائی تعاملات کا باعث بنے تو ان تعاملات کا خود پھیلنے والا سلسلہ قائم ہو جاتا ہے، جسے انشقاقی زنجیری تعامل کہتے ہیں۔',
 'کله چې یو هستوي تعامل په اوسط ډول د یوه یا ډېرو هستوي تعاملونو لامل شي، د دغو تعاملونو په خپله خپرېدونکې لړۍ رامنځته کېږي چې د انشقاق ځنځیري تعامل بلل کېږي.')
add('paragraph',r'In a sample of uranium, each of the neutrons emitted in fission can be absorbed by another nucleus of \({}^{235}\mathrm{U}\) and thus induce another fission process, resulting in the emission of still more neutrons, followed by more fissions, and so forth as shown in figure 20.16.',
 r'یورینیم کے ایک نمونے میں انشقاق سے خارج ہونے والا ہر نیوٹرون \({}^{235}\mathrm{U}\) کے کسی اور نیوکلئیس میں جذب ہو سکتا ہے اور یوں ایک اور انشقاق پیدا کر سکتا ہے، جس سے مزید نیوٹرون خارج ہوتے ہیں، پھر مزید انشقاق ہوتے ہیں، اور یہ سلسلہ جاری رہتا ہے، جیسا کہ شکل20.16 میں دکھایا گیا ہے۔',
 r'د یورانیم په یوه نمونه کې په انشقاق کې هر خوشې شوی نیوټرون د \({}^{235}\mathrm{U}\) د بلې هستې له خوا جذبېدای شي او بل انشقاق رامنځته کولی شي، چې لا نور نیوټرونونه، ورپسې نور انشقاقونه او داسې نور تولیدوي، لکه په20.16 شکل کې چې ښودل شوي دي.')
add('paragraph','As long as the average number of neutrons available to produce new fissions is greater than 1 per reaction, the number of fissions grows with time. This series of events is called fission chain reaction, each reaction release about 200MeV. Thus energy released is very high it is found that 1 kg of uranium delivers as much energy as 3000 tons of coal.',
 'جب تک نئے انشقاق پیدا کرنے کے لیے دستیاب نیوٹرونوں کی اوسط تعداد فی تعامل1 سے زیادہ رہے، انشقاقوں کی تعداد وقت کے ساتھ بڑھتی ہے۔ واقعات کے اس سلسلے کو انشقاقی زنجیری تعامل کہتے ہیں، ہر تعامل تقریباً200MeV توانائی خارج کرتا ہے۔ یوں خارج ہونے والی توانائی بہت زیادہ ہوتی ہے؛ معلوم ہوا ہے کہ1 kg یورینیم اتنی توانائی فراہم کرتا ہے جتنی3000 ٹن کوئلہ۔',
 'تر هغه چې د نویو انشقاقونو د تولید لپاره د موجودو نیوټرونونو منځنی شمېر په هر تعامل کې له1 څخه زیات وي، د انشقاقونو شمېر له وخت سره زیاتېږي. د پېښو دې لړۍ ته د انشقاق ځنځیري تعامل ویل کېږي، هر تعامل شاوخوا200MeV انرژي خوشې کوي. نو خوشې شوې انرژي ډېره زیاته ده؛ موندل شوې چې1 kg یورانیم د3000 ټنو ډبرو سکرو هومره انرژي ورکوي.')
def cluster(x,y,r):
    out=f'<circle cx="{x}" cy="{y}" r="{r}" fill="#e2e8f0"/>'
    # Source uses stylized clusters; mass numbers are explicit labels, not a bead count.
    for row in range(-4,5):
        for col in range(-4,5):
            dx=col*r/4+((row%2)*r/8);dy=row*r/4
            if dx*dx+dy*dy < (r-3)**2:
                color='#a5f3fc' if (row+col)%2 else '#fbcfe8'
                out+=f'<circle cx="{x+dx:.2f}" cy="{y+dy:.2f}" r="{r/8:.2f}" fill="{color}" stroke="#94a3b8" stroke-width=".6"/>'
    return out
def channels(lang):
    out=''
    for offset,upper,lower,count in [(0,(92,36,'Kr'),(141,56,'Ba'),3),(475,(94,38,'Sr'),(140,54,'Xe'),2)]:
        out+=f'<g transform="translate({offset} 0)">'
        out+=cluster(200,200,44)+isotope(204,119,235,92,'U')
        out+=cluster(359,58,28)+isotope(289,49,*upper)+cluster(359,337,31)+isotope(279,342,*lower)
        out+=arrow(235,164,326,80,'#1e3a8a')+arrow(235,237,325,309,'#1e3a8a')
        for x,y in ([(95,65),(59,200),(404,194)] if count==3 else [(95,65),(404,194)]):
            dx=x-200;dy=y-200;length=math.hypot(dx,dy)
            out+=arrow(200+dx*48/length,200+dy*48/length,x-dx*15/length,y-dy*15/length,'#1e3a8a')
            out+=f'<circle cx="{x}" cy="{y}" r="5" fill="#f9a8d4" stroke="#64748b"/>'+isotope(x+8,y-24,1,0,'n')
        out+='<circle cx="95" cy="328" r="5" fill="#f9a8d4" stroke="#64748b"/>'+isotope(98,308,1,0,'n')+arrow(112,307,169,245,'#b91c1c')+'</g>'
    return svg(out,950,392,{'en':'Figure20.15, two uranium235 fission channels: incoming neutron, barium141 and krypton92 with three outgoing neutrons; incoming neutron, xenon140 and strontium94 with two outgoing neutrons. All isotope atomic numbers retained.','ur':'شکل20.15، یورینیم235 کے دو انشقاقی راستے: آنے والا نیوٹرون، بیریم141 اور کرپٹون92 کے ساتھ تین خارج ہونے والے نیوٹرون؛ آنے والا نیوٹرون، زینون140 اور اسٹرونشیم94 کے ساتھ دو خارج ہونے والے نیوٹرون۔ تمام ایٹمی اعداد محفوظ ہیں۔','ps':'شکل20.15، د یورانیم235 د انشقاق دوه لارې: راتلونکی نیوټرون، باریم141 او کریپټون92 له دریو وتونکو نیوټرونونو سره؛ راتلونکی نیوټرون، زینون140 او سټرونشیم94 له دوو وتونکو نیوټرونونو سره. ټول اټومي عددونه ساتل شوي دي.'}[lang])
record={'id':'phys20-fission-energy-chain-reaction-360-361','title':'Fission fragments, energy and chain reaction','kind':'lesson','pdfPage':186,'printedPage':360,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=[
 'The prose identifies the excited intermediate as236U*, while the printed reaction uses235U*. Both retained.',
 'Printed reactant masses1.0087u and235.439u do not sum to the printed236.0526u. The subsequent Q subtraction instead uses236.0265u and prints0.2153u=200.44MeV; all original numbers retained.',
 'The products mass table prints barium141 with atomic number35, while its equation and figure show56. The table35 is retained.']
sec=section(record,T,L,('انشقاقی ٹکڑے، توانائی اور زنجیری تعامل','د انشقاق ټوټې، انرژي او ځنځیري تعامل'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[{'pdfPage':186,'printedPage':n,'sourcePdf':SOURCE} for n in (360,361)],sourceTableRows=ROWS,sourceIssues=issues,sourceBlocks=[{'id':'phys20-186-fission-channels','type':'figure','sourceFigure':'20.15','svg':channels('en'),'svgUrdu':channels('ur'),'svgPashto':channels('ps')}],sourceExcludedVisuals=[{'description':'Lise Meitner portrait','reason':'Decorative biographical portrait; full name, dates and biography retained as source text.'}])
if __name__=='__main__':
    with shared_class_data_lock():upsert([record],[sec],chapter_index=9)
    stage_reference(186,record,'Visually reinspected PDF186 printed360–361. Complete excited-state and neutron prose, biography, both Figure20.15 isotope-labelled fission pathways and equations, semantic mass table, all printed Q steps, energy comparison, and three chain-reaction paragraphs restored with Urdu/Pashto. Meitner portrait excluded as noninstructional while full biography retained. Source235/236, mass/sum/Q and Ba35/56 inconsistencies explicitly preserved.',issues)
    print('PDF186 full two-channel figure and calculation staged.')
