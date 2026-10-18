"""Printed 338: answer keys do not substitute for missing exercise source."""
from math12_reviewed_unit1 import heading,paragraph,page
from math12_reviewed_higher_derivatives import eq,note
from math12_reviewed_answers333 import groups
EX61=[heading('1. continued'),eq(r'(g)\;\frac{e^{5x}}5+C'),eq(r'(h)\;5\tan^{-1}x'),eq(r'(i)\;\frac29t^{9/2}'),*groups([
 (2,[('a',r'\frac1{27}(3x+4)^9+C'),('b',r'\frac{(x^3-4)^2}{2}+C'),('c',r'\frac{(x^3+7x)^9}{9}+C'),('d',r'-\frac13(x^3-7x)^{-3}+C'),('e',r'2\sqrt{3t^2-7}'),('f',r'2(x^{1/3}+4)^{3/2}'),('g',r'\frac23x^{3/2}+\frac65x^{5/2}+C'),('h',r'\frac{-1}{2(x^2+2x+2)}+C')]),
 (3,[('a',r'e^{6t}+C'),('b',r'\frac1{10}e^{5x^2+1}'),('c',r'\frac13e^{x^3-6x+4}'),('d',r'\frac{8^{7-3x^2}}{\ln8}+C')]),
 (4,[('',r'y=x^4+2x^3-3')]),
 (5,[('',r'y=\frac{(2x^2-1)^3}{12}-406.42')]),
 (6,[('a',r'-e^{-0.01t}'),('b',r'0.095')]),
 (7,[('a',r'w=0.0005h^3')])]),paragraph('7. (b) 171.5 ponds'),heading('8.'),paragraph('19,400'),note('Source-gap note: the corresponding Exercise 6.1 questions are unavailable in the supplied missing pages 142–157. The original key omits +C from several indefinite-form answers and spells the unit “ponds”; these printed entries are preserved without inferring missing questions.')]
EX62=[heading('Exercise 6.2'),*groups([
 (1,[('a',r'\frac{\sin^5x}{5}+C'),('b',r'\frac35(\sin x)^{5/3}+C'),('c',r'-\frac{(\ln(\cos x))^2}{2}+C'),('d',r'-\cos e^x+C'),('e',r'2\ln|\sin\sqrt{x}|+C'),('f',r'-\ln|\sin x+\cos x|+C')]),
 (2,[('a',r'\frac14\tan^{-1}(\frac{x}{4})+C'),('b',r'-\tan^{-1}(\cos x)+C'),('c',r'\frac12\sec^{-1}(\frac{e^x}{2})+C'),('d',r'\ln|x^2+4x+5|+\tan^{-1}(x+2)+C'),('e',r'\sin^{-1}(\frac{x+1}{\sqrt5})-\sqrt{5-(x+1)^2}+C')]),
 (3,[('a',r'\frac{x^2e^{2x}}2-\frac{xe^{2x}}2+\frac{e^{2x}}8+C'),('b',r'-x\sin x+\cos x+C'),('c',r'-\frac15e^{2x}\cos x+\frac25e^{2x}\sin x+C'),('d',r'\frac12e^x\sin x+\frac12e^x\cos x+C'),('e',r'x\sin^{-1}x+\sqrt{1-x^2}+C'),('f',r'-\frac13\cos(e^{3t})+C')])]),note('Source-gap note: the printed Exercise 6.2 questions lie in the unavailable source opening. The key formulas are preserved independently, including their signs and constants; matching them to missing integrands would be an inference, not a recovered transcription.')]
EX63=[heading('Exercise 6.3'),*groups([(1,[('a',r'\frac13\ln|\frac{x-3}{x}|+C'),('b',r'3x-\ln x+C'),('c',r'3\ln x+\ln(x+1)+\frac1x+\frac2{x+1}+C'),('d',r'\frac13\ln(x-1)-\frac16\ln(x^2+x+1)-\frac1{\sqrt3}\tan^{-1}(\sqrt{\frac43}(x+\frac12))+C'),('e',r'[\frac{x^2}{2}+x+2\ln(x-1)-2\ln(x)]'),('f',r'\frac12\ln|\frac{x-1}{x+1}|+C'),('g',r'\ln|\frac{(2x+1)^{5/6}}{(x-1)^{4/3}}|+C'),('h',r'x+\ln|\frac{(x-5)^3}{x+3}|+C')])]),note('SpaceBook clarification: indefinite integrals retain the domains of their source integrands; the learning solutions use logarithms of absolute values on valid real intervals where needed. The source’s Question 1(e) entry has no +C. Further Exercise 6.3 answers continue on page 339.')]
PAGES=[page('173_page_2.jpg',338,[heading('Answers'),*EX61,*EX62,*EX63])]
PAGES[0].update(title='Answers — Exercise 6.1 continuation, 6.2 and 6.3 opening',visualStatus='All source expressions typeset digitally; absent integrand source explicitly distinguished from available answer text',alternateVerification={'pdf':'Math Book for 12 class KPTBB.pdf','pdfPage':173,'side':'right'})
