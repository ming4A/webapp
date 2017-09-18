#coding:utf-8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask import flash,redirect,url_for
from form import LoginForm
from ext import db
from dataclass import User
from consts import DB_URI
from werkzeug.security import generate_password_hash as generate_password_hash
app = Flask(__name__)
app.debug = True
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'key'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
toolbar = DebugToolbarExtension(app)
db.init_app(app)
@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()
    user = User("woshikj009","woshio")
    db.session.add(user)
    db.session.commit()
@app.route('/')
def index():
    return render_template('base.html',name = u"陌生人")
@app.route('/login',methods = ['POST','GET'])
def login():
    username = None
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(name = username).first()
        if user is None:
            flash("The user is not exist.")
        if form.password.data != user.pw:
            flash("Wrong Password!")
            form.password.data = ''
        else:
            return redirect(url_for('userindex',id = username))
    return render_template('base.html',name = None,form = form)
@app.route('/user/<id>')
def userindex(id):
    return render_template('base.html',name = id,form = None)
@app.route('/home') 
def homeindex():
    return render_template('home.html')
@app.route('/rigist')
def rigister():
    pass
if __name__ == '__main__':
    app.run(host = 'localhost',port = 4000,debug= app.debug)
