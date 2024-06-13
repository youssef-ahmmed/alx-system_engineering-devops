# Project: 0x08. Networking basics #1

## Resources

#### Read or watch:

* [What is localhost](https://en.wikipedia.org/wiki/Localhost)
* [What is 0.0.0.0](https://en.wikipedia.org/wiki/0.0.0.0)
* [What is the hosts file](https://www.makeuseof.com/tag/modify-manage-hosts-file-linux/)
* [Netcat examples](https://www.thegeekstuff.com/2012/04/nc-command-examples/)
## Learning Objectives

### General

* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is <code>/etc/hosts</code>
* How to display your machine’s active network interfaces
## Tasks

**0. Change your home IP**
  * [0-change_your_home_IP](./0-change_your_home_IP): Bash script that configures an Ubuntu server with the below requirements.
  * Requirements:
    * localhost resolves to 127.0.0.2
    * facebook.com resolves to 8.8.8.8.
    * The checker is running on Docker, so make sure to read [this](http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

**1. Show attached IPs**
  * [1-wildcard](./1-wildcard):Bash script that displays all active IPv4
  IP's on the machine.

**2. Port listening on localhost**
  * [100-port_listening_on_localhost](./100-port_listening_on_localhost): Bash script that
  listens on port `98` on `localhost`.
