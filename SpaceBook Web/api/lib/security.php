<?php
// Shared security helpers for the account and sync endpoints. Compatible with PHP 7.4.

function sb_client_ip(): string
{
    return substr(isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '', 0, 45);
}

function sb_uuid4(): string
{
    $b = random_bytes(16);
    $b[6] = chr((ord($b[6]) & 0x0f) | 0x40);
    $b[8] = chr((ord($b[8]) & 0x3f) | 0x80);
    $h = bin2hex($b);
    return substr($h, 0, 8) . '-' . substr($h, 8, 4) . '-' . substr($h, 12, 4) . '-' . substr($h, 16, 4) . '-' . substr($h, 20, 12);
}

// Fixed-window counter. Returns ['ok' => within the limit, 'retry' => seconds until the window resets].
function sb_rate_hit(PDO $pdo, string $bucket, int $limit, int $windowSec): array
{
    $bucket = substr($bucket, 0, 100);
    // hits is assigned before window_start so it still sees the old window
    $pdo->prepare('INSERT INTO rate_limits (bucket, window_start, hits) VALUES (?, NOW(), 1)
                   ON DUPLICATE KEY UPDATE
                     hits         = IF(window_start < NOW() - INTERVAL ? SECOND, 1, hits + 1),
                     window_start = IF(window_start < NOW() - INTERVAL ? SECOND, NOW(), window_start)')
        ->execute([$bucket, $windowSec, $windowSec]);
    $st = $pdo->prepare('SELECT hits, TIMESTAMPDIFF(SECOND, NOW(), window_start + INTERVAL ? SECOND) AS retry
                         FROM rate_limits WHERE bucket = ?');
    $st->execute([$windowSec, $bucket]);
    $r = $st->fetch();
    return ['ok' => (int)$r['hits'] <= $limit, 'retry' => max(1, (int)$r['retry'])];
}

// CSRF defence for requests that arrive with the session cookie: browsers tell us where a request came from.
// A cross-site page cannot forge these headers. Requests with no such headers (curl, old browsers) pass, as
// SameSite=Lax on the cookie still covers them. Requests authenticated by a device token never need this.
function sb_request_is_same_site(): bool
{
    $site = isset($_SERVER['HTTP_SEC_FETCH_SITE']) ? $_SERVER['HTTP_SEC_FETCH_SITE'] : '';
    if ($site !== '' && $site !== 'same-origin' && $site !== 'none') return false;
    // The browser itself says the form came from this site. (A page sent with Referrer-Policy: no-referrer, as the administration pages were, makes
    // the browser put "Origin: null" on its own form posts, which the Origin check below refuses: that locked the administrators out of every form.)
    if ($site === 'same-origin') return true;
    $origin = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : '';
    if ($origin !== '' && $origin !== 'null') {
        $host = strtolower(isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : '');
        $oh = strtolower((string)parse_url($origin, PHP_URL_HOST));
        $op = parse_url($origin, PHP_URL_PORT);
        if ($oh . ($op ? ':' . $op : '') !== $host) return false;     // Host carries the port only when it is not the default
    } elseif ($origin === 'null') {
        return false;
    }
    return true;
}

function sb_audit(PDO $pdo, $userId, string $action, string $detail = ''): void
{
    try {
        $ua = isset($_SERVER['HTTP_USER_AGENT']) ? $_SERVER['HTTP_USER_AGENT'] : '';
        $pdo->prepare('INSERT INTO audit_log (user_id, action, ip, ua_hash, detail) VALUES (?, ?, ?, ?, ?)')
            ->execute([$userId, substr($action, 0, 40), sb_client_ip(), substr(sha1($ua), 0, 16), substr($detail, 0, 190)]);
    } catch (Throwable $e) {
        error_log('SpaceBook audit: ' . $e->getMessage());     // an audit failure must never block the request
    }
}

// ---------- devices (bearer tokens for sync) ----------

// Creates a device and returns ['id' => ..., 'token' => ...]. Only the SHA-256 of the token is stored.
function sb_device_issue(PDO $pdo, int $userId, string $name): array
{
    $id = sb_uuid4();
    $token = bin2hex(random_bytes(32));
    $pdo->prepare('INSERT INTO devices (id, user_id, token_hash, name, last_seen) VALUES (?, ?, ?, ?, NOW())')
        ->execute([$id, $userId, hash('sha256', $token), mb_substr($name, 0, 80)]);
    return ['id' => $id, 'token' => $token];
}

function sb_bearer_token(): string
{
    $h = isset($_SERVER['HTTP_AUTHORIZATION']) ? $_SERVER['HTTP_AUTHORIZATION']
        : (isset($_SERVER['REDIRECT_HTTP_AUTHORIZATION']) ? $_SERVER['REDIRECT_HTTP_AUTHORIZATION'] : '');
    return preg_match('/^Bearer\s+([0-9a-f]{64})$/i', trim($h), $m) ? strtolower($m[1]) : '';
}

// ['device_id' => ..., 'user_id' => ...] for a valid, unrevoked token of an active user; null otherwise.
function sb_device_from_request(PDO $pdo): ?array
{
    $t = sb_bearer_token();
    if ($t === '') return null;
    $st = $pdo->prepare("SELECT d.id, d.user_id, d.last_seen < NOW() - INTERVAL 5 MINUTE AS stale
                         FROM devices d JOIN users u ON u.id = d.user_id
                         WHERE d.token_hash = ? AND d.revoked = 0 AND u.status = 'active'");
    $st->execute([hash('sha256', $t)]);
    $d = $st->fetch();
    if (!$d) return null;
    if ($d['stale'] === null || (int)$d['stale'] === 1) {
        $pdo->prepare('UPDATE devices SET last_seen = NOW() WHERE id = ?')->execute([$d['id']]);
    }
    return ['device_id' => $d['id'], 'user_id' => (int)$d['user_id']];
}

function sb_device_revoke(PDO $pdo, string $deviceId, int $userId): void
{
    $pdo->prepare('UPDATE devices SET revoked = 1 WHERE id = ? AND user_id = ?')->execute([$deviceId, $userId]);
}

function sb_device_revoke_all(PDO $pdo, int $userId): void
{
    $pdo->prepare('UPDATE devices SET revoked = 1 WHERE user_id = ?')->execute([$userId]);
}
