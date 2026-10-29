# Plans, payments and access (built 2026-10-29)

One system for the website and the Android app. They share the PHP API and the one MySQL database, so a payment approved once opens the same access on both, and a suspension, a renewal, an expiry or a free extension reaches both. Nobody buys a plan twice. Code: `api/lib/billing.php` (every rule), `api/billing.php` + `api/v2/entitlements.php` (what both platforms call), `manage/` + `api/lib/manage.php` (the administrator's page), `js/sb_access.js` + `js/sb_billing.js` (the website and the app's web pages), the app's `access/AccessRules.kt`. Migration `010_billing`.

## 1. What is free and what is sold

| | Free, no account | Student plan | Teacher plan | Test Preparation module |
|---|---|---|---|---|
| Price, duration | free | PKR 500, 1 calendar month | PKR 500, 1 calendar month | PKR 500, 1 calendar month |
| Chapters | Chapters 1 and 2 of every subject of every class | every chapter of **all subjects of one chosen class** | every chapter of **1 to 10 chosen subjects** (one class or several) | no |
| Study Plan | 50 questions | **included for that class**, unlimited | not included (50 free) | not included (50 free) |
| Paper creation | 1 paper | not included (1 free) | **included for the chosen subjects** | not included (1 free) |
| Test Preparation | 50 questions | not included (50 free) | not included (50 free) | **the complete module**, unlimited, all classes and subjects |

Plans stack: a person may hold a Student plan for Class 9 and another for Class 10, a Teacher plan and the Test Preparation module together. A payment buys one plan; there is no combined cart (each payment record has one plan, one amount, one transaction id).

## 2. Where the rules are enforced (and what that does not cover)

* **The server decides and counts.** The free allowance (50 / 50 / 1) is counted by `sb_consume()` per **person**: a signed-in person is counted by account, a person without an account by the random **visitor id** their browser or phone keeps (`X-SB-Visitor`, cookie `sb_vid`). Signing in or registering brings what the browser had already used (`sb_free_merge`), a signed-in person's use is also written to the visitor, so refreshing, signing out, registering a fresh account, or using the other platform with the same account does not give a new allowance. The same question again costs nothing. Concurrent requests are serialised by a database lock.
* **Chapter 3 and later** are locked by the pages (website and the app's web pages) and by the app's native chapter list, using the server's answer (`access` in `api/v2/entitlements.php`). The textbooks themselves are static files that the website serves to everybody (as it always did and as the offline copies in the app are), so this lock is a product gate, not a vault: a person who edits the page's scripts can read them. Only a different architecture (serving chapters 2+ through PHP after an access check) would change that; it was not asked for and is not built.
* **The owner's pass ("Enter licence key").** A key only the owner knows, for showing the app somewhere: a button under "See plans" on the chapter lock, in the plans window, on Home and in Me > My plans (app). Entered on a device it opens every chapter and lifts the free limits **on that device** (`SBAccess.unlockWithKey` in `js/sb_access.js`; in the app the page tells the phone through `SBHost.setOwnerPass` and `AppViewModel` remembers it, so the native chapter list agrees). "My plans" shows "Owner access is on for this device. Turn off". **The key is written nowhere in the repository**: the code holds only a salted PBKDF2-SHA-256 hash of it (`OWNER_VERIFIER`, 600,000 rounds); five wrong keys in a row wait a minute. The server cannot know the pass, so it is device-side only (Test Preparation, Study Plan and paper counts are simply not asked for on that device) and it is **not protection**: the lock is a screen of the page and the books are files, so anyone who edits the page can skip it, with or without a key. To change the key, make a new salt and hash (`crypto.pbkdf2Sync(key, salt, 600000, 32, 'sha256')`), replace `OWNER_VERIFIER` and tell nobody the key in a commit, a message or a document. A key that follows the pattern of another password (the administrator's first password) is easier to guess from it: choose an unrelated one.
* **Limits of "no account" counting:** a person who clears **all** site data of the browser (or reinstalls the app) gets a new visitor id and a new anonymous allowance. Two devices without an account have two allowances. Creating many visitor ids from one address is rate-limited (120 per hour per address). With an account the allowance cannot be reset this way.
* A cached paid answer on a phone never outlives its end date: while offline the access is worked out again from the saved plans with the device's clock; online the server's answer replaces it at once. Offline free use is counted on the device and sent later; the server's count wins.

