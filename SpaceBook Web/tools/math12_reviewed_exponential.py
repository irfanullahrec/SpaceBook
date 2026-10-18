"""Unit 2 printed page 33, checked against JPG and full PDF spread 21."""
from math12_reviewed_unit1 import heading,paragraph,page,command
PAGES=[page('021_page_1.jpg',33,[
 heading('iv. Exponential Functions'),
 paragraph('The exponential function has widespread application in many areas of science and engineering. Areas which utilize the exponential function include expansion of materials, laws of cooling, radioactive decay and the discharge of a capacitor.'),
 paragraph(r'An equation of the form \(f(x)=b^x\), b > 0, b ≠ 1, b is a positive constant, defines an exponential function. The domain of f(x) is the set of all real numbers, and the range of f(x) is the set of all positive real numbers.'),
 {'type':'clarification','text':'The definition is faint in both supplied copies. Its function, positive-base condition, domain and range are legible, but the intervening descriptive wording remains a source-legibility issue; this digital paragraph does not claim a verified word-for-word transcription of the faint sentence.'},
 paragraph(r'We require the base to be positive and to avoid imaginary numbers such as \((-2)^{1/2}=\sqrt{-2}=i\sqrt2\).'),
 paragraph(r'We conclude b = 1 as a base, since \(f(x)=1^x=1\) is a constant function.'),
 {'type':'clarification','text':'The printed “We conclude b = 1” conflicts with the preceding b ≠ 1 condition. The intended restriction for a nonconstant exponential function excludes b = 1; base 1 gives the constant function 1.'},
 heading('Remember — Exponent laws'),paragraph('If a and b are positive real numbers, a ≠ 1 and b ≠ 1, then,'),
 command(None,r'\(a^xa^y=a^{x+y},\quad\frac{a^x}{b^x}=a^{x-y},\quad(a^x)^y=a^{xy},\quad(ab)^x=a^xb^x,\quad(\frac ab)^x=\frac{a^x}{b^x}\)'),
 command(None,r'\(a^x=a^y\text{ if and only if }x=y\)'),command(None,r'\(\text{For }x\ne0,\quad a^x=b^x\text{ if and only if }a=b\)'),
 {'type':'clarification','text':r'The printed quotient law uses b in its denominator but a single-base exponent subtraction on the right. The single-base law is \(\frac{a^x}{a^y}=a^{x-y}\). For different positive bases, \(\frac{a^x}{b^x}=(\frac ab)^x\). The other laws above apply under their stated positive-base conditions.'},
 heading('Base e Exponential Functions'),
 paragraph('Of all possible bases b, it can use for the exponential function y = bˣ, which ones are the most useful? If you look at the keys on a scientific calculator, you will likely see 10ˣ and eˣ. It is clear why base 10 would be important, because our number system is a base 10 system. But what is e, and why is it included as a base? It turns out that base e is used more frequently than all other bases combined. The reason for this is that certain formulas and the results of certain processes found in calculus and more advanced mathematics take on their simplest form if this base is used. This is why you will see e used extensively in expressions and formulas that model real-world phenomena. In fact, its use is so prevalent that you will often hear people refer to y = eˣ as the exponential function. The base e is an irrational number (like π) it cannot be represented exactly by any finite decimal fraction. However, it can be approximated as closely as we like by evaluating the expression'),
 command(None,r'\((1+\frac1x)^x\)','i'),
 paragraph('for sufficiently large x. What happens to the value of expression (i) as x increases without bound? The results are summarized in the following table:'),
 {'type':'dataTable','headers':['X','(1 + 1/x)ˣ'],'rows':[['1','2'],['10','2.59374...'],['100','2.70481...'],['1000','2.71692...'],['10000','2.71814...'],['100000','2.71827...'],['1000000','2.71828...']]},
 heading('Challenge'),paragraph('Use binomial theorem to find the value of e.')
])]
PAGES[0]['textStatus']='partial_source_legibility'
PAGES[0]['sourceDefects']=['The italic exponential definition remains faint; its full descriptive wording is not certified.']
PAGES[0]['visualStatus']='Exponent laws, seven-row e approximation table and challenge rendered digitally; faint definition explicitly flagged'
PAGES[0]['alternateVerification']={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':21,'side':'left','reason':'Checks exponent laws and all approximation table values; faint definition remains flagged in both copies.'}
