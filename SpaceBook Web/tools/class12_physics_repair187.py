"""PDF187 full critical-mass source and all three coded visuals."""
import math
from class12_source_review import upsert, section, shared_class_data_lock
from class12_fidelity_repair import stage_reference
from class12_physics_repair189 import text, arrow, isotope, svg
from class12_physics_repair186 import cluster
SOURCE='Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf'
T=[];L=[]
def add(kind,en,ur,ps):L.append({'type':kind,'indices':[len(T)]});T.append((en,ur,ps))
add('heading','FIGURE 20.16','شکل20.16','شکل20.16')
add('heading','A NUCLEAR CHAIN REACTION','ایک نیوکلیائی زنجیری تعامل','یو هستوي ځنځیري تعامل')
L.append({'type':'visual','blockId':'phys20-187-chain'})
add('paragraph','The successive fissioning of ever-increasing numbers of uranium-235 atoms.','یورینیم-235 کے مسلسل بڑھتی ہوئی تعداد والے ایٹموں کا پے در پے انشقاق۔','د یورانیم-235 د پرله پسې زیاتېدونکي شمېر اټومونو یو په بل پسې انشقاق.')
add('definition','The minimum amount of mass required to sustain a fission chain reaction is called critical mass. If the amount of uranium is too small the chain reaction will stop. If a chain reaction is to continue it is necessary that the mass of uranium must be greater or equal to this critical mass.',
 'انشقاقی زنجیری تعامل کو برقرار رکھنے کے لیے درکار کم سے کم کمیت کو نازک کمیت کہتے ہیں۔ اگر یورینیم کی مقدار بہت کم ہو تو زنجیری تعامل رک جائے گا۔ زنجیری تعامل جاری رہنے کے لیے ضروری ہے کہ یورینیم کی کمیت اس نازک کمیت سے زیادہ یا اس کے برابر ہو۔',
 'د انشقاق د ځنځیري تعامل د ساتلو لپاره اړینه تر ټولو کمه کتله بحراني کتله بلل کېږي. که د یورانیم اندازه ډېره کمه وي، ځنځیري تعامل به ودرېږي. د ځنځیري تعامل د دوام لپاره اړینه ده چې د یورانیم کتله له دې بحراني کتلې زیاته یا ورسره برابره وي.')
add('paragraph','The mass less than critical mass is called sub-critical and mass greater then critical mass is called super-critical as shown in figure 20.17.',
 'نازک کمیت سے کم کمیت کو تحت نازک اور نازک کمیت سے زیادہ کمیت کو فوق نازک کہتے ہیں، جیسا کہ شکل20.17 میں دکھایا گیا ہے۔',
 'له بحراني کتلې کمه کتله تر بحراني کچې ټیټه او تر بحراني کتلې زیاته کتله له بحراني کچې لوړه بلل کېږي، لکه په20.17 شکل کې چې ښودل شوي دي.')
add('heading','FIGURE 20.17','شکل20.17','شکل20.17')
L.append({'type':'visual','blockId':'phys20-187-critical-mass'})
add('paragraph','(a) In a sub-critical mass, too many neutrons escape before colliding (b) in the critical mass, enough neutrons encounter other nuclei to maintain a chain reaction.',
 '(a) تحت نازک کمیت میں بہت زیادہ نیوٹرون تصادم سے پہلے نکل جاتے ہیں (b) نازک کمیت میں کافی نیوٹرون دوسرے نیوکلئیسوں سے ٹکراتے ہیں، جس سے زنجیری تعامل برقرار رہتا ہے۔',
 '(a) تر بحراني کچې په ټیټه کتله کې ډېر نیوټرونونه له ټکر مخکې وځي (b) په بحراني کتله کې کافي نیوټرونونه له نورو هستو سره مخامخ کېږي او ځنځیري تعامل ساتي.')
