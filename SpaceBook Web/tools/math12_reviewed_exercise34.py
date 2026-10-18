"""Five independent Exercise 3.4 items, printed 90; key 333–334."""
QUESTIONS=[
 r'Use first-principles rules to differentiate: (a) \(y=\sin(2x)^1\); (b) \(y=\cot(3x)\); (c) \(y=\cos(3x)+\tan(3x)\); (d) \(y=\cot^2x\); (e) \(y=\tan\sqrt{x}\); (f) \(y=\sin^3x\).',
 r'Differentiate by any suitable rule: (a) \(x^2\cot(3x)\); (b) \(y=(\sin2x+\cot3x)^2\); (c) \(y=4\,\text{cosec }2x\); (d) \(y=2\tan(x+3)^2\); (e) \(y=\frac{\sqrt{\tan x}}{\cos\sqrt{x}}\); (f) \(y=\frac{1+\tan2x}{\text{cosec }3x}\).',
 r'Differentiate: (a) \(y=\cos^{-1}(\frac{x}{a})\); (b) \(y=\tan^{-1}(\frac{x}{p})\); (c) \(y=\cot^{-1}(\frac{a}{x})\); (d) \(y=\text{cosec}^{-1}\sqrt{1+x^2}\); (e) \(y=\text{cosec}^{-1}(t+3)\); (f) \(y=\frac1x\tan^{-1}(\frac{x+1}{x-1})\).',
 r'Profits on swimming-suit sales are \(P(t)=5-5\cos\frac{\pi t}{26}\), 0 ≤ t ≤ 104, measured in hundreds of dollars for sales t weeks after January first. (a) Find the rate of change at t weeks. (b) Evaluate at 8, 26 and 50 weeks.',
 r'A seated adult breathes in and exhales about 0.8 liter every 4 seconds. Lung volume is \(V(t)=0.45-0.35\cos\frac{\pi t}{2}\), 0 ≤ t ≤ 8. (a) Find the rate of flow at t seconds after exhaling. (b) Evaluate at 3, 4 and 5 seconds.'
]
STEPS=[
 [r'First principles use lim[h→0](f(x+h) − f(x))/h with h ≠ 0. Angles are radians. We use lim[k→0]sin k/k = 1 and continuity of sine and cosine.',
  r'(a) sin(2x+2h) − sin(2x) = 2cos(2x+h)sin h. Divide by h and take limits: 2cos(2x)·1. The printed superscript 1 does not change the function.',
  r'(b) cot(3x+3h) − cot(3x) = −sin(3h)/[sin(3x+3h)sin(3x)]. Divide by h, using sin(3h)/h → 3. The result is −3 cosec²(3x), where sin(3x) ≠ 0.',
  r'(c) Split the difference quotient into cosine and tangent terms. The cosine difference is −2sin(3x+3h/2)sin(3h/2), giving −3sin(3x). The tangent difference is sin(3h)/[cos(3x+3h)cos(3x)], giving 3sec²(3x). Add: 3[sec²(3x) − sin(3x)], with cos(3x) ≠ 0.',
  r'(d) Factor cot²(x+h) − cot²x = [cot(x+h) − cot x][cot(x+h) + cot x]. The first factor divided by h tends to −cosec²x; the second tends to 2cot x. Thus y′ = −2cot x cosec²x, with sin x ≠ 0.',
  r'(e) Set k = √(x+h) − √x. For x > 0, k/h = 1/[√(x+h) + √x] → 1/(2√x). The tangent difference divided by k tends to sec²√x. Multiply the two limits: y′ = sec²√x/(2√x), provided cos√x ≠ 0. At x = 0 the right slope is unbounded.',
  r'(f) Factor sin³(x+h) − sin³x = [sin(x+h) − sin x][sin²(x+h) + sin(x+h)sin x + sin²x]. The divided first factor tends to cos x and the second to 3sin²x. Thus y′ = 3sin²x cos x for every real x.'
 ],
 [r'(a) Product rule: d[x²cot(3x)]/dx = 2xcot(3x) − 3x²cosec²(3x). Require sin(3x) ≠ 0.',
  r'(b) With u = sin2x + cot3x, u′ = 2cos2x − 3cosec²3x. Then (u²)′ = 2u u′ = 2(sin2x + cot3x)(2cos2x − 3cosec²3x), with sin3x ≠ 0.',
  r'(c) The cosecant chain rule gives y′ = 4[−cosec2x cot2x]·2 = −8cosec2x cot2x, with sin2x ≠ 0.',
  r'(d) The key confirms that the printed square belongs to the argument: y = 2tan((x + 3)²). Set u = (x + 3)², u′ = 2(x + 3). Therefore y′ = 4(x + 3)sec²((x + 3)²), with cos((x + 3)²) ≠ 0. If it had meant 2[tan(x + 3)]², the derivative would instead be 4tan(x + 3)sec²(x + 3).',
  r'(e) Let N = √tan x and D = cos√x. For x > 0 and tan x > 0, N′ = sec²x/(2√tan x) and D′ = −sin√x/(2√x). Apply [DN′ − ND′]/D².',
  r'The result is \(\frac{\sqrt{x}\cos\sqrt{x}\sec^2x+\tan x\sin\sqrt{x}}{2\sqrt{x}\sqrt{\tan x}\cos^2\sqrt{x}}\). Require x > 0, tan x > 0, cos x ≠ 0 and cos√x ≠ 0 for this finite derivative. At allowable points where tan x = 0, including x = 0, the one-sided slope of √tan x is unbounded.',
  r'(f) On the original domain, 1/cosec3x = sin3x, so y = (1 + tan2x)sin3x. Product rule gives y′ = 2sec²2x sin3x + 3(1 + tan2x)cos3x. Equivalently [2sec²2x + 3cot3x(1 + tan2x)]/cosec3x. Preserve cos2x ≠ 0 and sin3x ≠ 0, even though the simplified product extends to some excluded points.'
 ],
 [r'Use principal inverse functions. A general inverse secant/cosecant derivative uses an absolute value in its denominator; treat constants as fixed and state the original domain.',
  r'(a) u = x/a, u′ = 1/a. Hence y′ = −1/[a√(1 − (x/a)²)] for a ≠ 0 and |x/a| < 1. The key’s −1/√(a² − x²) assumes a > 0. For a < 0 the derivative has the opposite sign.',
  r'(b) u = x/p gives y′ = (1/p)/(1 + x²/p²) = p/(p² + x²), for p ≠ 0 and all real x.',
  r'(c) u = a/x, u′ = −a/x². The decreasing arccot branch has derivative −1/(1 + u²), so y′ = a/(x² + a²), with x ≠ 0. If a = 0, the function is constant π/2 on its original domain and its derivative is 0.',
  r'(d) u = √(1 + x²) ≥ 1 and u′ = x/√(1 + x²). For x ≠ 0, y′ = −u′/[u√(u² − 1)] = −x/[(1 + x²)|x|]. Thus the key’s −1/(1 + x²) is valid on x > 0; for x < 0 the slope is +1/(1 + x²). At x = 0 the function exists but has a cusp and no two-sided derivative.',
  r'(e) The source variable is t, so compute dy/dt. With u = t + 3, y′ = −1/[|t + 3|√((t + 3)² − 1)], for |t + 3| > 1, meaning t < −4 or t > −2. At t = −4 and −2 the function exists but no finite derivative does. The key’s formula without absolute value requires t + 3 > 1.',
  r'(f) Let v = arctan((x + 1)/(x − 1)) and y = v/x. The inner derivative is −2/(x − 1)² and 1 + [(x + 1)/(x − 1)]² = 2(x² + 1)/(x − 1)². Hence v′ = −1/(x² + 1).',
  r'Product rule with (1/x)′ = −1/x² gives \(y′=-\frac1{x(x^2+1)}-\frac1{x^2}\tan^{-1}(\frac{x+1}{x-1})\), with x ≠ 0,1. The key prints a plus before the second term; differentiating 1/x requires the minus sign.'
 ],
 [r'P is measured in hundreds of dollars, while t is in weeks. Keep that scale when interpreting the derivative.',
  r'Let θ = πt/26. Then θ′ = π/26 and d(cosθ)/dt = −sinθ·π/26.',
  r'Thus P′(t) = (5π/26)sin(πt/26) hundreds of dollars per week, or (250π/13)sin(πt/26) dollars per week.',
  r'At t = 8, P′(8) = (5π/26)sin(4π/13) ≈ 0.49720771 hundreds of dollars/week = $49.720771/week; increasing.',
  r'At t = 26, sinπ = 0, so P′(26) = 0. At this point the weekly-profit model is at a local maximum.',
  r'At t = 50, P′(50) = (5π/26)sin(25π/13) ≈ −0.14458314 hundreds of dollars/week = −$14.458314/week; decreasing.',
  r'The key rounds these dollar rates to 50, 0 and −14. This is the rate of change of the modeled weekly-sales profit, rather than total accumulated profit.'
 ],
 [r'V is in liters and t is in seconds. Its rate V′ is in liters per second; positive means lung volume increases and negative means it decreases.',
  r'Let θ = πt/2. Then θ′ = π/2. Differentiating −0.35cosθ gives 0.35sinθ·π/2.',
  r'Thus V′(t) = (7π/40)sin(πt/2) liters/second, for interior times 0 < t < 8 (with endpoint one-sided rates where applicable).',
  r'At t = 3, sin(3π/2) = −1, so V′(3) = −7π/40 ≈ −0.54977871 L/s; lung volume is decreasing.',
  r'At t = 4, sin2π = 0, so V′(4) = 0 L/s at the minimum-volume turn in this model.',
  r'At t = 5, sin(5π/2) = 1, so V′(5) = 7π/40 ≈ 0.54977871 L/s; volume is increasing.',
  r'The key labels all three evaluations V′(3); the second and third labels should be V′(4) and V′(5). Its approximate values agree after that label correction. The source’s liters determine the units, rather than the key’s generic cubic units.'
 ]
]
ANSWERS=[
 r'(a) 2cos2x; (b) −3cosec²3x; (c) 3(sec²3x − sin3x); (d) −2cot x cosec²x; (e) sec²√x/(2√x); (f) 3sin²x cos x, on the domains explained in the steps.',
 r'(a) 2xcot3x − 3x²cosec²3x; (b) 2(sin2x + cot3x)(2cos2x − 3cosec²3x); (c) −8cosec2x cot2x; (d) 4(x + 3)sec²((x + 3)²); (e) the quotient displayed above; (f) 2sec²2x sin3x + 3(1 + tan2x)cos3x. Original-domain restrictions apply.',
 r'(a) −1/[a√(1 − (x/a)²)]; (b) p/(p² + x²); (c) a/(x² + a²); (d) −x/[|x|(1 + x²)]; (e) −1/[|t + 3|√((t + 3)² − 1)]; (f) −1/[x(x² + 1)] − arctan((x + 1)/(x − 1))/x², with restrictions stated above.',
 r'P′(t) = (5π/26)sin(πt/26) hundreds of dollars/week. At 8,26,50 weeks: approximately $49.72, $0 and −$14.46 per week.',
 r'V′(t) = (7π/40)sin(πt/2) L/s. At 3,4,5 seconds: approximately −0.5498, 0 and +0.5498 L/s.'
]
CLARIFICATIONS={
 1:'Part (d) is printed with the square after (x + 3). The key confirms it means tan of the squared argument. The alternative squared-tangent interpretation is explained separately.',
 2:'The key assumes positive a in (a), positive x in (d), and positive t + 3 in (e). General principal-branch solutions state the signs and absolute values. In (f), the key has an incorrect plus sign for the arctangent term. Part (e) is written in t and is differentiated with respect to t.',
 4:'The key repeats the time label V′(3) for all three rates. The source asks for t = 3,4,5; these are evaluated separately in liters per second.'
}
