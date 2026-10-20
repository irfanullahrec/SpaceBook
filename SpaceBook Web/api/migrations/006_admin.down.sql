-- Down for 006: removes the sync error record and the role column (every administrator becomes an ordinary user). Take a mysqldump first.
DROP TABLE IF EXISTS sync_errors;
ALTER TABLE users DROP COLUMN role;
