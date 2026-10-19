-- 002 Phase 2: devices, rate limits, audit log, sync ledger, activity catalog. Additive only: no existing table or row is touched.

-- One row per signed-in browser/app. The bearer token is random, only its SHA-256 is stored.
CREATE TABLE IF NOT EXISTS devices (
  id          CHAR(36) NOT NULL,
  user_id     INT UNSIGNED NOT NULL,
  token_hash  CHAR(64) NOT NULL,
  name        VARCHAR(80) NOT NULL DEFAULT '',
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_seen   TIMESTAMP NULL DEFAULT NULL,
  revoked     TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (id),
  UNIQUE KEY uq_devices_token (token_hash),
  KEY idx_devices_user (user_id, revoked),
  CONSTRAINT fk_devices_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Fixed-window counters: bucket is e.g. 'reg:ip:1.2.3.4' or 'sync:user:12'.
CREATE TABLE IF NOT EXISTS rate_limits (
  bucket       VARCHAR(100) NOT NULL,
  window_start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  hits         INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (bucket)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS audit_log (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id    INT UNSIGNED NULL DEFAULT NULL,
  action     VARCHAR(40) NOT NULL,
  ip         VARCHAR(45) NOT NULL DEFAULT '',
  ua_hash    CHAR(16) NOT NULL DEFAULT '',
  detail     VARCHAR(190) NOT NULL DEFAULT '',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_audit_user (user_id, created_at),
  KEY idx_audit_time (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Ledger of applied sync events (idempotency). Payloads are not kept after they are applied.
CREATE TABLE IF NOT EXISTS sync_events (
  user_id     INT UNSIGNED NOT NULL,
  event_id    CHAR(36) NOT NULL,
  server_seq  BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  device_id   CHAR(36) NOT NULL DEFAULT '',
  type        VARCHAR(20) NOT NULL,
  client_ts   BIGINT NOT NULL DEFAULT 0,
  received_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, event_id),
  UNIQUE KEY uq_sync_seq (server_seq),
  KEY idx_sync_user_seq (user_id, server_seq)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Authoritative list of rewardable activities once a build step can enumerate them (empty = pattern rules apply).
CREATE TABLE IF NOT EXISTS activity_catalog (
  activity_key   VARCHAR(190) NOT NULL,
  title          VARCHAR(190) NOT NULL DEFAULT '',
  steps_total    SMALLINT UNSIGNED NOT NULL DEFAULT 1,
  coins_step     TINYINT UNSIGNED NOT NULL DEFAULT 1,
  coins_complete TINYINT UNSIGNED NOT NULL DEFAULT 5,
  PRIMARY KEY (activity_key)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
