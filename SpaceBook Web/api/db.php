<?php
// Shared PDO connection. Creates the schema on first use so a fresh
// cPanel database works without a manual import.
//
// Credentials come from api/config.php (gitignored; on the live site it is written by
// .github/workflows/deploy.yml from GitHub secrets). The live database is on wantuch.pk
// itself (localhost); connections time out fast and the schema is applied once per
// schema version, not on every request.

function db_config(): array
{
    $cfgFile = __DIR__ . '/config.php';
    if (!is_file($cfgFile)) {
        throw new RuntimeException('api/config.php missing (copy config.sample.php)');
    }
    return require $cfgFile;
}

function db(): PDO
{
    static $pdo = null;
    if ($pdo) return $pdo;

    $c = db_config();
    $dsn = sprintf('mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4',
        $c['db_host'], $c['db_port'] ?? 3306, $c['db_name']);
    $pdo = new PDO($dsn, $c['db_user'], $c['db_pass'], [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
        PDO::ATTR_TIMEOUT            => 8,
    ]);

    $sql = file_get_contents(__DIR__ . '/schema.sql');
    // marker per database + schema version; if the folder is not writable the schema simply runs every time
    $mark = __DIR__ . '/.schema-' . md5($c['db_host'] . '|' . $c['db_name'] . '|' . $sql);
    if (!is_file($mark)) {
        $clean = preg_replace('/^\s*--.*$/m', '', $sql);
        foreach (array_filter(array_map('trim', explode(';', $clean))) as $stmt) {
            $pdo->exec($stmt);
        }
        foreach (glob(__DIR__ . '/.schema-*') ?: [] as $old) @unlink($old);
        @touch($mark);
    }
    return $pdo;
}
