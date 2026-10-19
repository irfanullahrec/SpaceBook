-- 004: which device last wrote a study plan. A save from that same device is a plain fast-forward (it already contains
-- its earlier edits, so un-ticking a task must stick); a save from another device on an older revision is merged.
ALTER TABLE study_plans ADD COLUMN last_device CHAR(36) NOT NULL DEFAULT '';
