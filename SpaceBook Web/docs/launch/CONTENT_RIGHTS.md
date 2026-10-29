# Content rights: the notice, the copy guard and what may be removed

Written 2026-10-29 on the owner's request (Classes 1 to 12, website and Android app). **This is engineering documentation, not legal advice.** The open legal questions are listed at the end for the owner and a lawyer.

## 1. Where things stand

* **No written permission of any rights holder is on file** (`FINDINGS_REGISTER.md` S-06; `docs/permissions/` has no record). The books are shown, and the app is meant to be offered under a subscription, without one. The notice below does not change that: it tells readers who owns what, it is not a licence.
* **Nothing was removed.** The "Not for sale" and "Free From Government" marks, the names of authors and contributors, the rights notices and the publisher's name are all still in the books. `CONTENT_RIGHTS_AUDIT.md` lists every one of them for a decision.
* **The notice and the copy guard are built and tested** (website and app). They were **pushed to `main` on 2026-10-29 on the owner's instruction (Web `8f68655d`, App `b764e5c`) while this permission question was still open**, so the owner took that decision knowingly: the notice states that rights stay with their owners, it does not make the books permitted.

## 2. The rule for removing anything

1. A "Not for sale" or free-distribution mark, or the name of a person who made the book, may be removed **only if** (a) a written permission of the rights holder for exactly that is filed in `docs/permissions/` **and** (b) removal is legally permitted (a lawyer says so). If either is missing, it stays.
2. **Credits and copyright / rights notices are attribution and stay in every case.** Even with a permission, a person's name is removed only with that person's consent.
3. A mark that is uncertain is flagged, not removed. `CONTENT_RIGHTS_AUDIT.md` and `content_rights_findings.csv` are that list.
4. Removing the stray watermark text from inside the typed pages (see below) also removes the legend, so it follows the same rule.

## 3. What the audit found (`node tools/rights/audit_markings.js --write`; it changes nothing)

322 served data files scanned, 16,606 matches. Pictures (covers, figures) were **not** scanned: their text cannot be searched here and a person must look at them (the covers carry the Textbook Board's mark).

| Category | Matches | Decision |
|---|---:|---|
| Not for sale | 5,807 | flagged, not removed |
| Free distribution ("Free From Government", distributed free, free of cost) | 209 | flagged, not removed |
| Rights notice (All rights reserved, Copyright, the c sign) | 776 | keep |
| Credit (authors, reviewers, editors, translators, illustrators) | 7,320 | keep |
| Board / publisher (Textbook Board, Government of Khyber Pakhtunkhwa) | 2,494 | keep |

The "Not for sale" matches are mostly **the scan's watermark text that ended up inside the typed pages** (5,733 in the older data files, mainly Class 12 Physics and Chemistry: a page footer in the middle of a paragraph), 160 are our own transcription notes ("Not For Sale is printed at the lower right"), and 61 are in the reviewed page books the reader draws. The free-distribution lines are mostly the books' own title-page legend ("Free From Government - NOT FOR SALE - Khyber Pakhtunkhwa Textbook Board Peshawar", 285 lines in 54 files). 97 files carry one of the two marks; 216 files carry a credit line.

## 4. The notice

Shown **once per book** (class + subject) on a device, the first time the book is opened, in the website and in the app (the app shows the same page). The record is kept on the device (`localStorage` `sb.rights.notice.v1`); a new book shows it again; the same book never does; clearing the app's data shows it again. It is a dialog the reader has to close ("I understand", Esc, or "Contact support", which opens the website's "Suggestions and problems" dialog: that is the support channel the notice names). It is accessible (a labelled modal dialog, the page behind it inert, Tab stays inside, buttons 44 px) and it fits a phone on its side.

The words, verbatim from the owner:

> SpaceBook provides an interactive learning environment designed to make education easier and more accessible. Rights in the original textbooks, text, illustrations, and other source materials remain with their respective owners. SpaceBook does not claim ownership of those materials. Subscription charges support the platform’s development, hosting, interactive features, and maintenance; they do not transfer ownership of textbook content or grant reproduction rights. Users may use content only as permitted by applicable law and the relevant licence. Unauthorized copying, redistribution, republication, or commercial reuse is prohibited. For attribution concerns, permission requests, or removal requests, please contact SpaceBook through its support channel.

* It does **not** say or imply that the Government, a textbook board or anybody else has given permission, licensed the books or endorses SpaceBook (a test checks that the words contain none of that). It says the opposite about ownership.
* It is **English only**. Urdu, Pashto and Arabic versions need a reviewed translation of legal wording; they were not machine-translated.
* The "relevant licence" is not defined anywhere yet; with no permission on file there may be none. Ask the lawyer whether that sentence should wait.
* Changing the words means changing `VERSION` in `js/sb_rights.js` so that everybody sees them once more.
* Automated test runs (`navigator.webdriver`) skip it so that the other test suites can click; `tests/reader/rights.js` turns it on.

## 5. The copy guard

In the reader only (the book text and its exercise pages), on the website and in the app:

| Switched off | How |
|---|---|
| Ctrl+C, the browser's Copy and Cut menu entries, Select All then copy | a `copy` / `cut` handler in `js/sb_rights.js` (also checks whether the selection reaches the book, so Select All does not bypass it) |
| Dragging selected text or a picture out of the book | a `dragstart` handler; exercise widgets that are dragged on purpose keep working |
| The Android selection bar's Copy, Cut, Share, Paste and the "process text" entries of other apps (Translate, Search ...) | `ui/web/GuardedWebView.kt` (`ExportFree`), tested by `ExportFreeTest` |

**Kept on purpose:** the text stays selectable; word meanings, sentence translation, read aloud, screen readers and the selection tools work as before; typing fields (notes, the search box, the report form, answer boxes) still copy; the person is told why in a polite status message. Nothing is hidden from screen readers and no `user-select: none` is used.

**Honest limits. This is a deterrent, not protection.** It does not stop, and cannot stop: screenshots or a photo of the screen; retyping; OCR; "view source", saving the page, developer tools; printing; reader or translation tools of the browser that read the page; a browser with scripts switched off; accessibility services that read the screen aloud or to another app; anything done by software on the person's device. The app does **not** set Android's `FLAG_SECURE` (that would blank screenshots and screen recordings of the whole app): the report dialog and support depend on screenshots, and the owner asked not to promise screenshot protection. Nobody should be told that copying is impossible.

## 6. Open legal questions (for the owner and a lawyer)

1. Who holds the rights in each book (the Textbook Board, the Government, the authors) and will they give **written permission** to show and redistribute the books in an app, and under a subscription? File it in `docs/permissions/`.
2. The books say "Free From Government - NOT FOR SALE". Is offering them under a subscription allowed with that legend, without it, or not at all?
3. May the board's and the Government's name and logo (covers, title pages) be shown, and in what wording, so that SpaceBook does not look like the publisher or endorsed?
4. Authors' and contributors' names: keep them as printed (the audit's default).
5. Is the notice enough, is "the relevant licence" accurate while no licence exists, and does it need Urdu / Pashto / Arabic versions?
6. What SpaceBook added (typed pages, answers written for the project, meanings, translations, games) is our work: state who owns it and under what terms.
