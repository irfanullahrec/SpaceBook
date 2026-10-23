-- Down for 007: removes the user items (bookmarks, notes, positions, marked words ...). The devices keep their own copies and send them again
-- if the migration is applied once more. Take a mysqldump first.
DROP TABLE IF EXISTS user_items;
DELETE FROM sync_changes WHERE kind = 'item';
