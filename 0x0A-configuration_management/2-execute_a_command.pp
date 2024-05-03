# Using Puppet to create a manifest that kills a process killmenow.

exec { 'kill_killmenow_process':
    command     => '/usr/bin/pkill killmenow',
    refreshonly => true,
    onlyif      => '/usr/bin/pgrep killmenow',
}
