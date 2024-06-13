# Project: 0x0B. SSH

## Resources

#### Read or watch:

* [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement)
* [What is a (physical) server - video](https://www.youtube.com/watch?v=B1ANfsDyjeA&ab_channel=TechnologyProfession)
* [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
* [SSH Config File](https://www.ssh.com/academy/ssh/config)
* [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
* [How Secure Shell Works](https://www.youtube.com/watch?v=ORcvSkgdA58&ab_channel=Computerphile)
* [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc&ab_channel=TraversyMedia)
## Learning Objectives

### General

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using  <code>#!/usr/bin/env bash</code> instead of <code>/bin/bash</code> 
## Tasks

| Task                                     | File                                                   |
|------------------------------------------|--------------------------------------------------------|
| 0. Use a private key                     | [0-use_a_private_key](./0-use_a_private_key)           |
| 1. Create an SSH key pair                | [1-create_ssh_key_pair](./1-create_ssh_key_pair)       |
| 2. Client configuration file             | [2-ssh_config](./2-ssh_config)                         |
| 3. Let me in!                            | -                                                      |
| 4. Client configuration file (w/ Puppet) | [100-puppet_ssh_config.pp](./100-puppet_ssh_config.pp) |
