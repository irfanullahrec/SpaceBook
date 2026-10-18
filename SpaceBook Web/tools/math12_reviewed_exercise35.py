"""Exercise 3.5, printed 98–99; questions and key 334 checked visually."""
QUESTIONS=[
 r'Use the rule of first principle to find the derivative of the following functions: (a) \(f(x)=e^{2x}\); (b) \(f(x)=\frac13e^{3x}\); (c) \(f(x)=\frac58e^{x^2}+1\); (d) \(f(x)=2^x\); (e) \(f(x)=4^{x+4}\); (f) \(f(x)=\log(x+1)\); (g) \(f(x)=\log_a(x^2)\); (h) \(f(x)=\sinh2x\).',
 r'Find f′(x): (a) \(11^{3-4x^3}\); (b) \(e^{\sqrt{x}-5}\); (c) \(x^5e^{1/x}\); (d) \(\frac{e^{2x}}{e^{-2x}+1}\); (e) \(\ln(e^{mx}-e^{-mx})\); (f) \(\frac{e^{ax}-e^{-ax}}{e^{ax}+e^{-ax}}\).',
 r'Find dy/dx using any suitable rule: (a) \(y=x^3\ln\sqrt{x}\); (b) \(y=x^2\sqrt{\ln x}\); (c) \(y=\ln\sqrt{\frac{x^2+1}{x^2-1}}\); (d) \(y=\ln(x-\sqrt{x^2+1})\); (e) \(y=e^{-2x}\cos2x\); (f) \(y=x^2e^{\sin x}\).',
 r'Differentiate: (a) \(y=\log(x+2)^3\); (b) \(y=\cosh3x\); (c) \(y=\sinh^{-1}(\cos x)\); (d) \(y=\tanh^{-1}(\frac{x}{2})\); (e) \(y=\ln(\text{coth }x)\); (f) \(y=x\cosh^{-1}x-\sqrt{x^2-1}\).',
 r'A research group (used hospital records) developed the approximate mathematical model related to systolic blood pressure and age is: \(p(x)=40+25\ln(x+1)\), 0 ≤ x ≤ 65, where p(x) is the pressure measured in millimeters of mercury and x is age in years. What is the rate of change of pressure at the end of 10 years? at the end of 30 years? at the end of 60 years?',
 r'A single cholera bacterium divides every 0.5 hour to produce two complete cholera bacteria. If we start with a colony of 5,000 bacteria, then after t hours there will be \(A(t)=5000\,2^{2t}\) bacteria. Find A′(t), A′(1) and A′(5). Interpret the results.',
 'Use MAPLE command “diff” to differentiate all the functions given in Q.3 and Q.4.'
]
STEPS=[
 [r'Use the difference quotient with increment h ≠ 0 and limit h → 0. For fixed a > 0, lim[k→0](aᵏ − 1)/k = ln a; for a = e the limit is 1.',
  r'(a) [e^(2x+2h) − e^(2x)]/h = 2e^(2x)[(e^(2h) − 1)/(2h)] → 2e^(2x).',
  r'(b) [(e^(3x+3h)/3) − (e^(3x)/3)]/h = e^(3x)[(e^(3h) − 1)/(3h)] → e^(3x).',
  r'(c) The +1 cancels in the difference. Let k = (x+h)² − x² = h(2x+h). The quotient becomes (5/8)e^(x²)[(eᵏ − 1)/k](2x+h), giving (5/4)x e^(x²). Extend the ratio at k = 0 by its limiting value 1; this also covers x = 0. The key incorrectly puts +1 inside the exponent.',
  r'(d) [2^(x+h) − 2ˣ]/h = 2ˣ[(2ʰ − 1)/h] → 2ˣln2. (e) The same argument with 4^(x+4) gives 4^(x+4)ln4, equal to 256·4ˣln4.',
  r'(f) For log base b > 0, b ≠ 1, the quotient is ln[1 + h/(x+1)]/(h ln b). Set k = h/(x+1); lim ln(1+k)/k = 1 gives 1/[(x+1)ln b], with x > −1. If log means natural logarithm, ln b = 1. The source does not specify the base; the key uses the natural-log result.',
  r'(g) The quotient for logₐ(x²) is ln[(x+h)²/x²]/(h ln a). Put k = h/x; for small h and x ≠ 0 this becomes 2ln(1+k)/(x k ln a), tending to 2/(x ln a). Require a > 0, a ≠ 1 and x ≠ 0.',
  r'(h) Use sinh2x = [e^(2x) − e^(−2x)]/2 and its difference quotient. The exponential limits give [2e^(2x) + 2e^(−2x)]/2 = 2cosh2x, for all real x.',
  r'The key’s entries for 1(h) and 4(a) appear exchanged: 1(h) is 2cosh2x; 4(a), under the key’s natural-log interpretation of a cubed argument, is 3/(x+2).'
 ],
 [r'(a) The source exponent is 3 − 4x³. Its inner derivative is −12x², so f′ = −12x²11^(3 − 4x³)ln11. The key instead solves the different exponent 3 − 4x⁵, giving −20x⁴11^(3 − 4x⁵)ln11.',
  r'(b) u = √x − 5 has u′ = 1/(2√x) for x > 0. Thus f′ = e^(√x − 5)/(2√x). At x = 0 the function exists, but the right slope is unbounded.',
  r'(c) Product rule with d(e^(1/x))/dx = −e^(1/x)/x² gives f′ = 5x⁴e^(1/x) − x³e^(1/x) = (5x⁴ − x³)e^(1/x), with x ≠ 0.',
  r'(d) N = e^(2x), N′ = 2e^(2x); D = e^(−2x) + 1, D′ = −2e^(−2x). The quotient numerator simplifies to 2(e^(2x) + 2). Hence f′ = 2(e^(2x) + 2)/(e^(−2x) + 1)², defined for every real x.',
  r'(e) u = e^(mx) − e^(−mx), u′ = m[e^(mx) + e^(−mx)]. The logarithm requires u > 0, equivalent to mx > 0 for real constant m. For m = 0 there is no real domain.',
  r'Thus f′ = m[e^(mx) + e^(−mx)]/[e^(mx) − e^(−mx)], on mx > 0. This equals m coth(mx).',
  r'(f) Let E = e^(ax), F = e^(−ax). Then N = E − F, N′ = a(E + F), D = E + F, D′ = a(E − F).',
  r'Quotient rule gives a[(E+F)² − (E−F)²]/(E+F)² = 4a EF/(E+F)² = 4a/(e^(ax)+e^(−ax))² = a sech²(ax), since EF = 1. This holds for all real a,x, including a = 0.'
 ],
 [r'(a) Require x > 0. Since ln√x = (1/2)ln x, differentiate (1/2)x³ln x: y′ = (3/2)x²ln x + (1/2)x² = (x²/2)(1 + 3ln x).',
  r'(b) x²√ln x is real for x ≥ 1. On x > 1, product and chain rules give y′ = 2x√ln x + x/(2√ln x) = x(4ln x + 1)/(2√ln x). At x = 1 its right slope is unbounded.',
  r'(c) Require (x² + 1)/(x² − 1) > 0, hence |x| > 1. Expand y = (1/2)[ln(x² + 1) − ln(x² − 1)].',
  r'Then y′ = x/(x² + 1) − x/(x² − 1) = −2x/(x⁴ − 1) = 2x/(1 − x⁴), on |x| > 1.',
  r'(d) As printed, √(x² + 1) > |x| for every real x, so x − √(x² + 1) < 0. Therefore the real logarithm and its real derivative do not exist at any real x.',
  r'If the intended function is ln|x − √(x² + 1)|, it equals ln(√(x² + 1) − x) = −arsinh x. Its derivative is −1/√(x² + 1), the key’s answer. This is a clarified alternative, not a silent change to the question.',
  r'(e) Product rule gives y′ = −2e^(−2x)cos2x − 2e^(−2x)sin2x = −2e^(−2x)(cos2x + sin2x), for all real x.',
  r'(f) Product and chain rules give y′ = 2xe^(sin x) + x²e^(sin x)cos x = xe^(sin x)(xcos x + 2), for all real x.'
 ],
 [r'(a) The printed log(x+2)³ is ambiguous. Under the key’s natural-log interpretation of a cubed argument, y = ln((x+2)³), x > −2. Then y = 3ln(x+2) and y′ = 3/(x+2). For another log base b multiply by 1/ln b.',
  r'If the cube instead belongs to the logarithm value, y = [log_b(x+2)]³ has derivative 3[log_b(x+2)]²/[(x+2)ln b]. These are different functions. The key’s 4(a) entry 2cosh2x belongs to 1(h), while 1(h)’s entry 3/(x+2) fits the natural log of the cubed argument.',
  r'(b) Chain rule gives y′ = 3sinh3x, for all real x.',
  r'(c) Let u = cos x, u′ = −sin x. Since d(arsinh u)/du = 1/√(1+u²), y′ = −sin x/√(1+cos²x), for all real x.',
  r'(d) u = x/2; artanh requires |u| < 1, so |x| < 2. Then y′ = (1/2)/(1 − x²/4) = 2/(4 − x²).',
  r'(e) ln(coth x) requires coth x > 0, giving x > 0. Then y′ = −cosech²x/coth x = −1/(sinh x cosh x) = −2cosech2x.',
  r'(f) Principal arcosh x and √(x² − 1) require x ≥ 1. On x > 1, the product rule gives arcosh x + x/√(x² − 1), while the root derivative is x/√(x² − 1).',
  r'The radical terms cancel, giving y′ = arcosh x for x > 1. At x = 1, y = 0 and the right derivative is 0; this is an endpoint one-sided derivative, not a two-sided derivative on an open real domain.'
 ],
 [r'This is an approximate textbook model on ages 0 ≤ x ≤ 65. Its derivative describes model pressure change per year, not a medical diagnosis.',r'Differentiate 40 + 25ln(x+1): the constant gives zero and the logarithm gives 1/(x+1).',r'Thus p′(x) = 25/(x+1) millimeters of mercury per year for interior ages, with one-sided endpoint rates where applicable.',r'At x = 10, p′(10) = 25/11 ≈ 2.2727 mmHg/year.',r'At x = 30, p′(30) = 25/31 ≈ 0.80645 mmHg/year.',r'At x = 60, p′(60) = 25/61 ≈ 0.40984 mmHg/year.',r'All three are positive, so modeled pressure is increasing; the rate decreases with age because its denominator increases. The key’s 2.27,0.81,0.41 are consistent rounded values.'],
 [r'One doubling every 0.5 hour means 2t doublings after t hours, so A(t) = 5000·2^(2t). This agrees with the source model.',r'For an exponential a^u, the derivative is a^u ln a times u′. Here a = 2 and u = 2t, so u′ = 2.',r'Thus A′(t) = 10000ln2·2^(2t) bacteria per hour, for t ≥ 0 under the population model.',r'At t = 1, 2^(2t) = 4. Hence A′(1) = 40000ln2 ≈ 27,725.887 bacteria/hour, about 27,726.',r'At t = 5, 2^(2t) = 1024. Hence A′(5) = 10,240,000ln2 ≈ 7,097,827.129 bacteria/hour, about 7,097,827.',r'These are instantaneous rates of increase, rather than population counts. The populations themselves are A(1) = 20,000 and A(5) = 5,120,000 bacteria.',r'The exact finite one-hour increase is A(t+1) − A(t) = 3A(t), which differs from the instantaneous derivative 2ln2·A(t).'],
 [r'Maple commands differentiate the exact Q.3 and Q.4 expressions. Keep original-domain restrictions and source ambiguities from those worked solutions; a symbolic output does not make an undefined real logarithm valid.',
  r'Q.3(a): diff(x^3*ln(sqrt(x)),x); gives (x²/2)(1 + 3ln x), x > 0.',
  r'Q.3(b): diff(x^2*sqrt(ln(x)),x); gives x(4ln x + 1)/(2√ln x), x > 1.',
  r'Q.3(c): diff(ln(sqrt((x^2+1)/(x^2-1))),x); gives 2x/(1 − x⁴), |x| > 1.',
  r'Q.3(d): diff(ln(x-sqrt(x^2+1)),x); can give the formal result −1/√(x²+1). The printed real logarithm has no real domain. That derivative belongs to the separately stated real alternative ln|x−√(x²+1)|.',
  r'Q.3(e): diff(exp(-2*x)*cos(2*x),x); gives −2e^(−2x)(cos2x + sin2x).',
  r'Q.3(f): diff(x^2*exp(sin(x)),x); gives xe^(sin x)(xcos x + 2).',
  r'Q.4(a), under the stated natural-log and cubed-argument interpretation: diff(ln((x+2)^3),x); gives 3/(x+2), x > −2. For a general base b, use ln((x+2)^3)/ln(b).',
  r'Q.4(b): diff(cosh(3*x),x); gives 3sinh3x.',
  r'Q.4(c): diff(arcsinh(cos(x)),x); gives −sin x/√(1+cos²x).',
  r'Q.4(d): diff(arctanh(x/2),x); gives 2/(4−x²), |x| < 2.',
  r'Q.4(e): diff(ln(coth(x)),x); gives −1/(sinh x cosh x) = −2cosech2x, x > 0.',
  r'Q.4(f): diff(x*arccosh(x)-sqrt(x^2-1),x); gives arcosh x, x > 1.'
 ]
]
ANSWERS=[
 '(a) 2e^(2x); (b) e^(3x); (c) (5/4)x e^(x²); (d) 2ˣln2; (e) 4^(x+4)ln4; (f) 1/[(x+1)ln b] for stated log base b; (g) 2/(x ln a); (h) 2cosh2x, on the domains explained above.',
 '(a) −12x²11^(3−4x³)ln11; (b) e^(√x−5)/(2√x); (c) (5x⁴−x³)e^(1/x); (d) 2(e^(2x)+2)/(e^(−2x)+1)²; (e) m coth(mx) on mx > 0; (f) a sech²(ax).',
 '(a) (x²/2)(1+3ln x); (b) x(4ln x+1)/(2√ln x); (c) 2x/(1−x⁴); (d) no real function as printed; the clarified ln of the absolute value has derivative −1/√(x²+1); (e) −2e^(−2x)(cos2x+sin2x); (f) xe^(sin x)(xcos x+2).',
 '(a) 3/(x+2) under the stated natural-log, cubed-argument interpretation; other interpretations explained above. (b) 3sinh3x; (c) −sin x/√(1+cos²x); (d) 2/(4−x²); (e) −2cosech2x; (f) arcosh x, with the original domains.',
 'p′(x) = 25/(x+1) mmHg/year. At ages 10,30,60: approximately 2.27,0.81,0.41 mmHg/year.',
 'A′(t) = 10000ln2·2^(2t) bacteria/hour. A′(1) ≈ 27,726 and A′(5) ≈ 7,097,827 bacteria/hour.',
 'All twelve corresponding Maple commands and derivatives are given above, with real-domain restrictions and the clarified alternative for Q.3(d).'
]
CLARIFICATIONS={0:'In 1(c), +1 is outside the exponential in the question, but the key places it inside. The key’s 1(h) and 4(a) entries are exchanged. The unbased log in 1(f) is unspecified; the key assumes natural log.',1:'Question 2(a) has x³ in its exponent; the key answers a different exponent containing x⁵. The learning solution follows the question.',2:'Question 3(d) has a negative logarithm argument for every real x and therefore no real domain. The key’s result applies to the explicitly separated ln-of-absolute-value alternative.',3:'Question 4(a) has ambiguous cube placement and no log base. The natural-log, cubed-argument interpretation matches the key’s misplaced 1(h) answer; both interpretations and a general log base are explained.'}
