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
  timeline?: Array<{
    year: string;
    date: string;
    event: string;
    significance: string;
  }>;
}
```
