from application import app
from flask import request, session
from werkzeug import check_password_hash
from application import db as d
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
    c = d.get_db().cursor()
    c.execute(sql, (username,))
    row = c.fetchone()
    if row is not None:
        print(row)
        id, login, password_hash = row
        if check_password_hash(password_hash, password) is True:
            return True
    return False