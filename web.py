#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pprint
#import sqlite3
import psycopg2
import datetime
import markdown
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


# DATABASE = '/tmp/sqlite3.db'


app = Flask(__name__)
file = os.getenv('CFG') if os.getenv('CFG') else 'app_dev.cfg'
app.config.from_pyfile(file)


def connect_db():
    return psycopg2.connect(database = app.config['PGSQL_DB'],
                            user = app.config['PGSQL_USER'],
                            password = app.config['PGSQL_PASS'],
                            host = app.config['PGSQL_HOST'],
                            port = app.config['PGSQL_PORT'])


@app.template_filter('unicode')
def unicode_filter(s):
    return s.decode('utf-8')


@app.template_filter('date')
def date_filter(s):
    s = str(s)
    return s[0:4] + '/' + s[4:6] + '/' + s[6:8]


@app.before_request
def before_request():
    g.today = datetime.datetime.today()
    g.db = connect_db()
    try:
        g.login = session['login']
    except:
        g.login = False


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def index():
    # cursor = g.db.execute('SELECT article, created_date from articles')
    print app.config['PGSQL_DB']
    print app.config['PGSQL_USER']
    print app.config['PGSQL_PASS']
    print app.config['PGSQL_HOST']
    print app.config['PGSQL_PORT']
    cursor = g.db.cursor()
    cursor.execute('SELECT article, created_date FROM articles')
    return render_template('index.html', var={'articles': cursor.fetchall(), 'title': app.config['TITLE']})


@app.route('/write', methods=['GET', 'POST'])
def write():
    var = {'article': '', 'date': '', 'title': app.config['TITLE']}
    if 'POST' == request.method and session['login']:
        var['date'] = request.form['date']
        try:
            cursor = g.db.cursor()
            cursor.execute('INSERT INTO articles (article, created_date) VALUES (%s, %s)', \
                               [request.form['article'], var['date']])
        except:
            g.db.rollback()
            cursor = g.db.cursor()
            cursor.execute('UPDATE articles SET article = %s WHERE created_date = %s', \
                               [request.form['article'], var['date']])

        g.db.commit()

    else:
        var['date'] = request.args.get('date')

    if ('' == var['date'] or None == var['date']):
        var['date'] = '%4d%02d%02d' % (g.today.year, g.today.month, g.today.day)

    try:
        cursor = g.db.cursor()
        cursor.execute('SELECT article FROM articles WHERE created_date = %s', [var['date']])
        var['article'] = cursor.fetchone()[0]
    except:
        var['article'] = ''

    return render_template('write.html', var=var)


@app.route('/article')
def article():
    cursor = g.db.cursor()
    cursor.execute('SELECT article, created_date FROM articles WHERE created_date = %s', [request.args.get('date')])
    return render_template('article.html', var={'article': markdown.markdown(cursor.fetchone()[0].decode('utf-8')), \
                                                    'title': app.config['TITLE'], \
                                                    'date': request.args.get('date')})


@app.route('/api', methods=['POST'])
def api():
    if session['login']:
        return markdown.markdown(request.form['article'].decode('utf-8'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'POST' == request.method:
        # if 'melody' == request.form['pass']:
        if app.config['PASSWORD'] == request.form['pass']:
            session['login'] = True
            return redirect(url_for('index'))

    return render_template('login.html', var={'title': app.config['TITLE']})


@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
