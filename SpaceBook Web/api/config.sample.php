<?php
// Copy to config.php and fill in. config.php is gitignored and is never put in an upload package.
// Use different passwords locally (XAMPP) and online (cPanel).
return [
    'db_host' => 'localhost',
    'db_name' => 'your_db_name',
    'db_user' => 'your_db_user',
    'db_pass' => 'CHANGE_ME',
    'db_port' => 3306,
    // optional: secret that unlocks the detailed report at api/health.php?token=...
    'health_token' => '',
];
