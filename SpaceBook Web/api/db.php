<?php
// Shared PDO connection.
//
// Credentials come from api/config.php (gitignored; on the live site it is written by
// .github/workflows/deploy.yml from GitHub secrets). Tests point SB_CONFIG at another file.
// The schema is versioned: pending migrations (api/migrations) are applied once, under a
// database lock, the first time a request finds the database behind; `php api/migrate.php`
// does the same from the command line. Connections time out fast.

function db_config(): array
{
    $cfgFile = getenv('SB_CONFIG') ?: (__DIR__ . '/config.php');
    if (!is_file($cfgFile)) {
        throw new RuntimeException('api/config.php missing (copy config.sample.php)');
    }
    return require $cfgFile;
}

// A connection with no migrations applied.
function db_connect(): PDO
{
    $c = db_config();
    $dsn = sprintf('mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4',
        $c['db_host'], isset($c['db_port']) ? $c['db_port'] : 3306, $c['db_name']);
    $pdo = new PDO($dsn, $c['db_user'], $c['db_pass'], [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
        PDO::ATTR_TIMEOUT            => 8,
    ]);
    // every time in the database (NOW(), subscription start and expiry) is UTC, whatever the host's own zone is
    $pdo->exec("SET time_zone = '+00:00'");
    return $pdo;
}

function db(): PDO
{
    static $pdo = null;
    if ($pdo) return $pdo;
    require_once __DIR__ . '/lib/migrate.php';
    $c = db_connect();
    sb_migrate_up($c);
    return $pdo = $c;
}
