"""Review Exercise 2, page 61; source JPG and full PDF 35 left."""
from math12_reviewed_unit1 import page,heading,paragraph
NUMS=['i','ii','iii','iv','v','vi','vii','viii','ix','x','xi','xii','xiii','xiv','xv']
QUESTIONS=[
 r'The independent variable in the function \(y=\frac{x^2+4x-3}{(x+3)^3}\) is:',
 r'If \(f(x)=\frac{3x^2-2}{3x+9}\) then f(−3) is:',
 r'The domain of \(f(x)=\frac{3x^2-2}{3x+9}\) is:',
 r'The Domain of \(f(x)=\frac{3x-2}{3x^2+9}\) is:',
 r'If f(x) = 2x + 3 then \(f^{-1}(5)\) is:',
 'If y is expressed in term of x as y = f(x) then y is called:',
 r'If \(f(x)=3x^2+2x-1\) and g(x) = x + 1 then f(g(x)) is:',
 'The value of e is:',
 r'If \(5^x=7\) then the value of x is:',
 r'\(\operatorname{Coth}x=\) ______',
 r'\(\ln(m)-\ln(n)=\) ______',
 r'The function \(f(x)=\frac{2}{x^2-9}\) is discontinuous at point:',
 r'\(\lim_{\theta\to0}\frac{\sin7\theta}{7\theta}=\)',
 r"If \(f(\theta)=\theta\sec\theta\) then \(f'(0)=\)",
 r'The inverse function of \(\frac{e^x-e^{-x}}{e^x+e^{-x}}\) is:'
]
OPTIONS=[
 [r'\(x\)',r'\(x^2\)',r'\(x^3\)',r'\(y\)'],
 [r'\(\frac{25}{18}\)',r'\(\frac{29}{18}\)',r'\(\frac{3}{1}\)','undefined'],
 [r'\((-\infty,-3)\cup(-3,\infty)\)',r'\((-\infty,-3)\cup(-3,\infty)\)',r'\([-\infty,-3]\)',r'\((-\infty,3)\)'],
 [r'\(x\geq-3\)',r'\(x\leq-3\)',r'\(\infty\leq x\leq\infty\)',r'\(-\infty<x<\infty\)'],
 ['13','−13','1','−1'],['implicit function','explicit function','linear function','identity function'],
 [r'\(3x^2+2x+1\)',r'\(3x^2+8x+4\)',r'\(3x^2+8x-1\)',r'\(3x^2-8x-4\)'],
 ['3.142',r'\(\frac{22}{7}\)','2.71','3.8'],
 [r'\(\frac{\ln7}{\ln5}\)',r'\(\frac{\ln5}{\ln7}\)',r'\(\frac{\ln x}{\ln5}\)',r'\(\frac{\ln7}{\ln x}\)'],
 [r'\(\frac{e^x-e^{-x}}{2}\)',r'\(\frac{e^x+e^{-x}}{2}\)',r'\(\frac{e^x+e^{-x}}{e^x-e^{-x}}\)',r'\(\frac{e^x-e^{-x}}{e^x+e^{-x}}\)'],
 [r'\(\ln(mn)\)',r'\(\ln(m+n)\)',r'\(\ln(m-n)\)',r'\(\ln\frac{m}{n}\)'],
 ['−1, 1','−2, 2','−3, 3','4, 4'],['1','2','3','90'],['0','1',r'\(\sqrt2\)','−1'],
 [r'\(\frac12\log\frac{2-x}{2+x}\)',r'\(\frac12\log\frac{2+x}{2-x}\)',r'\(\frac12\log\frac{-1-x}{x-1}\)',r'\(\frac12\log\frac{-1-x}{1-x}\)']
]
LETTERS=['a','d','a','d','c','b','b','c','a','c','d','c','a','b','c']
STEPS=[
 ['The independent variable is the input x. The value y is calculated from x.','Changing the powers or denominator does not change which variable is the input. Choose (a) x.'],
 ['At x = −3, the denominator is 3(−3) + 9 = 0.','The numerator is 3(−3)² − 2 = 25, so the expression would be 25/0, which is undefined. Choose (d).'],
 ['A rational function requires its denominator to be nonzero. Here 3x + 9 = 0 only at x = −3.','Thus the domain is all real numbers except −3: (−∞, −3) ∪ (−3, ∞). Choose (a), as in the printed key; printed (b) repeats the same interval.'],
 ['For every real x, x² ≥ 0, hence 3x² + 9 ≥ 9 > 0.','The denominator never vanishes. The domain is ℝ, expressed by −∞ < x < ∞. Choose (d).'],
 ['Solve y = 2x + 3 for x: x = (y − 3)/2. Thus f⁻¹(t) = (t − 3)/2.','At t = 5, f⁻¹(5) = (5 − 3)/2 = 1. Choose (c).'],
 ['In y = f(x), the dependent variable is isolated as a function of the independent variable.','This is an explicit function. Choose (b).'],
 [r'Substitute g(x) = x + 1 into f: \(f(g(x))=3(x+1)^2+2(x+1)-1\).',r'Expand: \(3x^2+6x+3+2x+2-1=3x^2+8x+4\). Choose (b).'],
 ['Euler’s number is approximately 2.718281828….','Among the printed choices, 2.71 is the intended approximation. It truncates to two decimal places; rounding to two places would give 2.72. Choose (c).'],
 ['Take natural logarithms: x ln 5 = ln 7.',r'Since ln 5 ≠ 0, \(x=\frac{\ln7}{\ln5}\). Choose (a).'],
 [r'By definition, \(\coth x=\frac{\cosh x}{\sinh x}\).',r'Using the exponential definitions, \(\coth x=\frac{e^x+e^{-x}}{e^x-e^{-x}}\), for x ≠ 0. Choose (c).'],
 ['For real logarithms assume m > 0 and n > 0.',r'The quotient law gives \(\ln m-\ln n=\ln(m/n)\). Choose (d).'],
 ['The denominator x² − 9 = (x − 3)(x + 3) vanishes at −3 and 3.','The numerator 2 is nonzero, so these are poles and discontinuities. Choose (c) −3, 3.'],
 ['Set u = 7θ. As θ → 0, u → 0.',r'The standard radian limit \(\lim_{u\to0}\sin u/u=1\) applies. Choose (a).'],
 [r"Using the product rule, \(f'(\theta)=\sec\theta+\theta\sec\theta\tan\theta\).",'At 0, sec 0 = 1 and tan 0 = 0, giving f′(0) = 1 + 0 = 1. Choose (b).'],
 [r'Write \(y=\frac{e^{2t}-1}{e^{2t}+1}\). Rearranging gives \(e^{2t}=\frac{1+y}{1-y}\).',r'Taking natural logs gives \(t=\frac12\ln\frac{1+y}{1-y}\), for −1 < y < 1.',r'The ratio in option (c), \(\frac{-1-x}{x-1}\), equals \(\frac{1+x}{1-x}\). Choose (c), interpreting the printed log as the natural logarithm.']
]
CLARIFICATIONS={13:'The printed answer key selects (a), 0. That is f(0), whereas the printed question asks for f′(0). The product rule gives f′(0) = 1, so the correct derivative choice is (b).',2:'The two printed interval options (a) and (b) appear identical. Both express the correct domain; the printed answer key selects (a). No distinction is invented.',7:'The printed choice 2.71 is an approximation by truncation, not an exact value of e or its two-decimal rounded value.',14:'The inverse uses the natural logarithm and has domain (−1, 1). Option (c) is algebraically equivalent because both numerator and denominator can be multiplied by −1.'}
BLOCKS=[{'type':'list','items':[f'({letter}) {value}' for letter,value in zip('abcd',options)]} for options in OPTIONS]
blocks=[heading('Review Exercise 2'),paragraph('1. Choose the correct option.')]
for i in range(15):
 blocks.extend([heading(NUMS[i]+'.'),paragraph(QUESTIONS[i]),BLOCKS[i]])
 if i in CLARIFICATIONS:blocks.append({'type':'clarification','text':CLARIFICATIONS[i]})
PAGES=[page('035_page_1.jpg',61,blocks)]
PAGES[0]['visualStatus']='All fifteen questions and all sixty printed options rendered as native text and mathematical notation; no source illustration'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':35,'side':'left','reason':'Restores clipped options and verifies denominator powers, derivative prime and inverse-function ratios.'}
PAGES[0]['sourceNotes']=['Question xiv key (a), 0, gives the function value instead of its derivative; the learning solution explains the correct derivative choice (b), 1. Question iii has duplicate printed interval options a/b; intended key a retained with ambiguity noted. Question viii uses truncated 2.71 for e; Question xv inverse requires natural logarithm and domain (−1,1).']
