-- Down for 008: removes the news feed (posts, comments, likes, reports). Nothing else changes. Take a mysqldump first: the posts are not kept anywhere else.
DROP TABLE IF EXISTS feed_reports;
DROP TABLE IF EXISTS feed_comment_likes;
DROP TABLE IF EXISTS feed_post_likes;
DROP TABLE IF EXISTS feed_comments;
DROP TABLE IF EXISTS feed_posts;
