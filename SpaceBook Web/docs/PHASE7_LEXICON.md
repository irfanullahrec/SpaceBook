# Phase 7 (first part): offline meanings, no third parties

**Problems found (ML-01, SEC-04).** (1) The first word lookup on the lazy page read the word list of **every book** to build the offline lexicon: 106 files, 150 MB, about 10 s in the test sandbox; on a phone that is a freeze or a crash. (2) A selected word or sentence was sent to Google (`translate.googleapis.com`) and, as a fallback, to MyMemory; word statistics sent batches of words to Google; the word popover asked MyMemory and then wrote the machine text into `ENG_URDU_DICT` as if it were a dictionary entry. (3) Nobody could say how much of the books the offline lexicon understands.

## What was built

| Piece | File | |
|---|---|---|
| Lexicon v1 | `tools/build/make_lexicon.js` -> `js/lexicon_data.js` | One generated file (12,738 rows `[English, Urdu, Pashto, Arabic]`, 0.64 MB) holding exactly what the runtime used to collect from `SB_OFFLINE_LEXICON`, every book's word list (Classes 1-11, the Maths readers) and `ENG_URDU_DICT`, in the same order, exact duplicates dropped. Part of `tools/build/all.js` (CI checks it is current). It is a lazy file on the lazy page. |
| Runtime | `js/universal_translate.js` `lexicon()` | Adds the rows instead of scanning the books (falls back to the old scan if the file is missing). First lookup: 1 file / 1 MB / 0.4 s (was 106 files / 150 MB / 10 s). |
| No third parties | `js/universal_translate.js`, `js/word_stats.js`, `js/app.js` | The calls to Google and MyMemory are gone. A word or sentence without a meaning on the device gets the word-by-word gloss or nothing ("meaning not yet available"); the popover's online lookup returns nothing and writes nothing. If you approve a translation service, it can be reached **only through your own server**: set `window.SB_TRANSLATE_PROXY` to its URL (`POST {text, src, tgt}` -> `{text}`); its answer is labelled as machine text. Unset by default. Together with the read-aloud change (Phase 4) the app now sends no text a student reads or selects to any website. |
| Coverage report | `tools/build/lexicon_report.js` -> `docs/LEXICON_COVERAGE.md` | Per direction and per class: how many distinct words (types) and how many occurrences in the books (tokens) have a meaning on the device. |
| Review queues | `docs/lexicon_review/*.csv` (6) | The 2,000 most frequent words without a meaning for English->Urdu, English->Pashto, English->Arabic and Urdu/Pashto/Arabic->English, most frequent first, with the classes that use them and an empty column for the translator. Code-sample and transcription tokens (`scan`, `pdf`, `kptbb`, `cout`...) are left out. |

## Tests (CI)

- `node tests/lexicon/equivalence.js`: the generated rows answer exactly like the old scan of every book on ~4,800 lookups in all 12 directions, and a lookup loads the lexicon and the dictionary, no book.
- `node tests/lexicon/privacy.js`: online, translating an unseen sentence and a known word, the old word lookup, all make **no** request to any website; with a proxy set only the proxy is called and its text is labelled as not from the book; no script names a third-party translation or speech host.
- `node tools/build/all.js --check` covers `js/lexicon_data.js`.

## Where the offline meanings stand (the numbers you asked for)

Whole project, share of occurrences in the books whose word has a meaning on the device: English->Urdu **84.3 %**, English->Pashto **78.7 %**, English->Arabic **63.2 %**; Urdu->English 82.4 %, Urdu->Pashto 70.1 %, Urdu->Arabic 65.4 %; Pashto->English 78.9 %, Pashto->Urdu 73.3 %; Arabic->English 59.7 %, Arabic->Urdu 49.4 %, Arabic->Pashto 51.4 %. As distinct words it is 11-17 % (the long tail of rare words). The Phase 7 targets (>= 95 % Urdu/Pashto, >= 85 % Arabic, by occurrences) are **not met**; closing the gap is translation work that I cannot do: the review queues are the work list, highest frequency first (the top 2,000 words of a queue cover a large share of the missing occurrences; the report states how much). Class by class numbers: `docs/LEXICON_COVERAGE.md`.

## Not done (honest list)

- The single interaction component (hover 250 ms, long-press on touch, keyboard focus, one card with the three other languages per language, RTL/LTR per line) replacing the legacy tooltip and popover paths; sentence translations stored per sentence in the book contract (`tr` of Contract v1, not started), word forms and suffix handling beyond what `offlineLookup` already does; provenance (`src`, `reviewed`) per lexicon row: rows carry none yet.
- The first global search still reads the Class 9-12 books (about 18 files / 51 MB): the offline full-text search index is Phase 12.
- Not verified in a real browser: hover/selection UI (only the lookup functions and the network behaviour are tested).

## Decisions for you

1. **Who translates** the review queues (Urdu, Pashto and especially Arabic meanings), and in what form they come back (fill the CSV column; I merge reviewed rows into the lexicon with `reviewed: true`).
2. **Online fallback**: keep it off (as now), or approve a translation service behind your own server (`SB_TRANSLATE_PROXY`); I would not send student text to a third party without your decision and a privacy statement.
