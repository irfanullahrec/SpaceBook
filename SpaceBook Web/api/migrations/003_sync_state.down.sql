-- Down for 003: removes the tables and column added by 003 (pull state). Plans, progress and test-prep sessions
-- themselves are untouched; per-MCQ counters and daily minutes recorded only in tp_answers/tp_days are lost,
-- and are rebuilt from test_prep_records for users who never used v2. Take a mysqldump first.
DROP TABLE IF EXISTS tp_runs;
DROP TABLE IF EXISTS tp_days;
DROP TABLE IF EXISTS tp_answers;
DROP TABLE IF EXISTS user_sync_state;
DROP TABLE IF EXISTS sync_changes;
ALTER TABLE study_plans DROP COLUMN rev;
