# 05 — Strategy & Future Roadmap

This document outlines the strategic engineering roadmap and content expansion plan for SpaceBook.

---

## 1. Strategic Goals & Vision

### Phase 1: Grade 9 Curriculum Completion & Hardening (Completed ✅)
- **All 8 Core Subjects Completed**:
  - Biology (9 Units, 56 Sections, 164 Solved Qs, 162 SLO Bank, 9 Practicals).
  - Chemistry (8 Units, Full Solved Numericals & Exercises, Vocabulary Bank).
  - Mathematics (17 Units, 88 Sections, 345 Examples/Theorems, 747 Problems).
  - Pakistan Studies (4 Chapters, 27 Sections, 100 Solved Qs, 20 Milestones).
  - English (15 Units, Full Trilingual Translations, 4,000+ Word Lexicon).
  - Urdu (15 Units, Tashreehat, Khulasa, Dual-Voice TTS Narration).
  - Physics & Computer Science (Core Theory, Review Exercises, Lab Experiments).
- **Architecture Standardization**:
  - Single-line consolidated headers.
  - Strict limit of 3 statistical cards per row.
  - All topic sections ("عنوان") collapsed by default.
  - Bilingual / Trilingual interactive tooltips.

---

### Phase 2: Grade 10 Verbatim Overhaul (In Progress 🚀)
Following the exact structural success of Grade 9, Grade 10 will undergo 100% textbook matching:
1. **Grade 10 Biology (Units 10–18)**:
   - Gaseous Exchange, Homeostasis, Coordination & Control, Support & Movement, Reproduction, Inheritance, Man & His Environment, Biotechnology, Pharmacology.
2. **Grade 10 Chemistry (Units 9–16)**:
   - Chemical Equilibrium, Acids, Bases & Salts, Organic Chemistry, Hydrocarbons, Biochemistry, Environmental Chemistry I (Atmosphere), Environmental Chemistry II (Water), Chemical Industries.
3. **Grade 10 Mathematics (Units 1–13)**:
   - Quadratic Equations, Theory of Quadratic Equations, Variations, Partial Fractions, Sets & Functions, Basic Statistics, Introduction to Trigonometry, Projection of a Side of a Triangle, Chords of a Circle, Tangent to a Circle, Chords & Arcs, Angle in a Segment of a Circle, Practical Geometry (Circles).
4. **Grade 10 Pakistan Studies & Languages**:
   - Post-1971 History, Constitution, Foreign Policy, Economy, Society, Culture.

---

### Phase 3: Higher Secondary (Grade 11 & 12 HSSC / F.Sc)
- Pre-Medical Group: F.Sc Biology, Chemistry, Physics.
- Pre-Engineering Group: F.Sc Mathematics, Chemistry, Physics.
- Computer Science Group: F.Sc Computer Science, Mathematics, Physics.
- Full ETEA / MDCAT / NUMS Entry Test preparation question banks aligned with KPK board textbooks.

---

## 2. Technical Roadmap & Architectural Initiatives

### A. Progressive Web App (PWA) & Offline-First Capability
- **Goal**: Enable students in remote or low-connectivity regions across Khyber Pakhtunkhwa to use the entire portal offline without active internet.
- **Implementation**:
  - Register a lightweight `service-worker.js`.
  - Cache static assets (`style.css`, fonts, JavaScript curriculum data).
  - Use `IndexedDB` to store student test attempts, bookmarks, and custom notes locally.

### B. Automated Cross-Platform Sync with Android App (`SpaceBook App/`)
- Maintain a single JSON source of truth in `js/` that can be automatically compiled into Kotlin data classes or SQLite/Room asset bundles for the Android application.
- Continuous integration scripts to verify parity between web views and native Android Compose screens.

### C. Automated Continuous Integration (CI) Verification Suite
- Script `test_all_subjects.js` runs automatically on pre-commit/pre-push hooks to verify:
  1. Syntax validation (`node -c`) on all JS files.
  2. Data integrity check: ensures all units have titles, sections, and exercises.
  3. DOM render verification: confirms every subject view renders valid HTML.
