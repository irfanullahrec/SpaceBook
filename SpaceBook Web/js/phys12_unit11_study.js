/* Canonical Unit 11 exercise answers. Printed source records are read, never replaced.
 * Answers are SpaceBook-authored; printed errors and conditional interpretations remain visible. */
(function () {
  'use strict';
  if (typeof PHYS_12_DATA === 'undefined') throw new Error('Load Physics 12 before its Unit 11 study bank.');
  const ch = PHYS_12_DATA.find(chapter => Number(chapter.number) === 11);
  const section = id => { const s = ch.sections.find(s => s.id === id); if (!s) throw new Error('Missing Physics source section ' + id); return s; };
  const ids = {
    mcq: 'phys12-front-exercise11-mcq-pages46-47', continuation: 'phys12-front-exercise11-mcq-cont48',
    conceptual: 'phys12-front-conceptual48', comprehensive: 'phys12-front-comprehensive49',
    numericalStart: 'phys12-front-numerical49', numerical: 'phys12-front-numerical50-51'
  };
  const sourcePdf = 'Books/12th/12th Physics/PDF/Physics Book for 12 class KPTBB.pdf';
  const source = (id, index, printedPage) => ({id, index, printedPage, para: section(id).paras[index]});
  const make = (kind, number, fragments) => {
    const join = language => fragments.map(f => f.para[language] || (language === 'text' ? f.para.text : '')).join(' ');
    return {
      id: 'phys12-u11-' + kind + '-' + String(number).padStart(2, '0'), qNo: number,
      q: join('text'), qUrdu: join('urdu'), qPashto: join('pashto'), originalSourceText: join('text'),
      origin: 'Textbook question with SpaceBook worked answer', answerOrigin: 'SpaceBook worked answer',
      sourceReferences: fragments.map(f => ({sourcePdf, pdfPage: f.printedPage <= 47 ? 28 : f.printedPage <= 49 ? 29 : 30, printedPage: f.printedPage, sectionId: f.id, paragraphIndices: [f.index]})),
      questionTranslationStatus: 'reuses_reviewed_source_translations', answerTranslationStatus: 'pending',
      answerReviewStatus: 'mathematics_and_source_question_checked', sourceClarification: ''
    };
  };
  const splitChoices = text => {
    const pieces = text.split(/\n[A-D]\.\s*/);
    return {q: pieces[0], options: pieces.slice(1)};
  };
  const answer = (item, steps, final, note = '') => Object.assign(item, {
    steps, sol: steps.join('\n'), solution: steps.join('\n'), answer: final || steps[steps.length - 1],
    sourceClarification: note
  });
  const mcqSteps = [
    ['F=(k/R²)q(Q−q). Complete the square: q(Q−q)=Q²/4−(q−Q/2)².', 'For 0≤q≤Q, the maximum occurs at q=Q/2. Select C.'],
    ['Repulsion shows that B and C have nonzero charges of the same sign.', 'Attraction does not prove that A is charged: A may have the opposite sign, or it may be neutral and polarized.', 'Therefore none of A–D is forced by the wording. If all three objects are explicitly assumed charged, B is the intended answer.'],
    ['The two forces form a Newton-third-law pair.', 'They are equal in magnitude and opposite in direction, regardless of whether the charges are 2 μC or 6 μC: F_AB=−F_BA. Select B.'],
    ['In electrostatic equilibrium the field inside a conductor is zero.', 'There is no potential difference between its points, so its potential is constant throughout. Select C under the equilibrium assumption.'],
    ['E=F/q has units N/C. Since 1 V=1 J/C and 1 J=1 N·m, V/m=N/C=J/(C·m).', 'Thus A, B and C express equivalent electric-field units if option C means J/(C·m). D, V·m, is not a field unit.'],
    ['The kinetic-energy gain of a proton accelerated from rest through a 1 kV potential drop is e×1000 V.', 'This is 1000 eV=1 keV, independent of proton mass. Select C.'],
    ['Convert r=20 cm=0.20 m and q=2 μC=2×10⁻⁶ C.', 'E=k|q|/r²=(9×10⁹)(2×10⁻⁶)/(0.20)²=4.5×10⁵ N/C.', 'No printed value matches; all printed choices also use N rather than N/C.'],
    ['Gauss’s law gives total outward flux q/ε₀ through the cube.', 'The centered charge and six equal faces give equal fluxes, so one face receives q/(6ε₀). A is the intended grouped expression.'],
    ['The net flux through a closed sphere is Q_enclosed/ε₀.', 'It depends on the enclosed charge, not the sphere’s area or radius. External charges contribute zero net flux. Select D.'],
    ['Use U=½CV² with C=1×10⁻⁶ F and V=4000 V.', 'U=½×10⁻⁶×4000²=8 J. Select A.'],
    ['The original figure has 2 μF, 3 μF and 6 μF in series across 10 V.', '1/C_eq=1/2+1/3+1/6=1 (μF)⁻¹, so C_eq=1 μF.', 'Every series capacitor carries the same charge: Q=C_eqV=10 μC. Thus the 3 μF capacitor carries 10 μC.', 'The numeric value in B is intended, but its printed unit μF is a capacitance unit. None of the printed options is a dimensionally correct charge.'],
    ['The ion has charge +2e and moves 8.00 m along a uniform 4.00 N/C field.', 'The field does work qEd=(2e)(4.00)(8.00)=64 eV. Released from rest, it gains kinetic energy 64 eV. Select B.'],
    ['Take ΔV=V_B−V_A. The potential-energy change is ΔU=qΔV.', 'The electric field’s work is W_field=−ΔU=−qΔV. Select A with this standard definition of ΔV.', 'The external work in quasistatic transport would instead be +qΔV. Reversing the definition of ΔV also reverses the sign.']
  ];
  const mcqCorrect = [2, null, 1, 2, null, 2, null, 0, 3, 0, null, 1, 0];
  const mcqFinal = ['C: q=Q/2', 'Underdetermined; B only if all three objects are known to be charged.', 'B: F_AB=−F_BA', 'C: constant throughout at electrostatic equilibrium', 'A, B and C under J/(C·m) grouping', 'C: 1 keV', '4.5×10⁵ N/C; no valid printed option', 'A, interpreted as q/(6ε₀)', 'D: enclosed charge', 'A: 8 J', '10 μC; B has the intended number but the wrong unit', 'B: 64 eV', 'A: W_field=−qΔV for ΔV=V_B−V_A'];
  const mcqs = mcqSteps.map((steps, i) => {
    const n = i + 1;
    const fragments = n <= 11 ? [source(ids.mcq, i, n <= 6 ? 46 : 47)] : n === 12 ? [source(ids.mcq, 11, 47), source(ids.continuation, 0, 48)] : [source(ids.continuation, 1, 48)];
    const item = make('mcq', n, fragments);
    for (const [field, language] of [['q', ''], ['qUrdu', 'Urdu'], ['qPashto', 'Pashto']]) {
      const parts = splitChoices(item[field]); item[field] = parts.q; item['options' + language] = parts.options;
    }
    if (item.options.length !== 4) throw new Error('Physics Unit 11 MCQ source choices do not align: ' + n);
    answer(item, steps, mcqFinal[i]); item.exp = item.sol;
    if (mcqCorrect[i] !== null) item.correct = mcqCorrect[i];
    if (n === 5) { item.correctAnswers = [0, 1, 2]; item.choiceIssues = 'Multiple equivalent units; option C grouping is typographically ambiguous.'; }
    if (n === 2) item.choiceIssues = 'No uniquely entailed printed choice unless all objects are assumed charged.';
    if (n === 7) item.choiceIssues = 'Calculated value absent; all source option units are wrong.';
    if (n === 11) item.choiceIssues = 'All choices use μF although a charge in μC is requested.';
    if ([2,5,7,11].includes(n)) item.sourceStatus = 'printed_choice_issue';
    if (n === 8) item.sourceClarification = 'The source prints q/6 ε₀ without explicit denominator grouping; the Gauss-law answer is q/(6ε₀).';
    if (n === 13) item.sourceClarification = 'The source does not explicitly define the order in ΔV. The answer uses ΔV=V_B−V_A and distinguishes field work from external work.';
    return item;
  });
  const conceptualSteps = [
    ['For an electrostatic potential, E=−∇V.', 'If V is constant throughout the region, all spatial derivatives vanish and E=0 there.'],
    ['Yes, under the stated fixed field direction and release from rest, with no other forces.', 'F=qE always lies along the same straight line. Its magnitude, hence the speed of the charge, may vary with position, but there is no transverse acceleration.', 'A positive charge accelerates along the field and a negative one opposite it. A neutral particle released at rest remains at rest.'],
    ['Potential difference is the change of potential energy per unit charge: ΔV=ΔU/q for q≠0.', 'Equivalently, ΔU=q(V_B−V_A); field work is −ΔU and quasistatic external work is +ΔU.'],
    ['A volt measures potential difference: 1 V=1 J/C.', 'An electron-volt measures energy: 1 eV=e×1 V≈1.602×10⁻¹⁹ J.', 'A charge of magnitude e gaining energy through 1 V gains 1 eV. The units measure different physical quantities and are not interchangeable.'],
    ['For a specified reference, the potential energy of a charge q in a source potential V is U=qV.', 'A high potential can therefore correspond to small potential energy when |q| is small; for example, 1 nC at 1000 V has U=1 μJ.', 'For a charged capacitor, the separate system-energy formula is U=½QV=½CV², so small capacitance can likewise limit stored energy.'],
    ['Yes outside the sphere if its charge density is spherically symmetric, even if that density varies with radius.', 'For r≥R, Gauss’s law then gives E=kQ/r² and V=kQ/r with V(∞)=0, the same as a central point charge.', 'An arbitrary angularly nonuniform distribution generally does not have exactly that external potential. Inside an extended distribution it is generally not kQ/r. The spherical-symmetry condition must be stated.'],
    ['The comparison requires a fixed quantity. For positive capacitances, C_parallel=C₁+C₂+C₃ exceeds C_series=(1/C₁+1/C₂+1/C₃)⁻¹.', 'Across the same fixed voltage, U=½C_eqV²: the parallel combination stores more energy.', 'For the same fixed net charge Q on the two-terminal combination, U=Q²/(2C_eq): the parallel combination stores LESS energy, and the series combination stores more.', 'Without specifying the charging conditions, the printed question has no unique comparison.'],
    ['Equipotential curves representing different potential values cannot cross.', 'At a crossing point the single-valued scalar potential would have to have two different values, which is impossible.'],
    ['Ordinary water contains mobile ions and permits leakage current between plates. This dissipates charge and energy rather than maintaining an ideal dielectric.', 'Its electrical behavior also depends strongly on purity, temperature and frequency, and water can cause corrosion or electrochemical reactions.', 'Highly purified water has specialized uses, but the large dielectric constant alone does not make ordinary water a suitable practical capacitor dielectric.'],
    ['For an ideal parallel-plate capacitor fully filled with a dielectric, C=κε₀A/d.', 'Increase the overlapping plate area A, reduce the gap d, or use a dielectric with higher relative permittivity κ, while respecting insulation and breakdown limits.']
  ];
  const shortQuestions = conceptualSteps.map((steps, i) => answer(make('conceptual', i+1, [source(ids.conceptual, i, 48)]), steps));
  shortQuestions[6].sourceClarification = 'Fixed voltage and fixed total charge give opposite comparisons. The old worked-answer section incorrectly claimed more energy in parallel for fixed Q.';
  const comprehensiveSteps = [
    ['For stationary point charges separated by r in vacuum, F=(1/(4πε₀))|q₁q₂|/r². The force acts on the joining line; like charges repel and unlike charges attract.', 'The vector forces on the two charges are equal and opposite. For charges in a homogeneous linear dielectric, replace ε₀ by ε=κε₀, reducing the force by κ under this model.', 'One coulomb is the charge transported by a current of one ampere in one second: 1 C=1 A·s. Equivalently in the ideal Coulomb-law comparison, two equal 1 C point charges 1 m apart in vacuum exert about 8.99×10⁹ N on one another.', 'The inverse-square law applies directly to point charges; extended distributions require summing or integrating their contributions.'],
    ['Electric field assigns to each position the force per unit positive test charge: E=lim(q₀→0)F/q₀.', 'Using a sufficiently small test charge avoids materially disturbing the source charges. A charge q placed in the field experiences F=qE.', 'The direction is the force direction on a positive test charge; a negative charge feels the opposite force.', 'Its units are N/C, equivalently V/m. For a point charge, E=(1/(4πε₀))(q/r²) r̂; positive q gives an outward field.'],
    ['Electric flux measures the field crossing an oriented surface: Φ=∫ E·dA.', 'For a flat surface of area A in a uniform field, Φ=EA cosθ, where θ is measured from the chosen area normal.', 'The signed maximum is +EA at θ=0°, zero flux occurs at 90°, and the signed minimum is −EA at 180°.', 'The magnitude is largest, EA, when the surface is perpendicular to the field, and smallest, zero, when the surface is parallel to the field. Distinguish signed flux from its magnitude.'],
    ['Gauss’s law for electrostatics is ∮ E·dA=Q_enclosed/ε₀, with outward area normals on a closed surface.', 'For a point charge q, E=q r̂/(4πε₀r²). A surface element subtends signed solid angle dΩ=(r̂·dA)/r², so E·dA=q dΩ/(4πε₀).', 'A closed surface enclosing the charge has total solid angle 4π, giving flux q/ε₀. For a charge outside it, the signed entering and leaving solid angles cancel, giving zero net flux.', 'By superposition, sum the contributions from all charges: only enclosed charges contribute to the net flux. The result extends to continuous distributions.', 'For a spherical Gaussian surface around a spherically symmetric source, E4πr²=Q_enclosed/ε₀. For a large ideal plane sheet, a pillbox gives 2EA=σA/ε₀, hence E=σ/(2ε₀).', 'A practical application is electrostatic shielding: free charges rearrange on a closed conducting enclosure until the field in its conducting material vanishes; an empty enclosed cavity with no internal charge is shielded from external electrostatic fields.'],
    ['Potential difference is work per unit charge supplied externally in quasistatic transport: V(r)−V(r₀)=−∫ from r₀ to r E·dl.', 'For a point source charge Q, the radial field is E_r=kQ/r². Choose V(∞)=0.', 'Then V(r)=−∫∞ʳ kQ/r′² dr′=kQ/r, for r>0.', 'Potential is a scalar; its sign follows Q under this reference. For several source charges, add their potentials algebraically.'],
    ['A capacitor consists of two conducting electrodes separated by an insulating gap or dielectric. Opposite charges ±Q on the conductors produce a potential difference V, with C=Q/V.', 'During quasistatic charging of a linear capacitor, when its charge is q the voltage is q/C.', 'Adding dq requires work dW=(q/C)dq. Integrating from 0 to Q gives U=∫₀Q(q/C)dq=Q²/(2C).', 'Using Q=CV gives the equivalent forms U=½QV=½CV². This stored energy is associated with the electric field.'],
    ['An equipotential surface has the same potential at every point. A displacement along it has dV=0 and the electrostatic field does no work on a charge moving along it.', 'For any infinitesimal displacement dl, dV=−E·dl. In a chosen coordinate direction s, E_s=−dV/ds.', 'In three dimensions, E=−∇V. The minus sign says that the electric field points toward decreasing potential.', 'Since E has no component along a regular equipotential surface, it is perpendicular to the surface wherever E is nonzero.'],
    ['In a dielectric, an applied field shifts bound positive and negative charge distributions slightly, and can partly align permanent molecular dipoles. This is polarization.', 'The resulting bound surface charges create a field opposing the applied field within a uniformly filled parallel-plate gap.', 'For a fixed free plate charge, the net field falls from E₀ to E₀/κ and the voltage from V₀ to V₀/κ. Therefore C=Q/V increases from C₀ to κC₀.', 'If the plates remain connected to a fixed-voltage source, the voltage stays fixed and the source supplies additional free charge Q=κC₀V. Distinguish these two boundary conditions.'],
    ['Take plates of area A, gap d much smaller than their lateral dimensions, and a homogeneous linear dielectric filling the gap. Neglect fringing.', 'The free surface charge density is σ=Q/A and ε=κε₀. The field magnitude is E=σ/ε=Q/(κε₀A).', 'The potential difference is V=Ed=Qd/(κε₀A).', 'Hence C=Q/V=κε₀A/d=κC₀, where C₀=ε₀A/d is the vacuum capacitance.'],
    ['For charging, connect an initially uncharged capacitor C to a constant-voltage source V₀ through resistance R at t=0. The circuit equation is R(dq/dt)+q/C=V₀.', 'Solving with q(0)=0 gives q(t)=CV₀[1−exp(−t/RC)] and i(t)=(V₀/R)exp(−t/RC).', 'For discharging, disconnect the source and connect a capacitor initially carrying Q₀ through R. Then R(dq/dt)+q/C=0.', 'Thus q(t)=Q₀exp(−t/RC). In the charging-positive convention, i=dq/dt=−(Q₀/RC)exp(−t/RC); its discharge-current magnitude is positive.', 'The time constant is τ=RC. At t=τ, charging has reached 1−e⁻¹≈63.2% of the final charge, while discharge leaves e⁻¹≈36.8% of the initial charge.', 'The coded diagrams show the charging source–resistor–capacitor loop and the source-disconnected discharge loop. Ideal charging and decay curves approach their limiting values asymptotically.'],
    ['An ordinary capacitor stores U=½CV². For a given safe voltage, storing domestic-scale energy requires a very large capacitance.', 'For example, storing 1 kWh=3.6×10⁶ J at 300 V requires C=2U/V²=80 F, even before allowing for losses or useful minimum voltage.', 'Its voltage falls as charge is withdrawn, and leakage, cost, size and dielectric breakdown constrain practical storage.', 'Capacitors are useful for short bursts and filtering; specialized high-capacitance devices have applications, but ordinary capacitors are not economical general-purpose household energy stores.']
  ];
  const longQuestions = comprehensiveSteps.map((steps, i) => answer(make('comprehensive', i+1, [source(ids.comprehensive, i, 49)]), steps));
  const numericalSteps = [
    ['Use k≈9.0×10⁹ N·m²/C² and e≈1.602×10⁻¹⁹ C.', 'F=k(26e)e/r²=(9.0×10⁹)26(1.602×10⁻¹⁹)²/(10⁻¹²)²≈6.01×10⁻³ N.', 'The opposite charges attract. With textbook e≈1.6×10⁻¹⁹ C, F≈5.99×10⁻³ N, agreeing with 6×10⁻³ N.'],
    ['The force on +4 μC from +2 μC has magnitude F₁=k(2×10⁻⁶)(4×10⁻⁶)/(0.10)²=7.2 N and is repulsive.', 'The force from −3 μC has magnitude F₂=k(3×10⁻⁶)(4×10⁻⁶)/(0.10)²=10.8 N and is attractive.', 'At the +4 μC vertex, one force points away from its neighboring charge and the other toward its neighboring charge. Their included angle is 120°, not the triangle’s interior 60°.', 'F=√(7.2²+10.8²+2·7.2·10.8 cos120°)=√90.72≈9.52 N.', 'The printed 15.7 N corresponds approximately to using 60° instead of 120°. Preserve the printed answer, but use 9.52 N for the stated signed-charge geometry.'],
    ['The midpoint is r=0.15/2=0.075 m from each charge.', 'The two fields point from the positive charge toward the negative charge and add: E=2kq/r²=2(9×10⁹)(2×10⁻⁷)/(0.075)²=6.40×10⁵ N/C.', 'The proton force is F=eE=(1.6×10⁻¹⁹)(6.40×10⁵)=1.024×10⁻¹³ N in the same direction.', 'The source calls this direction AB but does not label A and B in the printed question; the physical direction is unambiguously from + to −.'],
    ['The initial separation is r_i=0.12 m. Moving 4 cm closer gives r_f=0.12−0.04=0.08 m, not 0.04 m.', 'For slow transport, the external work equals the potential-energy increase: W_ext=kq₁q₂(1/r_f−1/r_i).', 'Substitute: W_ext=(9×10⁹)(15×10⁻¹⁰)(13×10⁻¹⁰)(1/0.08−1/0.12)=7.3125×10⁻⁸ J.', 'The work by the electric field is the negative of this value. The printed positive result uses external work.'],
    ['Assume the hollow sphere is a conducting spherical shell in electrostatic equilibrium with no internal charge.', 'At its surface, V=kQ/R=(9×10⁹)(14×10⁻⁶)/0.3=4.20×10⁵ V.', 'Inside the shell, E=0, so V remains the same constant 4.20×10⁵ V.', 'At 0.2 m from the surface, r=0.3+0.2=0.5 m, so V=kQ/r=2.52×10⁵ V.'],
    ['Interpret 280 J as external work in slow transport, as the printed answer does.', 'W_ext=q(V_f−V_i), so 280=2[V−(−12)].', 'Divide by 2: V+12=140, giving V=128 V.', 'If 280 J meant work by the field, the sign would reverse and V would be −152 V; the prompt should identify the work convention.'],
    ['For a positive point charge with zero potential at infinity, V=kq/r and E=kq/r².', 'Hence r=V/E=13/26=0.50 m.', 'Then q=Vr/k=(13)(0.50)/(9×10⁹)=7.22×10⁻¹⁰ C=0.722 nC.', 'Both the requested distance and charge are supplied; the printed answer lists only the charge.'],
    ['Put +8 μC at x=0 and −4 μC at x=0.10 m. With zero potential at infinity, V=0 requires 8/|x|=4/|x−0.10|.', 'Thus |x|=2|x−0.10|. Between the charges, x=2(0.10−x), giving x=0.20/3=0.0667 m.', 'To the right of −4 μC, x=2(x−0.10), giving x=0.20 m. To the left of +8 μC there is no solution.', 'The two finite zero-potential points are 6.67 cm from +8 μC between the charges, and 20.0 cm from +8 μC beyond −4 μC (10.0 cm beyond it).', 'The source prints only the between-charges point and mistakenly labels −4 μC as −4 μF in its answer.'],
    ['The electron initially moves along E, but its force −eE is opposite its velocity, so it slows down.', 'At the turning point, the initial kinetic energy has been removed: ½mv₀²=eEs.', 'Use m≈9.11×10⁻³¹ kg, v₀=29×10⁵ m/s=2.9×10⁶ m/s, e≈1.602×10⁻¹⁹ C and E=80 N/C.', 's=mv₀²/(2eE)≈0.2989 m≈0.299 m. The outward displacement before turning is along the initial velocity; the acceleration is opposite E.'],
    ['For series capacitors, 1/C_eq=1/4+1/6+1/8=13/24 in (μF)⁻¹. Therefore C_eq=24/13 μF≈1.846 μF.', 'The common series charge is Q=C_eqV=(24/13 μF)(250 V)=6000/13 μC≈461.54 μC.', 'Voltages are Q/C: V₄=1500/13≈115.38 V, V₆=1000/13≈76.92 V, and V₈=750/13≈57.69 V.', 'Check: V₄+V₆+V₈=3250/13=250 V. Differences from the printed approximate charge and voltages are rounding differences.'],
    ['The source circuit has 2 μF and 5 μF in parallel, giving C_p=7 μF, in series with 3 μF across 6 V.', 'C_eq=(3×7)/(3+7)=2.1 μF. The series charge is Q=2.1×6=12.6 μC.', 'The parallel pair has voltage V_p=Q/C_p=12.6/7=1.8 V.', 'The 5 μF capacitor therefore holds Q₅=(5 μF)(1.8 V)=9 μC. The source’s printed answer 9 μF has the wrong unit.'],
    ['The initially charged capacitor holds Q₀=C₁V₁=(6 μF)(120 V)=720 μC.', 'Assume the capacitors are connected in parallel, the source is disconnected, and leakage is negligible. Total charge is conserved.', 'The final combined capacitance is 6+4=10 μF, so their common voltage is V_f=720 μC/(10 μF)=72 V.', 'Their final charges are 432 μC and 288 μC, summing to 720 μC. Energy is not conserved in the capacitor fields alone during redistribution; some is dissipated or radiated.']
  ];
  const numericalFinal = ['≈6.0×10⁻³ N, attractive', '≈9.52 N for the stated geometry; printed 15.7 N is inconsistent', 'E=6.40×10⁵ N/C; F=1.024×10⁻¹³ N; both directed from + to −', 'W_ext=7.3125×10⁻⁸ J', '(a) 4.20×10⁵ V; (b) 4.20×10⁵ V; (c) 2.52×10⁵ V', '128 V for external work', 'r=0.50 m; |q|≈7.22×10⁻¹⁰ C', 'x=6.67 cm and x=20.0 cm from +8 μC toward −4 μC', 's≈0.299 m', 'C_eq≈1.846 μF; Q≈461.54 μC each; V≈115.38,76.92,57.69 V', 'Q₅=9 μC', 'V_f=72 V'];
  const numericals = numericalSteps.map((steps, i) => {
    const fragments = i === 0 ? [source(ids.numericalStart, 0, 49)] : [source(ids.numerical, i-1, i <= 7 ? 50 : 51)];
    return answer(make('numerical', i+1, fragments), steps, numericalFinal[i]);
  });
  numericals[1].sourceStatus = 'printed_answer_discrepancy';
  numericals[3].sourceClarification = 'The correct final separation is 8 cm. The old worked section incorrectly wrote 4 cm, despite displaying the printed 8 cm result.';
  numericals[7].sourceStatus = 'printed_answer_incomplete_and_wrong_unit';
  numericals[10].sourceStatus = 'printed_answer_wrong_unit';
  const svg = (label, body, h=240) => `<figure><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 ${h}" role="img" aria-label="${label}" style="width:100%;max-width:500px"><g fill="none" stroke="#334155" stroke-width="3">${body}</g></svg><figcaption>${label}</figcaption></figure>`;
  const text = (x,y,value) => `<text x="${x}" y="${y}" fill="#0f172a" stroke="none" font-size="17" text-anchor="middle">${value}</text>`;
  mcqs[10].diagramSvg = svg('Source MCQ 11: 2, 3 and 6 μF in series across 10 V', '<path d="M60 70H140M154 70H240M254 70H340M354 70H440V190H275M225 190H60V70M140 52V88M154 52V88M240 52V88M254 52V88M340 52V88M354 52V88"/>'+text(147,35,'2 μF')+text(247,35,'3 μF')+text(347,35,'6 μF')+text(250,220,'+ 10 V −'));
  mcqs[11].diagramSvg = svg('Source MCQ 12: positive ion between parallel plates', '<path d="M100 35V185M400 35V185M180 110H340M340 110L327 102M340 110L327 118"/><circle cx="155" cy="110" r="18"/>'+text(155,116,'+')+text(260,65,'E = 4.00 N/C →')+text(250,215,'8.00 m'),245);
  numericals[10].diagramSvg = svg('Source numerical 11: 3 μF in series with parallel 2 and 5 μF across 6 V', '<path d="M50 115H125M139 115H220M220 65V165M220 65H295M309 65H380M220 165H295M309 165H380M380 65V165M380 115H450V235H275M225 235H50V115M125 97V133M139 97V133M295 47V83M309 47V83M295 147V183M309 147V183"/>'+text(132,87,'3 μF')+text(302,35,'2 μF')+text(302,202,'5 μF')+text(250,264,'+ 6 V −'),285);
  // The already reviewed coded lesson diagrams supply both requested RC circuits.
  longQuestions[9].diagramSvg = section('phys12-front-rc-time-constant43').diagramSvg + section('phys12-front-discharge44').diagramSvg;
  const bank = {
    mcqs, shortQuestions, longQuestions, numericals,
    sourceTitle: 'Exercise 11 — Electrostatics', sourcePages: [46,47,48,49,50,51],
    answerOrigin: 'SpaceBook worked answers checked against original PDF pages 28–30',
    supersedesAnswerSectionId: '11.exercise.solved',
    sourceIssueCount: 9,
    limitations: ['Printed ambiguities and defective choices are retained.', 'Original English/Urdu/Pashto question text is reused; translations of newly authored answers remain pending.', 'No claim is made that the original textbook has been changed.']
  };
  ch.class12Exercise = bank;
  ch.class12StudyBank = bank;
  const old = ch.sections.find(item=>item.id===bank.supersedesAnswerSectionId);
  if(old){
    if(!old.originalAnswerDraft)old.originalAnswerDraft={title:old.title,theory:old.theory,source:old.source};
    old.title='Unit 11 Exercise — answers and source clarifications';
    old.theory=['MCQs','Conceptual questions','Comprehensive questions','Numericals'].map((label,index)=>label+'\n'+[mcqs,shortQuestions,longQuestions,numericals][index].map(item=>item.qNo+'. '+item.q+'\n'+item.steps.join('\n')+'\nAnswer: '+item.answer).join('\n\n')).join('\n\n');
    old.content=old.theory.replace(/\n/g,'<br>');old.source='SpaceBook-authored answers matched to the reviewed source exercise. Original answer draft retained in originalAnswerDraft.';
    const topic=(ch.topics||[]).find(item=>item.id===old.id);if(topic)Object.assign(topic,old);
  }
  globalThis.PHYS12_UNIT11_STUDY_REPORT={questionCount:46,mcqs:13,shortQuestions:10,longQuestions:11,numericals:12,answerTranslations:'pending',sourceQuestions:'Preserved and mapped to reviewed paragraphs; cross-page MCQ12 joined.',choiceIssues:mcqs.filter(q=>q.choiceIssues).map(q=>({number:q.qNo,issue:q.choiceIssues})),limitations:bank.limitations};
})();
