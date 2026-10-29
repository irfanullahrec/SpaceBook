-- 010 billing: free limits, plans, Easypaisa payment requests, subscriptions, the separate administrator account, the audit trail,
-- notifications and the usage numbers of the management dashboard. One database for the website and the Android app.
-- Additive, except two columns of users: user_type no longer has to be chosen (new accounts are 'general'), and signup_platform says
-- where an account was made. All times are UTC (api/db.php sets the session time zone).

ALTER TABLE users MODIFY user_type ENUM('school','teacher','student','general') NOT NULL DEFAULT 'general';
ALTER TABLE users ADD COLUMN signup_platform ENUM('web','app') NOT NULL DEFAULT 'web';

-- Someone using SpaceBook on one browser or one phone, signed in or not. The id is random and kept by the client; only used to count.
CREATE TABLE IF NOT EXISTS visitors (
  id          CHAR(32) NOT NULL,
  platform    ENUM('web','app') NOT NULL DEFAULT 'web',
  user_id     INT UNSIGNED NULL DEFAULT NULL,
  is_bot      TINYINT(1) NOT NULL DEFAULT 0,
  ip_hash     CHAR(16) NOT NULL DEFAULT '',
  first_seen  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_visitors_user (user_id),
  KEY idx_visitors_seen (last_seen),
  CONSTRAINT fk_visitors_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- The free allowance: one row per distinct question or paper used. owner_key is 'u:<user id>' or 'v:<visitor id>'; a signed-in person
-- writes to both, so signing out, registering again or using the other platform does not give a new allowance.
CREATE TABLE IF NOT EXISTS free_usage (
  owner_key  VARCHAR(40) NOT NULL,
  metric     VARCHAR(12) NOT NULL,
  item_key   VARCHAR(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (owner_key, metric, item_key),
  KEY idx_free_usage_metric (metric, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- One row per submitted Easypaisa payment. user_id has no foreign key on purpose: payment records outlive a deleted account.
CREATE TABLE IF NOT EXISTS payment_requests (
  id               INT UNSIGNED NOT NULL AUTO_INCREMENT,
  ref              CHAR(10) NOT NULL,
  user_id          INT UNSIGNED NOT NULL,
  contact_name     VARCHAR(100) NOT NULL DEFAULT '',
  contact_whatsapp VARCHAR(20) NOT NULL DEFAULT '',
  plan_type        ENUM('student','teacher','prep') NOT NULL,
  class_id         VARCHAR(16) NULL DEFAULT NULL,
  subjects_json    TEXT NULL,
  scope_key        CHAR(40) NOT NULL,
  amount_pkr       INT UNSIGNED NOT NULL,
  duration_months  TINYINT UNSIGNED NOT NULL DEFAULT 1,
  method           VARCHAR(20) NOT NULL DEFAULT 'easypaisa',
  trx_id           VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  trx_norm         VARCHAR(40) NOT NULL,
  active_trx       VARCHAR(40) NULL DEFAULT NULL,
  paid_on          DATE NULL DEFAULT NULL,
  idem_key         CHAR(32) NOT NULL,
  platform         ENUM('web','app') NOT NULL DEFAULT 'web',
  status           ENUM('pending','approved','rejected') NOT NULL DEFAULT 'pending',
  submitted_at     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  reviewed_by      INT UNSIGNED NULL DEFAULT NULL,
  reviewed_by_name VARCHAR(40) NOT NULL DEFAULT '',
  reviewed_at      DATETIME NULL DEFAULT NULL,
  review_note      VARCHAR(300) NOT NULL DEFAULT '',
  subscription_id  INT UNSIGNED NULL DEFAULT NULL,
  activated_at     DATETIME NULL DEFAULT NULL,
  expires_at       DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_pay_ref (ref),
  UNIQUE KEY uq_pay_idem (user_id, idem_key),
  UNIQUE KEY uq_pay_active_trx (active_trx),
  KEY idx_pay_user (user_id, id),
  KEY idx_pay_status (status, submitted_at),
  KEY idx_pay_trx (trx_norm),
  KEY idx_pay_reviewed (reviewed_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS subscriptions (
  id             INT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id        INT UNSIGNED NOT NULL,
  plan_type      ENUM('student','teacher','prep') NOT NULL,
  class_id       VARCHAR(16) NULL DEFAULT NULL,
  scope_key      CHAR(40) NOT NULL,
  status         ENUM('active','suspended') NOT NULL DEFAULT 'active',
  starts_at      DATETIME NOT NULL,
  expires_at     DATETIME NOT NULL,
  source         ENUM('payment','grant') NOT NULL DEFAULT 'payment',
  suspended_at   DATETIME NULL DEFAULT NULL,
  suspend_reason VARCHAR(300) NOT NULL DEFAULT '',
  created_at     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_sub_user (user_id, status, expires_at),
  KEY idx_sub_scope (user_id, scope_key),
  KEY idx_sub_expires (expires_at),
  CONSTRAINT fk_sub_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS subscription_subjects (
  subscription_id INT UNSIGNED NOT NULL,
  class_id        VARCHAR(16) NOT NULL,
  subject_id      VARCHAR(40) NOT NULL,
  PRIMARY KEY (subscription_id, subject_id),
  CONSTRAINT fk_subsub_sub FOREIGN KEY (subscription_id) REFERENCES subscriptions (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- The history of one subscription: every activation, renewal, extension, suspension and restoration, with who and why.
CREATE TABLE IF NOT EXISTS subscription_events (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  subscription_id INT UNSIGNED NOT NULL,
  event           ENUM('activated','renewed','extended','set_expiry','suspended','restored','granted') NOT NULL,
  payment_id      INT UNSIGNED NULL DEFAULT NULL,
  admin_id        INT UNSIGNED NULL DEFAULT NULL,
  admin_name      VARCHAR(40) NOT NULL DEFAULT '',
  old_expires_at  DATETIME NULL DEFAULT NULL,
  new_expires_at  DATETIME NULL DEFAULT NULL,
  reason          VARCHAR(300) NOT NULL DEFAULT '',
  created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_subev_sub (subscription_id, id),
  CONSTRAINT fk_subev_sub FOREIGN KEY (subscription_id) REFERENCES subscriptions (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- The separate administrator accounts of the management page. Not users: nothing on the public site can sign in as one.
CREATE TABLE IF NOT EXISTS admins (
  id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
  username            VARCHAR(40) NOT NULL,
  password_hash       VARCHAR(255) NOT NULL,
  must_change_password TINYINT(1) NOT NULL DEFAULT 1,
  status              ENUM('active','disabled') NOT NULL DEFAULT 'active',
  failed_logins       SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  locked_until        DATETIME NULL DEFAULT NULL,
  last_login_at       DATETIME NULL DEFAULT NULL,
  password_changed_at DATETIME NULL DEFAULT NULL,
  created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_admins_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Who did what, when, to whom, and what changed. Written in the same transaction as the change.
CREATE TABLE IF NOT EXISTS admin_audit (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  admin_id    INT UNSIGNED NULL DEFAULT NULL,
  admin_name  VARCHAR(40) NOT NULL DEFAULT '',
  action      VARCHAR(40) NOT NULL,
  target_type VARCHAR(20) NOT NULL DEFAULT '',
  target_id   VARCHAR(40) NOT NULL DEFAULT '',
  reason      VARCHAR(300) NOT NULL DEFAULT '',
  detail_json TEXT NULL,
  ip          VARCHAR(45) NOT NULL DEFAULT '',
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_admaudit_time (created_at),
  KEY idx_admaudit_target (target_type, target_id),
  KEY idx_admaudit_admin (admin_id, id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- What the student is told: a payment was received, approved or rejected, a plan was extended, suspended or restored.
CREATE TABLE IF NOT EXISTS notifications (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id         INT UNSIGNED NOT NULL,
  kind            VARCHAR(20) NOT NULL,
  title           VARCHAR(120) NOT NULL,
  body            VARCHAR(400) NOT NULL DEFAULT '',
  payment_id      INT UNSIGNED NULL DEFAULT NULL,
  subscription_id INT UNSIGNED NULL DEFAULT NULL,
  read_at         DATETIME NULL DEFAULT NULL,
  created_at      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_notif_user (user_id, id),
  CONSTRAINT fk_notif_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dashboard numbers. activity_days: one row per person (u:<id> or v:<id>) per day per platform, hits = actions that day.
-- usage_stats: popular classes, subjects and modules, and how often a free limit or a purchase prompt was met. No personal data.
CREATE TABLE IF NOT EXISTS activity_days (
  day       DATE NOT NULL,
  owner_key VARCHAR(40) NOT NULL,
  platform  ENUM('web','app') NOT NULL DEFAULT 'web',
  hits      INT UNSIGNED NOT NULL DEFAULT 1,
  PRIMARY KEY (day, owner_key, platform),
  KEY idx_actdays_owner (owner_key, day)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS usage_stats (
  day   DATE NOT NULL,
  kind  VARCHAR(12) NOT NULL,
  skey  VARCHAR(60) NOT NULL,
  hits  INT UNSIGNED NOT NULL DEFAULT 1,
  PRIMARY KEY (day, kind, skey)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- The first administrator. Only a bcrypt hash is stored (the plain password is not in this repository). The account must choose a
-- new password at its first sign-in. INSERT IGNORE: running this again never resets a password that was changed.
INSERT IGNORE INTO admins (username, password_hash, must_change_password) VALUES ('IrfanUllah123', '$2y$12$NGv8ELbzdG5P2UCdK3ZCNusIUfxvHnIlaHeGIpvTLYD8qo6WbxyiS', 1);
