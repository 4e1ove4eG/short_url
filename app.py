from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, g
from flask import redirect
from flask import session
import short_url
import json
import sqlite3
DATABASE = 'urls.db'
app = Flask(__name__)

app.secret_key = 'hsmgsg765$|'

def get_db():
    db = getattr(g,'_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/sign-up', methods=['GET', 'POST'])
def regisration():
    error = None
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        if len(username) <= 4 or len(password) <= 4:
            error = "Неправильный username или password."
        db = get_db()
        select_user = 'select 1 from users where login = ?'
        c = db.cursor()
        c.execute(select_user, (username,))
        if c.fetchone() is not None:
            error = "Пользователь уже существует"
        if error is None:
            sql_user = 'insert into users (login, password) values(?,?)'
            #data = (request.form['username'], request.form['password'])
            data = (username, generate_password_hash(password))
            db.cursor().execute(sql_user, data)
            db.commit()
    return render_template('registration.html', error = error)


@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
@app.route('/')
def hello_world():
    return render_template('url.html')


@app.route('/url', methods=['POST'])
def parse_url():
    if request.method == "POST":
        url = request.form['url']
        short_url_1 = short_url.encode_url(6)
        #f = open('url_base.json', 'a')
        #d = {url:short_url_1}
        #j = json.dumps(d)
        #f.write(j)
        #f.close()
        #short_url.encode_url()
        sql_insertquery = '''insert into urls (
        url
        ) values (?)'''
        datatuple = (url,)
        c = get_db()
        c.cursor().execute(sql_insertquery, datatuple)
        c.commit()
        cursor = c.cursor()
        cursor.execute('select max(id) from urls')
        max_id = cursor.fetchone()[0]
        print(max_id)
        short_url_1 = short_url.encode_url(max_id)
        sql_update = 'update urls set short_url = ? where id = ?'
        cursor.execute(sql_update, (short_url_1, max_id))
        c.commit()
        return render_template('post_url.html', url=url, short = short_url_1)



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
        #c.execute(create_sqltable)
        con.commit()
        return '1'
    except Exception as e:
        print(e)
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
        #c.execute(create_sqltable)
        con.commit()
        return '1'
    except Exception as e:
        print(e)



@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            session["login"] = request.form["username"]
            return render_template('login.html', username=request.form['username'])
        else:
            error = 'invalid username password'
    return render_template('login.html', error=error)


def valid_login(username, password):
    sql = 'select * from users where login = ?'
    c = get_db().cursor()
    c.execute(sql,(username,))
    row = c.fetchone()
    if row is not None:
       print(row)
       id,login,password_hash = row
       if check_password_hash(password_hash, password) is True:
           return True
    return False

@app.route('/<path>')
def go_url(path):
    db = get_db()
    select_sql = 'select url from urls where short_url = ?'
    data = (path,)
    c = db.cursor()
    r = c.execute(select_sql, data)
    url = c.fetchone()[0]
    return redirect(url)


if __name__ == '__main__':
    app.run()


