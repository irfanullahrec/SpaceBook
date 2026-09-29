# 02 — Functions & Components Reference

This document provides a comprehensive function-by-function reference for `js/app.js`.

---

## 1. Top-Level Navigation & Page Routing

### `renderPage(page)`
- **Purpose**: Master switcher between the 5 primary tabs of the application (`home`, `subjects`, `books`, `roadmap`, `study-plan`).
- **Signature**: `renderPage(page: string): void`
- **Behavior**: Calls the corresponding specialized page renderer and updates navigation UI states.

### `renderHome()`
- **Purpose**: Generates the modern student analytics dashboard.
- **Components**:
  - Daily & weekly question goal tracker.
  - Interactive activity bar charts.
  - Distinction / Progress performance badges.
  - Quick-start class portal cards (Class 9, 10, 11, 12).
  - Subject quick launch tiles with direct chapter jumping.

### `renderClasses()`
- **Purpose**: Displays the class selection directory.
- **Design Structure**:
  - Features the consolidated `.subjects-single-line-bar` next to the Back icon.
  - Top 3-card overview grid (4 Grades, 25 Core Subjects, 10,000+ Questions).
  - Grade cards grid navigating to `goToSubjects(classId)`.

### `goToSubjects(classId)`
- **Purpose**: Displays all subjects enrolled under a specific academic grade.
- **Key Enhancements**:
  1. **Single-Line Header**: Merges `← Back to All Classes`, breadcrumbs `Home › Subjects › Class 9`, title `📚 Class 9 — Subjects`, subtitle, and KPK Board badge into a single horizontal bar.
  2. **Class Overview Statistical Cards**: Renders 3 cards strictly in one row (`grid-template-columns: repeat(3, 1fr)`) showing Core Subjects, Total Units, and Solved Question Banks.
  3. **Rich Statistical Subject Cards**: Displays each subject with 3-metric statistics (Sections, Solved Qs, Exam SLOs), syllabus highlight tags, Urdu title, and verified badges.

### `openSubject(classId, subjId)`
- **Purpose**: Routes the user to the appropriate subject viewer engine:
  - `hasBio` or `cls9-bio` ➔ `openBioView(classId, subj)`
  - `hasChem` or `cls9-chem` ➔ `openChemView(classId, subj)`
  - `hasPhys` or `cls9-phy` ➔ `openPhysView(classId, subj)`
  - `hasEng` or `cls9-eng` ➔ `openEngView(classId, subj)`
  - `hasUrdu` or `cls9-urdu` ➔ `openUrduView(classId, subj)`
  - `hasMath` or `cls9-math` ➔ `openMathView(classId, subj)`
  - `hasPakStudy` or `cls9-pakstudy` ➔ `openPakStudyView(classId, subj)`
  - Generic subjects ➔ `openGenericSubjectView(classId, subj)`

---

## 2. Biology Subject Suite (`BIO_DATA`)

### `getBioChapterList(classId)`
- Returns `BIO_DATA` (Units 1–9) for Class 9 or `DATA.bio10Chapters` for Class 10.

### `openBioView(classId, subj)`
- Initializes Biology portal state: active unit, active tab (`sections`, `summary`, `exercise`, `slo`, `practicals`).
- Renders unit sidebar selector, PDF download button, top unit statistics (max 3 per row), and the 5-tab suite.

### `setBioTab(tabKey)` & `setBioSloTab(sloKey)` & `setBioExPart(partKey)`
- Smoothly switches between lesson tabs, SLO categories (`slo-mcqs`, `slo-sqs`, `slo-lqs`), or exercise parts (`mcqs`, `sqs`, `lqs`, `activities`).
- Auto-scrolls into view using `autoScrollToActiveTab`.

### Section Accordion Functions
- `renderBioSectionCard(sec, index)`: Renders section card with number badge, title, Urdu name pill, and toggle arrow. Collapsed by default.
- `toggleBioSecAccordion(index)`: Toggles open/close state of an individual section card.
- `expandAllBioSections()` / `collapseAllBioSections()`: Instant global expansion/collapse.

### `checkBioExMcq(qIndex, selectedOpt, correctOpt, encodedExp)`
- Evaluates student MCQ selection, turns selected button green/red, locks remaining choices, records performance statistics, and renders pedagogical rationale.

---

## 3. Chemistry Subject Suite (`DATA.chemChapters`)

### `openChemView(classId, subj)`
- Renders official KPK Chemistry portal (Units 1–8).
- Includes 7 distinct unit tabs: Topics Accordions, Solved Numericals, Solved Exercises, SLO Exam Bank, Vocabulary Bank, Key Formulas, and Practical Experiments.

### `renderChemVocabulary(ch, chIdx)` & `filterChemUnitVocab(query, unitNum)`
- Displays searchable vocabulary terms for chemistry with letter-by-letter alphabetic filtering and instant pronunciation.

---

## 4. Mathematics Subject Suite (`MATH_DATA`)

### `openMathView(classId, subj)`
- Full 17-unit portal for Grade 9 Mathematics.
- Tabs: Complete Theory & Methods, Worked Examples, Solved Exercises & Reviews, SLO Bank, and Formulas / Theorems Summary Sheet.

### `selectMathMcqOption(qIdx, optIdx, correctIdx, expEncoded)`
- Verifies mathematical multiple-choice problems with step-by-step reasoning.

---

## 5. Pakistan Studies Subject Suite (`PAKSTUDY_DATA`)

### `openPakStudyView(classId, subj)`
- Features Nastaleeq Urdu typography and RTL orientation.
- 5 Tabs: تفصیلی درسی اسباق (Verbatim Sections), اہم نکات (Key Points), مکمل مشقی سوالات (Solved Exercises), ایس ایل او امتحانی بینک (SLO Bank), and تاریخی سنگ میل (Historical Timeline).

### `renderPakStudyTimeline(ch)`
- Displays interactive chronological historical timeline cards with dates, badges, and significant historical milestones.

---

## 6. English Suite & Interactive Lexicon

### `showWordLookupPopover(wordText, targetEl, event)`
- Triggered when any student clicks on an English word in reading passages, exercises, or scientific notes.
- Queries `DICTIONARY_DATA` for exact Urdu and Pashto meanings.
- Supports asynchronous fallback to online translation if not found in local cache.
- Renders audio button triggering `playSingleWordTTS(word)`.

### `getWordAtPoint(x, y)`
- Uses `document.caretRangeFromPoint` / `caretPositionFromPoint` to detect exact word under the cursor without requiring individual span wrappers on every word.

---

## 7. Urdu Suite & Dual-Voice TTS Engine

### `openUrduView(classId, subj)`
- Renders 15 Grade 9 Urdu lessons across Hissa Nasar (نثر), Hissa Nazam (نظم), and Hissa Ghazal (غزل).
- Includes Tashreehat (تشریحات), Khulasa (خلاصہ), and exercise question models.

### `startUrduTts(prefix, gender)` / `pauseUrduTts()` / `stopUrduTts()`
- High-performance speech synthesis engine supporting synchronized karaoke-style word highlighting in Urdu Nastaleeq text.
- Supports Male and Female natural voices with adjustable speech playback rate.
