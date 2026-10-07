# 03 — Curriculum Datasets & Subjects Reference

This document outlines the data schema, textbook alignment, and scope for every subject dataset in SpaceBook.

---

## 1. Grade 9 Subject Overview Table

| Subject | Data File | Global Variable | Units / Lessons | Scope & Verbatim Status | Exercises & Solutions | Exam SLO Suite |
|---|---|---|---|---|---|---|
| **Biology** *(حیاتیات)* | `js/bio_data.js` | `BIO_DATA` | 9 Units | 56 Sections (100% Verbatim KPK Textbook) | 90 MCQs, 45 SQs, 29 LQs | 90 MCQs, 54 SQs, 18 LQs, 9 Practicals |
| **Chemistry** *(کیمسٹری)* | `js/data_chem.js` | `DATA.chemChapters` | 8 Units | Full Core Theory (100% Verbatim KPK Textbook) | 80+ MCQs, 75+ SQs & LQs | Solved Numericals & Key Reactions |
| **Mathematics** *(ریاضی)* | `js/math_data.js` | `MATH_DATA` | 17 Units | 88 Sections (100% Verbatim KPK Textbook) | 747+ Solved Problems, 68 Exercise Subtabs | 345+ Theorems & Worked Examples |
| **Pakistan Studies** *(مطالعہ پاکستان)* | `js/pakstudy_data.js` | `PAKSTUDY_DATA` | 4 Units | 27 Sections (100% Verbatim Nastaleeq Text) | 40 MCQs, 36 SQs, 24 LQs | 40 SLO MCQs, 24 SQs, 8 LQs, 54 Timeline Milestones |
| **English** *(انگریزی لازمی)* | `js/english_data.js` (+ `js/data_eng.js`) | `ENGLISH_DATA` / `DATA.engChapters` | 15 Units | Prose & Poems with Trilingual Translations | Complete Textbook Exercises & Writing | 300 MCQs, 150 SQs, 75 LQs, 4,000+ Word Lexicon |
| **Urdu** *(اردو لازمی)* | `js/urdu_data.js` | `URDU_DATA` | 15 Units | Hissa Nasar, Nazam & Ghazal with Tashreeh | Complete Mashqi Sawalat & Grammars | Dual-Voice Karaoke-Style Audio TTS |
| **Physics** *(طبیعیات)* | `js/data_phys.js` | `DATA.physChapters` | 9 Units | Physical Quantities to Thermal Properties | Solved End-of-Chapter MCQs & Review Qs | Step-by-Step Solved Numericals |
| **Islamyat** *(اسلامیات — کلاس ٩)* | `js/islamyat_data.js` | `ISLAMYAT_DATA` / `DATA.islamyatChapters` | 15 Units | Uthmani Ayaat, trilingual translations & SLO Q&A | Solved exercises, lughat & tashreeh | SLO MCQs, SQs, LQs per unit |
| **Islamyat** *(اسلامیات — کلاس ١٠)* | `js/islamyat_10_data.js` | `ISLAMYAT_10_DATA` / `DATA.islamyat10Chapters` | 18 Units | Uthmani Ayaat, trilingual translations & SLO Q&A | Solved exercises, lughat & tashreeh | SLO MCQs, SQs, LQs per unit |
| **Computer Science** | *(no dataset yet)* | generic fallback | 8 Units | Computer Fundamentals, OS, Data Comm, Security | Solved MCQs & Review Short Questions | Practical Lab Commands & Logic |

