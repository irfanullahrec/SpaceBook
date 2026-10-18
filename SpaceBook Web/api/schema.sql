-- SpaceBook accounts schema (MySQL 5.7+ / MariaDB 10.2+).
-- api/db.php also creates these automatically on first request.

CREATE TABLE IF NOT EXISTS users (
  id             INT UNSIGNED NOT NULL AUTO_INCREMENT,
  name           VARCHAR(100) NOT NULL,
  father_name    VARCHAR(100) NOT NULL,
  user_type      ENUM('school','teacher','student') NOT NULL,
  whatsapp       VARCHAR(20)  NOT NULL,           -- normalised, e.g. 923001234567
  password_hash  VARCHAR(255) NOT NULL,
  status         ENUM('active','blocked') NOT NULL DEFAULT 'active',
  created_at     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  last_login_at  TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_users_whatsapp (whatsapp),
  KEY idx_users_type (user_type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS login_attempts (
  id           INT UNSIGNED NOT NULL AUTO_INCREMENT,
  whatsapp     VARCHAR(20) NOT NULL,
  ip           VARCHAR(45) NOT NULL,
  success      TINYINT(1)  NOT NULL DEFAULT 0,
  attempted_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_attempts_lookup (whatsapp, attempted_at),
  KEY idx_attempts_ip (ip, attempted_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- One row per student per activity (a traced figure, a counting picture …).
-- steps_done holds the finished step numbers ("0,2,3"); coins are awarded by api/progress.php.
CREATE TABLE IF NOT EXISTS activity_progress (
  user_id            INT UNSIGNED NOT NULL,
  activity_key       VARCHAR(190) NOT NULL,
  title              VARCHAR(190) NOT NULL DEFAULT '',
  steps_total        SMALLINT UNSIGNED NOT NULL DEFAULT 1,
  steps_done         TEXT NOT NULL,
  coins_earned       INT UNSIGNED NOT NULL DEFAULT 0,
  times_completed    INT UNSIGNED NOT NULL DEFAULT 0,
  first_completed_at TIMESTAMP NULL DEFAULT NULL,
  last_completed_at  TIMESTAMP NULL DEFAULT NULL,
  updated_at         TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, activity_key),
  KEY idx_progress_user_time (user_id, updated_at),
  CONSTRAINT fk_progress_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Study plans made on the Study Plan page; plan_json is the whole plan (sessions, tasks, progress).
CREATE TABLE IF NOT EXISTS study_plans (
  user_id     INT UNSIGNED NOT NULL,
  plan_id     VARCHAR(40)  NOT NULL,
  plan_json   MEDIUMTEXT   NOT NULL,
  updated_ms  BIGINT UNSIGNED NOT NULL DEFAULT 0,
  deleted     TINYINT(1)   NOT NULL DEFAULT 0,
  updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, plan_id),
  CONSTRAINT fk_plans_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tests Preps: one statistics record per student (answers per MCQ id, daily minutes, the unfinished session).
CREATE TABLE IF NOT EXISTS test_prep_records (
  user_id     INT UNSIGNED NOT NULL,
  record_json MEDIUMTEXT   NOT NULL,
  updated_ms  BIGINT UNSIGNED NOT NULL DEFAULT 0,
  updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id),
  CONSTRAINT fk_tprec_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tests Preps: every finished practice / mock session (the track record); MCQ text is not stored, only ids and answers.
CREATE TABLE IF NOT EXISTS test_prep_sessions (
  user_id      INT UNSIGNED NOT NULL,
  session_id   VARCHAR(40)  NOT NULL,
  track        VARCHAR(40)  NOT NULL,
  mode         VARCHAR(10)  NOT NULL,
  questions    SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  correct      SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  duration_ms  INT UNSIGNED NOT NULL DEFAULT 0,
  started_ms   BIGINT UNSIGNED NOT NULL DEFAULT 0,
  session_json MEDIUMTEXT NOT NULL,
  created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, session_id),
  KEY idx_tpsess_track (user_id, track, started_ms),
  CONSTRAINT fk_tpsess_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
