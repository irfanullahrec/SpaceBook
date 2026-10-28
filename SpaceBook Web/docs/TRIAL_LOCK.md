# The 1-month free trial lock (website and app)

Added 2026-10-28 on the owner's request: **30 days after the first start, SpaceBook (website and app) shows only a lock screen** that asks the person to
**contact the developer on WhatsApp 0343 0155606**, or to type an **unlock code**. Their progress and notes on the device are kept.

| | Website | Android app |
|---|---|---|
| Code | `js/sb_license.js` + `css/sb_license.css` (first script of `index.html`) | `expiry/TrialGate.kt`, `LicenseCode.kt`, `AccessGate.kt`, `ui/lock/LockScreen.kt` |
| Where it remembers | the browser's `localStorage` key `sb.lic.v1` | `SharedPreferences` `sb_trial` |
| Trial length | `CFG.trialDays = 30` (0 = lock off) | `BuildConfig.TRIAL_DAYS`, `-Pspacebook.trialDays=N` (default 30, 0 = off) |
| Contact | `CFG.contactLocal` / `CFG.contactWa` | `Contact.LOCAL` / `Contact.WHATSAPP` |
| Inside the app's WebView | the page does nothing there (`window.SBHost` exists): the app has its own gate | – |

The same unlock codes work on both. Nothing is sent to the server: the lock needs no internet and does not touch the database.

## What the person sees

* Days 1 to 30: the app works. On the website a small notice appears in the last 7 days ("Free trial: 5 days left…", closed with OK, back the next day).
  The app shows the days left in Me > Free trial and on the Home account card.
* After day 30: a full-screen lock with the title *Your 1-month free trial has ended*, an Urdu line, a green **Contact the developer on WhatsApp: 0343 0155606**
  button, **Your device ID: ABCD-EFGH** with a Copy button, and a box **I have an unlock code**. The WhatsApp button opens
  `https://wa.me/923430155606` with the message "Assalam o Alaikum. My SpaceBook free trial has ended. My device ID is ABCD-EFGH. Please unlock it."
* Five wrong codes block the box for a minute, then two, four, … up to an hour.
* The website lock covers the whole window, makes the page behind it `inert` (no click, no Tab, no screen reader reaches it) and keeps Tab inside the
  lock. A page left open locks itself when the day passes; unlocking in one tab unlocks the others.

## The default unlock code (the quick way)

The owner has one **default unlock code**. Type it into **I have an unlock code** (website) or **Unlock code** (app) and the lock opens for **30 days from
that moment**. After 30 days the lock comes back and the same code is typed again (each time gives a new 30 days from then). It is case-sensitive; spaces
around it are ignored. It needs no internet and no tool.

* Only a salted PBKDF2-HMAC-SHA256 hash (100,000 rounds) of the code is in the repositories (`CFG.defaultCode` in `js/sb_license.js`, `DefaultCode.kt` in the
  app), never the code itself, and it is **not** written in this document.
* **Weak point, said plainly:** the repositories are public, so anyone can copy the hash and try to guess the code offline, and anyone who hears the code can
  use it (a student can pass it round). A long, unusual code is much safer than a short guessable one; do not use it for anything else (email, banks, other
  sites). For a person you do not want to give the shared code to, make a **signed code** for their device (below): it works on that device only.
* **Change the code:** `node tools/license/make_default.js "NEW CODE"` prints the salt and hash; paste them into `CFG.defaultCode` (`js/sb_license.js`) and
  `SALT` / `HASH` (`DefaultCode.kt`), then release both. `node tools/license/make_default.js --check "THE CODE"` says whether a code matches the hash in
  **both** files. Phones and browsers that already typed the old code keep their month; new months need the new code.
* **Change the 30 days:** `grantDays` (`js/sb_license.js`) and `DefaultCode.GRANT_DAYS`.

## HOW TO UNLOCK A PERSON WITH A SIGNED CODE (the part you do, for one device or longer)

1. The person sends you the **device ID** (it is in the WhatsApp message the button prepared, and on the lock screen).
2. On your PC, in the folder `SpaceBook Web`, run

   ```
   node tools/license/make_code.js ABCD-EFGH
   ```

   It prints one long code (starts with `SB1-`). Other forms:

   ```
   node tools/license/make_code.js ABCD-EFGH --days 365          valid 365 days from today (then the lock comes back)
   node tools/license/make_code.js ABCD-EFGH --until 2027-12-31   valid to the end of that day (UTC)
   node tools/license/make_code.js --any                          works on EVERY device: whoever has it can use it, keep it private
   node tools/license/make_code.js --verify SB1-...               read a code back (which device, until when)
   ```

