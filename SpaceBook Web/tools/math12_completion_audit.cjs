// Read-only content audit. This writes only the dedicated audit report.
// Counts are evaluated active records, not every subpart inside a question group.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const crypto = require('node:crypto');

const root = path.resolve(__dirname, '..');
const load = (relative, binding) => {
  const source = fs.readFileSync(path.join(root, relative), 'utf8');
  const sandbox = {};
  vm.createContext(sandbox);
  vm.runInContext(source + `\nthis.auditResult = ${binding};`, sandbox, { timeout: 15000, filename: relative });
  return sandbox.auditResult;
};
const units = load('js/math_12_data.js', 'MATH_12_DATA');
const book = load('js/math_12_book_data.js', 'MATH_12_BOOK_DATA');
const progress = JSON.parse(fs.readFileSync(path.join(root, 'docs/source-verification/math12.json'), 'utf8'));
const text = value => typeof value === 'string' ? value.trim() : '';
const steps = item => (item.steps || []).some(step => text(step) || text(step?.text));
const answered = item => ['answer', 'solution', 'sol', 'exp'].some(key => text(item[key])) || steps(item);
const explained = item => ['solution', 'sol', 'exp'].some(key => text(item[key])) || steps(item);
const placeholder = item => ['answer', 'solution', 'sol', 'exp'].some(key => /^(?:TODO|TBD|coming soon|answer pending|solution pending|not yet (?:available|implemented)|solution will be added)[.!\s]*$/i.test(text(item[key])));
const sum = values => values.reduce((total, value) => total + value, 0);
const countValues = values => values.reduce((counts, value) => {
  const key = String(value ?? 'unspecified');
  counts[key] = (counts[key] || 0) + 1;
  return counts;
}, {});
const compact = (item, unit, exercise) => ({
  unit, exercise, id: item.id, number: item.qNo || item.num,
  question: item.question || item.problem || item.q,
  answer: item.answer || item.sol,
  solutionStatus: item.solutionStatus,
  sourceStatus: item.sourceStatus,
  sourceReferences: item.sourceReferences || []
});
const emptyClassification = {
  'ex-2-6': 'Duplicate empty Review Exercise 2 shell; ex-2-5 contains the 15 active review MCQs.',
  'ex-6-5': 'Real source gap: Exercise 6.1 questions lie in missing printed pages 142–157. Printed answer-key context survives, but does not recover the questions.',
  'ex-7-3': 'Unnumbered empty parser shell titled Exercise. Numbered 7.1–7.4 and Review Exercise 7 are represented elsewhere.'
};

