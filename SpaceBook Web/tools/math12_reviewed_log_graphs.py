"""Printed page 39, compared visually with JPG and full PDF page 24 left."""
from math12_reviewed_unit1 import heading, paragraph, page

INVERSE={'type':'source-exponential-log-pair','title':'y = 2ˣ and y = log₂x, reflected across y = x','base':2,'specificBase':True,'points':[[3,8,'(3,8)'],[8,3,'(8,3)'],[0,1,'(0,1)'],[1,0,'(1,0)']]}
LOG_BASE={'type':'source-function-graph','xMin':-5,'xMax':12,'yMin':-12,'yMax':7,'xTicks':[-5,0,5,10],'yTicks':[-10,-5,5]}
SHIFT={**LOG_BASE,'title':'y = log₂(x − 2)','logarithm':{'base':2,'shift':2},'points':[[3,0,'(3,0)'],[4,1,'(4,1)']]}
NATURAL={**LOG_BASE,'title':'y = ln x','logarithm':{'base':2.718281828459045,'shift':0},'points':[[1,0,'(1,0)']]}
PAGES=[page('024_page_1.jpg',39,[
    heading(r'iii. Graphically representation of \(\log_a x\) and \(\log_e x\)'),
    heading('Example 15'),paragraph(r'Sketch the graph of \(y=\log_2 x\).'),heading('Solution'),
    paragraph(r'We can graph \(y=\log_2 x\) by plotting \(x=2^y\), since they are equivalent. Any ordered pair of numbers on the graph of the exponential function will be on the graph of the logarithmic function if we interchange the order of the components.'),
    paragraph(r'For example, ordered pair (3, 8) satisfies \(y=2^x\) and (8, 3) satisfies equation \(x=2^y\).'),
    heading('y = 2ˣ'),{'type':'dataTable','headers':['x','−5','−1','0','1','2','3'],'rows':[['y','0.03','0.5','1','2','4','8']]},
    paragraph('and'),heading('x = 2ʸ or y = log₂x'),{'type':'dataTable','headers':['y','0.03','0.5','1','2','3','8'],'rows':[['x','−5','−1','0','1','2','3']]},
    {'type':'clarification','text':'SpaceBook clarification: The second source table retains its printed row labels y and x, and the value 3 above x = 2. To tabulate y = log₂x by reversing the first table, the top values should be labelled x, the bottom values y, and the top value corresponding to y = 2 should be 4. The learning solution uses the correct inverse pairs.'},
    paragraph(r'The graphs of \(y=2^x\) and \(y=\log_2 x\) are shown in the Figure 2.14.'),
    {'type':'diagram','id':'math12-source-figure-2-14','caption':'Figure 2.14','diagram':INVERSE},
    heading('Example 16'),paragraph(r'Sketch the graph of \(y=\log_2(x-2)\).'),heading('Solution'),
    paragraph(r'We can graph \(y=\log_2(x-2)\) by plotting \(x-2=2^y\), since they are equivalent. Any ordered pair of numbers on the graph of the exponential function will be on the graph of the logarithmic function if we interchange the order of the components.'),
    {'type':'clarification','text':'SpaceBook clarification: For this shifted logarithm, use x = 2 + 2ʸ. Reversing the pairs of y = 2ˣ gives the unshifted logarithm; the x-coordinate must then increase by 2.'},
    paragraph('The graph is shown in the Figure 2.15.'),
    {'type':'diagram','id':'math12-source-figure-2-15','caption':'Figure 2.15','diagram':SHIFT},
    heading('Example 17'),paragraph(r'Sketch the graph of \(y=\ln x\).'),heading('Solution'),
    paragraph(r'We can graph \(y=\ln x\) by plotting \(x=e^y\), since they are equivalent.'),
    paragraph('Any ordered pair of numbers on the graph of the exponential function will be on the graph of the logarithmic function if we interchange the order of the components.'),
    paragraph('The graph is shown in the Figure 2.16.'),
    {'type':'diagram','id':'math12-source-figure-2-16','caption':'Figure 2.16','diagram':NATURAL},
    heading('Do You Know?'),paragraph('If we fold the paper along the dashed line y = x, the two graphs match exactly. The line y = x is a line of symmetry for the two graphs.')
])]
PAGES[0]['visualStatus']='Two source tables rendered digitally, with printed errors separately clarified; Figures 2.14–2.16 reconstructed as SVG from their given functions'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':24,'side':'left','reason':'Restores the clipped symmetry note and confirms table labels, values and logarithm equations.'}
