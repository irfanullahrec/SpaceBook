/* Class 12 Mathematics (calculus): hand-written, numerically checked worked solutions for items whose stored solution is a single line.
 * Each derivative / integral / identity is re-checked here (finite differences, Simpson's rule) at sample points when the file loads;
 * a pack whose numbers do not agree is not registered. The answers are the ones already printed in js/math_12_data.js. */
(function (root) {
  'use strict';
  const NS = root.SBVR; if (!NS || !NS.sol) return;
  const warn = m => { if (root.console) console.warn('sol_m12_calc: ' + m); };
  const tx = (text, m) => ({ text, m });
  const near = (a, b, tol) => Math.abs(a - b) <= (tol === undefined ? 1e-6 : tol);
  const D = (g, x) => (g(x + 1e-6) - g(x - 1e-6)) / 2e-6;
  const simpson = (g, a, b, n) => { n = n || 2000; const h = (b - a) / n; let s = g(a) + g(b); for (let i = 1; i < n; i++) s += g(a + i * h) * (i % 2 ? 4 : 2); return s * h / 3; };
  const add = (label, ok, q, steps) => { if (!ok) return warn(label + ' disagrees with its numeric check'); NS.sol.add({ q, steps }); };

  add('asin integral', near(D(x => Math.asin(x / 3), 1), 1 / Math.sqrt(9 - 1)), 'Evaluate ∫dx/√(a²−x²).', [
    'Recall the derivative of the inverse sine: d/dx sin⁻¹(u) = u′/√(1 − u²).',
    tx('Take u = x/a, so u′ = 1/a (a > 0):', '\\frac{d}{dx}\\sin^{-1}\\frac{x}{a}=\\frac{1/a}{\\sqrt{1-x^{2}/a^{2}}}=\\frac{1}{\\sqrt{a^{2}-x^{2}}}'),
    'The derivative is the integrand, so sin⁻¹(x/a) is an antiderivative.',
    tx('Therefore (for a > 0 and |x| < a):', '\\int\\frac{dx}{\\sqrt{a^{2}-x^{2}}}=\\sin^{-1}\\frac{x}{a}+C')]);

  add('ln integral', near(D(x => Math.log(Math.abs(x + Math.sqrt(x * x - 36))), 10), 1 / Math.sqrt(100 - 36)), 'Evaluate ∫dx/√(x²−36).', [
    'Use the standard form ∫dx/√(x² − a²) with a² = 36, so a = 6.',
    tx('Check by differentiating ln|x + √(x² − 36)|; the inner derivative is 1 + x/√(x² − 36):', '\\frac{d}{dx}\\ln\\left|x+\\sqrt{x^{2}-36}\\right|=\\frac{1+\\frac{x}{\\sqrt{x^{2}-36}}}{x+\\sqrt{x^{2}-36}}=\\frac{1}{\\sqrt{x^{2}-36}}'),
    tx('So, for |x| > 6:', '\\int\\frac{dx}{\\sqrt{x^{2}-36}}=\\ln\\left|x+\\sqrt{x^{2}-36}\\right|+C')]);

  add('polynomial integral', near(D(x => x ** 3 / 3 - 4 * x, 2.5), 2.5 * 2.5 - 4), 'Evaluate ∫(x²−4)dx.', [
    'Integrate term by term with the power rule ∫xⁿ dx = xⁿ⁺¹/(n + 1) and ∫k dx = kx.',
    tx('Each term:', '\\int x^{2}\\,dx=\\frac{x^{3}}{3},\\qquad \\int 4\\,dx=4x'),
    tx('Put them together and add one constant:', '\\int(x^{2}-4)\\,dx=\\frac{x^{3}}{3}-4x+C'),
    tx('Check by differentiating the result:', '\\frac{d}{dx}\\left(\\frac{x^{3}}{3}-4x\\right)=x^{2}-4')]);

  add('rational integral', near(D(x => Math.log(Math.abs(x - 8)), 3), 1 / (3 - 8)) && near((3 + 8) / (9 - 64), 1 / (3 - 8)), 'Evaluate ∫(x+8)/(x²−64) dx.', [
    tx('Factor the denominator (difference of squares):', 'x^{2}-64=(x-8)(x+8)'),
    tx('Cancel the common factor x + 8 (for x ≠ −8):', '\\frac{x+8}{x^{2}-64}=\\frac{x+8}{(x-8)(x+8)}=\\frac{1}{x-8}'),
    tx('Integrate the simpler fraction:', '\\int\\frac{x+8}{x^{2}-64}\\,dx=\\int\\frac{dx}{x-8}=\\ln|x-8|+C')]);

  add('exp definite integral', near(simpson(x => Math.exp(2 * x), 0, 1), (Math.exp(2) - 1) / 2, 1e-7), 'Evaluate ∫₀¹e^{2x}dx.', [
    tx('An antiderivative of e²ˣ is e²ˣ/2 (the chain rule gives back e²ˣ):', '\\int e^{2x}\\,dx=\\frac{e^{2x}}{2}'),
    tx('Apply the fundamental theorem, antiderivative at 1 minus at 0:', '\\int_{0}^{1}e^{2x}\\,dx=\\left[\\frac{e^{2x}}{2}\\right]_{0}^{1}=\\frac{e^{2}}{2}-\\frac{e^{0}}{2}=\\frac{e^{2}-1}{2}')]);

  add('coth', near(1 / Math.tanh(0.7), (Math.exp(0.7) + Math.exp(-0.7)) / (Math.exp(0.7) - Math.exp(-0.7))), 'Write coth x in exponential form.', [
    tx('By definition coth x = cosh x / sinh x, with:', '\\cosh x=\\frac{e^{x}+e^{-x}}{2},\\qquad \\sinh x=\\frac{e^{x}-e^{-x}}{2}'),
    tx('Divide; the common factor 1/2 cancels (x ≠ 0):', '\\coth x=\\frac{\\cosh x}{\\sinh x}=\\frac{(e^{x}+e^{-x})/2}{(e^{x}-e^{-x})/2}=\\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}')]);

  (function () {
    const C = 1.7, y = x => C * Math.exp(Math.exp(-x)), x0 = 0.4;
    add('separable e^x', near(Math.exp(x0) * D(y, x0) + y(x0), 0, 1e-5), 'Find the general solution of e^x(dy/dx)+y=0.', [
      tx('Move y to the right-hand side and divide by eˣ·y (y ≠ 0):', 'e^{x}\\frac{dy}{dx}=-y\\ \\Rightarrow\\ \\frac{1}{y}\\frac{dy}{dx}=-e^{-x}'),
      tx('Integrate both sides with respect to x (∫−e⁻ˣ dx = e⁻ˣ):', '\\int\\frac{dy}{y}=\\int-e^{-x}\\,dx\\ \\Rightarrow\\ \\ln|y|=e^{-x}+C_{1}'),
      tx('Exponentiate; the constant e^{C₁} becomes C:', 'y=Ce^{e^{-x}}')]);
  })();

  (function () {
    const C = 0.3, y = x => Math.sin(Math.asin(x) + C), x0 = 0.35;
    add('separable arcsin', near(Math.sqrt(1 - x0 * x0) * D(y, x0), Math.sqrt(1 - y(x0) ** 2), 1e-5), 'Solve √(1−x²)dy=√(1−y²)dx.', [
      tx('Separate the variables: divide by √(1 − x²)·√(1 − y²):', '\\frac{dy}{\\sqrt{1-y^{2}}}=\\frac{dx}{\\sqrt{1-x^{2}}}'),
      tx('Integrate both sides (each is a standard inverse sine):', '\\int\\frac{dy}{\\sqrt{1-y^{2}}}=\\int\\frac{dx}{\\sqrt{1-x^{2}}}\\ \\Rightarrow\\ \\sin^{-1}y=\\sin^{-1}x+C')]);
  })();

  (function () {
    const a = 2, b = 3, v = 1.2, u = a * Math.sqrt(1 - v * v / (b * b));
    const U = vv => a * Math.sqrt(1 - vv * vv / (b * b));
    add('ellipse implicit', near(D(U, v), -a * a * v / (b * b * u), 1e-5), 'Let \\(\\frac{u^2}{a^2}+\\frac{v^2}{b^2}=1\\), where a and b are nonzero constants.', [
      'a and b are fixed nonzero constants; the curve is an ellipse in the (v, u) coordinates.',
      tx('(a) Treat u as a function of v and differentiate both sides with respect to v:', '\\frac{2u}{a^{2}}\\frac{du}{dv}+\\frac{2v}{b^{2}}=0'),
      tx('Solve for du/dv (where u ≠ 0):', '\\frac{du}{dv}=-\\frac{2v/b^{2}}{2u/a^{2}}=-\\frac{a^{2}v}{b^{2}u}'),
      tx('(b) Now treat v as a function of u; the same steps with the roles swapped give:', '\\frac{2u}{a^{2}}+\\frac{2v}{b^{2}}\\frac{dv}{du}=0\\ \\Rightarrow\\ \\frac{dv}{du}=-\\frac{b^{2}u}{a^{2}v}\\quad(v\\neq0)')]);
  })();

  (function () {
    const f = x => x ** 3 - 3 * x * x - 9 * x + 1, fp = x => 3 * x * x - 6 * x - 9;
    const ok = [-3, -0.5, 0, 2, 4].every(x => near(fp(x), 3 * (x + 1) * (x - 3), 1e-9) && near(D(f, x), fp(x), 1e-4)) && fp(-2) > 0 && fp(0) < 0 && fp(5) > 0;
    add('cubic sign chart', ok, 'Draw f(x) = x³ − 3x² − 9x + 1 and f′(x) = 3x² − 6x − 9.', [
      tx('Differentiate term by term (power rule):', 'f\'(x)=3x^{2}-6x-9'),
      tx('Factor to find where f′ is zero:', '3x^{2}-6x-9=3(x^{2}-2x-3)=3(x+1)(x-3)'),
      'The zeros are x = −1 and x = 3; they split the number line into three intervals.',
      'For x < −1 or x > 3 both factors have the same sign, so f′(x) > 0: the graph of f′ lies above the x-axis and f is increasing.',
      'For −1 < x < 3 the factors have opposite signs, so f′(x) < 0: the graph of f′ lies below the x-axis and f is decreasing.',
      tx('Turning points of f (where f′ changes sign):', 'f(-1)=-1-3+9+1=6\\ (\\text{maximum}),\\qquad f(3)=27-27-27+1=-26\\ (\\text{minimum})')]);
  })();

  /* ---------- integration by parts (Ex 6.2 Q3) ---------- */
  (function () {
    const chk = [[x => Math.exp(2 * x) * (x * x / 2 - x / 2 + 1 / 4), x => x * x * Math.exp(2 * x)], [x => x * Math.sin(x) + Math.cos(x), x => x * Math.cos(x)],
      [x => Math.exp(2 * x) * (2 * Math.sin(x) - Math.cos(x)) / 5, x => Math.exp(2 * x) * Math.sin(x)], [x => Math.exp(x) * (Math.sin(x) + Math.cos(x)) / 2, x => Math.exp(x) * Math.cos(x)],
      [x => x * Math.asin(x) + Math.sqrt(1 - x * x), x => Math.asin(x)], [t => -Math.cos(Math.exp(3 * t)) / 3, t => Math.exp(3 * t) * Math.sin(Math.exp(3 * t))]];
    const ok = chk.every(([F, f], k) => [0.2, 0.5].every(x => near(D(F, x), f(x), 1e-4)));
    add('integration by parts', ok, 'Evaluate using integration by parts: (a)', [
      'Integration by parts: ∫u dv = uv − ∫v du. Choose u so that du is simpler, and dv so that v is easy to find.',
      tx('(a) u = x², dv = e²ˣdx, so du = 2x dx and v = e²ˣ/2:', '\\int x^{2}e^{2x}\\,dx=\\frac{x^{2}e^{2x}}{2}-\\int xe^{2x}\\,dx'),
      tx('Parts again on ∫xe²ˣdx (u = x, v = e²ˣ/2):', '\\int xe^{2x}\\,dx=\\frac{xe^{2x}}{2}-\\frac{e^{2x}}{4}'),
      tx('Put the two results together:', '\\int x^{2}e^{2x}\\,dx=e^{2x}\\left(\\frac{x^{2}}{2}-\\frac{x}{2}+\\frac14\\right)+C'),
      tx('(b) u = x, dv = cos x dx, so du = dx and v = sin x:', '\\int x\\cos x\\,dx=x\\sin x-\\int\\sin x\\,dx=x\\sin x+\\cos x+C'),
      tx('(c) Let I = ∫e²ˣsin x dx and J = ∫e²ˣcos x dx. Parts on each gives two equations:', 'I=-e^{2x}\\cos x+2J,\\qquad J=e^{2x}\\sin x-2I'),
      tx('Substitute J into the first equation and collect I:', 'I=-e^{2x}\\cos x+2e^{2x}\\sin x-4I\\ \\Rightarrow\\ 5I=e^{2x}(2\\sin x-\\cos x)'),
      tx('So:', '\\int e^{2x}\\sin x\\,dx=\\frac{e^{2x}(2\\sin x-\\cos x)}{5}+C'),
      tx('(d) The same two-step trick with exponent 1:', '\\int e^{x}\\cos x\\,dx=\\frac{e^{x}(\\sin x+\\cos x)}{2}+C'),
      tx('(e) u = sin⁻¹x, dv = dx, so du = dx/√(1 − x²) and v = x; then ∫x/√(1 − x²)dx = −√(1 − x²):', '\\int\\sin^{-1}x\\,dx=x\\sin^{-1}x-\\int\\frac{x}{\\sqrt{1-x^{2}}}\\,dx=x\\sin^{-1}x+\\sqrt{1-x^{2}}+C'),
      tx('(f) Substitution is more direct: w = e³ᵗ, dw = 3e³ᵗdt:', '\\int e^{3t}\\sin(e^{3t})\\,dt=\\frac13\\int\\sin w\\,dw=-\\frac{\\cos(e^{3t})}{3}+C'),
      tx('Check (f) by differentiating:', '\\frac{d}{dt}\\left(-\\frac{\\cos(e^{3t})}{3}\\right)=-\\frac13\\left(-\\sin(e^{3t})\\right)3e^{3t}=e^{3t}\\sin(e^{3t})')]);
  })();

  /* ---------- partial derivatives (Ex 11.1, Ex 11 review, worked example 11.2) ---------- */
  (function () {
    const fx = (f, x, y) => (f(x + 1e-6, y) - f(x - 1e-6, y)) / 2e-6, fy = (f, x, y) => (f(x, y + 1e-6) - f(x, y - 1e-6)) / 2e-6;
    const P = [[0.9, 1.3], [1.7, 0.6]];
    const chk = (f, gx, gy) => P.every(([x, y]) => near(fx(f, x, y), gx(x, y), 1e-4) && near(fy(f, x, y), gy(x, y), 1e-4));
    add('we-11-2', chk((x, y) => x ** 3 * y + x * y * y, (x, y) => 3 * x * x * y + y * y, (x, y) => x ** 3 + 2 * x * y), 'Find fₓ and fᵧ for f(x,y)=x³y+xy².', [
      tx('For fₓ keep y constant and differentiate each term with respect to x:', 'f_{x}=\\frac{\\partial}{\\partial x}(x^{3}y)+\\frac{\\partial}{\\partial x}(xy^{2})=3x^{2}y+y^{2}'),
      tx('For fᵧ keep x constant and differentiate each term with respect to y:', 'f_{y}=\\frac{\\partial}{\\partial y}(x^{3}y)+\\frac{\\partial}{\\partial y}(xy^{2})=x^{3}+2xy')]);
    add('us production', chk((x, y) => x ** 0.7 * y ** 0.3, (x, y) => 0.7 * x ** -0.3 * y ** 0.3, (x, y) => 0.3 * x ** 0.7 * y ** -0.7), 'The United States production function was estimated as z=x^0.7 y^0.3', [
      'Work on the positive-input domain x > 0, y > 0.',
      tx('Hold y constant and use the power rule in x (marginal productivity of labour):', 'z_{x}=\\frac{\\partial}{\\partial x}\\left(x^{0.7}y^{0.3}\\right)=0.7x^{-0.3}y^{0.3}'),
      tx('Hold x constant and use the power rule in y (marginal productivity of capital):', 'z_{y}=0.3x^{0.7}y^{-0.7}'),
      tx('Check: the exponents add to 1, so Euler’s relation gives back z:', 'xz_{x}+yz_{y}=(0.7+0.3)x^{0.7}y^{0.3}=z')]);
    add('canada production', chk((x, y) => x ** 0.4 * y ** 0.6, (x, y) => 0.4 * x ** -0.6 * y ** 0.6, (x, y) => 0.6 * x ** 0.4 * y ** -0.4), 'The Canadian production function is z=x^0.4 y^0.6', [
      'Work on the positive-input domain x > 0, y > 0.',
      tx('Treat y⁰·⁶ as a constant factor:', 'z_{x}=0.4x^{-0.6}y^{0.6}'),
      tx('Treat x⁰·⁴ as a constant factor:', 'z_{y}=0.6x^{0.4}y^{-0.4}'),
      tx('Check: the exponents add to 1, so', 'xz_{x}+yz_{y}=(0.4+0.6)x^{0.4}y^{0.6}=z')]);
    add('review q3', chk((x, y) => x * x + y * y, (x, y) => 2 * x, (x, y) => 2 * y), 'If f(x,y)=x²+y², find ∂f/∂x.', [
      'Treat y as a constant, so y² is a constant and its derivative is 0.',
      tx('Differentiate the x² term only:', '\\frac{\\partial f}{\\partial x}=\\frac{\\partial}{\\partial x}(x^{2})+\\frac{\\partial}{\\partial x}(y^{2})=2x+0=2x')]);
    add('review q4', near((1 / (1.3 + 0.6 + 1e-6) - 1 / (1.3 + 0.6 - 1e-6)) / 2e-6, -1 / (1.9 ** 2), 1e-4), 'Find ∂/∂x [1/(x+y)].', [
      tx('Write the fraction as a power:', '\\frac{1}{x+y}=(x+y)^{-1}'),
      tx('Chain rule with y constant (the inner derivative of x + y in x is 1):', '\\frac{\\partial}{\\partial x}(x+y)^{-1}=-(x+y)^{-2}\\cdot1=-\\frac{1}{(x+y)^{2}}')]);
    add('review q8', chk((x, y) => Math.cos(y) * Math.exp(x), (x, y) => Math.cos(y) * Math.exp(x), (x, y) => -Math.exp(x) * Math.sin(y)), 'If f(x,y)=cos y·e^x, find f_y.', [
      'Treat eˣ as a constant factor; only cos y depends on y.',
      tx('Differentiate cos y with respect to y:', 'f_{y}=e^{x}\\frac{\\partial}{\\partial y}(\\cos y)=-e^{x}\\sin y')]);
    add('review q9', chk((x, y) => 3 * x * y * y + x * x * y * y, (x, y) => 3 * y * y + 2 * x * y * y, (x, y) => 6 * x * y + 2 * x * x * y), 'If f(x,y)=3xy²+x²y², find f_x.', [
      'Treat y as a constant and differentiate each term with respect to x.',
      tx('Power rule on x in each term (3y² and y² are constant coefficients):', 'f_{x}=3y^{2}\\cdot1+y^{2}\\cdot2x=3y^{2}+2xy^{2}')]);
  })();
})(typeof window !== 'undefined' ? window : globalThis);
