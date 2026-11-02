# UI redesign: coverage of the supplied designs

Source designs: `Downloads\Presentation\WEB UI` (45 desktop screens, 1536x1024) and `APP UI` (50 phone screens, 1024x1536).
Backups made before any change: `D:\SpaceBook\Backups\Before-UI-Redesign-20261030\`.

Status words: **Done** = the layout, colours, icons and artwork follow the design with the real data behind it;
**Partial** = the frame, colours and main blocks follow the design but some blocks of the design are not built yet;
**Open** = still the old layout (restyled by the shared colours and sidebar only).
Numbers, names, dates and prices in the designs are examples: real data stays connected, and no example data is shown as if it were real.

Every screen needs a side-by-side image check. `Evidence` below says which ones were looked at in the browser or on the phone.

## Web (127.0.0.1:8790 locally)

| # | Design | Status | Where | Evidence |
|---|---|---|---|---|
| shell | Sidebar, header, tokens | Done | `css/sb_redesign.css`, `css/sb_design_match.css`, `index.html` | browser |
| 01 | My Study Bank | Done | `js/sb_design_ui.js`, `js/sb_home_plans.js` | browser |
| 02 | News Feed | Open | the website has no feed tab on this branch (it is on `main`) | - |
| 03 | Project Stats | Open | `js/word_stats.js` | - |
| 04 | Choose Your Class | Done | `js/app.js` `sbClassesPageHtml`, `css/sb_classes_page.css` | browser |
| 05 | Class 9 Subjects | Done | `js/sb_pages_enhance.js`, `css/sb_subjects_page.css` | browser |
| 06 | Chapters & Units | Partial | reader chapter list opens with titles (`sb_pages_enhance.js`) | browser |
| 07 | Interactive Book Reader | Partial | `css/sb_reader_shell.css` (frame, tabs, chapter list, page bar) | browser |
| 08-09 | Word / sentence meaning | Open | `js/universal_translate.js` | - |
| 10 | Vocabulary & Word Bank | Open | reader Words tab | - |
| 11-17 | Grammar, exercises, maths solutions, SLOs, practicals, video, drawing | Open | reader tabs | - |
| 18 | Tests Preps | Done | `js/sb_design_ui.js` `preparation`, `css/sb_tests_preps.css` | browser |
| 19-20 | Timed test, results | Open | `js/test_prep.js` | - |
| 21 | Create Test | Partial | three panels (`css/sb_createtest_page.css`); the summary column of the design is the "Test details" card | browser |
| 22-23 | Paper builder / preview | Partial | light control bar and title (`css/sb_papers_page.css`) | browser |
| 24 | Ask SpaceBook | Partial | header, example cards, chat colours (`css/sb_ask_page.css`); the Current Context / Related Questions column is not built | browser |
| 25-26 | Study plan setup / plan | Partial | headings and colours (`css/sb_studyplan_page.css`) | browser |
| 27 | Learning Games | Done | `css/sb_games_page.css` + design artwork | browser |
| 28-29 | Game levels, gameplay | Open | `js/sb_games.js` | - |
| 30 | Grammar & Word Analysis | Open | `js/sb_grammar_stats.js` | - |
| 31 | Saved Library | Done | `js/sb_library.js` `renderSaved`, `css/sb_saved_page.css` | browser (empty state) |
| 32 | Search | Partial | results dropdown styled as a card | - |
| 33-34 | Sign in / Create account | Done | `js/auth.js`, `css/sb_auth_pages.css` (WhatsApp number and father name stay: they are the real account fields) | browser |
| 35 | My Account | Done | `js/auth.js` `openAccount`, `css/sb_account_page.css` (no "Connected devices" block: the server keeps no device list) | built, not yet looked at |
| 36 | Reading & Offline Settings | Open | Settings opens Offline & Downloads | - |
| 37 | Choose a Plan | Done | `js/sb_billing.js`, `css/sb_billing_pages.css` | browser |
| 38 | Plan Coverage | Done | same | not yet looked at with data |
| 39 | Easypaisa Payment | Done | same (real account details; the design's masked ones are not used) | browser |
| 40 | My Plans & Payments | Done | same | needs a signed-in test account |
| 41 | Offline & Downloads | Done | `js/core/offline.js`, `css/sb_offline_page.css` | browser |
| 42 | Curriculum Roadmap | Open | no such page yet | - |
| 43-44 | Administration, content management | Partial | `manage/manage.css` (navy sidebar, cards); the design's charts and content editor are not built | - |
| 45 | Offline recovery | Done | `offline.html` | - |

## App (phone)

| # | Design | Status | Where | Evidence |
|---|---|---|---|---|
| theme | Colours, shapes, status bar | Done | `ui/theme/Theme.kt` | phone |
| 01 | News Feed (Home) | Partial | tab tiles and header (`ui/home/HomeTabs.kt`, `ReferenceDesign.kt`) | phone |
| 02-03 | My Stats, Project Stats | Partial | `ReferenceDesign.kt` (other agent), `HomeTabs.kt` | - |
| 04 | Library | Done | `ui/library/LibraryScreens.kt` | phone |
| 05 | Subject chapter list | Open | `SubjectContent` | - |
| 06-10 | Reader, meanings, notes, read aloud | Open (the reader is the website's page, so it follows the web redesign after the next sync) | - | - |
| 14 | Practice Hub | Done | `ui/practice/PracticeScreen.kt` + cropped artwork | phone |
| 15-29 | Test prep, create test, papers, ask, study plan, games, grammar | These are the website's pages inside the app: they follow the web work above after `sync_app.js` | - | - |
| 30 | Me | Done | `ui/me/MeScreens.kt` | built, not yet looked at |
| 31-32 | Account, settings | Open | - | - |
| 33-34 | Books on this phone, missing book | Open | `ui/offline/*` | - |
| 35-36 | Sign in, create account | Done | `ui/auth/AuthScreen.kt` | built, not yet looked at |
| 37-40 | Plans, coverage, payment, my plans | Website pages (web redesign) | - | - |
| 41-45, 50 | Comments, composer, quiz, reels, lock, recovery | Open | `ui/feed/*`, `ui/play/*`, `ui/lock/*` | - |
| 46-49 | Practical, video, SLO, drawing | Website pages | - | - |
