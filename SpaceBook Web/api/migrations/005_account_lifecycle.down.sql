-- Down for 005: deleted accounts become blocked ones, then the column and the extra status are removed.
UPDATE users SET status = 'blocked' WHERE status = 'deleted';
ALTER TABLE users DROP COLUMN deleted_at;
ALTER TABLE users MODIFY status ENUM('active','blocked') NOT NULL DEFAULT 'active';
