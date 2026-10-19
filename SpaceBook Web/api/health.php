<?php
// Deployment check.
//   GET api/health.php                -> {"ok":true,"db":true}   (public: nothing but up/down)
//   GET api/health.php?token=SECRET   -> adds PHP version, schema version, tables, error kind
// SECRET is 'health_token' in api/config.php. Without a configured token the detailed report is never shown.

// a fatal error (old PHP, missing extension) would otherwise leave an empty 500 body
$sbDetail = false;
register_shutdown_function(function () use (&$sbDetail) {
    $e = error_get_last();
    if ($e && in_array($e['type'], [E_ERROR, E_PARSE, E_CORE_ERROR, E_COMPILE_ERROR], true)) {
        if (!headers_sent()) http_response_code(500);
        echo json_encode(['ok' => false, 'db' => false] + ($sbDetail
            ? ['php' => PHP_VERSION, 'fatal' => basename($e['file']) . ':' . $e['line'] . ' ' . preg_replace('/\s+/', ' ', substr($e['message'], 0, 160))]
            : []));
    }
});

require __DIR__ . '/db.php';

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

try {
    $cfg = db_config();
    $tok = isset($cfg['health_token']) ? (string)$cfg['health_token'] : '';
    $sbDetail = $tok !== '' && isset($_GET['token']) && hash_equals($tok, (string)$_GET['token']);
} catch (Throwable $e) {
    $sbDetail = false;
}

$out = ['ok' => true, 'db' => false];
try {
    $pdo = db();
    $out['db'] = true;
    if ($sbDetail) {
        require_once __DIR__ . '/lib/migrate.php';
        $out['php'] = PHP_VERSION;
        $out['schema'] = sb_migrate_status($pdo);
        $out['tables'] = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
    }
} catch (Throwable $e) {
    $out['ok'] = false;
    http_response_code(500);
    if ($sbDetail) {
        $msg = $e->getMessage();
        // say which kind of failure without echoing hosts or user names
        $out['php'] = PHP_VERSION;
        $out['error'] = strpos($msg, 'config.php') !== false ? 'config.php missing'
            : (preg_match('/Access denied/i', $msg) ? 'access denied (user, password, or Remote MySQL host not allowed)'
            : (preg_match('/timed out|Connection refused|getaddrinfo|No route|2002/i', $msg) ? 'cannot reach the database server'
            : (preg_match('/Unknown database/i', $msg) ? 'database does not exist'
            : (preg_match('/could not find driver/i', $msg) ? 'PHP pdo_mysql extension missing' : 'database error'))));
    }
    error_log('SpaceBook health: ' . $e->getMessage());
}
echo json_encode($out, JSON_PARTIAL_OUTPUT_ON_ERROR);
