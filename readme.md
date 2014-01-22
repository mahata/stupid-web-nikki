## Prerequisite

Following software is needed to install stupid-web-nikki.

* VirtualBox 4.2.*
* Vagrant 1.4.*
* Ansible 1.4.*

## How to install (to local machine)

```
git clone git@github.com:mahata/.stupid-web-nikki.git
cd .stupid-web-nikki
vagrant up
```

### How to run the service

```
vagrant ssh
cd swn
python web.py
```

You'll be able to access it via http://localhost:5001/

You'll be able to login via http://localhost:5001/login and default password is "password".

### How to troubleshoot

```
vagrant destroy
vi ~/.ssh/known_host # <- delete a record which starts with 192.168.1.100
vagrant up
```

## How to install (to heroku)

FIX ME.
