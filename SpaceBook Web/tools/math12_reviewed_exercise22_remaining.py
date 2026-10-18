"""Learning enhancements for Exercise 2.2 Q4–8; source and keys checked separately."""
from math import e, log, sqrt, pi

def graph(q,label,title,**settings):
    return {'type':'diagram','id':f'math12-ex22-q{q}-{label}','caption':f'SpaceBook learning graph ({label})','diagram':{'type':'source-function-graph','title':title,**settings}}
def log_graph(q,label,title,shift=0,scale=1,offset=0,base=e,xmin=-5,xmax=22,ymin=-6,ymax=12,**extra):
    return graph(q,label,title,xMin=xmin,xMax=xmax,yMin=ymin,yMax=ymax,xTicks=[x for x in [-5,0,5,10,15,20] if xmin<=x<=xmax],yTicks=[y for y in [-5,0,5,10] if ymin<=y<=ymax],logarithm={'base':base,'shift':shift,'scale':scale,'offset':offset,**extra})
def table(label,xs,fn):
    return {'type':'dataTable','headers':['x']+[str(x) for x in xs],'rows':[[label]+[f'{fn(x):.3f}' for x in xs]]}

STEPS=[
    ['For every natural logarithm, require its argument to be positive. Use a calculator to evaluate the sample points shown in the tables.', '(a) y = ln x has domain x > 0, intercept (1, 0), vertical asymptote x = 0, and increases. (b) y = −ln x reflects that curve across the x-axis and decreases.', '(c) y = 2ln(x + 2) shifts ln x two units left and doubles its height. Domain x > −2, asymptote x = −2, intercept (−1, 0).', '(d) y = 4ln(x − 3) shifts ln x three units right and stretches it vertically by 4. Domain x > 3, asymptote x = 3, intercept (4, 0).', '(e) y = 4ln x − 2 stretches ln x vertically by 4 and moves it down 2. Domain x > 0, asymptote x = 0, intercept (√e, 0).', 'Draw smooth curves through the table points on their valid domains. Every range is ℝ; the vertical asymptotes are never part of the curves.'],
    ['(a) From x = 3 − t, obtain t = 3 − x. Substituting into y = 2t gives y = 6 − 2x.', 'At t = 0, 1, 2, the points are (3, 0), (2, 2), (1, 4). All real t produce the entire line; increasing t gives direction (−1, 2).', '(b) Divide x = 4cos t and y = −3sin t by their amplitudes, square, and add: x²/16 + y²/9 = cos²t + sin²t = 1.', 'The ellipse is centered at (0, 0), with horizontal semi-axis 4 and vertical semi-axis 3. Its endpoints are (±4, 0) and (0, ±3).', 'For t = 0, π/2, π, 3π/2, 2π, the points are (4, 0), (0, −3), (−4, 0), (0, 3), (4, 0). As t increases, travel clockwise; with unrestricted t, the ellipse repeats.'],
    ['(a) e⁻²ˣ is decreasing, passes through (0, 1), and has horizontal asymptote y = 0. (b) (2/3)e³ˣ is increasing, passes through (0, 2/3), and has the same asymptote.', '(c) 4ˣ is increasing through (0, 1). (d) 4⁻ˣ is its reflection across the y-axis and decreases through (0, 1). All four exponential domains are ℝ and ranges are (0, ∞).', '(e) log₂(x + 5) is increasing on x > −5, has asymptote x = −5 and intercept (−4, 0). Its range is ℝ.', '(f) log₂(x²) = 2log₂|x| is defined for x ≠ 0. It has two symmetric branches, intercepts (−1, 0), (1, 0), range ℝ, and vertical asymptote x = 0.', '(g) ln(2x − 5) is defined for x > 5/2. It is increasing, has intercept (3, 0), range ℝ and vertical asymptote x = 5/2.', 'Plot the anchor points and smooth curves shown in the learning graphs. Keep each function on its valid domain and do not join across a vertical asymptote.'],
    ['(a) x² + y² = 4 is a circle with center (0, 0) and radius 2. Mark (±2, 0) and (0, ±2).', '(b) x² + y² = 16 is a circle with center (0, 0) and radius 4. Mark (±4, 0) and (0, ±4).', '(c) x²/25 + y²/9 = 1 is an ellipse with horizontal semi-axis 5 and vertical semi-axis 3. Its vertices are (±5, 0), co-vertices (0, ±3), and foci (±4, 0).', '(d) x²/36 + y²/6 = 1 has horizontal semi-axis 6 and vertical semi-axis √6. Its vertices are (±6, 0), co-vertices (0, ±√6), and foci (±√30, 0).', 'Draw each smooth closed curve through its four axis endpoints, using equal units on the x- and y-axes. These are implicit equations; none is one single-valued function y of x.'],
    ['Choose an explicit plot command for Q1(a), (b), (c), (d), (f), and (g). Use an implicit plot command for the circle in Q1(e). The ranges below are chosen learning windows, not printed exercise ranges.', 'For (a), the coefficient a needs a value before drawing a numerical graph. The example command below uses a = 1, explicitly chosen for illustration.', 'For the logarithm in (d), express base 2 as ln(x)/ln(2) and restrict x to positive values. For the hyperbolic quotient in (f), split the range at x = 0.', 'For the square root in (g), restrict x ≥ 8. For the circle, plot the entire relation x² + y² = 36.', 'Enter the seven commands shown below and compare the result with the classification in Q1. The commands are learning enhancements; their mathematical expressions and domains have been checked.']
]
ANSWERS=[
    '(a)–(e) have range ℝ. Domains: (a),(b),(e): (0, ∞); (c): (−2, ∞); (d): (3, ∞). The graphs below show the required transformations.',
    '(a) y = 6 − 2x, direction (−1, 2). (b) x²/16 + y²/9 = 1, travelled clockwise as t increases.',
    '(a)–(d): exponential curves, domain ℝ, range (0, ∞). (e): x > −5; (f): x ≠ 0; (g): x > 5/2. All three logarithmic ranges are ℝ.',
    '(a) Circle radius 2; (b) circle radius 4; (c) ellipse semi-axes 5, 3; (d) ellipse semi-axes 6, √6. All centers are (0, 0).',
    'Use the seven checked expressions and domain restrictions below. The numerical window and a = 1 in part (a) are explicit learning choices.'
]
SOLUTION_BLOCKS={3:[]}
definitions=[('a','y = ln x',0,1,0,[1,6,12,18]),('b','y = −ln x',0,-1,0,[1,6,12,18]),('c','y = 2ln(x + 2)',-2,2,0,[1,6,12,18]),('d','y = 4ln(x − 3)',3,4,0,[4,6,12,18]),('e','y = 4ln x − 2',0,4,-2,[1,6,12,18])]
for label,title,shift,scale,offset,xs in definitions:
    SOLUTION_BLOCKS[3]+=[table(title,xs,lambda x,h=shift,a=scale,k=offset:a*log(x-h)+k),log_graph(4,label,title,shift,scale,offset)]
