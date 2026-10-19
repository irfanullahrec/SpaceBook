# Content review: what a student or a printed paper could be shown that is not real

Written 2026-10-20 (Phase 6, content integrity). Numbers come from `node tools/content_lint.js` (re-run it any time; `--check` runs in CI and stops them getting worse). Nothing below was *deleted from the data*: where a decision is yours, the code has a switch that is **off** until you approve.

## Fixed in code (no decision needed)

| Id | Problem | What changed |
|---|---|---|
| CONT-02 | Papers answer keys: the pool read `correctIndex`/`ans`, but most banks store the key as `correct`, so the printed key and the OMR sheet defaulted to option A. In the pool 100 % of the keys of Class 1-6, 9, 11, 12 Maths, all Islamiat and all Urdu questions were "A". | One reader, `sbMcqKey()` (accepts `correctIndex`, `answerIndex`, `correct`, `ans`, a letter, or the option text). Islamiat is now 23 % A, Urdu 22 % A. A question **without** a key now prints "Key not available" and fills no bubble: a missing key is never "A" again. |
| CONT-03 | The 15 Islamiat chapters carry a "video lecture" whose URL is a test video (`dQw4w9WgXcQ`), with an invented title, duration and instructor ("KPK Board Islamic Studies Specialist"). The Maths topic "Video" tab showed a fake player ("Click to Play Topic Lecture", "1080p HD", 18:45). | A video is embedded only when the chapter has a real YouTube embed URL; otherwise the tab says "There is no video lecture for this chapter yet." The fake Maths player and its tab button are gone. The 15 records are still in `js/islamyat_data.js` (data; replace them when real lectures exist). |
| PDF-01 | Every "Download PDF" / "Read Online" button pointed to `assets/books/*.pdf` (the folder does not exist), `file:///D:/SpaceBook/...` or `file://DESKTOP-R2HQSAV/...`: dead links on every student device, and the library said "PDF Available (n MB)" and "Format: High-Resolution PDF". | A PDF is linked only when its path is listed in `SB_PACKAGED_PDFS` (empty today). No PDF is packaged, so the buttons and the "PDF Available" claims are gone; the solved chapter notes button of the library stays. |

## Decisions for you

1. **Generated "Board SLO" practice (CONT-01).** Every topic of Class 9 and Class 10 Maths except section 1.1 shows questions made from the topic title by templates: 5 MCQ templates (the first option is always the right one), 3 short and 2 long question templates with generic "solutions". Counts: Class 9: 64 topics, 320 MCQs, 192 short, 128 long; Class 10: 122 topics, 610 MCQs, 366 short, 244 long (1,860 items). The same items feed Papers. Section 1.1 of Class 9 is hand-written (4 MCQs, 3 short, 2 long) and stays.
   - Switch (off by default): `window.SB_FLAGS = { hideGeneratedSlo: true }` or `localStorage.sb_flag_hideGeneratedSlo = 'on'`. With it on, the generated items disappear from the tab and from Papers, and the tab says "Verified practice questions for this topic are being prepared. See the Textbook Exercises tab."
   - Your decision: approve making it the default (I would change one line), and decide about the word "Board": until an official KPK SLO list is supplied these are not board questions; "KPK Board Standard" / "Board SLO" labels should become "Textbook practice".
2. **English videos.** Class 9/10 English shows the same three MP4s (`covers/Videos/English.mp4`, `URdu.mp4`, `1st Paraghraph.mp4`) in the Video tab of **every** chapter. Which chapter are they from? If it is one, they should appear only there; the tab then disappears elsewhere.
3. **Cayley and the year 1860.** The Class 9 Maths lesson says Cayley introduced the term matrix in 1860 (`js/math_data.js` lines 16 and 18, the Urdu gloss in `js/app.js`, a list line "Arthur Cayley (1860)", and one hand-written MCQ). Historians give Cayley's memoir on matrices as 1858, and the word "matrix" as Sylvester's, 1850. If the textbook says 1860 the lesson is a quotation and stays; if not, it needs correcting in the data. I did not change it.
4. **Papers use the same Maths questions for every class.** The pool returns the same 418 Class 9 questions for Class 1-6, 11 and 12 (Class 7, 8, 10 have their own). A Class 1 paper therefore contains Class 9 questions. That is a Papers design problem (Phase 9: blueprint and class-specific pools), listed here so nobody trusts those papers meanwhile.
5. **Repeated and skewed questions.** 445 repeated MCQ stems in the Papers pool; 15 Maths subjects have >= 80 % of the keyed questions on one option (all the generated ones above). Not changed: they go with decision 1.
6. **Which book PDFs may be packaged** (licence: the textbooks belong to the KPK Textbook Board). Listing a path in `SB_PACKAGED_PDFS` brings the buttons back for that book.

## Checked and left alone

Where the "Board SLO" label and 1.1's hand-written items are the only reviewed ones, the rest of the Maths view (lessons, topic exercises) comes from the textbook and was not touched.
