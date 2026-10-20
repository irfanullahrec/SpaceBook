# Protect-list (updated 2026-10-20; replaces section 7 of `SPACEBOOK_DEEP_AUDIT.md`)

Do not break, delete, or "tidy" these. Each line says why and what to do instead.

## Verified content and the pipelines that make it

| What | Why | Instead |
|---|---|---|
| `js/*_data.js`, `js/*_book.js`, `js/data_*.js`, `js/*12_exercise_banks.js`, `js/math_*_solutions.js`, `js/math12_*translation*.js` | transcriptions of the textbooks checked page by page against the scans | change the transcription and rerun the class pipeline; never edit the generated `.js`, never "repair" an answer key by guessing (leave it `null` and queue it) |
| `docs/source-verification/class-N/` (scans' transcriptions, `tools/`, notes on missing pages) | the only record of where each line came from | add to it; the archive plan never touches it |
| `covers/` and the figures under `assets/` that chapters reference | referenced by data and by the offline map | check `content/offline_map.json` and a text search of `js/` before moving anything |

## Generated files (regenerate, never edit)

`lazy.html`, `content/**`, `js/test_prep_bank.js`, `js/study_plan_index.js`, `js/word_stats_*.js`, `js/lexicon_data.js`, `docs/test_prep_review/no_key.csv`, `tests/baseline/html-*/`. Command: `node --max-old-space-size=8192 tools/build/all.js` from a clean checkout (`RELEASE_AND_ROLLBACK.md`).

## Locks that exist to stop silent change

`tests/contract/hooks.json` (who extends which function, in which order), `cls_books.json` (unit counts of the rebuilt books), `content_lint.json`, `tests/baseline/contrast.json`, `axe.json` and `html-2026-10-20/` (9,710 renders). Update them only with an intended change and look at the diff: a lock that changes without a reason is the bug.

## Owner decisions that are binding (UI and content)

- No language tabs or drop-downs for translation: clicking a sentence opens its EN / UR / PS lines (`sb_trilingual.js`); topic cards are collapsed and have their own full screen.
- Chapters follow the book's order: Lessons, Summary, Exercise, then practice, nothing repeated (`sb_structure.js`); only tabs with content are shown; tab and button labels follow the subject's medium (English, Urdu, Pashto, Arabic) (`sb_medium.js`).
- Classes 9 and 10 are the reference layout for Classes 11 and 12.
- Interactive MCQs: every multiple-choice question is a radio group with right / wrong feedback (`sb_mcq.js`).
- Word meanings never leave the device (no Google, no MyMemory), read-aloud uses the device's own voices, no third-party script or font at start-up (`validate.js` checks).
- Generated "Board SLO" practice stays behind the owner flag until approved; nothing that is not from a book may be labelled as a board question.

## Data and secrets

- `api/config.php` and any password, token or key never enter the repository or the upload (the workflow writes `config.php` from secrets; `tools/validate.js` and tests check that no secret is packaged).
- Student data is never deleted by a migration: migrations only add; `down` scripts are for emergencies and need a dump first.
- Logs hold ids and codes, never payloads (`audit_log`, `sync_errors`).
- `SpaceBook_Archive/` (outside the web folder) is the only copy of 7.2 GB of moved scratch files. It is deleted by the owner, if ever, never by a script (`CLEANUP_LOG.md`).

## Behaviour that must not regress (each has a test)

A missing answer key is "key not available", never option A (`sbMcqKey`); a paper is drawn from the books of its own class only; a placeholder video or a dead PDF link is never shown; the chapter of a subject is looked up from the arguments, not from the previously selected class (ARCH-02); a blocked or deleted account cannot sign in, sync or open the admin pages; an administrator cannot be created over HTTP.