SOLUTION_BLOCKS[4]=[
    graph(5,'a','y = 6 − 2x; increasing t moves left and up',xMin=-3,xMax=6,yMin=-6,yMax=12,xTicks=[-2,0,2,3,4,6],yTicks=[-4,2,4,6,8,10],polynomial=[6,-2],points=[[3,0,'t = 0'],[2,2,'t = 1'],[1,4,'t = 2']]),
    graph(5,'b','x = 4 cos t, y = −3 sin t; clockwise',xMin=-5,xMax=5,yMin=-3.75,yMax=3.75,xTicks=[-4,-2,0,2,4],yTicks=[-3,-2,2,3],ellipse={'a':4,'b':3},closedPoints=[[4,0],[0,-3],[-4,0],[0,3]])
]
SOLUTION_BLOCKS[5]=[]
for label,title,initial,rate,xmin,xmax,ymax in [('a','y = e⁻²ˣ',1,-2,-3,4,8),('b','y = (2/3)e³ˣ',2/3,3,-3,1,8),('c','y = 4ˣ',1,log(4),-3,2,17),('d','y = 4⁻ˣ',1,-log(4),-2,4,17)]:
    SOLUTION_BLOCKS[5].append(graph(6,label,title,xMin=xmin,xMax=xmax,yMin=0,yMax=ymax,xTicks=list(range(xmin,xmax+1)),yTicks=[1,2,4,6] if ymax==8 else [1,4,8,12,16],exponential={'initial':initial,'rate':rate},points=[[0,initial,'(0, '+('2/3' if initial!=1 else '1')+')']]))
