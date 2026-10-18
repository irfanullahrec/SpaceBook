<?php
// Temporary deployment probe; remove once the live DB works. Prints only yes/no checks
// and an error category, never hosts, user names or raw error messages.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
echo json_encode(['php' => PHP_VERSION, 'pdo_mysql' => extension_loaded('pdo_mysql'),
    'config' => is_file(__DIR__ . '/config.php')]), "\n";
flush();
try {
    $c = require __DIR__ . '/config.php';
    $pdo = new PDO(sprintf('mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4', $c['db_host'], $c['db_port'] ?? 3306, $c['db_name']),
        $c['db_user'], $c['db_pass'], [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_TIMEOUT => 8]);
    echo json_encode(['connect' => true, 'tables' => count($pdo->query('SHOW TABLES')->fetchAll())]), "\n";
} catch (Throwable $e) {
    $m = $e->getMessage();
    echo json_encode(['connect' => false, 'kind' => preg_match('/Access denied/i', $m) ? 'access denied'
        : (preg_match('/Unknown database/i', $m) ? 'unknown database'
        : (preg_match('/driver/i', $m) ? 'no driver'
        : (preg_match('/timed out|refused|getaddrinfo|2002/i', $m) ? 'unreachable' : get_class($e))))]), "\n";
}