## 3. The payment (Easypaisa, approved by hand)

1. The person chooses a plan (Student: a class; Teacher: up to 10 subjects; Test Preparation: nothing), **creates an account or signs in** (the choice is kept in `localStorage sb_checkout` through registration and sign-in; in the app the sign-in is the app's own screen and the window comes back), and the payment window shows: method Easypaisa, account **03456896156**, title **AMIN ALLAH** (each with a Copy button), plan, class or subjects, amount (PKR 500, set by the server, never by the browser), duration, the instructions, **Trx ID (Transaction ID)** (required) and an optional payment date.
2. **Submit Payment for Verification** saves a `payment_requests` row with status **pending** and shows the thank-you text word for word. Submitting never opens access.
3. Safe against repeats: a double tap or a retry after a lost answer returns the request already saved (`idem` key, and the same person + same transaction id); the same transaction id from another account is refused (409); a database unique key (`active_trx`) makes two live requests with one id impossible even in a race; a rejected request frees its id. The id is kept exactly as typed (text, leading zeros kept); comparisons ignore case.
4. In the account page ("My plans", website avatar menu; Me tab in the app) the request shows **Pending Verification**, then **Approved** with the exact start and end, or **Rejected** with the reason.
5. The administrator checks the **real Easypaisa record** (the page says that a transaction id alone is not proof), then **Approve** or **Reject** (a reason is required to reject and the student sees it). Approval is one transaction on the locked payment row, so pressing twice, or two administrators at once, grants once.
6. Approval starts the plan **now** for **one calendar month** (31 Jan + 1 month = 28/29 Feb), storing `starts_at` / `expires_at` (UTC). If the same person already has the **same plan** (same class, same subject list, or the module) still running, the month is added **after its current end date** (early renewal; same subscription, history says `renewed`). After the end date a new subscription starts at the approval time. If the matching plan is **suspended**, approval is refused until an administrator restores it.
7. The student gets a message in the account for every decision (also for extensions, suspensions, restorations and free grants), and expiry reminders (7 days before, and after the end) are shown in the account and on the Me tab of the app. There is no e-mail or WhatsApp sending: nothing in the system has a channel for it.

## 4. The management page

`https://<site>/manage/` (own folder, own login, own session cookie `spacebook_admin`, SameSite=Strict, no JavaScript on the page at all, strict CSP). The administrators are rows of table `admins`, **not** site users: nothing on the public site can sign one in or create one.

* First administrator: username **IrfanUllah123**, created by migration `010` with **only a bcrypt hash** (cost 12) of the agreed initial password; the password is in no file. `must_change_password = 1`: after the first sign-in the only page available is "Change your password" (12+ characters, letters and numbers, not containing the username, different from the current one).
* Sign-in protection: 30 attempts per address per 15 minutes; 5 wrong passwords lock that name for 15 minutes (even the right password is refused meanwhile); one plain message for a wrong password and an unknown name; the session is renewed at sign-in; it ends after 30 idle minutes or 12 hours; every POST needs the session's token and a same-site check; every request re-reads the administrator from the database; all failures and sign-ins are in the audit trail.
* Forgot the password: on the server, `php api/migrate.php admin-reset IrfanUllah123` prints a one-time temporary password (to be changed at the next sign-in). Nothing over HTTP can do this.
* Screens: **Dashboard** (cards, charts, date filter, CSV export, the definition of every number), **Payments** (search by transaction id, reference, name, WhatsApp number; filter by status, plan, date; the detail page with the checks to make, duplicates of the same transaction id, approve / reject), **Users** (search, filter by account state, plan state, platform, date; one person's page: class and subjects, free allowance used, payments, subscription history, suspend / restore the account, give free access), **Subscriptions** (list, suspend / restore each with a reason), **Free extension** (one person, several selected people, or everybody with a matching plan; choose plan and state; add days or set an end date; **preview who is affected**, then confirm with a reason: the confirmation is tied to the previewed list by a hash and refused if the list changed), **Audit trail** (who, when, what, why, from which address), **Password**.
* Every change an administrator makes is written to `admin_audit` in the same transaction (before / after dates, reason, the administrator's name). Suspending an account (existing `users.status = 'blocked'`) ends its devices' access at once; a restored account signs in again.

## 5. The numbers on the dashboard (defined on the page too)

Registered account = a non-deleted `users` row (administrators excluded). Verified revenue = amount of **approved** payments on the day of approval. Hit = one tracked action (a question answered in a limited module, a chapter or tool opened) sent by the website or the app; administrators and known bots (crawler or empty browser name) are not counted. Active people (day / 7 / 30 days) = distinct registered people with a hit. Anonymous visitors = distinct browsers or phones with hits that never signed in: an **estimate**. Sign-up to purchase = accounts created in the dates with at least one approved payment, over all created in them. Popular classes / subjects / modules = hits per key. Free-limit use = requests the server refused at the limit, purchase windows opened, people who used the whole allowance.

## 6. Both platforms

| | Website | Android app |
|---|---|---|
| Plans, payment window, My plans | `js/sb_billing.js` | the same window inside the app's web page (`SBApp.openPlans`, `openMyPlans`); the sign-in is the app's own screen |
| Chapter lock | `js/sb_access.js` hooks on `renderSubjectChapterView`, `renderMathChapter`, the Study Plan sheet | the same hooks (the app runs the website's page) + a lock on the native chapter list + the reader is never opened for a locked chapter |
| Test Preparation / Study Plan / paper limits | `test_prep.js`, `sb_mastery.js`, paper hooks call `SBAccess.useQuestion` | same pages |
| Plan card, expiry, pending | avatar menu > My plans | Me tab, "My plans" card |
| Rules shared by test | `tests/parity/access_contract.json` | the same file (copied by `sync_app.js`) in `AccessRulesTest` |

## 7. Tests

`php tests/php/run.php` (billing section: seed administrator, free limits, payment submit, duplicates, approve / reject, renewal, month end, expiry, suspension, extensions, the management page over HTTP, CSV, the shared contract), `node tests/access/unit.js`, `node --max-old-space-size=8192 tests/access/browser.js` (a real Chrome on a throwaway database: locked chapter, plans, register, payment, Pending Verification, approval opens the chapter, suspension, Test Preparation and paper limits, phone width), the app's `AccessRulesTest` and `NetworkTest`.

## 8. Decisions taken where the request left a scope open (please confirm or change)

1. **Test Preparation module** = the complete module for **all classes and subjects**, unlimited questions (it is not tied to a class).
2. **Study Plan under the Teacher plan**: not included (only the free 50 questions); the request lists it for the Student plan only.
3. **Teacher plan**: 1 to 10 subjects (not exactly 10); the paper limit is lifted for exactly those subjects.
4. **A "paper" is counted when it reaches the review stage** (or is printed), once per class + subject + paper type; changing Set A / B / C or shuffling the same paper costs nothing more.
5. **One payment = one plan.** Buying a Student plan and Test Preparation means two payments (two transaction ids).
6. **Reading a chapter inside the Study Plan sheet** follows the same chapter rule as the book pages.
7. **Under-payment**: the price is fixed at PKR 500 and shown to the person; if Easypaisa shows a smaller amount the administrator rejects with a reason.
8. **Notices are in the account only** (no WhatsApp / e-mail).
9. **The 30-day trial lock was removed** on 2026-10-29 at the owner's request (`docs/TRIAL_LOCK.md`): it was a fixed lock from before the plans, it would have locked paying students after day 30, and nothing replaces it: access is the free allowance plus the plans.

## 9. Owner steps after the deploy

1. The first request after the deploy applies migration 010 by itself (as always). Open `/manage/`, sign in as `IrfanUllah123` with the initial password and **change it straight away**: until then the account exists with the known initial password.
2. The agreed initial password is **the same string as `db_pass` in the local (git-ignored) `api/config.php`**, which is how it was found (a check that no tracked file contains the password). If the live database uses that password too, note that the repository is public and now holds a bcrypt hash of it: slow to guess, but it is a database password. **Change the database password** (cPanel, then the `DB_PASSWORD` secret) and do not reuse one password for both.
3. The old trial lock is gone from the website and the app; people who were locked on the live site open again with the next deploy and app update.
4. Give a copy of this page's section 4 to anyone who will approve payments; an extra administrator is a row in `admins` (ask for a command to create one).
