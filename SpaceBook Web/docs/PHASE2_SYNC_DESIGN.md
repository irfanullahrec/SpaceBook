# Phase 2 design: durable, idempotent synchronisation of user records

Status: **design for owner review, nothing implemented.** Written 2026-10-19 from reading `api/*.php`, `js/sb_rewards.js`, `js/sb_study_plan.js`, `js/test_prep.js`, `js/auth.js`. Server runs PHP 7.4 (`api/` must stay 7.4-compatible: no `match`, no typed properties, no `str_contains`).

## 1. What is wrong today (confirmed in the code)

| ID | Defect | Where |
|---|---|---|
| SYNC-01a | A signed-in step whose request fails (offline) returns `{ok:false}` and is **dropped**: not stored, not retried, no coins. | `sb_rewards.js` `step()`: `else r = {ok:false, earned:0}` |
| SYNC-01b | Any response with an `error` field (also a 500 or 429) turns the user into a **guest** and moves the step to guest data; the next login `sync` replays it, but until then the UI shows guest coins. | `sb_rewards.js` `step()`: `else if (r.error) { user = null; ... }` |
| SYNC-02a | Plan edits made offline are only re-pushed if the plan is **missing** on the server (`!serverIds.has(p.id)`); an edited-offline plan the server already knows is never pushed. | `sb_study_plan.js` `syncWithAccount()` |
| SYNC-02b | `persist()` fires `api('save')` once with no retry and no queue. | `sb_study_plan.js` `persist()` |
| SYNC-02c | Last-writer-wins by **client** clock (`Date.now()`): a device with a fast clock overwrites newer edits; whole plan replaced. Deleted ids from the server remove local plans, so an offline delete can reappear (delete is not queued). | same file, `updatedAt` compare |
| SYNC-03a | Guest test-prep data lives in `sbTP:v1:guest` and is never merged into the account on login. | `test_prep.js:138` |
| SYNC-03b | `push()` is scheduled only after a change, 2.5 s later, once; there is no retry and no `online`/`visibilitychange` trigger. Whole-record LWW (`updated_ms`) can drop one device's answers. | `test_prep.js` `schedulePush`, `api/test_prep.php` `save` |
| SEC-02 | The browser chooses `key`, `title`, `total` (≤ 200) and `step`; the server trusts them. A script can create unlimited activities with 200 steps each = 205 coins per request, 500 items per `sync`. No per-user limit. | `api/progress.php` |
| SEC-05a | Cookie endpoints have no CSRF token (SameSite=Lax only); login throttle is per phone number only (an attacker rotates numbers from one IP); distinct "number already registered"-type messages allow enumeration; no password reset or change; `login_attempts` is never pruned; `db()` runs DDL on a request path (writes `.schema-*` marker into `api/`); `health.php` is public and detailed. | `api/auth.php`, `api/db.php`, `api/health.php` |
| S-01 | Cookie lifetime is 30 days but PHP's `session.gc_maxlifetime` defaults to 24 min, so server sessions may disappear while the cookie lives → silent 401 → guest mode. Not yet confirmed on the live host. | `api/session.php` |
| PRIV-01 | No profile edit, export or delete. | `api/` |
| BAK-01 | No automated backup. | host |

## 2. Principles

1. **The device is the source of truth for what the student did; the server is the source of truth for what it counts as.** Every action becomes an immutable *event* with a client-generated id. Events are stored locally first, then delivered at least once; the server applies each event at most once.
2. **Never drop, never demote.** A failed or slow request leaves events in the outbox. A network/5xx/429 error never changes who the user is. Only an explicit `401` after a refresh attempt asks them to sign in again (and the outbox is kept, not cleared).
3. **Server decides rewards.** The browser sends facts ("step 3 of activity X done"), never coin amounts.
4. **Merge, don't overwrite.** Progress is a set of facts (grow-only); plans merge per field with server time; test-prep answers merge per MCQ.
5. **Old clients keep working.** `api/progress.php`, `study_plans.php`, `test_prep.php` stay until every client is on v2; v2 writes into the same tables where possible so there is nothing to migrate for those.

## 3. Event model

```
event = {
  eventId:  uuid v4 (client),            // idempotency key, UNIQUE per user on the server
  deviceId: uuid v4 (stored on device),
  type:     'step' | 'again' | 'plan.save' | 'plan.delete' | 'tp.answer' | 'tp.session' | 'tp.record',
  payload:  {...},                        // per type, validated server-side, max 64 KB
  clientTs: ms since epoch,               // informational only, never used to order
  schema:   1
}
```

