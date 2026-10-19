# Phase 3: lazy book data

**Problem (PERF-01).** `index.html` loads 262 scripts, 358 MB, before the first screen: 17 s to `DOMContentLoaded` and ~700 MB of heap in the browser on the development machine (1,063 MB in the Node test sandbox). Most of it is book text of subjects the student never opens in that visit.

**What was built** (`index.html` itself is untouched apart from one new script tag for the Maths 12 study banks; the lazy page is a generated copy beside it):

| File | Role |
|---|---|
| `js/core/lazy.js` | Runtime. Stands in for each large data global until it is first used; loads the file with one synchronous request, then forwards. |
| `tools/build/make_lazy.js` | Build. Writes `lazy.html` (a copy of `index.html` without the lazy `<script>` tags, plus `lazy.js` and an inline manifest) and `content/lazy_manifest.json`. `--check` exits 1 if they are stale. |
| `tools/build/lazy_eager.json` | Files that must stay in the page (the registry `data.js`, `word_stats_summary.js`) and the private helper names (temporaries and helper objects that only their own file uses). |
| `tools/build/lazy_overlays.json` | Scripts that only patch a lazy file's data at load (47: the Class 12 study and exercise-bank patches, the 20 Maths 12 translation/repair scripts, the Class 10 Chemistry/Physics source patches, the 11 Class 10 Biology unit sources). They run right after their parent loads, in their original order. |
| `tools/build/measure_lazy.js`, `inventory.js`, `probe_files.js` | Measurement: what loads at start-up and per subject; what every script defines; which files run alone. |
| `tools/build/lazy_parity.js` | Proof: renders every chapter and tab of every subject on both pages in one run and compares. |

**How it works.** A file is lazy when it runs alone in an empty context (with an empty `DATA` registry) and carries data: an array/object global, a key of a shared book container, or a key it adds to `DATA`. Files that only hold behaviour (readers, wrappers; objects holding functions unless the file is a `*_data.js`) stay eager. 152 files, 344 MB qualify.
- A global array/object (`ENGLISH_12_DATA`, `MATH_2_DATA`...) becomes a forwarding `Proxy`. `typeof X`, `Array.isArray(X)`, `'X' in window` do not load anything (the code is full of `typeof X !== 'undefined'` checks); the first real use does (`X.length`, `X[0]`, `for..of`, `JSON.stringify`...), after which the stand-in is replaced by the real value.
- A book in `CLSn_BOOKS` (`CLS2_BOOKS.math`) is an accessor on the pre-created container: reading it loads the file; `Object.keys(CLS2_BOOKS)` lists every book without loading.
- A book in `CLASS11_BOOKS` (the Class 11 registry) is handled the same way.
- A public function of a lazy file (the Class 11 renderers, Maths 12 helpers: 705 of them, plus those declared by an overlay such as `renderClass10PhysicsWorkedExamples`) is a stub that loads the file and calls the real function, which the file's own declaration has put in the stub's place. The build refuses a file whose function another script reassigns (that wrapper would be overwritten when the file loads): none today.
- A key a lazy file adds to the registry (`Object.assign(DATA, { chemChapters, chem10Chapters })`, `DATA.urduChapters = URDU_DATA`) is an accessor on `DATA` until the file loads; the generated page calls `SBLazy.attachData(DATA)` right after `data.js` (a `const`, out of reach of `lazy.js`).
- Top-level `const/let/var` of a lazy file become `window` properties when it runs (a script tag would make them global bindings).

**Measured** (Node sandbox with the real app, `tools/build/measure_lazy.js` and the memory script; browser numbers will differ but the ratio is what matters):

| | eager `index.html` | lazy `lazy.html` |
|---|---|---|
| scripts in the page | 262 | 64 |
| ready | 7.5 s | 0.23-0.29 s |
| heap after load | 1,063 MB | 21 MB |
| lazy files loaded at start | - | 0 of 152 |
| open Class 9 Biology | 207 ms (heap 1,066 MB) | 113 ms (heap 28 MB) |
| open Class 12 Physics (18 MB file) | 1.3 s (heap 1,077 MB) | 1.4 s (heap 60 MB, includes loading the file) |

Targets of the phase: initial JS transfer <= 3 MB compressed, DOMContentLoaded <= 2 s, heap after home <= 80 MB. The scripts left in the lazy page add up to about 12 MB uncompressed (`app.js` 1.4 MB, the English 10 chain 3.1 MB, small behaviour files); compressed that should be well under 3 MB but has not been measured (it needs the server compression below), and the heap figures are the Node sandbox's (no real DOM, fonts or images): the browser has to confirm both.

**Parity (the safety net).** Run from a clean checkout of the committed state (`git worktree`, sparse): all 147 subjects, 1,843 chapters (generic reader, Maths view and the 12 chapterless pages), 9,710 tab renders, hashed rendered HTML: lazy = eager, 0 differences, in forward and in reverse subject order; the eager page also equals `tests/baseline/html-2026-10-20`. The whole smoke suite (251 checks incl. global search and MCQ flows) passes on the lazy page (`SB_PAGE=lazy.html node tools/smoke.js`). An earlier version of the snapshot tool hashed stale content for the five Maths subjects and skipped the chapterless pages; it was rewritten (`tools/snapshot_html.js`) and the baseline regenerated (`tests/baseline/html-2026-10-20`), so the parity above is the corrected measurement.

