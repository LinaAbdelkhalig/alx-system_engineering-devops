#!/usr/bin/env bash
# this file manages a ssh config

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "Host *\n  IdentifyFile ~/.ssh/school\n PasswordAuthentication no\n",
}
