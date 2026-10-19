-- Down for 002: removes only tables created by 002 (devices/tokens, counters, audit trail, sync ledger, catalog).
-- Student data (activity_progress, study_plans, test_prep_*) is not touched. Take a mysqldump first.
DROP TABLE IF EXISTS activity_catalog;
DROP TABLE IF EXISTS sync_events;
DROP TABLE IF EXISTS audit_log;
DROP TABLE IF EXISTS rate_limits;
DROP TABLE IF EXISTS devices;
