<?php
// Scratch database for the Node end-to-end test.
//   php tests/sync/db.php create <config-file>   (drops and recreates the database, writes the config the API reads via SB_CONFIG)
//   php tests/sync/db.php drop
// Database: SB_TEST_DB_HOST (127.0.0.1), SB_TEST_DB_USER (root), SB_TEST_DB_PASS (empty), name spacebook_test_e2e.
$host = getenv('SB_TEST_DB_HOST') ?: '127.0.0.1';
$user = getenv('SB_TEST_DB_USER') ?: 'root';
$pass = getenv('SB_TEST_DB_PASS') !== false ? getenv('SB_TEST_DB_PASS') : '';
$name = 'spacebook_test_e2e';
$pdo = new PDO("mysql:host=$host;charset=utf8mb4", $user, $pass, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$cmd = isset($argv[1]) ? $argv[1] : '';
if ($cmd === 'create' && isset($argv[2])) {
    $pdo->exec("DROP DATABASE IF EXISTS `$name`");
    $pdo->exec("CREATE DATABASE `$name` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
    file_put_contents($argv[2], '<?php return ' . var_export(['db_host' => $host, 'db_name' => $name, 'db_user' => $user, 'db_pass' => $pass, 'db_port' => 3306, 'health_token' => ''], true) . ';');
    echo "created $name\n";
} elseif ($cmd === 'drop') {
    $pdo->exec("DROP DATABASE IF EXISTS `$name`");
    echo "dropped $name\n";
} else {
    fwrite(STDERR, "usage: php tests/sync/db.php create <config-file> | drop\n");
    exit(2);
}
