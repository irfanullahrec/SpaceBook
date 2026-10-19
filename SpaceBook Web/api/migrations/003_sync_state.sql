-- 003 Phase 2 step 4: pullable state. Adds tables and one column; no existing row is changed or removed.

-- Change log: one row each time something a device can pull changes (kind: act, plan, tpq, tpd, tps, tpr).
-- GET api/v2/sync.php?since=<seq> returns the current state of the objects named after that seq.
CREATE TABLE IF NOT EXISTS sync_changes (
  seq     BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id INT UNSIGNED NOT NULL,
  kind    VARCHAR(8) NOT NULL,
  ref     VARCHAR(190) NOT NULL,
  PRIMARY KEY (seq),
  KEY idx_changes_user_seq (user_id, seq)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS user_sync_state (
  user_id         INT UNSIGNED NOT NULL,
  legacy_imported TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tests Preps, per MCQ: attempts, correct answers, time of the last answer, was it right, total milliseconds.
CREATE TABLE IF NOT EXISTS tp_answers (
  user_id      INT UNSIGNED NOT NULL,
  mcq_id       VARCHAR(40) NOT NULL,
  attempts     INT UNSIGNED NOT NULL DEFAULT 0,
  correct      INT UNSIGNED NOT NULL DEFAULT 0,
  last_ts      BIGINT UNSIGNED NOT NULL DEFAULT 0,
  last_correct TINYINT(1) NOT NULL DEFAULT 0,
  total_ms     BIGINT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id, mcq_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tests Preps, per track and day: milliseconds practised, answers given, correct answers.
CREATE TABLE IF NOT EXISTS tp_days (
  user_id  INT UNSIGNED NOT NULL,
  track    VARCHAR(40) NOT NULL,
  day      CHAR(10) NOT NULL,
  ms       BIGINT UNSIGNED NOT NULL DEFAULT 0,
  answered INT UNSIGNED NOT NULL DEFAULT 0,
  correct  INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id, track, day)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- The unfinished session: the copy saved last wins unless it was cleared later.
CREATE TABLE IF NOT EXISTS tp_runs (
  user_id    INT UNSIGNED NOT NULL,
  run_json   MEDIUMTEXT NOT NULL,
  saved_ms   BIGINT UNSIGNED NOT NULL DEFAULT 0,
  cleared_ms BIGINT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Study plans get a revision number that the server increments on every accepted change.
ALTER TABLE study_plans ADD COLUMN rev INT UNSIGNED NOT NULL DEFAULT 0;
