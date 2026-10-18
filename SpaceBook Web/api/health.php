<?php
// Deployment check: GET api/health.php -> {"ok":true,"db":true,"tables":[...]}.
// Reports whether the database is reachable; never prints credentials.

// a fatal error (old PHP, missing extension) would otherwise leave an empty 500 body
register_shutdown_function(function () {
    $e = error_get_last();
    if ($e && in_array($e['type'], [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR], true)) {
        echo json_encode(['ok' => false, 'db' => false, 'php' => PHP_VERSION,
            'fatal' => basename($e['file']) . ':' . $e['line'] . ' ' . preg_replace('/\s+/', ' ', substr($e['message'], 0, 160))]);
    }
});

require __DIR__ . '/db.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$out = ['ok' => true, 'php' => PHP_VERSION, 'db' => false];
try {
    $pdo = db();
    $out['db'] = true;
    $out['tables'] = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
} catch (Throwable $e) {
    $out['ok'] = false;
    $msg = $e->getMessage();
    // say which kind of failure without echoing hosts or user names
    $out['error'] = strpos($msg, 'config.php') !== false ? 'config.php missing'
        : (preg_match('/Access denied/i', $msg) ? 'access denied (user, password, or Remote MySQL host not allowed)'
        : (preg_match('/timed out|Connection refused|getaddrinfo|No route|2002/i', $msg) ? 'cannot reach the database server'
        : (preg_match('/Unknown database/i', $msg) ? 'database does not exist'
        : (preg_match('/could not find driver/i', $msg) ? 'PHP pdo_mysql extension missing' : 'database error'))));
    http_response_code(500);
}
echo json_encode($out, JSON_PARTIAL_OUTPUT_ON_ERROR);
