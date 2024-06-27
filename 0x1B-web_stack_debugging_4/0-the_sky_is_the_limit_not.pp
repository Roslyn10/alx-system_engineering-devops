#Setting up Nginx to handle multiple requests
exec { 'set_ulimit_and_restart_nginx':
  command => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' /etc/default/nginx; service nginx restart\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
