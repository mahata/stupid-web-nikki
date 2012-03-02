#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


DATABASE = "/tmp/sqlite3.db"


app = Flask(__name__)
file = os.getenv("CFG") if os.getenv("CFG") else "app_dev.cfg"
app.config.from_pyfile(file)


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()
    try:
        g.login = session["login"]
    except:
        g.login = False


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, "db"):
        g.db.close()


@app.route("/")
def index():
    template = "index.html"
    return render_template(template)


@app.route("/write", methods=["Get", "POST"])
def write():
    if "POST" == request.method:
        g.db.execute("INSERT INTO articles (article, created_at) VALUES (?, ?)", ["hello", 1])
        g.db.commit()
        cur = g.db.execute('SELECT article FROM articles')
        print cur.fetchall()
        print str(g.db)

    template = "write.html"
    return render_template(template)


@app.route("/login", methods=["GET", "POST"])
def login():
    if "POST" == request.method:
        if "melody" == request.form.get("pass"):
            session["login"] = True
            return redirect(url_for("index"))

    template = "login.html"
    return render_template(template)


@app.route("/logout")
def logout():
    session.pop("login", None)
    return redirect(url_for("index"))


@app.route("/error")
def error():
    return "something is strange."


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
