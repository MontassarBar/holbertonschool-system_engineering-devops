#set up my client SSH configuration file so that I can connect to a server without typing a password

file_line {'ssh_config':
ensure   => present,
path     => '/etc/ssh/sshd_config',
line     => 'HostbasedAuthentication no',
multiple => true,
}
file_line {'ssh config':
ensure   => present,
path     => '/etc/ssh/sshd_config',
line     => 'IdentityFile ~/.ssh/school'
multiple => true,
}
