-- 007 user items: what a student keeps on one device and expects to find on the other (bookmarks, notes and highlights, where they
-- stopped reading, marked words, best game runs, the chosen class, ticked Board SLOs). One table with a small rule set per kind
-- (api/lib/items.php); the events are item.put / item.del in api/v2/sync.php and the rows come back in the pull (`items`).
-- Additive only: no existing table or row changes. A deleted item stays as a tombstone so a late, older save of it cannot bring it back.
CREATE TABLE IF NOT EXISTS user_items (
  user_id    INT UNSIGNED NOT NULL,
  kind       VARCHAR(8) NOT NULL,
  item_key   VARCHAR(160) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  value_json TEXT NOT NULL,
  at_ms      BIGINT UNSIGNED NOT NULL DEFAULT 0,
  deleted    TINYINT(1) NOT NULL DEFAULT 0,
  rev        INT UNSIGNED NOT NULL DEFAULT 1,
  updated_ms BIGINT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id, kind, item_key),
  KEY idx_items_user_kind (user_id, kind, deleted),
  CONSTRAINT fk_items_user FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
