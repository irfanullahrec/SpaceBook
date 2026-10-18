"""Printed page 44, source questions and Example 24 continuation."""
from math12_reviewed_unit1 import heading, paragraph, command, page

SURFACE={'type':'source-surface-frame','title':'z = cos(tx) sin(ty), printed frame t = 1','parameter':1}
QUESTIONS=[
    r'Recognize and write the type for each of the following functions:'+'\n'+r'(a) \(y=a\sin^2x+x\); (b) \(y=7x^4+3x^2-4x+5\); (c) \(y=\arctan x-7\); (d) \(y=\log_2 16+7\log_2(x)\); (e) \(x^2+y^2=36\); (f) \(y=\frac{e^{3x}+e^{-3x}}{e^{3x}-e^{-3x}}\); (g) \(y=\sqrt{x-8}\).',
    r'A sealed bar contains radium. The number of grams present at time t is given by \(Q(t)=100e^{-0.00043t}\), where t is measured in years. Find the amount of radium in the box at the following times:'+'\n'+'(a) t = 0; (b) t = 800; (c) t = 1600; (d) t = 5000.\nHow did you guess from the above results?',
    r'Using a calculator and point-by-point to plot the following exponential functions:'+'\n'+r'(a) \(h(x)=2^x\); [−5, 0]; (b) \(m(x)=3^{-x}\); [0, 3]; (c) \(N=e^t\); [0, 5]; (d) \(N=e^{-t}\); [0, 5].',
    r'Using a calculator and point-by-point to plot the following logarithmic functions:'+'\n'+r'(a) \(y=\ln x\); (b) \(y=-\ln x\); (c) \(y=2\ln(x+2)\); (d) \(y=4\ln(x-3)\); (e) \(y=4\ln x-2\).',
    r'Sketch the following parametric curves:'+'\n'+r'(a) \((x(t),y(t))=(3-t,2t)\), t is real number. (b) \((x(t),y(t))=(4\cos t,-3\sin t)\).',
    r'Sketch the graph of:'+'\n'+r'(a) \(e^{-2x}\); (b) \(\frac{2}{3}e^{3x}\); (c) \(4^x\); (d) \(4^{-x}\); (e) \(\log_2(x+5)\); (f) \(\log_2 x^2\); (g) \(\log_e(2x-5)\).',
    r'Sketch the graph of:'+'\n'+r'(a) \(x^2+y^2=4\); (b) \(x^2+y^2=16\); (c) \(\frac{x^2}{25}+\frac{y^2}{9}=1\); (d) \(\frac{x^2}{36}+\frac{y^2}{6}=1\).',
    'Use maple commands to plot the graphs of the functions given in Q.1.'
]
LESSON=[
    heading('b. Command'),command("plots[animate]('plot3d', [cos(t*x)*sin(t*y), x = −π..π, y = −π..π], t = 1..2);"),command(None,'t = 1.'),
    {'type':'diagram','id':'math12-source-figure-2-29','caption':'Figure 2.29','diagram':SURFACE},
    heading('Context Menu'),command('plots[animate](\'plot3d\', [cos(t*x)*sin(t*y), x = −π..π, y = −π..π, labels = [x, y, ""]], t = 1..2)'),command(None,'t = 1.'),
    {'type':'diagram','id':'math12-source-figure-2-30','caption':'Figure 2.30','diagram':SURFACE},
    paragraph('This graph is obtained through right-click on the last end of the expression by selecting "Plots < Plot Builder < Animation (choose 3D-Implicit Plot + Parameter)" on the context menu.'),
    {'type':'clarification','text':'The source question uses the notation (x(t), y(t)) for the product cos(tx) sin(ty), while the commands plot a three-dimensional surface z = cos(tx) sin(ty). Its stated t range is −1 to 2, but both displayed commands animate t from 1 to 2. These reconstructed figures show the printed frame t = 1; they are not a complete animation.'}
]
PAGES=[page('026_page_2.jpg',44,LESSON+[heading('Exercise 2.2')]+[paragraph(str(i+1)+'. '+q) for i,q in enumerate(QUESTIONS)])]
PAGES[0]['visualStatus']='All eight multi-part exercise questions and Maple commands rendered digitally; Figures 2.29–2.30 reconstructed as SVG surface meshes for their printed t = 1 frame'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':26,'side':'right','reason':'Confirms the clipped menu instruction, surface commands, radium exponent and every exercise subpart.'}
PAGES[0]['sourceNotes']=['Example 24 is verified across pages 43–44. Exercise 2.2 Questions 1–8 have worked learning solutions and digital graphs. Answer-key mismatches are identified separately.']
STEPS=[
    ['(a) The term a sin²x is trigonometric, so a sin²x + x is an explicit transcendental function when a ≠ 0. If a = 0, it reduces to the polynomial y = x.', '(b) 7x⁴ + 3x² − 4x + 5 is an algebraic polynomial of degree 4. (c) arctan x − 7 is an explicit inverse trigonometric function.', '(d) log₂16 + 7log₂x = 4 + 7log₂x is an explicit logarithmic function with x > 0.', '(e) x² + y² = 36 is an implicit algebraic equation defining a circle; it does not define one value of y for every interior x.', '(f) Dividing numerator and denominator by 2 identifies coth(3x), an explicit hyperbolic function with x ≠ 0. (g) √(x − 8) is an explicit algebraic irrational function with x ≥ 8.'],
    ['Use the given model Q(t) = 100 exp(−0.00043t); the answer is measured in grams.', 'At t = 0, Q(0) = 100 exp(0) = 100 g.', 'At t = 800, the exponent is −0.344. Q(800) ≈ 70.89 g.', 'At t = 1600, the exponent is −0.688. Q(1600) ≈ 50.26 g.', 'At t = 5000, the exponent is −2.15. Q(5000) ≈ 11.65 g.', 'The amount decreases exponentially and remains positive. After about 1600 years it is approximately half the initial amount; the exact model half-life is ln(2)/0.00043 ≈ 1612 years.']
]
ANSWERS=['(a) Trigonometric/polynomial combination (a ≠ 0); (b) polynomial; (c) inverse trigonometric; (d) logarithmic; (e) implicit circle equation; (f) hyperbolic coth(3x); (g) algebraic irrational.', '(a) 100 g; (b) 70.89 g; (c) 50.26 g; (d) 11.65 g. Exponential decay, approximately halving in 1600 years.']

