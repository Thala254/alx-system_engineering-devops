# sets up a client SSH configuration file so that we can connect to a server without using a password

exec { 'echo':
  path    => '/usr/bin:/bin:/usr/sbin',
  command => 'echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
}