# 01 — Project Structure & Architecture

## 1. Overview & Vision
SpaceBook is an educational portal engineered for secondary and higher secondary students studying under the **Khyber Pakhtunkhwa (KPK) Textbook Board, Peshawar** syllabus. Its core mission is to provide 100% textbook-matched, verified, interactive study content that empowers students to excel in their annual board examinations and SLO (Student Learning Outcomes) assessments.

---

## 2. Directory Hierarchy

```
D:\SpaceBook/                         # git repository root
├── .gitattributes                    # LF for every text file, binary assets excluded
├── .gitignore
│
├── SpaceBook Web/                    # Web application (the product)
│   ├── index.html                    # SPA entry — script load order lives here
│   ├── CONTRIBUTING.md               # file ownership table + merge/rebase rules
│   ├── css/
│   │   └── style.css                 # Master styling, themes, animations, responsive grids
│   ├── js/
│   │   ├── app.js                    # Controller: routers, tab switches, audio engine, renderers
│   │   │
│   │   │                             # ── core registry (SHARED, append-only) ──
│   │   ├── data.js                   # stats, classes, subjects, books, studyPlan, roadmap map
│   │   │
│   │   │                             # ── one data file per subject owner ──
│   │   ├── data_chem.js              # DATA.chemChapters / DATA.chem10Chapters
│   │   ├── data_phys.js              # DATA.physChapters / DATA.phys10Chapters
│   │   ├── data_eng.js               # DATA.engChapters  / DATA.eng10Chapters
│   │   ├── data_bio.js               # DATA.bioChapters  / DATA.bio10Chapters
│   │   ├── bio_data.js               # BIO_DATA        — Grade 9 Biology (Units 1–9)
│   │   ├── math_data.js              # MATH_DATA       — Grade 9 Mathematics (Units 1–17)
│   │   ├── pakstudy_data.js          # PAKSTUDY_DATA   — Grade 9 Pakistan Studies (Chapters 1–4)
│   │   ├── english_data.js           # ENGLISH_DATA    — Grade 9/10 English (Units 1–15)
│   │   ├── urdu_data.js              # URDU_DATA       — Grade 9 Urdu (Units 1–15)
│   │   ├── islamyat_data.js          # ISLAMYAT_DATA   — Grade 9 Islamyat (15 units)
│   │   ├── islamyat_10_data.js       # ISLAMYAT_10_DATA — Grade 10 Islamyat (18 units)
│   │   └── dictionary_data.js        # 4,000+ word English-Urdu-Pashto lexicon
│   │
│   ├── tools/
│   │   ├── validate.js               # pre-push gate: syntax, datasets, wiring, css balance
│   │   └── smoke.js                  # 51 UI smoke tests (every subject/tab/search path)
│   │
│   ├── docs/                         # Architecture & strategy documentation
│   │   ├── INDEX.md
│   │   ├── 01_PROJECT_STRUCTURE_AND_ARCHITECTURE.md
│   │   ├── 02_FUNCTIONS_AND_COMPONENTS_REFERENCE.md
│   │   ├── 03_CURRICULUM_DATASETS_AND_SUBJECTS.md
│   │   ├── 04_UI_UX_AND_PEDAGOGICAL_STRATEGY.md
│   │   └── 05_STRATEGY_AND_FUTURE_ROADMAP.md
│   │
│   └── kotlin/PhysChapters.kt        # shared sample of the Kotlin data model
│
├── SpaceBook App/                    # Native Android application (Kotlin + Jetpack Compose)
│   ├── app/
│   │   ├── src/main/java/...         # Compose screens, viewmodels, theme, local databases
│   │   ├── src/main/assets/          # Bundled curriculum assets
│   │   └── build.gradle.kts
│   └── build.gradle.kts
│
└── assets/
    └── books/                        # Downloadable official textbook PDFs (Class 9 & 10)
```

### Contribution model

Content is split **one file per subject** so several contributors can work in
parallel: two people editing `data_chem.js` and `data_phys.js` never collide.
The four shared files (`data.js`, `app.js`, `style.css`, `index.html`) are
append-only by convention, which lets git auto-merge their edits line-by-line.
See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the ownership table, the
rebase workflow, and conflict-resolution rules, and run
`node tools/validate.js && node tools/smoke.js` before every push.

---

## 3. Technology Stack & Design Decisions

### Web Architecture: Pure Vanilla JS Single Page Application (SPA)
- **Zero Heavy Framework Dependencies**: No React, Angular, or Vue build overhead. Loads instantly across all low-end devices, smartphones, and school computer labs.
- **Client-Side State Machine**: Handled in `state` object inside `app.js`:
  ```javascript
  const state = {
    page: "home",             // 'home', 'subjects', 'books', 'roadmap', 'study-plan'
    selectedClass: null,      // 'cls9', 'cls10', 'cls11', 'cls12'
    activeSubject: null,      // 'bio', 'chem', 'math', 'pakstudy', 'eng', 'urdu', 'phys', etc.
    activeBioTab: "sections", // 'sections', 'summary', 'exercise', 'slo', 'practicals'
    activeBioChapter: 0,
    activeMathChapter: 0,
    activePakStudyChapter: 0,
    ...
  };
  ```
- **Dynamic DOM Rendering**: UI views are rendered into `<main id="page-content"><div id="dashboard-body"></div></main>` via functional templates.
- **Local Persistence**: User performance, streak days, questions answered, and accuracy are tracked in browser `localStorage`.

---

## 4. Multi-Platform Synchronization
- Content defined in JSON-like structures in `js/*_data.js` is structured cleanly with JSON-compatible objects and arrays.
- This allows Android's Jetpack Compose Room/Gson parser to ingest identical datasets from `assets/` into Kotlin data classes, maintaining 100% parity between the Web Portal and Android Mobile App.
