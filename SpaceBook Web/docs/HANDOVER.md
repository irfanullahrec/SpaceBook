# Handover (2026-10-20): what the agent plan delivered, what is yours to decide, what nobody has checked

Nothing has been pushed. Everything below is on the local branch `phase/p2-server` (chain: `wip/2026-10-19` -> `phase/p0-security` -> `phase/p1-safety-net` -> `phase/p2-server`). `PROGRESS_LOG.md` has one entry per piece of work with a "Verified by" and a "Not verified" line each; this page is the short version.

## What was built, by phase

| Phase | Delivered | Where to read |
|---|---|---|
| 0 Security and deploy | the upload zip never carries `config.php`; strict FTPS; live checks; steps for you | `PHASE0_SERVER_STEPS.md` |
| 1 Safety net | `validate` (1,000+ checks), `smoke`, a tracer, a CI gate, a rewritten CONTRIBUTING | `CONTRIBUTING.md` |
| 2 Accounts and sync | migrations 001-006, hardened login, device tokens, `api/v2/sync.php`, coins decided on the server, plans and Tests Preps on the outbox, account screen, consent, backups, **administration** | `PHASE2_SYNC_DESIGN.md`, `BACKUP_RESTORE.md`, `ADMIN.md` |
| 3 Lazy loading | the start page loads in ~0.2 s and ~20 MB instead of 7.5 s and 1 GB; one build command; content-hash URLs | `PHASE3_LAZY_LOADING.md` |
| 4 Offline | service worker, hash-checked "Download for offline", device voices only | `PHASE4_OFFLINE.md` |
| 5 Rendering core (first part) | 109 hand-made function wrappers replaced by `SBHooks`; registry locked by a test | `PHASE5_HOOKS.md` |
| 6 Content integrity | answer keys never default to A; fake videos and dead PDF links removed; generated "Board SLO" practice behind a flag | `CONTENT_REVIEW.md` |
| 7 Meanings | one generated offline lexicon; nothing sent to Google or MyMemory | `PHASE7_LEXICON.md`, `LEXICON_COVERAGE.md` |
| 8 Security surface | header template, report-only content-security policy, threat model | `PHASE8_SECURITY.md`, `SERVER_CONFIG.md` |
| 9 Modules | Papers draw from the books of their class (most classes now have none), Set A / B / C are real, Test Prep review queue, administration | `CONTENT_REVIEW.md`, `ADMIN.md`, `PROGRESS_LOG.md` |
| 10 Cleanup | 7.2 GB of scratch files moved (not deleted) to `SpaceBook_Archive/` | `CLEANUP_LOG.md` |
| 11 Performance | measured against every budget; the one fix that matters is built and **off** (`lazyCards`) | `PERFORMANCE.md` |
| 12 Accessibility, search, docs | keyboard and screen-reader basics, AA contrast, axe-core on 15 views, search inside the books (offline), handover documents | `ACCESSIBILITY.md`, `SEARCH.md`, `ARCHITECTURE.md`, `DATA_CONTRACT.md`, `RELEASE_AND_ROLLBACK.md`, `PROTECT_LIST.md` |

## 2026-10-23 addendum: one product on two platforms