3. Send the code to the person on WhatsApp. They paste it into **I have an unlock code** (website) or **Unlock code** (app) and press **Unlock**.
   Spaces and line breaks that WhatsApp adds are ignored. The device stays unlocked, also after a restart.

A code is for **one device ID** (so a code cannot be passed round), unless you make it with `--any`. If the person clears the site data or reinstalls
the app, they get a new device ID and a new month; ask them for the new ID and make a new code.

**Your own phone and PC:** do the same with your own device IDs (or one `--any` code for yourself, kept private).

## The key (very important)

Codes are signed (ECDSA P-256) with a **private key that lives only on your PC**:

* `C:\Users\Shehroz Khan\SpaceBook-License\private_key.pem` (the tool reads it by default) and a backup copy in `D:\SpaceBook-License\private_key.pem`.
* It is **not** in any git repository and **not** in the zip files. Keep it secret and back it up. Anyone who has the file can make codes.
* The website and the app contain only the **public** key, so reading the source code (the repositories are public) does not let anyone make a code.
* If the file is lost you cannot make new codes. Fix: `node tools/license/make_code.js --init --key <new file>`, paste the printed public key into
  `CFG.publicKey` of `js/sb_license.js` and `PUBLIC_KEY` of `LicenseCode.kt`, release both, and re-issue codes (old codes stop working).
* On another PC: copy the file to `%USERPROFILE%\SpaceBook-License\private_key.pem`, or point to it with `--key FILE` or the environment variable `SPACEBOOK_LICENSE_KEY`.

## Changing the rule

* **Length:** `trialDays` in `js/sb_license.js`; for the app build with `.\gradlew.bat :app:assembleRelease -Pspacebook.trialDays=60`.
* **Switch it off** (for example in a build for yourself): `trialDays: 0` / `-Pspacebook.trialDays=0`.
* **Contact number:** `contactLocal` and `contactWa` (country code, no `+`, no leading 0) in `js/sb_license.js`; `Contact` in `AccessGate.kt`.
* After editing the website script: raise its `?v=` in `index.html` and run `node --max-old-space-size=8192 tools/build/all.js` (lazy page, service worker), then
  `tools/app/sync_app.js` for the app.
* The older **dated preview lock** of a build (`docs/EXPIRY.md` of the app) still exists, but a release build no longer carries a build date by default
  (`-Pspacebook.expireDays=0`), so the person's own 30 days are the only clock. A signed code for the phone opens both.

## When the 30 days start

At each person's **first start after this version is live** (not at the build date): the website records it the first time the page loads in that browser,
the app the first time it starts on that phone. People who already use the site get a fresh 30 days from then.

## Honest limits

This is a lock that lives on the person's own device, so it stops ordinary use but not a determined person:

* clearing the site's data, a private window, another browser or reinstalling the app gives a new month;
* someone who edits the page in the developer tools, or a rooted phone, can remove the lock;
* moving the clock **back** does not help (the latest time ever seen is kept), but a clock moved far **forward** by mistake locks the device until you issue a code.

A lock that cannot be bypassed has to be decided by the server (accounts with a "paid until" date in the database, checked on every request). That is
possible later on top of this (`api/v2/entitlements.php` already has the place for plans); it would not work offline, which the app is built for.

## Tests

* `node tests/license/unit.js` – codes, dates, device IDs, the trial clock, the default code, and the tools `tools/license/make_code.js` / `make_default.js` against the page's checker (40 checks).
* `SB_PAGE=lazy.html node --max-old-space-size=3072 tests/license/browser.js` – in Chrome: first visit, day 25 notice, day 31 lock (covers the window, the
  background inert, Tab stays inside, buttons 44 px, WhatsApp link with the device ID), wrong and right codes, a code for another device, a code that ended,
  a clock moved back, the default code (30 days from typing, remembered after a reload, gone from storage, the lock back after the month, the notice in its last days), the app's WebView, a phone-size screen (36 checks).
* App: `TrialGateTest`, `LicenseCodeTest` (codes and the default-code hash made in node are accepted in Kotlin; the trial clock; the default code for 30 days; both locks together), part of `:app:testDebugUnitTest`.