const perUnit = units.map(unit => {
  const exercises = unit.exercises || [];
  const records = exercises.flatMap(exercise => (exercise.problems || []).map(item => ({ exercise, item })));
  // Final repaired review exercises consist of individual MCQs. Source choices
  // are either embedded in question text or in sourceQuestionBlocks, not in
  // the separate interactive SLO MCQ schema.
  const review = records.filter(({ exercise }) => /^Review Exercise\b/.test(exercise.title));
  const mcqs = unit.slos?.mcqs || [];
  const short = unit.slos?.shortQuestions || [];
  const long = unit.slos?.longQuestions || [];
  const examples = unit.workedExamples || [];
  return {
    unit: unit.number, title: unit.title,
    sectionCount: (unit.sections || []).length,
    workedExampleCount: examples.length,
    workedExamplesMissingAnswerContent: examples.filter(item => !answered(item)).map(item => compact(item, unit.number)),
    exerciseContainers: exercises.length,
    activeExerciseProblemGroups: records.length,
    sourceReferencedExerciseProblemGroups: records.filter(({ item }) => item.sourceReferences?.length).length,
    exerciseProblemGroupsWithAnswerContent: records.filter(({ item }) => answered(item)).length,
    exerciseProblemGroupsWithoutAnswerContent: records.filter(({ item }) => !answered(item)).map(({ exercise, item }) => compact(item, unit.number, exercise.title)),
    literalAnswerPlaceholders: records.filter(({ item }) => placeholder(item)).map(({ exercise, item }) => compact(item, unit.number, exercise.title)),
    exerciseInventory: exercises.map(exercise => ({ id: exercise.id, title: exercise.title, problemGroups: (exercise.problems || []).length })),
    emptyExerciseContainers: exercises.filter(exercise => !exercise.problems?.length).map(exercise => ({ id: exercise.id, title: exercise.title, classification: emptyClassification[exercise.id] || 'Requires source review.' })),
    embeddedSourceReviewMcqs: {
      count: review.length,
      withAnswer: review.filter(({ item }) => answered(item)).length,
      withExplanation: review.filter(({ item }) => explained(item)).length,
      withInteractiveCorrectIndex: review.filter(({ item }) => Number.isInteger(item.correct) && Array.isArray(item.options) && item.correct >= 0 && item.correct < item.options.length).length,
      sourceOptionCaveats: review.filter(({ item }) => /no (?:\w+\s+)*correct|also|both|intended|closest|assuming|interpreting/i.test(text(item.answer))).map(({ exercise, item }) => compact(item, unit.number, exercise.title))
    },
    supplementalSlo: {
      mcqs: mcqs.length,
      mcqsWithValidCorrectIndex: mcqs.filter(item => Number.isInteger(item.correct) && Array.isArray(item.options) && item.correct >= 0 && item.correct < item.options.length).length,
      mcqsWithExplanation: mcqs.filter(item => text(item.exp)).length,
      shortQuestions: short.length,
      shortQuestionsWithAnswer: short.filter(answered).length,
      longQuestions: long.length,
      longQuestionsWithAnswer: long.filter(answered).length
    },
    explicitPartialRecords: records.filter(({ item }) => /partial|pending|unverified|uncertified|under_specified/i.test([item.solutionStatus, item.sourceStatus].filter(Boolean).join(' '))).map(({ exercise, item }) => compact(item, unit.number, exercise.title)),
    sourceGap: unit.sourceGap || null,
    archivedRecordsExcluded: {
      problemGroups: sum(exercises.map(exercise => exercise.unreviewedProblems?.length || 0)),
      replacedProblemSnapshots: records.filter(({ item }) => item.unreviewedSolution).length,
      duplicateWorkedExamples: unit.unreviewedDuplicateExamples?.length || 0,
      unreviewedExerciseContainers: unit.unreviewedExercises?.length || 0,
      unreviewedExerciseProblemGroups: sum((unit.unreviewedExercises || []).map(exercise => exercise.problems?.length || 0))
    }
  };
});

