<?php
// Database backup in pure PHP (shared hosts often hide `mysqldump`). Command line only; never deployed (tools/ is excluded).
//   php tools/backup/dump.php --out /home/USER/spacebook_backups [--keep 14] [--config /path/config.php]
// Writes <out>/spacebook-YYYYmmdd-HHMMSS.sql.gz containing CREATE TABLE + INSERT statements for every table, then deletes
// the oldest dumps beyond --keep. The output folder must be OUTSIDE public_html. Restore: tools/backup/restore.php.
// cPanel cron (daily 02:30):  30 2 * * *  /usr/local/bin/php /home/USER/tools/backup/dump.php --out /home/USER/spacebook_backups
// Compatible with PHP 7.4. Read-only on the database.

if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
$opt = getopt('', ['out:', 'keep:', 'config:']);
if (empty($opt['out'])) { fwrite(STDERR, "usage: php dump.php --out DIR [--keep 14] [--config FILE]\n"); exit(2); }
$out = rtrim(str_replace('\\', '/', $opt['out']), '/');
$keep = isset($opt['keep']) ? max(1, (int)$opt['keep']) : 14;
if (stripos($out, 'public_html') !== false) { fwrite(STDERR, "refusing to write backups inside public_html\n"); exit(2); }
$cfgFile = isset($opt['config']) ? $opt['config'] : (getenv('SB_CONFIG') ?: __DIR__ . '/../../api/config.php');
if (!is_file($cfgFile)) { fwrite(STDERR, "config file not found: $cfgFile\n"); exit(2); }
$c = require $cfgFile;
if (!is_dir($out) && !@mkdir($out, 0700, true)) { fwrite(STDERR, "cannot create $out\n"); exit(2); }

$pdo = new PDO(sprintf('mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4', $c['db_host'], isset($c['db_port']) ? $c['db_port'] : 3306, $c['db_name']),
    $c['db_user'], $c['db_pass'], [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
$pdo->exec('SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ');
$pdo->beginTransaction();                       // one consistent snapshot of all (InnoDB) tables
$file = $out . '/spacebook-' . date('Ymd-His') . '.sql.gz';
$tmp = $file . '.part';
$gz = gzopen($tmp, 'wb9');
if (!$gz) { fwrite(STDERR, "cannot write $tmp\n"); exit(1); }
$w = function ($s) use ($gz) { gzwrite($gz, $s); };
$w("-- SpaceBook backup " . gmdate('c') . " database " . $c['db_name'] . "\nSET NAMES utf8mb4;\nSET FOREIGN_KEY_CHECKS=0;\nSET UNIQUE_CHECKS=0;\n\n");
$tables = $pdo->query('SHOW FULL TABLES WHERE Table_type = \'BASE TABLE\'')->fetchAll(PDO::FETCH_COLUMN);
$rows = 0;
foreach ($tables as $t) {
    $create = $pdo->query('SHOW CREATE TABLE `' . str_replace('`', '``', $t) . '`')->fetch(PDO::FETCH_NUM);
    $w("DROP TABLE IF EXISTS `$t`;\n" . $create[1] . ";\n\n");
    $st = $pdo->query('SELECT * FROM `' . str_replace('`', '``', $t) . '`');
    $batch = [];
    $flush = function () use (&$batch, $w, $t) { if ($batch) { $w("INSERT INTO `$t` VALUES\n" . implode(",\n", $batch) . ";\n"); $batch = []; } };
    while ($r = $st->fetch(PDO::FETCH_NUM)) {
        $vals = [];
        foreach ($r as $v) $vals[] = $v === null ? 'NULL' : $pdo->quote((string)$v);
        $batch[] = '(' . implode(',', $vals) . ')';
        $rows++;
        if (count($batch) >= 300) $flush();
    }
    $flush();
    $w("\n");
}
$w("SET FOREIGN_KEY_CHECKS=1;\nSET UNIQUE_CHECKS=1;\n-- end of backup: " . count($tables) . " tables, $rows rows\n");
gzclose($gz);
$pdo->commit();
if (!rename($tmp, $file)) { fwrite(STDERR, "cannot finish $file\n"); exit(1); }
@chmod($file, 0600);
$all = glob($out . '/spacebook-*.sql.gz') ?: [];
sort($all);
foreach (array_slice($all, 0, max(0, count($all) - $keep)) as $old) @unlink($old);
echo basename($file), ' ', count($tables), ' tables, ', $rows, ' rows, ', filesize($file), " bytes, kept ", min(count($all), $keep), "\n";
