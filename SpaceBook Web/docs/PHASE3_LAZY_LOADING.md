# Phase 3 (first part): lazy book data

**Problem (PERF-01).** `index.html` loads 261 scripts, 358 MB, before the first screen: 17 s to `DOMContentLoaded` and ~700 MB of heap in the browser on the development machine (1,063 MB in the Node test sandbox). Most of it is book text of subjects the student never opens in that visit.

**What was built** (nothing in `index.html` changed; the production page is untouched):

| File | Role |
|---|---|
| `js/core/lazy.js` | Runtime. Stands in for each large data global until it is first used; loads the file with one synchronous request, then forwards. |
| `tools/build/make_lazy.js` | Build. Writes `lazy.html` (a copy of `index.html` without the lazy `<script>` tags, plus `lazy.js` and an inline manifest) and `content/lazy_manifest.json`. `--check` exits 1 if they are stale. |
| `tools/build/lazy_eager.json` | Files that must stay in the page (the registry `data.js`, `word_stats_summary.js`) and the private helper names of the Class 12 data files. |
| `tools/build/lazy_overlays.json` | Scripts that only patch a lazy file's data at load (15: `chem12_unit13_study`, `phys12_unit11_study`, the 13 `*12_exercise_banks`). They run right after their parent loads, in their original order. |
| `tools/build/measure_lazy.js`, `inventory.js`, `probe_files.js` | Measurement: what loads at start-up and per subject; what every script defines; which files run alone. |
| `tools/build/lazy_parity.js` | Proof: renders every chapter and tab of every subject on both pages in one run and compares. |

**How it works.** A data file is lazy when it runs alone in an empty context, defines only data (an array/object global, or a key of a shared `CLSn_BOOKS` container) and no global holds a function. 129 files, 289 MB qualify.
- A global array/object (`ENGLISH_12_DATA`, `MATH_2_DATA`...) becomes a forwarding `Proxy`. `typeof X`, `Array.isArray(X)`, `'X' in window` do not load anything (the code is full of `typeof X !== 'undefined'` checks); the first real use does (`X.length`, `X[0]`, `for..of`, `JSON.stringify`...), after which the stand-in is replaced by the real value.
- A book in `CLSn_BOOKS` (`CLS2_BOOKS.math`) is an accessor on the pre-created container: reading it loads the file; `Object.keys(CLS2_BOOKS)` lists every book without loading.
- Top-level `const/let/var` of a lazy file become `window` properties when it runs (a script tag would make them global bindings).

**Measured** (Node sandbox with the real app, `tools/build/measure_lazy.js` and the memory script; browser numbers will differ but the ratio is what matters):

| | eager `index.html` | lazy `lazy.html` |
|---|---|---|
| scripts in the page | 261 | 118 |
| ready | 7.2-7.5 s | 1.8-1.9 s |
| heap after load | 1,063 MB | 241 MB |
| lazy files loaded at start | - | 0 of 129 |
| open Class 9 Biology | 198-252 ms | 136-171 ms |
| open Class 12 Physics (18 MB file) | 1.3 s (+11 MB) | 1.5 s (+32 MB: includes loading it) |

**Parity (the safety net).** Run from a clean checkout of the committed state: all 147 subjects, 1,843 chapters (generic reader, Maths view and the 12 chapterless pages), 9,710 tab renders, hashed rendered HTML: lazy = eager, 0 differences, in forward and in reverse subject order. The whole smoke suite (251 checks incl. global search and MCQ flows) passes on the lazy page (`SB_PAGE=lazy.html node tools/smoke.js`). An earlier version of the snapshot tool hashed stale content for the five Maths subjects and skipped the chapterless pages; it was rewritten (`tools/snapshot_html.js`) and the baseline regenerated (`tests/baseline/html-2026-10-20`), so the parity above is the corrected measurement.

Bugs this caught while building (each is now a rule in the build): a reader script that exposes an API object looked like data (rule: a global holding a function means behaviour, stays eager); two behaviour files defining a public function (stay eager); 15 overlay scripts that patched lazy data at load and forced 130 MB to load at start (now run after their parent).

**Found, not caused by this work (ARCH-02, for Phase 5/6).** The app leaves the student's last sub-selection in the shared `state` object and the next subject inherits it. `node tools/stateleak.js` lists the keys: `activeSubjLessonSubTab`, `activeSubjWordsSubTab`, `activeSubjExCat`, `activeMathSloCategory`, `activeMathEx`, `class12ExerciseCategory`, `class12StudyCategory` (plus the intended `selectedClass`, `activeSubject`, `selectedSubjChapter`, `activeSubjTab`, `selectedMathChapter`, `mathClassId`). Example: choose "Long Questions" in Class 12 Physics, open Chemistry exercises, and "Long Questions" is preselected there; a fresh visit would show MCQs first. Whether a remembered category is wanted is a product decision (it is a sticky preference in effect, but it is neither scoped to the subject nor saved, so it behaves like a leak); the render core (Phase 5) should own it as explicit per-subject view state. Rendering order also changed content in two harmless ways: random ids (sb_mcq card ids, ids inside Maths diagram SVGs) and the `cls9`/`cls10` prefix of auto answer ids for the shared Class 9/10 Islamiat book. With the sticky keys reset and those ids normalised, forward and reverse order give identical hashes for all 9,710 renders (before: 1,522 differences with the first version of the tool, 190 once Maths and the counter were handled).

**Not done / limits.**
- `index.html` still loads everything. Switching production to the lazy page is a release decision (below); the file is deployed beside it as `lazy.html` so it can be tried in a real browser first.
- The 89 data-like files that stay eager (legacy Class 9/10 `DATA` extenders, Class 11, `urdu_data.js`, `math_*_data.js`...; about 40 MB) are the next candidates: they extend the shared `DATA` object at load and need the same overlay treatment, one subject at a time, with the same parity proof.
- Synchronous requests: the first use of a book blocks the page for the transfer + parse (a 20 MB file ~1 s on this machine). They are same-origin, once per file, and become cache hits once the service worker of Phase 4 exists. A spinner on `openSubject` (asynchronous pre-load) is possible later without changing call sites.
- Not tested in a real browser (Chrome could not run here): proxy behaviour is spec-defined and the same in V8, but only the Node sandbox was used. Features that scan every book (global search, word statistics, Papers) still work (they touch the books, which loads them: smoke tests cover search and MCQs) but are not faster.
- Manifest hashes are recorded (`sha256`) for the signed-package work of Phase 8; nothing verifies them yet.

**Cut-over (owner).** After trying `https://wantuch.pk/spacebook/lazy.html` in a browser: make the lazy page the default by generating it into `index.html` from a kept source copy (rename today's `index.html` to `index.src.html`, run `node tools/build/make_lazy.js --src index.src.html --out index.html`, update the test tools to read `index.src.html`), deploy, and keep `index.src.html` as the eager fallback. Rollback = restore the previous `index.html`.
