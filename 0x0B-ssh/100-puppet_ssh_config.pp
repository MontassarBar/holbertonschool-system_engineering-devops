#set up my client SSH configuration file so that I can connect to a server without typing a password

file {'ssh_config'
path => '/etc/ssh/sshd_config',
line => 'HostbasedAuthentication no',
}
file {'ssh config'
path => '/etc/ssh/sshd_config',
line => 'IdentityFile ~/.ssh/school'
}
