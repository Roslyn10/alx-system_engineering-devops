# Uses Puppet to install flask from pip3


package { 'python3-pip':
    ensure  => installed,
}


exec { 'flask':
      command => '/usr/bin/pip3 install Flask==2.2.0',
      creates => '/usr/local/lib/python3.*/dist-packages/Flask-2.1.0.dist-info',
      require => Package['python3-pip'],
}
