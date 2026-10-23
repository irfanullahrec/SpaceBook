# Games (Classes 1–12)

The **Games** tab (header and sidebar, `#games`) is a level-by-level arcade made from the textbooks. Six games, ten levels each; every right answer is a step that earns coins through the existing reward rules.

| Game | What you do | Made from | Classes |
|---|---|---|---|
| 📚 Quiz Quest | pick the right answer, three lives, 50:50 once per level | the MCQ bank (`js/test_prep_bank.js`), easy → hard, per subject | 1–10, 12 (Class 5: the true/false items; Class 11 has no bank) |
| ⚡ True or False | is the statement right? against the clock | the same questions turned into statements (a false one uses a known-wrong option) | as Quiz Quest |
| 🔤 Word Builder | put letters in order to spell the answer; typing works; hint | Classes 1–3: picture words; later classes: one-word answers of textbook questions | 1–4, 6–10, 12 |
| 🃏 Memory Match | look, hide, flip two cards: question ↔ answer (Classes 1–3: picture ↔ word) | short textbook question / answer pairs | 1–4, 6–10, 12 |
| ➕ Math Sprint | quick sums against the clock, one new skill per level, boss level mixes them | made-up sums, every answer computed (never typed in) | 1–12 |
| 🧸 Little Learners | counting, colours, shapes, letters, picture words, patterns | `js/games_vocab.js` (hand-made picture words) | 1–3 |

Where a class has too little material for a game the card says so instead of showing a thin game (a game needs 8 eligible textbook questions; the number of levels grows with the material, at most 10).

## Coins and levels (no new coin rules)

A level is an *activity* of `total` steps (one per question / word / pair). The screen calls `SBRewards.step(key, title, total, i)` when question *i* is answered right **without help** (no 50:50, no hint, first try for Word Builder), and `SBRewards.again(key)` after a passed run of an already finished level. The **server** pays (`api/lib/rewards.php`): +1 per new step, +5 when all steps are done, +2 once a day for replaying a finished level; the usual daily limits apply. Later levels are longer (5 → 12 steps), so they pay more. Nothing about coins is decided in the browser.

Reward key: `cls<N>|g-<game>-<scope>|u<level>|count|<hash>|<steps>`, the same `count` shape the Android games use, so no server change was needed and it works on the server that is live today (`tests/games/content.js` checks every key against the server pattern).

A level is **cleared** when 60 % of its steps are done (read back from the reward record, so it follows the account to every device) or one run reached 60 % (kept in `localStorage` key `sb_games_v1:<user>`, with the chosen class / subject, sound setting, streak). Level *n+1* opens when level *n* is cleared. Stars: 60 % = ★, 80 % = ★★, all = ★★★.

Study features: wrong answers show the book's explanation (`e`); the results list every missed question with the right answer; Urdu / Pashto translations of a question (`qu` / `qp`) open with one tap where the bank has them; picture words show Urdu and Pashto after each answer.

## Files

| File | Role |
|---|---|
| `js/sb_games_content.js` | pure content: Math Sprint ladders (ten skills per class), Little Learners ladders, pools and level plans from the MCQ bank, `levelKey`. Testable in Node. |
| `js/sb_games.js` | the page: hub, level map, intro, the three runners (choice / tiles / flip), results, sound, voice, coins. `window.renderGames`, `window.SBGames`. |
| `js/games_vocab.js` | picture words (emoji, English, Urdu, Pashto), colours, numbers, shapes, names for story sums. |
| `css/sb_games.css` | look (also tightens the header by a few pixels so the sixth tab fits). |
| `tests/games/content.js` | 73,000 checks, 16,000 answers recomputed independently, every game × class × subject built, keys match the server. |
| `tests/games/browser.js` (+ `harness.html`) | plays real levels in the installed Chrome: coins, locking, lives, hint penalty, +2 practice, reload, phone width, console. `--full` runs it on the whole app. |

`app.js` got two lines (`games` in the allowed start pages, and `renderPage` calls `renderGames`); `index.html` got the two nav links, the stylesheet and three scripts.

## Rules to keep

- A new game: add it to `GAMES`/`ORDER`, `planFor`, `buildLevel` in `sb_games_content.js` and, if it needs a new screen, a runner in `sb_games.js`. Report steps with `reportStep`, never call the server yourself.
- Maths questions are generated, so every generator must be correct by construction; add an independent check for a new skill to `tests/games/content.js`.
- Text from the MCQ bank is shown through `rich()` (escaped; `<sup>`/`<sub>` and `$…$` only). Generator output is trusted HTML written in the file.
- Level totals are part of the reward key; changing a ladder's `SIZES` after release changes the keys (old progress stays under the old keys).

