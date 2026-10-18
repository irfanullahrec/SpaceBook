from physics_page_tools import *

bar=lambda s:f'<tspan text-decoration="overline">{s}</tspan>'
p=[
pair('Figure 2.16 Equations of Motion','شکل 2.16 حرکت کی مساوات','شکل 2.16 د حرکت معادلې'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('From first equation of motion','حرکت کی پہلی مساوات سے','د حرکت له لومړۍ معادلې څخه'),
pair('or','یا','یا'),
pair('The above equation becomes','اوپر کی مساوات بن جاتی ہے۔','پورتنۍ معادله داسې کېږي'),
pair('since','چونکہ','ځکه'),
pair('therefore','لہٰذا','نو'),
pair('or','یا','یا'),
pair('therefore','لہٰذا','نو'),
pair('TIP km/h to m/s','ترکیب km/h سے m/s','لارښوونه له km/h څخه m/s ته'),
pair('To convert km/h to m/s, divide by 3.6','km/h کو m/s میں تبدیل کرنے کے لیے 3.6 سے تقسیم کریں۔','د km/h په m/s د اړولو لپاره پر 3.6 ووېشئ.'),
pair('Figure 2.17 Trapezoid','شکل 2.17 ذوزنقہ','شکل 2.17 ذوزنقه'),
pair('The area of a trapezoid is given by','ذوزنقے کا رقبہ یوں دیا جاتا ہے۔','د ذوزنقې مساحت داسې ورکول کېږي'),
pair('which is simply the average of the parallel sides multiplied by the base.','یعنی متوازی اضلاع کی اوسط کو بنیاد سے ضرب دیا جاتا ہے۔','چې په ساده ډول د موازي اړخونو منځنۍ اندازه په قاعده ضرب کول دي.'),
pair('Example 2.5 SPEEDING MOTORCYCLIST','مثال 2.5 تیز ہوتا موٹر سائیکل سوار','بېلګه 2.5 ګړندی کېدونکی موټرسایکل چلوونکی'),
pair('A motorcyclist starts from rest and moves with uniform acceleration of 1.9 m/s² for 22 s. Find the (a) velocity and (b) distance covered?','موٹر سائیکل سوار سکون سے شروع کر کے 22 s تک 1.9 m/s² کی یکساں تعجیل سے حرکت کرتا ہے۔ (a) سمتی رفتار اور (b) طے کردہ فاصلہ معلوم کریں؟','یو موټرسایکل چلوونکی له سکون څخه پیل کوي او د 22 s لپاره په 1.9 m/s² یوشان تعجیل حرکت کوي. (a) سرعت او (b) وهل شوی واټن ومومئ؟'),
pair('GIVEN:','دیے گئے:','ورکړل شوي:'),
pair('initial velocity vᵢ = 0 m/s','ابتدائی سمتی رفتار vᵢ = 0 m/s','لومړنی سرعت vᵢ = 0 m/s'),
pair('acceleration a = 1.9 m/s²','تعجیل a = 1.9 m/s²','تعجیل a = 1.9 m/s²'),
pair('Total time t = 22 s','کل وقت t = 22 s','ټول وخت t = 22 s'),
pair('REQUIRED:','مطلوب:','غوښتل شوي:'),
pair('a. Final velocity v𝒇 = ?','a. آخری سمتی رفتار v𝒇 = ؟','a. وروستی سرعت v𝒇 = ؟'),
pair('b. Distance s = ?','b. فاصلہ s = ؟','b. واټن s = ؟'),
pair('Editorial source-review note: Figure 2.16 labels the full-height velocity bracket vᵢ, while the adjacent table identifies DB as v𝒇. Both printed labels are retained.','ادارتی ماخذ جائزے کا نوٹ: شکل 2.16 پوری بلندی کے سمتی رفتار بریکٹ کو vᵢ کہتی ہے، جبکہ ساتھ کا جدول DB کو v𝒇 ظاہر کرتا ہے۔ دونوں چھپے لیبل برقرار ہیں۔','د سرچینې د کتنې سمونیز یادښت: شکل 2.16 د ټولې لوړوالي د سرعت قوس vᵢ بولي، خو څنګ ته جدول DB په v𝒇 پېژني. دواړه چاپ شوې نښې ساتل شوې دي.')]

refs=[block('physics9-third-table-'+seg.lower(),text(bar(seg)+' = '+rhs,5,43),w=190,h=75,ratio=.19) for seg,rhs in [('DB',sub('v','f')),('OA',sub('v','i')),('OD','t')]]
rows=['Line DB represents, final velocity v𝒇','Line OA represents, initial velocity vᵢ','Line segment OD represents, time t']
u=['لکیر DB آخری سمتی رفتار v𝒇 ظاہر کرتی ہے','لکیر OA ابتدائی سمتی رفتار vᵢ ظاہر کرتی ہے','قطعہ OD وقت t ظاہر کرتا ہے']
ps=['DB کرښه وروستی سرعت v𝒇 ښيي','OA کرښه لومړنی سرعت vᵢ ښيي','OD ټوټه وخت t ښيي']
table=dict(type='dataTable',id='physics9-third-equation-relations',title='Third equation source relationship table',headers=['',''],noHeader=True,sourceWidthRatio=.47,rows=[[t,dict(blockId=r['id'])] for t,r in zip(rows,refs)],translations=[dict(language='اردو',headers=['',''],rows=[[t,dict(blockId=r['id'])] for t,r in zip(u,refs)]),dict(language='پښتو',headers=['',''],rows=[[t,dict(blockId=r['id'])] for t,r in zip(ps,refs)])])
source=json.loads((OUT/'physics-page-054.json').read_text(encoding='utf-8'))
graph=json.loads(json.dumps(next(b for b in source['sections'][0]['blocks'] if b['id']=='physics9-motion-equations-figure214')));graph['id']='physics9-motion-equations-figure216';graph['sourceWidthRatio']=.43
for field in ['svg','svgUrdu','svgPashto']:
 s=graph[field].replace('Figure2.14','Figure2.16').replace('OA=DC=vi, DB=vf, CB=at, OD=AC=t','OA=vi, DB printed bracket vi, OD=t; trapezium shade')
 s=s.replace('M236 103V183M229 103h14M229 183h14','').replace('<path d="M62 183H205" stroke="#a13436" stroke-width="2"/>','')
 for unwanted in [text('C',217,191,'middle',18),text('a',117,137,'middle',19),text('t',133,204,'middle',18),text(sub('v','i'),224,224,'middle',20),text('at',255,149,'middle',20)]:s=s.replace(unwanted,'')
 s=s.replace(text(sub('v','f'),295,176,'middle',20),text(sub('v','i'),295,176,'middle',20))
 s=s.replace('<path d="M62 183L205 103"','<polygon points="62,250 62,183 205,103 205,250" fill="#eee4a8" fill-opacity=".35"/><path d="M62 183L205 103"')
 graph[field]=s
graph['graphData']=dict(points=dict(O=['0','0'],A=['0','vi'],B=['t','vf'],D=['t','0'],E=['0','vf']),shadedRegions=[['O','A','B','D']],sourceFullHeightBracketLabel='vi',axes=['velocity v (ms⁻¹)','time t (s)'])
f1=block('physics9-third-motion-values',text('s =',5,65)+frac('1','2',80,30)+text('('+sub('v','i')+' + '+sub('v','f')+') × t',132,65),w=420,ratio=.46)
first=block('physics9-third-proof-first-equation',text(sub('v','f')+' = '+sub('v','i')+' + at',5,43),w=285,h=75,ratio=.33)
rearr=block('physics9-third-proof-time',text('at = '+sub('v','f')+' − '+sub('v','i'),5,65)+text('or',275,65)+text('t =',335,65)+frac(sub('v','f')+' − '+sub('v','i'),'a',405,125),w=575,ratio=.63,ur=(text('at = '+sub('v','f')+' − '+sub('v','i'),5,65)+text('یا',275,65)+text('t =',335,65)+frac(sub('v','f')+' − '+sub('v','i'),'a',405,125)),ps=(text('at = '+sub('v','f')+' − '+sub('v','i'),5,65)+text('یا',275,65)+text('t =',335,65)+frac(sub('v','f')+' − '+sub('v','i'),'a',405,125)))
f2=block('physics9-third-proof-substitute-time',text('s =',5,65)+frac('1','2',80,30)+text('('+sub('v','i')+' + '+sub('v','f')+') ×',135,65)+frac('('+sub('v','f')+' − '+sub('v','i')+')','a',350,150),w=555,ratio=.61)
f3=block('physics9-third-proof-product',text('s =',5,65)+frac('1','2a',80,45)+text('('+sub('v','i')+' + '+sub('v','f')+')('+sub('v','f')+' − '+sub('v','i')+')',150,65),w=570,ratio=.62)
identity=block('physics9-difference-squares-identity',text('(a + b) × (a − b) = a² − b²',5,45),w=490,h=80,ratio=.54)
identityv=block('physics9-velocity-difference-squares',text('('+sub('v','i')+' + '+sub('v','f')+')('+sub('v','f')+' − '+sub('v','i')+') = '+sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),5,45),w=565,h=80,ratio=.62)
f4=block('physics9-third-motion-displacement-fraction',text('s =',5,65)+frac(sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),'2a',90,160),w=300,ratio=.34)
third=block('physics9-third-motion-equation214',text('2as = '+sup(sub('v','f'),'2')+' − '+sup(sub('v','i'),'2'),5,43)+number('2.14',430,15),w=515,h=80,ratio=.57,label='Equation2.14 twice acceleration times displacement equals final velocity squared minus initial velocity squared')
trapbody='<polygon points="80,161 80,105 208,26 208,157" fill="#efe9ba" fill-opacity=".6" stroke="#317b9c" stroke-width="3"/>'+text(sub('l','1'),52,139,'middle',21)+text(sub('l','2'),236,103,'middle',21)+text('w',148,181,'middle',21)
trap=block('physics9-trapezoid-figure217',trapbody,w=275,h=190,ratio=.33,label='Figure2.17 trapezoid with parallel vertical sides l1/l2 and horizontal width w',kind='vector')
trapformula=block('physics9-trapezoid-area',text('A =',5,65)+frac('1','2',80,30)+text('('+sub('l','1')+' + '+sub('l','2')+') × w',134,65),w=460,ratio=.41)
layout=[dict(type='sourceDataTable',tableId=table['id']),para(0,'heading'),visual(graph),para(1),visual(f1),para(2),visual(first),para(3),visual(rearr),para(4),visual(f2),visual(f3),para(5),visual(identity),para(6),visual(identityv),para(7),visual(f4),para(8),visual(third),para(9,'heading'),para(10,'quotation'),para(11,'heading'),visual(trap),para(12),visual(trapformula),para(13),para(14,'heading'),para(15),dict(type='parallelPhrases',columns=[[16,17,18,19],[20,21,22]]),para(23,'quotation')]
num=dict(num='2.5',name='SPEEDING MOTORCYCLIST',statement=p[15]['text'],given='\n'.join(q['text'] for q in p[17:20]),required=p[21]['text']+'\n'+p[22]['text'],formula='',solution='',answer='',sourcePendingContinuation=True,sourcePdfPage=56,sourcePrintedPage=51,pairedParagraphs=p[15:23])
save(56,'Third equation2.14 proof / table / Figure2.16 / trapezoid Figure2.17 / Example2.5 beginning',[section('2.5','2.5 EQUATIONS OF MOTION','2.5 حرکت کی مساوات','2.5 د حرکت معادلې',p,[table,*refs,graph,f1,first,rearr,f2,f3,identity,identityv,f4,third,trap,trapformula],layout)],'Fresh visible PDF and3.2x graph crop inspection. Third proof relationship table, full substitution/algebra, difference-of-squares box and numbered2.14 equation recreated with native fractions/overbars/subscripts/powers. Figure2.16 printed full-height vi label retained and separately explained; trapezoid parallel sides l1/l2,w and area formula preserved. Conversion tip and actual motorcyclist Example2.5 data/questions restored; source solution pending next page. All original prose and table/figure labels explicitly translated at book size.',tables=[table],numericals=[num])