add('paragraph',r'However Natural uranium consists of only about 0.7% of \({}^{235}\mathrm{U}\) and 99.3% \({}^{238}\mathrm{U}\), which means that most of the available uranium nuclei generally do not participate in the fission process but instead remove neutrons from being able to produce other fissions. To overcome this problem it is necessary to use enriched uranium, in which the abundance of \({}^{235}\mathrm{U}\) is increased beyond its natural value of 0.7%.',
 r'تاہم قدرتی یورینیم میں صرف تقریباً0.7% \({}^{235}\mathrm{U}\) اور99.3% \({}^{238}\mathrm{U}\) ہوتا ہے، جس کا مطلب ہے کہ یورینیم کے بیشتر دستیاب نیوکلئیس عموماً انشقاق میں حصہ نہیں لیتے، بلکہ نیوٹرونوں کو دوسرے انشقاق پیدا کرنے کے قابل رہنے سے روک دیتے ہیں۔ اس مسئلے پر قابو پانے کے لیے افزودہ یورینیم استعمال کرنا ضروری ہے، جس میں \({}^{235}\mathrm{U}\) کی مقدار اس کی قدرتی قدر0.7% سے بڑھا دی جاتی ہے۔',
 r'خو طبیعي یورانیم یوازې شاوخوا0.7% \({}^{235}\mathrm{U}\) او99.3% \({}^{238}\mathrm{U}\) لري؛ دا معنا لري چې د یورانیم ډېری موجودې هستې عموماً په انشقاق کې برخه نه اخلي، بلکې نیوټرونونه له نورو انشقاقونو د رامنځته کولو څخه باسي. د دې ستونزې د حل لپاره باید غني شوی یورانیم وکارول شي، چې په هغه کې د \({}^{235}\mathrm{U}\) اندازه له طبیعي0.7% څخه زیاته شوې وي.')
add('paragraph','Fission may take place in any of the heavy nuclei after capture of a neutron. However, low-energy neutrons are able to cause fission only in U-233, U-235, and Pu-239.',
 'نیوٹرون جذب کرنے کے بعد کسی بھی بھاری نیوکلئیس میں انشقاق ہو سکتا ہے۔ تاہم کم توانائی والے نیوٹرون صرف U-233، U-235 اور Pu-239 میں انشقاق پیدا کر سکتے ہیں۔',
 'د نیوټرون له جذب وروسته په هره درنه هسته کې انشقاق پېښېدای شي. خو د ټیټې انرژۍ نیوټرونونه یوازې په U-233، U-235 او Pu-239 کې انشقاق رامنځته کولی شي.')
