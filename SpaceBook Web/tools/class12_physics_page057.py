"""Sequential source correction for PDF page 57 of Class 12 Physics."""
import json
from html import escape
from class12_source_review import ROOT,upsert,section,checkpoint,sync_companions,shared_class_data_lock
SOURCE=r"Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf"
def pair(en,ur,ps): return (en,ur,ps)
def ref(p): return {'pdfPage':57,'printedPage':p,'sourcePdf':SOURCE}
def svg(body,label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 360" role="img" aria-label="{escape(label,quote=True)}" style="width:100%;max-width:680px;height:auto"><rect width="100%" height="100%" fill="#fff"/>{body}</svg>'

CONDUCTOR=[
 pair('B. THE FORCE ON CURRENT CARRYING CONDUCTOR AND MOTION OF CHARGE PARTICLE IN MAGNETIC FIELD','ب۔ کرنٹ بردار موصل پر قوت اور مقناطیسی میدان میں بار دار ذرہ کی حرکت','ب. پر جریان‌لرونکي هادي قوه او په مقناطیسي ساحه کې د چارج لرونکې ذرې حرکت'),
 pair('We have seen that a current-carrying wire experiences a force when placed in a magnetic field. Since a current in a wire consists of moving electric charges, we might expect that freely moving charged particles (not in a wire) would also experience a force when passing through a magnetic field. The force on a current carrying conductor is','ہم دیکھ چکے ہیں کہ مقناطیسی میدان میں رکھا کرنٹ بردار تار قوت محسوس کرتا ہے۔ چونکہ تار میں رو حرکت کرتے برقی باروں پر مشتمل ہے، اس لیے توقع ہے کہ آزاد حرکت کرتے بار دار ذرات (تار کے باہر) بھی مقناطیسی میدان سے گزرتے وقت قوت محسوس کریں گے۔ کرنٹ بردار موصل پر قوت یہ ہے:','موږ ولیدل چې په مقناطیسي ساحه کې اېښودل شوی جریان‌لرونکی سیم قوه تجربه کوي. ځکه په سیم کې جریان له خوځنده برېښنايي چارجونو جوړ دی، تمه ده چې ازاد خوځنده چارج‌لرونکي ذرات (له سیم بهر) هم د مقناطیسي ساحې د تېرېدو پر مهال قوه تجربه کړي. پر جریان‌لرونکي هادي قوه داسې ده:'),
 pair('F_B = B I L sin θ ...(1)','F_B = B I L sin θ ...(1)','F_B = B I L sin θ ...(1)'),
 pair('If N particles of charge q pass by a given point in time t, they constitute a current; then, by definition of current,','اگر وقت t میں بار q کے N ذرات کسی مقام سے گزریں تو وہ رو بناتے ہیں؛ رو کی تعریف کے مطابق،','که په وخت t کې د q چارج N ذرات له یوه ټاکلي ټکي تېر شي، جریان جوړوي؛ د جریان د تعریف له مخې،'),
 pair('I = Nq/t ...(2)','I = Nq/t ...(2)','I = Nq/t ...(2)'),
 pair('By definition of velocity,','رفتار کی تعریف کے مطابق،','د سرعت د تعریف له مخې،'),
 pair('v = L/t, or L = vt ...(3)','v = L/t، یا L = vt ...(3)','v = L/t، یا L = vt ...(3)'),
 pair('Putting equation 2 and equation 3 in equation 1, we get','مساوات 2 اور مساوات 3 کو مساوات 1 میں رکھنے سے','د 2 او 3 معادلو په 1 معادله کې په ایښودلو سره'),
 pair('F_B = B × (Nq/t) × (vt) sin θ','F_B = B × (Nq/t) × (vt) sin θ','F_B = B × (Nq/t) × (vt) sin θ'),
 pair('or F_B = B N q v sin θ','یا F_B = B N q v sin θ','یا F_B = B N q v sin θ'),
 pair('For a single particle, N = 1: F_B = Bqv sin θ, or F_B = qvB sin θ.','ایک ذرے کے لیے N = 1: F_B = Bqv sin θ، یا F_B = qvB sin θ۔','د یوه ذرې لپاره N = 1: F_B = Bqv sin θ، یا F_B = qvB sin θ.'),
 pair('In vector form, F⃗_B = q v⃗ × B⃗, or F⃗_B = qvB sin θ n̂.','سمتی صورت میں F⃗_B = q v⃗ × B⃗، یا F⃗_B = qvB sin θ n̂۔','په ویکتوري بڼه F⃗_B = q v⃗ × B⃗، یا F⃗_B = qvB sin θ n̂.'),
]
CIRCULAR=[
 pair('C. CIRCULAR MOTION OF CHARGE PARTICLE IN UNIFORM MAGNETIC FIELD','ج۔ یکساں مقناطیسی میدان میں بار دار ذرہ کی دائروی حرکت','ج. په یوشان مقناطیسي ساحه کې د چارج لرونکې ذرې دایروي حرکت'),
 pair('The path of a charged particle moving in a plane perpendicular to a uniform magnetic field is a circle. Let us consider a positively charged particle moving in a uniform magnetic field with its initial velocity perpendicular to the field. Let us assume the direction of the magnetic field is into the page as in Figure 13.19. As the particle changes the direction of its velocity in response to the magnetic force, the magnetic force remains perpendicular to the velocity.','یکساں مقناطیسی میدان کے عمود مستوی میں حرکت کرتے بار دار ذرے کا راستہ دائرہ ہوتا ہے۔ ایک مثبت بار دار ذرہ یکساں میدان میں اس کی ابتدائی رفتار کے میدان کے عمود ہونے کے ساتھ حرکت کرتا فرض کریں۔ شکل 13.19 کی طرح مقناطیسی میدان کو صفحے کے اندر کی سمت لیں۔ مقناطیسی قوت کے جواب میں ذرہ اپنی رفتار کی سمت بدلتا ہے، مگر مقناطیسی قوت رفتار کے عمود رہتی ہے۔','په یوشان مقناطیسي ساحه پر عمودې مستوي کې د خوځېدونکي چارج لرونکي ذرې لاره دایره ده. یو مثبت چارج لرونکی ذره په یوشان ساحه کې داسې ونیسئ چې لومړنی سرعت یې پر ساحه عمود وي. لکه په 13.19 شکل کې، مقناطیسي ساحه د پاڼې دننه لوري ته ونیسئ. ذره د مقناطیسي قوې په ځواب کې د سرعت لوری بدلوي، خو مقناطیسي قوه د سرعت پر لوري عمود پاتې کېږي.'),
 pair('QUIZ?','سوال؟','پوښتنه؟'),
 pair('1. Why is wheat flour usually passed near a magnet before being packed?','1۔ پیک کرنے سے پہلے گندم کے آٹے کو عموماً مقناطیس کے قریب سے کیوں گزارا جاتا ہے؟','1. غنم اوړه ولې عموماً له بسته‌بندۍ مخکې مقناطیس ته نږدې تېرېږي؟'),
 pair('2. Why does a steel ship become magnetized as it is constructed?','2۔ تعمیر کے دوران فولادی جہاز مقناطیسی کیوں ہو جاتا ہے؟','2. د جوړېدو پر مهال فولادي کښتۍ ولې مقناطیسي کېږي؟'),
 pair('FIGURE 13.19 — Circular trajectory of charged particle in magnetic field.','شکل 13.19 — مقناطیسی میدان میں بار دار ذرے کا دائروی راستہ۔','13.19 شکل — په مقناطیسي ساحه کې د چارج لرونکې ذرې دایروي لاره.'),
 pair('The particle moves in a circle because the magnetic force F_B is perpendicular to v and B and has a constant magnitude qvB. The centripetal force F_c is provided by magnetic force F_B; therefore,','ذرہ دائرے میں حرکت کرتا ہے کیونکہ مقناطیسی قوت F_B، v اور B کے عمود ہے اور اس کی مقدار qvB مستقل ہے۔ مرکز مائل قوت F_c، مقناطیسی قوت F_B فراہم کرتی ہے؛ لہٰذا،','ذره په دایره کې خوځېږي، ځکه مقناطیسي قوه F_B پر v او B عمود ده او اندازه یې qvB ثابته ده. مرکزي قوه F_c مقناطیسي قوه F_B برابروي؛ نو،'),
 pair('F_c = F_B ...(1)','F_c = F_B ...(1)','F_c = F_B ...(1)'),
 pair('For a particle of mass m moving with velocity v in a circle of radius r, the centripetal force F_c is','د m کتلې د ذرې لپاره چې په r رداس کے دائرے میں رفتار v سے حرکت کرے، مرکز مائل قوت F_c یہ ہے:','د m کتلې لرونکې ذرې لپاره چې د r شعاع په دایره کې د v سرعت سره خوځېږي، مرکزي قوه F_c داسې ده:'),
 pair('F_c = mv²/r ...(2)','F_c = mv²/r ...(2)','F_c = mv²/r ...(2)'),
 pair('If the charge on the particle is +q and it is moving with velocity v perpendicular to a magnetic field of strength B, the magnetic force F_B is maximum, which is','اگر ذرہ پر بار +q ہو اور وہ قوتِ میدان B کے عمود رفتار v سے حرکت کرے تو مقناطیسی قوت F_B زیادہ سے زیادہ ہوتی ہے:','که د ذرې چارج +q وي او د B قوې لرونکي مقناطیسي ساحې پر عمود د v سرعت سره خوځېږي، مقناطیسي قوه F_B تر ټولو زیاته وي، یعنې'),
 pair('F_B = qvB ...(3)','F_B = qvB ...(3)','F_B = qvB ...(3)'),
 pair('Putting equation 2 and equation 3 in equation 1, we get','مساوات 2 اور 3 کو مساوات 1 میں رکھنے سے','د 2 او 3 معادلو په 1 معادله کې په ایښودلو سره'),
 pair('mv²/r = qvB; therefore mv/r = qB ...(4)','mv²/r = qvB؛ لہٰذا mv/r = qB ...(4)','mv²/r = qvB؛ نو mv/r = qB ...(4)'),
 pair('The relation between linear and angular velocity is v = rω; therefore equation 4 can be written as','خطی اور زاویائی رفتار کا تعلق v = rω ہے؛ لہٰذا مساوات 4 کو یوں لکھ سکتے ہیں:','د خطي او زاویوي سرعت اړیکه v = rω ده؛ نو 4 معادله داسې لیکلی شو:'),
 pair('mrω/r = qB, or mω = qB; rearranging, ω = qB/m ...(5)','mrω/r = qB، یا mω = qB؛ ترتیب بدلنے سے ω = qB/m ...(5)','mrω/r = qB، یا mω = qB؛ په ترتیب بدلولو ω = qB/m ...(5)'),
 pair('From the above equation, we can determine the time period T of the charged particle.','اوپر کی مساوات سے بار دار ذرے کا دورانیہ T معلوم کیا جا سکتا ہے۔','له پورته معادلې څخه د چارج لرونکې ذرې د دورې موده T معلومولی شو.'),
 pair('T = 2π/ω = 2π/(qB/m) = 2πm/qB, since f = 1/T','T = 2π/ω = 2π/(qB/m) = 2πm/qB، کیونکہ f = 1/T۔','T = 2π/ω = 2π/(qB/m) = 2πm/qB، ځکه f = 1/T.'),
 pair('Therefore f = qB/(2πm) ...(13.8)','لہٰذا f = qB/(2πm) ...(13.8)','نو f = qB/(2πm) ...(13.8)'),
 pair('This is often called the cyclotron frequency of a particle in a field because this is the frequency at which particles revolve in a cyclotron.','اسے اکثر میدان میں ذرہ کی سائکلوٹرون تعدد کہتے ہیں، کیونکہ یہ وہ تعدد ہے جس سے ذرات سائکلوٹرون میں گردش کرتے ہیں۔','دې ته په ساحه کې د ذرې سایکلوټرون فریکونسي وايي، ځکه همدا هغه فریکونسي ده چې ذرات پرې په سایکلوټرون کې تاوېږي.'),
]

def make(identity,title,printed,pairs,layout,titles,refs,diagram=None):
 r={'id':identity,'title':title,'kind':'lesson','pdfPage':57,'printedPage':printed,'sourcePdf':SOURCE,'paragraphs':[p[0] for p in pairs]}
 s=section(r,pairs,layout,titles);s['kind']='lesson';s['sourceReferences']=[ref(x) for x in refs]
 if diagram:s.update(diagram);s['content']+=diagram['diagramSvg']
 return r,s
def orbit19(lang):
 labels={'en':('B into the page','Circular trajectory of charged particle in magnetic field'),'ur':('B صفحے کے اندر','مقناطیسی میدان میں بار دار ذرے کا دائروی راستہ'),'ps':('B د پاڼې دننه','په مقناطیسي ساحه کې د چارج لرونکې ذرې دایروي لاره')}[lang]
 b='<circle cx="330" cy="180" r="108" fill="none" stroke="#d4a72c" stroke-width="3" stroke-dasharray="7 4"/><g stroke="#334155" stroke-width="2">'
 for x in [235,285,335,385,435]:
  for y in [65,115,165,215,265]: b+=f'<path d="M{x-6} {y-6}l12 12m0-12l-12 12"/>'
 b+='</g><g fill="#16a34a" stroke="#166534" stroke-width="2"><circle cx="330" cy="72" r="15"/><circle cx="424" cy="235" r="15"/><circle cx="236" cy="235" r="15"/></g><g fill="#fff" font-size="14"><text x="323" y="77">+</text><text x="417" y="240">+</text><text x="229" y="240">+</text></g><path d="M330 72L380 100M424 235L405 180M236 235L255 180" stroke="#dc2626" stroke-width="3"/><path d="M372 93l13 10-16 2M398 187l9-15 6 16M253 190l-4-17 14 9" fill="#dc2626"/><path d="M330 72L350 180M424 235L330 180M236 235L330 180" stroke="#2563eb" stroke-width="3"/><path d="M350 180L365 160M330 180L311 165M330 180L348 197" stroke="#16a34a" stroke-width="3"/><path d="M360 165l7-13 4 15M318 168l-14-5 10 13M345 194l7 13-15-6" fill="#16a34a"/><text x="354" y="169">r</text><text x="383" y="92">v</text><text x="368" y="153">F_B</text><text x="24" y="325" font-size="13">'+labels[0]+' · '+labels[1]+'</text>'
 return svg(b,'Figure 13.19: positively charged particle circular trajectory in a uniform magnetic field directed into the page.')

if __name__=='__main__':
 cond=make('phys13-force-on-current-carrying-conductor104','Force on a current-carrying conductor and a moving charged particle',104,CONDUCTOR,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'equation','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'equation','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'equation','indices':[6]},{'type':'paragraph','indices':[7]},{'type':'equation','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]}],('کرنٹ بردار موصل اور حرکت کرتے بار دار ذرے پر قوت','پر جریان‌لرونکي هادي او خوځنده چارج لرونکې ذرې قوه'),[104])
 circ=CIRCULAR
 motion=make('phys13-circular-motion-cyclotron-frequency104-105','Circular motion of a charged particle in a uniform magnetic field',104,circ,[{'type':'heading','indices':[0]},{'type':'paragraph','indices':[1]},{'type':'heading','indices':[2]},{'type':'paragraph','indices':[3]},{'type':'paragraph','indices':[4]},{'type':'paragraph','indices':[5]},{'type':'visual'},{'type':'paragraph','indices':[6]},{'type':'equation','indices':[7]},{'type':'paragraph','indices':[8]},{'type':'equation','indices':[9]},{'type':'paragraph','indices':[10]},{'type':'equation','indices':[11]},{'type':'paragraph','indices':[12]},{'type':'equation','indices':[13]},{'type':'paragraph','indices':[14]},{'type':'equation','indices':[15]},{'type':'paragraph','indices':[16]},{'type':'equation','indices':[17]},{'type':'equation','indices':[18]},{'type':'paragraph','indices':[19]}],('یکساں مقناطیسی میدان میں بار دار ذرہ کی دائروی حرکت','په یوشان مقناطیسي ساحه کې د چارج لرونکې ذرې دایروي حرکت'),[104,105],{'diagramSvg':orbit19('en'),'diagramSvgUrdu':orbit19('ur'),'diagramSvgPashto':orbit19('ps')})
 records=[cond[0],motion[0]];sections=[cond[1],motion[1]]
 formulas=[{'id':'phys13-force-current-conductor','name':'Magnetic force on a current-carrying conductor','formula':CONDUCTOR[2][0],'latex':'F_B=BIL sin θ','sourceReferences':[ref(104)]},{'id':'phys13-force-single-moving-charge','name':'Magnetic force on a single moving charge','formula':CONDUCTOR[10][0],'latex':'F_B=qvB sin θ','sourceReferences':[ref(104)]},{'id':'phys13-cyclotron-frequency-13-8','name':'Cyclotron frequency','number':'13.8','formula':CIRCULAR[18][0],'latex':'f=qB/(2πm)','sourceReferences':[ref(105)]}]
 definitions=[{'term':'Cyclotron frequency','definition':CIRCULAR[19][0],'definitionUrdu':CIRCULAR[19][1],'definitionPashto':CIRCULAR[19][2],'sourceReferences':[ref(105)]}]
 with shared_class_data_lock():
  upsert(records,sections,chapter_index=2)
  sync_companions(chapter_index=2,retire_sections=['13.5'],trim_sections=[{'id':'13.6','startsAt':'D. DETERMINATION OF CHARGE TO MASS RATIO FOR AN ELECTRON','title':'Electron charge-to-mass ratio — first unchecked text on printed page 106'}],formulas=formulas,definitions=definitions)
 progress=json.loads((ROOT/'docs/source-verification/class-12/progress.json').read_text(encoding='utf-8'))
 if progress['nextPage']==57:
  checkpoint(57,'corrected_verified',[r['id'] for r in records],'Rendered and inspected PDF page 57, printed pages 104–105. Compared the current-carrying-conductor force, derivation from current and velocity to the single-particle force, vector form, uniform-field circular trajectory, Quiz questions, centripetal-force balance, equations leading to cyclotron frequency (13.8), and Figure 13.19. Added a native translated SVG trajectory and synchronized force/cyclotron formulas and definition. Preserved the legacy continuation from the next unchecked printed-page-106 section.',printed_pages=[104,105],chapter_number=13)
