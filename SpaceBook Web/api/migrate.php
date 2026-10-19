<?php
// Command line only:  php api/migrate.php status | up | down [N] | prune
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
require __DIR__ . '/db.php';
require __DIR__ . '/lib/migrate.php';

$pdo = db_connect();
$cmd = isset($argv[1]) ? $argv[1] : 'status';
switch ($cmd) {
case 'status':
    echo json_encode(sb_migrate_status($pdo)), "\n";
    break;
case 'up':
    echo 'applied: ', json_encode(sb_migrate_up($pdo)), "\n";
    break;
case 'down':
    echo 'undone: ', json_encode(sb_migrate_down($pdo, max(1, (int)(isset($argv[2]) ? $argv[2] : 1)))), "\n";
    break;
case 'prune':   // housekeeping: old login attempts, expired rate-limit counters, old audit rows
    $a = $pdo->exec('DELETE FROM login_attempts WHERE attempted_at < NOW() - INTERVAL 30 DAY');
    $b = $pdo->exec('DELETE FROM rate_limits WHERE window_start < NOW() - INTERVAL 1 DAY');
    $c = $pdo->exec('DELETE FROM audit_log WHERE created_at < NOW() - INTERVAL 365 DAY');
    echo "pruned login_attempts=$a rate_limits=$b audit_log=$c\n";
    break;
case 'purge':   // accounts deleted more than 30 days ago, with all their records
    require __DIR__ . '/lib/account.php';
    echo 'purged accounts: ', sb_purge_deleted($pdo, 30), "\n";
    break;
default:
    fwrite(STDERR, "usage: php api/migrate.php status|up|down [N]|prune|purge\n");
    exit(2);
}
