-- 008 news feed: what students post for each other (a question, a My Stats snapshot, the day's study progress, a study plan), and the likes,
-- comments, shares and reports on it. One post table (a share is a post that points at the original), a comment table (a reply points at its
-- comment), one like table per target so every like has a real foreign key, and a report table that lets a post hide itself from the feed
-- when enough different people report it. Additive only: no existing table or row changes. Text is stored as typed and escaped by the clients.
CREATE TABLE IF NOT EXISTS feed_posts (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id       INT UNSIGNED NOT NULL,
  kind          VARCHAR(12) NOT NULL DEFAULT 'text',
  body          TEXT NOT NULL,
  attach_json   TEXT NULL,
  shared_id     BIGINT UNSIGNED NULL,
  like_count    INT UNSIGNED NOT NULL DEFAULT 0,
  comment_count INT UNSIGNED NOT NULL DEFAULT 0,
  share_count   INT UNSIGNED NOT NULL DEFAULT 0,
  report_count  INT UNSIGNED NOT NULL DEFAULT 0,
  status        ENUM('visible','hidden','removed') NOT NULL DEFAULT 'visible',
  created_at    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_feed_posts_list (status, id),
  KEY idx_feed_posts_user (user_id, id),
  KEY idx_feed_posts_shared (shared_id),
  CONSTRAINT fk_feed_posts_user   FOREIGN KEY (user_id)   REFERENCES users (id) ON DELETE CASCADE,
  CONSTRAINT fk_feed_posts_shared FOREIGN KEY (shared_id) REFERENCES feed_posts (id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS feed_comments (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  post_id       BIGINT UNSIGNED NOT NULL,
  user_id       INT UNSIGNED NOT NULL,
  parent_id     BIGINT UNSIGNED NULL,
  body          VARCHAR(1200) NOT NULL,
  like_count    INT UNSIGNED NOT NULL DEFAULT 0,
  report_count  INT UNSIGNED NOT NULL DEFAULT 0,
  status        ENUM('visible','hidden','removed') NOT NULL DEFAULT 'visible',
  created_at    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  KEY idx_feed_comments_post (post_id, status, id),
  KEY idx_feed_comments_parent (parent_id),
  KEY idx_feed_comments_user (user_id),
  CONSTRAINT fk_feed_comments_post   FOREIGN KEY (post_id)   REFERENCES feed_posts (id) ON DELETE CASCADE,
  CONSTRAINT fk_feed_comments_user   FOREIGN KEY (user_id)   REFERENCES users (id) ON DELETE CASCADE,
  CONSTRAINT fk_feed_comments_parent FOREIGN KEY (parent_id) REFERENCES feed_comments (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS feed_post_likes (
  post_id    BIGINT UNSIGNED NOT NULL,
  user_id    INT UNSIGNED NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (post_id, user_id),
  KEY idx_feed_post_likes_user (user_id),
  CONSTRAINT fk_feed_post_likes_post FOREIGN KEY (post_id) REFERENCES feed_posts (id) ON DELETE CASCADE,
  CONSTRAINT fk_feed_post_likes_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS feed_comment_likes (
  comment_id BIGINT UNSIGNED NOT NULL,
  user_id    INT UNSIGNED NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (comment_id, user_id),
  KEY idx_feed_comment_likes_user (user_id),
  CONSTRAINT fk_feed_comment_likes_comment FOREIGN KEY (comment_id) REFERENCES feed_comments (id) ON DELETE CASCADE,
  CONSTRAINT fk_feed_comment_likes_user    FOREIGN KEY (user_id)    REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS feed_reports (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  target_type CHAR(1) NOT NULL,
  target_id   BIGINT UNSIGNED NOT NULL,
  user_id     INT UNSIGNED NOT NULL,
  reason      VARCHAR(16) NOT NULL,
  note        VARCHAR(200) NOT NULL DEFAULT '',
  created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uq_feed_reports (target_type, target_id, user_id),
  KEY idx_feed_reports_time (created_at),
  CONSTRAINT fk_feed_reports_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
