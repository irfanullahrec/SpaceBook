# Prompt: Build the new SpaceBook Android app (Kotlin)

You are building a brand-new native Android app (Kotlin, Jetpack Compose, Material 3) for **SpaceBook**, an education platform whose web version lives at https://wantuch.pk/spacebook. The source of truth for behaviour and content is the web project in `D:\SpaceBook\SpaceBook Web` (read `docs/HANDOVER.md`, `docs/06_PROJECT_AUDIT*`, `js/`, `php/` first).

## 0. Clean start
- Inspect `D:\SpaceBook\SpaceBook App`, list what is in it, then delete the entire folder contents (the owner rejects the old app and its UI). Create the new project at the same path.
- Package `pk.wantuch.spacebook`, minSdk 24, targetSdk latest, Kotlin + Compose, Hilt, Retrofit/OkHttp, Room (offline cache), WorkManager, Coil, Media3.

## 1. Live data & database (IMPORTANT security rule)
- The app must work live against the same MySQL database the web uses (cPanel DB `tafseelk_spacebook`). Plans, progress, coins, study plans, accounts and test results written from the app must appear on the web and vice versa.
- **Never put database host/user/password inside the APK** (an APK is trivially decompiled and the DB would be exposed). Instead the app talks to the existing PHP endpoints on wantuch.pk/spacebook (progress.php, study_plans.php, auth, payments…) over HTTPS. Add any missing JSON endpoints in the web `php/` folder, reading DB credentials from the server-side config / environment only. The owner supplies the DB password server-side; it must not be written into this repo or the app.
- Use token-based auth (short-lived access token + refresh), HTTPS only, certificate pinning optional.

## 2. Access model
- App opens straight into content with **no login required** (guest mode). Guest progress is stored locally and merged on login.
- Also include Register / Login / Logout / forgot password, profile, and class selection.
- Feature gating must come from one server-side "entitlements" source (payment plans). Whatever the web plan allows, the app allows; changing a plan in web or DB is reflected in both. Currently everything is unlocked; build the gate hooks now so limits can be switched on later without an app update.

## 3. Book reading
- Web uses a two-page spread on large screens; the app uses **single-page view** (swipe/tap to turn pages, pinch-zoom, page jump, bookmarks, continue where left off).
- Each page must look exactly like the printed/PDF page: fonts, sizes, colours, highlighted topics, boxes, exercises, diagrams, charts, graphs, shapes, maths (KaTeX/MathJax-quality), tables, RTL Urdu/Pashto/Arabic. Reuse the web page data (`CLSn_BOOKS`, page modules, SVG/figures) and render through a WebView per page or a native renderer that matches pixel-for-pixel; verify against the web on several books (Class 1 → 12).
- Preserve book-order structure per chapter: Lessons → Summary → Exercise → practice, plus the sticky page tabs (Board SLOs, Exercise, MCQs, SQs, LQs).

## 4. Port every web function (read the web fully first)
Study all of `js/` and list every function and event (hover, click, long-press, selection) and re-design for touch:
- Word meaning (tap/long-press a word) and sentence meaning (tap a sentence → EN / UR / PS lines, plus Arabic via the universal translator), fully offline lexicon.
- Language/medium handling (Urdu/Pashto/Arabic/English labels), no language drop-downs on the reading UI.
- Interactive MCQs (radio options, correct/wrong feedback), topic practice panels, exercise answers, step-by-step and vertical board-style solutions, animated visual-reasoning solutions for maths (vr_engine), page animations and activities (e.g. Class 1 trace/drag worksheets).
- Test Preps (MCQ bank, BISE Swat board centre), Study Plans + reminders (local notifications), Reward coins/progress, Word Stats / My Stats, search, bookmarks, notes/highlights.
- Port as a shared spec: write a feature-parity checklist and tick each item.

## 5. Study environment = social-feed style (Facebook-home inspired, but better)
- The Home and every study surface (page reading, exercises, solutions, test-prep review, study-plan items) is a vertical **feed of cards**, like Facebook's News Feed: author/subject header, content, reaction/action bar (like, save, share, explain, practise), comments/notes.
- It must look more attractive than Facebook, Instagram and X posts while staying distinct from them: unique SpaceBook identity, rich subject colours, big readable type, soft depth, micro-animations, smooth transitions, story-style continue-learning row at the top.
- Other screens (settings, plans, profile…) can use any good Material 3 layout.

## 6. UX
- Very easy for Class 1–3 children and equally good for Class 12: large touch targets, icon-first navigation, friendly mascot/illustrations, voice read-aloud, simple language, dark/light, accessibility (TalkBack, font scaling).
- Fast, offline-first caching of downloaded books; low-end device friendly (2 GB RAM).

## 7. Games tab
- Every page has a **Games** tab (placeholder now). Define the interface `PageGame(pageId, content) → coins` so a simple, page-related game (matching, quiz, drag-drop, word build) can be added later; completing it teaches the page content and awards coins through the same rewards API as the web.

## 8. Deliverables & process
1. Architecture doc + feature-parity checklist in `D:\SpaceBook\SpaceBook App\docs`.
2. Working Gradle project, debug APK, unit + UI tests, screenshot comparison against the web for sample pages.
3. Keep working to the end without stopping to ask "continue?"; commit only your own files; do not push (the owner pushes after all phases).
