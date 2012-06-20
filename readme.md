## Prerequisite

Following software is needed to install stupid-web-nikki.

* Python 2.7
  * pip
  * virtualenv
* PostgreSQL
* Git
* heroku (gem package)

## How to install (to local machine)

Following command list is a step-by-step instruction to install stupid-web-nikki to your local computer.

    $ cd /PATH/TO/INSTALL
    $ git clone git@github.com:mahata/.stupid-web-nikki.git
    $ virtualenv --python=/usr/bin/python2.7 ~/.stupid-web-nikki # Assuming python is installed on /usr/bin/python2.7
    $ source ~/.stupid-web-nikki/bin/activate
    $ cd .stupid-web-nikki
    $ pip install -r  requirements.txt
    $ cp local-add-config.sh.sample local-add-config.sh
    (modify local-add-config.sh: PGSQL_DB, PGSQL_USER, PGSQL_PASS)
    $ source local-add-config.sh
    $ psql PGSQL_DB -U PGSQL_USER
    PGSQL_DB=#
    DROP TABLE IF EXISTS articles;
    CREATE TABLE articles (
      id SERIAL,
      article TEXT,
      created_date INTEGER,
      UNIQUE(created_date)
    );
    
    DROP TABLE IF EXISTS access_log;
    CREATE TABLE access_log (
      id SERIAL,
      path VARCHAR(255),
      ip_address VARCHAR(20),
      user_agent TEXT,
      referer TEXT,
      access_time INTEGER
    );
    CTRL-D
    $ python web.py

After issuing commands above, you can access to the server via http://localhost:5000/.  You can login to the service via http://localhost:5000/login, and the password to login is written on _local-add-config.sh_ (PASSWORD).

## How to install (to heroku)

FIX ME.
