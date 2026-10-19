-- 005: account deletion. A deleted account is kept (status 'deleted', deleted_at set) for 30 days so an accidental or
-- malicious request can be undone by the owner, then `php api/migrate.php purge` removes the user and, by cascade, all
-- of their records.
ALTER TABLE users MODIFY status ENUM('active','blocked','deleted') NOT NULL DEFAULT 'active';
ALTER TABLE users ADD COLUMN deleted_at TIMESTAMP NULL DEFAULT NULL;
