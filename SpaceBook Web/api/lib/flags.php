<?php
// Owner switches that both the website and the Android app follow, so the two never run with different settings. Compatible with PHP 7.4.
//
//   syncV2  the offline-safe sync of coins, study plans and Tests Preps (js/core/sync.js, api/v2/sync.php). Default OFF.
//
// The answer is published by api/auth.php?action=me and api/v2/entitlements.php as `flags: {syncV2: bool}`. The website copies it
// to the browser (localStorage sb_sync_server) and the app hands it to its web page; a browser can still override it for testing
// (localStorage sb_sync_v2 = 'on' | 'off').
//
// To switch a flag on for everybody: create api/flags.local.php on the server (it is never in git and never uploaded by the deploy,
// so a push does not undo it):   <?php return ['syncV2' => true];
// or change the default below and push. Tests point SB_FLAGS_FILE at their own file.
// (Bookmarks, notes, reading position and the other user items need no switch: they have no older endpoint to fall back to.)

function sb_flags(): array
{
    $flags = ['syncV2' => false];
    $file = getenv('SB_FLAGS_FILE');
    if ($file === false || $file === '') $file = __DIR__ . '/../flags.local.php';
    if (is_file($file)) {
        $over = @include $file;
        if (is_array($over)) {
            foreach ($flags as $k => $_) if (array_key_exists($k, $over)) $flags[$k] = (bool)$over[$k];
        }
    }
    return $flags;
}