Bugs this caught while building (each is now a rule in the build):
- a reader script that exposes an API object looked like data (rule: a file that is not `*_data.js` and whose global holds a function is behaviour and stays eager); a file with only functions never qualifies;
- overlay scripts that patched lazy data at load forced 130 MB to load at start (now run after their parent);
- an overlay that declares public functions (`physics_10_source_data.js`) made Class 12 Physics fail with `renderClass10PhysicsWorkedExamples is not defined` until those functions got stubs (10 step errors and 100 differences, found by the parity run);
- the test sandbox ran only the manifest's inline script and not `attachData`, which hid every `DATA` accessor (Class 9/10 Chemistry and Physics showed one chapter instead of eight and nine);
- `class11BookBySubject()` scanned all Class 11 books to open one (now a key lookup; `tools/validate.js` checks the `subjectId = cls11-<key>` invariant);
- `math12_study_views.js` built every Maths 12 study bank at script load (now `warmMath12StudyBanks`, run after the book loads);
- the manifest held the generation date and CRLF-dependent hashes, so `--check` would have failed on any other day or machine.

**Found, not caused by this work (ARCH-02b: sticky view state, for Phase 5/6).** The app leaves the student's last sub-selection in the shared `state` object and the next subject inherits it. `node tools/stateleak.js` lists the keys: `activeSubjLessonSubTab`, `activeSubjWordsSubTab`, `activeSubjExCat`, `activeMathSloCategory`, `activeMathEx`, `class12ExerciseCategory`, `class12StudyCategory` (plus the intended `selectedClass`, `activeSubject`, `selectedSubjChapter`, `activeSubjTab`, `selectedMathChapter`, `mathClassId`). Example: choose "Long Questions" in Class 12 Physics, open Chemistry exercises, and "Long Questions" is preselected there; a fresh visit would show MCQs first. Whether a remembered category is wanted is a product decision (it is a sticky preference in effect, but it is neither scoped to the subject nor saved, so it behaves like a leak); the render core (Phase 5) should own it as explicit per-subject view state. Rendering order also changed content in two harmless ways: random ids (sb_mcq card ids, ids inside Maths diagram SVGs) and the `cls9`/`cls10` prefix of auto answer ids for the shared Class 9/10 Islamiat book. With the sticky keys reset and those ids normalised, forward and reverse order give identical hashes for all 9,710 renders (before: 1,522 differences with the first version of the tool, 190 once Maths and the counter were handled).

**ARCH-02 (book lookup depended on `state.selectedClass`) is fixed.** `getSubjectChapterList(subjKey, classId)` tested `classId === 'cls7' || state.selectedClass === 'cls7'` in 82 places, so with `state.selectedClass = 'cls7'`, `getSubjectChapterList('eng', 'cls9')` returned the Class 7 book (reproduced: 186 wrong answers in 2,431 lookups, e.g. `eng cls6` while `cls11` was selected gave 24 chapters instead of 9). Now the class asked for wins (`const cur = classId || state.selectedClass`; the Class 11 wrapper in `class11_study_views.js` likewise). `node tools/arch02_matrix.js` (also `--page lazy.html`, and a CI step) opens every subject, records the (subject, class) pairs the app really asks for and fetches each with every possible `state.selectedClass` (all 15 classes, `''`, `null`): 143 pairs x 17 = 2,431 lookups, 0 differences. The rendered HTML of all 9,710 tab renders is unchanged by the fix (the app always selects the class before asking). 67 other `state.selectedClass ===` tests remain in `app.js` outside this function; they are migrated with their consumers (registry-driven `openSubject`, next).

**Not done / limits.**
- `index.html` still loads everything. Switching production to the lazy page is a release decision (below); the file is deployed beside it as `lazy.html` so it can be tried in a real browser first.
- What stays eager (47 files, 5.6 MB): `app.js`, the small behaviour files, and the Class 10 English chain (`data_eng.js`, `english_10_data.js`, `english_10_source_review.js`, 3.1 MB). `english_10_data.js` defines `ENGLISH_10_DATA` and also overwrites `DATA.eng10Chapters`, which `data_eng.js` sets too, so the load order decides the final value and neither can be an independent lazy file; they need to become one parent with an overlay, with the same parity proof.
- Synchronous requests: the first use of a book blocks the page for the transfer + parse (a 20 MB file ~1 s on this machine). They are same-origin, once per file, and become cache hits once the service worker of Phase 4 exists. A spinner on `openSubject` (asynchronous pre-load) is possible later without changing call sites.
- Not tested in a real browser (Chrome could not run here): proxy behaviour is spec-defined and the same in V8, but only the Node sandbox was used. Features that scan every book (global search, word statistics, Papers) still work (they touch the books, which loads them: smoke tests cover search and MCQs) but are not faster.
- Manifest hashes are recorded (`sha256`) for the signed-package work of Phase 8; nothing verifies them yet.

**Cut-over (owner).** After trying `https://wantuch.pk/spacebook/lazy.html` in a browser: make the lazy page the default by generating it into `index.html` from a kept source copy (rename today's `index.html` to `index.src.html`, run `node tools/build/make_lazy.js --src index.src.html --out index.html`, update the test tools to read `index.src.html`), deploy, and keep `index.src.html` as the eager fallback. Rollback = restore the previous `index.html`.
