# The 1-month free trial lock (removed 2026-10-29)

Added on 2026-10-28 and **removed on 2026-10-29 at the owner's request**, when plans and payments arrived (`docs/BILLING.md`): it was a fixed lock that covered the
whole website and app 30 days after the first start and could only be opened with an unlock code. Access is now decided by the free allowance (Chapter 1 of every
subject, 50 Test Preparation questions, 50 Study Plan questions, 1 paper) and the plans a person has bought; nothing locks a person out after a month.

What went with it: `js/sb_license.js`, `css/sb_license.css`, `tools/license/` (the code makers), `tests/license/`, the `acct.trial` parity row, and in the app
`expiry/TrialGate.kt`, `LicenseCode.kt`, `DefaultCode.kt`, `AccessGate.kt` and the trial wording of `ui/lock/LockScreen.kt`. The dated **preview lock** of a preview APK
(`docs/EXPIRY.md`, `-Pspacebook.expireDays=N`) is a different thing and stays.

The full text of the old lock, its unlock codes and tests are in git history (commit b9d137f8 and the commits before this one). Unlock codes already given out and the
private key under `~/SpaceBook-License` are no longer used by anything; the key can be deleted when the owner is sure the lock will not come back.
