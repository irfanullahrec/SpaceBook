# Search inside the books (Phase 12): how it works, what it covers, what is not done

Written 2026-10-20. Code: `js/core/search.js` (words, ranking, the box in the header), `tools/build/make_search.js` (the index), `css/search.css`. Tests: `tests/search/search.js`.

## What a student sees

In the header search box, under the title matches (subjects, units, textbooks, which still work as before), a list **IN THE BOOKS**: chapters whose text contains every word typed (the last word may be unfinished). Each row says the chapter, class, subject and the number of matches; a click opens the book and the chapter (through the chapter's own button in the sidebar, so the page does what it always does).

- **Scope.** The book being read, plus the books downloaded for offline use. Nothing open and nothing downloaded: a note says so. **Search all classes** fetches every subject's index one after the other (see the size below) and keeps the best results, so memory stays flat.
- **Words in all four languages.** The index holds what a chapter shows: every tab of every chapter, plus the translation lines kept in `data-en` / `data-ur` / `data-ps` / `data-ar`. An Urdu word finds the English chapter whose translation holds it.
- **Letter variants.** One normaliser for the index and the query: Latin case, accents and simple plurals (`cells` = `cell`, `studies` = `study`); Arabic script: Arabic and Urdu kaf and yeh, the heh family (teh marbuta, Arabic heh, Urdu heh, do-chashmi heh), Pashto yeh / gaf variants, hamza and madda forms of alef, vowel marks, Quranic signs, tatweel, Arabic-Indic and Persian digits, zero-width characters. `كتاب`, `کتاب` and `کِتاب` are the same word. Pashto letters that are letters in their own right (ټ ډ ړ ږ ښ څ ځ ڼ) are kept distinct.
- **Private.** The query never leaves the page. Only static files of this site under `content/search/` are fetched (`tests/search/search.js` checks the request list).

## The index

`content/search/index.json`: for every subject that has a chapter list: class, name, the hash and size of its shard, and its chapters (title and the call the sidebar button makes). `content/search/<subject>.json`: `{ v, n, x }` where `x` maps a word to `[chapter, count, chapter, count, ...]`; title words count three times; a word that is in many chapters keeps its 24 best.

Built by `node --max-old-space-size=8192 tools/build/make_search.js` (part of `tools/build/all.js`, after the lazy page and before the offline map). Shards are fetched as `<subject>.json?v=<hash>`: the service worker keeps them for good (cache-first), and the subject's **Download for offline** package contains its shard and the shared index (`tools/build/make_offline.js`), so a downloaded book is searchable with no network.

`make_search.js --check` (CI, through `all.js --check`) is fast: it compares a hash of the book data and of what the normaliser *does* (its answer for every character of the basic plane), and re-renders three sample subjects and compares them byte for byte. A change in how text is taken from the page needs `BUILDER_VERSION` bumped in `make_search.js`.

## Not done, and why

- **No snippet and no jump to the word.** A row names the chapter, not the sentence. Storing sentences would multiply the size by ten; the book's own filter box (reader tools) finds the word inside the open chapter.
- **No tab is stored,** so a result opens the chapter on its default tab.
- **Subjects without a chapter list** (the Drawing books) are not indexed; the builder prints them.
- **Ranking is simple** (log of the counts, titles weigh three); no stemming for Urdu / Pashto / Arabic morphology (prefixes of the last word cover much of it); no spelling correction; no phrase search.
- **Not tried in a real browser** or on a phone, and not with a screen reader (the rows are buttons in a labelled group).
- **Size.** See the numbers in `docs/PROGRESS_LOG.md` for the build that was committed; "Search all classes" downloads all of them once (they are then cached).
