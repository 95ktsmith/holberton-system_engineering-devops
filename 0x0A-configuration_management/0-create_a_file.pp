# Creates a file in /tmp
file { 'tmp file':
    path    => '/tmp/holberton',
    content => 'I love Puppet',
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data'
}
