-- 009 feedback: suggestions, bug reports, textbook errors and wrong answers / meanings that students send from the website and the app, with an
-- optional picture. A report may come from a student who is not signed in (user_id stays NULL); client_id is made on the device so that a retry after a
-- lost connection never creates a second report. The picture lives in its own table (a JPEG the server re-encoded, so it carries no location data), is
-- read only through the administration page and is deleted with the report. Additive only: no existing table or row changes.
CREATE TABLE IF NOT EXISTS feedback_reports (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  client_id   CHAR(36) NOT NULL,
  user_id     INT UNSIGNED NULL,
  platform    VARCHAR(8) NOT NULL DEFAULT 'web',
  kind        VARCHAR(12) NOT NULL,
  message     TEXT NOT NULL,
  context_json TEXT NULL,
  has_image   TINYINT(1) NOT NULL DEFAULT 0,
  status      ENUM('new','seen','fixed','wontfix','duplicate') NOT NULL DEFAULT 'new',
  admin_note  VARCHAR(500) NULL,
  handled_by  INT UNSIGNED NULL,
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_feedback_client (client_id),
  KEY idx_feedback_list (status, id),
  KEY idx_feedback_kind (kind, id),
  KEY idx_feedback_user (user_id),
  CONSTRAINT fk_feedback_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS feedback_images (
  report_id  BIGINT UNSIGNED NOT NULL,
  mime       VARCHAR(20) NOT NULL,
  bytes      INT UNSIGNED NOT NULL,
  sha256     CHAR(64) NOT NULL,
  data       MEDIUMBLOB NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (report_id),
  CONSTRAINT fk_feedback_image_report FOREIGN KEY (report_id) REFERENCES feedback_reports (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
