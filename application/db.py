import sqlite3
from application import app
from flask import g



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DB_FILE'])
    return db


@app.route('/db')
def db():
    try:
        con = get_db()
        create_sqltable = '''create table if not exists urls (
        id integer PRIMARY key, 
        url text,
        short_url text
        )'''
        c = con.cursor()
        select_sql = '''select * from urls'''
        c.execute(select_sql)
        rows = c.fetchall()
        for row in rows:
            print(row)
        # c.execute(create_sqltable)
        con.commit()
        return '1'
    except Exception as e:
        print(e)


@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/db-users')
def db_users():
    try:
        con = get_db()
        create_sqltable = '''create table if not exists users (
        id integer PRIMARY key, 
        login text,
        password text
        )'''
        c = con.cursor()
        c.execute(create_sqltable)
        con.commit()
        select_sql = '''select * from users'''
        c.execute(select_sql)
        rows = c.fetchall()
        for row in rows:
            print(row)
        # c.execute(create_sqltable)
        con.commit()
        return '1'
    except Exception as e:
        print(e)
