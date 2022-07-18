# 0x09-web_infrastructure_design
## 0x09-web_infrastructure_design directory was created for 0x09. Web infrastructure design group project

### Project information:
This project includes three diagrams representing three diffent web infrastructure designs.
#### Simple web stack
Web infrastructure includes:
* 1 server
* 1 web server (Nginx)
* 1 application server
* 1 application files (your code base)
* 1 database (MySQL)
* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8
#### Distributed web infrastructure
Upgrading from Simple web stack infrastructure by adding:
* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 application files (your code base)
* 1 database (MySQL)
#### Secured and monitored web infrastructure
Upgrading from Distributed web infrastructure by adding:
* 3 firewalls
* 1 SSL certificate to serve www.foobar.com over HTTPS
* 3 monitoring clients (data collector for Sumologic or other monitoring services)

### File description:
| File name | Description |
|-----------|-------------|
| README.md | contains the information about the project |
| 0-simple_web_stack | Link to Simple web stack diagram |
| 1-distributed_web_infrastructure | Link to Distributed web infrastructure diagram |
| 2-secured_and_monitored_web_infrastructure | Link to Secured and monitored web infrastructure |
| web_infrastructure_specifics | Link to explaination documents about each infrastructure |

### Authors:
* Yuan Fang
* James Honey
* Cienna Nguyen