"""Unit 3 printed 94–96, verified against JPG and full PDF 51–52."""
from math12_reviewed_unit1 import heading,paragraph,page,command
def eq(s):return command(None,'\\('+s+'\\)')
def note(s):return {'type':'clarification','text':s}
PAGES=[page('051_page_2.jpg',94,[
 heading('3.7.1 Differentiation of the hyperbolic functions'),heading('i. Derivative of sinh x'),paragraph(r'If \(y=\sinh x=\frac{e^x-e^{-x}}2\), then on differentiation w.r.t. x it becomes:'),
 eq(r'\frac{dy}{dx}=\frac{d}{dx}\left[\frac{e^x-e^{-x}}2\right]=\frac12\left[\frac{d}{dx}(e^x)-\frac{d}{dx}(e^{-x})\right]=\frac12(e^x+e^{-x})=\cosh x'),
 heading('ii. Derivative of cosh x'),paragraph(r'If \(y=\cosh x=\frac{e^x+e^{-x}}2\), then on differentiation w.r.t. x it becomes:'),
 eq(r'\frac{dy}{dx}=\frac{d}{dx}\left[\frac{e^x+e^{-x}}2\right]=\frac12\left[\frac{d}{dx}(e^x)+\frac{d}{dx}(e^{-x})\right]=\frac12(e^x-e^{-x})=\sinh x'),
 heading('iii. Derivative of tanh x'),paragraph(r'If \(y=\tanh x=\frac{\sinh x}{\cosh x}\), then on differentiation w.r.t. x through quotient rule it becomes:'),
 eq(r'\frac{dy}{dx}=\frac{\cosh x\frac{d}{dx}(\sinh x)-\sinh x\frac{d}{dx}(\cosh x)}{\cosh^2x}=\frac{\cosh x\cosh x-\sinh x\sinh x}{\cosh^2x}=\frac{\cosh^2x-\sinh^2x}{\cosh^2x}=\frac1{\cosh^2x}=\text{sech}^2x'),eq(r'\cosh^2x-\sinh^2x=1'),
 heading('iv. Derivative of sech x'),paragraph(r'If \(y=\text{sech }x=\frac1{\cosh x}\), then on differentiation w.r.t. x through quotient rule it becomes:'),
 eq(r'\frac{dy}{dx}=\frac{\cosh x\frac{d}{dx}(1)-(1)\frac{d}{dx}(\cosh x)}{\cosh^2x}=\frac{\cosh x(0)-\sinh x}{\cosh^2x}=\frac{-\sinh x}{\cosh^2x}=-\frac{\sin x}{\cos x}\frac1{\cosh x}=-\tanh x\,\text{sech }x'),
 note('In the intermediate factorization the source drops h from sin and cos; these must be sinh and cosh. The earlier fraction −sinh x/cosh²x and final derivative −tanh x sech x are correct.'),
 heading('v. Derivative of cosech x'),paragraph(r'If \(y=\text{cosech }x=\frac1{\sinh x}\), then on differentiation w.r.t. x through quotient rule it becomes:'),
 eq(r'\frac{dy}{dx}=\frac{\sinh x\frac{d}{dx}(1)-(1)\frac{d}{dx}(\sinh x)}{\sinh^2x}=\frac{\sinh x(0)-\cosh x}{\sinh^2x}=\frac{-\cosh x}{\sinh^2x}=-\frac{\cosh x}{\sinh x}\frac1{\sinh x}=-\text{coth }x\,\text{cosech }x'),
 heading('vi. Derivative of coth x'),paragraph(r'If \(y=\text{coth }x=\frac{\cosh x}{\sinh x}\), then on differentiation w.r.t. x through quotient rule it becomes:'),
 eq(r'\frac{dy}{dx}=\frac{\sinh x\frac{d}{dx}(\cosh x)-\cosh x\frac{d}{dx}(\sinh x)}{\sinh^2x}=\frac{\sinh x\sinh x-\cosh x\cosh x}{\sinh^2x}=-\frac{\cosh^2x-\sinh^2x}{\sinh^2x}=-\frac1{\sinh^2x}=-\text{cosech}^2x'),eq(r'\cosh^2x-\sinh^2x=1'),
 heading('The hyperbolic formulas are listed below:'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(\sinh x)=\cosh x\)',r'ii. \(\frac{d}{dx}(\cosh x)=\sinh x\)',r'iii. \(\frac{d}{dx}(\tanh x)=\text{sech}^2x\)',r'iv. \(\frac{d}{dx}(\text{cosech }x)=-\text{coth }x\,\text{cosech }x\)',r'v. \(\frac{d}{dx}(\text{sech }x)=-\tanh x\,\text{sech }x\)',r'vi. \(\frac{d}{dx}(\text{coth }x)=-\text{cosech}^2x\)']},
 paragraph('The chain rule can be used to derive the generalization of the power rule and the rules for differentiating the hyperbolic functions, as summarized in the box:'),
 note('For real x, cosh x ≥ 1, so sinh, cosh, tanh and sech have no real poles. Cosech and coth require x ≠ 0 because sinh x = 0 only at zero. The generalized formulas continue on page 95. The scan’s right edge is faded, but the definitions, equations and mathematical conclusions are readable.')
]),page('052_page_1.jpg',95,[
 heading('Hyperbolic chain-rule formulas — continued'),
 {'type':'list','items':[r'i. \(\frac{d}{dx}(\sinh u)=\cosh u\frac{du}{dx}\)',r'ii. \(\frac{d}{dx}(\cosh u)=\sinh u\frac{du}{dx}\)',r'iii. \(\frac{d}{dx}(\tanh u)=\text{sech}^2u\frac{du}{dx}\)',r'iv. \(\frac{d}{dx}(\text{cosech }u)=-\text{coth }u\,\text{cosech }u\frac{du}{dx}\)',r'v. \(\frac{d}{dx}(\text{sech }u)=-\tanh u\,\text{sech }u\frac{du}{dx}\)',r'vi. \(\frac{d}{dx}(\text{coth }u)=-\text{cosech}^2u\frac{du}{dx}\)']},
 heading('Example 21'),paragraph(r'Differentiate the following functions: (a) \(y=\cosh(2x^2-1)\); (b) \(y=\text{sech}(\frac{1-x}{1+x})\).'),heading('Solution'),paragraph(r'a. If the given function is \(y=\cosh(2x^2-1)\), then the derivative of y w.r.t. x is:'),
 eq(r'\frac{dy}{dx}=\frac{d}{dx}[\cosh(2x^2-1)]=\sinh(2x^2-1)\frac{d}{dx}(2x^2-1)=\sinh(2x^2-1)\left[2\frac{d}{dx}(x^2)+\frac{d}{dx}(-1)\right]=4x\sinh(2x^2-1)'),
 paragraph(r'b. If the given function is \(y=\text{sech}(\frac{1-x}{1+x})\), then the derivative of y w.r.t. x is:'),
 eq(r'y′=\frac{d}{dx}\text{sech}(\frac{1-x}{1+x})=\frac{d}{du}(\text{sech }u)\frac{du}{dx},\quad u=\frac{1-x}{1+x}'),
 eq(r'=-\tanh u\,\text{sech }u\frac{d}{dx}(\frac{1-x}{1+x})=-\tanh u\,\text{sech }u\left[\frac{(-1)(1+x)-(1-x)(1)}{(1+x)^2}\right]'),
 eq(r'=\frac2{(1+x)^2}\tanh(\frac{1-x}{1+x})\text{sech}(\frac{1-x}{1+x})'),
 heading('3.7.2 Differentiation of inverse hyperbolic functions'),heading('i. Derivative of sinh⁻¹ x'),paragraph('If y = sinh⁻¹ x, then x = sinh y. The differentiation of x = sinh y w.r.t. y is:'),eq(r'\frac{dx}{dy}=\cosh y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac1{\cosh y}=\frac{\pm1}{\sqrt{1+\sinh^2y}}=\frac{\pm1}{\sqrt{1+x^2}},\quad\sinh y=x,\ \cosh^2y-\sinh^2y=1'),
 paragraph('Here, the sign of the radical is the same as that of cosh y which we know is always positive. Hence,'),eq(r'\frac{d}{dx}(\sinh^{-1}x)=\frac1{\sqrt{1+x^2}}'),
 heading('ii. Derivative of cosh⁻¹ x'),paragraph('If y = cosh⁻¹ x, then x = cosh y. The differentiation of x = cosh y w.r.t. y is:'),eq(r'\frac{dx}{dy}=\sinh y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac1{\sinh y}=\frac{\pm1}{\sqrt{\cosh^2y-1}}=\frac{\pm1}{\sqrt{x^2-1}},\quad\cosh y=x,\ \cosh^2y-\sinh^2y=1'),
 paragraph('Here, the sign of the radical is the same as that of cosh y which we know is always positive. Hence,'),eq(r'\frac{d}{dx}(\cosh^{-1}x)=\frac1{\sqrt{x^2-1}}'),
 note('Arsinh is real and differentiable for every real x. Principal arcosh has range y ≥ 0 and domain x ≥ 1; its finite derivative requires x > 1, so y > 0 and sinh y > 0. The source’s radical-sign sentence says cosh y, but its denominator is sinh y. The branch restriction on y supplies the correct positive sign. Example 21(b) excludes x = −1.')
]),page('052_page_2.jpg',96,[
 heading('iii. Derivative of tanh⁻¹ x'),paragraph('If y = tanh⁻¹ x, then x = tanh y. The differentiation of x = tanh y w.r.t. y is:'),eq(r'\frac{dx}{dy}=\text{sech}^2y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac1{\text{sech}^2y}=\frac1{1-\tanh^2y}=\frac1{1-x^2},\quad\text{sech}^2y=1-\tanh^2y,\ |x|<1,\ \tanh y=x'),
 heading('iv. Derivative of sech⁻¹ x'),paragraph('If y = sech⁻¹ x, then x = sech y. The differentiation of x = sech y w.r.t. y is:'),eq(r'\frac{dx}{dy}=-\text{sech }y\tanh y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac{-1}{\text{sech }y\tanh y}=\frac{-1}{\text{sech }y\sqrt{1-\text{sech}^2y}}=\frac{\pm(-1)}{x\sqrt{1-x^2}},\quad1-\text{sech}^2y=\tanh^2y,\ \text{sech }y=x'),
 paragraph('Here, the sign of the radical is the same as that of tanh y but we know that sech⁻¹ x is always positive, so that tanh y is always positive. Hence,'),eq(r'\frac{d}{dx}(\text{sech}^{-1}x)=\frac{-1}{x\sqrt{1-x^2}}'),
 heading('v. Derivative of cosech⁻¹ x'),paragraph('If y = cosech⁻¹ x, then x = cosech y. The differentiation of x = cosech y w.r.t. y is:'),eq(r'\frac{dx}{dy}=-\text{cosech }y\,\text{coth }y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac{-1}{\text{cosech }y\,\text{coth }y}=\frac{-1}{\text{cosech }y\sqrt{\text{cosech}^2y+1}}=\frac{\pm(-1)}{x\sqrt{x^2+1}},\quad\text{coth}^2y=\text{cosech}^2y+1,\ \text{cosech }y=x'),
 paragraph('Here, the sign of the radical is the same as that of coth y which is positive or negative according as x is positive or negative.'),
 eq(r'\frac{d}{dx}(\text{cosech}^{-1}x)=\frac{-1}{x\sqrt{x^2+1}}\text{ if }x>0,\quad\frac{d}{dx}(\text{cosech}^{-1}x)=\frac{-1}{-x\sqrt{x^2+1}}\text{ if }x<0'),paragraph('Thus,'),eq(r'\frac{d}{dx}(\text{cosech}^{-1}x)=\frac{-1}{|x|\sqrt{x^2+1}}\quad\text{for all values of }x'),
 heading('vi. Derivative of coth⁻¹ x'),paragraph('If y = coth⁻¹ x, then x = coth y. The differentiation of x = coth y w.r.t. y is:'),eq(r'\frac{dx}{dy}=-\text{cosech}^2y'),paragraph('Take its reciprocal to obtain the derivative of y w.r.t. x:'),
 eq(r'\frac{dy}{dx}=\frac{-1}{\text{cosech}^2y}=\frac1{\text{coth}^2y-1}=\frac1{x^2-1},\quad\text{cosech}^2y=\text{coth}^2y-1,\ |x|>1,\ \text{coth }y=x'),
 note(r'The coth-inverse proof loses a minus sign after its first fraction. The correct result is \(\frac{-1}{x^2-1}=\frac1{1-x^2}\) for |x| > 1, agreeing with the formula box on page 97. Artanh requires |x| < 1. Principal arsech has y ≥ 0, so its finite derivative requires 0 < x < 1 and then tanh y > 0; x = 1 has an unbounded one-sided slope. Arcosech requires x ≠ 0, so the source phrase “for all values of x” means all values in that domain.')
])]
for p in PAGES:
 p['title']='DIFFERENTIATION';p['visualStatus']='All six hyperbolic and inverse-hyperbolic proofs and native formula lists preserved with separate branch/sign clarifications'
 p['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':(p['page']+9)//2,'side':'left' if p['page']%2 else 'right','reason':'Checks hyperbolic identities, reciprocal derivative signs, principal branches and source sign errors.'}
EXAMPLES=[{'id':'we-3-source-21','num':'21','title':'Example 21','problem':r'Differentiate (a) \(y=\cosh(2x^2-1)\); (b) \(y=\text{sech}(\frac{1-x}{1+x})\).','given':'Hyperbolic cosine of a polynomial and hyperbolic secant of a quotient.','method':'Chain rule with quotient differentiation of the inner function.','steps':[r'(a) Set u = 2x² − 1; then u′ = 4x and d(cosh u)/du = sinh u.',r'Therefore y′ = 4x sinh(2x² − 1), for all real x.',r'Check (a) using cosh u = (eᵘ + e⁻ᵘ)/2: differentiation gives u′(eᵘ − e⁻ᵘ)/2 = u′ sinh u.',r'(b) Set u = (1 − x)/(1 + x), defined when x ≠ −1.',r'Quotient rule gives u′ = [−(1 + x) − (1 − x)]/(1 + x)² = −2/(1 + x)².',r'The outer derivative is −sech u tanh u. Multiply by the negative inner derivative to obtain y′ = 2sech u tanh u/(1 + x)².',r'Thus y′ = 2tanh((1 − x)/(1 + x))sech((1 − x)/(1 + x))/(1 + x)², for x ≠ −1. At x = 1, u = 0 and tanh u = 0, so the slope is zero. The original formula remains undefined at x = −1 even if one constructs a limiting extension.'],'answer':r'(a) \(4x\sinh(2x^2-1)\), all real x. (b) \(\frac2{(1+x)^2}\tanh(\frac{1-x}{1+x})\text{sech}(\frac{1-x}{1+x})\), x ≠ −1.','progressiveSolution':True,'solutionOrigin':'SpaceBook learning enhancement','sourceReferences':[{'page':95,'jpg':'052_page_1.jpg','verification':'complete question and source solution visually compared with JPG and full PDF'}]}]
