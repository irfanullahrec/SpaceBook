<?php
// Command line only:  php api/migrate.php status | up | down [N] | prune | purge | make-admin <whatsapp> | remove-admin <whatsapp> | admin-reset <username>
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
case 'prune':   // housekeeping: old login attempts, expired rate-limit counters, old audit rows, old tombstones of deleted saved items
    $a = $pdo->exec('DELETE FROM login_attempts WHERE attempted_at < NOW() - INTERVAL 30 DAY');
    $b = $pdo->exec('DELETE FROM rate_limits WHERE window_start < NOW() - INTERVAL 1 DAY');
    $c = $pdo->exec('DELETE FROM audit_log WHERE created_at < NOW() - INTERVAL 365 DAY');
    $d = $pdo->exec('DELETE FROM sync_errors WHERE created_at < NOW() - INTERVAL 90 DAY');
    $e = $pdo->exec('DELETE FROM user_items WHERE deleted = 1 AND updated_ms < ' . ((time() - 180 * 86400) * 1000));      // tombstones of deleted bookmarks and notes older than half a year
    require_once __DIR__ . '/lib/feedback.php';
    $f = sb_fb_prune($pdo);     // pictures of reports closed 90 days ago, reports closed a year ago
    $g = $pdo->exec('DELETE FROM activity_days WHERE day < UTC_DATE() - INTERVAL 400 DAY');
    $h = $pdo->exec('DELETE FROM usage_stats WHERE day < UTC_DATE() - INTERVAL 400 DAY');
    echo "pruned login_attempts=$a rate_limits=$b audit_log=$c sync_errors=$d user_items_deleted=$e feedback_images={$f['images']} feedback_reports={$f['reports']} activity_days=$g usage_stats=$h
";
    break;
case 'purge':   // accounts deleted more than 30 days ago, with all their records
    require __DIR__ . '/lib/account.php';
    echo 'purged accounts: ', sb_purge_deleted($pdo, 30), "\n";
    break;
case 'make-admin':      // the only way to create an administrator: nothing over HTTP can
case 'remove-admin':
    require __DIR__ . '/lib/admin.php';
    $num = preg_replace('/\D+/', '', isset($argv[2]) ? $argv[2] : '');
    if (preg_match('/^03\d{9}$/', $num)) $num = '92' . substr($num, 1);
    $id = $num === '' ? 0 : sb_set_role($pdo, $num, $cmd === 'make-admin' ? 'admin' : 'user');
    echo $id ? ($cmd === 'make-admin' ? "user #$id is now an administrator\n" : "user #$id is an ordinary user again\n") : "no active account with that number\n";
    exit($id ? 0 : 1);
case 'admin-reset':     // forgot the password of the management page: a new temporary one is printed here once (nothing over HTTP can do this)
    require __DIR__ . '/lib/manage.php';
    $pw = sb_m_reset_password($pdo, isset($argv[2]) ? $argv[2] : '');
    echo $pw === null ? "no such administrator\n" : 'temporary password for ' . $argv[2] . ": $pw\nIt must be changed at the next sign-in.\n";
    exit($pw === null ? 1 : 0);
default:
    fwrite(STDERR, "usage: php api/migrate.php status|up|down [N]|prune|purge|make-admin <whatsapp>|remove-admin <whatsapp>|admin-reset <username>\n");
    exit(2);
}