from math import log, exp
STEPS.append(['(a) Evaluate 2ˣ at x = −5, −4, −3, −2, −1, 0: 1/32, 1/16, 1/8, 1/4, 1/2, 1. Plot a smooth increasing curve on [−5, 0].', '(b) Evaluate 3⁻ˣ at x = 0, 1, 2, 3: 1, 1/3, 1/9, 1/27. Plot a smooth decreasing curve on [0, 3].', '(c) At t = 0, 1, 2, 3, 4, 5, eᵗ is approximately 1, 2.7183, 7.3891, 20.0855, 54.5982, 148.4132. Plot an increasing curve on [0, 5].', '(d) At the same t-values, e⁻ᵗ is approximately 1, 0.3679, 0.1353, 0.0498, 0.0183, 0.0067. Plot a decreasing curve on [0, 5].', 'Include both endpoints in each interval. The restricted ranges are (a) [1/32, 1], (b) [1/27, 1], (c) [1, e⁵], (d) [e⁻⁵, 1].'])
ANSWERS.append('(a) Increasing, range [1/32, 1]. (b) Decreasing, range [1/27, 1]. (c) Increasing, range [1, e⁵]. (d) Decreasing, range [e⁻⁵, 1].')
def learning_graph(label,title,xmax,ymax,rate,xmin=0):
    return {'type':'diagram','id':'math12-ex22-q3-'+label,'caption':'SpaceBook learning graph ('+label+')','diagram':{'type':'source-function-graph','title':title,'xMin':xmin,'xMax':xmax,'yMin':0,'yMax':ymax,'xTicks':list(range(xmin,xmax+1)),'yTicks':[.25,.5,.75,1] if ymax<2 else [40,80,120,160],'yGridStep':.25 if ymax<2 else 20,'exponential':{'initial':1,'rate':rate},'closedPoints':[[xmin,exp(rate*xmin)],[xmax,exp(rate*xmax)]]}}
SOLUTION_BLOCKS={2:[
    {'type':'dataTable','headers':['x','−5','−4','−3','−2','−1','0'],'rows':[['2ˣ','1/32','1/16','1/8','1/4','1/2','1']]},learning_graph('a','h(x) = 2ˣ on [−5, 0]',0,1.05,log(2),-5),
    {'type':'dataTable','headers':['x','0','1','2','3'],'rows':[['3⁻ˣ','1','1/3','1/9','1/27']]},learning_graph('b','m(x) = 3⁻ˣ on [0, 3]',3,1.05,-log(3)),
    {'type':'dataTable','headers':['t','0','1','2','3','4','5'],'rows':[['eᵗ','1','2.7183','7.3891','20.0855','54.5982','148.4132']]},learning_graph('c','N = eᵗ on [0, 5]',5,160,1),
    {'type':'dataTable','headers':['t','0','1','2','3','4','5'],'rows':[['e⁻ᵗ','1','0.3679','0.1353','0.0498','0.0183','0.0067']]},learning_graph('d','N = e⁻ᵗ on [0, 5]',5,1.05,-1)
]}

from math12_reviewed_exercise22_remaining import STEPS as REMAINING_STEPS, ANSWERS as REMAINING_ANSWERS, SOLUTION_BLOCKS as REMAINING_BLOCKS, CLARIFICATIONS
STEPS.extend(REMAINING_STEPS)
ANSWERS.extend(REMAINING_ANSWERS)
SOLUTION_BLOCKS.update(REMAINING_BLOCKS)
