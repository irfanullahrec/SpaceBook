<?php
// Helper for tests/access/browser.js (command line only): a throwaway database for the real-browser test of the plans flow.
//   php tests/access/db.php init <config file>            drop + create spacebook_test_access, write the config file, apply the migrations
//   php tests/access/db.php approve <config file> <id>    approve payment <id> as the seeded administrator (what the management page does)
//   php tests/access/db.php reject <config file> <id> <reason>
//   php tests/access/db.php suspend|restore <config file> <subscription id>
//   php tests/access/db.php json <config file> <SQL>      print the rows of a SELECT as JSON
//   php tests/access/db.php drop <config file>
if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
$api = realpath(__DIR__ . '/../../api');
$cmd = $argv[1] ?? ''; $cfgFile = $argv[2] ?? '';
$name = 'spacebook_test_access';
$host = getenv('SB_TEST_DB_HOST') ?: '127.0.0.1'; $user = getenv('SB_TEST_DB_USER') ?: 'root'; $pass = getenv('SB_TEST_DB_PASS') !== false ? getenv('SB_TEST_DB_PASS') : '';
if ($cmd === 'init') {
    $p = new PDO("mysql:host=$host;charset=utf8mb4", $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
    $p->exec("DROP DATABASE IF EXISTS `$name`");
    $p->exec("CREATE DATABASE `$name` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
    file_put_contents($cfgFile, '<?php return ' . var_export(['db_host' => $host, 'db_name' => $name, 'db_user' => $user, 'db_pass' => $pass, 'db_port' => 3306, 'health_token' => 't'], true) . ';');
    putenv('SB_CONFIG=' . $cfgFile);
    require $api . '/db.php';
    db();
    echo "ready\n";
    exit(0);
}
putenv('SB_CONFIG=' . $cfgFile);
require $api . '/db.php';
require $api . '/lib/billing.php';
$pdo = db();
$adm = $pdo->query("SELECT id, username FROM admins ORDER BY id LIMIT 1")->fetch();
switch ($cmd) {
case 'approve': echo json_encode(sb_payment_review($pdo, $adm, (int)$argv[3], 'approve', '')), "\n"; break;
case 'reject': echo json_encode(sb_payment_review($pdo, $adm, (int)$argv[3], 'reject', $argv[4] ?? 'not found')), "\n"; break;
case 'suspend': echo json_encode(sb_sub_suspend($pdo, $adm, (int)$argv[3], 'browser test')), "\n"; break;
case 'restore': echo json_encode(sb_sub_restore($pdo, $adm, (int)$argv[3], 'browser test')), "\n"; break;
case 'json': echo json_encode($pdo->query($argv[3])->fetchAll()), "\n"; break;
case 'drop': $pdo->exec('SELECT 1'); (new PDO("mysql:host=$host;charset=utf8mb4", $user, $pass))->exec("DROP DATABASE IF EXISTS `$name`"); echo "dropped\n"; break;
default: fwrite(STDERR, "unknown command\n"); exit(2);
}
