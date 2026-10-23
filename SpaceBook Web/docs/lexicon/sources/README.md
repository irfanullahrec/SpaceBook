# Open sources compiled into js/lexicon_data.js

Fetched ONCE at build time. Nothing in the app calls these services; the data is committed here and compiled by `tools/build/make_lexicon.js`.

| File | What | From | Licence / credit |
|---|---|---|---|
| `quran_words.json` | word-by-word English and Urdu meaning of each word of the Qur'an, filed under both the Uthmani and the plain (Imla'i) spelling | api.quran.com (v4), `tools/offline_meanings/fetch_quran_words.py` | Quran.com / Tanzil / Quranic Arabic Corpus translators; check their terms before a commercial release |
| `native_ur.tsv` | English meaning of Urdu words the books use | English Wiktionary (kaikki.org extract), `tools/offline_meanings/extract_kaikki_native.py` | CC BY-SA 4.0, https://en.wiktionary.org |
| `native_ps.tsv` | the same for Pashto words | same | CC BY-SA 4.0 |

Hand-written lists live next to them: `../curated/` (English words with Urdu, Pashto, Arabic), `../curated_native/` (Urdu / Pashto words with English),
`../curated_sentences/` (instruction lines and headings in all four languages).
