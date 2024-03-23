#!/usr/bin/pup
# puppet manifest to create a file

file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school1',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet\n',
}
