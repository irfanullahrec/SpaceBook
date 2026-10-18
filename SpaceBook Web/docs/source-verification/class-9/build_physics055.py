from physics_page_tools import *

bar=lambda s:f'<tspan text-decoration="overline">{s}</tspan>'
p=[
pair('putting these values in graph equation we get','گراف کی مساوات میں یہ قدریں رکھنے سے ملتا ہے۔','د ګراف په معادله کې د دې ارزښتونو په ایښودلو ترلاسه کوو'),
pair('B. Second Equation of Motion:','B. حرکت کی دوسری مساوات:','B. د حرکت دویمه معادله:'),
pair('Second equation of motion relates displacement s with initial velocity ‘vᵢ’ and acceleration ‘a’ in time ‘t’. As the area under velocity-time curve represents the displacement ‘s’ as shown in figure 2.14. Therefore, the displacement s of the object is:','حرکت کی دوسری مساوات وقت ‘t’ میں نقل مکانی s کو ابتدائی سمتی رفتار ‘vᵢ’ اور تعجیل ‘a’ سے مربوط کرتی ہے۔ شکل 2.14 کے مطابق سمتی رفتار وقت منحنی کے نیچے رقبہ نقل مکانی ‘s’ ظاہر کرتا ہے۔ اس لیے شے کی نقل مکانی s ہے:','د حرکت دویمه معادله په وخت ‘t’ کې بېځایه کېدل s له لومړني سرعت ‘vᵢ’ او تعجیل ‘a’ سره تړي. لکه په شکل 2.14 کې، د سرعت او وخت منحني لاندې مساحت بېځایه کېدل ‘s’ ښيي. نو د شي بېځایه کېدل s دی:'),
pair('Figure 2.15 Equations of Motion','شکل 2.15 حرکت کی مساوات','شکل 2.15 د حرکت معادلې'),
pair('putting values','قدریں رکھنے سے','د ارزښتونو په ایښودلو'),
pair('therefore','لہٰذا','نو'),
pair('C. Third Equation of Motion:','C. حرکت کی تیسری مساوات:','C. د حرکت درېیمه معادله:'),
pair('Third equation relate position s, velocity v (both final velocity v𝒇 and initial velocity vᵢ), and constant acceleration a without including time t. The area under the curve can be calculated by taking the total area of the trapezium OABD. The velocity-time graph the area of a trapezoid OABD will give the total displacement','تیسری مساوات مقام s، سمتی رفتار v (آخری v𝒇 اور ابتدائی vᵢ دونوں) اور مستقل تعجیل a کو وقت t شامل کیے بغیر مربوط کرتی ہے۔ منحنی کے نیچے رقبہ ذوزنقہ OABD کا کل رقبہ لے کر معلوم ہو سکتا ہے۔ سمتی رفتار وقت گراف میں ذوزنقہ OABD کا رقبہ کل نقل مکانی دے گا۔','درېیمه معادله موقعیت s، سرعت v (دواړه وروستی v𝒇 او لومړنی vᵢ) او ثابت تعجیل a د وخت t له شاملولو پرته سره تړي. د منحني لاندې مساحت د OABD ذوزنقې د ټول مساحت په اخیستلو محاسبه کېدای شي. د سرعت او وخت په ګراف کې د OABD ذوزنقې مساحت به ټول بېځایه کېدل ورکړي.')]

def relation(i,segment,rhs):
 return block(i,text(bar(segment)+' = '+rhs,5,43),w=190,h=75,ratio=.19)
db=relation('physics9-first-table-db','DB',sub('v','f'));dc=relation('physics9-first-table-dc','DC',sub('v','i'));cb=relation('physics9-first-table-cb','CB','at')
ac=relation('physics9-second-table-ac','AC','t');oa=relation('physics9-second-table-oa','OA',sub('v','i'));cb2=relation('physics9-second-table-cb','CB','at')
def table(i,title,rows,u,ps,refs):
 return dict(type='dataTable',id=i,title=title,headers=['',''],noHeader=True,sourceWidthRatio=.48,rows=[[t,dict(blockId=r['id'])] for t,r in zip(rows,refs)],translations=[dict(language='اردو',headers=['',''],rows=[[t,dict(blockId=r['id'])] for t,r in zip(u,refs)]),dict(language='پښتو',headers=['',''],rows=[[t,dict(blockId=r['id'])] for t,r in zip(ps,refs)])])
