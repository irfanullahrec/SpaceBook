"""Printed page 36, checked against JPG and full PDF physical page 22, right."""
from math12_reviewed_unit1 import heading, paragraph, command, figure, page

PAGES=[page('022_page_2.jpg',36,[
    heading('Solution'),paragraph('The number of days T that will take for the flu virus to infect n people is given by'),
    command(None,r'\(T(n)=-1.43\ln\left(\frac{10,000-n}{4998n}\right)\)','i'),
    paragraph('The number of days that will take for the virus to infect 500 people, is obtained by putting n = 500 in equation (i):'),
    paragraph(r'a. \(T(500)=-1.43\ln\left(\frac{10,000-500}{4998(500)}\right)=-1.43\ln\left(\frac{9500}{2499000}\right)=-1.43\ln(0.00380)\)'),
    paragraph('= −1.43(−5.57275) = 7.96903 ≈ 8 days'),
    paragraph(r'b. \(T(5000)=-1.43\ln\left(\frac{10,000-5000}{4998(5000)}\right)=-1.43\ln\left(\frac{5000}{24990000}\right)=-1.43\ln\left(\frac{1}{4998}\right)=12.17\approx12\) days'),
    heading('vi. Hyperbolic functions and their identities'),
    paragraph('In physics, it is shown that a heavy, flexible cable (for example a power line) that is suspended between two points at the same height assumes the shape of a curve called a catenary, with an equation of the form'),
    command(None,r'\(y=\frac{a}{2}\left(e^{\frac{x}{a}}+e^{-\frac{x}{a}}\right)\)','i'),
    figure('figure-2-8','Figure 2.8 Hanging cable','A transmission tower and a suspended power cable, illustrating a catenary'),
    paragraph('This is one of several important applications that involve combinations of exponential functions. In certain ways, the functions we shall study are analogous to the trigonometric functions, and they have essentially the same relationship to the hyperbola that the trigonometric functions have to the circle. For this reason, these functions are called hyperbolic functions. Three basic functions are the hyperbolic sine (denoted “sinhx” and pronounced “cinch”), the hyperbolic cosine (coshx; pronounced “kosh”) and the hyperbolic tangent (tanhx; pronounced “tansh”). They are listed as under:'),
    paragraph(r'\(\sinh x=\frac{e^x-e^{-x}}{2}\), \(\cosh x=\frac{e^x+e^{-x}}{2}\), \(\tanh x=\frac{e^x-e^{-x}}{e^x+e^{-x}}\), \(\coth x=\frac{e^x+e^{-x}}{e^x-e^{-x}}\)'),
    paragraph(r'\(\cosh^2x-\sinh^2x=1\)'),
    paragraph(r'\(\cosh(x+y)=\cosh x\cosh y+\sinh x\sinh y\)'),
    paragraph(r'\(\sinh(x+y)=\sinh x\cosh y+\cosh x\sinh y\)'),
    paragraph(r'The name “hyperbolic functions” comes from the fact that the functions sinh t and cosh t play the same role in the parametric representation of the hyperbolic \(x^2-y^2=1\), as the trigonometric functions sint and cost, do in the parametric representation of the circle \(x^2+y^2=1\).'),
    paragraph(r'Eliminating the parameter t from the parametric equations \(x=\cos t\), \(y=\sin t\) to obtain the equation of the circle: \(x^2+y^2=\cos^2t+\sin^2t=1\)'),
    paragraph(r'Similarly, the equations \(x=\cosh t\), \(y=\sinh t\) are the parametric equations of the hyperbola. Squaring these equations and subtracting the second from the first to obtain the equation of hyperbola: \(x^2-y^2=\cosh^2t-\sinh^2t=1\)'),
    heading('vii. Explicit and Implicit Functions'),
    paragraph(r'So far we have met many functions of the form \(y=f(x)\): \(y=x^2+3\), \(y=\sin x\), \(y=e^{x^3}-2x\) (i)'),
    paragraph('If y is equated to an expression involving only x terms, then we say that y is expressed explicitly in terms of x that is in equation (i).'),
    paragraph('Sometimes we have an equation connecting x and y but it is impossible to write it in the form y = f(x):'),
    paragraph(r'\(y=x^2-y^3+\sin x-\cos y=1\), \(\sin(x+y)+e^x+e^{-y}=x^3+y^3\) (ii)'),
    paragraph('In these cases we say that y is expressed implicitly in terms of x.'),
    {'type':'clarification','text':'The first implicit example prints the chain y = x² − y³ + sin x − cos y = 1. A usual single implicit relation is x² − y³ + sin x − cos y = 1. The original printed chain above is retained.'}
])]
PAGES[0]['visualStatus']='Hyperbolic identities and explicit/implicit equations rendered digitally; complex transmission-tower illustration retained as an isolated crop'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':22,'side':'right','reason':'Full spread confirms nested exponent x³, catenary exponents, hyperbolic identities and Example 11 arithmetic.'}
PAGES[0]['sourceNotes']=['Example 11 calls the virus flu in its solution although its question says covid-19; printed terminology preserved.','The first implicit-function example prints an unusual equality chain; source retained with a separate clarification.']
FIGURE_PDF_CROPS=[(22,'figure-2-8',(1318,411,1487,546))]
