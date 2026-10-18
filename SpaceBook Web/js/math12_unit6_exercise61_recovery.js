/* Mathematical companion to recovered Exercise 6.1, printed page 150.
 * Prompts and solutions are authored by SpaceBook; mathematical inputs follow the inspected scan.
 * This does not reproduce the recovered page's prose or replace the supplied original source files. */
(function () {
  'use strict';
  if (typeof MATH_12_DATA === 'undefined') throw new Error('Load Mathematics 12 before Exercise 6.1 recovery.');
  const chapter = MATH_12_DATA.find(ch => ch.id === 'unit-6');
  const exercise = chapter.exercises.find(ex => ex.id === 'ex-6-5');
  if (!exercise) throw new Error('The stable Exercise 6.1 container ex-6-5 is missing.');
  const ref = {
    page: 150, pageStart: 150, pageEnd: 150,
    recoveredPdf: 'docs/source-verification/class-12/sources/math12-unit6-recovered.pdf', pdfPage: 10,
    originalFullPdfPage: 155,
    verification: 'All 8 groups and 28 subparts visually inspected in the matching recovered scan; prompts are authored restatements, not verbatim prose.',
    sourceRelationship: 'Mathematical exercise companion to recovered source'
  };
  const part = (label, expression, result, working, domain = '') => ({label, expression, answer: result, steps: working, domain});
  const groups = [
    {
      number: 1, prompt: 'Find a family of antiderivatives for each expression. Treat a as constant.',
      promptUrdu: 'ہر عبارت کا غیر معین تکمل معلوم کریں۔ a کو مستقل سمجھیں۔',
      promptPashto: 'د هرې عبارت نامعین انتګرال پیدا کړئ. a ثابت وګڼئ.',
      parts: [
        part('a', '\\int x^3\\,dx', 'x⁴/4+C', ['Use ∫xⁿdx=xⁿ⁺¹/(n+1)+C with n=3.', 'Differentiating x⁴/4+C returns x³.']),
        part('b', '\\int(a+15)\\,dx', '(a+15)x+C', ['Both a and 15 are constants with respect to x.', 'Multiply their sum by x and add C.']),
        part('c', '\\int\\frac{1}{5x}\\,dx', '(1/5)ln|x|+C', ['Factor out 1/5 and use ∫dx/x=ln|x|+C.'], 'x≠0; work on an interval not crossing zero.'),
        part('d', '\\int(3x^2+4x-5)\\,dx', 'x³+2x²−5x+C', ['Integrate each term: ∫3x²dx=x³, ∫4xdx=2x², ∫−5dx=−5x.', 'Combine the terms with one arbitrary constant.']),
        part('e', '\\int(1+3t)t^3\\,dt', 't⁴/4+(3/5)t⁵+C', ['Expand the integrand to t³+3t⁴.', 'Integrate both powers using the power rule.']),
        part('f', '\\int\\frac{1}{x^3}\\,dx', '−1/(2x²)+C', ['Write 1/x³=x⁻³.', 'Its antiderivative is x⁻²/(−2)+C.'], 'x≠0.'),
        part('g', '\\int e^{5x}\\,dx', '(1/5)e⁵ˣ+C', ['The derivative of 5x is 5; divide the exponential by 5.', 'A derivative check gives (1/5)·5e⁵ˣ=e⁵ˣ.']),
        part('h', '\\int\\frac{5}{1+x^2}\\,dx', '5 arctan x+C', ['Factor out 5 and use d(arctan x)/dx=1/(1+x²).']),
        part('i', '\\int t^3\\sqrt{t}\\,dt', '(2/9)t⁹ᐟ²+C', ['Combine powers: t³√t=t⁷ᐟ².', 'Add one to the exponent and divide by 9/2, giving (2/9)t⁹ᐟ²+C.'], 'Real integrand for t≥0; the antiderivative calculation applies on t>0 and extends continuously to t=0.')
      ],
      clarification: 'The printed answer key omits +C in some indefinite integrals. Every indefinite answer here includes its arbitrary constant.'
    },
    {
      number: 2, prompt: 'Use a suitable change of variable to integrate each expression.',
      promptUrdu: 'مناسب متغیر بدل کر ہر عبارت کا تکمل معلوم کریں۔',
      promptPashto: 'د مناسب متغیر په بدلولو د هرې عبارت انتګرال پیدا کړئ.',
      parts: [
        part('a', '\\int(3x+4)^8\\,dx', '(3x+4)⁹/27+C', ['Let u=3x+4, so du=3dx.', 'The integral is (1/3)∫u⁸du=u⁹/27+C; substitute back.']),
        part('b', '\\int3x^2(x^3-4)\\,dx', '(x³−4)²/2+C', ['Let u=x³−4 and du=3x²dx.', 'Integrate ∫u du=u²/2+C.']),
        part('c', '\\int(3x^2+7)(x^3+7x)^8\\,dx', '(x³+7x)⁹/9+C', ['Let u=x³+7x. Its differential is du=(3x²+7)dx.', 'Integrate ∫u⁸du=u⁹/9+C.']),
        part('d', '\\int\\frac{3x^2-7}{(x^3-7x)^4}\\,dx', '−1/[3(x³−7x)³]+C', ['Let u=x³−7x, so du=(3x²−7)dx.', 'The integral is ∫u⁻⁴du=−u⁻³/3+C.'], 'x³−7x≠0; exclude x=0, ±√7.'),
        part('e', '\\int\\frac{6t}{\\sqrt{3t^2-7}}\\,dt', '2√(3t²−7)+C', ['Let u=3t²−7, so du=6t dt.', 'Integrate ∫u⁻¹ᐟ²du=2√u+C.'], '|t|>√(7/3).'),
        part('f', '\\int\\frac{\\sqrt{r^{1/3}+4}}{r^{2/3}}\\,dr', '2(∛r+4)³ᐟ²+C', ['Let u=∛r+4, using the real cube root. For r≠0, du=(1/3)r⁻²ᐟ³dr.', 'The integral becomes 3∫u¹ᐟ²du=2u³ᐟ²+C.', 'Return to r: 2(∛r+4)³ᐟ²+C.'], 'Use the real cube root; r≥−64 and r≠0. Differentiate on the open intervals (−64,0) or (0,∞).'),
        part('g', '\\int\\frac{x+3x^2}{\\sqrt{x}}\\,dx', '(2/3)x³ᐟ²+(6/5)x⁵ᐟ²+C', ['Set u=√x, so x=u² and dx=2u du.', 'The transformed integrand is [(u²+3u⁴)/u](2u)du=(2u²+6u⁴)du.', 'Its integral is (2/3)u³+(6/5)u⁵+C. Substitute u=√x.'], 'x>0 because √x is in the denominator.'),
        part('h', '\\int\\frac{x+1}{(x^2+2x+2)^2}\\,dx', '−1/[2(x²+2x+2)]+C', ['Let u=x²+2x+2, so du=2(x+1)dx.', 'The integral is (1/2)∫u⁻²du=−1/(2u)+C.', 'The denominator x²+2x+2=(x+1)²+1 is positive for all real x.'])
      ],
      clarification: 'Part (f) uses the variable r in the recovered question; the supplied printed key changes it to x. The answer here consistently uses r. Constants and real-domain restrictions are made explicit.'
    },
    {
      number: 3, prompt: 'Integrate these exponential expressions by substitution.',
      promptUrdu: 'متغیر بدل کر ان اسّی عبارات کے تکمل معلوم کریں۔',
      promptPashto: 'د متغیر په بدلولو د دې نمایي عباراتو انتګرالونه پیدا کړئ.',
      parts: [
        part('a', '\\int6e^{6t}\\,dt', 'e⁶ᵗ+C', ['Set u=6t, du=6dt.', 'Integrate ∫eᵘdu=eᵘ+C.']),
        part('b', '\\int xe^{5x^2+1}\\,dx', '(1/10)e^(5x²+1)+C', ['Set u=5x²+1; then du=10x dx.', 'The integral is (1/10)∫eᵘdu.']),
        part('c', '\\int(x^2-2)e^{x^3-6x+4}\\,dx', '(1/3)e^(x³−6x+4)+C', ['Set u=x³−6x+4, so du=3(x²−2)dx.', 'The integral is (1/3)∫eᵘdu=(1/3)eᵘ+C.']),
        part('d', '\\int8^{7-3x^2}(-6x)\\,dx', '8^(7−3x²)/ln 8+C', ['Set u=7−3x², du=−6x dx.', 'Since d(8ᵘ)/du=(ln8)8ᵘ, integrate ∫8ᵘdu=8ᵘ/ln8+C.'])
      ],
      clarification: 'An arbitrary constant is included for all four indefinite integrals, including the entries where the printed key omits it.'
    },
    {
      number: 4, prompt: 'Determine y(x) when dy/dx=4x³+6x² and y(1)=0.',
      promptUrdu: 'اگر dy/dx=4x³+6x² اور y(1)=0 ہو تو y(x) معلوم کریں۔',
      promptPashto: 'که dy/dx=4x³+6x² او y(1)=0 وي، y(x) پیدا کړئ.',
      steps: ['Integrate the slope: y=x⁴+2x³+C.', 'Apply y(1)=0: 0=1+2+C, giving C=−3.', 'Therefore y=x⁴+2x³−3.', 'Check: y′=4x³+6x² and y(1)=1+2−3=0.'],
      answer: 'y=x⁴+2x³−3'
    },
    {
      number: 5, prompt: 'Recover the curve whose derivative is x(2x²−1)² and which contains the point (3,3).',
      promptUrdu: 'وہ منحنی معلوم کریں جس کا مشتق x(2x²−1)² ہے اور جو نقطہ (3,3) سے گزرتا ہے۔',
      promptPashto: 'هغه منحني پیدا کړئ چې مشتق یې x(2x²−1)² وي او له (3,3) ټکي تېره شي.',
      steps: ['Let u=2x²−1. Then du=4x dx, so y=(1/4)∫u²du=u³/12+C.', 'At x=3, u=17. The initial condition gives 3=17³/12+C=4913/12+C.', 'Thus C=(36−4913)/12=−4877/12.', 'The exact curve is y=[(2x²−1)³−4877]/12.', 'Differentiate: y′=(1/12)·3(2x²−1)²·4x=x(2x²−1)². At x=3, y=(4913−4877)/12=3.'],
      answer: 'y=[(2x²−1)³−4877]/12',
      clarification: 'The printed answer key rounds the constant to −406.42. The exact constant is −4877/12≈−406.4166667; using the rounded constant does not satisfy y(3)=3 exactly.'
    },
    {
      number: 6, prompt: 'A cumulative excretion model has f′(t)=0.01e^(−0.01t), with t in minutes. (a) Find f(t), including its integration constant. (b) With f(0)=0, find the amount excreted in the first 10 minutes.',
      promptUrdu: 'اخراج کی مجموعی مقدار کے نمونے میں f′(t)=0.01e^(−0.01t) ہے اور t منٹوں میں ہے۔ (a) مستقل سمیت f(t) معلوم کریں۔ (b) اگر f(0)=0 ہو تو پہلے 10 منٹ میں خارج شدہ مقدار معلوم کریں۔',
      promptPashto: 'د ټولې خارج شوې اندازې په ماډل کې f′(t)=0.01e^(−0.01t) دی او t په دقیقو کې دی. (a) له ثابت سره f(t) پیدا کړئ. (b) که f(0)=0 وي، په لومړیو 10 دقیقو کې خارج شوې اندازه پیدا کړئ.',
      steps: ['(a) Integrate: f(t)=0.01[e^(−0.01t)/(−0.01)]+C=−e^(−0.01t)+C.', '(b) The initial condition gives 0=−1+C, so C=1 and f(t)=1−e^(−0.01t).', 'At t=10, the cumulative amount is f(10)=1−e⁻⁰·¹≈0.0951626 units.', 'The derivative is 0.01e^(−0.01t), and the model starts at zero and increases for t≥0.'],
      answer: '(a) f(t)=−e^(−0.01t)+C. (b) f(t)=1−e^(−0.01t), with f(10)≈0.0951626 units.',
      subpartCount: 2,
      clarification: 'The supplied key’s part (a) omits the constant. The initial condition in part (b) requires C=1, not zero.'
    },
    {
      number: 7, prompt: 'A weight–height model uses dW/dh=0.0015h², where W is in pounds and h in inches. (a) Find W(h) given W(60)=108. (b) Evaluate the model for a height of 5 feet 10 inches.',
      promptUrdu: 'وزن اور قد کے ایک نمونے میں dW/dh=0.0015h² ہے، جہاں W پاؤنڈ اور h انچ میں ہیں۔ (a) W(60)=108 سے W(h) معلوم کریں۔ (b) 5 فٹ 10 انچ کے قد پر نمونے کی قیمت معلوم کریں۔',
      promptPashto: 'د وزن او قد په یوه ماډل کې dW/dh=0.0015h² دی؛ W په پونډو او h په انچو کې دي. (a) د W(60)=108 له شرطه W(h) پیدا کړئ. (b) د 5 فوټه او 10 انچه قد لپاره د ماډل ارزښت پیدا کړئ.',
      steps: ['(a) Integrate: W(h)=0.0015h³/3+C=0.0005h³+C.', 'At h=60, 108=0.0005(60³)+C=108+C, hence C=0.', '(b) Convert 5 feet 10 inches to h=5·12+10=70 inches.', 'Then W(70)=0.0005(70³)=171.5 pounds.', 'This is the output of the exercise’s mathematical model, not an individual health or body-weight recommendation.'],
      answer: '(a) W(h)=0.0005h³. (b) 171.5 pounds.', subpartCount: 2
    },
    {
      number: 8, prompt: 'For 0≤t≤9 years, a city model satisfies dN/dt=400+600√t and N(0)=5000. Find N(9).',
      promptUrdu: '0≤t≤9 سال کے لیے شہر کی آبادی کا نمونہ dN/dt=400+600√t اور N(0)=5000 ہے۔ N(9) معلوم کریں۔',
      promptPashto: 'د 0≤t≤9 کلونو لپاره د ښار د نفوس ماډل dN/dt=400+600√t او N(0)=5000 دی. N(9) پیدا کړئ.',
      steps: ['Integrate the growth rate: N(t)=400t+600·(2/3)t³ᐟ²+C=400t+400t³ᐟ²+C.', 'Apply N(0)=5000 to obtain C=5000.', 'At t=9, t³ᐟ²=(√9)³=27.', 'Thus N(9)=400·9+400·27+5000=3600+10800+5000=19400.', 'Differentiating the recovered model returns 400+600√t on the specified interval.'],
      answer: 'N(t)=5000+400t+400t³ᐟ²; N(9)=19,400 people.'
    }
  ];
  const recovered = groups.map(group => {
    const lines = group.parts ? group.parts.map(p => `(${p.label}) \\(${p.expression}\\)`) : [];
    const steps = group.parts ? group.parts.flatMap(p => [
      `(${p.label}) ${p.steps.join(' ')} Answer: ${p.answer}.` + (p.domain ? ' Domain: ' + p.domain : '')
    ]) : group.steps;
    return {
      id: 'ex-6-1-recovered-q' + group.number, qNo: String(group.number),
      question: [group.prompt, ...lines].join('\n'),
      questionUrdu: [group.promptUrdu, ...lines].join('\n'), questionPashto: [group.promptPashto, ...lines].join('\n'),
      steps, solution: steps.join('\n'), answer: group.answer || group.parts.map(p => `(${p.label}) ${p.answer}`).join('; '),
      subparts: group.parts || [], subpartCount: group.parts ? group.parts.length : group.subpartCount || 1,
      progressiveSolution: true, solutionOrigin: 'SpaceBook worked solution',
      questionOrigin: 'SpaceBook-authored restatement of recovered mathematical exercise',
      sourceStatus: 'mathematical_inputs_recovered_from_matching_independent_scan',
      solutionStatus: 'worked and checked', sourceReferences: [{...ref}],
      sourceClarification: group.clarification || '',
      answerTranslationStatus: 'pending; question translations are authored'
    };
  });
  for (const item of recovered) {
    const prior = exercise.problems.findIndex(p => p.id === item.id);
    if (prior >= 0) exercise.problems[prior] = item;
    else exercise.problems.push(item);
  }
  exercise.pageStart = 150;
  exercise.pageEnd = 150;
  exercise.recoveredSourceReferences = [{...ref}];
  exercise.recoveryNotice = 'The original supplied files omitted this exercise. Its mathematical questions are now available from an independently recovered matching scan. These eight groups use original SpaceBook prose and worked solutions; the earlier supplied-file gap notes and printed answer key are retained as historical source context.';
  exercise.sourceStatus = 'recovered_mathematical_companion';
  exercise.recoveredQuestionGroups = 8;
  exercise.recoveredSubparts = 28;
})();
