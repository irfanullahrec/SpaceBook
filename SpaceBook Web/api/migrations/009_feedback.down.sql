-- Down for 009: removes the feedback reports and their pictures. Nothing else changes. Take a mysqldump first: the reports are not kept anywhere else.
DROP TABLE IF EXISTS feedback_images;
DROP TABLE IF EXISTS feedback_reports;
