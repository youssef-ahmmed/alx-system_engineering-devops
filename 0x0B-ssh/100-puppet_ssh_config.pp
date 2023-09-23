# Configuration file
include stdlib

file_line { 'Turn off password authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_cofig',
  line    => '#    PasswordAuthentication no',
  replace => true,
}

file_line { 'Configure private key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '#   IdentityFile ~/.ssh/school',
  replace => true,
}
