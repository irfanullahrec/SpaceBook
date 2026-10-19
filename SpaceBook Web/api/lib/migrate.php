<?php
// Schema migrations. Files: api/migrations/NNN_name.sql (up) and NNN_name.down.sql (down, optional).
// The applied version is kept in table schema_version. Compatible with PHP 7.4.
//   sb_migrate_up($pdo)        apply every pending migration (guarded by a DB lock, safe under concurrent requests)
//   sb_migrate_down($pdo, $n)  undo the last $n migrations (never below version 1)
//   sb_migrate_status($pdo)    ['current' => int, 'latest' => int, 'pending' => [files]]

function sb_migrations(): array
{
    $out = [];
    foreach (glob(__DIR__ . '/../migrations/*.sql') ?: [] as $f) {
        $base = basename($f);
        if (preg_match('/^(\d{3})_[a-z0-9_]+\.sql$/', $base, $m)) $out[(int)$m[1]] = $f;
    }
    ksort($out);
    return $out;
}

function sb_schema_version(PDO $pdo): int
{
    $pdo->exec('CREATE TABLE IF NOT EXISTS schema_version (
        version INT UNSIGNED NOT NULL, applied_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (version)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4');
    return (int)$pdo->query('SELECT COALESCE(MAX(version), 0) FROM schema_version')->fetchColumn();
}

function sb_sql_statements(string $sql): array
{
    $clean = preg_replace('/^\s*--.*$/m', '', $sql);
    return array_values(array_filter(array_map('trim', explode(';', $clean)), 'strlen'));
}

function sb_migrate_status(PDO $pdo): array
{
    $cur = sb_schema_version($pdo);
    $all = sb_migrations();
    $pending = [];
    foreach ($all as $v => $f) if ($v > $cur) $pending[] = basename($f);
    return ['current' => $cur, 'latest' => $all ? max(array_keys($all)) : 0, 'pending' => $pending];
}

function sb_migrate_up(PDO $pdo): array
{
    $applied = [];
    if (!sb_migrate_status($pdo)['pending']) return $applied;
    $lock = (int)$pdo->query("SELECT GET_LOCK('spacebook_migrate', 20)")->fetchColumn();
    if ($lock !== 1) throw new RuntimeException('Could not get the migration lock');
    try {
        $cur = sb_schema_version($pdo);                  // re-read: another request may have finished the work
        foreach (sb_migrations() as $v => $f) {
            if ($v <= $cur) continue;
            foreach (sb_sql_statements((string)file_get_contents($f)) as $stmt) $pdo->exec($stmt);   // DDL auto-commits
            $pdo->prepare('INSERT INTO schema_version (version) VALUES (?)')->execute([$v]);
            $applied[] = basename($f);
        }
    } finally {
        $pdo->query("SELECT RELEASE_LOCK('spacebook_migrate')");
    }
    return $applied;
}

function sb_migrate_down(PDO $pdo, int $steps = 1): array
{
    $undone = [];
    $cur = sb_schema_version($pdo);
    $all = sb_migrations();
    for ($i = 0; $i < $steps && $cur > 1; $i++) {
        if (!isset($all[$cur])) throw new RuntimeException("Migration $cur file is missing");
        $down = preg_replace('/\.sql$/', '.down.sql', $all[$cur]);
        if (!is_file($down)) throw new RuntimeException('No down-migration for ' . basename($all[$cur]));
        foreach (sb_sql_statements((string)file_get_contents($down)) as $stmt) $pdo->exec($stmt);
        $pdo->prepare('DELETE FROM schema_version WHERE version = ?')->execute([$cur]);
        $undone[] = basename($all[$cur]);
        $cur = sb_schema_version($pdo);
    }
    return $undone;
}