## Picture words: review queue

`js/games_vocab.js` is hand-written for the games (not book text). Urdu was written for common nouns; an empty Pashto cell means "not sure". Please have a native reader check the Pashto column (and the Urdu of *aeroplane*, *scissors*, *mouse*) before release, and fill the empty cells.

## Not done / not verified

- **Class 11 and Class 5** have no MCQ bank (Class 5: only true/false), so only Math Sprint (and True or False for Class 5) is playable there.
- Games per **book page** are built: see "Page arcade" below.
- Verified in Chrome through Playwright (hub, map, every game, phone width). Not run: the built-in browser pane (it refuses `localhost`), a real touch device, a screen reader, the service worker with the new files.
- `lazy.html`, `content/offline_map.json`, `content/sw_version.js` must be regenerated from a clean checkout (`tools/build/all.js --only lazy,offline`) before release, because three scripts and one stylesheet were added to `index.html`.

## Page arcade (2026-10-24): fifteen arcade games made from the page on screen

The 🎮 tab on a page's bar (and the **Games** button of the Android app's reader footer) opens an overlay of fifteen small arcade games. They are **not multiple choice**: the student steers, shoots, slices or builds, and every right answer is a word or number of *that page*. A page with too little text to make questions from shows "There are no games on this page" (the owner's rule), never a blank screen.

| Game | The learning is in |
|---|---|
| Subway Surfers, Temple Run, Car Racing | run through the lane / door / gate that holds the right answer; right answers make the car faster |
| Flappy Bird | fly through the gap that shows the right answer |
| Fruit Ninja, Balloon Pop, Bubble Shooter, Angry Birds | slice / pop / shoot / smash the one that holds the right answer |
| Football Penalty | the three corners of the goal hold answers; the right one is a goal |
| Snake | eat the right word to grow |
| Candy Crush | match each clue sweet with its answer sweet; pairs pop and new ones drop in |
| Treasure Hunt | walk the map; each locked gate needs its clue solved |
| Block Builder | solve a challenge to win blocks (stone, wood, glass, door, brick) and build the house |
| Hill Climb Racing | drive; when the tank is low a question appears, the right answer refuels |
| Train Simulator | stop the train in the marked zone, then answer the mission to open the doors |

**Where the questions come from** (`js/sb_arcade.js`, `extract(text)`, pure, tested under node): the text of the page unit (hidden translation lines, buttons and answer panels are removed). Sums the page already prints (`12 + 7 = 19`, only when the arithmetic is right) become "12 + 7 = ?"; a sentence with its most important word (a term the page repeats, a name) or a number taken out becomes a clue; the wrong options are other words or neighbouring numbers of the same page. English, Urdu, Pashto and Arabic text work. A page needs 3 usable questions.

**Coins**: each game on each page is one activity of at most 8 steps; every NEW right answer is a step through `SBRewards.step` with the key `cls<N>|g-pg-<game>-<subject>|u<chapter>|count|<hash>|<steps>` (the shape the server already accepts, `api/lib/rewards.php`), +5 for finishing, +2 for replaying a finished game once a day. Nothing about coins is decided in the browser, no server change was needed.

**Files**: `js/sb_arcade.js` (extraction, overlay, hub, loop, sounds, coins), `js/sb_arcade_runners.js`, `sb_arcade_shoot.js`, `sb_arcade_puzzle.js`, `sb_arcade_build.js` (the games, each `{id, name, emoji, teach, how, make(env)}`). The styles are injected by the script (no extra stylesheet).

**Tests**: `node tests/arcade/play.js` plays every game frame by frame in real Chrome (a clock it controls): a perfect player (`env.auto = 'right'`) must win every game without losing a life, a careless one (`'wrong'`) must lose every game; it also checks the hub, the no-content message, pause, back and close, and takes a picture of each game. `node tests/app/games_in_app.js` opens the arcade the way the Android app does (`SBApp.openGames()`), plays one for a few seconds and checks back / close.

**Adding a game**: write a file like `sb_arcade_runners.js`, register it with `SBArcade.register({...})`, add the script to `index.html`, give it an `env.auto` player in `update()`, and run `tests/arcade/play.js`.

**Not verified**: on a real phone (touch feel, frame rate on a low-end phone, the sound), and the Pashto / Urdu strings of the overlay by a native reader.
