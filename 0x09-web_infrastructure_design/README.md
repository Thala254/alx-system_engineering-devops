# 0x09. Web infrastructure design

## Resources

- [DNS](https://alx-intranet.hbtn.io/concepts/12)
  - [Learn everything about DNS in cartoon](https://howdns.works/)
  - [Types of DNS records](https://phoenixnap.com/kb/dns-record-types)
  - [A](https://support.dnsimple.com/articles/a-record/)
  - [CNAME](https://en.wikipedia.org/wiki/CNAME_record)
  - [MX](https://en.wikipedia.org/wiki/MX_record)
  - [TXT](https://en.wikipedia.org/wiki/TXT_record)
  - [Use DNS to scale with round-robin DNS](https://www.dnsknowledge.com/whatis/round-robin-dns/)
  - [What’s an NS Record?](https://support.dnsimple.com/articles/ns-record/)
  - [What’s an SOA Record?](https://support.dnsimple.com/articles/soa-record/)
  - [ What’s the point in having www in a url?](https://serverfault.com/questions/145777/what-s-the-point-in-having-www-in-a-url)
- [Monitoring](https://alx-intranet.hbtn.io/concepts/13)
- [Web Server](https://alx-intranet.hbtn.io/concepts/17)
  - [Web server -mdn](https://developer.mozilla.org/en-USdocs/Learn/Common_questions/What_is_a_web_server)
  - [Web server -whatis](https://www.techtarget.com/whatisdefinition/Web-server)
  - [Web server -wikipedia](https://en.wikipedia.org/wikiWeb_server)
  - [Containers](https://www.cio.com/article/247005what-are-containers-and-why-do-you-need-them.html)
  - [Virtual machine](https://en.wikipedia.org/wikiVirtual_machine)
- [Network basics](https://alx-intranet.hbtn.io/concepts/33)
  - [What is a protocol](https://www.techtarget.com/searchnetworking/definition/protocol)
  - [What is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)
  - [What is TCP/IP](https://www.techtarget.com/searchnetworking/definition/TCP-IP)
  - [What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
- [Load balancer](https://alx-intranet.hbtn.io/concepts/46)
  - [Load-balancing](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
    - [HAProxy](http://www.haproxy.org/) – A TCP load balancer.
    - [NGINX](https://www.nginx.com/resources/wiki/) – A http load balancer with SSL termination support. ([install Nginx on Linux](https://www.thegeekstuff.com/2011/07/install-nginx-from-source/), [how to Install and Configure Nginx on Ubuntu 20.04](https://phoenixnap.com/kb/how-to-install-nginx-on-ubuntu-20-04))
    - [mod_athena](http://ath.sourceforge.net/mod_athena_doc/html/index.html) – Apache based http load balancer.
    - Varnish – A reverse proxy based load balancer.
    - Balance – Open source TCP load balancer.
    - LVS – Linux virtual server offering layer 4 load balancing
    - [ fundamentals of TCP/IP Protocol](https://www.thegeekstuff.com/2011/11/tcp-ip-fundamentals/)
    - [F5 BIG-IP load balancer](https://www.f5.com/products/ways-to-deploy) (Setup [HTTPS load balance on F5](https://www.thegeekstuff.com/2013/09/f5-https-ssl-load-balance/))
    - CISCO system catalyst
    - Barracuda load balancer
    - Coytepoint load balancer
  - [Load-balancing algorithms](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-ndash-the-algorithms/ta-p/273759)
- [Server](https://alx-intranet.hbtn.io/concepts/67)
  - [What is a server - wikipedia](<https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement>)
  - [What is a server - youtube](https://www.youtube.com/watch?v=B1ANfsDyjeA)
  - [Where are servers hosted (data centers)](https://www.youtube.com/watch?v=iuqXFC_qIvA&t=33s)
- [What is a database](https://www.techtarget.com/searchdatamanagement/definition/database)
- [What’s the difference between a web server and an app server?](https://www.youtube.com/watch?v=S97eKyv2b9M)
- [DNS record types](https://pressable.com/?s=DNS&post_type=knowledgebase)
- [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA714)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)

## Objectives

To be able to:

- Draw a diagram covering the web stack you built with the sysadmin/devops track projects
- Explain what each component is doing
- Explain system redundancy
- Know all the mentioned acronyms: LAMP, SPOF, QPS

## Tasks

### 0.Simple web stack

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a [LAMP stack](https://alx-intranet.hbtn.io/rltoken/YVDX0XsC6XHp0nmezvT9vQ).

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:

- You must use:
  - 1 server
  - 1 web server (Nginx)
  - 1 application server
  - 1 application files (your code base)
  - 1 database (MySQL)
  - 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`
- You must be able to explain some specifics about this infrastructure:
  - What is a server
  - What is the role of the domain name
  - What type of DNS record www is in www.foobar.com
  - What is the role of the web server
  - What is the role of the application server
  - What is the role of the database
  - What is the server using to communicate with the computer of the user requesting the website
- You must be able to explain what the issues are with this infrastructure:
  - SPOF
  - Downtime when maintenance needed (like deploying new code web server needs to be restarted)
  - Cannot scale if too much incoming traffic

**Solution [0-simple_web_stack](0-simple_web_stack)**

![[task0]()](images/task0.jpg)

- A server is generally located in a data center and can be both virtual or physical.

- A server runs an operating system which enables it to run the services that it offers and it communicates over a network using TCP/IP protocol.

- There are two types of servers in the setup:

  - A web server - it's role is to serve static webpages.

  - An application server - it's role is to compute dynamic content and has a database.

- A database stores data for the application.

- The browser first checks if the IP of the domain is available locally, if it isn't available, it looks for the IP in the DNS records with help of the ISP.

- The purpose of the DNS in the diagram is to translate the record of the domain name to an IP address.

- www.foobar.com in this context is an A record since it resolves to an IP address

- The setup has the server has a single point of failure (SPOF) since it doesn't imlement redundancy.

- Therefore, upon deployment of updates and restarting the server, downtime would be experienced since the system wasn't redundant.

- This setup cannot scale as a single server cannot handle too much load alone and hence extra servers and a load balancer should be added to facilitate handling of more load

### 1.Distributed web infrastructure

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.

Requirements:

- You must add:
  - 2 servers
  - 1 web server (Nginx)
  - 1 application server
  - 1 load-balancer (HAproxy)
  - 1 set of application files (your code base)
  - 1 database (MySQL)
- You must be able to explain some specifics about this infrastructure:
  - For every additional element, why you are adding it
  - What distribution algorithm your load balancer is configured with and how it works
  - Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
  - How a database Primary-Replica (Master-Slave) cluster works
  - What is the difference between the Primary node and the Replica node in regard to the application
- You must be able to explain what the issues are with this infrastructure
  - Where are SPOF
  - Security issues (no firewall, no HTTPS)
  - No monitoring

**Solution [1-distributed_web_infrastructure](1-distributed_web_infrastructure)**

![[task1]()](images/task1.jpg)

- A new server containing a web server, application server and same code base has been added to facilitate redundancy.

- A load balancer has been added to distribute the traffic between the two servers and is configured as an active-active setup.

- The MYSQL Master-Replica used replication to keep the daa synchronized.

- The master database node accepts reads/writes while the Replica only accepts reads.

- The load balancer is still a SPOF since it's not redundant.

- There's no firewall on the load balancer nor the servers hence the traffic is unencrypted.

- There's no monitoring in the setup.

### 2.Secured and monitored web infrastructure

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

Requirements:

- You must add:
  - 3 firewalls
  - 1 SSL certificate to serve `www.foobar.com` over HTTPS
  - 3 monitoring clients (data collector for Sumologic or other monitoring services)
- You must be able to explain some specifics about this infrastructure:
  - For every additional element, why you are adding it
  - What are firewalls for
  - Why is the traffic served over HTTPS
  - What monitoring is used for
  - How the monitoring tool is collecting data
  - Explain what to do if you want to monitor your web server QPS
- You must be able to explain what the issues are with this infrastructure:
  - Why terminating SSL at the load balancer level is an issue
  - Why having only one MySQL server capable of accepting writes is an issue
  - Why having servers with all the same components (database, web server and application server) might be a problem

**Solution [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)**

![[task2]()](images/task2.jpg)

- Firewall filters network traffic in and out a machine

- HTTPS is setup to encrypt the network traffic hence intruders cannot intercept the traffic.

- Monitoring is used to check the status of the setup and its setup is composed of a client collecting data and sending it to the monitoring system.

- Terminating SSL at the load balancer level is an issue because the traffic between the load balancer and the web server is unencrypted hence valnurable to intrusion.

- Having servers with all the same components (database, web server,and application server) might be a problem because:

  - Their consumption will not grow the same way between each of them.

  - When there's maintenance performed on a server for a specific component, it will affect the other components on it.

- Load balancer is still a SPOF because it's not redundant.

### 3.Scale up

Readme

- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

Requirements:

- You must add:
  - 1 server
  - 1 load-balancer (HAproxy) configured as cluster with the other one
  - Split components (web server, application server, database) with their own server
- You must be able to explain some specifics about this infrastructure:
  - For every additional element, why you are adding it

**Solution [3-scale_up](3-scale_up)**

![[task3]()](images/Task3.jpg)

- More servers have been added to increase redundancy in the setup. Moreover, each server component works in isolation to further facilitate reliability of the setup.
- An additional load balancer was added to ensure that the load balance stops being a SPOF by increasing its redundancy.
- The load balancer was configured as a cluster to ensure that if one fails, the other takes over. The setup is active-passive.
