# Offline word and sentence meanings (hover a word, click a sentence)

What the student sees: rest the pointer on a word (press and hold on a phone) and a card shows its meaning in the other three languages
(English, Urdu, Pashto, Arabic); click a sentence and its meaning opens just below it in all four languages. **Both read only data that is
stored in the project and on the device. Nothing a student reads, hovers or selects is sent anywhere.** (`tests/lexicon/privacy.js`)

## Where a meaning comes from, in order of trust

| Tier | Source | Shown as |
|---|---|---|
| 1. The textbook | the book's own word list or sentence translation (`js/*_data.js`, shown by each reader) | plain |
| 2. Hand-written | `docs/lexicon/curated/*.txt` (words), `docs/lexicon/curated_sentences/*.txt` (instruction lines, unit titles) | plain |
| 3. Open dictionary | Qur'an word-by-word (api.quran.com, human translators) and English Wiktionary glosses for Urdu and Pashto words | plain |
| 4. Computer translation | a local NLLB-200 model run once at build time on sentences with no stored translation (`tools/offline_meanings/mt_sentences.py`) | `≈` in front |
| 5. Word by word | the words of the sentence looked up one by one when nothing is stored | `≈ … (word by word, offline)` |

A meaning is never invented at run time, and a tier-4 or tier-5 text is always marked so a student knows to check it with the teacher.
**This is not a guarantee of 100 % accuracy.** Tiers 1-3 were checked by people (tier 2 by the assistant that wrote this, not by a native-speaking teacher yet:
send `docs/lexicon_review/` to one); tier 4 is a machine and is wrong now and then, most often in Pashto and in short fragments.

## What was built (2026-10-21)

* `tools/build/make_lexicon.js` + `tools/offline_meanings/normalize.js` -> `js/lexicon_data.js`: every row is placed in the right language column **by script**.
  Before, an Urdu gloss for an English word could sit in the Pashto column and an English definition in the Urdu column (the hover card then showed English
  in the Urdu row; every Urdu -> English lookup of a book word failed). Rows are joined per English word ("season" -> "موسم، رُت").
* `js/sb_morph.js`: base forms. "running", "children", "studies", "hydrogens", "built" find the entry of run, child, study, hydrogen, build.
* ~7,100 hand-written word entries (the most frequent words of the books that had no meaning, most frequent first) and ~270 hand-written instruction lines.
* `js/sb_sentkey.js` + `js/sent_data_0..15.js`: stored sentence translations filed by a hash of the sentence's letters (case, punctuation, spacing ignored); a
  longer text is answered by joining its stored sentences. Written by `tools/offline_meanings/build_sentences.js`.
* `tools/build/make_offline.js`: a "Word and sentence meanings" package in Download for offline.

## Coverage (share of the words of the books that have a meaning on the device; `node tools/build/lexicon_report.js`)

See `docs/LEXICON_COVERAGE.md` (regenerated). Words and sentences that are still missing are listed in `docs/lexicon_review/*.csv` most frequent first.

## Re-running it

```
node tools/offline_meanings/check_curated.js            # lint the hand-written lists
node tools/build/make_lexicon.js                         # js/lexicon_data.js
python tools/offline_meanings/mt_sentences.py ...        # optional, hours: more computer-translated sentences (needs D:/nllb600, CT2_USE_MKL=0)
node tools/offline_meanings/build_sentences.js           # js/sent_data_*.js
node tools/build/all.js                                  # lazy page, search, offline map, service worker version
node tests/lexicon/equivalence.js; node tests/lexicon/sentences.js; node tests/lexicon/privacy.js
```

## Licences and credits (owner: please read)

* Wiktionary glosses (Urdu, Pashto) - CC BY-SA 4.0, https://en.wiktionary.org (extracted through kaikki.org). Credit and the same licence for the derived data.
* Qur'an word-by-word meanings - Quran.com / Tanzil / Quranic Arabic Corpus data fetched once from api.quran.com.
* NLLB-200 (Meta) model weights are **CC-BY-NC 4.0 (non-commercial)**. The computer-made sentences (tier 4) were produced with it. If the portal is a commercial
  service, drop the `m` entries (`node tools/offline_meanings/build_sentences.js --curated-only` is the switch to add) or get legal advice before shipping them.
