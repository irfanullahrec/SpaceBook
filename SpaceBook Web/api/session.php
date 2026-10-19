<?php
// Shared session cookie setup for every API endpoint (auth.php, progress.php, ...).
// The cookie lives 30 days, so the server-side session file must too: PHP's default
// session.gc_maxlifetime is 24 minutes, and on shared hosting another site's cleanup can
// delete our files from the shared temp folder. We keep sessions in a private folder and
// set the same lifetime on both sides.

const SB_SESSION_SECONDS = 60 * 60 * 24 * 30;

$sbSessionDir = sys_get_temp_dir() . DIRECTORY_SEPARATOR . 'spacebook_sessions';
if (!is_dir($sbSessionDir)) @mkdir($sbSessionDir, 0700, true);
if (is_dir($sbSessionDir) && is_writable($sbSessionDir)) session_save_path($sbSessionDir);
ini_set('session.gc_maxlifetime', (string)SB_SESSION_SECONDS);

session_set_cookie_params([
    'lifetime' => SB_SESSION_SECONDS,
    'path'     => '/',
    'httponly' => true,
    'samesite' => 'Lax',
    'secure'   => !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off',
]);
session_name('spacebook_sid');
session_start();
