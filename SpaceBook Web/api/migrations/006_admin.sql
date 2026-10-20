-- 006 Phase 9: administration. A role for the users who may open api/admin.php (set only from the command line:
-- php api/migrate.php make-admin <number>, never over HTTP), and a record of the sync events the server rejected
-- (code and ids only, never the payload) for the administrator's sync view.
ALTER TABLE users ADD COLUMN role ENUM('user','admin') NOT NULL DEFAULT 'user' AFTER user_type;

CREATE TABLE IF NOT EXISTS sync_errors (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id    INT UNSIGNED NOT NULL,
  device_id  CHAR(36) NOT NULL DEFAULT '',
  event_id   VARCHAR(40) NOT NULL DEFAULT '',
  code       VARCHAR(40) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_sync_err_time (created_at),
  KEY idx_sync_err_user (user_id, created_at),
  CONSTRAINT fk_sync_err_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