Types and payloads (map 1:1 to today's actions):

| type | payload | server effect |
|---|---|---|
| `step` | `{key, title, total, step}` | add step to `activity_progress` (same rules as today) |
| `again` | `{key}` | practice coin rule (once per day) |
| `plan.save` | `{plan}` (full plan, ≤ 256 KB) | merge into `study_plans` (see 6) |
| `plan.delete` | `{id}` | tombstone (`deleted=1`), wins over older saves |
| `tp.session` | `{session}` | `INSERT IGNORE` into `test_prep_sessions` (already idempotent by `session_id`) |
| `tp.answer` | `{mcqId, attempts, correct, lastTs}` | per-MCQ merge (see 7) |
| `tp.record` | `{days, run, runClearedAt}` | per-key merge |

Server response to a batch: `{ok:true, accepted:[eventId…], rejected:[{eventId, code}], cursor:<server_seq>, coins}`. `accepted` includes events already seen (duplicates are success). `rejected` are permanent (validation) and are removed from the outbox but shown in a dev log; transient problems return HTTP 5xx/429 and the whole batch stays.

## 4. Server (PHP 7.4, PDO)

New files only; old endpoints untouched until deprecation.

- `api/v2/sync.php`: `POST` batch (≤ 500 events, ≤ 1 MB body) and `GET ?since=<seq>` (changes since a cursor: progress rows, plans, test-prep record/sessions, coin total).
- `api/lib/{bootstrap,auth_device,validate,rewards,rate_limit}.php`.
- `api/migrations/NNN_name.sql` (+ `NNN_name.down.sql`), applied by `php api/migrate.php` from CI/CLI only. **`db()` stops running DDL on requests** (it will only check `schema_version`).

New tables:

```sql
devices(id CHAR(36) PK, user_id, token_hash CHAR(64), name, created_at, last_seen, revoked TINYINT)
sync_events(user_id, event_id CHAR(36), device_id, type, server_seq BIGINT AUTO_INCREMENT UNIQUE,
            client_ts BIGINT, received_at, PRIMARY KEY(user_id, event_id))    -- payload not kept after apply (privacy); only the ledger
audit_log(id, user_id, action, ip, ua_hash, created_at)
rate_limits(bucket VARCHAR(80) PK, window_start, count)                       -- login (ip, number), sync (user)
schema_version(version INT)
```

Existing tables get additive columns only (`activity_progress.server_seq`, `study_plans.server_seq/rev`, per-MCQ table below). No existing row is deleted or rewritten; each migration has a down-script and is run only after a fresh `mysqldump` (stored off the web root).

**Auth for sync.** A device token (random 32 bytes, stored hashed) in `Authorization: Bearer`, issued at login/registration with a device id, revocable on logout/"sign out everywhere". Cookie sessions stay for the existing pages; cookie-authenticated **POSTs require a CSRF token** (`X-CSRF` header, token returned by `me`). Token auth needs no CSRF, and a stolen cookie cannot POST without the token.

**Rewards without an activity list.** Keys come from the SVG in the page at runtime (`keyOf` in `sb_trace.js`), so a build-time catalog is not possible without a browser enumerator. Interim, enforceable rules instead of a catalog:
1. v2 accepts only the key shapes the app produces (`cls|subject|u<unit>|trace|count|<hash>|<n>` from `js/sb_trace.js`, and `plan|<planId>|<sessionId>` from `js/sb_study_plan.js`); v1 keeps its looser charset check;
2. an activity has at most **200 steps** (the old server limit). Measured 2026-10-19 on all shipped data: the largest figure has 126 countable items and 49 dashed paths, so the proposed 60 would have rejected real figures;
3. per user and 24 hours (fixed window): at most **600 coins** and **300 new activities** (approved defaults). Over the coin limit progress is still recorded but earns 0; past the activity limit the event is rejected as `activity_limit`. The same limits apply to v1 (`api/progress.php`), which uses the same library (`api/lib/rewards.php`);
4. `sync` rate limit: 60 batches/min/user -> HTTP 429 with `Retry-After`.
A true catalog (`activity_catalog`) is a Phase 6/9 follow-up once a build step can enumerate the figures; the table is created empty and, when filled, becomes authoritative (unknown key → `rejected: unknown_activity`).

**Auth hardening (same phase).** Throttle by IP *and* number *and* a global per-IP ceiling; identical error text for wrong number/wrong password; `password_hash` stays; add `change_password` (needs current password); **reset channel is an owner decision** (see 10); prune `login_attempts` older than 30 days from the migration runner; one session lifetime (set `session.gc_maxlifetime` = cookie lifetime in `session.php`, confirm on host); logout revokes the device token; `health.php` public output becomes `{"ok":true}` only, details behind a `HEALTH_TOKEN` in config.

**Profile.** `GET profile`, `POST profile` (name only; the WhatsApp number changes only through a verified channel), `GET export` (JSON of everything held), `POST delete` (soft delete: status `deleted`, data purged after 30 days by a CLI job; immediately revokes devices).

## 5. Client

New dev-independent modules, loaded before the three feature modules:

- `js/core/store.js`: small IndexedDB wrapper (`outbox`, `progress`, `plans`, `testprep`, `meta`) with a localStorage fallback if IndexedDB is unavailable. Phase 4 reuses the same stores; the **outbox is never evicted**, never cleared on logout (events stay tagged with the user id or `guest`).
- `js/core/sync.js`: `SBSync.emit(type, payload)` writes the event to the outbox **before** anything else, applies it to local state immediately (UI is always local-first), then triggers `flush()`. `flush()` runs on start, on `online`, on `visibilitychange`→visible, after each emit (debounced 1.5 s) and every 60 s while there are events; batches of ≤ 200, exponential back-off 2 s→5 min with jitter, `Retry-After` honoured; removes only `accepted`/`rejected` ids. A pull (`GET since=cursor`) follows every successful flush and on sign-in.
- `sb_rewards.js`: `step()`/`again()` call `emit`; local coin total is computed with the same rules (already true for guests) and **reconciled** with the server's `coins` in each response. The `user = null` demotion is deleted.
- `sb_study_plan.js`: `persist()`→`emit('plan.save')`; delete→`emit('plan.delete')`; `syncWithAccount()` becomes "pull since cursor"; the `!serverIds.has` special case goes.
- `test_prep.js`: answers/sessions emit events; the guest store `sbTP:v1:guest` is offered for merge at sign-in.
- **Guest → account:** on first sign-in with local guest data, show "Add this device's progress to your account?"; **Yes** re-tags the guest events with the user id and flushes (the server applies the same rules, so coins are earned once); **No** keeps them on the device as guest data (not deleted). This replaces the silent merge.

Bounded storage: sessions in the outbox payload are capped at 200 KB (as today); `pushed`/event ids older than 400 sent are compacted.

## 6. Merge rules

- **Progress:** union of steps; `times_completed` = max; coins are computed by the server once per (activity, step) first acceptance, so replays and two devices cannot double-pay.
- **Plans:** server assigns `rev` (increment per accepted save). Client sends `baseRev`; if `baseRev < rev` the server merges: tasks keep `done` if done on either side (grow-only), other fields take the newer `server_received_at`, never the client clock. Deleted tombstone wins over a save with `baseRev <= tombstone rev`. Offline deletes are events and are retried like everything else.
- **Test prep:** per-MCQ rows `(user_id, mcq_id, attempts, correct, last_ts)` merged by max attempts/last_ts; `days` merged per day by max minutes; session ids are unique so replays are no-ops. (Replaces whole-record LWW; the existing `test_prep_records` JSON is imported once into the per-MCQ table by the migration, not deleted.)

## 7. Migration & rollout

1. Merge migrations (additive); take `mysqldump` first and restore-test it once on the local MySQL copy.
2. Deploy v2 endpoints next to v1; no client uses them yet.
3. Ship client modules behind `SB.flags.syncV2` (localStorage override for testing, then on by default).
4. After a release with no v1 traffic (log check), mark v1 deprecated; remove only with owner approval.
5. Backups: nightly cPanel cron `mysqldump | gzip` to a folder outside `public_html`, plus off-site copy (owner chooses), 14-day rotation; one **restore drill** recorded in the progress log.

Rollback: client flag off → v1 paths (kept); server: down-migrations; deploys are atomic release folders (Phase 8) or revert + redeploy.

## 8. Tests (acceptance for the phase)

PHP CLI, against a scratch MySQL database (local XAMPP, never the live DB):
- same batch sent twice → one set of effects, identical `coins`;
- 1,000 events in 2 batches of 500 → all accepted; 501 events → 413/422;
- crafted request with 1,000 distinct keys → coin cap reached, `earned` 0 after the cap; `total` 10,000 → clamped/rejected;
- rate limit → 429 + `Retry-After`; revoked token → 401; wrong CSRF → 403;
- two devices: A and B offline, same activity different steps, then sync in both orders → same final state and coins (order-independent);
- plan edited on A offline, edited on B online → merged result deterministic, delete tombstone behaviour;
- migration up/down on a copy of a populated DB leaves row counts unchanged.

Browser (Playwright, needs ≥ 1.5 GB free RAM): complete steps offline → reload → reconnect → exactly once on the server; kill the network mid-flush; 401 mid-session keeps outbox; guest → account merge prompt both branches.

Gate: zero lost or duplicated events in all scripted scenarios; coins cannot be raised by a crafted request beyond the daily caps; one backup restored.

## 9. Work breakdown (each item = own branch/PR, v1 untouched until step 8)

1. Migration runner + `schema_version` + additive columns/tables (+ down) + CLI test DB harness.
2. `api/lib/*`, devices/token issuing in login/register/logout, CSRF, rate limiter, uniform errors, health split.
3. `api/v2/sync.php` POST (progress events + rewards rules) + PHP tests.
4. `GET since` + plans events + test-prep events + merge rules + tests.
5. `js/core/store.js`, `js/core/sync.js` + Node tests with a fake IndexedDB and fake server.
6. Convert `sb_rewards.js`, then `sb_study_plan.js`, then `test_prep.js` (one commit each, snapshot + smoke after each).
7. Guest merge prompt; profile/export/delete; password change.
8. Backups + restore drill; deprecate v1 (owner approval).

## 10. Decisions needed from the owner

1. **Password reset channel** (no email is collected today; WhatsApp number is the identity): WhatsApp OTP via a provider (cost, provider choice) vs admin-assisted reset in a future admin page.
2. **Coin caps** (proposed 600/day, 300 new activities/day, trace total ≤ 60): acceptable, or different numbers?
3. **Guest data prompt** wording and whether "No" should keep guest data forever or expire it.
4. **Backup destination** off the server (second hosting account, cloud drive, local machine).
5. Confirm the live host's PHP (7.4.33 seen on 2026-10-19) and whether it can be raised to 8.x, which would let the v2 code use modern syntax.
6. Approval to run migrations on the live DB (after a verified dump) — not before the Phase 0 server steps are done.

## 11. As built, steps 3-4 (2026-10-19)

Differences between this design and what was implemented in `api/v2/sync.php` and `api/lib/*`:

- **Pull cursor** is a change log (`sync_changes`: kind + ref per change), not `sync_events.server_seq`. `GET ?since=N` returns the *current* state of the objects named after N (absolute, so replays are harmless); `since=0` returns everything; pages of 2,000 changes with `more`. v1 endpoints (`progress.php`, `study_plans.php`, `test_prep.php`) also write to the change log, so v1 and v2 clients see each other's changes during the transition.
- **Test-prep answers are additive** (`tp.answer {mcqId, track, day, correct, ms, ts}`): attempts, correct and milliseconds are added per event, exactly once thanks to the ledger, so two devices answering the same MCQ both count. This replaces the "max attempts wins" rule written in section 6, which would lose one device's answers. "More attempts wins" is kept only for old-format records (v1 `save` and the one-time import of `test_prep_records`). `last_correct` follows the answer with the newest `ts`, whatever the delivery order. The `all` track is not stored; the pull computes it as the sum of the tracks.
- **Plans** merge by server revision as in section 6; plus tombstones for deletes that arrive before the plan; at most 50 plans (`plan_limit`); plan events up to 512 KB, sessions and runs up to 200 KB. The `rev` is added to plans in the pull.
- **Unfinished test-prep run** (`tp.run`, `tp.run.clear`) is ordered by the device-supplied `savedAt`/`clearedAt` (as the page already did), clamped to at most one day in the future.
- New event types are `plan.save`, `plan.delete`, `tp.answer`, `tp.session`, `tp.run`, `tp.run.clear` (see the header of `api/v2/sync.php`). Migration 003 adds `sync_changes`, `user_sync_state`, `tp_answers`, `tp_days`, `tp_runs` and `study_plans.rev`.
- Still open: the client (outbox, `js/core/*`), and the guest-merge prompt (steps 5-7).
