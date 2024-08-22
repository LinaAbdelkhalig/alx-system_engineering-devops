# increase the amount of traffic on nginx server

# increase the ulimit of the default file
exec { 'fix--for-nginx':
  # modify the ulimit val
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # specify the path for the command
  path    => '/usr/local/bin/:/bin/',
}

# restart nginx
exec { 'nginx-restart':
  # command to restart
  command => '/etc/init.d/nginx restart',
  # specify the path for the command
  path    => '/etc/init.d/',
}