The website and the Android app are now kept the same by tooling, not by memory: `docs/PARITY_MATRIX.md` (generated from `docs/parity.json`), `tools/parity/check.js`, `tools/parity/data_parity.js`, `tools/app/sync_app.js`, `tests/sync/parity_e2e.js`; see ARCHITECTURE section 11. New for students on both platforms: bookmarks, notes and highlights, the Saved list, "continue where you left off" (chapter, tab and page) and "my class" on the account (migration 007, `item.put` / `item.del`); study reminders as phone notifications; search inside the books, the Games arcade and My account in the app. New decisions are at the end of `docs/PARITY_MATRIX.md` (the sync switch, the password-reset channel, the other session's Home work, per-page quests, Quick Quiz).

## Decisions that are yours

1. **Push, and when.** `RELEASE_AND_ROLLBACK.md`. A push to `main` deploys and applies migrations 002-006 to the live database: take a dump first.
2. **Your server steps** (`PHASE0_SERVER_STEPS.md`): delete the leaked zip, `Options -Indexes`, rotate the database password, point the FTP account at `public_html/spacebook`, make the repository private.
3. **`deploy/spacebook.htaccess`**: install it (headers and a report-only policy).
4. **Generated "Board SLO" questions** (about 1,860 template items in Class 9 / 10 Maths, plus one per English unit): hide them for good (`hideGeneratedSlo`) and rename the labels from "Board" to "Textbook practice" until you supply an official SLO list.
5. **Papers for most classes are empty now** (they used to print Class 9 questions). Do you want question banks built for them from the textbook exercises?
6. **English videos** (the same three MP4s on every chapter): which chapter are they from? **Cayley and 1860** in the Class 9 Maths lesson: is that the book's text?
7. **Translation work**: the lexicon covers 84 % (English to Urdu), 79 % (to Pashto), 63 % (to Arabic) of word occurrences; the queues of the most frequent missing words are in `docs/lexicon_review/`. `docs/test_prep_review/no_key.csv` lists 81 questions that need an answer key.
8. **A signing key and a licensing model** (`PHASE8_SECURITY.md`) or "free for everyone, no licensing".
9. **A password-reset channel** (there is none), **an off-site backup destination**, **PHP 7.4 or 8** on the host, **a second step for administrators** if you want one.
10. **Fonts**: permission to download open-licence Noto fonts for Urdu / Pashto / Arabic (reading currently depends on the device's fonts).
11. **Turn on** the things that are off until you have seen them work: client sync (`sb_sync_v2`), `lazyCards` (`PERFORMANCE.md`), `hideGeneratedSlo`.

## What nobody has checked

- **Nothing was run in a real browser** (the built-in browser pane refused local addresses; the Playwright baseline in `tests/baseline/run.js` has never run). Everything was tested in Node: a vm sandbox for the app's logic, jsdom for DOM behaviour, axe-core in jsdom, a built-in PHP server against a throwaway MySQL. That covers logic and markup, not layout, colour as drawn, touch, fonts, speed on a phone, or the service worker's real lifecycle.
- **PHP 7.4 and MySQL 5.7** (what the host runs): the tests ran on PHP 8.2 / the local MySQL; the code avoids PHP 8 syntax (`tools/php74_lint.js`), but the CI job for 7.4 has not run on GitHub.
- **The GitHub workflow itself** has never run: expect the first run to find differences between the machines (Node, PHP and MySQL versions, case-sensitive paths).
- **Screen readers** (NVDA, TalkBack, VoiceOver) and **colour contrast of text whose background comes from a parent or a gradient**.
- **Low-end phone performance**: unknown. In CPU terms 41 of 9,698 tabs take over 150 ms and a Class 11 Maths lesson is 10.8 MB of HTML (`PERFORMANCE.md`).
- **The content-security policy is report-only.** Enforcing it needs the Phase 5 refactor (418 inline handlers, `eval`, 19 `MutationObserver`s).

## What is not done

The unified Book Content Contract and registry-driven `openSubject`; the second half of Phase 5 (observers, injected styles, `!important`, one render pass); the tab model for every chapter (TAB-01); per-row provenance for the lexicon and the interaction component; signed releases, licences, device activation and watermarking (your decisions); Papers question banks for the classes without one; statistics per subject and class; deleting superseded data files (needs real-browser traces) and the 114 unreferenced covers; `git gc` (needs a backup of `.git` first). Each is explained in the document of its phase.

## Work from another session that is NOT in these commits

The working folder also holds unfinished Class 1 / Class 2 interactive work by another session (`js/cls1_*.js`, `js/cls2_play_*.js`, their `<script>` lines in `index.html`, `js/english_1_book.js`, `docs/source-verification/class-1/tools/figs1.py`). None of it was committed here and none of it is in the generated files. When it is committed, the lazy page, the offline map and the search index must be regenerated from a clean checkout (`RELEASE_AND_ROLLBACK.md`, section 1) and the Class 1 / 2 HTML baseline will change.

## Before you push: the short list

1. Server steps done (item 2 above). 2. A fresh database dump. 3. `node --max-old-space-size=8192 tools/build/all.js --check` says fresh for every step, from a clean checkout of the commit you push. 4. Read the "Not verified" lines of the entries you care about in `PROGRESS_LOG.md`. 5. After the deploy, do the real-browser checks in `RELEASE_AND_ROLLBACK.md`, section 3.
