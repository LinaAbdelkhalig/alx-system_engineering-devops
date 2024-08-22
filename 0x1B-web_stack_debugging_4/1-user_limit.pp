# enable holberton to login and open files

# increade hard file limit for holberton
exec { 'increase-hard-file-limit':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# increase soft file limit
exec { 'increase-soft-file-limit':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
