# Phase 0: server steps for the owner

You do these steps yourself in cPanel on wantuch.pk (account `tafseelk`). Do them in this order. The agent does not touch the server.

## 1. Delete the leaked package (do this first)
cPanel > File Manager > `public_html/spacebook/` > select `spacebook_upload.zip` > Delete. Tick **"Skip the trash and permanently delete"**, because the trash also lives inside your account.

Check: `curl -I https://wantuch.pk/spacebook/spacebook_upload.zip` must return `404`.

## 2. Turn off directory listing
In `public_html/spacebook/`, create or edit `.htaccess` and add this line at the top:

```
Options -Indexes
```

Check: `https://wantuch.pk/spacebook/` must no longer show a file list. It should show 403, or the app once step 5 is done.

## 3. Rotate the database password
1. cPanel > MySQL Databases > Current Users > `tafseelk_spacebook` > Change Password. Generate a new strong password.
2. Edit `public_html/spacebook/api/config.php` in File Manager and set `db_pass` to the new password.
3. GitHub > irfanullahrec/SpaceBook > Settings > Secrets and variables > Actions: update `DB_PASSWORD` to the same new password.
4. Locally (XAMPP), use a **different** password in `D:\SpaceBook\SpaceBook Web\api\config.php` and for your local MySQL user.

## 4. Check whether the leak was used
cPanel > Metrics > Raw Access: download the log for wantuch.pk and search it for `spacebook_upload.zip`, from 2026-10-19 06:44 onwards. Also check cPanel > Security for any MySQL or phpMyAdmin logins you don't recognise. If the zip was downloaded by anyone else, treat all user records in the database as exposed.

## 5. Fix the FTP folder (the cause of the failing deploys)
The GitHub deploy uploads without errors, but the website returns 404 for `index.html`. That means the FTP account `spacebook@wantuch.pk` is rooted in some other folder.

cPanel > FTP Accounts > find `spacebook@wantuch.pk` > look at the **Directory** column. It must be exactly `public_html/spacebook`. If it shows something else (for example `spacebook` or `public_html/spacebook/spacebook`), either:
- delete the account and create it again with Directory `public_html/spacebook` (then update the `FTP_USERNAME`/`FTP_PASSWORD` secrets), or
- tell the agent the folder it shows. The agent will then give you the `FTP_DIR` variable value to set.

## 6. Delete the local copy
Delete `D:\SpaceBook\deploy\spacebook_upload.zip`. It still contains the old password. Empty the Recycle Bin afterwards. A new build (`python tools/build_upload_zip.py`) no longer contains `api/config.php`.

## After that, tell the agent
The agent will then run the external checks: zip → 404, no listing, `index.html` → 200, `api/health.php` → `"db":true`. The agent will push the fixed workflow only after your go-ahead, because a push to `main` deploys.
