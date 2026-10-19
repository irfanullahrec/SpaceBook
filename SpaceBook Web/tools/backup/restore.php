<?php
// Restore a dump made by tools/backup/dump.php into a database. Command line only; never deployed.
//   php tools/backup/restore.php --file backup.sql.gz --config /path/restore-config.php [--force]
// The config names the TARGET database (same keys as api/config.php). Without --force the target must have no tables, so a
// restore can never overwrite a live database by accident. To replace the live data, restore into a fresh database first,
// check it, and only then point api/config.php at it (or restore with --force after taking a fresh dump).
// Compatible with PHP 7.4.

if (PHP_SAPI !== 'cli') { http_response_code(404); exit; }
$opt = getopt('', ['file:', 'config:', 'force']);
if (empty($opt['file']) || empty($opt['config'])) { fwrite(STDERR, "usage: php restore.php --file DUMP.sql.gz --config TARGET-CONFIG.php [--force]\n"); exit(2); }
if (!is_file($opt['file']) || !is_file($opt['config'])) { fwrite(STDERR, "file or config not found\n"); exit(2); }
$c = require $opt['config'];
$pdo = new PDO(sprintf('mysql:host=%s;port=%d;dbname=%s;charset=utf8mb4', $c['db_host'], isset($c['db_port']) ? $c['db_port'] : 3306, $c['db_name']),
    $c['db_user'], $c['db_pass'], [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$existing = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
if ($existing && !isset($opt['force'])) { fwrite(STDERR, 'target database ' . $c['db_name'] . ' already has ' . count($existing) . " tables; use --force to replace them\n"); exit(3); }

$gz = gzopen($opt['file'], 'rb');
$stmt = '';
$n = 0;
while (($line = gzgets($gz)) !== false) {
    if ($stmt === '' && (trim($line) === '' || strncmp($line, '--', 2) === 0)) continue;
    $stmt .= $line;
    if (substr(rtrim($line), -1) === ';') {          // dump.php puts a statement's end at a line end; values with ";\n" inside are quoted on one line
        $pdo->exec($stmt);
        $stmt = '';
        $n++;
    }
}
gzclose($gz);
if (trim($stmt) !== '') { fwrite(STDERR, "unfinished statement at the end of the dump: the file is cut short\n"); exit(1); }
echo "restored $n statements into ", $c['db_name'], "\n";