L.append({'type':'visual','blockId':'phys20-187-fuel-pellets'})
add('paragraph','Fuel pellets contain enriched uranium-235. Each pellet contains the energy equivalent of 1 ton of coal.','ایندھن کی گولیوں میں افزودہ یورینیم-235 ہوتا ہے۔ ہر گولی میں1 ٹن کوئلے کے برابر توانائی ہوتی ہے۔','د سون ګولۍ غني شوی یورانیم-235 لري. هره ګولۍ د1 ټن ډبرو سکرو معادل انرژي لري.')
def trail(x1,y1,x2,y2,color='#38bdf8'):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="17" opacity=".25"/>'+arrow(x1,y1,x2,y2,'#0284c7')
def neutron(x,y):return f'<circle cx="{x}" cy="{y}" r="6" fill="#0284c7" stroke="#075985"/>'+isotope(x-2,y+30,1,0,'n')
CHAIN=[{'y':135,'upper':(87,35,'Br'),'lower':(146,57,'La'),'leaves':[45,143],'escape':'up'}, {'y':334,'upper':(93,36,'Kr'),'lower':(140,56,'Ba'),'leaves':[242,342]}, {'y':533,'upper':(90,37,'Rb'),'lower':(144,55,'Cs'),'leaves':[441,541],'escape':'down'}]
def chain(lang):
    out=trail(20,335,151,335)+neutron(58,335)+cluster(186,335,40)+isotope(165,402,235,92,'U')
    for x,y,nuclide in [(273,267,(93,36,'Kr')),(274,404,(140,56,'Ba'))]:out+=trail(209,335,x,y)+cluster(x,y,24)+isotope(x+65 if nuclide[2]=='Kr' else x,y+30 if nuclide[2]=='Kr' else y+62,*nuclide)
    for branch in CHAIN:
        y=branch['y'];out+=trail(226,335,448,y)+neutron(388,y+(335-y)*.25)+cluster(475,y,38)+isotope(458,y+64,235,92,'U')
        for fy,species in [(y-57,branch['upper']),(y+57,branch['lower'])]:out+=trail(496,y,566,fy)+cluster(585,fy,23)+isotope(645,fy+8,*species)
        for ly in branch['leaves']:
            out+=trail(517,y,842,ly)+neutron(763,ly+(y-ly)*.18)+cluster(882,ly,32)+isotope(955,ly+8,235,92,'U')
        if branch.get('escape'):
            ey=25 if branch['escape']=='up' else 663
            out+=trail(503,y,664,ey)+neutron(664,ey)
    return svg(out,1000,717,{'en':'Figure20.16: uranium235 fission produces krypton93 and barium140 then three uranium235 fissions; their products are bromine87/lanthanum146, krypton93/barium140 and rubidium90/caesium144. Six uranium235 targets receive neutrons; top and bottom branches also show escaping neutrons. Source labels and displayed neutron paths retained.','ur':'شکل20.16: یورینیم235 سے کرپٹون93 اور بیریم140، پھر یورینیم235 کے تین انشقاق؛ ان سے برومین87/لینتھینم146، کرپٹون93/بیریم140 اور روبیڈیم90/سیزیم144 بنتے ہیں۔ چھ یورینیم235 ہدف نیوٹرون حاصل کرتے ہیں؛ اوپر اور نیچے کی شاخوں میں نکل جانے والے نیوٹرون بھی ہیں۔ اصل لیبل اور راستے محفوظ ہیں۔','ps':'شکل20.16: د یورانیم235 انشقاق کریپټون93 او باریم140 جوړوي، بیا د یورانیم235 درې انشقاقونه؛ محصولات یې برومین87/لانتانیم146، کریپټون93/باریم140 او روبیډیم90/سیزیم144 دي. د یورانیم235 شپږ هدفونه نیوټرونونه ترلاسه کوي؛ پورته او لاندې څانګې وتونکي نیوټرونونه هم ښيي. اصلي نښې او لارې ساتل شوي دي.'}[lang])
def critical(lang):
    out=''
    for cx,cy,r,n,label in [(160,185,79,4,'(a)'),(518,185,145,10,'(b)')]:
        out+=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f5f3ff" stroke="#854d0e" stroke-width="3"/>'
        points=[(cx,cy)]+[(cx+r*.59*math.cos(i*math.tau/(n-1)),cy+r*.59*math.sin(i*math.tau/(n-1))) for i in range(n-1)]
        for i,(x,y) in enumerate(points):
            out+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="'+('#fbbf24' if i==0 else '#a5f3fc')+'" stroke="#334155"/>'
            for a in (i*.9+.2,i*.9+2.3,i*.9+4.3):
                reach=71 if n==4 else 36;out+=arrow(x+math.cos(a)*11,y+math.sin(a)*11,x+math.cos(a)*reach,y+math.sin(a)*reach,'#475569')
            if i>0 and n==10:
                px,py=points[(i%(n-1))+1];out+=arrow(x,y,px,py,'#475569')
        out+=text(cx,cy+r+40,label,24)
    return svg(out,720,403,{'en':'Figure20.17: smaller sub-critical mass with escaping neutron paths and larger critical mass with many paths meeting other nuclei. Panels a and b follow the printed caption.','ur':'شکل20.17: چھوٹی تحت نازک کمیت سے نیوٹرون نکل جاتے ہیں، جبکہ بڑی نازک کمیت میں بہت سے راستے دوسرے نیوکلئیسوں سے ملتے ہیں۔ حصے a اور b اصل عنوان کے مطابق ہیں۔','ps':'شکل20.17: له کوچنۍ، تر بحراني کچې ټیټې کتلې نیوټرونونه وځي، خو په لویه بحراني کتله کې ډېرې لارې له نورو هستو سره مخامخ کېږي. برخې a او b د اصلي تشریح مطابق دي.'}[lang])
