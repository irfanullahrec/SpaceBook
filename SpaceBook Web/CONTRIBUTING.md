# Contributing to SpaceBook

SpaceBook is a dependency-free vanilla-JS portal. Anyone can add or improve a
subject, as long as everyone follows the same file-ownership and sync rules.
The goal of these rules is simple: **no contributor's work is ever lost or
reverted during a merge or rebase.**

---

## 1. TL;DR

```bash
git switch -c feat/chem-unit-9        # 1. branch per subject/feature
# ...edit ONLY your subject's files  # 2. stay inside your lane
node tools/validate.js                # 3. 104 static + dataset checks
node tools/smoke.js                   # 4. 51 UI smoke tests
git add <your files>                  # 5. stage only your files
git commit -m "chem: unit 9 notes"
git fetch origin
git rebase origin/main                # 6. sync before pushing
git push -u origin feat/chem-unit-9   # 7. open a PR
```

Never force-push `main`. Never reset a branch you did not create.

---

## 2. File ownership table

Exactly one person/subject owns each file. If you need a change in a file you
do not own, ask the owner (or send a PR that touches only the lines you need).

| Area | File(s) | Notes |
|---|---|---|
| Core registry (shared) | `js/data.js` | `stats`, `classes`, `subjects`, `books`, `studyPlan`, roadmap `chapters` map — **append-only** |
| Chemistry | `js/data_chem.js` | `DATA.chemChapters`, `DATA.chem10Chapters` |
| Physics | `js/data_phys.js` | `DATA.physChapters`, `DATA.phys10Chapters` |
| English (chapter arrays) | `js/data_eng.js` | `DATA.engChapters`, `DATA.eng10Chapters` (search fallbacks) |
| Biology (chapter arrays) | `js/data_bio.js` | `DATA.bioChapters`, `DATA.bio10Chapters` |
| Biology (full textbook) | `js/bio_data.js` | `BIO_DATA` |
| Chemistry vocabulary | *(in `js/data_chem.js`)* | unit `tables` live inside `chemChapters` |
| English (full textbook) | `js/english_data.js` | `ENGLISH_DATA` — summaries, exercises, vocabulary |
| English lexicon | `js/dictionary_data.js` | `ENG_UNIT_VOCAB_WORDS`, `lookupEngWord()` |
| Mathematics | `js/math_data.js` | `MATH_DATA` + `DATA.mathChapters` |
| Pakistan Studies | `js/pakstudy_data.js` | `PAKSTUDY_DATA` |
| Urdu | `js/urdu_data.js` | `URDU_DATA` → `DATA.urduChapters` |
| Islamyat 9 / 10 | `js/islamyat_data.js`, `js/islamyat_10_data.js` | `ISLAMYAT_DATA`, `ISLAMYAT_10_DATA` |
| Controller / routing | `js/app.js` | **shared** — small, additive edits only |
| Styles | `css/style.css` | **shared** — add rules inside your own section |
| Page shell | `index.html` | **shared** — one `<script>` line per data file |
| Docs | `docs/*.md` | one doc per topic, owner of that topic |

Shared files (`data.js`, `app.js`, `style.css`, `index.html`) are the only
places where two contributors can meet. They are all **append/insert-only**:
you add lines in a new place instead of rewriting existing lines, so git can
auto-merge two people's work line-by-line.

---

## 3. Adding a new subject

1. **Content** — create `js/<subject>_data.js` (export a global like
   `const CHEM_DATA = [...]`), or extend your `js/data_<subject>.js` file and
   assign into the registry: `Object.assign(DATA, { ... })`.
2. **Register the subject** in `js/data.js`:
   - push an entry into `DATA.subjects.cls9` / `DATA.subjects.cls10`
   - push a matching entry into `DATA.books`
   - bump `classes[].subjects` (kept in sync automatically — `tools/validate.js`
     fails if the count drifts)
3. **Wire the script** in `index.html`, after `js/data.js` and before `js/app.js`.
4. **Route it** in `js/app.js` → `openSubject()`:
   ```js
   } else if (subj.hasYouSubject) {
     state.activeSubject = "yousubject";
     openYouSubjectView(classId, subj);
   }
   ```
5. **Add state** fields (`selectedXChapter`, `activeXTab`) to the `state` object
   at the top of `app.js`.
6. **Style it** in `css/style.css` inside your own commented section.
7. **Validate**: `node tools/validate.js && node tools/smoke.js`.
8. Add the subject to `docs/03_CURRICULUM_DATASETS_AND_SUBJECTS.md`.

---

## 4. Sync workflow (how work is never lost)

* `main` is the integration branch. Work on a short-lived feature branch.
* Before every push:

  ```bash
  git fetch origin
  git rebase origin/main
  ```

* Prefer **rebase** for your own un-pushed commits (keeps history linear) and
  a normal **merge** if a branch is already shared with someone else.
* If you must integrate two shared branches: `git merge` — never rewrite
  history someone else has already pulled.

### Conflict rules

Conflicts are git telling you two people wrote the same lines. Resolve
hunk-by-hunk and **keep both sides**:

| Conflict location | Resolution |
|---|---|
| `js/data.js` `subjects` / `books` | keep **both** entries, restore the surrounding commas |
| `js/data.js` roadmap `chapters` map | each subject owns its own keys — keep both |
| `index.html` `<script>` list | keep **both** lines, then run `tools/validate.js` |
| `css/style.css` | keep **both** rule blocks |
| `js/app.js` | keep both features; only merge truly shared helpers |
| your own `js/data_<subject>.js` | it is yours — your version wins |

Never resolve a conflict with `git checkout --theirs .` /
`git checkout --ours .` on the whole tree, and never `git reset --hard`
another contributor's branch.

---

## 5. Conventions

* **Line endings:** LF everywhere (`.gitattributes` enforces it; Windows
  contributors get LF in the worktree too). UTF-8 without BOM.
* **No build step, no dependencies.** Plain `<script>` tags in `index.html`,
  load order matters (core registry first).
* **Data is data.** Keep curriculum content out of `app.js`; put it in a data
  file so two contributors can edit different subjects simultaneously.
* **Validate before pushing** — both commands must exit `0`:

  ```bash
  node tools/validate.js   # syntax, datasets, index.html wiring, app.js statics, css balance
  node tools/smoke.js      # renders every subject/tab/search path in a DOM stub
  ```

---

## 6. Data file map

```
js/
├── data.js            core registry (SHARED, append-only)
├── data_chem.js       ┐
├── data_phys.js       │ per-subject DATA.* chapter arrays
├── data_eng.js        │ (one file per subject owner)
├── data_bio.js        ┘
├── bio_data.js        BIO_DATA
├── english_data.js    ENGLISH_DATA
├── dictionary_data.js lexicon + lookupEngWord()
├── math_data.js       MATH_DATA
├── pakstudy_data.js   PAKSTUDY_DATA
├── urdu_data.js       URDU_DATA
├── islamyat_data.js   ISLAMYAT_DATA      (Class 9)
├── islamyat_10_data.js ISLAMYAT_10_DATA  (Class 10)
└── app.js             controller (SHARED)
```

Every file above is loaded by `index.html` in that order; `tools/validate.js`
fails if a `<script src>` points at a missing file or a data file is skipped.
