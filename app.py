from application import app
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, g, abort
from flask import redirect
from flask import session
import short_url
import config
from application import db as d
import json
import sqlite3

DATABASE = app.config['DB_FILE']
app.secret_key = app.config['SECRET_KEY']

@app.route('/sign-up', methods=['GET', 'POST'])
def regisration():
    error = None
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        if len(username) <= 4 or len(password) <= 4:
            error = "Неправильный username или password."
        db = d.get_db()
        select_user = 'select 1 from users where login = ?'
        c = db.cursor()
        c.execute(select_user, (username,))
        if c.fetchone() is not None:
            error = "Пользователь уже существует"
        if error is None:
            sql_user = 'insert into users (login, password) values(?,?)'
            # data = (request.form['username'], request.form['password'])
            data = (username, generate_password_hash(password))
            db.cursor().execute(sql_user, data)
            db.commit()
    return render_template('registration.html', error=error)


@app.route('/')
def index():
    return render_template('templates/url.html')


@app.route('/url', methods=['POST'])
def parse_url():
    if request.method == "POST":
        url = request.form['url']
        short_url_1 = short_url.encode_url(6)
        # f = open('url_base.json', 'a')
        # d = {url:short_url_1}
        # j = json.dumps(d)
        # f.write(j)
        # f.close()
        # short_url.encode_url()
        sql_insertquery = '''insert into urls (
        url
        ) values (?)'''
        datatuple = (url,)
        c = d.get_db()
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
        return render_template('post_url.html', url=url, short=short_url_1)




@app.route('/<path>')
def go_url(path):
    db = d.get_db()
    select_sql = 'select url from urls where short_url = ?'
    data = (path,)
    c = db.cursor()
    r = c.execute(select_sql, data)
    fetch = c.fetchone()
    if fetch is not None:
        url = fetch()[0]
        return redirect(url)
    else:
        return abort(404, 'Not found')


if __name__ == '__main__':
    app.run()
