# Stupid Web Nikki

Stupid Web Nikki is a yet another Nikki (日記) system. Nikki (日記) means *DIARY* in Japanese, and this software is for you to write diary and publish it on the web.

## Prerequisite

Following software is needed to install stupid-web-nikki.

* VirtualBox 4.2.*
* Vagrant 1.4.*
* Ansible 1.4.*

## How to install (to local machine)

```
git clone git@github.com:mahata/stupid-web-nikki.git
cd stupid-web-nikki
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

### How to troubleshot

```
vagrant destroy
vi ~/.ssh/known_host # <- delete a record which starts with 192.168.1.100
vagrant up
```

## How to install (to Heroku)

Heroku keeps changing it's service so it depends on Heroku's status. Basically, you need to do following things to run this software on Heroku.

1. Create Heroku account if you don't have one yet (https://www.heroku.com/signup)
2. Create new application on Heroku dashboard (https://dashboard.heroku.com/apps)
3. On the application page, get following add-ons:
    * Heroku Postgres :: *
    * PG Backups
4. Copy `heroku-add-config.py.sample` to `heroku-add-config.py` and modify the file
5. Run `python heroku-add-config.py`
6. Check Git repository path for your application on Heroku (https://dashboard.heroku.com/apps/smart-web-nikki/settings), and run `git remote add heroku git@heroku.com:YOUR_OWN_APP.git`
6. Run `git push heroku master`

Or, it might be better off checking [Heroku official manual](https://devcenter.heroku.com/articles/getting-started-with-python).

## License

Stupid Web Nikki is released under the [MIT License](http://opensource.org/licenses/MIT).