t1=table('physics9-first-equation-relations','First equation source relationship table',['Line DB represents, final velocity v𝒇','Line DC represents, initial velocity vᵢ','Line segment CB, in terms of slope gives'],['لکیر DB آخری سمتی رفتار v𝒇 ظاہر کرتی ہے','لکیر DC ابتدائی سمتی رفتار vᵢ ظاہر کرتی ہے','قطعہ CB ڈھال کے لحاظ سے دیتا ہے'],['DB کرښه وروستی سرعت v𝒇 ښيي','DC کرښه لومړنی سرعت vᵢ ښيي','CB ټوټه د میلان له مخې ورکوي'],[db,dc,cb])
t2=table('physics9-second-equation-relations','Second equation source relationship table',['Line segment AC represents, time t','Line OA represents, initial velocity vᵢ','Line segment CB, in terms of slope is'],['قطعہ AC وقت t ظاہر کرتا ہے','لکیر OA ابتدائی سمتی رفتار vᵢ ظاہر کرتی ہے','قطعہ CB ڈھال کے لحاظ سے ہے'],['AC ټوټه وخت t ښيي','OA کرښه لومړنی سرعت vᵢ ښيي','CB ټوټه د میلان له مخې ده'],[ac,oa,cb2])
geometry=block('physics9-first-equation-segments',text(bar('DB')+' = '+bar('DC')+' + '+bar('CB'),5,43),w=330,h=75,ratio=.37)
first=block('physics9-first-motion-equation212',text(sub('v','f')+' = '+sub('v','i')+' + at',5,43)+number('2.12',385,15),w=475,h=80,ratio=.53,label='Equation2.12 final velocity equals initial velocity plus acceleration times time')
b=text('displacement',105,30,'middle')+text('s',105,67,'middle')+text('=',235,47)+text('Area of rectangle',401,30,'middle')+text('OACD',401,67,'middle')+text('+',559,47)+text('Area of triangle',719,30,'middle')+text('Δ ACB',719,67,'middle')
parts=block('physics9-second-equation-area-parts',b,w=890,h=95,ratio=.98,ur=b.replace('displacement','نقل مکانی').replace('Area of rectangle','مستطیل کا رقبہ').replace('Area of triangle','مثلث کا رقبہ'),ps=b.replace('displacement','بېځایه کېدل').replace('Area of rectangle','د مستطیل مساحت').replace('Area of triangle','د مثلث مساحت'))
segments=block('physics9-second-equation-segment-products',text('s = ('+bar('OA')+' × '+bar('AC')+') +',5,65)+frac('1','2',315,30)+text('× ('+bar('AC')+' × '+bar('CB')+')',365,65),w=625,ratio=.66)
values=block('physics9-second-equation-values',text('s = '+sub('v','i')+' × t +',5,65)+frac('1','2',238,30)+text('× (t × at)',288,65),w=480,ratio=.51)
second=block('physics9-second-motion-equation213',text('s = '+sub('v','i')+'t +',5,65)+frac('1','2',170,30)+text('at²',222,65)+number('2.13',400),w=490,ratio=.54,label='Equation2.13 displacement equals initial velocity times time plus one half acceleration times time squared')
third=block('physics9-third-equation-trapezium',text('s =',5,65)+frac('1','2',85,30)+text('('+bar('OA')+' + '+bar('DB')+') × '+bar('OD'),138,65),w=485,ratio=.53)
source=json.loads((OUT/'physics-page-054.json').read_text(encoding='utf-8'))
graph=json.loads(json.dumps(next(b for b in source['sections'][0]['blocks'] if b['id']=='physics9-motion-equations-figure214')))
graph['id']='physics9-motion-equations-figure215'
for field in ['svg','svgUrdu','svgPashto']:
 s=graph[field].replace('Figure2.14','Figure2.15').replace('M274 103V250M267 103h14M267 250h14','')
 s=s.replace('<path d="M62 183L205 103"','<rect x="62" y="183" width="143" height="67" fill="#e7dfa2" fill-opacity=".7"/><polygon points="62,183 205,103 205,183" fill="#76aacb" fill-opacity=".7"/><path d="M62 183L205 103"')
 s=s.replace(text(sub('v','f'),295,176,'middle',20),'')
 graph[field]=s
graph['graphData']['shadedRegions']=[['O','A','C','D'],['A','C','B']]
layout=[dict(type='sourceDataTable',tableId=t1['id']),visual(geometry),para(0),visual(first),para(1,'heading'),para(2),visual(parts),visual(segments),dict(type='sourceDataTable',tableId=t2['id']),para(3,'heading'),visual(graph),para(4),visual(values),para(5),visual(second),para(6,'heading'),para(7),visual(third)]
save(55,'First equation2.12 / second equation2.13 / two proof tables / Figure2.15 / third proof beginning',[section('2.5','2.5 EQUATIONS OF MOTION','2.5 حرکت کی مساوات','2.5 د حرکت معادلې',p,[t1,db,dc,cb,geometry,first,parts,segments,t2,ac,oa,cb2,graph,values,second,third],layout)],'Fresh visible page inspection. Two original headerless three-row/two-column segment relationship tables restored as semantic tables with native overbar/subscript equation cells and explicit translated cells. All first/second-motion proof steps, equations2.12/2.13, half fractions and shaded rectangle/triangle Figure2.15 restored with original graph geometry at book ratios. Complete second/third proof prose and trapezium formula retained and aligned to translations.',tables=[t1,t2])
