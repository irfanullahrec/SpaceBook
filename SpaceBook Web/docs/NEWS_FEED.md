# News Feed

Added 2026-10-26. The first tab of Home, on the website and in the Android app: students read each other's posts, like, comment (with replies), share a
post into their own feed or out of the app, report a post and delete their own. Both platforms use the same endpoint and the same tables; only the look
differs (`PARITY_MATRIX.md`, rows `social.*` and `ui.hometabs`).

## What a student can post

| kind | words | card (stored as small JSON) |
|---|---|---|
| `text` | required, 2-1500 characters | none |
| `question` | required | optional: subject, class, chapter |
| `stats` | optional | My Stats: questions, accuracy, minutes, streak, sessions, words, plans, up to 6 tests |
| `progress` | optional | the day: date, questions, right, minutes, goal, coins, streak, tasks done / total |
| `plan` | optional | a study plan: name, label, subjects, days, tasks, done (the server adds `pct`) |
| `share` | optional, up to 500 | none; points at the original post (a share of a share points at the original) |

The card is **made by the client from the student's own records** (Tests Preps, Study Plans, Word Stats of this browser or phone), never typed in, and
**rebuilt by the server from a whitelist of fields** (`sb_feed_attach_clean` in `api/lib/feed.php`): unknown fields are dropped, numbers clamped, texts cut.
A short plain post (up to 90 characters, one line) is drawn big on a colour, as a feed does with a few words.

## Tables (migration 008, `api/migrations/008_feed.sql`, down script `008_feed.down.sql`)

`feed_posts` (kind, body, attach_json, shared_id, counters, status `visible | hidden | removed`), `feed_comments` (post, parent, body, like_count, status),
`feed_post_likes`, `feed_comment_likes` (one row per student, so a like cannot count twice; real foreign keys), `feed_reports` (one per student per
post or comment). Counters live on the rows and change in the same transaction as the row they count. Deleting an account removes its posts, comments,
likes and reports by cascade; a share whose original is gone says so. Additive only: no existing table changes.

## The endpoint: `api/feed.php`

`list` (`before`, `limit`, `mine=1`, `kind=question`), `post`, `comments`, `create`, `share`, `like` (idempotent: `on` true or false), `comment` (with
`parent` for a reply; a reply to a reply sits under the same comment), `delete`, `comment_delete`, `report`. The golden file of every answer and request
is `tests/parity/feed_contract.json`; the PHP test checks the real answers against it, the app's `FeedLogicTest` and the website's `tests/feed/cards.js`
read the same shapes. Authentication is the same as `api/v2/sync.php`: a device token (the app) or the session cookie (the website; a write must then be
same-site). **Reading needs a signed-in student too.**

## Safety (the readers are school students)

* **Who is who.** Another student is shown as the first name and the first letter of the last word ("Ali K."); a school account shows its own name; a
  teacher or school gets a tick. The avatar is the initial on a colour made from the account number (`crc32('sbfeed' . id) % 360`). No number, father
  name, e-mail or account id is ever in an answer (a test searches the answers for them).
* **What may be written.** Valid UTF-8; control characters and direction overrides removed; a post over 1500 characters (comment 500) is refused, not cut;
  an e-mail address, a phone number (10 or more digits in a run, a list of single digits is fine) or a link is refused with the reason
  (`sb_feed_screen_text`). The same text twice within two minutes is refused (a double tap). Both clients escape text when they draw it, the administrator
  page too.
* **Limits per student:** 12 posts or shares an hour, 60 comments, 300 likes, 30 reports, 60 deletions, 240 reads a minute (`sb_rate_hit`).
* **Reports.** One per student per post or comment. **Three different students hide it at once** (`SB_FEED_HIDE_AT`) until an administrator restores it
  (its reports are cleared) or removes it: `api/admin.php?v=feed` (administrators are made on the command line, `php api/migrate.php make-admin <number>`);
  every restore and removal is in `audit_log`. A blocked or deleted account's posts leave the feed.
* **Delete.** The author deletes their own post or comment at any time (the row stays with status `removed` so shares of it read "no longer there").
* **The export of a student's data** (`api/auth.php?action=export`) holds their own posts and comments.

## Decisions for the owner (also in `parity.json`, `ownerDecisions`)

1. **Moderation level.** Today: three reports hide a post, links / phone numbers / e-mail addresses are refused, authors are abbreviated. For a children's app the
   owner may want more: posts shown only after a teacher approves them, a word filter in Urdu, Pashto and English (none exists), posting only inside one's
   own school, or no posting for the youngest classes. Any of these is a change in `api/lib/feed.php` only; both clients follow.
2. **Who reads.** Only signed-in students. Opening it to guests is one condition in `api/feed.php`, but then anybody who finds the address can read every post.
3. **Who watches.** Somebody has to look at `admin.php?v=feed` regularly; there is no e-mail or message when a post is hidden.
4. **Names.** Accounts carry the real name the student typed at registration; the feed shows first name and one initial. If students should pick a
   nickname instead, it is one more column and a setting in My Account.
5. **Retention.** Posts are kept until deleted. A purge of old posts (for example after a year) is not written.

## Where things are

| | Website | Android app |
|---|---|---|
| the page | `js/sb_feed.js` (tab added to Home by hooks on `renderHome` and `switchHomeStatsTab`) | `ui/feed/` (`FeedScreen`, `FeedPostItem`, `FeedCardsUi`, `CommentsSheet`, `ComposerSheet`, `FeedViewModel`), tabs in `ui/home/HomeTabs.kt` |
| talks to the server | `fetch('api/feed.php')` with the session cookie | `data/repo/FeedRepository`, `ApiService` (device token) |
| cards from the student's records | `SBFeed.cards` | `data/feed/FeedCards.kt` (`FeedCardBuilder`) on the `PrepSnapshot` of `assets/prep_summary.js` |
| offline | the newest page is kept in `localStorage` (`sbFeedCache:<id>`, removed at sign-out) | the newest page is kept in `filesDir/feed_cache_<id>.json` (removed at sign-out) |

## Tests

* `php tests/php/run.php` (`tests/php/feed_tests.php`): migration up and down, who may read and write, privacy of every answer, text rules, the four cards,
  paging, likes, comments and replies, shares, deleting, reports and hiding, the administrator page, blocked accounts, session and CSRF, rate limits, export
  and purge, and the golden file.
* `node tests/feed/cards.js`: dating of posts, the cards from a student's records, escaping.
* `node --max-old-space-size=3072 tests/feed/browser.js`: the page in a real Chrome against the real API (local only).
* App: `FeedLogicTest`, `FeedViewModelTest` (a fake server that speaks the API), `FeedUiTest` (Compose, Robolectric), `FeedScreenshotTest` (pictures in
  `app/build/screenshots`).
