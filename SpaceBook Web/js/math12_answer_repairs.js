/* Checked learning answers for source-limited Class 12 Mathematics questions.
 * Load after math_12_data.js. Source wording and unresolved source flags remain intact. */
(function () {
  'use strict';
  if (typeof MATH_12_DATA === 'undefined') throw new Error('Class 12 Mathematics data must load before answer repairs.');
  const problems = MATH_12_DATA.flatMap(chapter => (chapter.exercises || []).flatMap(exercise => exercise.problems || []));
  const find = id => {
    const matches = problems.filter(problem => problem.id === id);
    if (matches.length !== 1) throw new Error('Expected one Mathematics question: ' + id);
    return matches[0];
  };
  const update = (id, patch) => {
    const problem = find(id);
    Object.assign(problem, patch);
    if (patch.steps) problem.solution = patch.steps.join('\n');
    problem.progressiveSolution = true;
    problem.solutionOrigin = 'SpaceBook learning enhancement';
  };

  update('ex-2-1-q5', {
    steps: [
      'The domain is the set of horizontal coordinates occupied by the highlighted profile. The range is the set of its vertical coordinates. Read the highlighted curve, rather than every pixel in the photograph.',
      '(i) The landscape reaches the horizontal axis at the valley and reaches a highest visible level near y = 4. Its visible range is approximately [0, 4].',
      '(ii) The upper car profile has a highest marked point near (8, 3) and approaches the horizontal axis at its ends. Its intended visible range is approximately [0, 3].',
      'For either picture, let a and b be the x-coordinates of the left and right endpoints of the highlighted profile. If those endpoints are included, the domain is [a, b]. Exclude an endpoint only when the graph explicitly indicates that it is excluded.',
      'The supplied pictures do not identify both horizontal endpoints clearly enough to certify numerical domains. Thus the source-supported answer is D₁ = [a₁, b₁], R₁ ≈ [0, 4]; D₂ = [a₂, b₂], R₂ ≈ [0, 3], with the a and b endpoint values unresolved. A cropped photograph does not justify an infinite domain.',
      'Illustrative method only: if a separate profile is explicitly drawn from (−2, 1) to (6, 2), includes both endpoints, and takes every height from 0 to 4, its domain is [−2, 6] and its range is [0, 4]. These example endpoints are chosen for demonstration; they are not measurements recovered from either textbook photograph.'
    ],
    answer: '(i) D₁ = [a₁, b₁], R₁ ≈ [0, 4]. (ii) D₂ = [a₂, b₂], R₂ ≈ [0, 3], where a and b denote the included profile endpoints. Exact numerical domains remain unresolved in the supplied source.',
    solutionStatus: 'partial: photographic profile endpoints unverified',
    sourceStatus: 'unresolved_photographic_endpoints',
    sourceClarification: 'The visible range estimates and the domain-reading method are answered. The illustrative interval is explicitly supplemental; no numerical textbook endpoint has been invented.'
  });

  update('ex-2-3-project', {
    steps: [
      '(i) The highlighted roof profile consists of two straight sloping pieces meeting at a peak. It is an inverted absolute-value profile: a piecewise-linear function with a downward-pointing cusp.',
      'A general model of that function type is f(x) = k − a|x − h|, with a > 0. It has vertex (h, k); for x ≤ h it is k + a(x − h), and for x ≥ h it is k − a(x − h). This is a general form identifying the function family, not a transcription of the photograph’s unreadable coefficients.',
      '(ii) The displayed equation contains a squared x-shift with a negative coefficient. It is a quadratic function, represented by a downward-opening parabola.',
      'Its general vertex form is g(x) = k − a(x − h)², with a > 0. The graph has a smooth maximum at (h, k), whereas the absolute-value roof has a sharp corner.',
      'The question asks for the type of function, so these classifications answer it. Exact coefficients of the first printed model remain unreadable and have not been asserted.'
    ],
    answer: '(i) Inverted absolute-value (piecewise-linear) function. (ii) Quadratic function with a downward-opening parabola.',
    solutionStatus: 'worked and checked: requested function classifications',
    sourceStatus: 'partial_source_legibility: first model coefficients remain unreadable',
    sourceClarification: 'The requested classifications are complete from the visible curve shapes and formula structure. A full exact algebraic model is outside the question and remains uncertified in the source.'
  });

  update('ex-10-1-q2', {
    sourceQuestionBlocks: [{
      type: 'figure',
      src: 'assets/math12/ode290-q2c-source-review.jpg',
      caption: 'Exercise 10.1 Q2(c): original function and equation; the right-side exponent is unclear',
      alt: 'Source Q2(c), y = (x + c)e to the power −x and dy/dx + y = e with a smudged exponent. The exact right-side exponent is unresolved.',
      displayWidth: 408
    }],
    solutionStatus: 'partial: Q2(c) printed exponent unresolved; conditional calculation supplied',
    sourceStatus: 'partial_source_legibility',
    sourceClarification: 'Direct differentiation gives y′ + y = e^(−x) for the readable function in (c). This establishes the conditional mathematical answer without certifying the smudged printed exponent. Part (d) fails its printed equation with residual 6e^(−x). The source crop now shows Q2(c); the previous crop showed Q2(d).'
  });

  update('ex-12-2-q5', {
    steps: [
      'The source supplies the interval [0, 2] but no integrand f(x) or partition count. There is no unique numerical answer: for example, f(x) = 1 has area 2 while f(x) = 2 has area 4 on the same interval.',
      'For a specified integrand, choose N equal subintervals and set h = 2/N, xᵢ = ih, and fᵢ = f(xᵢ). For geometric area when f changes sign, apply the rule to |f| or split at the zeros; the ordinary rule approximates the signed integral.',
      'Trapezoidal rule: T_N = (h/2)[f₀ + 2(f₁ + ⋯ + f_(N−1)) + f_N].',
      'Simpson’s rule requires even N: S_N = (h/3)[f₀ + 4(f₁ + f₃ + ⋯ + f_(N−1)) + 2(f₂ + f₄ + ⋯ + f_(N−2)) + f_N]. Here N counts subintervals, so there are N/2 Simpson panels.',
      'Illustrative worked example only: choose f(x) = e^(−x) and N = 10. This chosen function is nonnegative on [0, 2]. These are supplemental inputs, not recovered missing textbook information.',
      'Then h = 0.2 and fᵢ = e^(−0.2i), i = 0, 1, …, 10. Substitution in the trapezoidal sum gives T₁₀ ≈ 0.8675450128.',
      'The odd-index sum is e^(−0.2) + e^(−0.6) + e^(−1) + e^(−1.4) + e^(−1.8); the even-index interior sum is e^(−0.4) + e^(−0.8) + e^(−1.2) + e^(−1.6). The Simpson sum gives S₁₀ ≈ 0.8646723662.',
      'The exact sample integral is [−e^(−x)]₀² = 1 − e^(−2) ≈ 0.8646647168. The absolute errors are approximately 0.0028802961 for T₁₀ and 0.0000076495 for S₁₀.',
      'The source-style illustrative Maple workflow is with(Student[Calculus1]): followed by ApproximateInt(exp(-x),x=0..2,method=trapezoid,output=plot); and ApproximateInt(exp(-x),x=0..2,method=simpson,output=plot);. These commands describe the illustrative plots; no Maple execution or default partition count is claimed. The N = 10 values above are independently calculated finite sums.',
      'For the original printed question, an integrand and partition must first be supplied. Different inputs give different approximations; the missing source data remain unresolved.'
    ],
    answer: 'No unique numerical source answer: f(x) and the partition are unspecified. Explicit supplemental example f(x) = e^(−x), N = 10: T₁₀ ≈ 0.8675450128; S₁₀ ≈ 0.8646723662; exact area ≈ 0.8646647168.',
    solutionStatus: 'partial: source omits integrand and partition; complete supplemental example supplied',
    sourceStatus: 'under_specified_source_problem',
    sourceClarification: 'The general formulas and labelled example answer the available mathematical task. They do not turn the incomplete printed prompt into a source-complete numerical question.'
  });

  globalThis.MATH12_ANSWER_REPAIRS = Object.freeze({
    questionIds: ['ex-2-1-q5', 'ex-2-3-project', 'ex-10-1-q2', 'ex-12-2-q5'],
    completeRequestedClassifications: ['ex-2-3-project'],
    unresolvedSourceAnswers: ['ex-2-1-q5', 'ex-10-1-q2', 'ex-12-2-q5'],
    missingSourcePages: [142, 157]
  });
})();
