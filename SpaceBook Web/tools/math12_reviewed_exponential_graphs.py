"""Printed page 38, visually checked against JPG and full PDF spread 23."""
from math import log
from math12_reviewed_unit1 import heading, paragraph, page

BASE={'type':'source-function-graph','xMin':-10,'xMax':10,'yMin':-10,'yMax':12,'xTicks':[-10,-5,0,5,10],'yTicks':[-10,-5,5,10]}
GROWTH={**BASE,'title':'y = 2ˣ','exponentialPair':[log(2)],'points':[[-5,2**-5,'(−5,0.03)'],[-1,.5,'(−1,0.5)'],[0,1,'(0,1)'],[1,2,'(1,2)'],[2,4,'(2,4)'],[3,8,'(3,8)']]}
PAIR={**BASE,'title':'y = 2ˣ and y = 2⁻ˣ','exponentialPair':[log(2),-log(2)],'points':[[-3,8,'(−3,8)'],[-2,4,'(−2,4)'],[-1,2,'(−1,2)'],[0,1,'(0,1)'],[1,2,'(1,2)'],[2,4,'(2,4)'],[3,8,'(3,8)'],[-5,2**-5,'(−5,0.03)'],[5,2**-5,'(5,0.03)']]}
GENERAL={**BASE,'title':'General exponential shapes (representative bases 2 and ½)','exponentialPair':[log(2),-log(2)]}
PAGES=[page('023_page_2.jpg',38,[
    heading('ii. Graphically representation of f(x) = aˣ'),
    heading('Example 14'),paragraph('Sketch the graph of y = 2ˣ.'),heading('Solution'),
    paragraph('To hand sketch graphs of equations such as y = 2ˣ or y = 2⁻ˣ simply make a table assigning integers to x, plot the resulting points, and then join these points with a smooth curve as shown in Figure 2.11.'),
    heading('y = 2ˣ'),{'type':'dataTable','headers':['x','−5','−1','0','1','2','3'],'rows':[['y','0.03','0.5','1','2','4','8']]},
    heading('y = 2⁻ˣ'),{'type':'dataTable','headers':['x','−3','−2','−1','0','1','5'],'rows':[['y','8','4','2','1','0.5','0.03']]},
    {'type':'diagram','id':'math12-source-figure-2-11','caption':'Figure 2.11','diagram':GROWTH},
    paragraph(r'It is useful to compare the graphs \(y=2^x\) and \(y=2^{-x}\) by plotting both on the same set of coordinate axes as shown in Figures 2.12. The graph of \(f(x)=b^x,\ b>1\) shown in Figure 2.13 looks very much like the graph of \(y=2^x\), and the graph of \(f(x)=b^{-x},\ 0<b<1\) in Figure 2.13 looks very much like the graph of \(y=2^{-x}\).'),
    {'type':'diagram','id':'math12-source-figure-2-12','caption':'Figure 2.12','diagram':PAIR},
    {'type':'diagram','id':'math12-source-figure-2-13','caption':'Figure 2.13','diagram':GENERAL},
    {'type':'clarification','text':'SpaceBook clarification: Figure 2.13 illustrates general increasing and decreasing shapes without specifying a base; this digital drawing uses representative bases 2 and ½. The source labels its decreasing curve y = b⁻ˣ with 0 < b < 1. That expression would increase: the decreasing case is y = bˣ for 0 < b < 1, as stated in property 4 below. The printed wording is retained above.'},
    paragraph('The graphs in Figures 2.12 and Figures 2.13 suggest the following important general properties of exponentia functions that are summarized in the box below:'),
    heading('Remember'),heading('Basic properties of the graph of f(x) = bˣ, b > 0, b ≠ 1'),
    {'type':'list','items':['1. All graphs will pass through the point (0, 1).','2. All graphs are continuous curves, with no holes or jumps.','3. If b > 1, then bˣ increases as x increases.','4. If 0 < b < 1, then bˣ decreases as x increases.']}
])]
PAGES[0]['visualStatus']='Two value tables and four properties rendered digitally; Figures 2.11–2.13 reconstructed as SVG, with representative bases disclosed for the general illustration'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':23,'side':'right','reason':'Full PDF resolves exponential signs, graph points and the four-property box.'}