def pellets(lang):
    out='<rect x="15" y="15" width="460" height="260" fill="#eff6ff"/>'
    for x in range(15,476,32):out+=f'<path d="M{x} 15V275" stroke="#cbd5e1"/>'
    for y in range(15,276,32):out+=f'<path d="M15 {y}H475" stroke="#cbd5e1"/>'
    for x,y in [(191,153),(232,149),(272,167),(229,179)]:out+=f'<path d="M{x-18} {y-17}v31a18 10 0 0 0 36 0v-31" fill="#1e293b" stroke="#020617"/><ellipse cx="{x}" cy="{y-17}" rx="18" ry="10" fill="#475569" stroke="#020617"/>'
    return svg(out,490,290,{'en':'Coded schematic of the unnumbered source photograph: a small group of dark cylindrical enriched uranium fuel pellets on a grid surface.','ur':'بغیر نمبر اصل تصویر کا کوڈ شدہ خاکہ: جالی دار سطح پر افزودہ یورینیم کے ایندھن کی چھوٹی سیاہ بیلن نما گولیوں کا گروہ۔','ps':'د بې شمېرې اصلي انځور کوډ شوې طرحه: پر جال لرونکې سطحه د غني شوي یورانیم د سون د وړو تورو سلنډري ګولیو یوه ډله.'}[lang])
record={'id':'phys20-critical-mass-natural-uranium-and-enrichment-362-363','title':'Critical mass, uranium enrichment and fission chain','kind':'lesson','pdfPage':187,'printedPage':362,'sourcePdf':SOURCE,'paragraphs':[x[0] for x in T]}
issues=['Figure20.16 shows two outgoing neutrons on the middle93Kr/140Ba branch and three on the90Rb/144Cs lower branch. These visible paths do not form balanced complete reaction counts; the source diagram is retained without adding or removing neutron paths.','The prose describes sub-critical and super-critical masses while Figure20.17 caption describes sub-critical and critical masses. Both source wordings retained.']
sec=section(record,T,L,('نازک کمیت، یورینیم کی افزودگی اور انشقاقی زنجیر','بحراني کتله، د یورانیم غني کول او د انشقاق ځنځیر'))
sec.update(kind='lesson',sourceClass12Physics=True,sourceReferences=[{'pdfPage':187,'printedPage':n,'sourcePdf':SOURCE} for n in (362,363)],sourceIssues=issues,sourceBlocks=[{'id':'phys20-187-chain','type':'figure','sourceFigure':'20.16','branchData':CHAIN,'svg':chain('en'),'svgUrdu':chain('ur'),'svgPashto':chain('ps')},{'id':'phys20-187-critical-mass','type':'figure','sourceFigure':'20.17','svg':critical('en'),'svgUrdu':critical('ur'),'svgPashto':critical('ps')},{'id':'phys20-187-fuel-pellets','type':'figure','representation':'Coded schematic of unnumbered source photograph','svg':pellets('en'),'svgUrdu':pellets('ur'),'svgPashto':pellets('ps')}])
if __name__=='__main__':
    with shared_class_data_lock():upsert([record],[sec],chapter_index=9)
    stage_reference(187,record,'Reinspected PDF187 printed362–363. Complete critical/sub/super-critical, natural composition, enrichment and low-energy fission text preserved. Figure20.16 includes all isotope labels (87Br/146La,93Kr/140Ba,90Rb/144Cs), six terminal uranium235 atoms, and source neutron paths. Figure20.17 and original full caption coded. Fuel pellet photo represented by coded cylinders/grid, retaining full caption and no invented figure number. All prose/labels aligned in Urdu/Pashto; visible source inconsistencies recorded.',issues)
    print('PDF187 full chain source and coded visuals staged.')
