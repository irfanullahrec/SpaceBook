"""Printed page 32: manually checked against JPG and full PDF page 20, right."""
from math12_reviewed_unit1 import heading, paragraph, command, page

PAGES = [page('020_page_2.jpg',32,[
    heading('2.4 Transcendental Functions'),
    paragraph('“Functions that are not algebraic are called transcendental functions.”'),
    paragraph('The functions, such as all trigonometric functions, hyperbolic functions, exponential functions and logarithmic functions are called transcendental functions.'),
    heading('Do You Know?'),
    paragraph(r'A polynomial \(P_n(x)\) is a function of the form'),
    command(None,r'\(f(x)=P_n(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_2x^2+a_1x+a_0\)','i'),
    paragraph(r'with n is a nonnegative integer and \(a_n,a_{n-1},\ldots,a_2,a_1,a_0\) are constants. If \(a_n\ne0\), then the integer n is called the degree of the polynomial.'),
    paragraph(r'The constant \(a_n\) is called the leading coefficient and the constant \(a_0\) is called the constant term of the polynomial function. In particular, the polynomial (i) is going to be a'),
    {'type':'dataTable','headers':['Function','Putting','Rule'],'rows':[
        ['constant function','n = 0',r'\(f(x)=a_0\)'],
        ['linear function','n = 1',r'\(f(x)=a_1x+a_0\)'],
        ['quadratic function','n = 2',r'\(f(x)=a_2x^2+a_1x+a_0\)'],
        ['cubic function','n = 3',r'\(f(x)=a_3x^3+a_2x^2+a_1x+a_0\)']
    ]},
    heading('2.4.1 Recognition of algebraic, trigonometric, inverse trigonometric, exponential, logarithmic, hyperbolic (and their identities), explicit and implicit functions, and parametric representation of functions'),
    heading('i. Algebraic functions'),
    paragraph('A function f(x) is called an algebraic function if it can be constructed using algebraic operations (such as adding, subtracting, multiplying, dividing or taking roots) starting with polynomials. Any rational function is an algebraic function e.g.'),
    paragraph(r'\(f(x)=x+5\), \(g(x)=3x^2+4x-7\) and \(h(t)=\frac{8t^3+5t-9}{t^4+1}\)'),
    heading('ii. Trigonometric functions'),
    paragraph('“Trigonometric function are the functions that describe the relationship between the sides and angles of a right triangle”.'),
    paragraph('Any trigonometric function include one or more of the following 6 trigonometric ratios.'),
    {'type':'list','items':['(i). sin(x)','(ii). cos(x)','(iii). tan(x)','(iv). csc(x)','(v). sec(x)','(vi). cot(x)']},
    paragraph('These function has completely discussed in grade (XI) Mathematics.'),
    heading('iii. Inverse trigonometric functions'),
    paragraph('“Inverse trigonometric function are simply defined as the inverse functions of the basic trigonometric function.”'),
    paragraph('These functions are used to get the angle with any of the trigonometric ratios. Inverse trigonometric functions are also known as “Arc functions” particularly these are 6 functions such as:'),
    {'type':'list','items':[
        r'(i). Arc sine(x) = \(\sin^{-1}(x)\) where x ∈ [−1, 1]',
        r'(ii). Arc cosine(x) = \(\cos^{-1}(x)\) where x ∈ [−1, 1]',
        r'(iii). Arc tangent(x) = \(\tan^{-1}(x)\) where x ∈ ℝ',
        r'(iv). Arc cosecant(x) = \(\csc^{-1}(x)\) where x ≥ 1 or x ≤ −1',
        r'(v). Arc secant(x) = \(\sec^{-1}(x)\) where x ≥ 1 or x ≤ −1',
        r'(vi). Arc cotangent(x) = \(\cot^{-1}(x)\) where x ∈ ℝ'
    ]},
    heading('Do You Know?'), paragraph('Inverse trigonometric functions are also termed as, cyclometric functions, arcus functions and anti trigonometric functions.'),
    paragraph('Inverse trigonometric functions are widely used in the field of physics, engineering, geometry and navigations.'),
    {'type':'clarification','text':'An inverse trigonometric function uses a selected one-to-one branch of the corresponding trigonometric function. Here sin⁻¹(x), cos⁻¹(x), and similar notation mean inverse functions, not reciprocals. The source lists input domains but does not specify all branch ranges on this page.'}
])]
PAGES[0]['visualStatus']='Polynomial rules, rational example and inverse-function domains rendered digitally; no instructional illustration'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':20,'side':'right','reason':'Full spread confirms polynomial subscripts, rational-function exponents and inverse-function domains.'}
