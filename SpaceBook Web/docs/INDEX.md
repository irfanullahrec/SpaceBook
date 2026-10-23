# SpaceBook — Comprehensive Documentation Index

Welcome to the official developer and architecture documentation for **SpaceBook** (Khyber Pakhtunkhwa Textbook Board Curriculum Portal).

This repository contains two core platforms:
1. **SpaceBook Web**: Pure client-side modern Single Page Application (SPA) powered by standard web technologies (HTML5, Vanilla JavaScript ES6+, CSS3) with zero heavy framework bloat.
2. **SpaceBook App**: Native Android mobile application written in Kotlin with Jetpack Compose.

---

## Start here (current, 2026-10-20)

| Document | What it answers |
|---|---|
| [HANDOVER](./HANDOVER.md) | what was delivered, what is yours to decide, what nobody has checked (read this first) |
| [ARCHITECTURE](./ARCHITECTURE.md) | how the app is built and loaded, the build, the tests, the deploy (supersedes 01) |
| [DATA_CONTRACT](./DATA_CONTRACT.md) | the shapes of the book data, the generated files and the wire formats |
| [RELEASE_AND_ROLLBACK](./RELEASE_AND_ROLLBACK.md) | before a push, what the push does, after the deploy, how to go back |
| [PROTECT_LIST](./PROTECT_LIST.md) | what must not be broken or deleted, and why |
| [PROGRESS_LOG](./PROGRESS_LOG.md) | what was done, what was verified, what was not, what is next |
| [PARITY_MATRIX](./PARITY_MATRIX.md) | the website and the Android app function by function: same, platform-specific or open, with the reasons (generated from `parity.json`; architecture section 11) |
| [BISE Swat alignment](./07_BISE_SWAT_ALIGNMENT.md) | what the Swat Board publishes for Classes 9-12 and how the app uses it (pattern, SLOs, model papers, answer sheet), findings, open points |
| [ACCESSIBILITY](./ACCESSIBILITY.md), [SEARCH](./SEARCH.md), [ADMIN](./ADMIN.md), [CONTENT_REVIEW](./CONTENT_REVIEW.md), [PHASE3_LAZY_LOADING](./PHASE3_LAZY_LOADING.md), [PHASE4_OFFLINE](./PHASE4_OFFLINE.md), [PHASE5_HOOKS](./PHASE5_HOOKS.md), [PHASE7_LEXICON](./PHASE7_LEXICON.md), [PHASE8_SECURITY](./PHASE8_SECURITY.md), [SERVER_CONFIG](./SERVER_CONFIG.md), [BACKUP_RESTORE](./BACKUP_RESTORE.md), [CLEANUP_LOG](./CLEANUP_LOG.md) | the feature and phase notes |

The documents numbered 01-06 below are older: 01 and the "Before every push" line are out of date (use ARCHITECTURE and RELEASE_AND_ROLLBACK).

## Documentation Modules

| Document | Description | Key Topics Covered |
|---|---|---|
| [**01. Project Structure & Architecture**](./01_PROJECT_STRUCTURE_AND_ARCHITECTURE.md) | High-level system design and directory structure | Folder layouts, data flows, offline caching, modular JS architecture, Android app relationship |
| [**02. Functions & Components Reference**](./02_FUNCTIONS_AND_COMPONENTS_REFERENCE.md) | Exhaustive catalog of every JavaScript function | Navigation routers, subject suites (Bio, Chem, Math, PakStudy, Eng, Urdu), TTS engine, dictionary popovers, state management |
| [**03. Curriculum Datasets & Subjects**](./03_CURRICULUM_DATASETS_AND_SUBJECTS.md) | Subject data schemas and verification status | Biology 9 (56 sections), Chemistry 9 (8 units), Mathematics 9 (17 units), Pakistan Studies 9 (4 units), English (15 units), Urdu (15 units) |
| [**04. UI/UX & Pedagogical Strategy**](./04_UI_UX_AND_PEDAGOGICAL_STRATEGY.md) | Design rules and student experience guidelines | Max 3 stats cards in a row, single-line header bars, default collapsed accordions, bilingual hover tooltips, Nastaleeq typography |
| [**05. Strategy & Future Roadmap**](./05_STRATEGY_AND_FUTURE_ROADMAP.md) | Long-term roadmap and operational strategy | Grade 10-12 expansion, offline PWA service workers, indexedDB storage, Android synchronizer, automated QA suites |
| [**Contributing**](../CONTRIBUTING.md) | Multi-contributor workflow (read before your first push) | File ownership table, adding a subject, rebase workflow, conflict-resolution rules, validation commands |

---

## Quick Reference Facts
- **Board Alignment**: Khyber Pakhtunkhwa Textbook Board, Peshawar (Official 2018–2026 Syllabus & SLO Framework).
- **Core Principle**: 100% Verbatim textbook accuracy without abridgment or paraphrasing.
- **Languages Supported**: English, Urdu (اردو), Pashto (پښتو), and Arabic (العربية).
- **Before every push**: see RELEASE_AND_ROLLBACK (`node tools/validate.js`, `node tools/smoke.js` and the other suites listed in ARCHITECTURE must pass; generated files must be fresh).
- **Current Completion (Grade 9)**:
  - 🧬 **Biology**: 9 / 9 Units (56 Verbatim Sections, 164 Solved Qs, 162 SLO Bank, 9 Practicals) — 100% Complete.
  - 🧪 **Chemistry**: 8 / 8 Units (Full Core Theory, Solved Exercises, Numericals, SLOs, Vocabulary Bank) — 100% Complete.
  - 📐 **Mathematics**: 17 / 17 Units (88 Sections, 345+ Worked Examples & Theorems, 747+ Solved Problems) — 100% Complete.
  - 🇵🇰 **Pakistan Studies**: 4 / 4 Units (27 Urdu Sections, 100 Solved Qs, 20 Historical Milestones) — 100% Complete.
  - 📖 **English**: 15 / 15 Units (Full Texts, Trilingual Translations, Solved Exercises, 4,000+ Word Lexicon) — 100% Complete.
  - 📗 **Urdu**: 15 / 15 Lessons (Nasar, Nazam, Ghazal, Tashreehat, Khulasa, Dual-Voice TTS) — 100% Complete.
  - ⚛️ **Physics**: 9 Units (Core theory, numericals, review MCQs).
  - 🕌 **Islamyat (Class 9)**: 15 / 15 Units (Uthmani Ayaat, trilingual translations, lughat, SLO Q&A) — 100% Complete.
  - 🕋 **Islamyat (Class 10)**: 18 / 18 Units (Uthmani Ayaat, trilingual translations, lughat, SLO Q&A) — 100% Complete.
  - 💻 **Computer Science**: 8 Units (Hardware, software, office automation, security).