SOLUTION_BLOCKS[5]+=[log_graph(6,'e','y = log₂(x + 5)',shift=-5,base=2,xmin=-6,xmax=5,ymax=5),log_graph(6,'f','y = log₂(x²)',base=2,xmin=-4,xmax=4,ymax=5,power=2),log_graph(6,'g','y = ln(2x − 5)',shift=2.5,xmin=1,xmax=7,ymax=4,inputFactor=2)]
SOLUTION_BLOCKS[6]=[]
for label,title,a,b in [('a','x² + y² = 4',2,2),('b','x² + y² = 16',4,4),('c','x²/25 + y²/9 = 1',5,3),('d','x²/36 + y²/6 = 1',6,sqrt(6))]:
    SOLUTION_BLOCKS[6].append(graph(7,label,title,xMin=-8,xMax=8,yMin=-6,yMax=6,xTicks=[-6,-4,-2,0,2,4,6],yTicks=[-4,-2,2,4],ellipse={'a':a,'b':b},closedPoints=[[a,0],[-a,0],[0,b],[0,-b]]))
COMMANDS=[('a','plot(sin(x)^2+x, x=-2*Pi..2*Pi);'),('b','plot(7*x^4+3*x^2-4*x+5, x=-2..2);'),('c','plot(arctan(x)-7, x=-10..10);'),('d','plot(4+7*ln(x)/ln(2), x=0.01..10);'),('e','plots[implicitplot](x^2+y^2=36, x=-7..7, y=-7..7);'),('f','plot([(exp(3*x)+exp(-3*x))/(exp(3*x)-exp(-3*x)), x=-3..-0.01], [(exp(3*x)+exp(-3*x))/(exp(3*x)-exp(-3*x)), x=0.01..3]);'),('g','plot(sqrt(x-8), x=8..18);')]
# Part (f) uses two explicit commands rather than a malformed combined list.
COMMANDS[5]=('f','plot((exp(3*x)+exp(-3*x))/(exp(3*x)-exp(-3*x)), x=-3..-0.01);\nplot((exp(3*x)+exp(-3*x))/(exp(3*x)-exp(-3*x)), x=0.01..3);')
SOLUTION_BLOCKS[7]=[block for label,text in COMMANDS for block in [{'type':'heading','text':'('+label+')'},{'type':'command','text':text,'result':None,'number':None}]]
CLARIFICATIONS={3:'The answer key on page 328 labels (c) with (18, 6.4), but 2ln(20) ≈ 5.991. Its (d) label (10, 10.8) is also inconsistent: 4ln(7) ≈ 7.784, while x = 18 gives about 10.832. These learning tables calculate directly from the exercise equations.',5:'The answer-key plots labelled (f) and (g) on page 330 correspond to the opposite exercise parts. This solution follows the question order: (f) log₂(x²), with two branches; (g) ln(2x − 5), with one shifted branch.'}
SOLUTION_BLOCKS[4][1]['diagram']['ellipse']['clockwise']=True
SOLUTION_BLOCKS[7]+=[
    graph(8,'a','y = sin²x + x (chosen a = 1)',xMin=-2*pi,xMax=2*pi,yMin=-7,yMax=8,xTicks=[-6,-3,0,3,6],yTicks=[-6,-3,3,6],functionSpec={'kind':'sin-squared-plus-x'}),
    graph(8,'b','y = 7x⁴ + 3x² − 4x + 5',xMin=-2,xMax=2,yMin=0,yMax=140,xTicks=[-2,-1,0,1,2],yTicks=[20,60,100,140],yGridStep=20,polynomial=[5,-4,3,0,7]),
    graph(8,'c','y = arctan x − 7',xMin=-10,xMax=10,yMin=-10,yMax=0,xTicks=[-10,-5,0,5,10],yTicks=[-9,-7,-5],functionSpec={'kind':'arctan-offset'}),
    log_graph(8,'d','y = 4 + 7log₂x',scale=7,offset=4,base=2,xmin=0,xmax=10,ymin=-30,ymax=30),
    graph(8,'e','x² + y² = 36',equalAspect=True,xMin=-7,xMax=7,yMin=-7,yMax=7,xTicks=[-6,-3,0,3,6],yTicks=[-6,-3,3,6],ellipse={'a':6,'b':6}),
    graph(8,'f','y = coth(3x), x ≠ 0',xMin=-3,xMax=3,yMin=-5,yMax=5,xTicks=[-3,-2,-1,0,1,2,3],yTicks=[-4,-2,2,4],functionSpec={'kind':'coth-three-x'}),
    graph(8,'g','y = √(x − 8), x ≥ 8',xMin=7,xMax=18,yMin=0,yMax=4,xTicks=[8,10,12,14,16,18],yTicks=[1,2,3,4],functionSpec={'kind':'sqrt-shift-eight'},closedPoints=[[8,0]])
]