> **File ownership:** every subject above lives in its own file (or its own
> `js/data_<subject>.js` slice of the core registry), so contributors editing
> different subjects never touch the same lines. See
> [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the ownership table and the
> merge/rebase rules. `node tools/validate.js` fails if a dataset file is
> missing, unloadable, or out of its expected size.

---

## 2. Dataset Schemas

### Biology (`BIO_DATA`)
```typescript
interface BioUnit {
  number: number;
  id: string;
  title: string;
  titleUrdu: string;
  pageRange: string;
  sections: Array<{
    id: string;
    num: string;
    title: string;
    titleUrdu: string;
    paragraphs: string[];
    callouts?: Array<{
      type: "scientific" | "ponder" | "society" | "activity";
      title: string;
      text: string;
    }>;
    quranVerses?: Array<{
      arabic: string;
      translation: string;
      surah: string;
    }>;
  }>;
  keyPoints: Array<{ num: number; text: string }>;
  exercise: {
    mcqs: Array<{ q: string; options: string[]; correct: number; exp: string }>;
    shortQuestions: Array<{ q: string; a: string }>;
    longQuestions: Array<{ q: string; a: string }>;
    activities?: Array<{ title: string; desc: string }>;
  };
  sloBank: {
    mcqs: Array<{ q: string; options: string[]; correct: number; cognitiveLevel: string; exp: string }>;
    sqs: Array<{ q: string; a: string; cognitiveLevel: string }>;
    lqs: Array<{ q: string; a: string; cognitiveLevel: string }>;
  };
  practicals: Array<{
    title: string;
    apparatus: string;
    procedure: string[];
    observation: string;
    precautions: string[];
  }>;
}
```

### Mathematics (`MATH_DATA`)
```typescript
interface MathUnit {
  number: number;
  id: string;
  title: string;
  titleUrdu: string;
  pageRange: string;
  badge: string;
  description: string;
  sections: Array<{
    id: string;
    title: string;
    theory: string;
    rules: string[];
  }>;
  examples: Array<{
    num: string;
    title: string;
    statement: string;
    solution: string[];
  }>;
  exercises: Array<{
    id: string;
    name: string;
    problems: Array<{
      qNum: string;
      statement: string;
      steps: string[];
      answer: string;
    }>;
  }>;
  reviewExercise: {
    mcqs: Array<{ q: string; options: string[]; correct: number; exp: string }>;
  };
}
```

### Pakistan Studies (`PAKSTUDY_DATA`)
```typescript
interface PakStudyChapter {
  number: number;
  id: string;
  title: string;
  titleEn: string;
  pageRange: string;
  badge: string;
  description: string;
  introQuranHadith?: Array<{
    arabic: string;
    translation: string;
    reference: string;
  }>;
  sections: Array<{
    id: string;
    title: string;
    content: string;
  }>;
  keyPoints: string[];
  exercise: {
    mcqs: Array<{ q: string; options: string[]; correct: number; exp: string }>;
    shortQuestions: Array<{ q: string; a: string }>;
    longQuestions: Array<{ q: string; a: string }>;
  };
  sloBank: {
    mcqs: Array<{ q: string; options: string[]; correct: number; cognitiveLevel: string; exp: string }>;
    sqs: Array<{ q: string; a: string; cognitiveLevel: string }>;
    lqs: Array<{ q: string; a: string; cognitiveLevel: string }>;
  };
  };\n  timeline?: Array<{\n    year: string;\n    date: string;\n    event: string;\n    significance: string;\n  }>;\n}\n```

---

## 6. Mathematics Dataset — Formatting Conventions

> [!IMPORTANT]
> All math datasets (`js/math_data.js`, `js/math_10_data.js`, `js/math_12_data.js`, etc.) use a **custom inline math syntax** rendered by `appendMathInlineText()` in `js/app.js`. Do NOT use standard KaTeX/MathJax — use the formats below.

### 6.1 Inline Math Syntax (string values in the dataset)

| What you want | Write in the JS string |
|---|---|
| Fraction p/q | `\frac{p}{q}` |
| Square root of x | `\sqrt{x}` |
| nth root of x | `\sqrt[n]{x}` |
| Superscript (power) | `x^{2}` or `x^{2+n}` |
| Subscript | `x_{1}` |
| Overline (mean) | `\bar{x}` or `\overline{x}` |
| Multiplication × | `\times` |
| Division ÷ | `\div` |
| Plus-minus ± | `\pm` |
| Dot product · | `\cdot` |
| Less-than-or-equal ≤ | `\leq` |
| Greater-than-or-equal ≥ | `\geq` |
| Not equal ≠ | `\neq` |
| Arrow → | `\to` or `→` (Unicode directly) |
| Infinity ∞ | `\infty` or `∞` |
| pi π | `\pi` or `π` |
| Real numbers ℝ | `\mathbb{R}` |
| Integers ℤ | `\mathbb{Z}` |
| Rationals ℚ | `\mathbb{Q}` |
| Line break in text | `\\` |

**You may also embed Unicode characters directly** in string values: `²`, `³`, `√`, `∈`, `∉`, `≠`, `≤`, `≥`, `→`, `π`, `∞`, `ℤ`, `ℝ`, `ℚ`, `ℕ` — the renderer accepts both.

Example:
```js
problem: "Find the roots of x^{2} - 5x + 6 = 0 using the quadratic formula: x = \\frac{-b \\pm \\sqrt{b^{2} - 4ac}}{2a}",
answer: "x = 2 or x = 3"
```

### 6.2 Matrix Notation

Matrices are written using double-bracket JSON notation directly inside any string field:

```
[[a, b], [c, d]]          → 2×2 matrix
[[a, b, c], [d, e, f]]    → 2×3 matrix
```

The renderer (`typesetMathTextNode`) automatically converts this to a properly typeset matrix with brackets.

### 6.3 Diagram Objects

Each `workedExample` or `exercise` item may include a `diagram` property. The `diagram.type` determines which SVG figure is rendered by `renderMathDiagram()`.

**Unit 1 (Algebra/Quadratics):**
```js
diagram: { type: "quadratic-graph", a: 1, b: -5, c: 6, xMin: -1, xMax: 6, yMin: -2, yMax: 8, xLabel: "x", yLabel: "y", points: [{x:2, y:0, label:"(2,0)"}, {x:3, y:0, label:"(3,0)"}] }
diagram: { type: "completing-square", coefficient: 6 }
diagram: { type: "rectangle-frame", outerWidth: 11, outerHeight: 6, frameWidth: "x" }
```

**Unit 2 (Polynomials):**
```js
diagram: { type: "rectangle-area", length: "2x+3", width: "x+1", area: "2x²+5x+3" }
diagram: { type: "right-triangle", base: "a", height: "b", hypotenuse: "c" }
diagram: { type: "synthetic-division", root: 2, coefficients: [1,-5,6,0], products: [null,2,-6,0], bottom: [1,-3,0,0] }
```

**Unit 6 (Statistics):**
```js
diagram: { type: "frequency-table", title: "...", headers: ["Class", "Frequency"], rows: [[...],[...]] }
diagram: { type: "histogram", bars: [{lower:0, upper:10, frequency:5}, ...], xLabel: "Marks", yLabel: "Frequency" }
diagram: { type: "frequency-polygon", points: [[5,5],[15,12],...], xLabel: "Marks", yLabel: "Frequency" }
diagram: { type: "ogive", points: [[10,5],[20,17],...] }
diagram: { type: "mode-histogram", bars: [...], mode: 25 }
diagram: { type: "graphical-summary", bars: [...], points: [...], q1: 22, q3: 36 }
diagram: { type: "category-bars", labels: ["A","B","C"], values: [5,12,8] }
```

**Unit 7 (Trigonometry):**
```js
diagram: { type: "sector", angle: "π/3", radius: "r", title: "Circular sector" }
diagram: { type: "unit-circle", angle: 45, x: "cos θ", y: "sin θ" }
diagram: { type: "quadrants", quadrant: 2 }
diagram: { type: "right-triangle", opposite: "a", adjacent: "b", hypotenuse: "c", angle: "θ" }
diagram: { type: "elevation", distance: "d", height: "h", angle: "θ", title: "Angle of elevation" }
```

**Units 8–17 (Geometry):**
```js
diagram: { type: "right-triangle", title: "Triangle with altitude" }
diagram: { type: "circle-chord", radius: 5, distance: 3, chord: 8, title: "Chord bisector theorem" }
diagram: { type: "tangent", title: "Tangent from an external point" }
diagram: { type: "pair-circles", title: "Two circles touching internally" }
diagram: { type: "sector", angle: "60°", radius: "r" }
```

### 6.4 Data File Structure

Each unit in a math dataset follows this schema:

```js
{
  id: "unit-1",
  number: 1,
  title: "Quadratic Equations",
  titleUrdu: "دو درجی مساوات",
  sections: [
    {
      id: "sec-1-1",
      title: "1.1 Introduction",
      theory: "Full verbatim textbook text. Use \\frac{}{} for fractions, \\sqrt{} for roots.",
      rules: ["Rule 1 text", "Rule 2 text"],          // optional
      examples: ["Example 1 text"],                    // optional
      keyPoints: ["Key point 1"]                       // optional
    }
  ],
  workedExamples: [
    {
      id: "we-1-1",
      num: "1.1",
      title: "Example 1.1",
      problem: "Solve x^{2} - 7x + 12 = 0 by factorization.",
      steps: [
        "Step 1: ...",
        "Step 2: ..."
      ],
      answer: "x = 3 or x = 4",
      diagram: { type: "quadratic-graph", ... }     // optional
    }
  ],
  exercises: [
    {
      id: "ex-1-1",
      title: "Exercise 1.1",
      problems: [
        {
          id: "ex-1-1-q1",
          qNo: "1",
          question: "Solve x^{2} - 5x + 6 = 0.",
          solution: "By factoring: (x-2)(x-3)=0, so x=2 or x=3.",
          diagram: { type: "quadratic-graph", ... }  // optional
        }
      ]
    }
  ]
}
```