const report = {
  generatedAt: new Date().toISOString(),
  scope: 'Class 12 Mathematics only. No content or UI changes.',
  auditType: 'Evaluated data-schema coverage; not a new mathematical correctness or source-visual verification.',
  countingRules: [
    'Only final evaluated active arrays are counted. Appended repair code supersedes old baseline data.',
    'An exercise record may contain multiple lettered subparts; counts are question groups, not subpart totals.',
    'A nonempty answer/solution/steps field proves answer presence, not correctness or source completeness.',
    'Source review MCQs embedded in exercises are separate from supplemental SLO MCQs.',
    'unreviewedProblems, unreviewedSolution, unreviewedDuplicateExamples and unreviewedExercises are archival parser/replacement material and are excluded from active question totals.',
    'Empty arrays in math_12_book_data.js are book metadata scaffolding; do not treat them as missing active answers.'
  ],
  inputs: ['js/math_12_data.js', 'js/math_12_book_data.js', 'docs/source-verification/math12.json'].map(relative => {
    const bytes = fs.readFileSync(path.join(root, relative));
    return { path: relative, bytes: bytes.length, sha256: crypto.createHash('sha256').update(bytes).digest('hex') };
  }),
  totals: {
    units: perUnit.length,
    workedExamples: sum(perUnit.map(unit => unit.workedExampleCount)),
    workedExamplesMissingAnswerContent: sum(perUnit.map(unit => unit.workedExamplesMissingAnswerContent.length)),
    exerciseProblemGroups: sum(perUnit.map(unit => unit.activeExerciseProblemGroups)),
    exerciseProblemGroupsWithAnswerContent: sum(perUnit.map(unit => unit.exerciseProblemGroupsWithAnswerContent)),
    exerciseProblemGroupsWithoutAnswerContent: sum(perUnit.map(unit => unit.exerciseProblemGroupsWithoutAnswerContent.length)),
    literalAnswerPlaceholders: sum(perUnit.map(unit => unit.literalAnswerPlaceholders.length)),
    embeddedSourceReviewMcqs: sum(perUnit.map(unit => unit.embeddedSourceReviewMcqs.count)),
    embeddedSourceReviewMcqsWithAnswer: sum(perUnit.map(unit => unit.embeddedSourceReviewMcqs.withAnswer)),
    embeddedSourceReviewMcqsWithExplanation: sum(perUnit.map(unit => unit.embeddedSourceReviewMcqs.withExplanation)),
    supplementalMcqs: sum(perUnit.map(unit => unit.supplementalSlo.mcqs)),
    supplementalMcqsWithValidCorrectIndex: sum(perUnit.map(unit => unit.supplementalSlo.mcqsWithValidCorrectIndex)),
    supplementalMcqsWithExplanation: sum(perUnit.map(unit => unit.supplementalSlo.mcqsWithExplanation)),
    supplementalShortQuestions: sum(perUnit.map(unit => unit.supplementalSlo.shortQuestions)),
    supplementalLongQuestions: sum(perUnit.map(unit => unit.supplementalSlo.longQuestions)),
    explicitPartialRecords: sum(perUnit.map(unit => unit.explicitPartialRecords.length)),
    emptyExerciseContainers: sum(perUnit.map(unit => unit.emptyExerciseContainers.length)),
    archivedProblemGroups: sum(perUnit.map(unit => unit.archivedRecordsExcluded.problemGroups)),
    archivedDuplicateWorkedExamples: sum(perUnit.map(unit => unit.archivedRecordsExcluded.duplicateWorkedExamples)),
    archivedExerciseContainers: sum(perUnit.map(unit => unit.archivedRecordsExcluded.unreviewedExerciseContainers))
  },
  firstConcreteGaps: [
    { priority: 1, unit: 1, area: 'Translation coverage', detail: 'Existing progress records only 47 passages, 82 sentences and 418 word meanings across the Unit 1 introduction/environment/basic commands. Remaining source and learning material is pending.' },
    { priority: 2, unit: 2, id: 'ex-2-1-q5', area: 'Source-dependent answer', detail: 'Photographic project horizontal endpoints remain uncertified; visible range estimates are supplied but exact domains are unresolved.' },
    { priority: 3, unit: 2, id: 'ex-2-3-project', area: 'Source legibility', detail: 'The first photographed roof model coefficients remain unclear. A qualified function-type answer exists; an exact algebraic model cannot be asserted.' },
    { priority: 4, unit: 6, id: 'ex-6-5', area: 'Missing source pages', detail: 'Printed pages 142–157 are absent from supplied formats. Source-complete opening, early examples and Exercise 6.1 require an additional source; existing answer-key fragments do not recover exact questions.' },
    { priority: 5, unit: 10, id: 'ex-10-1-q2', area: 'Source legibility', detail: 'Part (c) has an uncertified exponent. Its readable function has been differentiated conditionally, and part (d) is explicitly identified as inconsistent.' },
    { priority: 6, unit: 12, id: 'ex-12-2-q5', area: 'Under-specified printed question', detail: 'The source omits the integrand. A worked supplemental sample is supplied and labelled; no unique original numerical answer exists.' },
    { priority: 7, area: 'Quiz presentation', detail: '101 source review MCQs have prose answers/explanations in exercises but no options/correct index schema. If converting them to interactive quizzes, preserve cases with multiple or no valid printed choices.' }
  ],
  bookMetadata: { units: book.length, workedExamples: sum(book.map(unit => unit.workedExamples?.length || 0)), exerciseContainers: sum(book.map(unit => unit.exercises?.length || 0)) },
  savedSourceProgress: {
    bookStatus: progress.bookStatus,
    nextSource: progress.nextSource,
    pendingWork: progress.pendingWork,
    sourceCount: progress.sourceCount,
    pageEntries: progress.pages?.length,
    completePageEntries: (progress.pages || []).filter(page => page.pageComplete === true).length,
    textStatuses: countValues((progress.pages || []).map(page => page.textStatus)),
    translationStatuses: countValues((progress.pages || []).map(page => page.translationStatus)),
    translationCoverage: progress.translationCoverage,
    sourceGaps: progress.sourceGaps || [],
    unresolvedIssueDescriptions: progress.issues || []
  },
  perUnit
};
const output = path.join(root, 'docs/source-verification/class-12/math12-answer-audit.json');
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(output, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ output, totals: report.totals, perUnit: perUnit.map(unit => ({ unit: unit.unit, exercises: unit.activeExerciseProblemGroups, sourceMcqs: unit.embeddedSourceReviewMcqs.count, workedExamples: unit.workedExampleCount, partial: unit.explicitPartialRecords.length })) }, null, 2));
