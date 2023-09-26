# Install Nginx web server (w/ Puppet)

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

exec { 'redirect_me':
  command  => 'sed -i \'/listen 80 default_server;/a \    rewrite ^/redirect_me https://example.com/ permanent;\' /etc/nginx/sites-available/default;',
  provider => 'shell',
}

service { 'running':
  ensure  => running,
  require => Exec['nginx'],
}
