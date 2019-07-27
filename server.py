from flask import Flask, escape, request, render_template, g, abort, session, redirect, url_for
from flask_login import login_required, LoginManager, login_user, logout_user, current_user
import os
import json
import sqlite3
import uuid



parent_folder = os.path.dirname(os.path.abspath(__file__))
DATABASE = '{}/store.db'.format(parent_folder)

login_manager = LoginManager()
app = Flask(__name__, static_url_path='')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = 'static'
login_manager.init_app(app)


class User:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True
        # return true if user is authenticated, provided credentials

    def is_active(self):
        return True
        # return true if user is activte and authenticated

    def is_anonymous(self):
        return False
        # return true if annon, actual user return false

    def get_id(self):
        return self.id
        # return unicode id for user, and used to load user from user_loader callback

def get_db():
    """
    Get db cursor object to start executing sqlite3 commands
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    """
    Close connection to sqlite3 db
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@login_manager.user_loader
def load_user(admin_id):
    """
    Reload user object from user id stored in the session
    """
    c = get_db().execute(
        "SELECT * from admin where id = (?)", [admin_id])
    admin_row = c.fetchone()
    user = User(
        id=admin_row[0],
        username=admin_row[1],
        password=admin_row[2]
    )
    return user


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        print(username, password)

        c = get_db().execute(
            "SELECT * from admin where username = ? AND password = ?", [username, password])
        admin_row = c.fetchone()
        user = User(
            id=admin_row[0],
            username=admin_row[1],
            password=admin_row[2]
        )
        login_user(user)
        next = request.args.get('next')

        return redirect(next or url_for('admin'))
    return render_template('login.html')


@app.route('/admin')
@login_required
def admin():
    print(current_user, 'current_user')
    return render_template('admin.html', current_user=current_user)

@app.route('/new_item', methods = ['POST'])
@login_required
def new_item():
    name = request.form['itemName']
    price = request.form['itemPrice']
    conn = get_db()
    conn.execute("INSERT INTO item(name, price) VALUES(?,?)", [name, price])
    conn.commit()
    return "Success"
    
@app.route('/all_items')
def all_items():
    items = get_db().execute("SELECT * from item").fetchall()
    return json.dumps(items)

@app.route('/aboutus')
def about_us():
    return render_template("aboutus.html")

@app.route('/delete_item', methods = ['POST'])
@login_required
def delete_item():
    itemId = request.form['itemId']
    conn = get_db()
    conn.execute("DELETE FROM item where id=?", [itemId])
    conn.commit()
    return "Success"
    
if __name__ == '__main__':
    app.run()
