-- Down for 010: removes the billing tables (payment requests, subscriptions, admin accounts and audit, notifications, free-usage and dashboard
-- counters) and the two users columns. THIS DELETES MONEY RECORDS: take a mysqldump first. Accounts keep working; every plan reverts to free.
DROP TABLE IF EXISTS usage_stats;
DROP TABLE IF EXISTS activity_days;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS admin_audit;
DROP TABLE IF EXISTS admins;
DROP TABLE IF EXISTS subscription_events;
DROP TABLE IF EXISTS subscription_subjects;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS payment_requests;
DROP TABLE IF EXISTS free_usage;
DROP TABLE IF EXISTS visitors;
UPDATE users SET user_type = 'student' WHERE user_type = 'general';
ALTER TABLE users MODIFY user_type ENUM('school','teacher','student') NOT NULL;
ALTER TABLE users DROP COLUMN signup_platform;
