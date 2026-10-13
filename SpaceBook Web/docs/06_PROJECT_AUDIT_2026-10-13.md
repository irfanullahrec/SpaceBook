# Project audit — 2026-10-13

Scope: every class (PG → 12) and every subject registered in `js/data.js`, compared with the source scans in `D:\SpaceBook\Books\<class>\`. Each subject was also opened in the running app to record its reader tabs.

## 1. Books with no source scans

| Class | Book | State in the app |
|---|---|---|
| Play Group, Nursery, KG | All 12 subjects | Listed, but no source books exist anywhere |
| Class 1 | Urdu | Placeholder subject (1 empty unit) |
| Class 1 | General Knowledge | Placeholder subject (1 empty unit) |
| Class 3 | Urdu | Now shows the same "Textbook not available yet" page as Class 1 (it used to show fake placeholder units) |
| Class 7 | Pashto | `Books/7th/7th PAshto/` exists but is **empty (0 files)**. Not listed in the app. |

> Not a gap: KPK uses one Islamiat (compulsory) book for Classes 9 and 10, and one Islamiat Ikhtiari book for both years. `cls6_book_reader.js` already opens the Class 9 book for Class 10 Islamiat and the Class 10 book for Class 9 Ikhtiari.

## 2. Books that exist as scans but are missing or incomplete in the app

| Class | Book | Scans | Problem |
|---|---|---|---|
| 11 | Mathematics | 452 | **No data at all.** The subject opens with 0 units. |
| 11 | Islamic History | 344 | Subject `cls11-ishist` was just added (by another chat). Still being built. |
| 11 | Computer Science | 345 | In progress (`cs_11_data.js`, 10 units so far) |
| 12 | Economics | 335 | Raw docx dump: OCR noise, not checked page by page |
| 12 | Islamiat Ikhtiari | 265 | Raw docx dump (for example a stray "وجی" OCR error in unit 1). Not page-verified. |
| 12 | Islamic History | 238 | Raw docx dump with stray text ("42 کتابیار", "away"). Not page-verified. |
| 12 | Mutalia-e-Quran | 248 | Raw docx dump, 8 units. Not page-verified. |
| 10 | Mathematics | 332 | File header says "reconstruction in progress". Only about 0.33 MB of content for 332 pages. |
| 4 | Pashto | 154 | Data exists (23 lessons), but it uses the old reader and is not in `CLS4_BOOKS`. Its structure differs from Pashto in Classes 1–3, 5, 6 and 8. |
| 12 | Mathematics | 368 | Unit 1 shows "Exercises (0)". Worth checking. |

Every other book is complete: Classes 2, 5 and 6 entirely, and all books whose memory/pipeline notes say COMPLETE.

## 3. Same subject, different structure (tab sweep results)

The standard below is the layout most classes already use. Rows marked ✗ differ from it.

**English.** Standard: Lesson · Glossary · Exercise · Vocabulary · Use of Language · Grammar · Writing · SLOs + Original / +Urdu / +Pashto (Classes 1–9)
- ✗ Class 10, 12: old reader. Adds Paragraphs · Translations · Videos · Exercise (Solved).
- ✗ Class 11: no language tabs.

**Urdu.** Standard: سبق · مشق · SLOs · الفاظ · Grammar + Original / +English / +Pashto (Classes 1–8, 10)
- ✗ Class 9, 12: old reader. Adds پیراگراف و تحریر · تراجم · ویڈیو · مشق (حل شدہ).
- ✗ Class 11: only سبق · سوالات.

**Pashto.** Standard: لوست · مشغولتيا · SLOs · خاص لفظونه · قواعد + language tabs (Classes 1–3, 5, 6, 8)
- ✗ Class 4: old reader with different tabs.
- ✗ The language-tab order differs: Classes 1–3 and 5 show "+Urdu, +English"; Classes 6 and 8 show "+English, +Urdu".

**Islamiat, Social Studies, Geography, History, HPE, Drawing, Arabic, Pak Studies, Islamiat Ikhtiari.** Standard: Lessons · Important Concepts · Solved Exercises · Board SLO & MCQs · Summary & Key Points + language tabs
- ✗ All Class 11 books: only سبق · سوالات.
- ✗ Class 12 Pak Studies, Civics, Economics, HPE, Islamiat Ikhtiari and Islamic History: no language tabs.

**Mutalia-e-Quran.** Standard: Arabic / Urdu / Pashto / English ayah tabs (Classes 6–10)
- ✗ Class 11: only سبق · سوالات.
- ✗ Class 12: generic layout with no ayah language tabs.

**Science and Computer** (Physics, Chemistry, Biology, General Science, Computer, Statistics). Standard: Lessons · Concepts & Examples · Solved Exercises · Board SLO & MCQs · Summary & Formulas + language tabs (Classes 4–8; Class 9 Science and Computer; Class 10 Chemistry, Science and Computer)
- ✗ Class 9 Physics, Chemistry, Biology; Class 10 Physics, Biology; Class 12 Physics, Chemistry, Biology, Computer, Statistics: old tabs that repeat the standard ones (Complete Book Text · Translations · Videos · Exercise (Solved) · SLOs).
- ✗ Class 11 Physics, Chemistry, Biology, Statistics: no language tabs.
- ✗ Class 11 Computer Science: only Lesson · Exercise.

**Mathematics.** There are three layouts:
- (a) Lessons · Important Concepts · Solved Exercises … (Classes 1–4)
- (b) Lessons · Worked Examples · Exercises · Learning Outcomes · Summary (Classes 5, 6, 8)
- (c) Numbered "1. Lessons (n) · 2. Examples (n) …" (Classes 7, 9, 10, 12)
- Classes 9, 10 and 12 have no language tabs.
- Class 11 has no data.

**Naming.** The same subject has different names in different classes:
- Islamyat / Islamiat
- Drawing / Drawing & Art / Art & Model Drawing
- Mutalia-e-Quran / Mutalia-e-Quran-e-Hakeem
- Class 11 names carry "(Compulsory)" / "(Elective)" suffixes
- The Pakistan Studies id is `cls12-pak` in Class 12 but `pakstudy` in Classes 9–10

## 4. Changes made in this pass

1. **Universal translator** (`js/universal_translate.js` and `css/universal_translate.css`, loaded last in `index.html`).
   - Select any word or sentence in any tab of any class: drag, double-click, or long-press on a phone. A small bar appears under the text with the **other three** of English / اردو / پښتو / العربية, plus 🔊.
   - The source language is detected offline from the script letters. Urdu, Pashto and Arabic are told apart by their distinctive letters and harakat.
   - Tapping a language opens a compact card with tabs for all three targets, Listen and Copy. It closes on Esc or on a click outside.
   - Clicking a single word (the existing app.js word-click path) now opens the same card, so there is one translator everywhere instead of the old English-only popover. The textbook dictionary meaning is shown alongside the translation when it differs.
   - The last target language chosen for each source language is remembered.
   - Quranic Arabic shows a note pointing students to the approved textbook translation.
   - Uses the online engine (Google gtx, with MyMemory as fallback) and caches results. Offline, it falls back to the built-in dictionary.
   - Finishing a drag-selection inside a sentence no longer also toggles that sentence's translation drawer.
2. **`data.js`:**
   - Class-card subject counts now match the subject lists. They were wrong for Class 4 (6 → 8), Class 7 (7 → 12) and Class 11 (5 → 14).
   - Removed the duplicate Class 7 "History & Geography" placeholder. The real Geography and History books are complete as separate subjects.

3. **Continue where you left off** (`js/continue_learning.js` and `css/continue_learning.css`).
   - Remembers the last lesson opened in every subject, in this browser only.
   - Home and the Classes page show a "Continue learning" strip with the 4 most recent lessons. Each class's subject page shows "Continue in Class N" with its 3 most recent.
   - Reopening a subject at its first lesson shows a small "Continue where you left off" pill. It hides itself after 9 seconds.
   - Works by wrapping `openSubject` and the chapter openers (`selectSubjectChapter`, `select*Chapter`, `render*Chapter`, `openGenericChapterDetails`), so no reader code changed.
   - Tested: every class/subject with lessons is recorded. Resuming lands on the saved lesson in all reader types, including the Math readers (Classes 7, 9, 10, 12), Class 11 books and Class 10 Physics.

4. **One language bar in every book** (`js/structure_harmonizer.js`). Every reader now shows the standard lesson-level bar: 📖 Original (X) · X + L1 · X + L2. It is one global mode, so a choice carries across all books.
   - Old science readers (Class 9 Physics, Chemistry, Biology; Class 10 Physics, Biology; Class 12 Physics, Chemistry, Biology, Computer, Statistics): the 42-per-lesson paragraph switches are replaced by the standard bar. It drives their existing translation boxes.
   - Class 11 books: "+L1/+L2" opens each paragraph's own stored translation (the closed English/Pashto `<details>`).
   - Class 10 and 12 English, Class 12 Economics and Pak Studies: the textbook's sentence translations (`data-ur` / `data-ps`) are shown under each paragraph.
   - Class 9 Urdu: its stored English and Pashto translations are aligned to each paragraph or couplet.
   - Class 12 Urdu and Class 7/9/10/12 Math have no stored translations. Paragraphs there are machine-translated when they scroll into view, and each one is labelled "Machine translation".
   - Mathematics uses the same five tab names in every class: Lessons · Worked Examples · Exercises · SLOs & MCQs · Summary & Formulas. Counts are kept.
   - Not applied to Class 12 Mutalia-e-Quran: its text is a scrambled docx dump that needs the rebuild.
5. **Reader tools** (`js/reader_tools.js` and `css/reader_tools.css`):
   - ✓ ticks on lessons already opened
   - "Find a lesson" filter on lists of 10 or more lessons
   - Aa text-size control (90–150%)
   - "N of M lessons opened" progress on Continue cards
6. **Phone layout fix.** On phones, every reader put the 290px lesson list beside the lesson, leaving the lesson about 44px wide. The Class 12 stacked layout now applies to all classes, so the lesson is 348px wide on a 375px phone.
7. **Class 3 Urdu** now shows the same "Textbook not available yet" page as Class 1 Urdu and GK. Before, it showed fake placeholder units marked "Completed".
8. **Hover meanings** on English words now add Arabic to the dictionary's Urdu and Pashto.

## 5. Recommended next steps (largest benefit first)

1. **Class 11 main tabs.** Class 11 books (except Physics, Chemistry, Biology, Statistics and English) still show only سبق · سوالات, so they lack the standard family tabs (for example Urdu: سبق · مشق · SLOs · الفاظ · Grammar). This is the Class 11 pipeline's renderer.
2. Fill the data gaps in section 2, in this order: Class 11 Math, the Class 12 humanities rebuild (Economics, Islamiat Ikhtiari, Islamic History, Mutalia), Class 10 Math, Class 11 Islamic History.
3. Collect the missing source scans (section 1) or hide those placeholder subjects so students don't open empty books.
4. Ease of use:
   - in-book search
