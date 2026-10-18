<?php
// Router for the local PHP dev server:
//   php -S 127.0.0.1:8790 -t "SpaceBook Web" "SpaceBook Web/tools/dev_router.php"
// The app links cover art as ../Books/... (a sibling of the web folder), which
// resolves to /Books/... over HTTP. Serve those from D:\SpaceBook\Books;
// everything else is handled by the built-in server as usual.

$path = rawurldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));
if (!str_starts_with($path, '/Books/')) return false;

$root = realpath(dirname(__DIR__, 2) . '/Books');
$file = realpath($root . substr($path, strlen('/Books')));
if (!$root || !$file || !str_starts_with($file, $root . DIRECTORY_SEPARATOR) || !is_file($file)) {
    http_response_code(404);
    exit('Not found');
}

$types = ['jpg' => 'image/jpeg', 'jpeg' => 'image/jpeg', 'png' => 'image/png', 'webp' => 'image/webp',
          'gif' => 'image/gif', 'svg' => 'image/svg+xml', 'mp4' => 'video/mp4', 'webm' => 'video/webm',
          'pdf' => 'application/pdf'];
$ext = strtolower(pathinfo($file, PATHINFO_EXTENSION));
header('Content-Type: ' . ($types[$ext] ?? 'application/octet-stream'));
header('Content-Length: ' . filesize($file));
header('Cache-Control: max-age=3600');
readfile($file);
