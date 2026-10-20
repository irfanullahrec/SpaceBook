<?php
// Administration (Phase 9): the logic behind api/admin.php, kept apart from the page so that tests and the command line can use it.
// Compatible with PHP 7.4. Nothing here is reachable over HTTP by itself (api/lib/.htaccess denies the folder).
//
// Rules:
//  * The role is stored in users.role and can be changed ONLY from the command line (php api/migrate.php make-admin <whatsapp>):
//    no request, however authenticated, can make anyone an administrator.
//  * Every admin page re-reads the role and the status of the signed-in user from the database; the session only says who.
//  * Every change an administrator makes is written to audit_log together with who did it; so is looking at a person's details.
//  * An administrator cannot block themselves or another administrator (that is done on the command line, by the owner).

function sb_admin_h($s): string
{
    return htmlspecialchars((string)$s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

// The signed-in, active administrator of this session, or null.
function sb_admin_user(PDO $pdo): ?array
{
    if (empty($_SESSION['uid'])) return null;
    $st = $pdo->prepare("SELECT id, name, role, status FROM users WHERE id = ? AND status = 'active' AND role = 'admin'");
    $st->execute([(int)$_SESSION['uid']]);
    $u = $st->fetch();
    return $u ? $u : null;
}

function sb_admin_csrf(): string
{
    if (empty($_SESSION['admin_csrf']) || !is_string($_SESSION['admin_csrf'])) $_SESSION['admin_csrf'] = bin2hex(random_bytes(16));
    return $_SESSION['admin_csrf'];
}

function sb_admin_csrf_ok($token): bool
{
    return is_string($token) && !empty($_SESSION['admin_csrf']) && hash_equals($_SESSION['admin_csrf'], $token);
}

// 923001234567 -> 92300*****67 (lists show this; the person's page shows the whole number and is logged)
function sb_admin_mask(string $w): string
{
    $n = strlen($w);
    return $n <= 7 ? str_repeat('*', $n) : substr($w, 0, 5) . str_repeat('*', $n - 7) . substr($w, -2);
}

function sb_admin_counts(PDO $pdo): array
{
    $one = function (string $sql) use ($pdo) { return (int)$pdo->query($sql)->fetchColumn(); };
    $out = [
        'users'        => $one("SELECT COUNT(*) FROM users WHERE status <> 'deleted'"),
        'blocked'      => $one("SELECT COUNT(*) FROM users WHERE status = 'blocked'"),
        'deleted'      => $one("SELECT COUNT(*) FROM users WHERE status = 'deleted'"),
        'admins'       => $one("SELECT COUNT(*) FROM users WHERE role = 'admin' AND status = 'active'"),
        'new_7d'       => $one("SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL 7 DAY AND status <> 'deleted'"),
        'login_24h'    => $one("SELECT COUNT(*) FROM users WHERE last_login_at > NOW() - INTERVAL 1 DAY"),
        'devices_7d'   => $one('SELECT COUNT(*) FROM devices WHERE revoked = 0 AND last_seen > NOW() - INTERVAL 7 DAY'),
        'sync_24h'     => $one('SELECT COUNT(*) FROM sync_events WHERE received_at > NOW() - INTERVAL 1 DAY'),
        'sync_err_24h' => $one('SELECT COUNT(*) FROM sync_errors WHERE created_at > NOW() - INTERVAL 1 DAY'),
        'sync_err_7d'  => $one('SELECT COUNT(*) FROM sync_errors WHERE created_at > NOW() - INTERVAL 7 DAY'),
    ];
    $types = [];
    foreach ($pdo->query("SELECT user_type, COUNT(*) AS n FROM users WHERE status <> 'deleted' GROUP BY user_type") as $r) $types[$r['user_type']] = (int)$r['n'];
    $out['types'] = $types;
    return $out;
}

// Escapes % and _ so that a typed search is a plain substring search.
function sb_admin_like(string $s): string
{
    return '%' . str_replace(['\\', '%', '_'], ['\\\\', '\\%', '\\_'], $s) . '%';
}

// A page of people. $q: part of a name, or the start of a number. $status: '', 'active' or 'blocked'.
function sb_admin_users(PDO $pdo, string $q, string $status, int $page, int $per = 50): array
{
    $q = trim(mb_substr($q, 0, 60));
    $where = ["status <> 'deleted'"];
    $args = [];
    if ($status === 'active' || $status === 'blocked') { $where[] = 'status = ?'; $args[] = $status; }
    if ($q !== '') {
        $digits = preg_replace('/\D+/', '', $q);
        if (strlen($digits) >= 5 && strlen($digits) >= strlen($q) - 4) {
            if (strpos($digits, '00') === 0) $digits = substr($digits, 2);
            if (preg_match('/^0\d/', $digits)) $digits = '92' . substr($digits, 1);
            $where[] = 'whatsapp LIKE ?';
            $args[] = $digits . '%';
        } else {
            $where[] = '(name LIKE ? OR father_name LIKE ?)';
            $args[] = sb_admin_like($q); $args[] = sb_admin_like($q);
        }
    }
    $w = implode(' AND ', $where);
    $st = $pdo->prepare("SELECT COUNT(*) FROM users WHERE $w");
    $st->execute($args);
    $total = (int)$st->fetchColumn();
    $pages = max(1, (int)ceil($total / $per));
    $page = min(max(1, $page), $pages);
    $st = $pdo->prepare("SELECT id, name, father_name, user_type, role, status, whatsapp, created_at, last_login_at FROM users WHERE $w ORDER BY id DESC LIMIT " . (int)$per . ' OFFSET ' . (int)(($page - 1) * $per));
    $st->execute($args);
    return ['rows' => $st->fetchAll(), 'total' => $total, 'pages' => $pages, 'page' => $page];
}

// Everything the person's page shows; null when there is no such active or blocked account.
function sb_admin_user_detail(PDO $pdo, int $id): ?array
{
    $st = $pdo->prepare("SELECT id, name, father_name, user_type, role, status, whatsapp, created_at, last_login_at FROM users WHERE id = ? AND status <> 'deleted'");
    $st->execute([$id]);
    $u = $st->fetch();
    if (!$u) return null;
    $st = $pdo->prepare('SELECT id, name, created_at, last_seen, revoked FROM devices WHERE user_id = ? ORDER BY created_at DESC LIMIT 20');
    $st->execute([$id]);
    $u['devices'] = $st->fetchAll();
    $st = $pdo->prepare('SELECT COALESCE(SUM(coins_earned), 0) FROM activity_progress WHERE user_id = ?');
    $st->execute([$id]);
    $u['coins'] = (int)$st->fetchColumn();
    $st = $pdo->prepare('SELECT action, ip, detail, created_at FROM audit_log WHERE user_id = ? ORDER BY id DESC LIMIT 20');
    $st->execute([$id]);
    $u['audit'] = $st->fetchAll();
    $st = $pdo->prepare('SELECT code, event_id, created_at FROM sync_errors WHERE user_id = ? ORDER BY id DESC LIMIT 20');
    $st->execute([$id]);
    $u['sync_errors'] = $st->fetchAll();
    return $u;
}

// Block or unblock. Returns ['ok' => true] or ['ok' => false, 'error' => text]. Writes the audit row.
function sb_admin_set_status(PDO $pdo, array $admin, int $targetId, string $to, string $reason): array
{
    if ($to !== 'blocked' && $to !== 'active') return ['ok' => false, 'error' => 'Unknown status'];
    if ($targetId === (int)$admin['id']) return ['ok' => false, 'error' => 'You cannot block yourself'];
    $st = $pdo->prepare('SELECT id, role, status FROM users WHERE id = ?');
    $st->execute([$targetId]);
    $t = $st->fetch();
    if (!$t || $t['status'] === 'deleted') return ['ok' => false, 'error' => 'No such account'];
    if ($t['role'] === 'admin') return ['ok' => false, 'error' => 'An administrator is changed from the command line, not here'];
    if ($t['status'] === $to) return ['ok' => true, 'unchanged' => true];
    $reason = trim(preg_replace('/[\x00-\x1f\x7f]+/u', ' ', $reason));
    $pdo->prepare('UPDATE users SET status = ? WHERE id = ?')->execute([$to, $targetId]);
    if ($to === 'blocked') {
        require_once __DIR__ . '/security.php';
        sb_device_revoke_all($pdo, $targetId);                       // sync stops at once; the session cookie stops at the next request (status check)
    }
    sb_audit($pdo, $targetId, $to === 'blocked' ? 'admin_block' : 'admin_unblock', 'by:' . (int)$admin['id'] . ($reason !== '' ? ' ' . mb_substr($reason, 0, 100) : ''));
    return ['ok' => true];
}

// Sync problems: the codes the server rejected, counted, and the latest rows.
function sb_admin_sync(PDO $pdo, int $limit = 100): array
{
    $codes = [];
    foreach ($pdo->query('SELECT code, SUM(created_at > NOW() - INTERVAL 1 DAY) AS d1, COUNT(*) AS d7 FROM sync_errors WHERE created_at > NOW() - INTERVAL 7 DAY GROUP BY code ORDER BY d7 DESC') as $r) {
        $codes[] = ['code' => $r['code'], 'day' => (int)$r['d1'], 'week' => (int)$r['d7']];
    }
    $st = $pdo->prepare('SELECT e.id, e.user_id, e.device_id, e.event_id, e.code, e.created_at, u.name FROM sync_errors e LEFT JOIN users u ON u.id = e.user_id ORDER BY e.id DESC LIMIT ' . (int)$limit);
    $st->execute();
    $devices = $pdo->query('SELECT COUNT(*) AS n, SUM(last_seen < NOW() - INTERVAL 30 DAY) AS idle FROM devices WHERE revoked = 0')->fetch();
    return ['codes' => $codes, 'rows' => $st->fetchAll(), 'devices' => (int)$devices['n'], 'idle' => (int)$devices['idle']];
}

function sb_admin_audit_rows(PDO $pdo, string $action, int $userId, int $limit = 200): array
{
    $where = []; $args = [];
    if ($action !== '') { $where[] = 'a.action = ?'; $args[] = substr($action, 0, 40); }
    if ($userId > 0) { $where[] = 'a.user_id = ?'; $args[] = $userId; }
    $sql = 'SELECT a.id, a.user_id, a.action, a.ip, a.detail, a.created_at, u.name FROM audit_log a LEFT JOIN users u ON u.id = a.user_id'
         . ($where ? ' WHERE ' . implode(' AND ', $where) : '') . ' ORDER BY a.id DESC LIMIT ' . (int)$limit;
    $st = $pdo->prepare($sql);
    $st->execute($args);
    return $st->fetchAll();
}

function sb_admin_audit_actions(PDO $pdo): array
{
    return $pdo->query('SELECT action, COUNT(*) AS n FROM audit_log GROUP BY action ORDER BY n DESC')->fetchAll();
}

// What is deployed: the service worker version, the number of book files, the search index, the schema. Reads the generated files; missing = null.
function sb_admin_content_status(PDO $pdo, string $root): array
{
    require_once __DIR__ . '/migrate.php';
    $read = function (string $rel) use ($root) { $f = $root . '/' . $rel; return is_file($f) ? [(string)file_get_contents($f), filemtime($f)] : null; };
    $out = ['version' => null, 'built' => null, 'lazy_files' => null, 'offline_subjects' => null, 'search_subjects' => null, 'search_source' => null, 'schema' => sb_migrate_status($pdo)];
    if ($sw = $read('content/sw_version.js')) {
        if (preg_match('/"version"\s*:\s*"([^"]+)"/', $sw[0], $m)) $out['version'] = $m[1];
        $out['built'] = gmdate('Y-m-d H:i', $sw[1]) . ' UTC';
    }
    if ($lz = $read('content/lazy_manifest.json')) { $j = json_decode($lz[0], true); $out['lazy_files'] = is_array($j) && isset($j['files']) ? count($j['files']) : null; }
    if ($of = $read('content/offline_map.json')) { $j = json_decode($of[0], true); $out['offline_subjects'] = is_array($j) && isset($j['subjects']) ? count($j['subjects']) : null; }
    if ($sx = $read('content/search/index.json')) { $j = json_decode($sx[0], true); if (is_array($j)) { $out['search_subjects'] = isset($j['subjects']) ? count($j['subjects']) : null; $out['search_source'] = isset($j['source']) ? substr((string)$j['source'], 0, 12) : null; } }
    return $out;
}

// Rejected sync events are kept (code and ids only, never the payload) so that an administrator can see what is going wrong on devices.
// At most 20 rows per request and 200 per user and hour, so a broken client cannot fill the table.
function sb_record_sync_errors(PDO $pdo, int $userId, string $deviceId, array $rejected): void
{
    try {
        require_once __DIR__ . '/security.php';
        $rl = sb_rate_hit($pdo, 'syncerr:u:' . $userId, 200, 3600);
        if (!$rl['ok']) return;
        $ins = $pdo->prepare('INSERT INTO sync_errors (user_id, device_id, event_id, code) VALUES (?, ?, ?, ?)');
        foreach (array_slice($rejected, 0, 20) as $r) {
            $ins->execute([$userId, substr($deviceId, 0, 36), substr(isset($r['eventId']) ? (string)$r['eventId'] : '', 0, 40), substr(isset($r['code']) ? (string)$r['code'] : 'unknown', 0, 40)]);
        }
    } catch (Throwable $e) {
        error_log('SpaceBook sync_errors: ' . $e->getMessage());       // a failure here must never fail the sync
    }
}

// Command line only (php api/migrate.php make-admin|remove-admin <whatsapp>). Returns the user id or 0.
function sb_set_role(PDO $pdo, string $whatsapp, string $role): int
{
    if ($role !== 'admin' && $role !== 'user') return 0;
    $st = $pdo->prepare("SELECT id, status FROM users WHERE whatsapp = ? AND status = 'active'");
    $st->execute([$whatsapp]);
    $u = $st->fetch();
    if (!$u) return 0;
    $pdo->prepare('UPDATE users SET role = ? WHERE id = ?')->execute([$role, $u['id']]);
    require_once __DIR__ . '/security.php';
    sb_audit($pdo, (int)$u['id'], $role === 'admin' ? 'admin_grant' : 'admin_revoke', 'cli');
    return (int)$u['id'];
}
